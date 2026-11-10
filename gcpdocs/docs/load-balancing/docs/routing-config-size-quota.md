---
url: https://docs.cloud.google.com/load-balancing/docs/routing-config-size-quota/
title: Routing configuration size and quota units \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:51:54.619654+00:00
---

# Routing configuration size and quota units  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/routing-config-size-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Routing configuration size and quota units Stay organized with collections  Save and categorize content based on your preferences. 

The load balancer configuration size quotas measure the size of all routing configurations (URL maps for Application Load Balancers or TLS routes for Proxy Network Load Balancers) in a project, VPC network, or region of a VPC network, depending on the type of load balancer. Individual URL maps are limited to 1 MB of data each, with the exception of the classic Application Load Balancer, which retains its 64 KB limit. Quota units represent the complexity of your routing configuration. A routing configuration with few rules or short matchers consumes fewer quota units, while a highly complex configuration with many rules, hostnames, or path matchers consumes more.

## How the quota works

Only the routing configurations (URL maps or TLS routes) that are part of a complete Application Load Balancer or proxy Network Load Balancer configuration contribute to the usage of a load balancer configuration size quota. To be part of a complete configuration, a URL map or TLS route must be referenced by a target proxy (such as a target HTTP, HTTPS, or TCP proxy), and the target proxy must be referenced by a forwarding rule. Google Cloud calculates the total quota usage for routing configurations that are part of a complete configuration using the following formula:

_Quota usage = sum of single routing configuration quota units_ ×  _number of forwarding rules referencing the same configuration through a target proxy_

If a relationship between a forwarding rule, through a target proxy, to the routing configuration doesn't exist, the configuration doesn't contribute to the usage of a load balancer configuration size quota.

## Manage quota usage

The usage of each configuration size quota changes as you modify Application Load Balancers or Proxy Network Load Balancers:

  * **Updating a URL map or TLS route** : Modifying an existing URL map or TLS route (such as adding or removing host rules, path matchers, route rules, or SNI host matches) changes the number of quota units that the configuration uses. The number of quota units is multiplied by the number of forwarding rules that reference the configuration through target proxies.
  * **Updating a target proxy** : If you update a target proxy to reference a different URL map or TLS route, and no other target proxy references the previous configuration, the quota units used by the previous configuration no longer contribute to the usage of a configuration size quota.
  * **Creating or deleting a forwarding rule** : Creating a new forwarding rule associated with a target proxy that uses a URL map or TLS route increases the number of quota units that the configuration contributes to a configuration size quota. Conversely, deleting a forwarding rule reduces the number of quota units that the configuration contributes to a configuration size quota.



## Check quota usage

To determine the number of quota units an existing URL map uses, use the [`gcloud compute url-maps describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/describe):
    
    
    gcloud compute url-maps describe URL_MAP_NAME \
       [--region=REGION_NAME | --global] \
       --format="value(status)"
    

Replace the following:

  * `URL_MAP_NAME`: the name of your URL map.
  * `REGION_NAME`: the region where you defined the load balancer.



The output includes a read-only `status.quotaUsage` object showing the total number of units calculated for the URL map, as well as the number of forwarding rules using it.

For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#config-size-limits).

## What's next

  * [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
