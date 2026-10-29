---
url: https://docs.cloud.google.com/application-integration/docs/agent-skills-overview/
title: Application Integration agent skills \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T11:13:36.651160+00:00
---

# Application Integration agent skills  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/agent-skills-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Application Integration agent skills

Application Integration provides agent skills that can help your agent accomplish common tasks. Agents that use these skills can then accomplish tasks with higher fidelity than an agent without the skills.

Agent skills are a standardized way to give AI agents specific knowledge and instructions they can reuse. They contain resources like scripts, reference materials, and templates that help the agent complete tasks accurately and reliably. For more information about skills, see [Agent Skills Overview](https://agentskills.io/home).

For a walkthrough that uses all three skills, see [Build an integration with an AI agent](https://docs.cloud.google.com/application-integration/docs/build-integration-ai-agent).

## The Application Integration basics skill

The Application Integration basics skill, [`application-integration-basics`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-basics), contains instructions for setting up Application Integration, such as enabling the required APIs, provisioning a region, configuring IAM roles and run-as service accounts, choosing an interface, and checking quotas and limits.

### Install the Application Integration basics skill

To install the `application-integration-basics` skill, run the following command in your terminal:
    
    
    npx skills add google/skills --skill application-integration-basics
    

### Application Integration basics reference files

The Application Integration basics agent skill includes several reference files that provide technical depth. These references let the skill execute functions or commands accurately by providing specific context to the underlying model. By default, the Application Integration basics skill includes the following reference files:

  * [Core concepts](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/references/core-concepts.md)
  * [IAM and service accounts](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/references/iam-and-service-accounts.md)
  * [Provisioning and Terraform](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/references/provisioning-and-terraform.md)
  * [API access](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/references/api-access.md)
  * [Limits](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/references/limits.md)



## The Application Integration authoring skill

The Application Integration authoring skill, [`application-integration-authoring`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-authoring), contains instructions for building, versioning, publishing, and running integrations through the REST API, such as downloading or uploading integration versions as JSON, configuring API triggers and config variables, publishing drafts, invoking integrations, and promoting versions across environments.

### Install the Application Integration authoring skill

To install the `application-integration-authoring` skill, run the following command in your terminal:
    
    
    npx skills add google/skills --skill application-integration-authoring
    

### Application Integration authoring reference files

By default, the Application Integration authoring skill includes the following reference files:

  * [IntegrationVersion JSON](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/references/integration-version-json.md)
  * [REST API cheatsheet](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/references/rest-api-cheatsheet.md)
  * [Triggers and execution](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/references/triggers-and-execution.md)
  * [Tasks and gotchas](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/references/tasks-and-gotchas.md)
  * [CI/CD promotion](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/references/cicd-promotion.md)



## The Application Integration troubleshooting skill

The Application Integration troubleshooting skill, [`application-integration-troubleshooting`](https://github.com/google/skills/tree/main/skills/cloud/application-integration-troubleshooting), contains instructions for diagnosing failed, stuck, or silent integration runs, such as checking execution and task states, reading logs and metrics, resolving suspensions, checking Integration Connectors connection health, and fixing IAM, run-as service account, and quota errors.

### Install the Application Integration troubleshooting skill

To install the `application-integration-troubleshooting` skill, run the following command in your terminal:
    
    
    npx skills add google/skills --skill application-integration-troubleshooting
    

### Application Integration troubleshooting reference files

By default, the Application Integration troubleshooting skill includes the following reference files:

  * [Execution states](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/references/execution-states.md)
  * [Common errors](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/references/common-errors.md)
  * [Logging and monitoring](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/references/logging-and-monitoring.md)
  * [Suspensions](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/references/suspensions.md)
  * [Connectors health](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/references/connectors-health.md)



## What's next

  * To view the Application Integration basics `SKILL.md` file, see [`SKILL.md` (basics)](https://github.com/google/skills/blob/main/skills/cloud/application-integration-basics/SKILL.md).
  * To view the Application Integration authoring `SKILL.md` file, see [`SKILL.md` (authoring)](https://github.com/google/skills/blob/main/skills/cloud/application-integration-authoring/SKILL.md).
  * To view the Application Integration troubleshooting `SKILL.md` file, see [`SKILL.md` (troubleshooting)](https://github.com/google/skills/blob/main/skills/cloud/application-integration-troubleshooting/SKILL.md).
  * To build an integration by prompting an agent, see [Build an integration with an AI agent](https://docs.cloud.google.com/application-integration/docs/build-integration-ai-agent).
  * To learn more about agent skills, see [Agent Skills Overview](https://agentskills.io/home).
  * To view `SKILL.md` files for other Google Cloud products, see [`google/skills`](https://github.com/google/skills#agent-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
