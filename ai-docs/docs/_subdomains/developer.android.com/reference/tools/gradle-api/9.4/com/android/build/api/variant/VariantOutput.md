---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput/
title: VariantOutput \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:03:19.967757+00:00
---

# VariantOutput  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantOutput

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantOutput.kt+class:com.android.build.api.variant.VariantOutput)

Added in 4.2.0
    
    
    interface [VariantOutput](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput) : [VariantOutputConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration)

* * *

Defines a variant output.

This only applies to APKs as AARs and Bundles (AABs) do not support multiple outputs.

See https://developer.android.com/studio/build/configure-apk-splits.html for more information on multiple APK support.

See also  
---  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/Splits)` |   
  
## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>` |  `[enabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#enabled\(\))` Flag controlling whether the output is enabled.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[outputFileName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#outputFileName\(\))` The output file name for this Variant.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[versionCode](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#versionCode\(\))` The version code for this output.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[versionName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#versionName\(\))` The version name for this output.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.VariantOutputConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration) | `[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/FilterConfiguration)>` |  `[filters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration#filters\(\))` The list of `[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/FilterConfiguration)` for this output.  
---|---  
`[VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` |  `[outputType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration#outputType\(\))` The `[OutputType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` for this particular output  
  
## Public properties

### enabled

Added in 4.2.0
    
    
    val [enabled](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#enabled\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)>

Flag controlling whether the output is enabled.

It is safe to change the value in case a specific output should be disabled

### outputFileName

Added in 9.4.1
    
    
    val [outputFileName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#outputFileName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The output file name for this Variant.

It is safe to modify it once you need custom artifact name.

### versionCode

Added in 4.2.0
    
    
    val [versionCode](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#versionCode\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

The version code for this output.

This will be initialized with the variant's merged flavor value or read from the manifest file if unset.

It is safe to modify it. When using Splits/Multi-APK output, it is generally necessary to change this value per output.

### versionName

Added in 4.2.0
    
    
    val [versionName](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/VariantOutput#versionName\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The version name for this output.

This will be initialized with the variant's merged flavor value, or it will be read from the manifest source file if it's not set via the DSL, or it will be null if it's also not set in the manifest.

It is safe to modify it.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
