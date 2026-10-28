---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/google-sheets-integration/
title: Enable Sheets integration \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:32:38.503228+00:00
---

# Enable Sheets integration  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/google-sheets-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Enable Sheets integration Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Some Customer Experience Insights features support the use of Google Sheets for storing data. For these compatible features, you can use Sheets as a data source or destination, instead of Cloud Storage. To do this, you share a Sheets spreadsheet with the Customer Experience Insights [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) that is associated with your Google Cloud project.

## Integrate Sheets

To integrate Sheets with Customer Experience Insights, do the following:

  1. Find your Customer Experience Insights service account by going to IAM.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. To reveal the Customer Experience Insights service account, check the **Include Google-provided role grants** box.

For more help finding your Customer Experience Insights service account, see [Troubleshooting service account access](https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues).

  3. Share your spreadsheet with your Customer Experience Insights service account's email address.

  4. Copy the spreadsheet's URL.

  5. Paste the spreadsheet's URL into the CX Insights console or API. The spreadsheet URL contains the spreadsheet ID, as shown in the following example:
         
         https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit?gid=WORKSHEET_ID
         




Use `?gid=WORKSHEET_ID` to specify a worksheet in your spreadsheet. Specifying a worksheet is optional. If you don't specify a worksheet, CX Insights uses the first worksheet in the spreadsheet.

**Note:** Other information in the spreadsheet URL, such as the `resource_key` parameter, is ignored by CX Insights.

## Use Sheets with CX Insights

After integrating with your spreadsheet, CX Insights can read the data from your worksheet when an operation calls for it or use the entire spreadsheet. CX Insights can also create worksheet tabs. However, CX Insights can't connect to and use new spreadsheets, unless you share the spreadsheets first.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
