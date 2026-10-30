---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit/
title: Prepare nodes and deploy VCF by using the toolkit \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:40:20.659906+00:00
---

# Prepare nodes and deploy VCF by using the toolkit  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare nodes and deploy VCF by using the toolkit

This page describes how to use the VMware solution on Google Cloud toolkit to prepare bare-metal ESXi nodes, configure vSwitch networking and vSAN datastores, and deploy the VMware Cloud Foundation (VCF) installer appliance.

## Overview

The VMware solution toolkit automates the initial setup of bare-metal ESXi instances deployed in your Google Cloud project. When executed from a jumpbox VM, the toolkit performs the following actions:

  1. **Host credential verification and password reset** : Connects to each bare-metal ESXi instance and resets the initial ESXi `root` password to the `esxi-root-password` secret stored in Secret Manager.
  2. **Network configuration** : Configures `vSwitch0` and creates VLAN-tagged port groups for the VCF installer network.
  3. **Storage configuration** : Initializes local SSDs into a `vsanDatastore` pool.
  4. **VCF installer deployment** : Downloads the VCF installer Open Virtual Appliance (OVA) from the offline depot, deploys the appliance onto a designated target ESXi host, injects network and DNS parameters, and initializes the installer.

**Caution:** For security, you must reset the initial ESXi `root` password on each newly provisioned bare-metal instance before use. Running the toolkit automatically resets the ESXi `root` password on each host to the `esxi-root-password` secret stored in Secret Manager. If you don't run the toolkit, you must manually reset the `root` password on each bare-metal ESXi instance.

### Choose a deployment path

You can run the toolkit by using one of the following approaches:

  * **Path one: Provision a jumpbox by using Terraform (Recommended)** : Use Terraform to provision a dedicated Compute Engine jumpbox VM inside the ESXi host VPC, VPC subnet, Cloud NAT gateway, and Identity-Aware Proxy (IAP) SSH firewall rules.
  * **Path two: Use an existing jumpbox VM** : Run the toolkit directly from an existing Linux VM located inside the ESXi host VPC in a subnet with Private Google Access enabled.



* * *

## Before you begin

Before running the toolkit, complete the following prerequisites:

### Allowlist VLAN-based Layer 2 subnet networking

VMware solution requires your Virtual Private Cloud (VPC) network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

  * **Product** : Google Cloud VMware Engine
  * **Priority** : P2
  * **Category** : Network Connectivity
  * **Business Impact** : General Technical question
  * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment



For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

### Enable required APIs

You must have an active Google Cloud project with billing enabled (this can be the same Google Cloud project in which the ESXi hosts reside or a separate jumpbox project). Enable the following APIs:

  * Compute Engine API (`compute.googleapis.com`) — for jumpbox and ESXi host projects
  * Identity and Access Management (IAM) API (`iam.googleapis.com`) — for jumpbox project
  * Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`) — for jumpbox and ESXi host projects
  * Cloud Identity-Aware Proxy API (`iap.googleapis.com`) — for jumpbox project
  * Secret Manager API (`secretmanager.googleapis.com`) — for ESXi host project



To enable the APIs by using the `gcloud` CLI, run the following command:
    
    
    gcloud services enable \
        compute.googleapis.com \
        iam.googleapis.com \
        cloudresourcemanager.googleapis.com \
        iap.googleapis.com \
        secretmanager.googleapis.com \
        --project='PROJECT_ID'
    

Replace `PROJECT_ID` with the ID of your target Google Cloud project.

### Configure IAM permissions

The toolkit workflow uses the following identities and roles:

  * **Terraform Invoker** : The user or CI/CD identity launching `terraform apply`. Requires Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) on the Terraform Runner service account if impersonating the runner.
  * **Terraform Runner** : The identity provisioning the Terraform infrastructure: 
    * Compute Network Admin (`roles/compute.networkAdmin`)
    * Compute Instance Admin v1 (`roles/compute.instanceAdmin.v1`)
    * Compute Security Admin (`roles/compute.securityAdmin`)
    * Service Account User (`roles/iam.serviceAccountUser`)
    * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) on the target project (if using automated IAM management with Terraform)
  * **Jumpbox SSH User** : The identity connecting to the jumpbox VM by using IAP: 
    * IAP Tunnel Resource Accessor (`roles/iap.tunnelResourceAccessor`)
    * Compute Viewer (`roles/compute.viewer`)
  * **Jumpbox Script Runner** : The user or service account executing the Python toolkit script on the jumpbox: 
    * Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`)
    * Compute Admin (`roles/compute.admin`)
    * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)
  * **VMware Engine network drift service agent (P4SA)** (`service-PROJECT_NUMBER@gcp-sa-network-drift.iam.gserviceaccount.com`): 
    * Compute Network Admin (`roles/compute.networkAdmin`)

