---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient/
title: TestSuiteExecutionClient \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:57:39.536529+00:00
---

# TestSuiteExecutionClient  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestSuiteExecutionClient

[View Source](https://cs.android.com/search?q=file:com/android/build/api/testsuites/TestSuiteExecutionClient.kt+class:com.android.build.api.testsuites.TestSuiteExecutionClient)

Added in 8.13.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    class [TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient)

* * *

Simple API to retrieve the execution context set by the Test Task before running the junit test engine.

Input parameters can be requested in the DSL by adding `[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestEngineInputProperty)` to the `[com.android.build.api.dsl.JUnitEngineSpec.inputs](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/dsl/JUnitEngineSpec#inputs\(\))`.

At execution time, test engines can retrieve the requested parameters values using the `[inputParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#inputParameters\(\))` or the `[getInputParameter](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#getInputParameter\(kotlin.String\))` APIs.

## Summary

### Constants  
  
---  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[DEFAULT_ENV_VARIABLE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#DEFAULT_ENV_VARIABLE\(\))` Name of the environment property the junit engine expect to be set.  
  
### Public companion functions  
  
---  
`[TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[default](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#default\(\))()` Load the context using the default environment variable set by the test task  
`[TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[withEnvVariable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#withEnvVariable\(kotlin.String\))(variableName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Load the context using a specific environment variable.  
  
### Public constructors  
  
---  
`[TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#TestSuiteExecutionClient\(kotlin.collections.Collection\))(  
inputParameters: [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestEngineInputProperty)>  
)`  
  
### Public functions  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[getInputParameter](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#getInputParameter\(kotlin.String\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Retrieve a single input parameter using its name  
  
### Public properties  
  
---  
`[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestEngineInputProperty)>` |  `[inputParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#inputParameters\(\))` full list of resolved input parameters.  
  
## Constants

### DEFAULT_ENV_VARIABLE
    
    
    const val [DEFAULT_ENV_VARIABLE](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#DEFAULT_ENV_VARIABLE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Name of the environment property the junit engine expect to be set. This environment property will point to a file location which content will be an instance of TestEngineInputProperties serialized as a Json object.

## Public companion functions

### default

Added in 8.13.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [default](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#default\(\))(): [TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient)

Load the context using the default environment variable set by the test task

### withEnvVariable

Added in 8.13.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [withEnvVariable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#withEnvVariable\(kotlin.String\))(variableName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient)

Load the context using a specific environment variable.

## Public constructors

### TestSuiteExecutionClient

Added in 8.13.0
    
    
    [TestSuiteExecutionClient](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#TestSuiteExecutionClient\(kotlin.collections.Collection\))(  
        inputParameters: [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestEngineInputProperty)>  
    )

## Public functions

### getInputParameter

Added in 8.13.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [getInputParameter](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#getInputParameter\(kotlin.String\))(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Retrieve a single input parameter using its name

## Public properties

### inputParameters

Added in 8.13.0
    
    
    val [inputParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestSuiteExecutionClient#inputParameters\(\)): [Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/testsuites/TestEngineInputProperty)>

full list of resolved input parameters.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
