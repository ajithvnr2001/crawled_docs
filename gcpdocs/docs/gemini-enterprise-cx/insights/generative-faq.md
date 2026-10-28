---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/generative-faq/
title: Generative FAQ \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:35:15.649367+00:00
---

# Generative FAQ  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/generative-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Generative FAQ Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Generative FAQ in CX Insights shows you the questions that customers are asking your contact center and how these questions are being answered. This information can help you identify gaps in your FAQs, track trending questions, and improve customer service responses.

## How to begin

To enable the Generative FAQ feature, follow these steps:

  1. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights).
  2. If prompted, sign in using your Google Account.
  3. Enter your project ID.
  4. From the navigation menu on the left, select **Generative FAQ**.
  5. Click **Enable**.
  6. Provide an optional filter to narrow down your dataset.
  7. Choose an optional Agent from Dialogflow for answer content generation.
  8. Click **Start**. This process can take as long as 24 hours.



After the generation process, the questions appear in a table on this screen.

## After generation

The table shows aggregate metric information for each inquiry on conversations that have been ingested into CX Insights. Clicking on a customer inquiry row shows details and conversation samples with the related inquiry. 

For users with an active Generative AI Agent setup, generated answers to these questions appear on the side panel. To update the Generative AI Agent knowledge base, see the [Generative AI Agent documentation](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#agent).

To export generative FAQ as a CSV file, click **Download Spreadsheet**. Use the exported generative FAQ to improve your knowledge base.

As CX Insights ingests new conversations, you can regenerate questions by clicking **Regenerate**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