**Note:** You can provision IAM roles automatically by running `terraform apply` in the `iam/` directory before deploying infrastructure, or an administrator can grant them manually.

### Store credentials in Secret Manager

The toolkit retrieves passwords at runtime from Secret Manager and uses the `esxi-root-password` secret to reset the initial `root` password on each bare-metal ESXi instance. Create secrets in your Google Cloud project for the ESXi `root` password, VCF `root` password, and VCF local user (`admin`) password:
    
    
    # 1. Create Secret for ESXi Host Root Password
    gcloud secrets create esxi-root-password \
        --replication-policy='automatic' \
        --project='PROJECT_ID'
    echo -n 'YOUR_ESXI_ROOT_PASSWORD' | gcloud secrets versions add esxi-root-password \
        --data-file=- \
        --project='PROJECT_ID'
    # 2. Create Secret for VCF Installer Root Password
    gcloud secrets create vcf-root-password \
        --replication-policy='automatic' \
        --project='PROJECT_ID'
    echo -n 'YOUR_VCF_ROOT_PASSWORD' | gcloud secrets versions add vcf-root-password \
        --data-file=- \
        --project='PROJECT_ID'
    # 3. Create Secret for VCF Local User Password
    gcloud secrets create vcf-localuser-password \
        --replication-policy='automatic' \
        --project='PROJECT_ID'
    echo -n 'YOUR_VCF_ADMIN_PASSWORD' | gcloud secrets versions add vcf-localuser-password \
        --data-file=- \
        --project='PROJECT_ID'
    

Before you run the commands, replace the following:

  * `PROJECT_ID`: the ID of your target Google Cloud project.
  * `YOUR_ESXI_ROOT_PASSWORD`: the new `root` password to set on your bare-metal ESXi hosts, replacing the initial instance password.
  * `YOUR_VCF_ROOT_PASSWORD`: the `root` password for the VCF installer appliance.
  * `YOUR_VCF_ADMIN_PASSWORD`: the local administrator user password for the VCF installer appliance.

**Caution:** Ensure that the `root` and local user passwords for the VCF installer and SDDC Manager, as well as the ESXi `root` password, meet Broadcom's password requirements. Weak or non-compliant passwords can cause VCF installer deployment or bring-up to fail. For more information, see [Default password requirements for VCF components](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/fleet-management/manage-passwords/default-password-requirements-for-vcf-components.html) in the Broadcom documentation.

* * *

## Provision a jumpbox by using Terraform

If you don't have an existing jumpbox with network connectivity to your ESXi hosts, use the provided Terraform modules to deploy a jumpbox VM.

### Clone the toolkit repository

Clone the toolkit repository to your local workstation:
    
    
    mkdir -p ~/smve-toolkit
    cd ~/smve-toolkit
    git clone https://github.com/GoogleCloudPlatform/self-managed-vmware-solution-toolkit
    cd self-managed-vmware-solution-toolkit/smve-toolkit-jumpbox-tf
    

