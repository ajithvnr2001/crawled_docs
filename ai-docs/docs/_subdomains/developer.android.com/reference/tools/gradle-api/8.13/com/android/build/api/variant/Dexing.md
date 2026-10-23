---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing/
title: Dexing \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:38:48.130123+00:00
---

# Dexing  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Dexing

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Dexing.kt+class:com.android.build.api.variant.Dexing)

Added in 8.3.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [Dexing](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing)

* * *

Settings related to how dex files are produced.

To change any of these settings :
    
    
    androidComponents {  
        beforeVariants { variant ->  
            variant.dexing...  
        }  
    }

## Summary

### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isMultiDexEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#isMultiDexEnabled\(\))`  
`[RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  `[multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#multiDexKeepFile\(\))` If set, will point to a text file that specifies additional classes that will be compiled into the main dex file.  
`[RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)` |  `[multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#multiDexKeepProguard\(\))` If set, will point to the multiDex proguard file  
  
## Public properties

### isMultiDexEnabled

Added in 8.3.1
    
    
    val [isMultiDexEnabled](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#isMultiDexEnabled\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### multiDexKeepFile

Added in 8.3.1
    
    
    val [multiDexKeepFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#multiDexKeepFile\(\)): [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)

If set, will point to a text file that specifies additional classes that will be compiled into the main dex file.

Note that the `[GeneratesApkBuilder.enableMultiDex](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` must be set to true for this property to be used.

### multiDexKeepProguard

Added in 8.3.1
    
    
    val [multiDexKeepProguard](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/Dexing#multiDexKeepProguard\(\)): [RegularFileProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFileProperty.html)

If set, will point to the multiDex proguard file

Note that the `[GeneratesApkBuilder.enableMultiDex](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/variant/GeneratesApkBuilder#enableMultiDex\(\))` must be set to true for this property to be used.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
