---
url: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact/
title: ScopedArtifact \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:41:53.700466+00:00
---

# ScopedArtifact  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifact

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/ScopedArtifact.kt+class:com.android.build.api.artifact.ScopedArtifact)

Added in 7.4.0
    
    
    sealed class [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact) : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Single)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact)  
  
Known direct subclasses 

[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.CLASSES), [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.JAVA_RES), [ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)

`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
---|---  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
`[ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope  
  
* * *

List of ScopedArtifacts.Scope artifacts.

## Summary

### Nested types  
  
---  
`object [ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.CLASSES) : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Transformable), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Replaceable)` .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
`object [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.JAVA_RES) : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Transformable), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Replaceable)`  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES) : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact)` .class files, result of sources compilation and/or external dependencies depending on the scope  
  
### Protected constructors  
  
---  
`[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact#ScopedArtifact\(\))()`  
  
### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Protected constructors

### ScopedArtifact
    
    
    protected [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.2/com/android/build/api/artifact/ScopedArtifact#ScopedArtifact\(\))()

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
