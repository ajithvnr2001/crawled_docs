---
url: https://developer.android.com/guide/topics/manifest/attribution-element/
title: <attribution> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:19.669654+00:00
---

# <attribution>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/attribution-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <attribution> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <attribution android:tag="_string_ "
                 android:label="_string resource_">
        ...
    </attribution>

contained in:
    `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)`
description:
    If you develop a multi-purpose app, you can apply this tag to each part of your app when you [audit its data access](https://developer.android.com/privacy-and-security/audit-data-access). This helps you trace data access back to logical parts of your code. 
attributes:
    

`android:tag`
    A literal string that serves as a label for a particular capability of your app.
`android:label`
    A string resource that describes a particular capability of your app.
introduced in:
    API level 31

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-12 UTC."],[],[]] 
