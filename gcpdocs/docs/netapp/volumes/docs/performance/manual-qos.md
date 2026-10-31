---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/manual-qos/
title: Manual quality of service (QoS) \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:02.493583+00:00
---

# Manual quality of service (QoS)  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/manual-qos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manual quality of service (QoS) Stay organized with collections  Save and categorize content based on your preferences. 

In Google Cloud NetApp Volumes, manual quality of service (QoS) lets you configure volume throughput and IOPS limits independently of capacity to meet workload requirements and control storage costs.

## Benefits

Manual QoS offers the following benefits:

  * **Cost optimization** : Scale volume performance within your storage pool capacity to optimize cloud costs.

  * **Instant throughput adjustment** : Adjust volume throughput without downtime.

  * **Disaster recovery cost reduction** : Lower QoS for replicated volumes to reduce disaster recovery costs for destination pools.

  * **Enhanced performance for clones or caches** : Increase performance for clone or cache volumes with small allocated sizes.

  * **Flexible workload management** : Host multiple workloads in a single storage pool and adjust the throughput for each volume as needed.




## Considerations

Before you configure manual QoS, consider the following guidelines:

  * You can manage manual QoS using the Google Cloud CLI, NetApp Volumes API, or Terraform. The Google Cloud console isn't supported.

  * Manual QoS is supported for the Flex Unified, Standard, Premium, and Extreme service levels and isn't available for the Flex File service level.




## Manage manual QoS for Flex Unified Default-mode, Standard, Premium, and Extreme service levels

For volumes within a manual QoS storage pool, you can set throughput and capacity independently. The overall throughput of all volumes in a manual QoS pool is limited by the pool's total throughput. Pool throughput is determined by its allocated capacity and service level. For example, a 40 TiB Premium pool can achieve a maximum throughput of 2,560 MiBps at 64 MiBps per TiB, while a 200 TiB Extreme pool can support volumes with a combined throughput of 25,600 MiBps.

**Important:** You can create a new manual QoS pool or change an existing auto QoS pool to manual. This change is permanent, and you can't convert a manual QoS pool back to an auto QoS pool. However, you can move volumes from a manual pool to an auto pool.

After you set up the manual QoS pool, you can set the required throughput limit for each volume within it. The maximum throughput limit for a single volume is 4.5 GiBps, or 30 GiBps for [large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes).

The pool and volume commands or APIs display available and assigned throughput values for the pool to help you manage the total throughput. To create a manual QoS pool and define volume throughput, see Create a storage pool and Create a volume.

To configure throughput and IOPS limits using QoS policy groups in Flex Unified ONTAP-mode pools, see Manage manual QoS for Flex Unified ONTAP-mode.

### Create a storage pool

Create a storage pool using manual QoS for the Standard, Premium, or Extreme service levels:
    
    
      gcloud netapp storage-pools create POOL_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --capacity=CAPACITY \
        --service-level=SERVICE_LEVEL \
        --qos-type=QOS_TYPE \
        --network=name=NETWORK_NAME

Replace the following information:

  * `POOL_NAME`: the name of the pool you want to create. Your pool name must be unique per location.

  * `PROJECT_NAME`: the name of the project you want to create the storage pool in.

  * `LOCATION`: the location of the pool you want to create.

  * `CAPACITY`: the capacity of the pool in GiB.

  * `SERVICE_LEVEL`: the service level for your storage pool: `Standard`, `Premium`, or `Extreme`.

  * `QOS_TYPE`: the QoS type of your storage pool: `auto` or `manual`.

  * `NETWORK_NAME`: the name of the Virtual Private Cloud network.




Create a storage pool using manual QoS for the Flex Unified Default-mode service level:
    
    
      gcloud netapp storage-pools create POOL_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --capacity=CAPACITY \
        --service-level=flex \
        --type=unified \
        --mode=default \
        --qos-type=QOS_TYPE \
        --network=name=NETWORK_NAME

Replace the following information:

  * `POOL_NAME`: the name of the pool you want to create. Your pool name must be unique per location.

  * `PROJECT_NAME`: the name of the project you want to create the storage pool in.

  * `LOCATION`: the location of the pool you want to create.

  * `CAPACITY`: the capacity of the pool in GiB.

  * `QOS_TYPE`: the QoS type of your storage pool: `auto` or `manual`.

  * `NETWORK_NAME`: the name of the VPC network.




### Edit a storage pool

Edit an existing auto QoS storage pool to use manual QoS:
    
    
      gcloud netapp storage-pools update POOL_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --qos-type=QOS_TYPE

Replace the following information:

  * `POOL_NAME`: the name of the pool you want to update.

  * `PROJECT_NAME`: the name of the project.

  * `LOCATION`: the location of the pool.

  * `QOS_TYPE`: the updated QoS type for your storage pool. Only `manual` configuration is supported.




### Create a volume

Create a volume with a specified manual QoS throughput limit:
    
    
      gcloud netapp volumes create VOLUME_NAME \
        --project=PROJECT_NAME \
        --location=LOCATION \
        --storage-pool=STORAGE_POOL \
        --capacity=CAPACITY \
        --protocols=PROTOCOLS \
        --share-name=SHARE_NAME \
        --throughput-mibps=THROUGHPUT_MIBPS

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `PROJECT_NAME`: the name of the project in which to create the volume.

  * `LOCATION`: the location for the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume in GiB. This value defines the capacity that NAS clients see.

  * `PROTOCOLS`: the NAS protocols that the volume is exported with. Valid choices are NFSv3, NFSv4, SMB, and the following combinations:

    * `nfsv3,nfsv4`
    * `nfsv3,smb`
    * `nfsv4,smb`

