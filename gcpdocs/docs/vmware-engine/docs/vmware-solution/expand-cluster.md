---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster/
title: Add or remove nodes in a vSphere cluster \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:00.136323+00:00
---

# Add or remove nodes in a vSphere cluster  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add or remove nodes in a vSphere cluster

This document describes how to add one or more Compute Engine bare-metal nodes to an existing vSphere cluster (_cluster expansion_) and remove one or more nodes from a cluster (_cluster compaction_) in VMware Cloud Foundation (VCF) 9.1 in VMware solution on Google Cloud. Expand or compact a cluster when you need to increase or reduce the compute and vSAN storage capacity of an existing cluster in the management domain or a VI workload domain. The same procedure applies whether you add or remove a single node or multiple nodes: list one or more nodes in the `ADD_HOSTS` or `REMOVE_HOSTS` environment variable.

## Architecture summary

When you add or remove nodes in an existing vSphere cluster, the workflow uses the following architecture:

  * **Adding nodes** : Each new node is a `z3-highmem-192-highlssd-metal` bare-metal instance that you deploy in the same zone, placement policy, and machine type as the existing nodes of the cluster. Each node has a primary network interface (`nic0`) on the ESXi management subnet of your Virtual Private Cloud (VPC) network and VLAN-tagged Dynamic Network Interfaces for vMotion, vSAN, and NSX Tunnel Endpoint (TEP). The node joins the existing zonal network endpoint groups (NEGs). You then commission the node in SDDC Manager with the cluster's network pool and add it to the cluster.
  * **Removing nodes** : You first remove the node from the cluster in VCF, which migrates the workload VMs and evacuates the host's vSAN data. You then decommission the host from SDDC Manager and remove it from the zonal NEGs before you delete the underlying Compute Engine bare-metal instance.
  * **IP address alignment** : As with cluster creation, VCF allocates vMotion and vSAN IP addresses from the cluster's network pool, and NSX allocates TEP (`vmk10`) IP addresses from the NSX IP address pool. You align the Compute Engine Dynamic NICs of the new nodes with the VCF-allocated IP addresses while keeping all VCF validations enabled.
  * **No appliance changes** : Adding or removing cluster nodes doesn't require new Cloud DNS records, backend services, high availability (HA) policies, or forwarding rules for management appliances.



## Before you begin

Before you add or remove nodes, verify the requirements in the following sections and configure your environment variables.

### Verify environment requirements

