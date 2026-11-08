---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration/
title: Egress Control \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T09:12:40.227210+00:00
---

# Egress Control  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Egress Control Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

To control egress, you must have the necessary identity and access roles:

  * Project Editor: has access to manage and delete projects. Ask your IAM Org Admin to grant you the Project Editor (`project-editor`) role.



## Enforce no-egress traffic policy

By default, the no-egress traffic policy is enforced when a new project is created. You can ensure that this policy is enforced at the time you create a project.

###  Console 

To enforce the no-egress traffic policy, follow these steps when creating a project:

  1. Within the GDC console, navigate to **Projects**.
  2. Click the add **Add Project** button to create a project.
  3. Complete the required information for your project on the **Project name** and **Attach clusters** pages.
  4. On the **Network** page, under the **Egress Control** section, ensure the **Enforce no-egress traffic policy** checkbox is checked.
  5. Click **Next**.
  6. Review the details on the **Review** page.
  7. Click **Create**.



###  API 

By default, the no-egress traffic policy is enforced when you create a project. To enforce the no-egress traffic policy by using the API, ensure that the project metadata doesn't contain the `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org` label. If the label is already present, remove it.

**Caution:** Don't add the `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org` label to enforce the no-egress traffic policy. The system checks only for the presence of this label key and ignores its value. Setting it to any value, including `"false"`, disables the no-egress traffic policy and allows default outbound traffic outside the organization.
    
    
    apiVersion: resourcemanager.global.gdc.goog/v1
    kind: Project
    metadata:
      name: PROJECT_NAME
      namespace: platform
    

## Allow egress traffic

By default, a project enforces a no-egress traffic policy. The following are the default policies for a project with the no-egress traffic policy enforced:

  * Allow inbound traffic only from the same project. All other traffic is denied.
  * Allow outbound traffic to all destinations within the same organization. All other traffic is denied, which means that external traffic outside your organization is denied.



When the no-egress traffic policy is enforced, it blocks all egress traffic from the project to any destination outside the organization. This overrides any Project Network Policies (PNPs) that might otherwise allow egress traffic.

If you allow egress traffic by clearing the corresponding checkbox in the GDC console for a project, the default policies for the project are the following:

  * Allow inbound traffic only from the same project. All other traffic is denied.
  * Allow outbound traffic to all destinations, including external projects from other organizations.




###  Console 

Work through the following steps to allow egress traffic for a project:

  1. In the GDC console, go to **Projects** in the navigation menu.
  2. Click the name of the project where you want to allow egress traffic.
  3. Click edit **Edit** on the **Egress Control** field.
  4. On the **Edit Egress Control** page, clear the **Enforce no-egress traffic policy** checkbox.
  5. Click **Save**. The **Egress Control** field reflects that the policy is disabled.



###  API 

To allow egress traffic, add the `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"` label to the project metadata. The presence of this label key disables the default no-egress traffic policy, and the system ignores the label value.
    
    
    apiVersion: resourcemanager.global.gdc.goog/v1
    kind: Project
    metadata:
      name: PROJECT_NAME
      namespace: platform
      labels:
        networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"
    

You must create `ProjectNetworkPolicy` egress policies for your projects to restrict the outbound traffic. For more information, see [Configure project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
