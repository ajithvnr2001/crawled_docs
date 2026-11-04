---
url: https://www.sarvam.ai/blogs/sarvam-prism/
title: Sarvam Prism: a decision model built on Sarvam 105B | Sarvam AI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:04.103037+00:00
---

# Sarvam Prism: a decision model built on Sarvam 105B | Sarvam AI

> Source: https://www.sarvam.ai/blogs/sarvam-prism/

  1. [ Blog ](https://www.sarvam.ai/blogs)
  2. /
  3. [Research](https://www.sarvam.ai/blogs?category=Research)



# Introducing Sarvam Prism

![Introducing Sarvam Prism](https://assets.sarvam.ai/tr:w-1280,q-90,f-auto,c-at_max,dpr-auto/images/03117ysv/production/9de24f0346149d6c43848c8d4bb5b2611badf37a-1535x1025.png?rect=0,30,1535,768)

Nov 3, 20268 min read

Share

Nov 3, 2026·8 min read

Share

Today we are releasing Sarvam Prism, a System One decision model built on Sarvam 105B.   
  
Typeface created this category last month and named their Jev model after Kahneman’s System One thinking, the fast and intuitive mode of judgement that handles most of what people decide in a day. Much of work in an enterprise is a sequence of such decisions, and well calibrated decision models fit neatly into these workflows.

**Best-in-class accuracy & speed:** Prism sets a new point on the Pareto frontier of accuracy and speed among the 25 decision models we tested. The model scores 71.8 while responding in just 44 ms on B200 GPU, the highest-scoring model under 100 ms across the 25 models we tested, averaged over three indices. We believe System One models improve with scale and benefit from mixture-of-expert architecture trade-offs, hence Prism is trained on the Sarvam 105B-10B base.

**Calibration enterprises can trust:** For an enterprise to automate a workflow, it has to trust the model’s confidence on its output. Prism’s errors is always within its confidence bounds and its answer is not affected by the order in which options are presented. 

**Make it your own:** Every enterprise has its own way of making decisions, shaped by its data and outcomes of those decisions. We are releasing Prism with open weights so that enterprises can train this calibrated base on their own data and run it on their own infrastructure.

## Accurate and fast

We ran Prism and 24 other decision models through three indices ourselves, on the same benchmarks. We timed every model we could run on the same hardware (B200) using the bundled inference code.

### Accurate and fast

Average score across three indices against median response time, 25 decision models

  * Sarvam Prism
  * Timed by us
  * API-only (reported time)
  * Best score at each response time



Average score ↑

58

62

66

70

74

78

0

50

100

150

200

250

300

Pareto frontier

mammoth-1

GLiDE 1.2

elephant-1

d3-ultra

Torchcast-27B

Clef

OneJev-9B

Jev 1.14

Microsoft-Decision-1

KnowLine-35B

Sarvam Prism 71.8

Median response time per request (ms) →

Sarvam Prism: 71.8 at 44 ms

Average score across three indices and median response time, by model * Publicly reported response time; these models are API-only.Model| Average| Jev| Artificial Analysis| Indian languages| Response time (ms)  
---|---|---|---|---|---  
mammoth-1| 75.2| 75.3| 70.2| 80.1| 284  
GLiDE 1.2| 73.2| 72.0| 68.1| 79.4| 116  
Sarvam Prism| 71.8| 67.0| 65.9| 82.5| 44  
elephant-1| 71.3| 72.2| 67.6| 74.0| 145  
StartLux-27B| 70.8| 72.9| 61.5| 78.1| 117  
KnowLine-35B| 70.8| 70.7| 59.2| 82.6| 50  
d3-ultra| 70.3| 71.6| 62.8| 76.4| 229  
KnowLine-26B| 69.1| 68.2| 57.6| 81.4| 63  
AutoTrust-JEV-27B| 68.5| 67.3| 60.7| 77.6| 72  
OneJev-27B| 68.4| 69.6| 58.3| 77.2| 27  
H2O-Lightning-31B| 68.2| 67.9| 59.9| 76.7| 46  
Perplexity Decider v1.2| 68.0| 67.7| 61.2| 75.0| 117  
d3| 66.9| 65.5| 60.3| 75.0| 115  
Torchcast-27B| 66.5| 65.1| 59.6| 74.8| 32  
StartLux-9B| 66.2| 70.0| 58.8| 69.8| 60  
VisionJEV| 65.3| 66.4| 57.3| 72.3| 117  
Jev 1.14| 64.5| 60.7| 61.9| 70.8| 196*  
Amos 1 large| 63.4| 64.9| 55.5| 69.7| 121  
StartLux-4B| 63.3| 67.8| 58.4| 63.7| 60  
KnowLine-4B| 63.1| 66.8| 57.0| 65.6| 43  
OneJev-9B| 62.8| 65.3| 53.4| 69.6| 10  
Clef| 62.6| 61.7| 54.8| 71.2| 222  
Microsoft-Decision-1| 61.1| 57.8| 55.6| 70.0| 85*  
Perplexity Decider Flash| 60.3| 60.1| 58.4| 62.4| 62  
Clef-Flash| 58.1| 56.2| 52.1| 66.0| 162  
  
Up and to the left is better. Response time is the median per request on one NVIDIA B200 GPU.

### Scores on each index

Each index and their average, with median response time (higher is better)

  * Sarvam Prism (44 ms)
  * Perplexity Decider v1.2 (117 ms)
  * Jev 1.14 (196 ms*)
  * Clef (222 ms)
  * Microsoft-Decision-1 (85 ms*)



Jev Decision IndexSarvam Prism

67.0

Perplexity Decider v1.2

67.7

Jev 1.14

60.7

Clef

61.7

Microsoft-Decision-1

57.8

Artificial Analysis (ours)Sarvam Prism

65.9

Perplexity Decider v1.2

61.2

Jev 1.14

61.9

Clef

54.8

Microsoft-Decision-1

55.6

Indian languagesSarvam Prism

82.5

Perplexity Decider v1.2

75.0

Jev 1.14

70.8

Clef

71.2

Microsoft-Decision-1

70.0

AverageSarvam Prism

71.8

Perplexity Decider v1.2

68.0

Jev 1.14

64.5

Clef

62.6

Microsoft-Decision-1

61.1

405060708090

Score, axis starts at 40

Scores on each index and their average, by modelIndex| Sarvam Prism| Perplexity Decider v1.2| Jev 1.14| Clef| Microsoft-Decision-1  
---|---|---|---|---|---  
Jev Decision Index| 67.0| 67.7| 60.7| 61.7| 57.8  
Artificial Analysis (ours)| 65.9| 61.2| 61.9| 54.8| 55.6  
Indian languages| 82.5| 75.0| 70.8| 71.2| 70.0  
Average| 71.8| 68.0| 64.5| 62.6| 61.1  
  
* Publicly reported response time; these models are API-only.

The score averages three indices. The first is the [![](https://www.google.com/s2/favicons?domain=huggingface.co&sz=32)Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index), 37 public benchmarks. The second is our recreation of the Artificial Analysis Decision Index, where we replaced its private knowledge test with curated hard questions that include an “I don’t know” option. The third is an internal Indian-language benchmark. Response time is the median over 1,000 requests sent one at a time, with each model running its developers’ own inference code. Jev 1.14 and Microsoft-Decision-1 are available only through an API, so we plot their reported times (196 ms and 85 ms). Measured from our cluster, they took 431 ms and 533 ms respectively.

Prism has the highest average score of any model that answers in under 100 ms. A few models score higher overall, but they take between two and six times as long to respond. Prism's strongest results are on the hard questions of our Artificial Analysis recreation, which reward a model for saying "I don't know" rather than guessing due to its calibrated decisions. On Indian languages it performs on par or better with the best models we tested.

## Confidence you can trust

An enterprise automates a decision by acting on it only above a confidence threshold. This is safe only if the confidence output is calibrated which means its error rate should be lower than the model’s expected error rate. We evaluated calibration on public benchmarks from the Jev Decision Index and our internal Indian-language benchmark.

### Confidence you can trust

Expected vs actual mistakes on answers given with at least 90% confidence (lower is better)

50% confidence70% confidence90% confidence95% confidence

  * Mistakes the model expected
  * Actual: Sarvam Prism
  * Actual: no more than expected
  * Actual: more than expected (×N)



English

Sarvam Prism

3.3

2.2

Clef

2.8

2.3

Perplexity Decider

1.4

2.0×1.5

Microsoft-Decision-1

1.7

3.1×1.8

Jev 1.14

1.3

3.5×2.7

0%1%2%3%4%5%

Mistakes (% of confident answers)

Indian languages

Sarvam Prism

5.4

4.4

Clef

3.9

15.3×3.9

Perplexity Decider

3.0

8.1×2.7

Microsoft-Decision-1

3.0

10.1×3.3

Jev 1.14

3.4

16.1×4.8

0%5%10%15%20%

Mistakes (% of confident answers)

Expected vs actual mistakes at 90% confidence or moreModel| English: expected| English: actual| Indian: expected| Indian: actual  
---|---|---|---|---  
Sarvam Prism| 3.3%| 2.2%| 5.4%| 4.4%  
Clef| 2.8%| 2.3%| 3.9%| 15.3%  
Perplexity Decider| 1.4%| 2.0%| 3.0%| 8.1%  
Microsoft-Decision-1| 1.7%| 3.1%| 3.0%| 10.1%  
Jev 1.14| 1.3%| 3.5%| 3.4%| 16.1%  
  
English: 37 public benchmarks, 226,088 questions. Indian languages: the same benchmarks in 10 Indian languages and Hinglish, 20,108 questions.

**Prism makes fewer errors than its confidence scores predict, across every threshold we tested from 50% to 95%, in English and Indian languages.** For English answers at 90% confidence or higher, Prism predicts 3.3% errors and makes 2.2%. Clef is close, predicting 2.8% and making 2.3%. Perplexity Decider, Microsoft-Decision-1 and Jev 1.14 underestimate their errors by factors of 1.5, 1.8 and 2.7, respectively.

In Indian languages, Prism predicts 5.4% errors and makes 4.4%. The other models make 2.7 to 4.8 times as many errors as their confidence scores predict.

## Same answer, any order

Changing the order of options can change a model’s answer. We tested whether this happened with Prism across 2,000 questions. We ran the questions four times with shuffled options and four times without shuffling. Prism’s answers stayed the same across every shuffle, with no extra computation or loss in accuracy.

### Same answer, any order

Share of 2,000 questions whose answer changes (lower is better)

  * Options shuffled into four orders
  * Same request re-sent four times
  * Sarvam Prism



Sarvam Prism, fixed order

0.0%

0.0%

Clef

0.1%

0.0%

Sarvam Prism, options as sent

4.0%

0.0%

Microsoft-Decision-1

4.8%

4.8%

mammoth-1

8.8%

0.0%

GLiDE 1.2

8.9%

0.0%

Perplexity Decider v1.2

10.3%

0.0%

Jev 1.14

12.3%

5.6%

0%5%10%15%

Questions whose answer changes (%)

Share of questions whose answer changes, by modelModel| Shuffled| 95% interval| Re-sent  
---|---|---|---  
Sarvam Prism, fixed order| 0.0%| 0 to 0.2%| 0.0%  
Clef| 0.1%| 0 to 0.4%| 0.0%  
Sarvam Prism, options as sent| 4.0%| 3.3 to 5%| 0.0%  
Microsoft-Decision-1| 4.8%| 3.9 to 5.8%| 4.8%  
mammoth-1| 8.8%| 7.6 to 10.1%| 0.0%  
GLiDE 1.2| 8.9%| 7.7 to 10.2%| 0.0%  
Perplexity Decider v1.2| 10.3%| 9 to 11.7%| 0.0%  
Jev 1.14| 12.3%| 11 to 13.9%| 5.6%  
  
Perplexity Decider, GLiDE 1.2 and mammoth-1 give the same answer to the same request, but they change 9-10% of answers when the options are shuffled. Jev 1.14 changes 5.6% of answers when nothing changes and 12.3% when shuffled. Prism, reading options in the order sent, gives the same answer to the same request and changes 4.0% when shuffled. Prism closes that gap by putting the options into one fixed order before scoring, whatever order they arrive in, and returning each probability under the original option name. With that step, it changes 0 of 2,000 answers.

We’ve tested Prism on real-world use-cases like speech to speech harness, trace evaluations, prompt injections guardrails, intent routing for customer support, model routing, and document intelligence. 

We’re sharing some early benchmarks, and will be releasing more over time. 

## Agent trace evals

Agent work needs checking, both for whether the task succeeded and for whether the run needs a person to review it. We used three sets of recorded runs. AgentRewardBench contains web-agent runs on AssistantBench, VisualWebArena, WebArena and WorkArena, labelled by experts. τ-bench contains customer-service conversations, labelled by whether the task was completed. Who&When and TRAIL contain failed runs, labelled with the step and the agent responsible. All five models were scored on the same 700 runs (1,770 questions).

Each answer is checked against a known correct label, never another AI model's judgement. For whether a task succeeded or needs review, the labels come from human experts who reviewed each web-agent run (AgentRewardBench) or from the environment's own automatic check of the final result (τ-bench). For which agent caused a failure, human annotators marked the responsible agent in each failed run (Who&When, TRAIL).

### Judging agent runs

Accuracy judging 700 recorded agent runs (higher is better)

  * Sarvam Prism
  * Clef
  * Jev 1.14
  * Microsoft-Decision-1
  * Claude Haiku 5.5



Did the task succeed?Sarvam Prism

75.0%

Clef

71.6%

Jev 1.14

71.8%

Microsoft-Decision-1

71.3%

Claude Haiku 5.5

66.0%

Does the run need human review?Sarvam Prism

86.4%

Clef

80.4%

Jev 1.14

81.9%

Microsoft-Decision-1

83.4%

Claude Haiku 5.5

77.9%

Which agent caused the failure?Sarvam Prism

69.6%

Clef

60.9%

Jev 1.14

65.2%

Microsoft-Decision-1

45.7%

Claude Haiku 5.5

37.0%

All questionsSarvam Prism

78.5%

Clef

76.4%

Jev 1.14

76.4%

Microsoft-Decision-1

75.7%

Claude Haiku 5.5

70.7%

0%25%50%75%100%

Accuracy (%)

Agent-run judging accuracy, by modelQuestion| Sarvam Prism| Clef| Jev 1.14| Microsoft-Decision-1| Claude Haiku 5.5  
---|---|---|---|---|---  
Did the task succeed?| 75.0%| 71.6%| 71.8%| 71.3%| 66.0%  
Does the run need human review?| 86.4%| 80.4%| 81.9%| 83.4%| 77.9%  
Which agent caused the failure?| 69.6%| 60.9%| 65.2%| 45.7%| 37.0%  
All questions| 78.5%| 76.4%| 76.4%| 75.7%| 70.7%  
  
All questions also includes repeated loops, side effects, the step where a run first went wrong, and the type of error.

Prism scores a full agent run in about half a second on a single GPU. It reads the trace once and scores all five questions together. Claude Haiku 5.5, called through its API, takes a median 2.5 seconds per run and costs $0.64 per 1,000 runs. That makes Prism faster and cheaper alternative. Prism can also handle up to 131,072 tokens per question, so long traces can be evaluated in one pass rather than split into chunks.

## Agent security guardrails

This test uses an internal benchmark of 5,517 questions across nine tasks, built from vulnerabilities published since July 2026. Models are asked to classify whether the artifact is part of a phishing campaign, if an incoming prompt is trying to jailbreak and classifying attack types into MITRE frameworks.

We will expand this eval set and release it publicly in the coming weeks. 

### Security decisions

Accuracy on our internal cybersecurity benchmark, 5,517 questions (higher is better)

Sarvam Prism

89.0%

Clef

84.5%

Jev 1.14

78.6%

Microsoft-Decision-1

76.1%

50%60%70%80%90%100%

Accuracy (%), axis starts at 50%

Accuracy on the internal cybersecurity benchmark, by modelModel| Accuracy  
---|---  
Sarvam Prism| 89.0%  
Clef| 84.5%  
Jev 1.14| 78.6%  
Microsoft-Decision-1| 76.1%  
  
**Prism scores 89.0%, ahead of Clef (84.5%), Jev 1.14 (78.6%) and Microsoft-Decision-1 (76.1%).**

##  How it works

Prism is a LoRA fine-tune of Sarvam 105B. It takes the state, question and options as input and processes them in a single forward pass. A small scoring head returns a probability for each option, with no token-by-token generation.

### Training objective

Prism learns a probability distribution over the options through two equally weighted loss terms. The first is cross-entropy with 5% label smoothing, which discourages complete certainty. The second is a Brier loss, which measures squared probability error and makes confident mistakes costly. We attribute Prism’s calibration to these two training choices.

### The attention mask

The state and question form one block that is read in both directions. Each option sees that block and itself but never the other options, and every option starts from the same position. Only the answer token sees everything, and that is where the options are compared. Isolating the options makes each judgement independent. Reading both directions within a block adds about 3 points on the Jev Decision Index. 

### Attention Visibility Across Tokens

Three attention masks for one question with two options

  * State
  * Question
  * Option A
  * Option B
  * Answer
  * Blocked



Standard: left to right

SQABAns

SQABAns

Block, left to right inside

SQABAns

SQABAns

Prism: block, both directions

SQABAns

SQABAns

Rows: the word doing the reading. Columns: the words it can see, coloured by what they are. S = state, Q = question, A and B = two options, Ans = answer token.

Middle to right: about +3 points on the Jev Decision Index.

The state and question block is fully bidirectional, so a standard unmasked kernel computes it exactly. Only the thin strip of option and answer rows needs the custom mask. Splitting the computation this way makes attention 2.6 times faster on requests over 2048 tokens. FP8 changed the Jev Decision Index score by 0.01 points. In total, these steps make Prism 15.1 times faster.

### One attention mask, computed in two pieces

Prism's mask for one question with two options

  * Fast kernel, no mask
  * Masked kernel, only these rows
  * Blocked



StateQABAns

StateQABAns

State + question: a full squareFast kernel, no mask needed

Options + answer: a thin stripMasked kernel, only these rows

Rows: the word doing the reading. Columns: the words it can see. Q = question, A and B = two options, Ans = answer token.

## Making it fast

Prism started at 664 ms per median request, running in 16-bit precision across two B200 GPUs. We converted the weights to FP8 so the model fits on a single GPU, ran all 128 experts in one grouped kernel, captured the forward pass as a CUDA Graph, folded the FP8 conversion into the expert kernels, and merged the fine-tuning adapter into the model weights. Together, these bring the median request to 44 ms, 15× faster than where we started, with no drop in accuracy.

## Using Prism

Prism’s weights are on [![](https://www.google.com/s2/favicons?domain=huggingface.co&sz=32)Hugging Face](https://huggingface.co/sarvam/prism) under the [![](https://www.google.com/s2/favicons?domain=www.apache.org&sz=32)Apache 2.0 licence](https://www.apache.org/licenses/LICENSE-2.0). Prism runs in FP8 on one GPU with at least 120 GB of memory. It is also available on the Sarvam API at [![](https://www.google.com/s2/favicons?domain=indus.sarvam.ai&sz=32)Sarvam Indus](https://indus.sarvam.ai/model-catalogue/sarvam-prism). Each request takes a state, a question and any number of options that fit within the context window, and returns a probability for each option. The documentation is available [![](https://www.google.com/s2/favicons?domain=docs.sarvam.ai&sz=32)here](https://docs.sarvam.ai/api/token-factory/models/sarvam-prism). 

##  Read More 

[![Sarvam and HQ IDS establish joint framework for AI adoption across the Army, Navy and Air Force](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/a3a5f8505ad6cab5c30842e00317c560050ae623-3676x2214.png)Oct 27, 2026·AnnouncementSarvam and HQ IDS establish joint framework for AI adoption across the Army, Navy and Air Force](https://www.sarvam.ai/blogs/sarvam-hq-ids-mou)[![How we built the knowledge fabric for enterprise agents](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/5e43c24fcd35835f3ec68d2f5013267e046e3dfc-2160x1360.png)Oct 26, 2026·ResearchHow we built the knowledge fabric for enterprise agents](https://www.sarvam.ai/blogs/knowledge-fabric-enterprise-agents)[![Introducing Bulbul V4 Flash](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/f1489eb4cc72109b73bcfff300d89894cdb1d645-3840x2160.png)Oct 13, 2026·ResearchIntroducing Bulbul V4 Flash](https://www.sarvam.ai/blogs/bulbul-v4-flash)

Curious what else we're building? Explore our APIs and start creating. 

Curious what else we're building?

Explore our APIs and start creating.

[Get Started](https://indus.sarvam.ai)
