---
url: https://developer.android.com/topic/libraries/architecture/paging/v3-overview/
title: Paging library overview \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:08.009663+00:00
---

# Paging library overview  |  App architecture  |  Android Developers

> Source: https://developer.android.com/topic/libraries/architecture/paging/v3-overview/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



Stay organized with collections  Save and categorize content based on your preferences. 

# Paging library overview Part of [Android Jetpack](https://developer.android.com/jetpack).

The Paging library helps you load and display pages of data from a larger dataset from local storage or over a network. This approach lets your app use both network bandwidth and system resources more efficiently. The components of the Paging library are designed to fit into the recommended [Android app architecture](https://developer.android.com/jetpack/docs/guide), integrate cleanly with other [Jetpack](https://developer.android.com/jetpack) components, and provide first-class Kotlin support.

## Benefits of using the Paging library

The Paging library includes the following features:

  * In-memory caching for your paged data. This helps ensure that your app uses system resources efficiently while working with paged data.
  * Built-in request deduplication, which helps ensure that your app uses network bandwidth and system resources efficiently.
  * First-class support for Kotlin coroutines and flows.
  * Built-in support for error handling, including refresh and retry capabilities.



## Setup

To import Paging components into your Android app, add the following dependencies to your app's `build.gradle` file:

### Kotlin
    
    
    dependencies {
      val paging_version = "3.4.2"
    
      implementation("androidx.paging:paging-common:$paging_version")
    
      // Jetpack Compose integration
      implementation("androidx.paging:paging-compose:$paging_version")
    }

### Groovy
    
    
    dependencies {
      def paging_version = "3.4.2"
    
      implementation "androidx.paging:paging-common:$paging_version"
    
      // Jetpack Compose integration
      implementation "androidx.paging:paging-compose:$paging_version"
    }

## Library architecture

The Paging library's components operate in three layers of your app:

  * The repository layer
  * The `ViewModel` layer
  * The UI layer

![An image showing paged data flows from the PagingSource or RemoteMediator components in the repository layer to the Pager component in the ViewModel layer.
    Then the Pager component exposes a Flow of PagingData to the
    lazy layout components in the UI layer.](https://developer.android.com/static/topic/libraries/architecture/images/paging3-library-architecture.svg)**Figure 1.** An example of how the Paging library fits into your app architecture. 

This section describes the Paging library components that operate at each layer and how they work together to load and display paged data.

### Repository layer

The primary Paging library component in the repository layer is [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource). Each `PagingSource` object defines a source of data and how to retrieve data from that source. A `PagingSource` object can load data from any single source, including network sources and local databases.

Another Paging library component that you might use is [`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator). A `RemoteMediator` object handles paging from a layered data source, such as a network data source with a local database cache.

### ViewModel layer

The [`Pager`](https://developer.android.com/reference/kotlin/androidx/paging/Pager) component provides a public API for constructing instances of `PagingData` that are exposed in reactive streams, based on a `PagingSource` object and a [`PagingConfig`](https://developer.android.com/reference/kotlin/androidx/paging/PagingConfig) configuration object.

The component that connects the `ViewModel` layer to the UI is [`PagingData`](https://developer.android.com/reference/kotlin/androidx/paging/PagingData). A `PagingData` object is a container for a snapshot of paginated data. It queries a [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) object and stores the result.

### UI layer

The primary Paging UI API is [`collectAsLazyPagingItems()`](https://developer.android.com/reference/kotlin/androidx/paging/compose/collectAsLazyPagingItems.composable). It exposes paged items as a list of data that can be easily consumed by Compose's lazy layout components, like `LazyColumn` and `LazyRow`.

Add the `androidx.paging:paging-compose` library to use Compose-compatible APIs that let the UI automatically react to data loads, updates, and errors without the need for adapters or diffing logic. Use the [`collectAsLazyPagingItems()`](https://developer.android.com/reference/kotlin/androidx/paging/compose/collectAsLazyPagingItems.composable) extension function on a `Flow<PagingData>` to pass in the returned [`LazyPagingItems`](https://developer.android.com/reference/kotlin/androidx/paging/compose/LazyPagingItems) to `items()` in a `LazyColumn`.
    
    
    @Composable
    fun MessageList(pager: Pager<Int, Message>) {
        val lazyPagingItems = pager.flow.collectAsLazyPagingItems()
    
        LazyColumn {
            items(
                lazyPagingItems.itemCount,
                key = lazyPagingItems.itemKey { it.id }
            ) { index ->
                val message = lazyPagingItems[index]
                if (message != null) {
                    MessageRow(message)
                } else {
                    MessagePlaceholder()
                }
            }
        }
    }
    
    [LazyListSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/compose/snippets/src/main/java/com/example/compose/snippets/lists/LazyListSnippets.kt#L348-L365)

For more information, see [Large data-sets (paging)](https://developer.android.com/develop/ui/compose/lists#large-datasets).

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
  * [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration)
  * [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
