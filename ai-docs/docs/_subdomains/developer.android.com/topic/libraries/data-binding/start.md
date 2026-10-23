---
url: https://developer.android.com/topic/libraries/data-binding/start/
title: App Architecture: UI Layer - Get Started - Android Developers \u00a0|\u00a0 Views
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:22.570805+00:00
---

# App Architecture: UI Layer - Get Started - Android Developers  |  Views

> Source: https://developer.android.com/topic/libraries/data-binding/start/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



Stay organized with collections  Save and categorize content based on your preferences. 

# Get started

Learn how to get your development environment ready to work with the Data Binding Library, including support for data binding code in Android Studio.

The Data Binding Library offers both flexibility and broad compatibility—it's a support library, so you can use it with devices running Android 4.0 (API level 14) or higher.

We recommend using the latest Android Gradle plugin in your project. However, data binding is supported on version 1.5.0 and higher. For more information, see how to [update the Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin#updating-plugin).

## Build environment

To get started with data binding, download the library from the **Support Repository** in the Android SDK manager. For more information, see [Update the IDE and SDK Tools](https://developer.android.com/studio/intro/update).

To configure your app to use data binding, enable the `dataBinding` build option in your `build.gradle` file in the app module, as shown in the following example:
    
    
    android {
        ...
        buildFeatures {
            dataBinding true
        }
    }
    

**Note:** You must configure data binding for app modules that depend on libraries that use data binding, even if the app module doesn't directly use data binding.

## Android Studio support for data binding

Android Studio supports many of the editing features for data binding code. For example, it supports the following features for data binding expressions:

  * Syntax highlighting
  * Flagging of expression language syntax errors
  * XML code completion
  * References, including [navigation](https://www.jetbrains.com/help/idea/2017.1/navigation-in-source-code.html)—such as navigating to a declaration—and [quick documentation](https://www.jetbrains.com/help/idea/2017.1/viewing-inline-documentation.html)

**Caution:** Arrays and a [generic type](https://docs.oracle.com/javase/tutorial/java/generics/types.html), such as the [`Observable`](https://developer.android.com/reference/androidx/databinding/Observable) interface, might incorrectly display errors.

The **Preview** pane in the **Layout Editor** displays the default value of data binding expressions, if provided. For example, the **Preview** pane displays the `my_default` value on the `TextView` widget declared in the following example:
    
    
    <TextView android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@{user.firstName, default=my_default}"/>
    

If you need to display a default value only during the design phase of your project, you can use `tools` attributes instead of default expression values, as described in the [Tools attributes reference](https://developer.android.com/studio/write/tool-attributes).

## Additional resources

To learn more about data binding, consult the following additional resources.

  * [ Android Data Binding Library samples](https://github.com/android/databinding-samples)


  * [ Data Binding in Android codelab](https://codelabs.developers.google.com/codelabs/android-databinding)


  * [ Data Binding — lessons learnt](https://medium.com/androiddevelopers/data-binding-lessons-learnt-4fd16576b719)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Work with observable data objects](https://developer.android.com/topic/libraries/data-binding/observability)
  * [View binding](https://developer.android.com/topic/libraries/view-binding)
  * [Paging 2 library overview](https://developer.android.com/topic/libraries/architecture/paging)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
