---
url: https://docs.cloud.google.com/docs/migration/plan/landing-zones/
title: Enterprise landing zones and foundations \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:51.625110+00:00
---

# Enterprise landing zones and foundations  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/plan/landing-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Enterprise landing zones and foundations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the design principles, implementation options, and security blueprints used to establish enterprise landing zones on Google Cloud.

If you are a cloud architect, security administrator, or platform engineer, use the information on this page to evaluate landing zone deployment models, establish resource hierarchies, configure identity federation and hybrid networking, and enforce compliance controls before executing workload migrations.

Before you read this page, you should have a basic understanding of your organization's governance model, network topology, and compliance requirements.

## Landing zone implementation options

Google Cloud provides a structured progression of tools for building landing zones, as shown in the following diagram:

![Architecture diagram illustrating the progression from Google Cloud Setup guided flow to Infrastructure as Code and the Enterprise Foundations Blueprint.](https://docs.cloud.google.com/docs/migration/images/landing-zone-progression.svg)

### Guided setup with Google Cloud Setup

For small teams or initial pilot migrations, the [Google Cloud Setup guided flow](https://docs.cloud.google.com/docs/enterprise/cloud-setup) provides interactive console guidance to configure basic organization settings, billing accounts, administrative users, and initial project structures.

### Infrastructure as Code with Cloud Foundation Toolkit or Fabric

For repeatable, automated enterprise deployments, construct landing zones by using Infrastructure as Code (IaC) templates based on the following toolkits:

  * **[Foundation Toolkit (CFT)](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints)** : a collection of modular, production-ready Terraform blueprints created by Google Cloud that enforce standard security and networking patterns.
  * **[Cloud Foundation Fabric (CFF)](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric)** : an open-source suite of composable Terraform modules and end-to-end blueprint examples designed for fast implementation of enterprise environments.



### Enterprise foundations blueprint

For enterprise organizations requiring advanced security boundaries and compliance guardrails, deploy the [Enterprise Foundations Blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). Based on Foundation Toolkit modules, this blueprint provides the following features:

  * **Organizational hierarchy** : structured folders for development, staging, and production workloads.
  * **Identity and access management** : Cloud Identity federation and strict Identity and Access Management (IAM) role assignments.
  * **Hybrid networking** : Shared VPC network with Partner Interconnect or Dedicated Interconnect and Cloud DNS routing.
  * **Perimeter guardrails** : enforced organization policies and VPC Service Controls to prevent data exfiltration.



## Compliance framework mapping

When migrating regulated workloads to Google Cloud, map on-premises security controls to the following cloud security features:

  * **PCI-DSS and HIPAA compliance** : enforce VPC Service Controls perimeters and use [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs) to manage data residency and encryption keys.
  * **FedRAMP compliance** : deploy pre-configured FedRAMP landing zones by using [Assured Workloads control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate).
  * **Audit reporting** : enable [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) and export logs to [BigQuery](https://docs.cloud.google.com/bigquery/docs) for compliance reporting.



## Reference architectures

For architectural patterns, security controls, and design guides, see the following resources in the Google Cloud Architecture Center:

  * [Migration to Google Cloud: Building your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Google Cloud Landing Zone Design Guide](https://docs.cloud.google.com/architecture/landing-zones)
  * [Enterprise Security Foundations Blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations)
  * [Google Cloud Deployment Archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes)
  * [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)



## What's next

  * [Virtual machine migration](https://docs.cloud.google.com/docs/migration/scenarios/virtual-machine-migration.md)
  * [Database migration](https://docs.cloud.google.com/docs/migration/scenarios/database-migration.md)
  * [Unstructured data and storage migration](https://docs.cloud.google.com/docs/migration/scenarios/data-storage-migration.md)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
