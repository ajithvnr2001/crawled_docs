---
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes/
title: Use window size classes \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:39:45.326496+00:00
---

# Use window size classes  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



#  Use window size classes Stay organized with collections  Save and categorize content based on your preferences. 

Window size classes are a set of opinionated viewport breakpoints that help you design, develop, and test responsive/adaptive layouts. The breakpoints balance layout simplicity with the flexibility of optimizing your app for unique cases.

Window size classes categorize the display area available to your app as _compact_ , _medium_ , _expanded_ , _large_ , or _extra large_. Available width and height are classified separately, so at any point in time, your app has two window size classes—one for width, one for height. Available width is usually more important than available height due to the ubiquity of vertical scrolling, so the width window size class is likely more relevant to your app's UI.

![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/window-size-classes/window_size_classes_width.png)**Figure 1.** Representations of width-based window size classes. ![](https://developer.android.com/static/develop/ui/compose/images/layouts/adaptive/window-size-classes/window_size_classes_height.png)**Figure 2.** Representations of height-based window size classes. 

As visualized in the figures, the breakpoints allow you to continue thinking about layouts in terms of devices and configurations. Each size class breakpoint represents a majority case for typical device scenarios, which can be a helpful frame of reference as you think about the design of your breakpoint-based layouts.

Size class | Breakpoint | Device representation  
---|---|---  
Compact width | width < 600dp | 99.96% of phones in portrait  
Medium width | 600dp ≤ width < 840dp | 93.73% of tablets in portrait, most large unfolded inner displays in portrait  
Expanded width | 840dp ≤ width < 1200dp | 97.22% of tablets in landscape, most large unfolded inner displays in landscape are at least expanded width  
Large width | 1200dp ≤ width < 1600dp | Large tablet displays  
Extra-large width | width ≥ 1600dp | Desktop displays  
Compact height | height < 480dp | 99.78% of phones in landscape  
Medium height | 480dp ≤ height < 900dp | 96.56% of tablets in landscape, 97.59% of phones in portrait  
Expanded height | height ≥ 900dp | 94.25% of tablets in portrait  
**Note:** Most apps can build an adaptive UI by considering only the width window size class. However, also consider the height window size class for scenarios such as phones or open flippables in landscape orientation; the window width is typically medium, but window height is compact, in which case two pane layouts are not practical.

Although visualizing size classes as physical devices can be useful, window size classes are explicitly not determined by the size of the device screen. Window size classes are not intended for _isTablet_ ‑type logic. Rather, window size classes are determined by the window size available to your application regardless of the type of device the app is running on, which has two important implications:

  * **Physical devices do not guarantee a specific window size class.** The screen space available to your app can differ from the screen size of the device for many reasons. On mobile devices, split‑screen mode can partition the screen between two applications. On ChromeOS, Android apps can be presented in desktop‑type windows that are arbitrarily resizable. Foldables can have two different‑sized screens individually accessed by folding or unfolding the device.

  * **The window size class can change throughout the lifetime of your app.** While your app is running, device orientation changes, multitasking, and folding/unfolding can change the amount of screen space available. As a result, the window size class is dynamic, and your app's UI should adapt accordingly.




Window size classes map to the compact, medium, and expanded breakpoints in the [Material Design layout guidance](https://m3.material.io/foundations/layout/applying-layout/window-size-classes). Additionally, large and extra-large breakpoints have been added to better target desktop and connected displays.

Use window size classes to make high‑level application layout decisions, such as deciding whether to use a specific canonical layout to take advantage of additional screen space.

Compute the current [`WindowSizeClass`](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass) using the [`currentWindowAdaptiveInfo()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/currentWindowAdaptiveInfo.composable#currentWindowAdaptiveInfo\(kotlin.Boolean\)) top‑level function of the [`androidx.compose.material3.adaptive`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/package-summary) library. The function returns an instance of [`WindowAdaptiveInfo`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/WindowAdaptiveInfo), which contains [`windowSizeClass`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/WindowAdaptiveInfo#windowSizeClass\(\)). To support large and extra-large breakpoints, add the `supportLargeAndXLargeWidth` parameter set to `true` to the function call. The following example shows how to calculate the window size class and receive updates whenever the window size class changes:
    
    
    val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass
    
    [AdaptiveLayoutSnippets.kt](https://github.com/android/snippets/blob/c00fa11b95546bc9ad455cc1569fa9c8e5dd00e4/compose/snippets/src/main/java/com/example/compose/snippets/layouts/AdaptiveLayoutSnippets.kt#L85-L85)

## Manage layouts with window size classes

Window size classes enable you to change your app layout as the display space available to your app changes, for example, when a device folds or unfolds, the device orientation changes, or the app window is resized in multi‑window mode.

Localize the logic for handling display size changes by passing window size classes down as state to nested composables just like any other app state:
    
    
    @Composable
    fun MyApp(
        windowSizeClass: WindowSizeClass = currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true).windowSizeClass
    ) {
        // Decide whether to show the top app bar based on window size class.
        val showTopAppBar = windowSizeClass.isHeightAtLeastBreakpoint(WindowSizeClass.HEIGHT_DP_MEDIUM_LOWER_BOUND)
    
        // MyScreen logic is based on the showTopAppBar boolean flag.
        MyScreen(
            showTopAppBar = showTopAppBar,
            /* ... */
        )
    }
    
    [AdaptiveLayoutSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/layouts/AdaptiveLayoutSnippets.kt#L49-L61)

## Test window size classes

As you make layout changes, test the layout behavior across all window sizes, especially at the compact, medium, and expanded breakpoint widths.

If you have an existing layout for compact screens, first optimize your layout for the expanded width size class, since this size class provides the most space for additional content and UI changes. Then decide what layout makes sense for the medium width size class; consider adding a specialized layout.

## Next steps

To learn more about how to use window size classes to create responsive/adaptive layouts, see the following:

  * For Compose-based layouts: [Support different display sizes](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)

  * For view-based layouts: [Responsive/adaptive design with views](https://developer.android.com/develop/ui/views/layout/responsive-adaptive-design-with-views)




To learn more about what makes an app great on all devices and screen sizes, see:

  * [Migrate your UI to responsive layouts](https://developer.android.com/guide/topics/large-screens/migrate-to-responsive-layouts)
  * [Large screen app quality](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)



[ Previous arrow_back  Adaptive do’s and don’ts  ](https://developer.android.com/develop/ui/compose/layouts/adaptive/adaptive-dos-and-donts)

[ Next Support different display sizes  arrow_forward  ](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
