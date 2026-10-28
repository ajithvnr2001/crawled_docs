---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/
title: Query a Firestore collection with an array_contains_any filter \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:17:12.903754+00:00
---

# Query a Firestore collection with an array_contains_any filter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/

[ Skip to main content ](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/)
  * [Deutsch](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffirestore%2Fdocs%2Fsamples%2Ffirestore-query-filter-array-contains-any%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/docs)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)


Was this helpful?
#  Query a Firestore collection with an array_contains_any filter Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#whats-next)


Query a Firestore collection with an array_contains_any filter
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)


## Code sample
[C#](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#c)[Go](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#go)[Java](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#java)[Node.js](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#node.js)[PHP](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#php)[Python](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#python)[Ruby](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/#ruby) More
To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
CollectionReference citiesRef = db.Collection("cities");
Query query = citiesRef.WhereArrayContainsAny("Regions", new[] { "west_coast", "east_coast" });
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
cities := client.Collection("cities")
query := cities.Where("regions", "array-contains-any", []string{"west_coast", "east_coast"}).Documents(ctx)
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
CollectionReference citiesRef = db.collection("cities");

Query query =
    citiesRef.whereArrayContainsAny("regions", Arrays.asList("west_coast", "east_coast"));
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
const coastalCities = await citiesRef.where('regions', 'array-contains-any',
    ['west_coast', 'east_coast']).get();
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
$containsQuery = $citiesRef->where('regions', 'array-contains-any', ['west_coast', 'east_coast']);
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
cities_ref = db.collection("cities")

query = cities_ref.where(
    filter=FieldFilter(
        "regions", "array_contains_any", ["west_coast", "east_coast"]
    )
)
return query
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
cities_ref = firestore.col collection_path
costal_cities = cities_ref.where "regions", "array-contains-any", ["west_coast", "east_coast"]
```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
