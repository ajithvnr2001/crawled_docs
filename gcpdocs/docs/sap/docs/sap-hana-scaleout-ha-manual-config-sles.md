---
url: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-ha-manual-config-sles/
title: HA scale-out cluster configuration guide for SAP HANA on SLES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T08:21:04.681663+00:00
---

# HA scale-out cluster configuration guide for SAP HANA on SLES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-ha-manual-config-sles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  HA scale-out cluster configuration guide for SAP HANA on SLES Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy and configure a performance-optimized SUSE Linux Enterprise Server (SLES) high-availability (HA) cluster for an SAP HANA scale-out system on Google Cloud.

This guide includes the steps for:

  * Configuring an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) to reroute traffic in the event of a failure
  * Configuring a Pacemaker cluster on SLES to manage the SAP systems and other resources during a failover



This guide also includes steps for configuring SAP HANA system replication, but refer to the SAP documentation for the definitive instructions.

To deploy a SAP HANA system without a Linux high-availability cluster or a standby node host, see the following resources:

  * [Terraform: SAP HANA scale-up deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf)
  * [Terraform: SAP HANA multi-host scale-out deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-scaleout-deployment-tf)



This guide is intended for advanced SAP HANA users who are familiar with Linux high-availability configurations for SAP HANA.

## The system that this guide deploys

