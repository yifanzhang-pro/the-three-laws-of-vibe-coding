# Editing examples

These examples are fictional. Their numbers and findings must not be carried into another document. Each revision preserves the supplied evidence and uncertainty. The notes explain the editorial decision and the information that must survive; they are not text to append to a user's document.

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
