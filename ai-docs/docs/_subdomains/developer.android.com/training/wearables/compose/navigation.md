---
url: https://developer.android.com/training/wearables/compose/navigation/
title: Navigation with Compose for Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:08.008280+00:00
---

# Navigation with Compose for Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/compose/navigation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Navigation with Compose for Wear OS Stay organized with collections  Save and categorize content based on your preferences. 

Compose for Wear OS Material version 2.5 3

* * *

The [Navigation component](https://developer.android.com/guide/navigation) in Android Jetpack provides support for Jetpack Compose applications. You can navigate between composables while taking advantage of the Navigation component's infrastructure and features.

This page describes the differences with Jetpack Navigation on Compose for Wear OS.

**Note:** If you are not familiar with the Navigation component, review the [Navigating with Compose](https://developer.android.com/jetpack/compose/navigation) resources before continuing.

## Setup

Use the following dependency in your app module's build.gradle file:

### Kotlin
    
    
    dependencies {
        def wear_compose_version = "1.7.1"
        implementation "androidx.wear.compose:compose-navigation:$wear_compose_version"
    }

This is used **instead** of the `androidx.navigation:navigation-compose` artifact because it provides alternative implementations specific to Wear OS.

## Create a navigation controller, host and graph

Navigating with Compose for Wear OS requires the same three components needed on non-Wear OS apps: the navigation controller, host and graph.

Use [`rememberSwipeDismissableNavController()`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary#rememberSwipeDismissableNavController\(\)) to create an instance of `WearNavigator`, an implementation of `NavController` suitable for Wear OS applications:
    
    
    val navController = rememberSwipeDismissableNavController()
    
    [Navigation.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/navigation/Navigation.kt#L47-L47)

The [`NavController`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) is the primary API used to navigate in Compose applications. It controls navigating between composables in the navigation host which, on Wear OS, is [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary#SwipeDismissableNavHost\(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,androidx.wear.compose.navigation.SwipeDismissableNavHostState,kotlin.String,kotlin.Function1\)).
    
    
    val navController = rememberSwipeDismissableNavController()
    SwipeDismissableNavHost(
        navController = navController,
        startDestination = "message_list"
    ) {
        // TODO: build navigation graph
    }
    
    [Navigation.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/navigation/Navigation.kt#L54-L60)

Like the [`NavHost` composable](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#NavHost\(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,kotlin.String,kotlin.Function1\)), it takes a reference to the navigation controller, the route for the start destination, and the builder for the navigation graph which is shown here as a trailing lambda.

The start destination must be provided in the navigation graph builder, along with all other destinations that should be navigable with the navigation controller.

In your Wear OS app, declare [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable#SwipeDismissableNavHost\(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState\)) as a content of the [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) to support top-level components like time, scroll or position indicator, and page indicator. Use a [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold\(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1\)) object above the [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable#SwipeDismissableNavHost\(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState\)) and the [`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold\(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2\)) at the screen level to add a `TimeText` object to the screen by default and to make sure it animates correctly when navigating between screens. Additionally, `ScreenScaffold` adds a `PositionIndicator` for scrollable content. 
    
    
        AppScaffold {
            val navController = rememberSwipeDismissableNavController()
            SwipeDismissableNavHost(
                navController = navController,
                startDestination = "message_list"
            ) {
                composable("message_list") {
                    MessageList(onMessageClick = { id ->
                        navController.navigate("message_detail/$id")
                    })
                }
                composable("message_detail/{id}") {
                    MessageDetail(id = it.arguments?.getString("id")!!)
                }
            }
        }
    }
    
    // Implementation of one of the screens in the navigation
    @Composable
    fun MessageDetail(id: String) {
        // .. Screen level content goes here
        val scrollState = rememberTransformingLazyColumnState()
        val transformationSpec = rememberTransformationSpec()
    
        ScreenScaffold(
            scrollState = scrollState,
        ) { contentPadding ->
            // Screen content goes here
            // ...
    
    [Navigation.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/wear/src/main/java/com/example/wear/snippets/m3/navigation/Navigation.kt#L67-L124)

To learn more about Jetpack Navigation, see [Navigating with Compose](https://developer.android.com/jetpack/compose/navigation) or take the [Jetpack Compose Navigation code lab](https://developer.android.com/codelabs/jetpack-compose-navigation).

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Migrate Jetpack Navigation to Navigation Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/navigation)
  * [Navigation with Compose](https://developer.android.com/guide/navigation#framework-options)
  * [Navigate between screens with Compose](https://developer.android.com/codelabs/basic-android-kotlin-compose-navigation)



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


