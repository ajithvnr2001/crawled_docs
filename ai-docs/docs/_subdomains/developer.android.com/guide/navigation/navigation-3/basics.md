---
url: https://developer.android.com/guide/navigation/navigation-3/basics/
title: Understand and implement the basics \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:51.308553+00:00
---

# Understand and implement the basics  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/navigation-3/basics/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Understand and implement the basics Stay organized with collections  Save and categorize content based on your preferences. 

Navigation describes the way users move around your app. Users interact with UI elements, usually by tapping or clicking on them, and the app responds by displaying new content. If the user wants to go back to the previous content, they use the back gesture or tap the back button.

## Modeling navigation state

A convenient way of modeling this behavior is with a stack of content. As the user navigates _forward_ to new content, it is pushed on top of the stack. When they go _back_ from that content, it is popped off the stack and the previous content is displayed. In navigation terms, this stack is usually referred to as the **back stack** because it represents the content that the user _can go back to_.

![A software keyboard action button \(a checkmark icon\) circled in red.](https://developer.android.com/static/images/topic/libraries/architecture/back-stack.png)**Figure 1.** Diagram showing how the back stack changes with user navigation events.

## Create a back stack

In Navigation 3, the back stack does not actually contain content. Instead, it contains _references to content_ , known as **keys**. Keys can be any type but are usually simple, serializable data classes. Using references rather than content has the following benefits:

  * It is simple to navigate by pushing keys onto the back stack.
  * As long as the keys are serializable, the back stack can be saved to persistent storage, allowing it to survive configuration changes and process death. This is important because users expect to leave your app, come back to it later, and pick up where they left off with the same content being displayed. See [Save your back stack](https://developer.android.com/guide/navigation/navigation-3/save-state#save-back) for more information.



A key concept in the Navigation 3 API is that you own the back stack. The library:

  * Expects that your back stack will be a snapshot-state backed `List<T>`, where `T` is the type of your back stack `keys`. You can use `Any` or you can provide your own, more strongly-typed keys. When you see the terms "push" or "pop", the underlying implementation is to add or remove items from the end of a list.
  * Observes your back stack and reflects its state in the UI using a [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.composable).



The following example shows how to create keys and a back stack, and modify the back stack in response to user navigation events:
    
    
    // Define keys that will identify content
    data object ProductList
    data class ProductDetail(val id: String)
    
    @Composable
    fun MyApp() {
    
        // Create a back stack, specifying the key the app should start with
        val backStack = remember { mutableStateListOf<Any>(ProductList) }
    
        // Supply your back stack to a NavDisplay so it can reflect changes in the UI
        // ...more on this below...
    
        // Push a key onto the back stack (navigate forward), the navigation library will reflect the change in state
        backStack.add(ProductDetail(id = "ABC"))
    
        // Pop a key off the back stack (navigate back), the navigation library will reflect the change in state
        backStack.removeLastOrNull()
    }
    
    [BasicSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/navigation3/basic/BasicSnippets.kt#L32-L50)

## Resolve keys to content

Content is modeled in Navigation 3 using [`NavEntry`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntry), which is a class containing a composable function. It represents a _destination_ \- a single piece of content that the user can navigate _forward to_ and _back from_.

A `NavEntry` can also contain metadata - information about the content. This metadata can be read by container objects, like `NavDisplay`, to help them decide how to display the `NavEntry`'s content. For example, metadata can be used to override the default animations for a specific `NavEntry`. NavEntry `metadata` is a map of `String` keys to `Any` values, providing versatile data storage.

To convert a `key` to a `NavEntry`, create an Entry Provider. This is a function that accepts a `key` and returns a `NavEntry` for that `key`. It is usually defined as a lambda parameter when creating a `NavDisplay`.

There are two ways to create an Entry Provider, either by creating a lambda function directly, or by using the [`entryProvider`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#entryProvider\(kotlin.Function1,kotlin.Function1\)) DSL.

### Create an Entry Provider function directly

You typically create an Entry Provider function using a `when` statement, with a branch for each of your keys.
    
    
    entryProvider = { key ->
        when (key) {
            is ProductList -> NavEntry(key) { Text("Product List") }
            is ProductDetail -> NavEntry(
                key,
                metadata = mapOf("extraDataKey" to "extraDataValue")
            ) { Text("Product ${key.id} ") }
    
            else -> {
                NavEntry(Unit) { Text(text = "Invalid Key: $it") }
            }
        }
    }
    
    [BasicSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/navigation3/basic/BasicSnippets.kt#L59-L71)

### Use the `entryProvider` DSL

The `entryProvider` DSL can simplify your lambda function by avoiding the need to test against each of your key types, and construct a `NavEntry` for each one. Use the `entryProvider` builder function for this. It also includes default fallback behavior (throwing an error) if the key isn't found.
    
    
    entryProvider = entryProvider {
        entry<ProductList> { Text("Product List") }
        entry<ProductDetail>(
            metadata = mapOf("extraDataKey" to "extraDataValue")
        ) { key -> Text("Product ${key.id} ") }
    }
    
    [BasicSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/navigation3/basic/BasicSnippets.kt#L82-L87)

Note the following from the snippet:

  * `entry` is used to define a `NavEntry` with the given type and composable content
  * `entry` accepts a `metadata` parameter to set `NavEntry.metadata`



## Display the back stack

The back stack represents your app's navigation state. Whenever the back stack changes, the app UI should reflect the new back stack state. In Navigation 3, a `NavDisplay` observes your back stack and updates its UI accordingly. Construct it with following parameters:

  * Your back stack - this should be of type `SnapshotStateList<T>`, where `T` is the type of your back stack keys. It is an observable `List` so that it triggers recomposition of `NavDisplay` when it changes.
  * An `entryProvider` to convert the keys in your back stack to `NavEntry` objects.
  * Optionally, supply a lambda to the `onBack` parameter. This is called when the user triggers a back event.



The following example shows how to create a `NavDisplay`.
    
    
    data object Home
    data class Product(val id: String)
    
    @Composable
    fun NavExample() {
    
        val backStack = remember { mutableStateListOf<Any>(Home) }
    
        NavDisplay(
            backStack = backStack,
            onBack = { backStack.removeLastOrNull() },
            entryProvider = { key ->
                when (key) {
                    is Home -> NavEntry(key) {
                        ContentGreen("Welcome to Nav3") {
                            Button(onClick = {
                                backStack.add(Product("123"))
                            }) {
                                Text("Click to navigate")
                            }
                        }
                    }
    
                    is Product -> NavEntry(key) {
                        ContentBlue("Product ${key.id} ")
                    }
    
                    else -> NavEntry(Unit) { Text("Unknown route") }
                }
            }
        )
    }
    
    [BasicSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/navigation3/basic/BasicSnippets.kt#L93-L124)

By default, the `NavDisplay` shows the topmost `NavEntry` on the back stack in a single pane layout. The following recording shows this app running:

![`NavDisplay` default behavior with two
destinations.](https://developer.android.com/static/images/topic/libraries/architecture/nav3.gif)**Figure 2.** `NavDisplay` default behavior with two destinations.

## Destination lifecycle

`NavDisplay` uses [custom `LifecycleOwner`s](https://developer.android.com/topic/libraries/architecture/lifecycle#create-custom-lifecycle-owner) to cap the lifecycle state of a `NavEntry` based on both [Scene](https://developer.android.com/guide/navigation/navigation-3/scenes)-level constraints and Entry-level constraints.

For more information about lifecycles in Compose, see [Lifecycle in Jetpack Compose](https://developer.android.com/topic/libraries/architecture/lifecycle).

### Scene-level lifecycle constraints

`NavDisplay` manages the lifecycle of the active `Scene`s. Scene-level caps are determined as follows:

For non-overlay scenes:

  * **[`RESUMED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#RESUMED)** : Allowed only when the scene transition has settled and there are no active overlay scenes displaying on top of it.
  * **[`STARTED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#STARTED)** : Capped at `STARTED` while the scene transitions, such as when navigating forward or back, or when it's covered by an overlay.



For [overlay scenes](https://developer.android.com/reference/kotlin/androidx/navigation3/scene/OverlayScene), such as dialogs or bottom sheets:

  * **`RESUMED`** : Allowed only for the topmost, currently active overlay scene.
  * **`STARTED`** : Capped at `STARTED` for any underlying overlay scenes that are covered by a newer overlay.



### Entry-level lifecycle state

The library manages the maximum lifecycle state of each individual `NavEntry` based on its presence in the back stack:

  * **`RESUMED`** : If the entry is present in the current back stack, its lifecycle is allowed to go up to `RESUMED` (subject to the scene-level cap).
  * **[`CREATED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#CREATED)** : If the entry's **no longer in the back stack** , such as when it was popped but is still being rendered on screen while animating out, the library strictly caps its lifecycle at `CREATED`. This limit ensures that background or exiting entries stop executing active work such as collecting flows or launching coroutines bound to `RESUMED` or `STARTED` states while they finish their exit transitions.



### How they combine

For example, the final lifecycle state of a `NavEntry` is resolved as follows:

Scenario | Scene-Level Cap | Entry-Level Cap | Effective Cap  
---|---|---|---  
**Active entry, settled screen** (no transitions or overlays) | `RESUMED` | `RESUMED` | **`RESUMED`**  
**Active entry, during transition** (navigating to or from) | `STARTED` | `RESUMED` | **`STARTED`**  
**Active entry, covered by an overlay** (for example, a Dialog is open) | `STARTED` | `RESUMED` | **`STARTED`**  
**Popped entry, animating out** | `STARTED` or `RESUMED` | `CREATED` | **`CREATED`**  
  
## Putting it all together

The following diagram shows how data flows between the various objects in Navigation 3:

![A visualization of how data flows between the various objects in Navigation 3.](https://developer.android.com/static/images/topic/libraries/architecture/data-flow.png)**Figure 3.** Diagram showing how data flows through various objects in Navigation 3.

  1. **Navigation events initiate changes**. Keys are added or removed from the back stack in response to user interactions.

  2. **Change in back stack state triggers content retrieval**. The `NavDisplay` (a composable that renders a back stack) observes the back stack. In its default configuration, it displays the topmost back stack entry in a single pane layout. When the top key on the back stack changes, the `NavDisplay` uses this key to request the corresponding content from the entry provider.

  3. **Entry provider supplies content**. The entry provider is a function that resolves a key to a `NavEntry`. Upon receiving a key from the `NavDisplay`, the entry provider provides the associated `NavEntry`, which contains both the key and the content.

  4. **Content is displayed**. The `NavDisplay` receives the `NavEntry` and displays the content.




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
