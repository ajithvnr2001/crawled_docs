---
url: https://developer.android.com/training/wearables/compose/navigation3/
title: Navigation 3 \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:06.787836+00:00
---

# Navigation 3  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/compose/navigation3/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Navigation 3 Stay organized with collections  Save and categorize content based on your preferences. 

Navigation 3 is a navigation library designed from the ground up for Jetpack Compose. This guide explains how to implement Navigation 3 in Wear OS applications.

**Note:** Read this guide along with [the main Navigation 3 documentation](https://developer.android.com/guide/navigation/navigation-3). It focuses on the implementation for Wear OS apps, such as using the [`SwipeDismissableSceneStrategy`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation3/SwipeDismissableSceneStrategy).

## Core Concepts

  * **[`NavKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavKey)** : A type-safe, serializable identifier for a destination (screen) in your app.
  * **[`NavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavBackStack)** : A mutable list of `NavKey` instances representing the navigation history. You push and pop items directly from this list.
  * **[`rememberNavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#rememberNavBackStack)** : A composable that creates and persists the back stack across configuration changes and process death.
  * **[`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay)** : The core UI component that observes the back stack and renders the active screen.
  * **[`EntryProvider`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#entryProvider)** : A mapping DSL that links a `NavKey` to its actual `@Composable` UI.
  * **[`SwipeDismissableSceneStrategy`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation3/SwipeDismissableSceneStrategy)** : The Wear-specific strategy that wraps your screens in a swipe-to-dismiss gesture and handles built-in back animations.



## Step 1: Add dependencies

Add the required Navigation 3, Wear Compose, and Serialization dependencies to your project.

### Groovy
    
    
    dependencies {
        // Core Navigation 3 APIs
        implementation "androidx.navigation3:navigation3-runtime:1.3.0-alpha02"
        implementation "androidx.navigation3:navigation3-ui:1.3.0-alpha02"
    
        // Wear OS specific Navigation 3 integration
        implementation "androidx.wear.compose:compose-navigation3:1.7.1"
    
        // Kotlinx Serialization for type-safe routing
        implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.10.0"
    }

### Kotlin
    
    
    dependencies {
        // Core Navigation 3 APIs
        implementation("androidx.navigation3:navigation3-runtime:1.3.0-alpha02")
        implementation("androidx.navigation3:navigation3-ui:1.3.0-alpha02")
    
        // Wear OS specific Navigation 3 integration
        implementation("androidx.wear.compose:compose-navigation3:1.7.1")
    
        // Kotlinx Serialization for type-safe routing
        implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.10.0")
    }

## Step 2: Define destinations (`NavKey`s)

Screens are defined as strongly typed, serializable objects or data classes that implement the [`NavKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavKey) interface.
    
    
    @Serializable
    sealed interface Screen : NavKey {
        @Serializable
        data object Home : Screen
    
        @Serializable
        data class Details(val itemId: String) : Screen
    }
    
    [Navigation.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/java/com/example/wear/snippets/navigation3/Navigation.kt#L33-L40)

## Step 3: Setup `NavDisplay` and the back stack

At the root of your application, initialize the back stack and the Wear OS scene strategy, then plug them into [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay).
    
    
    // 1. Create the persistent back stack starting at the Home screen
    val backStack = rememberNavBackStack(Screen.Home)
    
    // 2. Initialize the Wear OS swipe-to-dismiss strategy
    val strategy = rememberSwipeDismissableSceneStrategy<NavKey>()
    
    // 3. Render the NavDisplay
    NavDisplay(
        backStack = backStack,
        sceneStrategies = listOf(strategy),
        entryProvider = entryProvider {
            // 4. Map keys to Composables
            entry<Screen.Home> {
                HomeScreen(
                    onNavigateToDetails = { id -> backStack.add(Screen.Details(id)) }
                )
            }
            entry<Screen.Details> { key ->
                DetailsScreen(
                    itemId = key.itemId,
                    onBack = { backStack.removeAt(backStack.lastIndex) }
                )
            }
        }
    )
    
    [Navigation.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/java/com/example/wear/snippets/navigation3/Navigation.kt#L46-L70)

## Step 4: Perform navigation actions

Because the back stack is just a customized `MutableList`, navigation is incredibly straightforward. You perform operations directly on the `backStack` instance:

  * **Navigate Forward** : `backStack.add(Screen.Details("123"))`
  * **Navigate Back** : `backStack.removeLast()` or `backStack.removeLastOrNull()`
  * **Clear and Reset** : `backStack.clear(); backStack.add(Screen.Home)` (or use list operations to replace the stack).



## Step 5: (Optional) Scope ViewModels to destinations

By default, [`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)s are scoped to the `Activity`. Navigation 3 provides a specific artifact ([`lifecycle-viewmodel-navigation3`](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/navigation3/package-summary)) to safely scope a `ViewModel` to a [`NavEntry`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavEntry) on the back stack. When the destination is popped off the back stack, the ViewModel is cleared.

  1. Add the dependency:
         
         implementation("androidx.lifecycle:lifecycle-viewmodel-navigation3:...")
         

  2. Add the ViewModel store decorator to your [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay)'s `entryDecorators`. You must also explicitly include the [`SaveableStateHolderNavEntryDecorator`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/SaveableStateHolderNavEntryDecorator) when providing custom decorators to retain Compose `rememberSaveable` state:
         
         NavDisplay(
             backStack = backStack,
             sceneStrategies = listOf(strategy),
             entryDecorators = listOf(
                 rememberSaveableStateHolderNavEntryDecorator(),
                 rememberViewModelStoreNavEntryDecorator()
             ),
             entryProvider = entryProvider {
                 entry<Screen.Home> {
                     // Any viewModel() requested here will be scoped to this NavEntry
                     val viewModel: HomeViewModel = viewModel()
                 }
             }
         )
         
         [Navigation.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/java/com/example/wear/snippets/navigation3/Navigation.kt#L98-L114)




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
