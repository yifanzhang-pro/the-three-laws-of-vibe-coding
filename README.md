# The Three Laws of Vibe Coding

1. Vibe coding must not generate slop or, through inaction, allow slop to enter and harm the codebase.

2. Vibe coding must deslop generated code according to developer intent, project conventions, and testing requirements, except where such requirements would conflict with the First Law.

3. Vibe coding must preserve development velocity, as long as doing so does not generate slop, obstruct deslopping, or conflict with the First or Second Law.

The laws set an order of priorities for AI-assisted development. Here, slop means filler or complexity that obscures meaning, lacks support, or serves no requirement. Length, formality, and unfamiliar style are not enough to make something slop.

## Deslop and humanize

[`deslop-and-humanize`](skills/deslop-and-humanize/SKILL.md) turns the laws into an editing workflow for Claude Code and Codex. It handles English and Chinese prose, research papers, feedback, commit messages and PR descriptions, and requested code cleanup. The skill is Markdown instructions with no provider-specific frontmatter, plus one optional Python script that uses only the standard library.

It reads for argument and voice before changing individual words. It then checks the revision against the original for lost facts, altered uncertainty, and broken technical notation; for file edits, [`check_fidelity.py`](skills/deslop-and-humanize/scripts/check_fidelity.py) lists the numbers, citation keys, labels, math, and links that differ between the two versions. A second editorial pass catches repeated endings or other formulaic structure that survived the first edit. Pasted text comes back as the finished text alone. A file edit comes back with a short report: what changed, which claims need a source, and which checks ran.

### What changes and what stays

| Material | Edit | Preserve |
| --- | --- | --- |
| Research prose | Staged openings, repeated conclusions, unsupported praise | Findings, assumptions, baselines, citations, and limitations |
| Feedback | Praise sandwiches, duplicate softeners, vague requests | Substantive criticism, warranted praise, and intended politeness |
| Personal writing and email | Generic phrasing and distracting repetition | The writer's actual opinions, humor, courtesies, and experiences |
| Documentation | Chat residue, obsolete drafting commentary, empty labels | Current behavior, commands, data, links, and relevant history |
| Commit messages and PR descriptions | The story of the work, praise, restated diffs, empty headings | What changed, why, and what was actually tested |
| Code, when requested | Redundant branches, unused scaffolding, unnecessary indirection | Observable behavior, interfaces, boundary checks, and useful comments |

A dash, passive sentence, or three-item list can be the right choice. These are cues to inspect in context, not automatic editing rules. The skill does not determine authorship or promise to bypass AI detectors. It also does not invent details to make a passage sound more personal.

### Install