### Configure Terraform variables

Go to the `infrastructure` directory and create the `terraform.tfvars` file:
    
    
    cd infrastructure
    cp terraform.tfvars.example terraform.tfvars
    

Update the `terraform.tfvars` file with your project parameters:
    
    
    project_id      = "PROJECT_ID"
    region          = "REGION"
    zone            = "ZONE" # Match target ESXi host zone
    # Network configuration
    create_subnet   = true
    vpc_name        = "VPC_NAME"
    subnet_name     = "smve-toolkit-subnet"
    subnet_cidr     = "10.10.0.0/28" # Minimum /29 required
    # Cloud NAT and egress
    enable_internet = true
    # Jumpbox VM instance
    jumpbox_name    = "smve-toolkit-jumpbox"
    

The following table describes key Terraform input variables:

Variable | Requirement | Default | Description  
---|---|---|---  
`project_id` | **Required** | None  | Google Cloud project ID where Terraform deploys the infrastructure.  
`region` | **Required** | None  | Target Google Cloud region (for example, `us-central1`).  
`zone` | Optional  | `${region}-a` | Target zone. Set this variable to match the zone of your bare-metal ESXi hosts to minimize latency.  
`vpc_name` | Conditional  | `""` | Name of the VPC network hosting the ESXi nodes. Required if the `create_subnet` variable is set to `true`.  
`create_subnet` | Optional  | `true` | Set to `true` to create a new subnet, or `false` to use an existing subnet.  
`subnet_name` | Optional  | `"smve-toolkit-subnet"` | Name of the subnetwork for the jumpbox VM. If the `create_subnet` variable is set to `false`, the subnet must exist in the `vpc_name` network.  
`subnet_cidr` | Conditional  | `""` | Primary IPv4 CIDR range (minimum `/29`). Required if the `create_subnet` variable is set to `true`.  
`enable_internet` | Optional  | `true` | Controls Cloud Router, Cloud NAT, and default route creation for internet egress. Set to `false` post-setup to tear down the NAT gateway, router, and route.  
`jumpbox_name` | Optional  | `"smve-toolkit-jumpbox"` | Name of the Compute Engine jumpbox VM.  
`machine_type` | Optional  | `"e2-micro"` | Machine type for the jumpbox VM instance.  
`boot_disk_size` | Optional  | `30` | Boot disk size in GB for the jumpbox VM instance (minimum 10 GB).  
`boot_disk_type` | Optional  | `"pd-balanced"` | Persistent disk type for jumpbox boot disk (`pd-balanced`, `pd-standard`, `pd-ssd`, `pd-extreme`).  
`boot_disk_image` | Optional  | `"debian-cloud/debian-12"` | OS boot disk image family or specific image `self_link`.  
`jumpbox_internal_ip` | Optional  | `""` | Static internal IPv4 address (for example, `"10.10.0.5"`), reserved IP name, or URI. Defaults to a dynamic ephemeral IP address.  
`service_account_email` | Optional  | `""` | Custom service account email to attach to the jumpbox VM. Defaults to the Compute Engine default service account.  
  
### Deploy the jumpbox infrastructure

Initialize and apply the Terraform configuration:
    
    
    export GOOGLE_IMPERSONATE_SERVICE_ACCOUNT='TERRAFORM_RUNNER_SA' # Optional: set only if impersonating a runner service account
    terraform init
    terraform validate
    terraform plan -out=tfplan
    terraform apply tfplan
    

Replace `TERRAFORM_RUNNER_SA` with the email address of the Terraform runner service account.

### Connect to the jumpbox by using IAP

Connect to the jumpbox VM by using IAP TCP forwarding (no public IP address required):
    
    
    gcloud compute ssh smve-toolkit-jumpbox \
        --project='PROJECT_ID' \
        --zone='ZONE' \
        --tunnel-through-iap
    