Following this guide, you deploy a multi-node SAP HANA HA system configured for full zone-redundancy with [an additional instance acting as a majority maker](https://github.com/sap-architecture/sap-hana/blob/master/pages/generic_architecture/module_high_availability.md#majority-maker-node), also known as tie-breaker node, which ensures that the cluster quorum is maintained in case of the loss of one zone.

The final deployment comprises of the following resources:

  * A primary and secondary site where each instance has a zonal counterpart.
  * Two sites configured for synchronous replication.
  * A single compute instance to act as a majority maker.
  * A Pacemaker high-availability cluster resource manager with a fencing mechanism.
  * Hyperdisk or Persistent Disk volumes to host the SAP HANA data and log directories, which are attached to each SAP HANA instance.



![Overview of a high-availability Linux cluster for a multi-node SAP HANA scaleout system](https://docs.cloud.google.com/static/sap/docs/images/ha-hana-scaleout-overview.svg)

This guide has you use the Terraform templates that are provided by Google Cloud to deploy the Compute Engine instances and the SAP HANA instances, which ensures that the compute instances and the base SAP HANA systems meet SAP supportability requirements and conform to best practices.

This guide also uses SAP HANA Studio to test SAP HANA system replication. If you prefer, you can use SAP HANA Cockpit instead. For information about installing SAP HANA Studio, see the following resources:

  * [Installing SAP HANA Studio on a Compute Engine Windows VM](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide#install_hana_studio)
  * [SAP HANA Studio Installation and Update Guide](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/2.0.02/en-US)



## Before you begin

Before you create the SAP HANA high availability cluster, make sure that you satisfy the following prerequisites:

  * You have read the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide) and the [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide). 
  * You or your organization has a Google Cloud account and you have created a project for the SAP HANA deployment. For information about creating Google Cloud accounts and projects, see [Setting up your Google account](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf#setting-up-your-google-account).
  * If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must create the required Assured Workloads folder. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 
  * The SAP HANA installation media is stored in a Cloud Storage bucket that is available in your deployment project and region. For information about how to upload SAP HANA installation media to a Cloud Storage bucket, see [Creating a Cloud Storage bucket for the SAP HANA installation files](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide-tf#creating_a_cloud_storage_bucket_for_the_sap_hana_installation_files).

  * If [OS login](https://docs.cloud.google.com/compute/docs/instances/access-overview#oslogin) is enabled in your project metadata, then you need to disable OS login temporarily until your deployment is complete. For deployment purposes, this procedure configures SSH keys in instance metadata. When OS login is enabled, metadata-based SSH key configurations are disabled, and this deployment fails. After deployment is complete, you can enable OS login again.

For more information, see:

    * [Enabling or disabling OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin)
    * [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata)
  * If you're using [VPC internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns), then the value of the `vmDnsSetting` variable in your project metadata must be either `GlobalOnly` or `ZonalPreferred` to enable the resolution of the node names across zones. The default setting of `vmDnsSetting` is `ZonalOnly`. For more information, see:

    * [Configuring DNS names for your project or instances](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#setting-zonal-dns)
    * [Querying custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#querying_custom_metadata)
    * [Setting project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide)
  * You have an NFS solution, such as the managed [Filestore](https://docs.cloud.google.com/filestore/docs) solution, for sharing the SAP HANA `/hana/shared` and `/hanabackup` volumes among the hosts in the scale-out SAP HANA system. To deploy Filestore NFS servers, see [Creating instances](https://docs.cloud.google.com/filestore/docs/creating-instances).

    * Note that the primary and secondary sites must have access to their own dedicated NFS paths to avoid overwriting data. To use a single Filestore instance, you must configure the deployment to use distinct sub-directories as the mount path. 

To avoid unintentionally exposing your VM instance to the internet, follow these recommendations: 

  * Use a NAT gateway.
  * [Create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) that block all external access that you don't require.
  * When you create your VMs: 
    * Specify a network tag for each VM for use in routing and firewall rules. If you use the Terraform configuration file that Google Cloud provides, specify a tag with `network_tags = "TAG"`.
    * Create the VMs without an external IP. If you use the Terraform configuration file that Google Cloud provides, specify `public_ip = false`.



## Creating a network

For security purposes, create a new network. You can control who has access by adding firewall rules or by using another access control method.

If your project has a default VPC network, then don't use it. Instead, create your own VPC network so that the only firewall rules in effect are those that you create explicitly.

During deployment, Compute Engine instances typically require access to the internet to download Google Cloud's Agent for SAP. If you are using one of the SAP-certified Linux images that are available from Google Cloud, then the compute instance also requires access to the internet in order to register the license and to access OS vendor repositories. A configuration with a NAT gateway and with VM network tags supports this access, even if the target compute instances don't have external IPs. 

To create a VPC network for your project, complete the following steps:

  1. Create a custom mode network. For more information, see [Creating a custom mode network](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_1).

  2. Create a subnetwork, and specify the region and IP range. For more information, see [Adding subnets](https://docs.cloud.google.com/vpc/docs/using-vpc#terraform_2).




## Setting up a NAT gateway

If you need to create one or more compute instances without public IP addresses, then you need to use network address translation (NAT) to enable the instances to access the internet. Use Cloud NAT, a Google Cloud distributed, software-defined managed service that lets the compute instances send outbound packets to the internet and receive any corresponding established inbound response packets. Alternatively, you can set up a separate compute instance as a NAT gateway.

**Key Point:** When you configure Cloud NAT, specify at least 160 as the minimum number of ports per compute instance. Certain operating system updates run concurrent processes that might exceed the Cloud NAT default for the number of ports, which can result in activation or download errors. 

When you create a Cloud NAT instance, specify the number of ports in the **Minimum ports per VM** field under **Advanced configurations** on the Create a NAT gateway page in the Google Cloud console.

To create a Cloud NAT instance for your project, see [Using Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-network-address-translation#terraform).

After you configure Cloud NAT for your project, your compute instances can securely access the internet without a public IP address.

## Adding firewall rules

By default, an _implied firewall rule_ blocks incoming connections from outside your Virtual Private Cloud (VPC) network. To allow incoming connections, set up a firewall rule for your VM. After an incoming connection is established with a VM, traffic is permitted in both directions over that connection.

You can also create a firewall rule to allow external access to specified ports, or to restrict access between VMs on the same network. If the `default` VPC network type is used, some additional default rules also apply, such as the `default-allow-internal` rule, which allows connectivity between VMs on the same network on all ports.

Depending on the IT policy that is applicable to your environment, you might need to isolate or otherwise restrict connectivity to your database host, which you can do by creating firewall rules.

Depending on your scenario, you can create firewall rules to allow access for:

  * The default SAP ports that are listed in [TCP/IP of All SAP Products](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).
  * Connections from your computer or your corporate network environment to your Compute Engine instance. If you are unsure of what IP address to use, talk to your company's network administrator.



To create the firewall rules for your project, see [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#terraform).

## Deploy the infrastructure and install SAP HANA

This guide has you use a Terraform configuration file provided by Google Cloud to deploy the following:

  * Two matching SAP HANA systems, each with two or more compute instances.
  * A single majority maker instance also known as tie-breaker node, which ensures the cluster quorum is maintained in case of the loss of one zone.



The SAP HANA systems use asynchronous system replication such that one of the SAP HANA systems functions as the primary, active system and the other functions as a secondary, standby system. You deploy both SAP HANA systems within the same [region](https://docs.cloud.google.com/compute/docs/regions-zones), ideally in different zones.

If you want to deploy a scale-out system with standby hosts for SAP HANA automatic host failover, then you must instead see [Terraform: SAP HANA scale-out system with host auto-failover deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-scaleout-tf-deployment-guide).

You define configuration options for the SAP HANA high-availability cluster in a Terraform configuration file.

The following instructions use Cloud Shell, but are generally applicable to a local terminal with Terraform installed and configured with the [Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started).

  1. Confirm that your current quotas for resources such as persistent disks and CPUs are sufficient for the SAP HANA systems you are about to install. If your quotas are insufficient, then your deployment fails.

For the SAP HANA quota requirements, see [Pricing and quota considerations for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. Open the Cloud Shell or your local terminal.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Download the `manual_sap_hana_scaleout_ha.tf` configuration file to your working directory by running the following command in Cloud Shell or your terminal:
         
         $ wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_ha/terraform/manual_sap_hana_scaleout_ha.tf

**Note:** Ensure that you have only a single Terraform configuration file in your working directory.
  4. Open the `manual_sap_hana_scaleout_ha.tf` file in the Cloud Shell code editor or, if you are using your terminal, then open the file in a text editor of your choice.

To open the Cloud Shell code editor, click the pencil icon in the upper right corner of the Cloud Shell terminal window.

  5. In the `manual_sap_hana_scaleout_ha.tf` file, for both `sap_hana_primary` and `sap_hana_secondary` update the argument values by replacing the contents inside the double quotation marks with the values for your installation. The arguments are described in the following table.

Argument | Data type | Description  
---|---|---  
`source` | String |  Specifies the location and version of the Terraform module to use during deployment.  The `manual_sap_hana_scaleout_ha.tf` configuration file includes two instances of the `source` argument: one that is active and one that is included as a comment. The `source` argument that is active by default specifies `latest` as the module version. The second instance of the `source` argument, which by default is deactivated by a leading `#` character, specifies a timestamp that identifies a module version.  If you need all of your deployments to use the same module version, then remove the leading `#` character from the `source` argument that specifies the version timestamp and add it to the `source` argument that specifies `latest`.   
`project_id` | String | Specify the ID of your Google Cloud project in which you are deploying this system. For example, `my-project-x`.  
`machine_type` | String |  Specify the type of Compute Engine machine type on which you want to run your SAP system. To see the list of certified machine types, go to [Certified solutions and machine types](https://docs.cloud.google.com/sap/docs/sap-certifications#certified-solutions-and-machine-types), and in the **Certified SAP solution** menu, select "SAP HANA". If you want to use a custom machine type, then specify a predefined machine type with a number of vCPUs that is closest to the number you need while still being larger. After deployment is complete, [modify the machine type of your compute instance](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations#modify_the_machine_type_of_your_compute_instance). For example, `n1-highmem-32`.  
`network` | String |  Specify the name of the network in which you need to create the load balancer that manages the VIP.  If you are using a shared VPC network, you must add the ID of the host project as a parent directory of the network name. For example, `HOST_PROJECT_ID/NETWORK_NAME`.   
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`linux_image` | String | Specify the name of the Linux operating system image on which you want to deploy your SAP system. For example, `sles-15-sp6-sap`. For the list of available operating system images, see the [Images](https://console.cloud.google.com/compute/images) page in the Google Cloud console.  
`linux_image_project` | String | Specify the Google Cloud project that contains the image that you have specified for the argument `linux_image`. This project might be your own project or a Google Cloud image project. For a Compute Engine image, specify `suse-sap-cloud`. To find the image project for your operating system, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).   
`primary_instance_name` | String | Specify a name of the VM instance for the primary SAP HANA system. The name can contain lowercase letters, numbers, or hyphens.   
`primary_zone` | String | Specify a zone in which the primary SAP HANA system is deployed. The primary and secondary zones must be in the same region. For example, `us-east1-c`.   
`secondary_instance_name` | String | Specify a name of the VM instance for the secondary SAP HANA system. The name can contain lowercase letters, numbers, or hyphens.   
`secondary_zone` | String | Specify a zone in which the secondary SAP HANA system is deployed. The primary and secondary zones must be in the same region. For example, `us-east1-b`.   
`sap_hana_deployment_bucket` | String | To automatically install SAP HANA on the deployed VMs, specify the path of the Cloud Storage bucket that contains the SAP HANA installation files. Don't include `gs://` in the path; include only the bucket name and the names of any folders. For example, `my-bucket-name/my-folder`. The Cloud Storage bucket must exist in the Google Cloud project that you specify for the `project_id` argument.  
`sap_hana_scaleout_nodes` | Integer | Specify the number of worker hosts that you need in your scale-out system. To deploy a scale-out system, you need at least one worker host. Terraform creates the worker hosts in addition to the primary SAP HANA instance. For example, if you specify `3`, then four SAP HANA instances are deployed in your scale-out system.  
`sap_hana_sid` | String | To automatically install SAP HANA on the deployed VMs, specify the SAP HANA system ID. The ID must consist of three alpha-numeric characters and begin with a letter. All letters must be in uppercase. For example, `HS4`.   
`sap_hana_instance_number` | Integer | Optional. Specify the instance number, 0 to 99, of the SAP HANA system. The default is `0`.  
`sap_hana_sidadm_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary `SIDadm` password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important:** After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_sidadm_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the `SIDadm` password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password` | String | To automatically install SAP HANA on the deployed VMs, specify a temporary database superuser password for the installation scripts to use during deployment. The password must contain at least 8 characters and include at least one uppercase letter, one lowercase letter, and a number. **Important** : After the installation is complete, make sure to change the password.  Instead of specifying password as plain text, we recommend that you use a secret. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_system_password_secret` | String | Optional. If you are using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the database superuser password, then specify the **Name** of the secret that corresponds to this password. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the Google Cloud project that you specify for the `project_id` argument. For more information, see [Password management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#password_management).   
`sap_hana_double_volume_size` | Boolean | Optional. To double the HANA volume size, specify `true`. This argument is useful when you want to deploy multiple SAP HANA instances or a disaster-recovery SAP HANA instance on the same VM. By default, the volume size is automatically calculated to be the minimum size required for the size of your VM, while still meeting the SAP certification and support requirements. The default value is `false`.   
`sap_hana_backup_size` | Integer | Optional. Specify size of the `/hanabackup` volume in GB. If you don't specify this argument or set it to `0`, then the installation script provisions Compute Engine instance with a HANA backup volume of two times the total memory.   
`sap_hana_sidadm_uid` | Integer | Optional. Specify a value to override the default value of the SID_LCadm user ID. The default value is `900`. You can change this to a different value for consistency within your SAP landscape.   
`sap_hana_sapsys_gid` | Integer | Optional. Overrides the default group ID for `sapsys`. The default value is `79`.   
`sap_vip` | String |  Optional. Specify the IP address that you are going to use for your VIP. The IP address must be within the range of IP addresses that are assigned to your subnetwork. The Terraform configuration file reserves this IP address for you.  From version `1.3.730053050` of the `sap_hana_ha` module, the `sap_vip` argument is optional. If you don't specify it, then Terraform automatically assigns an available IP address from subnetwork that you specify for the `subnetwork` argument.   
`primary_instance_group_name` | String | Optional. Specify the name of the unmanaged instance group for the primary node. The default name is `ig-PRIMARY_INSTANCE_NAME`.   
`secondary_instance_group_name` | String | Optional. Specify the name of the unmanaged instance group for the secondary node. The default name is `ig-SECONDARY_INSTANCE_NAME`.   
`loadbalancer_name` | String | Optional. Specify the name of the internal passthrough Network Load Balancer. The default name is `lb-SAP_HANA_SID-ilb`.   
`network_tags` | String | Optional. Specify one or more comma-separated network tags that you want to associate with your VM instances for firewall or routing purposes.  If you specify `public_ip = false` and don't specify a network tag, then make sure to provide another means of access to the internet.   
`disk_type` | String | Optional. Specify the default type of Persistent Disk or Hyperdisk volume that you want to deploy for the `/hana/data`, `/hana/log`, and `/usr/sap` directories in your deployment. For information about the default disk deployment performed by the Terraform configurations provided by Google Cloud, see [ Disk deployment by Terraform](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#disk-deployment-by-terraform). The following are valid values for this argument: `hyperdisk-extreme`, `hyperdisk-balanced`, `pd-ssd`, `pd-balanced`, and `pd-extreme`.  You can override this default disk type and the associated default disk size and default IOPS using some advanced arguments. For more information, navigate to your working directory, then run the `terraform init` command, and then see the `/.terraform/modules/manual_sap_hana_scaleout_ha/variables.tf` file. Before you use these arguments in production, make sure to test them in a non-production environment.  If you want to use [SAP HANA Native Storage Extension](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/4efaa94f8057425c8c7021da6fc2ddf5.html) (NSE), then you need to provision larger disks by using the advanced arguments.  
`use_single_shared_data_log_disk` | Boolean | Optional. The default value is `false`, which directs Terraform to deploy a separate persistent disk or Hyperdisk for each of the following SAP volumes: `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap`. To mount these SAP volumes on the same persistent disk or Hyperdisk, specify `true`.   
`include_backup_disk` | Boolean | Optional. The default value is `true`, which directs Terraform to deploy a separate disk to host the `/hanabackup` directory. The disk type is determined by the `backup_disk_type` argument. The size of this disk is determined by the `sap_hana_backup_size` argument. If you set the value for `include_backup_disk` as `false`, then no disk is deployed for the `/hanabackup` directory.  You can use only one backup option in your Terraform configuration - either disk based backup or Backint based backup. For more information, see [Backup management](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#backup_management).  
`public_ip` | Boolean |  Optional. Determines whether or not a public IP address is added to your VM instance. The default value is `true`. **Caution:** don't specify `false` unless you have a NAT gateway configured with a network tag defined for the VM or you have provided the VM with another route to the internet. If there is no route to the internet, the installation fails.   
`service_account` | String | Optional. Specify the email address of a user-managed service account to be used by the host VMs and by the programs that run on the host VMs. For example, `svc-acct-name@project-id.iam.gserviceaccount.com`.  If you specify this argument without a value, or omit it, then the installation script uses the Compute Engine default service account. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
`sap_deployment_debug` | Boolean | Optional. Only when Cloud Customer Care asks you to enable debugging for your deployment, specify `true`, which makes the deployment generate verbose deployment logs. The default value is `false`.   
`primary_reservation_name` | String | Optional. To use a specific [Compute Engine VM reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) for provisioning the VM instance that hosts your HA cluster's primary SAP HANA instance, specify the name of the reservation. By default, the installation script selects any available Compute Engine reservation based on the following conditions.  For a reservation to be usable, regardless of whether you specify a name or the installation script selects it automatically, the reservation must be set with the following: 
     * The `specificReservationRequired` option is set to `true` or, in the Google Cloud console, the **Select specific reservation** option is selected. 
     * Some Compute Engine machine types support CPU platforms that are not covered by the SAP certification of the machine type. If the target reservation is for any of the following machine types, then the reservation must specify the minimum CPU platforms as indicated: 
       * `n1-highmem-32`: Intel Broadwell
       * `n1-highmem-64`: Intel Broadwell
       * `n1-highmem-96`: Intel Skylake
       * `m1-megamem-96`: Intel Skylake
The minimum CPU platforms for all of the other machine types that are certified by SAP for use on Google Cloud conform to the SAP minimum CPU requirement.   
`secondary_reservation_name` | String | Optional. To use a specific [Compute Engine VM reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources) for provisioning the VM instance that hosts your HA cluster's secondary SAP HANA instance, specify the name of the reservation. By default, the installation script selects any available Compute Engine reservation based on the following conditions.  For a reservation to be usable, regardless of whether you specify a name or the installation script selects it automatically, the reservation must be set with the following: 
     * The `specificReservationRequired` option is set to `true` or, in the Google Cloud console, the **Select specific reservation** option is selected. 
     * Some Compute Engine machine types support CPU platforms that are not covered by the SAP certification of the machine type. If the target reservation is for any of the following machine types, then the reservation must specify the minimum CPU platforms as indicated: 
       * `n1-highmem-32`: Intel Broadwell
       * `n1-highmem-64`: Intel Broadwell
       * `n1-highmem-96`: Intel Skylake
       * `m1-megamem-96`: Intel Skylake
The minimum CPU platforms for all of the other machine types that are certified by SAP for use on Google Cloud conform to the SAP minimum CPU requirement.   
`primary_static_ip` | String | Optional. Specify a valid static IP address for the primary VM instance in your high-availability cluster. If you don't specify one, then an IP address is automatically generated for your VM instance. For example, `128.10.10.10`.  This argument is available in `sap_hana_ha` module version `202306120959` or later.   
`secondary_static_ip` | String | Optional. Specify a valid static IP address for the secondary VM instance in your high-availability cluster. If you don't specify one, then an IP address is automatically generated for your VM instance. For example, `128.11.11.11`.  This argument is available in `sap_hana_ha` module version `202306120959` or later.   
`primary_worker_static_ips` | List(String) | Optional. Specify an array of valid static IP addresses for the worker instances in the primary instance of your SAP HANA scale-out HA system. If you don't specify a value for this argument, then an IP address is automatically generated for each worker VM instance. For example, `[ "1.0.0.1", "2.3.3.4" ]`. The static IP addresses are assigned in the order of instance creation. For example, if you choose to deploy 3 worker instances but specify only 2 IP addresses for the argument `primary_worker_static_ips`, then these IP addresses are assigned to the first two VM instances that the Terraform configuration deploys. For the third worker VM instance, the IP address is automatically generated. This argument is available in `sap_hana_ha` module version `202307270727` or later.   
`secondary_worker_static_ips` | List(String) | Optional. Specify an array of valid static IP addresses for the worker instances in the secondary instance of your SAP HANA scale-out HA system. If you don't specify a value for this argument, then an IP address is automatically generated for each worker VM instance. For example, `[ "1.0.0.2", "2.3.3.5" ]`. The static IP addresses are assigned in the order of instance creation. For example, if you choose to deploy 3 worker instances but specify only 2 IP addresses for the argument `secondary_worker_static_ips`, then these IP addresses are assigned to the first two VM instances that the Terraform configuration deploys. For the third worker VM instance, the IP address is automatically generated. This argument is available in `sap_hana_ha` module version `202307270727` or later.   
  
The following examples show completed configuration files that define a high-availability cluster for an SAP HANA scale-out system. The cluster uses an internal passthrough Network Load Balancer to manage the VIP.

Terraform deploys the Google Cloud resources that are defined in the configuration file and then scripts take over to configure the operating system and install SAP HANA.

**Note:** The deployment scripts install SAP HANA only if the appropriate arguments are specified in the Terraform configuration file. To automatically install SAP HANA on the deployed VMs, you must specify the following arguments: 
     * `sap_hana_deployment_bucket`
     * `sap_hana_sid`
     * `sap_hana_sidadm_password` or `sap_hana_sidadm_password_secret`
     * `sap_hana_system_password` or `sap_hana_system_password_secret`
  6. In the same `manual_sap_hana_scaleout_ha.tf` file, update the argument values for `majority_maker`. The arguments are described in the following table.

Argument | Data type | Description  
---|---|---  
`project` | String | Specify the ID of your Google Cloud project in which you are deploying this system.  
`majority_maker_instance_name` | String | Specify a name for the Compute Engine VM instance that serves as the majority maker. This argument is available in `sap_hana_ha` module version `202307270727` or later.   
`majority_maker_instance_type` | String |  Specify the type of Compute Engine machine type that you want to use for the majority maker instance. For example, `n1-highmem-32`. For information about the SAP-certified machine types that you can use to run SAP HANA, go to [Certified solutions and machine types](https://docs.cloud.google.com/sap/docs/sap-certifications#certified-solutions-and-machine-types), and in the **Certified SAP solution** menu, select "SAP HANA". If you want to use a custom VM type, then specify a predefined machine type with a number of vCPUs that is closest to the number you need while still being larger. After the deployment is complete, [modify the machine type of your compute instance](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations#modify_the_machine_type_of_your_compute_instance). This argument is available in `sap_hana_ha` module version `202307270727` or later.  
`majority_maker_zone` | String | Specify a zone in which the majority maker VM instance is deployed. This zone must be in the same [region](https://docs.cloud.google.com/compute/docs/regions-zones) as the primary and secondary zones. For example, `us-east1-d`. Google Cloud recommends that the majority maker VM instance is deployed in a different zone than the primary and secondary SAP HANA systems. This argument is available in `sap_hana_ha` module version `202307270727` or later.   
`majority_maker_linux_image` | String | Using the same values as in the previous step, specify the complete image path as `"LINUX_IMAGE_PROJECT/LINUX_IMAGE"`. For example `"suse-sap-cloud/sles-15-sp7-sap"`.  
`subnetwork` | String | Specify the name of the subnetwork that you created in a previous step. If you are deploying to a shared VPC, then specify this value as `SHARED_VPC_PROJECT_ID/SUBNETWORK`. For example, `myproject/network1`.  
`service_account` | String | Optional. Specify the email address of a user-managed service account to be used by the host VMs and by the programs that run on the host VMs. For example, `svc-acct-name@project-id.iam.gserviceaccount.com`.  If you specify this argument without a value, or omit it, then the installation script uses the Compute Engine default service account. For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).   
`metadata_startup_script` | String | Don't edit this argument. By default the majority maker downloads the latest startup script to prepare the instance for Pacemaker managed clustering.  
  
For clarity, comments in the following example configuration are omitted.
         
         module "sap_hana_primary" {
           source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana/sap_hana_module.zip"
         
           project_id                     = "example-project-123456"
           zone                           = "us-west1-a"
           machine_type                   = "n1-highmem-32"
           subnetwork                     = "default"
           linux_image                    = "sles-15-sp7-sap"
           linux_image_project            = "suse-sap-cloud"
           instance_name                  = "hana-ha-1"
           sap_hana_sid                   = "HA1"
         
           sap_hana_deployment_bucket      = "my-hana-bucket"
           sap_hana_sidadm_password_secret = "hana_sid_adm_pwd"
           sap_hana_system_password_secret = "hana_sys_pwd"
           sap_hana_scaleout_nodes         = 1
           sap_hana_shared_nfs             = "10.10.10.1:/hana_scaleout/hana_a/shared"
           sap_hana_backup_nfs             = "10.10.10.1:/hana_scaleout/hana_a/backup"
         
         }
         module "sap_hana_secondary" {
           source = "https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana/sap_hana_module.zip"
         
           project_id                     = "example-project-123456"
           zone                           = "us-west1-b"
           machine_type                   = "n1-highmem-32"
           subnetwork                     = "default"
           linux_image                    = "sles-15-sp7-sap"
           linux_image_project            = "suse-sap-cloud"
           instance_name                  = "hana-ha-2"
           sap_hana_sid                   = "HA1"
         
           sap_hana_deployment_bucket      = "my-hana-bucket"
           sap_hana_sidadm_password_secret = "hana_sid_adm_pwd"
           sap_hana_system_password_secret = "hana_sys_pwd"
           sap_hana_scaleout_nodes         = 1
           sap_hana_shared_nfs             = "10.10.10.2:/hana_scaleout/hana_b/shared"
           sap_hana_backup_nfs             = "10.10.10.2:/hana_scaleout/hana_b/backup"
         }
         
         resource "google_compute_instance" "majority_maker" {
         
           project =  "example-project-123456"
         
           # majority_maker_instance_name
           name = "majority-maker"
         
           # majority_maker_instance_type
           machine_type = "n1-standard-8"
         
           # majority_maker_zone
           zone = "us-west1-c"
         
           boot_disk {
             initialize_params {
               # majority_maker_linux_image
               image = "suse-sap-cloud/sles-15-sp7-sap"
             }
           }
         
           network_interface {
             # network or subnetwork
             network = "default"
           }
         
             service_account {
             # service_account (Optional)
             # email  = svc-acct-name@project-id.iam.gserviceaccount.com.
             scopes = ["cloud-platform"]
           }
         
           # Don't edit the following line
           metadata_startup_script = "curl -s https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_ha/manual_instance_startup.sh | bash -s https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/sap_hana_ha/manual_instance_startup.sh"
         }
         

  7. Initialize your current working directory and download the Terraform provider plugin and module files for Google Cloud:
         
         terraform init

The `terraform init` command prepares your working directory for other Terraform commands.

To force a refresh of the provider plugin and configuration files in your working directory, specify the `--upgrade` flag. If the `--upgrade` flag is omitted and you don't make any changes in your working directory, Terraform uses the locally cached copies, even if `latest` is specified in the `source` URL.
         
         terraform init --upgrade 

  8. Optionally, create the Terraform execution plan:
         
         terraform plan

The `terraform plan` command shows the changes required by your current configuration. If you skip this step, the `terraform apply` command automatically creates a new plan and prompts you to approve it.

  9. Apply the execution plan:
         
         terraform apply

When you are prompted to approve the actions, enter `yes`.

The `terraform apply` command sets up the Google Cloud infrastructure and then hands control over to a script that configures the HA cluster and installs SAP HANA according to the arguments defined in the terraform configuration file.

While Terraform has control, status messages are written to the Cloud Shell. After the scripts are invoked, status messages are written to Logging and are viewable in the Google Cloud console, as described in Check the logs.




## Verifying the deployment of your HANA HA system

You can verify the deployment of your SAP HANA scale-out HA system by performing the following checks:

  * Check the logs
  * Check the configuration of the VM and the SAP HANA installation



### Check the logs

  1. In the Google Cloud console, open Cloud Logging to monitor installation progress and check for errors.

**Note:** You might incur costs when completing this step in Cloud Logging. For more information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

[Go to Cloud Logging](https://console.cloud.google.com/logs/query)

  2. Filter the logs:

     1. In the **Logs Explorer** page, go to the **Query** pane.

     2. From the **Resource** drop-down menu, select **Global** , and then click **Add**.

If you don't see the **Global** option, then in the query editor, enter the following query:
            
            resource.type="global"
            "Deployment"
            

     3. Click **Run query**.

  3. Analyze the filtered logs:

     * If `"--- Finished"` is displayed, then the deployment processing is complete and you can proceed to the next step.
     * If you see a quota error:

       1. On the IAM & Admin [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, increase any of your quotas that do not meet the SAP HANA requirements that are listed in the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#quotas).

       2. Open Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

       3. Go to your working directory and delete the deployment to clean up the VMs and persistent disks from the failed installation:
              
              terraform destroy

When you are prompted to approve the action, enter `yes`.

       4. Rerun your deployment.




### Check the configuration of the compute instances and the SAP HANA installation

**Note:** The deployment scripts install SAP HANA only if you specified the appropriate arguments in your Terraform configuration file. If you didn't specify them, then you can skip this step.

  1. After the SAP HANA system deploys without errors, connect to each compute instance by using SSH. In the Compute Engine [VM instances](https://console.cloud.google.com/compute/instances), you can click the SSH button for each compute instance, or you can use your preferred SSH method.

![SSH button on Compute Engine VM instances page.](https://docs.cloud.google.com/static/sap/docs/images/ha-ssh-button.png)

  2. Switch to the root user:
         
         sudo su -

  3. At the command prompt, enter `df -h`. Ensure that you see output that includes the `/hana` directories, such as `/hana/data`.
         
         [root@example-ha-vm1 ~]# df -h
           Filesystem                        Size  Used Avail Use% Mounted on
           devtmpfs                          126G     0  126G   0% /dev
           tmpfs                             126G   54M  126G   1% /dev/shm
           tmpfs                             126G   25M  126G   1% /run
           tmpfs                             126G     0  126G   0% /sys/fs/cgroup
           /dev/sda2                          30G  5.4G   25G  18% /
           /dev/sda1                         200M  6.9M  193M   4% /boot/efi
           /dev/mapper/vg_hana-shared        251G   52G  200G  21% /hana/shared
           /dev/mapper/vg_hana-sap            32G  477M   32G   2% /usr/sap
           /dev/mapper/vg_hana-data          426G  9.8G  417G   3% /hana/data
           /dev/mapper/vg_hana-log           125G  7.0G  118G   6% /hana/log
           /dev/mapper/vg_hanabackup-backup  512G  9.3G  503G   2% /hanabackup
           tmpfs                              26G     0   26G   0% /run/user/900
           tmpfs                              26G     0   26G   0% /run/user/899
           tmpfs                              26G     0   26G   0% /run/user/1003




### Clean up and retry deployment

If any of the deployment verification steps in the preceding sections show that the installation wasn't successful, then you must undo your deployment and retry it by completing the following steps:

  1. Resolve any errors to ensure that your deployment doesn't fail again for the same reason. For information about checking the logs, or resolving quota related errors, see Check the logs.

  2. Open Cloud Shell or, if you installed the Google Cloud CLI on your local workstation, then open a terminal.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Go to the directory that contains the Terraform configuration file that you used for this deployment.

  4. Delete all resources that are part of your deployment by running the following command:
         
         terraform destroy

When you are prompted to approve the action, enter `yes`.

  5. Retry your deployment as instructed earlier in this guide.




## Validate your installation of Google Cloud's Agent for SAP

After you have deployed a VM and installed your SAP system, validate that Google Cloud's Agent for SAP is functioning properly.

### Verify that Google Cloud's Agent for SAP is running

To verify that the agent is running, follow these steps:

  1. Establish an SSH connection with your Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Set up monitoring for SAP HANA

Optionally, you can monitor your SAP HANA instances by using Google Cloud's Agent for SAP. From version 2.0, you can configure the agent to collect the SAP HANA monitoring metrics and send them to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Cloud Monitoring lets you create dashboards to visualize these metrics, set up alerts based on metric thresholds, and more.

To monitor an HA cluster by using Google Cloud's Agent for SAP, make sure to follow the guidance given in [High-availability configuration for the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#high-availability_configuration_for_the_agent).

For more information about the collection of SAP HANA monitoring metrics using Google Cloud's Agent for SAP, see [SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics).

## (Optional) Create a list of instances for script automation

To partially automate some of the repetitive tasks during the configuration of SAP HANA system and Pacemaker cluster, you can use bash scripts. Throughout this guide, such bash scripts are used to speed up the configuration of your SAP HANA system and Pacemaker cluster. These scripts require a list of all deployed VM instances and their corresponding zones as an input.

To enable this automation, create a file named `nodes.txt` and include the details of all the deployed VM instances in the following format: zone name, whitespace, and then the VM instance name. The following sample file is used throughout this guide:
    
    
    # cat nodes.txt
      us-west1-a hana-ha-vm-1
      us-west1-a hana-ha-vm-1w1
      us-west1-a hana-ha-vm-1w2
      us-west1-b hana-majoritymaker
      us-west1-c hana-ha-vm-2
      us-west1-c hana-ha-vm-2w1
      us-west1-c hana-ha-vm-2w2
     

## Set up passwordless SSH access

To configure the Pacemaker cluster and to synchronize the SAP HANA secure store (SSFS) keys, passwordless SSH access is required between all nodes, including the majority maker instance. For passwordless SSH access, you need to add the SSH public keys to the instance metadata of all deployed instances.

The format of the metadata is `USERNAME: PUBLIC-KEY-VALUE`.

For more information about adding SSH keys to VMs, see [Add SSH keys to VMs that use metadata-based SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata).

### Manual steps

  1. For each instance in the primary and secondary systems, as well as the majority maker instance, collect the public key for the user `root`.
         
         gcloud compute ssh --quiet --zone ZONE_ID INSTANCE_NAME -- sudo cat /root/.ssh/id_rsa.pub

  2. Prepend the key with the string `root:` and write the key as a new line into the file called `public-ssh-keys.txt`, for example:
         
         root:ssh-rsa AAAAB3NzaC1JfuYnOI1vutCs= root@INSTANCE_NAME

  3. After collecting all SSH public keys, upload the keys as metadata to all instances:
         
         gcloud compute instances add-metadata --metadata-from-file ssh-keys=public-ssh-keys.txt --zone ZONE_ID INSTANCE_NAME




### Automated steps

Alternatively, to automate the process of setting up passwordless SSH access for all instances listed in `nodes.txt`, perform the following steps from Google Cloud console:

  1. Create a list of public keys from all deployed instances: 
         
         while read -u10 ZONE HOST ;  do echo "Collecting public-key from $HOST"; { echo 'root:'; gcloud compute ssh --quiet --zone $ZONE $HOST --tunnel-through-iap -- sudo cat /root/.ssh/id_rsa.pub; } | tr -ds '\n' " " >> public-ssh-keys.txt; done 10< nodes.txt

  2. Assign the SSH public keys as metadata entries to all instances: 
         
         while read -u10 ZONE HOST ;  do echo "Adding public keys to $HOST"; gcloud compute instances add-metadata --metadata-from-file ssh-keys=public-ssh-keys.txt --zone $ZONE $HOST; done 10< nodes.txt 




## Disable SAP HANA autostart

### Manual steps

For each SAP HANA instance in the cluster, make sure that SAP HANA autostart is disabled. For failovers, Pacemaker manages the starting and stopping of the SAP HANA instances in a cluster.

  1. On each host as SID_LCadm, stop SAP HANA:
         
         > HDB stop

  2. On each host, open the SAP HANA profile by using an editor, such as vi:
         
         vi /usr/sap/SID/SYS/profile/SID_HDBINST_NUM_HOST_NAME

  3. Set the `Autostart` property to `0`:
         
         Autostart=0

  4. Save the profile.

  5. On each host as SID_LCadm, start SAP HANA:
         
         > HDB start




### Automated steps

Alternatively, to disable SAP HANA autostart for all instances listed in `nodes.txt`, run the following script from Google Cloud console:
    
    
    while read -u10 ZONE HOST ;
     do gcloud compute ssh --verbosity=none --zone $ZONE $HOST -- "echo Setting Autostart=0 on \$HOSTNAME;
     sudo sed -i 's/Autostart=1/Autostart=0/g' /usr/sap/SID/SYS/profile/SID_HDBINST_NUM_\$HOSTNAME";
     done 10< nodes.txt
     

**Note:** Ignore the error "No such file or directory" that is shown when the automation script accesses the majority maker instance. This error is shown because the majority maker instance does not have SAP HANA installed. 

## Enable SAP HANA Fast Restart

Google Cloud **strongly** recommends enabling SAP HANA Fast Restart for each instance of SAP HANA, especially for larger instances. SAP HANA Fast Restart reduces restart time in the event that SAP HANA terminates, but the operating system remains running.

**Note:** If you deploy SAP HANA using Google Cloud's Terraform module `sap_hana` or `sap_hana_ha`, version `202309280828` or later, or the Terraform module `manual_sap_hana_scaleup_ha`, then fast restart is automatically enabled.

As configured by the automation scripts that Google Cloud provides, the operating system and kernel settings already support SAP HANA Fast Restart. You need to define the `tmpfs` file system and configure SAP HANA.

To define the `tmpfs` file system and configure SAP HANA, you can follow the manual steps or use the automation script that Google Cloud provides to enable SAP HANA Fast Restart. For more information, see:

  * Manual steps: Enable SAP HANA Fast Restart
  * Automated steps: Enable SAP HANA Fast Restart



For the complete authoritative instructions for SAP HANA Fast Restart, see the [SAP HANA Fast Restart Option documentation](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/ce158d28135147f099b761f8b1ee43fc.html).

### Manual steps

#### Configure the `tmpfs` file system

After the host VMs and the base SAP HANA systems are successfully deployed, you need to create and mount directories for the NUMA nodes in the `tmpfs` file system.

##### Display the NUMA topology of your VM

Before you can map the required `tmpfs` file system, you need to know how many NUMA nodes your VM has. To display the available NUMA nodes on a Compute Engine VM, enter the following command:
    
    
    lscpu | grep NUMA

For example, an `m2-ultramem-208` VM type has four NUMA nodes, numbered 0-3, as shown in the following example:
    
    
    NUMA node(s):        4
    NUMA node0 CPU(s):   0-25,104-129
    NUMA node1 CPU(s):   26-51,130-155
    NUMA node2 CPU(s):   52-77,156-181
    NUMA node3 CPU(s):   78-103,182-207

##### Create the NUMA node directories

Create a directory for each NUMA node in your VM and set the permissions.

For example, for four NUMA nodes that are numbered 0-3:
    
    
    mkdir -pv /hana/tmpfs{0..3}/SID
    chown -R SID_LCadm:sapsys /hana/tmpfs*/SID
    chmod 777 -R /hana/tmpfs*/SID

##### Mount the NUMA node directories to `tmpfs`

Mount the `tmpfs` file system directories and specify a NUMA node preference for each with `mpol=prefer`:

SID specify the SID with uppercase letters.
    
    
    mount tmpfsSID0 -t tmpfs -o mpol=prefer:0 /hana/tmpfs0/SID
    mount tmpfsSID1 -t tmpfs -o mpol=prefer:1 /hana/tmpfs1/SID
    mount tmpfsSID2 -t tmpfs -o mpol=prefer:2 /hana/tmpfs2/SID
    mount tmpfsSID3 -t tmpfs -o mpol=prefer:3 /hana/tmpfs3/SID

**Note:** if you change machine types and the NUMA nodes increase or decrease, you need to modify the `tmpfs` file system and the `[persistence]` section of the SAP HANA INI file, shown in the next section, to match the new number of NUMA nodes.

##### Update `/etc/fstab`

To ensure that the mount points are available after an operating system reboot, add entries into the file system table, `/etc/fstab`:
    
    
    tmpfsSID0 /hana/tmpfs0/SID tmpfs rw,nofail,relatime,mpol=prefer:0
    tmpfsSID1 /hana/tmpfs1/SID tmpfs rw,nofail,relatime,mpol=prefer:1
    tmpfsSID1 /hana/tmpfs2/SID tmpfs rw,nofail,relatime,mpol=prefer:2
    tmpfsSID1 /hana/tmpfs3/SID tmpfs rw,nofail,relatime,mpol=prefer:3

#### Optional: set limits on memory usage

The `tmpfs` file system can grow and shrink dynamically.

To limit the memory used by the `tmpfs` file system, you can set a size limit for a NUMA node volume with the `size` option. For example:
    
    
    mount tmpfsSID0 -t tmpfs -o mpol=prefer:0,size=250G /hana/tmpfs0/SID

You can also limit overall `tmpfs` memory usage for all NUMA nodes for a given SAP HANA instance and a given server node by setting the `persistent_memory_global_allocation_limit` parameter in the `[memorymanager]` section of the `global.ini` file.

#### SAP HANA configuration for Fast Restart

To configure SAP HANA for Fast Restart, update the `global.ini` file and specify the tables to store in persistent memory.

##### Update the `[persistence]` section in the `global.ini` file

Configure the `[persistence]` section in the SAP HANA `global.ini` file to reference the `tmpfs` locations. Separate each `tmpfs` location with a semicolon:
    
    
    [persistence]
    basepath_datavolumes = /hana/data
    basepath_logvolumes = /hana/log
    basepath_persistent_memory_volumes = /hana/tmpfs0/SID;/hana/tmpfs1/SID;/hana/tmpfs2/SID;/hana/tmpfs3/SID

The preceding example specifies four memory volumes for four NUMA nodes, which corresponds to the `m2-ultramem-208`. If you were running on the `m2-ultramem-416`, you would need to configure eight memory volumes (0..7).

Restart SAP HANA after modifying the `global.ini` file.

SAP HANA can now use the `tmpfs` location as persistent memory space.

##### Specify the tables to store in persistent memory

Specify specific column tables or partitions to store in persistent memory.

For example, to turn on persistent memory for an existing table, execute the SQL query:
    
    
    ALTER TABLE exampletable persistent memory ON immediate CASCADE

To change the default for new tables add the parameter `table_default` in the `indexserver.ini` file. For example:
    
    
    [persistent_memory]
    table_default = ON

For more information on how to control columns, tables and which monitoring views provide detailed information, see [SAP HANA Persistent Memory](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/1f61b13e096d4ef98e62c676debf117e.html).

### Automated steps

The automation script that Google Cloud provides to enable SAP HANA Fast Restart makes changes to directories `/hana/tmpfs*`, file `/etc/fstab`, and SAP HANA configuration. When you run the script, you might need to perform additional steps depending on whether this is the initial deployment of your SAP HANA system or you are resizing your machine to a different NUMA size.

For the initial deployment of your SAP HANA system or resizing the machine to increase the number of NUMA nodes, make sure that SAP HANA is running during the execution of automation script that Google Cloud provides to enable SAP HANA Fast Restart.

When you resize your machine to decrease the number of NUMA nodes, make sure that SAP HANA is stopped during the execution of the automation script that Google Cloud provides to enable SAP HANA Fast Restart. After the script is executed, you need to manually update the SAP HANA configuration to complete the SAP HANA Fast Restart setup. For more information, see SAP HANA configuration for Fast Restart.

**Note:** We strongly recommend that you run the script that Google Cloud provides to enable SAP HANA Fast Restart in a non-production environment and verify the results thoroughly before running the script in production environments. You assume the responsibility for correctly enabling SAP HANA Fast Restart.

To enable SAP HANA Fast Restart, follow these steps:

  1. Establish an SSH connection with your host VM.

  2. Switch to root: 
         
         sudo su -

  3. Download the `sap_lib_hdbfr.sh` script:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/lib/sap_lib_hdbfr.sh

  4. Make the file executable:
         
         chmod +x sap_lib_hdbfr.sh

  5. Verify that the script has no errors: 
         
         vi sap_lib_hdbfr.sh
         ./sap_lib_hdbfr.sh -help

If the command returns an error, contact Cloud Customer Care. For more information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

  6. Run the script after replacing SAP HANA system ID (SID) and password for the SYSTEM user of the SAP HANA database. To securely provide the password, we recommend that you use a secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

Run the script by using the name of a secret in Secret Manager. This secret must exist in the Google Cloud project that contains your host VM instance.
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -s SECRET_NAME 

Replace the following:

     * `SID`: specify the SID with uppercase letters. For example, `AHA`.
     * `SECRET_NAME`: specify the name of the secret that corresponds to the password for the SYSTEM user of the SAP HANA database. This secret must exist in the Google Cloud project that contains your host VM instance.

Alternatively, you can run the script using a plain text password. After SAP HANA Fast Restart is enabled, make sure to change your password. Using plain text password is not recommended as your password would be recorded in the command-line history of your VM.
    
    sudo ./sap_lib_hdbfr.sh -h 'SID' -p 'PASSWORD'

Replace the following:

     * `SID`: specify the SID with uppercase letters. For example, `AHA`.
     * `PASSWORD`: specify the password for the SYSTEM user of the SAP HANA database.



For a successful initial run, you should see an output similar to the following:
    
    
    INFO - Script is running in standalone mode
    ls: cannot access '/hana/tmpfs*': No such file or directory
    INFO - Setting up HANA Fast Restart for system 'TST/00'.
    INFO - Number of NUMA nodes is 2
    INFO - Number of directories /hana/tmpfs* is 0
    INFO - HANA version 2.57
    INFO - No directories /hana/tmpfs* exist. Assuming initial setup.
    INFO - Creating 2 directories /hana/tmpfs* and mounting them
    INFO - Adding /hana/tmpfs* entries to /etc/fstab. Copy is in /etc/fstab.20220625_030839
    INFO - Updating the HANA configuration.
    INFO - Running command: select * from dummy
    DUMMY
    "X"
    1 row selected (overall time 4124 usec; server time 130 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistence', 'basepath_persistent_memory_volumes') = '/hana/tmpfs0/TST;/hana/tmpfs1/TST;'
    0 rows affected (overall time 3570 usec; server time 2239 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistent_memory', 'table_unload_action') = 'retain';
    0 rows affected (overall time 4308 usec; server time 2441 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('indexserver.ini', 'SYSTEM') SET ('persistent_memory', 'table_default') = 'ON';
    0 rows affected (overall time 3422 usec; server time 2152 usec)
    

## Download SUSE packages

Uninstall the resource agents used for scale-up deployments and replace them with the resource agents used for scale-out.

For SLES for SAP 15 SP6 or later, using the `SAPHanaSR-angi` package is recommended. For SLES for SAP 15 SP5 or earlier, you can use the `SAPHanaSR-ScaleOut` and `SAPHanaSR-ScaleOut-doc` packages.

### Manual steps

Perform the following steps on all hosts, including the majority maker instance:

  1. Uninstall the SAP HANA scale-up resource agents:
         
         zypper remove SAPHanaSR SAPHanaSR-doc

  2. Install the SAP HANA scale-out resource agents:

###  SLES for SAP 15 SP5 or earlier 
         
         zypper in SAPHanaSR-ScaleOut SAPHanaSR-ScaleOut-doc

###  SLES for SAP 15 SP6 or SP7
         
         zypper install SAPHanaSR-angi

###  SLES for SAP 16 or later
         
         zypper install SAPHanaSR-angi

  3. Install `socat`:
         
         zypper install socat

  4. Install the latest operating system patches:
         
         zypper patch




### Automated steps

Alternatively, to automate this process for all instances listed in `nodes.txt`, run the following script from Google Cloud console:

###  SLES for SAP 15 SP5 or earlier 
    
    
    while read -u10 HOST ;  do gcloud compute ssh --zone $HOST -- "sudo zypper remove -y SAPHanaSR SAPHanaSR-doc; sudo zypper in -y SAPHanaSR-ScaleOut SAPHanaSR-ScaleOut-doc socat; sudo zypper patch -y"; done 10< nodes.txt

###  SLES for SAP 15 SP6 or SP7 
    
    
    while read -u10 HOST ;  do gcloud compute ssh --zone $HOST -- "sudo zypper remove -y SAPHanaSR SAPHanaSR-doc; sudo zypper in -y SAPHanaSR-angi socat; sudo zypper patch -y"; done 10< nodes.txt

###  SLES for SAP 16 or later 
    
    
    while read -u10 HOST ;  do gcloud compute ssh --zone $HOST -- "sudo zypper remove -y SAPHanaSR SAPHanaSR-doc; sudo zypper in -y SAPHanaSR-angi socat; sudo zypper patch -y"; done 10< nodes.txt

## Back up the databases

Create backups of your databases to initiate database logging for SAP HANA system replication and create a recovery point.

If you have multiple tenant databases in an MDC configuration, then back up each tenant database.

To create backups of new SAP HANA databases, complete the following steps:

  1. On the primary host, switch to the `SID_LCadm` user. Depending on your OS image, the command might be different.
         
         sudo -i -u SID_LCadm

  2. Create database backups:

     * For a SAP HANA single-database-container system:
           
           > hdbsql -t -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"

The following example shows a successful response from a new SAP HANA system:
           
           0 rows affected (overall time 18.416058 sec; server time 18.414209 sec)

     * For a SAP HANA multi-database-container system (MDC), create a backup of the system database as well as any tenant databases:
           
           > hdbsql -t -d SYSTEMDB -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"
           
           > hdbsql -t -d SID -u system -p SYSTEM_PASSWORD -i INST_NUM \
             "backup data using file ('full')"

The following example shows a successful response from a new SAP HANA system:
           
           0 rows affected (overall time 16.590498 sec; server time 16.588806 sec)

  3. Confirm that the logging mode is set to normal:
         
         > hdbsql -u system -p SYSTEM_PASSWORD -i INST_NUM \
           "select value from "SYS"."M_INIFILE_CONTENTS" where key='log_mode'"

The output is similar to the following:
         
         VALUE
         "normal"




## Enable SAP HANA system replication

As a part of enabling SAP HANA system replication, you need to copy the data and key files for the SAP HANA secure stores on the file system (SSFS) from the primary host to the secondary host. The method that this procedure uses to copy the files is just one possible method that you can use.

  1. On the primary host as `SID_LCadm`, enable system replication:
         
         > hdbnsutil -sr_enable --name=PRIMARY_HOST_NAME

  2. On the secondary host:

     1. As `SID_LCadm`, stop SAP HANA:
            
            > sapcontrol -nr INST_NUM -function StopSystem

     2. As root, archive the existing SSFS data and key files:
            
            # cd /usr/sap/SID/SYS/global/security/rsecssfs/
            # mv data/SSFS_SID.DAT data/SSFS_SID.DAT-ARC
            # mv key/SSFS_SID.KEY key/SSFS_SID.KEY-ARC

     3. Copy the data file from the primary host:
            
            # scp -o StrictHostKeyChecking=no \
            PRIMARY_HOST_NAME:/usr/sap/SID/SYS/global/security/rsecssfs/data/SSFS_SID.DAT \
            /usr/sap/SID/SYS/global/security/rsecssfs/data/SSFS_SID.DAT

     4. Copy the key file from the primary host:
            
            # scp -o StrictHostKeyChecking=no \
            PRIMARY_HOST_NAME:/usr/sap/SID/SYS/global/security/rsecssfs/key/SSFS_SID.KEY \
            /usr/sap/SID/SYS/global/security/rsecssfs/key/SSFS_SID.KEY

     5. Update ownership of the files:
            
            # chown SID_LCadm:sapsys /usr/sap/SID/SYS/global/security/rsecssfs/data/SSFS_SID.DAT
            # chown SID_LCadm:sapsys /usr/sap/SID/SYS/global/security/rsecssfs/key/SSFS_SID.KEY

     6. Update permissions for the files:
            
            # chmod 644 /usr/sap/SID/SYS/global/security/rsecssfs/data/SSFS_SID.DAT
            # chmod 640 /usr/sap/SID/SYS/global/security/rsecssfs/key/SSFS_SID.KEY

     7. As SID_LCadm, register the secondary SAP HANA system with SAP HANA system replication:
            
            > hdbnsutil -sr_register --remoteHost=PRIMARY_HOST_NAME --remoteInstance=INST_NUM \
            --replicationMode=syncmem --operationMode=logreplay --name=SECONDARY_HOST_NAME

     8. As SID_LCadm, start SAP HANA:
            
            > sapcontrol -nr INST_NUM -function StartSystem




### Validating system replication

On the primary host as `SID_LCadm`, confirm that SAP HANA system replication is active by running the following python script:
    
    
    $ python $DIR_INSTANCE/exe/python_support/systemReplicationStatus.py

If replication is set up properly, among other indicators, the following values are displayed for the `xsengine`, `nameserver`, and `indexserver` services:

  * The `Secondary Active Status` is `YES`
  * The `Replication Status` is `ACTIVE`



Also, the `overall system replication status` shows `ACTIVE`.

## Enable the SAP HANA HA/DR provider hooks

SUSE recommends that you enable the SAP HANA HA/DR provider hooks, which let SAP HANA to send out notifications for certain events and improves failure detection. The SAP HANA HA/DR provider hooks require SAP HANA 2.0 SPS 03 or a later version for the `SAPHanaSR` hook, and SAP HANA 2.0 SPS 05 or a later version for `SAPHanaSR-angi` hook.

**Note:** If you want to implement the HA/DR provider hooks on a pre-existing SAP HANA system with near-zero downtime, then instead refer to the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide). 

On both the primary and secondary site, complete the following steps:

  1. As `SID_LCadm`, stop SAP HANA:
         
         > sapcontrol -nr 00 -function StopSystem

  2. As root or `SID_LCadm`, open the `global.ini` file for editing:
         
         > vi /hana/shared/SID/global/hdb/custom/config/global.ini

  3. Add the following definitions to the `global.ini` file:

###  SLES for SAP 15 SP5 or earlier 
         
         [ha_dr_provider_saphanasrmultitarget]
         provider = SAPHanaSrMultiTarget
         path = /usr/share/SAPHanaSR-ScaleOut/
         execution_order = 1
         
         [ha_dr_provider_sustkover]
         provider = susTkOver
         path = /usr/share/SAPHanaSR-ScaleOut/
         execution_order = 2
         sustkover_timeout = 30
         
         [ha_dr_provider_suschksrv]
         provider = susChkSrv
         path = /usr/share/SAPHanaSR-ScaleOut/
         execution_order = 3
         action_on_lost = stop
         
         [trace]
         ha_dr_saphanasrmultitarget = info
         ha_dr_sustkover = info

###  SLES for SAP 15 SP6 or SP7 
         
         [ha_dr_provider_susHanaSR]
         provider = susHanaSR
         path = /usr/share/SAPHanaSR-angi
         execution_order = 1
         
         [ha_dr_provider_suschksrv]
         provider = susChkSrv
         path = /usr/share/SAPHanaSR-angi
         execution_order = 3
         action_on_lost = kill
         
         [ha_dr_provider_susTkOver]
         provider = susTkOver
         path = /usr/share/SAPHanaSR-angi
         execution_order = 2
         sustkover_timeout = 30
         
         [trace]
         ha_dr_sushanasr = info
         ha_dr_suschksrv = info
         ha_dr_sustkover = info

The `action_on_lost` parameter defines the action that the hook must take when it identifies a lost `indexserver`.

For the `action_on_lost` parameter, you can choose one of the following values:

     * `ignore`: The hook does nothing and writes to trace files.
     * `stop`: The hook triggers `sapcontrol ... StopSystem`.
     * `kill`: The hook triggers `HDB kill-<signal>`.
     * `fence`: The hook triggers `crm node fence <host>`.

For more information, see the [`susCheckSrv.py`](https://github.com/SUSE/SAPHanaSR/blob/main/man/susChkSrv.py.7) man page.

###  SLES for SAP 16 or later 
    
    [ha_dr_provider_susHanaSR]
    provider = susHanaSR
    path = /usr/share/SAPHanaSR-angi
    execution_order = 1
    
    [ha_dr_provider_suschksrv]
    provider = susChkSrv
    path = /usr/share/SAPHanaSR-angi
    execution_order = 3
    action_on_lost = kill
    
    [ha_dr_provider_susTkOver]
    provider = susTkOver
    path = /usr/share/SAPHanaSR-angi
    execution_order = 2
    sustkover_timeout = 30
    
    [trace]
    ha_dr_sushanasr = info
    ha_dr_suschksrv = info
    ha_dr_sustkover = info

The `action_on_lost` parameter defines the action that the hook must take when it identifies a lost `indexserver`.

For the `action_on_lost` parameter, you can choose one of the following values:

     * `ignore`: The hook does nothing and writes to trace files.
     * `stop`: The hook triggers `sapcontrol ... StopSystem`.
     * `kill`: The hook triggers `HDB kill-<signal>`.
     * `fence`: The hook triggers `crm node fence <host>`.

For more information, see the [`susCheckSrv.py`](https://github.com/SUSE/SAPHanaSR/blob/main/man/susChkSrv.py.7) man page.

  4. As root, create a custom configuration file in the `/etc/sudoers.d` directory by running the following command. This new configuration file allows the `SID_LCadm` user to access the cluster node attributes when the `srConnectionChanged()` hook method is called.
         
         > visudo -f /etc/sudoers.d/SAPHanaSR

  5. In the `/etc/sudoers.d/SAPHanaSR` file, add the following text:

###  SLES for SAP 15 SP5 or earlier 

Replace `SID_LC` with the SID in lowercase letters. 
         
         SID_LCadm ALL=(ALL) NOPASSWD: /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_*
         SID_LCadm ALL=(ALL) NOPASSWD: /usr/sbin/crm_attribute -n hana_SID_LC_gsh *
         SID_LCadm ALL=(ALL) NOPASSWD: /usr/sbin/SAPHanaSR-hookHelper --sid=SID_LC *

###  SLES for SAP 15 SP6 or SP7 

Replace the following: 

     * `SITE_A`: the site name of the primary SAP HANA server
     * `SITE_B`: the site name of the secondary SAP HANA server
     * `SID_LC`: the SID, specified using lowercase letters
To view the site names, you can run the `crm_mon -A1 | grep site` command as the root user, on either the SAP HANA primary server or the secondary server. 
    
    Cmnd_Alias SOK_SITEA = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SFAIL_SITEA = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SFAIL -t crm_config -s SAPHanaSR
    Cmnd_Alias SOK_SITEB = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SFAIL_SITEB = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SFAIL -t crm_config -s SAPHanaSR
    SID_LCadm ALL=(ALL) NOPASSWD: /usr/bin/SAPHanaSR-hookHelper --sid=SID --case=*
    SID_LCadm ALL=(ALL) NOPASSWD: SOK_SITEA, SFAIL_SITEA, SOK_SITEB, SFAIL_SITEB

###  SLES for SAP 16 or later 

Replace the following: 

     * `SITE_A`: the site name of the primary SAP HANA server
     * `SITE_B`: the site name of the secondary SAP HANA server
     * `SID_LC`: the SID, specified using lowercase letters
To view the site names, you can run the `crm_mon -A1 | grep site` command as the root user, on either the SAP HANA primary server or the secondary server. 
    
    Cmnd_Alias SOK_SITEA = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SFAIL_SITEA = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_A -v SFAIL -t crm_config -s SAPHanaSR
    Cmnd_Alias SOK_SITEB = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SOK -t crm_config -s SAPHanaSR
    Cmnd_Alias SFAIL_SITEB = /usr/sbin/crm_attribute -n hana_SID_LC_site_srHook_SITE_B -v SFAIL -t crm_config -s SAPHanaSR
    SID_LCadm ALL=(ALL) NOPASSWD: /usr/bin/SAPHanaSR-hookHelper --sid=SID --case=*
    SID_LCadm ALL=(ALL) NOPASSWD: SOK_SITEA, SFAIL_SITEA, SOK_SITEB, SFAIL_SITEB

  6. In your `/etc/sudoers` file, make sure that the following text is included:

     * For SLES for SAP 15 SP3 or later: 
           
           **@** includedir /etc/sudoers.d

     * For versions up to SLES for SAP 15 SP2: 
           
           **#** includedir /etc/sudoers.d

Note that the `#` in this text is part of the syntax and does not mean that the line is a comment.

**Note:** While the procedure in this section is recommended by SUSE, you can use an alternative approach. Instead of creating a drop-in configuration file, you can add the required access directly to your `/etc/sudoers` file.
  7. As `SID_LCadm`, start SAP HANA:
         
         > sapcontrol -nr 00 -function StartSystem

  8. After you complete the cluster configuration for SAP HANA, you can verify that the hook functions correctly during a failover test as described in [Troubleshooting the SAPHanaSR python hook](https://www.suse.com/support/kb/doc/?id=000019865) and [HA cluster takeover takes too long on HANA indexserver failure](https://www.suse.com/support/kb/doc/?id=000020845). 




## Configure the Cloud Load Balancing failover support

The internal passthrough Network Load Balancer service with failover support routes traffic to the active host in an SAP HANA cluster based on a health check service.

### Reserve an IP address for the virtual IP

The virtual IP (VIP) address , which is sometimes referred to as a _floating_ IP address, follows the active SAP HANA system. The load balancer routes traffic that is sent to the VIP to the VM that is currently hosting the active SAP HANA system.

  1. Open Cloud Shell:

[Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Reserve an IP address for the virtual IP. This is the IP address that applications use to access SAP HANA. If you omit the `--addresses` flag, an IP address in the specified subnet is chosen for you:
         
         $ [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) VIP_NAME \
           --region CLUSTER_REGION --subnet CLUSTER_SUBNET \
           --addresses VIP_ADDRESS

For more information about reserving a static IP, see [Reserving a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

  3. Confirm IP address reservation:
         
         $ [gcloud compute addresses describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) VIP_NAME \
           --region CLUSTER_REGION

You should see output similar to the following example:
         
         address: 10.0.0.19
         addressType: INTERNAL
         creationTimestamp: '2020-05-20T14:19:03.109-07:00'
         description: ''
         id: '8961491304398200872'
         kind: compute#address
         name: vip-for-hana-ha
         networkTier: PREMIUM
         purpose: GCE_ENDPOINT
         region: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/addresses/vip-for-hana-ha
         status: RESERVED
         subnetwork: https://www.googleapis.com/compute/v1/projects/example-project-123456/regions/us-central1/subnetworks/example-subnet-us-central1




### Create instance groups for your host VMs

  1. In Cloud Shell, create two unmanaged instance groups and assign the primary master host VM to one and the secondary master host VM to the other:
         
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) PRIMARY_IG_NAME \
           --zone=PRIMARY_ZONE \
           --instances=PRIMARY_HOST_NAME
         $ [gcloud compute instance-groups unmanaged create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE
         $ [gcloud compute instance-groups unmanaged add-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) SECONDARY_IG_NAME \
           --zone=SECONDARY_ZONE \
           --instances=SECONDARY_HOST_NAME
         

  2. Confirm the creation of the instance groups:
         
         $ [gcloud compute instance-groups unmanaged list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/list)

You should see output similar to the following example:
         
         NAME          ZONE           NETWORK          NETWORK_PROJECT        MANAGED  INSTANCES
         hana-ha-ig-1  us-central1-a  example-network  example-project-123456 No       1
         hana-ha-ig-2  us-central1-c  example-network  example-project-123456 No       1




### Create a Compute Engine health check

  1. In Cloud Shell, create the health check. For the port used by the health check, choose a port that is in the private range, 49152-65535, to avoid clashing with other services. The check-interval and timeout values are slightly longer than the defaults so as to increase failover tolerance during Compute Engine live migration events. You can adjust the values, if necessary:
         
         $ [gcloud compute health-checks create tcp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/tcp) HEALTH_CHECK_NAME --port=HEALTHCHECK_PORT_NUM \
           --proxy-header=NONE --check-interval=10 --timeout=10 --unhealthy-threshold=2 \
           --healthy-threshold=2

  2. Confirm the creation of the health check:
         
         $ [gcloud compute health-checks describe HEALTH_CHECK_NAME](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/describe)

You should see output similar to the following example:
         
         checkIntervalSec: 10
         creationTimestamp: '2020-05-20T21:03:06.924-07:00'
         healthyThreshold: 2
         id: '4963070308818371477'
         kind: compute#healthCheck
         name: hana-health-check
         selfLink: https://www.googleapis.com/compute/v1/projects/example-project-123456/global/healthChecks/hana-health-check
         tcpHealthCheck:
          port: 60000
          portSpecification: USE_FIXED_PORT
          proxyHeader: NONE
         timeoutSec: 10
         type: TCP
         unhealthyThreshold: 2




### Create a firewall rule for the health checks

Define a firewall rule for a port in the private range that allows access to your host VMs from the IP ranges that are used by Compute Engine health checks, `35.191.0.0/16` and `130.211.0.0/22`. For more information, see [Creating firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

  1. If you don't already have one, add a network tag to your host VMs. This network tag is used by the firewall rule for health checks.
         
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) PRIMARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone PRIMARY_ZONE
         $ [gcloud compute instances add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) SECONDARY_HOST_NAME \
           --tags NETWORK_TAGS \
           --zone SECONDARY_ZONE
         

  2. If you don't already have one, create a firewall rule to allow the health checks:
         
         $ [gcloud compute firewall-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) RULE_NAME \
           --network NETWORK_NAME \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags NETWORK_TAGS \
           --rules tcp:HLTH_CHK_PORT_NUM

For example:
         
         gcloud compute firewall-rules create  fw-allow-health-checks \
         --network example-network \
         --action ALLOW \
         --direction INGRESS \
         --source-ranges 35.191.0.0/16,130.211.0.0/22 \
         --target-tags cluster-ntwk-tag \
         --rules tcp:60000




### Configure the load balancer and failover group

  1. Create the load balancer backend service:
         
         $ [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) BACKEND_SERVICE_NAME \
           --load-balancing-scheme internal \
           --health-checks HEALTH_CHECK_NAME \
           --no-connection-drain-on-failover \
           --drop-traffic-if-unhealthy \
           --failover-ratio 1.0 \
           --region CLUSTER_REGION \
           --global-health-checks

  2. Add the primary instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group PRIMARY_IG_NAME \
           --instance-group-zone PRIMARY_ZONE \
           --region CLUSTER_REGION

  3. Add the secondary, failover instance group to the backend service:
         
         $ [gcloud compute backend-services add-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) BACKEND_SERVICE_NAME \
           --instance-group SECONDARY_IG_NAME \
           --instance-group-zone SECONDARY_ZONE \
           --failover \
           --region CLUSTER_REGION

  4. Create a forwarding rule. For the IP address, specify the IP address that you reserved for the VIP. If you need to access the SAP HANA system from outside of the region that is specified below, include the flag `--allow-global-access` in the definition:
         
         $ [gcloud compute forwarding-rules create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) RULE_NAME \
           --load-balancing-scheme internal \
           --address VIP_ADDRESS \
           --subnet CLUSTER_SUBNET \
           --region CLUSTER_REGION \
           --backend-service BACKEND_SERVICE_NAME \
           --ports ALL

For more information about cross-region access to your SAP HANA high-availability system, see [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal#client-access).


**Note:** Your backend instance groups won't register as healthy until you have completed the Pacemaker cluster configuration.

### Test the load balancer configuration

Even though your backend instance groups won't register as healthy until later, you can test the load balancer configuration by setting up a listener to respond to the health checks. After setting up a listener, if the load balancer is configured correctly, the status of the backend instance groups changes to healthy.

The following sections present different methods that you can use to test the configuration.

#### Testing the load balancer with the `socat` utility

You can use the `socat` utility to temporarily listen on the health check port. You need to install the `socat`utility anyway, because you use it later when you configure cluster resources.

  1. On both primary and secondary master host VMs as root, install the `socat` utility:
         
         # zypper install -y socat

  2. Start a `socat` process to listen for 60 seconds on the health check port:
         
         # timeout 60s socat - TCP-LISTEN:HLTH_CHK_PORT_NUM,fork

  3. In Cloud Shell, after waiting a few seconds for the health check to detect the listener, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/hana-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/hana-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/hana-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/hana-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth




#### Testing the load balancer using port 22

If port 22 is open for SSH connections on your host VMs, you can temporarily edit the health checker to use port 22, which has a listener that can respond to the health checker.

To temporarily use port 22, follow these steps:

  1. Click your health check in the console:

[Go to Health checks page](https://console.cloud.google.com/compute/healthChecks)

  2. Click **Edit**.

  3. In the **Port** field, change the port number to 22.

  4. Click **Save** and wait a minute or two.

  5. In Cloud Shell, check the health of your backend instance groups:
         
         $ [gcloud compute backend-services get-health](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) BACKEND_SERVICE_NAME \
           --region CLUSTER_REGION

You should see output similar to the following:
         
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instanceGroups/hana-ha-ig-1
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-a/instances/hana-ha-vm-1
            ipAddress: 10.0.0.35
            port: 80
          kind: compute#backendServiceGroupHealth
         ---
         backend: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instanceGroups/hana-ha-ig-2
         status:
          healthStatus:
          ‐ healthState: HEALTHY
            instance: https://www.googleapis.com/compute/v1/projects/example-project-123456/zones/us-central1-c/instances/hana-ha-vm-2
            ipAddress: 10.0.0.34
            port: 80
          kind: compute#backendServiceGroupHealth

  6. When you are done, change the health check port number back to the original port number.




## Set up Pacemaker

The following procedure configures the SUSE implementation of a Pacemaker cluster on Compute Engine VMs for SAP HANA.

For more information about the configuring high-availability clusters on SLES, see the [SUSE Linux Enterprise High Availability Extension](https://documentation.suse.com/#sle-ha) documentation for your version of SLES.

### Initialize the cluster

On the primary host as root, initialize the cluster:

###  SLES 15 
    
    
    crm cluster init -y

###  SLES 12 
    
    
    ha-cluster-init -y

Ignore the warnings related to SBD and default password. SBD and default password are not used in this deployment.

### Configure the cluster

Perform the following steps on the primary host as root.

#### Enable maintenance mode

Put the Pacemaker cluster in maintenance mode:
    
    
    crm configure property maintenance-mode="true"

#### Configure the general cluster properties

Configure the following general cluster properties:
    
    
    crm configure property stonith-timeout="300s"
    crm configure property stonith-action="reboot"
    crm configure property stonith-enabled="true"
    crm configure property cluster-infrastructure="corosync"
    crm configure property cluster-name="hacluster"
    crm configure property placement-strategy="balanced"
    crm configure property no-quorum-policy="freeze"
    crm configure property concurrent-fencing="true"
    
    crm configure rsc_defaults migration-threshold="50"
    crm configure rsc_defaults resource-stickiness="1000"
    
    crm configure op_defaults timeout="600"

### Edit the corosync.conf default settings

  1. Open the `/etc/corosync/corosync.conf` file using an editor of your choice.

  2. Remove the `consensus` parameter.

  3. Modify the remaining parameters according to Google Cloud's recommendations.

The following table shows the `totem` parameters for which Google Cloud recommends values, along with the impact of changing the values. For the default values of these parameters, which can differ between Linux distributions, see the documentation for your Linux distribution. Parameter | Recommended value | Impact of changing the value  
---|---|---  
`secauth` | `off` | Disables authentication and encryption of all `totem` messages.  
`join` | 60 (ms) | Increases how long the node waits for `join` messages in the membership protocol.  
`max_messages` | 20 | Increases the maximum number of messages that might be sent by the node after receiving the token.  
`token` | 20000 (ms) |  Increases how long the node waits for a `totem` protocol token before the node declares a token loss, assumes a node failure, and starts taking action.  Increasing the value of the `token` parameter makes the cluster more tolerant of momentary infrastructure events, such as a live migration. However, it can also make the cluster take longer to detect and recover from a node failure.  The value of the `token` parameter also determines the default value of the `consensus` parameter, which controls how long a node waits for consensus to be achieved before it attempts to re-establish configuration membership.   
`consensus` | N/A |  Specifies, in milliseconds, how long to wait for consensus to be achieved before starting a new round of membership configuration.  We recommend that you omit this parameter. When the `consensus` parameter is not specified, Corosync sets its value to 1.2 times the value of the `token` parameter. If you use the `token` parameter's recommended value of `20000`, then the `consesus` parameter is set with the value `24000`.  If you explicitly specify a value for `consensus`, then make sure that the value is `24000` or `1.2*token`, whichever is greater.   
`token_retransmits_before_loss_const` | 10 | Increases the number of token retransmits that the node attempts before it concludes that the recipient node has failed and takes action.  
`transport` | 
     * For SLES: `udpu`
     * For RHEL 8 or later: `knet`
     * For RHEL 7: `udpu`
| Specifies the transport mechanism used by corosync.  



#### Join all hosts to Pacemaker cluster

Join all other hosts, including the majority maker, to the Pacemaker cluster on the primary host:

##### Manual steps

###  SLES 15 
    
    
    crm cluster join -y -c PRIMARY_HOST_NAME

###  SLES 12 
    
    
    ha-cluster-join -y -c PRIMARY_HOST_NAME

##### Automated steps

Alternatively, to automate this process for all instances listed in `nodes.txt`, run the following script from Google Cloud console:
    
    
    while read -u10 HOST ;  do echo "Joining $HOST to Pacemaker cluster";
    gcloud compute ssh --tunnel-through-iap --quiet --zone $HOST -- sudo ha-cluster-join -y -c PRIMARY_HOST_NAME;
    done 10< nodes.txt

Ignore the error message `ERROR: cluster.join: Abort: Cluster is currently active` that is triggered when joining the primary node to itself. 

From any host as root, confirm that the cluster shows all nodes:
    
    
    # crm_mon -s

You should see output similar to the following:
    
    
    CLUSTER OK: 5 nodes online, 0 resources configured

### Set up fencing

You set up fencing by defining a cluster resource with a fence agent for each host VM.

To ensure the correct sequence of events after a fencing action, you also configure the operating system to delay the restart of Corosync after a VM is fenced. You also adjust the Pacemaker timeout for reboots to account for the delay.

#### Create the fencing device resources

#### Manual steps

On the primary host, as root, create the fencing resources for all nodes in the primary and secondary cluster:

  1. Run the following command after replacing `PRIMARY_HOST_NAME` with the hostname of a node in the primary cluster:
         
         # crm configure primitive STONITH-"PRIMARY_HOST_NAME" stonith:fence_gce \
             op monitor interval="300s" timeout="120s" \
             op start interval="0" timeout="60s" \
             params port="PRIMARY_HOST_NAME" zone="PRIMARY_ZONE" project="PROJECT_ID" \
             pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30

  2. Repeat the previous step for all other nodes in the primary cluster.

  3. Run the following command after replacing `SECONDARY_HOST_NAME` with the hostname of a node in the secondary cluster.
         
         # crm configure primitive STONITH-"SECONDARY_HOST_NAME" stonith:fence_gce \
             op monitor interval="300s" timeout="120s" \
             op start interval="0" timeout="60s" \
             params port="SECONDARY_HOST_NAME" zone="SECONDARY_ZONE" project="PROJECT_ID" \
             pcmk_reboot_timeout=300 pcmk_monitor_retries=4

  4. Repeat the previous step for all other nodes in the secondary cluster.

  5. Run the following command after replacing `MAJORITY_MAKER_HOSTNAME` with the hostname of the majority maker instance:
         
         # crm configure primitive STONITH-"MAJORITY_MAKER_HOSTNAME" stonith:fence_gce \
             op monitor interval="300s" timeout="120s" \
             op start interval="0" timeout="60s" \
             params port="MAJORITY_MAKER_HOSTNAME" zone="MAJORITY_MAKER_ZONE" project="PROJECT_ID" \
             pcmk_reboot_timeout=300 pcmk_monitor_retries=4

  6. Set the location of the fencing device:
         
         # crm configure location LOC_STONITH_"PRIMARY_HOST_NAME" \
             STONITH-"PRIMARY_HOST_NAME" -inf: "PRIMARY_HOST_NAME"

  7. Repeat the previous step for all other hosts on the primary and secondary clusters including the majority maker host.




### Set a delay for the restart of Corosync

#### Manual steps

  1. On all hosts as root, create a `systemd` drop-in file that delays the startup of Corosync to ensure the proper sequence of events after a fenced VM is rebooted:
         
         systemctl edit corosync.service

  2. Add the following lines to the file:
         
         [Service]
         ExecStartPre=/bin/sleep 60

  3. Save the file and exit the editor.

  4. Reload the systemd manager configuration.
         
         systemctl daemon-reload

  5. Confirm the drop-in file was created:
         
         service corosync status

You should see a line for the drop-in file, as shown in the following example:
         
         ● corosync.service - Corosync Cluster Engine
            Loaded: loaded (/usr/lib/systemd/system/corosync.service; disabled; vendor preset: disabled)
           **Drop-In: /etc/systemd/system/corosync.service.d
                    └─override.conf**
            Active: active (running) since Tue 2021-07-20 23:45:52 UTC; 2 days ago




#### Automated steps

Alternatively, to automate this process for all instances listed in `nodes.txt`, run the following script from Google Cloud console:
    
    
    while read -u10 HOST;  do gcloud compute ssh --tunnel-through-iap --quiet --zone $HOST   --  "sudo mkdir -p /etc/systemd/system/corosync.service.d/; sudo echo -e '[Service]\nExecStartPre=/bin/sleep 60' | sudo tee -a /etc/systemd/system/corosync.service.d/override.conf; sudo systemctl daemon-reload"; done 10< nodes.txt

### Create a local cluster IP resource for the VIP address

To configure the VIP address in the operating system, create a local cluster IP resource for the VIP address that you reserved earlier:
    
    
    # crm configure primitive rsc_vip_int-primary IPaddr2 \
         params ip=VIP_ADDRESS cidr_netmask=32 nic="lo" op monitor interval=3600s timeout=60s

**Note:** To ensure that the SAP HANA cluster is future compatible and supports `systemd` dynamic NIC naming convention, use the loopback interface (`lo`) with the `IPaddr2` resource configuration instead of a static interface name like `ethX` or `ensX`.

### Set up the helper health-check service

The load balancer uses a listener on the health-check port of each host to determine where the primary instance of the SAP HANA cluster is running.

To manage the listeners in the cluster, you create a resource for the listener.

These instructions use the `socat` utility as the listener.

  1. On both hosts as root, install the `socat utility`:
         
         # zypper in -y socat

  2. On the primary host create a resource for the helper health-check service:
         
         crm configure primitive rsc_healthcheck-primary anything \
         params binfile="/usr/bin/socat" \
         cmdline_options="-U TCP-LISTEN:HEALTHCHECK_PORT_NUM,backlog=10,fork,reuseaddr /dev/null" \
         op monitor timeout=20s interval=10s \
         op_params depth=0

  3. Group the VIP and helper health-check service resources:
         
         # crm configure group g-primary rsc_vip_int-primary rsc_healthcheck-primary meta resource-stickiness="0"




### Create the `SAPHanaTopology` primitive resource

You define the `SAPHanaTopology` primitive resource in a temporary configuration file, which you then upload to Corosync.

On the primary host as root:

  1. Create a temporary configuration file for the `SAPHanaTopology` configuration parameters:
         
         # vi /tmp/cluster.tmp

  2. Copy and paste the `SAPHanaTopology` resource definitions into the `/tmp/cluster.tmp` file:

###  SLES for SAP 15 SP5 or earlier 
         
         primitive rsc_SAPHanaTopology_SID_HDBINST_NUM ocf:suse:SAPHanaTopology \
          operations \$id="rsc_sap2_SID_HDBINST_NUM-operations" \
          op monitor interval="10" timeout="600" \
          op start interval="0" timeout="600" \
          op stop interval="0" timeout="300" \
          params SID="SID" InstanceNumber="INST_NUM"
         
         clone cln_SAPHanaTopology_SID_HDBINST_NUM rsc_SAPHanaTopology_SID_HDBINST_NUM \
          meta clone-node-max="1" target-role="Started" interleave="true"
          location SAPHanaTop_not_on_majority_maker cln_SAPHanaTopology_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

###  SLES for SAP 15 SP6 or SP7 
         
         primitive rsc_SAPHanaTopology_SID_HDBINST_NUM ocf:suse:SAPHanaTopology \
          operations \$id="rsc_sap2_SID_HDBINST_NUM-operations" \
          op monitor interval="10" timeout="600" \
          op start interval="0" timeout="600" \
          op stop interval="0" timeout="300" \
          params SID="SID" InstanceNumber="INST_NUM"
         
         clone cln_SAPHanaTopology_SID_HDBINST_NUM rsc_SAPHanaTopology_SID_HDBINST_NUM \
          meta clone-node-max="1" interleave="true"
          location SAPHanaTop_not_on_majority_maker cln_SAPHanaTopology_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

###  SLES for SAP 16 or later 
         
         primitive rsc_SAPHanaTopology_SID_HDBINST_NUM ocf:suse:SAPHanaTopology \
          operations \$id="rsc_sap2_SID_HDBINST_NUM-operations" \
          op monitor interval="10" timeout="600" \
          op start interval="0" timeout="600" \
          op stop interval="0" timeout="300" \
          params SID="SID" InstanceNumber="INST_NUM"
         
         clone cln_SAPHanaTopology_SID_HDBINST_NUM rsc_SAPHanaTopology_SID_HDBINST_NUM \
          meta clone-node-max="1" interleave="true"
          location SAPHanaTop_not_on_majority_maker cln_SAPHanaTopology_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

  3. Edit the `/tmp/cluster.tmp` file to replace the variable text with the SID and instance number for your SAP HANA system.

  4. On the primary as root, load the contents of the `/tmp/cluster.tmp` file into Corosync:
         
         crm configure load update /tmp/cluster.tmp




### Create the `SAPHana` primitive resource

You define the `SAPHana` primitive resource by using the same method that you used for the `SAPHanaTopology` resource: in a temporary configuration file, which you then upload to Corosync.

  1. Replace the temporary configuration file:
         
         # rm /tmp/cluster.tmp
         # vi /tmp/cluster.tmp

  2. Copy and paste the `SAPHana` resource definitions into the `/tmp/cluster.tmp` file:

###  SLES for SAP 15 SP5 or earlier 
         
         primitive rsc_SAPHana_SID_HDBINST_NUM ocf:suse:SAPHanaController \
          operations \$id="rsc_sap_SID_HDBINST_NUM-operations" \
          op start interval="0" timeout="3600" \
          op stop interval="0" timeout="3600" \
          op promote interval="0" timeout="3600" \
          op demote interval="0" timeout="3600" \
          op monitor interval="60" role="Master" timeout="700" \
          op monitor interval="61" role="Slave" timeout="700" \
          params SID="SID" InstanceNumber="INST_NUM" PREFER_SITE_TAKEOVER="true" \
          DUPLICATE_PRIMARY_TIMEOUT="7200" AUTOMATED_REGISTER="true"
         
         ms msl_SAPHana_SID_HDBINST_NUM rsc_SAPHana_SID_HDBINST_NUM \
          meta master-node-max="1" master-max="1" clone-node-max="1" \
          target-role="Started" interleave="true"
         
         colocation col_saphana_ip_SID_HDBINST_NUM 4000: g-primary:Started \
          msl_SAPHana_SID_HDBINST_NUM:Master
         order ord_SAPHana_SID_HDBINST_NUM Optional: cln_SAPHanaTopology_SID_HDBINST_NUM \
          msl_SAPHana_SID_HDBINST_NUM
          location SAPHanaCon_not_on_majority_maker  msl_SAPHana_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

###  SLES for SAP 15 SP6 or SP7 
         
         primitive rsc_SAPHana_SID_HDBINST_NUM ocf:suse:SAPHanaController \
          operations \$id="rsc_sap_SID_HDBINST_NUM-operations" \
          op start interval="0" timeout="3600" \
          op stop interval="0" timeout="3600" \
          op promote interval="0" timeout="3600" \
          op demote interval="0" timeout="3600" \
          op monitor interval="60" role="Promoted" timeout="700" \
          op monitor interval="61" role="Unpromoted" timeout="700" \
          params SID="SID" InstanceNumber="INST_NUM" PREFER_SITE_TAKEOVER="true" \
          DUPLICATE_PRIMARY_TIMEOUT="7200" AUTOMATED_REGISTER="true" \
          HANA_CALL_TIMEOUT="120" ON_FAIL_ACTION="fence"
         
         clone mst_SAPHana_SID_HDBINST_NUM rsc_SAPHana_SID_HDBINST_NUM \
          meta clone-node-max="1" \
          target-role="Started" interleave="true" promotable="true"
         
         colocation col_saphana_ip_SID_HDBINST_NUM 4000: g-primary:Started \
          mst_SAPHana_SID_HDBINST_NUM:Promoted
         
         order ord_SAPHana_SID_HDBINST_NUM Optional: cln_SAPHanaTopology_SID_HDBINST_NUM \
          mst_SAPHana_SID_HDBINST_NUM
          location SAPHanaCon_not_on_majority_maker  mst_SAPHana_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

###  SLES for SAP 16 or later 
         
         primitive rsc_SAPHana_SID_HDBINST_NUM ocf:suse:SAPHanaController \
          operations \$id="rsc_sap_SID_HDBINST_NUM-operations" \
          op start interval="0" timeout="3600" \
          op stop interval="0" timeout="3600" \
          op promote interval="0" timeout="3600" \
          op demote interval="0" timeout="3600" \
          op monitor interval="60" role="Promoted" timeout="700" \
          op monitor interval="61" role="Unpromoted" timeout="700" \
          params SID="SID" InstanceNumber="INST_NUM" PREFER_SITE_TAKEOVER="true" \
          DUPLICATE_PRIMARY_TIMEOUT="7200" AUTOMATED_REGISTER="true" \
          HANA_CALL_TIMEOUT="120" ON_FAIL_ACTION="fence"
         
         clone mst_SAPHana_SID_HDBINST_NUM rsc_SAPHana_SID_HDBINST_NUM \
          meta clone-node-max="1" \
          target-role="Started" interleave="true" promotable="true"
         
         colocation col_saphana_ip_SID_HDBINST_NUM 4000: g-primary:Started \
          mst_SAPHana_SID_HDBINST_NUM:Promoted
         
         order ord_SAPHana_SID_HDBINST_NUM Optional: cln_SAPHanaTopology_SID_HDBINST_NUM \
          mst_SAPHana_SID_HDBINST_NUM
          location SAPHanaCon_not_on_majority_maker  mst_SAPHana_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

Optionally, you can add the `ON_FAIL_ACTION` parameter to the `SAPHanaController` resource. This parameter defines how the resource agent escalates monitoring failures on the SAP HANA primary node. The `ON_FAIL_ACTION` parameter accepts following values:

     * `proceed`: This value directs the resource agent to proceed with the failure as usual and initiate the "demote-stop" sequence. This is the default value.
     * `fence`: This value directs the resource agent to trigger the sequence of actions that follow a failed "stop" action, which includes fencing the concerned node.

For more information, see the [`SAPHanaController-scale-out`](https://github.com/SUSE/SAPHanaSR/blob/main/man/SAPHanaController-scale-out.7) man page.

For a [multi-tier](https://help.sap.com/viewer/4e9b18c116aa42fc84c7dbfd02111aba/2.0.05/en-US/2e6c71ab55f147e19b832565311a8e4e.html) SAP HANA HA cluster, if you are using a version earlier than SAP HANA 2.0 SP03, set `AUTOMATED_REGISTER` to `false`. This prevents a recovered instance from attempting to self-register for replication to a HANA system that already has a replication target configured. For SAP HANA 2.0 SP03 or later, you can set `AUTOMATED_REGISTER` to `true` for SAP HANA configurations that use multitier system replication. For additional information, see:

     * [SAP HANA System Replication Scale-Up](https://documentation.suse.com/sbp/all/single-html/SLES4SAP-hana-sr-guide-PerfOpt-15/)
     * [HANA Scale-Up HA with System Replication & Automated Failover](https://blogs.sap.com/2018/10/23/hana-scale-up-ha-with-system-replication-automated-failover-using-suse-hae-on-sles-12-sp-3-part-3/)
  3. On the primary as root, load the contents of the `/tmp/cluster.tmp` file into Corosync:
         
         crm configure load update /tmp/cluster.tmp




### Create the `SAPHanaFilesystem` primitive resource

This section is applicable only when you're using the `SAPHanaSR-angi` hook. If you're not using the `SAPHanaSR-angi` hook, then skip this section.

You create the `SAPHanaFilesystem` resource by using the same method that you used for the `SAPHanaTopology` resource - you define it in a temporary configuration file that you upload to Corosync:

  1. Replace the temporary configuration file:
         
         rm /tmp/cluster.tmp
         vi /tmp/cluster.tmp

  2. Copy and paste the `SAPHana` resource definitions into the `/tmp/cluster.tmp` file:
         
         primitive rsc_SAPHanaFileSystem_SID_HDBINST_NUM ocf:suse:SAPHanaFilesystem \
          operations \$id="rsc_sap3_SID_HDBINST_NUM-operations" \
          op monitor interval="10" timeout="600" \
          op start interval="0" timeout="600" \
          op stop interval="0" timeout="300" \
          params SID="SID" InstanceNumber="INST_NUM"
         
         clone cln_SAPHanaFileSystem_SID_HDBINST_NUM rsc_SAPHanaFileSystem_SID_HDBINST_NUM \
          meta clone-node-max="1  interleave="true"
          location SAPHanaFil_not_on_majority_maker cln_SAPHanaFil_SID_HDBINST_NUM -inf: MAJORITY_MAKER_HOSTNAME

Optionally, you can add the `ON_FAIL_ACTION` parameter to the `SAPHanaFilesystem` resource. This parameter defines the internal resource agent decision in case of a monitoring failure. The `ON_FAIL_ACTION` parameter accepts following values:

     * `ignore`: This value directs the resource agent to report the failure information into the logs and take no further action.
     * `fence`: This value directs the resource agent to trigger the sequence of actions that follow a failed "stop" action, which includes fencing the concerned node. This is the default value.

For more information, see the [`SAPHanaFilesystem`](https://github.com/SUSE/SAPHanaSR/blob/main/man/ocf_suse_SAPHanaFilesystem.7) man page.

  3. On the primary node, as the root user, load the contents of the `/tmp/cluster.tmp` file into Corosync:
         
         crm configure load update /tmp/cluster.tmp




### Confirm SAP HANA system replication is active

On the primary host as SID_LCadm, check the replication status:
    
    
    # python $DIR_INSTANCE/exe/python_support/systemReplicationStatus.py

### Activate the cluster

  1. On the primary host as root, take the cluster out of maintenance mode:
         
         # crm configure property maintenance-mode="false"

If you receive a prompt that asks you to remove "maintenance", enter `y`.

  2. Wait for 15 seconds and then on the primary host as root, check the status of the cluster:
         
         # crm status

The following examples shows the status of an active, properly configured cluster:

###  SLES for SAP 15 SP5 or earlier 
         
         7 nodes configured
         21 resources configured
         Online: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 sap-majoritymaker ]
         
         
         Full list of resources:
         
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-1w1 (stonith:fence_gce):  Started hana-ha-vm-1
         STONITH-hana-ha-vm-1w2 (stonith:fence_gce):  Started hana-ha-vm-2
         STONITH-sap-majoritymaker      (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):  Started hana-ha-vm-2w1
         STONITH-hana-ha-vm-2w1 (stonith:fence_gce):  Started hana-ha-vm-2w2
         STONITH-hana-ha-vm-2w2 (stonith:fence_gce):  Started sap-majoritymaker
         Clone Set: cln_SAPHanaTopology_HA1_HDB22 [rsc_SAPHanaTopology_HA1_HDB22]
             Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]
         Resource Group: g-primary
             rsc_vip_int-primary        (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1
             rsc_healthcheck-primary    (ocf::heartbeat:anything):      Started hana-ha-vm-1
         Clone Set: msl_SAPHana_HA1_HDB22 [rsc_SAPHana_HA1_HDB22] (promotable)
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]

###  SLES for SAP 15 SP6 or SP7 
         
         7 nodes configured
         30 resources configured
         Online: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 sap-majoritymaker ]
         
         
         Full list of resources:
         
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-1w1 (stonith:fence_gce):  Started hana-ha-vm-1
         STONITH-hana-ha-vm-1w2 (stonith:fence_gce):  Started hana-ha-vm-2
         STONITH-sap-majoritymaker      (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):  Started hana-ha-vm-2w1
         STONITH-hana-ha-vm-2w1 (stonith:fence_gce):  Started hana-ha-vm-2w2
         STONITH-hana-ha-vm-2w2 (stonith:fence_gce):  Started sap-majoritymaker
         Clone Set: cln_SAPHanaTopology_HA1_HDB22 [rsc_SAPHanaTopology_HA1_HDB22]
             Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]
         Resource Group: g-primary
             rsc_vip_int-primary        (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1
             rsc_healthcheck-primary    (ocf::heartbeat:anything):      Started hana-ha-vm-1
         Clone Set: mst_SAPHana_HA1_HDB22 [rsc_SAPHana_HA1_HDB22] (promotable)
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]
         Clone Set: cln_SAPHanaFileSystem_HA1_HDB22 [rsc_SAPHanaFileSystem_HA1_HDB22]
             Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]

###  SLES for SAP 16 or later 
         
         7 nodes configured
         30 resources configured
         Online: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 sap-majoritymaker ]
         
         
         Full list of resources:
         
         
         STONITH-hana-ha-vm-1   (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-1w1 (stonith:fence_gce):  Started hana-ha-vm-1
         STONITH-hana-ha-vm-1w2 (stonith:fence_gce):  Started hana-ha-vm-2
         STONITH-sap-majoritymaker      (stonith:fence_gce):  Started hana-ha-vm-1w2
         STONITH-hana-ha-vm-2   (stonith:fence_gce):  Started hana-ha-vm-2w1
         STONITH-hana-ha-vm-2w1 (stonith:fence_gce):  Started hana-ha-vm-2w2
         STONITH-hana-ha-vm-2w2 (stonith:fence_gce):  Started sap-majoritymaker
         Clone Set: cln_SAPHanaTopology_HA1_HDB22 [rsc_SAPHanaTopology_HA1_HDB22]
             Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]
         Resource Group: g-primary
             rsc_vip_int-primary        (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-1
             rsc_healthcheck-primary    (ocf::heartbeat:anything):      Started hana-ha-vm-1
         Clone Set: mst_SAPHana_HA1_HDB22 [rsc_SAPHana_HA1_HDB22] (promotable)
             Masters: [ hana-ha-vm-1 ]
             Slaves: [ hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]
         Clone Set: cln_SAPHanaFileSystem_HA1_HDB22 [rsc_SAPHanaFileSystem_HA1_HDB22]
             Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-1w2 hana-ha-vm-2 hana-ha-vm-2w1 hana-ha-vm-2w2 ]
             Stopped: [ sap-majoritymaker ]




## Test failover

Test your cluster by simulating a failure on the primary host. Use a test system or run the test on your production system before you release the system for use.

Backup the system before the test.

You can simulate a failure in a variety of ways, including:

  * `HDB stop`
  * `HDB kill`
  * `iptables ... DROP` for instances with multiple network interfaces
  * `echo c > /proc/sysrq-trigger`



These instructions use `iptables` to simulate a network disruption between your two hosts in the cluster. Use the `ip link` command on an instance with a single network interface and use the `iptables` command on instances with one or more network interfaces. The test validates both failover as well as fencing. In the case where your instances have multiple network interfaces defined, you use the `iptables` command on the secondary host to drop incoming and outgoing traffic based on the IP used by the primary host for cluster communication, thereby simulating a network connection loss to the primary.

  1. On the secondary host, as root, use the `iptables` command to drop all incoming and outgoing network traffic to primary host.
         
         # iptables -A INPUT -s PRIMARY_CLUSTER_IP -j DROP; iptables -A OUTPUT -d PRIMARY_CLUSTER_IP -j DROP

  2. Once the primary host is fenced and restarted, delete the added lines from iptable on secondary host to re-initiate the network traffic to primary host. Reconnect to either host by using SSH and change to the root user.
         
         # iptables -D INPUT -s PRIMARY_CLUSTER_IP -j DROP; iptables -D OUTPUT -d PRIMARY_CLUSTER_IP -j DROP

  3. Enter `crm status` to confirm that the primary host is now active on the VM that used to contain the secondary host. Automatic restart is enabled in the cluster, so the stopped host restarts and assumes the role of secondary host, as shown in the following example.

###  SLES for SAP 15 SP5 or earlier 
         
         Stack: corosync
         Current DC: hana-ha-vm-2 (version 2.0.1+20190417.13d370ca9-3.9.1-2.0.1+20190417.13d370ca9) - partition with quorum
         Last updated: Fri Jun 12 16:46:07 2020
         Last change: Fri Jun 12 16:46:07 2020 by root via crm_attribute on hana-ha-vm-2
         
         2 nodes configured
         8 resources configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 hana-ha-vm-1w1 hana-ha-vm-2w1]
         
         Full list of resources:
         
          STONITH-hana-ha-vm-1   (stonith:fence_gce):  Started hana-ha-vm-2
          STONITH-hana-ha-vm-2   (stonith:fence_gce):  Started hana-ha-vm-1
          STONITH-hana-ha-vm-1w1   (stonith:fence_gce):    Started hana-ha-vm-2w1
          STONITH-hana-ha-vm-1w1   (stonith:fence_gce):    Started hana-ha-vm-mm
          STONITH-hana-ha-vm-mm   (stonith:fence_gce):    Started hana-ha-vm-1w1
          Clone Set: cln_SAPHanaTopology_HA1_HDB22 [rsc_SAPHanaTopology_HA1_HDB22]
              Started: [ hana-ha-vm-1 hana-ha-vm-2 hana-ha-vm-1w1 hana-ha-vm-2w1
              Stopped: [ hana-ha-vm-mm ]]
          Resource Group: g-primary
              rsc_vip_int-primary        (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-2
              rsc_healthcheck-primary        (ocf::heartbeat:anything):      Started hana-ha-vm-2
          Clone Set: msl_SAPHana_HA1_HDB22 [rsc_SAPHana_HA1_HDB22] (promotable)
              Masters: [ hana-ha-vm-2 ]
              Slaves: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-2w1
              Stopped: [ hana-ha-vm-mm ]]

###  SLES for SAP 15 SP6 or later 
         
         Stack: corosync
         Current DC: hana-ha-vm-2 (version 2.1.7+20231219.0f7f88312-150600.6.3.1-2.1.7+20231219.0f7f88312) - partition with quorum
         Last updated: Thu Dec 12 12:40:27 2024
         Last change: Thu Dec 12 12:46:27 2024 by root via crm_attribute on hana-ha-vm-2
         
         5 nodes configured
         22 resources configured
         
         Online: [ hana-ha-vm-1 hana-ha-vm-2 hana-ha-vm-1w1 hana-ha-vm-2w1]
         
         Full list of resources:
         
          STONITH-hana-ha-vm-1   (stonith:fence_gce):  Started hana-ha-vm-2
          STONITH-hana-ha-vm-2   (stonith:fence_gce):  Started hana-ha-vm-1
          STONITH-hana-ha-vm-1w1   (stonith:fence_gce):    Started hana-ha-vm-2w1
          STONITH-hana-ha-vm-1w1   (stonith:fence_gce):    Started hana-ha-vm-mm
          STONITH-hana-ha-vm-mm   (stonith:fence_gce):    Started hana-ha-vm-1w1
          Clone Set: cln_SAPHanaTopology_HA1_HDB22 [rsc_SAPHanaTopology_HA1_HDB22]
              Started: [ hana-ha-vm-1 hana-ha-vm-2 hana-ha-vm-1w1 hana-ha-vm-2w1
              Stopped: [ hana-ha-vm-mm ]]
          Resource Group: g-primary
              rsc_vip_int-primary        (ocf::heartbeat:IPaddr2):       Started hana-ha-vm-2
              rsc_healthcheck-primary        (ocf::heartbeat:anything):      Started hana-ha-vm-2
          Clone Set: mst_SAPHana_HA1_HDB22 [rsc_SAPHana_HA1_HDB22] (promotable)
              Masters: [ hana-ha-vm-2 ]
              Slaves: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-2w1
              Stopped: [ hana-ha-vm-mm ]]
          Clone Set: cln_SAPHanaFileSystem_HA1_HDB22 [rsc_SAPHanaFileSystem_HA1_HDB22]
              Started: [ hana-ha-vm-1 hana-ha-vm-1w1 hana-ha-vm-2 hana-ha-vm-2w1 ]
              Stopped: [ sap-majoritymaker ]




## Evaluate your SAP HANA workload

To automate continuous validation checks for your SAP HANA high-availability workloads running on Google Cloud, you can use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

Workload Manager lets you automatically scan and evaluate your SAP HANA high-availability workloads against best practices from SAP, Google Cloud, and OS vendors. This helps improve the quality, performance, and reliability of your workloads.

For information about the best practices that Workload Manager supports for evaluating SAP HANA high-availability workloads running on Google Cloud, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices). For information about creating and running an evaluation using Workload Manager, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).

## Troubleshooting

To troubleshoot problems with high-availability configurations for SAP HANA on SLES, see [Troubleshooting high-availability configurations for SAP](https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha).

## Getting support for SAP HANA on SLES

If you need help resolving a problem with high-availability clusters for SAP HANA on SLES, gather the required diagnostic information and contact Cloud Customer Care. For more information, see [High-availability clusters on SLES diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-ha-sles).

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



### Connecting to SAP HANA

If the host VMs don't have an external IP address for SAP HANA, you can only connect to the SAP HANA instances through the bastion instance using SSH or through the Windows server through SAP HANA Studio.

  * To connect to SAP HANA through the bastion instance, connect to the bastion host, and then to the SAP HANA instance(s) by using an SSH client of your choice.

  * To connect to the SAP HANA database through SAP HANA Studio, use a remote desktop client to connect to the Windows Server instance. After connection, manually [install SAP HANA Studio](https://help.sap.com/hana/SAP_HANA_Studio_Installation_Update_Guide_en.pdf) and access your SAP HANA database.




## Post-deployment tasks

After you complete the deployment, finish with the following steps:

  1. Change the temporary passwords for the SAP HANA system administrator and database superuser. For example:
         
         sudo passwd SID_LCadm

For information from SAP about changing the password, see [Reset the `SYSTEM` User Password of the System Database](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/6b13cdd1982f4aa6b90b443663d17d7e.html).

  2. Before using your SAP HANA instance, configure and backup your new SAP HANA database.

  3. If your SAP HANA system is deployed on a VirtIO network interface, then we recommend that you ensure the value of the TCP parameter `/proc/sys/net/ipv4/tcp_limit_output_bytes` is set to `1048576`. This modification helps improve the overall network throughput on the VirtIO network interface without affecting the network latency. 




For more information, see:

  * [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).
  * [SAP HANA Installation and Update Guide](http://help.sap.com/hana/SAP_HANA_Server_Installation_Guide_en.pdf).



## What's next

See the following resource for more information: 

* [Automated SAP HANA System Replication in Scale-Up in pacemaker cluster](https://access.redhat.com/articles/3004101)
* [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide)
* [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide)
* For more information about VM administration and monitoring, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
