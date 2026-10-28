---
url: https://docs.cloud.google.com/model-armor/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:45:33.143383+00:00
---

# Troubleshoot  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Model Armor.

This section contains troubleshooting steps that you might find helpful if you have problems using Model Armor.

## All API calls to Model Armor return a 404 Not Found error

Establish a Private Service Connect to the Model Armor APIs. This error typically occurs when Model Armor regional endpoints (REPs) are accessed using Private Google Access or without a Private Service Connect. For more information, see [About accessing regional endpoints through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

## Sensitive Data Protection filter gives an error or is skipped

Verify the following:

  * The Sensitive Data Protection template is in the same region as the Model Armor endpoint being called.
  * The service agent making the Model Armor request has the `dlp.User` and `dlp.Reader` roles in the project containing the Sensitive Data Protection template.



This error occurs due to client errors in the `SanitizeUserPrompt` or `SanitizeModelResponse` requests or issues with the Sensitive Data Protection template.

## Model Armor global endpoint errors

Ensure that you're making the API requests to the appropriate regional endpoint instead of the global endpoint.

Model Armor supports the following operations only on its regional endpoints:

  * Create, read, update, delete, and list operations on templates.
  * `SanitizeUserPrompt` and `SanitizeModelResponse` API requests.



If you make the API requests for those operations to the global endpoint, you see the following error:
    
    
    {
      "error": {
        "code": 403,
        "message": "Write access to project '<PROJECT_ID>' was denied",
        "status": "PERMISSION_DENIED"
      }
    }
    

## Certificate errors when accessing Model Armor regional endpoints

This error typically occurs when Model Armor regional endpoints are accessed from within a VPC network using Private Google Access or VPC Service Controls, and the certificate verification fails.

For example, you might see an error message similar to the following:
    
    
    curl: (60) SSL: no alternative certificate subject name matches target host name 'modelarmor.europe-west4.rep.googleapis.com'
    

To resolve this issue, [create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) to the Model Armor APIs. For more information, see [About accessing regional endpoints through Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

## Region doesn't support the requested capabilities

You might see an error message similar to the following:
    
    
    Region '<var>REGION</var>' does not support the requested capabilities: '<var>CAPABILITIES</var>'
    

This error occurs when you attempt to create or update a template in a region with feature restrictions, and the request enables features that aren't supported in that region.

To resolve this issue:

  1. Identify the unsupported capabilities listed in the error message.
  2. Review the [feature availability by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region) to confirm which features aren't available for your target region.
  3. Remove the unsupported features from the template that you're creating or updating.



Alternatively, use a different Model Armor region that supports the features, if your data residency requirements allow.

## Template data residency compliance is required

You might see a `400` (`FAILED_PRECONDITION`) error message similar to the following:
    
    
    Template data residency compliance is required. The 'Enforce data residency' field must not be set to false.
    

This error occurs when the **Require Model Armor Template Data Residency Compliance** (`constraints/modelarmor.managed.requireTemplateDataResidencyCompliance`) managed Organization Policy Service constraint is enforced and you create or update a Model Armor template with data residency compliance disabled. Data residency compliance is disabled when you set `data_residency_compliant` to `false` or clear the **Enforce data residency** option. Because this constraint is enforced by default, editing any setting, such as a filter, on an existing template that already has `data_residency_compliant` set to `false` also triggers this error. Existing templates and requests to sanitize prompts and responses aren't affected unless you update the template.

To resolve this issue, do one of the following:

  * Enable data residency compliance on the template by setting `data_residency_compliant` to `true` or by selecting the **Enforce data residency** option.
  * If you need to keep data residency compliance disabled for the template, follow the steps in [Disable the organization policy constraint for data residency](https://docs.cloud.google.com/model-armor/manage-templates#disable-data-residency-constraint) to have your Organization Policy Administrator disable the constraint.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
