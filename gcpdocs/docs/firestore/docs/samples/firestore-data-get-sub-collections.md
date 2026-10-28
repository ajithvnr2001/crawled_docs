---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-get-sub-collections/
title: Get Firestore documents in nested collections \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:31:48.795155+00:00
---

# Get Firestore documents in nested collections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-get-sub-collections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Get Firestore documents in nested collections Stay organized with collections  Save and categorize content based on your preferences. 

Get Firestore documents in nested collections

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    DocumentReference cityRef = db.Collection("cities").Document("SF");
    IAsyncEnumerable<CollectionReference> subcollections = cityRef.ListCollectionsAsync();
    IAsyncEnumerator<CollectionReference> subcollectionsEnumerator = subcollections.GetAsyncEnumerator(default);
    while (await subcollectionsEnumerator.MoveNextAsync())
    {
        CollectionReference subcollectionRef = subcollectionsEnumerator.Current;
        Console.WriteLine("Found subcollection with ID: {0}", subcollectionRef.Id);
    }

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/firestore"
    	"google.golang.org/api/iterator"
    )
    
    func getCollections(ctx context.Context, client *firestore.Client) error {
    	iter := client.Collection("cities").Doc("SF").Collections(ctx)
    	for {
    		collRef, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Printf("Found collection with id: %s\n", collRef.ID)
    	}
    	return nil
    }
    

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Iterable<CollectionReference> collections =
        db.collection("cities").document("SF").listCollections();
    
    for (CollectionReference collRef : collections) {
      System.out.println("Found subcollection with id: " + collRef.getId());
    }

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const sfRef = db.collection('cities').doc('SF');
    const collections = await sfRef.listCollections();
    collections.forEach(collection => {
      console.log('Found subcollection with id:', collection.id);
    });

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $cityRef = $db->collection('samples/php/cities')->document('SF');
    $collections = $cityRef->collections();
    foreach ($collections as $collection) {
        printf('Found subcollection with id: %s' . PHP_EOL, $collection->id());
    }

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = db.collection("cities").document("SF")
    collections = city_ref.collections()
    for collection in collections:
        for doc in collection.stream():
            print(f"{doc.id} => {doc.to_dict()}")

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    city_ref = firestore.doc "#{collection_path}/SF"
    city_ref.cols do |col|
      puts col.collection_id
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
