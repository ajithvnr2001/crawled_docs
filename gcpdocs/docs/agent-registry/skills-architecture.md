---
url: https://docs.cloud.google.com/agent-registry/skills-architecture/
title: Skills architecture \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:37.479875+00:00
---

# Skills architecture  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/skills-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Skills architecture Stay organized with collections  Save and categorize content based on your preferences. 

In Agent Registry, skills let you package instructions, optional scripts, and domain knowledge into modular capabilities that extend an agent's reasoning and workflow. By registering standalone skills in Agent Registry, you can centrally version, scan, govern, and share reusable task logic across your agents. Agent Registry also indexes inline [Agent2Agent (A2A)](https://docs.cloud.google.com/agent-registry/a2a-protocol) skills declared on your agents' Agent Cards so other agents can discover and call them.

## Skill types

Agent Registry supports two types of skills:

  * **Standalone skills** : version-controlled packages registered as top-level `Skill` resources in Agent Registry. Standalone skills contain `SKILL.md` instruction files, optional scripts, and metadata assets managed independently of any single agent deployment.
  * **A2A skills** : capability descriptions listed inline in the `skills` field of an agent's `agent-card.json` [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) that tell other agents when and how to delegate work to it.



For a comparison of these two models, see Differences between standalone and A2A skills.

## Standalone skills

Standalone skills are top-level resources in Agent Registry, governed alongside agents, MCP servers, and endpoints. Unlike those components, standalone skills don't use separate [`Service` resources](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#agentic-components-representation). Instead, you register, version, and query standalone skills directly across three resource levels:

  * **Publishers** : `Publisher` resources that establish the ownership, verification tier, and [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) syntax for a collection of skills.
  * **Skill containers** : top-level `Skill` resources in Agent Registry that consumers discover and resolve at runtime, each maintaining a pointer to a default serving revision of the skill.
  * **Skill revisions** : immutable, read-only `SkillRevision` resources containing a skill package's instructions, optional scripts, and metadata assets at a specific version.



### Publishers

Every standalone skill in Agent Registry belongs to a publisher. Publishers establish the provenance, verification tier, and naming prefix for skills:

  * **Google-managed publishers (`FIRST_PARTY`)**: verified publishers that Google manages, such as `cloud.google.com` and `discoveryengine.googleapis.com`. Google-managed skills from these publishers are discoverable across all projects when you set up Agent Registry and use the following [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) format: `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`. For example: `urn:skill:discoveryengine.googleapis.com:discoveryengine:report-writing`.
  * **Private publishers (`PRIVATE`)**: the default `private` publisher automatically assigned to custom skills that you manually register within a Google Cloud [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project). To prevent naming collisions with verified Google-managed skills, Agent Registry automatically prepends the `private-` prefix to the [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers). You can't register custom `Publisher` resources. Private skills use the following Uniform Resource Name (URN) format for the skill identifier: `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-SKILL_ID`. For example: `urn:skill:projects-PROJECT_NUMBER:locations:global:private-incident-triage`.



For instructions on inspecting publishers, see [Review skill publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).

### Skill containers

A skill container is a `Skill` resource that represents a standalone skill within a governance project and location. For a manually created skill, Agent Registry generates a [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) in the format `projects/PROJECT_NUMBER/locations/LOCATION/skills/private-SKILL_ID`.

The `Skill` resource serves as the stable reference point for discovery in Agent Registry and maintains the following fields:

  * **Descriptive metadata** : the human-readable display name (`displayName`), summary description (`description`), [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) (`skillId`), and publisher (`publisher`) attribution. To modify the descriptive metadata of an existing skill, see [Update skill metadata](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).
  * **Default revision pointer** : the `defaultRevision` field, which references the specific `SkillRevision` resource served when you use or download the skill without requesting an explicit revision ID. To modify the default revision of an existing skill, see [Update the default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).
  * **Target lifecycle state** : the `targetState` field, which controls whether the skill is in an active, disabled, deprecated, or decommissioned state. For more information, see Skill lifecycle states. To update the target state for lifecycle transitions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).
  * **Security scanning configuration** : the `scanningConfig.policy` field, which controls whether Agent Registry automatically scans uploaded skill revisions for security issues and blocks downloads or default revision promotions when findings are detected. For more information, see Scanning policies. To update the scanning policy of a skill, see [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).



For instructions on viewing and updating skills, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills) and [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).

### Skill revisions

