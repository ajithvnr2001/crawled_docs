---
url: https://developer.android.com/topic/performance/rendering/overdraw/
title: Reduce overdraw \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:10.715843+00:00
---

# Reduce overdraw  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/rendering/overdraw/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Reduce overdraw Stay organized with collections  Save and categorize content based on your preferences. 

This page explains what overdraw is, how to diagnose it, and ways to eliminate or mitigate it.

When an app draws the same pixel more than once within a single frame, this is called _overdraw_. Overdraw is usually unnecessary, and it's best to eliminate it. Overdraw becomes a performance problem when it wastes GPU time to render pixels that don't contribute to what the user sees on the screen.

## About overdraw

Overdraw refers to the system drawing a pixel on the screen multiple times in a single frame of rendering. For example, if you have a stack of UI cards, each card hides a portion of the one below it. However, the system still needs to draw the hidden portions of the cards in the stack. This is because stacked cards are rendered according to the [painter's algorithm](https://en.wikipedia.org/wiki/Painter%27s_algorithm)—that is, in back-to-front order. This sequence of rendering lets the system apply proper alpha blending to translucent objects, such as shadows.

**Note:** Although low-end devices continue to improve in GPU performance, their displays remain at relatively low resolutions. Unless optimizing for a known low-performance GPU device, we recommend instead focusing on optimizing UI thread work to help ensure smooth app performance.

## Find overdraw problems

The platform offers the following tools to help you determine if overdraw is affecting your app's performance.

### Debug GPU Overdraw tool

The Debug GPU Overdraw tool uses color-coding to show the number of times your app draws each pixel on the screen. The higher this count is, the more likely it is that overdraw will affect your app's performance.

For more information, see [Visualize GPU overdraw](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering#debug_overdraw).

### Profile GPU Rendering tool

The Profile GPU Rendering tool displays the time each stage of the rendering pipeline takes to display a single frame as a scrolling histogram. The **Process** part of each bar, indicated in orange, shows when the system is swapping buffers. This metric provides important clues about overdraw.

On less performant GPUs, available fill-rate—the speed at which the GPU can fill the frame buffer—can be low. As the number of pixels required to draw a frame increases, the GPU might take longer to process new commands and ask the rest of the system to wait until it can catch up. The **Process** bar shows this spike as the GPU gets overwhelmed trying to draw pixels as fast as possible. Issues other than the raw numbers of pixels might also cause this metric to spike. For example, if the Debug GPU Overdraw tool shows heavy overdraw and **Process** spikes, there's likely an issue with overdraw.

For more information, see [Profile GPU rendering speed](https://developer.android.com/topic/performance/rendering/inspect-gpu-rendering#profile_rendering).

**Note:** The Profile GPU Rendering tool doesn't work with apps that use the NDK. This is because the system pushes framework messages to the background whenever OpenGL takes a full-screen context. In such cases, you might find a profiling tool provided by the GPU manufacturer helpful.

## Fix overdraw

You can do the following to reduce or eliminate overdraw:

  * Remove unnecessary backgrounds in layouts.
  * Reduce transparency.



This section provides information about both of these approaches.

**Note:** In the past, one popular way of reducing overdraw was flattening the view hierarchy. This is no longer a performance requirement, because in a Compose app the UI tree is laid out in a single pass regardless of how deeply nested the composables are in the layout. For more information, see [Compose layout basics](https://developer.android.com/develop/ui/compose/layouts/basics#model).

### Remove unnecessary backgrounds in layouts

By default, a layout doesn't have a background, which means it doesn't render anything directly by itself. However, when layouts do have backgrounds, they might contribute to overdraw.

You can improve rendering performance by removing unnecessary backgrounds, such as a background that isn't visible because it's completely covered by everything the app is drawing on top of it. For example, a child [`Box`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/Box.composable) or a layout with a `.background` modifier might completely cover a parent container's background, rendering the parent's drawing pass entirely invisible to the user yet still fully processed by the GPU.

To find out why you're overdrawing, look at the component tree in the [Layout Inspector](https://developer.android.com/develop/ui/compose/tooling/debug) tool. You can look for backgrounds that aren't visible to the user and eliminate them. You can also eliminate unnecessary backgrounds wherever there are multiple containers that share a background color. Set the window background to the main background color of your app and leave all containers above it with no background values defined.

### Reduce transparency

Rendering transparent pixels on screen, known as _alpha rendering_ , is a key contributor to overdraw. Unlike standard overdraw—when the system completely hides existing drawn pixels by drawing opaque pixels on top of them—transparent objects require existing pixels to be drawn first, so that the right blending equation can occur.

Visual effects like transparent animations, fade-outs, and drop shadows involve some transparency, and can therefore contribute significantly to overdraw. You can improve overdraw in these situations by reducing the number of transparent objects you render. For example, you can get gray text by drawing black text in a [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/Text.composable#Text\(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle\)) composable and applying a translucent alpha value using `modifier = Modifier.alpha(0.5f)`. However, you can get the same effect with better performance by directly setting the composable's text color to an opaque gray: `color = Color.Black.copy(alpha = 0.5f)`.

To learn more about performance costs that transparency imposes throughout the entire drawing pipeline, watch [Hidden Costs of Transparency](https://www.youtube.com/watch?v=wIy8g8yNhNk&index=46&list=PLWz5rJ2EKKc9CBxr3BVjPTPoDPLdPIFCE).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
