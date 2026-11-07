---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access/
title: Troubleshoot cross-cloud data access \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:29:19.305677+00:00
---

# Troubleshoot cross-cloud data access  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot cross-cloud data access Stay organized with collections  Save and categorize content based on your preferences. 

When you access cross-cloud data with Lakehouse, you can diagnose and resolve issues with background metadata refresh, private interconnect routing over Cross-Cloud Interconnect, and Service Directory endpoint resolution. Resolving these issues helps keep federated table metadata fresh and restores private cross-cloud query execution.

## Data and resources are stale or not updating

Lakehouse federated catalogs synchronize metadata from a remote cloud based on a refresh interval. A federated catalog's background metadata refresh can take longer when the federated catalog contains many resources (shares, schemas, namespaces, and tables). If a previous refresh overruns, the current refresh is skipped and the next refresh runs at the following scheduled interval.

If queried data appears stale, the federated catalog's background metadata refresh might be overrunning or failing. If you delete a resource in the remote cloud, it is removed from Lakehouse on the next completed background metadata refresh.

Check the background metadata refresh status on a federated catalog in the **Lakehouse** page in the Google Cloud console, or by using the Google Cloud CLI:

[Go to Lakehouse](https://console.cloud.google.com/biglake)
    
    
    gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID"
    
    gcloud biglake delta-sharing catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID"

## AWS Glue Data Catalog troubleshooting

If background metadata refresh fails after you configure `--metadata-service-directory-name` on an AWS Glue federated catalog in the Lakehouse runtime catalog, check the following:

  * **Verify private catalog endpoint mapping:** Confirm that the Hybrid Connectivity Network Endpoint Group (NEG) or Service Directory endpoint for background metadata refresh points to the private IP address of your AWS Glue Interface VPC Endpoint (`com.amazonaws.AWS_REGION.glue`) on TCP port `443`, rather than your Amazon S3 Interface VPC Endpoint.
  * **Verify IAM role trust policy and permissions:** Confirm that your Amazon Web Services (AWS) IAM role trust policy allows the federated catalog's Google Cloud service account (`biglake-service-account`) to assume the role (`sts:AssumeRoleWithWebIdentity`), and that the role has permissions to read your AWS Glue database and table metadata (`glue:GetDatabase`, `glue:GetDatabases`, `glue:GetTable`, `glue:GetTables`).
  * **Check VPC endpoint security group rules:** Confirm that the AWS Security Group attached to your AWS Glue Interface VPC Endpoint allows inbound HTTPS traffic on TCP port `443` from your Google Cloud Virtual Private Cloud (VPC) subnet and proxy-only subnet CIDR ranges.



## Databricks Unity Catalog troubleshooting

### Tables are empty or not discovered during background metadata refresh

If the federated catalog background metadata refresh indicates completion (such as `Refresh successfully completed`), but tables in the federated catalog don't appear or listing tables returns `0` items, check the following:

  * **`EXTERNAL USE SCHEMA` privilege:** Verify that the Databricks Service Principal has been granted the `EXTERNAL USE SCHEMA` privilege on the target schemas or catalog in Databricks Unity Catalog. Without this privilege, background metadata refresh and credential vending for queries fail.
  * **External data access setting:** Verify that **External data access** is enabled on the Databricks Unity Catalog metastore.
  * **External location:** Verify that your Databricks Unity Catalog and tables use an external storage location (such as Amazon S3, Microsoft Azure Data Lake Storage Gen2, or Cloud Storage) rather than default storage.



### Background metadata refresh fails over Cross-Cloud Interconnect

If background metadata refresh fails when `--metadata-service-directory-name` is configured for Databricks Unity Catalog in the Lakehouse runtime catalog, verify the following:

  * **Workspace private endpoint target:** Confirm that your metadata Service Directory endpoint or internal regional proxy Network Load Balancer backend targets the private IP address of your Databricks workspace AWS PrivateLink interface endpoint or Azure Private Endpoint on TCP port `443`, rather than your remote storage endpoint, and that `--unity-instance-name` matches your workspace hostname.
  * **Workspace private access settings:** If your Databricks workspace enforces private access settings or IP access lists, verify that requests arriving through your private endpoint from your Google Cloud VPC network are permitted.



### Background metadata refresh fails or returns 401 Unauthorized

If the background metadata refresh status reports an error (such as `401 Unauthorized`) or cannot discover schemas, verify the following:

  * **Service Principal federation policy:** In the Databricks Account Console (**Account settings > Security > Identity provider setup > Federation policies**), verify that the Service Principal federation policy is configured as follows: 
    * **Issuer URL:** `https://accounts.google.com`
    * **Subject:** The numeric Unique ID of the federated catalog's `biglake-service-account` service account (not its email address).
    * **Audience:** `https://accounts.cloud.databricks.com`
  * **Secret Manager permissions:** If using secret-based authentication, verify that the secret exists in the specified regional location and that the `biglake-service-account` has the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role granted.
  * **Service Principal permissions:** Ensure that the Databricks Service Principal has read access to the target workspace and Databricks Unity Catalog.



### Interactive query fails with 401 Unauthorized or token validation error

When user identity federation is enabled, interactive queries dynamically mint an end-user identity token and validate it against an Account-wide federation policy in Databricks. If queries fail with `401 Unauthorized` or token validation errors while background metadata refresh is healthy, check the following:

  * **Account-wide federation policy configured:** Ensure that an **Account-wide federation policy** (distinct from the Service Principal policy) is created in the Databricks Account Console under **Account settings > Security > Identity provider setup > Federation policies**.
  * **Case-sensitive audience matching:** Databricks validates the `aud` (audience) claim strictly case-sensitively. Verify that the **Audiences** field in the Databricks Account-wide federation policy matches the exact casing of the metastore-scoped `audience` claim (`databricks-METASTORE_ID`) retrieved from your federated catalog. Any uppercase or lowercase discrepancy (for example, in the `databricks-` prefix or metastore UUID) causes Databricks token validation to reject the query with `401 Unauthorized`.
  * **Issuer URL:** Verify that the **Issuer URL** matches the exact `issuer-url` claim from the federated catalog: `https://www.gstatic.com/biglake/federation/organizations/ORGANIZATION_ID`.
  * **Metastore audience availability:** The metastore-scoped `audience` claim is populated only after the first background metadata refresh cycle completes (typically within 5 minutes). If you configure the policy with a placeholder value or before the first refresh cycle completes, queries fail. Run `gcloud biglake iceberg catalogs describe` to verify that the `audience` claim on the federated catalog has been populated before configuring the policy.



## Snowflake Horizon Catalog troubleshooting

### Background metadata refresh fails with Code 16 (Unauthenticated)

If the background metadata refresh for a Snowflake Horizon Catalog fails with status `Code 16` (`UNAUTHENTICATED`), verify the following:

  * **Secret payload formatting:** Ensure that the secret token in Secret Manager contains the required JSON structure (`{"client_secret": "SNOWFLAKE_PAT_TOKEN", "scope": "session:role:SNOWFLAKE_ROLE"}`) rather than the raw programmatic access token (PAT) string.
  * **Token expiration and permissions:** Verify that the Snowflake PAT is valid and that the associated user and role have privileges to read the target catalog and databases.
  * **PrivateLink or Private Link account identifier:** If you configured `--metadata-service-directory-name` to synchronize metadata over Cross-Cloud Interconnect using AWS PrivateLink or Azure Private Link, verify that `--snowflake-account-identifier` specifies your Snowflake `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`) rather than your public account identifier.
  * **Network policy:** If background metadata refresh connects over the public internet and a Snowflake network policy is active, verify that Google's egress IP address ranges from [`goog.json`](https://www.gstatic.com/ipranges/goog.json) are included in your network policy's allowed IP list.