A skill revision (`SkillRevision`) resource represents an immutable, versioned snapshot of a skill package. The [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) is in the following format: `projects/PROJECT_NUMBER/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID`.

When you update a skill's instructions, optional scripts, or metadata assets, you don't modify the existing package in place. Instead, you upload a new ZIP archive to create a new revision. When Agent Registry validates that the archive meets the [Agent Skills Specification](https://agentskills.io/specification#validation) and [ingestion payload constraints](https://docs.cloud.google.com/agent-registry/register-skills#payload-constraints), the revision enters the **Active** (`ACTIVE`) state.

If security scanning is enabled on the skill, Agent Registry also scans the revision package asynchronously, records the [scan status](https://docs.cloud.google.com/agent-registry/scan-skills#review-scan-status), and publishes any detected findings as read-only `Finding` resources.

You can then [update the default revision pointer](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) on the parent skill to serve the new revision. If you delete the revision that is set as the skill's default revision, Agent Registry clears the default revision pointer and transitions the active skill to the **Disabled** (`DISABLED`) state.

Separating the skill container from its skill revision snapshots provides the following benefits:

  * **Deterministic execution** : agents pinned to a specific revision are protected from unexpected prompt changes or script updates.
  * **Controlled rollbacks** : you can upload and verify new skill revisions, or revert the `defaultRevision` pointer to an earlier revision if an issue occurs.
  * **Auditability** : historical revisions of the skill package remain preserved and inspectable until explicitly deleted.



For instructions on uploading, downloading, and deleting revisions, see [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).

## Package specification

Standalone skills are packaged as ZIP archives that comply with the open standard [Agent Skills Specification](https://agentskills.io/specification).

The archive must contain a `SKILL.md` file at its root, as well as any scripts or metadata assets that are required by the skill. The `SKILL.md` file defines the instructions for the skill. This file combines YAML front matter metadata, such as `name` and `description`, with natural language instructions interpreted by agent runtimes, and references to any optional scripts or supporting assets in the archive.

When you register a skill or create a revision, Agent Registry validates the archive against [ingestion payload constraints](https://docs.cloud.google.com/agent-registry/register-skills#payload-constraints), parses the `SKILL.md` file, and indexes its metadata for search and discovery.

## Skill lifecycle states

To control how a standalone skill is served and downloaded at runtime, you can transition the target state (`targetState`) of the skill container across the following states:

  * **Draft (`DRAFT`)**: the skill is in draft or lacks a revision and isn't served at runtime. A skill also enters the **Draft** state when you create it with an initial revision, a target state of **Active** , and the `ENABLED_BLOCKING` scanning policy while its initial revision scan is pending. Resolution and payload downloads aren't available when a skill is in the **Draft** state.
  * **Active (`ACTIVE`)**: the skill is served, indexed for discovery, and available for runtime resolution and payload downloads. Setting a skill to **Active** requires its default revision to point to an active skill revision or an initial revision provided during skill creation. To update a skill's default revision, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).
  * **Disabled (`DISABLED`)**: the skill isn't served at runtime, and resolution and payload downloads fail immediately. A skill also transitions to the **Disabled** state if its default revision is deleted. Unlike the **Decommissioned** state, you can enable a disabled skill by setting a valid default revision and updating its target state to **Active**.
  * **Deprecated (`DEPRECATED`)**: the skill remains resolvable and downloadable, but indicates that it will be decommissioned after a grace period.
  * **Decommissioned (`DECOMMISSIONED`)**: the skill is permanently deactivated, no longer served, and _can't_ be reverted to **Active** or any other state. A skill can be decommissioned only after it has already been deprecated. Provide sufficient time to migrate before decommissioning the skill. Because this state is terminal, use it with caution.



When you create a skill, the valid target state values for lifecycle transitions and the resulting skill's state depend on whether you provide an initial skill revision and on the skill's scanning policy:

Initial revision | Allowed target state during creation | Scanning policy | Resulting skill state  
---|---|---|---  
**Not provided** : `initialRevision` is omitted | `TARGET_STATE_DRAFT` or `TARGET_STATE_DISABLED` | Any | `STATE_DRAFT` or `STATE_DISABLED` when the long-running operation (LRO) for creating the skill completes.  
**Provided** : `initialRevision` is set as `defaultRevision` | `TARGET_STATE_DRAFT` or `TARGET_STATE_DISABLED` | Any | Sets the initial revision as the parent skill's default revision and places the skill in `STATE_DRAFT` or `STATE_DISABLED` when the LRO for creating the skill completes.  
**Provided** : `initialRevision` set as `defaultRevision` | `TARGET_STATE_ACTIVE` | `DISABLED` or `ENABLED_NONBLOCKING` | Sets the initial revision as the parent skill's default revision and transitions the parent skill directly to `STATE_ACTIVE` when the LRO for creating the skill completes.  
**Provided** : `initialRevision` set as `defaultRevision` | `TARGET_STATE_ACTIVE` | `ENABLED_BLOCKING` (default) | Sets the initial revision as the parent skill's default revision and places the skill in `STATE_DRAFT` when the LRO for creating the skill completes. When the background scan finishes, Agent Registry transitions the parent skill to `STATE_ACTIVE` only if the scan produces no security findings and the parent skill is still in `STATE_DRAFT` with the default revision pointing to the initial revision.  
  
You can update a skill's lifecycle state using the Google Cloud console, the Google Cloud CLI, or the Agent Registry API without deleting historical revisions. To download a revision's ZIP payload, the parent skill must be in the **Active** or **Deprecated** state, and the revision itself must be in the **Active** state. If the skill's scanning policy is set to `ENABLED_BLOCKING`, the revision must also have no security findings. For step-by-step instructions, see [Manage skill lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle).

## Skill security and governance

Agent Registry provides the following security and governance controls for standalone skills.

### Customer-managed encryption keys (CMEK)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Agent Registry encrypts customer content at rest. Agent Registry handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Agent Registry. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your skill revisions with CMEKs, the experience of accessing your Agent Registry skill revisions is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To protect skill payloads at rest with CMEK, configure a `SkillEncryptionSpec` resource for the target supported location, which can be `us` or `eu`. This configuration is optional, but you must configure CMEK before registering any skills in that location. You can't set or update the Cloud Key Management Service key for a location after a skill has been created there, and the key must reside in the corresponding Cloud KMS multi-region, as described in the following section.

#### CMEK limitations and requirements

Before configuring CMEK for skills, review the following requirements and limitations:

  * **Configure CMEK before creating skills in the location** : you can set or update the Cloud KMS key (`cryptoKeyName`) for a location only when no skills exist in that project and location. If any skill already exists in the target location, updating the `SkillEncryptionSpec` fails with a `FAILED_PRECONDITION` error.
  * **Supported skill locations and required Cloud KMS key locations** : CMEK for skills is supported only in the `us` and `eu` skill locations. The Cloud KMS symmetric encryption key that you select must reside in the corresponding Cloud KMS multi-region location shown in the following table:

Skill location | Required Cloud KMS key location  
---|---  
`us` | `us`  
`eu` | `europe`  
  
Cloud KMS uses specific location identifiers that might differ from the identifiers used by Agent Registry for skill locations. You must use the Cloud KMS key location identifier. If you specify a key in any other location, such as `global` or a single region, then the request fails with an `INVALID_ARGUMENT` error.

  * **Service agent permissions** : before configuring CMEK or uploading skill revisions in a CMEK-enabled location, you must grant the Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the Cloud KMS key to your project's Agent Registry service agent: `service-PROJECT_NUMBER@gcp-sa-agentregistry.iam.gserviceaccount.com`. If the service agent doesn't exist in your project yet, create it by following the steps in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).

  * **IAM permissions** : to view the `SkillEncryptionSpec` resource, you must have the `agentregistry.skillEncryptionSpecs.get` permission, which is included in the Agent Registry API Viewer (`roles/agentregistry.viewer`) role. To set or update the `SkillEncryptionSpec` resource, you must have the `agentregistry.skillEncryptionSpecs.update` permission, which is included in the Agent Registry API Admin (`roles/agentregistry.admin`) role.




#### Enforce CMEK using Organization Policy Service

You can use [CMEK organization policy constraints](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to require CMEK protection for skills and restrict which Cloud KMS keys can be used across your organization, folder, or project. Agent Registry evaluates these constraints when creating a skill or skill revision, and not when configuring or updating the `SkillEncryptionSpec` resource:

  * **Require CMEK protection ([`constraints/gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek))**: add `agentregistry.googleapis.com` to the `deniedValues` list of the `constraints/gcp.restrictNonCmekServices` constraint. When this policy is enforced, Agent Registry rejects requests to create skills or skill revisions in any location that doesn't have a `SkillEncryptionSpec` resource configured.
  * **Restrict allowed Cloud KMS projects ([`constraints/gcp.restrictCmekCryptoKeyProjects`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#restrict-cmek-projects))**: configure the `allowedValues` list on the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint, for example, `under:projects/KMS_PROJECT_ID`, `under:folders/FOLDER_ID`, or `under:organizations/ORGANIZATION_ID`. When this policy is enforced in a CMEK-enabled location, Agent Registry verifies that the Cloud KMS key configured in the location's `SkillEncryptionSpec` resource belongs to an allowed project before creating skills or skill revisions.



Because Agent Registry evaluates `constraints/gcp.restrictCmekCryptoKeyProjects` when you create a skill or skill revision rather than when you configure the `SkillEncryptionSpec` resource, verify that your Cloud KMS key resides in a project allowed by your organization policy before creating skills in that location. If you apply or update `constraints/gcp.restrictCmekCryptoKeyProjects` after configuring CMEK so that the configured key's project is no longer allowed, subsequent skill and skill revision creations in that location fail with a `FAILED_PRECONDITION` error. Additionally, because you can update a `SkillEncryptionSpec` resource only when no skills exist in the location, switching to a key in a different project requires deleting all existing skills in that location first.

For instructions on configuring these constraints, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

### Scanning policies

You configure scanning behaviors at the skill level, so scanning configuration is set directly on each `Skill` resource. Scanning configuration is decoupled from the lifecycle state of the skill, letting you independently adjust security enforcement.

Configuring any scanning policy is subject to your organization's security policies. If an organization policy constraint is applied to your organization or folder, such as requiring blocking enforcement, you can configure only scanning policies permitted by that constraint.

Agent Registry supports the following scanning policies for skills:

  * **Enabled (Blocking) (`ENABLED_BLOCKING`)**: defines the default blocking policy. Agent Registry automatically scans every uploaded skill revision for security risks such as unauthorized data exfiltration, exposed credentials, and prompt injection. If the scan detects security findings, Agent Registry blocks downloading the skill's revision archive and prevents promoting the revision as the default revision. Detected issues are exposed as read-only `Finding` resources in your governance project: `projects/PROJECT_NUMBER/locations/LOCATION/findings/FINDING_ID`. Setting a revision as the default revision is also blocked when its scan results are pending. If you create a skill with an initial revision and set its target state to **Active** , the skill starts in the **Draft** state when creation completes. The skill automatically transitions to **Active** in the background only if the scan completes with no findings and the skill is still in the **Draft** state with the default revision pointing to that initial revision.
  * **Enabled (Non-blocking) (`ENABLED_NONBLOCKING`)**: operates in an audit mode. Revisions are scanned and findings are published to Agent Registry, but downloads and default version promotions are permitted with warning notices.
  * **Disabled (`DISABLED`)**: disables scanning entirely. Revisions uploaded to the skill aren't scanned.



To learn how Agent Registry applies enforcement rules based on the scanning policy, see Understand policy enforcement points. To configure a scanning policy, see [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).

#### Understand policy enforcement points

The following table describes how Agent Registry applies enforcement rules for each operation based on the skill's scanning policy. To manage default revisions and lifecycle states for skills, see [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

Operation | `ENABLED_BLOCKING` (default) | `ENABLED_NONBLOCKING` | `DISABLED`  
---|---|---|---  
**Creating a skill with an initial revision and active target state** (`TARGET_STATE_ACTIVE`) | Sets the initial revision as the parent skill's default revision (`defaultRevision`), but places the skill in the `STATE_DRAFT` state when the long-running operation (LRO) for creating the skill completes. When scanning finishes, Agent Registry transitions the parent skill to `STATE_ACTIVE` only if the scan produces no security findings and the parent skill is still in `STATE_DRAFT` with the default revision pointing to the initial revision. | Sets the initial revision as the parent skill's default revision and transitions the parent skill's state to `STATE_ACTIVE` as soon as the LRO for creating the skill completes. | Sets the initial revision as the parent skill's default revision and transitions the parent skill's state to `STATE_ACTIVE` as soon as the LRO for creating the skill completes.  
**Downloading a revision payload** | Attempting to download a revision's ZIP payload when the revision has security findings fails with a `FAILED_PRECONDITION` error. | Permitted even if findings are present, with high-visibility security warning notices referencing the findings. | Permitted without scanning checks.  
**Promoting a revision as the default revision** (`defaultRevision`) | Attempting to set a revision as the skill's default revision when the revision has security findings or when its scan results are still pending fails with a `FAILED_PRECONDITION` error. | Permitted even if findings are present or scan results are pending, with high-visibility security warning notices referencing any findings. | Permitted without scanning checks.  
**Updating the skill's scanning policy** (`scanningConfig.policy`) | Attempting to update a skill's scanning policy to `ENABLED_BLOCKING` when its current default revision has security findings, pending scan results, or failed or incomplete scan results fails with a `FAILED_PRECONDITION` error. You must first update the default revision to a revision that has completed scanning with no findings. | Permitted, unless restricted by an organization policy constraint, regardless of the scan status of the current default revision. | Permitted, unless restricted by an organization policy constraint, regardless of the scan status of the current default revision.  
  
### Organization policy enforcement

You can establish organization-wide governance to prevent skill registration with scanning disabled. Agent Registry doesn't provide built-in managed constraints for skill scanning. You must define a custom organization policy constraint.

By configuring a custom organization policy constraint on the `Skill` resource, you can deny setting the scanning policy to `DISABLED` while, for example, conditionally allowing exemptions for testing environments using Resource Manager tags.

#### Supported capabilities and limitations

When configuring custom organization policy constraints for Agent Registry skill scanning, consider the following capabilities and limitations:

The following capabilities are supported:

  * **Scanning settings** : you can create or update custom organization policy constraints only for scanning policy settings on `Skill` resources.
  * **Common Expression Language (CEL) attribute** : all values for scanning policies are supported for CEL expressions. When you create a skill without specifying a scanning policy, Agent Registry uses the system default value for the scanning policy, which is `ENABLED_BLOCKING`, before evaluating the custom constraint.
  * **Policy actions** : the action type for the custom constraint supports standard boolean rules, for example, `custom.skillsScanningEnforcement` denying `resource.scanningConfig.policy == "DISABLED"`.
  * **Conditional exemptions** : you can use standard Resource Manager tags with CEL expressions in the organization policy rule, for example, exempting projects tagged with `exempt-scanning-enforcement: true`.



The following are limitations for custom organization policy constraints:

  * **No skill revision or payload inspection** : custom organization policies can't inspect `SkillRevision` resources, file contents, uncompressed package sizes, or security findings. Uncompressed size limits and findings gating are enforced by Agent Registry at runtime.
  * **No retroactive modification of existing skills** : enforcing a custom constraint doesn't retroactively modify existing skills. However, when you update an existing skill, Agent Registry evaluates the custom constraint against the resulting state of the `Skill` resource. If an existing skill has a scanning policy set to `DISABLED`, any subsequent update to that skill is denied unless the update also sets the scanning policy to a compliant value.



To enforce organization-wide scanning policies, see [Enforce scanning using Organization Policy Service](https://docs.cloud.google.com/agent-registry/scan-skills#org-policy).

## Differences between standalone and A2A skills

Agent Registry supports both standalone skills and inline A2A skills. The following table compares their characteristics:

Characteristic | Standalone skill | Inline A2A skill  
---|---|---  
**Resource type** | Top-level `Skill` resource in Agent Registry with child `SkillRevision` resources. | Nested array within the `Agent` resource.  
**Package content** | ZIP archive containing `SKILL.md`, optional scripts, and supporting assets. | JSON object in the Agent Card containing `id`, `name`, and `description`.  
**Versioning model** | Immutable skill revision snapshots with a configurable `defaultRevision` pointer. | Tied directly to updates of the agent's `agent-card.json`.  
**Execution model** | Downloaded and loaded into an agent's context or runtime environment. | Advertises task capabilities for inter-agent delegation.  
**Specification** | [Agent Skills Specification](https://agentskills.io/specification). | [Agent2Agent (A2A) specification](https://a2a-protocol.org/).  
**Governance scope** | Governed across projects independently of individual agent deployments. | Coupled to the lifecycle of the host agent deployment.  
  
For more information about how Agent Registry indexes Agent Cards, A2A transport bindings, and task lifecycle states, see [A2A protocol](https://docs.cloud.google.com/agent-registry/a2a-protocol).

## What's next

  * [Register skills](https://docs.cloud.google.com/agent-registry/register-skills).
  * [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).
  * [Manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions).
  * [Scan skills for security issues](https://docs.cloud.google.com/agent-registry/scan-skills).
  * [Review skill publisher details](https://docs.cloud.google.com/agent-registry/review-publishers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