Verify that your environment meets the following requirements:

  * **Permissions** : You have the required Identity and Access Management (IAM) roles on the target project, including Compute Admin (`roles/compute.admin`), DNS Administrator (`roles/dns.admin`), and Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`).
  * **Credentials in Secret Manager** : If you changed or rotated your ESXi `root`, SDDC Manager, vCenter Server, or NSX Manager passwords in VCF after initial deployment, Secret Manager isn't updated automatically. Before you run the commands in this document, update the corresponding secrets in Secret Manager or provide the updated passwords directly so that they match your active VCF credentials.
  * **Cluster and domain health** : The target cluster and its domain are healthy (vCenter Server, vSAN, NSX Manager, SDDC Manager, and VCF Operations) and have no failed tasks.
  * **To add nodes** :

    * Your project has sufficient `z3` bare-metal quota in the target region and zone.
    * The new nodes use the same machine type as the existing nodes in the cluster (`z3-highmem-192-highlssd-metal` for vSAN Express Storage Architecture (ESA)) and are assigned to the cluster's existing placement policy (each placement policy belongs to only one cluster).
    * Each new node has NVMe local SSD devices without pre-existing partitions.
    * If your organization enforces the `constraints/compute.trustedImageProjects` organization policy or uses a VPC Service Controls service perimeter, ensure that your project allows image access to the `smve-prod-public-images` project (`projects/999037279871`). For more information, see [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management#before-you-begin).
    * **VLAN-based networking** : VMware solution requires your VPC network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

      * **Product** : Google Cloud VMware Engine
      * **Priority** : P2
      * **Category** : Network Connectivity
      * **Business Impact** : General Technical question
      * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

  * **To remove nodes** :

    * The remaining nodes have sufficient compute and vSAN storage capacity for your active workloads.
    * After node removal, the cluster retains at least three nodes (the minimum for vSAN with one failure to tolerate (`FTT=1`)) or the minimum host count that your active storage policies require (see vSAN failures to tolerate and host count).
  * **Jumpbox VM** : You have access to a jumpbox VM with the `gcloud` CLI, `curl`, and `jq` installed, and with network connectivity to the VPC network (for example, in the `bm-gcp-demo` subnet).




### Review example environment parameters

The commands in this document use the following example parameters:

Input parameter | Example value | Description  
---|---|---  
Project ID, region, and zone | `PROJECT_ID` / `us-east4` / `us-east4-b` | Same project, region, and zone as the target cluster  
Customer ID | `demo` | Identifier used in existing resource names  
Target cluster | `cl02` (`esxi-h7`, `esxi-h8`, `esxi-h9`) | Existing cluster in the management domain or a VI workload domain  
Placement policy | `bm-cl02` | Existing group placement policy of the cluster  
Network pool and VDS | `cl02-np01` / `cl02-vds-01` | Existing network pool and vSphere Distributed Switch (VDS) of the cluster  
NSX TEP IP pool | `cl02-tep-pool` | Existing NSX IP address pool of the cluster  
NSX Manager | `nsx01.vmware.gve` | NSX Manager of the cluster's domain (or `nsx05.vmware.gve` for the `wld01` workload domain with a dedicated NSX instance)  
Machine type | `z3-highmem-192-highlssd-metal` | Same machine type as the existing nodes in the cluster  
VPC network and subnets (VLAN ID) | `bm-demo`; `bm-mgmt-demo` (untagged), `bm-vmotion-demo` (`2`), `bm-vsan-demo` (`3`), `bm-nsx-demo` (`4`) | Existing VPC network and Layer 2 subnets  
Zonal NEGs | `bm-mgmt-demo`, `bm-nsx-tep-demo` | Existing management and NSX TEP NEGs  
SDDC Manager | `sddcm.vmware.gve` (`192.168.0.3`) | Existing SDDC Manager appliance  
ESXi `root` password | `esxi-root-password` | Existing Secret Manager secret that holds the ESXi `root` password  
  
### Plan IP addresses and hostnames

**Warning:** New nodes share the Layer 2 subnets of all existing domains and clusters. Hostnames and IP addresses must not overlap with any existing host or appliance (for example, management domain hosts using `192.168.0.131`–`192.168.0.134` and appliances using `192.168.0.3`–`192.168.0.19`; workload domain hosts using `192.168.0.151`–`192.168.0.153` and appliances using `192.168.0.20`–`192.168.0.24`; or `cl02` cluster hosts using `192.168.0.161`–`192.168.0.163` with vMotion, vSAN, and TEP `.21`–`.23`). Reusing IP addresses causes `IP_IN_USE` errors on Dynamic NICs.

The following example adds two nodes (`esxi-h10` and `esxi-h11`) to the `cl02` cluster, and then removes one of them (`esxi-h11`). To add or remove a single node, include only that node in your environment variable array:

ESXi host | Management IP (`nic0`) | vMotion (VLAN 2) | vSAN (VLAN 3) | NSX TEP (VLAN 4) | Availability domain | Action  
---|---|---|---|---|---|---  
`esxi-h10` | `192.168.0.164` | `192.168.2.24` | `192.168.3.24` | `192.168.4.24` | `4` | Add  
`esxi-h11` | `192.168.0.165` | `192.168.2.25` | `192.168.3.25` | `192.168.4.25` | `5` | Add, then remove  
  
Distribute the cluster's nodes across availability domains within the cluster's placement policy: because the existing nodes (`esxi-h7` through `esxi-h9`) use availability domains `1` through `3`, the new nodes use availability domains `4` and `5`.

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

Set the following environment variables in your jumpbox shell. List the nodes to add in the `ADD_HOSTS` environment variable and the nodes to remove in the `REMOVE_HOSTS` environment variable (one or more entries each):
    
    
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
    export PLACEMENT_POLICY="bm-${CLUSTER_NAME}"          # Existing placement policy of the cluster
    export NETWORK_POOL_NAME="${CLUSTER_NAME}-np01"        # Existing network pool of the cluster
    export VDS_NAME="${CLUSTER_NAME}-vds-01"               # Existing VDS of the cluster
    export MACHINE_TYPE="z3-highmem-192-highlssd-metal"    # Same machine type as existing nodes
    export ESXI_IMAGE_FAMILY="astra-vcf-9-1-x"
    export ESXI_IMAGE_PROJECT="smve-prod-offline-depot"
    export SDDC_MANAGER="sddcm.vmware.gve"                 # 192.168.0.3
    export VCF_USER="admin@local"
    export VCF_PASSWORD="VCF_ADMIN_PASSWORD"
    export ESXI_PASSWORD_SECRET="esxi-root-password"
    export NSX_MANAGER="nsx01.vmware.gve"                  # NSX Manager of the cluster's domain
    export MTU=8896
    
    # Nodes to add: name mgmt_ip vmotion_ip vsan_ip tep_ip availability_domain
    ADD_HOSTS=(
      "esxi-h10 192.168.0.164 192.168.2.24 192.168.3.24 192.168.4.24 4"
      "esxi-h11 192.168.0.165 192.168.2.25 192.168.3.25 192.168.4.25 5"
    )
    
    # Nodes to remove (short hostnames)
    REMOVE_HOSTS=(esxi-h11)
    
    # Retrieve an SDDC Manager API token (re-run when the token expires)
    TOKEN=$(curl -s -X POST "https://${SDDC_MANAGER}/v1/tokens" \
        -H "Content-Type: application/json" \
        -d "{\"username\":\"${VCF_USER}\",\"password\":\"${VCF_PASSWORD}\"}" | jq -r '.accessToken')
    

Before you run the commands, replace the following:

  * `PROJECT_ID`: the ID of your target Google Cloud project.
  * `VCF_ADMIN_PASSWORD`: your SDDC Manager administrator password.



Confirm that none of your planned IP addresses are already in use by existing forwarding rules or instances:
    
    
    gcloud compute forwarding-rules list --project="${PROJECT_ID}" --regions="${REGION}" \
        --format="table(name,IPAddress,subnetwork.basename())"
    gcloud compute instances list --project="${PROJECT_ID}" --zones="${ZONE}" \
        --format="table(name,networkInterfaces[].networkIP.list())"
    

## Add nodes to a cluster

To expand an existing vSphere cluster by adding bare-metal nodes, complete the steps in the following sections.

### Create DNS records

Because the forward and reverse Cloud DNS managed zones already exist, create forward (`A`) and reverse (`PTR`) records for the new nodes only:
    
    
    for entry in "${ADD_HOSTS[@]}"; do
      read -r HOST MGMT_IP _ <<< "${entry}"
      gcloud dns record-sets create "${HOST}.${DOMAIN}." \
          --rrdatas="${MGMT_IP}" --type=A --ttl=300 \
          --zone="${DNS_ZONE}" --project="${PROJECT_ID}"
      REV=$(echo "${MGMT_IP}" | awk -F. '{print $4"."$3"."$2"."$1".in-addr.arpa."}')
      gcloud dns record-sets create "${REV}" \
          --rrdatas="${HOST}.${DOMAIN}." --type=PTR --ttl=300 \
          --zone="${REV_DNS_ZONE}" --project="${PROJECT_ID}"
    done
    
    # Verify DNS records
    gcloud dns record-sets list --zone="${DNS_ZONE}" --project="${PROJECT_ID}" \
        --filter="name~'esxi-h1[01]'"
    

### Create bare-metal instances

Create each new node in the cluster's existing placement policy with the primary ESXi management NIC (`nic0`) and VLAN-tagged Dynamic NICs for vMotion (VLAN 2), vSAN (VLAN 3), and NSX TEP (VLAN 4).

**Caution:** Nodes that are assigned to a placement policy must belong to only one cluster so that availability domains map accurately to vSAN fault domains. Use the existing placement policy of the cluster that you're expanding; don't create a new placement policy.
    
    
    for entry in "${ADD_HOSTS[@]}"; do
      read -r HOST MGMT_IP VMOTION_IP VSAN_IP TEP_IP AD <<< "${entry}"
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
        --filter="resourcePolicies~${PLACEMENT_POLICY}" \
        --format="table(name,status,networkInterfaces[].vlan.list(),networkInterfaces[].networkIP.list())"
    

**Note:** The command configures each node with the `gcve-node=true` label, the `mm-gcve-node` network tag, and deletion protection to match the existing cluster nodes.

### Update NEG membership

All nodes of a cluster in a zone must belong to the same zonal NEG of the subnet. Add the new nodes to the management NEG and to the NSX TEP NEG. You don't need to modify HA policies or forwarding rules:
    
    
    for entry in "${ADD_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"
      for NEG in "${MGMT_NEG}" "${TEP_NEG}"; do
        gcloud compute network-endpoint-groups update "${NEG}" \
            --zone="${ZONE}" --add-endpoint="instance=${HOST}" --project="${PROJECT_ID}"
      done
    done
    
    # Verify NEG endpoints
    for NEG in "${MGMT_NEG}" "${TEP_NEG}"; do
      gcloud compute network-endpoint-groups list-network-endpoints "${NEG}" \
          --zone="${ZONE}" --project="${PROJECT_ID}" \
          --format="table(networkEndpoint.instance,networkEndpoint.ipAddress)"
    done
    

### Reset the ESXi root password

Reset the `root` password of each new node to match the ESXi `root` password stored in Secret Manager. You use the same secret to commission the nodes in a later step. If you changed or rotated your ESXi `root` or VCF passwords after initial deployment, update the corresponding secret in Secret Manager before you run these commands.

To reset the `root` password on each new node, run the following commands from the jumpbox VM and enter the initial ESXi `root` password when prompted:
    
    
    ESXI_ROOT_PASSWORD=$(gcloud secrets versions access latest \
        --secret="${ESXI_PASSWORD_SECRET}" --project="${PROJECT_ID}")
    
    for entry in "${ADD_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"
      ssh -o StrictHostKeyChecking=no "root@${HOST}.${DOMAIN}" \
          "esxcli system account set -i root -p '${ESXI_ROOT_PASSWORD}' -c '${ESXI_ROOT_PASSWORD}'"
    done
    

**Caution:** If your password contains a single quotation mark (`'`), the remote SSH command fails. In that case, connect to each host interactively over SSH and run the `passwd root` command.

