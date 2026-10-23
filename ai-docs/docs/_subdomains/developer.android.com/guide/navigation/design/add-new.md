---
url: https://developer.android.com/guide/navigation/design/add-new/
title: Add support for new destination types \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:36.510887+00:00
---

# Add support for new destination types  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/design/add-new/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Add support for new destination types Stay organized with collections  Save and categorize content based on your preferences. 

The [`NavController`](https://developer.android.com/reference/androidx/navigation/NavController) type relies on one or more [`Navigator`](https://developer.android.com/reference/androidx/navigation/Navigator) objects to perform the navigation operation. By default, `NavController` supports leaving the navigation graph by navigating to another activity using the [`ActivityNavigator`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator) class and its nested [`ActivityNavigator.Destination`](https://developer.android.com/reference/androidx/navigation/ActivityNavigator.Destination) class.

To navigate to any other type of destination, one or more additional `Navigator` objects must be added to the `NavController`. For example, when using fragments as destinations, the [`NavHostFragment`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment) automatically adds the [`FragmentNavigator`](https://developer.android.com/reference/androidx/navigation/fragment/FragmentNavigator) class to its `NavController`.

To add a new `Navigator` object to a `NavController`, use the [`getNavigatorProvider()`](https://developer.android.com/reference/androidx/navigation/NavController#getNavigatorProvider\(\)) method, followed by the [`addNavigator()`](https://developer.android.com/reference/androidx/navigation/NavigatorProvider#addNavigator\(androidx.navigation.Navigator\)) method.

The following code shows an example of adding a `CustomNavigator` object to a `NavController`:

### Kotlin
    
    
    val customNavigator = CustomNavigator()
    navController.navigatorProvider += customNavigator

### Java
    
    
    CustomNavigator customNavigator = new CustomNavigator();
    navController.getNavigatorProvider().addNavigator(customNavigator);

Most `Navigator` classes have a nested destination subclass. This subclass can be used to specify additional attributes unique to your destination. For more information about destination subclasses, see the reference documentation for the appropriate [`Navigator`](https://developer.android.com/reference/androidx/navigation/Navigator) class.

## Additional resources

To learn more about navigation, see the following additional resources.

### Codelabs

  * [ Learn Jetpack Navigation codelab](https://codelabs.developers.google.com/codelabs/android-navigation/index.html?index=..%2F..%2Findex#0)



### Videos

  * [ Android Jetpack: Manage UI navigation with Navigation Controller ](https://www.youtube.com/watch?v=8GCXtCjtg40)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
