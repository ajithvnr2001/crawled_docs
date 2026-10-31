---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-vpc-custom-mcp-server/
title: Prerequisites to set up a custom MCP server data store with VPC connectivity \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:51:23.330080+00:00
---

# Prerequisites to set up a custom MCP server data store with VPC connectivity  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-vpc-custom-mcp-server/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Prerequisites to set up a custom MCP server data store with VPC connectivity Stay organized with collections  Save and categorize content based on your preferences. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_.**Key Term:** In the Model Context Protocol (MCP) specification, capabilities are called _tools_. In Gemini Enterprise data stores, these tools are referred to as _actions_. The two terms can be used interchangeably.

This page explains the prerequisites and network infrastructure required to route Gemini Enterprise traffic to a custom Model Context Protocol (MCP) server through your Virtual Private Cloud (VPC) network. Use this setup if your MCP server is privately hosted inside a VPC network, or if it's publicly hosted and requires requests from static IP addresses.

To try an end-to-end walkthrough using a sample application, see the [**Gemini Enterprise with Agent Gateway all-traffic VPC egress and Cloud NAT static IP to external MCP server**](https://codelabs.developers.google.com/agw-ge-egress-vpc-all-traffic) codelab.

## Overview

By default, Gemini Enterprise can't access resources hosted inside private networks. To let Gemini Enterprise securely communicate with private tools or actions in your infrastructure, you route traffic through the Egress Agent Gateway into your private VPC network.

This connectivity model supports the following deployment use cases:

  * **Private network hosting** : Your private MCP server runs inside a private VPC network and doesn't have a public IP address.
  * **Hybrid and multicloud connectivity** : Connects actions on your private MCP server deployed across multicloud or on-premises environments over hybrid networks.
  * **Static IP egress for public MCP servers** : Routes outbound traffic to a publicly hosted MCP server through your VPC network and Cloud NAT so that requests originate from reserved static external IPv4 addresses that your destination server can allow.

**Note:** Agent Gateway governs Gemini Enterprise egress exclusively for outbound query-time tool execution to custom MCP servers, action connectors, and agents. It doesn't proxy generative model inference calls, knowledge data store retrieval (RAG), built-in assistant tools, or connector ingestion jobs. Inbound traffic into Gemini Enterprise isn't supported.

You define this connectivity declaratively. An _agent connectivity template_ holds your egress configuration: which network attachment to use, which domains to resolve privately, and which traffic to route through your VPC network. The Egress Agent Gateway then references that template to reach your custom MCP server.

You create the following three resources:

  1. A Private Service Connect **network attachment** that Agent Gateway uses to deploy a Private Service Connect interface inside your VPC network for egress.
  2. An **agent connectivity template** that points to that network attachment and defines your DNS peering and egress routing behavior.
  3. An **Agent Gateway** that references the template and routes your app's outbound requests.



## Verify requirements and permissions

Before you provision network infrastructure, verify your project resources, APIs, and Identity and Access Management (IAM) permissions.

### Resource requirements

Ensure you have the following resources available in your Google Cloud environment. Depending on your use case, you need either a private MCP server or a public MCP server.

Required resource | Description  
---|---  
**Private VPC network** | A secure VPC network containing the infrastructure and workloads you want to connect to Gemini Enterprise.  
**Agent Gateway and connectivity template** | A regional Egress Agent Gateway in `us-central1` or `europe-west1` associated with an agent connectivity template. The connectivity template specifies the Private Service Connect interface network attachment, DNS peering settings, and VPC egress routing mode to connect to your VPC, letting Gemini Enterprise route outbound requests to your custom MCP server. For more information, see [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) and [Set up VPC connectivity for Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity).  
**TrustConfig**  
(Optional) | Optional. A Certificate Manager `TrustConfig` resource that defines custom root and intermediate CA trust stores (or certificates in an allowlist). You reference this resource in an agent connectivity template so Agent Gateway can validate outbound TLS connections to private MCP servers that use private CAs or self-signed certificates. For more information, see [TLS certificate requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity#tls-certificate-requirements).  
**Private MCP server**  
(For private hosting) | A server that implements the Model Context Protocol and hosts your internal actions or data. This server runs privately within your VPC network and uses the `StreamableHTTP` transport.   
  
If your private MCP server uses a private domain name (such as `mcp.cymbal.internal`), Google service agents resolve domain names through private DNS peering when granted the **DNS Peer** (`roles/dns.peer`) role and configured with `dnsPeeringConfig` in your agent connectivity template. For details, see Create an agent connectivity template.  
**Public MCP server**  
(For static IP egress) | A server that implements the MCP, is reachable over public endpoints using the `StreamableHTTP` transport, and requires requests to originate from static external IPv4 addresses: 

  * **Public Cloud DNS resolution** : Private Cloud DNS peering isn't required; the server resolves through standard public DNS.
  * **Gateway egress configuration** : In your agent connectivity template, set `vpcEgress` to `ALL_TRAFFIC` to route internet-bound requests through your VPC network over the Private Service Connect interface.
  * **Deterministic egress with Cloud NAT** : Configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) with reserved static external IPv4 addresses on the subnet assigned to your network attachment so the destination MCP server can allow requests from your source IP addresses.
  * **VPC route inheritance** : Traffic injected into your VPC network follows your VPC route table, such as a default internet gateway route (`0.0.0.0/0`) or a next-hop firewall appliance.

  
**Authentication server**  
(Optional) | Optional. An authentication server running inside your private VPC network if your private MCP server requires OAuth 2.0 authentication.  
  
### Enable required APIs

Enable the minimum required APIs in the Google Cloud project where you deploy Agent Gateway and your Gemini Enterprise app:

  * **Compute Engine API (`compute.googleapis.com`):** Provides core networking infrastructure, subnets, routing, and Private Service Connect network attachments.
  * **Network Connectivity API (`networkconnectivity.googleapis.com`):** Manages cross-project and Shared VPC network endpoints.
  * **Network Security API (`networksecurity.googleapis.com`):** Creates and enforces authorization policies (`authzPolicies`) for gateway traffic.
  * **Network Services API (`networkservices.googleapis.com`):** Manages Agent Gateway resources (`agentGateways`) and connectivity templates (`agentConnectivityTemplates`).
  * **Service Extensions API (`serviceextensions.googleapis.com`):** Creates and manages authorization extensions (`authzExtensions`) for Identity-Aware Proxy (IAP) delegated authorization.
  * **Identity and Access Management API (`iam.googleapis.com`):** Manages service accounts and IAM Unified Access Policies (UAPs) for agent identities.
  * **Identity-Aware Proxy API (`iap.googleapis.com`):** Authenticates and verifies agent, endpoint, and server traffic.
  * **Agent Registry API (`agentregistry.googleapis.com`):** Registers and manages agents, MCP servers, and tool endpoints governed by the gateway.
  * **Discovery Engine API (`discoveryengine.googleapis.com`):** Enables Gemini Enterprise data stores and connectors.



To enable the minimum required APIs, run the following command:
    
    
    gcloud services enable \
        compute.googleapis.com \
        networkconnectivity.googleapis.com \
        networksecurity.googleapis.com \
        networkservices.googleapis.com \
        serviceextensions.googleapis.com \
        iam.googleapis.com \
        iap.googleapis.com \
        agentregistry.googleapis.com \
        discoveryengine.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with the project ID where you deploy Agent Gateway.

Depending on your configuration, you might also need to enable optional APIs:

  * **Cloud DNS API (`dns.googleapis.com`):** Required only if you configure DNS peering for private domain resolution.
  * **Certificate Manager API (`certificatemanager.googleapis.com`):** Required only if you configure custom TLS trust anchors (`TrustConfig`) when connecting to private backends that use private CAs or self-signed certificates.



### Verify required IAM roles

To configure VPC connectivity for Agent Gateway and custom MCP server data stores, ensure that the identity used for provisioning and the service agents have the required roles.

#### Standalone project deployments

In a standalone project where the gateway, network attachment, and VPC network reside in the same project, standard Agent Gateway permissions apply (along with **Discovery Engine Editor** , `roles/discoveryengine.editor`, to create custom MCP server data stores). For details, see [Required roles](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#required-roles).

#### Shared VPC or cross-project deployments

If you use a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) or cross-project setup where the target VPC network, subnets, or private DNS zones reside in a central host project (`TARGET_VPC_PROJECT_ID`), the roles required on the host project depend on where you create the Private Service Connect network attachment:

  * **Service project (recommended)** : You create the network attachment in the same service project as Agent Gateway, pointing to the host project's subnet. This approach follows the principle of least privilege because the Agent Gateway service agent only requires `roles/compute.networkUser` on the host project.
  * **Host project** : You create the network attachment directly in the central host project. Because the gateway connects across project boundaries, the service agent requires higher administrative permissions (`roles/compute.networkAdmin` or a custom role with `compute.networkAttachments.update`) to accept the connection in the host project.



Grant the following roles on the host project in addition to standard Agent Gateway permissions:

Principal or identity | Required IAM role | Purpose  
---|---|---  
**Provisioning identity** 1  
(User account or deployment service account) | 

  * Compute Network Viewer (`roles/compute.networkViewer`)
  * DNS Reader (`roles/dns.reader`)
  * Network Connectivity Regional Endpoint Admin (`roles/networkconnectivity.regionalEndpointAdmin`)
  * Network Connectivity Consumer Network Admin (`roles/networkconnectivity.consumerNetworkAdmin`)

| Allows backend validation of the target VPC network, subnets, network attachment, and private DNS zones during gateway creation or updates.  
**Network attachment creator**  
(Administrator creating the attachment) | 

  * Compute Network User (`roles/compute.networkUser`)

| Allows using a Shared VPC subnet in the host project to create a Private Service Connect network attachment.  
**Network attachment in the service project (Recommended)**  
**Agent Gateway service agent** 2 | 

  * Compute Network User (`roles/compute.networkUser`)
  * DNS Peer (`roles/dns.peer`)

| Allows the Agent Gateway service agent to use the host project subnet for the network attachment, connect the Private Service Connect interface to route egress traffic, and peer with private Cloud DNS zones in the host project.  
**Network attachment in the host project**  
**Agent Gateway service agent** 2 | 

  * Compute Network Admin (`roles/compute.networkAdmin`), or a custom role with: 
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.update`
    * `compute.regionOperations.get`
  * DNS Peer (`roles/dns.peer`)

| Allows the Agent Gateway service agent to update the host project network attachment to allow the connection from the Agent Gateway tenant project, to route egress traffic, and peer with private Cloud DNS zones in the host project.  
  
1 For the provisioning identity, basic project-level roles such as Viewer (`roles/viewer`) or Editor (`roles/editor`) on the host project are also sufficient.

2 The Agent Gateway service agent is formatted as `service-AGENT_GATEWAY_PROJECT_NUMBER@gcp-sa-agentgateway.iam.gserviceaccount.com`.

#### Grant roles to the Agent Gateway service agent

Create the Agent Gateway service identity and grant the required roles:
    
    
    gcloud beta services identity create \
        --service=networkservices.googleapis.com \
        --project=AGENT_GATEWAY_PROJECT_ID
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:service-AGENT_GATEWAY_PROJECT_NUMBER@gcp-sa-agentgateway.iam.gserviceaccount.com" \
        --role="roles/compute.networkUser"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:service-AGENT_GATEWAY_PROJECT_NUMBER@gcp-sa-agentgateway.iam.gserviceaccount.com" \
        --role="roles/dns.peer"
    

Replace the following:

  * `AGENT_GATEWAY_PROJECT_ID`: The project ID where you deploy Agent Gateway.
  * `TARGET_PROJECT_ID`: The project ID where you grant the roles. For standalone deployments, this is the same as `AGENT_GATEWAY_PROJECT_ID`. For Shared VPC or cross-project deployments, this is your host project ID (`TARGET_VPC_PROJECT_ID`).
  * `AGENT_GATEWAY_PROJECT_NUMBER`: The numeric project number of the project where you deploy Agent Gateway.



## (Optional) Register OAuth application

If your private MCP server requires OAuth 2.0 authentication, register Gemini Enterprise as an OAuth client application with your identity provider.

### Google Identity

If Google is your identity provider, perform the following steps in the Google Cloud console:

  1. In the Google Cloud console, go to the **Credentials** page.
  2. Click **Create credentials** and select **OAuth client ID**.
  3. In the **Application type** list, select **Web application**.
  4. Optional: If prompted, select **This client will be used by an AI-powered agent** to designate the client for agent workflows.
  5. In the **Name** field, enter a descriptive name for your client application.
  6. In the **Authorized redirect URIs** section, click **Add URI** and enter:  
`https://vertexaisearch.cloud.google.com/oauth-redirect`
  7. Click **Create**.
  8. In the **OAuth client created** dialog, copy the **Client ID** and **Client Secret**.



### Third-party providers

If you use a third-party identity provider, such as Okta or Azure AD, perform the following steps in your provider's administration portal:

  1. Go to your identity provider's administration portal.
  2. Create a new OAuth client application.
  3. Set the authorization redirect URL to:  
`https://vertexaisearch.cloud.google.com/oauth-redirect`
  4. Grant the necessary OAuth scopes to the client application.
  5. Obtain the **Client ID** and **Client Secret** to use during data store configuration.



## Create a network attachment

Create a Private Service Connect network attachment inside your private VPC network. Agent Gateway uses this network attachment to deploy a Private Service Connect interface inside your VPC network for egress.

  1. Ensure that you have the following prerequisites ready:

     * You have enabled the Compute Engine API in the project where you create the network attachment.
     * A subnetwork that meets all of the following requirements: 
       * It's in the region that matches your Gemini Enterprise app location: `us-central1` for **global** or **us** multi-region apps, or `europe-west1` for **eu** multi-region apps.
       * Its IP address range is at least `/28`.
       * It has [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga) enabled.
       * It isn't already used by another network attachment.
     * The required IAM roles: 
       * **Compute Network Admin** (`roles/compute.networkAdmin`) on the project where you create the network attachment.
       * If the subnetwork is in a Shared VPC host project: **Compute Network User** (`roles/compute.networkUser`) on the subnetwork. You must create the network attachment in a service project attached to the host project.
  2. In the Google Cloud console, go to the **Network attachments** page.

[Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

  3. Click **Create network attachment**.

  4. In the **Name** field, enter a descriptive name such as `cymbal-mcp-vpc-attachment`.

  5. Select the **Network** , **Region** , and **Subnetwork** that meet the prerequisites in Step 1.

  6. Under **Connection preference** , select **Automatically accept all connections**.

  7. Click **Create network attachment**.

  8. After creation completes, copy the **Resource URI** of the network attachment for use in the next step. The URI has the following format:
         
         projects/PROJECT_ID/regions/LOCATION/networkAttachments/ATTACHMENT_NAME
         




### (Optional) Configure Cloud NAT for static IP egress

If your use case is static IP egress to a public or external MCP server that requires requests to originate from reserved IP addresses, configure Cloud NAT on the subnetwork assigned to your network attachment:

  1. **Reserve a static external IPv4 address:** Reserve a regional static IP address in the same region as your network attachment:
         
         gcloud compute addresses create STATIC_IP_NAME \
             --region=LOCATION \
             --project=PROJECT_ID
         

  2. **Create a Cloud Router:** If your VPC network doesn't already have a Cloud Router in the region, create one:
         
         gcloud compute routers create ROUTER_NAME \
             --network=NETWORK_NAME \
             --region=LOCATION \
             --project=PROJECT_ID
         

  3. **Create a Cloud NAT gateway:** Create a Cloud NAT gateway associated with the Cloud Router and bind it to the reserved static IP address. Ensure that the NAT gateway covers the subnetwork assigned to your network attachment:
         
         gcloud compute routers nats create NAT_NAME \
             --router=ROUTER_NAME \
             --region=LOCATION \
             --nat-custom-subnet-ip-ranges=SUBNET_NAME \
             --nat-external-ip-pool=STATIC_IP_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `STATIC_IP_NAME`: A name for the reserved external IP address.
     * `LOCATION`: The region matching your network attachment (`us-central1` or `europe-west1`).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `ROUTER_NAME`: The name of the Cloud Router.
     * `NETWORK_NAME`: The name of your VPC network.
     * `NAT_NAME`: A name for the new Cloud NAT gateway.
     * `SUBNET_NAME`: The subnetwork assigned to your network attachment.



For more information, see [Set up and manage Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#create-nat-gateway).

## Create an agent connectivity template

Define an agent connectivity template that encapsulates your VPC egress configuration, including your network attachment, DNS peering, and egress routing mode. You create the connectivity template and Agent Gateway with the gcloud CLI. For more information about connectivity template architecture and routing options, see [Set up VPC connectivity for Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity).

**Important:** Network attachment and connectivity template configurations are immutable after you apply them. To update any VPC egress settings (such as the network attachment, subnet, DNS peering configuration, or VPC egress mode), you must create a new connectivity template with the updated configuration and update the Agent Gateway to reference the new template.

  1. Create a YAML configuration file named `agw-connectivity-template.yaml`:
         
         name: projects/AGENT_GATEWAY_PROJECT_NUMBER/locations/LOCATION/agentConnectivityTemplates/CONNECTIVITY_TEMPLATE_NAME
         accessPath: AGENT_TO_ANYWHERE
         deploymentModel: CENTRALIZED
         egressNetworkConfig:
           networkAttachment: PSC_NETWORK_ATTACHMENT_URI
           # Optional: Delete the dnsPeeringConfig block if you don't require private DNS peering
           dnsPeeringConfig:
             domains:
               - DOMAIN_NAME
             targetNetwork: TARGET_VPC_NETWORK_URI
           vpcEgress: VPC_EGRESS_MODE
           # Optional: Include tlsConfig if your MCP server uses a private CA or self-signed certificate
           # tlsConfig:
           #   trustConfig: projects/AGENT_GATEWAY_PROJECT_NUMBER/locations/LOCATION/trustConfigs/TRUST_CONFIG_NAME
           #   additionalRoots: ADDITIONAL_ROOTS_OPTION
         

Keep the `accessPath` and `deploymentModel` values as shown, and replace the following:

     * `AGENT_GATEWAY_PROJECT_NUMBER`: The numeric project number of the Google Cloud project where the gateway is deployed. To retrieve your project number, run: `gcloud projects describe PROJECT_ID --format="value(projectNumber)"`.
     * `LOCATION`: The region for the agent connectivity template, which corresponds to your Gemini Enterprise app location: 
       * For `global` or `us` multi-region apps, specify `us-central1`.
       * For `eu` multi-region apps, specify `europe-west1`.
     * `CONNECTIVITY_TEMPLATE_NAME`: A name of your choice for the new agent connectivity template resource (for example, `cymbal-mcp-connectivity-template`).
     * `PSC_NETWORK_ATTACHMENT_URI`: The **Resource URI** that you copied in Create a network attachment. This value has the form `projects/PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME`. If the network attachment is in a different project from the gateway (for example, a Shared VPC host project), specify the full resource path.
     * `DOMAIN_NAME`: (Optional) One or more domain suffixes for private DNS peering (for example, `cymbal.internal.` or `run.app.`). Add a list item under `domains` for each domain suffix that you want to peer. Each value must end with a trailing dot (`.`) and have a corresponding private Cloud DNS managed zone authorized for the target network. If your MCP server uses a public domain or split-horizon DNS, DNS peering isn't required and you can omit `dnsPeeringConfig`. For root domain peering, VPC Service Controls, and other advanced DNS scenarios, see [Set up VPC connectivity for Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity).
     * `TARGET_VPC_NETWORK_URI`: The resource URI of the target VPC network, in the form `projects/PROJECT_ID/global/networks/NETWORK_NAME`. This network must be the exact same VPC network where you created the network attachment.
     * `VPC_EGRESS_MODE`: The egress traffic routing setting. Set to `PRIVATE_RANGES_ONLY` (default) to route traffic destined for private IP ranges (RFC 1918, RFC 6598, Class E) through your VPC network, or set to `ALL_TRAFFIC` to route all outbound agent traffic (including public internet addresses) through your VPC network.
     * `tlsConfig`: (Optional) The TLS configuration for server certificate validation when connecting to private endpoints over HTTPS that use private CAs or self-signed certificates: 
       * `TRUST_CONFIG_NAME`: The name of the Certificate Manager `TrustConfig` resource containing your private CA certificates or trust anchors.
       * `ADDITIONAL_ROOTS_OPTION`: Specifies whether to trust publicly trusted CA roots in addition to your custom trust config. Set to `PUBLICLY_TRUSTED_ROOTS` (default) to trust both certificates validated by the `trustConfig` parameter and all publicly trusted CAs. Set to `NO_ADDITIONAL_ROOTS` to trust only certificates validated by the `trustConfig` parameter. For instructions on creating a `TrustConfig` resource in Certificate Manager, see [Set up VPC connectivity for Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity#tls-certificate-requirements).
  2. Run the following command to create the agent connectivity template:
         
         gcloud network-services agent-connectivity-templates import CONNECTIVITY_TEMPLATE_NAME \
             --source="agw-connectivity-template.yaml" \
             --location=LOCATION \
             --project=AGENT_GATEWAY_PROJECT_ID
         

Replace the following:

     * `CONNECTIVITY_TEMPLATE_NAME`: The name of the agent connectivity template resource.
     * `LOCATION`: The location where you created the agent connectivity template resource. For example, `us-central1`.
     * `AGENT_GATEWAY_PROJECT_ID`: The Google Cloud project ID where you deploy Agent Gateway.



## Create an Agent Gateway

Create an Agent Gateway resource that references the agent connectivity template. For more information about deploying gateways for Gemini Enterprise, see [Route Gemini Enterprise traffic through Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy).

  1. Create a gateway YAML configuration file named `cymbal-agent-gateway-vpc-egress.yaml`:
         
         name: AGENT_GATEWAY_NAME
         protocols:
           - MCP
         googleManaged:
           governedAccessPath: AGENT_TO_ANYWHERE
         agentConnectivityTemplate: projects/AGENT_GATEWAY_PROJECT_NUMBER/locations/LOCATION/agentConnectivityTemplates/CONNECTIVITY_TEMPLATE_NAME
         # Optional: Include only when using Agent Registry governance or IAP authorization
         registries:
           - //agentregistry.googleapis.com/projects/PROJECT_ID/locations/REGISTRY_LOCATION
         

Keep the `protocols` and `googleManaged` values as shown, and replace the following:

     * `AGENT_GATEWAY_NAME`: A name of your choice for the Agent Gateway resource (for example, `cymbal-mcp-gateway`).
     * `AGENT_GATEWAY_PROJECT_NUMBER`: The numeric project number of the Google Cloud project where you create the gateway.
     * `LOCATION`: The region of the gateway. This value must match the region of your network attachment and connectivity template (`us-central1` or `europe-west1`).
     * `CONNECTIVITY_TEMPLATE_NAME`: The name of the agent connectivity template that you created in Create an agent connectivity template.
     * `PROJECT_ID`: Your Google Cloud project ID. Required only when associating your gateway with Agent Registry for unified agent governance, tool discovery, and IAP access policies. Omit the `registries` block if you use basic authorization.
     * `REGISTRY_LOCATION`: The location of your Agent Registry instance, which must align with your Gemini Enterprise app and gateway location: 
       * If your app location is `us`, use `us-central1` or `us`.
       * If your app location is `eu`, use `europe-west1`, `eu`, or `global`.
       * If your app location is `global`, use `us-central1`, `us`, or `global`.
  2. Run the following command to create the Agent Gateway resource:
         
         gcloud network-services agent-gateways import AGENT_GATEWAY_NAME \
             --source="cymbal-agent-gateway-vpc-egress.yaml" \
             --location=LOCATION \
             --project=AGENT_GATEWAY_PROJECT_ID
         

Replace the following:

     * `AGENT_GATEWAY_NAME`: The name of the Agent Gateway resource.
     * `LOCATION`: The region where you create the gateway (`us-central1` or `europe-west1`).
     * `AGENT_GATEWAY_PROJECT_ID`: The Google Cloud project ID where you create the gateway.



## Create an authorization policy

After you create the Agent Gateway, configure an authorization policy to allow egress traffic through the gateway. If you register your MCP server in Agent Registry and want to control agent access with IAM policies, use IAP authorization. Otherwise, use basic authorization, which allows all egress traffic through the gateway.

###  IAP authorization 

Deploy an IAP authorization extension in `DRY_RUN` audit mode. This mode permits egress traffic so you can validate connectivity without blocking requests. For more information, see [Delegate authorization to IAP](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization#configure-authz-iap).

  1. Define an authorization extension in a YAML file named `iap-request-authz-extension.yaml`:
         
         name: cymbal-iap-request-authz-ext
         service: iap.googleapis.com
         failOpen: false
         timeout: 1s
         metadata:
           iapPolicyVersion: "V2"
           iamEnforcementMode: "DRY_RUN"
         

  2. Import the authorization extension:
         
         gcloud service-extensions authz-extensions import cymbal-iap-request-authz-ext \
             --source=iap-request-authz-extension.yaml \
             --location=LOCATION \
             --project=PROJECT_ID
         

  3. Define an authorization policy in a YAML file named `iap-request-authz-policy.yaml`:
         
         name: cymbal-iap-request-authz-policy
         target:
           resources:
             - "projects/PROJECT_ID/locations/LOCATION/agentGateways/AGENT_GATEWAY_NAME"
         policyProfile: REQUEST_AUTHZ
         action: CUSTOM
         customProvider:
           authzExtension:
             resources:
               - "projects/PROJECT_ID/locations/LOCATION/authzExtensions/cymbal-iap-request-authz-ext"
         

  4. Import the authorization policy:
         
         gcloud network-security authz-policies import cymbal-iap-request-authz-policy \
             --source=iap-request-authz-policy.yaml \
             --location=LOCATION \
             --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID.
     * `LOCATION`: The location of your Agent Gateway, such as `us-central1` or `europe-west1`.
     * `AGENT_GATEWAY_NAME`: The name of your Agent Gateway resource (such as `cymbal-mcp-gateway`).

**Note:** In `DRY_RUN` mode, the gateway permits all traffic and logs policy decisions. Before you enforce policies, [create IAM agent policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies-uap) that grant the `iap.resources.egressViaIAP` permission to your agents. Then remove `iamEnforcementMode: "DRY_RUN"` from the extension YAML file and import the extension again.

###  Basic authorization 

If your deployment doesn't require IAP or IAM agent policies, configure a basic authorization policy to allow all egress traffic through the gateway (leave the optional `registries` block commented out in your gateway YAML configuration):

  1. Create a configuration file named `basic-authz-policy-allow-all.yaml`:
         
         name: AGENT_GATEWAY_NAME-authz-policy-allow-all
         target:
           resources:
             - "projects/PROJECT_ID/locations/LOCATION/agentGateways/AGENT_GATEWAY_NAME"
         policyProfile: REQUEST_AUTHZ
         action: ALLOW
         httpRules:
           - to:
               operations:
                 - paths:
                     - prefix: /
         

  2. Import the authorization policy:
         
         gcloud network-security authz-policies import AGENT_GATEWAY_NAME-authz-policy-allow-all \
             --source=basic-authz-policy-allow-all.yaml \
             --location=LOCATION \
             --project=PROJECT_ID
         

  3. Verify the active authorization policy:
         
         gcloud network-security authz-policies describe AGENT_GATEWAY_NAME-authz-policy-allow-all \
             --location=LOCATION \
             --project=PROJECT_ID
         

Replace the following:

     * `AGENT_GATEWAY_NAME`: The name of your Agent Gateway resource.
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `LOCATION`: The location of your Agent Gateway (`us-central1` or `europe-west1`).



## Update firewall rules

Agent Gateway egress into your VPC network doesn't require an egress firewall rule, because VPC networks allow egress traffic by default. If you've configured firewall rules that deny egress, such as rules that block internet-bound traffic, add a rule that allows egress from your network attachment subnet. For static IP egress to a public MCP server, this rule must allow traffic to the server's public IP addresses.

If you connect to a private MCP server hosted inside your VPC network, you must also create an ingress firewall rule that allows incoming connections from your network attachment subnet:

  1. In the Google Cloud console, go to the **Firewall** page.
  2. Click **Create firewall rule**.
  3. In the **Name** field, enter a name such as `allow-cymbal-mcp-gateway-ingress`.
  4. Select the **VPC network** where your private MCP server runs.
  5. Set **Direction of traffic** to **Ingress**.
  6. Set **Action on match** to **Allow**.
  7. In **Targets** , select **Specified target tags** or **All instances in the network** according to your network deployment model.
  8. In **Source IPv4 ranges** , enter the IP address range of the subnet associated with your network attachment.
  9. Under **Protocols and ports** , select **Specified protocols and ports** and specify the TCP port used by your private MCP server, such as `tcp:443` or `tcp:8080`.
  10. Click **Create**.



## Verify the gateway configuration

Confirm that your gateway, agent connectivity template, and Private Service Connect network attachment are properly linked and accepted:

  1. Verify that the gateway references your agent connectivity template:
         
         gcloud network-services agent-gateways describe AGENT_GATEWAY_NAME \
             --location=LOCATION \
             --project=AGENT_GATEWAY_PROJECT_ID
         

The output includes an `agentConnectivityTemplate` field that references the template you created. If this field is missing, the gateway isn't routing traffic through your VPC network. Verify that the `agentConnectivityTemplate` value in your gateway YAML file is correct, and then import the file again.

  2. Verify that your agent connectivity template references your network attachment:
         
         gcloud network-services agent-connectivity-templates describe CONNECTIVITY_TEMPLATE_NAME \
             --location=LOCATION \
             --project=AGENT_GATEWAY_PROJECT_ID
         

In the output, confirm that `egressNetworkConfig.networkAttachment` points to your network attachment resource URI.

  3. Verify that your network attachment shows an accepted connection:
         
         gcloud compute network-attachments describe ATTACHMENT_NAME \
             --region=LOCATION \
             --project=PROJECT_ID
         

In the output, confirm that `connectionEndpoints` lists an entry with `status: ACCEPTED`.




### Troubleshoot common gateway errors

If Gemini Enterprise fails to connect to your custom MCP server through the gateway, inspect the HTTP status code returned in the chat turn or Cloud Logging:

Error | Cause | Resolution  
---|---|---  
**HTTP 403 Forbidden** | Outbound egress through Agent Gateway is blocked by default until an active authorization policy is bound to the gateway. | Ensure you completed Create an authorization policy and that your policy targets your gateway's full resource path:   
`projects/PROJECT_ID/locations/LOCATION/agentGateways/AGENT_GATEWAY_NAME`   
  
To confirm the policy is active, run:   
`gcloud network-security authz-policies describe AGENT_GATEWAY_NAME-authz-policy-allow-all --location=LOCATION --project=PROJECT_ID`  
**HTTP 503 Service Unavailable** | The gateway can't resolve your private MCP server hostname or can't route packets into your VPC network. | 

  * If your server uses a private domain name (such as `mcp.cymbal.internal`), verify that `dnsPeeringConfig.domains` in your agent connectivity template includes the domain suffix with a trailing dot (`.`), and that your private Cloud DNS zone is authorized for the target VPC network.
  * Verify that the network attachment subnet has [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga) enabled.
  * Verify that your firewall rules allow ingress traffic from the network attachment subnet to your MCP server on the configured port.

  
  
## What's next

  * To create your custom MCP server data store after completing the prerequisite setup, see [Create the custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server#create-the-custom-mcp-server-data-store).
  * For detailed Agent Gateway governance options, see [Set up VPC connectivity for Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-vpc-connectivity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
