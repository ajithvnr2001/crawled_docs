---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo/
title: DependenciesInfo \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:51:58.381634+00:00
---

# DependenciesInfo  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DependenciesInfo

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/DependenciesInfo.kt+class:com.android.build.api.dsl.DependenciesInfo)

Added in 4.2.0
    
    
    interface [DependenciesInfo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo)

* * *

DSL object to specify whether to include SDK dependency information in APKs and Bundles.

Including dependency information in your APK or Bundle allows Google Play to ensure that any third-party software your app uses complies with [Google Play's Developer Program Policies](https://support.google.com/googleplay/android-developer/topic/9858052). For more information, see the Play Console support page [Using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880).

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[includeInApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo#includeInApk\(\))` If false, information about SDK dependencies of an APK will not be added to its signature block.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[includeInBundle](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo#includeInBundle\(\))` If false, information about SDK dependencies of an App Bundle will not be added to it.  
  
## Public properties

### includeInApk

Added in 4.2.0
    
    
    var [includeInApk](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo#includeInApk\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

If false, information about SDK dependencies of an APK will not be added to its signature block.

### includeInBundle

Added in 4.2.0
    
    
    var [includeInBundle](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/DependenciesInfo#includeInBundle\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

If false, information about SDK dependencies of an App Bundle will not be added to it.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
