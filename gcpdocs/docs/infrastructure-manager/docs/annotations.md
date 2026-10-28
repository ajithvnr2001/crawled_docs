---
url: https://docs.cloud.google.com/infrastructure-manager/docs/annotations/
title: Annotations and labels \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:30:02.630086+00:00
---

# Annotations and labels  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Annotations and labels Stay organized with collections  Save and categorize content based on your preferences. 

Infrastructure Manager lets you attach optional metadata to deployments using annotations and labels. These key-value pairs help you organize, track, and filter your deployments across Google Cloud.

## What are annotations and labels?

_Annotations_ are key-value pairs of free-form text. You can use them to attach arbitrary information associated with the resource. 

You can use _labels_ to organize resources. For example, you can apply logic based on label selection.

Annotations are used for storing non-identifying information typically used by client tools to store arbitrary data attached to a resource, while labels are typically used to organize resources.

For more information about using annotations with Google Cloud, see [annotations AIP](https://google.aip.dev/148#annotations) documentation. To learn more about using labels, see the [labels overview](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels) documentation.

## Annotation and label constraints

As with annotations, labels are key-value pairs that must conform to the following limitations:

  * Keys and values both must be 128 bytes or less.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * Keys must start with a lowercase letter or international character.
  * All characters must use UTF-8 encoding. International characters are allowed. For example:
        
        --annotation="appVersion=v.1.2.3,environment=production"
        




## Use annotations and labels with Infra Manager

The use of annotations and labels can be applied in a variety of ways across your Google Cloud infrastructure.

When you create or update deployments with Infra Manager, you can use annotations and labels to monitor deployments or query sets of information. For more information, see [deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources), [update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment), or [preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

## What's next

Use Infra Manager to standardize, reuse, and scale your infrastructure with Google Cloud:

  * [Deploy a VPC using Terraform](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-vpc-with-terraform)
  * [Deploy infrastructure using Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
