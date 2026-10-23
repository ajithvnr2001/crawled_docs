---
url: https://saif.google/agent-risk-self-assessment/
title: SAIF Agent Risk Self-Assessment: Check Your AI Agent Security
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:20:57.708721+00:00
---

# SAIF Agent Risk Self-Assessment: Check Your AI Agent Security

> Source: https://saif.google/agent-risk-self-assessment/

![](https://www.gstatic.com/marketing-cms/assets/images/8f/97/85b1cf10464e962f05f392235da7/agents-risk-self-assessment-icon.svg)

# 

Agent Risk Self Assessment

AI Agents are sensitive to a specific set of risks. We developed this self-assessment for security practitioners, to help identify which AI risks may be most relevant to your agents.

Use this assessment to start conversations and guide further research.

Take the Agent Self Assessment 

![](https://www.gstatic.com/marketing-cms/assets/images/8f/97/85b1cf10464e962f05f392235da7/agents-risk-self-assessment-icon.svg)

# 

Agent Risk Self Assessment

This is a resource to help you understand which SAIF risks may be relevant to your organization.

It is for informational purposes only and does not constitute or replace professional advice. Your answers are not collected or shared. By continuing, you agree with the terms.

Learn more.

## About this self-assessment

### For informational purposes only

This self-assessment is intended to help you understand what AI security risks may be relevant to your organization. By using this self-assessment, you agree that this resource is for informational purposes only. Consult a security professional for advice. You're encouraged to talk to a security professional about what your results may mean for your organization. Google disclaims any liability, loss, or risk incurred as a consequence of using this resource.

### Private and secure

Google does not collect or share answers or results from the self-assessment. We collect data only to analyze traffic, and we use that data only in ways that do not identify you and that follow our Privacy Policy.

No thanks  I agree 

![](https://www.gstatic.com/marketing-cms/assets/images/8f/97/85b1cf10464e962f05f392235da7/agents-risk-self-assessment-icon.svg)

# 

Agent Risk Self Assessment

## Identity and authorization

Does your AI Agent use an agent-specific identity with well-scoped credentials to ensure it can access only the data and tools it actually needs and is authorized to use?

  * Yes
  * No
  * Maybe



## Observability

Does your AI Agent keep a clear record of its actions, inputs, and outputs so users and operators can monitor and audit what it is doing on their behalf?

  * Yes
  * No
  * Maybe



## User Control

Does your AI Agent use Human-in-The-Loop (HiTL) or Human-on-The-Loop (HoTL) mechanisms, enabling users to oversee and govern actions involving critical systems and sensitive data?

  * Yes
  * No
  * Maybe



## Built-in model safety

Is your AI Agent powered by a model that has built-in adversarial safeguards to protect itself against prompt injection attacks and to prevent it from generating harmful content (or code)?

  * Yes
  * No
  * Maybe



## In-tool guardrails

Does your AI Agent have policy guardrails to prevent accidental or malicious misuse of your data and systems?

  * Yes
  * No
  * Maybe



## Input and output screening

Does your AI Agent check incoming requests for attacks and sanitize its responses to prevent data leaks?

  * Yes
  * No
  * Maybe



## Testing

Have you tested your AI Agent to see how it handles prompt injection attacks designed to trick it into breaking security rules?

  * Yes
  * No
  * Maybe



Back Continue

![](https://www.gstatic.com/marketing-cms/assets/images/4e/26/24dbdd8e4d6f8dba6f7215fa9368/agents-risk-self-assessment-icon.svg)

# 

SAIF Agent Security Risk Report

Based on your self assessment answers, the following risks may be relevant to your organization.

Based on your self assessment answers, your risks are well mitigated. Please review this report for additional information.

Share this report

  * Copy link

× 

Get shareable link 



This report has been shared with you. Start over to create your own report.

  * Agent risks
  * Assessment & mitigations



### Agent **risks**

#### Rogue actions

An agent executes an operation (via tools or APIs) that is not aligned with the user's intent; either accidentally (due to a model hallucination or reasoning error) or maliciously (due to indirect prompt injection through untrusted content).

#### Sensitive Data Disclosure (or Data Exfiltration)

An agent reveals private, confidential, or proprietary information to unauthorized parties.

### Assessment **& mitigations**

Expand all Collapse all

###  Mitigations that need consideration

#### Identity and authorization

Does your AI Agent use an agent-specific identity with well-scoped credentials to ensure it can access only the data and tools it actually needs and is authorized to use? ****

**Mitigation**  
Tightly scoping access to data and tools limits the potential impact of a _rogue action_ through deterministic controls tailored to the intended functionality of an agent (principle of least privilege).

#### Observability

Does your AI Agent keep a clear record of its actions, inputs, and outputs so users and operators can monitor and audit what it is doing on their behalf? ****

**Mitigation**  
Implementing auditable logs brings transparency that allows monitoring agent activity, enabling you to detect _rogue actions_ or the _disclosure of sensitive data_ and take corrective measures.

#### User Control

Does your AI Agent use Human-in-The-Loop (HiTL) or Human-on-The-Loop (HoTL) mechanisms, enabling users to oversee and govern actions involving critical systems and sensitive data? ****

**Mitigation**  
Ensuring the user has the final word before an agent performs state-changing or irreversible actions with high consequences is a powerful safeguard against _rogue actions_ and the _disclosure of sensitive data_ , guaranteeing that the planned agent action is aligned with user intent.

#### Built-in model safety

Is your AI Agent powered by a model that has built-in adversarial safeguards to protect itself against prompt injection attacks and to prevent it from generating harmful content (or code)? ****

**Mitigation**  
Building on a safe foundation forms a strong initial protection against _rogue actions_ by guarding against prompt injections and preventing many forms of unwanted actions by default. This may include adversarial fine-tuning or other model-level techniques.

#### In-tool guardrails

Does your AI Agent have policy guardrails to prevent accidental or malicious misuse of your data and systems? ****

**Mitigation**  
Defining security policies that implement a product-specific set of constraints on the actions that the tools the agent calls can perform prevents _rogue actions_ (often in conjunction with **User Control**). Critic models may further augment in-tool guardrails.

#### Input and output screening

Does your AI Agent check incoming requests for attacks and sanitize its responses to prevent data leaks? ****

**Mitigation**  
Blocking adversarial queries from reaching your agent closes an avenue for triggering malicious _rogue actions_. Sanitizing or blocking insecure content before your agent outputs it to applications, extensions, or users prevents the _disclosure of sensitive data_ and the triggering of _rogue actions_ in adjacent systems. Input screening may include prompt injection classifiers, among others.

#### Testing

Have you tested your AI Agent to see how it handles prompt injection attacks designed to trick it into breaking security rules? ****

**Mitigation**  
Have you tested your AI Agent to see how it handles prompt injection attacks designed to trick it into breaking security rules?

###  Mitigations in place

#### Identity and authorization

Does your AI Agent use an agent-specific identity with well-scoped credentials to ensure it can access only the data and tools it actually needs and is authorized to use? ****

**Mitigation**  
Tightly scoping access to data and tools limits the potential impact of a _rogue action_ through deterministic controls tailored to the intended functionality of an agent (principle of least privilege).

#### Observability

Does your AI Agent keep a clear record of its actions, inputs, and outputs so users and operators can monitor and audit what it is doing on their behalf? ****

**Mitigation**  
Implementing auditable logs brings transparency that allows monitoring agent activity, enabling you to detect _rogue actions_ or the _disclosure of sensitive data_ and take corrective measures.

#### User Control

Does your AI Agent use Human-in-The-Loop (HiTL) or Human-on-The-Loop (HoTL) mechanisms, enabling users to oversee and govern actions involving critical systems and sensitive data? ****

**Mitigation**  
Ensuring the user has the final word before an agent performs state-changing or irreversible actions with high consequences is a powerful safeguard against _rogue actions_ and the _disclosure of sensitive data_ , guaranteeing that the planned agent action is aligned with user intent.

#### Built-in model safety

Is your AI Agent powered by a model that has built-in adversarial safeguards to protect itself against prompt injection attacks and to prevent it from generating harmful content (or code)? ****

**Mitigation**  
Building on a safe foundation forms a strong initial protection against _rogue actions_ by guarding against prompt injections and preventing many forms of unwanted actions by default. This may include adversarial fine-tuning or other model-level techniques.

#### In-tool guardrails

Does your AI Agent have policy guardrails to prevent accidental or malicious misuse of your data and systems? ****

**Mitigation**  
Defining security policies that implement a product-specific set of constraints on the actions that the tools the agent calls can perform prevents _rogue actions_ (often in conjunction with **User Control**). Critic models may further augment in-tool guardrails.

#### Input and output screening

Does your AI Agent check incoming requests for attacks and sanitize its responses to prevent data leaks? ****

**Mitigation**  
Blocking adversarial queries from reaching your agent closes an avenue for triggering malicious _rogue actions_. Sanitizing or blocking insecure content before your agent outputs it to applications, extensions, or users prevents the _disclosure of sensitive data_ and the triggering of _rogue actions_ in adjacent systems. Input screening may include prompt injection classifiers, among others.

#### Testing

Have you tested your AI Agent to see how it handles prompt injection attacks designed to trick it into breaking security rules? ****

**Mitigation**  
Have you tested your AI Agent to see how it handles prompt injection attacks designed to trick it into breaking security rules?

Share this report

  * Copy link

× 

Get shareable link 



Start again 

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



