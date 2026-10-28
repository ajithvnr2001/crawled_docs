---
url: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls/
title: Configure VPC Service Controls for ULL Packet Mirroring \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:31:24.177556+00:00
---

# Configure VPC Service Controls for ULL Packet Mirroring  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/configure-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Service Controls for ULL Packet Mirroring

**Preview — ULL Packet Mirroring for exchange participants**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VPC Service Controls provides security for Ultra Low Latency (ULL) Packet Mirroring to help reduce the risk of data theft when traffic or data moves between different network environments or organizations. You can use VPC Service Controls to place projects containing ULL Packet Mirroring resources inside service perimeters.

This page describes how to configure VPC Service Controls for ULL Packet Mirroring collector resources (`UllMirroringCollector`).

For more information, see [Components of ULL Packet Mirroring](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/packet-mirroring-ull#packet-mirroring-comp).

Before you begin, review the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  1. Verify that you have the required Identity and Access Management (IAM) roles to administer VPC Service Controls. For more information, see [IAM roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Network Security API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=networksecurity)

  6. Verify that you have the required IAM roles to manage ULL Packet Mirroring resources. For more information, see [Set up Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull#roles).



## Overview of perimeter rules for ULL Packet Mirroring

Perimeter rules for ULL Packet Mirroring act as security guardrails to control communication between isolated Virtual Private Cloud (VPC) environments while allowing specific, necessary traffic. Depending on your deployment topology, you might need to configure VPC Service Controls egress rules and ingress rules to allow communication between your collector project and the exchange operator's engine project when managing ULL Packet Mirroring collectors (`UllMirroringCollector`).

To protect ULL Packet Mirroring resources, add the Network Security API (`networksecurity.googleapis.com`) to the list of restricted services within your collector service perimeter.

The following table summarizes the required VPC Service Controls configuration for each deployment scenario:

Scenario | Topology | Required VPC Service Controls configuration  
---|---|---  
Create collector in a different project (same service perimeter) | Different project, same perimeter | No additional rules are required because both projects belong to the same service perimeter.  
Create collector in a different project (separate service perimeter) | Different project, separate perimeters | Add bidirectional egress rules between the engine project and the collector project for `networksecurity.googleapis.com`.  
  
## Add APIs to the service perimeter

To protect ULL Packet Mirroring resources within a service perimeter, add the Network Security API to the list of restricted services.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. In the table, click the name of the service perimeter that you want to modify.

  3. Click **Edit**.

  4. On the **Edit service perimeter** page, click **Restricted services** and then **Add services**.

  5. Select **Network security API** (`networksecurity.googleapis.com`).

  6. Click **Add selected services** and then click **Save**.




###  gcloud 

To add restricted services to an existing service perimeter, use the [`gcloud access-context-manager perimeters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_NAME \
        --policy=POLICY_ID \
        --add-restricted-services=networksecurity.googleapis.com
    

Replace the following:

  * `PERIMETER_NAME`: the name of the service perimeter.
  * `POLICY_ID`: the ID of your organization's access policy.



## Configure egress rules for cross-perimeter collectors

Configure a collector-to-engine egress rule on your service perimeter to allow the `UllMirroringCollector` resource to connect to the `UllMirroringEngine` in the exchange operator's engine project.

Before you create the `UllMirroringCollector` resource, verify that your exchange operator has completed the following steps in the engine project and service perimeter:

  * Granted the `roles/networksecurity.ullMirroringEngineUser` IAM role on the engine project to the caller, such as your user account or service account.
  * Configured an egress rule in the engine service perimeter that allows traffic to your collector project (`projects/COLLECTOR_PROJECT_NUMBER`).
  * If you create the collector from outside the engine service perimeter, configured an ingress rule in that perimeter to allow the caller and source environment (`projects/CALLER_PROJECT_NUMBER`).



### Configure egress from collector perimeter to engine project

Add the following egress policy to the collector service perimeter:

**Note:** If you restrict the Compute Engine API (`compute.googleapis.com`) in your perimeter, you must also allow the `RegionForwardingRulesService.Get` method.
    
    
    egressPolicies:
    - egressFrom:
        # Optional: To allow all users or service accounts, you can replace the
        # identities list with identityType: ANY_IDENTITY,
        # ANY_USER_ACCOUNT, or ANY_SERVICE_ACCOUNT.
        identities:
        - PRINCIPAL_IDENTIFIER
      egressTo:
        operations:
        - serviceName: networksecurity.googleapis.com
          methodSelectors:
          - method: '*'
        # Optional: The compute.googleapis.com service is required only if you
        # restrict the Compute Engine API in your perimeter.
        - serviceName: compute.googleapis.com
          methodSelectors:
          - method: RegionForwardingRulesService.Get
        resources:
        - projects/ENGINE_PROJECT_NUMBER
      title: Allow egress to engine project for ULL mirroring
    

Replace the following:

  * `PRINCIPAL_IDENTIFIER`: the identity that initiates the collector creation request. For information about supported identities and their identifier formats, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).
  * `ENGINE_PROJECT_NUMBER`: the project number of the project that hosts the `UllMirroringEngine`.



## Configure ingress rules for callers

You can create a `UllMirroringCollector` resource from outside the service perimeters, such as from a separate project or an external network. When you send this request, VPC Service Controls evaluates both the collector project (`parent`) and the engine project (`engine`) in a single API call.

Both the collector service perimeter and the engine service perimeter must have ingress rules that allow the caller and source environment. If either perimeter lacks a matching ingress rule, the request fails with a `403 SECURITY_POLICY_VIOLATED` error.

### Configure ingress to the collector perimeter

Add the following ingress policy to the collector service perimeter to allow the external caller:
    
    
    ingressPolicies:
    - ingressFrom:
        # Optional: To allow all users or service accounts, you can replace the
        # identities list below with identityType: ANY_IDENTITY,
        # ANY_USER_ACCOUNT, or ANY_SERVICE_ACCOUNT.
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: projects/CALLER_PROJECT_NUMBER
      ingressTo:
        operations:
        - serviceName: networksecurity.googleapis.com
          methodSelectors:
          - method: '*'
        # Optional: The compute.googleapis.com service is required only if you
        # restrict the Compute Engine API in your perimeter.
        - serviceName: compute.googleapis.com
          methodSelectors:
          - method: RegionForwardingRulesService.Get
        resources:
        - projects/COLLECTOR_PROJECT_NUMBER
      title: Allow external caller into collector perimeter
    

Replace the following:

  * `PRINCIPAL_IDENTIFIER`: the identity that initiates the collector creation request. For information about supported identities and their identifier formats, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).
  * `CALLER_PROJECT_NUMBER`: the project number of the project from which the caller originates.
  * `COLLECTOR_PROJECT_NUMBER`: the project number of the project that hosts the `UllMirroringCollector`.



## Create and manage access levels

To permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter.

For more information, see [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## Troubleshoot perimeter violations

If creating a `UllMirroringCollector` fails with a `403 SECURITY_POLICY_VIOLATED` error, inspect the VPC Service Controls audit logs in Cloud Logging to identify which perimeter blocked the request:

  * **Violation on the collector or engine perimeter** (`ingressViolations` or `NETWORK_NOT_IN_SAME_SERVICE_PERIMETER`): verify that both perimeters have ingress rules that allow your identity (`principalEmail`) and source project or access level.
  * **Violation between the collector and engine projects** (`egressViolations` or `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER`): verify that both perimeters have bidirectional egress rules for `networksecurity.googleapis.com`.
  * **Compute Engine API restriction** (`RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER`): if an audit log shows `serviceName` as `compute.googleapis.com` and `method` as `compute.v1.RegionForwardingRulesService.Get`, your perimeter restricts Compute Engine APIs. Verify that your egress and ingress rules include the `RegionForwardingRulesService.Get` method selector.

**Note:** To prevent configuration rejections, specify the method selector as `RegionForwardingRulesService.Get`, without the `compute.v1.` prefix.



For more information about diagnosing access denials with unique IDs or troubleshooting tokens in the VPC Service Controls violation analyzer, see [Access the violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter#access-the-violation-analyzer).

## What's next

  * [Set up Packet Mirroring for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/packet-mirroring/set-up-packet-mirroring-ull)
  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
