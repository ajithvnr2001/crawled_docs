---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/vcf-appliance-addition/
title: Add VCF appliances by using Terraform \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:27:54.403306+00:00
---

# Add VCF appliances by using Terraform  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/vcf-appliance-addition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add VCF appliances by using Terraform

This page describes how to provision Google Cloud load balancers, reserved internal IPv4 addresses, and Cloud DNS records for additional VMware Cloud Foundation (VCF) management appliances in VMware solution on Google Cloud by using the end-to-end (E2E) Terraform automation modules.

**Note:** You can add appliances by using the E2E Terraform modules only for clusters whose Google Cloud resources were initially provisioned by using the E2E Terraform modules. For prerequisites, initial setup, and module usage, see [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform).

## Add additional appliances

To add new management appliances to an existing cluster, use the same Terraform workspace and state file (`terraform.tfstate`) that you used during the initial deployment of the cluster. Add an appliance to the `mgmt_ip_values` map if the appliance is supposed to be on the management subnet and add it to the `nsx_ip_values` map if it is supposed to be on the NSX TEP subnet.

The following steps show how to add the VCF Automation Appliance virtual IP (VIP) (`auto-vip`) and VCF Automation Runtime (`auto-platform`) appliances (based on the sample configuration in the `e2e-terraform/sample_management_cluster.tfvars` file):

  1. **Update your variable definitions file (`management_cluster.tfvars`)**: Set the `deployment_mode` variable to `"appliance_addition"` and add the new appliance entries directly to the `mgmt_ip_values` (or `nsx_ip_values`) map:
         
         deployment_mode = "appliance_addition"
         
         mgmt_ip_values = {
           # VCF Control Plane Core Services
           "sddcm"     = "10.200.0.9"              # VCF SDDC Manager Appliance
           "collector" = "10.200.0.10"             # VMware Cloud Proxy Appliance
           "vc01"      = "10.200.0.11"             # Management vCenter Server Appliance (VCSA)
           "license"   = "10.200.0.16"             # VCF License Manager Service
           "shared01"  = "10.200.0.17"             # VCF Instance Service Manager
           "vidb"      = "10.200.0.18"             # VMware Workspace ONE Access / Identity Broker
           "vsp01"     = "10.200.0.50"             # VCF Services Runtime Platform
           "vsrt"      = "10.200.0.51-10.200.0.62" # VCF Services Runtime IP Pool
         
           # VMware Aria Suite Operations & Automation Services
           "ops01"    = "10.200.0.12" # VMware Aria Operations Primary Node
           "ops02"    = "10.200.0.24" # VMware Aria Operations Replica Node
           "ops03"    = "10.200.0.25" # VMware Aria Operations Data Node
           "fleetlcm" = "10.200.0.13" # VMware Aria Operations Fleet Management Service
         
           # New appliances added in this operation
           "auto-vip"      = "10.200.0.20" # VCF Automation Appliance VIP
           "auto-platform" = "10.200.0.21" # VCF Automation Runtime
           # "auto-node"   = "10.200.0.81-10.200.0.85" # VCF Automation Cluster Node IP Pool (5 nodes)
         
           # NSX Management Cluster & Management Interfaces
           "nsx01" = "10.200.0.14" # NSX Management Cluster Floating Virtual IP (VIP)
           "nsx02" = "10.200.0.15" # NSX Manager Node 1 Management IP
           "nsx03" = "10.200.0.22" # NSX Manager Node 2 Management IP
           "nsx04" = "10.200.0.23" # NSX Manager Node 3 Management IP
         }
         

  2. **Generate and apply the Terraform execution plan** :
         
         terraform plan -var-file='management_cluster.tfvars' -out=tfplan
         terraform apply tfplan
         




### Expected behavior

When you apply the `appliance_addition` configuration, Terraform performs the following non-disruptive operations:

  * Reserves the static internal IPv4 addresses (`10.200.0.20` and `10.200.0.21`) for the new appliances.
  * Provisions Regional Backend Services (`vcf-mgmt-sample-auto-vip-lb` and `vcf-mgmt-sample-auto-platform-lb`) configured with the `GARP_RA` high availability fast IP move policy.
  * Provisions Regional Forwarding Rules (`vcf-mgmt-sample-auto-vip-fr` and `vcf-mgmt-sample-auto-platform-fr`).
  * Registers forward (`A`) and reverse (`PTR`) records in Cloud DNS.



## What's next

  * Deploy the appliance in your VCF 9.x cluster by using the online or offline depot.
  * Learn how to scale cluster capacity in [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
