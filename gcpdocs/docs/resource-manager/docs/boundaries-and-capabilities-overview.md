---
url: https://docs.cloud.google.com/resource-manager/docs/boundaries-and-capabilities-overview/
title: Management boundaries overview \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:39:11.957851+00:00
---

# Management boundaries overview  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/boundaries-and-capabilities-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Management boundaries overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document introduces management boundaries and capability configurations in Resource Manager. Management boundaries establish dynamic, tag-based administrative perimeters across multiple Google Cloud projects, allowing centralized governance and discovery from a designated management project.

## Management boundaries and the hub-and-spoke model

In addition to static folder hierarchy containment, Resource Manager supports a dynamic, tag-partitioned hub-and-spoke management model:

  * **Management project (Hub)** : A centralized Google Cloud project that hosts the control plane, management APIs, metadata, and cross-project views for services enabled in a `CapabilityConfig`.
  * **Member projects (Spokes)** : Google Cloud projects across folders or the organization that contain workloads, services, and resources. Projects join a boundary dynamically when you attach matching resource tags.



This model decouples administrative management scopes from the physical folder hierarchy, enabling cross-folder governance for distributed teams and multi-project architectures.

## Core resources

Tag-based management boundaries can be defined at either the organization or folder level using three Resource Manager resources:

  * **Boundary configuration (`BoundaryConfig`)**: Defined at the organization or folder level. Establishes the partitioning tag key (for example, `123456789012/env`) used to classify member projects. If no tag key is configured, a boundary under that parent includes all descendant projects.
  * **Boundary (`Boundary`)**: A logical partition within an organization or folder. Projects with matching effective tag values (for example, `env=prod`), or all descendant projects when no tag key is configured on the parent `BoundaryConfig`, are dynamically included in the boundary.
  * **Capability configuration (`CapabilityConfig`)**: Defined at the organization, folder, or project level. At the organization or folder level, it associates one or more boundaries with a designated management project and specifies the management capabilities enabled across the perimeter. At the project level, it enables management capabilities for a single standalone project without boundaries.



## Supported capabilities

Capability configurations support the following management experiences:

  * **`AGENT_MANAGEMENT` (gcloud CLI: `agent-management`)**: Enables centralized discovery, identity registry, and cross-project agent governance in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview).



## Dynamic membership and tag inheritance

Project membership in a boundary updates dynamically in response to tag and resource hierarchy changes:

  1. **Tag binding** : When you bind a matching tag value to a project, the project immediately joins the boundary. If the boundary is associated with a `CapabilityConfig`, the services enabled in that `CapabilityConfig` discover and manage the project's resources through the `CapabilityConfig`'s management project.
  2. **Tag inheritance** : Tags attached to parent folders or organizations are inherited by child projects. Child projects inherit boundary membership unless explicitly overridden with a different tag value.
  3. **Tag removal or update** : When you unbind or change a project's tag, the project is removed from the boundary without deleting the underlying infrastructure.
  4. **Project and folder life cycle changes** : When a project is created, undeleted, or moved into the folder or organization (directly or as part of a folder move) and matches the boundary criteria (matching tag filter, or no tag key configured on the parent `BoundaryConfig`), it is automatically included in the boundary. When a project is deleted or moved out, it is automatically removed from the boundary.



Within a single parent folder or organization, boundaries are mutually exclusive. Because a parent node's `BoundaryConfig` uses a single tag key and a project can have only one effective tag value per tag key, a project can belong to at most one boundary per parent node. If you configure boundaries on multiple ancestor nodes in the resource hierarchy (for example, on an organization and a child folder), a descendant project can belong to at most one boundary at each ancestor level.

## What's next

  * [Configure management boundaries](https://docs.cloud.google.com/resource-manager/docs/manage-capability-configs)
  * [Learn about creating tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing)
  * [Learn about Agent Registry](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
