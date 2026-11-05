---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue/
title: Set up cross-cloud connection for AWS Glue \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:19:34.224896+00:00
---

# Set up cross-cloud connection for AWS Glue  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-aws-glue/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud connection for AWS Glue Stay organized with collections  Save and categorize content based on your preferences. 

A cross-cloud connection to an AWS Glue Data Catalog lets you query data from that catalog directly within Google Cloud. This capability unifies your data analytics by integrating your external data sources with your existing Google Cloud environment.

After you set up the connection, you can query and govern your federated Apache Iceberg tables in Lakehouse without moving files.

## Before you begin

  1. Review the [Lakehouse overview](https://docs.cloud.google.com/lakehouse/docs/introduction) to understand how Lakehouse manages access to data.
  2. Read [about accessing cross-cloud data](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) to understand how it works.
  3. Review the [supported catalogs](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#supported-catalogs) to verify supported configurations.
  4. Optional: If you plan to route query reads or background metadata refresh over a private interconnect between your Google Cloud Virtual Private Cloud (VPC) network and your AWS VPC, verify that you have an active AWS account, provision a [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or [Partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview), establish BGP sessions with your Cloud Router, and verify that you have the required Identity and Access Management (IAM) permissions in both cloud environments.

  5. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to set up Lakehouse for cross-cloud data access, ask your administrator to grant you the following IAM roles on your project: 

  * Manage Lakehouse catalogs: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * Route traffic over private interconnect (User): [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Route traffic over private interconnect (Catalog service account): 
    * [Service Directory Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)
    * [Service Directory PSC Authorized Service ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.pscAuthorizedService) (`roles/servicedirectory.pscAuthorizedService`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Limitations and considerations

This section lists the limitations and considerations for accessing cross-cloud data.

  * **VPC Service Controls:** If the project that contains your federated catalog endpoint or underlying Cloud Storage bucket is inside a VPC Service Controls service perimeter, then you must configure egress or ingress rules. For more information, see [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * **Supported cloud providers for Cross-Cloud Interconnect:** Using a private interconnect to route query transport, background metadata refresh, or both is supported with AWS. You can use [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or [partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview).
  * **Network routing:** If you don't configure a private interconnect for query transport or background metadata refresh, the corresponding traffic routes over the public internet using TLS. Routing query reads over the public internet can result in higher egress fees from your remote cloud provider and less predictable performance.
  * **Read-only:** Federated catalogs in Lakehouse are read-only views of the remote catalog. Resource manipulation (such as creating, updating, or deleting resources) isn't supported and must be performed directly in the remote catalog.
  * **Data freshness:** The `--refresh-interval` flag for a federated catalog determines how often metadata is synchronized. The value must be `0s` (disabled) or at least `300s` (5 minutes). A catalog's background metadata refresh may take longer the more namespace and table resources there are. If the previous refresh overruns, the current refresh is skipped, and the next refresh is scheduled at the following interval. Queries use the most recently synchronized catalog metadata, so changes made in the remote catalog, such as new tables, schema updates, or newly committed data, aren't visible in Lakehouse until the next background metadata refresh completes. 
  * **Lakehouse caching:** Cross-cloud caching is disabled by default (`--cross-cloud-cache=disabled`). You can enable or disable caching at the federated catalog or connection level. Customer-managed encryption keys (CMEK) aren't supported for caching; cached files are encrypted using Google-owned and Google-managed encryption keys. If the `constraints/gcp.restrictNonCmekServices` organization policy constraint is enforced on a table in the query, caching is automatically disabled for that query. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching). 
  * **Data residency and compliance:** When you enable cross-cloud caching on a federated catalog or connection, Lakehouse temporarily stores cached files at rest in the Google Cloud region where the query runs. If your remote cloud files reside in a different jurisdiction, verify that cross-region caching meets your organization's data residency and compliance requirements before enabling it. 



## General workflow

To access cross-cloud data, follow these general steps:

  * **Set up Cross-Cloud Interconnect (optional):** Configure a private connection between your Google Cloud VPC network and your AWS VPC.
  * **Set up federation:** Configure authentication by creating an IAM role with a placeholder trust policy in AWS. Then, create a federated catalog in Lakehouse and update the trust policy.
  * **Verify the connection:** Verify that Lakehouse can connect to your remote catalog.
  * **Query data:** Run queries against your federated data by using BigQuery or Managed Service for Apache Spark using the 4-part `PROJECT_ID.CATALOG_NAME.NAMESPACE.TABLE` naming convention. You can optionally enable cross-cloud caching on the federated catalog to help reduce cross-cloud egress costs and accelerate subsequent queries. For more information, see [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * **Configure permissions:** Use IAM to manage who can view and query the federated data.



## Set up Cross-Cloud Interconnect (optional)

By default, both query data reads and background metadata refresh travel over the public internet using TLS. To help enhance network isolation, provide predictable latency, and reduce data transfer costs, you can configure a private interconnect between your Google Cloud VPC network and your remote cloud network (AWS VPC).

You can provision either of the following private interconnect options:

  * [**Dedicated Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process): A dedicated physical connection.
  * [**Partner Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview): A connection to AWS through a supported service provider.



Establish BGP sessions between your Cloud Router in Google Cloud and your remote cloud network to enable route exchange.

You can configure private routing over Cross-Cloud Interconnect for either or both of the following traffic paths, depending on your security and cost requirements:

  * **Query transport (`--service-directory-name`):** Routes query reads from BigQuery or open-source engines to your remote object storage (Amazon S3) to help lower cross-cloud egress fees and keep query latency predictable.
  * **Background metadata refresh (`--metadata-service-directory-name`):** Routes control-plane background metadata refresh and authentication requests from the Lakehouse runtime catalog to your remote AWS Glue Data Catalog private endpoint—for example, when your remote catalog restricts public internet access.



If you route both query transport and background metadata refresh over Cross-Cloud Interconnect, complete the private endpoint, routing, and Service Directory service steps once for your remote storage endpoint and once for your remote catalog endpoint. Both Service Directory services must reside in the same Google Cloud region as your federated catalog and can share the same proxy-only subnet and Service Directory namespace.

You can use either of two architectural flows to route traffic from Service Directory to your remote private endpoints:

  * **Internal regional proxy Network Load Balancer routing:** Uses a Google Cloud internal regional proxy Network Load Balancer to distribute requests across Hybrid Connectivity Network Endpoint Groups (NEGs) that point to your remote private endpoint IP addresses (AWS Elastic Network Interfaces (ENIs)). This flow is required for Partner Cross-Cloud Interconnect and recommended for Dedicated Cross-Cloud Interconnect for load balancing, scalability, and high availability.
  * **Direct endpoint routing:** Connects Service Directory directly to a single remote private endpoint IP address. This flow works only with Dedicated Cross-Cloud Interconnect and isn't supported for Partner Cross-Cloud Interconnect.



Select the configuration flow that matches your architecture requirements:

###  Internal regional proxy Network Load Balancer 

To configure an internal regional proxy Network Load Balancer that distributes requests across your remote private endpoint IP addresses, follow these steps:

**Configure remote cloud private endpoints**

Create private endpoints in the remote network and subnets that connect to your Google Cloud VPC network through Cross-Cloud Interconnect, and note the private IP addresses assigned to each endpoint:

  * **For private query transport (remote object storage):** Create an [Interface VPC Endpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) (`com.amazonaws.AWS_REGION.s3`) in your AWS VPC, and note the private IP addresses of the provisioned ENIs.
  * **For private background metadata refresh (remote catalog):** Create an [Interface VPC Endpoint for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html) (`com.amazonaws.AWS_REGION.glue`) in your AWS VPC, and note the private IP addresses of the provisioned ENIs.
  * **Inbound security rules:** Verify that the AWS Security Groups attached to your private endpoints allow inbound TCP traffic on port `443` from your Google Cloud VPC CIDR ranges. Include the CIDR range of your Google Cloud proxy-only subnet to allow health checks and forwarded traffic.



**Configure Google Cloud networking**

**Important:** You must deploy all Google Cloud resources in this section (health check, hybrid NEGs, backend service, and load balancer) in the same region where your Cross-Cloud Interconnect VLAN attachment is located. If they are in different regions, traffic fails to route to your remote endpoint.

Run the following commands to configure the internal load balancer. If you are routing both query transport and background metadata refresh over Cross-Cloud Interconnect, configure a separate backend service, target TCP proxy, and forwarding rule for your storage endpoint and your catalog endpoint. For advanced configurations, see [Set up an internal regional proxy Network Load Balancer for hybrid endpoints](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).

**Note:** Before you begin, ensure that you have a proxy-only subnet configured in your VPC network in the region. If you don't have one, create it:
    
    
    gcloud compute networks subnets create PROXY_SUBNET_NAME \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=REGION \
        --network=VPC_NETWORK \
        --range=PROXY_SUBNET_RANGE

Replace the following:

  * `PROXY_SUBNET_NAME`: a name for the proxy-only subnet.
  * `PROXY_SUBNET_RANGE`: an unused CIDR range within your VPC network (for example, `10.129.0.0/23`).

**Important:** Cloud Router doesn't automatically advertise proxy-only subnets using BGP. You must manually configure your Cloud Router to advertise `PROXY_SUBNET_RANGE` to your remote network using custom route advertisements so that response traffic from your remote endpoint can route back to the load balancer.

  1. Create a regional TCP health check:
         
         gcloud compute health-checks create tcp HEALTH_CHECK_NAME \
             --region=REGION \
             --port=443

Replace the following:

     * `HEALTH_CHECK_NAME`: a name for the health check.
     * `REGION`: the Google Cloud region (for example, `us-east4`).
  2. Create Hybrid Connectivity Network Endpoint Groups (NEGs) and add endpoints:

Create a hybrid NEG (`NON_GCP_PRIVATE_IP_PORT`) for each zone:
         
         gcloud compute network-endpoint-groups create NEG_NAME \
             --network-endpoint-type=NON_GCP_PRIVATE_IP_PORT \
             --zone=ZONE \
             --network=VPC_NETWORK

Add the private IP address of your remote endpoint ENI to the hybrid NEG:
         
         gcloud compute network-endpoint-groups update NEG_NAME \
             --zone=ZONE \
             --add-endpoint="ip=REMOTE_ENDPOINT_IP,port=443"

Replace the following:

     * `NEG_NAME`: a name for the hybrid NEG.
     * `ZONE`: the Google Cloud zone (for example, `us-east4-a`). This zone must reside within the region of your Cross-Cloud Interconnect VLAN attachment.
     * `VPC_NETWORK`: the name of your VPC network.
     * `REMOTE_ENDPOINT_IP`: the private IP address of your remote storage or remote catalog private endpoint in that zone.

If your remote endpoint has multiple private IP addresses distributed across zones, repeat these commands to create hybrid NEGs and add endpoints for each zone.

  3. Create and configure the backend service:

Create a regional backend service with internal managed load balancing:
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=TCP \
             --region=REGION \
             --health-checks=HEALTH_CHECK_NAME \
             --health-checks-region=REGION

Add your hybrid NEGs to the backend service:
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --region=REGION \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-zone=ZONE \
             --balancing-mode=CONNECTION \
             --max-connections=MAX_CONNECTIONS

Replace the following:

     * `BACKEND_SERVICE_NAME`: a name for the backend service.
     * `NEG_NAME`: the name of the hybrid NEG that you created in the preceding step.
     * `ZONE`: the Google Cloud zone (for example, `us-east4-a`).
     * `MAX_CONNECTIONS`: the maximum concurrent connections for the backend (for example, `100`).

Repeat the `add-backend` command for each hybrid NEG that you created.

  4. Configure the load balancer frontend:

Create a target TCP proxy:
         
         gcloud compute target-tcp-proxies create TARGET_PROXY_NAME \
             --backend-service=BACKEND_SERVICE_NAME \
             --region=REGION

Create a forwarding rule to route traffic to the target proxy:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=VPC_NETWORK \
             --subnet=VPC_SUBNET \
             --ports=443 \
             --region=REGION \
             --target-tcp-proxy=TARGET_PROXY_NAME \
             --target-tcp-proxy-region=REGION \
             --allow-global-access

Replace the following:

     * `TARGET_PROXY_NAME`: a name for the target proxy.
     * `FORWARDING_RULE_NAME`: a name for the forwarding rule.
     * `VPC_SUBNET`: the name of your VPC subnetwork.



After creating the forwarding rule for the load balancer, note the internal IP address assigned to it. This is your `ILB_IP_ADDRESS`.

**Configure Service Directory**

Register the internal load balancer's IP address in Service Directory so that Lakehouse can discover and route to it privately. If you configured separate load balancer forwarding rules for query transport and background metadata refresh, create a separate Service Directory service and endpoint for each forwarding rule IP address.

  1. Create a namespace for your remote private endpoints:
         
         gcloud service-directory namespaces create NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `NAMESPACE`: a unique identifier for your namespace.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region (for example, `us-east4`). This must be the same region as your federated catalog.
  2. Create a service in the Service Directory namespace:
         
         gcloud service-directory services create SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `SERVICE_NAME`: a unique identifier for your service (create a separate service name, such as `METADATA_SERVICE_NAME`, when registering a background metadata refresh endpoint).
  3. Create an endpoint for the load balancer forwarding rule in the service:
         
         gcloud service-directory endpoints create ENDPOINT_NAME \
             --project=PROJECT_ID \
             --namespace=NAMESPACE \
             --service=SERVICE_NAME \
             --location=REGION \
             --network=projects/PROJECT_NUMBER/global/networks/VPC_NETWORK \
             --address=ILB_IP_ADDRESS \
             --port=443

Replace the following:

     * `ENDPOINT_NAME`: a unique identifier for your endpoint.
     * `PROJECT_NUMBER`: your Google Cloud project number. Use your project number in the `--network` flag.
     * `ILB_IP_ADDRESS`: the internal IP address of your load balancer forwarding rule.



###  Direct endpoint 

To configure Service Directory to route traffic directly to a single remote private endpoint IP address over Dedicated Cross-Cloud Interconnect, follow these steps:

  1. Create the private endpoint in your remote cloud network:

     * **For private query transport:** Create an [Interface VPC Endpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) (`com.amazonaws.AWS_REGION.s3`) in your AWS VPC.
     * **For private background metadata refresh:** Create an [Interface VPC Endpoint for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html) (`com.amazonaws.AWS_REGION.glue`) in your AWS VPC.

Note the private IP address and port (`443`) of each endpoint, and verify that your AWS Security Groups allow inbound TCP traffic on port `443` from your Google Cloud VPC network.

  2. Create a namespace for your remote private endpoints:
         
         gcloud service-directory namespaces create NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `NAMESPACE`: a unique identifier for your namespace.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region (for example, `us-east4`). This must be the same region as your federated catalog.
  3. Create a service in the Service Directory namespace (if you are routing both query transport and background metadata refresh privately, create a separate service for each endpoint):
         
         gcloud service-directory services create SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION

Replace the following:

     * `SERVICE_NAME`: a unique identifier for your service (create a separate service name, such as `METADATA_SERVICE_NAME`, when registering a background metadata refresh endpoint).
  4. Create an endpoint in the service with the private IP address and port of your remote private endpoint:
         
         gcloud service-directory endpoints create ENDPOINT_NAME \
             --service=SERVICE_NAME \
             --namespace=NAMESPACE \
             --project=PROJECT_ID \
             --location=REGION \
             --address=REMOTE_ENDPOINT_IP \
             --port=REMOTE_ENDPOINT_PORT \
             --network=projects/PROJECT_NUMBER/global/networks/VPC_NETWORK

Replace the following:

     * `ENDPOINT_NAME`: a unique identifier for your endpoint.
     * `REMOTE_ENDPOINT_IP`: the private IP address of your remote storage or remote catalog private endpoint (for example, `10.0.1.45`).
     * `REMOTE_ENDPOINT_PORT`: the port number of your remote private endpoint (for example, `443`).
     * `PROJECT_NUMBER`: your Google Cloud project number. Use your project number in the `--network` flag.
     * `VPC_NETWORK`: the Google Cloud VPC network name associated with your private interconnect.



## Set up federation

To query your data, you must set up a Lakehouse federated catalog that connects to your remote AWS Glue Data Catalog.

### Create the AWS IAM role with a placeholder trust policy

Lakehouse provisions a Google service account ID after catalog creation. Create the AWS IAM role with a placeholder trust policy.

  1. Create a file named `trust_policy.json`:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "Federated": "accounts.google.com"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                 "StringEquals": {
                   "accounts.google.com:aud": [
                     "PLACEHOLDER_VALUE"
                   ],
                   "accounts.google.com:sub": [
                     "PLACEHOLDER_VALUE"
                   ]
                 }
               }
             }
           ]
         }

  2. Run the AWS CLI command to create the role with the placeholder trust policy. We recommend setting the maximum session duration to 12 hours (`43200` seconds) to prevent credential expiration during long-running jobs:
         
         aws iam create-role \
           --role-name AWS_ROLE_NAME \
           --assume-role-policy-document file://trust_policy.json \
           --max-session-duration 43200

Replace the following:

     * `AWS_ROLE_NAME`: a name for your AWS IAM role. For example, `lakehouse_glue_federation_role`.



### Attach a permissions policy

Attach a permissions policy to your IAM role that lets Lakehouse access the AWS region's Glue Data Catalog and S3 buckets. This policy also grants access to S3 table buckets if you use the [AWS Lake Formation S3 Tables integration](https://docs.aws.amazon.com/lake-formation/latest/dg/enable-s3-tables-catalog-integration.html). If you have [upgraded from the default AWS Glue data permissions to the AWS Lake Formation model](https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html), you might need to grant additional permissions in Lake Formation instead.

  1. Create a file named `permissions_policy.json` with the following policy configuration.

**Important:** For ease of use, the following AWS IAM policy doesn't have restrictive `Resource` elements. We recommend restricting access to the specific [Glue resources](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html), [S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html), and [S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-setting-up.html) that your architecture requires.
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "GlueRead",
               "Effect": "Allow",
               "Action": [
                 "glue:GetCatalog",
                 "glue:GetDatabase",
                 "glue:GetDatabases",
                 "glue:GetTable",
                 "glue:GetTables"
               ],
               "Resource": "arn:aws:glue:AWS_REGION:AWS_ACCOUNT_ID:*"
             },
             {
               "Sid": "S3Read",
               "Effect": "Allow",
               "Action": [
                 "s3:ListBucket",
                 "s3:GetObject"
               ],
               "Resource": [
                 "arn:aws:s3:::*"
               ]
             },
             {
               "Sid": "S3TablesRead",
               "Effect": "Allow",
               "Action": [
                 "s3tables:GetTableBucket",
                 "s3tables:ListNamespaces",
                 "s3tables:GetNamespace",
                 "s3tables:ListTables",
                 "s3tables:GetTable",
                 "s3tables:GetTableMetadataLocation",
                 "s3tables:GetTableData"
               ],
               "Resource": [
                 "arn:aws:s3tables:AWS_REGION:AWS_ACCOUNT_ID:*"
               ]
             }
           ]
         }

If you are using customer-managed keys hosted in AWS Key Management Service (KMS) to encrypt AWS Glue, Amazon S3, or Amazon S3 Tables resources, you must add a statement granting KMS key access to decrypt the resources:
         
         # ...
         {
           "Sid": "GlueS3S3TablesKmsDecrypt",
           "Effect": "Allow",
           "Action": [
               "kms:Decrypt"
           ],
           "Resource": [
               "arn:aws:kms:AWS_REGION:AWS_ACCOUNT_ID:key/key_id_for_glue",
               "arn:aws:kms:AWS_REGION:AWS_ACCOUNT_ID:key/key_id_for_s3",
               "arn:aws:kms:AWS_REGION:AWS_ACCOUNT_ID:key/key_id_for_s3_tables"
           ]
         }
         # ...

  2. Attach this permissions policy to your IAM role:
         
         aws iam put-role-policy \
           --role-name AWS_ROLE_NAME \
           --policy-name AWS_POLICY_NAME \
           --policy-document file://permissions_policy.json

Replace the following:

     * `AWS_ROLE_NAME`: the name of your AWS IAM role. For example, `lakehouse_glue_federation_role`.
     * `AWS_POLICY_NAME`: a name for your permissions policy. For example, `lakehouse_glue_federation_policy`.
     * `AWS_REGION`: the AWS region where your Glue catalog or S3 Tables reside. For example, `us-east-1`.
     * `AWS_ACCOUNT_ID`: your 12-digit AWS account ID string. For example, `123456789012`.



### Create a federated catalog

Create the federated catalog using the Google Cloud console or the Google Cloud CLI.

**Note:** When establishing an AWS Glue federated catalog, the `warehouse` property inside `glue_catalog_info` (or `--glue-warehouse` flag) must be set to your 12-digit AWS Account ID string or S3 table bucket catalog, rather than an S3 bucket URI. AWS Glue Iceberg REST endpoints resolve warehouse catalogs by using the Account ID directly.

To prevent premature background metadata refresh failures while AWS trust relationships are propagating, initialize the catalog without specifying a refresh schedule (which defaults to `0s`).

###  Console 

To create a federated catalog:

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click add_box **Create catalog**.

  3. Click **Federated catalog**.

The **Catalog configuration** section appears.

  4. For **Federated catalog source** , select **AWS Glue**.

  5. For **Data location** , select the Lakehouse region where you want to create the federated catalog. For example, `us-east4`. To minimize latency (even over public internet) select the Google Cloud region closest to your AWS region.

  6. Click **Continue**.

The **Connection details** section appears.

  7. In the **Remote catalog details** section, in the **AWS warehouse** field, enter your AWS account ID or S3 table bucket catalog. For example: `123456789012` or `123456789012:s3tablescatalog/my-table-bucket`.

  8. In the **AWS region** field, enter your AWS region. For example: `us-east-1`.

  9. In the **AWS role ARN** field, enter your AWS role ARN. Use the following format: `arn:aws:iam::AWS_ACCOUNT_ID:role/AWS_ROLE_NAME`.

  10. Under **Transport layer** , select **Public internet** or **Dedicated private interconnect**. If you select **Dedicated private interconnect** , configure the following fields:

     * In the **Service directory name** field, enter the path to your transport Service Directory service in the format `projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME`.
     * Optional: To synchronize catalog metadata privately over Cross-Cloud Interconnect, in the **Metadata service directory name** field, enter the path to your metadata Service Directory service in the format `projects/PROJECT_ID/locations/REGION/namespaces/METADATA_SERVICE_DIRECTORY_NAMESPACE/services/METADATA_SERVICE_NAME`.
  11. Click **Create**.




###  gcloud 

#### Public internet (no CCI)

If you don't configure Cross-Cloud Interconnect, connections travel over the public internet using TLS.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="glue" \
        --glue-warehouse="GLUE_OR_S3_TABLE_BUCKET_WAREHOUSE" \
        --glue-aws-region="AWS_REGION" \
        --glue-aws-role-arn="arn:aws:iam::AWS_ACCOUNT_ID:role/AWS_ROLE_NAME" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE"

#### Customer-owned (CCI)

If you configured a private interconnect (Dedicated or Partner Cross-Cloud Interconnect), provide the Service Directory service reference for private query transport (`--service-directory-name`), private background metadata refresh (`--metadata-service-directory-name`), or both. You can also add or update either flag on an existing catalog by running `gcloud biglake iceberg catalogs update`.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="glue" \
        --glue-warehouse="GLUE_OR_S3_TABLE_BUCKET_WAREHOUSE" \
        --glue-aws-region="AWS_REGION" \
        --glue-aws-role-arn="arn:aws:iam::AWS_ACCOUNT_ID:role/AWS_ROLE_NAME" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE" \
        --service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME" \
        --metadata-service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/METADATA_SERVICE_DIRECTORY_NAMESPACE/services/METADATA_SERVICE_NAME"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: a name for your federated catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Lakehouse region where the federated catalog is created. This must be the same region as the Service Directory namespace and regional secret.
  * `GLUE_OR_S3_TABLE_BUCKET_WAREHOUSE`: your target warehouse catalog identifier. For an AWS region's Glue Data Catalog, enter your 12-digit AWS account ID string. For example, `123456789012`. To use an S3 table bucket in the region, enter `AWS_ACCOUNT_ID:s3tablescatalog/S3_TABLE_BUCKET`. For example, `123456789012:s3tablescatalog/my-table-bucket`.
  * `AWS_ACCOUNT_ID`: your 12-digit AWS account ID string. For example, `123456789012`.
  * `AWS_REGION`: the AWS region where your Glue catalog or S3 table bucket resides. For example, `us-east-1`.
  * `AWS_ROLE_NAME`: the name of your AWS IAM role. For example, `lakehouse_glue_federation_role`.
  * `NAMESPACE_FILTERS`: Optional: a comma-separated list of namespaces to federate. For example, `ns1,ns2`. If omitted, Lakehouse includes all namespaces.
  * `CROSS_CLOUD_CACHE_MODE`: Optional: whether to enable cross-cloud caching on the federated catalog (`enabled` or `disabled`). Defaults to `disabled`. When set to `enabled`, Lakehouse caches remote files in the catalog's Google Cloud region. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).
  * If you are using a private interconnect (Cross-Cloud Interconnect), specify either or both of the following Service Directory references (omit either flag if you aren't routing that traffic layer over Cross-Cloud Interconnect): 
    * `SERVICE_DIRECTORY_NAMESPACE` and `SERVICE_NAME`: the Service Directory namespace and service name that you created for private query transport to remote object storage.
    * `METADATA_SERVICE_DIRECTORY_NAMESPACE` and `METADATA_SERVICE_NAME`: the Service Directory namespace and service name that you created for private background metadata refresh.



### Update the trust policy

When the catalog is created, Lakehouse provisions a unique service account for it, which is returned as the `biglake-service-account-id` field in the catalog creation response. You use this service account to establish the trust relationship.

  1. Run the following command to extract the `biglake-service-account-id` value into an active bash variable:
         
         LAKEHOUSE_SA_ID=$(gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID" \
           --format="value(biglake-service-account-id)")

  2. Update your AWS IAM role's trust policy to replace the placeholder with your verified Google Service Agent ID. The condition block validates both `sub` and `aud` matching. Write the policy to a file named `trust_policy_comprehensive.json`:
         
         cat > trust_policy_comprehensive.json << EOF
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "Federated": "accounts.google.com"
               },
               "Action": "sts:AssumeRoleWithWebIdentity",
               "Condition": {
                 "StringEquals": {
                   "accounts.google.com:aud": [
                     "$LAKEHOUSE_SA_ID"
                   ],
                   "accounts.google.com:sub": [
                     "$LAKEHOUSE_SA_ID"
                   ]
                 }
               }
             }
           ]
         }
         EOF

  3. Apply the finalized policy to your AWS role:
         
         aws iam update-assume-role-policy \
           --role-name AWS_ROLE_NAME \
           --policy-document file://trust_policy_comprehensive.json

