---
url: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/
title: Vertex AI - Predict task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:09:47.605761+00:00
---

# Vertex AI - Predict task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/

[ Skip to main content ](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/)
  * [Deutsch](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=de)
  * [Español](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=es-419)
  * [Français](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=id)
  * [Italiano](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=it)
  * [Português](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=ja)
  * [한국어](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fapplication-integration%2Fdocs%2Fgcp-tasks%2Fconfigure-vertex-ai-predict-task%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/application-integration/docs)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#before-you-begin)
  * [Configure the Vertex AI - Predict task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#configure-the-vertex-ai---predict-task)
  * [Task input parameters](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#params)
  * [Task output](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#task-output)
  * [Error handling strategy](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#error-handling-strategy)
  * [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#quotas-and-limits)
  * [What's next](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#params)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)


Was this helpful?
Send feedback 
  * On this page
  * [Before you begin](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#before-you-begin)
  * [Configure the Vertex AI - Predict task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#configure-the-vertex-ai---predict-task)
  * [Task input parameters](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#params)
  * [Task output](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#task-output)
  * [Error handling strategy](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#error-handling-strategy)
  * [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#quotas-and-limits)
  * [What's next](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#params)


# Vertex AI - Predict task Stay organized with collections  Save and categorize content based on your preferences.
The **Vertex AI - Predict** task lets you perform an online prediction. Online predictions are synchronous requests made to a model [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints). You can use online predictions when making requests in response to application inputs or when you require timely inferences.
[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) is a Google Cloud service that allows you to train and deploy ML models and AI applications, and customize large language models (LLMs) for use in your AI-powered applications. 
## Before you begin
Ensure that you perform the following tasks in your Google Cloud project before configuring the **Vertex AI - Predict** task:
  1. Enable the Vertex AI API (`aiplatform.googleapis.com`). 
[ Enable the Vertex AI API ](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)
  2. Deploy the [model](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) resource to the [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints).
  3. Create an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile). Application Integration uses an authentication profile to connect to an authentication endpoint for the **Vertex AI - Predict** task. 
  4. Ensure that [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is **NOT** setup for Application Integration in your Google Cloud project. 


## Configure the Vertex AI - Predict task
  1. In the Google Cloud console, go to the **Application Integration** page. 
[Go to Application Integration](https://console.cloud.google.com/integrations)
  2. In the navigation menu, click **Integrations**. 
The **Integrations** page appears listing all the integrations available in the Google Cloud project. 
  3. Select an existing integration or click **Create integration** to create a new one. 
If you are creating a new integration: 
    1. Enter a name and description in the **Create Integration** pane.
    2. Select a region for the integration. 
    3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. 
    4. Click **Create**. The newly created integration opens in the _integration editor_. 
  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Vertex AI - Predict** element in the integration editor.
  6. Click the **Vertex AI - Predict** element on the designer to view the **Vertex AI - Predict** task configuration pane.
  7. Go to **Authentication** , and select an existing authentication profile that you want to use. 
Optional. If you have not created an authentication profile prior to configuring the task, Click **+ New authentication profile** and follow the steps as mentioned in [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile).
  8. Go to **Task Input** , and configure the displayed inputs fields using the following [Task input parameters](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task/#params) table. 
Changes to the inputs fields are saved automatically.


## Task input parameters
The following table describes the input parameters of the **Vertex AI - Predict** task:   
| Property   | Data type   | Description   |  
| --- | --- | --- |  
| Region   | String   | Model endpoint [location](https://docs.cloud.google.com/document-ai/docs/regions). For example: `us` - United States.  |  
| ProjectsId   | String   | Your Google Cloud project ID.  |  
| Endpoint  | String   | The name of the [endpoint](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints) requested to serve the prediction.  |  
| Request   | JSON   | See [request JSON structure.](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict#request-body)  |  
## Task output
The **Vertex AI - Predict** task returns a response containing the [prediction](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/PredictResponse). 
## Error handling strategy
An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 
## Quotas and limits
For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).
## What's next
  * For information about how to use the Vertex AI task with a pre-existing model, see [AI powered applications with Application Integration and Vertex AI](https://www.googlecloudcommunity.com/gc/Integration-Services/AI-powered-applications-with-Application-Integration-and-Vertex/td-p/696540).
  * To learn how to use Vertex AI in Application Integration, see [Enhancing your business integration flows with Vertex AI](https://www.googlecloudcommunity.com/gc/Integration-Services/Enhancing-your-business-integration-flows-with-GenAI-Vertex-AI/td-p/696527).
  * [Test and publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) your integration.
  * Add a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task).
  * Learn about [all supported tasks and triggers](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-tasks-for-google-cloud-services).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
