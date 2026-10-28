---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster/
title: Add a vSphere cluster to a domain \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:05.108009+00:00
---

# Add a vSphere cluster to a domain  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add a vSphere cluster to a domain

This document describes how to add a vSphere cluster to an existing VMware Cloud Foundation (VCF) 9.1 domain in VMware solution on Google Cloud by using Compute Engine bare-metal instances. Add a cluster when you need to scale compute and vSAN storage capacity beyond a single cluster, isolate workloads, or apply separate vSphere Lifecycle Manager (vLCM) images or vSAN storage policies within an existing domain. You can add the cluster to either of the following domains in the same project, Virtual Private Cloud (VPC) network, and zone:

  * **Management domain** : Adds a cluster managed by the management vCenter Server and NSX Manager.
  * **VI workload domain** : Adds a cluster managed by the workload domain vCenter Server and its NSX Manager instance.



## Architecture summary

When you add a vSphere cluster to an existing VCF domain, the deployment uses the following architecture:

  * **Bare-metal ESXi hosts** : Each new ESXi host is a `z3-highmem-192-highlssd-metal` bare-metal instance attached to the existing Layer 2 subnets of your VPC network (ESXi management, vMotion, vSAN, and NSX Tunnel Endpoint (TEP)). Each host connects through a primary network interface (`nic0`) and VLAN-tagged Dynamic Network Interfaces.
  * **No additional management appliances** : Because you add the cluster to the vCenter Server and NSX Manager that already manage the target domain, you don't deploy new management appliances. You also don't create new appliance Cloud DNS records, backend services, high availability (HA) policies, or forwarding rules. Instead, you add the new hosts to the existing zonal network endpoint groups (NEGs).
  * **IP address allocation and alignment** : VCF allocates vMotion and vSAN IP addresses from a network pool, and NSX allocates TEP (`vmk10`) IP addresses from an NSX IP address pool. Because neither pool supports per-host static assignment in VCF 9.1, you align the Compute Engine Dynamic NICs with the VCF-allocated IP addresses during deployment while keeping all VCF validations enabled.



## Before you begin

Before you create the cluster, verify the requirements in the following sections and configure your environment variables.

### Verify environment requirements

