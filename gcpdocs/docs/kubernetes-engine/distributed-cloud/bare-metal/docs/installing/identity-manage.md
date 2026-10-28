---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/identity-manage/
title: Manage identity with GKE Identity Service \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:43.618577+00:00
---

# Manage identity with GKE Identity Service  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/identity-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Manage identity with GKE Identity Service Stay organized with collections  Save and categorize content based on your preferences. 

GKE Identity Service lets you integrate existing identity providers to authenticate users to Google Distributed Cloud clusters. Users can connect to the Kubernetes API server from the command line by using [OpenID Connect (OIDC)](https://openid.net/connect/) or [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/), or through the Google Cloud console by using OIDC.

The service supports admin, user, hybrid, and standalone clusters, connecting to on-premises systems such as [Active Directory Federation Services (ADFS)](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) and public providers such as Okta. If your organization uses Google Accounts, use the [connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) to manage cluster access.

## Architecture overview

The GKE Identity Service runs as a Pod inside the cluster control plane. During cluster lifecycle phases, the API Server is dynamically configured to use the in-cluster GKE Identity Service as the authentication webhook for all incoming requests. The API Server [isn't able to use in-cluster DNS](https://github.com/kubernetes/minikube/issues/3772). As a result, the API Server is configured to access GKE Identity Service as a REST resource access. In audit logs, this invocation is recorded as a `CREATE` request to the Services or proxy resource by a `system:anonymous` user.

## Before you begin

  * To prompt users for consent and authorize their user account, a browser-based authentication flow is used. Headless systems aren't supported.

  * To authenticate through the Google Cloud console, each cluster that you want to configure must be [registered with your project fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation).




## Setup process and options

GKE Identity Service supports identity providers using the following protocols:

  * [OpenID Connect (OIDC)](https://openid.net/connect/). We provide specific instructions for setup for some popular OpenID providers, including Microsoft, but you can use any provider that implements OIDC.

  * [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/). You can use GKE Identity Service to authenticate using LDAP with Active Directory or an LDAP server.


**Note:** If you use the `ClientConfig` field to configure GKE Identity Service directly inside a cluster, cluster updates can overwrite the field. Instead, use the `authentication` field on the cluster custom resource or set up your GKE Identity Service at the [fleet level](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster) so your configuration persists during an update.

### OIDC

  1. Register GKE Identity Service as a client with your OIDC provider following the instructions in [Configuring providers for GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider).

  2. Choose from the following cluster configuration options:

     * (Recommended) Configure your clusters at fleet level following the instructions in [Configuring clusters for fleet-level GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster). With this option, your authentication configuration is centrally managed by Google Cloud.

     * Configure your clusters individually following the instructions in [Configuring clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster).

  3. Set up user access to your clusters, including role-based access control (RBAC), following the instructions in [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access).




### LDAP

To get started with LDAP, follow the instructions in [Set up GKE Identity Service with LDAP](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap).

## Access clusters

After GKE Identity Service has been set up, users can sign in to configured clusters using either the command line or the Google Cloud console.

  * (Recommended) Learn how to sign in to registered clusters with your OIDC or LDAP ID in [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing).

  * Learn how to sign in to clusters from the Google Cloud console in [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) (OIDC only).




## Troubleshoot the login flow

To troubleshoot [login flows that authenticate directly on the GKE Identity Service server with a fully qualified domain name (FQDN)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access), you can use the GKE Identity Service diagnostic utility. The diagnostic utility simulates login flows with your OIDC provider to quickly identify configuration problems. This tool requires a version 1.32 or higher cluster and only supports OIDC. For more information, see [GKE Identity Service diagnostic utility](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
