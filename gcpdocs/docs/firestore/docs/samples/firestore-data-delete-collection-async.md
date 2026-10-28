---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/
title: Delete a Firestore collection (async) \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T15:19:29.730012+00:00
---

# Delete a Firestore collection (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/

[ Skip to main content ](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/)
  * [Deutsch](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/docs)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)


#  Delete a Firestore collection (async) Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#whats-next)


Delete a Firestore collection and documents within (async).
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Delete documents and fields](https://docs.cloud.google.com/firestore/native/docs/manage-data/delete-data)


## Code sample
[Python](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-delete-collection-async/#python) More
To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
async def delete_collection(coll_ref):

    await db.recursive_delete(coll_ref)

```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
