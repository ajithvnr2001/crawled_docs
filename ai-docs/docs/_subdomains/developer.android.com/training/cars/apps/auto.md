---
url: https://developer.android.com/training/cars/apps/auto/
title: Add support for Android Auto to your templated app \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:12.697721+00:00
---

# Add support for Android Auto to your templated app  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/auto/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Add support for Android Auto to your templated app Stay organized with collections  Save and categorize content based on your preferences. 

Read the following information to learn how to make changes to your app's manifest so that Android Auto can discover and interact with your app's `CarAppService`.

## Declare Android Auto support

The [Android Auto host](https://developer.android.com/training/cars/apps/library/glossary-concepts) checks whether the app has declared support for [Android Auto](https://developer.android.com/training/cars#auto). To enable this support, include the following entry in your app's manifest:
    
    
    <application>
        ...
        <meta-data
            android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>
    

That manifest entry refers to another XML file that you create with the path `AppProjectDirectory/app/src/main/res/xml/automotive_app_desc.xml`. In that file, you declare what Android Auto capabilities your app supports.

Apps using the [Android for Cars App Library](https://developer.android.com/reference/androidx/car/app/package-summary) must declare the `template` capability in the `automotive_app_desc.xml` file:
    
    
    <automotiveApp>
        <uses name="template" />
    </automotiveApp>
    

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