Before you run the command, replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project hosting the jumpbox VM.
  * `ZONE`: the Google Cloud zone where the jumpbox VM is deployed.

**Note:** Run all commands after this step from the jumpbox VM terminal unless noted otherwise.

* * *

## Use an existing jumpbox VM

If you bring an existing jumpbox VM, it must be a Linux Compute Engine VM located inside the same VPC network hosting the bare-metal ESXi nodes. This VPC placement requirement is mandatory to ensure network connectivity to the offline depot Private Service Connect (PSC) endpoint hosting the VCF installer OVA.

Before executing the toolkit, verify that your existing jumpbox VM satisfies the following requirements:

  1. **VPC placement** : You must deploy the VM within the VPC network hosting the ESXi nodes.
  2. **Google Cloud API access** : The subnetwork hosting the jumpbox VM must have Private Google Access enabled (`private_ip_google_access = true`) or outbound internet access to reach `secretmanager.googleapis.com`, `compute.googleapis.com`, and `iam.googleapis.com`.
  3. **Package installation egress** : Outbound HTTP/HTTPS access (by using Cloud NAT, a corporate proxy, or direct egress) to install Python dependencies.
  4. **API enablement and IAM permissions** : The identity running the script must have the `roles/secretmanager.secretAccessor`, `roles/compute.admin`, and `roles/resourcemanager.projectIamAdmin` roles on your Google Cloud project.
  5. **SSH connectivity** : The jumpbox must allow SSH ingress on TCP port 22 from the IAP IP range (`35.235.240.0/20`) or authorized public IP ranges, and the connecting identity must have the applicable roles (`roles/iap.tunnelResourceAccessor` and `roles/compute.viewer`).



* * *

## Set up the toolkit on the jumpbox

On your jumpbox terminal, install dependencies and download the toolkit script.

### Install system packages

Install Python 3, `pip`, `venv`, and Git:
    
    
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv git
    

### Obtain the toolkit scripts

Clone the repository or copy the scripts from your local workstation:

  * **Option A (clone by using Git)** :
        
        mkdir -p ~/smve-toolkit
        cd ~/smve-toolkit
        git clone https://github.com/GoogleCloudPlatform/self-managed-vmware-solution-toolkit
        cd self-managed-vmware-solution-toolkit/python
        

  * **Option B (copy from your local workstation by using`gcloud compute scp`)**:
        
        gcloud compute scp --recurse ./smve-toolkit smve-toolkit-jumpbox:~/ \
          --project='PROJECT_ID' \
          --zone='ZONE' \
          --tunnel-through-iap
        # On the jumpbox terminal, go to the copied folder:
        cd ~/smve-toolkit/python
        




### Create and activate a Python virtual environment
    
    
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    

* * *

## Configure the toolkit script config file

Create a `config.json` configuration file on the jumpbox VM to specify your target ESXi instances and VCF deployment settings.

### Configuration parameters

