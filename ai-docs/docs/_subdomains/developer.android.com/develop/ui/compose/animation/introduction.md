---
url: https://developer.android.com/develop/ui/compose/animation/introduction/
title: Animations in Compose \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:40.111340+00:00
---

# Animations in Compose  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/compose/animation/introduction/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



Stay organized with collections  Save and categorize content based on your preferences. 

###  [ Animations in Compose ](https://developer.android.com/develop/ui/compose/animation/quick-guide)

Animations are essential in a modern mobile app in order to realize a smooth and understandable user experience. 

[Quick guide](https://developer.android.com/develop/ui/compose/animation/quick-guide)

##  Animation modifiers and composables 

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/animated_visibility_column.gif)](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility)

###  [ Animate appearance and disappearance ](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility)

The `AnimatedVisibility` composable allows you to hide or show content easily. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedvisibility)

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/animated_content_size.gif)](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animateContentSize)

###  [ Animate content size changes ](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animateContentSize)

Use `animateContentSize()` to achieve automatic size change animations. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animateContentSize)

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/animated_content_slower.gif)](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent)

###  [ Animate between different composables ](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent)

Use `AnimatedContent` to animate between composables that have different content. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent)

##  Value-based animations 

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/animated_padding.gif)](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state)

###  [ Animate a single value ](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state)

Use `animate*AsState` functions to animate an individual property, such as opacity. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/value-based#animate-as-state)

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/multiple_properties.gif)](https://developer.android.com/develop/ui/compose/animation/quick-guide#concurrent-animations)

###  [ Animate multiple values together ](https://developer.android.com/develop/ui/compose/animation/quick-guide#concurrent-animations)

Use `Transition` to animate multiple values at once. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/quick-guide#concurrent-animations)

[ ![](https://developer.android.com/static/develop/ui/compose/images/animations/animated_forever.gif)](https://developer.android.com/develop/ui/compose/animation/value-based#rememberinfinitetransition)

###  [ Animate properties indefinitely ](https://developer.android.com/develop/ui/compose/animation/value-based#rememberinfinitetransition)

Use `InfiniteTransition` to animate properties continuously. 

[Learn more](https://developer.android.com/develop/ui/compose/animation/value-based#rememberinfinitetransition)

[ ![](https://developer.android.com/static/images/picto-icons/interoperable.svg) ](https://developer.android.com/develop/ui/compose/animation/customize)

###  [ Customize your animations ](https://developer.android.com/develop/ui/compose/animation/customize)

Learn how to customize your animations duration, easing curve and spring configuration. 

[Customize](https://developer.android.com/develop/ui/compose/animation/customize)

[ ![](https://developer.android.com/static/images/picto-icons/bug-2.svg) ](https://developer.android.com/develop/ui/compose/animation/testing)

###  [ Test animations ](https://developer.android.com/develop/ui/compose/animation/testing)

Learn how to write tests for your animations. 

[Testing](https://developer.android.com/develop/ui/compose/animation/testing)

[ ![](https://developer.android.com/static/images/picto-icons/spanner.svg) ](https://developer.android.com/develop/ui/compose/animation/tooling)

###  [ Android Studio Tooling ](https://developer.android.com/develop/ui/compose/animation/tooling)

Learn all about how to preview your animations in Android Studio. 

[Tooling](https://developer.android.com/develop/ui/compose/animation/tooling)

[ Next Choose an animation API  arrow_forward  ](https://developer.android.com/develop/ui/compose/animation/choose-api)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2024-07-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-01 UTC."],[],[]] 
