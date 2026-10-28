---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/
title: Vector Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:18:41.937941+00:00
---

# Vector Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/

[ Skip to main content ](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/)
  * [Deutsch](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Vector Functions](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#vector_functions)
    * [COSINE_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#cosine_distance)
    * [DOT_PRODUCT](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#dot_product)
    * [EUCLIDEAN_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#euclidean_distance)
    * [MANHATTAN_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#manhattan_distance)
    * [VECTOR_LENGTH](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#vector_length)
  * [What's next](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)


Send feedback 
  * On this page
  * [Vector Functions](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#vector_functions)
    * [COSINE_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#cosine_distance)
    * [DOT_PRODUCT](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#dot_product)
    * [EUCLIDEAN_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#euclidean_distance)
    * [MANHATTAN_DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#manhattan_distance)
    * [VECTOR_LENGTH](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#vector_length)
  * [What's next](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#whats_next)


# Vector Functions Reference Stay organized with collections  Save and categorize content based on your preferences.
## **Vector Functions**  
| Name   | Description   |  
| --- | --- |  
|  `COSINE_[DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#cosine_distance)`  | Returns the cosine distance between two vectors   |  
|  `DOT_[PRODUCT](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#dot_product)`  | Returns the dot product between two vectors   |  
|  `EUCLIDEAN_[DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#euclidean_distance)`  | Returns the euclidean distance between two vectors   |  
|  `MANHATTAN_[DISTANCE](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#manhattan_distance)`  | Returns the manhattan distance between two vectors   |  
|  `VECTOR_[LENGTH](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#vector_length)`  | Returns the number of elements in a vector   |  
### COSINE_DISTANCE
**Syntax:**

```
cosine_distance(x: VECTOR, y: VECTOR) -> FLOAT64

```

**Description:**
Returns the cosine distance between `x` and `y`.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#node.js)[Web](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#web-modular-api)[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#go) More

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").cosineDistance(sampleVector).as("cosineDistance")
  )
  .execute();
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2082-L2088)

```

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").cosineDistance(sampleVector).as("cosineDistance")));
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3356-L3360)

```

```
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").cosineDistance(sampleVector).as("cosineDistance")
  ])
  .execute()
[PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1329-L1335)

```

```
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
    )
    .execute()
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2691-L2697)

```

```
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
    )
    .execute();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2936-L2942)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("embedding").cosine_distance(sample_vector).as_("cosineDistance")
    )
    .execute()
)
[firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1700-L1711)

```

```
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(cosineDistance(field("embedding"), sampleVector).as("cosineDistance"))
        .execute()
        .get();
[PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1631-L1638)

```

```
sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
snapshot := client.Pipeline().
	Collection("books").
	Select(firestore.Fields(
		firestore.CosineDistance(firestore.FieldOf("embedding"), sampleVector).As("cosineDistance"),
	)).
	Execute(ctx)
[pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_vector.go#L28-L34)

```

### DOT_PRODUCT
**Syntax:**

```
dot_product(x: VECTOR, y: VECTOR) -> FLOAT64

```

**Description:**
Returns the dot product of `x` and `y`.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#node.js)[Web](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#web-modular-api)[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#go) More

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").dotProduct(sampleVector).as("dotProduct")
  )
  .execute();
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2095-L2101)

```

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").dotProduct(sampleVector).as("dotProduct")
  )
);
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3367-L3373)

```

```
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").dotProduct(sampleVector).as("dotProduct")
  ])
  .execute()
[PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1343-L1349)

```

```
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").dotProduct(sampleVector).alias("dotProduct")
    )
    .execute()
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2705-L2711)

```

```
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").dotProduct(sampleVector).alias("dotProduct")
    )
    .execute();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2950-L2956)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("embedding").dot_product(sample_vector).as_("dotProduct"))
    .execute()
)
[firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1719-L1728)

```

```
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(dotProduct(field("embedding"), sampleVector).as("dotProduct"))
        .execute()
        .get();
[PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1645-L1652)

```

```
sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
snapshot := client.Pipeline().
	Collection("books").
	Select(firestore.Fields(
		firestore.DotProduct(firestore.FieldOf("embedding"), sampleVector).As("dotProduct"),
	)).
	Execute(ctx)
[pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_vector.go#L48-L54)

```

### EUCLIDEAN_DISTANCE
**Syntax:**

```
euclidean_distance(x: VECTOR, y: VECTOR) -> FLOAT64

```

**Description:**
Computes the euclidean distance between `x` and `y`.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#node.js)[Web](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#web-modular-api)[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#go) More

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  )
  .execute();
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2108-L2114)

```

```
const sampleVector = [0.0, 1, 2, 3, 4, 5];
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  )
);
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3380-L3386)

```

```
let sampleVector = [0.0, 1, 2, 3, 4, 5]
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
  ])
  .execute()
[PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1357-L1363)

```

```
val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
    )
    .execute()
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2719-L2725)

```

```
double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
    )
    .execute();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2964-L2970)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field
