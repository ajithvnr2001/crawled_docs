---
url: https://developer.android.com/topic/libraries/view-binding/migration/
title: Migrate from Kotlin synthetics to Jetpack view binding \u00a0|\u00a0 Views \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:22.115029+00:00
---

# Migrate from Kotlin synthetics to Jetpack view binding  |  Views  |  Android Developers

> Source: https://developer.android.com/topic/libraries/view-binding/migration/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



#  Migrate from Kotlin synthetics to Jetpack view binding Stay organized with collections  Save and categorize content based on your preferences. 

Kotlin Android Extensions is deprecated, which means that using Kotlin synthetics for view binding is no longer supported. If your app uses Kotlin synthetics for view binding, use this guide to migrate to Jetpack view binding.

If your app doesn't already use Kotlin synthetics for view binding, see [View binding](https://developer.android.com/topic/libraries/view-binding) for basic usage information.

## Update the Gradle file

Like Android Extensions, Jetpack view binding is enabled on a module-by-module basis. For each module that uses view binding, set the `viewBinding` build option to `true` in the module-level `build.gradle` file:

### Groovy
    
    
    android {
        ...
        buildFeatures {
            viewBinding true
        }
    }

### Kotlin
    
    
    android {
        ...
        buildFeatures {
            viewBinding = true
        }
    }

If your app doesn't use [`Parcelable`](https://developer.android.com/reference/android/os/Parcelable) features, remove the line that enables Kotlin Android Extensions:

### Groovy
    
    
    plugins {
      id 'kotlin-android-extensions'
    }

### Kotlin
    
    
    plugins {
        kotlin("android.extensions")
    }

**Note:** If your app uses `Parcelable` features, switch to using the standalone `kotlin-parcelize` Gradle plugin described in [Parcelable implementation generator](https://developer.android.com/kotlin/parcelize).

To learn more about enabling view binding in a module, see [Setup instructions](https://developer.android.com/topic/libraries/view-binding#setup).

## Update activity and fragment classes

With Jetpack view binding, a binding class is generated for each XML layout file that the module contains. The name of this binding class is the name of the XML file in Pascal case with the word _Binding_ added at the end. For example, if the name of the layout file is `result_profile.xml`, the name of the generated binding class is `ResultProfileBinding`.

To use the generated binding classes instead of synthetic properties to reference views, change your activity and fragment classes by doing the following:

  1. Remove all imports from `kotlinx.android.synthetic`.

  2. Inflate an instance of the generated binding class for the activity or fragment to use.

     * For activities, follow the instructions in [Use view binding in activities](https://developer.android.com/topic/libraries/view-binding#activities) to inflate an instance in your activity's [`onCreate()`](https://developer.android.com/reference/kotlin/android/app/Activity#oncreate) method.
     * For fragments, follow the instructions in [Use view binding in fragments](https://developer.android.com/topic/libraries/view-binding#fragments) to inflate an instance in your fragment's [`onCreateView()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#oncreateview) method.
  3. Change all view references to use the binding class instance instead of synthetic properties:



    
    
    // Reference to "name" TextView using synthetic properties.
    name.text = viewModel.nameString
    
    // Reference to "name" TextView using the binding class instance.
    binding.name.text = viewModel.nameString
    

To learn more, see the [Usage](https://developer.android.com/topic/libraries/view-binding#usage) section in the view binding guide.

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [View binding](https://developer.android.com/topic/libraries/view-binding)
  * [Paging library overview](https://developer.android.com/topic/libraries/architecture/paging/v3-overview)
  * [Test your Paging implementation](https://developer.android.com/topic/libraries/architecture/paging/test)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
