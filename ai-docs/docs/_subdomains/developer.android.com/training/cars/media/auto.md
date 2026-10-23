---
url: https://developer.android.com/training/cars/media/auto/
title: Add support for Android Auto to your media app \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:00.456711+00:00
---

# Add support for Android Auto to your media app  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/media/auto/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Add support for Android Auto to your media app Stay organized with collections  Save and categorize content based on your preferences. 

You need to make a few changes to your app's manifest so that Android Auto can discover and interact with your app's media browser service.

**Important:** This guide assumes that you have already [built a media browser service](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy) and you want to add support for Android Auto to your existing project. If you are new to app development for cars, see the [Android for Cars overview page](https://developer.android.com/training/cars).

## Declare media support for Android Auto

Use the following manifest entry to declare that your phone app supports Android Auto:
    
    
    <application>
        ...
        <meta-data android:name="com.google.android.gms.car.application"
            android:resource="@xml/automotive_app_desc"/>
        ...
    </application>
    

This manifest entry refers to an XML file that declares what automotive capabilities your app supports. To indicate that you have a media app, add an XML file named `automotive_app_desc.xml` to the `res/xml/` directory in your project. This file should include the following content:
    
    
    <automotiveApp>
        <uses name="media"/>
    </automotiveApp>
    

## Report an Android Auto Media issue

If you run into an issue while developing your media app for Android Auto, you can report it using the [Google Issue Tracker](https://issuetracker.google.com/issues?q=status:open%20componentid:192643). Be sure to fill out all the requested information in the issue template.

[Create a new issue](https://issuetracker.google.com/issues/new?component=192643)

Before filing a new issue, check whether it is already reported in the issues list. You can subscribe to and vote for issues by clicking the star for an issue in the tracker. For more information, see [Subscribing to an Issue](https://developers.google.com/issue-tracker/guides/subscribe#starring_an_issue).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
