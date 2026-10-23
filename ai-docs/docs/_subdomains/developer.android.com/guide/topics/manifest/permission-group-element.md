---
url: https://developer.android.com/guide/topics/manifest/permission-group-element/
title: <permission-group> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:23.502212+00:00
---

# <permission-group>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/permission-group-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <permission-group> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <permission-group android:description="_string resource_"
                      android:icon="_drawable resource_"
                      android:label="_string resource_"
                      android:name="_string_ " />

contained in:
    `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)`
description:
    Declares a name for a logical grouping of related permissions. Individual permissions join the group through the `permissionGroup` attribute of the `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)` element. Members of a group are presented together in the user interface. 

This element doesn't declare a permission itself, only a category in which permissions can be placed. For information about declaring permissions and assigning them to groups, see the `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)` element. 

attributes:
    

`android:description`
    User-readable text that describes the group. The text is longer and more explanatory than the label. This attribute must be set as a reference to a string resource. Unlike the `label` attribute, it can't be a raw string.
`android:icon`
    An icon representing the permission. This attribute must be set as a reference to a drawable resource containing the image definition.
`android:label`
    A user-readable name for the group. As a convenience, the label can be directly set as a raw string while you're developing the application. However, when the application is ready to be published, set it as a reference to a string resource, so that it can be localized like other strings in the user interface.
`android:name`
    The name of the group. This is the name that can be assigned to a `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)` element's `[android:permissionGroup](https://developer.android.com/guide/topics/manifest/permission-element#pgroup)` attribute.
introduced in:
    API level 1
see also:
    `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)`   
`[<permission-tree>](https://developer.android.com/guide/topics/manifest/permission-tree-element)`   
`[<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