Parameter | Required | Data type | Description  
---|---|---|---  
`project` | Yes  | `string` | Target Google Cloud project ID where bare-metal ESXi instances reside.  
`zone` | Yes | `string` | Target Google Cloud zone where ESXi nodes reside.  
`gce_nodes` | Yes  | `list(string)` or `object` | Explicit list of bare-metal ESXi instance names (for example, `["vcf-mgmt-sample-node-1", "vcf-mgmt-sample-node-2"]`), or an object discovering instances by `prefix` (for example, `{"prefix": "vcf-mgmt-sample"}`) or `subnet` (`{"subnet": "vcf-mgmt-subnet"}`).  
`esxi_root_password_secret` | Yes  | `string` | Secret Manager secret name or resource path containing the ESXi root password.  
`vcf_deployment_config` | Optional  | `object` | Configuration object for VCF installer deployment and initialization. Omit this object if you don't need to deploy the VCF installer on any of the nodes being prepared.  
`└─ target_gce_node` | Conditional  | `string` | Target bare-metal node hosting the initial deployment workloads. Required if the `vcf_deployment_config` object is defined.  
`└─ vcf_appliance_root_password_secret` | Conditional  | `string` | Secret Manager secret name containing the VCF appliance root password.  
`└─ vcf_appliance_local_user_password_secret` | Conditional  | `string` | Secret Manager secret name containing the VCF appliance local user (admin) password.  
`└─ vcf_installer_ip_source` | Conditional  | `string` or `object` | IP address source for the VCF installer (SDDC Manager). Specify `{"reserved_address": "ADDRESS_NAME"}`, `{"forwarding_rule": "RULE_NAME"}`, or a direct resource URI string (for example, `projects/PROJECT_ID/regions/REGION/forwardingRules/RULE_NAME`).  
`└─ vcf_installer_fqdn` | Conditional  | `string` | Fully qualified domain name (FQDN) for the VCF installer (SDDC Manager).  
`└─ offline_depot_subnet_cidr` | Conditional  | `string` | Primary IPv4 CIDR range for the dedicated offline depot subnet (for example, `/29`). Must not overlap with or reuse any existing subnets in the VPC.  
`└─ dns_server` | Optional  | `string` | DNS server IP address (for example, the reserved DNS IP from your subnet or a custom DNS server). Defaults to the Google Cloud metadata server (`169.254.169.254`) if omitted. Specify an IP address from a non-Layer 2 subnet if you use Cloud DNS.  
  
### Sample configurations

The following tabs show sample `config.json` configurations (based on templates available in the `python/examples/` directory) for different instance targeting approaches and IP allocation strategies:

###  Explicit node list 

Use this configuration (`python/examples/config_explicit_nodes.json`) to target specific ESXi instance names:
    
    
    {
    // Target Google Cloud project ID where bare-metal ESXi instances reside
    "project": "PROJECT_ID",
    // Target Google Cloud Compute Engine zone for ESXi instances
    "zone": "us-east4-c",
    // Explicit list of bare-metal ESXi Compute Engine instance names
    "gce_nodes": [
      "vcf-mgmt-sample-node-1",
      "vcf-mgmt-sample-node-2",
      "vcf-mgmt-sample-node-3",
      "vcf-mgmt-sample-node-4"
    ],
    // Secret Manager secret containing the ESXi root password
    "esxi_root_password_secret": "esxi-root-password",
    // Optional Jumpbox logging configuration (defaults to ~/logs/vcf_deployer_<timestamp>.log).
    // DEBUG level is default for file logs and console level can be controlled by "log_level" (defaults to INFO).
    // "log_dir": "~/logs",
    // "log_file": "~/logs/vcf_deployer_custom.log",
    // "log_level": "INFO",
    // VCF deployment and initialization parameters
    "vcf_deployment_config": {
      // Target bare-metal node hosting the initial deployment workloads
      "target_gce_node": "vcf-mgmt-sample-node-1",
      // IPv4 CIDR range for dedicated offline depot subnetwork (for example, /29). Must not overlap with or reuse any existing subnets in the VPC
      "offline_depot_subnet_cidr": "10.2.100.0/29",
      // Secret Manager secret containing the VCF appliance root password
      "vcf_appliance_root_password_secret": "vcf-root-password",
      // Secret Manager secret containing the VCF appliance local user password
      "vcf_appliance_local_user_password_secret": "vcf-localuser-password",
      // Source identifier for the VCF Installer (SDDC Manager) IP address
      "vcf_installer_ip_source": {
        "forwarding_rule": "vcf-mgmt-sddcm-fr"
      },
      // Fully qualified domain name for SDDC Manager / VCF Installer
      "vcf_installer_fqdn": "sddcm.gcve-vcf.test.gve",
      // DNS server IP. If gcp_subnet was created during Cloud DNS configuration from E2E TF, use the DNS reserved IP from that subnet. Otherwise, supply a custom DNS server IP. Defaults to Google Cloud metadata server (169.254.169.254) if omitted.
      "dns_server": "10.0.100.2"
    }
    }
    

