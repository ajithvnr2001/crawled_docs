---
url: https://developer.android.com/guide/topics/manifest/permission-tree-element/
title: <permission-tree> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:23.397172+00:00
---

# <permission-tree>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/permission-tree-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <permission-tree> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <permission-tree android:icon="_drawable resource_"
                     android:label="_string resource_"
                     android:name="_string_ " />

contained in:
    `[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)`
description:
    Declares the base name for a tree of permissions. The application takes ownership of all names within the tree. It can dynamically add new permissions to the tree by calling `[PackageManager.addPermission()](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))`. Names within the tree are separated by periods ('`.`'). For example, if the base name is `com.example.project.taxes`, permissions like the following might be added: 

`com.example.project.taxes.CALCULATE`   
`com.example.project.taxes.deductions.STORE_RECEIPTS`   
`com.example.project.taxes.deductions.ACCESS_RECORDS`

This element doesn't declare a permission itself, only a namespace in which permissions can be placed. For more information about declaring permissions, see the `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)` element. 

attributes:
    

`android:icon`
    An icon representing all the permissions in the tree. This attribute must be set as a reference to a drawable resource containing the image definition.
`android:label`
    A user-readable name for the group. As a convenience, the label can be directly set as a raw string during development. However, when the application is ready to be published, set it as a reference to a string resource, so that it can be localized like other strings in the user interface.
`android:name`
    The name at the base of the permission tree. It serves as a prefix to all permission names in the tree. Use Java-style scoping so that the name is unique. The name must have more than two period-separated segments in its path. For example, `com.example.base` is OK, but `com.example` isn't.
introduced in:
    API level 1
see also:
    `[<permission>](https://developer.android.com/guide/topics/manifest/permission-element)`   
`[<permission-group>](https://developer.android.com/guide/topics/manifest/permission-group-element)`   
`[<uses-permission>](https://developer.android.com/guide/topics/manifest/uses-permission-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
