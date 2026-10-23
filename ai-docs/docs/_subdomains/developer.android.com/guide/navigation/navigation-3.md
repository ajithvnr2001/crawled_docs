---
url: https://developer.android.com/guide/navigation/navigation-3/
title: Navigation 3 \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:47.707073+00:00
---

# Navigation 3  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/navigation/navigation-3/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  Navigation 3 Stay organized with collections  Save and categorize content based on your preferences. 

##  Android skills 

[View on GitHub open_in_new ](https://github.com/android/skills/tree/main/navigation/navigation-3)

###  Jetpack Navigation 3 

Use an Android skill to help you build using Jetpack Navigation 3.

To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:
    
    
    android skills add navigation-3

Navigation 3 is a navigation library designed to work with Compose. With Navigation 3, you have full control over your back stack, and you navigate between destinations by adding and removing items from a list. It creates a flexible app navigation system by providing:

  * Conventions for modeling a back stack, where each entry on the back stack represents content that the user has navigated to
  * A UI that automatically updates with back stack changes (including [animations](https://developer.android.com/guide/navigation/navigation-3/animate-destinations))
  * A scope for items in the back stack, allowing state to be retained while an item is in the back stack
  * An adaptive layout system that allows multiple destinations to be displayed at the same time, enabling seamless switching between those layouts
  * A mechanism for content to communicate with its parent layout ([metadata](https://developer.android.com/guide/navigation/navigation-3/metadata))
  * Inter-destination communication to [return results](https://developer.android.com/guide/navigation/navigation-3/return-results) between screens



At a high level, you implement Navigation 3 in the following ways:

  1. Define the content that users can navigate to in your app, each with a unique key, and add a function to resolve that key to the content. See [Resolve keys to content](https://developer.android.com/guide/navigation/navigation-3/basics#resolve-keys).
  2. Create a back stack that keys are pushed onto and removed as users navigate your app. See [Create a back stack](https://developer.android.com/guide/navigation/navigation-3/basics#create-back).
  3. Use a [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay.composable) to display your app's back stack. Whenever the back stack changes, it updates the UI to display relevant content. See [Display the back stack](https://developer.android.com/guide/navigation/navigation-3/basics#display-back).
  4. Modify `NavDisplay`'s [scene strategies](https://developer.android.com/guide/navigation/navigation-3/custom-layouts) as needed to support adaptive layouts and different platforms.
  5. [Support deep links](https://developer.android.com/guide/navigation/navigation-3/deep-links) to navigate directly to destinations.



You can see the [full source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:navigation3/) for Navigation 3 on AOSP.

## Improvements upon Jetpack Navigation

Navigation 3 improves upon the original Jetpack Navigation API in the following ways:

  * Provides a simpler integration with Compose
  * Offers you full control of the back stack
  * Makes it possible to create layouts that can read more than one destination from the back stack at the same time, allowing them to adapt to changes in window size and other inputs.



Read more about Navigation 3's principles and API design choices in the [announcement blog post](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html).

## Code samples

The [recipes repository](https://github.com/android/nav3-recipes) contains examples of how to use the Navigation 3 building blocks to solve common navigation challenges.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
