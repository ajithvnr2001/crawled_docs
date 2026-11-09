---
url: https://docs.cloud.google.com/walkthroughs/workload-manager/create-evaluation/
title: Create and run an evaluation \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T07:07:02.944177+00:00
---

# Create and run an evaluation  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/walkthroughs/workload-manager/create-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)



Send feedback 

#  Create and run an evaluation Stay organized with collections  Save and categorize content based on your preferences. 

In this walkthrough, you create and run an evaluation in Workload Manager to detect configuration deviations from standards and best practices.

### Create a workload evaluation

To create a workload evaluation in the Google Cloud console, follow these steps:

  1. Select the Google Cloud consumer project where you want to store and run the evaluation.
  2. If prompted, to enable the required API for Workload Manager, click **Enable**.
  3. Click **New evaluation**.
  4. In the **Name & rules** pane, configure the evaluation details and select the rules to evaluate: 
     1. For **Evaluation name** , enter a name for the workload evaluation.
     2. Optional: For **Description** , enter a description for the workload evaluation.
     3. In the **Workload type** field, select the type of workload evaluation.
     4. From the **Rules table** , select the best practice rules to include in the workload evaluation.
  5. Click **Continue**.
  6. In the **Scope & filters** pane, specify the target projects and resource filters for the evaluation: 
     1. In the **Evaluation scope** section, to add the target projects that contain the resources that you want to evaluate, click **Browse projects**.
     2. Optional: To share rule findings across target projects, select the **Share findings** checkbox.
     3. Optional: In the **Apply filters to resources** section, to select specific resources from the target projects, click **Add filter** , and then use any of the following filter types: 
        * **Service account** : filter Compute Engine instances by their attached service account.
        * **Label** : filter resources by key-value label pairs.
        * **Name** : filter resources by resource ID pattern.

Multiple filters within the same filter type use `OR` logic. Filters across different filter types use `AND` logic.

  7. Click **Continue**.
  8. In the **Frequency & notification** pane, configure the evaluation schedule and alert notifications: 
     1. In the **Scheduling** section, select how frequently you want the evaluation to run.
     2. Optional: In the **Notification** section, select the events for which you want to receive alert notifications, and then select your notification channels.
  9. Click **Continue**.
  10. In the **Review** pane, review the workload evaluation settings. To modify any settings, click the pane name in the left navigation.
  11. Click **Create**.



### Run a workload evaluation

To run the workload evaluation on demand in the Google Cloud console, follow these steps:

  1. Click the name of the evaluation that you want to run.
  2. On the **Evaluation information** page, click **Run**. 

A workload evaluation takes a few minutes to complete. Before you view the results, wait for the evaluation run to finish.




### Next step

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
