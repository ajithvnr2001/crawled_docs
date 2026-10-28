---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform/
title: Deploy nodes and VCF by using Terraform and toolkit \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:03.107755+00:00
---

# Deploy nodes and VCF by using Terraform and toolkit  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy nodes and VCF by using Terraform and toolkit

This document explains how to use Terraform automation to deploy bare-metal ESXi nodes, Layer 2 broadcast networks, Cloud DNS, and regional internal load balancers (ILBs) for VMware solution on Google Cloud with VMware Cloud Foundation (VCF).

The automation provisions the following infrastructure:

  * Dedicated bare-metal ESXi hypervisors (`z3-highmem-192-highlssd-metal` or `z3-highmem-192-metal`).
  * Multi-VLAN Layer 2 broadcast networks with jumbo frames (MTU 8896).
  * Cloud DNS private managed zones and inbound query forwarding policies.
  * Regional ILBs with Gratuitous ARP / Router Advertisement (`GARP_RA`) Fast IP Move high availability.
  * Zonal network endpoint groups (NEGs) for management and NSX datapath interfaces.



## Before you begin

Before you run the Terraform automation, install the required tools, enable the required APIs, allowlist Layer 2 subnet networking, and verify the following requirements for your Google Cloud project:

  1. Ensure that your project has sufficient bare-metal node quota in your target region and zone. For required quotas and instructions on how to view or request quota increases, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas).
  2. Ensure that you have the required Identity and Access Management (IAM) permissions, including `Compute Admin` (`roles/compute.admin`) and, if you use Cloud DNS, `DNS Administrator` (`roles/dns.admin`).
  3. Plan your Domain Name System (DNS) infrastructure to support forward and reverse lookups for all planned ESXi node hostnames and VCF appliance endpoints.
  4. **Node hostnames** : Provide the fully qualified domain name (FQDN) of each node during deployment. This ensures that ESXi generates certificates using hostnames.
  5. **Trusted image policy** : If your organization doesn't enforce the `constraints/compute.trustedImageProjects` organization policy, then no action is required. If your organization enforces this policy, then allow `projects/smve-prod-public-images` so that Compute Engine can create bare-metal boot disks. For more information, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).
  6. **VPC Service Controls** : If your target project isn't in a service perimeter, then no action is required. If your project is in a service perimeter, then add an egress rule that allows `compute.googleapis.com` operations to the `smve-prod-public-images` project (`projects/999037279871`):
         
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




### Install Terraform

You must install Terraform CLI version 1.3.0 or later. To install Terraform, select the tab for your operating system:

###  Debian or Ubuntu 

To install Terraform on Debian or Ubuntu, run the following commands:
    
    
    sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
    curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo 'deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com '"$(lsb_release -cs)"' main' | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt-get update && sudo apt-get install -y terraform
    

###  RHEL or CentOS 

To install Terraform on RHEL or CentOS, run the following commands:
    
    
    sudo yum install -y yum-utils
    sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
    sudo yum -y install terraform
    

###  Generic Linux 

To install Terraform by directly downloading the binary, run the following commands:
    
    
    export TERRAFORM_VERSION='1.9.5'
    curl -fsSLO 'https://releases.hashicorp.com/terraform/'"${TERRAFORM_VERSION}"'/terraform_'"${TERRAFORM_VERSION}"'_linux_amd64.zip'
    unzip 'terraform_'"${TERRAFORM_VERSION}"'_linux_amd64.zip'
    sudo mv terraform /usr/local/bin/
    rm 'terraform_'"${TERRAFORM_VERSION}"'_linux_amd64.zip'
    

### Enable Google Cloud APIs

Enable the following required APIs in your target Google Cloud project:

Service endpoint | Purpose  
---|---  
`compute.googleapis.com` | Bare-metal instances, Virtual Private Cloud (VPC) networks, Layer 2 subnets, firewalls, NEGs, regional ILBs, and static IP reservations.  
`dns.googleapis.com` | Private forward and reverse DNS managed zones, inbound forwarding policies, and DNS record sets.  
  
To enable the required APIs by using the `gcloud` CLI, run the following command:
    
    
    gcloud services enable \
        compute.googleapis.com \
        dns.googleapis.com \
        --project='PROJECT_ID'
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

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

### Allowlist VLAN-based Layer 2 subnet networking

VMware solution requires your Virtual Private Cloud (VPC) network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

  * **Product** : Google Cloud VMware Engine
  * **Priority** : P2
  * **Category** : Network Connectivity
  * **Business Impact** : General Technical question
  * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment



