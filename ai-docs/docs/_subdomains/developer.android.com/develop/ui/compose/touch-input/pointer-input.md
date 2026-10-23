---
url: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/
title: Pointer input in Compose \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:35:25.995832+00:00
---

# Pointer input in Compose  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/compose/touch-input/pointer-input/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



#  Pointer input in Compose Stay organized with collections  Save and categorize content based on your preferences. 

Compose provides a variety of APIs to help you detect gestures that are generated from user interactions. The APIs cover a wide range of use cases:

  * Some of them are **high-level** and designed to cover the most commonly used gestures. For example, the [`clickable`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#\(androidx.compose.ui.Modifier\).clickable\(kotlin.Boolean,kotlin.String,androidx.compose.ui.semantics.Role,kotlin.Function0\)) modifier allows easy detection of a click, and it also provides accessibility features and displays visual indicators when tapped (such as ripples).

  * There are also less commonly used gesture detectors that offer more flexibility on a **lower level** , like [`PointerInputScope.detectTapGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#\(androidx.compose.ui.input.pointer.PointerInputScope\).detectTapGestures\(kotlin.Function1,kotlin.Function1,kotlin.coroutines.SuspendFunction2,kotlin.Function1\)) or [`PointerInputScope.detectDragGestures`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#\(androidx.compose.ui.input.pointer.PointerInputScope\).detectDragGestures\(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2\)) but don't include the extra features.




Learn more about pointer input on the following pages:

  * [Understand gestures](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures) gives an explanation of the core concepts playing a role when handling pointer input.
  * [Tap and press](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/tap-and-press) expands on single pointer, single position events.
  * [Scroll](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/scroll) explains how to implement scrolling containers, and handles interoperability concerns.
  * [Drag composables](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/drag-composables) explains how to move UI elements along a single axis, across two dimensions, or between predefined anchor points using modifiers like `draggable`, `draggable2D`, and `anchoredDraggable`.
  * [Multi-touch](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/multi-touch) dives into situations where more than one pointer is used.



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Enable user interactions](https://developer.android.com/develop/ui/compose/text/user-interactions)
  * [Semantics in Compose](https://developer.android.com/develop/ui/compose/semantics)
  * [Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers)



[ Next Understand gestures  arrow_forward  ](https://developer.android.com/develop/ui/compose/touch-input/pointer-input/understand-gestures)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
