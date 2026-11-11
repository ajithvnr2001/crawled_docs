---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_rxnorm/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:42.938861+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_rxnorm/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The RxNorm Drug Vocabulary data store for Gemini Enterprise lets you look up standardized drug names, ingredients, strengths, dose forms, and National Drug Codes (NDCs) in the public RxNorm drug vocabulary using natural language. End users can do the following without leaving Gemini Enterprise:

  * Find RxNorm concept unique identifiers (RxCUIs) for a generic or brand drug name and strength.
  * Get an RxCUI's status, ingredients, strengths, and dose form.
  * Map an NDC to its RxCUI, and list the NDCs of a drug product.



Because the RxNorm API is public, the RxNorm Drug Vocabulary data store doesn't require an account, credentials, or an OAuth application.

## Supported actions

When the RxNorm Drug Vocabulary data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. These actions only read data, and they're enabled by default.

Action | Description  
---|---  
Search RxNorm drugs by name | Finds RxNorm products for a drug name, grouped as generic drugs, branded drugs, generic packs, and branded packs. If no product matches, returns ranked approximate matches.  
Get RxNorm concept details | Returns the status, name, ingredients, strengths, and dose form of an RxCUI. For a remapped RxCUI, returns the replacement RxCUI.  
Map an NDC to RxNorm | Maps an NDC to its RxCUI, concept name, and NDC status.  
List NDCs for an RxNorm product | Lists the active NDCs of a drug product RxCUI, in 11-digit form.  
**Note:** All four actions send the drug name, RxCUI, or NDC from the user's request to the public RxNorm API. By default, Gemini Enterprise asks the user to confirm each request before sending it.

The RxNorm Drug Vocabulary data store contains drug data, not patient data. Don't include patient information, such as patient names, dates of birth, or medical record numbers, in requests that use the RxNorm Drug Vocabulary data store.

## Limitations

The RxNorm Drug Vocabulary data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing RxNorm Drug Vocabulary data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The RxNorm Drug Vocabulary data store is supported only in the `global` and `us` locations.

  * **Search RxNorm drugs by name** accepts a drug name from 2 to 100 characters.

  * **Get RxNorm concept details** and **List NDCs for an RxNorm product** accept an RxCUI of 1 to 8 characters, for example, `1049221`.

  * **Map an NDC to RxNorm** accepts an NDC of 11 to 13 characters: the NDC as printed on the package, with hyphens, or the 11-digit form. A 10-digit NDC without hyphens isn't accepted.

  * If a value is shorter or longer than these limits, Gemini Enterprise doesn't send the request and asks the user to correct the value.

  * **List NDCs for an RxNorm product** returns no NDCs for ingredient, brand name, retired, or unknown RxCUIs. To list NDCs, use a drug product RxCUI.




## What's next

  * To create and configure a data store with RxNorm Drug Vocabulary, see [Set up a RxNorm Drug Vocabulary data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_rxnorm/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
