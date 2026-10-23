---
url: https://developer.android.com/training/wearables/tiles/interactions/
title: Interact with tiles \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:24.010833+00:00
---

# Interact with tiles  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/tiles/interactions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Interact with tiles Stay organized with collections  Save and categorize content based on your preferences. 

Tiles can do more than just display information; they can also be interactive. To make an element such as [`textButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#\(androidx.wear.protolayout.material3.MaterialScope\).textButton\(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,androidx.wear.protolayout.material3.TextButtonStyle,androidx.wear.protolayout.ModifiersBuilders.Padding\)) respond to taps, generate a click handler using [`clickable()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/package-summary#clickable\(androidx.wear.protolayout.ActionBuilders.Action,kotlin.String,kotlin.Float,kotlin.Float\)) and associate it with the layout element.

You can configure a `Clickable` to trigger an action in two main ways:

  1. **Launch an activity directly** : Use [`launchAction()`](https://developer.android.com/reference/androidx/wear/protolayout/ActionBuilders#launchAction\(android.content.ComponentName\)) for cases where you need to open an activity immediately.
  2. **Delegate to your tile service** : Use [`loadAction()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/package-summary#loadAction\(androidx.wear.protolayout.expression.DynamicDataMap\)) to trigger logic within your `TileService`. This is a more flexible approach that lets you refresh the tile's content, update its state, or launch a more complex activity.

**Note:** The system automatically creates a tappable area of at least 48dp x 48dp around each `Clickable` element for accessibility purposes. If you have multiple interactive elements, maintain enough spacing between them to prevent their touch targets from overlapping. [Material components for tiles](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary) already follow this guidance.

## Launch an exported activity

If a user tap should immediately launch an activity, use [`launchAction()`](https://developer.android.com/reference/androidx/wear/protolayout/ActionBuilders#launchAction\(android.content.ComponentName\)). Provide a `ComponentName` to identify the activity. The activity must be [exported](https://developer.android.com/guide/topics/manifest/activity-element#exported). With this approach, you can pass `Intent` extras with the action. However, it's not possible to set custom `Intent` flags.

The following example shows how to create a `Clickable` to launch `TileActivity` with two extras, `name` and `age`:
    
    
    textButton(
        labelContent = {
            text("launchAction()".layoutString, typography = BODY_LARGE)
        },
        onClick =
        clickable(
            action =
            launchAction(
                ComponentName(
                    "com.example.wear",
                    "com.example.wear.snippets.m3.tile.TileActivity",
                ),
                mapOf(
                    "name" to ActionBuilders.stringExtra("Bartholomew"),
                    "age" to ActionBuilders.intExtra(21),
                ),
            )
        ),
    )
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L251-L269)

Inside the launched activity, retrieve the values from the intent extras:
    
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    
        // When this activity is launched from the tile InteractionLaunchAction,
        // "name" will be "Bartholomew" and "age" will be 21
        val name = intent.getStringExtra("name")
        val age = intent.getStringExtra("age")
    
        // ...
    }
    
    [TileActivity.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/TileActivity.kt#L50-L61)

## Handle interactions in your tile service

For more flexible interactions, use [`loadAction()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/package-summary#loadAction\(androidx.wear.protolayout.expression.DynamicDataMap\)). When a user taps an element configured with `loadAction`, the system re-invokes your [`TileService.onTileRequest()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileRequest\(androidx.wear.tiles.RequestBuilders.TileRequest\)). This lets you run logic in your service to update the tile, change its state, and perform more complex tasks.

### Refresh the tile's content

The simplest use of `loadAction` is to signal a refresh. Call [`loadAction`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/package-summary#loadAction\(androidx.wear.protolayout.expression.DynamicDataMap\)) with no arguments. When tapped, the system calls `onTileRequest()`, allowing your service to return a new layout with updated content.
    
    
    textButton(
        onClick = clickable(loadAction()),
        labelContent = { text("Refresh".layoutString) },
    )
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L106-L109)

**Note:** To avoid a visual flicker when the tile reloads, design your layout so that only the content that changes is updated. The overall layout structure and animations should remain consistent between reloads.

### Distinguish among multiple interactive elements

If your tile contains multiple interactive elements, you can associate an ID with the `Clickable` modifier:
    
    
    textButton(
        labelContent = {
            text("Deep Link me!".layoutString, typography = BODY_LARGE)
        },
        onClick = clickable(id = "foo", action = loadAction()),
    )
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L164-L169)

Inside `onTileRequest()`, you can check this ID using `requestParams.currentState.lastClickableId` to decide what action to perform.

**Example: Launching an activity with a deep link**

This pattern is ideal for launching an activity with a [deep link](https://developer.android.com/guide/navigation/design/deep-link#compose-implicit). The user tap reloads the tile, your service inspects the ID, and then launches the new activity. To control the back stack, use a `TaskStackBuilder` to provide a better navigation experience for the user. When the user taps the element, they are taken directly to the deep-linked screen (the `message_detail/1` screen from the example). Because [`.addNextIntentWithParentStack()`](https://developer.android.com/reference/android/app/TaskStackBuilder#addNextIntentWithParentStack\(android.content.Intent\)) was used, the parent activity is also added to the back stack. This means if the user swipes back, they will navigate up to the app's main screen (`MessageList` in the example) instead of immediately exiting to the tile. Swiping back a second time returns them to the tile.
    
    
    override fun onTileRequest(
        requestParams: RequestBuilders.TileRequest
    ): ListenableFuture<Tile?> {
        val lastClickableId = requestParams.currentState.lastClickableId
        if (lastClickableId == "foo") {
            TaskStackBuilder.create(this)
                .addNextIntentWithParentStack(
                    Intent(
                        Intent.ACTION_VIEW,
                        "googleandroidsnippets://app/message_detail/1".toUri(),
                        this,
                        TileActivity::class.java,
                    )
                )
                .startActivities()
        }
        // ... User didn't tap a button (either first load or tapped somewhere else)
        // ...
    }
    
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L118-L150)

Then, in `TileActivity`, configure your navigation to match the `googleandroidsnippets://app/message_detail/{id}` pattern.
    
    
    AppScaffold {
        val navController = rememberSwipeDismissableNavController()
        SwipeDismissableNavHost(
            navController = navController,
            startDestination = "message_list",
        ) {
            // ...
            composable(
                route = "message_detail/{id}",
                deepLinks =
                listOf(
                    navDeepLink {
                        uriPattern = "googleandroidsnippets://app/message_detail/{id}"
                    }
                ),
            ) {
                val id = it.arguments?.getString("id") ?: "0"
                MessageDetails(details = "message $id")
            }
        }
    }
    
    [TileActivity.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/TileActivity.kt#L68-L104)

Use `TaskStackBuilder` to provide a better navigation experience for the user. When the user taps the element, they are taken directly to the deep-linked screen—in this example, that's the `message_detail/1` screen. Because [`.addNextIntentWithParentStack()`](https://developer.android.com/guide/navigation/design/deep-link#compose-implicit) was used, the parent activity is also added to the back stack. This means if the user swipes back, they will navigate up to the app's main screen—`MessageList` in the example—instead of immediately exiting to the tile. Swiping back a second time returns them to the tile.

### Update state within the tile

Your tile has a [`StateBuilders.State`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/StateBuilders.State) object that stores key-value pairs and persists across reloads. You can use `loadAction()` to update this state when a user interacts with the tile.

To do this, pass a [`DynamicDataMap`](https://developer.android.com/reference/androidx/wear/protolayout/expression/DynamicDataMap) to `loadAction()` containing the new state values.
    
    
    textButton(
        labelContent = {
            text("loadAction()".layoutString, typography = BODY_LARGE)
        },
        onClick =
        clickable(
            action =
            loadAction(
                dynamicDataMapOf(
                    stringAppDataKey("name") mapTo "Javier",
                    intAppDataKey("age") mapTo 37,
                )
            )
        ),
    )
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L223-L237)

When `onTileRequest()` is triggered by this action, you can read the updated data from `requestParams.currentState.stateMap`. This is useful for interactions that directly modify data on the tile, like incrementing a counter or toggling a setting.
    
    
    override fun onTileRequest(
        requestParams: RequestBuilders.TileRequest
    ): ListenableFuture<Tile> {
    
        // When triggered by loadAction(), "name" will be "Javier", and "age" will
        // be 37.
        with(requestParams.currentState.stateMap) {
            val name = this[stringAppDataKey("name")]
            val age = this[intAppDataKey("age")]
        }
    
        // ...
    }
    
    [Interaction.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/tile/Interaction.kt#L178-L203)

## Recommended for you

  * [Create your first Tile in Wear OS](https://developer.android.com/codelabs/wear-tiles)
  * [Migrate to ProtoLayout namespaces](https://developer.android.com/training/wearables/tiles/migrate-to-protolayout)
  * [Show dynamic updates in tiles](https://developer.android.com/training/wearables/tiles/dynamic)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
