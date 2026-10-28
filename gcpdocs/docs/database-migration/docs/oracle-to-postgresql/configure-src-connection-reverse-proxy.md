---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/
title: Use source private IP connectivity with a reverse proxy \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:09:13.300151+00:00
---

# Use source private IP connectivity with a reverse proxy  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/

[ Skip to main content ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/)
  * [Deutsch](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=de)
  * [Español](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=es-419)
  * [Français](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=id)
  * [Italiano](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=it)
  * [Português](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=ja)
  * [한국어](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Set up a reverse proxy](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/#set-up-reverse-proxy)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)


Send feedback 
#  Use source private IP connectivity with a reverse proxy Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Set up a reverse proxy](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/#set-up-reverse-proxy)
  * [What's next](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy/#whats_next)


This page explains how to set up a reverse proxy on a Compute Engine Virtual Machine (VM) to facilitate source private connectivity for heterogeneous Oracle migrations.
A reverse proxy VM is required when you want to use [ private IP connectivity](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source) with a source that resides in a different Virtual Private Cloud network than the one where you create a private connectivity configuration for VPC peering.
## Set up a reverse proxy
To create a Compute Engine VM to host the proxy, follow these steps:
  1. [ Create a Linux VM instance in Compute Engine](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance). 
  2. After you connect to the machine, create the necessary `iptables` routing to forward the traffic. You can use the following script. 
Before using any of the command data below, make the following replacements:
     * SOURCE_PRIVATE_IP with the private IP address of your source instance. 
     * PORT with the port number where your source Oracle instance is listening for connections. 

```
#! /bin/bash

export DB_ADDR=SOURCE_PRIVATE_IP
export DB_PORT=PORT

# Enable the VM to receive packets whose destinations do
# not match any running process local to the VM
echo 1 > /proc/sys/net/ipv4/ip_forward

# Ask the Metadata server for the IP address of the VM nic0
# network interface:
md_url_prefix="http://169.254.169.254/computeMetadata/v1/instance"
vm_nic_ip="$(curl -H "Metadata-Flavor: Google" ${md_url_prefix}/network-interfaces/0/ip)"

# Clear any existing iptables NAT table entries (all chains):
iptables -t nat -F

# Create a NAT table entry in the prerouting chain, matching
# any packets with destination database port, changing the destination
# IP address of the packet to your source instance IP address:
iptables -t nat -A PREROUTING \
     -p tcp --dport $DB_PORT \
     -j DNAT \
     --to-destination $DB_ADDR

# Create a NAT table entry in the postrouting chain, matching
# any packets with destination database port, changing the source IP
# address of the packet to the NAT VM's primary internal IPv4 address:
iptables -t nat -A POSTROUTING \
     -p tcp --dport $DB_PORT \
     -j SNAT \
     --to-source $vm_nic_ip

# Save iptables configuration:
iptables-save
```

Your proxy VM is now running. Continue with the rest of the steps required for your source connectivity. 


## What's next
  * Learn more about source connectivity methods. See [ Source connectivity methods overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source).
  * To get a complete, step-by-step migration walkthrough, see [ Oracle to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/guide).


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
