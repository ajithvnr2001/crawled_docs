---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec/
title: JUnitEngineSpec \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:25:13.310496+00:00
---

# JUnitEngineSpec  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# JUnitEngineSpec

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/JUnitEngineSpec.kt+class:com.android.build.api.variant.JUnitEngineSpec)

Added in 9.0.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [JUnitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec)

Known direct subclasses 

[JUnitEngineSpecBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpecBuilder)

`[JUnitEngineSpecBuilder](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpecBuilder)` |   
---|---  
  
* * *

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,org.gradle.api.provider.Provider\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>)` Adds a new key value pair property to the list of inputs of this test engine, the value will only be resolved at execution time.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,kotlin.String\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Adds a new key value pair property to the list of inputs for this test engine.  
  
### Public properties  
  
---  
`[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` |  `[enginesDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#enginesDependencies\(\))` Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of runtime-only dependencies to find and load configured junit engines.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[includeEngines](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#includeEngines\(\))` Returns the final list of included engines for this tes suite.  
`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteInputParameters)>` |  `[inputs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#inputs\(\))` Returns the final list of inputs required by the junit engine running the test suite.  
  
## Public functions

### addInputProperty

Added in 9.0.1
    
    
    fun [addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,org.gradle.api.provider.Provider\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a new key value pair property to the list of inputs of this test engine, the value will only be resolved at execution time.

### addInputProperty

Added in 9.0.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [addInputProperty](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#addInputProperty\(kotlin.String,kotlin.String\))(propertyName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), propertyValue: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adds a new key value pair property to the list of inputs for this test engine.

## Public properties

### enginesDependencies

Added in 9.0.1
    
    
    val [enginesDependencies](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#enginesDependencies\(\)): [DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)

Returns a `[DependencyCollector](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyCollector.html)` that collects the set of runtime-only dependencies to find and load configured junit engines.

### includeEngines

Added in 9.0.1
    
    
    val [includeEngines](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#includeEngines\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Returns the final list of included engines for this tes suite.

you must use the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` API and access the parameters located in `[TestSuiteBuilder.junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteBuilder#junitEngineSpec\(\))` to add new engines.

### inputs

Added in 9.0.1
    
    
    val [inputs](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/JUnitEngineSpec#inputs\(\)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/dsl/AgpTestSuiteInputParameters)>

Returns the final list of inputs required by the junit engine running the test suite.

Since these inputs can change the build flow, it is too late to change them here, you must use the `[AndroidComponentsExtension.beforeVariants](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/AndroidComponentsExtension#beforeVariants\(com.android.build.api.variant.VariantSelector,kotlin.Function1\))` API and access the parameters located in `[TestSuiteBuilder.junitEngineSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/TestSuiteBuilder#junitEngineSpec\(\))`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