### Add the new IP addresses to the network pool and the TEP pool

The cluster's network pool (`cl02-np01`) and NSX TEP pool (`cl02-tep-pool`) initially contain only the IP addresses of the existing cluster nodes. Add the exact Compute Engine Dynamic NIC IP addresses of the new nodes to both pools so that VCF and NSX allocate IP addresses from the set that is already configured on the Compute Engine NICs.

  1. **Update the network pool (vMotion and vSAN)** : Add the new nodes' vMotion and vSAN IP addresses to the `cl02-np01` network pool by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

In **VCF Operations** , go to **Network pool management** , select the `cl02-np01` network pool, edit the vMotion and vSAN networks, and add the IP address ranges for the new nodes.

###  SDDC Manager API 

Run the following commands to add one single-IP range per new node to the network pool:
         
         POOL_ID=$(curl -s "https://${SDDC_MANAGER}/v1/network-pools" -H "Authorization: Bearer ${TOKEN}" \
             | jq -r --arg n "${NETWORK_POOL_NAME}" '.elements[] | select(.name==$n) | .id')
         NETWORKS=$(curl -s "https://${SDDC_MANAGER}/v1/network-pools/${POOL_ID}/networks" \
             -H "Authorization: Bearer ${TOKEN}")
         VMOTION_NET_ID=$(echo "${NETWORKS}" | jq -r '.elements[] | select(.type=="VMOTION") | .id')
         VSAN_NET_ID=$(echo "${NETWORKS}" | jq -r '.elements[] | select(.type=="VSAN") | .id')
         
         for entry in "${ADD_HOSTS[@]}"; do
           read -r HOST MGMT_IP VMOTION_IP VSAN_IP _ <<< "${entry}"
           curl -s -X POST "https://${SDDC_MANAGER}/v1/network-pools/${POOL_ID}/networks/${VMOTION_NET_ID}/ip-pools" \
               -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
               -d "{\"start\":\"${VMOTION_IP}\",\"end\":\"${VMOTION_IP}\"}"
           curl -s -X POST "https://${SDDC_MANAGER}/v1/network-pools/${POOL_ID}/networks/${VSAN_NET_ID}/ip-pools" \
               -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
               -d "{\"start\":\"${VSAN_IP}\",\"end\":\"${VSAN_IP}\"}"
         done
         
         # Verify the network pool IP ranges
         curl -s "https://${SDDC_MANAGER}/v1/network-pools/${POOL_ID}/networks" -H "Authorization: Bearer ${TOKEN}" \
             | jq -r '.elements[] | [.type, (.ipPools | map(.start + "-" + .end) | join(","))] | @tsv'
         

  2. **Update the NSX TEP IP pool** : In NSX Manager (the `NSX_MANAGER` host), go to **Networking** > **IP Address Pools** , edit the `cl02-tep-pool` IP address pool, and add the new nodes' TEP IP addresses to the subnet's IP ranges (`192.168.4.24`–`192.168.4.25` in this example) while keeping the gateway set to `192.168.4.1`. Verify the updated pool configuration:
         
         NSX_PW="NSX_ADMIN_PASSWORD"
         curl -s -u "admin:${NSX_PW}" "https://${NSX_MANAGER}/policy/api/v1/infra/ip-pools" \
             | jq -r '.results[] | [.id, .display_name] | @tsv'
         
         TEP_POOL_ID="TEP_POOL_ID"   # ID of cl02-tep-pool from the preceding output
         curl -s -u "admin:${NSX_PW}" \
             "https://${NSX_MANAGER}/policy/api/v1/infra/ip-pools/${TEP_POOL_ID}/ip-subnets" \
             | jq '.results[] | {cidr, gateway_ip, allocation_ranges}'
         

