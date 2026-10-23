---
url: https://developer.android.com/training/cars/apps/library/constraints-api/
title: Constraints API \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:07.320559+00:00
---

# Constraints API  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/constraints-api/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Constraints API Stay organized with collections  Save and categorize content based on your preferences. 

Different cars can allow for differing numbers of [`Item`](https://developer.android.com/reference/androidx/car/app/model/Item) instances to be displayed to the user at a time. Use the [`ConstraintManager`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager) to check the content limit at runtime and to set the appropriate number of items in your templates.

**Important:** The host sets these limits, which can't be modified by client apps. To see minimum values, see the [`integers.xml`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:car/app/app/src/main/res/values/integers.xml) resource file.

Get a `ConstraintManager` from the `CarContext`:
    
    
    val manager = carContext.getCarService(ConstraintManager::class.java)
    
    [Constraints.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/Constraints.kt#L26-L26)

Query the retrieved `ConstraintManager` object for the relevant content limit. For example, to get the number of items that can be displayed in a grid, call [`getContentLimit`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager#getContentLimit\(int\)) with [`CONTENT_LIMIT_TYPE_GRID`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager#CONTENT_LIMIT_TYPE_GRID\(\)):
    
    
    val gridItemLimit = manager.getContentLimit(ConstraintManager.CONTENT_LIMIT_TYPE_GRID)
    
    [Constraints.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/Constraints.kt#L30-L30)

[ Previous arrow_back  Connection API  ](https://developer.android.com/training/cars/apps/library/connection-api)

[ Next Car Hardware APIs  arrow_forward  ](https://developer.android.com/training/cars/apps/library/car-hardware-api)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
