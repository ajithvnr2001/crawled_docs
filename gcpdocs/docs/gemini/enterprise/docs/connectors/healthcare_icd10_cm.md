---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_icd10_cm/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:26.808085+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_icd10_cm/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The ICD-10 Codes data store for Gemini Enterprise lets you search and validate ICD-10-CM diagnosis codes, billable status, and hierarchy using natural language. End users can do the following without leaving Gemini Enterprise:

  * Search ICD-10-CM codes by condition, symptom, or code prefix.
  * Check whether a code is billable or needs more specificity.
  * List the codes under a category, such as `E11`.



Because the ICD-10-CM API is public, the ICD-10 Codes data store doesn't require an account, credentials, or an OAuth application.

## Supported actions

When the ICD-10 Codes data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. These actions only read data, and they're enabled by default.

Action | Description  
---|---  
Search Icd10 Codes | Finds ICD-10-CM codes and their official descriptions by condition, symptom, or code prefix. Returns up to 25 codes by default, and up to 100.  
Validate Icd10 Code | Checks whether a code exists and whether it's billable. A code is billable when it matches exactly and has no more specific codes under it. If the code isn't billable, lists the more specific codes.  
Lookup Code Hierarchy | Lists the more specific codes under an ICD-10-CM category in one request.  
**Note:** All three actions send the search terms or code from the user's request to the public ICD-10-CM API. By default, Gemini Enterprise asks the user to confirm each request before sending it.

The ICD-10 Codes data store contains diagnosis code data, not patient data. Don't include patient information, such as patient names, dates of birth, medical record numbers, or other protected health information (PHI), in requests that use the ICD-10 Codes data store.

## Limitations

The ICD-10 Codes data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing ICD-10 Codes data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The ICD-10 Codes data store is supported only in the `global` and `us` locations.

  * The ICD-10 Codes data store covers ICD-10-CM diagnosis codes only. It doesn't cover ICD-10-PCS procedure codes.

  * **Search Icd10 Codes** accepts search terms from 2 to 200 characters.

  * **Validate Icd10 Code** and **Lookup Code Hierarchy** accept a code with a letter, a digit, and a letter or digit, optionally followed by a dot and 1 to 4 letters or digits, for example, `E11`, `E11.9`, or `S82.101A`. Codes are converted to uppercase, and a code without its dot gets one. For example, `E119` becomes `E11.9`.

  * If a code doesn't match this format, Gemini Enterprise doesn't send the request and asks the user to correct the code.




## What's next

  * To create and configure a data store with ICD-10 Codes, see [Set up a ICD-10 Codes data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_icd10_cm/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 
