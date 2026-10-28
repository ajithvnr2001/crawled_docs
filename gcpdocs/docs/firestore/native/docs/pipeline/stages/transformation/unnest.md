---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/
title: Unnest (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:58:00.615927+00:00
---

# Unnest (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/

[ Skip to main content ](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/)
  * [Deutsch](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffirestore%2Fnative%2Fdocs%2Fpipeline%2Fstages%2Ftransformation%2Funnest%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Description](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#description)
  * [Examples](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#examples)
  * [Behavior](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#behavior)
    * [Alias and Index Field](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#alias_and_index_field)
    * [Non Array Values](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#non_array_values)
    * [Empty Array Values](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#empty_array_values)
    * [Nested Unnest](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#nested_unnest)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)


Was this helpful?
Send feedback 
  * On this page
  * [Description](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#description)
  * [Examples](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#examples)
  * [Behavior](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#behavior)
    * [Alias and Index Field](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#alias_and_index_field)
    * [Non Array Values](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#non_array_values)
    * [Empty Array Values](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#empty_array_values)
    * [Nested Unnest](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#nested_unnest)


# Unnest (Transformation Stage) Stay organized with collections  Save and categorize content based on your preferences.
## Description
Generates a new document for each element in an array.
The new documents contain all the fields from the input along with a different element from the array. The array element is stored to the `alias` given, potentially overwriting any pre-existing value with the same field name.
Optionally, the `index_field` argument can be specified. When present, it includes the element's zero-based index from the source array in the output documents.
This stage behaves similar to `CROSS JOIN UNNEST(...)` in many SQL systems.
## Examples
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();

```

## Behavior
### Alias and Index Field
The `alias` and optional `index_field` will overwrite the original fields if the fields already exist in the input document. If the `index_field` is not provided, the output documents won't contain this field.
For example, for the following collection:
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
await db.collection("users").add({name: "foo", scores: [5, 4], userScore: 0});
await db.collection("users").add({name: "bar", scores: [1, 3], attempt: 5});

```

The `unnest` stage can be used to extract each individual score per user.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();

```

In this case, `userScore` and `attempt` are both overwritten.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}
  {name: "bar", scores: [1, 3], userScore: 1, attempt: 0}
  {name: "bar", scores: [1, 3], userScore: 3, attempt: 1}

```

#### Additional examples
[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#go) More

```
let results = try await db.pipeline()
  .database()
  .unnest(Field("arrayField").as("unnestedArrayField"), indexField: "index")
  .execute()
[PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L433-L436)

```

```
val results = db.pipeline()
    .database()
    .unnest(field("arrayField").alias("unnestedArrayField"), UnnestOptions().withIndexField("index"))
    .execute()
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1771-L1774)

```

```
Task<Pipeline.Snapshot> results = db.pipeline()
    .database()
    .unnest(field("arrayField").alias("unnestedArrayField"), new UnnestOptions().withIndexField("index"))
    .execute();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2017-L2020)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.pipeline_stages import UnnestOptions

results = (
    client.pipeline()
    .database()
    .unnest(
        Field.of("arrayField").as_("unnestedArrayField"),
        options=UnnestOptions(index_field="index"),
    )
    .execute()
)
[firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L520-L531)

```

```
Pipeline.Snapshot results =
    firestore
        .pipeline()
        .database()
        .unnest("arrayField", "unnestedArrayField", new UnnestOptions().withIndexField("index"))
        .execute()
        .get();
[PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L532-L538)

```

```
snapshot := client.Pipeline().
	Database().
	UnnestWithAlias("arrayField", "unnestedArrayField", firestore.WithUnnestIndexField("index")).
	Execute(ctx)
[pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_general.go#L1820-L1823)

```

### Non Array Values
If the input expression evaluates to a non-array value, then this stage will return the input document as is with the `index_field` set to `NULL`, if specified.
For example, for the following collection:
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
await db.collection("users").add({name: "foo", scores: 1});
await db.collection("users").add({name: "bar", scores: null});
await db.collection("users").add({name: "qux", scores: {backupScores: 1}});

```

The `unnest` stage can be used to extract each individual score per user.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();

```

This produces the following documents with `attempt` set to `NULL`.

```
  { name: "foo", scores: 1, attempt: null }
  { name: "bar", scores: null, attempt: null }
  { name: "qux", scores: { backupScores: 1 }, attempt: null }

```

### Empty Array Values
If the input expression evaluates to an empty array, then no document will be returned for that input document.
For example, for the following collection:
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
await db.collection("users").add({name: "foo", scores: [5, 4]});
await db.collection("users").add({name: "bar", scores: []});

```

The `unnest` stage can be used to extract each individual score per user.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("scores").as("userScore"), /* index_field= */ "attempt")
    .execute();

```

This produces the following documents with user `bar` missing from the output.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}

```

In order to return documents with empty arrays as well, you can wrap the unnested value in an array. For example:
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(
      conditional(
        equal(field("scores"), []),
        array([field("scores")]),
        field("scores")
      ).as("userScore"),
    /* index_field= */ "attempt")
    .execute();

```

This will now return document with user `bar`.

```
  {name: "foo", scores: [5, 4], userScore: 5, attempt: 0}
  {name: "foo", scores: [5, 4], userScore: 4, attempt: 1}
  {name: "bar", scores: [], userScore: [], attempt: 0}

```

#### Additional examples
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js)[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#go) More

```
    // Input
    // { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
    // { identifier : 2, neighbors: []                   }
    // { identifier : 3, neighbors: "Bob"                }

    const results = await db.pipeline()
      .database()
      .unnest(Field.of("neighbors"), "unnestedNeighbors", "index")
      .execute();

    // Output
    // { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
    // { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
    // { identifier: 3, neighbors: "Bob", index: null}
    
```

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

let results = try await db.pipeline()
  .database()
  .unnest(Field("neighbors").as("unnestedNeighbors"), indexField: "index")
  .execute()

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}
PipelineSnippets.swift[](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L444-L457)

```

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

val results = db.pipeline()
    .database()
    .unnest(field("neighbors").alias("unnestedNeighbors"), UnnestOptions().withIndexField("index"))
    .execute()

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}
DocSnippets.kt[](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1782-L1795)

```

```
// Input
// { identifier : 1, neighbors: [ "Alice", "Cathy" ] }
// { identifier : 2, neighbors: []                   }
// { identifier : 3, neighbors: "Bob"                }

Task<Pipeline.Snapshot> results = db.pipeline()
    .database()
    .unnest(field("neighbors").alias("unnestedNeighbors"), new UnnestOptions().withIndexField("index"))
    .execute();

// Output
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Alice", index: 0 }
// { identifier: 1, neighbors: [ "Alice", "Cathy" ], unnestedNeighbors: "Cathy", index: 1 }
// { identifier: 3, neighbors: "Bob", index: null}
DocSnippets.java[](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2028-L2041)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.pipeline_stages import UnnestOptions

# Input
# { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
# { "identifier" : 2, "neighbors": []                   }
# { "identifier" : 3, "neighbors": "Bob"                }

results = (
    client.pipeline()
    .database()
    .unnest(
        Field.of("neighbors").as_("unnestedNeighbors"),
        options=UnnestOptions(index_field="index"),
    )
    .execute()
)

# Output
# { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
#   "unnestedNeighbors": "Alice", "index": 0 }
# { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
#   "unnestedNeighbors": "Cathy", "index": 1 }
# { "identifier": 3, "neighbors": "Bob", "index": null}
firestore_pipelines.py[](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L539-L562)

```

```
// Input
// { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
// { "identifier" : 2, "neighbors": []                   }
// { "identifier" : 3, "neighbors": "Bob"                }

Pipeline.Snapshot results =
    firestore
        .pipeline()
        .database()
        .unnest("neighbors", "unnestedNeighbors", new UnnestOptions().withIndexField("index"))
        .execute()
        .get();

// Output
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Alice", "index": 0 }
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Cathy", "index": 1 }
// { "identifier": 3, "neighbors": "Bob", "index": null}
PipelineSnippets.java[](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L545-L563)

```

```
// Input
// { "identifier" : 1, "neighbors": [ "Alice", "Cathy" ] }
// { "identifier" : 2, "neighbors": []                   }
// { "identifier" : 3, "neighbors": "Bob"                }

results, err := client.Pipeline().
	Database().
	UnnestWithAlias("neighbors", "unnestedNeighbors", firestore.WithUnnestIndexField("index")).
	Execute(ctx).Results().GetAll()
if err != nil {
	fmt.Fprintf(w, "GetAll failed: %v", err)
	return err
}

// Output
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Alice", "index": 0 }
// { "identifier": 1, "neighbors": [ "Alice", "Cathy" ],
//   "unnestedNeighbors": "Cathy", "index": 1 }
// { "identifier": 3, "neighbors": "Bob", "index": nil}
pipeline_snippets_general.go[](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_general.go#L1837-L1856)

```

### Nested Unnest
In the case the expression evaluates to a nested array, multiple `unnest(...)` stages must be used to flatten each nested level.
For example, for the following collection:
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
await db.collection("users").add({name: "foo", record: [{scores: [5, 4], avg: 4.5}, {scores: [1, 3], old_avg: 2}]});

```

The `unnest(...)` stage can be used sequentially to extract the innermost array.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/unnest/#node.js) More

```
const userScore = await db.pipeline()
    .collection("/users")
    .unnest(field("record").as("record"))
    .unnest(field("record.scores").as("userScore"), /* index_field= */ "attempt")
    .execute();

```

This produces the following documents:

```
  { name: "foo", record: [{ scores: [5, 4], avg: 4.5 }], userScore: 5, attempt: 0 }
  { name: "foo", record: [{ scores: [5, 4], avg: 4.5 }], userScore: 4, attempt: 1 }
  { name: "foo", record: [{ scores: [1, 3], avg: 2 }], userScore: 1, attempt: 0 }
  { name: "foo", record: [{ scores: [1, 3], avg: 2 }], userScore: 3, attempt: 1 }

```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
