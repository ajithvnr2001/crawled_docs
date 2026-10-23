---
url: https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop/
title: Drag and drop \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:57.960934+00:00
---

# Drag and drop  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/compose/touch-input/user-interactions/drag-and-drop/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



#  Drag and drop Stay organized with collections  Save and categorize content based on your preferences. 

Jetpack Compose supports drag and drop with two modifiers:

  * [`dragAndDropSource`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/dragAndDropSource.modifier#\(androidx.compose.ui.Modifier\).dragAndDropSource\(kotlin.Function1\)): Specifies a composable as the starting point of the drag gesture
  * [`dragAndDropTarget`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/draganddrop/dragAndDropTarget.modifier#\(androidx.compose.ui.Modifier\).dragAndDropTarget\(kotlin.Function1,androidx.compose.ui.draganddrop.DragAndDropTarget\)): Specifies a composable that accepts the dropped data



For example, to enable users to drag an image in your app, create an image composable and add the `dragAndDropSource` modifier. To set up a drop target, create another image composable and add the `dragAndDropTarget` modifier.

The modifiers can be applied to multiple drag sources and multiple drop targets.

The modifiers enable apps to share data between two or more composables using [`ClipData`](https://developer.android.com/reference/kotlin/android/content/ClipData), which is interoperable with [`View`](https://developer.android.com/reference/kotlin/android/view/View) implementations.

**Note:** Drag and drop is different from [pick up and move](https://m3.material.io/foundations/interaction/gestures#af76950f-a24c-43bd-bfcd-a9eb15768142), a common list pattern.

## Specify a drag source

To enable drag events inside a component, add the `dragAndDropSource` modifier. This takes a function as a parameter. Inside this function, use [`DragAndDropTransferData`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draganddrop/DragAndDropTransferData) to represent the transferable data. The data can be a remote URI, rich text data on the clipboard, a local file, or more, but they all need to be wrapped in a `ClipData` object. Provide plain text, for example, as follows:
    
    
    Modifier.dragAndDropSource { _ ->
        DragAndDropTransferData(
            ClipData.newPlainText(
                "image Url", url
            )
        )
    }
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L45-L51)

To allow the drag action to cross the borders of the app, the `DragAndDropTransferData` constructor accepts a `flags` argument. In the following example, the [`DRAG_FLAG_GLOBAL`](https://developer.android.com/reference/kotlin/android/view/View#drag_flag_global) constant specifies that data can be dragged from one app into another:
    
    
    Modifier.dragAndDropSource { _ ->
        DragAndDropTransferData(
            ClipData.newPlainText(
                "image Url", url
            ),
            flags = View.DRAG_FLAG_GLOBAL
        )
    }
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L55-L62)

`DragAndDropTransferData` accepts flags supported by the Android View system. See the list of [View](https://developer.android.com/reference/kotlin/android/view/View) constants for an exhaustive list of available flags.

## Receive drop data

Assign the `dragAndDropTarget` modifier to a composable to enable the composable to receive drag-and-drop events. The modifier has two parameters: the first acts as a filter and specifies the kind of data the modifier can accept, and the second delivers the data in a callback.

Note that the callback instance should be _remembered_. The following snippet shows how to remember the callback:
    
    
    val callback = remember {
        object : DragAndDropTarget {
            override fun onDrop(event: DragAndDropEvent): Boolean {
                // Parse received data
                return true
            }
        }
    }
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L66-L73)

To accept data from other apps, use the [`requestDragAndDropPermission`](https://developer.android.com/reference/android/app/Activity#requestDragAndDropPermissions\(android.view.DragEvent\)) to enable the reception, and release it once done:
    
    
    val externalAppCallback = remember {
        object : DragAndDropTarget {
            override fun onDrop(event: DragAndDropEvent): Boolean {
                val permission =
                    activity.requestDragAndDropPermissions(event.toAndroidDragEvent())
                // Parse received data
                permission?.release()
                return true
            }
        }
    }
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L78-L88)

It's important to remember that the `DragAndDropEvent` returned from the Compose callback is different from the one expected by the `requestDragAndDropPermission` method, so you need to call the [`toAndroidDragEvent()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draganddrop/DragAndDropEvent#\(androidx.compose.ui.draganddrop.DragAndDropEvent\).toAndroidDragEvent\(\)) extension function on the parameter before passing it to the permission request.

The next snippet demonstrates how to handle dropped plain text:
    
    
    Modifier.dragAndDropTarget(
        shouldStartDragAndDrop = { event ->
            event.mimeTypes().contains(ClipDescription.MIMETYPE_TEXT_PLAIN)
        }, target = callback // or externalAppCallback
    )
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L93-L97)

The callback function should return `true` if the event is consumed, or `false` if the event is refused and does not propagate to the parent component.

## Handle drag-and-drop events

Override callbacks in the [`DragAndDropTarget`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draganddrop/DragAndDropTarget) interface to observe when a drag-and-drop event starts, ends, or enters or exits a component for precise control of the UI and the app's behavior:
    
    
    object : DragAndDropTarget {
        override fun onStarted(event: DragAndDropEvent) {
            // When the drag event starts
        }
    
        override fun onEntered(event: DragAndDropEvent) {
            // When the dragged object enters the target surface
        }
    
        override fun onEnded(event: DragAndDropEvent) {
            // When the drag event stops
        }
    
        override fun onExited(event: DragAndDropEvent) {
            // When the dragged object exits the target surface
        }
    
        override fun onDrop(event: DragAndDropEvent): Boolean = true
    }
    
    [DragAndDropSnippets.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/compose/snippets/src/main/java/com/example/compose/snippets/draganddrop/DragAndDropSnippets.kt#L101-L119)

## Additional resources

Codelab: [Drag and drop in Compose](https://developer.android.com/codelabs/codelab-dnd-compose)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
