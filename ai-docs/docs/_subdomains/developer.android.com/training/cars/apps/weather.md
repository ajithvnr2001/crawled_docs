---
url: https://developer.android.com/training/cars/apps/weather/
title: Build a weather app \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:11.457600+00:00
---

# Build a weather app  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/weather/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Build a weather app Stay organized with collections  Save and categorize content based on your preferences. 

Weather apps let users see relevant weather information related to their current location or along their route. Weather apps can also provide navigation capabilities – see [Build navigation apps for cars](https://developer.android.com/training/cars/apps/navigation) for more details on building navigation apps.

**Design guidelines:** Refer to [Weather apps](https://developers.google.com/cars/design/create-apps/app-types/weather) for UX guidance specific to weather apps. 

## Declare the weather category in your manifest

Your app must declare the `androidx.car.app.category.WEATHER` [car app category](https://developer.android.com/training/cars/apps#supported-app-categories) in the intent filter of its [`CarAppService`](https://developer.android.com/reference/androidx/car/app/CarAppService).
    
    
    <application>
        ...
       <service
           ...
            android:name=".MyCarAppService"
            android:exported="true">
          <intent-filter>
            <action android:name="androidx.car.app.CarAppService" />
            <category android:name="androidx.car.app.category.WEATHER"/>
          </intent-filter>
        </service>
        ...
    <application>
    

### Declare navigation support

If your app can also be used for navigation, it must also follow the guidance found at [Declare navigation support in your manifest](https://developer.android.com/training/cars/apps/navigation#declare-navigation-support) when declaring its category. The intent filter used to declare your app's category should include both categories:
    
    
    <intent-filter>
      <action android:name="androidx.car.app.CarAppService" />
      <category android:name="androidx.car.app.category.WEATHER"/>
      <category android:name="androidx.car.app.category.NAVIGATION"/>
    </intent-filter>
    

## Implement your app's functionality

To implement your app, refer to [Using the Android for Cars App Library](https://developer.android.com/training/cars/apps) on how Car App Library apps are built. Also, be sure to familiarize yourself with the [Car app quality guidelines for weather apps](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=weather#app_categories), as your app will be reviewed against these guidelines.

### Draw maps

Weather apps can access the [`MapWithContentTemplate`](https://developer.android.com/reference/androidx/car/app/navigation/model/MapWithContentTemplate), which can be used to display lists and other types of content alongside a map that is rendered by your app. See [Draw maps](https://developer.android.com/training/cars/apps#draw-maps) for more details on using this template.

**Important:** Keep the [Weather Functionality](https://developer.android.com/docs/quality-guidelines/car-app-quality?category=weather#weather-functionality) quality guidelines in mind when determining what to render on a map

To access the template, your app needs to declare either the `androidx.car.app.MAP_TEMPLATES` or `androidx.car.app.NAVIGATION_TEMPLATES` permission in its `AndroidManifest.xml` file:
    
    
    <manifest ...>
      ...
      <!-- Use the MAP_TEMPLATES permission if your app doesn't provide navigation functionality -->
      <uses-permission android:name="androidx.car.app.MAP_TEMPLATES"/>
    
      <!-- Use the NAVIGATION_TEMPLATES permission if your app provides navigation functionality -->
      <uses-permission android:name="androidx.car.app.NAVIGATION_TEMPLATES"/>
      ...
    </manifest>
    

**Caution:** Don't include both the `androidx.car.app.MAP_TEMPLATES` and the `androidx.car.app.NAVIGATION_TEMPLATES` permissions in your manifest, or your app will be rejected during review.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
