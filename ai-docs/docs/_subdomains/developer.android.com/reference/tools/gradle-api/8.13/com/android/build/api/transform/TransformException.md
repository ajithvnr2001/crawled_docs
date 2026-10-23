---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException/
title: TransformException \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:37:10.245463+00:00
---

# TransformException  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TransformException

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/TransformException.java+class:com.android.build.api.transform.TransformException)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    class [TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException) : [Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)  
|  ↳ | [java.lang.Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html)  
|  |  ↳ | [com.android.build.api.transform.TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException)  
  
* * *

**This class is deprecated.**  


An exception during the execution of a Transform.

## Summary

### Public constructors  
  
---  
`[TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.String\))(s: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)`  
`[TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.Throwable\))(throwable: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)`  
`[TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.String,java.lang.Throwable\))(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)`  
  
### Inherited functions  
  
---  
From [java.lang.Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html) | `synchronized [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html)(exception: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)`  
---|---  
`synchronized [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!` |  `[fillInStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html)()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getLocalizedMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html)()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-message.html)()`  
`synchronized [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!>!` |  `[getSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html)()`  
`synchronized [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!` |  `[initCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html)(cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[toString](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/to-string.html)()`  
  
### Inherited properties  
  
---  
From [java.lang.Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html) | `[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!` |  `[cause](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html#cause--)`  
---|---  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[StackTraceElement](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/StackTraceElement.html)!>!` |  `[stackTrace](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html#stackTrace--)`  
  
## Public constructors

### TransformException

Added in 4.2.0

Deprecated in 7.0.0
    
    
    [TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.String\))(s: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)

### TransformException

Added in 4.2.0

Deprecated in 7.0.0
    
    
    [TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.Throwable\))(throwable: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)

### TransformException

Added in 4.2.0

Deprecated in 7.0.0
    
    
    [TransformException](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/TransformException#TransformException\(java.lang.String,java.lang.Throwable\))(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
