---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpecBuilder/
title: JUnitEngineSpecBuilder \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:36:50.473289+00:00
---

# JUnitEngineSpecBuilder  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpecBuilder/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JUnitEngineSpecBuilder

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JUnitEngineSpecBuilder.kt+class:com.android.build.api.variant.JUnitEngineSpecBuilder)

Added in 9.3.3
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [JUnitEngineSpecBuilder](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpecBuilder) : [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec)

* * *

## Summary

### Public properties  
  
---  
`[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)>` |  `[inputs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpecBuilder#inputs\(\))` Returns a mutable list of inputs required by the junit engine running the test suite.  
  
### Inherited functions  
  
---  
From [com.android.build.api.variant.JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec) | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,org.gradle.api.provider.Provider\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` Adds a new key value pair property to the list of inputs of this test engine, the value will only be resolved at execution time.  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,kotlin.String\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new key value pair property to the list of inputs for this test engine.  
  
### Inherited properties  
  
---  
From [com.android.build.api.variant.JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec) | `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` |  `[enginesDependencies](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec#enginesDependencies\(\))` Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of runtime-only dependencies to find and load configured junit engines.  
---|---  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[includeEngines](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpec#includeEngines\(\))` Returns the final list of included engines for this tes suite.  
  
## Public properties

### inputs
    
    
    val [inputs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/JUnitEngineSpecBuilder#inputs\(\)): [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)>

Returns a mutable list of inputs required by the junit engine running the test suite.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
