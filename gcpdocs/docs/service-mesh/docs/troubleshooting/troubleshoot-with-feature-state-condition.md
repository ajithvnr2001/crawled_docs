---
url: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-with-feature-state-condition/
title: Understanding Feature State Conditions \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:34:55.204782+00:00
---

# Understanding Feature State Conditions  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-with-feature-state-condition/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understanding Feature State Conditions

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

This page describes how to interpret and act upon Conditions reported on your Cloud Service Mesh cluster or fleet.

To check for conditions, run this command:
    
    
      gcloud container fleet mesh describe --project FLEET_PROJECT
    

The output may include `conditions` in `membershipStates` for a cluster, like:
    
    
      ...
      membershipStates:
        projects/test-project/locations/us-central1/memberships/my-membership:
          servicemesh:
            conditions:
              - code: <CONDITION_CODE>
                details: ...
                documentationLink: ....
                severity: ...
    

Values of `code` are described in more detail on this page.

## NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED

You may see the `NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED` error code in the `Conditions` field of your membership:
    
    
        membershipStates:
          projects/test-project/locations/us-central1/memberships/my-membership:
            servicemesh:
              conditions:
              - code: NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED
                details: One or more node pools have workload identity federation disabled.
                documentationLink: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
                severity: ERROR
              controlPlaneManagement:
                details:
                - code: REVISION_FAILED_PRECONDITION
                  details: Required in-cluster components are not ready. This will be retried
                    within 15 minutes.
                implementation: TRAFFIC_DIRECTOR
                state: FAILED_PRECONDITION
    

This error is shown if the GKE cluster does not have [Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled on all node pools of that cluster, since this is a prerequisites for the installation of Cloud Service Mesh.

To resolve this error message, you must follow instructions to [Enable Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) on all node pools. Note that enablement may vary depending on your specific cluster case.

After enablement, the error message should be automatically removed and your cluster should go back to `ACTIVE` state. If the issue persists and you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/docs/getting-support).

## MESH_IAM_PERMISSION_DENIED

This error indicates that the Cloud Service Mesh service agent in the fleet project does not have the required permissions on the cluster project. This can happen if the cluster is in a different project than the fleet, or if the permissions were revoked.

To troubleshoot, follow one of the following methods:

###  Google Cloud console 

  1. In the Google Cloud console, navigate to the **IAM & Admin** > **IAM**.

  2. Select **Include Google-provided role grants**.

  3. Review the **Principal** list.

If you see the service agent with the required IAM role in the list, then it is configured correctly.

**Note:** The format of the service agent's identifier is `service-PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com`, and the required IAM role is Anthos Service Mesh Service Agent (`roles/anthosservicemesh.serviceAgent`).

If the list doesn't include the service agent and the required role, then continue to the next step.

  4. Grant the Anthos Service Mesh Service Agent role (`roles/anthosservicemesh.serviceAgent`) to the Cloud Service Mesh service agent on the project. For instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** Ensure that you don't have any automated tooling that will revert this change. If the error recurs, then update any relevant configurations.



###  Google Cloud CLI 

  1. In the Google Cloud CLI, run the following command to check if the required IAM role has been granted:
         
         gcloud projects get-iam-policy PROJECT_ID  \
         --flatten="bindings[].members" \
         --filter="bindings.members:serviceAccount:service-PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com AND bindings.role:roles/anthosservicemesh.serviceAgent" \
         --format='table(bindings.role)'
         

  2. Review the **`ROLE`** list.

If you see any roles in the list, then it is configured correctly.

If you don't see any roles in the list, then the required role was revoked.

  3. To grant the required role to the service agent, run the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
          --role="roles/anthosservicemesh.serviceAgent"
         

**Note:** Ensure that you don't have any automated tooling that will revert this change. If the error recurs, then update any relevant configurations.



If permission is verified while issue persists, contact Google customer support for further assistance.

## MESH_IAM_CROSS_PROJECT_PERMISSION_DENIED

This error indicates that the fleet project service account does not have enough permission to access a different project (the cluster project or the network project).

For [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks), make sure to grant all the fleet projects service account `Anthos Service Mesh Service Agent` role in the Shared VPC network project.

For the GKE fleet project and cluster project scenarios, make sure to grant the fleet project service account `Anthos Service Mesh Service Agent` role in the cluster project.

Example troubleshooting command:

  1. Verify if your network project or cluster project service account has granted `Anthos Service Mesh Service Agent` role to the fleet project service account. If not, run:
         
         gcloud projects add-iam-policy-binding NETWORK_OR_CLUSTER_PROJECT_ID  \
             --member "serviceAccount:service-FLEET_PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
             --role roles/anthosservicemesh.serviceAgent
         

In addition, confirm that you don't have automation that would remove this binding.

  2. If permission is verified while issue persists, contact Google customer support for further assistance.




## CONFIG_VALIDATION_ERROR

This error indicates that some mesh related configuration applied on one or more memberships in the fleet cannot be successfully applied. The error details describe how best the user can address this.
    
    
      membershipStates:
        projects/test-project/locations/us-central1/memberships/my-membership:
          servicemesh:
            conditions:
            - code: CONFIG_VALIDATION_ERROR
              details: 'Unsupported ProxyConfig fields: [proxyconfig.statNameLength]'
              severity: ERROR
            controlPlaneManagement:
    

Config validation errors for a specific configuration mandate user action. For example, errors regarding usage of unsupported api fields are best addressed by removing the offending configuration from the Mesh API.

In the Cloud Console, navigate to Kubernetes Engine > Secrets & ConfigMaps > istio-asm-managed (the name of the ConfigMap depends upon which release channel you are using; e.g. istio-asm-managed-stable or istio-asm-managed-rapid) then select the YAML tab.

For example, meshConfig.configSources is no longer supported:
    
    
    apiVersion: v1
    data:
      mesh: |
        enablePrometheusMerge: true
        trustDomain: "foobar.svc.id.goog"
        trustDomainAliases:
          - cluster.local
    
        configSources:
          - address: k8s://
          - address: fs:///var/lib/istio/config/data
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
