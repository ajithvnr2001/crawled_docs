---
url: https://developer.android.com/guide/topics/manifest/meta-data-element/
title: <meta-data> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:22.348362+00:00
---

# <meta-data>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/meta-data-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <meta-data> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <meta-data android:name="_string_ "
               android:resource="_resource specification_"
               android:value="_string_ " />

contained in:
    `[<activity>](https://developer.android.com/guide/topics/manifest/activity-element)`   
`[<activity-alias>](https://developer.android.com/guide/topics/manifest/activity-alias-element)`   
`[<application>](https://developer.android.com/guide/topics/manifest/application-element)`   
`[<provider>](https://developer.android.com/guide/topics/manifest/provider-element)`   
`[<receiver>](https://developer.android.com/guide/topics/manifest/receiver-element)`   
`[<service>](https://developer.android.com/guide/topics/manifest/service-element)`
description:
    A name-value pair for an item of additional, arbitrary data that can be supplied to the parent component. A component element can contain any number of `<meta-data>` subelements. The values from all of them are collected in a single `[Bundle](https://developer.android.com/reference/android/os/Bundle)` object and made available to the component as the `[PackageItemInfo.metaData](https://developer.android.com/reference/android/content/pm/PackageItemInfo#metaData)` field. 

Specify ordinary values through the `[value](https://developer.android.com/guide/topics/manifest/meta-data-element#val)` attribute. To assign a resource ID as the value, use the `[resource](https://developer.android.com/guide/topics/manifest/meta-data-element#rsrc)` attribute instead. For example, the following code assigns whatever value is stored in the `@string/kangaroo` resource to the `zoo` name:
    
    
    <meta-data android:name="zoo" android:value="@string/kangaroo" />

On the other hand, using the `resource` attribute assigns `zoo` the numeric ID of the resource, not the value stored in the resource:
    
    
    <meta-data android:name="zoo" android:resource="@string/kangaroo" />

We highly recommend that you avoid supplying related data as multiple separate `<meta-data>` entries. Instead, if you have complex data to associate with a component, store it as a resource and use the `resource` attribute to inform the component of its ID.

attributes:
    

`android:name`
    A unique name for the item. To keep the name unique, use a Java-style naming convention, such as "`com.example.project.activity.fred`".
`android:resource`
    A reference to a resource. The ID of the resource is the value assigned to the item. The ID is retrieved from the meta-data `Bundle` using the `[Bundle.getInt()](https://developer.android.com/reference/android/os/BaseBundle#getInt\(java.lang.String\))` method.
`android:value`
    The value assigned to the item. The data types that can be assigned as values and the `Bundle` methods that components use to retrieve those values are listed in the following table:   
Type | Bundle method  
---|---  
String: use double backslashes (`\\`) to escape characters, such as `\\n` for a new line and `\\uxxxxx` for a Unicode character | `[getString()](https://developer.android.com/reference/android/os/BaseBundle#getString\(java.lang.String\))`  
Integer: for example, `100` | `[getInt()](https://developer.android.com/reference/android/os/BaseBundle#getInt\(java.lang.String\))`  
Boolean: either `true` or `false` | `[getBoolean()](https://developer.android.com/reference/android/os/BaseBundle#getBoolean\(java.lang.String\))`  
Color: in the form `#rgb`, `#argb`, `#rrggbb`, or `#aarrggbb` | `[getInt()](https://developer.android.com/reference/android/os/BaseBundle#getInt\(java.lang.String\))`  
Float: for example, `1.23` | `[getFloat()](https://developer.android.com/reference/android/os/Bundle#getFloat\(java.lang.String\))`  
introduced in:
    API level 1

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
