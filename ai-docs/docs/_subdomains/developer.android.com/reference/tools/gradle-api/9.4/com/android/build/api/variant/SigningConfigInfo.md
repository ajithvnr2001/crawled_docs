---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo/
title: SigningConfigInfo \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:03:49.844760+00:00
---

# SigningConfigInfo  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SigningConfigInfo

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/SigningConfigInfo.kt+class:com.android.build.api.variant.SigningConfigInfo)

Added in 9.4.1
    
    
    class [SigningConfigInfo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo) : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

Configuration information required to sign a build artifact.

## Summary

### Public constructors  
  
---  
`[SigningConfigInfo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#SigningConfigInfo\(java.io.File,kotlin.String,kotlin.String,kotlin.String,kotlin.String\))(  
storeFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html),  
storePassword: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
keyAlias: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
keyPassword: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
storeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
)`  
  
### Public functions  
  
---  
`open operator [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[equals](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?)`  
`open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[hashCode](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#hashCode\(\))()`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[toString](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#toString\(\))()`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[keyAlias](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#keyAlias\(\))` The key alias.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[keyPassword](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#keyPassword\(\))` The key password.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` |  `[storeFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storeFile\(\))` The keystore file.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[storePassword](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storePassword\(\))` The keystore password.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[storeType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storeType\(\))` The keystore type.  
  
## Public constructors

### SigningConfigInfo

Added in 9.4.1
    
    
    [SigningConfigInfo](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#SigningConfigInfo\(java.io.File,kotlin.String,kotlin.String,kotlin.String,kotlin.String\))(  
        storeFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html),  
        storePassword: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        keyAlias: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        keyPassword: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),  
        storeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)  
    )

## Public functions

### equals
    
    
    open operator fun [equals](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#equals\(kotlin.Any\))(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

### hashCode
    
    
    open fun [hashCode](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#hashCode\(\))(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### toString
    
    
    open fun [toString](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#toString\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

## Public properties

### keyAlias

Added in 9.4.1
    
    
    val [keyAlias](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#keyAlias\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The key alias.

### keyPassword

Added in 9.4.1
    
    
    val [keyPassword](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#keyPassword\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The key password.

### storeFile

Added in 9.4.1
    
    
    val [storeFile](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storeFile\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)

The keystore file.

### storePassword

Added in 9.4.1
    
    
    val [storePassword](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storePassword\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The keystore password.

### storeType

Added in 9.4.1
    
    
    val [storeType](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/variant/SigningConfigInfo#storeType\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

The keystore type. Default: pkcs12

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
