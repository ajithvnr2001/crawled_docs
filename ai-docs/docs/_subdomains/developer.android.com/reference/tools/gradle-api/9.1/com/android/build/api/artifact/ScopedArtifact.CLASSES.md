---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES
title: ScopedArtifact.CLASSES \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:59:02.436242+00:00
---

# ScopedArtifact.CLASSES  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ScopedArtifact.CLASSES

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/ScopedArtifact.kt+class:com.android.build.api.artifact.ScopedArtifact.CLASSES)

Added in 7.4.0
    
    
    object [ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES) : [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact), [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Appendable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Transformable), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Replaceable)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact)  
|  |  |  ↳ | [com.android.build.api.artifact.ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES)  
  
* * *

.class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation

content of `[POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)` plus anything added to `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES)` after compilation.

You should use this if you just need to consume all the classes that will be packaged in the project.

If you need to generate bytecodes post compilation and also need to have access to the compiled classes, you cannot directly consume `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES)` and append to it as it would create a circular dependency.

Instead, consume `[POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)` and use `[CLASSES](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ScopedArtifact.CLASSES)` to append your bytecodes to.
    
    
    extension.onVariants(extension.selector().withBuildType("debug")) { variant ->  
        val generatorTask = project.tasks.register(  
             "postCompilation${variant.name.capitalizeFirstChar()}Task",  
             AddPostCompilationCodeGeneratorTask::class.java) { task ->  
                 // configure your task  
             }  
      
        // consume the result of compilation  
        variant.artifacts.forScope(Scope.PROJECT)  
             .use(generatorTask)  
             .toGet(  
                 ScopedArtifact.POST_COMPILATION_CLASSES,  
                 AddPostCompilationCodeGeneratorTask::jars,  
                 AddPostCompilationCodeGeneratorTask::dirs  
        )  
      
        // and produce the new bytecodes.  
        variant.artifacts.forScope(Scope.PROJECT)  
            .use(generatorTask)  
            .toAppend(ScopedArtifact.CLASSES, AddPostCompilationCodeGeneratorTask::outputDir)  
    }

## Summary

### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
---|---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/ArtifactKind)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/artifact/Artifact#kind\(\))`  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-12-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-19 UTC."],[],[]] 
