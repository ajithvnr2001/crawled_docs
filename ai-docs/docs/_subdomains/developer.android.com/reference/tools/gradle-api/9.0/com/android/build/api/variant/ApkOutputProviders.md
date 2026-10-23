---
url: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders/
title: ApkOutputProviders \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:23:01.627424+00:00
---

# ApkOutputProviders  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# ApkOutputProviders

[View Source](https://cs.android.com/search?q=file:com/android/build/api/variant/ApkOutputProviders.kt+class:com.android.build.api.variant.ApkOutputProviders)

Added in 8.8.0
    
    
    interface [ApkOutputProviders](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders)

* * *

Provides APIs to obtain ordered collection of APK batches, each intended for local installation, facilitating staged installations.

As an example , let's take a Gradle `[org.gradle.api.Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)` that needs all the Apks for local deployment:
    
    
    abstract class FetchApkTask: DefaultTask() {  
      @get:Internal  
      abstract val apkOutput: Property<com.android.build.api.variant.ApkOutput>  
      
      @TaskAction  
      fun execute() {  
        def apkInstallGroups = apkOutput.apkInstallGroups  
            for(installGroup: installGroups) {  
                installOnDevice(installGroup.apks)  
           }  
      }  
    }  
      
    val taskProvider: TaskProvider<FetchApkTask> =  
        tasks.register("installAppApks", FetchApkTask::class.java)  
      
    androidComponents {  
       onVariants(selector().withName("debug")) { variant ->  
           val appVariant = variant as? ApplicationVariant  
           appVariant?.let {  
               it.outputProviders.provideApkOutputToTask(  
                    taskProvider,  
                    FetchApkTask::getOutput, '  
                    DeviceSpec("testDevice", 33, "", emptyList(), true)  
               )  
           }  
       }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `<TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [provideApkOutputToTask](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders#provideApkOutputToTask\(org.gradle.api.tasks.TaskProvider,kotlin.Function1,com.android.build.api.variant.DeviceSpec\))(  
taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>,  
taskInput: (TaskT) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[ApkOutput](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutput)>,  
deviceSpec: [DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec)  
)` Add Variant's Apk Output for a specific device specification to a Task.  
  
## Public functions

### provideApkOutputToTask

Added in 8.8.0
    
    
    fun <TaskT : [Task](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html)> [provideApkOutputToTask](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders#provideApkOutputToTask\(org.gradle.api.tasks.TaskProvider,kotlin.Function1,com.android.build.api.variant.DeviceSpec\))(  
        taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>,  
        taskInput: (TaskT) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[ApkOutput](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutput)>,  
        deviceSpec: [DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add Variant's Apk Output for a specific device specification to a Task. The Apk Output includes an ordered collection of batches of Apks to install on a device that matches the device specification available at the configuration time.

Parameters  
---  
`taskProvider: [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)<TaskT>` |  the `[TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)` returned by Gradle's Task manager when registering the Task of type `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders#provideApkOutputToTask\(org.gradle.api.tasks.TaskProvider,kotlin.Function1,com.android.build.api.variant.DeviceSpec\))`.  
`taskInput: (TaskT) -> [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)<[ApkOutput](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutput)>` |  The method reference the `[TaskT](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/ApkOutputProviders#provideApkOutputToTask\(org.gradle.api.tasks.TaskProvider,kotlin.Function1,com.android.build.api.variant.DeviceSpec\))` will use to retrieve the current artifact  
`deviceSpec: [DeviceSpec](https://developer.android.com/reference/tools/gradle-api/9.0/com/android/build/api/variant/DeviceSpec)` |  the device specification  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
