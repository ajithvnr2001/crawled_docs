---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:48.841139+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

The Epic EHR data store for Gemini Enterprise lets clinicians ask questions about patients in your organization's Epic EHR using natural language. When a question needs Epic data, Gemini Enterprise calls Epic's FHIR R4 APIs as the signed-in user and answers from the data that Epic returns.

The connector is read-only. Gemini Enterprise reads data from Epic when a question needs it, and the data store doesn't index or copy Epic data. Each user authorizes the connector with their own Epic account through SMART on FHIR, and Epic applies that user's access rights.

## Supported actions

When the Epic EHR data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. All actions read Epic EHR data and are enabled by default.

Action | Description  
---|---  
Search Patients | Finds patients by MRN, Epic patient ID, or family name and birth date.  
Get Patient | Returns one patient's demographic record, including contact details.  
Search Observations | Returns a patient's lab results, vital signs, social history, and other observations.  
Search Conditions | Returns a patient's problem list, encounter diagnoses, medical history, and health concerns.  
Search Immunizations | Returns a patient's immunization history.  
Search Procedures | Returns a patient's completed procedures and surgical history.  
Search Medication Requests | Returns a patient's medication orders and prescriptions.  
Search Allergies | Returns a patient's drug, food, and environmental allergies, with criticality and reactions.  
Search Diagnostic Reports | Returns a patient's lab panels and pathology, cardiology, and radiology reports.  
Get Report Text | Returns the result text of a diagnostic report.  
Search Clinical Notes | Returns a patient's progress notes, discharge summaries, history and physical notes, consult notes, and operative reports.  
Get Note Text | Returns the full text of a clinical note.  
Search Encounters | Returns a patient's hospital admissions, emergency department visits, and outpatient visits.  
Search Service Requests | Returns a patient's orders, referrals, consults, and scheduled procedures.  
Search Coverage | Returns a patient's insurance policies, coverage status, and payer.  
Describe Epic Capabilities | Returns the resources and search parameters that your Epic FHIR server supports.  
  
Actions run with the permissions of the user who authorized the connector. A user can only read the records that they can already read in Epic.

## Required permissions

When a user authorizes the connector, Gemini Enterprise requests the following SMART on FHIR scopes:

Scope | Purpose  
---|---  
`openid` | Identifies the signed-in user.  
`fhirUser` | Identifies the FHIR resource that represents the signed-in user.  
`offline_access` | Lets Gemini Enterprise refresh access without asking the user to sign in again.  
`user/Patient.read` | Reads patient records.  
`user/Observation.read` | Reads lab results, vital signs, and other observations.  
`user/Condition.read` | Reads problems and diagnoses.  
`user/MedicationRequest.read` | Reads medication orders.  
`user/AllergyIntolerance.read` | Reads allergies.  
`user/Encounter.read` | Reads encounters.  
`user/ServiceRequest.read` | Reads orders and referrals.  
`user/Coverage.read` | Reads insurance coverage.  
`user/DiagnosticReport.read` | Reads diagnostic reports.  
`user/DocumentReference.read` | Reads clinical notes.  
`user/Binary.read` | Reads the text of notes and reports.  
  
For information about the Epic APIs that grant these scopes, see [Enable the Epic APIs](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration#enable-apis).

## Limitations

The Epic EHR data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Epic EHR data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Epic EHR data store is supported only in the `global` and `us` locations.
  * Patient searches need an MRN, an Epic patient ID, or a family name and birth date. Epic returns no results for a name alone or a birth date alone.
  * Each search is for one patient. The connector can't list or browse patients or answer questions across patients.
  * Each search returns at most 50 records per page, and Epic doesn't report a total count. Answers that depend on many records might be incomplete.
  * The connector can't read PDF documents. Note and report text longer than about 20,000 characters is truncated.
  * The connector doesn't read devices and implants, care plans, goals, scheduled appointments, care teams, family history, medication administration, consents, patient flags, or imaging studies.
  * Epic doesn't return records that it withholds from the signed-in user.



## What's next

  * To register the Epic app that the connector uses, see [Epic EHR configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration).

  * To create and configure a data store with Epic EHR, see [Set up an Epic EHR data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/set-up-data-store).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
