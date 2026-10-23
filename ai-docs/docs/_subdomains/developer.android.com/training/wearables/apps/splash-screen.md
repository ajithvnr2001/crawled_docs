---
url: https://developer.android.com/training/wearables/apps/splash-screen/
title: Add a splash screen \u00a0|\u00a0 Wear OS \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:37:10.528468+00:00
---

# Add a splash screen  |  Wear OS  |  Android Developers

> Source: https://developer.android.com/training/wearables/apps/splash-screen/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Wear OS ](https://developer.android.com/training/wearables)



#  Add a splash screen Stay organized with collections  Save and categorize content based on your preferences. 

If your app implements a custom splash screen or uses a launcher theme, migrate your app to the [`SplashScreen`](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen) library, available in Jetpack, to ensure it displays correctly on all Wear OS versions.

See step by step implementation instructions on this page to learn how to add a splash screen using the `SplashScreen` library such that the screen meets [design guidelines](https://developer.android.com/training/wearables/design/launch#branded).

## Add dependencies

Add the following dependency to your app module's `build.gradle` file:

### Groovy
    
    
    dependencies {
        implementation "androidx.core:core-splashscreen:1.2.0"
    }

### Kotlin
    
    
    dependencies {
        implementation("androidx.core:core-splashscreen:1.2.0")
    }

Make sure you are using version `1.0.1` or higher, to get support for default Wear OS dimensions.

## Add a theme

Create a splash screen theme in `res/values/styles.xml`. The parent element depends on the icon's shape:

  * If the icon is round, use `Theme.SplashScreen`.
  * If the icon is a different shape, use `Theme.SplashScreen.IconBackground`.



Use `windowSplashScreenBackground` to fill the background with a single black color. Set the values of `postSplashScreenTheme` to the theme that the Activity should use and `windowSplashScreenAnimatedIcon` to a drawable or animated drawable:
    
    
    <resources>
        <style name="Theme.App" parent="@android:style/Theme.DeviceDefault" />
    
        <style name="Theme.App.Starting" parent="Theme.SplashScreen">
            <!-- Set the splash screen background to black -->
            <item name="windowSplashScreenBackground">@android:color/black</item>
            <!-- Use windowSplashScreenAnimatedIcon to add a drawable or an animated
                 drawable. -->
            <item name="windowSplashScreenAnimatedIcon">@drawable/splash_screen</item>
            <!-- Set the theme of the Activity that follows your splash screen. -->
            <item name="postSplashScreenTheme">@style/Theme.App</item>
        </style>
    </resources>
    
    [styles.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/res/values/styles.xml#L18-L30)

If you use a non-round icon, you need to set a white background color underneath your icon. In this case, use the `Theme.SplashScreen.IconBackground` as parent theme and set the `windowSplashScreenIconBackgroundColor` attribute:
    
    
    <style name="Theme.App.Starting" parent="Theme.SplashScreen">
        <!-- Set a white background behind the splash screen icon. -->
        <item name="windowSplashScreenIconBackgroundColor">@android:color/white</item>
    </style>
    
    [styles.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/res_other/values/styles.xml#L21-L24)

The other attributes are optional.

## Create a drawable for the theme

Splash screen themes requires a drawable to pass into the `windowSplashScreenAnimatedIcon` attribute. For example, you can create it by adding a new file `res/drawable/splash_screen.xml` and using app launcher icon and correct splash screen icon size:
    
    
    <layer-list xmlns:android="http://schemas.android.com/apk/res/android">
        <item
            android:width="@dimen/splash_screen_icon_size"
            android:height="@dimen/splash_screen_icon_size"
            android:drawable="@mipmap/ic_launcher"
            android:gravity="center" />
    </layer-list>
    
    [splash_screen.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/res/drawable/splash_screen.xml#L18-L24)

The splash screen icon size is defined in `res/values/dimens.xml` and differs depending whether the icon is round:
    
    
    <resources>
        <!-- Round app icon can take all of default space -->
        <dimen name="splash_screen_icon_size">48dp</dimen>
    </resources>
    
    [dimens.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/res/values/dimens.xml#L18-L21)

...or non-round and therefore must use the icon background:
    
    
    <resources>
        <!-- Non-round icon with background must use reduced size to fit circle -->
        <dimen name="splash_screen_icon_size">36dp</dimen>
    </resources>
    
    [dimens.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/res_other/values/dimens.xml#L18-L21)

## Specify the theme

In your app's manifest file (`AndroidManifest.xml`), replace the theme of the starting activity -- usually the ones that define a launcher item or are otherwise exported -- to the theme you created in the previous step:
    
    
    <activity
        android:name=".snippets.SplashScreenActivity"
        android:exported="true"
        android:taskAffinity=""
        android:theme="@style/Theme.App.Starting">
        <!-- ... -->
    </activity>
    
    [AndroidManifest.xml](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/AndroidManifest.xml#L58-L70)

## Update your starting activity

Install your splash screen in the starting activity before calling `super.onCreate()` and loading your composable:
    
    
    class SplashScreenActivity : ComponentActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            installSplashScreen()
            super.onCreate(savedInstanceState)
    
            setContent {
                WearApp()
            }
        }
    }
    
    [SplashScreenActivity.kt](https://github.com/android/snippets/blob/0a65e4dc9edd850e8da5a6d1bcccac19289ab691/wear/src/main/java/com/example/wear/snippets/SplashScreenActivity.kt#L25-L34)

## Additional resources

[Learn more about splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen) in general and how you can use them in your app.

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Migrate your splash screen implementation to Android 12 and later](https://developer.android.com/develop/ui/views/launch/splash-screen/migrate)
  * [Splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen)
  * [Integrate App Actions with Android widgets](https://developer.android.com/develop/devices/assistant/widgets)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