###  Node name prefix filter 

Use this configuration (`python/examples/config_prefix_filter.json`) to dynamically discover ESXi instances matching a name prefix and use a forwarding rule:
    
    
    {
    // Target Google Cloud project ID where bare-metal ESXi instances reside
    "project": "PROJECT_ID",
    // Target Google Cloud Compute Engine zone for ESXi instances
    "zone": "us-east4-c",
    // Discover ESXi instances matching a given instance name prefix
    "gce_nodes": {
      "prefix": "vcf-mgmt-sample"
    },
    // Secret Manager secret containing the ESXi root password
    "esxi_root_password_secret": "esxi-root-password",
    // Optional Jumpbox logging configuration (defaults to ~/logs/vcf_deployer_<timestamp>.log).
    // DEBUG level is default for file logs and console level can be controlled by "log_level" (defaults to INFO).
    // "log_dir": "~/logs",
    // "log_file": "~/logs/vcf_deployer_custom.log",
    // "log_level": "INFO",
    // VCF deployment and initialization parameters
    "vcf_deployment_config": {
      // Target bare-metal node hosting the initial deployment workloads
      "target_gce_node": "esxi-node-0",
      // IPv4 CIDR range for dedicated offline depot subnetwork (for example, /29). Must not overlap with or reuse any existing subnets in the VPC
      "offline_depot_subnet_cidr": "10.2.100.0/29",
      // Secret Manager secret containing the VCF appliance root password
      "vcf_appliance_root_password_secret": "vcf-root-password",
      // Secret Manager secret containing the VCF appliance local user password
      "vcf_appliance_local_user_password_secret": "vcf-localuser-password",
      // Source identifier for the VCF Installer (SDDC Manager) forwarding rule
      "vcf_installer_ip_source": {
        "forwarding_rule": "vcf-mgmt-sddcm-fr"
      },
      // Fully qualified domain name for SDDC Manager / VCF Installer
      "vcf_installer_fqdn": "sddcm.gcve-vcf.test.gve",
      // DNS server IP. If gcp_subnet was created during Cloud DNS configuration from E2E TF, use the DNS reserved IP from that subnet. Otherwise, supply a custom DNS server IP. Defaults to Google Cloud metadata server (169.254.169.254) if omitted.
      "dns_server": "10.0.100.2"
    }
    }
    

###  Subnet discovery filter 

Use this configuration (`python/examples/config_subnet_filter.json`) to dynamically discover ESXi instances attached to a specific subnet and supply a full resource URI for the IP source:
    
    
    {
    // Target Google Cloud project ID where bare-metal ESXi instances reside
    "project": "PROJECT_ID",
    // Target Google Cloud Compute Engine zone for ESXi instances
    "zone": "us-east4-c",
    // Discover ESXi instances attached to a specific primary management subnet
    "gce_nodes": {
      "subnet": "vcf-mgmt-subnet"
    },
    // Secret Manager secret containing the ESXi root password
    "esxi_root_password_secret": "esxi-root-password",
    // Optional Jumpbox logging configuration (defaults to ~/logs/vcf_deployer_<timestamp>.log).
    // DEBUG level is default for file logs and console level can be controlled by "log_level" (defaults to INFO).
    // "log_dir": "~/logs",
    // "log_file": "~/logs/vcf_deployer_custom.log",
    // "log_level": "INFO",
    // VCF deployment and initialization parameters
    "vcf_deployment_config": {
      // Target bare-metal node hosting the initial deployment workloads
      "target_gce_node": "esxi-node-0",
      // IPv4 CIDR range for dedicated offline depot subnetwork (for example, /29). Must not overlap with or reuse any existing subnets in the VPC
      "offline_depot_subnet_cidr": "10.2.100.0/29",
      // Secret Manager secret containing the VCF appliance root password
      "vcf_appliance_root_password_secret": "vcf-root-password",
      // Secret Manager secret containing the VCF appliance local user password
      "vcf_appliance_local_user_password_secret": "vcf-localuser-password",
      // Direct resource URI for the VCF Installer (SDDC Manager) forwarding rule
      "vcf_installer_ip_source": "projects/PROJECT_ID/regions/us-east4/forwardingRules/vcf-mgmt-sddcm-fr",
      // Fully qualified domain name for SDDC Manager / VCF Installer
      "vcf_installer_fqdn": "sddcm.gcve-vcf.test.gve",
      // DNS server IP. If gcp_subnet was created during Cloud DNS configuration from E2E TF, use the DNS reserved IP from that subnet. Otherwise, supply a custom DNS server IP. Defaults to Google Cloud metadata server (169.254.169.254) if omitted.
      "dns_server": "10.0.100.2"
    }
    }
    

