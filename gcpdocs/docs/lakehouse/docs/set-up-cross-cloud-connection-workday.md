---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday/
title: Set up cross-cloud connection for Workday Data Lake \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T08:33:52.033126+00:00
---

# Set up cross-cloud connection for Workday Data Lake  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud connection for Workday Data Lake Stay organized with collections  Save and categorize content based on your preferences. 

A cross-cloud connection to [Workday Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/workday-data-lake.html) lets you query your Workday data directly within Google Cloud. This capability unifies your data analytics by integrating your external data sources with your existing Google Cloud environment.

After you set up the connection, you can manage access to your federated data in _borderless Lakehouse_.

## Use cases

Connecting Lakehouse to Workday Data Lake supports several key use cases:

  * **Unify analytics:** Correlate Workday HR and compensation data with Google Cloud data, for example, to provide context for sales and quotas.
  * **Leverage Google Cloud ecosystem:** For example, use Google's agent framework with BigQuery ML and Workday HR data to predict employee retention.
  * **Stream real-time, no-copy data:** Analyze Workday procurement and accounts payable data alongside logistics and inventory data stored in Google Cloud to report supply chain inefficiencies and optimize vendor costs.



## Before you begin

  1. Review the [Lakehouse overview](https://docs.cloud.google.com/lakehouse/docs/introduction) to understand how Lakehouse manages access to data.
  2. Read [about accessing cross-cloud data](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) to understand how it works.
  3. Review the [supported catalogs](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#supported-catalogs) to verify compatibility.
  4. Understand how to use [regional Secret Manager secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs) to authenticate with Workday Data Lake.
  5. Check in with your Workday Data Lake administrators to set up authentication as described in this document. Administrators might need to contact Workday Support to enable Data Lake access, which can take time to resolve.

  6. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the BigLake, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,secretmanager.googleapis.com)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the BigLake, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com,secretmanager.googleapis.com)




### Required roles

