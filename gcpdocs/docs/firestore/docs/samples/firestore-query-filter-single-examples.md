---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-single-examples/
title: Querying Firestore collections with one range \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:28:17.716715+00:00
---

# Querying Firestore collections with one range  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-single-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Querying Firestore collections with one range Stay organized with collections  Save and categorize content based on your preferences. 

Querying Firestore collections with one range

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query stateQuery = citiesRef.WhereEqualTo("State", "CA");
    Query populationQuery = citiesRef.WhereGreaterThan("Population", 1000000);
    Query nameQuery = citiesRef.WhereGreaterThanOrEqualTo("Name", "San Francisco");

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    countryQuery := cities.Where("state", "==", "CA")
    popQuery := cities.Where("population", "<", 1000000)
    cityQuery := cities.Where("name", ">=", "San Francisco")

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Query stateQuery = cities.whereEqualTo("state", "CA");
    Query populationQuery = cities.whereLessThan("population", 1000000L);
    Query nameQuery = cities.whereGreaterThanOrEqualTo("name", "San Francisco");

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const stateQueryRes = await citiesRef.where('state', '==', 'CA').get();
    const populationQueryRes = await citiesRef.where('population', '<', 1000000).get();
    const nameQueryRes = await citiesRef.where('name', '>=', 'San Francisco').get();

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $stateQuery = $citiesRef->where('state', '=', 'CA');
    $populationQuery = $citiesRef->where('population', '>', 1000000);
    $nameQuery = $citiesRef->where('name', '>=', 'San Francisco');

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = db.collection("cities")
    
    cities_ref.where(filter=FieldFilter("state", "==", "CA"))
    cities_ref.where(filter=FieldFilter("population", "<", 1000000))
    cities_ref.where(filter=FieldFilter("name", ">=", "San Francisco"))

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    state_query      = cities_ref.where "state", "=", "CA"
    population_query = cities_ref.where "population", ">", 1_000_000
    name_query       = cities_ref.where "name", ">=", "San Francisco"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
