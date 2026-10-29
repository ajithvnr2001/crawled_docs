---
url: https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count/
title: Scale the number of replicas \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:56:40.748609+00:00
---

# Scale the number of replicas  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/scale-replica-count/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Scale the number of replicas Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to scale the number of replicas for an instance.

## Update the number of replicas

You can scale an instance by updating its number of replicas.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the ID of the instance that you want to scale.

  3. Scroll to the **Configurations** section.

  4. Next to the **Replicas per shard** field, click **Edit replica count** (_edit_).

  5. From the **Replicas** menu, select the number of replicas that you want for the instance. You can select 0-5 replicas per shard.

  6. Click **Update instance**.




### gcloud

To update the number of replicas, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command:
    
    
    gcloud memorystore instances update INSTANCE_ID \
      --location=REGION_ID \
      --replica-count=REPLICA_COUNT
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance.
  * REGION_ID: the region where the instance is located.
  * REPLICA_COUNT: the number of replicas (per shard) that you want for the instance. Acceptable values are `0`-`5`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
