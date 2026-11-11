---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/platform-application/pa-ao-operations/metrics-vmm/
title: Virtual Machine Management (VMM) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:51:39.607680+00:00
---

# Virtual Machine Management (VMM)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/platform-application/pa-ao-operations/metrics-vmm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag)



Send feedback 

#  Virtual Machine Management (VMM) Stay organized with collections  Save and categorize content based on your preferences. 

Virtual Machine Management (VMM) metrics track CPU, memory, disk, and network usage for virtual machines (VMs) in your Google Distributed Cloud (GDC) air-gapped projects. Your default permissions let you view metrics for the VMs in your projects. Platform administrator (PA) permissions also grant access to metrics for user workload VMs and Kubernetes cluster node VMs across all projects. GDC doesn't support guest environment metrics on Windows VMs.

For information about the VM-level metrics dashboard and how it visualizes these metrics, see [Monitor VM metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/monitor/monitor-metrics).

## Metrics list

Use the `namespace` label to filter the VMs in different namespaces.

Name and Description | Type | Scrape interval | Labels  
---|---|---|---  
`compute_instance_cpu_usage`  
The amount of time each vCPU spends in different states. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **state** : The state of the vCPU, such as running, stopped, or paused.
  * **id** : The numerical index of the vCPU, which ranges from `0` to the maximum vCPU count `- 1`.

  
`compute_instance_memory_available_bytes`  
The amount of memory available to the VM. | Gauge | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.

  
`compute_instance_memory_usable_bytes`  
The amount of memory that you can give to the VM from the available memory without having to use the swap or ballooning. | Gauge | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.

  
`compute_instance_memory_total_bytes`  
The amount of memory that the VM actually uses. | Gauge | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.

  
`compute_instance_disk_bytes_allocated`  
Count of bytes totally allocated to the disk from the underlying storage system. | Gauge | 1 min | 

  * **name** : The name of the VM disk.
  * **namespace** : The project to which the VM disk belongs.
  * **pvc** : The underlying `PersistentVolumeClaim` name.

  
`compute_instance_disk_bytes_used`  
Count of bytes that the disk uses in the underlying storage system. This metric reflects on total disk storage being utilized. However, the metric lacks visibility into the actual file system usage, which is only known to the guest operating system. | Gauge | 1 min | 

  * **name** : The name of the VM disk.
  * **namespace** : The project to which the VM disk belongs.
  * **pvc** : The underlying `PersistentVolumeClaim` name.

  
`compute_instance_disk_read_bytes_count`  
Count of bytes read from disk. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_write_bytes_count`  
Count of bytes written to disk. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_read_ops_count`  
Count of disk I/O read operations. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_write_ops_count`  
Count of disk I/O write operations. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_read_time_ms`  
The cumulative time spent on the read operations that are in progress. That is, the actual time in queue and when disks are busy. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_write_time_ms`  
The cumulative time spent on the write operations that are in progress. That is, the actual time in queue and when disks are busy. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **drive** : The name of the VM disk drive.

  
`compute_instance_disk_flush_requests_total`  
Storage flush requests. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.

  
`compute_instance_disk_flush_times_ms`  
Total time in microseconds spent on cache flushing. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.

  
`compute_instance_network_received_bytes_count`  
Count of bytes received from the network. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_received_packet_count`  
Count of the packets received from the network. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_sent_bytes_count`  
Count of bytes sent to the network. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_sent_packet_count`  
Count of packets sent to the network. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_receive_errors_count`  
Count of error packets received. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_receive_packets_dropped_count`  
The number of RX packets dropped on vNIC interfaces. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_transmit_errors_count`  
Count of network error packets transmitted. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
`compute_instance_network_transmit_packets_dropped_count`  
The number of TX packets dropped on vNIC interfaces. | Counter | 10 s | 

  * **name** : The name of the VM.
  * **namespace** : The project associated with the VM.
  * **interface** : The network interface name, such as eth0.
  * **network** : The name of the network. For example, `pod-network`.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
