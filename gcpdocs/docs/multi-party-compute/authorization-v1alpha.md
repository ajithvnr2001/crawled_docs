---
url: https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha/
title: Securing the MPC Service using IAM Roles \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:38.242484+00:00
---

# Securing the MPC Service using IAM Roles  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)



#  Securing the MPC Service using IAM Roles Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This page covers the deprecated `v1alpha1` API and will be removed in December 2026. For the `v1beta` API, see [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization).

## Security Model: Defense-in-Depth

The Multi-party Compute (MPC) API implements a defense-in-depth security architecture that relies on strict Identity and Access Management (IAM) controls. This model ensures that no single identity or compromised Google Account can unilaterally compromise the platform or extract assets.

  * **Layer 1: Identity & Access Management (IAM)**: All requests are verified at the edge to confirm the caller has the explicit permissions required to invoke specific Google Cloud API methods (see [IAM Overview](https://cloud.google.com/iam/docs/overview)). Accounts lacking sufficient privileges are immediately rejected with a `403 Forbidden` error, preventing unauthorized traffic from reaching the application layer.
  * **Layer 2: Separation of Duties (SoD)** : The MPC platform enforces strict role separation to ensure that distinct governance and execution actions cannot be performed by the same individual. By defining distinct roles—such as restricting Policy Authors to only editing policies, and Signers to only signing transaction payloads—the system ensures that a single rogue agent or compromised account cannot independently execute sensitive transactions.
  * **Layer 3: Principle of Least Privilege** : Access is granted strictly based on job function, ensuring users have only the minimum permissions required to perform their duties. For example, the Compliance or Audit team operates with the least privilege, retaining strictly read-only access to monitor activity. They can view policies and inspect transaction logs for oversight, but lack any ability to modify policies, initiate transactions, or interact with assets.



* * *

## Personas & Separation of Duties

Security is enforced by decoupling **Administration** (setting up the board) from **Governance** (defining rules) and **Execution** (moving assets).

Persona | Domain | IAM Role Assigned | Core Responsibilities  
---|---|---|---  
**Administrator** | Administration | mpc.admin | Provisions resources. Cannot sign transactions or author policies.  
**Policy Author** | Governance | mpc.editor | Defines and edits operational policies (e.g., spending limits).  
**Signer** | Execution | mpc.editor | Signs transaction payloads. Cannot author policies.  
**Compliance** | Oversight | mpc.viewer | Read-only access to monitor activity and inspect policies. Cannot modify policies or initiate transactions.  
  
> **Note:** **Evaluation Mode** : When following the user guide independently, a single Google Cloud IAM identity can be used to simulate actions across the various personas (e.g., signing as both Alice and Bob from one workstation). In a real-world scenario, strict **Separation of Duties** should be enforced by using distinct IAM identities and unique cryptographic keys for each persona.

## Predefined IAM roles

The following table details the specific IAM permissions for the Multi-party Compute (MPC) API and the roles that grant them. For more information about the API operations, see the [MPC API Reference](https://docs.cloud.google.com/multi-party-compute/reference/rest).

Role | Permissions  
---|---  
**Multi-party Compute Viewer**  
`(roles/mpc.viewer)`  
  
Provides read-only access across the API (Get/List operations on all resources). Best suited for auditors or monitoring tools.  
  
Lowest-level resources where you can grant this role:  


  * KeyRing

| `mpc.googleapis.com/keyRings.get`  
`mpc.googleapis.com/keyRings.list`  
`mpc.googleapis.com/keys.get`  
`mpc.googleapis.com/keys.list`  
`mpc.googleapis.com/policies.get`  
`mpc.googleapis.com/policies.list`  
`mpc.googleapis.com/policyAuthorTrustBundles.get`  
`mpc.googleapis.com/proposals.get`  
`mpc.googleapis.com/proposals.list`  
`mpc.googleapis.com/signers.get`  
`mpc.googleapis.com/signers.list`  
**Multi-party Compute Editor**  
`(roles/mpc.editor)`  
  
Designed for Policy Authors and Participants (Signers). Grants the ability to manage policies, create proposals, and record participant decisions.  
  
Lowest-level resources where you can grant this role:  


  * KeyRing

| Includes all `roles/mpc.viewer` permissions, plus:  
  
`mpc.googleapis.com/keyRings.update`  
`mpc.googleapis.com/keys.update`  
`mpc.googleapis.com/policies.addQuorumSignature`  
`mpc.googleapis.com/policies.create`  
`mpc.googleapis.com/policies.revoke`  
`mpc.googleapis.com/proposals.create`  
`mpc.googleapis.com/proposals.fetchProposalSignature`  
`mpc.googleapis.com/proposals.recordParticipantDecision`  
**Multi-party Compute Admin**  
`(roles/mpc.admin)`  
  
Designed for Administrators. Grants full access to provision infrastructure, generate keys, and register participant public keys.  
  
Lowest-level resources where you can grant this role:  


  * Instance

| Includes all `roles/mpc.editor` permissions, plus:  
  
`mpc.googleapis.com/keyRings.create`  
`mpc.googleapis.com/keyRings.delete`  
`mpc.googleapis.com/keys.create`  
`mpc.googleapis.com/policyAuthorTrustBundles.update`  
`mpc.googleapis.com/signers.create`  
  
## Custom Roles

To grant a Participant strict least-privilege access instead of using the broader predefined roles like `roles/mpc.editor`, you can create a [Custom IAM Role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) containing only the exact permissions they need to participate in operations.

### Example Custom Role Command
    
    
    gcloud iam roles create customMpcSigner \
      --project="PROJECT_ID" \
      --title="Custom MPC Signer" \
      --description="Restricted role for transaction participants" \
      --permissions="mpc.googleapis.com/proposals.get,mpc.googleapis.com/proposals.list,mpc.googleapis.com/proposals.recordParticipantDecision"
    

## Resource-Level & Conditioned IAM

By adhering to the principle of least privilege, you can scope IAM roles to a limited boundary using [IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview).

If multiple business units operate in the same Google Cloud Project using a shared instance, you can enforce separation by placing resources into separate KeyRings (e.g. `KeyRing A` and `KeyRing B`). You can grant `roles/mpc.editor` to a Service Account using an IAM condition that restricts it exclusively to operations occurring within a designated KeyRing (`KeyRing A`), while restricting access to other KeyRings in the same instance.

### Example Command

An example of creating a KeyRing-scoped role binding:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:sa-name@PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/mpc.editor" \
      --condition="expression=resource.name.startsWith('projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/mpc/keyRings/KEYRING_ID'),title=KeyRing_Scoped_Editor"
    

## Federated identities (Bring Your Own Identity)

You can authenticate and authorize Multi-party Compute requests using external corporate Identity Providers (such as Okta, Microsoft Entra ID, or Ping Identity) or external workload runtimes without creating Google Accounts or managing service account keys:

  * **[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)** : Maps organization-level workforce pools (`locations/global/workforcePools/<var>WORKFORCE_POOL_ID</var>`) to human personas—such as Administrators, Policy Authors, Signers, and Compliance—by binding IAM roles to external IdP groups.
  * **[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)** : Maps project-level workload identity pools (`projects/<var>PROJECT_NUMBER</var>/locations/global/workloadIdentityPools/<var>WORKLOAD_POOL_ID</var>`) to automated co-signer nodes running in AWS, Azure, or Kubernetes.



Federated principals must also be granted the **Service Usage Consumer** role (`roles/serviceusage.serviceUsageConsumer`) on the consumer project so that API requests can attribute quota and billing to the project.

### Example federated role bindings
    
    
    # Allow members of the workforce pool to consume APIs through the consumer project
    gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/<var>WORKFORCE_POOL_ID</var>/*" \
      --role="roles/serviceusage.serviceUsageConsumer"
    
    # Grant MPC Admin to an external IdP administrators group
    gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/<var>WORKFORCE_POOL_ID</var>/group/mpc-admins" \
      --role="roles/mpc.admin"
    
    # Grant MPC Editor to an external IdP signers group
    gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
      --member="principalSet://iam.googleapis.com/locations/global/workforcePools/<var>WORKFORCE_POOL_ID</var>/group/mpc-signers" \
      --role="roles/mpc.editor"
    

Replace the following:

  * `<var>PROJECT_ID</var>`: the consumer project ID for your Multi-party Compute instance.
  * `<var>WORKFORCE_POOL_ID</var>`: the organization-level workforce identity pool ID.



For a complete end-to-end walkthrough, see [Configure Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
