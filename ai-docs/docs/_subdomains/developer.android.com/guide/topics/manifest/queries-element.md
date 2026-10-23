---
url: https://developer.android.com/guide/topics/manifest/queries-element/
title: <queries> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:25.907887+00:00
---

# <queries>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/queries-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <queries> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <queries>
        <package android:name="_string_ " />
        <intent>
            ...
        </intent>
        <provider android:authorities="_list_ " />
        ...
    </queries>

contained in:
    `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)`
description:
    

Specifies the set of other apps that an app intends to interact with. These other apps are specified by package name, by intent signature, or by provider authority, as described in the following sections on this page.

**Note:** Some packages are [visible automatically](https://developer.android.com/training/package-visibility/automatic). Your app always sees these packages in its queries for other installed apps. To view other packages, declare your app's need for increased package visibility using the `<queries>` element.

Learn more about how to use the `<queries>` element in [Package visibility filtering on Android](https://developer.android.com/training/package-visibility).

child elements:
    

`<package>`
    

Specifies a single app that your app intends to access. This other app might integrate with your app, or your app might use services that the other app provides.

attributes:

`android:name`
    **Required.** Specifies the package name of the other app.
`<intent>`
    

Specifies an [intent filter signature](https://developer.android.com/training/basics/intents/filters). Your app can discover other apps that have matching [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) elements.

**Note:** There are some restrictions on the options that you can include in this `<intent>` element, compared to a typical intent filter signature. Learn more about these restrictions in [Packages that match an intent filter signature](https://developer.android.com/training/package-visibility/declaring#intent-filter-signature).

`<provider>`
    

Specifies one or more [content provider authorities](https://developer.android.com/guide/topics/providers/content-provider-basics#ContentURIs). Your app can discover other apps whose content providers use the specified authorities.

**Note:** There are some restrictions on the options that you can include in this `<provider>` element, compared to a typical [`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element) manifest element. Usually, you only specify the `android:authorities` attribute.

introduced in:
    API level 30
see also:
    [Package visibility filtering on Android](https://developer.android.com/training/package-visibility)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
