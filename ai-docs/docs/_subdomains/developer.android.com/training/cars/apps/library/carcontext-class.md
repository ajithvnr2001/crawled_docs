---
url: https://developer.android.com/training/cars/apps/library/carcontext-class/
title: CarContext class \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:03.636993+00:00
---

# CarContext class  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/carcontext-class/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  CarContext class Stay organized with collections  Save and categorize content based on your preferences. 

The [`CarContext`](https://developer.android.com/reference/androidx/car/app/CarContext) class extends [`ContextWrapper`](https://developer.android.com/reference/android/content/ContextWrapper), making it accessible to your `Session` and `Screen` instances. `CarContext` provides access to essential car services, including the:

  * [`ScreenManager`](https://developer.android.com/reference/androidx/car/app/ScreenManager), to manage the [screen stack](https://developer.android.com/training/cars/apps/library/template-restrictions).
  * [`AppManager`](https://developer.android.com/reference/androidx/car/app/AppManager), to get general app-related functionality, such as accessing the `Surface` object for [drawing maps](https://developer.android.com/training/cars/apps/library/draw-maps).
  * [`NavigationManager`](https://developer.android.com/reference/androidx/car/app/navigation/NavigationManager), used by turn-by-turn navigation apps to communicate [navigation metadata](https://developer.android.com/training/cars/apps/navigation#navigation-metadata) and other [navigation-related events](https://developer.android.com/training/cars/apps/navigation#starting-ending-stopping-navigation) with the host.



To see a list of library functionality available to navigation apps, see [Access the navigation templates](https://developer.android.com/training/cars/apps/navigation#access-navigation-templates).

`CarContext` also offers other functionality, such as letting you load drawable resources by using the configuration from the car screen and signaling that your app should display its map in [dark theme](https://developer.android.com/training/cars/apps/library/draw-maps#dark-theme).

[ Previous arrow_back  Template restrictions  ](https://developer.android.com/training/cars/apps/library/template-restrictions)

[ Next CarAppService, Session, and Screen lifecycles  arrow_forward  ](https://developer.android.com/training/cars/apps/library/lifecycles)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
