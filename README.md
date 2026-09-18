## The Three Laws of Vibe Coding

1. Vibe coding must not generate slop or, through inaction, allow slop to enter and harm the codebase.

2. Vibe coding must deslop generated code according to developer intent, project conventions, and testing requirements, except where such requirements would conflict with the First Law.

3. Vibe coding must preserve development velocity, as long as doing so does not generate slop, obstruct deslopping, or conflict with the First or Second Law.

## Deslop and humanize skill

[`deslop-and-humanize`](skills/deslop-and-humanize/SKILL.md) applies these principles to writing and code. It removes filler, formulaic phrasing, and unnecessary complexity while preserving the author's meaning, evidence, and tone, and the code's behavior. It covers English and Chinese, with guidance for research conclusions and feedback.

The same skill folder works with Claude Code and Codex. It has no scripts, tool dependencies, or provider-specific frontmatter.

### Install

Clone this repository, then run the commands for your tool from the repository root:

```sh
git clone https://github.com/yifanzhang-pro/the-three-laws-of-vibe-coding.git
cd the-three-laws-of-vibe-coding
```

Claude Code:

```sh
mkdir -p "$HOME/.claude/skills"
if [ ! -e "$HOME/.claude/skills/deslop-and-humanize" ] && [ ! -L "$HOME/.claude/skills/deslop-and-humanize" ]; then
  cp -R skills/deslop-and-humanize "$HOME/.claude/skills/"
else
  echo 'Skill already exists; review it before replacing it.'
fi
```

Codex:

```sh
mkdir -p "$HOME/.agents/skills"
if [ ! -e "$HOME/.agents/skills/deslop-and-humanize" ] && [ ! -L "$HOME/.agents/skills/deslop-and-humanize" ]; then
  cp -R skills/deslop-and-humanize "$HOME/.agents/skills/"
else
  echo 'Skill already exists; review it before replacing it.'
fi
```

For a project-only installation, copy the whole skill folder into that project's `.claude/skills/` for Claude Code or `.agents/skills/` for Codex instead. Keep `references/` alongside `SKILL.md`. These locations follow the [Claude Code](https://code.claude.com/docs/en/skills) and [Codex](https://developers.openai.com/codex/skills) documentation. Restart your session if the new skill does not appear.

### Use

In Claude Code:

```text
/deslop-and-humanize Edit the conclusion in paper.tex. Preserve the claims, citations, and limitations.
```

In Codex:

```text
$deslop-and-humanize Edit feedback.md to sound direct and natural. Keep every substantive criticism.
```

It can also be selected automatically for requests such as "Deslop this diff without changing behavior." Ordinary feature development does not need this skill.
