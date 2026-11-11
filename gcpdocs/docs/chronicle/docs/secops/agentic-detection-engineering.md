---
url: https://docs.cloud.google.com/chronicle/docs/secops/agentic-detection-engineering/
title: Use the Detection Engineering Agent \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:37:39.925264+00:00
---

# Use the Detection Engineering Agent  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/agentic-detection-engineering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Detection Engineering Agent

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This guide is for security engineers and SOC analysts who want to evaluate and strengthen their Google Security Operations security posture against new and existing threats, using the AI-powered **Detection Engineering Agent** in Google SecOps.

You can access the agent using Model Context Protocol (MCP) tools operated by compatible AI clients (for example, Google Antigravity or Claude Code). Using the Detection Engineering Agent, you can extract threat intelligence and automatically draft [YARA-L](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-overview) rules, which improves time-to-value for custom security automation and accelerates risk mitigation.

## Key terminology

  * **Detection Engineering Agent** : An AI-powered engineering assistant embedded in Google SecOps, operated by AI clients (for example, Antigravity or Claude Code) using MCP tools.
  * **Model Context Protocol (MCP)** : An open-source standard for connecting AI applications to external systems, which is used across Google Cloud services to securely connect AI agents and applications to various data sources and infrastructure tools.
  * **Threat Detection Opportunity (TDO)** : A formalized data model designed to identify, track, and prioritize potential new detection rules or analytics.
  * **Synthetic events** : [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) logs generated to simulate an input TDO.



## Before you begin

Before you begin, confirm the following prerequisites are met:

  * **Environment check—AI client**
  * **Required roles and permissions**



### Environment check — AI client

You must operate an AI client (such as Antigravity or Claude Code) capable of interfacing with MCP tools.

### Required roles and permissions

This section lists the required Identity and Access Management (IAM) permissions and recommended predefined roles for both human users and service accounts.

#### Required roles for all principal users

Every principal calling the Detection Engineering Agent must have the following roles: **MCP Tool User** and **Chronicle API Viewer**. Ensure that a system administrator updates these roles for all principal users.

For more information, see [Configure MCP](https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp).

#### Required core permissions

The following permissions are required to run the Detection Engineering Agent:

  * `chronicle.ade.generateThreatDetectionOpportunity`
  * `chronicle.ade.generateSyntheticEvents`
  * `chronicle.ade.evaluateRuleCoverage`
  * `chronicle.ade.generateRules`
  * `chronicle.operations.get`



#### Required rule management and parser permissions

The following permissions are required to manage rules and parsers:

  * `chronicle.rules.list`
  * `chronicle.rules.get`
  * `chronicle.rules.verify`
  * `chronicle.rules.create`
  * `chronicle.rules.update`
  * `chronicle.ruleDeployments.get`
  * `chronicle.ruleDeployments.update`
  * `chronicle.parsers.list`
  * `chronicle.parsers.get`
  * `chronicle.logTypes.list`



#### Required remote MCP server and project service usage permissions

The following permissions are required to call the remote MCP server and use project services for MCP tools:

  * `mcp.tools.call` (granted by the `roles/mcp.toolUser` role)
  * `serviceusage.services.use` (granted by the `roles/serviceusage.serviceUsageConsumer` role)



#### Required and recommended predefined roles

The following predefined roles provide the necessary permissions for both human users and service accounts:

  * `roles/chronicle.admin` (or `roles/chronicle.editor`)
  * `roles/mcp.toolUser`
  * `roles/serviceusage.serviceUsageConsumer`



## Set up the MCP server

To create your `settings.json` file, see [Configure MCP](https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp). After you collect the required values, make sure that the contents of your `settings.json` file look like the following:
    
    
    {
      "name": "my_extension_name",
      "version": "1.0.0",
      "mcpServers": {
        "GoogleSecOps": {
          "httpUrl": "https://us-chronicle.googleapis.com/mcp",
          "authProviderType": "google_credentials",
          "oauth": {
            "scopes": [
              "https://www.googleapis.com/auth/cloud-platform",
              "https://www.googleapis.com/auth/chronicle"
            ]
          },
          "timeout": 300000,
          "headers": {
            "x-goog-user-project": "my-cloud-project-name"
          }
        }
      }
    }
    

## Set up a context file

