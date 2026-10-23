---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext/
title: TestTaskContext \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:21:33.105686+00:00
---

# TestTaskContext  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestTaskContext

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/TestTaskContext.kt+class:com.android.build.api.dsl.TestTaskContext)

Added in 8.12.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [TestTaskContext](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext)

* * *

## Summary

### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[suiteName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#suiteName\(\))` Suite name the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is testing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[targetName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetName\(\))` `[AgpTestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteTarget)` name the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is targeting.  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[targetedDevices](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetedDevices\(\))` Returns the list of devices this `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task targets.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[targetedVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetedVariant\(\))` Targeted variant the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is running against.  
  
## Public properties

### suiteName

Added in 8.12.0
    
    
    val [suiteName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#suiteName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Suite name the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is testing.

TODO : Maybe replace with TestSuite Variant object once the variant interfaces become public.

### targetName

Added in 8.12.0
    
    
    val [targetName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

`[AgpTestSuiteTarget](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteTarget)` name the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is targeting.

### targetedDevices

Added in 8.12.0
    
    
    val [targetedDevices](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetedDevices\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Returns the list of devices this `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task targets. In case the test runs on the host machine, the list will be empty.

### targetedVariant

Added in 8.12.0
    
    
    val [targetedVariant](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/TestTaskContext#targetedVariant\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Targeted variant the `[org.gradle.api.tasks.testing.Test](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/Test.html)` task is running against.

TODO: Replace with `[com.android.build.api.variant.Component](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Component)` ?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