Depending on the protocol type you choose, we recommend that you add the protocol-specific flags such as `--export-policy` or `--smb-settings`.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

  * `THROUGHPUT_MIBPS`: the throughput limit of the volume in MiBps.




For more information about additional optional flags, see [Google Cloud SDK documentation about volume creation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create).

## Manage manual QoS for Flex Unified ONTAP-mode service level

In Flex Unified ONTAP-mode storage pools, you can set throughput and IOPS limits by using QoS policy groups (QPGs). You can create multiple QPGs and assign volumes to them based on your workload performance needs. Using QPGs helps prevent one workload from affecting others and provides consistent performance across multiple workloads in a single Flex Unified ONTAP-mode pool. As performance needs change, you can move existing volumes to a different QPG without downtime.

QoS policy groups offer the following features:

  * **Dedicated versus shared performance allocation** : Choose whether throughput and IOPS limits are shared across all volumes in the QPG (`is-shared=true`) or applied separately to each volume (`is-shared=false`).

  * **Granular throughput and IOPS limits** : Set maximum throughput (MiBps) and IOPS limits for each policy group to meet your application performance goals.

  * **Dynamic volume assignment** : Assign volumes to a policy group when you create them, change the assignment while workloads are running, or keep volumes assigned to the default shared performance setting for the pool (`qos-policy-group none`).

  * **Live limit modifications** : Change throughput and IOPS limits for existing QoS policy groups in real time without interrupting I/O or causing storage downtime.




### Create a new QoS policy group

Create a new QoS policy group in an ONTAP-mode storage pool:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "qos policy-group create -policy-group QPG_NAME -vserver SVM_NAME -max-throughput IOPS,THROUGHPUT -is-shared IS_SHARED_TRUE_OR_FALSE"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `QPG_NAME`: the name of the QPG you want to create.

  * `SVM_NAME`: the name of the storage virtual machine (SVM).

  * `IOPS`: the IOPS limit to assign to the volumes in the QPG. Specify an integer value with a minimum of 1 IOPS.

  * `THROUGHPUT`: the maximum throughput limit to assign to the volumes in the QPG. Specify an integer value with a minimum of 1 MiBps.

  * `IS_SHARED_TRUE_OR_FALSE`: a boolean value that specifies how QoS limits are applied. Specify `true` to enable shared QoS for all volumes assigned to the QPG, or `false` to enable dedicated QoS for each volume individually. This property is immutable and can't be updated after you create the QPG.




### Assign a QoS policy group to a volume

Assign a QoS policy group when you create a volume:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "volume create -volume VOLUME_NAME -vserver SVM_NAME -aggregate AGGREGATE_NAME -size SIZE -junction-path /VOLUME_NAME -qos-policy-group QPG_NAME"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `VOLUME_NAME`: the name of the new volume that you want to create.

  * `SVM_NAME`: the name of the SVM.

  * `AGGREGATE_NAME`: the name of the aggregate.

  * `SIZE`: the size of the volume in GiB.

  * `QPG_NAME`: the name of the QPG to assign to the volume.




### Assign a QoS policy group to an existing volume

Assign a QoS policy group to an existing volume:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "volume modify -vserver SVM_NAME -volume VOLUME_NAME -qos-policy-group QPG_NAME"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `SVM_NAME`: the name of the SVM.

  * `VOLUME_NAME`: the name of the volume to which you want to assign the QPG.

  * `QPG_NAME`: the name of the new QPG to assign to the volume.




### Remove a QoS policy group from a volume

Remove a QoS policy group from a volume by setting `-qos-policy-group` to `none`:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "volume modify -vserver SVM_NAME -volume VOLUME_NAME -qos-policy-group none"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `SVM_NAME`: the name of the SVM.

  * `VOLUME_NAME`: the name of the volume from which you want to remove the QPG.




### Modify a QoS policy group

Update the throughput and IOPS limits for an existing QoS policy group:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "qos policy-group modify -policy-group QPG_NAME -max-throughput IOPS,THROUGHPUT"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `QPG_NAME`: the name of the QPG that you want to modify.

  * `IOPS`: the updated maximum IOPS limit for the QPG. The minimum value is 1 IOPS.

  * `THROUGHPUT`: the updated maximum throughput limit for the QPG. The minimum value is 1 MiBps.




### Delete a QoS policy group

**Note:** Before you delete a QoS policy group, remove the QPG from all assigned volumes or assign a different QPG to those volumes. If the QPG is still assigned to any volumes, the delete command fails.

Delete a QoS policy group:
    
    
      gcloud netapp storage-pools execute STORAGE_POOL_NAME \
        --location=LOCATION \
        -- "qos policy-group delete -policy-group QPG_NAME"

Replace the following information:

  * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool.

  * `LOCATION`: the location of the ONTAP-mode storage pool.

  * `QPG_NAME`: the name of the QPG that you want to delete.




## What's next

Read about [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