To get started, set up a [context](https://geminicli.com/docs/cli/gemini-md/) file to ensure that Gemini targets the correct Google SecOps instance for every request.

To keep everything lightweight, Google recommends starting with the following content in your `GEMINI.md` file and then building from there. Replace the placeholder values with the correct information for your Google SecOps instance and environment:
    
    
    When using the Google SecOps MCP server, use these parameters for EVERY request: Customer ID: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa Region: us Project ID: my-cloud-project-name
    

## Set up the skill to interact with the tools

Google highly recommends using the `detection-engineering-coverage-evaluation` skill to interact with the tools. This skill prevents the AI from summarizing or abbreviating critical tool outputs.

This skill is built-in as `detection-engineering-coverage-evaluation` and is hosted publicly in the [Google Agent Skills GitHub repository](https://github.com/google/skills/blob/main/skills/cloud/detection-engineering-coverage-evaluation/SKILL.md).

**Caution:** Gemini might try to take shortcuts (such as summarizing tool output or overzealously compacting the TDO). Using the `detection-engineering-coverage-evaluation` skill enforces proper iterative execution.

## Key capabilities

This section describes key capabilities for threat analysis and rule generation that the Detection Engineering Agent provides.

### Generate Threat Detection Opportunities

The `generate_threat_detection_opportunity` tool extracts and enriches raw threat intelligence from sources (for example, security blogs and internal findings) to create prioritized TDOs for analysis. The TDOs produced in this step inform the subsequent detection engineering agent steps to evaluate existing rule coverage or generate new rules.

  * To use the `generate_threat_detection_opportunity` tool, instruct Gemini to use `curl` to extract the text, or copy and paste raw text from a threat report into the tool.



### Generate synthetic events

To generate synthetic events for a TDO, your Google SecOps instance must have ingested raw logs and an active parser for at least one of the supported log types in that TDO.

#### Supported log types

Synthetic event generation supports the following eight log types:

Category | Vendor or product | Log type  
---|---|---  
Endpoint detection and response (EDR) | [CrowdStrike Falcon](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr) | `CS_EDR`  
Endpoint detection and response (EDR) | [Microsoft Defender for Endpoint](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint) | `MICROSOFT_DEFENDER_ENDPOINT`  
Endpoint detection and response (EDR) | [SentinelOne EDR](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr) | `SENTINEL_EDR`  
Antivirus and endpoint | [Windows Defender ATP](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp) | `WINDOWS_DEFENDER_ATP`  
DNS | [Zscaler DNS](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dns) | `ZSCALER_DNS`  
Google Cloud | [Google Workspace Activities](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workspace-activity) | `WORKSPACE_ACTIVITY`  
Identity and access management | [Okta](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta) | `OKTA`  
SaaS applications | [Microsoft 365 (Office 365)](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365) | `OFFICE_365`  
  
### Evaluate coverage

The Detection Engineering Agent checks whether existing rules in your Google SecOps instance trigger on simulated events ingested through [event simulation](https://docs.cloud.google.com/chronicle/docs/secops/event-simulation). If any rules match the simulated events, the tool returns the matching rule identifiers and coverage result metadata. If no rules match, an empty result is returned, signaling a coverage gap.

### Generate draft rules

The Detection Engineering Agent codifies detection logic by creating draft YARA-L rules from user input or natural language to address gaps identified during coverage evaluation. When you use the `detection-engineering-coverage-evaluation` skill, the agent generates draft rules only for TDOs that no existing rule matches, and only after coverage evaluation finishes for all TDOs. This prevents duplicate rules for threats that existing rules already cover.

The `generate_rules` tool doesn't automatically add the draft rules to your Google SecOps instance. After you review the draft rules, you can add them in either of the following ways:

  * **Use your AI client** : The `detection-engineering-coverage-evaluation` skill prompts you to approve or reject each draft rule. For each rule that you approve, the AI client calls the `create_rule` tool on the Google SecOps MCP server to create the rule in your instance.
  * **Create the rule manually** : Copy the rule text from the tool output and create the rule in the [Rules Editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules).



## Troubleshooting

Use the following table to self-remediate common issues during the evaluation process:

Issue | Description | Fix  
---|---|---  
**Tool failure** | The `generate_synthetic_events` tool repeatedly fails. | Verify that the TDO includes at least one of the supported log types and that your Google SecOps instance has ingested raw logs and an active parser for that log type. Otherwise, skip synthetic event generation for that TDO and continue with the remaining TDOs.  
**Summarization error** | The AI abbreviates log types or takes shortcuts during execution. | Ensure the `detection-engineering-coverage-evaluation` skill is actively being used to interface with the system.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
