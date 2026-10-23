---
url: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory/
title: AsmClassVisitorFactory \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:57:13.188217+00:00
---

# AsmClassVisitorFactory  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# AsmClassVisitorFactory

[View Source](https://cs.android.com/search?q=file:com/android/build/api/instrumentation/AsmClassVisitorFactory.kt+class:com.android.build.api.instrumentation.AsmClassVisitorFactory)

Added in 4.2.0
    
    
    interface [AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory)<ParametersT : [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/InstrumentationParameters)> : [Serializable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/Serializable.html)

* * *

A factory to create class visitor objects to instrument classes.

The implementation of this interface must be an abstract class where the `[parameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#parameters\(\))` and `[instrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#instrumentationContext\(\))` are left unimplemented. The class must have an empty constructor which will be used to construct the factory object.

## Summary

### Public functions  
  
---  
`[ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` |  `[createClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))(  
classContext: [ClassContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/ClassContext),  
nextClassVisitor: [ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)  
)` Creates a class visitor object that will visit a class with the given `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isInstrumentable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#isInstrumentable\(com.android.build.api.instrumentation.ClassData\))(classData: [ClassData](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/ClassData))` Whether the factory wants to instrument the class with the given `[classData](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#isInstrumentable\(com.android.build.api.instrumentation.ClassData\))`.  
  
### Public properties  
  
---  
`[InstrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/InstrumentationContext)` |  `[instrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#instrumentationContext\(\))` Contains parameters to help instantiate the visitor objects.  
`[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<ParametersT>` |  `[parameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#parameters\(\))` The parameters that will be instantiated, configured using the given config when registering the visitor, and injected on instantiation.  
  
## Public functions

### createClassVisitor

Added in 4.2.0
    
    
    fun [createClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))(  
        classContext: [ClassContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/ClassContext),  
        nextClassVisitor: [ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)  
    ): [ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)

Creates a class visitor object that will visit a class with the given `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`. The returned class visitor must delegate its calls to `[nextClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`. If at this point the factory is not interested in instrumenting the class with given `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`, then return `[nextClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`.

The given `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))` contains static information about the classes before starting the instrumentation process. Any changes in interfaces or superclasses for the class with the given `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))` or for any other class in its classpath by a previous visitor will not be reflected in the `[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))` object.

`[classContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))` can also be used to get the data for classes that are in the runtime classpath of the class being visited.

This method must handle asynchronous calls.

Parameters  
---  
`classContext: [ClassContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/ClassContext)` |  contains information about the class that will be instrumented by the returned class visitor.  
`nextClassVisitor: [ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` |  the `[ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` to which the created `[ClassVisitor](https://asm.ow2.io/javadoc/org/objectweb/asm/ClassVisitor.html)` must delegate method calls.  
  
### isInstrumentable

Added in 4.2.0
    
    
    fun [isInstrumentable](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#isInstrumentable\(com.android.build.api.instrumentation.ClassData\))(classData: [ClassData](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/ClassData)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether the factory wants to instrument the class with the given `[classData](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#isInstrumentable\(com.android.build.api.instrumentation.ClassData\))`.

If returned true, `[createClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))` will be called and the returned class visitor will visit the class.

This method must handle asynchronous calls.

## Public properties

### instrumentationContext

Added in 4.2.0
    
    
    val [instrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#instrumentationContext\(\)): [InstrumentationContext](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/InstrumentationContext)

Contains parameters to help instantiate the visitor objects.

This field must be left unimplemented.

### parameters

Added in 4.2.0
    
    
    val [parameters](https://developer.android.com/reference/tools/gradle-api/9.4/com/android/build/api/instrumentation/AsmClassVisitorFactory#parameters\(\)): [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<ParametersT>

The parameters that will be instantiated, configured using the given config when registering the visitor, and injected on instantiation.

This field must be left unimplemented.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
