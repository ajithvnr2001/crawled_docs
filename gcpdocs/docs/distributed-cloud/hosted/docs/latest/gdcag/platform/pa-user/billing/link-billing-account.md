---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/link-billing-account/
title: Link billing account to project \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T05:49:04.021572+00:00
---

# Link billing account to project  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/link-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Link billing account to project Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for linking a billing account to a project in GDC. This allows costs incurred by the project's resources to be tracked and charged to the specified billing account.

## Before you begin

Ask your Organization Identity and Access Management (IAM) Admin to grant you the following required roles:

  * **Global Organization Billing Account Admin** : create, manage, and bind the `BillingAccount` resource in the `platform` namespace. Ask your Organization IAM administrator to grant you the `organization-billing-account-admin` role in the `platform` namespace.

  * **Global Organization Billing Account User** : read, list, and bind the `BillingAccount` resource in the `platform` namespace. Ask your Organization IAM administrator to grant you the `organization-billing-account-user` role in the `platform` namespace.

  * **Global Organization Billing Account Manager** : read, list, create, and update the `BillingAccountBinding` resource across namespaces (such as the `platform` namespace for organization-level billing or a project namespace for project-level billing). Ask your Organization IAM administrator to grant you the `organization-billing-manager` role.


**Note:** Billing for all projects is managed by the same IAM role. To separate billing administration for different projects, one dedicated role is required for each project. Contact your Organization IAM Admin to create additional roles for individual project administration requirements.

### Get the kubeconfig file

To run verification commands against the global API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#global-resources-kubeconfig) the kubeconfig file for the global API server if you don't have one.

**Note:** When managing `BillingAccount` and `BillingAccountBinding` custom resources (CRs) using YAML manifests, note that they are global resources and must be applied to the global API server. Don't apply or modify these YAML files directly using `kubectl apply` or `kubectl edit`. Instead, follow the Git-based Infrastructure as Code (IaC) workflow in the `IAC-R0004: Create and merge a merge request` runbook to commit them to the `infrastructure/global/orgs/ORG_NAME/oc/bil/` directory of the `iac` repository and go through the multi-party approval (MPA) process.

## Create a billing account

If you need to create a new billing account before linking it to a project, follow the instructions in [Create a new billing account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#create-a-new-billing-account).

## Link project to billing account

To associate a project with an existing billing account, see the steps for [Link a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#link-bil-account-to-project-or-org).

## Change the linked billing account for a project

If you need to change the billing account associated with a project, see [Change the linked billing account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts#change-bil-account).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
