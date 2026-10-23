---
url: https://developer.android.com/studio/projects/templates/
title: Add code from a template \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:36.314751+00:00
---

# Add code from a template  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/projects/templates/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Add code from a template Stay organized with collections  Save and categorize content based on your preferences. 

Android Studio provides code templates that follow the Android design and development best practices to get you on the right track to creating beautiful, functional apps. You can use templates to create new app modules, individual activities, or other specific Android project components.

Some templates provide starter code for common usage contexts, such as navigation drawers or login screens. You can choose from these app module and activity templates when you first [create your project](https://developer.android.com/studio/projects/create-project), when you [add a new app module within an existing project](https://developer.android.com/studio/projects/add-app-module), or when you add a new activity within an app module.

In addition to activities, you can also add other Android project components to an existing app using templates. These templates include both code components, such as services and composables, and non-code components, such as folders and XML files.

This page discusses how to add Android project components like activities to your project and describes the commonly used activity templates available in Android Studio. Note that most Android Studio templates depend on [AndroidX](https://developer.android.com/jetpack/androidx) and use [Material Design 3](https://m3.material.io/) principles to help you quickly build responsive UIs.

## Add a project component

Android Studio groups templates by the type of component that they add, such as an **Activity** or a Compose component, as shown in figure 1.

To add an Android project component using a template, use the **Project** window. Right-click on the folder in which you want to add the new component, and select **New**. Based on what components can be added to the folder you clicked on, you then see a list of template types like those shown in figure 1.

When you select the template you want to add, a corresponding wizard window appears and asks for the component's configuration information, such as its name. After you enter the configuration information, Android Studio creates and opens the files for your new component. It also runs a Gradle build to sync your project.

![](https://developer.android.com/static/studio/images/projects/templates-menu.png)**Figure 1**. The templates menu, accessible through the **File** > **New** menu or by right-clicking in the **Project** window.

## Select an activity template

One of the most common uses of templates is adding new activities to an existing app module. There are templates for creating screens for logging into an account, presenting a list of items with details, or scrolling through a long block of text.

Android Studio also provides templates for a variety of different app module types, including Wear OS, Android TV, and Cloud App Engine. You can view templates for these different module types when adding a project component. Templates also exist for more API-specific modules and activities, such as Google AdMobs Ads and Google Maps.

![](https://developer.android.com/static/studio/images/projects/empty-compose-activity-template.png)**Figure 2**. The Empty Compose Activity template.

One of the most commonly used templates is the Empty Compose Activity template, which creates an empty activity with a sample composable and a preview of the composable. It lets you start from scratch when building your app module or activity.

![](https://developer.android.com/static/studio/images/projects/empty-compose-activity-template-detail.png)**Figure 3**. Configuration for the Empty Compose Activity template.

For more information on building Compose apps in Android Studio, see [Get started with Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
