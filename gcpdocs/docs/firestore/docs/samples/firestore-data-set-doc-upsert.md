---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/
title: Update a Firestore document using merge \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:56:38.257868+00:00
---

# Update a Firestore document using merge  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/

[ Skip to main content ](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/)
  * [Deutsch](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/docs)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)


#  Update a Firestore document using merge Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#whats-next)


Update a Firestore document using merge
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Add and update data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)


## Code sample
[C#](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#c)[Go](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#go)[Java](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#java)[Node.js](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#node.js)[PHP](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#php)[Python](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#python)[Ruby](https://docs.cloud.google.com/firestore/docs/samples/firestore-data-set-doc-upsert/#ruby) More
To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
DocumentReference docRef = db.Collection("cities").Document("LA");
Dictionary<string, object> update = new Dictionary<string, object>
{
    { "capital", false }
};
await docRef.SetAsync(update, SetOptions.MergeAll);
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```

import (
	"context"
	"log"

	"cloud.google.com/go/firestore"
)

func updateDocCreateIfMissing(ctx context.Context, client *firestore.Client) error {
	_, err := client.Collection("cities").Doc("BJ").Set(ctx, map[string]interface{}{
		"capital": true,
	}, firestore.[MergeAll](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_MergeAll))

	if err != nil {
		// Handle any errors in an appropriate way, such as returning them.
		log.Printf("An error has occurred: %s", err)
	}

	return err
}

```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
// asynchronously update doc, create the document if missing
Map<String, Object> update = new HashMap<>();
update.put("capital", true);

ApiFuture<WriteResult> writeResult =
    db.collection("cities").document("BJ").set(update, SetOptions.merge());
// ...
System.out.println("Update time : " + writeResult.get().getUpdateTime());
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
const cityRef = db.collection('cities').doc('BJ');

const res = await cityRef.set({
  capital: true
}, { merge: true });
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
$cityRef = $db->collection('samples/php/cities')->document('BJ');
$cityRef->set([
    'capital' => true
], ['merge' => true]);
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
city_ref = db.collection("cities").document("BJ")

city_ref.set({"capital": True}, merge=True)
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
city_ref = firestore.doc "#{collection_path}/LA"
city_ref.set({ capital: false }, merge: true)
```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
