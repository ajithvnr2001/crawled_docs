---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/configure-offline-depot/
title: Configure a VCF software depot \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:01.654853+00:00
---

# Configure a VCF software depot  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/configure-offline-depot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a VCF software depot

To deploy and upgrade VMware Cloud Foundation (VCF) in VMware solution on Google Cloud, your VCF Installer and SDDC Manager appliances need access to VCF software bundles, patches, and compatibility metadata. This document compares the available VCF software repository architectures and explains how to configure private connectivity to the Google-provided offline depot by using Private Service Connect.

## Choose your repository architecture

You can provide VCF software bundles to your VMware solution environment by using either of the following methods:

  * **Broadcom public repository (online depot)** : Connect your VCF Installer and SDDC Manager appliances directly to the Broadcom online depot over the internet (for example, by using Cloud NAT or an outbound web proxy) and authenticate with your Broadcom Support Portal credentials and download token. For more information, see the [Broadcom documentation on connecting to the online depot](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/lifecycle-management/binary-management-for-vmware-cloud-foundation/binary-management-for-vcf-core-components/configure-an-online-depot-for-a-vcf-instance.html).
  * **Google-provided offline depot (Private Service Connect)** : Connect privately to a regional software repository hosted by Google Cloud over a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect). All software downloads remain on the Google Cloud internal network without requiring internet egress.



The following table compares the two repository architectures:

Feature  | Broadcom online depot | Google-provided offline depot   
---|---|---  
**Network path** | Outbound internet access (Cloud NAT or proxy) | Private VPC connectivity (Private Service Connect endpoint)   
**Authentication** | Broadcom Support Portal download token | VPC-level access control through Private Service Connect   
**Bandwidth and latency** | Depends on internet egress configuration | High-throughput regional transfer within Google Cloud   
**Air-gapped support** | Not supported without an external jump host | Supported for isolated VPC environments   
  
## Before you begin

**Note:** If you use one of the deployment workflows in the [Deployment options overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options), the VMware solution toolkit configures the offline depot for you. Skip the Configure the Google-provided offline depot section and go to What's next.

Before you configure a Private Service Connect endpoint for the Google-provided offline depot, complete the following prerequisites:

  1. Enable the required Google Cloud APIs in your project. The following table lists the required APIs:

Service name | API identifier | Purpose  
---|---|---  
Compute Engine API | `compute.googleapis.com` | Provisions subnets, internal IP addresses, and forwarding rules  
Cloud DNS API | `dns.googleapis.com` | Creates private DNS zones and records for depot resolution  
Service Directory API | `servicedirectory.googleapis.com` | Registers Private Service Connect endpoints  
  
To enable these APIs by using the Google Cloud CLI, run the following command:
         
         gcloud services enable compute.googleapis.com \
            dns.googleapis.com \
            servicedirectory.googleapis.com \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
  2. Verify that your user account or service account has the following Identity and Access Management (IAM) roles on the target project:

     * Compute Network Admin (`roles/compute.networkAdmin`)
     * DNS Administrator (`roles/dns.admin`)
  3. Set up your Virtual Private Cloud (VPC) network and plan your subnet IP address ranges for management, vSAN, vMotion, and NSX Tunnel Endpoints (TEP). Set the VPC network MTU to `8896` bytes before you deploy the nodes, and create new subnets in VMware solution while creating the nodes.

VMware solution requires your VPC network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

     * **Product** : Google Cloud VMware Engine
     * **Priority** : P2
     * **Category** : Network Connectivity
     * **Business Impact** : General Technical question
     * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).




## Configure the Google-provided offline depot

To set up private access to the regional VCF offline depot, provision a dedicated standard (non-Layer 2 broadcast) subnet, deploy a Private Service Connect endpoint, and configure Cloud DNS resolution.

### Provision the offline depot subnet

Create a dedicated standard (non-Layer 2 broadcast) subnet with a minimum CIDR size of `/29` in the same region as your bare-metal nodes:

**Note:** Don't deploy the Private Service Connect endpoint or reserve its `GCE_ENDPOINT` IP address in Layer 2 ARP broadcast or VLAN-tagged node subnets (such as the VCF management, `vSAN`, `vMotion`, or `NSX-TEP` subnets). For more information, see [Known issues](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues#dns-inbound-forwarding-subnet).
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --network=VPC_NETWORK_NAME \
        --region=REGION \
        --range=SUBNET_CIDR \
        --project=PROJECT_ID
    

Before you run the command, replace the following:

  * `SUBNET_NAME`: the name of the standard subnet for the offline depot endpoint (for example, `snet-offline-depot`).
  * `VPC_NETWORK_NAME`: the name of your VPC network.
  * `REGION`: the Google Cloud region where your bare-metal nodes reside (for example, `us-central1`).
  * `SUBNET_CIDR`: an unused CIDR block of `/29` or larger (for example, `192.168.10.0/29`).
  * `PROJECT_ID`: the ID of your Google Cloud project.



