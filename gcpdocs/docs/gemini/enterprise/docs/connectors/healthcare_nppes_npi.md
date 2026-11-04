---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_nppes_npi/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:52.518006+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_nppes_npi/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The NPPES NPI Registry data store for Gemini Enterprise lets you look up and verify U.S. healthcare providers in the public CMS National Plan and Provider Enumeration System (NPPES) NPI Registry using natural language. End users can do the following without leaving Gemini Enterprise:

  * Look up an individual provider (NPI-1) or a healthcare organization (NPI-2) by its 10-digit National Provider Identifier (NPI), and get its name, credential, status, addresses, and specialties with state license numbers.
  * Search for clinicians and healthcare organizations, such as hospitals, clinics, and pharmacies, by name, specialty, city, state, or ZIP code.
  * Check whether an NPI is well formed before looking it up.



Because the NPPES NPI Registry is public, connecting the NPPES NPI Registry connector doesn't require a CMS account, credentials, or an OAuth application.

## Supported actions

When the NPPES NPI Registry data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. These actions only read data, and they're enabled by default.

Action | Description  
---|---  
Lookup NPI | Returns the full NPPES record for a 10-digit NPI, including the provider or organization name, credential, entity type (NPI-1 or NPI-2), status, practice and mailing addresses, and specialties with state license numbers.  
Batch lookup NPIs | Returns the NPPES records for up to 10 NPIs in a single request, in the same order as the requested NPIs.  
Search providers | Searches for individual providers (NPI-1) or healthcare organizations (NPI-2) by name, organization name, specialty, city, state, or ZIP code, and returns a summary of each matching provider.  
Validate NPI Luhn | Checks whether an NPI is well formed: exactly 10 digits, with a valid check digit. This action doesn't query the NPPES NPI Registry.  
**Note:** **Lookup NPI** , **Batch lookup NPIs** , and **Search providers** send the NPIs or search criteria from the user's request to the public CMS NPPES API. By default, Gemini Enterprise asks the user to confirm each of these requests before sending it. For **Batch lookup NPIs** , the user confirms the whole batch once. **Validate NPI Luhn** doesn't send data to CMS and runs without confirmation.

The NPPES NPI Registry contains provider data, not patient data. Don't include patient information, such as patient names, dates of birth, or medical record numbers, in requests that use the NPPES NPI Registry.

## Limitations

The NPPES NPI Registry data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing NPPES NPI Registry data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The NPPES NPI Registry data store is supported only in the `global` and `us` locations.

  * The NPPES NPI Registry covers only U.S. healthcare providers and organizations.

  * The NPPES NPI Registry is a self-reported enumeration registry. Its records don't confirm a provider's current licensure, board certification, or network participation.

  * The connector uses the public CMS NPPES API, which is shared with other callers and can throttle requests. When the API throttles requests, lookups can be temporarily unavailable.

  * **Batch lookup NPIs** accepts up to 10 NPIs per request.

  * **Search providers** has the following constraints:

    * It returns up to 200 records per request, and 10 by default.
    * A last name can't be the only search criterion. Combine it with a first name, city, state, ZIP code, or specialty.
    * A state or an entity type (NPI-1 or NPI-2) can't be the only search criterion.
    * First names are matched exactly, without nicknames. For example, a search for `Bob` doesn't find `Robert`. Use the formal name or a wildcard, such as `Rob*`.
    * Names and ZIP codes support a trailing wildcard (`*`) after at least two characters, for example, `Sm*` or `237*`.
    * Each result is a summary that contains the NPI, a link to the provider's public NPPES profile, the provider or organization name, one specialty, one city and state, and a telephone number with its area code and prefix masked. To get all of a provider's addresses and specialties, use **Lookup NPI**.
  * **Validate NPI Luhn** checks only the format and check digit of an NPI. A valid result doesn't mean that the NPI is assigned, is active, or belongs to a specific provider. To confirm those details, use **Lookup NPI**.




## What's next

  * To create and configure a data store with NPPES NPI Registry, see [Set up an NPPES NPI Registry data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/healthcare_nppes_npi/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
