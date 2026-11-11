---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration/
title: Epic EHR configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:55:18.790518+00:00
---

# Epic EHR configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/epic-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Epic EHR configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to register and configure an Epic app before you create the Epic EHR data store. Your organization registers its own Epic app. Your Epic analyst usually completes these steps.

## Register the Epic app

Register an app for Gemini Enterprise in [Epic on FHIR](https://fhir.epic.com), and make it available in your Epic environments. Use the following settings:

Setting | Value  
---|---  
Application Audience | Clinicians or Administrative Users  
Incoming APIs | The R4 APIs listed in Enable the Epic APIs  
Outgoing APIs | None  
Will this app register dynamic clients? | No  
Is Confidential Client | Yes  
Requires Persistent Access | Yes  
Uses Rolling Refresh Tokens | Yes  
JWK Set URL | Leave blank  
SMART on FHIR Version | R4  
SMART Scope Version | SMART v1  
FHIR ID Generation Scheme | Use 64-Character-Limited FHIR IDs for USCDI FHIR Resources  
  
Your organization's persistent access settings for the app determine how long a user's authorization lasts. When it ends, the user authorizes the connector again.

## Set the redirect URIs

In the app, register both of the following redirect URIs exactly as shown:

  * `https://vertexaisearch.cloud.google.com/oauth-redirect`
  * `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth.html`



## Enable the Epic APIs

In the app, enable the R4 read and search APIs for the following FHIR resources: Patient, Observation, Condition, MedicationRequest, AllergyIntolerance, DiagnosticReport, DocumentReference, Binary, Encounter, ServiceRequest, Coverage, Immunization, and Procedure.

Some resources, such as Observation and Condition, have a separate API for each category, for example labs and vital signs. Enable the categories that you want users to query. Don't enable write APIs.

If an API isn't enabled, only the actions that use it fail.

## Get the client ID and client secret

Epic issues a non-production client ID and a production client ID for the app. Use the client ID that matches the Epic environment that your URLs point to. Because the app is a confidential client, it also has a client secret. You enter the client ID and client secret when you [create the data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/set-up-data-store#create-data-store).

## Find your Epic endpoints

To create the data store, you need three URLs from your Epic environment: the FHIR R4 base URL, the authorize URL, and the token URL. Your Epic analyst can provide them. Your organization's SMART configuration, at `FHIR_BASE_URL/.well-known/smart-configuration`, also lists the authorize URL (`authorization_endpoint`) and the token URL (`token_endpoint`). Replace FHIR_BASE_URL with your FHIR R4 base URL.

Enter each URL with `https://` and without a trailing slash. For example, Epic's public sandbox uses the following URLs:

URL | Epic sandbox example  
---|---  
FHIR R4 base URL | `https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4`  
Authorize URL | `https://fhir.epic.com/interconnect-fhir-oauth/oauth2/authorize`  
Token URL | `https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token`  
  
## Troubleshoot

The following table lists common issues and how to resolve them:

Issue | Resolution  
---|---  
The console shows one of the following messages: 

  * "Epic FHIR R4 URL must be an https:// URL without a trailing slash."
  * "Epic Authorize URL must be an https:// URL without a trailing slash."
  * "Epic Token URL must be an https:// URL without a trailing slash."

| Enter the URL with `https://` and without a trailing slash.  
The console shows "Failed to obtain refresh token." | In the Epic app, select **Is Confidential Client** and **Requires Persistent Access** , and save the changes. Then, in the Google Cloud console, click **Verify Auth** again.  
Epic reports that the redirect URI doesn't match. | Register both redirect URIs exactly as shown in Set the redirect URIs.  
Epic shows "Invalid OAuth 2.0 request" during sign-in. | Each Epic sign-in link works only once, so reloading the sign-in window shows this error. Close the window, and start the sign-in again without reloading. If the error continues, check that the app has the APIs for the requested scopes.  
Epic returns `invalid_client`. | The client ID or client secret is wrong, has extra spaces, or belongs to the other Epic environment. Enter the client ID and client secret for the environment that your URLs point to.  
The sign-in window doesn't return to Gemini Enterprise, or the connector isn't authorized after sign-in. | Close the sign-in window, reload Gemini Enterprise, and authorize the connector again.  
One action fails, and other actions work. | The Epic API for that action isn't enabled. Enable it in the app, and then have the user authorize the connector again.  
Gemini Enterprise says "I'm sorry, it seems you are not allowed to perform this operation. Please contact an administrator." to a user who authorized the connector before. | The user's Epic authorization has ended. The user authorizes the connector again.  
Gemini Enterprise doesn't find a patient by name. | Add the birth date, or use the MRN or Epic patient ID.  
Gemini Enterprise says that some records couldn't be retrieved. | Epic security withholds these records from the user. Users see only the records that Epic allows them to see.  
The text of a report or note isn't available. | The document is a PDF or another format that the connector can't read. Open the document in Epic.  
Authorization keeps failing in one app only. | Remove the Epic EHR data store from the app, add it back, and authorize the connector again.  
  
## What's next

  * To create and configure a data store with Epic EHR, see [Set up an Epic EHR data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/epic/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
