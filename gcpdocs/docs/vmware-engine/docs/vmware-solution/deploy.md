---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy/
title: Deploy nodes and configure appliance networking by using the console \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:40:20.443005+00:00
---

# Deploy nodes and configure appliance networking by using the console  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy nodes and configure appliance networking by using the console

This page describes how to use the Google Cloud console to deploy bare-metal ESXi nodes and configure Google Cloud networking constructs in preparation for deploying VMware Cloud Foundation (VCF) in VMware solution on Google Cloud.

Completing the steps on this page prepares your Google Cloud infrastructure for VCF bring-up, but **does not** deploy VCF or the VCF management appliances themselves:

  * **What this workflow does** : Provisions bare-metal ESXi compute instances, configures primary and dynamic network interfaces (NICs), sets up VPC subnets and zonal network endpoint groups (NEGs), and pre-configures Google Cloud load-balancing constructs and IP address reservations for your future VCF management appliances and NSX datapath.
  * **What this workflow does not do** : It doesn't reset the initial ESXi `root` password, initialize ESXi host networking (`vSwitch0` and vSAN), deploy the VCF Installer, or deploy VCF management appliances (such as vCenter Server, SDDC Manager, or NSX Manager). To reset the initial ESXi `root` password, initialize your hosts, and deploy VCF after completing these steps, you must run the VMware solution toolkit and complete bring-up in the VCF Installer, as described in [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).



## Before you begin

Before you start, verify that you have completed the following requirements:

  1. Ensure that your project has sufficient bare-metal node quota in your target region and zone. For required quotas and instructions on how to view or request quota increases, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas).
  2. Ensure that you have the required Identity and Access Management (IAM) permissions, including `Compute Admin` (`roles/compute.admin`) and, if you use Cloud DNS, `DNS Administrator` (`roles/dns.admin`).
  3. Set up your Virtual Private Cloud (VPC) network and plan your subnet IP address ranges for management, vSAN, vMotion, and NSX Tunnel Endpoints (TEP). Set the VPC network MTU to `8896` bytes before you deploy the nodes, and create new subnets in VMware solution while creating the nodes.

VMware solution requires your VPC network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

     * **Product** : Google Cloud VMware Engine
     * **Priority** : P2
     * **Category** : Network Connectivity
     * **Business Impact** : General Technical question
     * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

**Note:** On Google Cloud console, **VMware Engine** > **Self-managed** option will not be visible till your project is enabled.
  4. Plan your Domain Name System (DNS) infrastructure to support forward and reverse lookups for all planned ESXi node hostnames and VCF appliance endpoints.

  5. **Node hostnames** : Provide the fully qualified domain name (FQDN) of each node during deployment. This ensures that ESXi generates certificates using hostnames.

  6. **Password requirements** : Ensure that the `root` and local user passwords for the VCF Installer and SDDC Manager, as well as the ESXi `root` password, meet Broadcom's password requirements. For more information, see [Default password requirements for VCF components](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/fleet-management/manage-passwords/default-password-requirements-for-vcf-components.html) in the Broadcom documentation.

  7. **Trusted image policy** : If your organization doesn't enforce the `constraints/compute.trustedImageProjects` organization policy, then no action is required. If your organization enforces this policy, then allow `projects/smve-prod-public-images` so that Compute Engine can create bare-metal boot disks. For more information, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).

  8. **VPC Service Controls** : If your target project isn't in a service perimeter, then no action is required. If your project is in a service perimeter, then add an egress rule that allows `compute.googleapis.com` operations to the `smve-prod-public-images` project (`projects/999037279871`):
         
         - egressFrom:
             identityType: ANY_IDENTITY
           egressTo:
             operations:
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: "*"
             resources:
             - projects/999037279871
         

For more information, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).




### Verify regional quota

Before you provision bare-metal nodes or create a cluster, verify that your project has sufficient regional and global Compute Engine quota. Add the resources of all existing clusters in the region to the following incremental values before you compare them against your project quota:

