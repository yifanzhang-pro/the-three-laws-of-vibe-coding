# The Three Laws of Vibe Coding

1. Vibe coding must not generate slop or, through inaction, allow slop to enter and harm the codebase.

2. Vibe coding must deslop generated code according to developer intent, project conventions, and testing requirements, except where such requirements would conflict with the First Law.

3. Vibe coding must preserve development velocity, as long as doing so does not generate slop, obstruct deslopping, or conflict with the First or Second Law.

The laws set an order of priorities for AI-assisted development. Here, slop means filler or complexity that obscures meaning, lacks support, or serves no requirement. Length, formality, and unfamiliar style are not enough to make something slop.

## Deslop and humanize

[`deslop-and-humanize`](skills/deslop-and-humanize/SKILL.md) turns the laws into an editing workflow for Claude Code and Codex. It handles English and Chinese prose, research papers, feedback, and requested code cleanup. The shared skill is Markdown only, with no tool dependencies or provider-specific frontmatter.

It reads for argument and voice before changing individual words. It then checks the revision against the original for lost facts, altered uncertainty, and broken technical notation. A second editorial pass catches repeated endings or other formulaic structure that survived the first edit. The default output is the finished text; intermediate drafts stay internal unless requested.

### What changes and what stays

| Material | Edit | Preserve |
| --- | --- | --- |
| Research prose | Staged openings, repeated conclusions, unsupported praise | Findings, assumptions, baselines, citations, and limitations |
| Feedback | Praise sandwiches, duplicate softeners, vague requests | Substantive criticism, warranted praise, and intended politeness |
| Personal writing and email | Generic phrasing and distracting repetition | The writer's actual opinions, humor, courtesies, and experiences |
| Documentation | Chat residue, obsolete drafting commentary, empty labels | Current behavior, commands, data, links, and relevant history |
| Code, when requested | Redundant branches, unused scaffolding, unnecessary indirection | Observable behavior, interfaces, boundary checks, and useful comments |

A dash, passive sentence, or three-item list can be the right choice. These are cues to inspect in context, not automatic editing rules. The skill does not determine authorship or promise to bypass AI detectors. It also does not invent details to make a passage sound more personal.

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

For voice matching, include a short sample and identify it separately from the text to edit:

```text
Use this paragraph as a sample of my voice: [sample]
Humanize the following draft: [draft]
Keep its facts and opinions; do not borrow experiences from the sample.
```

You can also ask “去掉这段文字的 AI 味，保留技术含义” or “Deslop this diff without changing behavior.” The skill can be selected automatically when the request matches. Ask for comments only if you want a review without file edits. Ordinary feature development and authorship detection are outside its scope.

### Example

Before:

> In conclusion, our groundbreaking framework represents a significant step forward in multi-agent research. Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. However, we did not control for total compute.

After:

> Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. Total compute was not controlled, so these results do not establish an efficiency gain at equal compute.

This is a fictional example. The revision keeps the measurement and the missing control; it does not claim an 18% efficiency gain. See the [worked examples](skills/deslop-and-humanize/references/examples.md) for Chinese prose, feedback, voice matching, and cases that should remain unchanged.

## Read the guidance

- [Skill instructions](skills/deslop-and-humanize/SKILL.md): scope, fidelity, editing, review, and delivery.
- [Prose patterns](skills/deslop-and-humanize/references/patterns.md): recurring problems and the exceptions that prevent over-editing.
- [Worked examples](skills/deslop-and-humanize/references/examples.md): before/after passages with preservation notes.
- [Project page](https://yifanzhang-pro.github.io/the-three-laws-of-vibe-coding/): the laws and an overview of the skill.

## Acknowledgments and editorial choices

The prose guidance draws on [blader/humanizer](https://github.com/blader/humanizer/tree/9862685f575c65a8247f90369951df1b3416e3d6), particularly its attention to paragraph structure, author voice, staged rhetoric, and a review after rewriting. The upstream MIT notice and reviewed revision are included in the [skill's attribution file](skills/deslop-and-humanize/references/humanizer-notice.txt), so attribution travels with an installed copy.

This adaptation uses contextual judgments in place of automatic punctuation bans or fixed pattern rankings. It requires source support for added detail and preserves substantive claims even when their attribution needs checking. It returns the final revision by default and adds safeguards for research writing, Chinese prose, and code behavior. The examples here are original to this repository.
