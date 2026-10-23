---
url: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library/
title: Create Baseline Profiles for a library \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:01.873341+00:00
---

# Create Baseline Profiles for a library  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile-library/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Create Baseline Profiles for a library Stay organized with collections  Save and categorize content based on your preferences. 

To create Baseline Profiles for a library, use the [Baseline Profile Gradle plugin](https://developer.android.com/topic/performance/baselineprofiles/configure-baselineprofiles).

There are three modules involved in creating Baseline Profiles for a library:

  * Sample app module: contains the sample app that uses your library.
  * Library module: the module you want to generate the profile for.
  * Baseline Profile module: the test module that generates the Baseline Profiles.



To generate a Baseline Profile for a library, perform the following steps:

  1. Create a new `com.android.test` module—for example, `:baseline-profile`.
  2. Configure the `build.gradle.kts` file for the `:baseline-profile` module. [The configuration is essentially the same as for an app](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile#create-new-profile-plugin), but make sure to set the `targetProjectPath` to the sample app module.
  3. Create a Baseline Profile test in the `:baseline-profile` test module. This needs to be specific to the sample app and must use all the functionalities of the library.
  4. Update the configuration in `build.gradle.ktss` file in the library module, say `:library`.
     1. Apply the plugin `androidx.baselineprofile`.
     2. Add a `baselineProfile` dependency to the `:baseline-profile` module.
     3. Apply the consumer plugin configuration you want, as shown in the following example.

### Kotlin
    
    plugins {
        id("com.android.library")
        id("androidx.baselineprofile")
    }
    
    android { ... }
    
    dependencies {
        ...
        // Add a baselineProfile dependency to the `:baseline-profile` module.
        baselineProfile(project(":baseline-profile"))
    }
    
    // Baseline Profile Gradle plugin configuration.
    baselineProfile {
    
        // [Filters](https://developer.android.com/topic/performance/baselineprofile/configure-baselineprofiles#filter-profile-rules) the generated profile rules. 
        // This example keeps the classes in the `com.library` package all its subpackages.
        filter {
            include "com.mylibrary.**"
        }
    }

### Groovy
    
    plugins {
        id 'com.android.library'
        id 'androidx.baselineprofile'
    }
    
    android { ... }
    
    dependencies {
        ...
        // Add a baselineProfile dependency to the `:baseline-profile` module.
        baselineProfile ':baseline-profile'
    }
    
    // Baseline Profile Gradle plugin configuration.
    baselineProfile {
    
        // [Filters](https://developer.android.com/topic/performance/baselineprofile/configure-baselineprofiles#filter-profile-rules) the generated profile rules. 
        // This example keeps the classes in the `com.library` package all its subpackages.
        filter {
            include 'com.mylibrary.**'
        }
    }

  5. Add the `androidx.baselineprofile` plugin to the `build.gradle.kts` file in the app module `:sample-app`. 

### Kotlin
         
         plugins {
             ...
             id("androidx.baselineprofile")
         }

### Groovy
         
         plugins {
             ...
             id 'androidx.baselineprofile'
         }

  6. Generate the profile by running the following code: `./gradlew :library:generateBaselineProfile`.



At the end of the generation task, the Baseline Profile is stored at `library/src/main/generated/baselineProfiles`.

[ Previous arrow_back  Create Baseline Profiles  ](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)

[ Next Configure Baseline Profile generation  arrow_forward  ](https://developer.android.com/topic/performance/baselineprofiles/configure-baselineprofiles)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
