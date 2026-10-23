---
url: https://developer.android.com/training/cars/apps/library/draw-maps/
title: Draw maps \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:09.084088+00:00
---

# Draw maps  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/draw-maps/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Draw maps Stay organized with collections  Save and categorize content based on your preferences. 

Navigation, point of interest (POI), and weather apps using the following templates can draw maps by accessing a [`Surface`](https://developer.android.com/reference/android/view/Surface).

To use the following templates, your app must declare one of these corresponding permissions in a `<uses-permission>` element in the `AndroidManifest.xml` file.

Template | Permission | Guidance  
---|---|---  
[`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate) | `androidx.car.app.NAVIGATION_TEMPLATES` | [Navigation](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates)  
[`MapWithContentTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapWithContentTemplate) | `androidx.car.app.NAVIGATION_TEMPLATES` _or,_ `androidx.car.app.MAP_TEMPLATES` |  [Navigation](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates), [POI](https://developer.android.com/training/cars/apps/poi#access-map-template), [Weather](https://developer.android.com/training/cars/apps/weather#access-map-template)  
[`MapTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapTemplate) (_deprecated_) | `androidx.car.app.NAVIGATION_TEMPLATES` | [Navigation](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates)  
[`PlaceListNavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/PlaceListNavigationTemplate) (_deprecated_) | `androidx.car.app.NAVIGATION_TEMPLATES` | [Navigation](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates)  
[`RoutePreviewNavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/RoutePreviewNavigationTemplate) (_deprecated_) | `androidx.car.app.NAVIGATION_TEMPLATES` | [Navigation](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates)  
  
## See the reference implementation

To view a complete reference implementation, see [Navigation Sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:car/app/app-samples/navigation/).

## Declare the surface permission

In addition to the permission required for the template that your app is using, your app must declare the `androidx.car.app.ACCESS_SURFACE` permission in its `AndroidManifest.xml` file to get access to the surface:
    
    
    <manifest ...>
      ...
      <uses-permission android:name="androidx.car.app.ACCESS_SURFACE" />
      ...
    </manifest>
    

## Access the surface

To access the `Surface` that the host provides, you must implement a [`SurfaceCallback`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback) and provide that implementation to the [`AppManager`](https://developer.android.com/reference/androidx/car/app/AppManager) car service. The current `Surface` is passed to your `SurfaceCallback` in the `SurfaceContainer` parameter of the `onSurfaceAvailable()` and `onSurfaceDestroyed()` callbacks.

### Kotlin
    
    
    carContext.getCarService(AppManager::class.java).setSurfaceCallback(surfaceCallback)
    

### Java
    
    
    carContext.getCarService(AppManager.class).setSurfaceCallback(surfaceCallback);
    

## Use a virtual display to render content

In addition to rendering directly into the `Surface` using the `Canvas` API, you can also render Views into the `Surface` using the `VirtualDisplay` and `Presentation` APIs, as this example shows:
    
    
    class HelloWorldSurfaceCallback(context: Context) : SurfaceCallback {
      lateinit var virtualDisplay: VirtualDisplay
      lateinit var presentation: Presentation
    
      override fun onSurfaceAvailable(surfaceContainer: SurfaceContainer) {
          virtualDisplay = context
              .getSystemService(DisplayManager::class.java)
              .createVirtualDisplay(
                  VIRTUAL_DISPLAY_NAME ,
                  surfaceContainer.width,
                  surfaceContainer.height,
                  surfaceContainer.dpi,
                  surfaceContainer.surface,
                  0
              )
    
          presentation = Presentation(context, virtualDisplay.display)
    
          // Instantiate the view to be used as the content view
          val view = ...
    
          presentation.setContentView(view)
          presentation.show()
      }
    
      override fun onSurfaceDestroyed(surfaceContainer: SurfaceContainer) {
        presentation.dismiss()
        // This handles releasing the Surface provided when creating the VirtualDisplay
        virtualDisplay.release()
      }
    }
    

### Use Compose to render to the virtual display

You can use a `ComposeView` as the content view of the `Presentation`. Because `ComposeView` is used outside an activity, confirm that it or a parent view propagates a `LifecycleOwner` and `SavedStateRegistryOwner`. To do this, use `setViewTreeLifecycleOwner` and `setViewTreeSavedStateRegistryOwner`.

`Session` already implements `LifecycleOwner`. To serve both roles, your implementation can additionally implement `SavedStateRegistryOwner`.
    
    
    class HelloWorldSession() : Session(), SavedStateRegistryOwner { ... }
    
    class HelloWorldSurfaceCallback(session: HelloWorldSession) : SurfaceCallback {
      ...
    
      override fun onSurfaceAvailable(surfaceContainer: SurfaceContainer) {
        ...
        val view = ComposeView(session.carContext)
        view.setViewTreeLifecycleOwner(session)
        view.setViewTreeSavedStateRegistryOwner(session)
        view.setContent {
          // Composable content
        }
    
        presentation.setContentView(view)
        presentation.show()
      }
    
      ...
    }
    

## Understand the surface visible area

The host can draw user interface elements for the templates on top of the map. The host calls the [`SurfaceCallback.onVisibleAreaChanged`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onVisibleAreaChanged\(android.graphics.Rect\)) method to communicate the area of the surface most likely to be unobstructed and visible to the user.

To minimize the number of changes, the host calls the [`SurfaceCallback.onStableAreaChanged`](https://developer.android.com/reference/androidx/car/app/SurfaceCallback#onStableAreaChanged\(android.graphics.Rect\)) method with the smallest rectangle, which is always visible according to the current template.

For example, when a navigation app uses the [`NavigationTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/NavigationTemplate) with an [action strip](https://developer.android.com/training/cars/apps/library/interact-map#map-action-strip) on top, to make more space on the screen the action strip can be concealed when the user hasn't interacted with the screen. This case results in a callback to `onStableAreaChanged` and `onVisibleAreaChanged` with the same rectangle.

When the action strip is concealed, only `onVisibleAreaChanged` is called with the larger area. If the user interacts with the screen, only `onVisibleAreaChanged` is called with the first rectangle.

## Support dark theme

Apps must redraw their map onto the `Surface` instance with the proper dark colors when the host determines conditions warrant it, as described in [Android app quality for cars](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=navigation,poi,weather#MR-1).

To draw a dark map, use the [`CarContext.isDarkMode`](https://developer.android.com/reference/androidx/car/app/CarContext#isDarkMode\(\)) method. When dark theme status changes, you receive a call to [`Session.onCarConfigurationChanged`](https://developer.android.com/reference/androidx/car/app/Session#onCarConfigurationChanged\(android.content.res.Configuration\)).

**Important:** By default, apps must draw with light colors and support the dark theme, as described. However, apps can allow users to persistently display the app in either the light or dark theme.

## Draw maps on the cluster display

In addition to drawing maps on the main display, navigation apps can also support drawing maps on the cluster display behind the steering wheel. To learn more, see [Drawing to the cluster display](https://developer.android.com/training/cars/apps/navigation#drawing_to_the_cluster_display).

[ Next Let users interact with your map  arrow_forward  ](https://developer.android.com/training/cars/apps/library/interact-map)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
