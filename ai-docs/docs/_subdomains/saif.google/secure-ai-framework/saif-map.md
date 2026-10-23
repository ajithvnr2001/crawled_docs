---
url: https://saif.google/secure-ai-framework/saif-map/
title: SAIF Map of AI Risks and Controls - SAIF
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:20:56.781268+00:00
---

# SAIF Map of AI Risks and Controls - SAIF

> Source: https://saif.google/secure-ai-framework/saif-map/

## SAIF **Risk Map**

AI risks are everywhere. Take the tour to see how different risks are introduced, exploited, and mitigated throughout the AI development process.

Start tour 

### For each AI risk, this tour shows:

  * #### Introduced

The components where systems, processes, or people could introduce a risk into the model development lifecycle.

  * #### Exposed

The components where security practitioners, systems, or users can recognize or encounter risks that have been introduced.

  * #### Mitigated

The components where organizations can take steps to mitigate or remediate a risk.




Use the “next” button to take the entire tour, or jump to a specific risk with the top navigation bar.

### Data Poisoning

#### Introduced

Data Poisoning poses a risk throughout the data lifecycle. Data can be poisoned before it is ingested, during processing or training, or while the data is in storage. This makes it a critical concern across all data handling systems.

#### Exposed

Data Poisoning is exposed during development in the data filtering and processing steps or the training, tuning, and evaluation stages. It’s also exposed in the model itself, when it produces inaccurate results, malicious outputs, or unexpected behavior.

#### Mitigated

Proactive mitigation against Data Poisoning happens early in development. This includes data sanitization, secure systems and access controls, and mechanisms to ensure data and model integrity.

### Unauthorized Training Data

#### Introduced

Unauthorized Training Data is introduced early in development if not properly filtered out during data ingestion, data processing, and model evaluation during training.

#### Exposed

The risk is exposed during development, through data filtering and processing steps or training, tuning, and evaluation. It is also exposed during model use, when the model may produce inferences based on data it shouldn’t have access to.

#### Mitigated

Mitigations for this risk start early, with careful data selection, filtering, and evaluation during training to catch any lingering issues.

### Model Source Tampering

#### Introduced

Model Source Tampering is a risk that’s introduced when model code, training frameworks, or model weights are not hardened against supply chain attacks and tampering.

#### Exposed

This risk is exposed in the model frameworks and code components, if the tampering is discovered at the source. Otherwise, the risk is exposed in the model, through its modified behavior during use.

#### Mitigated

Safeguard against this risk by employing robust access controls and integrity management for model code and weights, comprehensive inventory tracking to monitor and verify models and code throughout systems, and secure-by-default infrastructure tools.

### Excessive Data Handling

#### Introduced

The risk of Excessive Data Handling is introduced when data sources lack proper metadata tagging for effective management or when model and data storage infrastructure isn't designed to address data lifecycle concerns.

#### Exposed

This risk is exposed in both the model and in storage components, leading to data retention or usage beyond permissible limits.

#### Mitigated

Mitigate this risk with data filtering and processing, along with automation for data archiving, deletion, or issuing alerts for models trained with outdated data.

### Model Exfiltration

#### Introduced

Model Exfiltration is introduced when storage or serving infrastructure lacks adequate security against attacks.

#### Exposed

This risk is exposed if attackers target vulnerabilities in serving or storage systems to steal model code or weights.

#### Mitigated

Mitigate this risk by hardening both storage and serving systems to prevent unauthorized access and protect against model theft.

### Model Deployment Tampering

#### Introduced

The risk of Model Deployment Tampering is introduced within the model serving components, specifically when the serving infrastructure is vulnerable to manipulation.

#### Exposed

This risk is exposed if attackers tamper with production models within the model serving component.

#### Mitigated

Mitigation focuses on hardening the model serving infrastructure with secure-by-default tooling.

### Denial of ML Service

#### Introduced

The risk of Denial of ML Service arises in the application component when a model is exposed to excessive access. Additionally, some types of Denial of ML Service (such as energy-latency attacks) stem from the fundamental functioning of the model itself.

#### Exposed

This risk is exposed during application use, when attackers either overwhelm the model with excessive calls or use carefully crafted "sponge examples" that take advantage of model weaknesses to degrade performance.

#### Mitigated

Mitigation occurs at the application level, using input filtering and employing rate limiting and load balancing to control the volume of calls to the model.

### Model Reverse Engineering

#### Introduced

The risk of Model Reverse Engineering arises within the application component when excessive access to the model is granted for queries.

#### Exposed

This risk is exposed if attackers send excessive queries to the model and leverage the responses to reverse engineer its weights.

#### Mitigated

Mitigate this risk with rate limiting within the application API or using other protective measures at the application level to prevent excessive model access.

### Insecure Integrated Component

#### Introduced

