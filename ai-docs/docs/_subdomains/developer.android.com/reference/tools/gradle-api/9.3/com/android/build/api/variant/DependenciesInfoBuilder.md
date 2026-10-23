---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder/
title: DependenciesInfoBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:35:17.143511+00:00
---

# DependenciesInfoBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# DependenciesInfoBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/DependenciesInfoBuilder.kt+class:com.android.build.api.variant.DependenciesInfoBuilder)

Added in 7.0.0
    
    
    interface [DependenciesInfoBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder)

* * *

Interface for component builder that specifies whether to include SDK dependency information in APKs and Bundles for the variant

Including dependency information in your APK or Bundle allows Google Play to ensure that any third-party software your app uses complies with [Google Play's Developer Program Policies](https://support.google.com/googleplay/android-developer/topic/9858052). For more information, see the Play Console support page [Using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880).

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[includeInApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder#includeInApk\(\))` Set to `true` if information about SDK dependencies of an APK should be added to its signature block, `false` otherwise.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[includeInBundle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder#includeInBundle\(\))` Set to `true` if information about SDK dependencies of an App Bundle should be added to it, `false` otherwise.  
  
## Public properties

### includeInApk

Added in 8.1.0
    
    
    var [includeInApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder#includeInApk\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if information about SDK dependencies of an APK should be added to its signature block, `false` otherwise.

Default value will match `[com.android.build.api.dsl.DependenciesInfo.includeInApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependenciesInfo#includeInApk\(\))`

It's not safe to read this value. Use `[DependenciesInfo.includedInApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfo#includedInApk\(\))` instead (found on `[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariant)`

### includeInBundle

Added in 8.1.0
    
    
    var [includeInBundle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfoBuilder#includeInBundle\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Set to `true` if information about SDK dependencies of an App Bundle should be added to it, `false` otherwise.

Default value will match `[com.android.build.api.dsl.DependenciesInfo.includeInBundle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/DependenciesInfo#includeInBundle\(\))`

It's not safe to read this value. Use `[DependenciesInfo.includedInBundle](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/DependenciesInfo#includedInBundle\(\))` instead (found on `[ApplicationVariant](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/ApplicationVariant)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
