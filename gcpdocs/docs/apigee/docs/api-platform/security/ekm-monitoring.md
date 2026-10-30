---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/ekm-monitoring/
title: EKM health monitoring \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:41:02.143532+00:00
---

# EKM health monitoring  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/ekm-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  EKM health monitoring Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes how to monitor the health of your Cloud External Key Manager (Cloud EKM) used with Apigee and how to configure alerts for Cloud EKM-related issues using Cloud Logging.

Apigee may rely on Cloud EKM for CMEK. If the Cloud EKM becomes unavailable due to network issues, or if keys are disabled or unreachable, Apigee services that rely on encryption may be impacted.

**Note:** The EKM monitoring feature is available only for Apigee organizations that were configured to use CMEK with EKM when the organization was created. It is not possible to enable this feature for existing organizations. 

## Monitoring Cloud EKM issues in Cloud Logging

When Apigee encounters an issue with a Cloud EKM, such as a state change to denied, key disabled, billing disabled, or key unreachable, it generates a log entry in [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). You can view these logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) and configure log-based alerts to be notified of such events.

The log entry contains details about the organization and instance experiencing the issue, but omits the key name for security reasons.

To find Cloud EKM-related log entries in Logs Explorer, follow these steps:

  1. Go to the **Logs Explorer** page in the Google Cloud console. 

[ Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following query in the query editor field and click **Run query** : 
         
         Apigee EKM key health issue detected

  3. If Cloud EKM issues have occurred, the query results will show log entries detailing the event.

![Click to enlarge](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ekm-error-log.png)![EKM error log entry](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ekm-error-log.png)

## Configure log-based alerts for Cloud EKM issues

You can create a log-based alert policy to notify you when Apigee logs an Cloud EKM-related error. These alerts can help you proactively identify and address issues with your Cloud EKM.

To configure a log-based alert based on the Cloud EKM error message string, see [ Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in the Cloud Logging documentation.

When creating the alert, use the same query filter as described in  Monitoring Cloud EKM issues in Cloud Logging to match the specific Cloud EKM log entries.

## Alerting limitations and recovery

Be aware of the following limitations when you configure and respond to Cloud EKM health alerts:

  * **Recurring alerts:** While a key remains unreachable, Apigee generates a log entry approximately once every hour. If you configure a log-based alert, you receive a notification at this cadence until the underlying issue is resolved.
  * **No recovery notification:** Apigee does not generate a log entry or send a notification when the Cloud EKM becomes reachable again. A log-based alert resolves on its own after Apigee stops generating the error log entries, based on the auto-close configuration of your alerting policy.
  * **Verifying recovery:** Because no recovery log entry is generated, confirm that your Cloud EKM is reachable again by performing an operation that requires the key, such as deploying an API proxy, and verifying that it succeeds.



## Troubleshooting limitations

Apigee logging indicates when there is an issue with the Cloud EKM connection or key status. However, detailed troubleshooting of the Cloud EKM itself (e.g., diagnosing network connectivity issues or problems on the external key manager's side) is outside the scope of Apigee monitoring. If you receive alerts about Cloud EKM issues, you should investigate the health and configuration of your Cloud EKM service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
