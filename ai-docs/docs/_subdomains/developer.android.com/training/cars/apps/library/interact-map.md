---
url: https://developer.android.com/training/cars/apps/library/interact-map/
title: Let users interact with your map \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:10.043990+00:00
---

# Let users interact with your map  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/interact-map/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Let users interact with your map Stay organized with collections  Save and categorize content based on your preferences. 

When using the following templates, you can add support for users to interact with the maps you draw, such as letting them see different parts of a map by zooming and panning.

Template | Car App API level support  
---|---  
`NavigationTemplate` | 2  
`PlaceListNavigationTemplate` _(deprecated)_ | 4  
`RoutePreviewNavigationTemplate` _(deprecated)_ | 4  
`MapTemplate` _(deprecated)_ | 5 _(template introduced)_  
`MapWithContentTemplate` | 7 _(template introduced)_  
  
## Implement interactivity callbacks

The [`SurfaceCallback`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback) interface has several callback methods you can implement to add interactivity to maps built with the templates in the preceding section:

Interaction | Method | Car App API level support  
---|---|---  
Tap | [`onClick`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onClick\(float,%20float\)) | 5  
Pinch to zoom | [`onScale`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScale\(float,%20float,%20float\)) | 2  
Single-touch drag | [`onScroll`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScroll\(float,%20float\)) | 2  
Single-touch fling | [`onFling`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onFling\(float,%20float\)) | 2  
Double-tap | [`onScale`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScale\(float,%20float,%20float\)) _(template host determines scale factor)_ | 2  
Rotary nudge in pan mode | [`onScroll`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onScroll\(float,%20float\)) _(template host determines distance factor)_ | 2  
  
## Add a map action strip

These templates can have a map action strip for map-related actions such as zooming in and out, recentering, displaying a compass, and other actions you choose to display. The map action strip can contain up to four icon-only buttons that can be refreshed without affecting task depth. The action strip is concealed when in the idle state and reappears in the active state.

To receive map interactivity callbacks, you **must** add an `Action.PAN` button in the map action strip. When the user presses the **Pan** button, the host enters pan mode, as described in Understand pan mode.

If your app omits the `Action.PAN` button in the map action strip, it doesn't receive user input from the `SurfaceCallback` methods, and the host closes any previously activated pan mode.

On a touchscreen, the **Pan** button isn't displayed.

## Understand pan mode

In pan mode, the template host translates user input from non-touch input devices, such as rotary controllers and touchpads, into the appropriate `SurfaceCallback` methods. Respond to the user action to enter or exit pan mode with the [`setPanModeListener`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate.Builder#setPanModeListener\(androidx.car.app.navigation.model.PanModeListener\)) method in the `NavigationTemplate.Builder`. The host can hide other UI components in the template while the user is in pan mode.

[ Previous arrow_back  Draw maps  ](https://developer.android.com/training/cars/apps/library/draw-maps)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
