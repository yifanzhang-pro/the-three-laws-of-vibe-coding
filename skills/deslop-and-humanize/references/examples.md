# Editing examples

These examples are fictional. Their numbers and findings must not be carried into another document. Each revision preserves the supplied evidence and uncertainty.

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

> Please report the number of random seeds used in the evaluation. Without it, readers cannot tell how many independent runs support the result.

The request stays polite and explains why the missing detail matters. It does not invent a requirement for a particular number of seeds.

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
