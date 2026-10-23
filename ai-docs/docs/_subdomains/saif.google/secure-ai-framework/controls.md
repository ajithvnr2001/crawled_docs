---
url: https://saif.google/secure-ai-framework/controls/
title: Security Controls for Generative AI Systems - SAIF
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:08.071440+00:00
---

# Security Controls for Generative AI Systems - SAIF

> Source: https://saif.google/secure-ai-framework/controls/

![](https://www.gstatic.com/marketing-cms/assets/images/66/6a/7dd52d914e2bbe67708424e113c9/focus-on-agents-icon.svg)

# Controls

  
The following sections describe controls available to organizations for specific AI risks.   
  
Each control is mapped onto the corresponding risks it can address, with the exception of Governance and Assurance controls, which apply universally to all risks and every stage of the AI development process. 

  * Data
  * Infrastructure
  * Model
  * Application
  * Assurance
  * Governance



## Data controls

Expand all Collapse all

##  Privacy Enhancing Technologies

### Privacy Enhancing Technologies

Use technologies that minimize, de-identify, or restrict use of PII data in training or evaluating models.   
  
  
**Control**   
Privacy Enhancing Technologies   
  
**Who can implement**   
Model Creators   
  
**Risk mapping**   
Sensitive Data Disclosure 

Use technologies that minimize, de-identify, or restrict use of PII data in training or evaluating models.  
  
  
**Control**  
Privacy Enhancing Technologies  
  
**Who can implement**  
Model Creators  
  
**Risk mapping**  
Sensitive Data Disclosure

##  Training Data Management

### Training Data Management

Ensure that all data used to train and evaluate models is authorized for the intended purposes.   
  
**Control**   
Training Data Management   
  
**Who can implement**   
Model Creators   
  
**Risk mapping**   
[Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data), [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data)

Ensure that all data used to train and evaluate models is authorized for the intended purposes.  
  
**Control**  
Training Data Management  
  
**Who can implement**  
Model Creators  
  
**Risk mapping**  
[ Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data), [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data)

##  Training Data Sanitization

### Training Data Sanitization

Detect and remove or remediate poisoned or sensitive data in training and evaluation.   
  
**Control**   
Training Data Sanitization   
  
**Who can implement**   
Model Creators   
  
**Risk mapping**   
[Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data)

Detect and remove or remediate poisoned or sensitive data in training and evaluation.  
  
**Control**  
Training Data Sanitization  
  
**Who can implement**  
Model Creators  
  
**Risk mapping**  
[ Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data)

##  User Data Management

### User Data Management

Store, process, and use all user data (e.g. prompts and logs) from AI applications in compliance with user consent.   
  
**Control**   
User Data Management   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling)

Store, process, and use all user data (e.g. prompts and logs) from AI applications in compliance with user consent.  
  
**Control**  
User Data Management  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling)

## Infrastructure controls

Expand all Collapse all

##  Model and Data Inventory Management

### Model and Data Inventory Management

Ensure that all data, code, models, and transformation tools used in AI applications are inventoried and tracked.   
  
**Control**   
Model and Data Inventory Management   
  
**Who can implement**   
Model Creators, Model Consumers (if storing models)   
  
**Risk mapping**   
[Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration)

Ensure that all data, code, models, and transformation tools used in AI applications are inventoried and tracked.  
  
**Control**  
Model and Data Inventory Management  
  
**Who can implement**  
Model Creators, Model Consumers (if storing models)  
  
**Risk mapping**  
[ Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration)

##  Model and Data Access Controls

### Model and Data Access Controls

Minimize internal access to models, weights, datasets, etc. in storage and in production use.   
  
**Control**   
Model and Data Access Controls   
  
**Who can implement**   
Model Creators, Model Consumers (if storing models)   
  
**Risk mapping**   
[Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration)

Minimize internal access to models, weights, datasets, etc. in storage and in production use.  
  
**Control**  
Model and Data Access Controls  
  
**Who can implement**  
Model Creators, Model Consumers (if storing models)  
  
**Risk mapping**  
[ Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration)

##  Model and Data Integrity Management

### Model and Data Integrity Management

Ensure that all data, models, and code used to produce AI models are verifiably integrity-protected during development and deployment.   
  
**Control**   
Model and Data Integrity Management   
  
**Who can implement**   
Model Creators, Model Consumers (if storing models)   
  
**Risk mapping**   
[Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering)

