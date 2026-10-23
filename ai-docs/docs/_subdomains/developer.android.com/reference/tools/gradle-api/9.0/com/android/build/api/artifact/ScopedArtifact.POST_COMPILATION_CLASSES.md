---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES
title: ScopedArtifact.POST_COMPILATION_CLASSES \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:14:21.219236+00:00
---

# ScopedArtifact.POST_COMPILATION_CLASSES  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifact.POST_COMPILATION_CLASSES

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/ScopedArtifact.kt+class:com.android.build.api.artifact.ScopedArtifact.POST_COMPILATION_CLASSES)

Added in 9.0.1
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    object [ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES) : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)  
  
* * *

.class files, result of sources compilation and/or external dependencies depending on the scope

Do not use this unless you are producing bytecodes post compilation, see `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)`. This artifact is only providing a readonly view of the compiled classes, to add or replace classes, use `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)`

To add new bytecode or transform existing bytecode, use `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)`. Bytecode added to `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)`, or transformed `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.CLASSES)` will not impact the content of `[POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)`

It is not possible to register such bytecode generator through the DSL, one must use this Variant API.

The classes registered through this API will be visible to the `[com.android.build.api.variant.Instrumentation](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/Instrumentation)` pipeline.

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-13 UTC."],[],[]] 