**Note:** AWS IAM changes can take a few minutes to propagate.



### Enable background metadata refresh

Now that secure trust relationships are successfully established across both platforms, update your catalog to activate background metadata refresh (every 5 minutes or `300s`, or larger).

###  gcloud 
    
    
    gcloud biglake iceberg catalogs update FEDERATED_CATALOG_NAME \
      --project="PROJECT_ID" \
      --refresh-interval="300s"

###  REST 
    
    
    curl -s -X PATCH \
      -H "x-goog-user-project: PROJECT_ID" \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://biglake.googleapis.com/iceberg/v1/restcatalog/extensions/projects/PROJECT_ID/catalogs/FEDERATED_CATALOG_NAME?updateMask=federated_catalog_options.refresh_options.refresh_schedule" \
      -d '{
        "federated_catalog_options": {
          "refresh_options": {
            "refresh_schedule": {
              "refresh_interval": "300s"
            }
          }
        }
      }'

### Complete private interconnect setup (Cross-Cloud Interconnect only)

If you route query transport, background metadata refresh, or both over a private interconnect (Dedicated or Partner Cross-Cloud Interconnect), you must grant the Lakehouse catalog service account permissions to discover and authorize connections through Service Directory. If your transport Service Directory service and metadata Service Directory service are hosted in different Google Cloud projects, grant these roles on each project that hosts a Service Directory service.

