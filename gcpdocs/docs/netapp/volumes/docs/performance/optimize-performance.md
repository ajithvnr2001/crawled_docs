---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance/
title: Optimize performance \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T06:00:24.836067+00:00
---

# Optimize performance  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Optimize performance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can optimize Google Cloud NetApp Volumes performance by adjusting volume and client-side configurations. These adjustments enhance throughput, reduce latency, and improve overall data transfer efficiency for your applications.

## Before you begin

Before you make changes to your volumes to optimize performance, review [performance considerations](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing).

## Adjust volume settings

You can optimize performance by adjusting the following volume settings:

  * **Increase volume capacity** : you can increase the capacity of your Premium, Extreme or Standard service level volume to improve maximum achievable volume throughput. For volumes of the Flex File service level, increase storage pool's capacity instead. For the Flex Unified or Flex File custom-performance, increase the storage pool's throughput and IOPS.

  * **Upgrade your service level** : you can move a Premium service level volume to a storage pool with an Extreme service level to improve throughput.

  * **Use manual QoS pools to assign greater throughput** : you can decrease the assigned throughput of larger volumes with low throughput requirements, and increase the throughput of smaller volumes that need higher performance up to the available pool throughput.




Increasing volume capacity and upgrading service levels are both non-disruptive to I/O workloads in process on the volume and don't affect access to the volume in any way.

## Adjust the client

You can improve performance by adjusting the following settings on the client:

  * **Co-locate clients** : latency results are directly impacted by the capabilities and location of the client. For best results, place the client in the same region as the volume or as close as possible. Test the zonal impact by testing latency from a client in each zone and use the zone with the lowest latency.

  * **Configure Compute Engine network bandwidth** : the network capabilities of Compute Engine virtual machines depend on the instance type used. Typically, larger instances can drive more network throughput. We recommend that you select a client virtual machine with an appropriate network bandwidth capability, select the Google Virtual NIC (gVNIC) network interface and enable `Tier_1` performance. For more information, see Compute Engine documentation on [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

  * **Optimize your client settings** : for Linux clients, see [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).




## What's next

Read about [manual QoS](https://docs.cloud.google.com/netapp/volumes/docs/performance/manual-qos).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
