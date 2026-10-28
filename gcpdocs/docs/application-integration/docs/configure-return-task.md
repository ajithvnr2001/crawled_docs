---
url: https://docs.cloud.google.com/application-integration/docs/configure-return-task/
title: Return task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:43:06.928479+00:00
---

# Return task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-return-task/

[ Skip to main content ](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/application-integration/docs/configure-return-task/)
  * [Deutsch](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=de)
  * [Español](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=es-419)
  * [Français](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=id)
  * [Italiano](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=it)
  * [Português](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=ja)
  * [한국어](https://docs.cloud.google.com/application-integration/docs/configure-return-task/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fapplication-integration%2Fdocs%2Fconfigure-return-task%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/application-integration/docs)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Configure the Return task](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#configure-the-return-task)
  * [Configuration properties](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#params)
  * [Error handling strategy](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#error-handling-strategy)
  * [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#quotas-and-limits)
  * [What's next](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)


Was this helpful?
Send feedback 
  * On this page
  * [Configure the Return task](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#configure-the-return-task)
  * [Configuration properties](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#params)
  * [Error handling strategy](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#error-handling-strategy)
  * [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#quotas-and-limits)
  * [What's next](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#whats-next)


# Return task Stay organized with collections  Save and categorize content based on your preferences.
The **Return** task lets you customize the error messages corresponding to the HTTP response codes that are returned during an integration execution failure. 
You can modify or customize error messages for the following HTTP response codes:   
| HTTP code  | Canonical code  |  
| --- | --- |  
| 400  | `INVALID_ARGUMENT`  |  
| 400  | `OUT_OF_RANGE`  |  
| 401  | `UNAUTHENTICATED`  |  
| 403  | `PERMISSION_DENIED`  |  
| 404  | `NOT_FOUND`  |  
| 409  | `ALREADY_EXISTS`  |  
| 429  | `RESOURCE_EXHAUSTED`  |  
| 499  | `CANCELLED`  |  
## Configure the Return task
To configure the **Return** task: 
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
  5. Click and place the **Return** task element in the integration editor.
  6. Click the **Return** task element on the designer to open the **Return** task configuration pane.
  7. Configure the displayed fields using the [Configuration properties](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#params) for the task as detailed in the tables below. 
All changes to the properties are saved automatically. 


## Configuration properties
The following table describes the configuration properties of the **Return** task.   
|  **Property**  |  **Data type**  |  **Description**  |  
| --- | --- | --- |  
|  `**HTTP code**`  | Integer   | The [`4XX`](https://docs.cloud.google.com/application-integration/docs/configure-return-task/#codes) HTTP code for which you want to customize the error message.   |  
|  `**Customized return message**`  | String   | The custom error message for the specified HTTP code.   |  
## Error handling strategy
An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 
## Quotas and limits
For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).
## What's next
  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