Ensure that all data, models, and code used to produce AI models are verifiably integrity-protected during development and deployment.  
  
**Control**  
Model and Data Integrity Management  
  
**Who can implement**  
Model Creators, Model Consumers (if storing models)  
  
**Risk mapping**  
[ Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering)

##  Secure-by-Default ML Tooling

### Secure-by-Default ML Tooling

Use secure-by-default frameworks, libraries, software systems, and hardware components for AI development or deployment to protect confidentiality and integrity of AI assets and outputs.   
  
**Control**   
Secure-by-Default ML Tooling   
  
**Who can implement**   
Model Creators, Model Consumers (if storing models)   
  
**Risk mapping**   
[Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration), [Model Deployment Tampering](https://saif.google/secure-ai-framework/risks#model-deployment-tampering)

Use secure-by-default frameworks, libraries, software systems, and hardware components for AI development or deployment to protect confidentiality and integrity of AI assets and outputs.  
  
**Control**  
Secure-by-Default ML Tooling  
  
**Who can implement**  
Model Creators, Model Consumers (if storing models)  
  
**Risk mapping**  
[ Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning), [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering), [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration), [Model Deployment Tampering](https://saif.google/secure-ai-framework/risks#model-deployment-tampering)

## Model controls

Expand all Collapse all

##  Input Validation and Sanitization

### Input Validation and Sanitization

Block or restrict adversarial queries to AI models.   
  
**Control**   
Input Validation and Sanitization   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection)

Block or restrict adversarial queries to AI models.  
  
**Control**  
Input Validation and Sanitization  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection)

##  Output Validation and Sanitization

### Output Validation and Sanitization

Block, nullify, or sanitize insecure output from AI models before passing it to applications, extensions or users.   
  
**Control**   
Output Validation and Sanitization   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data)

Block, nullify, or sanitize insecure output from AI models before passing it to applications, extensions or users.  
  
**Control**  
Output Validation and Sanitization  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data)

##  Adversarial Training and Testing

### Adversarial Training and Testing

Use techniques to make AI models robust to adversarial inputs (i.e. prompts) in the context of their use in applications.   
  
