---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform/
title: Manage node capacity by using Terraform \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:16.881712+00:00
---

# Manage node capacity by using Terraform  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage node capacity by using Terraform

This page describes how to expand or reduce cluster capacity in VMware solution on Google Cloud by adding bare-metal ESXi nodes to, or deleting bare-metal ESXi nodes from, an existing cluster by using the end-to-end (E2E) Terraform automation modules.

**Note:** You can manage capacity by using the E2E Terraform modules only for clusters whose Google Cloud resources were initially provisioned by using the E2E Terraform modules. For prerequisites, initial setup, and module usage, see [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform). To decommission and delete nodes by using the Google Cloud console instead, see [Manage node capacity](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management#delete-nodes).

## Expand cluster capacity

To expand an existing cluster from X nodes to X \+ N nodes, use the same Terraform workspace and state file (`terraform.tfstate`) that you used during the initial deployment of the cluster.

The following steps show how to add a fifth node (`vcf-mgmt-sample-node-5`) to a four-node management cluster (based on the sample configuration in the `e2e-terraform/sample_management_cluster.tfvars` file):

  1. **Update your variable definitions file (`management_cluster.tfvars`)**: Update the configuration variables in your `management_cluster.tfvars` file as follows:

     * Set the `deployment_mode` variable to `"node_addition"`.
     * Update the `number_of_nodes` variable from `4` to `5`.
     * Append `"vcf-mgmt-sample-node-5"` to the `node_names` list if you explicitly specified `node_names` during cluster creation. Leave the `node_names` list empty if you didn't specify it initially.
     * Append new IPv4 addresses to the `mgmt_nic_ip_values`, `vsan_ip_values`, `vmotion_ip_values`, `nsx_tep_ip_values`, and `additional_dynamic_nics` lists if you explicitly specified these variables during cluster creation. If you left these lists empty for automatic allocation, don't update them.
     * Update the `availability_domains` list (for example, `[1, 2, 3, 4, 5]`) if you explicitly specified this variable during cluster creation. If you left it empty, don't update it.
    
    deployment_mode = "node_addition"
    number_of_nodes = 5
    
    node_names = [
      "vcf-mgmt-sample-node-1",
      "vcf-mgmt-sample-node-2",
      "vcf-mgmt-sample-node-3",
      "vcf-mgmt-sample-node-4",
      "vcf-mgmt-sample-node-5" # New node
    ]
    
    mgmt_nic_ip_values = ["10.200.0.3", "10.200.0.4", "10.200.0.5", "10.200.0.6", "10.200.0.7"]
    vsan_ip_values     = ["10.200.1.3", "10.200.1.4", "10.200.1.5", "10.200.1.6", "10.200.1.7"]
    vmotion_ip_values  = ["10.200.2.3", "10.200.2.4", "10.200.2.5", "10.200.2.6", "10.200.2.7"]
    nsx_tep_ip_values  = ["10.200.3.3", "10.200.3.4", "10.200.3.5", "10.200.3.6", "10.200.3.7"]
    
    additional_dynamic_nics = [
      {
        name            = "additional-nic-1"
        subnet_name     = "vcf-mgmt-sample-additional-subnet-1"
        vlan_id         = 210
        ip_address_type = "reserved_custom"
        ip_values       = ["10.200.4.3", "10.200.4.4", "10.200.4.5", "10.200.4.6", "10.200.4.7"]
      }
    ]
    
    availability_domains = [1, 2, 3, 4, 5]
    

  2. **Generate and apply the Terraform execution plan** :
         
         terraform plan -var-file='management_cluster.tfvars' -out=tfplan
         terraform apply tfplan
         

  3. **Attach the new nodes to the network endpoint groups (NEGs)** : Retrieve and run the generated `gcloud compute network-endpoint-groups update` commands from the `neg_attachment_commands` Terraform output to attach the new instances to the management and NSX NEGs:
         
         # View attachment commands from Terraform outputs
         terraform output neg_attachment_commands
         # Run the generated commands to attach the new instance to the Management and NSX NEGs
         gcloud compute network-endpoint-groups update vcf-mgmt-sample-neg \
            --zone='ZONE' \
            --project='PROJECT_ID' \
            --add-endpoint='instance=vcf-mgmt-sample-node-5'
         gcloud compute network-endpoint-groups update vcf-mgmt-sample-nsx-neg \
            --zone='ZONE' \
            --project='PROJECT_ID' \
            --add-endpoint='instance=vcf-mgmt-sample-node-5'
         

Before you run the commands, replace the following:

     * `ZONE`: The Google Cloud zone where the cluster resides.
     * `PROJECT_ID`: The ID of your target Google Cloud project.



### Expected behavior

When you apply the `node_addition` configuration, Terraform performs the following non-disruptive operations:

  * Provisions only the new bare-metal ESXi instance (`vcf-mgmt-sample-node-5`) and reserves its associated internal IPv4 addresses.
  * Generates the `neg_attachment_commands` output so that you can attach the new instances to the existing management and NSX zonal NEGs.
  * Registers forward (`A`) and reverse (`PTR`) Cloud DNS records for the new node.
  * Leaves all existing running nodes, load balancers, and network configurations uninterrupted.



## What's next

**Caution:** For security, you must reset the initial ESXi `root` password on each newly provisioned bare-metal instance before use. Running the node preparation toolkit automatically resets the ESXi `root` password on each host to the `esxi-root-password` secret stored in Secret Manager. If you don't run the node preparation toolkit, you must manually reset the `root` password on each bare-metal ESXi instance.

After you expand cluster capacity, complete the following steps:

  1. Run the toolkit script (`python3 -m vcf_deployer.main --config config.json`) as described in [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit) to reset the initial ESXi `root` password on each new host and initialize the new ESXi nodes for cluster addition. Omit the `vcf_deployment_config` object in the `config.json` file.
  2. Commission and add the prepared node to your VMware Cloud Foundation (VCF) 9.x cluster by using the VMware UI or APIs.



## Reduce cluster capacity

To reduce an existing cluster from X nodes to X \- N nodes, use the same Terraform workspace and state file (`terraform.tfstate`) that you used during the initial deployment of the cluster.

**Warning:** Before you delete nodes from Google Cloud by using the E2E Terraform modules, you must first remove the nodes from your VMware Cloud Foundation (VCF) 9.x cluster. Deleting a node from Google Cloud before you remove it from the VCF cluster can cause unexpected traffic loss, data loss, or both.

The following steps show how to delete the third node (`vcf-mgmt-sample-node-3`) from the five-node management cluster described in Expand cluster capacity:

  1. **Remove the node from the VCF cluster** : Remove the target ESXi host from your VCF 9.x cluster and decommission it by using VMware SDDC Manager. For more information, see [Decommission hosts in VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html).

  2. **If applicable, disable deletion protection on the node** : Terraform can't delete an instance that has deletion protection enabled. If deletion protection isn't enabled on the nodes that you want to delete, skip this step. Otherwise, disable deletion protection on each node that you want to delete:
         
         gcloud compute instances update vcf-mgmt-sample-node-3 \
            --zone='ZONE' \
            --project='PROJECT_ID' \
            --no-deletion-protection
         

Before you run the command, replace the following:

     * `ZONE`: The Google Cloud zone where the cluster resides.
     * `PROJECT_ID`: The ID of your target Google Cloud project.

To disable deletion protection by using the Google Cloud console instead, see [Decommission and delete nodes](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management#delete-nodes).

  3. **Update your variable definitions file (`management_cluster.tfvars`)**: Update the configuration variables in your `management_cluster.tfvars` file as follows:

     * Set the `deployment_mode` variable to `"node_deletion"`.
     * Update the `number_of_nodes` variable from `5` to `4`.
     * Specify the `node_names` list with the names of the remaining nodes, and remove `"vcf-mgmt-sample-node-3"` from the list.
     * Remove the IPv4 addresses of the deleted node from the `mgmt_nic_ip_values`, `vsan_ip_values`, `vmotion_ip_values`, `nsx_tep_ip_values`, and `additional_dynamic_nics` lists if you explicitly specified these variables during cluster creation.
     * Specify the `availability_domains` list with the availability domain of each remaining node (for example, `[1, 2, 4, 5]`).

In `node_deletion` mode, you must always explicitly specify the `node_names` and `availability_domains` lists, even if you didn't specify them during cluster creation or any earlier Terraform operation on the cluster (for example, if the node names were auto-generated). Specifying these lists ensures that Terraform deletes only the intended node. Make sure that each entry matches the name and availability domain of the corresponding remaining node.
    
    deployment_mode = "node_deletion"
    number_of_nodes = 4
    
    # Always required in node_deletion mode
    node_names = [
      "vcf-mgmt-sample-node-1",
      "vcf-mgmt-sample-node-2",
      # "vcf-mgmt-sample-node-3" removed
      "vcf-mgmt-sample-node-4",
      "vcf-mgmt-sample-node-5"
    ]
    
    mgmt_nic_ip_values = ["10.200.0.3", "10.200.0.4", "10.200.0.6", "10.200.0.7"]
    vsan_ip_values     = ["10.200.1.3", "10.200.1.4", "10.200.1.6", "10.200.1.7"]
    vmotion_ip_values  = ["10.200.2.3", "10.200.2.4", "10.200.2.6", "10.200.2.7"]
    nsx_tep_ip_values  = ["10.200.3.3", "10.200.3.4", "10.200.3.6", "10.200.3.7"]
    
    additional_dynamic_nics = [
      {
        name            = "additional-nic-1"
        subnet_name     = "vcf-mgmt-sample-additional-subnet-1"
        vlan_id         = 210
        ip_address_type = "reserved_custom"
        ip_values       = ["10.200.4.3", "10.200.4.4", "10.200.4.6", "10.200.4.7"]
      }
    ]
    
    # Always required in node_deletion mode
    availability_domains = [1, 2, 4, 5]
    

  4. **Generate and apply the Terraform execution plan** : Review the plan output to verify that Terraform destroys only the resources of the node that you want to delete, and then apply the plan:
         
         terraform plan -var-file='management_cluster.tfvars' -out=tfplan
         terraform apply tfplan
         




### Expected behavior

When you apply the `node_deletion` configuration, Terraform performs the following operations:

  * Deletes only the targeted bare-metal ESXi instance (`vcf-mgmt-sample-node-3`) and its boot disk.
  * Removes the deleted instance from the management and NSX zonal NEGs.
  * Releases the reserved internal IPv4 addresses of the deleted node.
  * Deletes the forward (`A`) and reverse (`PTR`) Cloud DNS records of the deleted node.
  * Leaves all remaining nodes, load balancers, and network configurations uninterrupted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
