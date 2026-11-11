---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_cms_coverage/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:43.699390+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_cms_coverage/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The CMS Coverage data store for Gemini Enterprise lets you use natural language to look up Medicare coverage policies in the public Medicare Coverage Database of the Centers for Medicare & Medicaid Services (CMS). End users can do the following without leaving Gemini Enterprise:

  * Search National Coverage Determinations (NCDs) and Local Coverage Determinations (LCDs) by service, item, procedure, or condition.
  * Limit LCDs to the ones that apply in a US state or territory.
  * Read the coverage criteria of an NCD or LCD, such as covered indications and limitations.



Because the Medicare Coverage Database is public, connecting the CMS Coverage connector doesn't require a CMS account, credentials, or an OAuth application.

## Supported actions

When the CMS Coverage data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. These actions only read data, and they're enabled by default.

Action | Description  
---|---  
Search coverage policies | Searches NCD and LCD titles for a service, item, procedure, or condition. Returns the ID, title, and Medicare Coverage Database link of each matching policy, and the contractors and effective date of each matching LCD. If the user names a US state or territory, returns only the LCDs that apply there. NCDs apply nationwide and aren't filtered by state.  
Get NCD details | Looks up an NCD by its NCD number, such as `40.2`, and returns the current version, including its benefit category, effective date, and coverage text, such as the indications and limitations of coverage.  
Get LCD details | Looks up an LCD by its LCD ID, such as `L33822`, and returns the version that's in effect, including its contractors, status, dates, and coverage text, such as the indications and limitations of coverage and the documentation requirements.  
**Note:** By default, Gemini Enterprise asks the user to confirm each **Search coverage policies** request before the connector sends it to the public CMS Coverage API. **Get NCD details** and **Get LCD details** send only the ID of the requested policy to CMS, and they run without confirmation.

The CMS Coverage connector returns Medicare coverage policies, not patient data. Don't include patient information, such as patient names, dates of birth, Medicare beneficiary identifiers, or medical record numbers, in requests that use the CMS Coverage connector.

## Limitations

The CMS Coverage data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing CMS Coverage data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The CMS Coverage data store is supported only in the `global` and `us` locations.

  * The CMS Coverage connector covers only Medicare NCDs and LCDs. It doesn't return billing and coding articles, whose IDs start with `A`. These articles usually contain the CPT, HCPCS, and ICD-10 code lists for an LCD.

  * NCDs and LCDs describe the conditions under which Medicare covers an item or service. The connector doesn't check a patient's eligibility or decide whether Medicare covers a specific claim.

  * The connector uses the public CMS Coverage API, which is shared with other callers and can throttle requests. When the API throttles requests, lookups can be temporarily unavailable.

  * **Search coverage policies** matches words in policy titles. It doesn't search the policy text or billing codes. To find the policies for a CPT, HCPCS, or ICD-10 code, ask about the service or condition that the code describes.

  * **Search coverage policies** has the following constraints:

    * A policy matches when its title contains every search word, in any order. Only the first 3 search words are used.
    * A policy also matches when its title contains any one of up to 4 alternative terms, such as synonyms or abbreviations.
    * Results can include unrelated policies whose titles contain the same words.
    * Each LCD is listed once, as the version that's in effect. Retired LCDs, and LCDs and revisions that take effect later, aren't listed.
    * Retired NCDs are listed. Their titles end with `- RETIRED` or `(RETIRED)`.
  * **Get LCD details** returns the version of an LCD that's in effect. If CMS has published a revision that takes effect later, the result includes the date when the revision takes effect. For an LCD that has no version in effect yet, the action returns the version that takes effect next. If the LCD is retired, the result includes its retirement date.




## What's next

  * To create and configure a data store with CMS Coverage, see [Set up a CMS Coverage data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_cms_coverage/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
