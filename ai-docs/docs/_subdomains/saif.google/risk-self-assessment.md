---
url: https://saif.google/risk-self-assessment/
title: SAIF Risk Self-Assessment: Check Your AI Security
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:15.589601+00:00
---

# SAIF Risk Self-Assessment: Check Your AI Security

> Source: https://saif.google/risk-self-assessment/

![](https://www.gstatic.com/marketing-cms/assets/images/aa/95/27445b8c4b8c86ee5598d0cec1f8/agents-risk-self-assessment-icon.svg)

# 

Risk Self Assessment

Every organization and AI implementation is unique. We developed this self-assessment for security practitioners, to help identify which AI risks may be most relevant to you.

Use this assessment to start conversations and guide further research.

Start Assessment 

![](https://www.gstatic.com/marketing-cms/assets/images/aa/95/27445b8c4b8c86ee5598d0cec1f8/agents-risk-self-assessment-icon.svg)

# 

Risk Self Assessment

This is a resource to help you understand which SAIF risks may be relevant to your organization.

It is for informational purposes only and does not constitute or replace professional advice. Your answers are not collected or shared. By continuing, you agree with the terms.

Learn more.

## About this self-assessment

### For informational purposes only

This self-assessment is intended to help you understand what AI security risks may be relevant to your organization. By using this self-assessment, you agree that this resource is for informational purposes only. Consult a security professional for advice. You're encouraged to talk to a security professional about what your results may mean for your organization. Google disclaims any liability, loss, or risk incurred as a consequence of using this resource.

### Private and secure

Google does not collect or share answers or results from the self-assessment. We collect data only to analyze traffic, and we use that data only in ways that do not identify you and that follow our Privacy Policy.

No thanks  I agree 

![](https://www.gstatic.com/marketing-cms/assets/images/aa/95/27445b8c4b8c86ee5598d0cec1f8/agents-risk-self-assessment-icon.svg)

# 

Risk Self Assessment

## Risk Assessment Questions

Which of the following best describes your organization’s use of Generative AI models? You may select more than one option.

  * **Model Creator:** Organizations that either train and tune foundation models for Generative AI, or tune acquired models for more domain-specific tasks. 
  * **Model Consumer:** Organizations that build AI applications, features, or products using models, but do not create or tune the models themselves. The models may be accessed via an API to a managed service, or downloaded and packaged into the application or product being produced. 



Back Continue

![](https://www.gstatic.com/marketing-cms/assets/images/aa/95/27445b8c4b8c86ee5598d0cec1f8/agents-risk-self-assessment-icon.svg)

# 

Risk Self Assessment

## Risk Assessment Questions

Do you have robust management of all training, tuning, or evaluation data used with your models to ensure that sensitive, unauthorized, or malicious data does not enter your models?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Are you able to detect, remove, and remediate malicious or accidental changes in your training, tuning, or evaluation data?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Is any sensitive user data used in training, tuning, or evaluating your AI models?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you have robust management of all user data that results from your Generative AI applications to ensure that user data is stored, processed, and used in accordance with user consents and user policies?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Are you able to ensure that all data, models, and code used to train, tune, or evaluate models cannot be tampered without detection during model development and during deployment?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you protect your Generative AI applications and models against large-scale malicious queries from user accounts, devices, or via APIs?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Are you using secure-by-default designs and coding frameworks in applications integrated with Generative AI applications?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs?

  * Yes
  * No
  * Maybe



## Risk Assessment Questions

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users?

  * Yes
  * No
  * Maybe



Back Continue

![](https://www.gstatic.com/marketing-cms/assets/images/05/2f/292a8d5c463aa0ca1a2851923fde/agents-risk-self-assessment-icon.svg)

# 

SAIF Risk Report

Based on your self assessment answers, the following  risks may be relevant to your organization.

Share this report

  * Copy link

× 

Get shareable link 



This report has been shared with you. Start over to create your own report.

### Assessment **& risks**

Expand all Collapse all

###  Risks which are relevant to your organisation

#### Data Poisoning

Altering data sources used to train the model. In terms of impact, Data Poisoning is comparable to modifying the logic of an application to change its behavior.

The following controls may help mitigate this risk:

  * [Training Data Sanitization](https://saif.google/secure-ai-framework/controls#training-data-sanitization)
  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Model and Data Access Control](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)



Read more about the risk of [Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning).

Are you able to detect, remove, and remediate malicious or accidental changes in your training, tuning, or evaluation data? ****

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are you able to ensure that all data, models, and code used to train, tune, or evaluate models cannot be tampered without detection during model development and during deployment? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Unauthorized Training Data

Using unauthorized data for model training. Using a model trained with Unauthorized Training Data might lead to legal or ethical challenges.

The following controls may help mitigate this risk:

  * [Training Data Management](https://saif.google/secure-ai-framework/controls#training-data-management)



Read more about the risk of [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data).

Do you have robust management of all training, tuning, or evaluation data used with your models to ensure that sensitive, unauthorized, or malicious data does not enter your models? ****

#### Model Source Tampering

Tampering with the model's code or data. Model Source Tampering is similar to tampering with traditional software code, and can create vulnerabilities or unintended behavior.

The following controls may help mitigate this risk:

  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Model and Data Access Controls](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)
  * [Model and Data Inventory Management](https://saif.google/secure-ai-framework/controls#model-and-data-inventory-management)



Read more about the risk of [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering).

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are you able to ensure that all data, models, and code used to train, tune, or evaluate models cannot be tampered without detection during model development and during deployment? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Excessive Data Handling

Unauthorized collection, retention, processing, or sharing of user data. Excessive Data Handling may lead to policy and legal challenges.

The following controls may help mitigate this risk:

  * [User Data Management](https://saif.google/secure-ai-framework/controls#user-data-management)



Read more about the risk of [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling).

Do you have robust management of all user data that results from your Generative AI applications to ensure that user data is stored, processed, and used in accordance with user consents and user policies? ****

#### Model Exfiltration

Theft of a model. Similar to stealing code, this threat has both intellectual property and security implications.

The following controls may help mitigate this risk:

  * [Model and Data Inventory Management](https://saif.google/secure-ai-framework/controls#model-and-data-inventory-management)
  * [Model and Data Access Controls](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)



Read more about the risk of [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration).

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Model Deployment Tampering

Unauthorized changes to model deployment components. Model Deployment Tampering can result in changes to model behavior.

The following controls may help mitigate this risk:

  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)



Read more about the risk of [Model Deployment Tampering](https://saif.google/secure-ai-framework/risks#model-deployment-tampering).

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Denial of ML Service

Overloading ML systems with resource-intensive queries. Like traditional DoS attacks, Denial of ML Service can reduce availability of or entirely disrupt a service.

The following controls may help mitigate this risk:

  * [Application Access Management](https://saif.google/secure-ai-framework/controls#application-access-management)



Read more about the risk of [Denial of ML Service](https://saif.google/secure-ai-framework/risks#denial-of-ml-service).

Do you protect your Generative AI applications and models against large-scale malicious queries from user accounts, devices, or via APIs? ****

#### Model Reverse Engineering

Recreating a model by analyzing its inputs, outputs, and behaviors. A reverse engineer model can be used to create imitation products or adversarial attacks.

The following controls may help mitigate this risk:

  * [Application Access Management](https://saif.google/secure-ai-framework/controls#application-access-management)



Read more about the risk of [Model Reverse Engineering](https://saif.google/secure-ai-framework/risks#model-reverse-engineering).

Do you protect your Generative AI applications and models against large-scale malicious queries from user accounts, devices, or via APIs? ****

#### Insecure Integrated Component

Software vulnerabilities that can be leveraged to compromise AI models. Insecure Integrated Component can lead to privacy and security concerns, as well as potential ethical and legal challenges.

The following controls may help mitigate this risk:

  * [Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions)



Read more about the risk of [Insecure Integrated Component](https://saif.google/secure-ai-framework/risks#insecure-integrated-component).

Are you using secure-by-default designs and coding frameworks in applications integrated with Generative AI applications? ****

#### Prompt Injection

Tricking a model to run unintended commands. In terms of impact, Prompt Injection can change a model's behavior.

The following controls may help mitigate this risk:

  * [Input Validation and Sanitization](https://saif.google/secure-ai-framework/controls#input-validation-and-sanitization)
  * [Adversarial Training and Testing](https://saif.google/secure-ai-framework/controls#adversarial-training-and-testing)



Read more about the risk of [Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

#### Model Evasion

Changes to a prompt input to cause the model to produce incorrect inferences. Model Evasion can lead to reputational, legal, security, and privacy risks.

The following controls may help mitigate this risk:

  * [Adversarial Training and Testing](https://saif.google/secure-ai-framework/controls#adversarial-training-and-testing)



Read more about the risk of [Model Evasion](https://saif.google/secure-ai-framework/risks#model-evasion).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Sensitive Data Disclosure

Disclosure of sensitive data by the model. Sensitive Data Disclosure poses a threat to user privacy, organizational reputation, and intellectual property.

The following controls may help mitigate this risk:

  * [Privacy Enhancing Technologies](https://saif.google/secure-ai-framework/controls#privacy-enhancing-technologies)
  * [User Data Management](https://saif.google/secure-ai-framework/controls#user-data-management)
  * [Input](https://saif.google/secure-ai-framework/controls#input-validation-and-sanitization) and [Output](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization) Validation and Sanitization



Read more about the risk of [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure).

Is any sensitive user data used in training, tuning, or evaluating your AI models? ****

Do you have robust management of all user data that results from your Generative AI applications to ensure that user data is stored, processed, and used in accordance with user consents and user policies? ****

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

#### Inferred Sensitive Data

Model inferring personal information not contained in training data or inputs. Inferred Sensitive Data may be considered a data privacy incident.

The following controls may help mitigate this risk:

  * [Training Data Management](https://saif.google/secure-ai-framework/controls#training-data-management)
  * [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization)



Read more about the risk of [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data).

Do you have robust management of all training, tuning, or evaluation data used with your models to ensure that sensitive, unauthorized, or malicious data does not enter your models? ****

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Insecure Model Output

Unvalidated model output passed to the end user. Insecure Model Output poses risks to organizational reputation, security, and user safety.

The following controls may help mitigate this risk:

  * [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization)



Read more about the risk of [Insecure Model Output](https://saif.google/secure-ai-framework/risks#insecure-model-output).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Rogue Actions

Unintentional model-based actions executed via extensions. Rogue Actions can create a cascading, risk to organizational reputation, user trust, security, and safety.

The following controls may help mitigate this risk:

  * [Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions)
  * [Agent User Control](https://saif.google/secure-ai-framework/controls#agent-user-control)
  * [Agent Observability](https://saif.google/secure-ai-framework/controls#agent-observability)



Read more about the risk of [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions).

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

###  Risks which you have mitigated

#### Data Poisoning

Altering data sources used to train the model. In terms of impact, Data Poisoning is comparable to modifying the logic of an application to change its behavior.

The following controls may help mitigate this risk:

  * [Training Data Sanitization](https://saif.google/secure-ai-framework/controls#training-data-sanitization)
  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Model and Data Access Control](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)



Read more about the risk of [Data Poisoning](https://saif.google/secure-ai-framework/risks#data-poisoning).

Are you able to detect, remove, and remediate malicious or accidental changes in your training, tuning, or evaluation data? ****

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are you able to ensure that all data, models, and code used to train, tune, or evaluate models cannot be tampered without detection during model development and during deployment? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Unauthorized Training Data

Using unauthorized data for model training. Using a model trained with Unauthorized Training Data might lead to legal or ethical challenges.

The following controls may help mitigate this risk:

  * [Training Data Management](https://saif.google/secure-ai-framework/controls#training-data-management)



Read more about the risk of [Unauthorized Training Data](https://saif.google/secure-ai-framework/risks#unauthorized-training-data).

Do you have robust management of all training, tuning, or evaluation data used with your models to ensure that sensitive, unauthorized, or malicious data does not enter your models? ****

#### Model Source Tampering

Tampering with the model's code or data. Model Source Tampering is similar to tampering with traditional software code, and can create vulnerabilities or unintended behavior.

The following controls may help mitigate this risk:

  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Model and Data Access Controls](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)
  * [Model and Data Inventory Management](https://saif.google/secure-ai-framework/controls#model-and-data-inventory-management)



Read more about the risk of [Model Source Tampering](https://saif.google/secure-ai-framework/risks#model-source-tampering).

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are you able to ensure that all data, models, and code used to train, tune, or evaluate models cannot be tampered without detection during model development and during deployment? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Excessive Data Handling

Unauthorized collection, retention, processing, or sharing of user data. Excessive Data Handling may lead to policy and legal challenges.

The following controls may help mitigate this risk:

  * [User Data Management](https://saif.google/secure-ai-framework/controls#user-data-management)



Read more about the risk of [Excessive Data Handling](https://saif.google/secure-ai-framework/risks#excessive-data-handling).

Do you have robust management of all user data that results from your Generative AI applications to ensure that user data is stored, processed, and used in accordance with user consents and user policies? ****

#### Model Exfiltration

Theft of a model. Similar to stealing code, this threat has both intellectual property and security implications.

The following controls may help mitigate this risk:

  * [Model and Data Inventory Management](https://saif.google/secure-ai-framework/controls#model-and-data-inventory-management)
  * [Model and Data Access Controls](https://saif.google/secure-ai-framework/controls#model-and-data-access-controls)
  * [Model and Data Integrity Management](https://saif.google/secure-ai-framework/controls#model-and-data-integrity-management)
  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)



Read more about the risk of [Model Exfiltration](https://saif.google/secure-ai-framework/risks#model-exfiltration).

Do you have a complete inventory of all models, datasets (for training, tuning, or evaluation), and related ML artifacts (such as code)? ****

Do you have robust access controls on all models, datasets, and related ML artifacts to minimize, detect, and prevent unauthorized reading or copying? ****

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Model Deployment Tampering

Unauthorized changes to model deployment components. Model Deployment Tampering can result in changes to model behavior.

The following controls may help mitigate this risk:

  * [Secure-by-Default ML Tooling](https://saif.google/secure-ai-framework/controls#secure-by-default-ml-tooling)



Read more about the risk of [Model Deployment Tampering](https://saif.google/secure-ai-framework/risks#model-deployment-tampering).

Are the frameworks, libraries, software systems, and hardware components used in the development and deployment of your models analyzed for and protected against security vulnerabilities? ****

#### Denial of ML Service

Overloading ML systems with resource-intensive queries. Like traditional DoS attacks, Denial of ML Service can reduce availability of or entirely disrupt a service.

The following controls may help mitigate this risk:

  * [Application Access Management](https://saif.google/secure-ai-framework/controls#application-access-management)



Read more about the risk of [Denial of ML Service](https://saif.google/secure-ai-framework/risks#denial-of-ml-service).

Do you protect your Generative AI applications and models against large-scale malicious queries from user accounts, devices, or via APIs? ****

#### Model Reverse Engineering

Recreating a model by analyzing its inputs, outputs, and behaviors. A reverse engineer model can be used to create imitation products or adversarial attacks.

The following controls may help mitigate this risk:

  * [Application Access Management](https://saif.google/secure-ai-framework/controls#application-access-management)



Read more about the risk of [Model Reverse Engineering](https://saif.google/secure-ai-framework/risks#model-reverse-engineering).

Do you protect your Generative AI applications and models against large-scale malicious queries from user accounts, devices, or via APIs? ****

#### Insecure Integrated Component

Software vulnerabilities that can be leveraged to compromise AI models. Insecure Integrated Component can lead to privacy and security concerns, as well as potential ethical and legal challenges.

The following controls may help mitigate this risk:

  * [Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions)



Read more about the risk of [Insecure Integrated Component](https://saif.google/secure-ai-framework/risks#insecure-integrated-component).

Are you using secure-by-default designs and coding frameworks in applications integrated with Generative AI applications? ****

#### Prompt Injection

Tricking a model to run unintended commands. In terms of impact, Prompt Injection can change a model's behavior.

The following controls may help mitigate this risk:

  * [Input Validation and Sanitization](https://saif.google/secure-ai-framework/controls#input-validation-and-sanitization)
  * [Adversarial Training and Testing](https://saif.google/secure-ai-framework/controls#adversarial-training-and-testing)



Read more about the risk of [Prompt Injection](https://saif.google/secure-ai-framework/risks#prompt-injection).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

#### Model Evasion

Changes to a prompt input to cause the model to produce incorrect inferences. Model Evasion can lead to reputational, legal, security, and privacy risks.

The following controls may help mitigate this risk:

  * [Adversarial Training and Testing](https://saif.google/secure-ai-framework/controls#adversarial-training-and-testing)



Read more about the risk of [Model Evasion](https://saif.google/secure-ai-framework/risks#model-evasion).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Sensitive Data Disclosure

Disclosure of sensitive data by the model. Sensitive Data Disclosure poses a threat to user privacy, organizational reputation, and intellectual property.

The following controls may help mitigate this risk:

  * [Privacy Enhancing Technologies](https://saif.google/secure-ai-framework/controls#privacy-enhancing-technologies)
  * [User Data Management](https://saif.google/secure-ai-framework/controls#user-data-management)
  * [Input](https://saif.google/secure-ai-framework/controls#input-validation-and-sanitization) and [Output](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization) Validation and Sanitization



Read more about the risk of [Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure).

Is any sensitive user data used in training, tuning, or evaluating your AI models? ****

Do you have robust management of all user data that results from your Generative AI applications to ensure that user data is stored, processed, and used in accordance with user consents and user policies? ****

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

#### Inferred Sensitive Data

Model inferring personal information not contained in training data or inputs. Inferred Sensitive Data may be considered a data privacy incident.

The following controls may help mitigate this risk:

  * [Training Data Management](https://saif.google/secure-ai-framework/controls#training-data-management)
  * [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization)



Read more about the risk of [Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#inferred-sensitive-data).

Do you have robust management of all training, tuning, or evaluation data used with your models to ensure that sensitive, unauthorized, or malicious data does not enter your models? ****

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Insecure Model Output

Unvalidated model output passed to the end user. Insecure Model Output poses risks to organizational reputation, security, and user safety.

The following controls may help mitigate this risk:

  * [Output Validation and Sanitization](https://saif.google/secure-ai-framework/controls#output-validation-and-sanitization)



Read more about the risk of [Insecure Model Output](https://saif.google/secure-ai-framework/risks#insecure-model-output).

Do you perform adversarial testing and training on models and Generative AI applications to improve resistance to adversarial inputs? ****

#### Rogue Actions

Unintentional model-based actions executed via extensions. Rogue Actions can create a cascading, risk to organizational reputation, user trust, security, and safety.

The following controls may help mitigate this risk:

  * [Agent Permissions](https://saif.google/secure-ai-framework/controls#agent-permissions)
  * [Agent User Control](https://saif.google/secure-ai-framework/controls#agent-user-control)
  * [Agent Observability](https://saif.google/secure-ai-framework/controls#agent-observability)



Read more about the risk of [Rogue Actions](https://saif.google/secure-ai-framework/risks#rogue-actions).

Do you build or deploy Generative AI powered agents or tools that can take actions on behalf of internal or external users? ****

Share this report

  * Copy link

× 

Get shareable link 



Start again 

  * ![](https://www.gstatic.com/marketing-cms/assets/images/e9/bc/394093d7467588f812f19c1b266d/g-shield-lockup-footer.svg)



