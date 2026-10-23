---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException/
title: PropertyAccessNotAllowedException \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:56:59.056768+00:00
---

# PropertyAccessNotAllowedException  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# PropertyAccessNotAllowedException

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/PropertyAccessNotAllowedException.kt+class:com.android.build.api.variant.PropertyAccessNotAllowedException)

Added in 8.3.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    class [PropertyAccessNotAllowedException](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException) : [RuntimeException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/RuntimeException.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)  
|  ↳ | [java.lang.Exception](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Exception.html)  
|  |  ↳ | [java.lang.RuntimeException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/RuntimeException.html)  
|  |  |  ↳ | [com.android.build.api.variant.PropertyAccessNotAllowedException](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException)  
  
* * *

Exception thrown when users are trying to access `[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)` properties.

`[VariantBuilder](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/VariantBuilder)` properties are defined as kotlin properties so users can use simple assignment rather than calling a set function. However, those properties can only be set.

It is not safe to read the property value as other registered `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callbacks can run later and change the value.

If you need the final value of a property, it is most likely available in the `[Variant](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/Variant)` hierarchy accessible through the `[AndroidComponentsExtension.onVariants](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/AndroidComponentsExtension#onVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` callbacks.

## Summary

### Public constructors  
  
---  
`[PropertyAccessNotAllowedException](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#PropertyAccessNotAllowedException\(kotlin.String,kotlin.String\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), location: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[location](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#location\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[propertyName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#propertyName\(\))`  
  
### Inherited functions  
  
---  
From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/add-suppressed.html)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html))`  
---|---  
`open [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` |  `[fillInStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/fill-in-stack-trace.html)()`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getLocalizedMessage](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-localized-message.html)()`  
`open [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[StackTraceElement](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/StackTraceElement.html)>` |  `[getStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-stack-trace.html)()`  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)>` |  `[getSuppressed](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/get-suppressed.html)()`  
`open [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)` |  `[initCause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/init-cause.html)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html))`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)()`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)(p0: [PrintStream](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/PrintStream.html))`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[printStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/print-stack-trace.html)(p0: [PrintWriter](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/PrintWriter.html))`  
`open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setStackTrace](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/set-stack-trace.html)(p0: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[StackTraceElement](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/StackTraceElement.html)>)`  
  
### Inherited properties  
  
---  
From [kotlin.Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html) | `open [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)?` |  `[cause](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/cause.html)`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[message](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/message.html)`  
  
## Public constructors

### PropertyAccessNotAllowedException

Added in 8.3.1
    
    
    [PropertyAccessNotAllowedException](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#PropertyAccessNotAllowedException\(kotlin.String,kotlin.String\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), location: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))

## Public properties

### location

Added in 8.3.1
    
    
    val [location](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#location\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

### propertyName

Added in 8.3.1
    
    
    val [propertyName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/variant/PropertyAccessNotAllowedException#propertyName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
