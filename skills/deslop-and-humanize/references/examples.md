# Editing examples

These examples are fictional. Their numbers and findings must not be carried into another document. Each revision preserves the supplied evidence and uncertainty. The notes explain the editorial decision and the information that must survive; they are not text to append to a user's document.

Read the cases that match the document in front of you:

- Research and technical prose: [research conclusion](#research-conclusion), [technical notation](#preserve-technical-notation-during-a-prose-edit), [a comparison list](#a-comparison-cannot-silently-lose-an-item), [an attribution problem](#an-attribution-problem-should-stay-visible), [a staged contrast](#remove-a-staged-contrast-without-losing-the-mechanism)
- Chinese: [technical prose](#chinese-technical-prose), [translationese in a message](#chinese-translationese-in-a-message)
- Feedback, email, and voice: [feedback](#feedback), [email courtesy](#courtesy-belongs-in-an-email), [voice from a sample](#preserve-voice-without-inventing-an-experience)
- Repository prose: [commit message](#a-commit-message-says-what-changed-and-why), [report after a file edit](#report-after-a-file-edit)
- Restraint: [a clear sentence](#a-clear-sentence-needs-no-edit), [a light edit](#a-light-edit-stays-light), [a necessary code comment](#a-code-comment-can-be-necessary)
- Code: [cleanup with evidence](#code-cleanup-needs-evidence-of-equivalence)

## Research conclusion

Before:

> In conclusion, our groundbreaking framework represents a significant step forward in multi-agent research. Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. These findings highlight the transformative potential of collaboration. However, we did not control for total compute, and it remains unclear whether the improvement persists at larger scales.

After:

> Across three runs, shared memory reduced duplicate experiments by 18% relative to independent agents. Total compute was not controlled, so these results do not establish an efficiency gain at equal compute. Whether the reduction persists at larger scales remains untested.

The revision keeps the result, baseline, sample size, and limits. It removes praise and makes the consequence of the missing control explicit. “Shared memory makes research 18% more efficient” would change both the metric and the claim.

## Feedback

Before:

> This is a compelling and timely contribution. That said, it might be worth considering whether the authors could perhaps provide additional clarity regarding the evaluation setup, especially the number of random seeds, which is not currently reported.

After:

> Please report the number of random seeds used in the evaluation. This would clarify whether the results cover multiple seeds.

The request stays polite and explains why the missing detail matters. It does not invent a requirement for a particular number of seeds or assume that each run uses a different seed.

## Chinese technical prose

Before:

> 值得注意的是，本方法通过引入共享缓存机制，有效赋能了推理流程的全面优化。在 batch size 为 8 的实验中，平均延迟从 120 ms 降至 95 ms。这充分彰显了该方法在实际应用中的巨大潜力，但其他 batch size 尚未测试。

After:

> 引入共享缓存后，在 batch size 为 8 的实验中，平均延迟从 120 ms 降至 95 ms。其他 batch size 尚未测试。

The revision preserves the measured quantity, condition, and limitation. It does not generalize the result to every workload or replace latency with throughput.

## A clear sentence needs no edit

> The estimate is unbiased under independent sampling, but its variance increases as the success probability approaches zero.

Keep this sentence. The contrast and technical terms carry information. Replacing “unbiased” with “accurate” would lose precision.

## A code comment can be necessary

```python
# The upstream service may retry a completed request; preserve idempotency.
if request_id in completed:
    return completed[request_id]
```

Keep the guard and explanation unless the surrounding contract has changed. They describe required behavior. Removing them because the branch looks defensive would be a functional change.

## Remove a staged contrast without losing the mechanism

Before:

> Here's the thing: the index is not just a convenience. It is the foundation of discovery. Each entry records a result and links to its parent experiment. That is the real win.

After:

> Each index entry records a result and links to its parent experiment.

The links explain what the index contains. The revised text does not claim that it improves discovery or eliminates duplicated work, because neither result was supplied.

## Preserve voice without inventing an experience

Draft:

> I found the setup frustrating. The first run failed twice, but the error message identified the missing package. Once installed, the example worked. Overall, this represents a testament to the project's commitment to a seamless developer experience.

Supplied voice sample, about a different subject:

> I like the bike. The brakes squeak, which annoys me, but I'm keeping it.

Revision:

> The setup frustrated me. The first run failed twice, but the error message pointed to the missing package. I installed it, and the example worked.

The revision uses the sample's directness and keeps the draft's frustration. It does not add a late-night debugging session, a claim about support staff, or a feeling of relief. The sample's facts have no place in the revision.

## An attribution problem should stay visible

Before:

> Experts agree that the new scheduler halves training cost, underscoring its transformative potential.

Revision:

> Experts agree that the new scheduler halves training cost.

Separate editorial note:

> The draft does not identify the experts or the evidence for the cost claim. Please supply the source and comparison conditions before presenting this as an established result.

Removing the empty ending is a style edit. Deleting “experts agree” would make an unsupported attribution look like a verified result. Do not invent a citation or silently discard the cost claim. This revision is still unresolved, not publication-ready factual validation.

## A comparison cannot silently lose an item

Before:

> The experiment comprehensively evaluated SGD, AdamW, and Muon under the same token budget, thereby highlighting the breadth of our analysis.

After:

> The experiment evaluated SGD, AdamW, and Muon under the same token budget.

All three optimizers and the comparison condition remain. A three-item list is appropriate here. “Several optimizers” would lose information in a full edit; it may be appropriate in an explicitly requested summary.

## Courtesy belongs in an email

Before:

> Hi Lin, thank you for sending the revised draft. I would be grateful if you could let me know whether Tuesday works for a short call. Best, Sam

After:

> Hi Lin, thank you for sending the revised draft. Could you let me know whether Tuesday works for a short call? Best, Sam

The request becomes simpler while retaining the thanks, question, and sign-off. Do not strip “let me know” just because it resembles an assistant's closing offer. Keep the more formal original if the user wants that register.

## Preserve technical notation during a prose edit

Before:

```tex
It is worth noting that, under Assumption~\ref{ass:independent}, the estimator $\hat g$ is unbiased; see Eq.~\eqref{eq:gradient}.
```

After:

```tex
Under Assumption~\ref{ass:independent}, the estimator $\hat g$ is unbiased; see Eq.~\eqref{eq:gradient}.
```

The assumption, mathematical symbol, and both references remain. Do not rewrite the equation or omit the assumption to shorten the sentence.

## Code cleanup needs evidence of equivalence

Before:

```python
def is_enabled(config):
    # Check whether the enabled flag is true and return a boolean.
    if config.enabled:
        return True
    else:
        return False
```

After, when the surrounding contract confirms `config.enabled` is a plain boolean field:

```python
def is_enabled(config):
    return config.enabled
```

The contract matters. If the field can contain other values, this rewrite changes the return value or type. Inspect that contract rather than assuming the shorter version is equivalent. Run the relevant existing behavior checks when applying the change.

## Chinese translationese in a message

Before:

> 王老师您好，非常感谢您对我们的论文进行了详细的审阅。对于您所提出的关于实验设置方面的问题，我们已经在修订稿中进行了相应的补充说明。值得一提的是，我们新增了 3 组对比实验。如果您还有任何其他的问题的话，请随时与我们联系。

After:

> 王老师您好，非常感谢您详细审阅我们的论文。您提出的实验设置问题，我们已在修订稿中补充说明，并新增了 3 组对比实验。如果还有其他问题，请随时联系我们。

The salutation, the thanks, 您, the count of experiments, and the closing invitation all remain; the invitation is a real request from one person to another. The edit removes 进行 with a noun, 对于…方面, 的话, and an opener that announced the next sentence. It does not make the message casual.

## A light edit stays light

Request: “Fix the grammar, nothing else.”

Before:

> Our approach, which leverage a shared cache, reduce average latency from 120 ms to 95 ms at batch size 8. It is worth noting that this represent a meaningful improvement.

After:

> Our approach, which leverages a shared cache, reduces average latency from 120 ms to 95 ms at batch size 8. It is worth noting that this represents a meaningful improvement.

Three verbs now agree with their subjects. The second sentence is filler and “leverages” could be “uses,” but the user asked for grammar. Mention the sentence in one line after the revision if it seems worth their attention; do not cut it.

## A commit message says what changed and why

Draft written after a long debugging session:

```text
Fix critical caching bug and significantly improve robustness

After extensive investigation, I discovered that the cache was not
properly handling retries. This commit comprehensively addresses the
issue by introducing a robust idempotency check, ensuring a seamless
experience for users.

- Updated cache.py
- Added tests
- All tests pass
```

Revision, in a repository whose history uses short imperative subjects:

```text
Return cached response for retried request IDs

The upstream service retries requests that already completed. Each
retry ran the handler again and wrote a duplicate row. Look up the
request ID in the completed map first and return the stored response.

Tested: pytest tests/test_cache.py (2 new cases for retried IDs)
```

The subject names the behavior. The body gives the cause and the fix, which the diff alone does not explain. The investigation, the praise, and the file list are gone, because the diff already shows which files changed. “All tests pass” became the command that ran; if nothing ran, the line would say so or be absent.

## Report after a file edit

Request: “Deslop `sections/results.tex`.”

```text
Edited: sections/results.tex, paragraphs 1–4 and the caption of Table 2
Changes:
- Cut two staged openers and the summary sentence that repeated paragraph 3
- Replaced “demonstrates the superiority of” with the measured difference already given in the sentence
- Merged the two sentences on the missing compute control so the limitation sits next to the result
Flags:
- Line 41, “widely regarded as the standard baseline”: no citation. Kept as written; needs a source or a narrower claim.
- Line 58 says 18% and Table 2 says 17.6%. Left both; one of them needs to change.
Checks: check_fidelity.py --git sections/results.tex reported one number missing (the “2” in “2 key insights,” from a deleted sentence) and no citation, label, or math changes; tectonic build passed with no undefined references.
Not done: the abstract in main.tex repeats the sentence at line 58; left untouched because it was outside the request.
```

The report tells the author where to look in the diff and what still needs a decision. It does not list every changed word, restate the request, or say the text is now publication-ready. The flags are in the report and not in the `.tex` file.
