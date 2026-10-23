---
url: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact/
title: SingleArtifact \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:06:02.478843+00:00
---

# SingleArtifact  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SingleArtifact

[View Source](https://cs.android.com/search?q=file:com/android/build/api/artifact/SingleArtifact.kt+class:com.android.build.api.artifact.SingleArtifact)

Added in 7.0.0
    
    
    sealed class [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> : [Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Single)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)  
|  ↳ | [com.android.build.api.artifact.Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Single)  
|  |  ↳ | [com.android.build.api.artifact.SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)  
  
Known direct subclasses 

[SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AAR), [SingleArtifact.AGGREGATED_LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_HTML_REPORT), [SingleArtifact.AGGREGATED_LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_SARIF_REPORT), [SingleArtifact.AGGREGATED_LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_TEXT_REPORT), [SingleArtifact.AGGREGATED_LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_XML_REPORT), [SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE), [SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK), [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.ASSETS), [SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.BUNDLE), [SingleArtifact.LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_HTML_REPORT), [SingleArtifact.LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_SARIF_REPORT), [SingleArtifact.LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_TEXT_REPORT), [SingleArtifact.LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_XML_REPORT), [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST), [SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS), [SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT), [SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE), [SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE), [SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST), [SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST), [SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE)

`[SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AAR)` |  The final AAR file as it would be published.  
---|---  
`[SingleArtifact.AGGREGATED_LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_HTML_REPORT)` |  The aggregated HTML lint report file  
`[SingleArtifact.AGGREGATED_LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_SARIF_REPORT)` |  The aggregated SARIF lint report file  
`[SingleArtifact.AGGREGATED_LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_TEXT_REPORT)` |  The aggregated text lint report file  
`[SingleArtifact.AGGREGATED_LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_XML_REPORT)` |  The aggregated XML lint report file  
`[SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE)` |  Universal APK that contains assets for all screen densities.  
`[SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK)` |  Directory where APK files will be located.  
`[SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.ASSETS)` |  Assets that will be packaged in the resulting AAR, APK or Bundle.  
`[SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.BUNDLE)` |  The final Bundle ready for consumption at Play Store.  
`[SingleArtifact.LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_HTML_REPORT)` |  The HTML lint report file  
`[SingleArtifact.LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_SARIF_REPORT)` |  The SARIF lint report file  
`[SingleArtifact.LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_TEXT_REPORT)` |  The text lint report file  
`[SingleArtifact.LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_XML_REPORT)` |  The XML lint report file  
`[SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST)` |  Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`[SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS)` |  The directory containing all the native library (.so) files that will be packaged in the APK, AAR, or Bundle.  
`[SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT)` |  The metadata for the library dependencies.  
`[SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE)` |   
`[SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE)` |   
`[SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST)` |  A file containing the list of public resources exported by a library project.  
`[SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST)` |  The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).  
`[SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE)` |  Points to the Version control information when VCS tagging is enabled (which is by default in release builds)  
  
* * *

Public `[Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact)` for Android Gradle plugin.

These are `[Artifact.Single](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Single)`, see `[MultipleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/MultipleArtifact)` for multiple ones.

All methods in the `[Artifacts](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifacts)` class should be supported with any subclass of this class.

## Summary

### Nested types  
  
---  
`object [SingleArtifact.AAR](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AAR) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` The final AAR file as it would be published.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.AGGREGATED_LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_HTML_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The aggregated HTML lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.AGGREGATED_LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_SARIF_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The aggregated SARIF lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.AGGREGATED_LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_TEXT_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The aggregated text lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.AGGREGATED_LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.AGGREGATED_LINT_XML_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The aggregated XML lint report file  
`object [SingleArtifact.APK](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.ContainsMany](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.ContainsMany), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` Directory where APK files will be located.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.APK_FROM_BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.APK_FROM_BUNDLE) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` Universal APK that contains assets for all screen densities.  
`object [SingleArtifact.ASSETS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.ASSETS) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` Assets that will be packaged in the resulting AAR, APK or Bundle.  
`object [SingleArtifact.BUNDLE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.BUNDLE) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` The final Bundle ready for consumption at Play Store.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.LINT_HTML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_HTML_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The HTML lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.LINT_SARIF_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_SARIF_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The SARIF lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.LINT_TEXT_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_TEXT_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The text lint report file  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.LINT_XML_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.LINT_XML_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The XML lint report file  
`object [SingleArtifact.MERGED_MANIFEST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_MANIFEST) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` Merged manifest file that will be used in the APK, Bundle and InstantApp packages.  
`object [SingleArtifact.MERGED_NATIVE_LIBS](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.MERGED_NATIVE_LIBS) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The directory containing all the native library (.so) files that will be packaged in the APK, AAR, or Bundle.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.METADATA_LIBRARY_DEPENDENCIES_REPORT) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)` The metadata for the library dependencies.  
`object [SingleArtifact.OBFUSCATION_MAPPING_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_FILE) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)`  
`object [SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.OBFUSCATION_MAPPING_PARTITION_FILE) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact), [Artifact.Replaceable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Replaceable), [Artifact.Transformable](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Transformable)`  
`object [SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.PUBLIC_ANDROID_RESOURCES_LIST) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` A file containing the list of public resources exported by a library project.  
`@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
object [SingleArtifact.RUNTIME_SYMBOL_LIST](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.RUNTIME_SYMBOL_LIST) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` The text symbol output file (R.txt) containing a list of resources and their ids (including of transitive dependencies).  
`object [SingleArtifact.VERSION_CONTROL_INFO_FILE](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact.VERSION_CONTROL_INFO_FILE) : [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)` Points to the Version control information when VCS tagging is enabled (which is by default in release builds)  
  
### Protected constructors  
  
---  
`<T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact#SingleArtifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category,kotlin.String\))(  
kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/ArtifactKind)<T>,  
category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Category),  
fileName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?  
)`  
  
### Public functions  
  
---  
`open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact#getFileSystemLocationName\(\))()`  
  
### Inherited functions  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact) | `open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[getFolderName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#getFolderName\(\))()`  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  `[name](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#name\(\))()` Provide a unique name for the artifact type.  
  
### Inherited properties  
  
---  
From [com.android.build.api.artifact.Artifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact) | `[Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Category)` |  `[category](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#category\(\))`  
---|---  
`[ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/ArtifactKind)<T>` |  `[kind](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact#kind\(\))`  
  
## Protected constructors

### SingleArtifact
    
    
    protected <T : [FileSystemLocation](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemLocation.html)> [SingleArtifact](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact#SingleArtifact\(com.android.build.api.artifact.ArtifactKind,com.android.build.api.artifact.Artifact.Category,kotlin.String\))(  
        kind: [ArtifactKind](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/ArtifactKind)<T>,  
        category: [Artifact.Category](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/Artifact.Category) = Category.INTERMEDIATES,  
        fileName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)? = null  
    )

## Public functions

### getFileSystemLocationName
    
    
    open fun [getFileSystemLocationName](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact#getFileSystemLocationName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |  Depending on `[T](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/artifact/SingleArtifact)`, returns the file name of the folder under the variant-specific folder or an empty string to use defaults.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
