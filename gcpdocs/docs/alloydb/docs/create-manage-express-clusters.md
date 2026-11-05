---
url: https://docs.cloud.google.com/alloydb/docs/create-manage-express-clusters/
title: Create and manage AlloyDB Express clusters \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:18:44.070751+00:00
---

# Create and manage AlloyDB Express clusters  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/create-manage-express-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create and manage AlloyDB Express clusters Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create, connect to, edit, view, delete, and upgrade AlloyDB Express clusters and instances.

For more information about how AlloyDB Express capabilities differ from AlloyDB capabilities, see [AlloyDB Express overview](https://docs.cloud.google.com/alloydb/docs/express-overview). To create an AlloyDB cluster instead, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

## Before you begin

Before you create or manage AlloyDB Express clusters, complete the following prerequisites:

  * Enable the AlloyDB API and other required APIs in your Google Cloud project so that your project is [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin).
  * If you use the [AlloyDB remote MCP server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp), [configure your MCP client](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp#configure-client) to connect to either the global MCP server endpoint (`https://alloydb.googleapis.com/mcp`) or a regional endpoint (`https://alloydb.REGION_ID.rep.googleapis.com/mcp`). Regional endpoints are currently in Preview.



### Required roles

To get the permissions that you need to create and manage AlloyDB Express clusters and instances, ask your administrator to grant you the following IAM roles on your project: 

  * [AlloyDB Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)
  * [Owner ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * [Editor ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * Use the AlloyDB remote MCP server: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an AlloyDB Express cluster and instance

You can create an AlloyDB Express cluster and its primary instance using the Google Cloud console, the Google Cloud CLI, the AlloyDB REST API, or the [AlloyDB remote MCP server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp).

An AlloyDB Express cluster supports PostgreSQL 18 and contains a single zonal primary instance that starts with 1 vCPU (4 GB RAM) and scales storage automatically up to 20 GB. If you plan to upgrade a 1 vCPU instance in place to AlloyDB later without resizing to 2 vCPUs, create your cluster in a region that also supports the [C4A machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).

Default connectivity settings depend on the tool that you use:

  * Google Cloud console: enables both public DNS on the primary instance and Private Service Connect on the cluster by default. You can configure Private Service Connect consumer Google Cloud projects later by editing the instance's connectivity settings.

  * gcloud CLI, REST API, and AlloyDB remote MCP server: enables only Private Service Connect on the cluster by default. When you create the primary instance, enable public DNS if you want to connect over public DNS, and allowlist consumer Google Cloud projects where you want to create Private Service Connect endpoints for the instance.




###  Console 

  1. In the Google Cloud console, go to the **Get started** page.

[Go to Get started](https://console.cloud.google.com/alloydb/get-started)

If your Google Cloud project already has clusters and you start from the **Clusters** page instead, click **Create cluster** in the toolbar to open the **Select configuration** page. Both pages display preset cluster configuration cards (**AlloyDB Express** , **Production (single zone)** , and **Production (multi-zone)**).

  2. In the **AlloyDB Express** card, click **Create cluster** to open the **Create an AlloyDB Express cluster** pane.

  3. In the **Create an AlloyDB Express cluster** pane, configure your cluster:

     * For **Cluster ID** , enter an ID for your cluster, or keep the default ID.
     * For **Password** , enter a password for the default `postgres` user, or click **Generate** to generate a password. You can [change the password](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles#change-password) later from the **Users** page.
     * For **Region** , select a [supported region](https://docs.cloud.google.com/alloydb/docs/express-overview#supported-regions) for your cluster. If you plan to upgrade a 1 vCPU instance to AlloyDB later without resizing to 2 vCPUs, select a region that supports the [C4A machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).
  4. Click **Create cluster**.

The Google Cloud console creates your AlloyDB Express cluster and its 1 vCPU primary instance with both Private Service Connect and public DNS enabled by default, and then opens AlloyDB Studio so you can query your database.

You can't change connectivity settings during cluster creation in the Google Cloud console, but you can update authorized external networks or Private Service Connect settings later by editing the instance's connectivity settings.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. To create an AlloyDB Express cluster, run the [`gcloud beta alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/create) command with the `--enable-express` flag:
         
         gcloud beta alloydb clusters create CLUSTER_ID \
             --region=REGION_ID \
             --password=PASSWORD \
             --enable-express \
             --project=PROJECT_ID
         

Replace the following:

     * `CLUSTER_ID`: the ID of the cluster that you want to create. The ID must start with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
     * `REGION_ID`: the [supported region](https://docs.cloud.google.com/alloydb/docs/express-overview#supported-regions) where you want to create the cluster. If you plan to upgrade a 1 vCPU instance to AlloyDB later without resizing to 2 vCPUs, choose a region that also supports the [C4A machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).
     * `PASSWORD`: the initial password for the default `postgres` database user.
     * `PROJECT_ID`: the ID of the Google Cloud project where you want to create the cluster.
**Note:** By default, creating an AlloyDB Express cluster in the gcloud CLI enables Private Service Connect for private connectivity from a Virtual Private Cloud (VPC) network, while public DNS is enabled at the instance level in the next step. To make Private Service Connect reachable, you must allowlist consumer Google Cloud projects using `--allowed-psc-projects` when you create or update the primary instance.
  2. To create the primary instance in your AlloyDB Express cluster, run the [`gcloud beta alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/create) command and choose your connectivity flags:

     * Public DNS only: specify `--enable-public-dns` and omit `--allowed-psc-projects`.
     * Private Service Connect only: omit `--enable-public-dns` and specify `--allowed-psc-projects=ALLOWED_PROJECT_ID` to allow Private Service Connect connections from your consumer Google Cloud project.
     * Both public DNS and Private Service Connect: specify both `--enable-public-dns` and `--allowed-psc-projects=ALLOWED_PROJECT_ID`.
    
    gcloud beta alloydb instances create INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --instance-type=PRIMARY \
        --cpu-count=1 \
        --enable-public-dns \
        --allowed-psc-projects=ALLOWED_PROJECT_ID \
        --project=PROJECT_ID
    

Replace the following:

     * `INSTANCE_ID`: the ID of the primary instance that you want to create.
     * `ALLOWED_PROJECT_ID` (Optional): a comma-separated list of Google Cloud project IDs or project numbers allowed to create Private Service Connect endpoints to this instance. Omit `--allowed-psc-projects` if you're configuring public DNS only.
**Note:** AlloyDB Express clusters support only zonal availability (`--availability-type=ZONAL`). You must create the primary instance with a CPU count of `1` (1 vCPU, 4 GB RAM). Specifying any value other than `1` fails. If needed, you can update the instance to `2` (2 vCPUs, 8 GB RAM) after creation.



###  REST 

  1. To create an AlloyDB Express cluster, send a `POST` request to the [`projects.locations.clusters.create`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters/create) endpoint with `expressConfig.enabled` set to `true`.

Before using any of the request data, make the following replacements:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `REGION_ID`: the [supported region](https://docs.cloud.google.com/alloydb/docs/express-overview#supported-regions) where you want to create the cluster. If you plan to upgrade a 1 vCPU instance to AlloyDB later without resizing to 2 vCPUs, choose a region that also supports the [C4A machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).
     * `CLUSTER_ID`: the ID of the cluster that you want to create.
     * `INITIAL_USERNAME`: the username for the initial database user (for example, `postgres`).
     * `INITIAL_USER_PASSWORD`: the password for the initial database user.

HTTP method and URL:
    
    POST https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters?clusterId=CLUSTER_ID
    

Request JSON body:
    
    {
      "databaseVersion": "POSTGRES_18",
      "expressConfig": {
        "enabled": true
      },
      "initialUser": {
        "user": "INITIAL_USERNAME",
        "password": "INITIAL_USER_PASSWORD"
      }
    }
    

  2. After the cluster creation operation completes, create the primary instance by sending a `POST` request to the [`projects.locations.clusters.instances.create`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/create) endpoint with `machineConfig.cpuCount` set to `1` (specifying any value other than `1` fails on creation). Choose your connectivity fields in the request body:

     * Public DNS only: set `"networkConfig": {"publicDnsEnabled": true}` and omit `"pscInstanceConfig"`.
     * Private Service Connect only: omit `"publicDnsEnabled"` (which defaults to `false`) and set `"pscInstanceConfig": {"allowedConsumerProjects": ["ALLOWED_PROJECT_ID"]}`.
     * Both public DNS and Private Service Connect: include both `"networkConfig": {"publicDnsEnabled": true}` and `"pscInstanceConfig": {"allowedConsumerProjects": ["ALLOWED_PROJECT_ID"]}`.

Before using any of the request data, make the following replacements:

     * `INSTANCE_ID`: the ID of the primary instance that you want to create.
     * `ALLOWED_PROJECT_ID` (Optional): the Google Cloud project IDs or project numbers allowed to create Private Service Connect endpoints to this instance.

HTTP method and URL:
    
    POST https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances?instanceId=INSTANCE_ID
    

Request JSON body:
    
    {
      "instanceType": "PRIMARY",
      "availabilityType": "ZONAL",
      "machineConfig": {
        "cpuCount": 1
      },
      "networkConfig": {
        "publicDnsEnabled": true
      },
      "pscInstanceConfig": {
        "allowedConsumerProjects": [
          "ALLOWED_PROJECT_ID"
        ]
      }
    }
    




###  MCP 

You can use an MCP client or call the [AlloyDB remote MCP server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp) directly to create an AlloyDB Express cluster and its primary instance.

In an MCP client, you can use a single prompt to create both the AlloyDB Express cluster and its primary instance. Your MCP client automatically calls `create_cluster`, polls `get_operation`, and calls `create_instance`:
    
    
    Create an AlloyDB Express cluster named CLUSTER_ID in REGION_ID with a primary instance named INSTANCE_ID.
    

To run each step individually or call the MCP tools directly, follow these steps:

  1. To create an AlloyDB Express cluster, enter a prompt in your MCP client or call the [`create_cluster`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_cluster) MCP tool with `express_config.enabled` set to `true`.

Before using any of the request data, make the following replacements:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `REGION_ID`: the [supported region](https://docs.cloud.google.com/alloydb/docs/express-overview#supported-regions) where you want to create the cluster. If you plan to upgrade a 1 vCPU instance to AlloyDB later without resizing to 2 vCPUs, choose a region that also supports the [C4A machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).

     * `CLUSTER_ID`: the ID of the cluster that you want to create.

In your MCP client, you can enter a prompt similar to the following:
    
    Create an AlloyDB Express cluster named CLUSTER_ID in REGION_ID.
    

Tool call parameters:
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "create_cluster",
        "arguments": {
          "parent": "projects/PROJECT_ID/locations/REGION_ID",
          "cluster_id": "CLUSTER_ID",
          "express_config": {
            "enabled": true
          }
        }
      }
    }
    

**Note:** By default, creating an AlloyDB Express cluster using `create_cluster` enables Private Service Connect (`"psc_enabled": true`), while public DNS is enabled at the instance level. AlloyDB Express clusters don't support VPC peering using the `network` field.

To make Private Service Connect reachable from a VPC network, allowlist consumer Google Cloud projects in `"psc_instance_config"` when you create or update the primary instance.

  2. The `create_cluster` tool returns a long-running operation. Poll the status of the operation using the [`get_operation`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/get_operation) MCP tool until `done` is `true` and the cluster is in the `READY` state.

  3. To create the primary instance in your AlloyDB Express cluster, enter a prompt in your MCP client or call the [`create_instance`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/create_instance) MCP tool. Choose your connectivity settings:

     * Public DNS only: set `"public_dns_enabled": true` and omit `"psc_instance_config"`.

     * Private Service Connect only: omit `"public_dns_enabled"` (which defaults to `false`) and set `"psc_instance_config"` with `"allowed_consumer_projects"` (or `"psc_auto_connections"` specifying `"consumer_project"` and `"consumer_network"`).

     * Both public DNS and Private Service Connect: set both `"public_dns_enabled": true` and `"psc_instance_config"`.

Before using any of the request data, make the following replacements:

     * `INSTANCE_ID`: the ID of the primary instance that you want to create.

     * `ALLOWED_PROJECT_ID`: optional: the Google Cloud project IDs or project numbers allowed to create Private Service Connect endpoints to this instance.

In your MCP client, you can enter a prompt similar to the following:
    
    Please create a primary instance named INSTANCE_ID in my AlloyDB Express cluster CLUSTER_ID.
    

Tool call parameters:
    
    {
      "jsonrpc": "2.0",
      "id": 2,
      "method": "tools/call",
      "params": {
        "name": "create_instance",
        "arguments": {
          "parent": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID",
          "instance_id": "INSTANCE_ID",
          "type": "PRIMARY",
          "public_dns_enabled": true,
          "psc_instance_config": {
            "allowed_consumer_projects": [
              "ALLOWED_PROJECT_ID"
            ]
          }
        }
      }
    }
    

**Note:** For AlloyDB Express clusters, if you omit `cpu_count` and `machine_type`, `create_instance` uses the default AlloyDB Express machine configuration (`1` vCPU and `4` GB of RAM). Specifying a `cpu_count` other than `1` when creating an AlloyDB Express primary instance fails. In `create_instance`, `public_dns_enabled` defaults to `false` if omitted, and the tool enables Data API access (`data_api_access: ENABLED`) and IAM database authentication (`db_iam_authentication: true`) automatically.
  4. Poll the instance creation operation using the [`get_operation`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/get_operation) MCP tool until `done` is `true` and the instance is in the `READY` state.




## Connect to an AlloyDB Express instance

AlloyDB Express supports the following inbound database connectivity options:

  * Public DNS (default): provides a publicly routable DNS name (`networkInfo.publicDnsName`) so you can connect from clients outside of a VPC network.
  * Private Service Connect: lets you connect privately to your instance from within your VPC network through Private Service Connect endpoints without exposing your database to the public internet.

**Note:** To run SQL queries directly in the Google Cloud console without configuring local clients or network rules, use [AlloyDB Studio](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect). AI agents and MCP clients can also run SQL queries using the [`execute_sql`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/execute_sql) and [`execute_sql_read_only`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/execute_sql_read_only) tools on the [AlloyDB remote MCP server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp#execute-sql).

### Connect over public DNS

When you connect over public DNS from outside a VPC network, you can do one of the following:

  * Connect directly using a PostgreSQL client (such as `psql`): requires allowlisting your client IP addresses in authorized external networks first.
  * Connect using the gcloud CLI or the Auth Proxy, or use the [AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors): encrypts traffic automatically and doesn't require configuring authorized external networks.



#### Connect directly using a PostgreSQL client

By default, the public DNS endpoint rejects all direct client IP addresses. You must allowlist your client CIDR blocks before you connect directly with `psql`.

  1. Configure authorized external networks on your primary instance.

You can't add or remove authorized external networks individually. Each update overwrites the existing list. Provide a comma-separated list of all CIDR blocks that you want to allow.

###  Console 

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. In the **Resource name** column, click the name of your AlloyDB Express cluster.

     3. On the **Overview** page, go to **Instances in your cluster** , locate your primary instance, and click more_vert **Instance actions > Edit** (or go to **Connectivity** in the navigation menu and click **Edit**).

     4. Under **Connectivity** , ensure public connectivity is enabled.

     5. Under **Authorized external networks** , enter a comma-separated list of IPv4 CIDR ranges (for example, `203.0.113.0/24`), or click **Use my IP** to add the `/32` IPv4 address of your current machine.

     6. Click **Update instance**.

###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Run the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--authorized-external-networks` flag:
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --authorized-external-networks=CIDR_RANGE1,CIDR_RANGE2 \
        --project=PROJECT_ID
    

Replace the following:

     * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
     * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
     * `REGION_ID`: the region where your cluster is located.
     * `CIDR_RANGE1`, `CIDR_RANGE2`: a comma-separated list of IPv4 address ranges in CIDR notation (for example, `203.0.113.0/24`).
     * `PROJECT_ID`: the ID of your Google Cloud project.

###  REST 

Send a `PATCH` request to the [`projects.locations.clusters.instances.patch`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch) endpoint with `updateMask=networkConfig.authorizedExternalNetworks`.

Before using any of the request data, make the following replacements:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `REGION_ID`: the region where your cluster is located.
     * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
     * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
     * `CIDR_RANGE1`, `CIDR_RANGE2`: IPv4 address ranges in CIDR notation (for example, `203.0.113.0/24`).

HTTP method and URL:
    
    PATCH https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID?updateMask=networkConfig.authorizedExternalNetworks
    

Request JSON body:
    
    {
      "networkConfig": {
        "authorizedExternalNetworks": [
          {
            "cidrRange": "CIDR_RANGE1"
          },
          {
            "cidrRange": "CIDR_RANGE2"
          }
        ]
      }
    }
    

###  MCP 

Enter a prompt in your MCP client or call the [`update_instance`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/update_instance) MCP tool with the `authorized_external_networks` field.

Before using any of the request data, make the following replacements:

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `REGION_ID`: the region where your cluster is located.

     * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.

     * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.

     * `CIDR_RANGE1`, `CIDR_RANGE2`: IPv4 address ranges in CIDR notation, such as `203.0.113.0/24`.

In your MCP client, you can enter a prompt similar to the following:
    
    Please update the AlloyDB instance INSTANCE_ID in cluster CLUSTER_ID to allow external connections from CIDR_RANGE1.
    

Tool call parameters:
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "update_instance",
        "arguments": {
          "instance": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID",
          "authorized_external_networks": [
            "CIDR_RANGE1",
            "CIDR_RANGE2"
          ]
        }
      }
    }
    

  2. Retrieve your instance's public DNS name:

###  Console 

     1. In the Google Cloud console, go to the **Clusters** page and click your AlloyDB Express cluster name.
     2. Go to **Connectivity** (or view the primary instance card on the **Overview** page) and copy the instance's public DNS name.

###  gcloud 

Run the [`gcloud beta alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/describe) command to retrieve the `networkInfo.publicDnsName` value:
    
    gcloud beta alloydb instances describe INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --format="value(networkInfo.publicDnsName)" \
        --project=PROJECT_ID
    

The output uses the following format:
    
    IDENTIFIER.IDENTIFIER.REGION_ID.alloydb.s.cloud.goog
    

In this output, `IDENTIFIER` is a system-generated alphanumeric identifier.

###  REST 

Send a `GET` request to the [`projects.locations.clusters.instances.get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/get) endpoint and read the `networkInfo.publicDnsName` field from the response:
    
    GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
    

###  MCP 

Enter a prompt in your MCP client or call the [`get_instance`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/get_instance) MCP tool and read the `networkInfo.publicDnsName` field from the response.

In your MCP client, you can enter a prompt similar to the following:
    
    Please get the public DNS name of the AlloyDB instance INSTANCE_ID in cluster CLUSTER_ID.
    

Tool call parameters:
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "get_instance",
        "arguments": {
          "name": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID"
        }
      }
    }
    

  3. Connect to your database using a standard PostgreSQL connection URI and your instance's public DNS name:
         
         psql postgresql://USERNAME@PUBLIC_DNS_NAME/DATABASE_NAME

Replace the following:

     * `USERNAME`: the PostgreSQL database username (for example, `postgres`).
     * `PUBLIC_DNS_NAME`: the public DNS name of your AlloyDB Express instance (for example, `1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d.a.us-central1.alloydb.s.cloud.goog`).
     * `DATABASE_NAME`: the name of the database to connect to (the default database is `postgres`).
  4. When prompted, enter the password for the database user.




#### Connect using gcloud CLI or the Auth Proxy

To connect over public DNS without configuring authorized external networks, you can use either the [`gcloud beta alloydb connect`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/connect) command or the standalone Auth Proxy client (`alloydb-auth-proxy`) with the `--public-ip` flag. Although AlloyDB Express displays a public DNS name rather than a public IP address, the control plane provisions an underlying public connection for the instance that the Auth Proxy resolves automatically when you specify `--public-ip`.

To start a local Auth Proxy instance and open a `psql` session using the gcloud CLI, run the `gcloud beta alloydb connect` command with the `--public-ip` flag:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --public-ip \
        --user=USERNAME \
        --database=DATABASE_NAME \
        --project=PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `REGION_ID`: the region where your cluster is located.
  * `USERNAME`: the database username (defaults to `postgres`).
  * `DATABASE_NAME`: the database name (defaults to `postgres`).
  * `PROJECT_ID`: the ID of your Google Cloud project.



For more information about connecting with the gcloud CLI, including IAM database authentication (`--auto-iam-authn`), see [Connect using gcloud CLI](https://docs.cloud.google.com/alloydb/docs/connect-gcloud).

Alternatively, you can download and run the standalone Auth Proxy client with the `--public-ip` flag:
    
    
    ./alloydb-auth-proxy \
        "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID" \
        --public-ip

For information about downloading, configuring, and connecting through the standalone Auth Proxy client, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).

### Connect over Private Service Connect

For private connectivity from within your VPC network without exposing your database to the public internet, you can configure Private Service Connect on your AlloyDB Express instance. You can connect to a Private Service Connect endpoint either directly from a client inside your VPC network or using the Auth Proxy. For more information about connecting to Private Service Connect, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect).

When following those instructions for AlloyDB Express, create your cluster and 1 vCPU zonal primary instance as described in Create an AlloyDB Express cluster and instance with Private Service Connect enabled; AlloyDB Express supports inbound Private Service Connect connectivity to a single zonal primary instance.

## Edit an AlloyDB Express instance

You can update the CPU count (1 vCPU or 2 vCPUs) or database flags of an AlloyDB Express primary instance.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource name** column, click the name of your AlloyDB Express cluster.

  3. On the **Overview** page, in the **Instances in your cluster** section, locate your primary instance and click **Edit primary** (or click more_vert **Instance actions > Edit**).

  4. On the **Edit primary instance** page, update the instance settings:

     * Under **Machine** , in the **Machine Type** list, select **1 vCPU, 4 GB** or **2 vCPU, 8 GB**.
     * Optional: To configure database flags, expand **Flags** (or click **Show advanced options** and expand **Flags**) and click **Add flag**. Select a flag from the **New database flag** list, provide a value, and click **Done**.
  5. Click **Update instance**.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To scale the instance by changing its CPU count (`1` or `2`) or to update its database flags, run the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --cpu-count=CPU_COUNT \
        --database-flags=FLAGS \
        --project=PROJECT_ID
    

Replace the following:

  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `REGION_ID`: the region where your cluster is located.
  * `CPU_COUNT`: the number of vCPUs for the instance (`1` for 1 vCPU, 4 GB RAM or `2` for 2 vCPUs, 8 GB RAM).
  * `FLAGS` (Optional): a comma-separated list of database flags and values in the `FLAG_NAME=VALUE` format. If you're only updating the CPU count, omit the `--database-flags` flag. For more information about supported flags, see [Supported database flags](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).
  * `PROJECT_ID`: the ID of your Google Cloud project.

**Note:** To update network connectivity settings for an AlloyDB Express primary instance, you can use the following flags:

  * `--enable-public-dns` or `--no-enable-public-dns`: enables or disables public DNS for the instance. This flag is available only in `gcloud beta` ([`gcloud beta alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/update)).
  * `--allowed-psc-projects=[ALLOWED_PSC_PROJECTS,...]`: updates the comma-separated list of consumer Google Cloud project IDs or project numbers allowed to create Private Service Connect endpoints to the instance.



###  REST 

To update the CPU count or database flags of an AlloyDB Express primary instance, send a `PATCH` request to the [`projects.locations.clusters.instances.patch`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch) endpoint and specify the fields that you're updating in the `updateMask` query parameter.

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION_ID`: the region where your cluster is located.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
  * `CPU_COUNT`: the number of vCPUs for the instance (`1` or `2`).
  * `FLAG_NAME` and `FLAG_VALUE` (Optional): the database flag name and value to set. If you're only updating the CPU count, set `updateMask=machineConfig.cpuCount` and omit `databaseFlags` from the request body.



HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID?updateMask=machineConfig.cpuCount,databaseFlags
    

Request JSON body:
    
    
    {
      "machineConfig": {
        "cpuCount": CPU_COUNT
      },
      "databaseFlags": {
        "FLAG_NAME": "FLAG_VALUE"
      }
    }
    

###  MCP 

To update the CPU count or database flags of an AlloyDB Express primary instance, enter a prompt in your MCP client or call the [`update_instance`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/update_instance) MCP tool.

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.

  * `REGION_ID`: the region where your cluster is located.

  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.

  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.

  * `CPU_COUNT`: the number of vCPUs for the instance (`1` or `2`).

  * `FLAG_NAME` and `FLAG_VALUE`: optional: the database flag name and value to set. If you're only updating the CPU count, omit `database_flags` from `arguments`.




In your MCP client, you can enter a prompt similar to the following:
    
    
    Please update the AlloyDB instance INSTANCE_ID in cluster CLUSTER_ID to CPU_COUNT vCPUs.
    

Tool call parameters:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/call",
      "params": {
        "name": "update_instance",
        "arguments": {
          "instance": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID",
          "cpu_count": CPU_COUNT,
          "database_flags": {
            "FLAG_NAME": "FLAG_VALUE"
          }
        }
      }
    }
    

## View AlloyDB Express cluster and instance details

You can view a list of your AlloyDB Express clusters, view details about a specific AlloyDB Express cluster or instance, and check your cluster's compute and storage usage.

For more information, see [View the list of clusters](https://docs.cloud.google.com/alloydb/docs/cluster-list), [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view), and [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view).

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

In the **Resource name** column, AlloyDB Express clusters display an bolt **Express** tag next to the cluster name.

  2. To view detailed information about a cluster and its primary instance, click the cluster name in the **Resource name** column.

  3. On the **Overview** page, view the cluster details under **Cluster details** (including the bolt **Express** tag next to **Cluster ID** and **Total storage used** out of the 20 GB limit) and the primary instance details under **Instances in your cluster**.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  * To view a list of clusters in your project, run the [`gcloud alloydb clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/list) command:
        
        gcloud alloydb clusters list --project=PROJECT_ID
        

  * To view details about a specific cluster, run the [`gcloud alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/describe) command:
        
        gcloud alloydb clusters describe CLUSTER_ID \
            --region=REGION_ID \
            --project=PROJECT_ID
        

  * To view details about a specific instance, run the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command:
        
        gcloud alloydb instances describe INSTANCE_ID \
            --cluster=CLUSTER_ID \
            --region=REGION_ID \
            --project=PROJECT_ID
        




Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `REGION_ID`: the region where your cluster is located.
  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.



###  REST 

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION_ID`: the region where your cluster is located.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.

  * To view a list of clusters in a region, send a `GET` request to the [`projects.locations.clusters.list`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters/list) endpoint:
        
        GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters
        

  * To view details about a cluster, send a `GET` request to the [`projects.locations.clusters.get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters/get) endpoint:
        
        GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID
        

  * To view details about an instance, send a `GET` request to the [`projects.locations.clusters.instances.get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/get) endpoint:
        
        GET https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
        




###  MCP 

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.

  * `REGION_ID`: the region where your cluster is located.

  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.

  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.

  * To view a list of clusters in a region, enter a prompt in your MCP client or call the [`list_clusters`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/list_clusters) MCP tool.

In your MCP client, you can enter a prompt similar to the following:
        
        Please list the AlloyDB clusters in REGION_ID in project PROJECT_ID.
        

Tool call parameters:
        
        {
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/call",
          "params": {
            "name": "list_clusters",
            "arguments": {
              "parent": "projects/PROJECT_ID/locations/REGION_ID"
            }
          }
        }
        

  * To view details about a cluster, enter a prompt in your MCP client or call the [`get_cluster`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/get_cluster) MCP tool.

In your MCP client, you can enter a prompt similar to the following:
        
        Please show the details of the AlloyDB cluster CLUSTER_ID in REGION_ID.
        

Tool call parameters:
        
        {
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/call",
          "params": {
            "name": "get_cluster",
            "arguments": {
              "name": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID"
            }
          }
        }
        

  * To view details about an instance, enter a prompt in your MCP client or call the [`get_instance`](https://docs.cloud.google.com/alloydb/docs/reference/mcp/alloydb/mcp/tools_list/get_instance) MCP tool.

In your MCP client, you can enter a prompt similar to the following:
        
        Please show the details of the AlloyDB instance INSTANCE_ID in cluster CLUSTER_ID.
        

Tool call parameters:
        
        {
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/call",
          "params": {
            "name": "get_instance",
            "arguments": {
              "name": "projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID"
            }
          }
        }
        




### View compute and storage usage

To check the storage and compute used by your AlloyDB Express cluster and primary instance, use the Google Cloud console or Cloud Monitoring:

  * In the Google Cloud console, open your cluster's **Overview** page:

    * Storage used: under **Cluster details** , view **Total storage used** to see how much storage your cluster is using out of the 20 GB limit.
    * Compute and connections: view the **CPU utilization** and **Active connections** charts on the **Overview** page, or click **System insights** in the navigation menu to view detailed CPU, memory, and storage metrics.
  * In [Cloud Monitoring Metrics Explorer](https://docs.cloud.google.com/alloydb/docs/monitor-instance), query the following metrics for the `alloydb.googleapis.com/Cluster` and `alloydb.googleapis.com/Instance` monitored resource types:

    * Storage used: `alloydb.googleapis.com/cluster/storage/usage`
    * CPU utilization: `alloydb.googleapis.com/instance/cpu/average_utilization` and `alloydb.googleapis.com/instance/cpu/maximum_utilization`
    * Active connections: `alloydb.googleapis.com/database/postgresql/backends`



## Delete an AlloyDB Express cluster or instance

You can delete an AlloyDB Express primary instance or cluster when you no longer need it.

For more information, see [Delete an instance](https://docs.cloud.google.com/alloydb/docs/instance-delete) and [Delete a cluster](https://docs.cloud.google.com/alloydb/docs/cluster-delete).

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource name** column, click the name of your AlloyDB Express cluster.

  3. On the **Overview** page, delete the primary instance or the cluster:

     * To delete the primary instance, go to the **Instances in your cluster** section, click more_vert **Instance actions > Delete**, enter the instance ID in the dialog, and click **Delete**.
     * To delete the cluster, first delete the primary instance in the cluster, and then click **Delete cluster** , enter your cluster ID in the **Delete cluster** dialog, and click **Delete**.
**Note:** You can't delete a cluster that contains an instance using the Google Cloud console. To delete a cluster and its primary instance in a single step, use the `--force` flag in the gcloud CLI or the `force=true` parameter in the REST API.



###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  * To delete an instance, run the [`gcloud alloydb instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/delete) command:
        
        gcloud alloydb instances delete INSTANCE_ID \
            --cluster=CLUSTER_ID \
            --region=REGION_ID \
            --project=PROJECT_ID
        

  * To delete a cluster, run the [`gcloud alloydb clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/delete) command. If the cluster still contains its primary instance, include the `--force` flag to delete the primary instance and the cluster together:
        
        gcloud alloydb clusters delete CLUSTER_ID \
            --region=REGION_ID \
            --force \
            --project=PROJECT_ID
        




Replace the following:

  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `REGION_ID`: the region where your cluster is located.
  * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST 

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION_ID`: the region where your cluster is located.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `INSTANCE_ID`: the ID of your AlloyDB Express primary instance.

  * To delete an instance, send a `DELETE` request to the [`projects.locations.clusters.instances.delete`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/delete) endpoint:
        
        DELETE https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID
        

  * To delete a cluster (including its primary instance when you specify `force=true`), send a `DELETE` request to the [`projects.locations.clusters.delete`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters/delete) endpoint:
        
        DELETE https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID?force=true
        




## Upgrade an AlloyDB Express cluster to AlloyDB

You can perform an in-place upgrade of your AlloyDB Express cluster to an AlloyDB cluster.

The upgrade preserves your database data, schemas, extensions, user credentials, networking configuration (including your public DNS name and Private Service Connect endpoints), and primary instance vCPU count.

The following list describes the resources and settings that change during the upgrade process:

  * CPU count, memory ratio, and compute capacity: your instance retains its current vCPU count (1 vCPU or 2 vCPUs) and upgrades from the AlloyDB Express 1:4 vCPU-to-memory ratio (4 GB or 8 GB RAM) to the AlloyDB 1:8 vCPU-to-memory ratio (8 GB RAM for 1 vCPU or 16 GB RAM for 2 vCPUs). After the upgrade, you can scale compute up to 288 vCPUs. 
    * When you upgrade a 1 vCPU instance, you are limited to regions that support the C4A machine series. For supported regions, see [Regional availability for C4A](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).
    * If your AlloyDB Express instance isn't in a region that supports C4A machine types, you must first update your primary instance to a 2 vCPU configuration before upgrading. In the Google Cloud console, if you click **Upgrade** for a 1 vCPU instance in an unsupported region, a message prompts you to resize your instance to 2 vCPUs first.
  * Provisioned compute and billing: the upgrade disables scale-to-zero compute, and your instance runs as an always-on AlloyDB instance billed at [AlloyDB rates](https://docs.cloud.google.com/alloydb/pricing).
  * Storage capacity: the upgrade removes the 20 GB storage limit. Storage scales up to a default quota of 16 TiB per cluster, and you can request a [storage quota increase](https://docs.cloud.google.com/alloydb/quotas#cluster-storage-quotas) to scale up to 128 TiB.
  * Enterprise features: the upgrade unlocks regional high availability (HA), which is covered by the 99.99% uptime service level agreement (SLA). It also unlocks read pool instances, cross-region replication, continuous backup and recovery, and automated and on-demand backups.

**Note:** You can't convert to CMEK as part of the upgrade.

To upgrade your AlloyDB Express cluster to an AlloyDB cluster, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource name** column, click the name of your AlloyDB Express cluster.

  3. On the **Overview** page, under **Cluster details** , locate **Cluster ID** , and then click **Upgrade**.

If your primary instance is a 1 vCPU instance in a region that doesn't support the C4A machine series, a message appears:

`Upgrading to AlloyDB requires a 2 vCPU instance in the REGION_ID region. Resize your instance to 2 vCPUs first.`

To resize your instance to 2 vCPUs, click **Edit instance**. After resizing your instance, click **Upgrade** again.

  4. In the **Upgrade from AlloyDB Express** pane, enter your **Cluster ID** to confirm the upgrade, and then click **Confirm**.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To upgrade your AlloyDB Express cluster to an AlloyDB cluster, run the [`gcloud beta alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/clusters/update) command with the `--no-enable-express` flag:
    
    
    gcloud beta alloydb clusters update CLUSTER_ID \
        --region=REGION_ID \
        --no-enable-express \
        --project=PROJECT_ID
    

Replace the following:

  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.
  * `REGION_ID`: the region where your cluster is located.
  * `PROJECT_ID`: the ID of your Google Cloud project.



If your primary instance is a 1 vCPU instance in a region that doesn't support the C4A machine series, the command fails with the following error:

`Upgrading to AlloyDB is not supported for 1-vCPU instances in location "REGION_ID". Please update the instance to use 2 vCPUs and try the upgrade again.`

To resolve this error, update your primary instance to 2 vCPUs (`--cpu-count=2`), and then run the upgrade command again.

###  REST 

To upgrade your AlloyDB Express cluster to an AlloyDB cluster, send a `PATCH` request to the [`projects.locations.clusters.patch`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters/patch) endpoint with `updateMask=expressConfig.enabled` and set `expressConfig.enabled` to `false`.

Before using any of the request data, make the following replacements:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION_ID`: the region where your cluster is located.
  * `CLUSTER_ID`: the ID of your AlloyDB Express cluster.



HTTP method and URL:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID?updateMask=expressConfig.enabled
    

Request JSON body:
    
    
    {
      "expressConfig": {
        "enabled": false
      }
    }
    

If your primary instance is a 1 vCPU instance in a region that doesn't support the C4A machine series, the request fails with the following error:

`Upgrading to AlloyDB is not supported for 1-vCPU instances in location "REGION_ID". Please update the instance to use 2 vCPUs and try the upgrade again.`

To resolve this error, update your primary instance to 2 vCPUs (`"machineConfig": {"cpuCount": 2}`), and then send the upgrade request again.

## What's next

  * [Learn more about AlloyDB Express](https://docs.cloud.google.com/alloydb/docs/express-overview)

  * [Use the AlloyDB remote MCP server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
