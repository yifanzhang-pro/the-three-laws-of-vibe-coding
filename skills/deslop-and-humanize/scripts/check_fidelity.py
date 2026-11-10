#!/usr/bin/env python3
"""List the checkable facts that differ between two versions of a text.

    check_fidelity.py BEFORE AFTER
    check_fidelity.py --git [--rev REV] PATH [PATH ...]

The second form compares each PATH at REV (default HEAD) with the working tree.

The script extracts numbers, citation keys, labels, cross-references, math,
code, link targets, and capitalized names from both versions and prints the
items whose counts differ. It also prints qualifier words ("only", "may",
"仅", "可能", ...) whose counts changed. It needs only the standard library.

Exit status: 0 when nothing differs, 1 when something does, 2 on a usage or
read error. A difference is a question for the editor, not a verdict, and a
clean run does not show that the meaning survived.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter

CITE = re.compile(r"\\(?:[a-zA-Z]*cite[a-zA-Z]*|nocite)\*?(?:\[[^\]]*\])*\{([^}]*)\}")
REF = re.compile(r"\\(?:[a-zA-Z]*ref|[cC]ref[a-z]*|autoref|nameref|pageref)\*?\{([^}]*)\}")
LABEL = re.compile(r"\\label\{([^}]*)\}")
FILE_ARG = re.compile(r"\\(?:input|include|includegraphics|bibliography|addbibresource)(?:\[[^\]]*\])?\{([^}]*)\}")
MATH_ENV = "equation|align|aligned|gather|multline|eqnarray|displaymath|math|flalign|alignat"
MATH = re.compile(
    r"\\begin\{(" + MATH_ENV + r")\*?\}.*?\\end\{\1\*?\}"
    r"|\$\$.+?\$\$"
    r"|\\\[.+?\\\]"
    r"|\\\(.+?\\\)"
    r"|(?<![\\$])\$(?!\s)[^$\n]+?(?<![\s\\])\$(?!\d)",
    re.S,
)
FENCE = re.compile(r"^(```|~~~)[^\n]*\n.*?^\1[ \t]*$", re.S | re.M)
VERBATIM = re.compile(r"\\begin\{(verbatim|lstlisting|minted)\*?\}.*?\\end\{\1\*?\}", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`|\\(?:texttt|verb\*?|lstinline|path)\{[^}]*\}")
MD_CITE = re.compile(r"(?<![\w.])@([A-Za-z][\w:.\-/]*\w)")
URL = re.compile(r"https?://[^\s<>\"')\]}]+")
MD_LINK = re.compile(r"\]\(([^)\s]+)[^)]*\)")
NUMBER = re.compile(r"(?<![\w.])\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-+]?\d+)?(?:\s?\\?%)?")
NUMBER_WORD = re.compile(
    r"\b(?:zero|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|"
    r"forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|"
    r"half|twice|thrice|double|doubles|doubled|triple|tripled|halves|halved)\b",
    re.I,
)
ZH_NUMBER = re.compile(r"[零〇一二两三四五六七八九十百千万亿]{1,}(?=[个次倍种类项轮组条篇年月天日周秒成%％])|[零〇二两三四五六七八九十百千万亿半]+倍|翻倍|减半")
TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*")
MID_SENTENCE_NAME = re.compile(r"(?<=[a-z,;:] )[A-Z][a-z]+(?:[-'][A-Za-z]+)*")

QUALIFIERS_EN = [
    "only", "not", "never", "may", "might", "could", "cannot", "at least",
    "at most", "up to", "on average", "approximately", "roughly", "nearly",
    "almost", "before", "after", "until", "unless", "except", "without",
    "relative to", "compared with", "compared to", "at the same time",
    "significant", "significantly", "likely", "unlikely", "suggest",
    "suggests", "preliminary",
]
QUALIFIERS_ZH = [
    "仅", "只有", "只", "可能", "或许", "大约", "约", "平均", "至少", "至多",
    "最多", "最少", "尚未", "未", "没有", "不能", "不会", "无法", "除非",
    "除了", "部分", "所有", "同时", "之前", "之后", "相比", "相对于", "显著",
    "初步",
]


def is_name(token: str) -> bool:
    """True for acronyms, CamelCase, and letter-digit identifiers such as AdamW, SGD, FP32, GPT-4."""
    upper = sum(c.isupper() for c in token)
    has_digit = any(c.isdigit() for c in token)
    camel = re.search(r"[a-z][A-Z]", token) is not None
    return upper >= 2 or camel or (upper >= 1 and has_digit)


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).replace("\r\n", "\n")


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def take(pattern: re.Pattern, text: str, bucket: Counter, group: int = 0, split_keys: bool = False) -> str:
    """Count every match (or one group of it) in bucket and blank the matches out of text."""

    def repl(match: re.Match) -> str:
        value = match.group(group)
        if split_keys:
            for key in value.split(","):
                if key.strip():
                    bucket[key.strip()] += 1
        else:
            bucket[squash(value)] += 1
        return " "

    return pattern.sub(repl, text)


def extract(raw: str) -> dict[str, Counter]:
    text = normalize(raw)
    out: dict[str, Counter] = {
        name: Counter()
        for name in ("citations", "labels", "references", "files", "math", "code", "links", "numbers", "names", "qualifiers")
    }
    if re.search(r"\\(?:begin|section|cite|label|ref)\b", text):
        # TeX: drop comments so a commented-out draft does not count; keep an escaped \%.
        text = re.sub(r"(?<!\\)%.*", "", text)

    text = take(FENCE, text, out["code"])
    text = take(VERBATIM, text, out["code"])
    text = take(CITE, text, out["citations"], group=1, split_keys=True)
    text = take(REF, text, out["references"], group=1, split_keys=True)
    text = take(LABEL, text, out["labels"], group=1)
    text = take(FILE_ARG, text, out["files"], group=1)
    text = take(MATH, text, out["math"])
    text = take(INLINE_CODE, text, out["code"])
    text = take(MD_LINK, text, out["links"], group=1)
    text = take(URL, text, out["links"])
    text = take(MD_CITE, text, out["citations"], group=1)

    for match in TOKEN.finditer(text):
        if is_name(match.group(0)):
            out["names"][match.group(0)] += 1
    for match in MID_SENTENCE_NAME.finditer(text):
        out["names"][match.group(0)] += 1
    for match in NUMBER.finditer(text):
        out["numbers"][re.sub(r"[\s\\]", "", match.group(0))] += 1
    for match in NUMBER_WORD.finditer(text):
        out["numbers"][match.group(0).lower()] += 1
    for match in ZH_NUMBER.finditer(text):
        out["numbers"][match.group(0)] += 1

    lowered = text.lower()
    for word in QUALIFIERS_EN:
        count = len(re.findall(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])", lowered))
        if count:
            out["qualifiers"][word] = count
    # Longest first, so "只有" is not also counted as "只".
    remaining = text
    for word in sorted(QUALIFIERS_ZH, key=len, reverse=True):
        count = remaining.count(word)
        if count:
            out["qualifiers"][word] = count
            remaining = remaining.replace(word, " ")
    return out


def show(item: str, limit: int = 100) -> str:
    return item if len(item) <= limit else item[: limit - 1] + "…"


def compare(before: str, after: str, title: str) -> bool:
    old, new = extract(before), extract(after)
    lines: list[str] = []
    for category in ("citations", "references", "labels", "files", "math", "code", "links", "numbers", "names"):
        missing = old[category] - new[category]
        added = new[category] - old[category]
        if missing:
            lines.append(f"  {category} only in the original:")
            lines += [f"    - {show(k)}" + (f"  (x{n})" if n > 1 else "") for k, n in sorted(missing.items())]
        if added:
            lines.append(f"  {category} only in the revision:")
            lines += [f"    + {show(k)}" + (f"  (x{n})" if n > 1 else "") for k, n in sorted(added.items())]
    changed = sorted(
        (word, old["qualifiers"][word], new["qualifiers"][word])
        for word in set(old["qualifiers"]) | set(new["qualifiers"])
        if old["qualifiers"][word] != new["qualifiers"][word]
    )
    if changed:
        lines.append("  qualifier counts that changed (original -> revision):")
        lines += [f"    ~ {word}: {a} -> {b}" for word, a, b in changed]
    print(f"{title}")
    if lines:
        print("\n".join(lines))
    else:
        print("  no differences in the items this script can see")
    return bool(lines)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List numbers, citations, labels, math, code, links, names, and qualifiers that differ between two versions of a text.",
        epilog="Every line is something to explain or restore. A clean run is not proof that the meaning survived.",
    )
    parser.add_argument("--git", action="store_true", help="compare each PATH at --rev with the working tree")
    parser.add_argument("--rev", default="HEAD", help="revision for --git (default: HEAD)")
    parser.add_argument("paths", nargs="+", metavar="PATH")
    args = parser.parse_args()

    differs = False
    try:
        if args.git:
            for path in args.paths:
                spec = f"{args.rev}:./{os.path.relpath(path)}"
                shown = subprocess.run(["git", "show", spec], capture_output=True, text=True, encoding="utf-8")
                if shown.returncode != 0:
                    print(f"{path}: not found at {args.rev}: {shown.stderr.strip()}", file=sys.stderr)
                    return 2
                differs |= compare(shown.stdout, read(path), f"{path} ({args.rev} -> working tree)")
        else:
            if len(args.paths) != 2:
                parser.error("give BEFORE and AFTER, or use --git PATH ...")
            differs = compare(read(args.paths[0]), read(args.paths[1]), f"{args.paths[0]} -> {args.paths[1]}")
    except (OSError, UnicodeDecodeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 1 if differs else 0


if __name__ == "__main__":
    sys.exit(main())