Quota metric | Resources required per bare-metal node | Resources required for a 3-node cluster  
---|---|---  
`compute.googleapis.com/cpus_per_vm_family` for `Z3` | 192 vCPUs | 3 × 192 = 576 vCPUs  
`compute.googleapis.com/local_ssd_total_storage_per_vm_family` for `Z3` | 72 TB | 3 × 72 TB = 216 TB  
`compute.googleapis.com/hyperdisk_balanced_total_storage` | 128 GB | 3 × 128 GB = 384 GB  
`compute.googleapis.com/resource_policies` | 0 when adding nodes to an existing cluster | 1 spread placement policy per cluster  
`compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha` | 0 when adding nodes or clusters without new appliances | 1 per new VCF management appliance VIP or NSX Edge endpoint  
  
For the complete list of required quotas and instructions on how to view or request quota increases, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas).

## Deploy bare-metal nodes and configure node networking

To provision bare-metal ESXi nodes and configure their network interfaces, do the following:

  1. In the Google Cloud console, go to **VMware Engine** > **Self-managed** > **Overview**.

[Go to Overview](https://console.cloud.google.com/vmwareengine/self-managed/overview)

  2. Click **Start Deployment** to launch the infrastructure provisioning and configuration workflow.

  3. In the **Node Configuration** section, select the **Region** and **Zone** where you want to deploy your nodes.

  4. Select a **Placement policy** , or click **Create new placement policy** :

     * If you create a placement policy, enter a name and select the number of availability domains (up to 8).
**Caution:** Nodes assigned to a placement policy must belong to only one cluster to ensure an accurate mapping between availability domains and vSAN fault domains.
  5. Select the **VCF version** that you plan to deploy on the nodes.

  6. Select the **Machine type** and specify the number of nodes to create. A high availability (HA) VCF deployment requires a minimum of four nodes.

  7. In the **Quickname Wizard** section, enter the **Resource name prefix** and **Domain name suffix** :

     * **Resource name prefix** : The prefix that VMware solution prepends to all generated resource names.
     * **Domain name suffix** : The DNS domain suffix that VMware solution uses to generate the fully qualified domain name (FQDN) for each node.
  8. Review the **Node name** , **Hostname** , and **Availability domain** for each node. Provide the fully qualified domain name (FQDN) in the **Hostname** field. To modify the defaults, click **Edit** :

     * **Availability domain** : Select an availability domain for each node. Distribute nodes evenly across the configured availability domains in your placement policy to align with vSAN fault domain requirements. For more information, see [Placement policies and availability domains](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies).
     * **Internal IPv4 address** : Select **Ephemeral (Automatic)** , **Ephemeral (Custom)** , or **Reserved** : 
       * If you select **Ephemeral (Custom)** , enter the IP address.
       * If you select **Reserved** , select an existing reserved static IP or specify the configuration details.
  9. To prevent accidental node deletion, select **Enable delete protection**. This option is enabled by default.

  10. Optionally, click **Manage labels** to add metadata labels to your nodes.

  11. Click **Continue** to proceed to node network configuration.

  12. In the **Networking** section, select the **VPC Network** for your nodes.

  13. In the **Network Interface** section, configure the primary interface:

     * Select an existing **Subnet** or click **Create subnet** to define a new subnet with a name, description, and IPv4 range.
     * Select an existing **Network Endpoint Group** or click **Create network endpoint group** to create a new group. The workflow automatically adds all provisioned nodes to this group.
**Caution:** All nodes in a cluster within a single zone must belong to the same network endpoint group of the subnet for VCF network appliances to route traffic across cluster nodes.
  14. Configure dynamic network interfaces for VMware traffic:

     * **Dynamic NIC (vSAN)** : Select or create the subnet for vSAN clustering traffic. Optionally, assign a network endpoint group.
     * **Dynamic NIC (vMotion)** : Select or create the subnet for live VM migration traffic. Optionally, assign a network endpoint group.
     * **Dynamic NIC (NSX Tunnel Endpoint)** : Select or create the subnet and network endpoint group for NSX TEP overlay traffic.
  15. Optional: Add additional dynamic NICs if your architecture requires dedicated interfaces for custom workload traffic.

  16. Click **Continue** to proceed to appliance networking setup.




## Configure appliance networking

To pre-configure Google Cloud load-balancing resources and IP reservations for the VCF management appliances and NSX datapath that you will deploy during VCF bring-up, do the following:

  1. On the **Configure Appliance Networking** page, select the **VCF Deployment Model**. For high availability deployments, select **High Availability Deployment** (requires 4 or more nodes).
  2. In the **Management Appliances** and **NSX Datapath** tables, review the preconfigured Google Cloud networking resource names and endpoints.
  3. To customize names or internal IP assignments, click **Edit** for the corresponding table: 
     * Select **Ephemeral (Automatic)** , **Ephemeral (Custom)** , or **Reserved** for each appliance endpoint.
     * If you use reserved addresses, provide the reserved IP address or specify static reservation details.
  4. Click **Continue** to review the configuration summary.
  5. Verify the configuration details and click **Deploy** to provision your bare-metal nodes and configure your appliance networking resources.



## Configure Cloud DNS zones and records

When you deploy bare-metal instances and configure appliance networking by using the Google Cloud console, you must create DNS zones and forward (`A`) and reverse (`PTR`) records if you don't already have them in place.

You can automate Cloud DNS and Network Time Protocol (NTP) DNS setup by running the standalone `scripts/cloud_dns/vcf_cloud_dns_sync.py` script in the [VMware solution toolkit repository](https://github.com/GoogleCloudPlatform/self-managed-vmware-solution-toolkit/blob/main/scripts/cloud_dns/vcf_cloud_dns_sync.py). The script performs the following operations:

  * Enables the Cloud DNS API (`dns.googleapis.com`).
  * Ensures that a Cloud DNS server policy (with default settings) is attached to your VPC network.
  * Ensures that private forward and reverse lookup zones exist and are bound to your VPC network.
  * Synchronizes forward (`A`) and reverse (`PTR`) DNS records for Z3 bare-metal nodes and management-subnet internal load balancer frontends (stripping the `-fr` suffix and skipping IP-only NSX TEP and uplink subnet load balancers).
  * Manages the NTP DNS record (`ntp.DOMAIN_NAME`) in your private forward lookup zone (for example, pointing to the Compute Engine metadata server at `169.254.169.254`).



To obtain the script, clone the toolkit repository and go to the `scripts/cloud_dns` directory:
    
    
    git clone https://github.com/GoogleCloudPlatform/self-managed-vmware-solution-toolkit
    cd self-managed-vmware-solution-toolkit/scripts/cloud_dns
    

**Note:** If you have already set your default project by running `gcloud config set project PROJECT_ID`, you can omit the `--project-id` flag from the following commands.

### Preview changes in dry-run mode

To preview all Cloud DNS API, policy, zone, node and internal load balancer record, and NTP operations without applying any changes, run the script with the `--dry-run` flag:
    
    
    python3 vcf_cloud_dns_sync.py \
        --project-id PROJECT_ID \
        --vpc-network VPC_NETWORK_NAME \
        --domain DOMAIN_NAME \
        --sync-all \
        --set-ntp-ip 169.254.169.254 \
        --dry-run
    

### Run initial day-0 DNS setup

Run the following command after you provision your VPC network, subnets, Z3 bare-metal instances, NEGs, and internal load balancer forwarding rules in the Google Cloud console, and before you run VCF Installer validation. This command enables the Cloud DNS API, creates the VPC DNS policy, creates private forward and `/16` (or `/8`) reverse zones from non-NSX subnets, registers all node and management frontend `A` and `PTR` records (skipping NSX subnet load balancers), and configures `ntp.DOMAIN_NAME` to point to the Compute Engine metadata server (`169.254.169.254`):
    
    
    python3 vcf_cloud_dns_sync.py \
        --project-id PROJECT_ID \
        --vpc-network VPC_NETWORK_NAME \
        --domain DOMAIN_NAME \
        --sync-all \
        --set-ntp-ip 169.254.169.254
    

### Synchronize records for day-2 scale-out

After you add new Z3 bare-metal hosts or workload domain internal load balancer forwarding rules in the Google Cloud console, re-run the script with the `--sync-all` flag to register only the newly added records (existing unchanged records are skipped automatically):
    
    
    python3 vcf_cloud_dns_sync.py \
        --project-id PROJECT_ID \
        --vpc-network VPC_NETWORK_NAME \
        --domain DOMAIN_NAME \
        --sync-all
    

### Bootstrap DNS zones and VPC policy before provisioning compute resources

If you want to enable the Cloud DNS API, create the VPC DNS policy, and create forward and reverse zones before you provision bare-metal nodes or load balancer frontends, run the following command:
    
    
    python3 vcf_cloud_dns_sync.py \
        --project-id PROJECT_ID \
        --vpc-network VPC_NETWORK_NAME \
        --domain DOMAIN_NAME \
        --reverse-zones REVERSE_ZONE_NAME=REVERSE_SUBNET_CIDR \
        --setup-zones
    

### Use custom resource names or pre-created administrator resources

To override default resource names or skip creating the VPC DNS policy or managed zones when an administrator has pre-provisioned them, use one of the following options:

  * **Specify custom zone and policy names** (you can specify multiple `--reverse-zones` entries):
        
        python3 vcf_cloud_dns_sync.py \
            --project-id PROJECT_ID \
            --vpc-network VPC_NETWORK_NAME \
            --domain DOMAIN_NAME \
            --dns-policy CUSTOM_DNS_POLICY_NAME \
            --forward-zone CUSTOM_FORWARD_ZONE_NAME \
            --reverse-zones REVERSE_ZONE_1=CIDR_1 REVERSE_ZONE_2=CIDR_2 \
            --sync-all
        

  * **Skip creating the VPC DNS policy** (when the policy already exists):
        
        python3 vcf_cloud_dns_sync.py \
            --project-id PROJECT_ID \
            --vpc-network VPC_NETWORK_NAME \
            --domain DOMAIN_NAME \
            --no-create-dns-policy \
            --sync-all
        

  * **Skip creating forward and reverse zones** (when zones are pre-created by an administrator; you must pass `--reverse-zones`):
        
        python3 vcf_cloud_dns_sync.py \
            --project-id PROJECT_ID \
            --vpc-network VPC_NETWORK_NAME \
            --domain DOMAIN_NAME \
            --reverse-zones REVERSE_ZONE_1=CIDR_1 REVERSE_ZONE_2=CIDR_2 \
            --no-create-zones \
            --sync-all
        




Before you run the preceding commands, replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `VPC_NETWORK_NAME`: the name of your VPC network.
  * `DOMAIN_NAME`: the DNS domain suffix for your VCF environment (for example, `vcf.example.com`).
  * `REVERSE_ZONE_NAME=REVERSE_SUBNET_CIDR`: the managed zone name and CIDR block for a reverse lookup zone (for example, `smve-rev-10-10=10.10.0.0/16`).
  * `CUSTOM_DNS_POLICY_NAME`: a custom name for the Cloud DNS server policy.
  * `CUSTOM_FORWARD_ZONE_NAME`: a custom name for the private forward managed zone.
  * `REVERSE_ZONE_1=CIDR_1` and `REVERSE_ZONE_2=CIDR_2`: one or more reverse managed zone name and CIDR pairs (for example, `my-rev-zone-1=10.10.1.0/24 my-rev-zone-2=10.10.2.0/24`).



## What's next

After your bare-metal nodes, Google Cloud networking resources, and DNS records are configured, complete the following steps to prepare your hosts and deploy VCF:

**Caution:** For security, you must reset the initial ESXi `root` password on each newly provisioned bare-metal instance before use. Running the prepare nodes toolkit automatically resets the ESXi `root` password on each host to the `esxi-root-password` secret stored in Secret Manager. If you don't run the prepare nodes toolkit, you must manually reset the `root` password on each bare-metal ESXi instance.

  1. If you use an external DNS server instead of configuring Cloud DNS by using `vcf_cloud_dns_sync.py`, update your DNS server with forward (`A`) and reverse (`PTR`) records for: 
     * All ESXi node hostnames and internal IP addresses.
     * All VCF management appliance hostnames and internal IP addresses.
  2. Run the prepare nodes toolkit to reset the initial ESXi `root` password on each host, initialize ESXi hosts, and deploy the VCF Installer. For step-by-step instructions, see [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).
  3. Access the VMware Cloud Foundation (VCF) installer to complete deployment and bring up your management domain. For instructions on completing VCF bring-up, see [Deploy a new VCF fleet or a new VCF instance](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html) in the Broadcom documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
