---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration/
title: VariantOutputConfiguration \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:21:30.938998+00:00
---

# VariantOutputConfiguration  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# VariantOutputConfiguration

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/VariantOutputConfiguration.kt+class:com.android.build.api.variant.VariantOutputConfiguration)

Added in 4.2.0
    
    
    interface [VariantOutputConfiguration](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration)

Known direct subclasses 

[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact), [VariantOutput](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutput)

`[BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/BuiltArtifact)` |  Represents a built artifact that is present in the file system.  
---|---  
`[VariantOutput](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutput)` |  Defines a variant output.  
  
* * *

Configuration for a given build output.

This only applies to APKs as AARs and Bundles (AABs) do not support multiple outputs.

See https://developer.android.com/studio/build/configure-apk-splits.html for more information on multiple APK support.

See also  
---  
`[Splits](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/Splits)` |   
  
## Summary

### Nested types  
  
---  
`enum [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)` The type of an output.  
  
### Public properties  
  
---  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/FilterConfiguration)>` |  `[filters](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration#filters\(\))` The list of `[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/FilterConfiguration)` for this output.  
`[VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` |  `[outputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration#outputType\(\))` The `[OutputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` for this particular output  
  
## Public properties

### filters

Added in 4.2.0
    
    
    val [filters](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration#filters\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/FilterConfiguration)>

The list of `[FilterConfiguration](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/FilterConfiguration)` for this output.

If the list is empty this means there is no filter associated to this output. This is typically the case for `[OutputType.SINGLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType#SINGLE)`

### outputType

Added in 4.2.0
    
    
    val [outputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration#outputType\(\)): [VariantOutputConfiguration.OutputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType)

The `[OutputType](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/variant/VariantOutputConfiguration.OutputType)` for this particular output

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
