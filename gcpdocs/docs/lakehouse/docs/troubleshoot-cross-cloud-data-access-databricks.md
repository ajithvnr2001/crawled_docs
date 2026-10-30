---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-databricks/
title: Troubleshoot cross-cloud data access for Databricks Unity Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:40:07.308471+00:00
---

# Troubleshoot cross-cloud data access for Databricks Unity Catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-databricks/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot cross-cloud data access for Databricks Unity Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, send an email to [biglake-help@google.com](mailto:biglake-help@google.com).

This page shows you how to troubleshoot background metadata refresh and user identity federation for cross-cloud data access with Databricks Unity Catalog. For general cross-cloud data access troubleshooting, such as connectivity and routing over private interconnects, see [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

## Tables are empty or not discovered during refresh

If the catalog background metadata refresh indicates success (such as `Refresh successfully completed`), but tables in the federated catalog do not appear or listing tables returns 0 items, check the following:

  * **`EXTERNAL USE SCHEMA` privilege:** Verify that the Databricks Service Principal has been granted the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog in Unity Catalog. Without this privilege, background metadata refresh and credential vending for queries will fail.
  * **External data access setting:** Verify that **External data access** is enabled on the Databricks Unity Catalog metastore.
  * **External location:** Verify that the Databricks Unity Catalog and tables use an external storage location (such as Cloud Storage or Amazon S3) rather than default storage.



## Metadata synchronization fails or returns 401 Unauthorized

If the background metadata refresh status reports an error (such as `401 Unauthorized`) or cannot discover schemas, verify the following:

  * **Service Principal federation policy:** In the Databricks Account Console (**Account settings > Security > Identity provider setup > Federation policies**), verify that the Service Principal federation policy is configured as follows: 
    * **Issuer URL:** `https://accounts.google.com`
    * **Subject:** The numeric Unique ID of the catalog's `biglake-service-account` service account (not its email address).
    * **Audience:** `https://accounts.cloud.databricks.com`
  * **Secret Manager permissions:** If using secret-based authentication, verify that the secret exists in the specified regional location and that the `biglake-service-account` has the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role granted.
  * **Service Principal permissions:** Ensure that the Databricks Service Principal has read access to the target workspace and catalog.



## Interactive query fails with 401 Unauthorized or token validation error

When user identity federation is enabled, interactive queries dynamically mint an end-user identity token and validate it against an Account-wide federation policy in Databricks. If queries fail with `401 Unauthorized` or token validation errors while background metadata synchronization is healthy, check the following:

  * **Account-wide federation policy configured:** Ensure that an **Account-wide federation policy** (distinct from the Service Principal policy) is created in the Databricks Account Console under **Account settings > Security > Identity provider setup > Federation policies**.
  * **Case-sensitive audience matching:** Databricks validates the `aud` (audience) claim strictly case-sensitively. Verify that the **Audiences** field in the Databricks Account-wide federation policy matches the exact casing of the metastore-scoped `audience` claim (`databricks-METASTORE_ID`) retrieved from your catalog. Any uppercase or lowercase discrepancy (for example, in the `databricks-` prefix or metastore UUID) causes Databricks token validation to reject the query with `401 Unauthorized`.
  * **Issuer URL:** Verify that the **Issuer URL** matches the exact `issuer-url` claim from the catalog: `https://www.gstatic.com/biglake/federation/organizations/ORGANIZATION_ID`.
  * **Metastore audience availability:** The metastore-scoped `audience` claim is populated only after the first background metadata refresh cycle completes (typically within 5 minutes). If you configure the policy with a placeholder value or before the first refresh cycle completes, queries fail. Run `gcloud biglake iceberg catalogs describe` to verify that the `audience` claim has been populated before configuring the policy.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
