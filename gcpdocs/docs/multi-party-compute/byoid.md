---
url: https://docs.cloud.google.com/multi-party-compute/byoid/
title: Configure Workforce Identity Federation (BYOID) \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:40.299638+00:00
---

# Configure Workforce Identity Federation (BYOID)  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/byoid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Configure Workforce Identity Federation (BYOID) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how to configure Bring Your Own Identity (BYOID) for the Multi-party Compute API using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). With identity federation, human users and automated signer workloads can authenticate to Multi-party Compute using your organization's external Identity Provider (IdP)—such as Okta, Microsoft Entra ID, or Ping Identity. You don't need to create Google Accounts or manage long-lived service account keys.

## Overview

Identity federation integrates with the Multi-party Compute defense-in-depth security model across the following layers:

  1. **Edge Identity and Access Management (IAM) authorization** : Callers exchange credentials from an external OpenID Connect (OIDC) or SAML 2.0 IdP with the Google Cloud Security Token Service (Security Token Service) for a short-lived federated access token. The Google Cloud API gateway evaluates IAM role bindings against the federated principal URI before forwarding requests to your Multi-party Compute instance, and propagates the federated identity (`principalSubject`) for [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  2. **Separation of duties and cryptographic approval** : IAM roles separate administrative provisioning (`roles/mpc.admin`), operational participation (`roles/mpc.editor`), and read-only oversight (`roles/mpc.viewer`). Within your instance, Admins, Policy Authors, and Signers also need a User whose role (`ADMIN`, `POLICY_AUTHOR`, or `SIGNER`) the instance checks for methods that act on behalf of a User, and approvals must be signed with the authorization key registered on that User. For more information, see [How a request is authorized](https://docs.cloud.google.com/multi-party-compute/authorization#two-checks).



Depending on the caller type, you can use two identity federation mechanisms:

  * **Workforce Identity Federation** (`locations/global/workforcePools/...`): Authenticates **human users** (Administrators, Policy Authors, Signers, and Compliance) using organization-level workforce pools mapped to your corporate IdP. This guide walks through configuring Workforce Identity Federation end to end.
  * **Workload Identity Federation** (`projects/.../locations/global/workloadIdentityPools/...`): Authenticates **automated workloads** (such as headless co-signer daemons running in AWS, Azure, or Kubernetes) using project-level workload identity pools.



For more information about how IAM roles map to Multi-party Compute personas, see [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization).

## Before you begin

Before starting, make sure you have the following:

  1. A Google Cloud organization and a consumer project onboarded to Multi-party Compute.
  2. The `gcloud` CLI and `jq` installed, and `gcloud` authenticated with an administrative account that holds the following roles: 
     * **Workforce Pool Admin** (`roles/iam.workforcePoolAdmin`) on your Google Cloud organization (if creating a new workforce pool in Step 1).
     * **Project IAM Admin** (`roles/resourcemanager.projectIamAdmin`) and **Service Usage Admin** (`roles/serviceusage.serviceUsageAdmin`) on your consumer project.
  3. The required APIs enabled on your consumer project:
         
         gcloud services enable mpc.googleapis.com iam.googleapis.com sts.googleapis.com \
           --project="my-project"
         

  4. An external OIDC or SAML 2.0 application configured in your corporate IdP. If you plan to use interactive browser sign-in with the `gcloud` CLI, configure the Google Cloud redirect URI in your IdP application (see the setup guides for [Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta) and [Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id)).


**Note:** If your organization already has a workforce identity pool and provider configured, you can skip Step 1. If your federated users will use Cloud Key Management Service (Cloud KMS) to generate and sign with their authorization keys in the [Multi-party Compute User Guide](https://docs.cloud.google.com/multi-party-compute/user-guide), also enable `cloudkms.googleapis.com` and grant the appropriate Cloud KMS roles (such as `roles/cloudkms.admin` and `roles/cloudkms.signerVerifier`).

## Setup

Update the following variables to populate the commands throughout this guide.

**Important:** If you leave or refresh this page, these input fields might reset to their default values.

### Required setup parameters

Customize these parameters to match your Google Cloud environment and external IdP configuration.

Parameter | Value | Description  
---|---|---  
**Organization ID** | `123456789012` | Your numeric Google Cloud organization ID.  
**Project ID** | `my-project` | The consumer project ID registered for your Multi-party Compute instance.  
**Domain ID** | `67317436-0f29-ba9e-9146-d11c0bd8df9b` | The unique domain ID assigned to your Multi-party Compute instance.  
**Instance Path ID** | `mpc-unit-bob-123` | The instance path ID assigned to your Multi-party Compute instance.  
**Location** | `us-central1` | Deployment location (`us-central1`). For more information, see [Multi-party Compute locations](https://docs.cloud.google.com/multi-party-compute/locations).  
**Workforce Pool ID** | `mpc-workforce-pool` | The organization-level workforce identity pool ID.  
**Provider ID** | `mpc-oidc-provider` | The workforce identity pool provider ID.  
**IdP Issuer URI** | `https://idp.example.com` | Your external OIDC IdP issuer URI.  
**IdP Client ID** | `mpc-client` | The OAuth 2.0 client ID configured in your external IdP.  
  
* * *

## Step 1: Configure a workforce identity pool and provider

Workforce identity pools (`locations/global/workforcePools/mpc-workforce-pool`) are organization-level resources that map to your enterprise IdP tenant. You don't need to create separate workforce pools for each project or role.

  1. Create a workforce identity pool in your Google Cloud organization:
         
         gcloud iam workforce-pools create "mpc-workforce-pool" \
           --organization="123456789012" \
           --location="global" \
           --display-name="MPC Workforce Pool"
         

  2. Create an OIDC workforce pool provider that trusts your external IdP and maps subject and group claims:
         
         gcloud iam workforce-pools providers create-oidc "mpc-oidc-provider" \
           --workforce-pool="mpc-workforce-pool" \
           --location="global" \
           --display-name="MPC Enterprise OIDC Provider" \
           --issuer-uri="https://idp.example.com" \
           --client-id="mpc-client" \
           --attribute-mapping="google.subject=assertion.sub,google.groups=assertion.groups" \
           --web-sso-response-type="id-token" \
           --web-sso-assertion-claims-behavior="only-id-token-claims"
         

**Note:** By default, Security Token Service discovers and rotates public signing keys from your IdP's `/.well-known/openid-configuration` endpoint. If you are testing with an offline or synthetic OIDC issuer that isn't publicly reachable, pass `--jwk-json-path="<var>PATH_TO_JWK_FILE</var>"`, replacing `<var>PATH_TO_JWK_FILE</var>` with the local path to your issuer's public JSON Web Key Set (JWKS) file. For SAML 2.0 providers, use `gcloud iam workforce-pools providers create-saml` with `--idp-metadata-path`.



* * *

## Step 2: Grant IAM roles to federated principals

To call the MPC API, federated principals require two types of IAM role bindings on your consumer project (`my-project`):

  1. **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`), which authorizes the federated identity to attribute API quota and billing to your consumer project.
  2. **An Multi-party Compute role** (`roles/mpc.admin`, `roles/mpc.editor`, or `roles/mpc.viewer`), which authorizes specific Multi-party Compute operations.

**Note:** At the IAM layer, both Policy Authors and Signers are granted `roles/mpc.editor`. Inside your instance, separation of duties between authoring transaction policies and approving transactions is enforced by each caller's User role (`POLICY_AUTHOR` or `SIGNER`) and by the authorization key registered on that User. For more information, see Add federated identities as v1beta Users and [How a request is authorized](https://docs.cloud.google.com/multi-party-compute/authorization#two-checks).

In production, bind IAM roles to distinct IdP groups within your workforce pool:
    
    
    # 1. Allow members of the workforce pool to consume APIs through the consumer project
    gcloud projects add-iam-policy-binding "my-project" \
      --role="roles/serviceusage.serviceUsageConsumer" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/*"
    
    # 2. Grant MPC Admin to the enterprise administrators group
    gcloud projects add-iam-policy-binding "my-project" \
      --role="roles/mpc.admin" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/group/mpc-admins"
    
    # 3. Grant MPC Editor to Policy Authors and Signers groups
    gcloud projects add-iam-policy-binding "my-project" \
      --role="roles/mpc.editor" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/group/mpc-policy-authors"
    
    gcloud projects add-iam-policy-binding "my-project" \
      --role="roles/mpc.editor" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/group/mpc-signers"
    
    # 4. Grant MPC Viewer to the Compliance group
    gcloud projects add-iam-policy-binding "my-project" \
      --role="roles/mpc.viewer" \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/group/mpc-auditors"
    

**Note:** The group identifier in `principalSet://.../group/<var>GROUP_ID</var>` must match the mapped `google.groups` claim value from your IdP assertion. For more information, see [Workforce principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).**Caution:** If you are evaluating Multi-party Compute in an isolated test environment with a synthetic user that doesn't emit group claims, you can bind `roles/mpc.admin` to a single subject (`principal://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/subject/<var>USER_SUBJECT</var>`, where `<var>USER_SUBJECT</var>` is the user's `sub` claim) or to a dedicated test pool (`principalSet://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/*`). Never bind `roles/mpc.admin` to `/*` on a production workforce pool, because doing so grants administrative access to every user in your corporate IdP tenant.

### Automated signer workloads (Workload Identity Federation)

If you run automated co-signer daemons outside Google Cloud (for example, in AWS, Azure, or Kubernetes), configure a project-scoped [workload identity pool and provider](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers). Grant `roles/serviceusage.serviceUsageConsumer` and `roles/mpc.editor` to the workload principal (`principal://iam.googleapis.com/projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>WORKLOAD_POOL_ID</var>/subject/<var>SIGNER_NODE_SUBJECT</var>`, replacing `<var>PROJECT_NUMBER</var>`, `<var>WORKLOAD_POOL_ID</var>`, and `<var>SIGNER_NODE_SUBJECT</var>` with your project number, workload pool ID, and workload `sub` claim), and generate an Application Default Credentials file using `gcloud iam workload-identity-pools create-cred-config`.

### Add federated identities as v1beta Users

In the v1beta API, the IAM roles from this step let a federated identity call your instance. To act inside the instance, as an Admin, Policy Author, or Signer, the identity also needs a [User](https://docs.cloud.google.com/multi-party-compute/authorization#user-roles). The instance identifies the caller by matching the caller's principal against the `principal` field of each User.

For a Workforce Identity Federation identity, set `principal` to the identity's subject principal identifier:
    
    
    principal://iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/subject/SUBJECT_ID
    

Replace `SUBJECT_ID` with the value that your provider maps to `google.subject`. With the attribute mapping in Step 1, it's the `sub` claim of the user's ID token.

When you set `principal`, keep the following in mind:

  * **Use a`principal://` identifier, not a `principalSet://` identifier.** A User is one person. Group and pool identifiers such as `principalSet://.../group/mpc-signers` work in IAM role bindings, but they never match a caller, so a User created with one can't act in the instance.
  * **Match the subject exactly.** The instance compares workforce and workload subjects case-sensitively, so copy the subject as your IdP issues it. Google Account emails, such as `alice@example.com`, are compared case-insensitively.
  * **You can't change`principal` later.** To change a User's identity, disable the User and create a new one.



* * *

## Step 3: Authenticate and obtain a federated access token

The MPC API doesn't accept OIDC tokens or SAML assertions directly from your IdP. Exchange the IdP credential with Security Token Service for a federated Google Cloud access token before calling your Multi-party Compute instance endpoint (`*.mpc.goog`).

You can obtain and manage federated access tokens automatically using Application Default Credentials (ADC) and the `gcloud` CLI, or programmatically using the Security Token Service API.

### Application Default Credentials and gcloud CLI

In production client applications and interactive CLI sessions, use a configuration file so that the Google Cloud SDK and [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained) handle the background Security Token Service token exchange, caching, and refreshes automatically.

**Option A: Interactive browser sign-in**

Generate a sign-in configuration file and authenticate both the `gcloud` CLI and Application Default Credentials (ADC) with your corporate IdP:
    
    
    gcloud iam workforce-pools create-login-config \
      "locations/global/workforcePools/mpc-workforce-pool/providers/mpc-oidc-provider" \
      --activate \
      --output-file="login-config.json"
    
    gcloud config set billing/quota_project "my-project"
    gcloud auth login --login-config="login-config.json"
    gcloud auth application-default login --login-config="login-config.json"
    

**Option B: Non-interactive sign-in with a credential configuration file (ADC)**

If an external process supplies and refreshes a signed OIDC token in a local file (for example, `/var/run/secrets/tokens/oidc-token`) before the token expires, generate an external credential configuration file:
    
    
    gcloud iam workforce-pools create-cred-config \
      "locations/global/workforcePools/mpc-workforce-pool/providers/mpc-oidc-provider" \
      --subject-token-type="urn:ietf:params:oauth:token-type:id_token" \
      --credential-source-file="/var/run/secrets/tokens/oidc-token" \
      --workforce-pool-user-project="my-project" \
      --output-file="credential-config.json"
    
    export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credential-config.json"
    

**Export the access token for`curl` requests:**

After completing Option A or Option B, export the federated access token from ADC into `ACCESS_TOKEN`:
    
    
    export ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"
    

### Direct REST STS token exchange

If you are integrating a custom client without Google Cloud SDKs, exchange a signed OIDC ID token (`<var>IDP_ID_TOKEN</var>`) directly with Security Token Service. Include `userProject` in the `options` field so that Google Cloud attributes the token to your consumer project:
    
    
    # Set IDP_ID_TOKEN to the signed OIDC JWT assertion from your external IdP
    # export IDP_ID_TOKEN="eyJhbGciOiJSUzI1NiIs..."
    
    STS_RESPONSE=$(curl -sS -X POST "https://sts.googleapis.com/v1/token" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:token-exchange" \
      --data-urlencode "audience=//iam.googleapis.com/locations/global/workforcePools/mpc-workforce-pool/providers/mpc-oidc-provider" \
      --data-urlencode "scope=https://www.googleapis.com/auth/cloud-platform" \
      --data-urlencode "requested_token_type=urn:ietf:params:oauth:token-type:access_token" \
      --data-urlencode "subject_token_type=urn:ietf:params:oauth:token-type:id_token" \
      --data-urlencode "subject_token=${IDP_ID_TOKEN}" \
      --data-urlencode 'options={"userProject":"my-project"}')
    
    export ACCESS_TOKEN=$(echo "${STS_RESPONSE}" | jq -er '.access_token') || echo "${STS_RESPONSE}" | jq .
    

* * *

## Step 4: Verify federated API access

Verify that your federated credentials, `userProject` attribution, and IAM role bindings are working by listing the Users in your Multi-party Compute instance. Because `mpc.googleapis.com/users.list` is included in `roles/mpc.viewer`, `roles/mpc.editor`, and `roles/mpc.admin`, any authorized federated persona can run this check:
    
    
    curl -sS -X GET \
      -H "Authorization: Bearer ${ACCESS_TOKEN}" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1beta/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/users" | jq .
    

A `200 OK` JSON response (either `{}` on a fresh instance or a list of `users`) confirms that your federated identity is authenticated and authorized to call your Multi-party Compute instance.

This check uses only IAM. To confirm that the instance also recognizes your identity as a User, check that one of the returned Users has your `principal://` identifier in its `principal` field. For more information, see Add federated identities as v1beta Users.

* * *

## Troubleshooting

If you encounter authentication or permission errors when calling Multi-party Compute with federated credentials, verify the following requirements:

### User project attribution (`401 UNAUTHENTICATED: Unable to determine client project number`)

  * **Cause** : Organization-level workforce pool credentials aren't intrinsically bound to a single Google Cloud project unless a user project is specified during token exchange or on the request.
  * **Resolution** : Include `options: {"userProject": "<var>PROJECT_ID</var>"}` in your Security Token Service token exchange request body (or `--workforce-pool-user-project` in `gcloud iam workforce-pools create-cred-config`), and include the `X-Goog-User-Project: <var>PROJECT_ID</var>` header on your MPC API calls.



### Missing Service Usage permission (`403 PERMISSION_DENIED`)

  * **Cause** : The federated principal or group lacks permission to attribute API usage to the consumer project specified in `userProject` or `X-Goog-User-Project`.
  * **Resolution** : Grant `roles/serviceusage.serviceUsageConsumer` to your `principal://` or `principalSet://` member on the consumer project (see Step 2).



### Consumer project mismatch (`403 PERMISSION_DENIED: Project is not allowed to call the API through this host`)

  * **Cause** : Each dedicated Multi-party Compute instance endpoint only accepts requests from the consumer project configured for that instance.
  * **Resolution** : Verify that `<var>PROJECT_ID</var>` in both the request URL path and the `userProject` / `X-Goog-User-Project` header matches the consumer project provisioned for your Multi-party Compute instance.



### Invalid credential (`401 UNAUTHENTICATED: Request credential is invalid`)

  * **Cause** : A third-party OIDC token or SAML assertion was sent directly to the Multi-party Compute endpoint without first exchanging it using Security Token Service.
  * **Resolution** : Exchange your IdP credential through `https://sts.googleapis.com/v1/token` (or use Application Default Credentials) and pass the resulting Google Cloud access token in the `Authorization: Bearer` header.



### Domain restricted sharing policy blocks role bindings (`400 FAILED_PRECONDITION`)

  * **Cause** : Your Google Cloud organization enforces the `constraints/iam.allowedPolicyMemberDomains` organization policy, which restricts which principal domains can be granted IAM roles on projects.
  * **Resolution** : Ask your Organization Policy Administrator to add your workforce pool principal set to the allowed policy member domains on your consumer project or organization, or test in a project where `constraints/iam.allowedPolicyMemberDomains` allows your workforce pool.



## What's next

  * To create Users, Teams, transaction policies, and keys, and to sign transactions with your federated identity, follow the [Multi-party Compute User Guide](https://docs.cloud.google.com/multi-party-compute/user-guide). Set each User's principal to the `principal://` identifier described in Add federated identities as v1beta Users.
  * The user guide retrieves each persona's access token with `gcloud auth print-access-token`, which uses `gcloud` CLI credentials, not Application Default Credentials. Sign in each federated user with `gcloud auth login --login-config`, as shown in Option A of Step 3.
  * Learn more about User roles, IAM permissions, and resource-level conditions in [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
