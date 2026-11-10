---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields/
title: Add Fields (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T06:06:12.624422+00:00
---

# Add Fields (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add Fields (Transformation Stage)

## Description

Add new fields to the documents produced by the previous stage.

The generated documents will contain all the fields from the previous stage along with all newly added fields, overwriting any field that shares the same name from the previous document. The `add_fields(...)` stage allows updating nested fields by specifying a nested field name as the alias.

## Examples

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("soldBooks").add(field("unsoldBooks")).as("totalBooks"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/26874dbbb01f2545ea82fe7bdbfb4adcee87ee4c/firestore-next/test.firestore.js#L2644-L2647)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("soldBooks").add(Field("unsoldBooks")).as("totalBooks")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/26bd4eba55c68017aa0d2e4389227920c1994fbe/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L584-L587)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1890-L1893)

##### Java  
Android
    
    
          Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2136-L2139)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("soldBooks").add(Field.of("unsoldBooks")).as_("totalBooks"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/e7081bb30f3610ad13228056b08bd7a14f309af9/snippets/firestore/firestore_pipelines.py#L683-L690)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(add(field("soldBooks"), field("unsoldBooks")).as("totalBooks"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L667-L673)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Add(firestore.FieldOf("soldBooks"), firestore.FieldOf("unsoldBooks")).As("totalBooks"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/1b7781c77366c3cff42201a77e7f67016c8381b0/firestore/pipeline_snippets_arithmetic.go#L28-L33)

## Behavior

### Overlapping Fields

Assigning an expression an alias that is already in the documents from the previous stage will cause the `add_fields(...)` stage to overwrite the previous field. This can be used to chain up multiple expressions over the same field name, like:

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/users")
      .addFields(field('age').abs().as('age'))
      .addFields(field('age').add(10).as('age'))
      .execute();
    

### Nested Fields

Nested fields (e.g. those with `.` syntax) can be updated as part of this stage. This makes it possible to update a field "in-place" such as in:

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/users")
      .addFields(field('address.city').toLower().as('address.city'))
      .execute();
    

Assigning an expression to a nested field will implicitly create any missing parent fields as well.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
