---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/InstrumentationContext/
title: InstrumentationContext \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:15:46.157472+00:00
---

# InstrumentationContext  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/InstrumentationContext/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# InstrumentationContext

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/InstrumentationContext.kt+class:com.android.build.api.instrumentation.InstrumentationContext)

Added in 4.2.0
    
    
    interface [InstrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/InstrumentationContext) : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

Instrumentation context data that will be injected to `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/AsmClassVisitorFactory)` on instantiation.

## Summary

### Public properties  
  
---  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>` |  `[apiVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/InstrumentationContext#apiVersion\(\))` The asm api version to be passed to the `[ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` constructor.  
  
## Public properties

### apiVersion

Added in 4.2.0
    
    
    val [apiVersion](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/instrumentation/InstrumentationContext#apiVersion\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)>

The asm api version to be passed to the `[ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` constructor.
    
    
    | AGP version | Corresponding ASM version |  
    |-------------|---------------------------|  
    | 4.2.0 - 7.0 |            ASM7           |  
    |    7.1.0+   |            ASM9           |

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
