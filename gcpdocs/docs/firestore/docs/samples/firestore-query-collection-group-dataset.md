---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/
title: Create a collection of Firestore documents \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:17:07.969644+00:00
---

# Create a collection of Firestore documents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/

[ Skip to main content ](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/)
  * [Deutsch](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffirestore%2Fdocs%2Fsamples%2Ffirestore-query-collection-group-dataset%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/docs)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)


Was this helpful?
#  Create a collection of Firestore documents Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#explore-further)
  * [Code sample](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#code-sample)
  * [What's next](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#whats-next)


Create a collection of Firestore documents
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)


## Code sample
[C#](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#c)[Go](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#go)[Java](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#java)[Node.js](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#node.js)[PHP](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#php)[Python](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#python)[Ruby](https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset/#ruby) More
To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
CollectionReference citiesRef = db.Collection("cities");
await citiesRef.Document("SF").Collection("landmarks").Document()
    .SetAsync(new { Name = "Golden Gate Bridge", Type = "bridge" });
await citiesRef.Document("SF").Collection("landmarks").Document()
    .SetAsync(new { Name = "Legion of Honor", Type = "museum" });
await citiesRef.Document("LA").Collection("landmarks").Document()
    .SetAsync(new { Name = "Griffith Park", Type = "park" });
await citiesRef.Document("DC").Collection("landmarks").Document()
    .SetAsync(new { Name = "Lincoln Memorial", Type = "memorial" });
await citiesRef.Document("DC").Collection("landmarks").Document()
    .SetAsync(new { Name = "National Air And Space Museum", Type = "museum" });
await citiesRef.Document("TOK").Collection("landmarks").Document()
    .SetAsync(new { Name = "Ueno Park", Type = "park" });
await citiesRef.Document("TOK").Collection("landmarks").Document()
    .SetAsync(new { Name = "National Museum of Nature and Science", Type = "museum" });
await citiesRef.Document("BJ").Collection("landmarks").Document()
    .SetAsync(new { Name = "Jingshan Park", Type = "park" });
await citiesRef.Document("BJ").Collection("landmarks").Document()
    .SetAsync(new { Name = "Beijing Ancient Observatory", Type = "museum" });
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import (
	"context"
	"fmt"

	"cloud.google.com/go/firestore"
)

// collectionGroupSetup sets up a collection group to query.
func collectionGroupSetup(projectID, cityCollection string) error {
	ctx := context.Background()

	client, err := firestore.NewClient(ctx, projectID)
	if err != nil {
		return fmt.Errorf("firestore.NewClient: %w", err)
	}
	defer client.Close()

	landmarks := []struct {
		city, name, t string
	}{
		{"SF", "Golden Gate Bridge", "bridge"},
		{"SF", "Legion of Honor", "museum"},
		{"LA", "Griffith Park", "park"},
		{"LA", "The Getty", "museum"},
		{"DC", "Lincoln Memorial", "memorial"},
		{"DC", "National Air and Space Museum", "museum"},
		{"TOK", "Ueno Park", "park"},
		{"TOK", "National Museum of Nature and Science", "museum"},
		{"BJ", "Jingshan Park", "park"},
		{"BJ", "Beijing Ancient Observatory", "museum"},
	}

	cities := client.Collection(cityCollection)
	for _, l := range landmarks {
		if _, err := cities.Doc(l.city).Collection("landmarks").[NewDoc](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/firestore/latest/index.html#cloud_google_com_go_firestore_CollectionRef_NewDoc)().Set(ctx, map[string]string{
			"name": l.name,
			"type": l.t,
		}); err != nil {
			return fmt.Errorf("Set: %w", err)
		}
	}

	return nil
}

```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
CollectionReference cities = db.collection("cities");

final List<ApiFuture<WriteResult>> futures =
    Arrays.asList(
        cities
            .document("SF")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Golden Gate Bridge");
                    put("type", "bridge");
                  }
                }),
        cities
            .document("SF")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Legion of Honor");
                    put("type", "museum");
                  }
                }),
        cities
            .document("LA")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Griffith Park");
                    put("type", "park");
                  }
                }),
        cities
            .document("LA")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "The Getty");
                    put("type", "museum");
                  }
                }),
        cities
            .document("DC")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Lincoln Memorial");
                    put("type", "memorial");
                  }
                }),
        cities
            .document("DC")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "National Air and Space Museum");
                    put("type", "museum");
                  }
                }),
        cities
            .document("TOK")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Ueno Park");
                    put("type", "park");
                  }
                }),
        cities
            .document("TOK")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "National Museum of Nature and Science");
                    put("type", "museum");
                  }
                }),
        cities
            .document("BJ")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Jingshan Park");
                    put("type", "park");
                  }
                }),
        cities
            .document("BJ")
            .collection("landmarks")
            .document()
            .set(
                new HashMap<String, String>() {
                  {
                    put("name", "Beijing Ancient Observatory");
                    put("type", "museum");
                  }
                }));
final List<WriteResult> landmarks = ApiFutures.allAsList(futures).get();
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
const citiesRef = db.collection('cities');

await citiesRef.doc('SF').collection('landmarks').doc().set({
  name: 'Golden Gate Bridge',
  type: 'bridge'
});
await citiesRef.doc('SF').collection('landmarks').doc().set({
  name: 'Legion of Honor',
  type: 'museum'
});
await citiesRef.doc('LA').collection('landmarks').doc().set({
  name: 'Griffith Park',
  type: 'park'
});
await citiesRef.doc('LA').collection('landmarks').doc().set({
  name: 'The Getty',
  type: 'museum'
});
await citiesRef.doc('DC').collection('landmarks').doc().set({
  name: 'Lincoln Memorial',
  type: 'memorial'
});
await citiesRef.doc('DC').collection('landmarks').doc().set({
  name: 'National Air and Space Museum',
  type: 'museum'
});
await citiesRef.doc('TOK').collection('landmarks').doc().set({
  name: 'Ueno Park',
  type: 'park'
});
await citiesRef.doc('TOK').collection('landmarks').doc().set({
  name: 'National Museum of Nature and Science',
  type: 'museum'
});
await citiesRef.doc('BJ').collection('landmarks').doc().set({
  name: 'Jingshan Park',
  type: 'park'
});
await citiesRef.doc('BJ').collection('landmarks').doc().set({ 
  name: 'Beijing Ancient Observatory',
  type: 'museum'
});
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
$citiesRef = $db->collection('samples/php/cities');
$citiesRef->document('SF')->collection('landmarks')->newDocument()->set([
    'name' => 'Golden Gate Bridge',
    'type' => 'bridge'
]);
$citiesRef->document('SF')->collection('landmarks')->newDocument()->set([
    'name' => 'Legion of Honor',
    'type' => 'museum'
]);
$citiesRef->document('LA')->collection('landmarks')->newDocument()->set([
    'name' => 'Griffith Park',
    'type' => 'park'
]);
$citiesRef->document('LA')->collection('landmarks')->newDocument()->set([
    'name' => 'The Getty',
    'type' => 'museum'
]);
$citiesRef->document('DC')->collection('landmarks')->newDocument()->set([
    'name' => 'Lincoln Memorial',
    'type' => 'memorial'
]);
$citiesRef->document('DC')->collection('landmarks')->newDocument()->set([
    'name' => 'National Air and Space Museum',
    'type' => 'museum'
]);
$citiesRef->document('TOK')->collection('landmarks')->newDocument()->set([
    'name' => 'Ueno Park',
    'type' => 'park'
]);
$citiesRef->document('TOK')->collection('landmarks')->newDocument()->set([
    'name' => 'National Museum of Nature and Science',
    'type' => 'museum'
]);
$citiesRef->document('BJ')->collection('landmarks')->newDocument()->set([
    'name' => 'Jingshan Park',
    'type' => 'park'
]);
$citiesRef->document('BJ')->collection('landmarks')->newDocument()->set([
    'name' => 'Beijing Ancient Observatory',
    'type' => 'museum'
]);
print('Added example landmarks collections to the cities collection.' . PHP_EOL);
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
cities = db.collection("cities")

sf_landmarks = cities.document("SF").collection("landmarks")
sf_landmarks.document().set({"name": "Golden Gate Bridge", "type": "bridge"})
sf_landmarks.document().set({"name": "Legion of Honor", "type": "museum"})
la_landmarks = cities.document("LA").collection("landmarks")
la_landmarks.document().set({"name": "Griffith Park", "type": "park"})
la_landmarks.document().set({"name": "The Getty", "type": "museum"})
dc_landmarks = cities.document("DC").collection("landmarks")
dc_landmarks.document().set({"name": "Lincoln Memorial", "type": "memorial"})
dc_landmarks.document().set(
    {"name": "National Air and Space Museum", "type": "museum"}
)
tok_landmarks = cities.document("TOK").collection("landmarks")
tok_landmarks.document().set({"name": "Ueno Park", "type": "park"})
tok_landmarks.document().set(
    {"name": "National Museum of Nature and Science", "type": "museum"}
)
bj_landmarks = cities.document("BJ").collection("landmarks")
bj_landmarks.document().set({"name": "Jingshan Park", "type": "park"})
bj_landmarks.document().set(
    {"name": "Beijing Ancient Observatory", "type": "museum"}
)
```

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
cities_ref = firestore.col collection_path

sf_landmarks = cities_ref.document("SF").collection("landmarks")
sf_landmarks.document.set(
  {
    name: "Golden Gate Bridge",
    type: "bridge"
  }
)
sf_landmarks.document.set(
  {
    name: "Legion of Honor",
    type: "museum"
  }
)

la_landmarks = cities_ref.document("LA").collection("landmarks")
la_landmarks.document.set(
  {
    name: "Griffith Park",
    type: "park"
  }
)
la_landmarks.document.set(
  {
    name: "The Getty",
    type: "museum"
  }
)

dc_landmarks = cities_ref.document("DC").collection("landmarks")
dc_landmarks.document.set(
  {
    name: "Lincoln Memorial",
    type: "memorial"
  }
)
dc_landmarks.document.set(
  {
    name: "National Air and Space Museum",
    type: "museum"
  }
)

tok_landmarks = cities_ref.document("TOK").collection("landmarks")
tok_landmarks.document.set(
  {
    name: "Ueno Park",
    type: "park"
  }
)
tok_landmarks.document.set(
  {
    name: "National Museum of Nature and Science",
    type: "museum"
  }
)

bj_landmarks = cities_ref.document("BJ").collection("landmarks")
bj_landmarks.document.set(
  {
    name: "Jingshan Park",
    type: "park"
  }
)
bj_landmarks.document.set(
  {
    name: "Beijing Ancient Observatory",
    type: "museum"
  }
)
```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
