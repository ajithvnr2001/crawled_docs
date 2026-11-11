---
url: https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview/
title: AI Protection overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:29:04.330613+00:00
---

# AI Protection overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  AI Protection overview Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

AI Protection helps you manage the security posture of your AI workloads across your Google Cloud environment. You can use it to gain visibility into your AI inventory, detect threats, and mitigate risks to your AI systems.

AI Protection is available with organization-level and project-level activations of Security Command Center. Based on your activation scope, the **AI Security** dashboard in the Google Cloud console shows aggregated data across all projects and resources or data for the selected project.

## Capabilities of AI Protection

AI Protection helps you manage threats and risks to components in your AI systems. Your service tier determines the available capabilities, which include the following:

  * **Assess your AI asset inventory** : understand your AI systems and assets.
  * **Identify vulnerabilities** (Premium and Enterprise (Deprecated) service tiers): identify software vulnerabilities (CVEs) and plaintext secrets in agentic workloads deployed with Agent Runtime.
  * **Identify risks** (Premium and Enterprise (Deprecated) service tiers): identify risks and their impact on the ecosystem based on Attack Path Simulation and predefined security graph rules, with agents and MCP servers as high-value resources.
  * **Detect over-privileged agents** : detect Agent Runtime agents that are granted excessive permissions.
  * **Manage compliance** : proactively verify that AI assets in your deployments adhere to relevant security standards. The Standard service tier includes baseline security findings with [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials), while Premium and Enterprise service tiers include advanced framework compliance.
  * **Detect and manage threats** : detect and respond to potential threats to your AI systems and assets in a timely manner.



## Use cases for AI Protection

AI Protection helps organizations enhance their security by identifying and mitigating threats and risks related to AI systems and sensitive data. The following use cases are examples of how AI Protection can be used in different organizations:

  * **Financial services institution: customer financial data**

A large financial services institution uses AI models that process sensitive financial data.

    * **Challenge:** processing highly sensitive financial data with AI models entails several risks, including the risk of data breaches, data exfiltration during training or inference, and vulnerabilities in the underlying AI infrastructure.
    * **Use case:** AI Protection continuously monitors AI workflows for suspicious activity, works to detect unauthorized data access and anomalous model behavior, performs sensitive data classification, and aids in improving your compliance with regulations such as PCI DSS and GDPR.
  * **Healthcare provider: patient privacy and compliance**

A major healthcare provider manages electronic health records and uses AI for diagnostics and treatment planning, dealing with Protected Health Information (PHI).

    * **Challenge:** PHI analyzed by AI models is subject to strict regulations like HIPAA. Risks include accidental PHI exposure through misconfigurations or malicious attacks that target AI systems for patient data.
    * **Use case:** AI Protection identifies and alerts on potential HIPAA violations, detects unauthorized PHI access by models or users, flags vulnerable and potentially misconfigured AI services, and monitors for data leakage.
  * **Manufacturing and robotics company: proprietary intellectual property**

A manufacturing company specializing in advanced robotics and automation relies heavily on AI for optimizing production lines and robotic control, with vital intellectual property (IP) embedded within its AI algorithms and manufacturing data.

    * **Challenge:** proprietary AI algorithms and sensitive operational data are vulnerable to theft from insider threats or external adversaries, potentially leading to competitive disadvantage or operational disruption.
    * **Use case:** AI Protection monitors for unauthorized access to AI models and code repositories, detects attempts to exfiltrate trained models and unusual data access patterns, and flags vulnerabilities in AI development environments to prevent IP theft.



## Detection services in AI Protection

The following section describes rules and detection services that create findings when you enable AI Protection. Both the Security Command Center service tier and activation scope (organization-level or project-level) determine which detection services Security Command Center supports and the findings that are created. Security Command Center automatically enables some detection services, but you must manually configure others. For more information, see [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection).

### AI Discovery service

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This is a built-in service that uses Cloud Monitoring data to discover AI models and determine whether Model Armor protects models. On the Standard service tier, AI Discovery doesn't support the detection of [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models.