### Deploy the Private Service Connect endpoint

Reserve an internal IP address for the endpoint and create a forwarding rule that targets the regional offline depot service attachment:

  1. Reserve a regional internal IP address with the `GCE_ENDPOINT` purpose:
         
         gcloud compute addresses create offline-depot-ip \
            --region=REGION \
            --subnet=SUBNET_NAME \
            --purpose=GCE_ENDPOINT \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `REGION`: the Google Cloud region (for example, `us-central1`).
     * `SUBNET_NAME`: the name of your standard offline depot subnet.
     * `PROJECT_ID`: the ID of your Google Cloud project.
  2. Retrieve the reserved internal IP address so that you can use it when you configure DNS:
         
         gcloud compute addresses describe offline-depot-ip \
            --region=REGION \
            --format='get(address)' \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `REGION`: the Google Cloud region.
     * `PROJECT_ID`: the ID of your Google Cloud project.
  3. Create the Private Service Connect forwarding rule pointing to the regional offline depot service attachment:
         
         gcloud compute forwarding-rules create offline-depot-endpoint \
            --region=REGION \
            --network=VPC_NETWORK_NAME \
            --address=offline-depot-ip \
            --target-service-attachment=projects/smve-prod-offline-depot/regions/REGION/serviceAttachments/offline-depot-service-attachment-REGION \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `REGION`: the Google Cloud region where your bare-metal nodes are deployed (for example, `us-central1`).
     * `VPC_NETWORK_NAME`: the name of your VPC network.
     * `PROJECT_ID`: the ID of your Google Cloud project.



### Configure Cloud DNS resolution

The offline depot HTTPS server presents a TLS certificate for `offline-depot.REGION.selfmanagedvmwareengine.goog`. Create a private Cloud DNS zone and an `A` record so that your VCF appliances resolve this fully qualified domain name (FQDN) to your Private Service Connect endpoint IP address:

  1. Create a private managed DNS zone for the regional domain:
         
         gcloud dns managed-zones create offline-depot-zone \
            --dns-name=REGION.selfmanagedvmwareengine.goog. \
            --description='Private DNS zone for the regional VCF offline depot' \
            --visibility=private \
            --networks=VPC_NETWORK_NAME \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `REGION`: the Google Cloud region (for example, `us-central1`).
     * `VPC_NETWORK_NAME`: the name of your VPC network.
     * `PROJECT_ID`: the ID of your Google Cloud project.
  2. Create an `A` record for `offline-depot.REGION.selfmanagedvmwareengine.goog.` that maps to your reserved Private Service Connect IP address:
         
         gcloud dns record-sets create offline-depot.REGION.selfmanagedvmwareengine.goog. \
            --zone=offline-depot-zone \
            --type=A \
            --ttl=300 \
            --rrdatas=PSC_INTERNAL_IP \
            --project=PROJECT_ID
         

Before you run the command, replace the following:

     * `REGION`: the Google Cloud region.
     * `PSC_INTERNAL_IP`: the internal IP address reserved for `offline-depot-ip`.
     * `PROJECT_ID`: the ID of your Google Cloud project.
**Note:** If you register the Private Service Connect forwarding rule with a Service Directory namespace during endpoint creation, Google Cloud can automatically populate the private DNS record in your linked Cloud DNS zone.



### Associate the DNS zone with connected VPC networks

If your VCF management appliances or jump host reside in a Shared VPC or a peered VPC network, authorize those networks to query the `offline-depot-zone` private zone. For instructions on binding additional VPC networks or configuring cross-project DNS peering, see [Manage private zones across VPC networks](https://docs.cloud.google.com/dns/docs/zones/manage-zones#cross-project-binding).

## Verify connectivity

From a jump host or management VM inside your VPC network, verify that DNS resolution and HTTPS connectivity to the regional offline depot succeed:

  1. Verify that the regional FQDN resolves to your Private Service Connect internal IP address:
         
         nslookup offline-depot.REGION.selfmanagedvmwareengine.goog
         

  2. Test HTTPS connectivity to the offline depot endpoint:
         
         curl -I https://offline-depot.REGION.selfmanagedvmwareengine.goog
         

Before you run the commands, replace the following:

     * `REGION`: the Google Cloud region where you configured the endpoint (for example, `us-central1`).

A successful connection returns an HTTP `200 OK` or `301`/`302` response from the depot web server.




## What's next

  * Review the [Deployment options overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options).
  * Deploy your environment by using [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform) or [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
