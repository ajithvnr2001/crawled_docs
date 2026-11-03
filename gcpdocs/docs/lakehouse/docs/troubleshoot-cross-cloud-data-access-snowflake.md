---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access-snowflake/
title: Troubleshoot cross-cloud data access for Snowflake Horizon Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:33:52.493423+00:00
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

When you connect Lakehouse to Snowflake Horizon Catalog, you can diagnose and resolve authentication, private account identifier, and background metadata refresh errors so your external Apache Iceberg tables stay synchronized. For general network routing and Service Directory checks over Cross-Cloud Interconnect, see [Connectivity or routing issues](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access#connectivity-routing-issues).

## Background metadata refresh fails with Code 16 (Unauthenticated)

If the background metadata refresh for a Snowflake Horizon Catalog fails with status `Code 16` (`UNAUTHENTICATED`), verify the following:

  * **Secret payload formatting:** Ensure that the secret token in Secret Manager contains the required JSON structure (`{"client_secret": "SNOWFLAKE_PAT_TOKEN", "scope": "session:role:SNOWFLAKE_ROLE"}`) rather than the raw programmatic access token (PAT) string.
  * **Token expiration and permissions:** Verify that the Snowflake PAT is valid and that the associated user and role have privileges to read the target catalog and databases.
  * **PrivateLink or Private Link account identifier:** If you configured `--metadata-service-directory-name` to synchronize metadata over Cross-Cloud Interconnect using Amazon Web Services (AWS) PrivateLink or Microsoft Azure Private Link, verify that `--snowflake-account-identifier` specifies your Snowflake `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`) rather than your public account identifier.
  * **Network policy:** If background metadata refresh connects over the public internet and a Snowflake network policy is active, verify that Google's egress IP address ranges from [`goog.json`](https://www.gstatic.com/ipranges/goog.json) are included in your network policy's allowed IP list.



## Background metadata refresh fails over Cross-Cloud Interconnect

If background metadata refresh fails when `--metadata-service-directory-name` is configured for Snowflake Horizon Catalog in the Lakehouse runtime catalog, verify the following:

  * **Snowflake private endpoint target:** Confirm that your metadata Service Directory endpoint or internal regional proxy Network Load Balancer backend points to the private IP address of your Snowflake AWS PrivateLink interface endpoint or Azure Private Endpoint on TCP port `443`, rather than your remote object storage endpoint.
  * **Private account identifier:** Confirm that `--snowflake-account-identifier` uses your `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
