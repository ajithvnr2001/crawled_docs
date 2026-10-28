---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/
title: AlloyDB Omni performance tuning parameters on a VM \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:43:14.495114+00:00
---

# AlloyDB Omni performance tuning parameters on a VM  |  AlloyDB Omni using RPM: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Flinux%2Fcurrent%2Fdocs%2Fperformance-tuning-parameters%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/reference/database-flags)


Was this helpful?
Send feedback 
#  AlloyDB Omni performance tuning parameters on a VM Stay organized with collections  Save and categorize content based on your preferences.
Select a documentation version:  18.4.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/performance-tuning-parameters)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/performance-tuning-parameters)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/performance-tuning-parameters)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/performance-tuning-parameters)

This document describes performance tuning parameters that can improve AlloyDB Omni performance on a VM. These suggested tuning parameters are based on the results of running a set of workloads that exhibit different read and write patterns, caching behaviors, and index access patterns. 
Most default PostgreSQL parameter values remain unchanged, because the changes are limited to parameters that benefit the majority of applications. The suggested values of these parameters should generally improve performance on modern hardware.  
| Database parameter  | AlloyDB Omni default  | Suggested setting  |  
| --- | --- | --- |  
| `random_page_cost`  | 4.0  | 1.1  |  
| `temp_buffers`  | 8 MB  | 128 MB  |  
| `max_wal_size`  | 1 GB  | 20 GB  |  
| `min_wal_size`  | 80 MB  | 10 GB  |  
| `default_toast_compression`  | pglz  | lz4  |  
| `maintenance_work_mem`  | 64 MB  | 1 GB for smaller machines 2 GB for larger machines  |  
| `max_worker_processes`  | 64  | `max(64, # vCPUs)`  |  
| `max_parallel_workers`  | 8  | `max(8, # vCPUs)`  |  
| `max_parallel_workers_per_gather`  | 2  | `max(2, # vCPUs / 2)`  |  
| `work_mem`  | 4 MB  | 128 to 512 MB, depending on workload and the amount of memory available  |  
| `effective_cache_size`  | 40% * DRAM  | 80% * DRAM  |  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
