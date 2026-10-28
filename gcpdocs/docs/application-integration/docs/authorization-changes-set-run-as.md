---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as/
title: Set a run-as service account \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:50:59.597760+00:00
---

# Set a run-as service account  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set a run-as service account

This page details the steps for each integration that [requires a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected) but doesn't currently have one, as part of preparing for the [authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

## Set the service account

  1. Create or select a service account, and grant it the roles required by the integration's tasks. To determine the necessary roles, review the roles currently held by your project's Application Integration service agent (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`), and assign only the permissions that this specific integration requires.
  2. [Grant the Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) role on the run-as service account to any user or entity that requires access, including automation and trigger service accounts.
  3. Open the integration in the integration editor, and then click settings **Integration settings** in the editor toolbar. 

![The integration editor toolbar showing the Integration settings icon next to the Integration information icon, and the Publish button on the right.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-editor-toolbar.png)![The integration editor toolbar showing the Integration settings icon next to the Integration information icon, and the Publish button on the right.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-editor-toolbar.png)

  4. In the **Integration settings** pane, click the **Service account** drop-down list, and select the service account. If the service account does not exist yet, click **New service account** to create it. 

![The Service account list open in the Integration settings pane, displaying 'No service account' alongside a list of available project service accounts.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-select.png)![The Service account list open in the Integration settings pane, displaying 'No service account' alongside a list of available project service accounts.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-select.png)

  5. Click **Save**. 

![The Integration settings pane with a service account selected in the Service account field, followed by the Save button.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-selected.png)![The Integration settings pane with a service account selected in the Service account field, followed by the Save button.](https://docs.cloud.google.com/static/application-integration/images/runas-sa-selected.png)

  6. Click **Publish**. The new run-as service account takes effect for all future executions of this published version. For more information, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).



## Use one service account per integration

Google Cloud recommends using a dedicated, minimally scoped service account for each integration rather than a single broadly privileged account shared across multiple integrations. This approach provides the following benefits:

  * Limits the security and operational impact to a single integration.
  * Clearly identifies each integration in your audit logs by the name of its service account.



For more information, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

## What's next

  * If publishing or an execution fails after making this change, see [Troubleshoot authorization errors](https://docs.cloud.google.com/application-integration/docs/authorization-changes-troubleshoot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
