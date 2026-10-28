---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-snowflake/
title: Troubleshoot cross-cloud data access for Snowflake Horizon Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:38:46.377970+00:00
---

# Troubleshoot cross-cloud data access for Snowflake Horizon Catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-snowflake/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot cross-cloud data access for Snowflake Horizon Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

This page shows you how to troubleshoot background metadata refresh for cross-cloud data access with Snowflake Horizon Catalog. For general cross-cloud data access troubleshooting, such as connectivity and routing over private interconnects, see [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

## Refresh fails with Code 16 (Unauthenticated)

If the background metadata refresh for a Snowflake Horizon Catalog fails with status `Code 16` (`UNAUTHENTICATED`), verify the following:

  * **Secret payload formatting:** Ensure that the secret token in Secret Manager contains the required JSON structure (`{"client_secret": "<var>SNOWFLAKE_PAT_TOKEN</var>", "scope": "session:role:<var>SNOWFLAKE_ROLE</var>"}`) rather than the raw Personal Access Token (PAT) string.
  * **Token expiration and permissions:** Ensure the Snowflake PAT is valid and the associated user and role have sufficient privileges to access the target catalog and databases.
  * **Network policy:** If a Snowflake network policy is configured, ensure that Google's egress IP address ranges from [`goog.json`](https://www.gstatic.com/ipranges/goog.json) are allowlisted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
