---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope
title: QualifiedContent.Scope \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:37:04.853528+00:00
---

# QualifiedContent.Scope  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# QualifiedContent.Scope

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/QualifiedContent.java+class:com.android.build.api.transform.QualifiedContent.Scope)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    enum [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope) : [QualifiedContent.ScopeType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType)

* * *

The scope of the content. 

This indicates what the content represents, so that Transforms can apply to only part(s) of the classes or resources that the build manipulates.

## Summary

### Enum Values  
  
---  
`[EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES)` |  Only the external libraries  
`[PROJECT](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROJECT)` |  Only the project (module) content  
`[PROJECT_LOCAL_DEPS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROJECT_LOCAL_DEPS)` |  **This enum value is deprecated.** local dependencies are now processed as `[EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES)`  
`[PROVIDED_ONLY](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROVIDED_ONLY)` |  Local or remote dependencies that are provided-only  
`[SUB_PROJECTS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#SUB_PROJECTS)` |  Only the sub-projects (other modules)  
`[SUB_PROJECTS_LOCAL_DEPS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#SUB_PROJECTS_LOCAL_DEPS)` |  **This enum value is deprecated.** local dependencies are now processed as `[EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES)`  
`[TESTED_CODE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#TESTED_CODE)` |  Code that is being tested by the current variant, including dependencies  
  
### Public functions  
  
---  
`java-static [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!` |  `[valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the enum constant of this type with the specified name.  
`java-static [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!>!` |  `[values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#values\(\))()` Returns an array containing the constants of this enum type, in the order they're declared.  
  
### Public properties  
  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |  `[value](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#value\(\))`  
  
### Inherited functions  
  
---  
From [com.android.build.api.transform.QualifiedContent.ScopeType](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType) | `abstract [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[name](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.ScopeType#name\(\))()` Scope name, readable by humans.  
---|---  
  
## Enum Values

### EXTERNAL_LIBRARIES
    
    
    val [QualifiedContent.Scope.EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

Only the external libraries

### PROJECT
    
    
    val [QualifiedContent.Scope.PROJECT](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROJECT): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

Only the project (module) content

### PROJECT_LOCAL_DEPS
    
    
    val [QualifiedContent.Scope.PROJECT_LOCAL_DEPS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROJECT_LOCAL_DEPS): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

**This enum value is deprecated.**  


local dependencies are now processed as `[EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES)`

Only the project's local dependencies (local jars)

### PROVIDED_ONLY
    
    
    val [QualifiedContent.Scope.PROVIDED_ONLY](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#PROVIDED_ONLY): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

Local or remote dependencies that are provided-only

### SUB_PROJECTS
    
    
    val [QualifiedContent.Scope.SUB_PROJECTS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#SUB_PROJECTS): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

Only the sub-projects (other modules)

### SUB_PROJECTS_LOCAL_DEPS
    
    
    val [QualifiedContent.Scope.SUB_PROJECTS_LOCAL_DEPS](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#SUB_PROJECTS_LOCAL_DEPS): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

**This enum value is deprecated.**  


local dependencies are now processed as `[EXTERNAL_LIBRARIES](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#EXTERNAL_LIBRARIES)`

Only the sub-projects's local dependencies (local jars).

### TESTED_CODE
    
    
    val [QualifiedContent.Scope.TESTED_CODE](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#TESTED_CODE): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)

Code that is being tested by the current variant, including dependencies

## Public functions

### valueOf

Added in 4.2.0
    
    
    java-static fun [valueOf](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#valueOf\(java.lang.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!): [QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Returns  
---  
`[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!` |  the enum constant with the specified name  
  
Throws  
---  
`[java.lang.IllegalArgumentException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/IllegalArgumentException.html)` |  if this enum type has no constant with the specified name  
  
### values

Added in 4.2.0
    
    
    java-static fun [values](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#values\(\))(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!>!

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

Returns  
---  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[QualifiedContent.Scope](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope)!>!` |  an array containing the constants of this enum type, in the order they're declared  
  
## Public properties

### value
    
    
    val [value](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/transform/QualifiedContent.Scope#value\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
