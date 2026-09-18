---
name: deslop-and-humanize
description: Remove AI-style filler, formulaic prose, and unnecessary code complexity while preserving meaning and behavior. Use when asked to deslop, humanize, remove AI tone, 去AI味, or clean up generated writing or code. Supports English and Chinese; ordinary feature work and factual review alone are outside this skill's scope.
---

# Deslop and humanize

Apply the Three Laws of Vibe Coding to editing: avoid adding slop; clean up according to the user's intent and project conventions; keep the work proportionate. For prose, this means making the author's actual point easier to read. For code, it means removing complexity that serves no requirement.

## Establish the edit

Read the requested material and enough surrounding context to understand its purpose. Use the existing audience, language, register, and project conventions unless the user asks to change them. A paper should still sound like a paper; a friendly email should still sound like its sender.

Respect the requested scope. A grammar fix is a light edit. A request to deslop a conclusion permits restructuring that conclusion, not rewriting the paper. For a repository request, inspect the relevant diff and nearby code before changing it. Ask only when the target or intended meaning cannot be inferred safely.

## Preserve what matters

- Keep facts, numbers, units, names, citations, assumptions, and substantive limitations. Preserve attribution and direct quotations unless explicitly asked to edit the quoted text.
- Preserve the strength of claims. Do not turn an observation into causation, a possibility into a guarantee, or preliminary evidence into a general result. Do not soften a supported claim just to sound cautious.
- Keep technical terms when they carry meaning. Do not replace a precise term with a vague synonym to avoid repetition.
- Preserve equations, LaTeX commands, labels, references, code identifiers, and public interfaces. Edit surrounding language without breaking syntax.
- Never invent evidence, anecdotes, opinions, personal experience, or citations to make the author sound human. If a factual conflict blocks the rewrite, flag it separately instead of silently choosing an answer.

## Edit prose

Start with meaning and structure, then edit sentences. Put the main claim where the reader needs it, connect each claim to its evidence, and remove passages that merely announce or repeat the point.

Look for these problems in context:

- Empty openings and transitions: “In today's rapidly evolving landscape,” “It is worth noting,” “Furthermore,” or “综上所述” when they add no relationship or information.
- Unsupported praise and scale: “groundbreaking,” “transformative,” “seamless,” “robust,” “赋能,” or “具有重要意义” without an explanation of what happened or improved.
- Stock rhetoric: repeated “not X, but Y,” forced three-part lists, rhetorical questions answered immediately, and paragraphs that all follow the same template.
- Inflated verbs and noun phrases: prefer “use” to “leverage” when the meaning is identical; replace “conduct an evaluation of” with “evaluate.”
- Excess formatting: bold lead-ins on every bullet, headings for single sentences, and lists where connected prose would explain the reasoning better.
- Repeated conclusions, generic future-work promises, and claims that only restate the abstract.

These are cues to inspect, not banned words or punctuation. Keep a contrast, list, transition, or em dash when it does useful work. Do not perform mechanical synonym substitution or strip all connective language.

Make the result natural through concrete subjects, direct verbs, coherent paragraphs, and sentence lengths suited to the argument. Preserve warmth, humor, and distinctive phrasing already present. Do not add slang, deliberate mistakes, choppy fragments, or fake personality. Do not claim that an edit can evade AI detectors or establish human authorship.

For Chinese, remove translationese and stacked abstractions while retaining the intended level of formality. Do not translate the document or switch languages unless requested.

For research conclusions, state what the work established and under what conditions; keep the limitations that affect interpretation. Include future work only when it names a concrete unresolved question. For feedback, identify the issue, explain its consequence, and suggest a specific correction without a generic praise sandwich.

Read [references/examples.md](references/examples.md) when editing research conclusions, reviewer feedback, or Chinese prose, or when an example would help calibrate how much to change. The examples illustrate judgment, not templates to copy.

## Edit code when code is in scope

Follow the repository's conventions and preserve behavior. Inspect callers, types, and tests before removing a wrapper, fallback, validation, or abstraction. Remove unused scaffolding, redundant branches, comments that only narrate syntax, and abstractions that add indirection without serving a current need.

Keep comments explaining constraints or surprising decisions. Keep error handling and boundary validation that protect real inputs or contracts. Do not classify unfamiliar code as slop, remove checks merely to shorten a function, or introduce a new abstraction during cleanup without a demonstrated need. Treat a discovered behavior bug as a separate issue unless fixing it is within the user's request.

## Check and deliver

Compare the revision with the original for lost qualifications, changed claims, broken references, or altered behavior. Read the edited passage as a whole: sentence-level improvements can still leave a repetitive argument. Leave already-clear material alone. Stop when the concrete problems are resolved.

For code changes, run relevant existing checks and add tests only when needed to establish behavior. For document changes, use the project's available build or render checks when markup or layout is affected. Report checks actually run and any material verification limits.

For pasted prose, return the revised text directly unless the user asks for explanation. For file edits, make the edits and briefly report meaningful changes. Follow any requested diff or comment format. Keep unresolved factual questions separate from the polished text. Publishing, sending, or opening a PR requires authorization from the user's request; using this skill alone does not grant it.