The risk of Insecure Integrated Components is introduced in the application and agent/plugin components, specifically through integrations that permit manipulation of inputs or outputs.

#### Exposed

This risk is exposed within the application or agent/plugin components, if attackers exploit the security vulnerability to gain unauthorized model access, insert malicious code, or compromise systems.

#### Mitigated

Mitigate this risk by addressing vulnerabilities directly within the application and agent/plugin components, and by enforcing strict permissions for agents and plugins.

### Prompt Injection

#### Introduced

Prompt Injection is an inherent risk in AI models, because of the potential confusion between instructions and input data.

#### Exposed

This risk is exposed during model usage, specifically within the model input handling and model components. Attackers may inject commands within prompts, potentially causing unintended model actions.

#### Mitigated

Mitigation involves robust filtering and processing of inputs and outputs. Additionally, thorough training, tuning, and evaluation processes help fortify the model against prompt injection attacks.

### Model Evasion

#### Introduced

Model Evasion is an inherent risk in AI models, as their core functionality relies on distinguishing between inputs to trigger specific inferences.

#### Exposed

This risk is exposed within the model component itself during its usage.

#### Mitigated

Mitigation occurs in the training, tuning, and evaluation phases, where robust models can be developed using extensive and diverse data to better withstand such attacks.

### Sensitive Data Disclosure

#### Introduced

The risk of Sensitive Data Disclosure is introduced in several components. It can also be inherent to models due to their non-deterministic nature. This risk is amplified by data handling practices that fail to filter sensitive information, or by training processes that neglect to evaluate the model's potential for disclosure. In agentic contexts, the risk is introduced when an agent uses its privileged access and integrated tools to disclose sensitive information from a user's emails, files, or other connected systems.

#### Exposed

This risk is exposed within the application, when the model inadvertently reveals sensitive data it shouldn't. In agentic systems, the risk is magnified when an agent uses its privileged access and integrated tools to reveal sensitive data in interactions with a third party.

#### Mitigated

Mitigate sensitive data disclosure by: filtering model outputs, rigorously testing the model during training, tuning, and evaluation, and removing or labeling sensitive data during sourcing, filtering, and processing before it's used for training. For agents, implement controls at multiple levels of the system, including enforcing permissions on the agent’s access to tools and sensitive data, safely rendering agent outputs, and using application-level warnings to get user confirmation before executing actions that may disclose sensitive information.

For more details, see [Focus on Agents](https://saif.google/focus-on-agents).

### Inferred Sensitive Data

#### Introduced

The risk of Inferred Sensitive Data is introduced in several components. It's inherent to models due to their non-deterministic nature and is amplified by inadequate data handling practices that fail to filter sensitive information. It can also be due to training processes that neglect to evaluate the model's potential for sensitive inferences.

#### Exposed

This risk is exposed within the model when it generates a response containing inferred sensitive data that it shouldn't.

#### Mitigated

Mitigation is multi-pronged: filtering model outputs to prevent revealing inferred sensitive data, rigorously testing the model during training, tuning, and evaluation to prevent sensitive inferences, and proactively removing or labeling data that could lead to such inferences during sourcing, filtering, and processing before training.

### Insecure Model Output

#### Introduced

The risk of Insecure Model Output is inherent to AI models due to their non-deterministic nature, which can lead to unexpected and potentially harmful outputs.

#### Exposed

This risk is exposed within the model itself during usage, either through accidental triggers or deliberate exploitation.

#### Mitigated

Mitigation includes robust model validation and sanitization processes within the model output handling component to screen and filter for insecure responses.

### Rogue Actions

#### Introduced

Integrating agents into an AI system introduces the risk of Rogue Actions by dramatically expanding the model's ability to trigger real-world actions and consequences. This risk is introduced through a failure of the reasoning core to align with the user’s intent, or through the poisoning of orchestration components like tools, memory, and retrieved data.

#### Exposed

This vulnerability is exposed during application usage when the model inadvertently triggers an unintended action.

#### Mitigated

Mitigating Rogue Actions requires a multi-layered defense, starting with filtering and standardizing all inputs before they reach the model and defining tool limitations in the agent’s system instructions. Harden the reasoning core and model themselves with adversarial training to recognize prompt injection. Within orchestration, govern the agent’s capabilities with observability, policy engines, and credentialed tool access, implementing contextual agent security. Finally, normalize and sanitize outputs during rendering, and implement user-facing notifications and other safeguards tailored to the specific application or platform to prevent exploitation.

For more details, see [Focus on Agents](https://saif.google/focus-on-agents).

### Next Steps

Now that you understand the basics of the SAIF Risk Map, explore more detailed information about [Risks](https://saif.google/secure-ai-framework/saif-map/risks), [Controls](https://saif.google/secure-ai-framework/saif-map/controls), and [Components](https://saif.google/secure-ai-framework/saif-map/components).

Previous 

Next 

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