### Background metadata refresh fails over Cross-Cloud Interconnect

If background metadata refresh fails when `--metadata-service-directory-name` is configured for Snowflake Horizon Catalog in the Lakehouse runtime catalog, verify the following:

  * **Snowflake private endpoint target:** Confirm that your metadata Service Directory endpoint or internal regional proxy Network Load Balancer backend points to the private IP address of your Snowflake AWS PrivateLink interface endpoint or Azure Private Endpoint on TCP port `443`, rather than your remote object storage endpoint.
  * **Private account identifier:** Confirm that `--snowflake-account-identifier` uses your `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`).



## Connectivity or routing issues

If you encounter query transport or background metadata refresh failures when routing traffic over Cross-Cloud Interconnect, verify the following:

  * **Verify route propagation:** Check Cloud Router in Google Cloud to verify that it has learned your AWS VPC or Azure Virtual Network (VNet) prefixes. Check your AWS or Azure route tables to verify that they have routes back to your Google Cloud VPC network. If you use an internal regional proxy Network Load Balancer, verify that Cloud Router advertises your proxy-only subnet CIDR range through custom BGP route advertisements.
  * **Check internal load balancer health:** In the Google Cloud console, go to **Network Services > Load balancing**, and verify that the Hybrid Connectivity Network Endpoint Group (NEG) backends for your transport and metadata backend services are healthy. If a backend is unhealthy, check private interconnect connectivity and remote security rules.
  * **Test connectivity from Google Cloud:** Create a test VM instance in the same Google Cloud VPC network and subnet as the internal load balancer or Service Directory endpoint, and test connectivity to your AWS Elastic Network Interface (ENI) or Azure Private Endpoint network interface (NIC) IP addresses on TCP port `443` (for example, by using `curl` or `nc`).
  * **Verify Service Directory configuration and permissions:** Confirm that the Service Directory services configured in `--service-directory-name` (for query transport) and `--metadata-service-directory-name` (for background metadata refresh) are in the same Google Cloud region as your federated catalog. If a background metadata refresh for a federated catalog fails with a `Permission 'servicedirectory.services.resolve' denied` error, verify that the federated catalog's unique service account ID (`biglake-service-account` field) has the `roles/servicedirectory.viewer` and `roles/servicedirectory.pscAuthorizedService` roles on each project that hosts a Service Directory service.
  * **Check security groups and firewall rules:** Verify that Google Cloud firewall rules, AWS Security Groups, and Azure Network Security Groups (NSGs) allow TCP traffic on port `443` between your Google Cloud VPC CIDR ranges (including any proxy-only subnet CIDR range) and your remote private endpoints.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
