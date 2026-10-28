---
url: https://docs.cloud.google.com/healthcare-api/docs/reference-patterns/
title: Reference patterns \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:28:42.966198+00:00
---

# Reference patterns  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Reference patterns Stay organized with collections  Save and categorize content based on your preferences. 

This page provides links to sample code and technical reference guides for common Cloud Healthcare API use cases. Use these resources to learn, identify best practices, and leverage sample code to build the features that you need.

**Note:** If you have implemented a reference pattern, we want to hear from you. Complete this [short survey](https://www.techvalidate.com/registration/google-reference-patterns-customer-survey) to let us know about your experience.

The reference patterns listed here are code-oriented and meant to get you quickly to implementation. To see a broader range of Cloud Healthcare API solutions, review the list of [Cloud Healthcare API technical reference guides](https://docs.cloud.google.com/docs/tutorials?q=Healthcare).

## Interoperability

**Note:** The provided Whistle [sample code](https://github.com/GoogleCloudPlatform/healthcare-data-harmonization/tree/master/wstl1/mapping_configs/hl7v2_fhir_r4) uses use Whistle 1, an unsupported legacy version. Whistle 2 sample code will be provided when available. Solution | Description | Links  
---|---|---  
**Convert HL7v2 messages to FHIR resources** | Learn how to ingest an HL7v2 message from an electronic health record (EHR) and transform it to a FHIR resource using the Cloud Healthcare API, Dataflow, and Whistle. |  Blog post: [Advancing healthcare with the Healthcare Interoperability Readiness Program](https://cloud.google.com/blog/topics/healthcare-life-sciences/google-cloud-healthcare-interoperability-readiness-program) Sample code: [Healthcare data harmonization HL7v2 to FHIR configurations](https://github.com/GoogleCloudPlatform/healthcare-data-harmonization/tree/master/wstl1/mapping_configs/hl7v2_fhir_r4) Sample data: [Simulated Hospital](https://github.com/google/simhospital#simulated-hospital)  
**Convert FHIR resources to OMOP** | Learn how to convert a FHIR resource to the Observational Medical Outcomes Partnership (OMOP) data model using the Cloud Healthcare API, Whistle, and BigQuery. |  Blog post: [Powering open source healthcare research on Google Cloud](https://cloud.google.com/blog/topics/healthcare-life-sciences/powering-open-source-healthcare-research-on-google-cloud) Sample code: [FHIR to OMOP CDM: mapping guide](https://github.com/GoogleCloudPlatform/healthcare-data-harmonization/tree/master/wstl1/mapping_configs/fhir_omop#fhir-to-omop-cdm-mapping-guide) Public dataset: [Synthetic patient data in OMOP](https://console.cloud.google.com/marketplace/product/hhs/synpuf)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
