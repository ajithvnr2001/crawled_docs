---
url: https://developer.android.com/training/cars/apps/library/lifecycles/
title: CarAppService, Session, and Screen lifecycles \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:03.799680+00:00
---

# CarAppService, Session, and Screen lifecycles  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/lifecycles/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  CarAppService, Session, and Screen lifecycles Stay organized with collections  Save and categorize content based on your preferences. 

The [`Session`](https://developer.android.com/reference/androidx/car/app/Session) and [`Screen`](https://developer.android.com/reference/androidx/car/app/Screen) classes implement the [`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner) interface. As the user interacts with the app, lifecycle callbacks of your `Session` and `Screen` objects are invoked, as illustrated in Figures 1 and 2.

### CarAppService and Session lifecycles

To learn more, see the [`Session.getLifecycle`](https://developer.android.com/reference/androidx/car/app/Session#getLifecycle\(\)) method.

![](https://developer.android.com/static/images/training/cars/carappservice-session-lifecycle.png)**Figure 1**. Session lifecycle.

### Screen lifecycle

To learn more, see [`Screen.getLifecycle`](https://developer.android.com/reference/androidx/car/app/Screen#getLifecycle) method.

![](https://developer.android.com/static/images/training/cars/screen-lifecycle.png)**Figure 2**. Screen lifecycle.

[ Previous arrow_back  CarContext class  ](https://developer.android.com/training/cars/apps/library/carcontext-class)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
