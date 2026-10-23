---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating/
title: ReplacedByIncubating \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:28:21.819243+00:00
---

# ReplacedByIncubating  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ReplacedByIncubating

[View Source](https://cs.android.com/search?q=file:com/android/build/api/annotations/ReplacedByIncubating.kt+class:com.android.build.api.annotations.ReplacedByIncubating)

Added in 8.8.0
    
    
    @[Target](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [AnnotationTarget.CLASS, AnnotationTarget.FUNCTION, AnnotationTarget.FIELD, AnnotationTarget.CONSTRUCTOR, AnnotationTarget.PROPERTY_GETTER, AnnotationTarget.PROPERTY_SETTER])  
    @[Retention](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.annotation/-retention/index.html)(value = AnnotationRetention.RUNTIME)  
    annotation [ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating)

* * *

Annotation for APIs that are in the process of being replaced by an `[org.gradle.api.Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)` API.

When replacing a stable method with a new API which is `[org.gradle.api.Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)`, we cannot directly deprecate the old method as it would leave the user to use either between a deprecated or an incubating API.

Therefore, when replacing a public API with a new version, the following rules apply :

  * The new API will be annotated with `[org.gradle.api.Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)`

  * The old API will be annotated with `[ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating)` but will not be deprecated yet.

  * Once the new API becomes stable, the old API `[ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating)` will be replaced with a `[Deprecated](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-deprecated/index.html)` annotation.

  * After the deprecation period has passed, the old API will be removed.




Users can use this annotation presence to start moving their code to the new API if they do not object using an incubating potentially unstable API.

This interface is meant to document the Android Gradle Plugin APIs and should not be used by third party plugins/build logic.

## Summary

### Public constructors  
  
---  
`[ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#ReplacedByIncubating\(kotlin.String,kotlin.Long\))(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), bugId: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html))`  
  
### Public properties  
  
---  
`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` |  `[bugId](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#bugId\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[message](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#message\(\))`  
  
## Public constructors

### ReplacedByIncubating
    
    
    [ReplacedByIncubating](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#ReplacedByIncubating\(kotlin.String,kotlin.Long\))(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), bugId: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html))

## Public properties

### bugId
    
    
    val [bugId](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#bugId\(\)): [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)

### message
    
    
    val [message](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/annotations/ReplacedByIncubating#message\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
