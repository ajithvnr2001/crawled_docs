---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis/
title: Enable Vertex AI APIs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T02:29:56.826347+00:00
---

# Enable Vertex AI APIs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Enable Vertex AI APIs Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI in Google Distributed Cloud (GDC) air-gapped provides pre-trained APIs for integrating artificial intelligence (AI) and machine learning (ML) into your air-gapped applications. Enable or deactivate these APIs in the GDC console so that users in your organization can interact with AI models and capabilities.

In the GDC console, you can enable [Generative AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-overview), [Online Prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions), [Optical Character Recognition (OCR)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ocr), [Speech-to-Text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-stt), [Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation), and [Vertex AI Workbench](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-intro). This document is for application developers in application operator groups who optimize air-gapped applications with AI features. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you begin, check that you've done the following prerequisite steps:

  1. You must have the AI Platform Admin (`ai-platform-admin`) role to set up access to the Vertex AI APIs. You can contact your IAM Org Admin or IAM Project Admin to request the role if you don't already have it. Alternatively, you can ask your administrator to enable Vertex AI APIs on your behalf. For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).
  2. Set up the GDC domain name system (DNS). If you haven't set up the DNS, work with your Infrastructure Operator (IO) to complete this prerequisite.
  3. [Set up a project to use Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).
  4. If you bring your own model because you want to use [Online Prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions) or run artificial intelligence (AI) and machine learning (ML) notebooks in a GPU environment, make sure to [allocate GPU machines](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster#gpu) for the correct cluster types.

**Note:** Pre-trained APIs run on a shared service Kubernetes cluster managed by the infrastructure.



## Enable pre-trained APIs

You can enable Vertex AI service APIs and models using the GDC console.

After meeting the prerequisites, follow these steps to enable APIs:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in). If you can't sign in, see [Connect to an identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, click **Enable** on a specific service to enable that API.

**Note:** The GDC console doesn't display the buttons to enable the pre-trained APIs if you don't have the correct permissions.
  4. In the confirmation dialog, click **Enable**. A progress message displays.




The enablement duration varies. It might take between 15 and 45 minutes to finish, depending on the state of the cluster.

If you want to view the status of the pre-trained APIs, [view the service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

The VAI-A0001 alert for `Enabling State Time Limit Reached` triggers if the services take a long time to be enabled. In this case, your IO must review the [VAI-R0001](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/gdcag-io/service-manual/vai/runbooks/vai-r0001) runbook for details.

**Note:** You can't enable an API while you wait for another API to finish deactivating.

## Deactivate pre-trained APIs

You can deactivate pre-trained APIs using the GDC console.

After meeting the prerequisites, follow these steps to deactivate APIs:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.
  3. On the **Pre-trained APIs** page, click **Disable** on a specific service to deactivate that API.

**Note:** The GDC console doesn't display the buttons to deactivate the pre-trained APIs if you don't have the correct permissions.
  4. In the confirmation dialog, enter _disable_ in the text field to confirm that you want to take that action. Then, click **Disable**. A progress message displays.




If you want to view the status of the pre-trained APIs, [view the service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).

**Note:** You can't deactivate an API while you wait for another API to finish enabling.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
