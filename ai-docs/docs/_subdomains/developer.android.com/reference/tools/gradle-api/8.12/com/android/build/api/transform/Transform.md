---
url: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform/
title: Transform \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:05:29.754648+00:00
---

# Transform  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Transform

[View Source](https://cs.android.com/search?q=file:com/android/build/api/transform/Transform.java+class:com.android.build.api.transform.Transform)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    abstract class [Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform)

* * *

**This class is deprecated.**  


This API is planned to be removed in Android Gradle Plugin 9.0.

A Transform that processes intermediary build artifacts. 

This API is deprecated and is planned to be removed in Android Gradle plugin 9.0. 

There is no single replacement. For more information about how to migrate, see [ https://developer.android.com/studio/releases/gradle-plugin-roadmap ](https://developer.android.com/studio/releases/gradle-plugin-roadmap). 

For each added transform, a new task is created. The action of adding a transform takes care of handling dependencies between the tasks. This is done based on what the transform processes. The output of the transform becomes consumable by other transforms and these tasks get automatically linked together. 

The Transform indicates what it applies to (content, scope) and what it generates (content). 

A transform receives input as a collection `[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)`, which is composed of s and `[DirectoryInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/DirectoryInput)`s. Both provide information about the `[Scope](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.Scope)`s and `[ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)`s associated with their particular content. 

The output is handled by `[TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider)` which allows creating new self-contained content, each associated with their own Scopes and Content Types. The content handled by TransformInput/Output is managed by the transform system, and their location is not configurable. 

It is best practice to write into as many outputs as Jar/Folder Inputs have been received by the transform. Combining all the inputs into a single output prevents downstream transform from processing limited scopes. 

While it's possible to differentiate different Content Types by file extension, it's not possible to do so for Scopes. Therefore if a transform request a Scope but the only available Output contains more than the requested Scope, the build will fail. If a transform request a single content type but the only available content includes more than the requested type, the input file/folder will contain all the files of all the types, but the transform should only read, process and output the type(s) it requested. 

Additionally, a transform can indicate secondary inputs/outputs. These are not handled by upstream or downstream transforms, and are not restricted by type handled by transform. They can be anything. 

It's up to each transform to manage where these files are, and to make sure that these files are generated before the transform is called. This is done through additional parameters when register the transform. 

These secondary inputs/outputs allow a transform to read but not process any content. This can be achieved by having `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getScopes\(\))` return an empty list and use `[getReferencedScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getReferencedScopes\(\))` to indicate what to read instead.

## Summary

### Public constructors  
  
---  
`[Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#Transform\(\))()`  
  
### Public functions  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
[applyToVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#applyToVariant\(com.android.build.api.variant.VariantInfo\))(variant: [VariantInfo](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo)!)` Whether this transform should be applied to a given variant.  
`abstract ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  `[getInputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getInputTypes\(\))()` Returns the type(s) of data that is consumed by the Transform.  
`abstract [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` |  `[getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getName\(\))()` Returns the unique name of the transform.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!` |  `[getOutputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getOutputTypes\(\))()` Returns the type(s) of data that is generated by the Transform.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html))[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getParameterInputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getParameterInputs\(\))()` Returns a map of non-file input parameters using a unique identifier as the map key.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getReferencedScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getReferencedScopes\(\))()` Returns the referenced scope(s) for the Transform.  
`abstract ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!` |  `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getScopes\(\))()` Returns the scope(s) of the Transform.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!` |  `[getSecondaryDirectoryOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryDirectoryOutputs\(\))()` Returns a list of additional (out of streams) directory(ies) that this Transform creates.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!` |  `~~[getSecondaryFileInputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileInputs\(\))~~()` **This function is deprecated.** replaced by `[getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))`  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!` |  `[getSecondaryFileOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileOutputs\(\))()` Returns a list of additional (out of streams) file(s) that this Transform creates.  
`([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!>!` |  `[getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))()` Returns a list of additional file(s) that this Transform needs to run.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCacheable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#isCacheable\(\))()` Returns if this transform's outputs should be cached.  
`abstract [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#isIncremental\(\))()` Returns whether the Transform can perform incremental work.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setOutputDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#setOutputDirectory\(org.gradle.api.provider.Property<org.gradle.api.file.Directory>\))(directory: [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)!>!)` For Transforms that produce an output available though the [BuildArtifactsHolder] provider based interfaces should indicate the output directory of the produced artifact  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setOutputFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#setOutputFile\(org.gradle.api.provider.Property<org.gradle.api.file.RegularFile>\))(file: [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)!>!)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))(transformInvocation: [TransformInvocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInvocation)!)` Executes the Transform.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `~~[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.Context,java.util.Collection<com.android.build.api.transform.TransformInput>,java.util.Collection<com.android.build.api.transform.TransformInput>,com.android.build.api.transform.TransformOutputProvider,boolean\))~~(  
context: [Context](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context)!,  
inputs: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)!>!,  
referencedInputs: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)!>!,  
outputProvider: [TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider)!,  
isIncremental: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
)` **This function is deprecated.** replaced by `[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))`.  
  
## Public constructors

### Transform

Added in 4.2.0

Deprecated in 7.0.0
    
    
    [Transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#Transform\(\))()

## Public functions

### applyToVariant

Added in 4.2.0

Deprecated in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun [applyToVariant](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#applyToVariant\(com.android.build.api.variant.VariantInfo\))(variant: [VariantInfo](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether this transform should be applied to a given variant. 

since 3.4

Parameters  
---  
`variant: [VariantInfo](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/variant/VariantInfo)!` |  information about the current variant.  
  
Returns  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  true if the transform should be applied to a given variant, false otherwise.  
  
### getInputTypes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    abstract fun [getInputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getInputTypes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!

Returns the type(s) of data that is consumed by the Transform. This may be more than one type. **This must be of type`[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.DefaultContentType)`**

### getName

Added in 4.2.0

Deprecated in 7.0.0
    
    
    abstract fun [getName](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getName\(\))(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!

Returns the unique name of the transform. 

This is associated with the type of work that the transform does. It does not have to be unique per variant.

### getOutputTypes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getOutputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getOutputTypes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[QualifiedContent.ContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.ContentType)!>!

Returns the type(s) of data that is generated by the Transform. This may be more than one type. 

The default implementation returns `[getInputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getInputTypes\(\))`. 

**This must be of type`[QualifiedContent.DefaultContentType](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/QualifiedContent.DefaultContentType)`**

### getParameterInputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getParameterInputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getParameterInputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html))[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!

Returns a map of non-file input parameters using a unique identifier as the map key. 

Changes to values returned in this map will trigger a new execution of the Transform even if the content inputs haven't been touched. 

Changes to these values force a non incremental execution. 

The default implementation returns an empty Map.

### getReferencedScopes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getReferencedScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getReferencedScopes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!

Returns the referenced scope(s) for the Transform. These scopes are not consumed by the Transform. They are provided as inputs, but are still available as inputs for other Transforms to consume. 

The default implementation returns an empty Set.

### getScopes

Added in 4.2.0

Deprecated in 7.0.0
    
    
    abstract fun [getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getScopes\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html))[Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)<[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!>!

Returns the scope(s) of the Transform. This indicates which scopes the transform consumes.

### getSecondaryDirectoryOutputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getSecondaryDirectoryOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryDirectoryOutputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!

Returns a list of additional (out of streams) directory(ies) that this Transform creates. 

These File instances can only represent directories. For files, use `[getSecondaryFileOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileOutputs\(\))`

Changes to directories returned in this list will trigger a new execution of the Transform even if the qualified-content inputs haven't been touched. 

Changes to these output directories force a non incremental execution. 

The default implementation returns an empty collection.

### getSecondaryFileInputs

Added in 4.2.0

Deprecated in 4.2.0
    
    
    fun ~~[getSecondaryFileInputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileInputs\(\))~~(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!

**This function is deprecated.**  


replaced by `[getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))`

Returns a list of additional file(s) that this Transform needs to run. Preferably, use `[getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))` API which allow eah secondary file to indicate if changes can be handled incrementally or not. This API will treat all additional file change as a non incremental event. 

Changes to files returned in this list will trigger a new execution of the Transform even if the qualified-content inputs haven't been touched. 

Any changes to these files will trigger a non incremental execution. 

The default implementation returns an empty collection.

### getSecondaryFileOutputs

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getSecondaryFileOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileOutputs\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)!>!

Returns a list of additional (out of streams) file(s) that this Transform creates. 

These File instances can only represent files, not directories. For directories, use `[getSecondaryDirectoryOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryDirectoryOutputs\(\))`

Changes to files returned in this list will trigger a new execution of the Transform even if the qualified-content inputs haven't been touched. 

Changes to these output files force a non incremental execution. 

The default implementation returns an empty collection.

### getSecondaryFiles

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))(): ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[SecondaryFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/SecondaryFile)!>!

Returns a list of additional file(s) that this Transform needs to run. 

Changes to files returned in this list will trigger a new execution of the Transform even if the qualified-content inputs haven't been touched. 

Each secondary input has the ability to be declared as necessitating a non incremental execution in case of change. This Transform can therefore declare which secondary file changes it supports in incremental mode. 

The default implementation returns an empty collection.

### isCacheable

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [isCacheable](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#isCacheable\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns if this transform's outputs should be cached. Please read Javadoc if you would like to make your transform cacheable.

### isIncremental

Added in 4.2.0

Deprecated in 7.0.0
    
    
    abstract fun [isIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#isIncremental\(\))(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns whether the Transform can perform incremental work. 

If it does, then the TransformInput may contain a list of changed/removed/added files, unless something else triggers a non incremental run.

### setOutputDirectory

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [setOutputDirectory](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#setOutputDirectory\(org.gradle.api.provider.Property<org.gradle.api.file.Directory>\))(directory: [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)!>!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

For Transforms that produce an output available though the [BuildArtifactsHolder] provider based interfaces should indicate the output directory of the produced artifact

Parameters  
---  
`directory: [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html)!>!` |   
  
### setOutputFile

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [setOutputFile](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#setOutputFile\(org.gradle.api.provider.Property<org.gradle.api.file.RegularFile>\))(file: [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html)!>!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### transform

Added in 4.2.0

Deprecated in 7.0.0
    
    
    fun [transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))(transformInvocation: [TransformInvocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInvocation)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Executes the Transform. 

The inputs are packaged as an instance of `[TransformInvocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInvocation)`

  * The inputs collection of `[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)`. These are the inputs that are consumed by this Transform. A transformed version of these inputs must be written into the output. What is received is controlled through `[getInputTypes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getInputTypes\(\))`, and `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getScopes\(\))`.
  * The referencedInputs collection of `[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)`. This is for reference only and should be not be transformed. What is received is controlled through `[getReferencedScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getReferencedScopes\(\))`.

A transform that does not want to consume anything but instead just wants to see the content of some inputs should return an empty set in `[getScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getScopes\(\))`, and what it wants to see in `[getReferencedScopes](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getReferencedScopes\(\))`. 

Even though a transform's `[isIncremental](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#isIncremental\(\))` returns true, this method may be receive `false` in isIncremental. This can be due to 

  * a change in secondary files (`[getSecondaryFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFiles\(\))`, `[getSecondaryFileOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryFileOutputs\(\))`, `[getSecondaryDirectoryOutputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getSecondaryDirectoryOutputs\(\))`)
  * a change to a non file input (`[getParameterInputs](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#getParameterInputs\(\))`)
  * an unexpected change to the output files/directories. This should not happen unless tasks are improperly configured and clobber each other's output.
  * a file deletion that the transform mechanism could not match to a previous input. This should not happen in most case, except in some cases where dependencies have changed.

In such an event, when isIncremental is false, the inputs will not have any incremental change information: 

  * `[getStatus](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/JarInput#getStatus\(\))` will return `[NOTCHANGED](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Status#NOTCHANGED)` even though the file may be added/changed.
  * `[getChangedFiles](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/DirectoryInput#getChangedFiles\(\))` will return an empty map even though some files may be added/changed.



Parameters  
---  
`transformInvocation: [TransformInvocation](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInvocation)!` |  the invocation object containing the transform inputs.  
  
Throws  
---  
`[java.io.IOException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/IOException.html)` |  if an IO error occurs.  
`[java.lang.InterruptedException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/InterruptedException.html)` |   
`[com.android.build.api.transform.TransformException](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformException)` |  Generic exception encapsulating the cause.  
  
### transform

Added in 4.2.0

Deprecated in 4.2.0
    
    
    fun ~~[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.Context,java.util.Collection<com.android.build.api.transform.TransformInput>,java.util.Collection<com.android.build.api.transform.TransformInput>,com.android.build.api.transform.TransformOutputProvider,boolean\))~~(  
        context: [Context](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Context)!,  
        inputs: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)!>!,  
        referencedInputs: ([Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html))[Collection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-collection/index.html)<[TransformInput](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformInput)!>!,  
        outputProvider: [TransformOutputProvider](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformOutputProvider)!,  
        isIncremental: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


replaced by `[transform](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/Transform#transform\(com.android.build.api.transform.TransformInvocation\))`.

Throws  
---  
`[java.io.IOException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/IOException.html)` |   
`[com.android.build.api.transform.TransformException](https://developer.android.com/reference/tools/gradle-api/8.12/com/android/build/api/transform/TransformException)` |   
`[java.lang.InterruptedException](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/InterruptedException.html)` |   
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-05-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-20 UTC."],[],[]] 