from google.cloud.firestore_v1.vector import Vector

sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
result = (
    client.pipeline()
    .collection("books")
    .select(
        Field.of("embedding")
        .euclidean_distance(sample_vector)
        .as_("euclideanDistance")
    )
    .execute()
)
[firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1736-L1749)

```

```
double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(euclideanDistance(field("embedding"), sampleVector).as("euclideanDistance"))
        .execute()
        .get();
[PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1659-L1666)

```

```
sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
snapshot := client.Pipeline().
	Collection("books").
	Select(firestore.Fields(
		firestore.EuclideanDistance(firestore.FieldOf("embedding"), sampleVector).As("euclideanDistance"),
	)).
	Execute(ctx)
[pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_vector.go#L68-L74)

```

### MANHATTAN_DISTANCE
**Syntax:**

```
manhattan_distance(x: VECTOR, y: VECTOR) -> FLOAT64

```

**Description:**
Computes the manhattan distance between `x` and `y`.
### VECTOR_LENGTH
**Syntax:**

```
vector_length(vector: VECTOR) -> INT64

```

**Description:**
Returns the number of elements in a `VECTOR`.
[Node.js](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#node.js)[Web](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#web-modular-api)[Swift](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#swift)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java-android)[Python](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#python)[Java](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#java)[Go](https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/#go) More

```
const result = await db.pipeline()
  .collection("books")
  .select(
    field("embedding").vectorLength().as("vectorLength")
  )
  .execute();
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2121-L2126)

```

```
const result = await execute(db.pipeline()
  .collection("books")
  .select(
    field("embedding").vectorLength().as("vectorLength")
  )
);
[test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3393-L3398)

```

```
let result = try await db.pipeline()
  .collection("books")
  .select([
    Field("embedding").vectorLength().as("vectorLength")
  ])
  .execute()
[PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1371-L1376)

```

```
val result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").vectorLength().alias("vectorLength")
    )
    .execute()
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2733-L2738)

```

```
Task<Pipeline.Snapshot> result = db.pipeline()
    .collection("books")
    .select(
        field("embedding").vectorLength().alias("vectorLength")
    )
    .execute();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2978-L2983)

```

```
from google.cloud.firestore_v1.pipeline_expressions import Field

result = (
    client.pipeline()
    .collection("books")
    .select(Field.of("embedding").vector_length().as_("vectorLength"))
    .execute()
)
[firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1757-L1764)

```

```
Pipeline.Snapshot result =
    firestore
        .pipeline()
        .collection("books")
        .select(vectorLength(field("embedding")).as("vectorLength"))
        .execute()
        .get();
[PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1673-L1679)

```

```
snapshot := client.Pipeline().
	Collection("books").
	Select(firestore.Fields(
		firestore.VectorLength(firestore.FieldOf("embedding")).As("vectorLength"),
	)).
	Execute(ctx)
[pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/18bb064d1db6c801e23874ca8029e465722ce6f0/firestore/pipeline_snippets_vector.go#L88-L93)

```

## What's next
  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