**Control**   
Adversarial Training and Testing   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[Model Evasion](https://saif.google/secure-ai-framework/risks#model-evasion), [Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data), [Insecure Model Output](https://saif.google/secure-ai-framework/risks#insecure-model-output)

Use techniques to make AI models robust to adversarial inputs (i.e. prompts) in the context of their use in applications.  
  
**Control**  
Adversarial Training and Testing  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ Model Evasion](https://saif.google/secure-ai-framework/risks#model-evasion), [Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data), [Insecure Model Output](https://saif.google/secure-ai-framework/risks#insecure-model-output)

## Application controls

Expand all Collapse all

##  Application Access Management

### Application Access Management

Ensure that only authorized users and endpoints can access specific resources for authorized actions.   
  
**Control**   
Application Access Management   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
[Denial of ML Service](https://saif.google/secure-ai-framework/risks#denial-of-ml-service), [Model Reverse Engineering](https://saif.google/secure-ai-framework/risks#model-reverse-engineering)

Ensure that only authorized users and endpoints can access specific resources for authorized actions.  
  
**Control**  
Application Access Management  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
[ Denial of ML Service](https://saif.google/secure-ai-framework/risks#denial-of-ml-service), [Model Reverse Engineering](https://saif.google/secure-ai-framework/risks#model-reverse-engineering)

##  User Transparency and Controls

### User Transparency and Controls

Inform users of relevant AI risks with disclosures, and provide transparency and control experiences for use of their data in AI applications.   
  
**Control**   
User Transparency and Controls   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling)

Inform users of relevant AI risks with disclosures, and provide transparency and control experiences for use of their data in AI applications.  
  
**Control**  
User Transparency and Controls  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
[ Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling)

##  Agent User Control

### Agent User Control

Ensure user approval for any actions performed by agents/plugins that alter user data or act on the user’s behalf.   
  
**Control**   
Agent User Control   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

Ensure user approval for any actions performed by agents/plugins that alter user data or act on the user’s behalf.  
  
**Control**  
Agent User Control  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
[ Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

##  Agent Permissions

### Agent Permissions

Use least-privilege principle as the upper bound on agentic system permissions to minimize the number of tools that an agent is permitted to interact with and the actions it is allowed to take. An agentic system’s use of privileges should be [contextual and dynamic](https://arxiv.org/pdf/2501.17070), adapting to the specific user query and trusted contextual information. This design also applies to agents that have access to user information. For example, an agent asked to fill out a form or answer questions should share only [contextually appropriate information](https://openreview.net/pdf?id=l9rATNBB8Y) and can be designed to dynamically minimize exposed data using [reference monitors](https://arxiv.org/abs/2405.05175).   
  
**Control**   
Agent Permissions   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
[Insecure Integrated System](https://saif.google/secure-ai-framework/risks#insecure-integrated-component), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

Use least-privilege principle as the upper bound on agentic system permissions to minimize the number of tools that an agent is permitted to interact with and the actions it is allowed to take. An agentic system’s use of privileges should be [contextual and dynamic](https://arxiv.org/pdf/2501.17070), adapting to the specific user query and trusted contextual information. This design also applies to agents that have access to user information. For example, an agent asked to fill out a form or answer questions should share only [contextually appropriate information](https://openreview.net/pdf?id=l9rATNBB8Y) and can be designed to dynamically minimize exposed data using [reference monitors](https://arxiv.org/abs/2405.05175).  
  
**Control**  
Agent Permissions  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
[ Insecure Integrated System](https://saif.google/secure-ai-framework/risks#insecure-integrated-component), [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

##  Agent Observability (New)

### Agent Observability (New)

Ensure an agent's actions, tool use, and reasoning are transparent and auditable through logging, allowing for debugging, security oversight, and user insights into agent activity.   
  
**Control**   
Agent Observability   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
[Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

Ensure an agent's actions, tool use, and reasoning are transparent and auditable through logging, allowing for debugging, security oversight, and user insights into agent activity.  
  
**Control**  
Agent Observability  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
[ Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure), [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions)

## Assurance controls

Expand all Collapse all

##  Red Teaming

### Red Teaming

Identify security and privacy improvements through self-driven adversarial attacks on AI infrastructure and products.   
  
**Control**   
Red Teaming   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Identify security and privacy improvements through self-driven adversarial attacks on AI infrastructure and products.  
  
**Control**  
Red Teaming  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

##  Vulnerability Management

### Vulnerability Management

Proactively and continually test and monitor production infrastructure and products for security and privacy regressions.   
  
**Control**   
Vulnerability Management   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Proactively and continually test and monitor production infrastructure and products for security and privacy regressions.  
  
**Control**  
Vulnerability Management  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

##  Threat Detection

### Threat Detection

Detect and alert on internal or external attacks on AI assets, infrastructure, and products.   
  
**Control**   
Threat Detection   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Detect and alert on internal or external attacks on AI assets, infrastructure, and products.  
  
**Control**  
Threat Detection  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

##  Incident Response Management

### Incident Response Management

Manage response to AI security and privacy incidents.   
  
**Control**   
Incident Response Management   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Manage response to AI security and privacy incidents.  
  
**Control**  
Incident Response Management  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

## Governance controls

Expand all Collapse all

##  User Policies and Education

### User Policies and Education

Publish easy to understand AI security and privacy policies and education for users.   
  
**Control**   
User Policies and Education   
  
**Who can implement**   
Model Consumers   
  
**Risk mapping**   
Will vary 

Publish easy to understand AI security and privacy policies and education for users.  
  
**Control**  
User Policies and Education  
  
**Who can implement**  
Model Consumers  
  
**Risk mapping**  
Will vary

##  Internal Policies and Education

### Internal Policies and Education

Publish comprehensive AI security and privacy policies and education for your employees.   
  
**Control**   
Internal Policies and Education   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Publish comprehensive AI security and privacy policies and education for your employees.  
  
**Control**  
Internal Policies and Education  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

##  Product Governance

### Product Governance

Validate that all AI models and products meet the established security and privacy requirements.   
  
**Control**   
Product Governance   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Validate that all AI models and products meet the established security and privacy requirements.  
  
**Control**  
Product Governance  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

##  Risk Governance

### Risk Governance

Inventory, measure, and monitor residual risk to AI in your organization.   
  
**Control**   
Risk Governance   
  
**Who can implement**   
Model Creators, Model Consumers   
  
**Risk mapping**   
[All](https://saif.google/secure-ai-framework/risks)

Inventory, measure, and monitor residual risk to AI in your organization.  
  
**Control**  
Risk Governance  
  
**Who can implement**  
Model Creators, Model Consumers  
  
**Risk mapping**  
[ All](https://saif.google/secure-ai-framework/risks)

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



