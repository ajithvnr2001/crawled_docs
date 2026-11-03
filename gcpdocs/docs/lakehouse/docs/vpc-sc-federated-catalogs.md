---
url: https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs/
title: Use VPC Service Controls with federated catalog endpoints \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:44:06.805974+00:00
---

# Use VPC Service Controls with federated catalog endpoints  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use VPC Service Controls with federated catalog endpoints Stay organized with collections  Save and categorize content based on your preferences. 

In the Lakehouse runtime catalog, [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter rules for federated catalog endpoints let you query external Apache Iceberg tables in BigQuery while helping prevent data exfiltration. When your Google Cloud projects or Cloud Storage buckets reside inside a service perimeter, you can configure egress rules for Amazon S3 and Microsoft Azure Data Lake Storage (ADLS) Gen2 or ingress rules for Cloud Storage. These rules authorize background metadata refresh and queries for tables registered in AWS Glue Data Catalog, Databricks Unity Catalog, Snowflake Horizon Catalog, and Workday Data Lake.

If your projects aren't inside a service perimeter, then federated catalog endpoints work without any VPC Service Controls configuration. For cross-cloud connections to SAP Business Data Cloud (SAP BDC), see [VPC Service Controls configuration for SAP BDC](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-config-sap-bdc). To protect buckets accessed through the Apache Iceberg REST catalog endpoint in credential vending mode, see [Use VPC Service Controls with credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending#vpc-sc).

## Before you begin

  1. Set up a federated catalog endpoint for [AWS Glue Data Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue), [Databricks Unity Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-databricks), [Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake), or [Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday).
  2. [Create one or more service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) for your projects, depending on where your table files are stored:

     * **External cloud storage (Amazon S3 or ADLS Gen2)** : protect your federated catalog endpoint project with a perimeter that restricts `biglake.googleapis.com` and `bigquery.googleapis.com`. For the required egress rule, see Add an egress rule for external cloud storage.
     * **Cloud Storage** : protect your Cloud Storage bucket project with a perimeter that restricts `storage.googleapis.com`. The bucket project and the federated catalog endpoint project can either share a single perimeter or reside in separate perimeters. For the required ingress rule, see Add an ingress rule for Cloud Storage buckets in a service perimeter.
  3. If users or service accounts outside the perimeter query the federated catalog endpoint, then add an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that admits them to the catalog endpoint project's perimeter.




### Required roles

To get the permissions that you need to configure service perimeters, ask your administrator to grant you the following IAM roles on your organization: 

  * Configure service perimeters and ingress or egress policies: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use cases and required perimeter rules

The perimeter rules that you configure depend on where your table files reside and where your query callers run:

Use case | Required perimeter rule | Configuration steps  
---|---|---  
**Query cross-cloud tables in Amazon S3 or ADLS Gen2** : query Apache Iceberg tables in `s3://` buckets or `abfss://` containers through a federated catalog endpoint in a protected BigQuery project while blocking unauthorized external egress. | Add an **egress rule** on the catalog endpoint project's perimeter that allows both the catalog endpoint's `blirc-...` service account and your query principals to read the approved external buckets or containers. | Find the catalog endpoint's service account, and then add an egress rule for external cloud storage.  
**Access external catalog tables in protected Cloud Storage buckets** : query Databricks Unity Catalog or Snowflake Horizon Catalog tables stored in a `gs://` bucket inside a perimeter that restricts `storage.googleapis.com` (even in the same project and perimeter as the federated catalog endpoint). | Add an **ingress rule** on the Cloud Storage bucket project's perimeter that allows the remote catalog's Google Cloud service account to access `storage.googleapis.com`. | Add an ingress rule for Cloud Storage buckets in a service perimeter.  
**Allow queries from callers outside the catalog endpoint perimeter** : run BigQuery jobs in the catalog endpoint project from analyst accounts, BI tools, or workload service accounts located outside the perimeter. | Add an **ingress rule** on the catalog endpoint project's perimeter that admits the external callers to `bigquery.googleapis.com` and `biglake.googleapis.com`, in addition to the storage rule for your table location. | Configure caller ingress using the [ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference), and then follow the storage procedure for your table location.  
  
## How VPC Service Controls evaluates federated catalog endpoint traffic

A federated catalog endpoint performs two distinct operations that read from your underlying storage: background metadata refresh and BigQuery queries. How VPC Service Controls evaluates these operations depends on where your table files are stored:

  * **External cloud storage (Amazon S3 or Azure Data Lake Storage Gen2)** : VPC Service Controls evaluates egress from the catalog endpoint project's service perimeter against the caller identity on Google Cloud and the target external bucket or container:

Operation | Identity evaluated | Resource evaluated  
---|---|---  
**Background metadata refresh** | The catalog endpoint's auto-provisioned Lakehouse service account (`blirc-PROJECT_NUMBER-ID@gcp-sa-biglakerestcatalog.iam.gserviceaccount.com`) | The external bucket or container that holds the table's Apache Iceberg metadata  
**Query** | The user or service account that runs the BigQuery job | The external buckets or containers that hold the table's metadata and data files  
  
For tables stored in Amazon S3 or ADLS Gen2, your perimeter's egress rule must include all of the following:

    * **Identities** : both the catalog endpoint's service account and your query principals.
    * **External resources** : every bucket or container that your tables use for metadata and data files.
    * **Operations** : both `bigquery.googleapis.com` (with the `externalResource.read` permission) and `biglake.googleapis.com` (with all methods, `'*'`).
  * **Cloud Storage (Databricks Unity Catalog or Snowflake Horizon Catalog external locations on Google Cloud)** : during both background metadata refresh and BigQuery queries, BigQuery and Lakehouse read from Cloud Storage using the downscoped credentials vended by the remote catalog rather than the catalog endpoint's `blirc-...` service account. When the Cloud Storage bucket project is inside a service perimeter that restricts `storage.googleapis.com`, `storage.googleapis.com` evaluates the remote catalog's Google Cloud service account as an external identity attempting perimeter ingress. This evaluation applies even when the bucket is in the same project and service perimeter as the federated catalog endpoint. You must add an ingress rule to the bucket project's service perimeter that allows the remote catalog's Google Cloud service account to access `storage.googleapis.com`.




VPC Service Controls only evaluates storage reads performed by BigQuery and Lakehouse (`biglake.googleapis.com`). It doesn't evaluate calls that Lakehouse makes to the remote catalog's API endpoint (such as listing namespaces and tables), and it doesn't govern external query engines that read your storage directly.

### External resource formats

Specify external resources in egress rules as an exact bucket or container URI. Object paths and wildcards aren't supported. Bucket, container, and storage account names must be lowercase; rules that contain uppercase characters in these names are rejected when you save the rule. Azure Data Lake Storage Gen2 (`abfss://`) and Azure Blob Storage (`azure://`) URIs aren't interchangeable in VPC Service Controls egress rules; for federated catalog endpoints, you must specify the `abfss://` format.

The following table shows the supported external resource URI formats for federated catalog endpoints:

Storage service | Format | Example  
---|---|---  
Amazon S3 | `s3://BUCKET_NAME` | `s3://my-iceberg-warehouse`  
Azure Data Lake Storage Gen2 | `abfss://CONTAINER@STORAGE_ACCOUNT.dfs.core.windows.net` | `abfss://unity-catalog-storage@mystorageaccount.dfs.core.windows.net`  
  
## Find the catalog endpoint's service account

Lakehouse provisions a dedicated service account for each federated catalog endpoint when you create the catalog endpoint. For tables in Cloud Storage, skip to Add an ingress rule for Cloud Storage buckets in a service perimeter. If your tables are stored in Amazon S3 or ADLS Gen2, then retrieve this service account email address for your egress rule:
    
    
    gcloud biglake iceberg catalogs describe CATALOG_ID \
        --project=PROJECT_ID \
        --format='value(biglake-service-account)'
    

Replace the following:

  * `CATALOG_ID`: the ID of your federated catalog endpoint.
  * `PROJECT_ID`: the ID of the Google Cloud project that contains the federated catalog endpoint.



The command returns an email address in the following format:
    
    
    blirc-PROJECT_NUMBER-ID@gcp-sa-biglakerestcatalog.iam.gserviceaccount.com
    

## Add an egress rule for external cloud storage

If tables accessed through your federated catalog endpoint are stored in Amazon S3 or ADLS Gen2, then add an egress rule to the service perimeter that protects your catalog endpoint project.

###  Console 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your organization and access policy, and then click the name of the service perimeter that contains your catalog endpoint project.

  3. Click **Edit** , and then in the **Egress policy** section, click **Add an egress rule**.

  4. In the **From** section, under **Identities** , select **Select identities & groups**, click **Add identities** , and add the catalog endpoint's service account and the users or service accounts that run queries.

  5. In the **To** section:

     1. Select **External resources** , click **Add resources** , enter each `s3://` bucket or `abfss://` container that your tables use, and click **Add external resources**.
     2. Under **Operations or IAM roles** , configure the following services in the **API operations** table: 
        * **BigQuery API** (`bigquery.googleapis.com`): to restrict the default all-methods (`*`) entry to read-only access, open the action menu for `bigquery.googleapis.com` and click **Edit** , select **Select methods** , select the `externalResource.read` permission, and click **Add selected methods**.
        * **BigLake API** (`biglake.googleapis.com`): click **Add operations** , select **BigLake API** (`biglake.googleapis.com`), select **All methods** , and click **Add all methods**.
  6. Click **Save**.




###  gcloud CLI 

  1. Create a file named `egress.yaml` that specifies the catalog endpoint's service account, the query principals, and every external bucket or container that your tables use. For the full schema, see the [egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).
         
         - egressFrom:
             identities:
             - serviceAccount:CATALOG_ENDPOINT_SERVICE_ACCOUNT
             - user:QUERY_USER_EMAIL
           egressTo:
             externalResources:
             - s3://S3_BUCKET_NAME
             - abfss://ADLS_CONTAINER@STORAGE_ACCOUNT.dfs.core.windows.net
             operations:
             - serviceName: bigquery.googleapis.com
               methodSelectors:
               - permission: externalResource.read
             - serviceName: biglake.googleapis.com
               methodSelectors:
               - method: '*'
         

Replace the following:

     * `CATALOG_ENDPOINT_SERVICE_ACCOUNT`: the catalog endpoint's service account email address that you retrieved earlier.
     * `QUERY_USER_EMAIL`: the email address of a user or service account that runs queries through the federated catalog endpoint. For a service account, use the `serviceAccount:` prefix instead of `user:`. Alternatively, replace `identities` with `identityType: ANY_IDENTITY` to allow any principal in the perimeter.
     * `S3_BUCKET_NAME`, `ADLS_CONTAINER`, and `STORAGE_ACCOUNT`: the external storage locations that hold your table metadata and data files. Include only the entries that apply to your storage provider.
  2. Find the numeric ID of your organization's access policy:
         
         gcloud access-context-manager policies list \
             --organization=ORGANIZATION_ID \
             --format='value(name)'
         

Replace `ORGANIZATION_ID` with your numeric organization ID.

  3. Apply the egress rule to your service perimeter:

**Caution:** The `--set-egress-policies` flag replaces all existing egress rules on the perimeter. If your perimeter already has egress rules, then export them first and append the new rule to the file before updating the perimeter.
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --policy=POLICY_ID \
             --set-egress-policies=egress.yaml
         

Replace the following:

     * `PERIMETER_NAME`: the name of your service perimeter.
     * `POLICY_ID`: the numeric ID of your access policy.

To test the rule before enforcing it, apply it to a dry-run configuration using `gcloud access-context-manager perimeters dry-run update` and enforce it after validation using `gcloud access-context-manager perimeters dry-run enforce`.

  4. Verify that the rule is active:
         
         gcloud access-context-manager perimeters describe PERIMETER_NAME \
             --policy=POLICY_ID \
             --format='yaml(status.egressPolicies)'
         




## Add an ingress rule for Cloud Storage buckets in a service perimeter

If tables in a remote catalog (such as Databricks Unity Catalog or Snowflake Horizon Catalog) are stored in a Cloud Storage bucket protected by a perimeter that restricts `storage.googleapis.com`, then add an ingress rule to the bucket project's service perimeter. Because BigQuery and Lakehouse authenticate to Cloud Storage using the remote catalog's Google Cloud service account (not the `blirc-...` service account), this rule is required even when the bucket is in the same project and perimeter as the federated catalog endpoint.

###  Console 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your organization and access policy, and then click the name of the service perimeter that protects the project that contains your Cloud Storage bucket.

  3. Click **Edit** , and then in the **Ingress policy** section, click **Add an ingress rule**.

  4. In the **From** section:

     1. Under **Identities** , select **Select identities & groups**, click **Add identities** , and add the Google Cloud service account provisioned by the remote catalog for your Cloud Storage bucket.
     2. Under **Sources** , select **All sources** (or select **Select sources** to specify an access level).
  5. In the **To** section:

     1. Under **Resources** , select **Select resources**. On the **Projects** tab, click **Add projects** , select the project that contains your Cloud Storage bucket, and click **Add selected projects**.
     2. Under **Operations or IAM roles** , select **Select operations** , click **Add operations** , select **Cloud Storage API** (`storage.googleapis.com`), select **All methods** , and click **Add all methods**. Alternatively, select **Select methods** to choose specific [supported service methods](https://docs.cloud.google.com/vpc-service-controls/docs/supported-method-restrictions) (such as `google.storage.objects.get`, `google.storage.objects.list`, and `google.storage.buckets.get`), and click **Add selected methods**.
  6. Click **Save**.




###  gcloud CLI 

  1. Create a file named `ingress.yaml` that allows the remote catalog's Google Cloud service account to access `storage.googleapis.com` in the bucket's project. For the full schema, see the [ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).
         
         - ingressFrom:
             identities:
             - serviceAccount:REMOTE_CATALOG_GCS_SERVICE_ACCOUNT
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: storage.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - projects/BUCKET_PROJECT_NUMBER
         

Replace the following:

     * `REMOTE_CATALOG_GCS_SERVICE_ACCOUNT`: the Google Cloud service account email address provisioned by the remote catalog to access your Cloud Storage bucket (for example, from `DESCRIBE STORAGE CREDENTIAL` in Databricks Unity Catalog or `DESC EXTERNAL VOLUME` in Snowflake Horizon Catalog).
     * `BUCKET_PROJECT_NUMBER`: the numeric project number of the project that contains the Cloud Storage bucket.
  2. Find the numeric ID of your organization's access policy:
         
         gcloud access-context-manager policies list \
             --organization=ORGANIZATION_ID \
             --format='value(name)'
         

Replace `ORGANIZATION_ID` with your numeric organization ID.

  3. Apply the ingress rule to the service perimeter that protects the bucket project:

**Caution:** The `--set-ingress-policies` flag replaces all existing ingress rules on the perimeter. If your perimeter already has ingress rules, then export them first and append the new rule to the file before updating the perimeter.
         
         gcloud access-context-manager perimeters update BUCKET_PERIMETER_NAME \
             --policy=POLICY_ID \
             --set-ingress-policies=ingress.yaml
         

Replace the following:

     * `BUCKET_PERIMETER_NAME`: the name of the service perimeter that protects the bucket project.
     * `POLICY_ID`: the numeric ID of your access policy.

To test the rule before enforcing it, apply it to a dry-run configuration using `gcloud access-context-manager perimeters dry-run update` and enforce it after validation using `gcloud access-context-manager perimeters dry-run enforce`.

  4. Verify that the rule is active:
         
         gcloud access-context-manager perimeters describe BUCKET_PERIMETER_NAME \
             --policy=POLICY_ID \
             --format='yaml(status.ingressPolicies)'
         




## Verify the configuration

Service perimeter policy updates can take up to 30 minutes to propagate. After your rule takes effect, verify that background metadata refresh and BigQuery queries complete without VPC Service Controls denials:

  1. Wait for the next scheduled background metadata refresh cycle to finish, and then check [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied) in Cloud Audit Logs to confirm that no VPC Service Controls violations occur. Background metadata refresh runs automatically on its refresh schedule and can't be triggered manually.

**Note:** Running `gcloud biglake iceberg tables list` doesn't verify your perimeter rules if tables were synchronized before you enforced the perimeter. When VPC Service Controls blocks access to a table during background metadata refresh, Lakehouse skips that table and continues synchronizing the remaining tables, while `tables list` returns Lakehouse's previously synchronized copy.

In the Logs Explorer, select the protected project—your catalog endpoint project for external cloud storage, or your Cloud Storage bucket project for Cloud Storage tables. For more information, see [Retrieve VPC Service Controls errors from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors). Run the following query:
         
         log_id("cloudaudit.googleapis.com/policy")
         protoPayload.metadata.@type:"type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
         

If violation entries appear after your rule propagates, then inspect the `egressViolations.targetResource`, `ingressViolations.targetResource`, and `authenticationInfo.principalEmail` fields in the log entry to confirm that they match the resources and identities in your rule. If new tables fail to synchronize and no `VpcServiceControlAuditMetadata` entries appear, then check your remote catalog permissions and credentials; see [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

  2. Run a test query against a table in BigQuery using the four-part **P.C.N.T** (**Project.Catalog.Namespace.Table**) naming convention:
         
         SELECT COUNT(*)
         FROM `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`;
         

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project that contains the federated catalog endpoint.
     * `CATALOG_ID`: the ID of your federated catalog endpoint.
     * `NAMESPACE`: the namespace in the federated catalog endpoint.
     * `TABLE_NAME`: the name of a table in the namespace.

If a query is blocked by VPC Service Controls, then the error message includes a `vpcServiceControlsUniqueIdentifier` value. Filter [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied) in the Logs Explorer by matching `protoPayload.metadata.vpcServiceControlsUniqueId` to that identifier:
    
    log_id("cloudaudit.googleapis.com/policy")
    protoPayload.metadata.@type:"type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"
    protoPayload.metadata.vpcServiceControlsUniqueId="UNIQUE_IDENTIFIER"
    

Replace `UNIQUE_IDENTIFIER` with the `vpcServiceControlsUniqueIdentifier` value from the error message.




## What's next

  * [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data)
  * [Credential vending overview](https://docs.cloud.google.com/lakehouse/docs/credential-vending)
  * [VPC Service Controls ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules)
  * [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
