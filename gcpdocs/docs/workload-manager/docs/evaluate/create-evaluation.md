---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation/
title: Create and run an evaluation \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T07:07:03.099374+00:00
---

# Create and run an evaluation  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Create and run an evaluation Stay organized with collections  Save and categorize content based on your preferences. 

You can use Workload Manager to create and run automated evaluations that scan your workloads against industry standards and Google Cloud best practices. Running evaluations regularly lets you detect configuration drift and architectural risks early across your projects, helping you improve workload reliability, security, and performance.

You can create and run workload evaluations by using the Google Cloud console or the Workload Manager API. For conceptual information about how evaluations work, see [About Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).

## Limitations

Workload Manager supports running up to 25 evaluations simultaneously every 1 hour per project. If a project has more than 25 evaluations, then limit hourly evaluations to 25, or set the evaluation schedule to run every 6 hours or less frequently.

## Before you begin

Before you create and run a workload evaluation, complete the following prerequisites:

  1. Verify that the Google Cloud resources that you want to evaluate are already created in the target project. For a list of supported resources and rules, see the [Google Cloud Best Practices Reference](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).

  2. Enable the required APIs in the Google Cloud consumer project where you create and run evaluations:

     * [Enable the Workload Manager API](https://docs.cloud.google.com/workload-manager/docs/enable).

     * If you evaluate workloads against custom rules or best practices, enable the [Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) and the [Cloud Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com).

  3. If you evaluate an application or database workload, verify that you have set up the required agent or operator on all the compute instances or clusters that run your workload:

     * [SAP workload](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap)

     * [SQL Server workload](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sql-server)

     * [MySQL workload](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-mysql)

     * [Redis workload](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-redis)

     * [OpenShift workload](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-operator-for-openshift) ([Preview](https://cloud.google.com/products#product-launch-stages))

  4. Optional: If you want to include custom rules in addition to built-in Google Cloud best practices, upload a sample rule from the [`GoogleCloudPlatform/workload-manager`](https://github.com/GoogleCloudPlatform/workload-manager) GitHub repository to a Cloud Storage bucket whose top level contains the `/lib` and `/rules` folders. For more information about uploading custom rules, see [Write custom rules using Rego](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules#upload-custom-rules).

  5. To create and run evaluations, verify that you have the required roles and permissions.

  6. If you use the Workload Manager API to create evaluations, manually create the Workload Manager service agent in the consumer project and grant it the following roles:

     * Workload Manager Service Agent (`roles/workloadmanager.serviceAgent`) in the target projects.

     * If you set an evaluation schedule, Workload Manager Worker (`roles/workloadmanager.worker`) in the consumer project.

When you use the Google Cloud console, Workload Manager creates the service agent automatically. For more information about configuring service agents, see [Workload Manager service agents](https://docs.cloud.google.com/workload-manager/docs/access-control/service-accounts).




### Required roles

To get the permissions that you need to create and run a workload evaluation, ask your administrator to grant you the following IAM roles: 

  * Create and run an evaluation: [Workload Manager Evaluation Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`) on the consumer project 
  * Create a service agent (first evaluation only): [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the consumer and target projects 
  * Read Cloud Asset Inventory data (custom rules and best practices): [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`) on the consumer project 
  * Read custom rules from a Cloud Storage bucket (optional): [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the consumer project 
  * Create alert notifications (optional): [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the consumer project 
  * Export evaluation results to BigQuery (optional): [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) on the consumer project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and run a workload evaluation. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and run a workload evaluation:

  * Create and run an evaluation: 
    * `workloadmanager.evaluations.create` on the consumer project
    * `workloadmanager.evaluations.run` on the consumer project
  * Create a service agent (first evaluation only): `resourcemanager.projects.setIamPolicy` on the consumer and target projects 
  * Read Cloud Asset Inventory data (custom rules and best practices): `cloudasset.assets.searchAllResources` on the consumer project 
  * Read custom rules from a Cloud Storage bucket (optional): 
    * `storage.objects.get` on the consumer project
    * `storage.objects.list` on the consumer project
  * Create alert notifications (optional): `monitoring.timeSeries.create` on the consumer project 
  * Export evaluation results to BigQuery (optional): 
    * `bigquery.datasets.get` on the consumer project
    * `bigquery.tables.create` on the consumer project
    * `bigquery.tables.updateData` on the consumer project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles across consumer and target projects, see [IAM roles in consumer and target projects for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles) and [Workload Manager IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions).

## Create a workload evaluation

You can create a workload evaluation by using the Google Cloud console or the Workload Manager API. To create an evaluation that uses custom rules, see [Evaluate workloads using custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/evaluate-using-custom-rules).

###  Console 

To create a workload evaluation in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/evaluations)

  2. Select the Google Cloud consumer project where you want to store and run the evaluation.

  3. If prompted, to enable the required API for Workload Manager, click **Enable**.

  4. Click **New evaluation**.

  5. In the **Name & rules** pane, configure the evaluation details and select the rules to evaluate:

     1. For **Evaluation name** , enter a name for the workload evaluation.

     2. Optional: For **Description** , enter a description for the workload evaluation.

     3. In the **Workload type** field, select one of the following supported workload types:

        * **SAP**

        * **SQL Server**

        * **MySQL**

        * **Redis**

        * **OpenShift**

        * **Custom**

When you select **Custom** , you can evaluate your workloads against [Google Cloud best practices](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general) or against [custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/evaluate-using-custom-rules) stored in Cloud Storage.

     4. From the **Rules table** , select the best practice rules to include in the workload evaluation. For more information about each rule, see [Google Cloud Best Practices Reference](https://docs.cloud.google.com/workload-manager/docs/evaluate/best-practices-general).

  6. Click **Continue**.

  7. In the **Scope & filters** pane, specify the target projects and resource filters for the evaluation:

     1. In the **Evaluation scope** section, to add the target projects that contain the resources that you want to evaluate, click **Browse projects**.

     2. Optional: To share rule findings across target projects, select the **Share findings** checkbox. For more information, see Share evaluation findings.

     3. Optional: In the **Apply filters to resources** section, to select specific resources from the target projects, click **Add filter** , and then use any of the following filter types:

        * **Service account** : filter Compute Engine instances by their attached service account.

        * **Label** : filter resources by key-value label pairs.

        * **Name** : filter resources by resource ID pattern.

Multiple filters within the same filter type use `OR` logic. Filters across different filter types use `AND` logic.

     4. If prompted, select the [region](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) where you want Workload Manager to store the evaluation data.

  8. Click **Continue**.

  9. In the **Frequency & notification** pane, configure the evaluation schedule, export destination, and alert notifications:

     1. In the **Scheduling** section, select how frequently you want the evaluation to run.

     2. Optional: To export evaluation results to a regional BigQuery dataset in the same region as your evaluation, select **Save to BigQuery dataset** and specify the dataset. To create a separate table for the evaluation, select **Create a new results table for this evaluation**.

     3. Optional: In the **Notification** section, select the events for which you want to receive alert notifications, and then select your [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels).

  10. Click **Continue**.

  11. In the **Review** pane, review the workload evaluation settings. To modify any settings, click the pane name in the left navigation.

  12. Click **Create**.




###  REST 

To create a workload evaluation by using the Workload Manager API, follow these steps:

  1. Optional: To retrieve the list of available rule names for your workload type, send a `GET` request to the [`projects.locations.rules.list`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.rules/list) method:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "X-Goog-User-Project: CONSUMER_PROJECT_ID" \
             "https://workloadmanager.googleapis.com/v1/projects/CONSUMER_PROJECT_ID/locations/LOCATION_ID/rules?evaluationType=EVALUATION_TYPE"
         

Replace the following:

     * `CONSUMER_PROJECT_ID`: the ID of the consumer project where you run evaluations

     * `LOCATION_ID`: the [supported region](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) for the evaluation, such as `us-central1`

     * `EVALUATION_TYPE`: the [workload evaluation type](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations#EvaluationType), such as `SAP`, `SQL_SERVER`, `MYSQL`, `REDIS`, `OPENSHIFT`, or `OTHER`

  2. To create the evaluation, send a `POST` request to the [`projects.locations.evaluations.create`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations/create) method:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json; charset=utf-8" \
             -H "X-Goog-User-Project: CONSUMER_PROJECT_ID" \
             -d '{
               "description": "DESCRIPTION",
               "evaluationType": "EVALUATION_TYPE",
               "ruleNames": [
                 "RULE_NAMES"
               ],
               "resourceFilter": {
                 "scopes": [
                   "projects/TARGET_PROJECT_ID"
                 ],
                 "resourceIdPatterns": [
                   "RESOURCE_ID_PATTERNS"
                 ],
                 "inclusionLabels": {
                   "LABEL_KEY": "LABEL_VALUE"
                 },
                 "gceInstanceFilter": {
                   "serviceAccounts": [
                     "SERVICE_ACCOUNT_EMAIL"
                   ]
                 }
               },
               "schedule": "SCHEDULE",
               "bigQueryDestination": {
                 "destinationDataset": "projects/BQ_PROJECT_ID/datasets/BQ_DATASET_ID",
                 "createNewResultsTable": true
               }
             }' \
             "https://workloadmanager.googleapis.com/v1/projects/CONSUMER_PROJECT_ID/locations/LOCATION_ID/evaluations?evaluationId=EVALUATION_ID"
         

Replace the following:

     * `CONSUMER_PROJECT_ID`: the ID of the consumer project where you create the evaluation

     * `LOCATION_ID`: the [supported region](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations) where Workload Manager stores the evaluation, such as `us-central1`

     * `EVALUATION_ID`: a unique ID for the evaluation

     * `DESCRIPTION`: a description of the evaluation

     * `EVALUATION_TYPE`: the [workload evaluation type](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations#EvaluationType), such as `SAP`, `SQL_SERVER`, `MYSQL`, `REDIS`, `OPENSHIFT`, or `OTHER`

     * `RULE_NAMES`: a comma-separated list of rule IDs to include in the evaluation

     * `TARGET_PROJECT_ID`: the project ID or project number of the target project that contains the resources to evaluate

     * `RESOURCE_ID_PATTERNS`: optional resource name patterns to filter evaluated resources, such as `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance*`

     * `LABEL_KEY` and `LABEL_VALUE`: optional key-value label pairs to filter resources

     * `SERVICE_ACCOUNT_EMAIL`: optional service account email address to filter Compute Engine instances

     * `SCHEDULE`: optional cron expression in UTC for recurring evaluation runs, such as `0 */6 * * *` to run every 6 hours

     * `BQ_PROJECT_ID` and `BQ_DATASET_ID`: optional project ID and regional BigQuery dataset ID for exporting evaluation results

For more information about supported fields, see the [`Evaluation`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations#Evaluation) resource reference.




## Run a workload evaluation

In addition to running evaluations on a recurring schedule, you can run an existing workload evaluation on demand at any time by using the Google Cloud console or the Workload Manager API.

###  Console 

To run a workload evaluation in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/evaluations)

  2. Click the name of the evaluation that you want to run.

  3. On the **Evaluation information** page, click **Run**.

A workload evaluation takes a few minutes to complete. Before you view the latest results, wait for the evaluation run to finish.




###  REST 

To run a workload evaluation by using the Workload Manager API, send a `POST` request to the [`projects.locations.evaluations.executions.run`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations.executions/run) method:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -H "X-Goog-User-Project: CONSUMER_PROJECT_ID" \
        -d '{
          "executionId": "EXECUTION_ID"
        }' \
        "https://workloadmanager.googleapis.com/v1/projects/CONSUMER_PROJECT_ID/locations/LOCATION_ID/evaluations/EVALUATION_ID/executions:run"
    

Replace the following:

  * `CONSUMER_PROJECT_ID`: the ID of the consumer project that stores the evaluation.

  * `LOCATION_ID`: the region of the evaluation, such as `us-central1`.

  * `EVALUATION_ID`: the ID of the evaluation that you want to run.

  * `EXECUTION_ID`: an optional unique ID for this execution run. To let Workload Manager generate an ID automatically, omit this field.




The request returns a long-running [`Operation`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.operations#Operation). To check the status of the execution or list its results, use the [`projects.locations.evaluations.executions.get`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations.executions/get) and [`projects.locations.evaluations.executions.results.list`](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations.executions.results/list) methods.

## Share evaluation findings

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Sharing evaluation findings lets resource owners in target projects view configuration findings in their local project consoles and on integrated pages such as Compute Engine. This capability does not require direct IAM access to the consumer project.

### Required roles

To get the permissions that you need to share evaluation findings, ask your administrator to grant you the following IAM roles: 

  * [Workload Manager Evaluation Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`) on the consumer project
  * [Workload Manager Evaluation Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadmanager#workloadmanager.evaluationAdmin) (`roles/workloadmanager.evaluationAdmin`) on the target project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to share evaluation findings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to share evaluation findings:

  * `workloadmanager.evaluations.create` on the consumer project
  * `workloadmanager.evaluations.update` on the consumer project
  * `workloadmanager.findings.create` on the target project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Edit an evaluation to share findings

To enable or disable sharing findings for an existing evaluation, follow these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/evaluations)

  2. Click the name of the evaluation that you want to edit.

  3. Click **Edit**.

  4. In the **Scope & filters** section, select or clear the **Share findings** checkbox.

  5. Click **Save**.




### Visibility of shared findings

When you enable **Share findings** , Workload Manager propagates rule findings to all target projects that are specified in the evaluation scope. Findings are visible in the **Rule findings** tab and on integrated pages such as the Compute Engine **Overview** page.

When you disable **Share findings** , Workload Manager stops propagating rule findings to target projects, and the findings remain visible only within the consumer project.

## Set alert notifications for evaluations

You can configure alert notifications so that Workload Manager notifies your chosen notification channels when specific evaluation events occur, such as when an evaluation detects new findings or fails to run. If you didn't configure alert notifications when you created the evaluation, you can add or update them for an existing evaluation in the Google Cloud console by following these steps:

  1. In the Google Cloud console, go to the **Workload Manager** page.

[Go to Workload Manager](https://console.cloud.google.com/workload-manager/evaluations)

  2. Click the name of the evaluation for which you want to enable alert notifications.

  3. Click **Edit**.

  4. Select the **Notification** section.

  5. Select the events for which you want to receive alert notifications, and then select your [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels).

  6. Click **Save**.




## What's next

  * [View evaluation results and history](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-evaluation-results)

  * [View Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/evaluate/view-rule-findings)

  * [About Workload Manager rule findings](https://docs.cloud.google.com/workload-manager/docs/about-rule-findings)

  * [View Workload Manager rule findings in Compute Engine](https://docs.cloud.google.com/compute/docs/view-wlm-findings)

  * [Evaluate workloads using custom rules](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/evaluate-using-custom-rules)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