For information about findings that this service creates, see [AI Discovery service findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#aip-ds-findings).

### Compliance Manager frameworks

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

AI Protection uses Compliance Manager frameworks that Security Command Center deploys automatically in [detective mode](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#cm-scan-types).

#### Compliance Manager built-in frameworks

AI Protection includes the following frameworks. When you enable AI Protection, Security Command Center automatically enables these frameworks in your organization or project.

  * [Security Essentials framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) is available on the Standard, Premium, and Enterprise service tiers.

  * [Google Recommended AI Essentials - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#aipp) is available on Premium and Enterprise service tiers.




Depending on your service tier, you can configure additional Compliance Manager [frameworks and cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#built-in-frameworks). For more information about Compliance Manager, see [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview).

#### Compliance Manager custom frameworks

You can create custom frameworks by making copies of built-in frameworks available on your service tier.

  * **Customization:** you can add or remove cloud controls in your custom frameworks to match your security policies.
  * **Targeted application:** you can apply custom frameworks to specific organizations, folders, or projects. For example, you can apply specific jurisdictional controls to specific folders to ensure that data remains within a particular geographical region.
  * **Limitation:** you cannot assign AI Protection frameworks to applications.



### Event Threat Detection rules for Gemini Enterprise Agent Platform assets

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Event Threat Detection detects several potential threats involving Gemini Enterprise Agent Platform assets, such as anomalous service account activity, sensitive permission changes, and agentic identity abuse.

Finding categories that apply to AI assets include the following:

  * [ `Credential Access: AI Agent Anomalous Access to Metadata Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-anomalous-access-to-metadata-service)
  * [ `Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-folder)
  * [ `Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-org)
  * [ `Defense Evasion: Project Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-project)
  * [ `Discovery: AI Agent Service Account Self-Investigation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-iam-anomalous-behavior-service-account-gets-own-iam-policy)
  * [ `Discovery: AI Agent Unauthorized Service Account API Call`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-unauthorized-service-account-api-call)
  * [ `Discovery: Evidence of Port Scanning from AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-port-scanning-evidence)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Extraction`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil-to-cloud-storage)
  * [ `Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-vpc-violation)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-external)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-public)
  * [ `Impact: Gemini Discovery Engine API Document Import by External User`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gemini-discovery-engine-api-document-import-by-external-user)
  * [ `Impact: Gemini Discovery Engine API Document Import from External Resource`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gemini-discovery-engine-api-document-import-from-external-resource)
  * [ `Impact: Gemini Discovery Engine API Document Import VPC Perimeter Violation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gemini-discovery-engine-api-document-import-vpc-perimeter-violation)
  * [ `Initial Access: AI Agent Identity Excessive Permission Denied Actions`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-excessive-failed-attempt)
  * [ `Initial Access: Dormant Service Account Activity in AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-dormant-service-account-used-in-action)
  * [ `Persistence: External Access Granted to Gemini Discovery Engine API Apps`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-access-granted-to-gemini-discovery-engine-api-apps)
  * [ `Persistence: New AI API Method`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-behavior-new-api-method)
  * [ `Persistence: New Geography for AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-iam-anomalous-behavior-ip-geolocation)
  * [ `Persistence: Sensitive AI Permission Added to Custom Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-ai-permission-added-to-custom-role)
  * [ `Persistence: Sensitive Role Granted by AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-granted-by-ai-agent)
  * [ `Persistence: Sensitive Role Granted to External AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-ai-agent-granted-sensitive-role)
  * [ `Privilege Escalation: AI Agent Cross-Project Access Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-access-token)
  * [ `Privilege Escalation: AI Agent Cross-Project OpenID Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-openid)
  * [ `Privilege Escalation: AI Agent Token Generation Using Implicit Delegation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-implicit-delegation)
  * [ `Privilege Escalation: AI Agent Token Generation Using signJwt`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-sign-jwt)
  * [ `Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonation-of-sa-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-data-access)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-admin-activity)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-data-access)



