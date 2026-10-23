---
url: https://developer.android.com/training/cars/apps/library/refresh-template/
title: Refresh the contents of a template \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:05.652723+00:00
---

# Refresh the contents of a template  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/refresh-template/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Refresh the contents of a template Stay organized with collections  Save and categorize content based on your preferences. 

Your app can request the content of a `Screen` to be invalidated by calling the [`Screen.invalidate`](https://developer.android.com/reference/androidx/car/app/Screen#invalidate\(\)) method. The host subsequently calls back into your app's [`Screen.onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate\(\)) method to retrieve the template with the new contents.

When refreshing a `Screen`, it's important to understand the specific content in the template that can be updated so the host doesn't count the new template against the template quota. To learn more, see [Template restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).

We recommend that you structure your screens to have a one-to-one mapping between a `Screen` and the type of template it returns through its `onGetTemplate` implementation.

[ Previous arrow_back  Implement screen navigation  ](https://developer.android.com/training/cars/apps/library/screen-navigation)

[ Next Review the testing library  arrow_forward  ](https://developer.android.com/training/cars/apps/library/test-library)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