To get the permissions that you need to set up cross-cloud access, ask your administrator to grant you the following IAM roles on your project: 

  * Manage Lakehouse catalogs: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * Manage secrets: [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** When using secret-based authentication, to follow the principle of least privilege and avoid granting access to all secrets in the project, have a Secret Manager administrator create the secret for you and grant you permissions to modify only that specific secret for Lakehouse.

### Limitations and considerations

This section lists the limitations and considerations for accessing cross-cloud data.

  * **VPC Service Controls:** If the project that contains your federated catalog endpoint or underlying Cloud Storage bucket is inside a VPC Service Controls service perimeter, then you must configure egress or ingress rules. For more information, see [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * **Read-only:** Federated catalogs in Lakehouse are read-only views of the remote catalog. Resource manipulation (such as creating, updating, or deleting resources) isn't supported and must be performed directly in the remote catalog.
  * **Data freshness:** The `--refresh-interval` flag for a federated catalog determines how often metadata is synchronized. The value must be `0s` (disabled) or at least `300s` (5 minutes). A catalog's background metadata refresh may take longer the more namespace and table resources there are. If the previous refresh overruns, the current refresh is skipped, and the next refresh is scheduled at the following interval. Queries use the most recently synchronized catalog metadata, so changes made in the remote catalog, such as new tables, schema updates, or newly committed data, aren't visible in Lakehouse until the next background metadata refresh completes. 
  * **Lakehouse caching:** Cross-cloud caching is disabled by default (`--cross-cloud-cache=disabled`). You can enable or disable caching at the federated catalog or connection level. Customer-managed encryption keys (CMEK) aren't supported for caching; cached files are encrypted using Google-owned and Google-managed encryption keys. If the `constraints/gcp.restrictNonCmekServices` organization policy constraint is enforced on a table in the query, caching is automatically disabled for that query. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching). 
  * **Data residency and compliance:** When you enable cross-cloud caching on a federated catalog or connection, Lakehouse temporarily stores cached files at rest in the Google Cloud region where the query runs. If your remote cloud files reside in a different jurisdiction, verify that cross-region caching meets your organization's data residency and compliance requirements before enabling it. 



## General workflow

To access cross-cloud data in Workday Data Lake, follow these general steps:

  1. **Set up federation:** Configure secret-based authentication and create a federated catalog in Lakehouse. 
     1. In Workday, set up the Data Lake and Workday API credentials.
     2. Create a secret in Secret Manager with your Workday API credentials.
     3. Create a federated catalog in Lakehouse and grant the catalog service account access to the secret.
  2. **Verify the connection:** Verify that Lakehouse can connect to your remote catalog and synchronize metadata.
  3. **Query data:** Run queries against your federated data using BigQuery or Managed Service for Apache Spark. You can optionally enable cross-cloud caching on the federated catalog to help reduce cross-cloud egress costs and accelerate subsequent queries. For more information, see [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  4. **Configure permissions:** Use Identity and Access Management (IAM) to manage who can view and query the federated data.



## Set up federation

To query your data, you must set up a Lakehouse federated catalog that connects to your remote Workday Data Lake.

### Configure authentication

Federation requires authenticating to the remote Workday Data Lake using credentials stored securely in regional [Secret Manager](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs) secrets.

  1. In Workday, complete the following:

     1. Set up the Data Lake.
     2. Register API Client for Data Lake (Refresh Token Grant).
     3. Set up security and table exports in the Data Lake.

For end-to-end instructions on completing this process, see [Get Started with Workday Data Lake](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-data-lake/workday-data-lake.html).

  2. Create a JSON file named `credentials.json` with the credentials from the previous step:
         
         {
           "client_id": "CLIENT_ID",
           "client_secret": "CLIENT_SECRET",
           "refresh_token": "REFRESH_TOKEN"
         }

Replace the following:

     * `CLIENT_ID`: The OAuth client ID from your Workday API Client for Integrations.
     * `CLIENT_SECRET`: The OAuth client secret from your Workday API Client for Integrations.
     * `REFRESH_TOKEN`: The non-expiring refresh token generated for your Workday ISU.
  3. Configure the regional endpoint for Secret Manager:

By default, Secret Manager uses a global endpoint. To avoid connectivity issues and minimize latency and data transfer costs, create your secret and catalog in the same region. To override the default global endpoint with a regional secret, run the following command:
         
         gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/

Replace the following:

     * `REGION`: The Google Cloud region where you store your Secret Manager secret. For example, `us-east4`.
  4. Upload the payload to Secret Manager:
         
         gcloud secrets create WORKDAY_SECRET_NAME \
           --location="REGION" \
           --project="PROJECT_ID" \
           --data-file=credentials.json

  5. Securely delete the `credentials.json` file to prevent credential leakage.

Replace the following:

     * `WORKDAY_SECRET_NAME`: A unique name for your Workday secret in Secret Manager, for example, `workday-api-credentials` or `workday-data-lake-secret`.
     * `REGION`: The Google Cloud region where you create the secret, for example, `us-east4`.
     * `PROJECT_ID`: Your Google Cloud project ID.



### Create a federated catalog

Create the federated catalog using the Google Cloud console or the `gcloud` CLI:

###  Console 

To create a federated catalog, follow these steps:

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click **Create catalog** , and then select **Federated catalog**.

The **Create Federated catalog** page appears.

  3. In the **Catalog configuration** section:

     1. In the **Federated catalog source** list, select **Workday (Data Lake)**.
     2. In the **Catalog name (in Lakehouse)** field, enter a name for the catalog.
     3. In the **Data location** list, select the region where you want to create the federated catalog, for example, `us-east4`. This must match the region of your Secret Manager secret. To minimize latency and data transfer costs, do the following when selecting a region: 
        * If your Workday instance is on Amazon Web Services (AWS), select the Google Cloud region closest to your AWS region.
        * If your Workday instance is on Google Cloud, select the exact same region.
     4. Optional: Under **Cross-cloud caching** , select **Enable cross-cloud caching** to cache remote files in the catalog's Google Cloud region and accelerate query performance. You can also update this setting later by editing the catalog details. For more information about how caching works, retention, and pricing, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).
     5. Click **Continue**.
  4. In the **Connection details** section:

     1. In the **Remote catalog details** section: 
        * In the **Workday Base URL** field, enter the base URL of your Workday instance. For example, `impl-services1.wd12.myworkday.com` or `wd501.myworkday.com`.
        * In the **Workday Tenant** field, enter your Workday tenant name, for example, `my_company_tenant`.
     2. In the **Authentication Method** section, in the **Secret Manager Secret** field, enter the resource name of your regional secret. Use the following format: `projects/PROJECT_ID/locations/REGION/secrets/WORKDAY_SECRET_NAME`.
     3. In the **Refresh interval** section, in the **Refresh interval** field, enter how often (in seconds) to update the catalog metadata (for example, `300`). To disable background metadata refresh, enter `0`.
  5. Click **Create**.




###  gcloud CLI 

To create a federated catalog using the `gcloud` CLI, run the following command:
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="workday" \
        --secret-name="projects/PROJECT_ID/locations/REGION/secrets/WORKDAY_SECRET_NAME" \
        --workday-base-url="WORKDAY_BASE_URL" \
        --workday-tenant="WORKDAY_TENANT" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: A name for your federated catalog in Lakehouse.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `REGION`: The Lakehouse region where you create the federated catalog, for example, `us-east4`. This region must be the same region where you stored your secret. To minimize latency and data transfer costs, do the following when selecting a region: 
    * If your Workday instance is on AWS, select the Google Cloud region closest to your AWS region.
    * If your Workday instance is on Google Cloud, select the exact same region.
  * `WORKDAY_SECRET_NAME`: The name of your Workday secret in Secret Manager.
  * `WORKDAY_BASE_URL`: The base URL of your Workday instance. For example, `impl-services1.wd12.myworkday.com` or `wd501.myworkday.com`.
  * `WORKDAY_TENANT`: The Workday tenant name.
  * `REFRESH_INTERVAL`: Optional: specifies how often to update the catalog's information. Set this value as a duration, for example, `300s` or `5m`. Shorter intervals update data more often but can cost more in API calls. Longer intervals can cost less, but the queried data might not reflect your most current dataset. If omitted, the refresh interval defaults to 5 minutes (`300s`). Setting the value to `0s` disables background metadata refresh.
  * `NAMESPACE_FILTERS`: Optional: a comma-separated list of namespaces to federate, for example, `finance,hr`. If omitted, Lakehouse includes all namespaces.
  * `CROSS_CLOUD_CACHE_MODE`: Optional: whether to enable cross-cloud caching on the federated catalog (`enabled` or `disabled`). Defaults to `disabled`. When set to `enabled`, Lakehouse caches remote files in the catalog's Google Cloud region. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).



### Complete authentication setup

After you create the catalog, Lakehouse provisions a unique service account for it, identified as `biglake-service-account` in the resource description.

You must grant this service account the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) on the secret that you created earlier. It might take a few minutes for new IAM policies to take effect.

###  Console 

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click the name of the federated catalog that you created for Workday.

  3. On the **Catalog details** page, in the alert banner, click **Grant secret permissions**.

Lakehouse grants the `roles/secretmanager.secretAccessor` role on the secret to the provisioned service account.




###  gcloud CLI 

  1. Grant the catalog's service account permission to access the secret:
         
         gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
         gcloud secrets add-iam-policy-binding WORKDAY_SECRET_NAME \
           --project="PROJECT_ID" \
           --location="REGION" \
           --member="serviceAccount:$(gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
               --project="PROJECT_ID" \
               --format='value(biglake-service-account)')" \
               --role="roles/secretmanager.secretAccessor"

  2. To verify that the federated catalog service account has access to the secret, run the following command:
         
         gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
         gcloud secrets get-iam-policy WORKDAY_SECRET_NAME \
              --project="PROJECT_ID" \
              --location="REGION"

In the output, verify that the `biglake-service-account` service account has the `roles/secretmanager.secretAccessor` role.




Replace the following:

  * `REGION`: The Google Cloud region where you store your Secret Manager secret and created the federated catalog, for example, `us-east4`.
  * `WORKDAY_SECRET_NAME`: The name of your Workday secret in Secret Manager.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `FEDERATED_CATALOG_NAME`: The name of your federated catalog in Lakehouse.



## Verify the connection

Verify that the background metadata refresh completed successfully and synchronized your namespaces and tables.

  1. Verify that the refresh status indicates success:
         
         gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID"

  2. Confirm that the namespaces are synchronized:
         
         gcloud biglake iceberg namespaces list \
           --project="PROJECT_ID" \
           --catalog="FEDERATED_CATALOG_NAME"




Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `FEDERATED_CATALOG_NAME`: The name of your federated catalog in Lakehouse.



## What's next

  * [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