With the [`skills` CLI](https://github.com/vercel-labs/skills), which needs Node.js 22.20 or later, one command installs the skill for both tools in your user directory:

```sh
npx skills add yifanzhang-pro/the-three-laws-of-vibe-coding --skill deslop-and-humanize -g -a claude-code -a codex
```

Leave out `-g` to install into the current project. `npx skills update deslop-and-humanize` fetches a newer version later.

Without Node, clone the repository and link the skill folder, so that `git pull` updates the installed skill:

```sh
git clone https://github.com/yifanzhang-pro/the-three-laws-of-vibe-coding.git
cd the-three-laws-of-vibe-coding
```

Claude Code:

```sh
mkdir -p "$HOME/.claude/skills" && ln -s "$PWD/skills/deslop-and-humanize" "$HOME/.claude/skills/deslop-and-humanize"
```

Codex:

```sh
mkdir -p "$HOME/.agents/skills" && ln -s "$PWD/skills/deslop-and-humanize" "$HOME/.agents/skills/deslop-and-humanize"
```

`ln -s` refuses to replace an existing skill of the same name; look at what is there before removing it. To pin a copy, or to install into one project, use `cp -R skills/deslop-and-humanize <dir>` with `.claude/skills/` for Claude Code or `.agents/skills/` for Codex as the directory. Keep `references/` and `scripts/` alongside `SKILL.md`. These locations follow the [Claude Code](https://code.claude.com/docs/en/skills) and [Codex](https://developers.openai.com/codex/skills) documentation. Restart your session if the new skill does not appear.

### Use

In Claude Code, `/deslop-and-humanize` followed by the target; in Codex, `$deslop-and-humanize`:

```text
/deslop-and-humanize Edit the conclusion in paper.tex. Preserve the claims, citations, and limitations.
```

```text
$deslop-and-humanize Edit feedback.md to sound direct and natural. Keep every substantive criticism.
```

The request sets the mode, and the skill does not go further than the request:

| You write | You get |
| --- | --- |
| The skill name alone | An edit of the text you last pasted, or of the prose in your uncommitted diff |
| “Proofread” or “light” | Word-level fixes; sentences and structure stay |
| “Deslop,” “humanize,” “polish,” 润色, 去AI味 | Sentence and paragraph edits inside the passage |
| “Rewrite” or “restructure” | Permission to move and merge material |
| “Review” or “comments only” | Comments on quoted phrases, and no file edits |
| “Write the commit message,” “draft the abstract” | New text written under the same rules |
| “Deslop this diff without changing behavior” | Code cleanup with the existing checks run |

For voice matching, include a short sample and identify it separately from the text to edit:

```text
Use this paragraph as a sample of my voice: [sample]
Humanize the following draft: [draft]
Keep its facts and opinions; do not borrow experiences from the sample.
```

The skill can also be selected automatically when a request matches. Ordinary feature development and authorship detection are outside its scope.

### Use it across a repository

Agents forget a skill that nothing in the repository mentions. To have every prose edit in a project go through it, put this in the project's `AGENTS.md`, or in `CLAUDE.md` for Claude Code alone:

```markdown
## Writing

Use the `deslop-and-humanize` skill for every prose edit and every new piece of prose: papers, docs, READMEs, issues, PR descriptions, and commit messages. If the skill is not installed, read `SKILL.md` and the files it points to at
https://github.com/yifanzhang-pro/the-three-laws-of-vibe-coding/tree/master/skills/deslop-and-humanize
before editing.
```

Add the project's own vocabulary and build commands below it. The skill reads the project's agent instructions first and treats them as overriding its general guidance.

### Check an edit yourself

The fidelity script also works by hand on any two versions of a file, or on a file you have edited since the last commit:

```sh
python3 skills/deslop-and-humanize/scripts/check_fidelity.py before.md after.md
```

```sh
python3 skills/deslop-and-humanize/scripts/check_fidelity.py --git paper/intro.tex
```

It prints the numbers, citation keys, labels, cross-references, math, code, links, and capitalized names found in one version and not the other, and the qualifier words whose counts changed. It exits with status 1 when anything differs. It cannot see a paraphrase that changes a claim, so a clean run is a floor and not a proof.

### Example

Before:

> In conclusion, our groundbreaking framework represents a significant step forward in multi-agent research. Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. However, we did not control for total compute.

After:

> Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. Total compute was not controlled, so these results do not establish an efficiency gain at equal compute.

This is a fictional example. The revision keeps the measurement and the missing control; it does not claim an 18% efficiency gain. See the [worked examples](skills/deslop-and-humanize/references/examples.md) for Chinese prose, feedback, voice matching, a commit message, and cases that should remain unchanged.

## Read the guidance

- [Skill instructions](skills/deslop-and-humanize/SKILL.md): scope, fidelity, editing, review, and delivery.
- [Prose patterns](skills/deslop-and-humanize/references/patterns.md): recurring problems and the exceptions that prevent over-editing.
- [Chinese prose](skills/deslop-and-humanize/references/chinese.md): translationese, official register, and punctuation, with the cases to leave alone.
- [Worked examples](skills/deslop-and-humanize/references/examples.md): before/after passages with preservation notes.
- [Fidelity check](skills/deslop-and-humanize/scripts/check_fidelity.py): the script described above.
- [Project page](https://yifanzhang-pro.github.io/the-three-laws-of-vibe-coding/): the laws and an overview of the skill.

## Acknowledgments and editorial choices

The prose guidance draws on [blader/humanizer](https://github.com/blader/humanizer/tree/9862685f575c65a8247f90369951df1b3416e3d6), particularly its attention to paragraph structure, author voice, staged rhetoric, and a review after rewriting. The upstream MIT notice and reviewed revision are included in the [skill's attribution file](skills/deslop-and-humanize/references/humanizer-notice.txt), so attribution travels with an installed copy.

This adaptation uses contextual judgments in place of automatic punctuation bans or fixed pattern rankings. It requires source support for added detail and preserves substantive claims even when their attribution needs checking. It returns the final revision by default and adds safeguards for research writing, Chinese prose, and code behavior. The examples here are original to this repository.
