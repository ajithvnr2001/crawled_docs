---
url: https://www.sarvam.ai/blogs/knowledge-fabric-enterprise-agents/
title: Knowledge fabric for enterprise AI agents | Sarvam AI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T16:23:04.877188+00:00
---

# Knowledge fabric for enterprise AI agents | Sarvam AI

> Source: https://www.sarvam.ai/blogs/knowledge-fabric-enterprise-agents/

  1. [ Blog ](https://www.sarvam.ai/blogs)
  2. /
  3. [Research](https://www.sarvam.ai/blogs?category=Research)



# How we built the knowledge fabric for enterprise agents

![How we built the knowledge fabric for enterprise agents](https://assets.sarvam.ai/tr:w-1280,q-90,f-auto,c-at_max,dpr-auto/images/03117ysv/production/5e43c24fcd35835f3ec68d2f5013267e046e3dfc-2160x1360.png)

Oct 26, 202611 min read

Share

Oct 26, 2026·11 min read

Share

## Making fragmented enterprise data agent-queryable

Enterprise AI agents are only as useful as the context provided to them. The knowledge required to answer complex queries is scattered across documents, databases, and the heads of domain experts who know how it all fits together, and almost none of it is organized for an AI agent to actually use.

Consider a simple banking query: A customer wants a credit card with zero forex markup, airport lounge access, and a credit limit of up to ₹10 lakh. If multiple cards qualify, they want the one with the lowest annual fee.

An experienced relationship manager answers this effortlessly. Years on the job have given them a mental model of the bank's portfolio. They know which sources contain the relevant terms, how eligibility rules interact, and which fee schedules override others.

When these data sources are made available to agents, that accumulated understanding does not carry through. Since the information is not organized, with each query, the agent retrieves a handful of passages and tries to piece together the relevant products, rules, and exceptions. It can miss important details, and on the next question, much of the work starts again from scratch.

Sarvam's knowledge fabric does this work ahead of time, transforming an organization's documents and data into a structured knowledge layer that agents can query, navigate, and cite to answer complex questions. We have spent the last few months building the fabric with early customers and testing it on public benchmarks.

On Harvey's [![](https://www.google.com/s2/favicons?domain=www.harvey.ai&sz=32)LAB benchmark](https://www.harvey.ai/blog/legal-agent-bench-law-firm-knowledge), with GLM 5.3 as the agent model, answers met 84.2% of expert rubric criteria, up from 55.1% with agentic RAG, while average task cost fell from $0.64 to $0.28, outperforming Harvey's own harness reported at 79.1% for GPT-5.6 Sol and 71.7% for Opus 4.8.

On Sierra's [![](https://www.google.com/s2/favicons?domain=sierra.ai&sz=32)tau-knowledge](https://sierra.ai/blog/tau-knowledge) banking benchmark, the fabric matched baseline accuracy with 64% fewer tokens, with GLM 5.2 running both setups.

In this post, we go deeper into the architecture behind the knowledge fabric, why we designed it the way we did and what we learned from building and testing it in practice.

## Why traditional search falls short

Most enterprise search systems today are built on retrieval-augmented generation (RAG), where documents are split into small chunks and indexed for search. When a question arrives, the system retrieves the most relevant chunks and passes them to the model as context.

Better embeddings, chunking strategies and rerankers can improve retrieval quality, but retrieving relevant passages is not the same as having a structured understanding of the underlying information. This creates two problems.

  1. **Important context gets lost.** Chunking can strip a passage of the surrounding text or related facts that qualify or substantiate it. The retrieved passage still looks relevant and complete, so the agent can give the wrong answer confidently.
  2. **Answers remain incomplete.** Many questions require aggregating information spread across multiple sources, and the answer is correct only if all relevant information is found. Vector search returns passages closest to the query, but the agent has no reliable way of knowing what else exists or whether it has found everything. It keeps searching without knowing when it is done, repeating this work for every query.



#### Passages lose their context

The agent reads each passage apart from the document it came from.

##### A value loses its label

A value can be separated from its heading, footnote or customer segment.

##### Facts stay separated across files

The agent must infer that two documents describe the same customer or transaction.

#### The agent can't tell if it found everything

Ranked results do not reveal what was missed or when the search is finished.

##### Some matches are found, others are missed

A plausible answer can still omit qualifying records elsewhere in the corpus.

##### The same work repeats for every question

The next query starts without the understanding assembled during the previous one.

## Our approach

We wanted agents to work more like the relationship manager, starting each question with the context already in place and decided to design the knowledge fabric to ingest the documents once, and intelligently compile it into two layers.

The first layer is a knowledge tree, which organises any corpus so that an agent can navigate it, without needing a model of the domain. The second is a domain ontology, which models the entities in a domain and the relationships between them. In our financial products example, the tree would let an agent find and read each product’s terms and conditions, and the ontology would let it filter every card by its features such as forex markup, lounge access and annual fees in a single query.

### A wider agent surface for knowledge retrieval

#### Orient

See what exists and how it connects.

#### Traverse and filter

Follow links, then narrow the set.

#### Aggregate

Count, sum and compare the full set.

#### Search

Find passages by exact term and by meaning.

#### Read

Go from summary to passage to source, and cite it.

## Improving search with knowledge trees

Anyone who has ever used a coding agent has seen how well it can work through a large codebase with the use of filesystem primitives allowing it to access directories, read files, run search and retrieval and improve its understanding of the code. We bring these primitives to an organisation’s data with a knowledge tree.

Building a knowledge tree starts with parsing where we convert every file into markdown using [![](https://www.google.com/s2/favicons?domain=www.sarvam.ai&sz=32)Sarvam Vision 2.1](https://www.sarvam.ai/blogs/sarvam-vision-2-1) for scanned pages, complex layouts, tables and Indic scripts. Each long document then becomes a folder with a short index alongside it. For a 200-page annual report, the index is a single page listing the title, a summary and each section with its page range, allowing the agent to read the index first, pick the section it needs and open only those pages.

We serve the tree over MCP, so any agent can list folders, read indexes, search the corpus, open page ranges and inspect tables. Every citation points back to the passage, image or table row on the source page.

### Layer 1: the knowledge tree

  * Folder with an index
  * Document with a summary
  * Table kept as data
  * Search hit and its place in the tree



To measure the value the tree adds, we compared the tree with flat hybrid retrieval on four public benchmarks, using GLM 5.2 over the same parsed documents in both cases. One agent could only search passages, while the other could also read indexes, move through the document hierarchy and open tables.

Benchmark| Hybrid retrieval| Knowledge-tree navigation  
---|---|---  
BrowseComp-Plus, 830 deep-research questions| 75.5%| 91.3%  
BRIGHT-Pro, 739 reasoning-heavy questions| 84.3%| 90.4%  
FinanceBench, 150 questions over company filings| 82.1%| 88.7%  
OfficeQA Pro, 133 questions over Treasury bulletins| 33.8%| 51.6%  
  
Scroll

Scroll

The gains were largest when an answer needed evidence from several documents or from a table, suggesting that the tree helped the agent reach that material. However, it did not solve completeness. The agent still had to work out which documents described the same thing and whether it had found every relevant record, which is the problem the second layer addresses.

## A domain ontology that agents can query like a database

Some questions are closer to database queries than searches: finding every card with zero forex markup and lounge access requires filtering across the bank’s cards, which an agent can only do reliably if each card’s features are already recorded in a form it can query. The second layer, the domain ontology, provides this structure. It defines the kinds of things a domain contains, the properties each one has and how they relate, and records what every document says in those terms.

We used Harvey's LAB firm-knowledge benchmark that places an agent inside a simulated law firm with 9,288 files covering 266 matters for 46 clients, and gives it 250 requests of the kind a partner might make, to test the knowledge fabric.

One request asks: "Pull all our Capital Markets offerings that were done on a firm-commitment basis, along with the executed underwriting agreements."

Answering it means finding every capital-markets offering, checking how each one was underwritten and working out which documents are executed under underwriting agreements. Those facts are scattered across transaction documents, agreements and matters, so search can find examples but does not guarantee a complete list.

For LAB we defined five entity types: clients, matters, transactions, documents and agreements, where a transaction carries properties such as its kind, status, value and underwriting basis recorded in a document, and relationships connect different entities.

### Layer 2: the domain ontology

#### Client

namesector

has

#### Matter

practice areaopenedclosed

includes

#### Transaction

kindstatusvalueunderwriting

contains

has agreement

Entity type

Property

Relationship

#### Document

typedatedraft or executed

records

#### Agreement

partiesgoverning lawsigned on

With the ontology in place, the agent answered the capital-markets request in three steps:

  1. Listed all 22 capital-markets offerings.
  2. Filtered for firm-commitment offerings and joined them to their executed agreements, leaving 14 that qualified.
  3. Opened the supporting passages and cited each result.



### Finding every firm-commitment offering

Return the executed underwriting agreement for every offering that qualifies.

Browsing

#### Knowledge tree

  * Found
  * Missed
  * False positive
  * Other files



7 of 14

qualifying offerings found

3

false positives

Querying

#### Ontology
    
    
    **find** transactions  **where** kind = capital markets offering    **and** underwriting = firm commitment**follow** has agreement  **where** executed**return** offering, agreement, cited source

One query over typed entities returns the complete set, and every result links back to its source document.

14 of 14

qualifying offerings found

0

false positives

Counts are from the Harvey LAB run. The query is a simplified illustration, and so is where each document sits in the tree.

## Results on Harvey LAB

We ran this benchmark in three configurations: agentic RAG over a flat chunk index, the knowledge tree, and the ontology with the knowledge tree still available.

| Agentic RAG| Knowledge tree| Ontology  
---|---|---|---  
Rubric criteria met| 55.1%| 74.4%| 84.2%  
Tasks fully solved| 72| 92| 109  
Tasks left unanswered| 9| 7| 0  
Tool calls per task| 36.5| 59.2| 14.2  
Tokens per task| 1.80M| 3.79M| 0.86M  
Time per task| 30.0 min| 30.8 min| 8.6 min  
Cost per task| $0.64| $1.18| $0.28  
  
Scroll

Scroll

### The ontology is more accurate and uses fewer tokens

  * Agentic RAG
  * Knowledge tree
  * Ontology



Rubric criteria met

50%

60%

70%

80%

90%

↖ Better

Ontology84.2% · 0.86M tokens · 14.2 calls

Agentic RAG55.1% · 1.8M tokens · 36.5 calls

Knowledge tree74.4% · 3.79M tokens · 59.2 calls

01M2M3M4M

Tokens per task

The knowledge tree improved the criteria pass rate over agentic RAG but that exploration was expensive and used more than twice as many tokens. The ontology improved the criteria pass rate further while bringing token use below the RAG baseline, because filtering and joining happened in the database instead of through repeated reading and reasoning. The ontology-based setup also returned an answer for every task and required less than a quarter of the tool calls used by the tree alone, with the performance gap widening on larger tasks.

## Results on tau-knowledge

We tested the knowledge fabric on [![](https://www.google.com/s2/favicons?domain=sierra.ai&sz=32)Sierra's tau-knowledge benchmark](https://sierra.ai/blog/tau-knowledge) which puts an agent on the support desk of a simulated bank, with 698 documents covering product terms, fees, eligibility rules and internal procedures. Each task needs information from 18.6 documents on average, and the 97 tasks are scored all or nothing, so a single missed fee or eligibility condition fails the whole task.

Across the full benchmark, we integrated the knowledge fabric into Sierra's harness and compared it with Sierra's default retrieval setup, which gives the agent BM25, embedding search and a shell. We ran both in our own environment with GLM 5.2 as the agent model. The agent using the knowledge fabric completed 39 tasks, compared with 38 for the baseline, while using 64% fewer tokens.

### tau-knowledge: the same accuracy with 64% fewer tokens

  * Sierra baseline
  * Knowledge fabric



#### Total tokens across all 97 tasks

288.1M

102.4M64% fewer

#### Tokens per solved task

7.58M

2.62M2.9× fewer

GLM 5.2 as the agent model in both setups, run in Sierra's harness in our own environment.

## Setting up the knowledge fabric

Because it does not depend on a model of the domain, the knowledge tree layer can be built in the background as soon as the files are uploaded. The ontology has to be built for each domain, and agents do most of that work, with domain experts reviewing what they produce.

  * Users define the sources the fabric should draw on, uploading documents and tables and setting up connectors to the systems where the rest of their data lives.
  * Agents draft the domain model from that material, covering its types, relationships, glossary and value lists, and domain experts review and correct it.
  * Agents then compile the documents and tables into the fabric. Data that changes constantly, such as a live transactions database, is queried at runtime, so the source system still decides who can see what.
  * Long-running agents help the fabric keep improving by reviewing the traces and feedback. As new records arrive, agents help extend the ontology incrementally, and when an agent answering a question runs into a gap, such as a record missing a property or two names for the same entity, it proposes a fix.
  * Those proposals, along with any extraction the agents were unsure of, go to the human reviewer. Every change is versioned, and we rerun the domain's evaluation set before an update goes live.



The fabric can run inside an organisation’s own environment, including small air-gapped setups that use smaller models.

Agents & interfaces

Reason, plan and act on the organisation’s context.

  * Chat
  * Voice agents
  * Applications
  * Your own agents



Search

MCP

Cited response

01 · Inputs

#### Raw sources

  * Documents

PDFs, decks, web pages

  * Media

audio, video, images

  * Structured data

spreadsheets, databases, APIs

  * Business systems

CRM, ERP, ticketing

  * Conversations

email, chat, calls




02 · The fabric

#### Knowledge fabric

Domain model

##### Ontology

The business’s vocabulary of types, links and rules, shared by every agent.

Shapes

##### Context graph

Entities

Relationships

Decisions

Precedents

Catalog

Data lineage

Access control

03 · Signals

#### Audit trail

  * Queries and reads
  * Decisions and approvals
  * Corrections
  * Outcomes and feedback
  * Exceptions and failures



Ontology-guided ingestion

Decision traces

Agents & interfaces

Reason, plan and act on the organisation’s context.

  * Chat
  * Voice agents
  * Applications
  * Your own agents



Search

MCP

Cited response

02 · The fabric

#### Knowledge fabric

Domain model

##### Ontology

The business’s vocabulary of types, links and rules, shared by every agent.

Shapes

##### Context graph

Entities

Relationships

Decisions

Precedents

Catalog

Data lineage

Access control

Ontology-guided ingestion

Decision traces

01 · Inputs

#### Raw sources

  * Documents

PDFs, decks, web pages

  * Media

audio, video, images

  * Structured data

spreadsheets, databases, APIs

  * Business systems

CRM, ERP, ticketing

  * Conversations

email, chat, calls




03 · Signals

#### Audit trail

  * Queries and reads
  * Decisions and approvals
  * Corrections
  * Outcomes and feedback
  * Exceptions and failures



## Final thoughts

The biggest lesson from this work is how much an agent's results depend on the substrate it works over. The knowledge fabric gives the agent a more intelligent substrate, where that structure is already in place, much as the relationship manager we started with already knows how the bank's products fit together. Building that substrate once, ahead of time, makes agents more accurate and cheaper to run.

We are excited about what this makes possible: agents that start every task already understanding how an organisation's knowledge fits together and are continuously working to make compilation more accurate and efficient. We are continuing to improve the accuracy and efficiency of compilation by refining the harness that builds the fabric and testing different models at each step.

The next step is memory. The fabric should become more useful as more agents share it, and what one agent learns, whether a correction, a decision or a user's preference, should be available to the rest. We are designing a persistent, shared memory for agents, built on similar primitives. We will be sharing more of what we learn along the way.

## References

  * Harvey, [![](https://www.google.com/s2/favicons?domain=www.harvey.ai&sz=32)LAB: Law Firm Knowledge](https://www.harvey.ai/blog/legal-agent-bench-law-firm-knowledge). The firm-knowledge tasks behind our ontology results: a simulated law firm with 9,288 files and 250 partner-style requests, graded against expert-written rubrics. The corpus, tasks and grader are on [![](https://www.google.com/s2/favicons?domain=github.com&sz=32)GitHub](https://github.com/harveyai/harvey-labs).
  * Sierra, [![](https://www.google.com/s2/favicons?domain=sierra.ai&sz=32)tau-knowledge](https://sierra.ai/blog/tau-knowledge). A customer-support benchmark over a simulated bank's product terms, fees and procedures, where each task is scored all or nothing.
  * [![](https://www.google.com/s2/favicons?domain=github.com&sz=32)BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus). Deep-research questions over a fixed corpus of about 100,000 documents, so retrieval setups can be compared on the same data.
  * [![](https://www.google.com/s2/favicons?domain=github.com&sz=32)BRIGHT-Pro](https://github.com/yale-nlp/Bright-Pro). Retrieval questions where finding the right documents takes reasoning beyond keyword or semantic overlap.
  * [![](https://www.google.com/s2/favicons?domain=github.com&sz=32)FinanceBench](https://github.com/patronus-ai/financebench). Questions over public company filings with verified answers.
  * [![](https://www.google.com/s2/favicons?domain=arxiv.org&sz=32)OfficeQA Pro](https://arxiv.org/abs/2603.08655). Questions over US Treasury bulletins, many of which depend on values in tables.
  * Zhang, Khattab and Kraska, [![](https://www.google.com/s2/favicons?domain=alexzhang13.github.io&sz=32)Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/). A model that calls itself recursively over a long context held in a code environment, so it can read far more than fits in one prompt.
  * Moonshot AI, [![](https://www.google.com/s2/favicons?domain=www.kimi.com&sz=32)Kimi K2.5](https://www.kimi.com/blog/kimi-k2-5.html). A model trained to split a task across up to 100 parallel sub-agents, with strong results on BrowseComp.



##  Read More 

[![Introducing Sarvam Prism](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/9de24f0346149d6c43848c8d4bb5b2611badf37a-1535x1025.png?rect=0,30,1535,768)Nov 3, 2026·ResearchIntroducing Sarvam Prism](https://www.sarvam.ai/blogs/sarvam-prism)[![Sarvam and HQ IDS establish joint framework for AI adoption across the Army, Navy and Air Force](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/a3a5f8505ad6cab5c30842e00317c560050ae623-3676x2214.png)Oct 27, 2026·AnnouncementSarvam and HQ IDS establish joint framework for AI adoption across the Army, Navy and Air Force](https://www.sarvam.ai/blogs/sarvam-hq-ids-mou)[![Introducing Bulbul V4 Flash](https://assets.sarvam.ai/tr:w-800,q-70,f-auto,dpr-auto/images/03117ysv/production/f1489eb4cc72109b73bcfff300d89894cdb1d645-3840x2160.png)Oct 13, 2026·ResearchIntroducing Bulbul V4 Flash](https://www.sarvam.ai/blogs/bulbul-v4-flash)

Curious what else we're building? Explore our APIs and start creating. 

Curious what else we're building?

Explore our APIs and start creating.

[Get Started](https://indus.sarvam.ai)