Verify that your environment meets the following requirements:

  * **Permissions** : You have the required Identity and Access Management (IAM) roles on the target project, including Compute Admin (`roles/compute.admin`), DNS Administrator (`roles/dns.admin`), and Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`).
  * **Credentials in Secret Manager** : If you changed or rotated your ESXi `root`, SDDC Manager, vCenter Server, or NSX Manager passwords in VCF after initial deployment, Secret Manager isn't updated automatically. Before you run the commands in this document, update the corresponding secrets in Secret Manager or provide the updated passwords directly so that they match your active VCF credentials.
  * **Domain health** : The target domain is healthy (vCenter Server, vSAN, NSX Manager, SDDC Manager, and VCF Operations) and has no failed tasks.
  * **vSphere Lifecycle Manager (vLCM) image** : A vLCM image is available in the VCF image library, or you plan to extract an image from a host. Use the same image that your existing clusters use so that all hosts stay aligned.
  * **Storage devices** : Each new host has NVMe local SSD devices without pre-existing partitions, as required for vSAN.
  * **Minimum node count** : A cluster requires at least three bare-metal nodes, which is the minimum required for vSAN with one failure to tolerate (`FTT=1`).
  * **Machine type** : All nodes in the cluster use the same machine type (`z3-highmem-192-highlssd-metal` for vSAN Express Storage Architecture (ESA)).
  * **Zone** : The new cluster is in the same zone as the existing management and NSX TEP zonal NEGs.
  * **Jumpbox VM** : You have access to a jumpbox VM with the `gcloud` CLI, `curl`, and `jq` installed, and with network connectivity to the VPC network (for example, in the `bm-gcp-demo` subnet).
  * **Trusted image policy and VPC Service Controls** : If your organization enforces the `constraints/compute.trustedImageProjects` organization policy or uses a VPC Service Controls service perimeter, ensure that your project allows image access to the `smve-prod-public-images` project (`projects/999037279871`). For more information, see [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management#before-you-begin).
  * **VLAN-based networking** : VMware solution requires your VPC network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

    * **Product** : Google Cloud VMware Engine
    * **Priority** : P2
    * **Category** : Network Connectivity
    * **Business Impact** : General Technical question
    * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).




### Review example environment parameters

The commands in this document use the following example parameters:

Input parameter | Example value | Description  
---|---|---  
Project ID | `PROJECT_ID` | Same Google Cloud project as the target domain  
Region and zone | `us-east4` / `us-east4-b` | Same zone as the existing zonal NEGs  
Customer ID | `demo` | Identifier used in existing resource names  
Target domain | `mgmt-domain` (or `wld01`) | Existing management domain or VI workload domain  
Cluster name | `cl02` | Name of the new vSphere cluster  
Machine type | `z3-highmem-192-highlssd-metal` | Homogeneous machine type for all nodes in the cluster  
Node count | `3` | Minimum node count for vSAN `FTT=1`  
VPC network | `bm-demo` | Existing VPC network  
Subnets (VLAN ID) | `bm-mgmt-demo` (untagged), `bm-vmotion-demo` (`2`), `bm-vsan-demo` (`3`), `bm-nsx-demo` (`4`) | Existing Layer 2 subnets  
Zonal NEGs | `bm-mgmt-demo`, `bm-nsx-tep-demo` | Existing management and NSX TEP NEGs  
ESXi image | Family `astra-vcf-9-1-x`, project `smve-prod-offline-depot` | Same ESXi image build as the existing clusters  
DNS domain and zones | `vmware.gve` / `dns-zone-demo`, `rev-dns-zone-demo` | Existing Cloud DNS forward and reverse managed zones  
SDDC Manager | `sddcm.vmware.gve` (`192.168.0.3`) | Existing SDDC Manager appliance  
ESXi `root` password | `esxi-root-password` | Existing Secret Manager secret holding the ESXi `root` password  
  
### Plan IP addresses and hostnames

**Warning:** The new cluster shares the subnets of your existing domains. Hostnames and all host IP addresses must not overlap with the management domain (for example, hosts `esxi-h0` through `esxi-h3` using `192.168.0.131`–`192.168.0.134`, `192.168.2.3`–`192.168.2.6`, `192.168.3.3`–`192.168.3.6`, TEP pool `192.168.4.3`–`192.168.4.10`, and appliances using `192.168.0.3`–`192.168.0.19`) or with any workload domain (for example, hosts `esxi-h4` through `esxi-h6` using `192.168.0.151`–`192.168.0.153` and `.11`–`.13`, and appliances using `192.168.0.20`–`192.168.0.24`). Reusing IP addresses causes `IP_IN_USE` errors on Dynamic NICs.

The following table shows the example IP address plan for the three new ESXi hosts:

ESXi host | Management IP (`nic0`) | vMotion (VLAN 2) | vSAN (VLAN 3) | NSX TEP (VLAN 4)  
---|---|---|---|---  
`esxi-h7` | `192.168.0.161` | `192.168.2.21` | `192.168.3.21` | `192.168.4.21`  
`esxi-h8` | `192.168.0.162` | `192.168.2.22` | `192.168.3.22` | `192.168.4.22`  
`esxi-h9` | `192.168.0.163` | `192.168.2.23` | `192.168.3.23` | `192.168.4.23`  
  
### Choose the target domain

The target domain that you select determines which vCenter Server, NSX Manager, and overlay transport zone manage the new cluster:

Parameter or resource | Cluster in the management domain | Cluster in a VI workload domain  
---|---|---  
`TARGET_DOMAIN` variable | `mgmt-domain` | `wld01`  
Managing vCenter Server | `vc01.vmware.gve` | `vc02.vmware.gve`  
`NSX_MANAGER` variable | `nsx01.vmware.gve` (management NSX) | `nsx05.vmware.gve` (dedicated NSX) or `nsx01.vmware.gve` (shared management NSX)  
`TRANSPORT_ZONE` variable | `overlay-tz-mgmt-nsxt` | Overlay transport zone of the workload domain NSX instance  
  
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

### Set environment variables

Set the following environment variables in your jumpbox shell to use in the commands throughout this guide:
    
    
    export PROJECT_ID="PROJECT_ID"
    export REGION="us-east4"
    export ZONE="us-east4-b"
    export CUSTOMER_ID="demo"
    export VPC_NETWORK="bm-${CUSTOMER_ID}"
    export DOMAIN="vmware.gve"
    export DNS_ZONE="dns-zone-${CUSTOMER_ID}"
    export REV_DNS_ZONE="rev-dns-zone-${CUSTOMER_ID}"
    export MGMT_SUBNET="bm-mgmt-${CUSTOMER_ID}"
    export VMOTION_SUBNET="bm-vmotion-${CUSTOMER_ID}"
    export VSAN_SUBNET="bm-vsan-${CUSTOMER_ID}"
    export TEP_SUBNET="bm-nsx-${CUSTOMER_ID}"
    export MGMT_NEG="bm-mgmt-${CUSTOMER_ID}"
    export TEP_NEG="bm-nsx-tep-${CUSTOMER_ID}"
    export CLUSTER_NAME="cl02"
    export PLACEMENT_POLICY="bm-${CLUSTER_NAME}"
    export NETWORK_POOL_NAME="${CLUSTER_NAME}-np01"
    export TEP_POOL_NAME="${CLUSTER_NAME}-tep-pool"
    export VDS_NAME="${CLUSTER_NAME}-vds-01"
    export MACHINE_TYPE="z3-highmem-192-highlssd-metal"
    export ESXI_IMAGE_FAMILY="astra-vcf-9-1-x"
    export ESXI_IMAGE_PROJECT="smve-prod-offline-depot"
    export SDDC_MANAGER="sddcm.vmware.gve"            # 192.168.0.3
    export VCF_USER="admin@local"
    export VCF_PASSWORD="VCF_ADMIN_PASSWORD"
    export ESXI_PASSWORD_SECRET="esxi-root-password"  # Secret Manager secret holding the ESXi root password
    export MTU=8896                                   # VPC MTU
    
    # Target domain parameters
    export TARGET_DOMAIN="mgmt-domain"                # Or wld01
    export NSX_MANAGER="nsx01.vmware.gve"             # Or nsx05.vmware.gve for wld01 with a dedicated NSX instance
    export TRANSPORT_ZONE="overlay-tz-mgmt-nsxt"      # Overlay transport zone of the target NSX instance
    
    # Ordered host list: name mgmt_ip vmotion_ip vsan_ip tep_ip
    CLUSTER_HOSTS=(
      "esxi-h7 192.168.0.161 192.168.2.21 192.168.3.21 192.168.4.21"
      "esxi-h8 192.168.0.162 192.168.2.22 192.168.3.22 192.168.4.22"
      "esxi-h9 192.168.0.163 192.168.2.23 192.168.3.23 192.168.4.23"
    )
    
    # TEP pool range matching the new hosts' Compute Engine TEP NIC IPs
    export TEP_CIDR="192.168.4.0/24"
    export TEP_GATEWAY="192.168.4.1"
    export TEP_START="192.168.4.21"
    export TEP_END="192.168.4.23"
    

Before you run the commands, replace the following:

  * `PROJECT_ID`: the ID of your target Google Cloud project.
  * `VCF_ADMIN_PASSWORD`: your SDDC Manager administrator password.



Confirm that none of your planned IP addresses are already in use by existing forwarding rules or instances:
    
    
    gcloud compute forwarding-rules list --project="${PROJECT_ID}" --regions="${REGION}" \
        --format="table(name,IPAddress,subnetwork.basename())"
    gcloud compute instances list --project="${PROJECT_ID}" --zones="${ZONE}" \
        --format="table(name,networkInterfaces[].networkIP.list())"
    

## Create DNS records

When you deployed the management domain, you created the Layer 2 subnets, Cloud DNS inbound forwarding policy, and forward and reverse managed zones. Because adding a cluster doesn't deploy new appliances, you only need to create forward (`A`) and reverse (`PTR`) records for the new ESXi hosts:
    
    
    add_dns() {
      local name=$1 ip=$2
      gcloud dns record-sets create "${name}.${DOMAIN}." \
          --rrdatas="${ip}" --type=A --ttl=300 \
          --zone="${DNS_ZONE}" --project="${PROJECT_ID}"
      local rev
      rev=$(echo "${ip}" | awk -F. '{print $4"."$3"."$2"."$1".in-addr.arpa."}')
      gcloud dns record-sets create "${rev}" \
          --rrdatas="${name}.${DOMAIN}." --type=PTR --ttl=300 \
          --zone="${REV_DNS_ZONE}" --project="${PROJECT_ID}"
    }
    
    for entry in "${CLUSTER_HOSTS[@]}"; do
      read -r HOST MGMT_IP _ <<< "${entry}"
      add_dns "${HOST}" "${MGMT_IP}"
    done
    
    # Verify DNS records
    gcloud dns record-sets list --zone="${DNS_ZONE}" --project="${PROJECT_ID}" \
        --filter="name~'esxi-h[7-9]'"
    

## Create bare-metal instances

Create a dedicated placement policy for the new cluster. You then create each bare-metal ESXi host with a primary management interface (`nic0`) and VLAN-tagged Dynamic NICs for vMotion (VLAN 2), vSAN (VLAN 3), and NSX TEP (VLAN 4).

### Create a placement policy

**Caution:** Nodes that are assigned to a placement policy must belong to only one cluster so that availability domains map accurately to vSAN fault domains. Create a new placement policy for the new cluster.

Create the group placement policy:
    
    
    gcloud compute resource-policies create group-placement "${PLACEMENT_POLICY}" \
        --region="${REGION}" \
        --availability-domain-count=6 \
        --collocation=COLLOCATED \
        --project="${PROJECT_ID}"
    

### Create boot disks and bare-metal ESXi instances

Create the Google Cloud Hyperdisk Balanced boot disk and bare-metal ESXi instance for each host in the cluster:
    
    
    i=0
    for entry in "${CLUSTER_HOSTS[@]}"; do
      read -r HOST MGMT_IP VMOTION_IP VSAN_IP TEP_IP <<< "${entry}"
      AD=$(( (i % 6) + 1 )); i=$((i + 1))
    
      # Create boot disk
      gcloud compute disks create "${HOST}" \
          --image-project="${ESXI_IMAGE_PROJECT}" \
          --image-family="${ESXI_IMAGE_FAMILY}" \
          --type=hyperdisk-balanced --interface=NVME --size=128GB \
          --guest-os-features=IDPF \
          --zone="${ZONE}" --project="${PROJECT_ID}"
    
      # Create bare-metal ESXi host
      gcloud compute instances create "${HOST}" \
          --zone="${ZONE}" \
          --machine-type="${MACHINE_TYPE}" \
          --can-ip-forward \
          --resource-policies="${PLACEMENT_POLICY}" \
          --availability-domain="${AD}" \
          --hostname="${HOST}.${DOMAIN}" \
          --disk="name=${HOST},boot=yes,auto-delete=yes" \
          --labels=gcve-node=true \
          --tags=mm-gcve-node \
          --deletion-protection \
          --maintenance-policy=TERMINATE \
          --restart-on-failure \
          --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
          --project="${PROJECT_ID}" \
          --network-interface="network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=${MGMT_SUBNET},no-address,private-network-ip=${MGMT_IP}" \
          --network-interface="network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=${VMOTION_SUBNET},no-address,private-network-ip=${VMOTION_IP},vlan=2" \
          --network-interface="network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=${VSAN_SUBNET},no-address,private-network-ip=${VSAN_IP},vlan=3" \
          --network-interface="network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=${TEP_SUBNET},no-address,private-network-ip=${TEP_IP},vlan=4"
    done
    
    # Verify instance creation and network interfaces
    gcloud compute instances list --project="${PROJECT_ID}" --zones="${ZONE}" \
        --filter="name~'esxi-h[7-9]'" \
        --format="table(name,status,networkInterfaces[].vlan.list(),networkInterfaces[].networkIP.list())"
    

**Note:** The command configures each host with the `gcve-node=true` label and the `mm-gcve-node` network tag to match the node provisioning automation and firewall rules. The `--deletion-protection` flag prevents accidental deletion; clear this flag before you decommission and delete a node.

## Update NEG membership

All nodes in a zone must belong to the same zonal NEG of the subnet so that VCF network appliances can route traffic across cluster nodes. Add the new hosts to the existing management NEG and NSX TEP NEG:
    
    
    # List the NEGs in the zone (management and NSX TEP)
    gcloud compute network-endpoint-groups list --zones="${ZONE}" --project="${PROJECT_ID}" \
        --format="table(name,subnetwork.basename(),networkEndpointType,size)"
    
    ALL_NEGS=("${MGMT_NEG}" "${TEP_NEG}")
    for entry in "${CLUSTER_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"
      for NEG in "${ALL_NEGS[@]}"; do
        gcloud compute network-endpoint-groups update "${NEG}" \
            --zone="${ZONE}" \
            --add-endpoint="instance=${HOST}" \
            --project="${PROJECT_ID}"
      done
    done
    
    # Verify NEG endpoints
    for NEG in "${ALL_NEGS[@]}"; do
      gcloud compute network-endpoint-groups list-network-endpoints "${NEG}" \
          --zone="${ZONE}" --project="${PROJECT_ID}" \
          --format="table(networkEndpoint.instance,networkEndpoint.ipAddress)"
    done
    

**Note:** You don't need to modify backend services, HA policies, or forwarding rules. The vCenter Server and NSX Manager appliances that manage the new cluster already have load-balancing resources configured, and adding a cluster doesn't deploy new appliances. Don't change the HA policy leader of your existing appliances.

## Reset the ESXi root password

For security and host commissioning, reset the `root` password of each new host to the ESXi `root` password stored in Secret Manager. You use the same secret to commission the hosts in a later step. Ensure that the password meets VCF complexity requirements (at least 15 characters, including uppercase letters, lowercase letters, digits, and special characters). If you changed or rotated your ESXi `root` or VCF passwords after initial deployment, update the corresponding secret in Secret Manager before you run these commands.

To reset the `root` password on each new host, run the following commands from the jumpbox VM and enter the initial ESXi `root` password when prompted:
    
    
    # 1. Read the ESXi root password from Secret Manager
    ESXI_ROOT_PASSWORD=$(gcloud secrets versions access latest \
        --secret="${ESXI_PASSWORD_SECRET}" --project="${PROJECT_ID}")
    
    # 2. Reset the root password on each new host
    for entry in "${CLUSTER_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"
      ssh -o StrictHostKeyChecking=no "root@${HOST}.${DOMAIN}" \
          "esxcli system account set -i root -p '${ESXI_ROOT_PASSWORD}' -c '${ESXI_ROOT_PASSWORD}'"
    done
    
    # 3. Optional: Verify that the FQDN is set and vmk0 is configured as STATIC
    ssh "root@esxi-h7.${DOMAIN}" \
        'esxcli system hostname get; esxcli network ip interface ipv4 get -i vmk0'
    

**Caution:** If your password contains a single quotation mark (`'`), the remote SSH command fails. In that case, connect to each host interactively over SSH and run the `passwd root` command.

