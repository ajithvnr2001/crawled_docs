---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects/
title: Create Harbor projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:20:35.894260+00:00
---

# Create Harbor projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create Harbor projects Stay organized with collections  Save and categorize content based on your preferences. 

In Harbor, a project serves as a logical unit for organizing and managing a collection of container images. It provides a way to group related artifacts together and apply specific policies, access controls, and replication rules to the entire collection. Images cannot be pushed or pulled to Harbor before a project is created.

## Before you begin

Before you begin, you must initialize your identity with the Harbor registry by signing in to the Harbor UI at least once.

**Warning:** Attempting to create a Harbor project without first initializing your Harbor identity can cause the process to fail or remain pending.

### Required IAM role

To create Harbor projects and manage image namespaces, contact your IAM Project Admin to request the **Harbor Project Creator** (`harbor-project-creator`) role, which lets you create, get, and watch Harbor projects in the project namespace. This role includes the required permissions to define new image namespaces so you can establish security boundaries for your containerized applications.

## Create a Harbor project

Create a Harbor project by using the GDC console, the gdcloud CLI, or the API.

###  Console 

In the GDC console, follow these steps:

  1. Click the **Harbor Container Registry** link in the **CI/CD** section in the navigation menu.
  2. Click **Create a Harbor project**.
  3. Enter the name of the project.
  4. Optional: Vulnerability scanning is enabled by default. To disable automatic vulnerability scanning for Harbor projects, click the **Enable vulnerability scanning for the project** toggle. For more information, see [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities).
  5. Click **Create**.
  6. A confirmation message appears stating your project is created successfully.
  7. After your Harbor project is created, sign in to the Harbor UI to confirm that you can view the Harbor project.



###  gdcloud 

Create the Harbor project:
    
    
      gdcloud harbor harbor-projects create HARBOR_PROJECT \
        --project=PROJECT \
        --instance=INSTANCE
    

Replace the following:

  * `HARBOR_PROJECT`: the name of the Harbor project to create.
  * `PROJECT`: the name of the GDC project.
  * `INSTANCE`: the name of the instance.



###  API 

The GDC console and the gdcloud CLI set the Harbor project creator to your user account. When you use the API, you must set the `spec.creatorSubject` field yourself.

  1. Create a `HarborInstanceProject` custom resource on the zonal management API server. You can't change the `creatorSubject` or `autoScan` field after you create the resource, so check both values before you create it.
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER create -f - <<EOF
         apiVersion: artifactregistry.gdc.goog/v1
         kind: HarborInstanceProject
         metadata:
           name: INSTANCE-HARBOR_PROJECT
           namespace: PROJECT
         spec:
           projectName: HARBOR_PROJECT
           harborInstanceRef:
             name: INSTANCE
           creatorSubject:
             apiGroup: rbac.authorization.k8s.io
             kind: User
             name: HARBOR_USERNAME
           autoScan: true
         EOF
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the path to the kubeconfig file for the zonal management API server. For more information, see [Switch to a zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `INSTANCE`: the name of the Harbor registry instance.
     * `HARBOR_PROJECT`: the name of the Harbor project to create.
     * `PROJECT`: the name of the GDC project that contains the Harbor registry instance.
     * `HARBOR_USERNAME`: your Harbor username, exactly as shown in the Harbor UI user menu after you sign in. This user becomes the Harbor Project Admin of the Harbor project. Use the username of a person, not a service account. For more information, see Before you begin.

The `autoScan` field enables automatic vulnerability scanning for images that are pushed to the project. To disable automatic scanning, set it to `false`. For more information, see [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities).

**Caution:** The `spec.creatorSubject` field is required. Omitting or removing this field stops the Harbor service from processing changes to Harbor resources across your organization. To recover, see Fix a Harbor project created without a creator.
  2. Verify that the Harbor project is created and the creator is assigned:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get harborinstanceproject INSTANCE-HARBOR_PROJECT \
           -n PROJECT
         

The `PROJECTCREATEDSTATUS` column shows `Created`, and the `PROJECTSUBJECTASSIGNEDSTATUS` column shows `SubjectAssigned`.

If the `PROJECTSUBJECTASSIGNEDSTATUS` column shows `SubjectAssignError`, check the condition message:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           describe harborinstanceproject INSTANCE-HARBOR_PROJECT \
           -n PROJECT
         

A `user ... not found` message means that the user specified in the `creatorSubject` field hasn't signed in to the Harbor UI yet. The Harbor service retries every 30 seconds, so the status changes to `SubjectAssigned` after the user signs in.




## Fix a Harbor project created without a creator

If a `HarborInstanceProject` resource in any project of your organization doesn't set the `spec.creatorSubject` field, the Harbor service stops processing changes to Harbor resources across your organization. Symptoms include Harbor instances that don't become ready, new Harbor projects that stay without a status, and image pulls that fail with `x509: certificate signed by unknown authority` errors.

To fix this issue, you need the **Harbor Instance Admin** (`harbor-instance-admin`) role in the project that contains the affected resource. If you don't have this role, ask a user who has it to complete these steps. If you don't know which resource is affected, contact your infrastructure operator (IO), who can find it in the Harbor service logs.

  1. Check whether the affected `HarborInstanceProject` resource sets the `spec.creatorSubject` field:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get harborinstanceproject HARBOR_INSTANCE_PROJECT \
           -n PROJECT -o jsonpath='{.spec.creatorSubject}'
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the path to the kubeconfig file for the zonal management API server. For more information, see [Switch to a zonal context](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones#switch-zonal-context).
     * `HARBOR_INSTANCE_PROJECT`: the name of the `HarborInstanceProject` resource. Resources that you create from the **API** tab on this page are named `INSTANCE-HARBOR_PROJECT`.
     * `PROJECT`: the name of the GDC project that contains the resource.

Empty output means that the field isn't set.

  2. Confirm the Harbor username to assign as the Harbor Project Admin with the owner of the GDC project. Because you can't change the `spec.creatorSubject` field after you set it, verify the username before you add the field to each affected resource:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           patch harborinstanceproject HARBOR_INSTANCE_PROJECT \
           -n PROJECT --type merge \
           -p '{"spec":{"creatorSubject":{"apiGroup":"rbac.authorization.k8s.io","kind":"User","name":"HARBOR_USERNAME"}}}'
         

Replace `HARBOR_USERNAME` with the Harbor username of the user to assign as the Harbor Project Admin. This role can delete images and manage project members. The user must have signed in to the Harbor UI at least once, and the username must exactly match the name shown in the Harbor UI user menu.

  3. Verify that the creator is assigned:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get harborinstanceproject HARBOR_INSTANCE_PROJECT \
           -n PROJECT
         

After all affected resources are fixed, the Harbor service restarts and resumes processing changes within about 10 minutes, and the `PROJECTSUBJECTASSIGNEDSTATUS` column shows `SubjectAssigned`. If image pulls from Harbor still fail after 15 minutes, contact your IO. Give the IO the names and projects of the resources that you fixed, so that the IO can check for other affected resources and restart the Harbor service if needed.




## What's next

After you create a Harbor project, configure your Docker and Helm clients to connect to your Harbor registry:

  * [Configure Docker to trust the Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust)
  * [Sign in to Docker and Helm](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
