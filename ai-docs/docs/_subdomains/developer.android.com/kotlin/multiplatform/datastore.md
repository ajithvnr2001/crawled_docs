---
url: https://developer.android.com/kotlin/multiplatform/datastore/
title: Set up DataStore for KMP \u00a0|\u00a0 Kotlin \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:29.889986+00:00
---

# Set up DataStore for KMP  |  Kotlin  |  Android Developers

> Source: https://developer.android.com/kotlin/multiplatform/datastore/

  * [ Android Developers ](https://developer.android.com/)
  * [ Get started ](https://developer.android.com/get-started/overview)
  * [ Kotlin ](https://developer.android.com/kotlin)
  * [ Guides ](https://developer.android.com/kotlin/first)



#  Set up DataStore for KMP Stay organized with collections  Save and categorize content based on your preferences. 

The DataStore library stores data asynchronously, consistently, and transactionally, overcoming some of the drawbacks of SharedPreferences. This page focuses on creating DataStore in Kotlin Multiplatform (KMP) projects. For more information on DataStore, see the [primary documentation for DataStore](https://developer.android.com/topic/libraries/architecture/datastore) and [official samples](https://github.com/android/kotlin-multiplatform-samples).

**Note:** Only [DataStore Preferences](https://developer.android.com/topic/libraries/architecture/datastore#preferences-datastore) is supported in KMP projects.

## Set up dependencies

**Note:** DataStore supports KMP in versions 1.1.0 and higher.

To set up DataStore in your KMP project, add the dependencies for the artifacts in the `build.gradle.kts` file for your module:
    
    
    commonMain.dependencies {
      // DataStore library
      implementation("androidx.datastore:datastore-core:1.2.1")
      // The Preferences DataStore library
      implementation("androidx.datastore:datastore-preferences-core:1.2.1")
    }
    

## Define the DataStore classes

You can define the `DataStore` class with `DataStoreFactory` inside the common source of your shared KMP module. Placing these classes in common sources allows them to be shared across all target platforms. You can use [`actual` and `expect` declarations](https://kotlinlang.org/docs/multiplatform-expect-actual.html) to create platform-specific implementations.

## Create the DataStore instance

You need to define how to instantiate the DataStore object on each platform. This is the only part of the API that is required to be in the specific platform source sets due to the differences in file system APIs.

### Common
    
    
    // shared/src/commonMain/kotlin/createDataStore.kt
    
    /**
     *   Gets the singleton DataStore instance, creating it if necessary.
     */
    fun createDataStore(storage: Storage<Preferences>): DataStore<Preferences> =
            DataStoreFactory.create(storage = storage)
    
    internal const val dataStoreFileName = "dice.preferences_pb"
    

### Android

To create the `DataStore` instance on Android, you need a [`Context`](https://developer.android.com/reference/android/content/Context) along with the path.
    
    
    // shared/src/androidMain/kotlin/createDataStore.android.kt
    
    fun createDataStore(): DataStore<Preferences> = createDataStore(
        storage = FileStorage(
            serializer = PreferencesSerializer,
            produceFile = { context.filesDir.resolve(dataStoreFileName) }
        )
    )
    

### iOS

On iOS, you can retrieve the path from the `NSDocumentDirectory`:
    
    
    // shared/src/iosMain/kotlin/createDataStore.ios.kt
    
    fun createDataStore(): DataStore<Preferences> = createDataStore(
        storage = OkioStorage(
            fileSystem = FileSystem.SYSTEM,
            serializer = PreferencesSerializer,
            producePath = {
                val documentDirectory: NSURL? = NSFileManager.defaultManager.URLForDirectory(
                    directory = NSDocumentDirectory,
                    inDomain = NSUserDomainMask,
                    appropriateForURL = null,
                    create = false,
                    error = null,
                )
                (requireNotNull(documentDirectory).path + "/$dataStoreFileName").toPath()
            }
        )
    )
    

### Web

To create the `DataStore` instance on Web, you can use `WebLocalStorage` or `WebSessionStorage`:
    
    
    // shared/src/jsMain/kotlin/createDataStore.web.kt (also works for wasmJsMain)
    
    fun createDataStore(): DataStore<Preferences> = createDataStore(
        storage = WebLocalStorage(
            serializer = PreferencesSerializer,
            name = dataStoreFileName
        )
    )
    

### JVM (Desktop)

To create the `DataStore` instance on JVM (Desktop), provide a path using Java or Kotlin APIs:
    
    
    // shared/src/jvmMain/kotlin/createDataStore.desktop.kt
    
    fun createDataStore(): DataStore<Preferences> = createDataStore(
        storage = FileStorage(
            serializer = PreferencesSerializer,
            produceFile = { File(System.getProperty("java.io.tmpdir"), dataStoreFileName) }
        )
    )
    

**Note:** `System.getProperty("java.io.tmpdir")` points to the temporary folder on the system, which might be cleaned upon reboot. On macOS, you can instead use the `~/Library/Application Support/[your-app]` folder.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
