---
url: https://docs.cloud.google.com/armor/docs/create-security-policies/
title: Create and view Cloud Armor security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:50:46.882961+00:00
---

# Create and view Cloud Armor security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/create-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Create and view Cloud Armor security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can create Google Cloud Armor security policies to filter incoming traffic to your application. For information about security policy concepts, see the [Cloud Armor security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

**Caution:** You can configure Cloud Armor by using Google Kubernetes Engine (GKE) ingress security policies. When you apply changes to GKE resources, Cloud Armor configuration is overwritten. For information about configuring Cloud Armor on GKE, see [Configure ingress features through BackendConfig parameters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_backendconfig_parameters) in [Cloud Armor ingress security policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#cloud_armor).

## Before you begin

Before you configure security policies, do the following:

  * Make sure that you're familiar with [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) concepts.

  * Examine your existing backend services to determine which ones don't have a security policy attached. These backend services and their associated backends are not protected. To add Cloud Armor protection, attach a new or existing security policy to the backend service.




### Set up IAM permissions for Cloud Armor security policies

The following operations require the Identity and Access Management (IAM) [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`):

  * Configuring, modifying, updating, and deleting a Cloud Armor security policy
  * Using the following API methods: 
    * `SecurityPolicies insert`
    * `SecurityPolicies delete`
    * `SecurityPolicies patch`
    * `SecurityPolicies addRule`
    * `SecurityPolicies patchRule`
    * `SecurityPolicies removeRule`



A user with the [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) can perform the following operations:

  * Setting a Cloud Armor security policy for a backend service
  * Using the following API methods: 
    * `BackendServices setSecurityPolicy`
    * `BackendServices list` (`gcloud` only)



Users with the [Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) and the Compute Network Admin role (`roles/compute.networkAdmin`) can view Cloud Armor security policies by using the `SecurityPolicies` API methods `get`, `list`, and `getRule`.

### Set up IAM permissions for custom roles

The following table lists the IAM roles' base permissions, their associated API methods, and the roles that grant that permission.

IAM permission | API methods | Roles  
---|---|---  
`compute.securityPolicies.create` | `SecurityPolicies insert` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
`compute.securityPolicies.delete` | `SecurityPolicies delete` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
`compute.securityPolicies.get` | `SecurityPolicies get`  
`SecurityPolicies getRule` | [Security Admin (`roles/iam.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#iam.securityAdmin)  
`compute.securityPolicies.list` | `SecurityPolicies list` | [Security Admin (`roles/iam.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#iam.securityAdmin)  
Both of the following: 

  * `compute.securityPolicies.use`
  * `compute.backendServices.  
setSecurityPolicy`

| `BackendServices  
setSecurityPolicy` | [Compute Network Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.networkAdmin)  
`compute.securityPolicies.update` | `SecurityPolicies patch`  
`SecurityPolicies addRule`  
`SecurityPolicies patchRule`  
`SecurityPolicies removeRule` | [Compute Security Admin (`roles/compute.securityAdmin`)](https://docs.cloud.google.com/iam/docs/understanding-roles#compute.securityAdmin)  
  
## Create security policies

Use the Google Cloud console, the Google Cloud CLI, or the REST API to configure Cloud Armor security policies, rules, and expressions. When you use the gcloud CLI, use the `--type` flag to specify whether the security policy is a backend security policy or an edge security policy.

If you're unfamiliar with security policy configuration, review the [example security policies](https://docs.cloud.google.com/armor/docs/example-policies). To add rules to a security policy or view rule expressions, see [Create and view security policy rules](https://docs.cloud.google.com/armor/docs/create-security-policy-rules).

## List security policies

Follow the steps in this section to list Cloud Armor security policies in your project.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. To view a policy, in the list of policies, click the name of that specific policy.




###  gcloud 
    
    
    gcloud compute security-policies list
    

For example:
    
    
    gcloud compute security-policies list
    

Output: 
    
    
    NAME: my-policy
    REGION: us-central1
    

For more information, see [`gcloud compute security-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/list).

## What's next

  * [Create and view security policy rules](https://docs.cloud.google.com/armor/docs/create-security-policy-rules)
  * [Manage security policies](https://docs.cloud.google.com/armor/docs/manage-security-policies)
  * [Manage security policy rules](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules)
  * [Tune web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
