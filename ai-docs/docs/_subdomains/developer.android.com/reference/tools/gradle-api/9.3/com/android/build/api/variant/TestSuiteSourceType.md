---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType/
title: TestSuiteSourceType \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:40:00.976305+00:00
---

# TestSuiteSourceType  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteSourceType

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/TestSuiteSourceType.kt+class:com.android.build.api.variant.TestSuiteSourceType)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    enum [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.variant.TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)  
  
* * *

Type of a source abstraction.

## Summary

### Enum Values  
  
---  
`[ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#ASSETS)` |   
`[HOST_JAR](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#HOST_JAR)` |   
`[TEST_APK](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#TEST_APK)` |   
  
### Public functions  
  
---  
`[TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
## Enum Values

### ASSETS
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [TestSuiteSourceType.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#ASSETS): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)

### HOST_JAR
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [TestSuiteSourceType.HOST_JAR](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#HOST_JAR): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)

### TEST_APK
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    val [TestSuiteSourceType.TEST_APK](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#TEST_APK): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)

## Public functions

### valueOf

Added in 9.3.3
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 9.3.3
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[TestSuiteSourceType](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/TestSuiteSourceType)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