## Create a dedicated network pool

VCF allocates vMotion and vSAN IP addresses from the network pool that you select when commissioning hosts. Because the network pools of your existing clusters contain only their own host IP addresses, create a dedicated network pool whose IP ranges contain the exact vMotion and vSAN IP addresses that you pre-assigned to the new hosts' Compute Engine Dynamic NICs. Using a dedicated network pool keeps the VCF IP allocation within the set of pre-assigned Compute Engine IP addresses, so you only need to align the host-to-IP ordering later if a mismatch occurs.

You can create the network pool by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

In **VCF Operations** , go to **Network pool management** , click **Create network pool** , and create the `cl02-np01` network pool with the vMotion (VLAN `2`, `192.168.2.21`–`192.168.2.23`) and vSAN (VLAN `3`, `192.168.3.21`–`192.168.3.23`) network settings and an MTU of `8896` bytes.

###  SDDC Manager API 

Run the following commands to create the network pool and retrieve its ID:
    
    
    TOKEN=$(curl -s -X POST "https://${SDDC_MANAGER}/v1/tokens" \
        -H "Content-Type: application/json" \
        -d "{\"username\":\"${VCF_USER}\",\"password\":\"${VCF_PASSWORD}\"}" | jq -r '.accessToken')
    
    curl -s -X POST "https://${SDDC_MANAGER}/v1/network-pools" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "{
          \"name\": \"${NETWORK_POOL_NAME}\",
          \"networks\": [
            { \"type\": \"VMOTION\", \"vlanId\": 2, \"mtu\": ${MTU},
              \"subnet\": \"192.168.2.0\", \"mask\": \"255.255.255.0\", \"gateway\": \"192.168.2.1\",
              \"ipPools\": [ { \"start\": \"192.168.2.21\", \"end\": \"192.168.2.23\" } ] },
            { \"type\": \"VSAN\", \"vlanId\": 3, \"mtu\": ${MTU},
              \"subnet\": \"192.168.3.0\", \"mask\": \"255.255.255.0\", \"gateway\": \"192.168.3.1\",
              \"ipPools\": [ { \"start\": \"192.168.3.21\", \"end\": \"192.168.3.23\" } ] }
          ]
        }"
    
    # Retrieve the network pool ID for host commissioning
    POOL_ID=$(curl -s "https://${SDDC_MANAGER}/v1/network-pools" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r --arg n "${NETWORK_POOL_NAME}" '.elements[] | select(.name==$n) | .id')
    echo "${POOL_ID}"
    