For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

### Configure organization policy and VPC Service Controls

Bare-metal ESXi instances in VMware solution boot from Google-provided ESXi images hosted in the `smve-prod-public-images` project, which has project number `999037279871`. By default, no additional configuration is required. Apply the following configurations only if your organization enforces a trusted image policy or uses VPC Service Controls:

  * **Trusted image policy** : If your organization doesn't enforce the `constraints/compute.trustedImageProjects` organization policy, then no action is required. If your organization enforces this policy, then allow `projects/smve-prod-public-images` so that Compute Engine can create bare-metal boot disks. For more information, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).
  * **VPC Service Controls egress rule** : If your target project isn't in a service perimeter, then no action is required. If your project is in a service perimeter, then add an egress rule that allows `compute.googleapis.com` operations to the `smve-prod-public-images` project (`projects/999037279871`):
        
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




## Configure IAM permissions and roles

The identity that runs Terraform (a human administrator or an automated CI/CD service account) requires the following IAM roles on the target Google Cloud project:

Role | Role ID | Scope of use  
---|---|---  
Compute Admin | `roles/compute.admin` | Provision bare-metal compute instances, attach custom boot disk images, configure placement policies, and manage multi-NIC interfaces. Manage VPC networks, Layer 2 broadcast subnets, static IP reservations, regional ILBs, backend services, forwarding rules, and zonal NEGs. Create and manage VPC ingress firewall security rules.  
DNS Administrator | `roles/dns.admin` | Manage Cloud DNS private forward and reverse zones, inbound query forwarding policies, and `A` and `PTR` resource record sets.  
Service Account User | `roles/iam.serviceAccountUser` | Grant this role on the default Compute Engine service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`) to allow instance provisioning with the `cloud-platform` scope.  
  
### Grant roles by using the gcloud CLI

To assign the required project-level roles and service account permissions, run the following commands:
    
    
    # Assign required project-level roles (use 'serviceAccount:SA_EMAIL' if granting to a service account)
    for ROLE in \
        roles/compute.admin \
        roles/dns.admin; do
      gcloud projects add-iam-policy-binding 'PROJECT_ID' \
          --member='user:USER_EMAIL' \
          --role=${ROLE}
    done
    # Grant Service Account User role on the Compute Engine default service account
    gcloud iam service-accounts add-iam-policy-binding \
        'PROJECT_NUMBER-compute@developer.gserviceaccount.com' \
        --member='user:USER_EMAIL' \
        --role='roles/iam.serviceAccountUser' \
        --project='PROJECT_ID'
    

Before you run the commands, replace the following:

  * `PROJECT_ID`: The ID of your target Google Cloud project.
  * `PROJECT_NUMBER`: The project number of your target Google Cloud project.
  * `USER_EMAIL`: The email address of your user identity.



## Authenticate the Terraform runner

Choose one of the following authentication strategies based on your operational environment:

  * Authenticate by using service account impersonation (recommended)
  * Authenticate by using Application Default Credentials
  * Authenticate by using a service account key file



### Authenticate by using service account impersonation

Service account impersonation eliminates long-lived credential keys by generating short-lived OAuth 2.0 access tokens. Your personal identity authenticates, while Terraform runs as the designated service account. Google Cloud audits actions performed by Terraform against the service account.

  1. Grant your personal Google Cloud identity the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on the runner service account:
         
         gcloud iam service-accounts add-iam-policy-binding 'SA_EMAIL' \
            --member='user:USER_EMAIL' \
            --role='roles/iam.serviceAccountTokenCreator' \
            --project='PROJECT_ID'
         

Before you run the command, replace the following:

     * `SA_EMAIL`: The email address of the Terraform runner service account.
     * `USER_EMAIL`: The email address of your personal Google Cloud identity.
     * `PROJECT_ID`: The ID of your target Google Cloud project.
  2. Authenticate your local environment:
         
         gcloud auth application-default login
         

  3. Set the `GOOGLE_IMPERSONATE_SERVICE_ACCOUNT` environment variable to enforce impersonation across Terraform executions:
         
         export GOOGLE_IMPERSONATE_SERVICE_ACCOUNT='SA_EMAIL'
         




### Authenticate by using Application Default Credentials

Use Application Default Credentials (ADC) in development and testing environments where your user identity holds the required permissions directly. Google Cloud audits actions against your personal identity:
    
    
    gcloud auth application-default login
    gcloud config set project 'PROJECT_ID'
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

### Authenticate by using a service account key file

Use a service account key file in automated CI/CD pipelines (such as Cloud Build, GitHub Actions, or Jenkins) where interactive user login isn't supported and authentication relies on long-lived service account credential keys. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file:
    
    
    export GOOGLE_APPLICATION_CREDENTIALS='KEY_FILE'
    

Replace `KEY_FILE` with the path to your service account JSON key.

## Review the modular architecture

Terraform coordinates resource provisioning across four modular stages. This modular design enforces strict dependency ordering to ensure that networking prerequisites exist before you deploy compute hosts, load balancers, and DNS records:
    
    
    +-----------------------------------------------------------------------------------+
    | STAGE 1: VPC Network Infrastructure, Firewalls & Cloud DNS (modules/vpc)          |
    | - Custom VPC Network (MTU 8896 jumbo frames)                                      |
    | - VPC Ingress Allow-All Firewall Rule                                             |
    | - Dedicated Standard Subnetwork (for DNS inbound resolver)                        |
    | - Cloud DNS Private Forward & Reverse Managed Zones                               |
    | - Cloud DNS Inbound Forwarding Policy (Dynamic DNS_RESOLVER IP discovery)         |
    +-----------------------------------------------------------------------------------+
                                             │
                                             ▼
    +-----------------------------------------------------------------------------------+
    | STAGE 2: L2 Broadcast Subnetworks & Zonal NEGs (modules/subnets)                  |
    | - Primary Management Subnet (Untagged Native VLAN, ARP broadcast learning)        |
    | - Storage & Infrastructure Subnets: vSAN (VLAN tagged), vMotion, NSX TEP          |
    | - Optional Dynamic Workload Subnets                                               |
    | - Zonal Network Endpoint Groups (GCE_VM_IP_DEDICATED_BACKEND) for Mgmt & NSX TEP   |
    +-----------------------------------------------------------------------------------+
                                             │
                                             ▼
    +-----------------------------------------------------------------------------------+
    | STAGE 3: Bare-Metal ESXi Hosts, IP Allocations & Host DNS (modules/hosts)         |
    | - Compute Resource Placement Policy (Availability Domain Count: 5-8, default: 6)  |
    | - Universal IP Allocator: Static reservations & dynamic allocation for all NICs   |
    | - Bare-Metal ESXi Instances (z3-highmem-192-highlssd-metal, 4+ Multi-NICs)        |
    | - Automated NEG Endpoint Attachments (in cluster_creation mode)                   |
    | - Cloud DNS Forward (A) and Reverse (PTR) Records for all ESXi Hosts              |
    +-----------------------------------------------------------------------------------+
                                             │
                                             ▼
    +-----------------------------------------------------------------------------------+
    | STAGE 4: Regional Internal Load Balancers & Appliances (modules/appliances)       |
    | - Regional Backend Services (GARP_RA Fast IP Move HA Policy)                      |
    | - Regional Forwarding Rules (L3_DEFAULT / ALL_PORTS / allow_global_access)        |
    | - Automated Cloud DNS Forward (A) and Reverse (PTR) Records for Mgmt Appliances   |
    +-----------------------------------------------------------------------------------+
    

## Provision resources for the management cluster

**Caution:** Each distinct cluster (the management domain management cluster or an individual workload domain data cluster) must use its own dedicated directory or isolated Terraform state backend.

The management domain management cluster hosts core VCF control plane appliances (SDDC Manager, vCenter Server, NSX Management cluster, and VMware Aria Suite) and ESXi hypervisors.

### Set up the Terraform workspace

Create a dedicated workspace directory and clone the toolkit repository by using Git:
    
    
    mkdir -p ~/vcf-deployments/mgmt-cluster
    cd ~/vcf-deployments/mgmt-cluster
    git clone https://github.com/GoogleCloudPlatform/self-managed-vmware-solution-toolkit
    

### Configure the variable definitions file

Create your variable definitions file (`management_cluster.tfvars`) with your target environment values. Copy the `sample_management_cluster.tfvars` file from the `e2e-terraform` directory into your `management_cluster.tfvars` file, and follow the inline instructions and comments to update any fields as needed:
    
    
    cp self-managed-vmware-solution-toolkit/e2e-terraform/sample_management_cluster.tfvars \
        self-managed-vmware-solution-toolkit/e2e-terraform/management_cluster.tfvars
    

### Apply the Terraform configuration

Go to the `self-managed-vmware-solution-toolkit/e2e-terraform` directory, and initialize and apply the Terraform configuration:
    
    
    cd self-managed-vmware-solution-toolkit/e2e-terraform
    terraform init
    terraform plan -var-file='management_cluster.tfvars' -out=tfplan
    terraform apply tfplan
    

## Review and export Terraform outputs

After you run `terraform apply`, Terraform exposes structured outputs across four categories:

  * `gcp_resources_self_links`: Complete Google Cloud resource self-link URLs for VPC networking, subnets, instances, placement policies, NEGs, backend services, forwarding rules, firewalls, and Cloud DNS zones.
  * `neg_attachment_commands`: 
    * When the `deployment_mode` variable is set to `"cluster_creation"`: Returns a status message indicating that Terraform automatically attaches NEGs during cluster creation.
    * When the `deployment_mode` variable is set to `"node_addition"`: Provides the `gcloud compute network-endpoint-groups update` commands required to attach newly provisioned ESXi host instances to both management and NSX NEGs.
    * When the `deployment_mode` variable is set to `"appliance_addition"`: Returns a status message indicating that NEGs remain attached to existing cluster nodes and that Terraform does not modify them during appliance addition.
  * `python_scripts_input_config`: Structured parameter configuration payload for the downstream VCF installer deployment automation scripts in the toolkit `python` directory. You can convert this output into the JSON format expected by the toolkit Python scripts by running the helper script described in the next section.
  * `management_domain_deployment_input_config`: Structured input for management domain deployment with most fields pre-populated from end-to-end provisioning. You can edit this input where required or indicated, and convert it into a JSON file for management domain deployment by using the export script described in the next section.



### Export deployment configurations

The toolkit includes a helper script (`scripts/export_deployment_config.py`) that extracts configuration blocks from Terraform outputs and exports them into formatted, schema-compliant JSON files for downstream workflows:

  * `management_domain_deployment_input_config`: Input JSON for the VCF management domain deployment.
  * `python_scripts_input_config`: Input JSON (`config.json`) for the toolkit Python automation scripts (`vcf_deployer`).



#### Run the helper script

Run the helper script from the `e2e-terraform` directory (or specify the `-d` or `-i` flags) by choosing one of the following options:

  * Export both configurations simultaneously:
        
        python3 ../scripts/export_deployment_config.py --config all --output-dir .
        

This command generates the following files:

    * `management_domain_deployment_input.json`
    * `python_scripts_input_config.json`
  * Export only the VCF management domain deployment input JSON:
        
        python3 ../scripts/export_deployment_config.py --config mgmt -o management_domain_deployment_input.json
        

  * Export only the Python toolkit input JSON:
        
        python3 ../scripts/export_deployment_config.py --config python -o config.json
        

  * Export from saved Terraform outputs or piped standard input (`stdin`):
        
        # From stdin pipe:
        terraform output -json | python3 ../scripts/export_deployment_config.py --config all --output-dir .
        
        # From a saved JSON file:
        terraform output -json > outputs.json
        python3 ../scripts/export_deployment_config.py -i outputs.json --config all --output-dir .
        




## What's next

**Caution:** For security, you must reset the initial ESXi `root` password on each newly provisioned bare-metal instance before use. Running the node preparation toolkit automatically resets the ESXi `root` password on each host to the `esxi-root-password` secret stored in Secret Manager. If you don't run the node preparation toolkit, you must manually reset the `root` password on each bare-metal ESXi instance.

  1. Run the node preparation toolkit to reset the initial ESXi `root` password on each host, prepare the nodes for VCF deployment, and deploy the VCF installer appliance by using the `python_scripts_input_config` output from the end-to-end Terraform configuration (converted into JSON by using the helper script). For instructions, see [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).
  2. Configure the connection to the regional offline depot in the VCF installer to download the required software bundles: 
     * **Protocol** : `HTTPS`
     * **FQDN** (don't use an IP address): `offline-depot.REGION.selfmanagedvmwareengine.goog` (replace `REGION` with the Google Cloud region where your bare-metal nodes reside)
     * **Port** : `443`
     * **Username** : `vcf-depot-user`
     * **Password** : `Google1!`
  3. Deploy the management domain by providing the `management_domain_deployment_input_config` JSON file (exported by using the helper script) to the VCF installer. Ensure that you replace all fields marked as `user_should_input` in the input configuration with your target values. For instructions on completing the VCF bring-up workflow, see [Deploy a new VCF fleet or a new VCF instance](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html) in the Broadcom documentation.
  4. Expand cluster capacity by adding nodes in [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform).
  5. Provision load balancers and DNS records for additional VCF appliances in [Add VCF appliances by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/vcf-appliance-addition).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
