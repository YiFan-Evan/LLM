# DeriEval: A Framework for Evaluating and Improving the Derivation Capability of Large Language Models

To protect our research work, we will not release the full code of the DeriEval framework at this stage (including components such as knowledge generation, dataset construction, executor invocation, and result analysis). At this time, we are only making part of the model output files and partial evaluation code available. Once our work is accepted, all the code will be released.

## RQ1

---

Does DeriEval assessment honestly reflect the model’s derivation capability?

Comparison table of results in DeriEval and other frameworks:

[//]: # (Robust	Ours Column Adding	sqa	67	76.1111 wikisql	82.5	95.3608 wtq	74.5	82.4742 Column Masking	sqa	54	61.6667 wikisql	87	68.75 wtq	73.5	77.6471 Column Order Shuffling	sqa	60.5	56.3218 wikisql	94.5	95.9391 wtq	75	72.0207 Row Order Shuffling	sqa	11	11.4943 wikisql	94	93.9086 wtq	57.5	58.8542)

| Transformation | Dataset | RobuT | DeriEval | Transformation | Dataset |  PromptBench | DeriEval |
| --- | --- |-------| --- | --- | --- | --- | --- |
| Column Adding | SQA | 67    | 76.1111 | CheckList | SST-2 | 0.967 | 0.954901961 |
| | WikiSQL | 82.5  | 95.3608 | | QQP | 0.995 | 0.984313725 |
| | WTQ | 74.5  | 82.4742 | | MRPC | 0.999 | 0.987254902 |
| Column Masking | SQA | 54    | 61.6667 | StressTest | SST-2 | 1 | 0.95 |
| | WikiSQL | 87    | 68.75 | | QQP | 1 | 1 |
| | WTQ | 73.5  | 77.6471 | | MRPC | 0.95 | 0.9625 |
| Column Order Shuffling | SQA | 60.5  | 56.3218 | TextBugger | SST-2 | 1 | 0.945833333 |
| | WikiSQL | 94.5  | 95.9391 | | QQP | 0.997619048 | 0.984473684 |
| | WTQ | 75    | 72.0207 | | MRPC | 0.998134328 | 0.988148148 |
| Row Order Shuffling | SQA | 11    | 11.4943 | DeepWordBug | SST-2 | 0.940909091 | 0.934821429 |
| | WikiSQL | 94    | 93.9086 | | QQP | 0.9953125 | 0.826153846 |
| | WTQ | 57.5  | 58.8542 | | MRPC | 0.998461538 | 0.975 |

[//]: # (Robust	Ours Column Adding	sqa	67	76.1111 wikisql	82.5	95.3608 wtq	74.5	82.4742 Column Masking	sqa	54	61.6667 wikisql	87	68.75 wtq	73.5	77.6471 Column Order Shuffling	sqa	60.5	56.3218 wikisql	94.5	95.9391 wtq	75	72.0207 Row Order Shuffling	sqa	11	11.4943 wikisql	94	93.9086 wtq	57.5	58.8542)



## RQ2

---

Can large models understand and apply derivation relation during problem solving?

Derivation capability performance of different models on various tasks:

[//]: # (choice	invariant	logic	math	algrithm	space O1-mini	0.71151591	0.70075377	0.88650754	0.70697486	0.73740369	0.9 Claude-3.5	0.47042088	0.49833333	0.60273504	0.55833333	0.47166667	0.385 GPT-4o	0.72650754	0.53	0.41704144	0.59603651	0.51888889	0.13 Kimi	0.61	0.485	0.34595446	0.55666667	0.42666667	0.20833333 Qwen	0.56666667	0.495	0.35321984	0.52896142	0.36731156	0.11166667 Gpt-3.5-turbo	0.475	0.46	0.16687573	0.17755345	0.29666667	0.08333333)

| Model |  Choice | Invariant | Logic | Math | Algorithm | Space |
| --- | --- | --- | --- | --- | --- | --- |
| O1-mini | 0.71151591 | 0.70075377 | 0.88650754 | 0.70697486 | 0.73740369 | 0.9 |
| Claude-3.5 | 0.47042088 | 0.49833333 | 0.60273504 | 0.55833333 | 0.47166667 | 0.385 |
| GPT-4o | 0.72650754 | 0.53 | 0.41704144 | 0.59603651 | 0.51888889 | 0.13 |
| Kimi | 0.61 | 0.485 | 0.34595446 | 0.55666667 | 0.42666667 | 0.20833333 |
| Qwen | 0.56666667 | 0.495 | 0.35321984 | 0.52896142 | 0.36731156 | 0.11166667 |
| Gpt-3.5-turbo | 0.475 | 0.46 | 0.16687573 | 0.17755345 | 0.29666667 | 0.08333333 |


## RQ3

---

Can prompt engineering techniques effectively enhance the derivation capability performance of large models?

Improvement of GPT-4o under different prompt engineering methods:

[//]: # (knowledge	one_shot	five_shot	CoT	back	anology avg-1	0.18	0.1175	0.184166667	0.056388889	0.050833333	0.050833333 avg-2	0.19759293	0.081763053	0.171801367	0.111338216	0.076365261	0.020734043 avg-3	0.078943054	-0.035358777	0.025177622	0.137637939	0.090544343	0.005336352 avgt	0.152178661	0.054634759	0.127048552	0.101788348	0.072580979	0.025634576)

| Case | KC   | One-shot | Five-shot | CoT | Back-step   | Analogy |
|------|------| --- | --- | --- |-------------| --- |
| 1    | 0.18 | 0.1175 | 0.184166667 | 0.056388889 | 0.050833333 | 0.050833333 |
| 2    | 0.19759293 | 0.081763053 | 0.171801367 | 0.111338216 | 0.076365261 | 0.020734043 |
| 3    | 0.078943054 | -0.035358777 | 0.025177622 | 0.137637939 | 0.090544343 | 0.005336352 |
| Avg  | 0.152178661 | 0.054634759 | 0.127048552 | 0.101788348 | 0.072580979 | 0.025634576 |