**Note:** The catalog service account is an internal Google Cloud service agent. It might not appear in your project's service account list in the Google Cloud console, but you can assign roles to it manually.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant access** (or **Add**).

  3. In the **New principals** field, enter the Lakehouse catalog service account email address. You can retrieve this email address by describing the catalog (see the **gcloud** tab).

  4. In the **Role** menu, select **Service Directory Viewer** (`roles/servicedirectory.viewer`).

  5. Click **Add another role** , and then select **Service Directory PSC Authorized Service** (`roles/servicedirectory.pscAuthorizedService`).

  6. Click **Save**.




###  gcloud 

Grant the required roles to the catalog's service account on the project hosting your Service Directory services:
    
    
    # Grant Service Directory Viewer
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:$(gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --format='value(biglake-service-account)')" \
    --role="roles/servicedirectory.viewer"
    
    # Grant Service Directory PSC Authorized Service
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="serviceAccount:$(gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --format='value(biglake-service-account)')" \
    --role="roles/servicedirectory.pscAuthorizedService"

## Verify the connection

Verify that the catalog background metadata refresh cycle completed successfully and namespaces are synchronized.

  1. Verify that the refresh status indicates success:
         
         gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID"

  2. Confirm that the namespaces are synchronized:
         
         gcloud biglake iceberg namespaces list \
           --project="PROJECT_ID" \
           --catalog="FEDERATED_CATALOG_NAME"




## What's next

  * [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * [Troubleshoot cross-cloud data access](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