**Note:** Configure an MTU of `8896` bytes (matching the VPC network MTU) for vMotion, vSAN, and the vSphere Distributed Switch (VDS). Don't reuse the network pool of an existing cluster because its free IP addresses don't match the IP addresses on the new hosts' Compute Engine NICs.

## Commission the hosts

Commission the new ESXi hosts into the SDDC Manager inventory by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

  1. In **VCF Operations** , go to **Inventory** > **Hosts** > **Commission Hosts**.
  2. Select the `cl02-np01` network pool and select the **vSAN ESA** storage type.
  3. Enter the host FQDNs (`esxi-h7.vmware.gve`, `esxi-h8.vmware.gve`, and `esxi-h9.vmware.gve`) and `root` credentials.
  4. Accept the SSL thumbprints, validate the hosts, and click **Commission**.



###  SDDC Manager API 

Run the following commands to validate and commission the hosts, and then poll the task ID until it returns `Successful`:
    
    
    ESXI_PASSWORD=$(gcloud secrets versions access latest \
        --secret="${ESXI_PASSWORD_SECRET}" --project="${PROJECT_ID}")
    
    HOST_FQDNS=$(for entry in "${CLUSTER_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"; echo "${HOST}.${DOMAIN}"
    done | jq -R . | jq -s .)
    
    HOSTS_JSON=$(jq -n --argjson f "${HOST_FQDNS}" --arg p "${ESXI_PASSWORD}" \
        --arg np "${POOL_ID}" --arg npn "${NETWORK_POOL_NAME}" \
        '$f | map({fqdn: ., username: "root", password: $p, storageType: "VSAN_ESA",
                   networkPoolId: $np, networkPoolName: $npn})')
    
    # 1. Validate hosts
    curl -s -X POST "https://${SDDC_MANAGER}/v1/hosts/validations" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" -d "${HOSTS_JSON}"
    
    # 2. Commission hosts
    TASK_ID=$(curl -s -X POST "https://${SDDC_MANAGER}/v1/hosts" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${HOSTS_JSON}" | jq -r '.id')
    
    # 3. Poll task status until Successful
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    

If a host SSL thumbprint displays an internal (non-FQDN) certificate name, the DNS search domain isn't configured on the host. On the affected ESXi host, run the `esxcli network ip dns search add -d vmware.gve` command, re-run the `/var/lib/vmware/osdata/init.sh` script, and then run the `/sbin/generate-certificates` command and restart the `rhttpproxy` and `hostd` services (`/etc/init.d/rhttpproxy restart && /etc/init.d/hostd restart`).

## Check pre-deployment IP alignment

Keep all vSAN, vMotion, and network connectivity validations enabled in SDDC Manager. These validation checks pass only when the `vmk1` (vMotion) and `vmk2` (vSAN) IP addresses that VCF assigns to each host match the Compute Engine Dynamic NIC IP addresses of that host. If a mismatch occurs because SDDC Manager assigns pool IP addresses in a different host order, the cluster creation task pauses at the connectivity check. You then align the Dynamic NICs in a subsequent step before retrying the task.

  1. **Verify that the network pool range matches the Compute Engine vMotion and vSAN NIC IP addresses** : Confirm that the network pool contains only the IP addresses that you pre-assigned to the new hosts' Dynamic NICs (`192.168.2.21`–`192.168.2.23` and `192.168.3.21`–`192.168.3.23` in this example):
         
         # Inspect network pool definition
         curl -s "https://${SDDC_MANAGER}/v1/network-pools/${POOL_ID}" \
             -H "Authorization: Bearer ${TOKEN}" | jq '.networks[] | {type, vlanId, mtu, ipPools}'
         
         # Inspect Compute Engine dynamic NIC IPs per new host (VLAN 2 = vMotion, 3 = vSAN, 4 = TEP)
         for entry in "${CLUSTER_HOSTS[@]}"; do
           read -r HOST _ <<< "${entry}"
           echo "== ${HOST}"
           gcloud compute instances describe "${HOST}" --zone="${ZONE}" --project="${PROJECT_ID}" \
               --format="table(networkInterfaces[].name,networkInterfaces[].vlan,networkInterfaces[].networkIP)"
         done
         

  2. **Assign IP addresses in ascending hostname order** : Pre-assign the Compute Engine IP addresses in ascending hostname order (`esxi-h7` → `.21`, `esxi-h8` → `.22`, `esxi-h9` → `.23`) so that the set of IP addresses is identical on both sides.

  3. **Confirm that SDDC Manager doesn't bypass validations** : On the SDDC Manager appliance (as `root`), verify that the `application.properties` file doesn't contain any `validation.disable.*` properties:
         
         # Must return no output. If any validation.disable.* line is present, remove it
         # and run: systemctl restart domainmanager
         grep -n 'validation.disable' /etc/vmware/vcf/domainmanager/application.properties
         

If you add the cluster by using the SDDC Manager API, don't set the `"skipValidations": true` property in the request body.

  4. **Size the NSX TEP pool to match the Compute Engine TEP NIC IP addresses** : Configure a new static NSX TEP IP address pool for the cluster with the range `192.168.4.21`–`192.168.4.23` (from the `TEP_START` variable to the `TEP_END` variable), matching the IP addresses on the new hosts' VLAN 4 Dynamic NICs, and set the gateway to `192.168.4.1`.




## Add the cluster

You can add the cluster to your target domain by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

Sign in to **VCF Operations** , go to **Inventory** , expand **VCF Instances** , select the target domain (`mgmt-domain` or `wld01`), and click **Add cluster** (or in the SDDC Manager UI, go to **Workload Domains** > _target domain_ > **Actions** > **Add Cluster**). Complete the wizard by using the following settings:

Wizard page | Field | Value  
---|---|---  
Storage | Type | **vSAN** , **Enable vSAN ESA** , **vSAN HCI** , data-in-transit encryption off  
Cluster | Cluster name | `cl02`  
Image | vLCM image | Select the image that your existing clusters use, or select **Extract an image from a host in this VCF instance** (by using `esxi-h7`)  
Hosts | Hosts | `esxi-h7`, `esxi-h8`, `esxi-h9` (commissioned as vSAN ESA with the `cl02-np01` network pool)  
vSphere Distributed Switch | Profile | **Default** (single VDS) or custom: 1 uplink (`uplink1` → `vmnic0`), MTU `8896`, traffic types ESX Management, VM Management, vMotion, vSAN, and NSX  
NSX switch mode | Virtual switch operational mode | Clear **Apply the default virtual switch mode configured in NSX Manager** and set **Operational Mode** to **Standard**. VMware solution hosts don't support the default mode (**Enhanced Datapath Standard**).  
NSX host overlay | TEP VLAN and IP assignment | VLAN `4` (matching the existing NSX configuration), **Static IP pool** (don't use DHCP): new pool `cl02-tep-pool`, CIDR `192.168.4.0/24`, range `192.168.4.21`–`192.168.4.23`, gateway `192.168.4.1`  
Review | Submit | Click **Finish**. Go to **Fleet Management** > **Tasks** to monitor the task and record the task ID (`TASK_ID`).  
**Note:** The default VDS profile doesn't create a port group for workload VMs. If the cluster runs VMs on a VLAN-backed network, create a distributed port group after you create the cluster or use a custom switch configuration.

###  SDDC Manager API 

Retrieve the target domain ID, vLCM image personality ID, and commissioned host IDs, and then validate and submit the specification for creating the cluster:
    
    
    # 1. Retrieve target domain ID, vLCM image personality ID, and host specs
    DOMAIN_ID=$(curl -s "https://${SDDC_MANAGER}/v1/domains" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r --arg d "${TARGET_DOMAIN}" '.elements[] | select(.name==$d) | .id')
    
    curl -s "https://${SDDC_MANAGER}/v1/personalities" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r '.elements[] | [.personalityId, .personalityName] | @tsv'
    IMAGE_ID="PERSONALITY_ID"   # Select the personalityId of the existing clusters' image
    
    HOST_SPECS=$(curl -s "https://${SDDC_MANAGER}/v1/hosts" -H "Authorization: Bearer ${TOKEN}" \
        | jq --argjson f "${HOST_FQDNS}" --arg vds "${VDS_NAME}" '
            [.elements[] | select(.fqdn as $x | $f | index($x))
             | {id, hostNetworkSpec: {vmNics: [{id: "vmnic0", uplink: "uplink1", vdsName: $vds}]}}]')
    echo "${HOST_SPECS}" | jq 'length'   # Must equal 3
    
    # 2. Construct the cluster specification (without skipValidations)
    CLUSTER_SPEC=$(jq -n \
        --arg domain "${DOMAIN_ID}" --arg name "${CLUSTER_NAME}" --arg img "${IMAGE_ID}" \
        --argjson hosts "${HOST_SPECS}" --arg vds "${VDS_NAME}" --argjson mtu "${MTU}" \
        --arg tz "${TRANSPORT_ZONE}" --arg pool "${TEP_POOL_NAME}" \
        --arg cidr "${TEP_CIDR}" --arg gw "${TEP_GATEWAY}" --arg s "${TEP_START}" --arg e "${TEP_END}" '
    {
      domainId: $domain,
      computeSpec: { clusterSpecs: [{
        name: $name,
        clusterImageId: $img,
        hostSpecs: $hosts,
        datastoreSpec: { vsanDatastoreSpec: { datastoreName: ($name + "-vsan"), esaConfig: { enabled: true } } },
        networkSpec: {
          vdsSpecs: [{
            name: $vds, mtu: $mtu,
            portGroupSpecs: [
              { name: ($vds + "-pg-mgmt"),    transportType: "MANAGEMENT", activeUplinks: ["uplink1"], teamingPolicy: "loadbalance_loadbased" },
              { name: ($vds + "-pg-vmotion"), transportType: "VMOTION",    activeUplinks: ["uplink1"], teamingPolicy: "loadbalance_loadbased" },
              { name: ($vds + "-pg-vsan"),    transportType: "VSAN",       activeUplinks: ["uplink1"], teamingPolicy: "loadbalance_loadbased" }
            ],
            nsxtSwitchConfig: {
              transportZones: [ { name: $tz, transportType: "OVERLAY" } ],
              hostSwitchOperationalMode: "STANDARD"
            }
          }],
          nsxClusterSpec: { nsxTClusterSpec: {
            uplinkProfiles: [{ name: ($name + "-uplink-profile"),
              teamings: [ { policy: "LOADBALANCE_SRCID", activeUplinks: ["uplink-1"] } ],
              transportVlan: 4 }],
            ipAddressPoolsSpec: [{ name: $pool,
              subnets: [{ cidr: $cidr, gateway: $gw, ipAddressPoolRanges: [ { start: $s, end: $e } ] }] }]
          }},
          networkProfiles: [{
            name: ($name + "-network-profile"), isDefault: true,
            nsxtHostSwitchConfigs: [{
              vdsName: $vds, uplinkProfileName: ($name + "-uplink-profile"), ipAddressPoolName: $pool,
              vdsUplinkToNsxUplink: [ { vdsUplinkName: "uplink1", nsxUplinkName: "uplink-1" } ]
            }]
          }]
        }
      }]}
    }')
    
    # 3. Validate the cluster specification
    curl -s -X POST "https://${SDDC_MANAGER}/v1/clusters/validations" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${CLUSTER_SPEC}" | jq '{executionStatus, resultStatus}'
    
    # 4. Create the cluster and poll the task
    TASK_ID=$(curl -s -X POST "https://${SDDC_MANAGER}/v1/clusters" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${CLUSTER_SPEC}" | jq -r '.id')
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    

Before you run the commands, replace `PERSONALITY_ID` with the `personalityId` value of your cluster vLCM image.

If VCF assigns a host a vMotion or vSAN IP address that differs from its Compute Engine Dynamic NIC, the task stops at the verification step for vSAN and vMotion connectivity. Leave the task in the failed state, complete the steps in Align vMotion and vSAN dynamic NICs, and then retry the task. Don't cancel the task or disable the validation check.

**Caution:** Always configure the gateway in the TEP IP address pool. A missing gateway causes the `NSX_VDL2` agent and host status to report `Degraded` even when Bidirectional Forwarding Detection (BFD) is up. If the wizard rejects a CIDR value, enter it in `gateway/prefix` format (for example, `192.168.4.1/24`).

## Align vMotion and vSAN dynamic NICs

Apply the steps in this section if the cluster creation task stops at the verification step for vSAN and vMotion connectivity. If the task passes that step, run only steps 1 and 2 to confirm IP alignment, and then proceed to Align NSX TEP dynamic NICs.

  1. **Read the VCF-allocated IP addresses** : Query the SDDC Manager `/v1/hosts` endpoint (or the SDDC Manager `platform` database) to review which vMotion (`vmk1`) and vSAN (`vmk2`) IP addresses VCF allocated to each host:
         
         curl -s "https://${SDDC_MANAGER}/v1/hosts" -H "Authorization: Bearer ${TOKEN}" | jq -r '
           ["FQDN","STATUS","CLUSTER","MGMT_IP","VMOTION_IP","VSAN_IP"],
           (.elements | sort_by(.fqdn)[] | [
              .fqdn, (.status // "-"), (.cluster.name // .cluster.id // "-"),
              (([.ipAddresses[]? | select(.type=="MANAGEMENT") | .ipAddress] | first) // "-"),
              (([.ipAddresses[]? | select(.type=="VMOTION")    | .ipAddress] | first) // "-"),
              (([.ipAddresses[]? | select(.type=="VSAN")       | .ipAddress] | first) // "-")
           ]) | @tsv' | column -t
         
         # Alternative (run on the SDDC Manager appliance shell):
         # psql -h localhost -U postgres -d platform \
         #   -c "select hostname, vmotion_ip_address, vsan_ip_address from host;"
         

  2. **Compare with the Compute Engine Dynamic NICs** : List the current Dynamic NIC IP addresses on each new host:
         
         for entry in "${CLUSTER_HOSTS[@]}"; do
           read -r HOST _ <<< "${entry}"
           echo "== ${HOST}"
           gcloud compute instances describe "${HOST}" --zone="${ZONE}" --project="${PROJECT_ID}" \
               --format="table(networkInterfaces[].name,networkInterfaces[].vlan,networkInterfaces[].networkIP)"
         done
         

  3. **Delete all mismatched Dynamic NICs first, and then add them back** : Delete every mismatched Dynamic NIC (the `nic0.2` interface for vMotion and the `nic0.3` interface for vSAN) across all mismatched hosts before you re-add any interface; otherwise, swapped IP addresses between two hosts fail with an `IP_IN_USE` error:
         
         # Example: VCF assigned esxi-h7 vMotion 192.168.2.22 and vSAN 192.168.3.22
         HOST="esxi-h7"
         VCF_VMOTION_IP="192.168.2.22"
         VCF_VSAN_IP="192.168.3.22"
         
         # 3a. Delete mismatched NICs (run on all mismatched hosts before running 3b)
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.2 \
             --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.3 \
             --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         
         # 3b. Re-add the dynamic NICs with the VCF-allocated IP addresses
         # vMotion (VLAN 2)
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=2 \
             --network="${VPC_NETWORK}" --subnetwork="${VMOTION_SUBNET}" \
             --private-network-ip="${VCF_VMOTION_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         
         # vSAN (VLAN 3)
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=3 \
             --network="${VPC_NETWORK}" --subnetwork="${VSAN_SUBNET}" \
             --private-network-ip="${VCF_VSAN_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         

  4. **Retry the failed cluster task** : In **VCF Operations** , go to **Fleet Management** > **Tasks** to retry the task, or run the following SDDC Manager API command:
         
         curl -s -X PATCH "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" \
             -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
             -d '{"status": "RETRY"}'
         

The retried task runs the connectivity check for vSAN and vMotion again and succeeds after all Compute Engine Dynamic NICs match the VCF-assigned IP addresses.




## Align NSX TEP dynamic NICs

After NSX configures the hosts as transport nodes, verify and align the VLAN 4 NSX TEP (`vmk10`) Dynamic NICs on the new hosts.

  1. **Retrieve the NSX-allocated TEP IP addresses** : Query the NSX Manager of the target domain (`NSX_MANAGER`), or run the `esxcli network ip interface ipv4 get -i vmk10` command on each ESXi host:
         
         NSX_PW="NSX_ADMIN_PASSWORD"
         
         # Map transport node ID to hostname
         curl -s -u "admin:${NSX_PW}" "https://${NSX_MANAGER}/api/v1/transport-nodes" \
             | jq -r '.results[] | [.id, .display_name] | @tsv'
         
         # Map transport node ID to TEP device and IP address
         curl -s -u "admin:${NSX_PW}" "https://${NSX_MANAGER}/api/v1/transport-nodes/state" \
             | jq -r '.results[] | [.transport_node_id, .state,
                 ([.host_switch_states[]?.endpoints[]? | .device_name + "=" + .ip] | join(","))] | @tsv'
         

Before you run the commands, replace `NSX_ADMIN_PASSWORD` with the NSX Manager `admin` password (available from the SDDC Manager `/v1/credentials` endpoint or VCF Operations password management).

  2. **Compare with the Compute Engine TEP NIC (VLAN 4)** : Compare the NSX-assigned `vmk10` IP addresses against the VLAN 4 Dynamic NIC IP addresses on the new hosts (`esxi-h7`, `esxi-h8`, and `esxi-h9`). Only the new hosts are in scope; don't modify the TEP NICs of hosts in other clusters.

  3. **Recreate mismatched TEP NICs** : For all mismatched new hosts, first detach each host from the TEP NEG and delete the `nic0.4` interface across all mismatched hosts. You then re-add the `nic0.4` interface and re-attach the hosts to the TEP NEG:
         
         # Example: Compute Engine has 192.168.4.21 on esxi-h7, but NSX assigned 192.168.4.23
         HOST="esxi-h7"
         CURRENT_TEP_IP="192.168.4.21"
         NSX_TEP_IP="192.168.4.23"
         
         # 3a. Detach the host from the TEP NEG
         gcloud compute network-endpoint-groups update "${TEP_NEG}" \
             --zone="${ZONE}" --project="${PROJECT_ID}" \
             --remove-endpoint="instance=${HOST},ip=${CURRENT_TEP_IP}"
         
         # 3b. Delete the mismatched TEP NIC (nic0.4) on all mismatched hosts first
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.4 \
             --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         
         # 3c. Re-add nic0.4 with the NSX-allocated IP address
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=4 \
             --network="${VPC_NETWORK}" --subnetwork="${TEP_SUBNET}" \
             --private-network-ip="${NSX_TEP_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         
         # 3d. Re-attach the host to the TEP NEG
         gcloud compute network-endpoint-groups update "${TEP_NEG}" \
             --zone="${ZONE}" --project="${PROJECT_ID}" \
             --add-endpoint="instance=${HOST}"
         




## Verify the cluster deployment

After the cluster creation task completes and you align all Dynamic NICs, verify the following:

  * **vCenter Server (`vc01` or `vc02`)**: The `cl02` cluster and all three hosts are connected and healthy with no network alarms.
  * **vSAN** : For the `cl02` cluster, go to **Monitor** > **vSAN** > **Skyline Health** and confirm that all health checks pass and that the vSAN datastore shows the combined capacity of all three hosts.
  * **NSX Manager** : Go to **System** > **Fabric** > **Hosts** and confirm that each new host shows **Success** and **Up** , and that all overlay tunnels are up.
  * **VCF Operations** : The cluster status is **Active** in the target domain and the task list shows no failed tasks.
  * **Existing clusters** : All other clusters in the domain remain healthy.
  * **Optional** : Migrate a test VM by using vMotion between an existing cluster and the `cl02` cluster, and between hosts within the `cl02` cluster.



From an ESXi host shell (for example, `esxi-h7`), verify jumbo frame connectivity (`8896` MTU minus 28-byte IP/ICMP header = `8868` bytes) across the vMotion, vSAN, and NSX TEP interfaces:
    
    
    esxcli network ip interface ipv4 get                        # Verify vmk0, vmk1, vmk2, and vmk10 IPs
    vmkping -S vmotion -I vmk1 -d -s 8868 192.168.2.22          # vMotion
    vmkping -I vmk2 -d -s 8868 192.168.3.22                     # vSAN
    vmkping ++netstack=vxlan -I vmk10 -d -s 8868 192.168.4.22   # NSX TEP
    

### Optional: Configure vSAN failures to tolerate

For vSAN ESA, VCF creates and assigns a default datastore storage policy based on the cluster type and number of hosts. To configure the FTT setting explicitly, choose a policy supported by your cluster host count:

Failures to tolerate | Data placement scheme | Minimum hosts  
---|---|---  
`FTT=1` | RAID-1 (mirroring) or RAID-5 (erasure coding) | 3 (4 or more recommended to rebuild after a host failure or during maintenance)  
`FTT=2` | RAID-1 (mirroring) | 5  
`FTT=2` | RAID-6 (erasure coding) | 6  
  
To set the default storage policy in the vSphere Client of the target domain's vCenter Server (`vc01` or `vc02`), do the following:

  1. Deactivate automatic policy management for the vSAN ESA cluster so that vSAN doesn't overwrite your custom default policy.
  2. Go to **Policies and Profiles** > **VM Storage Policies** > **Create** , enable vSAN storage rules, and in the **Availability** section, select **Failures to tolerate** (for example, **1 failure - RAID-1 (Mirroring)** for 3 to 4 hosts, or **2 failures - RAID-6 (Erasure Coding)** for 6 or more hosts).
  3. Set the new policy as the datastore default: select the `cl02` vSAN datastore, go to **Configure** > **General** > **Default Storage Policy** > **Edit** , and select the new policy.
  4. Apply the policy to existing VMs (**VM Policies** > **Edit VM Storage Policies**). Go to **Monitor** > **vSAN** > **Virtual Objects** for the `cl02` cluster to verify compliance.



## Troubleshoot cluster creation

The following table lists common issues, causes, and resolutions when adding a vSphere cluster to a domain:

Issue | Cause | Resolution  
---|---|---  
vSAN and vMotion connectivity validation fails; new hosts report unhealthy | When you create or expand a cluster, SDDC Manager allocates `vmk1` and `vmk2` IP addresses from the network pool without preserving the host order. | Keep validations enabled. Create a dedicated network pool matching the Compute Engine NIC IP addresses, verify pre-deployment alignment, and if the task pauses at the connectivity check, align the Dynamic NICs and retry the task.  
NSX host status is `Degraded` or tunnels are down after you add the cluster | NSX Manager assigns TEP (`vmk10`) IP addresses from the IP pool randomly, so they might not match the Compute Engine TEP NIC; Dynamic NIC subnets don't support DHCP. | Use a dedicated TEP IP pool matching the Compute Engine TEP IP addresses and align the TEP Dynamic NICs after NSX host preparation.  
`NSX_VDL2` agent or host reports `Degraded` while BFD is up | The gateway IP address is missing in the NSX TEP IP pool. | Configure the subnet gateway (`192.168.4.1`) in the TEP IP pool.  
`IP_IN_USE` error when re-adding a Dynamic NIC | Two hosts swapped IP addresses, or a planned IP address overlaps with another cluster. | Delete all mismatched Dynamic NICs across all hosts first before re-adding any interface, and verify that your IP plan doesn't overlap with existing clusters.  
NSX virtual switch mode isn't supported | In VCF 9.x, the default NSX virtual switch mode is **Enhanced Datapath Standard** , which VMware solution hosts don't support. | Clear **Apply the default virtual switch mode configured in NSX Manager** and set **Operational Mode** to **Standard** (or `"hostSwitchOperationalMode": "STANDARD"` in the API specification). For more information, see [NSX virtual switch mode](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues#nsx-virtual-switch-mode).  
Hosts can't ping the subnet gateway (`.1`) | Google Cloud doesn't respond to ICMP echo requests on subnet gateway IP addresses. | Expected behavior; ignore gateway ping warnings.  
Time synchronization (NTP) configuration | Bare-metal hosts use the Compute Engine metadata server for time synchronization. | Use the metadata server IP address (`169.254.169.254`) directly as the NTP server.  
Host thumbprint or certificate shows an internal name | The DNS search domain isn't set on the host or the hostname has a trailing dot. | Run the `esxcli network ip dns search add -d vmware.gve` command, re-run the `/var/lib/vmware/osdata/init.sh` script, and then run the `/sbin/generate-certificates` command and restart the `rhttpproxy` and `hostd` services.  
Host commissioning fails | The `vmk0` VMkernel adapter still uses DHCP because the startup service didn't convert it. | Run the `esxcli network ip interface ipv4 get -i vmk0` command. If the type is `DHCP`, set it to static manually (for example, on `esxi-h7`: `esxcli network ip interface ipv4 set -i vmk0 -t static -I 192.168.0.161 -N 255.255.255.0 -g 192.168.0.1`).  
vSAN replication errors, vMotion timeouts, or NSX overlay fragmentation | VCF defaults the VDS, VMkernel adapters, and NSX profiles to an MTU of `9000` bytes, and the VPC network drops frames larger than `8896` bytes. | Configure an MTU of `8896` bytes on the VDS, network pool (vMotion and vSAN), and NSX uplink profile. For more information, see [VDS MTU mismatch](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues#vds-mtu-mismatch).  
Wizard prompts for a VLAN ID for the overlay port group | The default VDS profile requires the NSX host overlay VLAN ID. | Enter the TEP VLAN ID of your existing NSX configuration (`4` in this guide).  
No port group exists for workload VMs on the new cluster | The default VDS profile creates only infrastructure port groups. | Create a distributed port group for workload VMs after you create the cluster, or use a custom switch configuration.  
Hosts can't be added with the selected vLCM image | The cluster's vLCM image differs from the ESXi build installed on the hosts. | Use the same ESXi image family that your existing clusters use, or extract the image from one of the new hosts.  
  
## What's next

  * Expand or compact an existing cluster in [Add or remove nodes in a vSphere cluster](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster).
  * Manage bare-metal node capacity in the Google Cloud console in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).
  * Review cluster sizing and architecture guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Review common deployment and operational workarounds in [Known issues](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues).
  * Learn more about [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics) and [bare-metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
