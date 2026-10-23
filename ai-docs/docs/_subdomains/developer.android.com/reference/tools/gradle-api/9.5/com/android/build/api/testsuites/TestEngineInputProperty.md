---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty/
title: TestEngineInputProperty \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:16:02.363127+00:00
---

# TestEngineInputProperty  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# TestEngineInputProperty

[View Source](https://cs.android.com/search?q=file:com/android/build/api/testsuites/TestEngineInputProperty.kt+class:com.android.build.api.testsuites.TestEngineInputProperty)

Added in 8.13.0
    
    
    data class [TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty)

* * *

Definition of a single property that is passed from the AGP Test task to the junit engine configured for the test suite.

## Summary

### Constants  
  
---  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[BINARY_FOLDERS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#BINARY_FOLDERS\(\))` List of binary folders to find tests in, separated by `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)`  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[COVERAGE_DIR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#COVERAGE_DIR\(\))` Path to the coverage data directory  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[LOGGING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#LOGGING_FILE\(\))` Path to a file location to use as the logging output.  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[RESULTS_DIR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#RESULTS_DIR\(\))` Path to the results directory  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[SERIAL_IDS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#SERIAL_IDS\(\))` Serial IDs to deploy to  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[SOURCE_FOLDERS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#SOURCE_FOLDERS\(\))` List of source folders to find tests in, separated by `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)`  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[STREAMING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#STREAMING_FILE\(\))` Path to a file location to use to stream results back to the Test task  
`const [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[TESTED_APPLICATION_ID](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#TESTED_APPLICATION_ID\(\))` Tested application ID  
  
### Public constructors  
  
---  
`[TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#TestEngineInputProperty\(kotlin.String,kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))`  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#name\(\))`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[value](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#value\(\))`  
  
## Constants

### BINARY_FOLDERS
    
    
    const val [BINARY_FOLDERS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#BINARY_FOLDERS\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

List of binary folders to find tests in, separated by `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)`

### COVERAGE_DIR
    
    
    const val [COVERAGE_DIR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#COVERAGE_DIR\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Path to the coverage data directory

### LOGGING_FILE
    
    
    const val [LOGGING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#LOGGING_FILE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Path to a file location to use as the logging output.

### RESULTS_DIR
    
    
    const val [RESULTS_DIR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#RESULTS_DIR\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Path to the results directory

### SERIAL_IDS
    
    
    const val [SERIAL_IDS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#SERIAL_IDS\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Serial IDs to deploy to

### SOURCE_FOLDERS
    
    
    const val [SOURCE_FOLDERS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#SOURCE_FOLDERS\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

List of source folders to find tests in, separated by `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)`

### STREAMING_FILE
    
    
    const val [STREAMING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#STREAMING_FILE\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Path to a file location to use to stream results back to the Test task

### TESTED_APPLICATION_ID
    
    
    const val [TESTED_APPLICATION_ID](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#TESTED_APPLICATION_ID\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Tested application ID

## Public constructors

### TestEngineInputProperty

Added in 8.13.0
    
    
    [TestEngineInputProperty](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#TestEngineInputProperty\(kotlin.String,kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))

## Public properties

### name

Added in 8.13.0
    
    
    val [name](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#name\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

### value

Added in 8.13.0
    
    
    val [value](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/testsuites/TestEngineInputProperty#value\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
