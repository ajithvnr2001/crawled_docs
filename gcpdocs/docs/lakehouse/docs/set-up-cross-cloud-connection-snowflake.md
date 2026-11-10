---
url: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake/
title: Set up cross-cloud connection for Snowflake Horizon Catalog \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:46:28.165476+00:00
---

# Set up cross-cloud connection for Snowflake Horizon Catalog  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-snowflake/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Set up cross-cloud connection for Snowflake Horizon Catalog Stay organized with collections  Save and categorize content based on your preferences. 

A cross-cloud connection to a Snowflake Horizon Catalog on Amazon Web Services (AWS), Microsoft Azure, or Google Cloud lets you query data from that catalog directly within Google Cloud. This capability unifies your data analytics by integrating your external data sources with your existing Google Cloud environment.

After you set up the connection, you can manage access to your federated data in _borderless Lakehouse_.

## Before you begin

  1. Review the [Lakehouse overview](https://docs.cloud.google.com/lakehouse/docs/introduction) to understand how Lakehouse manages access to data.
  2. Read [about accessing cross-cloud data](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) to understand how it works.
  3. Review the [supported catalogs](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#supported-catalogs) to verify supported configurations.
  4. Understand how to use [regional Secret Manager secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs). This is required to set up Lakehouse with Snowflake Horizon Catalog using secret-based authentication.
  5. Optional: If you plan to route query reads or background metadata refresh over a private interconnect between your Google Cloud Virtual Private Cloud (VPC) network and your remote cloud network (AWS VPC or Azure VNet), verify that you have an active account with your remote provider, provision a [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) or [partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview), establish BGP sessions with your Cloud Router, and verify that you have the required Identity and Access Management (IAM) permissions in both cloud environments.

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
  * Manage secrets (if using secret-based authentication): [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) 
  * Route traffic over private interconnect (User): [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Route traffic over private interconnect (Catalog service account): 
    * [Service Directory Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.viewer) (`roles/servicedirectory.viewer`)
    * [Service Directory PSC Authorized Service ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicedirectory#servicedirectory.pscAuthorizedService) (`roles/servicedirectory.pscAuthorizedService`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** If using secret-based authentication, to follow the principle of least privilege and avoid granting access to all secrets in the project, have a Secret Manager administrator create the secret for you and grant you permissions to modify only that specific secret for Lakehouse.

### Limitations and considerations

This section lists the limitations and considerations for accessing cross-cloud data.

  * **VPC Service Controls:** If the project that contains your federated catalog endpoint or underlying Cloud Storage bucket is inside a VPC Service Controls service perimeter, then you must configure egress or ingress rules. For more information, see [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * **Supported cloud providers for Cross-Cloud Interconnect:** Using a private interconnect to route query transport, background metadata refresh, or both is supported with AWS and Azure. You can use [Dedicated Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process) (for AWS or Azure) or [partner Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview).
  * **Network routing:** If you don't configure a private interconnect for query transport or background metadata refresh, the corresponding traffic routes over the public internet using TLS. Routing query reads over the public internet can result in higher egress fees from your remote cloud provider and less predictable performance.
  * **Snowflake Horizon Catalog supported tables:** Only Apache Iceberg tables in Snowflake Horizon Catalog are synchronized to Lakehouse. Non-Iceberg Snowflake tables are ignored during background metadata refresh.
  * **Network policy and egress IP addresses:** When background metadata refresh connects over the public internet, Lakehouse uses Google global infrastructure egress IP addresses to reach your Snowflake internet-facing endpoint. If you configure a Snowflake network policy for public internet access, add the Google egress IP address ranges from [`goog.json`](https://www.gstatic.com/ipranges/goog.json) to your network policy's allowed IP list. When you configure private background metadata refresh over Cross-Cloud Interconnect, metadata requests route privately through your VPC network to your Snowflake PrivateLink endpoint.
  * **Read-only:** Federated catalogs in Lakehouse are read-only views of the remote catalog. Resource manipulation (such as creating, updating, or deleting resources) isn't supported and must be performed directly in the remote catalog.
  * **Data freshness:** The `--refresh-interval` flag for a federated catalog determines how often metadata is synchronized. The value must be `0s` (disabled) or at least `300s` (5 minutes). A catalog's background metadata refresh may take longer the more namespace and table resources there are. If the previous refresh overruns, the current refresh is skipped, and the next refresh is scheduled at the following interval. Queries use the most recently synchronized catalog metadata, so changes made in the remote catalog, such as new tables, schema updates, or newly committed data, aren't visible in Lakehouse until the next background metadata refresh completes. 
  * **Lakehouse caching:** Cross-cloud caching is disabled by default (`--cross-cloud-cache=disabled`). You can enable or disable caching at the federated catalog or connection level. Customer-managed encryption keys (CMEK) aren't supported for caching; cached files are encrypted using Google-owned and Google-managed encryption keys. If the `constraints/gcp.restrictNonCmekServices` organization policy constraint is enforced on a table in the query, caching is automatically disabled for that query. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching). 
  * **Data residency and compliance:** When you enable cross-cloud caching on a federated catalog or connection, Lakehouse temporarily stores cached files at rest in the Google Cloud region where the query runs. If your remote cloud files reside in a different jurisdiction, verify that cross-region caching meets your organization's data residency and compliance requirements before enabling it. 



## General workflow

To access cross-cloud data, follow these general steps:

  * **Set up Cross-Cloud Interconnect (optional):** Configure a private connection between your Google Cloud VPC network and your remote cloud provider.
  * **Set up federation:** Configure authentication and create a federated catalog in Lakehouse. 
    * **Secret-based authentication (PAT):** Create a secret in Secret Manager with your remote catalog credentials. Then, create a federated catalog in Lakehouse and grant the catalog service account access to the secret.
    * **Workload Identity Federation (WIF):** Create a federated catalog in Lakehouse specifying the required Snowflake role. Then, link the catalog's service account ID to a service user in Snowflake. The Snowflake service user must have usage permissions on the remote Snowflake Horizon Catalog.
  * **Verify the connection:** Verify that Lakehouse can connect to your remote catalog.
  * **Query data:** Run queries against your federated data using BigQuery or Managed Service for Apache Spark. You can optionally enable cross-cloud caching on the federated catalog to help reduce cross-cloud egress costs and accelerate subsequent queries. For more information, see [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * **Configure permissions:** Use IAM to manage who can view and query the federated data.



## Set up Cross-Cloud Interconnect (optional)

By default, both query data reads and background metadata refresh travel over the public internet using TLS. To help enhance network isolation, provide predictable latency, and reduce data transfer costs, you can configure a private interconnect between your Google Cloud VPC network and your remote cloud network (AWS VPC or Azure Virtual Network (VNet)).

You can provision either of the following private interconnect options:

  * [**Dedicated Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#setup-process): A dedicated physical connection to AWS or Azure.
  * [**Partner Cross-Cloud Interconnect**](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-cci-for-csp-overview): A connection to AWS through a supported service provider.



Establish BGP sessions between your Cloud Router in Google Cloud and your remote cloud network to enable route exchange.

You can configure private routing over Cross-Cloud Interconnect for either or both of the following traffic paths, depending on your security and cost requirements:

  * **Query transport (`--service-directory-name`):** Routes query reads from BigQuery or open-source engines to your remote object storage (Amazon S3 or Azure Data Lake Storage Gen2 (ADLS Gen2)) to help lower cross-cloud egress fees and keep query latency predictable.
  * **Background metadata refresh (`--metadata-service-directory-name`):** Routes control-plane background metadata refresh and authentication requests from the Lakehouse runtime catalog to your remote Snowflake Horizon Catalog private endpoint—for example, when your remote catalog restricts public internet access.



If you route both query transport and background metadata refresh over Cross-Cloud Interconnect, complete the private endpoint, routing, and Service Directory service steps once for your remote storage endpoint and once for your remote catalog endpoint. Both Service Directory services must reside in the same Google Cloud region as your federated catalog and can share the same proxy-only subnet and Service Directory namespace.

You can use either of two architectural flows to route traffic from Service Directory to your remote private endpoints:

  * **Internal regional proxy Network Load Balancer routing:** Uses a Google Cloud internal regional proxy Network Load Balancer to distribute requests across Hybrid Connectivity Network Endpoint Groups (NEGs) that point to your remote private endpoint IP addresses (AWS Elastic Network Interfaces (ENIs) or Azure Private Endpoint network interfaces (NICs)). This flow is required for Partner Cross-Cloud Interconnect and recommended for Dedicated Cross-Cloud Interconnect for load balancing, scalability, and high availability.
  * **Direct endpoint routing:** Connects Service Directory directly to a single remote private endpoint IP address. This flow works only with Dedicated Cross-Cloud Interconnect and isn't supported for Partner Cross-Cloud Interconnect.



Select the configuration flow that matches your architecture requirements:

###  Internal regional proxy Network Load Balancer 

To configure an internal regional proxy Network Load Balancer that distributes requests across your remote private endpoint IP addresses, follow these steps:

**Configure remote cloud private endpoints**

Create private endpoints in the remote network and subnets that connect to your Google Cloud VPC network through Cross-Cloud Interconnect, and note the private IP addresses assigned to each endpoint:

  * **For private query transport (remote object storage):** On AWS, create an [Interface VPC Endpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) (`com.amazonaws.AWS_REGION.s3`) in your AWS VPC, and note the ENI private IP addresses. On Azure, create an [Azure Private Endpoint for Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-private-endpoints) targeting your ADLS Gen2 storage account (`dfs` or `blob`) in your Azure VNet, and note the NIC private IP address.
  * **For private background metadata refresh (remote catalog):** In Snowflake, run `SELECT SYSTEM$GET_PRIVATELINK_CONFIG();` to obtain your PrivateLink service identifier and your `.privatelink` account identifier. On AWS, follow [AWS PrivateLink and Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink) to create an Interface VPC Endpoint in your AWS VPC, and note the ENI private IP addresses. On Azure, follow [Azure Private Link and Snowflake](https://docs.snowflake.com/en/user-guide/privatelink-azure) to create an Azure Private Endpoint in your Azure VNet, and note the NIC private IP address.
  * **Inbound security rules:** Verify that the AWS Security Groups or Azure Network Security Groups (NSGs) attached to your private endpoints allow inbound TCP traffic on port `443` (and port `80` if your Snowflake configuration uses OCSP) from your Google Cloud VPC CIDR ranges. Include the CIDR range of your Google Cloud proxy-only subnet to allow health checks and forwarded traffic.



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

Add the private IP address of your remote endpoint ENI or NIC to the hybrid NEG:
         
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

     * **For private query transport:** Create an [Interface VPC Endpoint for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in your AWS VPC or an [Azure Private Endpoint for Azure Storage](https://learn.microsoft.com/azure/storage/common/storage-private-endpoints) (`dfs` or `blob`) in your Azure VNet.
     * **For private background metadata refresh:** Run `SELECT SYSTEM$GET_PRIVATELINK_CONFIG();` in Snowflake, and create an Interface VPC Endpoint following [AWS PrivateLink and Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink) or an Azure Private Endpoint following [Azure Private Link and Snowflake](https://docs.snowflake.com/en/user-guide/privatelink-azure).

Note the private IP address and port (`443`) of each endpoint, and verify that your AWS Security Groups or Azure NSGs allow inbound TCP traffic on port `443` from your Google Cloud VPC network.

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

To query your data, you must set up a Lakehouse federated catalog that connects to your remote Snowflake Horizon Catalog.

### Configure authentication

Federation requires credentials or role configuration to access the remote Snowflake Horizon Catalog. Choose one of the following methods.

###  Secret-based (PAT) 

This option uses a programmatic access token (PAT) stored securely with regional [Secret Manager](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs) secrets.

  1. Generate a [programmatic access token (PAT)](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) that has read access to the target catalog.

  2. Create a JSON file named `credentials.json` with your payload:
         
         {
           "client_secret": "SNOWFLAKE_PAT_TOKEN",
           "scope": "session:role:SNOWFLAKE_ROLE"
         }

**Important:** Store this JSON structure in the secret, not the raw Personal Access Token (PAT) string. Storing the raw token without the JSON wrapper causes background metadata refresh to fail with Code 16.

Replace the following:

     * `SNOWFLAKE_PAT_TOKEN`: Your Snowflake Programmatic Access Token (PAT).
     * `SNOWFLAKE_ROLE`: The specific Snowflake role required for the session. For example, `ICEBERG_VIEW`.
**Note:** The `client_id` parameter isn't required for Snowflake Horizon Catalog setups because authentication is handled by the PAT and the scope.
  3. Configure the regional endpoint for Secret Manager:

By default, Secret Manager uses a global endpoint. However, Lakehouse requires that your secrets be stored in the same region as your Lakehouse catalog. To interact with regional secrets using the Google Cloud CLI, you must override the default API endpoint for your current session or profile.
         
         gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/

Replace the following:

     * `REGION`: The Google Cloud region where your Secret Manager secret is stored. For example, `us-east4`. To avoid connectivity issues, your secret and your catalog must be created in the same region.
  4. Upload the payload to Secret Manager:
         
         gcloud secrets create SNOWFLAKE_SECRET_NAME \
           --location="REGION" \
           --project="PROJECT_ID" \
           --data-file=credentials.json

Replace the following:

     * `SNOWFLAKE_SECRET_NAME`: A name for your Snowflake secret.
     * `PROJECT_ID`: your Google Cloud project ID.



###  Workload Identity Federation 

Workload Identity Federation (WIF) avoids the use of long-lived secrets by linking a Lakehouse catalog service account directly to a Snowflake service user. There is no prerequisite setup. Continue with creating the federated catalog.

### Create a federated catalog

Create the federated catalog using the Google Cloud console or the `gcloud` CLI.

###  Console 

To create a federated catalog:

  1. In the Google Cloud console, go to **Lakehouse**.

[Go to Lakehouse](https://console.cloud.google.com/biglake)

  2. Click add_box **Create catalog**.

  3. Click **Federated catalog**.

The **Catalog configuration** section appears.

  4. For **Federated catalog source** , select **Snowflake (Horizon)**.

  5. For **Data location** , select the Lakehouse region where you want to create the federated catalog. For example, `us-east4`. To minimize latency (even over public internet) do the following when selecting a region:

     * If your Snowflake Horizon Catalog is on AWS, select the Google Cloud region closest to your AWS region.
     * If your Snowflake Horizon Catalog is on Azure, select the Google Cloud region closest to your Azure region.
     * If your Snowflake Horizon Catalog is on Google Cloud, select the exact same region.
  6. Optional: Under **Cross-cloud caching** , select **Enable cross-cloud caching** to cache remote files in the catalog's Google Cloud region and accelerate query performance. You can also update this setting later by editing the catalog details. For more information about how caching works, retention, and pricing, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).

  7. Click **Continue**.

The **Connection details** section appears.

  8. In the **Remote catalog details** section, in the **Snowflake account identifier** field, enter your Snowflake account identifier (for example, `myorg-myaccount`). If you route background metadata refresh privately over AWS PrivateLink or Azure Private Link, enter your `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`).

  9. In the **Snowflake warehouse** field, enter your Snowflake warehouse name. This is also known as the database name in Snowflake Horizon Catalog.

  10. Select an option for **Authentication Method** :

     * For **Secret** , enter the name of your secret for **Secret-based (PAT)**. Use the following format: `projects/PROJECT_ID/locations/REGION/secrets/SNOWFLAKE_SECRET_NAME`.
     * For **OIDC** , enter your Snowflake role for **Workload Identity Federation**. For example, `ICEBERG_VIEW`.
  11. Under **Transport layer** , select **Public internet** (default) or **Dedicated private interconnect**. If you select **Dedicated private interconnect** , configure the following fields:

     * In the **Service directory name** field, enter the path to your transport Service Directory service in the format `projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME`.
     * Optional: To synchronize catalog metadata privately over Cross-Cloud Interconnect, in the **Metadata service directory name** field, enter the path to your metadata Service Directory service in the format `projects/PROJECT_ID/locations/REGION/namespaces/METADATA_SERVICE_DIRECTORY_NAMESPACE/services/METADATA_SERVICE_NAME`.
  12. Click **Create**.




To update **Transport layer** , **Service directory name** , or **Metadata service directory name** on an existing federated catalog, open the catalog in **Lakehouse** , click **Edit catalog** , modify the fields, and click **Save**.

###  gcloud 

###  Secret-based (PAT) 

If you use secret-based authentication, you must specify `--secret-name`.

#### Public internet (no CCI)

If you don't configure Cross-Cloud Interconnect, connections travel over the public internet using TLS.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="snowflake" \
        --secret-name="projects/PROJECT_ID/locations/REGION/secrets/SNOWFLAKE_SECRET_NAME" \
        --snowflake-account-identifier="SNOWFLAKE_ACCOUNT_IDENTIFIER" \
        --snowflake-warehouse="SNOWFLAKE_WAREHOUSE" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE"

#### Customer-owned (CCI)

If you configured a private interconnect (Dedicated or Partner Cross-Cloud Interconnect), provide the Service Directory service reference for private query transport (`--service-directory-name`), private background metadata refresh (`--metadata-service-directory-name`), or both. You can also add or update either flag on an existing catalog by running `gcloud biglake iceberg catalogs update`.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="snowflake" \
        --secret-name="projects/PROJECT_ID/locations/REGION/secrets/SNOWFLAKE_SECRET_NAME" \
        --snowflake-account-identifier="SNOWFLAKE_ACCOUNT_IDENTIFIER" \
        --snowflake-warehouse="SNOWFLAKE_WAREHOUSE" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE" \
        --service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME" \
        --metadata-service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/METADATA_SERVICE_DIRECTORY_NAMESPACE/services/METADATA_SERVICE_NAME"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: a name for your federated catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Lakehouse region where the federated catalog is created. This must be the same region as the Service Directory namespace and regional secret. To minimize latency: 
    * If your Snowflake Horizon Catalog is on AWS, select the Google Cloud region closest to your AWS region.
    * If your Snowflake Horizon Catalog is on Azure, select the Google Cloud region closest to your Azure region.
    * If your Snowflake Horizon Catalog is on Google Cloud, select the exact same region.
  * `SNOWFLAKE_SECRET_NAME`: the name of your Snowflake secret.
  * `SNOWFLAKE_ACCOUNT_IDENTIFIER`: your Snowflake account identifier (for example, `myorg-myaccount`). If you specify `--metadata-service-directory-name` to synchronize metadata over PrivateLink or Private Link, use your `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`).
  * `SNOWFLAKE_WAREHOUSE`: the Snowflake warehouse that you want to federate with. This is also known as the database name in Snowflake Horizon Catalog.
  * `REFRESH_INTERVAL`: Optional: Specifies how often background metadata refresh runs. Set this value as a duration, for example, `330s` or `5m30s`.
  * `NAMESPACE_FILTERS`: Optional: a comma-separated list of namespaces to federate. For example, `ns1,ns2`. If omitted, Lakehouse includes all namespaces.
  * `CROSS_CLOUD_CACHE_MODE`: Optional: whether to enable cross-cloud caching on the federated catalog (`enabled` or `disabled`). Defaults to `disabled`. When set to `enabled`, Lakehouse caches remote files in the catalog's Google Cloud region. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).
  * If you are using a private interconnect (Cross-Cloud Interconnect), specify either or both of the following Service Directory references (omit either flag if you aren't routing that traffic layer over Cross-Cloud Interconnect): 
    * `SERVICE_DIRECTORY_NAMESPACE` and `SERVICE_NAME`: the Service Directory namespace and service name that you created for private query transport to remote object storage.
    * `METADATA_SERVICE_DIRECTORY_NAMESPACE` and `METADATA_SERVICE_NAME`: the Service Directory namespace and service name that you created for private background metadata refresh.



###  Workload Identity Federation 

If you use Workload Identity Federation, you must specify `--snowflake-role`.

#### Public internet (no CCI)

If you don't configure Cross-Cloud Interconnect, connections travel over the public internet using TLS.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="snowflake" \
        --snowflake-account-identifier="SNOWFLAKE_ACCOUNT_IDENTIFIER" \
        --snowflake-warehouse="SNOWFLAKE_WAREHOUSE" \
        --snowflake-role="SNOWFLAKE_ROLE" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE"

#### Customer-owned (CCI)

If you configured a private interconnect (Dedicated or Partner Cross-Cloud Interconnect), provide the Service Directory service reference for private query transport (`--service-directory-name`), private background metadata refresh (`--metadata-service-directory-name`), or both. You can also add or update either flag on an existing catalog by running `gcloud biglake iceberg catalogs update`.
    
    
    gcloud biglake iceberg catalogs create FEDERATED_CATALOG_NAME \
        --project="PROJECT_ID" \
        --primary-location="REGION" \
        --catalog-type="federated" \
        --federated-catalog-type="snowflake" \
        --snowflake-account-identifier="SNOWFLAKE_ACCOUNT_IDENTIFIER" \
        --snowflake-warehouse="SNOWFLAKE_WAREHOUSE" \
        --snowflake-role="SNOWFLAKE_ROLE" \
        --refresh-interval="REFRESH_INTERVAL" \
        --namespace-filters="NAMESPACE_FILTERS" \
        --cross-cloud-cache="CROSS_CLOUD_CACHE_MODE" \
        --service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/SERVICE_DIRECTORY_NAMESPACE/services/SERVICE_NAME" \
        --metadata-service-directory-name="projects/PROJECT_ID/locations/REGION/namespaces/METADATA_SERVICE_DIRECTORY_NAMESPACE/services/METADATA_SERVICE_NAME"

Replace the following:

  * `FEDERATED_CATALOG_NAME`: a name for your federated catalog.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Lakehouse region where the federated catalog is created. This must be the same region as the Service Directory namespace and regional secret. To minimize latency: 
    * If your Snowflake Horizon Catalog is on AWS, select the Google Cloud region closest to your AWS region.
    * If your Snowflake Horizon Catalog is on Azure, select the Google Cloud region closest to your Azure region.
    * If your Snowflake Horizon Catalog is on Google Cloud, select the exact same region.
  * `SNOWFLAKE_ACCOUNT_IDENTIFIER`: your Snowflake account identifier (for example, `myorg-myaccount`). If you specify `--metadata-service-directory-name` to synchronize metadata over PrivateLink or Private Link, use your `.privatelink` account identifier (for example, `myorg-myaccount.privatelink`).
  * `SNOWFLAKE_WAREHOUSE`: the Snowflake warehouse that you want to federate with. This is also known as the database name in Snowflake Horizon Catalog.
  * `SNOWFLAKE_ROLE`: the specific Snowflake role required for the session. For example, `ICEBERG_VIEW`.
  * `REFRESH_INTERVAL`: Specifies how often background metadata refresh runs. Set this value as a duration, for example, `330s` or `5m30s`.
  * `NAMESPACE_FILTERS`: Optional: a comma-separated list of namespaces to federate. For example, `ns1,ns2`. If omitted, Lakehouse includes all namespaces.
  * `CROSS_CLOUD_CACHE_MODE`: Optional: whether to enable cross-cloud caching on the federated catalog (`enabled` or `disabled`). Defaults to `disabled`. When set to `enabled`, Lakehouse caches remote files in the catalog's Google Cloud region. For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching).
  * If you are using a private interconnect (Cross-Cloud Interconnect), specify either or both of the following Service Directory references (omit either flag if you aren't routing that traffic layer over Cross-Cloud Interconnect): 
    * `SERVICE_DIRECTORY_NAMESPACE` and `SERVICE_NAME`: the Service Directory namespace and service name that you created for private query transport to remote object storage.
    * `METADATA_SERVICE_DIRECTORY_NAMESPACE` and `METADATA_SERVICE_NAME`: the Service Directory namespace and service name that you created for private background metadata refresh.



### Complete authentication setup

Complete the authentication process using your chosen authentication type.

###  Secret-based (PAT) 

When the catalog is created, Lakehouse provisions a unique service account for it (returned as `biglake-service-account` in the resource description).

You must grant this service account permission to access the secret you created earlier. Note that propagating IAM policies can take a few minutes.

Grant the federated catalog's service account permission to access the secret:
    
    
    gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
    gcloud secrets add-iam-policy-binding SNOWFLAKE_SECRET_NAME \
      --project="PROJECT_ID" \
      --location="REGION" \
      --member="serviceAccount:$(gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
          --project="PROJECT_ID" \
          --format='value(biglake-service-account)')" \
      --role="roles/secretmanager.secretAccessor"

To verify that the federated catalog service account has access to the secret, run the following command:
    
    
    gcloud config set api_endpoint_overrides/secretmanager https://secretmanager.REGION.rep.googleapis.com/
    gcloud secrets get-iam-policy SNOWFLAKE_SECRET_NAME \
        --project="PROJECT_ID" \
        --location="REGION"

In the output, verify that the `biglake-service-account` service account has the `roles/secretmanager.secretAccessor` role assigned to it.

###  Workload Identity Federation 

After creating the catalog, you must link its service account identity to a service user in Snowflake.

  1. Extract the **Lakehouse Service Account ID** (Subject) from the catalog details.

You can get this from the JSON response of the creation command (field `biglake-service-account-id`).

Alternatively, you can run the describe command on the catalog to get the value:
         
         gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID"

Look for the `biglake-service-account-id` in the output.

  2. Log into your Snowflake management instance and execute the following script to establish the trust relationship with the Lakehouse service identity:
         
         USE ROLE ACCOUNTADMIN;
         
         CREATE USER SNOWFLAKE_SERVICE_USER
           TYPE = SERVICE
           WORKLOAD_IDENTITY = (
             TYPE = GCP
             SUBJECT = 'LAKEHOUSE_SERVICE_ACCOUNT_ID'
           )
           DEFAULT_ROLE = SNOWFLAKE_ROLE
           COMMENT = 'Service user for Lakehouse cross-cloud access';
         
         -- Also explicitly GRANT permissions to the role
         GRANT ROLE SNOWFLAKE_ROLE TO USER SNOWFLAKE_SERVICE_USER;

Replace the following:

     * `SNOWFLAKE_SERVICE_USER`: a name for the new service user in Snowflake.
     * `LAKEHOUSE_SERVICE_ACCOUNT_ID`: the service account ID extracted in the previous step.
     * `SNOWFLAKE_ROLE`: the Snowflake role (must match the role specified during catalog creation).



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

Verify that the catalog background metadata refresh cycle completed successfully and namespaces and tables are synchronized.

  1. Verify that the refresh status indicates success:
         
         gcloud biglake iceberg catalogs describe FEDERATED_CATALOG_NAME \
           --project="PROJECT_ID"

  2. Confirm that the namespaces are synchronized:
         
         gcloud biglake iceberg namespaces list \
           --project="PROJECT_ID" \
           --catalog="FEDERATED_CATALOG_NAME"

  3. Confirm that the tables in a namespace are synchronized:
         
         gcloud biglake iceberg tables list \
           --project="PROJECT_ID" \
           --catalog="FEDERATED_CATALOG_NAME" \
           --namespace="NAMESPACE_ID"




## What's next

  * [Query remote data](https://docs.cloud.google.com/lakehouse/docs/query-remote-data).
  * [Use VPC Service Controls with federated catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-federated-catalogs).
  * [Troubleshoot cross-cloud data access for Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access#snowflake-issues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
