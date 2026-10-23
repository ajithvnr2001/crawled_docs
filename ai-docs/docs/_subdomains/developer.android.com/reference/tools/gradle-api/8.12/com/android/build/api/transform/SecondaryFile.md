---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile/
title: SecondaryFile \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:27.529756+00:00
---

# SecondaryFile  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# SecondaryFile

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/SecondaryFile.java+class:com.android.build.api.transform.SecondaryFile)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    class [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)

* * *

**This class is deprecated.**  


A secondary input file(s) for a `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)`. A secondary input is part of the transform inputs and can be decorated to indicate if a change to the input would trigger a non incremental `[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))`. call. The collection should only contain one file.

## Summary

### Public constructors  
  
---  
`[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#SecondaryFile\(java.io.File,boolean\))(  
secondaryInputFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!,  
supportsIncrementalBuild: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
)`  
  
### Public functions  
  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  `~~[getFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFile\(\))~~()` **This function is deprecated.** use getFileCollection  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!` |  `[getFileCollection](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFileCollection\(\))()` Returns the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` handle for this secondary input to a `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)` if this `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` is constructed with `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`.  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!` |  `[getFileCollection](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFileCollection\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)!)` Returns the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` handle for this secondary input to a `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)`  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `~~[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(java.io.File\))~~(file: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!)` **This function is deprecated.** Use `[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(org.gradle.api.file.FileCollection\))`  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(org.gradle.api.file.FileCollection\))(file: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!)` Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will not trigger a full, non-incremental build.  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(java.util.function.Supplier<org.gradle.api.file.FileCollection>\))(file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!)` Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will not trigger a full non-incremental build.  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `~~[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(java.io.File\))~~(file: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!)` **This function is deprecated.** Use `[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(org.gradle.api.file.FileCollection\))`  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(org.gradle.api.file.FileCollection\))(file: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!)` Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will always trigger a full, non-incremental build.  
`java-static [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!` |  `[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(java.util.function.Supplier<org.gradle.api.file.FileCollection>\))(file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!)` Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will always trigger a full non-incremental build.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[supportsIncrementalBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#supportsIncrementalBuild\(\))()` Returns true if this secondary input changes can be handled by the receiving `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)` incrementally.  
  
## Public constructors

### SecondaryFile

Added in 4.2.0

Deprecated in 7.0.0
    
    
    [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#SecondaryFile\(java.io.File,boolean\))(  
        secondaryInputFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!,  
        supportsIncrementalBuild: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
    )

Parameters  
---  
`secondaryInputFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  the `[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)` this `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` will point to  
`supportsIncrementalBuild: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  if true, changes to the file can be handled incrementally by the transform  
  
See also  
---  
`[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(java.io.File\))` |   
`[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(java.io.File\))` |   
  
## Public functions

### getFile

Added in 4.2.0

Deprecated in 4.2.0
    
    
    fun ~~[getFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFile\(\))~~(): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!

**This function is deprecated.**  


use getFileCollection

Returns the file handle for this secondary input to a Transform.

Returns  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!` |  a file handle.  
  
### getFileCollection

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getFileCollection](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFileCollection\(\))(): [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!

Returns the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` handle for this secondary input to a `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)` if this `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` is constructed with `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`. Otherwise, null is returned. 

Note this method is not part of the API of `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)`.

Returns  
---  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!` |  FileCollection of this SecondaryFile  
  
### getFileCollection

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getFileCollection](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#getFileCollection\(org.gradle.api.Project\))(project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)!): [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!

Returns the `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)` handle for this secondary input to a `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)`

If this `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` is constructed with `[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)`, the supplied will be used to create a `[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)`.

Parameters  
---  
`project: [Project](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html)!` |  for creating a FileCollection when necessary.  
  
Returns  
---  
`[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!` |  FileCollection of this SecondaryFile  
  
### incremental

Added in 4.2.0

Deprecated in 4.2.0
    
    
    java-static fun ~~[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(java.io.File\))~~(file: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

**This function is deprecated.**  


Use `[incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(org.gradle.api.file.FileCollection\))`

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will not trigger a full, non-incremental build.

### incremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    java-static fun [incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(org.gradle.api.file.FileCollection\))(file: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will not trigger a full, non-incremental build.

### incremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    java-static fun [incremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#incremental\(java.util.function.Supplier<org.gradle.api.file.FileCollection>\))(file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will not trigger a full non-incremental build.

Parameters  
---  
`file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!` |  a supplier of file collection.  
  
### nonIncremental

Added in 4.2.0

Deprecated in 4.2.0
    
    
    java-static fun ~~[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(java.io.File\))~~(file: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

**This function is deprecated.**  


Use `[nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(org.gradle.api.file.FileCollection\))`

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will always trigger a full, non-incremental build.

### nonIncremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    java-static fun [nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(org.gradle.api.file.FileCollection\))(file: [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will always trigger a full, non-incremental build.

### nonIncremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    java-static fun [nonIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#nonIncremental\(java.util.function.Supplier<org.gradle.api.file.FileCollection>\))(file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!): [SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!

Creates a `[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)` instance that, when modified, will always trigger a full non-incremental build.

Parameters  
---  
`file: [Supplier](https://developer.android.com/reference/tools/gradle-api/8.12/java/util/function/Supplier)<[FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html)!>!` |  a supplier of file collection.  
  
### supportsIncrementalBuild

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [supportsIncrementalBuild](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile#supportsIncrementalBuild\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if this secondary input changes can be handled by the receiving `[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)` incrementally. If false, a change to the file returned by getFileCollection will trigger a non incremental build.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  true when the input file changes can be handled incrementally, false otherwise.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
