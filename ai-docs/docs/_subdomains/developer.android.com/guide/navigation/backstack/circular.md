---
url: https://developer.android.com/guide/navigation/backstack/circular/
title: Circular navigation \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:42.360544+00:00
---

# Circular navigation  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/backstack/circular/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Circular navigation Stay organized with collections  Save and categorize content based on your preferences. 

A clear example of where you need to pop back to a destination is when your navigation is circular. This document outlines that use case.

## Scenario

Imagine your app has three destinations: A, B, and C. It also has actions that lead from A to B, B to C, and C back to A. The corresponding navigation graph appears as follows:

![a demonstration of circular navigation](https://developer.android.com/static/images/topic/libraries/architecture/navigation-getting-started-pop.png)**Figure 1.** A circular navigation graph with three destinations: A, B, and C.

With each navigation action, the `NavController` adds the new destination to the back stack. As such, repeatedly navigating through the flow in the diagram would cause your back stack would to contain multiple sets of each destination: A, B, C, A, B, C, A, B, C.

## Solution

To avoid repetition in your back stack, specify [`popUpTo()`](https://developer.android.com/guide/navigation/backstack#pop) and [`inclusive`](https://developer.android.com/guide/navigation/backstack#pop-back-destination) in your call to `NavController.navigate()` or in your navigation action.

Consider a case where after reaching destination C, the back stack contains one instance of each destination: A, B, C. You need to ensure that you have defined `popUpTo()` and `inclusive` in the action or call to `navigate()` that takes the user from destination C to destination A.

In this case, when the user navigates from destination C back to destination A, the `NavController` also pops up to A. This means that it removes B and C from the stack. With `inclusive = true`, it also pops the first A, effectively clearing the stack.

**Note:** This is similar to calling [`popBackStack()` and passing `inclusive`](https://developer.android.com/guide/navigation/backstack#pop-back-destination).

### Compose implementation

The following is the implementation of the solution for circular `popUpTo()` in Compose:
    
    
    // When creating your `NavGraph` in your `NavHost`.
    composable("c") {
        DestinationC(
            onNavigateToA = {
              navController.navigate("a") {
                popUpTo("a") {
                  inclusive = true
                }
              }
            },
        )
    }
    

### Views implementation

The following is the implementation of the solution for circular `popUpTo` in Views:
    
    
    <fragment
        android:id="@+id/c"
        android:name="com.example.myapplication.C"
        android:label="fragment_c"
        tools:layout="@layout/fragment_c">
    
        **< action
            android:id="@+id/action_c_to_a"
            app:destination="@id/a"
            app:popUpTo="@+id/a"
            app:popUpToInclusive="true"/>**
    </fragment>
    

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
