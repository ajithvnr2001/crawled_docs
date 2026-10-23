---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters/
title: AgpTestSuiteInputParameters \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:03.387622+00:00
---

# AgpTestSuiteInputParameters  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AgpTestSuiteInputParameters

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/AgpTestSuiteInputParameters.kt+class:com.android.build.api.dsl.AgpTestSuiteInputParameters)

Added in 9.3.3
    
    
    enum [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [kotlin.Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)  
|  ↳ | [com.android.build.api.dsl.AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)  
  
* * *

List of possible input parameters a Junit engine can consume to run successfully.

Each JUnit engine has particular inputs requirements and these must be passed across processes as the JUnit engine runs in a separate VM. Therefore, we cannot just use the Gradle's Provider APIs, plus those JUnit engines can run im multiple build systems.

So to express an input requirement in the Android ecosystem, a JUnit engine configuration can use a combination of the ones defined below. In the case of Gradle build system, the Test task will automatically become dependent on the tasks producing the artifacts and the artifacts location will be passed ot the JUnit engine.

To express the engine's requirements, the user must add the required inputs using the `[JUnitEngineSpec.inputs](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/JUnitEngineSpec#inputs\(\))` collection of `[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)`

TODO: possibly explore how junit engine could also express their dependencies to avoid users having the manually add those. TODO: Describe how the JUnit engine can retrieve the values at execution time once experimentation concluded.

## Summary

### Enum Values  
  
---  
`[AAPT2_EXECUTABLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#AAPT2_EXECUTABLE)` |  Path to the AAPT2 executable.  
`[ADB_EXECUTABLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#ADB_EXECUTABLE)` |  Path to the ADB executable.  
`[ANDROID_TEST_EXECUTION_MODE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#ANDROID_TEST_EXECUTION_MODE)` |  The execution mode for the test suite.  
`[LOCAL_TESTED_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#LOCAL_TESTED_APKS)` |  `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of local test APK files containing compiled Android resources (such as resources.arsc, assets, and merged manifests) for HostJar test suites.  
`[MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#MERGED_MANIFEST)` |  Path to the merged manifest file.  
`[STATIC_FILES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#STATIC_FILES)` |  `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of directories containing the static source files for the test suite.  
`[TESTED_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TESTED_APKS)` |  TODO: provide an access through the BuiltArtifactsLoader (moved out of gradle-api) ?  
`[TEST_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_APKS)` |  Path to the test APKs.  
`[TEST_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_CLASSES)` |  `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of folders containing test classes for this suite.  
`[TEST_CLASSPATH](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_CLASSPATH)` |  `[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of jar files or folders for the runtime classpath of the test classes  
`[TEST_UTIL_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_UTIL_APKS)` |  Comma separated list of APK files that are used for testing utilities.  
  
### Public functions  
  
---  
`[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Returns the enum constant of this type with the specified name.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)>` |  `[values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
### Public properties  
  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[propertyName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#propertyName\(\))`  
  
## Enum Values

### AAPT2_EXECUTABLE
    
    
    val [AgpTestSuiteInputParameters.AAPT2_EXECUTABLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#AAPT2_EXECUTABLE): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Path to the AAPT2 executable.

### ADB_EXECUTABLE
    
    
    val [AgpTestSuiteInputParameters.ADB_EXECUTABLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#ADB_EXECUTABLE): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Path to the ADB executable.

### ANDROID_TEST_EXECUTION_MODE
    
    
    val [AgpTestSuiteInputParameters.ANDROID_TEST_EXECUTION_MODE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#ANDROID_TEST_EXECUTION_MODE): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

The execution mode for the test suite.

### LOCAL_TESTED_APKS
    
    
    val [AgpTestSuiteInputParameters.LOCAL_TESTED_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#LOCAL_TESTED_APKS): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

`[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of local test APK files containing compiled Android resources (such as resources.arsc, assets, and merged manifests) for HostJar test suites.

These local test APKs are generated when Android resources are included in local test suites, allowing tests (such as screenshot tests or unit tests) to access these resources at execution time.

### MERGED_MANIFEST
    
    
    val [AgpTestSuiteInputParameters.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#MERGED_MANIFEST): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Path to the merged manifest file.

### STATIC_FILES
    
    
    val [AgpTestSuiteInputParameters.STATIC_FILES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#STATIC_FILES): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

`[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of directories containing the static source files for the test suite. The test suite must have been configured using the `[AgpTestSuite.assets](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#assets\(kotlin.Function1\))` method.

### TESTED_APKS
    
    
    val [AgpTestSuiteInputParameters.TESTED_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TESTED_APKS): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

TODO: provide an access through the BuiltArtifactsLoader (moved out of gradle-api) ?

`[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of APK files to be tested.

The test suite must have been configured using the `[AgpTestSuite.testApk](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#testApk\(kotlin.Function1\))`.

### TEST_APKS
    
    
    val [AgpTestSuiteInputParameters.TEST_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_APKS): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Path to the test APKs.

### TEST_CLASSES
    
    
    val [AgpTestSuiteInputParameters.TEST_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_CLASSES): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

`[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of folders containing test classes for this suite. The test suite must have been configured using the `[AgpTestSuite.hostJar](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuite#hostJar\(kotlin.Function1\))`.

### TEST_CLASSPATH
    
    
    val [AgpTestSuiteInputParameters.TEST_CLASSPATH](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_CLASSPATH): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

`[java.io.File.pathSeparator](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html#pathSeparator--)` separated list of jar files or folders for the runtime classpath of the test classes

### TEST_UTIL_APKS
    
    
    val [AgpTestSuiteInputParameters.TEST_UTIL_APKS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#TEST_UTIL_APKS): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Comma separated list of APK files that are used for testing utilities.

## Public functions

### valueOf

Added in 9.3.3
    
    
    fun [valueOf](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#valueOf\(kotlin.String\))(value: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Throws  
---  
`kotlin.IllegalArgumentException` |  if this enum type has no constant with the specified name  
  
### values

Added in 9.3.3
    
    
    fun [values](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[AgpTestSuiteInputParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters)>

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

## Public properties

### propertyName

Added in 9.3.3
    
    
    val [propertyName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/dsl/AgpTestSuiteInputParameters#propertyName\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
