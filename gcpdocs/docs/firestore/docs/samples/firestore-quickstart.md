---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-quickstart/
title: Getting started with Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:51:49.002137+00:00
---

# Getting started with Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Getting started with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Getting started with Firestore

## Code sample

### Kotlin
    
    
    import com.google.api.gax.rpc.ApiException
    import com.google.api.gax.rpc.NotFoundException
    import com.google.cloud.firestore.FirestoreOptions
    import java.util.concurrent.ExecutionException
    
    /**
     * Retrieves all documents from a Firestore collection and prints their metadata
     * and fields.
     *
     * @param projectId Google Cloud project identifier (for example, "example-project-id").
     * @param collectionId Firestore collection identifier to query (for example, "example-collection").
     */
    fun getCollectionDocuments(projectId: String, collectionId: String) {
      val options =
        FirestoreOptions.getDefaultInstance()
          .toBuilder()
          .setProjectId(projectId)
          .build()
    
      try {
        options.service.use { firestore ->
          val collectionReference = firestore.collection(collectionId)
          println("Retrieving documents from collection '$collectionId'...")
          val querySnapshot = collectionReference.get().get()
    
          println("Resource ID: ${collectionReference.path}")
          println("Document Count: ${querySnapshot.documents.size}")
          println("Read Time: ${querySnapshot.readTime}")
          for (document in querySnapshot.documents) {
            println("Document ID: ${document.id}")
            println("Creation Date: ${document.createTime}")
            println("Data: ${document.data}")
            println("Update Time: ${document.updateTime}")
          }
        }
      } catch (err: ExecutionException) {
        val message =
          when (val cause = err.cause) {
            is NotFoundException ->
              "error: Firestore database not found in project '$projectId': ${cause.message}"
            is ApiException ->
              "error: failed to retrieve collection '$collectionId' in project '$projectId': ${cause.message}"
            else ->
              "error: execution failed while querying collection '$collectionId' in project '$projectId': ${err.message}"
          }
        System.err.println(message)
      } catch (err: InterruptedException) {
        Thread.currentThread().interrupt()
        System.err.println(
          "error: interrupted while querying collection '$collectionId' in project '$projectId': ${err.message}"
        )
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