###  Node preparation only (no VCF installer) 

Omit the `vcf_deployment_config` object in the `config.json` file if you don't need to deploy the VCF installer appliance on any of the nodes being prepared (for example, when preparing nodes for day-2 node addition or workload data cluster creation):
    
    
    {
    "project": "PROJECT_ID",
    "zone": "ZONE",
    "gce_nodes": {
      "subnet": "SUBNET_NAME"
    },
    "esxi_root_password_secret": "esxi-root-password"
    }
    

Replace the following in your `config.json` file (and remove any inline comments before running the Python script):

  * `PROJECT_ID`: the ID of the Google Cloud project where your bare-metal ESXi instances reside.
  * `ZONE`: the Google Cloud zone where your bare-metal ESXi instances reside (for example, `us-east4-c`).
  * `SUBNET_NAME`: the name of the VPC subnet attached to your ESXi instances (for example, `vcf-mgmt-subnet`).



* * *

## Run the toolkit script

Authenticate with Google Cloud by using Application Default Credentials on the jumpbox terminal:
    
    
    gcloud auth application-default login --no-browser
    

**Note:** If the preceding command doesn't work in your environment, run `gcloud auth application-default login` without the `--no-browser` flag.

With your virtual environment active (`source venv/bin/activate`) and `config.json` configured, execute the toolkit:
    
    
    python3 -m vcf_deployer.main --config config.json
    

### Execution workflow

The script runs automated validation checks and executes the following setup stages:

  1. **Pre-flight validation** : Confirms that target instances run supported ESXi images, validates Secret Manager access, verifies IP CIDR alignment, and computes SSL certificate thumbprints.
  2. **Credential configuration and password reset** : Connects to each host and resets the initial ESXi `root` password to the `esxi-root-password` secret stored in Secret Manager.
  3. **vSwitch and port group creation** : Configures `vSwitch0` and creates VLAN-tagged port groups (`vlan-VLAN_ID-RANDOM_SUFFIX`).
  4. **vSAN initialization** : Formats local NVMe SSDs into a `vsanDatastore`.
  5. **VCF installer deployment** : Deploys the VCF OVA onto `target_gce_node`, injects network configuration, and starts the appliance.



After execution completes, deactivate the virtual environment:
    
    
    deactivate
    

* * *

## Post-deployment tasks

After running the toolkit and deploying the VCF installer appliance, perform the following post-deployment configuration:

### Disable internet egress on jumpbox (optional)

After Python dependencies are installed, you can tear down Cloud NAT to enforce strict egress security. In your workstation `terraform.tfvars`:
    
    
    enable_internet = false
    

**Caution:** If Terraform created the subnet, keep `create_subnet = true` when updating `enable_internet = false`. Changing `create_subnet` from `true` to `false` instructs Terraform to stop managing the subnet, scheduling it for deletion.

