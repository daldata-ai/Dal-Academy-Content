# 02 · Data Processing Architectures

Batch, micro-batch, streaming, state, windows, latency, and reliability.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hanoufalmogri/Dal-Academy-Content/blob/main/phases/phase-1/02-processing-architectures/02-processing-architectures.ipynb)

| Notebook | Level | Prerequisites |
|---|---|---|
| [02-processing-architectures.ipynb](02-processing-architectures.ipynb) | Intermediate | [01 · Data Foundations & Data Types](../01-data-foundations/) |

## What you will be able to do

- Choose batch, micro-batch, or streaming based on business latency and complexity.
- Explain event time, processing time, state, windows, and late data.
- Simulate incremental processing with state and idempotent event handling.
- Reason about throughput, partitions, backpressure, delivery semantics, and recovery.
- Translate a business SLA into an architecture decision.

## Contents

1. Environment & events
2. Processing models at a glance
3. Latency, throughput, and freshness are different
4. Event time vs processing time
5. Windowing: make infinite streams computable
6. Stateful processing
7. Idempotency and duplicates
8. Partitions, ordering, and keys
9. Backpressure and capacity
10. Architecture selection framework

**Previous:** [01 · Data Foundations & Data Types](../01-data-foundations/)
