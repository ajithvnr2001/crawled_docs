---
url: https://developer.android.com/training/wearables/compose/
title: Use Jetpack Compose on Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:34:39.539194+00:00
---

# Use Jetpack Compose on Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/compose/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Use Jetpack Compose on Wear OS Stay organized with collections  Save and categorize content based on your preferences. 

Compose for Wear OS Material version 2.5 3

* * *

![Compose code and a preview of the watch face in Android Studio](https://developer.android.com/static/wear/images/components/Compose_hero_m3.png)**Figure 1.** Jetpack Compose for Wear OS

[Compose for Wear OS](https://developer.android.com/jetpack/androidx/releases/wear-compose) is similar to Compose for mobile. However, there are some key differences. This guide walks you through the similarities and differences.

Compose for Wear OS is part of Android Jetpack, and like the other Wear Jetpack libraries you use, it helps you write better code faster. This is our recommended approach for building user interfaces for [Wear OS apps](https://developer.android.com/training/wearables/user-interfaces#apps).

If you are unfamiliar with using the Jetpack Compose toolkit, check out the [Compose pathway](https://developer.android.com/courses/pathways/compose). Many of the development principles for mobile Compose apply to Compose for Wear OS. See [Why Compose](https://developer.android.com/jetpack/compose/why-adopt) for more information on the general advantages of a declarative UI framework. To learn more about Compose for Wear OS, see the [Compose for Wear OS Pathway](https://developer.android.com/courses/pathways/wear-compose) and the [Wear OS samples repository](https://github.com/android/wear-os-samples/tree/main/ComposeStarter#readme) on GitHub.

##  Android skills 

[View on GitHub open_in_new ](https://github.com/android/skills/tree/main/wear/wear-compose-m3)

###  Wear Compose Material 3 

Use an Android skill to help you build using Jetpack Compose on Wear OS, including migrating from earlier versions of Material to Material3.

To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:
    
    
    android skills add wear-compose-m3

## Material Design in Jetpack Compose on Wear OS

Jetpack Compose on Wear OS offers an implementation of [Material 3](https://developer.android.com/design/ui/wear/guides/get-started), which helps you design more engaging app experiences. The [Material Design components](https://developer.android.com/design/ui/wear/guides/components/buttons) on Wear OS are built on top of [Wear Material Theming](https://developer.android.com/design/ui/wear/guides/styles/theme). This theming is a systematic way to customize Material Design and better reflect your product's brand.

## Compatibility

Compose for Wear OS works on watches that support Wear OS 3.0 (API Level 30) and watches that use Wear OS 2.0 (API level 25 and above). Using [version 1.5](https://developer.android.com/jetpack/androidx/releases/wear-compose) of Compose for Wear OS requires using version 1.8 of [androidx.compose](https://developer.android.com/jetpack/androidx/releases/compose) libraries and Kotlin 1.9.0. You can use the [BOM mapping](https://developer.android.com/develop/ui/compose/bom/bom-mapping) and [Compose to Kotlin compatibility map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) to check Compose compatibility. 

## Surfaces

Compose for Wear OS makes building apps on Wear OS easier. For more information see [Apps](https://developer.android.com/training/wearables/apps#building-an-app). Use our built-in components to create user experiences that conform to Wear OS guidelines. For more information about components, see our [design guidance](https://developer.android.com/design/ui/wear/guides/components/buttons).

## Setting up

Using Jetpack Compose with Wear OS is similar to using Jetpack Compose for any other Android project. The main difference is that Jetpack Compose for Wear adds Wear-specific libraries that make it easier to create user interfaces tailored to watches. In some cases those components share the same name as their non-wear counterparts, such as [`androidx.wear.compose.material3.Button`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/Button.composable#Button\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.String,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.wear.compose.material3.ButtonColors,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.wear.compose.material3.SurfaceTransformation,kotlin.Function1\)) and [`androidx.compose.material3.Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Button.composable#Button\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1\)). 

### Create a new app in Android Studio

To create a new project that includes Jetpack Compose, proceed as follows:

  1. If you're in the **Welcome to Android Studio** window, click **Start a new Android Studio project**. If you already have an Android Studio project open, select **File > New > Import Sample** from the menu bar.
  2. Search for **Compose for Wear** and select **Compose for Wear OS Starter.**
  3. In the **Configure your project** window, do the following: 
     1. Set the **Application name**.
     2. Choose the **Project location** for your sample.
  4. Click **Finish**.
  5. Verify that the project's `build.gradle` file is configured correctly, as described in [Gradle properties files](https://developer.android.com/studio/build#properties-files).



Now you're ready to start developing an app using Compose for Wear OS.

### Jetpack Compose toolkit dependencies

To use Jetpack Compose with Wear OS, you'll need to include Jetpack Compose toolkit dependencies in your app's `build.gradle` file. Most of the dependency changes related to Wear OS are in the [top architectural layers](https://developer.android.com/jetpack/compose/layering), surrounded by a red box in the following image.

![4 rectangles. From top to bottom, the rectangles contain 'Material', 'Foundation', 'UI', and 'Runtime'. The top 2 rectangles are surrounded by a red box](https://developer.android.com/static/wear/images/components/ComposeDependencies.png)**Figure 2.** Dependency changes for Wear OS in the Compose architecture

That means many of the dependencies you already use with Jetpack Compose don't change when targeting Wear OS. For example, the UI, runtime, compiler, and animation dependencies remain the same.

However, Wear OS has its own versions of `material` and `material3`, `foundation`, and `navigation` libraries, so check that you're using the proper libraries.

Use the [`WearComposeMaterial`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary) version of APIs where possible. While it's technically possible to use the mobile version of Compose Material, it is not optimized for the unique requirements of Wear OS. In addition, mixing Compose Material with Compose Material for Wear OS can result in unexpected behavior. For example, because each library has its own `MaterialTheme` class, there's the possibility of colors, typography, or shapes being inconsistent if both versions are used.

The following table outlines the dependency differences between Wear OS and Mobile:

**Wear OS Dependency**   
(androidx.wear.*)  | **Comparison** | **Mobile Dependency**   
(androidx.*)   
---|---|---  
[androidx.wear.compose:compose-material3](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary) | **_instead of_** | androidx.compose.material:material3   
[androidx.wear.compose:compose-navigation](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary) | **_instead of_** | androidx.navigation:navigation-compose   
[androidx.wear.compose:compose-foundation](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/package-summary) | **_in addition to_** | androidx.compose.foundation:foundation   
**Note:** Other non-mobile material dependencies can be used, such as material ripple and material icons extended.

The following snippet shows an example `build.gradle` file that includes these dependencies:

### Kotlin
    
    
    dependencies {
    
        val composeBom = platform("androidx.compose:compose-bom:2026.09.00")
    
        // General compose dependencies
        implementation(composeBom)
        implementation("androidx.activity:activity-compose:1.13.0")
        implementation("androidx.compose.ui:ui-tooling-preview:1.12.1")
        // Other compose dependencies
    
        // Compose for Wear OS dependencies
        implementation("androidx.wear.compose:compose-material3:1.7.1")
    
        // Foundation is additive, so you can use the mobile version in your Wear OS app.
        implementation("androidx.wear.compose:compose-foundation:1.7.1")
    
        // Wear OS preview annotations
        implementation("androidx.wear.compose:compose-ui-tooling:1.7.1")
    
        // If you are using Compose Navigation, use the Wear OS version (NOT THE MOBILE VERSION).
        // Uncomment the line below and update the version number.
        // implementation("androidx.wear.compose:compose-navigation:1.7.1")
    
        // Testing
        testImplementation("junit:junit:4.13.2")
        androidTestImplementation("androidx.test.ext:junit:1.1.3")
        androidTestImplementation("androidx.test.espresso:espresso-core:3.4.0")
        androidTestImplementation("androidx.compose.ui:ui-test-junit4:1.0.3")
        debugImplementation("androidx.compose.ui:ui-tooling:1.4.1")
    
    }

## Feedback

Try out Compose for Wear OS and use the [issue tracker](https://issuetracker.google.com/issues/new?component=1077552&template=1598429&pli=1) to provide suggestions and feedback.

Join the [#compose-wear channel](https://surveys.jetbrains.com/s3/kotlin-slack-sign-up) on Kotlin Slack to connect with developer community and let us know your experience.

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Resources in Compose](https://developer.android.com/develop/ui/compose/resources)
  * [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3)
  * [Get Started with Jetpack Compose](https://developer.android.com/develop/ui/compose/documentation)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 

  * [ ![X](https://developer.android.com/_static/android/images/logo-x.svg) X  ](https://x.com/AndroidDev)

Follow @AndroidDev on X

  * [ ![YouTube](https://www.gstatic.com/images/icons/material/product/2x/youtube_48dp.png) YouTube  ](https://www.youtube.com/user/androiddevelopers)

Check out Android Developers on YouTube

  * [ ![LinkedIn](https://developer.android.com/_static/android/images/logo-linkedin.svg) LinkedIn  ](https://www.linkedin.com/showcase/androiddev)

Connect with the Android Developers community on LinkedIn




  * ### More Android

    * [ Android ](https://www.android.com)
    * [ Android for Enterprise ](https://www.android.com/enterprise/)
    * [ Security ](https://www.android.com/security-center/)
    * [ Source ](https://source.android.com)
    * [ News ](https://developer.android.com/news)
    * [ Blog ](https://android-developers.googleblog.com/)
    * [ Podcasts ](https://developer.android.com/podcasts)
  * ### Discover

    * [ Gaming ](https://developer.android.com/games)
    * [ Machine Learning ](https://developer.android.com/ml)
    * [ Health & Fitness ](https://developer.android.com/health-and-fitness)
    * [ Camera & Media ](https://developer.android.com/media)
    * [ Privacy ](https://developer.android.com/privacy)
    * [ 5G ](https://developer.android.com/training/connectivity/5g)
  * ### Android Devices

    * [ Large screens ](https://developer.android.com/large-screens)
    * [ Wear OS ](https://developer.android.com/wear)
    * [ ChromeOS devices ](https://developer.android.com/chrome-os)
    * [ Android for cars ](https://developer.android.com/cars)
    * [ Android TV ](https://developer.android.com/tv)
  * ### Releases

    * [ Android 17 ](https://developer.android.com/about/versions/17)
    * [ Android 16 ](https://developer.android.com/about/versions/16)
    * [ Android 15 ](https://developer.android.com/about/versions/15)
    * [ Android 14 ](https://developer.android.com/about/versions/14)
    * [ Android 13 ](https://developer.android.com/about/versions/13)
    * [ Android 12 ](https://developer.android.com/about/versions/12)
    * [ Android 11 ](https://developer.android.com/about/versions/11)
  * ### Documentation and Downloads

    * [ Android Studio guide ](https://developer.android.com/studio/intro)
    * [ Developers guides ](https://developer.android.com/guide)
    * [ API reference ](https://developer.android.com/reference)
    * [ Download Studio ](https://developer.android.com/studio)
    * [ Android NDK ](https://developer.android.com/ndk)
  * ### Support

    * [ Report platform bug ](https://issuetracker.google.com/issues/new?component=190923&template=841312)
    * [ Report documentation bug ](https://issuetracker.google.com/issues/new?component=192697)
    * [ Google Play support ](https://support.google.com/googleplay/android-developer)
    * [ Join research studies ](https://g.co/userresearch/androiddeveloperfooter)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/android/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com)
  * [ Chrome ](https://developer.chrome.com/home)
  * [ Firebase ](https://firebase.google.com)
  * [ Google Cloud Platform ](https://cloud.google.com)
  * [ All products ](https://developers.google.com/products/)



  * [ Privacy ](https://policies.google.com/privacy)
  * [ License ](https://developer.android.com/license)
  * [ Brand guidelines ](https://developer.android.com/distribute/marketing-tools/brand-guidelines)
  * Manage cookies 
  * Get news and tips by email [ Subscribe ](https://developer.android.com/updates)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


