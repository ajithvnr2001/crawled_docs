---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact/
title: Artifact \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:23:49.529087+00:00
---

# Artifact  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Artifact

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/Artifact.kt+class:com.android.build.api.artifact.Artifact)

Added in 4.2.0
    
    
    abstract class [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

Known direct subclasses 

[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple), [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)

`[Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)` |  Denotes possible multiple `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances for this artifact type.  
---|---  
`[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)` |  Denotes a single `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instance of this artifact type at a given time.  
  
Known indirect subclasses 

[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD), [MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA), [MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES), [MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES), [MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact), [ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.CLASSES), [ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.JAVA_RES), [ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES), [ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact), [SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AAR), [SingleArtifact.AGGREGATED_LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_HTML_REPORT), [SingleArtifact.AGGREGATED_LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_SARIF_REPORT), [SingleArtifact.AGGREGATED_LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_TEXT_REPORT), [SingleArtifact.AGGREGATED_LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_XML_REPORT), [SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE), [SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.APK), [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.ASSETS), [SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.BUNDLE), [SingleArtifact.LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_HTML_REPORT), [SingleArtifact.LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_SARIF_REPORT), [SingleArtifact.LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_TEXT_REPORT), [SingleArtifact.LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_XML_REPORT), [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST), [SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS), [SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT), [SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE), [SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE), [SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST), [SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST), [SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE), [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)

`[MultipleArtifact.MULTIDEX_KEEP_PROGUARD](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.MULTIDEX_KEEP_PROGUARD)` |  Text files with additional ProGuard rules to be used to determine which classes are compiled into the main dex file.  
---|---  
`[MultipleArtifact.NATIVE_DEBUG_METADATA](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_DEBUG_METADATA)` |  Directories with native debug metadata  
`[MultipleArtifact.NATIVE_SYMBOL_TABLES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.NATIVE_SYMBOL_TABLES)` |  Directories with debug symbol table  
`[MultipleArtifact.PRE_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact.PRE_COMPILATION_CLASSES)` |  Directories containing generated code that will be added to compile classpath for the module.  
`[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/MultipleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
`[ScopedArtifact.CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope; includes users' transformation, but does not include Jacoco instrumentation  
`[ScopedArtifact.JAVA_RES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.JAVA_RES)` |   
`[ScopedArtifact.POST_COMPILATION_CLASSES](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact.POST_COMPILATION_CLASSES)` |  .class files, result of sources compilation and/or external dependencies depending on the scope  
`[ScopedArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ScopedArtifact)` |  List of ScopedArtifacts.Scope artifacts.  
`[SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AAR)` |  The final AAR file as it would be published.  
`[SingleArtifact.AGGREGATED_LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_HTML_REPORT)` |  The aggregated HTML lint report file  
`[SingleArtifact.AGGREGATED_LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_SARIF_REPORT)` |  The aggregated SARIF lint report file  
`[SingleArtifact.AGGREGATED_LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_TEXT_REPORT)` |  The aggregated text lint report file  
`[SingleArtifact.AGGREGATED_LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_XML_REPORT)` |  The aggregated XML lint report file  
`[SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE)` |  Universal APK that contains assets for all screen densities.  
`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
`[SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.ASSETS)` |  Assets that will be packaged in the resulting AAR, APK or Bundle.  
`[SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.BUNDLE)` |  The final Bundle ready for consumption at Play Store.  
`[SingleArtifact.LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_HTML_REPORT)` |  The HTML lint report file  
`[SingleArtifact.LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_SARIF_REPORT)` |  The SARIF lint report file  
`[SingleArtifact.LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_TEXT_REPORT)` |  The text lint report file  
`[SingleArtifact.LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.LINT_XML_REPORT)` |  The XML lint report file  
`[SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)` |  Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`[SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS)` |  The directory containing all the native library (.so) files that will be packaged in the APK, AAR, or Bundle.  
`[SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT)` |  The metadata for the library dependencies.  
`[SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)` |   
`[SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE)` |   
`[SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST)` |  A file containing the list of public resources exported by a library project.  
`[SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)` |  The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).  
`[SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE)` |  Points to the Version control information when VCS tagging is enabled (which is by default in release builds)  
`[SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/SingleArtifact)` |  Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.  
  
* * *

Defines a type of artifact handled by the Android Gradle Plugin.

Each instance of `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` is produced by a `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` and potentially consumed by any number of tasks.

An artifact can potentially be produced by more than one task (each task acting in an additive behavior), but consumers must be aware when more than one artifact can be present, implementing the `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)` interface will indicate such requirement.

An artifact must be one of the supported `[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)` and must be provided when the constructor is called. ArtifactKind also defines the specific `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` subclass used.

## Summary

### Nested types  
  
---  
`interface [Artifact.Appendable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Appendable)` Denotes an artifact type that can be appended to.  
`enum [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html)` Defines the kind of artifact type. this will be used to determine the output file location for instance.  
`interface [Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.ContainsMany)` Denotes a `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` that may contain zero to many `[com.android.build.api.variant.BuiltArtifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/BuiltArtifact)`.  
`abstract class [Artifact.Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` Denotes possible multiple `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances for this artifact type.  
`interface [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Replaceable)` Denotes an artifact type that can be replaced.  
`abstract class [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Single)<FileTypeT : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)` Denotes a single `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instance of this artifact type at a given time.  
`interface [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Transformable)` Denotes an artifact type that can be transformed.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
interface [Artifact.WithQualifiers](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.WithQualifiers)` Denotes a `[Multiple](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Multiple)` artifact that can have qualifiers attached to each of its `[FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)` instances.  
  
### Public companion properties  
  
---  
`[ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind.DIRECTORY)` |  `[DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#DIRECTORY\(\))` `[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)` for `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`  
`[ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind.FILE)` |  `[FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#FILE\(\))` `[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)` for `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`  
  
### Public constructors  
  
---  
`<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#Artifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<T>,  
category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)  
)`  
  
### Public functions  
  
---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))()`  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Public properties  
  
---  
`[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#category\(\))`  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<T>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Public companion properties

### DIRECTORY
    
    
    val [DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#DIRECTORY\(\)): [ArtifactKind.DIRECTORY](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind.DIRECTORY)

`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)` for `[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)`

### FILE
    
    
    val [FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#FILE\(\)): [ArtifactKind.FILE](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind.FILE)

`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)` for `[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)`

## Public constructors

### Artifact
    
    
    <T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [Artifact](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#Artifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category\))(  
        kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<T>,  
        category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)  
    )

## Public functions

### getFileSystemLocationName

Added in 4.2.0
    
    
    open fun [getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFileSystemLocationName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  Depending on `[T](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact)`, returns the file name of the folder under the variant-specific folder or an empty string to use defaults.  
  
### getFolderName

Added in 4.2.0
    
    
    open fun [getFolderName](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#getFolderName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  The folder name under which the artifact files or folders should be stored.  
  
### name

Added in 4.2.0
    
    
    fun [name](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#name\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Provide a unique name for the artifact type. For external plugins defining new types, consider adding the plugin name to the artifact's name to avoid collision with other plugins.

## Public properties

### category

Added in 4.2.0
    
    
    val [category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#category\(\)): [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact.Category)

### kind

Added in 4.2.0
    
    
    val [kind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/Artifact#kind\(\)): [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/artifact/ArtifactKind)<T>

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