Before you run the commands, replace the following:

     * `NSX_ADMIN_PASSWORD`: your NSX Manager `admin` password (available from the SDDC Manager `/v1/credentials` endpoint or VCF Operations).
     * `TEP_POOL_ID`: the ID of the `cl02-tep-pool` IP address pool.
**Note:** If the TEP pool has no free IP addresses, NSX can't prepare the new nodes. If the pools contain other free IP addresses (for example, IP addresses that were released by previously removed nodes), VCF or NSX might allocate those IP addresses instead of the new nodes' Compute Engine NIC IP addresses. If that happens, you align the NICs in Align vMotion and vSAN dynamic NICs and Align NSX TEP dynamic NICs.



### Commission the nodes

Commission the new nodes into the SDDC Manager inventory by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

  1. In **VCF Operations** , go to **Inventory** > **Hosts** > **Commission Hosts**.
  2. Select the `cl02-np01` network pool and select the **vSAN ESA** storage type.
  3. Enter the new host FQDNs and `root` credentials.
  4. Accept the SSL thumbprints, validate the hosts, and click **Commission**.



###  SDDC Manager API 

Run the following commands to validate and commission the hosts, and then poll the task status until it returns `Successful`:
    
    
    ADD_FQDNS=$(for entry in "${ADD_HOSTS[@]}"; do
      read -r HOST _ <<< "${entry}"; echo "${HOST}.${DOMAIN}"
    done | jq -R . | jq -s .)
    
    HOSTS_JSON=$(jq -n --argjson f "${ADD_FQDNS}" --arg p "${ESXI_ROOT_PASSWORD}" \
        --arg np "${POOL_ID}" --arg npn "${NETWORK_POOL_NAME}" \
        '$f | map({fqdn: ., username: "root", password: $p, storageType: "VSAN_ESA",
                   networkPoolId: $np, networkPoolName: $npn})')
    
    # 1. Validate hosts
    curl -s -X POST "https://${SDDC_MANAGER}/v1/hosts/validations" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" -d "${HOSTS_JSON}"
    
    # 2. Commission hosts and poll until Successful
    TASK_ID=$(curl -s -X POST "https://${SDDC_MANAGER}/v1/hosts" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${HOSTS_JSON}" | jq -r '.id')
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    

If a host SSL thumbprint displays an internal (non-FQDN) certificate name, run the `esxcli network ip dns search add -d vmware.gve` command on the host, re-run the `/var/lib/vmware/osdata/init.sh` script, and then run the `/sbin/generate-certificates` command and restart the `rhttpproxy` and `hostd` services.

### Check pre-expansion IP alignment

Keep all vSAN, vMotion, and network connectivity validations enabled in SDDC Manager. These validation checks pass only when the `vmk1` and `vmk2` IP addresses that VCF assigns to each new node match its Compute Engine Dynamic NIC IP addresses.

  1. **Verify that unused pool IP addresses match the new Compute Engine NIC IP addresses** : Compare the network pool ranges with the IP addresses that existing hosts already use and the Compute Engine NICs of the new nodes. The only pool IP addresses that existing hosts don't use should be the new nodes' IP addresses:
         
         # List vMotion and vSAN IP addresses already used by hosts
         curl -s "https://${SDDC_MANAGER}/v1/hosts" -H "Authorization: Bearer ${TOKEN}" | jq -r '
           .elements | sort_by(.fqdn)[] | [.fqdn,
             (([.ipAddresses[]? | select(.type=="VMOTION") | .ipAddress] | first) // "-"),
             (([.ipAddresses[]? | select(.type=="VSAN")    | .ipAddress] | first) // "-")] | @tsv'
         
         # List Compute Engine dynamic NIC IPs of the new nodes (VLAN 2 = vMotion, 3 = vSAN, 4 = TEP)
         for entry in "${ADD_HOSTS[@]}"; do
           read -r HOST _ <<< "${entry}"
           echo "== ${HOST}"
           gcloud compute instances describe "${HOST}" --zone="${ZONE}" --project="${PROJECT_ID}" \
               --format="table(networkInterfaces[].name,networkInterfaces[].vlan,networkInterfaces[].networkIP)"
         done
         

  2. **Confirm that SDDC Manager doesn't bypass validations** : On the SDDC Manager appliance (as `root`), verify that the `application.properties` file doesn't contain any `validation.disable.*` properties:
         
         # Must return no output. If any validation.disable.* line is present, remove it
         # and run: systemctl restart domainmanager
         grep -n 'validation.disable' /etc/vmware/vcf/domainmanager/application.properties
         




### Expand the cluster

Add the commissioned nodes to the target cluster by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

In **VCF Operations** (or the SDDC Manager UI), open the cluster's domain, select the `cl02` cluster, choose **Actions** > **Add Host** , select the commissioned nodes, map the `vmnic0` interface to the `uplink1` uplink of the cluster's VDS, and submit the workflow. Go to **Fleet Management** > **Tasks** to monitor the task and record its ID (set the `TASK_ID` variable to this value for the next section).

###  SDDC Manager API 

Run the following commands to validate the expansion specification and expand the cluster:
    
    
    CLUSTER_ID=$(curl -s "https://${SDDC_MANAGER}/v1/clusters" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r --arg c "${CLUSTER_NAME}" '.elements[] | select(.name==$c) | .id')
    
    HOST_SPECS=$(curl -s "https://${SDDC_MANAGER}/v1/hosts?status=UNASSIGNED_USEABLE" \
        -H "Authorization: Bearer ${TOKEN}" \
        | jq --argjson f "${ADD_FQDNS}" --arg vds "${VDS_NAME}" '
            [.elements[] | select(.fqdn as $x | $f | index($x))
             | {id, hostNetworkSpec: {vmNics: [{id: "vmnic0", uplink: "uplink1", vdsName: $vds}]}}]')
    echo "${HOST_SPECS}" | jq 'length'   # Must equal the number of ADD_HOSTS
    
    EXPANSION_SPEC=$(jq -n --argjson h "${HOST_SPECS}" \
        '{clusterExpansionSpec: {hostSpecs: $h, deployWithoutLicenseKeys: true}}')
    
    # 1. Validate (resolve any reported error before continuing)
    curl -s -X POST "https://${SDDC_MANAGER}/v1/clusters/${CLUSTER_ID}/validations" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${EXPANSION_SPEC}" | jq '{executionStatus, resultStatus}'
    
    # 2. Expand the cluster and poll the task
    TASK_ID=$(curl -s -X PATCH "https://${SDDC_MANAGER}/v1/clusters/${CLUSTER_ID}" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${EXPANSION_SPEC}" | jq -r '.id')
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    

When you expand a cluster, SDDC Manager allocates vMotion and vSAN IP addresses from the network pool without preserving the host order. If SDDC Manager assigns a new node an IP address that differs from its Compute Engine Dynamic NIC, the task pauses at the verification step for vSAN and vMotion connectivity. Leave the task in the failed state, complete the steps in Align vMotion and vSAN dynamic NICs, and then retry the same task. Don't start a new expansion request for these nodes: after a failed expansion, the nodes are no longer in the unassigned state, and SDDC Manager rejects a new expansion request.

### Align vMotion and vSAN dynamic NICs

Complete the steps in this section if the cluster expansion task pauses at the verification step for vSAN and vMotion connectivity. If the task passes that step, run only step 1 to confirm the alignment, and then proceed to Align NSX TEP dynamic NICs.

  1. **Read the VCF-allocated IP addresses and compare them with the Compute Engine NICs** : Run the two commands from step 1 of Check pre-expansion IP alignment. Only the new nodes are in scope.

  2. **Delete all mismatched Dynamic NICs first, and then add them back** : Delete every mismatched Dynamic NIC (the `nic0.2` interface for vMotion and the `nic0.3` interface for vSAN) on every new node before you re-add any interface; otherwise, swapped IP addresses fail with an `IP_IN_USE` error:
         
         # Example: VCF swapped the IP addresses of esxi-h10 and esxi-h11
         HOST="esxi-h10"
         VCF_VMOTION_IP="192.168.2.25"
         VCF_VSAN_IP="192.168.3.25"
         
         # 2a. Delete mismatched NICs (run on all mismatched nodes before running 2b)
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.2 --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.3 --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         
         # 2b. Add the dynamic NICs back with the VCF-allocated IP addresses
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=2 \
             --network="${VPC_NETWORK}" --subnetwork="${VMOTION_SUBNET}" \
             --private-network-ip="${VCF_VMOTION_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=3 \
             --network="${VPC_NETWORK}" --subnetwork="${VSAN_SUBNET}" \
             --private-network-ip="${VCF_VSAN_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         

  3. **Retry the failed task** : In **VCF Operations** , go to **Fleet Management**

> **Tasks** to retry the expansion task, or run the following SDDC Manager API command:
         
         curl -s -X PATCH "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" \
             -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
             -d '{"status": "RETRY"}'
         

If the task fails again, repeat steps 1 and 2 before retrying.




### Align NSX TEP dynamic NICs

After NSX configures the new nodes as transport nodes, verify and align the VLAN 4 NSX TEP (`vmk10`) Dynamic NICs on the new nodes.

  1. **Retrieve the NSX-allocated TEP IP addresses** : Query NSX Manager (or run the `esxcli network ip interface ipv4 get -i vmk10` command on each ESXi host):
         
         # Map transport node ID to hostname
         curl -s -u "admin:${NSX_PW}" "https://${NSX_MANAGER}/api/v1/transport-nodes" \
             | jq -r '.results[] | [.id, .display_name] | @tsv'
         
         # Map transport node ID to TEP device and IP address
         curl -s -u "admin:${NSX_PW}" "https://${NSX_MANAGER}/api/v1/transport-nodes/state" \
             | jq -r '.results[] | [.transport_node_id, .state,
                 ([.host_switch_states[]?.endpoints[]? | .device_name + "=" + .ip] | join(","))] | @tsv'
         

  2. **Recreate mismatched TEP NICs** : Compare the NSX-allocated `vmk10` IP addresses with the Compute Engine TEP NIC (VLAN 4) of each new node. Only the new nodes are in scope; don't modify the TEP NICs of existing nodes. For all mismatched new nodes, first detach each node from the TEP NEG and delete the `nic0.4` interface across all mismatched nodes. You then re-add the `nic0.4` interface and re-attach the nodes to the TEP NEG:
         
         # Example: Compute Engine has 192.168.4.24 on esxi-h10, but NSX assigned 192.168.4.25
         HOST="esxi-h10"
         CURRENT_TEP_IP="192.168.4.24"
         NSX_TEP_IP="192.168.4.25"
         
         # 2a. Detach the node from the TEP NEG
         gcloud compute network-endpoint-groups update "${TEP_NEG}" \
             --zone="${ZONE}" --project="${PROJECT_ID}" \
             --remove-endpoint="instance=${HOST},ip=${CURRENT_TEP_IP}"
         
         # 2b. Delete the mismatched TEP NIC on all mismatched nodes first
         gcloud compute instances network-interfaces delete "${HOST}" \
             --network-interface=nic0.4 --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
         
         # 2c. Re-add nic0.4 with the NSX-allocated IP address
         gcloud compute instances network-interfaces add "${HOST}" \
             --parent-nic-name=nic0 --vlan=4 \
             --network="${VPC_NETWORK}" --subnetwork="${TEP_SUBNET}" \
             --private-network-ip="${NSX_TEP_IP}" --no-address \
             --zone="${ZONE}" --project="${PROJECT_ID}"
         
         # 2d. Re-attach the node to the TEP NEG
         gcloud compute network-endpoint-groups update "${TEP_NEG}" \
             --zone="${ZONE}" --project="${PROJECT_ID}" \
             --add-endpoint="instance=${HOST}"
         




### Verify the cluster expansion

After the cluster expansion task succeeds, verify the following:

  * **vCenter Server** : The new nodes are connected and healthy in the `cl02` cluster with no network alarms.
  * **vSAN** : For the `cl02` cluster, go to **Monitor** > **vSAN** > **Skyline Health** and confirm that all health checks pass and that the datastore capacity includes the new nodes.
  * **NSX Manager** : Go to **System** > **Fabric** > **Hosts** and confirm that each new node shows **Success** and **Up** , and that overlay tunnels are up.
  * **VCF Operations** : The new nodes are assigned to the `cl02` cluster and the task list has no failed tasks.



From an ESXi host shell (for example, `esxi-h10`), verify jumbo frame connectivity (`8896` MTU minus 28-byte IP/ICMP header = `8868` bytes):
    
    
    esxcli network ip interface ipv4 get                        # Verify vmk0, vmk1, vmk2, and vmk10 IPs
    vmkping -S vmotion -I vmk1 -d -s 8868 192.168.2.21          # vMotion (netstack might be default)
    vmkping -I vmk2 -d -s 8868 192.168.3.21                     # vSAN
    vmkping ++netstack=vxlan -I vmk10 -d -s 8868 192.168.4.21   # NSX TEP
    

#### vSAN failures to tolerate and host count

Use the following table to determine how many nodes your cluster requires when you add nodes or must retain when you remove nodes:

Failures to tolerate | Data placement scheme | Minimum hosts  
---|---|---  
`FTT=1` | RAID-1 (mirroring) or RAID-5 (erasure coding) | 3 (4 or more recommended to rebuild after a host failure or during maintenance)  
`FTT=2` | RAID-1 (mirroring) | 5  
`FTT=2` | RAID-6 (erasure coding) | 6  
  
## Remove nodes from a cluster

**Warning:** Always remove and decommission a node in VCF before you delete its Compute Engine bare-metal instance. Deleting an instance without decommissioning it leaves orphaned host records and can make the cluster unstable. Deleting an instance permanently deletes all data on its local SSDs.

### Complete pre-removal checks

Before you remove any nodes from a cluster, verify the following:

  * **Host count** : After node removal, the cluster retains at least three nodes, and at least the minimum host count listed in vSAN failures to tolerate and host count that your active storage policies require.
  * **Capacity** : In vCenter Server, for the `cl02` cluster, go to **Monitor** > **vSAN** > **Data Migration Pre-check** for each node that you plan to remove (with the **Full data migration** option) and confirm that the remaining nodes have sufficient vSAN and compute capacity.
  * **Health** : vSAN Skyline Health passes with no errors and there are no failed tasks in VCF Operations or SDDC Manager.
  * **HA policy leaders** : Confirm that no backend service uses a node that you're removing as its HA policy leader. If a backend service uses one of those nodes as its leader, update the leader to a remaining node (the host that runs the appliance VM after migration):
        
        gcloud compute backend-services list --regions="${REGION}" --project="${PROJECT_ID}" \
            --format="table(name,haPolicy.leader.networkEndpoint.instance)"
        
        # Run only if a node being removed is an HA policy leader (example: move rbs-vc02-demo to esxi-h0)
        NEG_LINK=$(gcloud compute network-endpoint-groups describe "${MGMT_NEG}" \
            --zone="${ZONE}" --project="${PROJECT_ID}" --format="value(selfLink)")
        gcloud compute backend-services update "rbs-vc02-${CUSTOMER_ID}" \
            --ha-policy-leader-backend-group="${NEG_LINK}" --ha-policy-leader-instance=esxi-h0 \
            --region="${REGION}" --project="${PROJECT_ID}"
        




### Remove the nodes from the cluster

Remove the target nodes from the cluster in VCF. VCF places each node into maintenance mode, migrates its VMs, and evacuates its vSAN data. You can remove the nodes by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

In **VCF Operations** (or the SDDC Manager UI), open the cluster's domain, select the `cl02` cluster, choose **Actions** > **Remove Host** , select the nodes to remove, and confirm.

###  SDDC Manager API 

Run the following commands to validate the compaction specification and remove the hosts from the cluster:
    
    
    CLUSTER_ID=$(curl -s "https://${SDDC_MANAGER}/v1/clusters" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r --arg c "${CLUSTER_NAME}" '.elements[] | select(.name==$c) | .id')
    
    REMOVE_FQDNS=$(for HOST in "${REMOVE_HOSTS[@]}"; do echo "${HOST}.${DOMAIN}"; done | jq -R . | jq -s .)
    
    COMPACTION_SPEC=$(curl -s "https://${SDDC_MANAGER}/v1/hosts" -H "Authorization: Bearer ${TOKEN}" \
        | jq --argjson f "${REMOVE_FQDNS}" '
            {clusterCompactionSpec: {hosts: [.elements[] | select(.fqdn as $x | $f | index($x)) | {id}]}}')
    echo "${COMPACTION_SPEC}" | jq '.clusterCompactionSpec.hosts | length'   # Must equal the number of REMOVE_HOSTS
    
    # 1. Validate the compaction specification
    curl -s -X POST "https://${SDDC_MANAGER}/v1/clusters/${CLUSTER_ID}/validations" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${COMPACTION_SPEC}" | jq '{executionStatus, resultStatus}'
    
    # 2. Remove the hosts and poll the task until Successful
    TASK_ID=$(curl -s -X PATCH "https://${SDDC_MANAGER}/v1/clusters/${CLUSTER_ID}" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${COMPACTION_SPEC}" | jq -r '.id')
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    

**Caution:** Don't add the `"force": true` or `"forceByPassingSafeMinSize": true` properties to the compaction specification. These properties bypass validation and allow the cluster to have fewer hosts than its safe minimum size.

### Decommission the nodes

After you remove the nodes from the cluster, decommission them from the SDDC Manager inventory by using VCF Operations or the SDDC Manager API:

###  VCF Operations 

In **VCF Operations** , go to **Inventory** > **Hosts** , select the unassigned nodes, and click **Decommission** (for more information, see [Decommission hosts in the VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html)).

###  SDDC Manager API 

Run the following commands to send a decommission request and poll the task until it returns `Successful`:
    
    
    DECOMMISSION_SPEC=$(echo "${REMOVE_FQDNS}" | jq 'map({fqdn: .})')
    TASK_ID=$(curl -s -X DELETE "https://${SDDC_MANAGER}/v1/hosts?skipFailedHosts=false" \
        -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
        -d "${DECOMMISSION_SPEC}" | jq -r '.id')
    curl -s "https://${SDDC_MANAGER}/v1/tasks/${TASK_ID}" -H "Authorization: Bearer ${TOKEN}" | jq -r '.status'
    
    # Verify that the nodes are no longer listed in the inventory
    curl -s "https://${SDDC_MANAGER}/v1/hosts" -H "Authorization: Bearer ${TOKEN}" \
        | jq -r '.elements[] | [.fqdn, .status] | @tsv'
    

### Remove the nodes from the NEGs

Remove the decommissioned nodes from the management NEG and the NSX TEP NEG:
    
    
    for HOST in "${REMOVE_HOSTS[@]}"; do
      for NEG in "${MGMT_NEG}" "${TEP_NEG}"; do
        gcloud compute network-endpoint-groups update "${NEG}" \
            --zone="${ZONE}" --remove-endpoint="instance=${HOST}" --project="${PROJECT_ID}"
      done
    done
    
    # Verify NEG endpoints
    for NEG in "${MGMT_NEG}" "${TEP_NEG}"; do
      gcloud compute network-endpoint-groups list-network-endpoints "${NEG}" \
          --zone="${ZONE}" --project="${PROJECT_ID}" \
          --format="table(networkEndpoint.instance,networkEndpoint.ipAddress)"
    done
    

If the `gcloud` CLI rejects the removal from the TEP NEG without an explicit IP address, include the endpoint IP address (as shown by the verification command) in the `--remove-endpoint` flag: `--remove-endpoint="instance=HOST,ip=TEP_IP"`.

### Delete the bare-metal instances

Clear deletion protection on each decommissioned host and delete the Compute Engine bare-metal instance (Compute Engine automatically deletes the boot disk with the instance):
    
    
    for HOST in "${REMOVE_HOSTS[@]}"; do
      # Clear deletion protection, and then delete the instance and its boot disk
      gcloud compute instances update "${HOST}" --no-deletion-protection \
          --zone="${ZONE}" --project="${PROJECT_ID}"
      gcloud compute instances delete "${HOST}" \
          --zone="${ZONE}" --project="${PROJECT_ID}" --quiet
    done
    
    # Verify remaining instances in the placement policy
    gcloud compute instances list --project="${PROJECT_ID}" --zones="${ZONE}" \
        --filter="resourcePolicies~${PLACEMENT_POLICY}" --format="table(name,status)"
    

### Clean up DNS records and IP pools

Delete the forward (`A`) and reverse (`PTR`) Cloud DNS records of the removed nodes:
    
    
    for HOST in "${REMOVE_HOSTS[@]}"; do
      MGMT_IP=$(gcloud dns record-sets describe "${HOST}.${DOMAIN}." --type=A \
          --zone="${DNS_ZONE}" --project="${PROJECT_ID}" --format="value(rrdatas[0])")
      REV=$(echo "${MGMT_IP}" | awk -F. '{print $4"."$3"."$2"."$1".in-addr.arpa."}')
      gcloud dns record-sets delete "${REV}" --type=PTR --zone="${REV_DNS_ZONE}" --project="${PROJECT_ID}"
      gcloud dns record-sets delete "${HOST}.${DOMAIN}." --type=A --zone="${DNS_ZONE}" --project="${PROJECT_ID}"
    done
    

The vMotion, vSAN, and TEP IP addresses of the removed nodes become free again in the network pool and the NSX TEP pool. You can either retain those IP addresses for a future node (by assigning that future node the same Compute Engine NIC IP addresses) or remove them from the pools so that VCF and NSX don't allocate them to a future node whose Compute Engine NICs use different IP addresses.

### Verify the node removal

After you complete the node removal workflow, verify the following:

  * **vCenter Server** : The `cl02` cluster shows only the remaining nodes, all connected and healthy, and vSphere HA and DRS report no errors.
  * **vSAN** : Skyline Health passes and all virtual objects are compliant (for the `cl02` cluster, go to **Monitor** > **vSAN** > **Virtual Objects**).
  * **NSX Manager** : The removed nodes are no longer listed as transport nodes, and the remaining nodes show **Up**.
  * **VCF Operations and SDDC Manager** : The removed nodes are no longer in the host inventory, and there are no failed tasks.
  * **Google Cloud** : The bare-metal instances, boot disks, NEG endpoints, and DNS records of the removed nodes are deleted.



## Troubleshoot cluster expansion and node removal

The following table lists common issues, causes, and resolutions when adding or removing nodes in a vSphere cluster:

Issue | Cause | Resolution  
---|---|---  
Cluster expansion fails at the connectivity check for vSAN and vMotion; new nodes report unhealthy | When you expand a cluster, SDDC Manager allocates `vmk1` and `vmk2` IP addresses from the network pool without preserving the host order. | Keep validations enabled. Add only the new nodes' IP addresses to the network pool; if the task pauses at the connectivity check, align the Dynamic NICs and retry the same task.  
NSX host status is `Degraded` or tunnels are down on the new nodes | NSX Manager assigns TEP (`vmk10`) IP addresses from the IP pool randomly, so they might not match the Compute Engine TEP NIC. | Align the NSX TEP Dynamic NICs as described in Align NSX TEP dynamic NICs.  
NSX can't prepare the new nodes | The cluster's NSX TEP IP pool has no free IP addresses. | Add the new nodes' TEP IP addresses to the TEP IP pool, and then retry the task.  
SDDC Manager rejects a new expansion request for the same nodes | A failed expansion task leaves the nodes outside the `UNASSIGNED_USEABLE` state. | Retry the failed task (`PATCH /v1/tasks/TASK_ID` with `{"status": "RETRY"}`) instead of submitting a new expansion request.  
Commissioning a node fails because the node is already commissioned | You can't commission a host twice. | Proceed with the cluster expansion, or decommission the node first if you must commission it again (for example, with a different network pool).  
`IP_IN_USE` error when re-adding a Dynamic NIC | Two nodes swapped IP addresses, or a planned IP address overlaps with another node. | Delete all mismatched Dynamic NICs across all new nodes first before re-adding any interface, and verify your IP address plan.  
Node removal validation fails | Removing the nodes reduces the cluster to fewer hosts than its minimum size, or the remaining nodes lack sufficient capacity. | Remove fewer nodes or add capacity first; don't use the `"force": true` property.  
`gcloud` CLI refuses to delete the bare-metal instance | Deletion protection is enabled on the instance. | Run the `gcloud compute instances update HOST --no-deletion-protection` command before deleting the instance.  
Incorrect vSAN fault domains after adding nodes | You created new nodes in a different placement policy, or two clusters share a placement policy. | Create new nodes in the cluster's own placement policy and distribute them across availability domains.  
vSAN errors, vMotion timeouts, or NSX overlay fragmentation | The configured MTU is larger than the VPC network MTU (`8896` bytes). | New nodes inherit the cluster's VDS and pools; keep the MTU set to `8896` bytes across all components.  
Host SSL thumbprint or certificate shows an internal name | The DNS search domain isn't set on the host. | Run the `esxcli network ip dns search add -d vmware.gve` command, re-run the `/var/lib/vmware/osdata/init.sh` script, and then run the `/sbin/generate-certificates` command and restart the `rhttpproxy` and `hostd` services.  
Hosts can't ping the subnet gateway (`.1`) | Google Cloud doesn't respond to ICMP echo requests on subnet gateway IP addresses. | Expected behavior; ignore gateway ping warnings.  
  
## What's next

  * Add a new vSphere cluster to an existing domain in [Add a vSphere cluster to a domain](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster).
  * Manage bare-metal node capacity in the Google Cloud console in [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management).
  * Scale node capacity by using Terraform in [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform).
  * Review placement policy guidelines in [Placement policies and availability domains](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies).
  * Review cluster sizing and architecture guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Review common deployment and operational workarounds in [Known issues](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
