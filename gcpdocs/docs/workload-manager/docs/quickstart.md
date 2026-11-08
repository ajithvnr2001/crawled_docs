---
url: https://docs.cloud.google.com/workload-manager/docs/quickstart/
title: Quickstart: Evaluate workloads against Google Cloud best practices and custom rules \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T05:38:27.796039+00:00
---

# Quickstart: Evaluate workloads against Google Cloud best practices and custom rules  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Quickstart: Evaluate workloads against Google Cloud best practices and custom rules Stay organized with collections  Save and categorize content based on your preferences. 

Workload Manager helps you scan your workloads to detect configuration deviations from standards and best practices, improving system quality, reliability, and performance. In this quickstart, you create and run a workload evaluation in the Google Cloud console to check your workloads against [Google Cloud best practices](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general) and custom rules.

## Before you begin

  1. Verify that the Google Cloud resources that you want to evaluate are already created in the target project. For a list of supported resources and rules, see the [Google Cloud Best Practices Reference](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).
  2. Enable the following APIs in the Google Cloud consumer project where you create and run the evaluation: 
     * [Workload Manager API](https://docs.cloud.google.com/workload-manager/docs/enable)
     * [Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)
     * [Cloud Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com)
  3. Optional: If you want to include custom rules in addition to built-in Google Cloud best practices, upload a sample rule from the [`GoogleCloudPlatform/workload-manager`](https://github.com/GoogleCloudPlatform/workload-manager) GitHub repository to a Cloud Storage bucket whose top level contains the `/lib` and `/rules` folders. For more information about uploading custom rules, see [Write custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules#upload-custom-rules).



### Required roles

To get the permissions that you need to create and run a workload evaluation, ask your administrator to grant you the following IAM roles: 

  * Create and run an evaluation: [Workload Manager Evaluation Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`) on the consumer project 
  * Create a service agent (first evaluation only): [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the consumer and target projects 
  * Read Cloud Asset Inventory data: [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`) on the consumer project 
  * Read custom rules from a Cloud Storage bucket (optional): [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the consumer project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and run a workload evaluation. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and run a workload evaluation:

  * Create and run an evaluation: 
    * `workloadmanager.evaluations.create` on the consumer project
    * `workloadmanager.evaluations.run` on the consumer project
  * Create a service agent (first evaluation only): `resourcemanager.projects.setIamPolicy` on the consumer and target projects 
  * Read Cloud Asset Inventory data: `cloudasset.assets.searchAllResources` on the consumer project 
  * Read custom rules from a Cloud Storage bucket (optional): 
    * `storage.objects.get` on the consumer project
    * `storage.objects.list` on the consumer project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about required roles in consumer and target projects, see [IAM roles in consumer and target projects for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles) and [Workload Manager IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions).

## Create a workload evaluation

To create a workload evaluation in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[ Go to Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation)   
school The remaining steps appear in the Google Cloud console. 

  2. Select the Google Cloud consumer project where you want to store and run the evaluation.
  3. If prompted, to enable the required API for Workload Manager, click **Enable**.
  4. Click **New evaluation**.
  5. In the **Name & rules** pane, configure the evaluation details and select the rules to evaluate: 
     1. For **Evaluation name** , enter `my-custom-evaluation`.
     2. Optional: For **Description** , enter a description for the workload evaluation.
     3. In the **Workload type** field, select **Custom**.
     4. Optional: To include custom rules in addition to built-in Google Cloud best practices, select the Cloud Storage bucket that contains your custom rules.
     5. From the **Rules table** , select the best practice rules to validate your resources against. For more information about the supported rules, see [Google Cloud Best Practices Reference](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).
  6. Click **Continue**.
  7. In the **Scope & filters** pane, specify the target scopes, resource filters, and evaluation regions: 
     1. In the **Evaluation scope** section, to select the organizations, folders, or projects in which you want to run the evaluation, click **Browse scopes**.
     2. Optional: To share rule findings across target scopes, select the **Share findings** checkbox.
     3. Optional: In the **Apply filters to resources** section, to select specific resources, click **Add filter** , and then use any of the following filter types: 
        * **Service account** : filter Compute Engine instances by their attached service account.
        * **Label** : filter resources by key-value label pairs.
        * **Name** : filter resources by resource ID pattern.

Multiple filters within the same filter type use `OR` logic. Filters across different filter types use `AND` logic.

     4. In the **Locations for evaluation data** section, select the **Regions** where you want Workload Manager to store the evaluation data.
  8. Click **Continue**.
  9. In the **Frequency & notification** pane, configure the evaluation schedule and alert notifications: 
     1. In the **Scheduling** section, select how frequently you want the evaluation to run.
     2. Optional: In the **Notification** section, select the events for which you want to receive alert notifications, and then select your notification channels.
  10. Click **Continue**.
  11. In the **Review** pane, review the workload evaluation settings. To modify any settings, click the pane name in the left navigation.
  12. Click **Create**.



## Run a workload evaluation

To run the workload evaluation on demand in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[ Go to Workload Manager](https://console.cloud.google.com/workloads?walkthrough_id=workload-manager--create-evaluation)   
school The remaining steps appear in the Google Cloud console. 

  2. Click `my-custom-evaluation`.
  3. On the **Evaluation information** page, click **Run**. 

A workload evaluation takes a few minutes to complete. Before you view the results, wait for the evaluation run to finish.




## Clean up

If you no longer need the `my-custom-evaluation` workload evaluation or the optional Cloud Storage bucket that you created in this quickstart, you can delete them. Deleting an evaluation doesn't affect your workloads. For more information about deleting an evaluation, see [Delete an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/delete-evaluation).

## What's next

  * [Google Cloud Best Practices Reference](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general)
  * [Create and run an evaluation using the Google Cloud console or REST API](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)
  * [View evaluation results and history](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-evaluation-results)
  * [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings)
  * [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
