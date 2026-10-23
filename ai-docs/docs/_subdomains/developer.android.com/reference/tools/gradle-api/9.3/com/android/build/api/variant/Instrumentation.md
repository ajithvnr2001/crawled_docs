---
url: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation/
title: Instrumentation \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:36:44.632592+00:00
---

# Instrumentation  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Instrumentation

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/Instrumentation.kt+class:com.android.build.api.variant.Instrumentation)

Added in 7.2.0
    
    
    interface [Instrumentation](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation)

* * *

Options to register asm class visitors and to configure the instrumentation process.

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[setAsmFramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#setAsmFramesComputationMode\(com.android.build.api.instrumentation.FramesComputationMode\))(mode: [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode))` Sets the frame computation mode that will be applied to the bytecode of the classes instrumented by ASM visitors registered through `[transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<ParamT : [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationParameters)> [transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))(  
classVisitorFactoryImplClass: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory)<ParamT>>,  
scope: [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationScope),  
instrumentationParamsConfig: (ParamT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
)` Registers an asm class visitor to instrument the classes defined by the given scope.  
  
### Public properties  
  
---  
`[SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[excludes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#excludes\(\))` The set of glob patterns to exclude from instrumentation.  
  
## Public functions

### setAsmFramesComputationMode

Added in 7.2.0
    
    
    fun [setAsmFramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#setAsmFramesComputationMode\(com.android.build.api.instrumentation.FramesComputationMode\))(mode: [FramesComputationMode](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets the frame computation mode that will be applied to the bytecode of the classes instrumented by ASM visitors registered through `[transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))`. The default mode is to `[copy frames](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/FramesComputationMode#COPY_FRAMES)`.

When setting this multiple times, the mode with the highest enum value will be selected.

### transformClassesWith

Added in 7.2.0
    
    
    fun <ParamT : [InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationParameters)> [transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))(  
        classVisitorFactoryImplClass: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory)<ParamT>>,  
        scope: [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationScope),  
        instrumentationParamsConfig: (ParamT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Registers an asm class visitor to instrument the classes defined by the given scope. An instance of the factory will be instantiated and used to create visitors for each class.

Example:
    
    
    androidComponents {  
        onVariants(selector().all(), {  
            instrumentation.transformClassesWith(AsmClassVisitorFactoryImpl.class,  
                                                 InstrumentationScope.Project) { params ->  
                params.x = "value"  
            }  
            instrumentation.setAsmFramesComputationMode(COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS)  
        })  
    }

Parameters  
---  
`classVisitorFactoryImplClass: [Class](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Class.html)<[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory)<ParamT>>` |  the factory class implementing `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory)`  
`scope: [InstrumentationScope](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationScope)` |  either instrumenting the classes of the current project or the project and its dependencies  
`instrumentationParamsConfig: (ParamT) -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  the configuration function to be applied to the instantiated `[InstrumentationParameters](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/InstrumentationParameters)` object before passed to `[AsmClassVisitorFactory.createClassVisitor](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor\(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor\))`.  
  
## Public properties

### excludes

Added in 7.2.0
    
    
    val [excludes](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#excludes\(\)): [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of glob patterns to exclude from instrumentation. Classes matching any of these patterns in the project sources and dependencies jars do not get instrumented by any `[AsmClassVisitorFactory](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/instrumentation/AsmClassVisitorFactory)` registered via `[transformClassesWith](https://developer.android.com/reference/tools/gradle-api/9.3/com/android/build/api/variant/Instrumentation#transformClassesWith\(java.lang.Class,com.android.build.api.instrumentation.InstrumentationScope,kotlin.Function1\))`.

Do not add the file extension to the end as the filtration is done on compiled classes and the `.class` suffix is not included in the pattern matching.

Example usage:
    
    
    androidComponents {  
        onVariants(selector().all(), {  
            instrumentation.excludes.add("com`/`example`/`donotinstrument`/`**")  
            instrumentation.excludes.add("**`/`*Test")  
        })  
    }

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
