---
url: https://developer.android.com/training/testing/ui-tests/behavior/
title: Behavior UI Tests \u00a0|\u00a0 Test your app on Android \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:56.422676+00:00
---

# Behavior UI Tests  |  Test your app on Android  |  Android Developers

> Source: https://developer.android.com/training/testing/ui-tests/behavior/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Test your app on Android ](https://developer.android.com/training/testing)



#  Behavior UI Tests Stay organized with collections  Save and categorize content based on your preferences. 

Behavior UI tests are tests that analyze the UI hierarchy to make assertions on the properties of the UI elements.

## Jetpack frameworks

Jetpack includes various frameworks that provide APIs for writing UI tests:

  * The **[Espresso testing framework](https://developer.android.com/training/testing/espresso)** (Android 4.0.1, API level 14 or higher) provides APIs for writing UI tests to simulate user interactions with _Views_ within a single target app. A key benefit of using Espresso is that it provides automatic synchronization of test actions with the UI of the app you are testing. Espresso detects when the main thread is idle, so it is able to run your test commands at the appropriate time, improving the reliability of your tests.
  * **[Jetpack Compose](https://developer.android.com/jetpack/compose)** (Android 5.0, API level 21 or higher) provides a set of [_testing APIs_](https://developer.android.com/jetpack/compose/testing) to launch and interact with Compose screens and components. Interactions with Compose elements are synchronized with tests and have complete control over time, animations and recompositions.
  * **[UI Automator](https://developer.android.com/training/testing/ui-automator)** (Android 4.3, API level 18 or higher) is a UI testing framework suitable for cross-app functional UI testing across system and installed apps. The UI Automator APIs allows you to perform operations such as opening the Settings menu or the app launcher on a test device.
  * **[Robolectric](https://developer.android.com/training/testing/local-tests/robolectric)** (Android 4.1, API level 16 or higher) lets you create _local_ tests that run on your workstation or continuous integration environment in a regular JVM, instead of on an emulator or device. It can use Espresso or Compose testing APIs to interact with UI components.



## Additional resources

For more information about creating UI tests, consult the following resources.

### Documentation

  * [Build instrumented tests](https://developer.android.com/training/testing/instrumented-tests)
  * [Espresso](https://developer.android.com/training/testing/espresso)
  * [Compose Testing](https://developer.android.com/jetpack/compose/testing)



### Codelabs

  * [Introduction to Test Doubles and Dependency Injection](https://developer.android.com/codelabs/advanced-android-kotlin-training-testing-test-doubles)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-05 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-05 UTC."],[],[]] 