Re-apply Terraform:
    
    
    terraform apply
    

### Review known issues before you proceed

Review all documented issues on the [Known issues](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues) page before you start the VCF deployment. Overlooking these issues can cause deployment failures.

* * *

## Troubleshooting

This section describes how to diagnose and resolve common issues when configuring or executing the toolkit.

### Inspect toolkit execution logs on the jumpbox

When you run the toolkit on the jumpbox, the Python script writes detailed execution logs to the `~/logs/` directory in the jumpbox home directory. Each log file is named `vcf_deployer_TIMESTAMP.log`. If a node preparation or VCF installer deployment step fails, inspect the most recent `vcf_deployer_*.log` file in `~/logs/` to diagnose the failure.

### VCF installer deployment failure due to weak passwords

  * **Symptom** : The Python toolkit script fails or behaves unexpectedly during VCF installer deployment and initialization.
  * **Resolution** : Don't store weak passwords in Secret Manager because weak passwords can cause the Python script for VCF installer deployment to fail. Ensure that the `root` and local user passwords for the VCF installer and SDDC Manager, as well as the ESXi `root` password, meet Broadcom's password requirements. For more information, see [Default password requirements for VCF components](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/fleet-management/manage-passwords/default-password-requirements-for-vcf-components.html) in the Broadcom documentation.



### Permission denied (`roles/iam.serviceAccountTokenCreator`)

  * **Symptom** : Errors during service account impersonation while running Terraform.
  * **Resolution** : Ensure that the identity running Terraform has `roles/iam.serviceAccountTokenCreator` granted on the Terraform runner service account.



### IAP SSH connection failure (403 Forbidden / timeout)

  * **Symptom** : `gcloud compute ssh` fails to establish an IAP tunnel.
  * **Resolution** : 
    * Verify that the Cloud Identity-Aware Proxy API (`iap.googleapis.com`) is enabled.
    * Ensure that your user identity has `roles/iap.tunnelResourceAccessor` and `roles/compute.viewer`.
    * Verify that firewall rule `allow-iap-ssh-*` exists and permits ingress from `35.235.240.0/20` on TCP port 22.



### Subnet deletion warning on re-apply (`create_subnet` flag)

  * **Symptom** : Running `terraform apply` after setting `enable_internet = false` attempts to destroy the subnet.
  * **Resolution** : Keep `create_subnet = true` if Terraform created the subnet. Changing `create_subnet` to `false` instructs Terraform to stop managing the resource, scheduling it for deletion.



* * *

## What's next

  * **If you prepared the nodes and deployed a VCF installer for management domain deployment** : 
    1. Configure the connection to the regional offline depot in the VCF installer to download the required software bundles: 
       * **Protocol** : `HTTPS`
       * **FQDN** (don't use an IP address): `offline-depot.REGION.selfmanagedvmwareengine.goog` (replace `REGION` with the Google Cloud region where your bare-metal nodes reside)
       * **Port** : `443`
       * **Username** : `vcf-depot-user`
       * **Password** : `Google1!`
    2. Deploy the management domain: 
       * If you provisioned your Google Cloud resources by using the end-to-end Terraform modules ([Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform)), convert the `management_domain_deployment_input_config` Terraform output to JSON by using the helper script (`scripts/export_deployment_config.py`), replace all fields marked as `user_should_input` with your target values, and supply the JSON file to the VCF installer.
       * If you provisioned your Google Cloud resources without using the end-to-end Terraform modules, provide the management domain configuration inputs manually in the VCF installer.
       * For instructions on completing the VCF installer bring-up workflow, see [Deploy a new VCF fleet or a new VCF instance](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html) in the Broadcom documentation.
  * **If you prepared the nodes for adding to an existing cluster** : Add the prepared nodes to your VMware VCF 9.x cluster by using the VMware UI or APIs.
  * Learn how to add and remove nodes in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management) or [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
