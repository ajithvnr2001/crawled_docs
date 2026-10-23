---
url: https://developer.android.com/training/cars/apps/library/screen-navigation/
title: Implement screen navigation \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:05.486948+00:00
---

# Implement screen navigation  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/screen-navigation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Implement screen navigation Stay organized with collections  Save and categorize content based on your preferences. 

Apps often present a number of different screens, each possibly using different templates the user can navigate through as they interact with the interface.

The `ScreenManager` class provides a screen stack you can use to push screens that can be popped automatically when the user selects a **Back** button on the car screen or uses the hardware **Back** button available in some cars.

This code shows how to add a back action to a message template as well as an action to push a new screen when selected by the user:
    
    
    val header = Header.Builder()
        .setStartHeaderAction(Action.BACK)
        .build()
    
    val template = MessageTemplate.Builder("Hello world!")
        .setHeader(header)
        .addAction(
            Action.Builder()
                .setTitle("Next screen")
                .setOnClickListener { screenManager.push(NextScreen(carContext)) }
                .build()
        )
        .build()
    
    [ScreenNavigation.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/ScreenNavigation.kt#L30-L42)

The [`Action.BACK`](https://developer.android.com/reference/androidx/car/app/model/Action#BACK\(\)) object is a standard [`Action`](https://developer.android.com/reference/androidx/car/app/model/Action) that automatically invokes [`ScreenManager.pop`](https://developer.android.com/reference/androidx/car/app/ScreenManager#pop\(\)). This behavior can be overridden by using the [`OnBackPressedDispatcher`](https://developer.android.com/reference/androidx/activity/OnBackPressedDispatcher) instance available from the `CarContext`.

To promote safe driving, the screen stack can consist of no more than five screens. To learn more, see [Template restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).

[ Previous arrow_back  Create your start screen  ](https://developer.android.com/training/cars/apps/library/start-screen)

[ Next Refresh the contents of a template  arrow_forward  ](https://developer.android.com/training/cars/apps/library/refresh-template)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