For a full list of Event Threat Detection findings that apply to AI assets, see [Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

### Agent Platform Threat Detection for Agent Runtime

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Threat Detection ([Preview](https://cloud.google.com/products/#product-launch-stages)) provides runtime threat detection for agents deployed to Agent Runtime. It monitors running agents for potential attacks and generates findings in Security Command Center.

Agent Platform Threat Detection generates findings for Agent Runtime, including the following categories:

  * [ `Command and Control: Steganography Tool Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-steganography-tool-detected)
  * [ `Credential Access: Find Google Cloud Credentials`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-find-gcp-credentials)
  * [ `Credential Access: GPG Key Reconnaissance`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-gpg-key-reconnaissance)
  * [ `Credential Access: Search Private Keys or Passwords`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-search-private-keys-or-passwords)
  * [ `Defense Evasion: Base64 ELF File Command Line`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-elf-file-cmdline)
  * [ `Defense Evasion: Base64 Encoded Python Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-encoded-python-script-executed)
  * [ `Defense Evasion: Base64 Encoded Shell Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-encoded-shell-script-executed)
  * [ `Defense Evasion: Launch Code Compiler Tool In Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-launch-code-compiler-tool-in-container)
  * [ `Execution: Added Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-binary-executed)
  * [ `Execution: Added Malicious Library Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-library-loaded)
  * [ `Execution: Added Malicious Skill Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-skill-executed)
  * [ `Execution: Added Malicious Skill Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-skill-loaded)
  * [ `Execution: Built in Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-built-in-malicious-binary-executed)
  * [ `Execution: Container Escape`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-container-escape)
  * [ `Execution: Fileless Execution in /memfd:`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-fileless-execution-detection-memfd)
  * [ `Execution: Kubernetes Attack Tool Execution`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-kubernetes-attack-tool-execution)
  * [ `Execution: Local Reconnaissance Tool Execution`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-local-reconnaissance-tool-execution)
  * [ `Execution: Malicious Python Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-python-executed)
  * [ `Execution: Modified Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-binary-executed)
  * [ `Execution: Modified Malicious Library Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-library-loaded)
  * [ `Execution: Modified Malicious Skill Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-skill-executed)
  * [ `Execution: Modified Malicious Skill Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-skill-loaded)
  * [ `Execution: Netcat Remote Code Execution in Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-netcat-remote-code-execution-in-container)
  * [ `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-possible-arbitrary-command-execution-through-cups)
  * [ `Execution: Possible Remote Command Execution Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-possible-remote-command-execution-detected)
  * [ `Execution: Program Run with Disallowed HTTP Proxy Env`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-program-run-with-disallowed-http-proxy-env)
  * [ `Execution: Socat Reverse Shell Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-socat-reverse-shell-detected)
  * [ `Execution: Suspicious OpenSSL Shared Object Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-suspicious-openssl-shared-object-loaded)
  * [ `Exfiltration: Launch Remote File Copy Tools in Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-launch-remote-file-copy-tools-in-container)
  * [ `Impact: Detect Malicious Cmdlines`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-detect-malicious-cmdlines)
  * [ `Impact: Remove Bulk Data from Disk`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-remove-bulk-data-from-disk)
  * [ `Impact: Suspicious crypto mining activity using the Stratum Protocol`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-detect-crypto-miners-using-stratum-protocol)
  * [ `Malicious Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-script-executed)
  * [ `Malicious URL Observed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-url-observed)
  * [ `Privilege Escalation: Attempt to Abuse Sudo For Privilege Escalation (CVE-2019-14287)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-abuse-sudo-for-privilege-escalation)
  * [ `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-polkit-local-privilege-escalation-vulnerability)
  * [ `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-sudo-potential-privilege-escalation)
  * [ `Reverse Shell`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-reverse-shell)
  * [ `Unexpected Child Shell`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-unexpected-child-shell)



Learn more about [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview).

### Agent Platform Vulnerability Assessment

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Vulnerability Assessment ([Preview](https://cloud.google.com/products/#product-launch-stages)) identifies vulnerabilities and plaintext secrets, such as credentials, keys, access tokens, or certificates, in Gemini Enterprise Agent Platform container images.

For more information, see [Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#aevs) in "Detection Services".

### Notebook Security Scanner

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Notebook Security Scanner ([Preview](https://cloud.google.com/products/#product-launch-stages)) scans Colab Enterprise notebooks to detect vulnerabilities in Python packages.

For information, see [Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) in "Detection Services".

### Sensitive Data Protection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Sensitive Data Protection discovery service is a fully managed Google Cloud service that helps you discover, classify, and protect your sensitive data. You can use Sensitive Data Protection to determine whether you're storing sensitive or personally identifiable information (PII).

For more information, see [Sensitive Data Protection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp) in "Detection Services".

### Model Armor

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

After you enable Model Armor and [configure Model Armor](https://docs.cloud.google.com/model-armor/integrations) to integrate with one or more AI-related components, you can investigate Model Armor findings in Security Command Center.

On the Security Command Center Standard service tier, AI Protection doesn't support [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models.

To configure Model Armor, see [Create and manage templates](https://docs.cloud.google.com/model-armor/manage-templates).

### Risk Engine

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Risk Engine is a feature in Security Command Center that assesses the risk exposure of your cloud deployments, assigns attack exposure scores to vulnerability findings and your high-value resources, and diagrams paths that a potential attacker could take to reach your high-value resources.

For more information, see [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#risk-engine) in "Detection Services".

## Supported resources in AI Protection

AI Protection discovers assets using the following mechanisms:

  * Declarative AI assets: assets that AI lifecycle management tools (such as Gemini Enterprise Agent Platform) track.
  * Inferred AI assets: general-purpose assets (such as compute and storage assets) that process AI data or workloads.
  * Model-as-a-Service (API only): assets that make programmatic calls into first-party or third-party AI models.



This section defines supported AI inventory and assets that AI Protection can help secure.

  * **Gemini Enterprise & Agent search apps**: these are AI systems that can perceive their environment, make decisions, and take actions to achieve specific goals.
  * **Endpoints** : AI application workloads range from internal tools aimed at improving employee productivity to consumer-facing solutions designed to enhance the user experience and drive business. Examples include AI agents, virtual assistants, conversational AI chatbots, and personalized recommendations. AI Protection identifies these as **Agent Platform endpoints** in the **AI resources** tab on the **Assets page**.
  * **Data sources** : supported data sources include BigQuery tables, Cloud Storage, Agent Platform datasets, and Gemini Enterprise datastores.
  * **Models** : AI Protection identifies AI models as foundation AI models, fine-tuned AI models, standard first-party AI models, and custom AI models. Examples include the following: 
    * [Gemini](https://docs.cloud.google.com/gemini/docs/overview) (available on Premium and Enterprise (Deprecated) service tiers)
    * [Llama](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama)
    * [translation models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/translate/translate-text)
    * Custom models for specific tasks
  * **AI assets** : AI assets contribute to machine learning operation pipelines and are used by AI workloads. Types of AI assets include the following:
  * **Model Context Protocol (MCP) servers** : AI Protection identifies MCP servers that are cataloged in [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry). To use this feature, you must [configure App Hub API](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection#configure-app-hub) in each project that hosts an MCP server.



## Impacts from service tier changes

If you downgrade the service tier from Premium or Enterprise to Standard, the downgrade affects your AI Protection capabilities as follows:

  * **Detection services** : Security Command Center disables detection services and Compliance Manager frameworks that the Standard tier doesn't support. For more information, see [Manage service tiers in Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#manage-service-tiers).
  * **Investigative features** : you lose access to advanced investigative features, such as attack path simulations for AI assets, agent vulnerability assessment, and detection of over-privileged agents.
  * **Findings become inactive:** findings created by Compliance Manager frameworks that are not supported on the Standard tier become inactive. For more information, see [Manage service tiers in Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable#manage-service-tiers).



If you upgrade back to the Premium or Enterprise tier, Security Command Center restores the advanced features, but doesn't automatically recover any framework deployments that were removed during the downgrade. You must manually redeploy the frameworks.

## What's next

  * [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection)
  * [Review AI security](https://docs.cloud.google.com/security-command-center/docs/review-ai-security)
  * [Assess risk using dashboard data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
