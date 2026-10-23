---
url: https://developer.android.com/codelabs/kmp-migrate-room/
title: Migrate existing apps to Room KMP \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:32.048991+00:00
---

# Migrate existing apps to Room KMP  |  Android Developers

> Source: https://developer.android.com/codelabs/kmp-migrate-room/

  * [ Android Developers ](https://developer.android.com/)



#  Migrate existing apps to Room KMP Stay organized with collections  Save and categorize content based on your preferences. 

##  1\. Before you begin 

## **Prerequisites**

  * Basic understanding of [Kotlin Multiplatform](https://developer.android.com/kotlin/multiplatform).
  * Experience with Kotlin.
  * Basic understanding of [Swift syntax](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html).
  * [Xcode and iOS simulator](https://developer.apple.com/documentation/safari-developer-tools/installing-xcode-and-simulators) installed.



## **What you need**

  * The latest [stable version of Android Studio](https://developer.android.com/studio/).
  * A Mac machine with a macOS system.
  * [Xcode 16.1](https://developer.apple.com/xcode/) and iPhone simulator with iOS 16.0 or higher.



## **What you learn**

  * How to share a Room Database between an Android app and an iOS app.



##  2\. Get set up 

To get started, follow these steps:

  1. Clone the GitHub repository with the following terminal command:


    
    
    $ git clone https://github.com/android/codelab-android-kmp.git
    

Alternatively, you can download the repository as a zip file:

[file_downloadDownload the starting point](https://github.com/android/codelab-android-kmp/archive/refs/heads/main.zip)

  2. In **Android Studio** , open the **`migrate-room`** project, which contains the following branches:


  * `main`: Contains the starter code for this project, where you make changes to complete the codelab.
  * `end`: Contains the solution code for this codelab.



**Note:** The git repository contains also other codelabs, use the **migrate-room** project.

We recommend that you begin with the `main` branch and follow the codelab step by step at your own pace.

  3. If you want to see the solution code, run this command:


    
    
    $ git clone -b end https://github.com/android/codelab-android-kmp.git
    

Alternatively, you can download the solution code:

[file_downloadDownload the final code](https://github.com/android/codelab-android-kmp/archive/refs/heads/end.zip)

##  3\. Understand the sample app 

This tutorial consists of the Fruitties sample application built in native frameworks (Jetpack Compose on Android, SwiftUi on iOS).

The Fruitties app offers two main features:

  * A list of _Fruit_ items, each with a button to add the item to a Cart.
  * A _Cart_ displayed at the top, showing how many fruits have been added and their quantities.



![4a7f262b015d7f78.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/4a7f262b015d7f78.png)

## **Android app architecture**

The Android app follows the official [Android architecture guidelines](https://developer.android.com/topic/architecture) to maintain a clear and modular structure.

![Architecture diagram of the Android application before KMP integration](https://developer.android.com/static/codelabs/kmp-migrate-room/img/8f9a3dafa1669d1e.png)

## **iOS app architecture**

![Architecture diagram of the iOS application before KMP integration](https://developer.android.com/static/codelabs/kmp-migrate-room/img/aba4991e8c672de8.png)

## **KMP Shared Module**

This project has already been set up with a shared module for KMP, although it is currently empty. If your project hasn't been set up with a shared module yet, start with the [Getting Started with Kotlin Multiplatform](https://developer.android.com/kmp-get-started) codelab.

##  4\. Prepare the Room database for KMP integration 

Before you move the Room database code from the Fruitties Android app to the `shared` module, you need to ensure that the app is compatible with Kotlin Multiplatform (KMP) Room APIs. This section walks you through that process.

One key update is using a SQLite driver compatible with both Android and iOS. To support Room database functionality across multiple platforms, you can use the `BundledSQLiteDriver`. This driver bundles SQLite directly into the application, making it suitable for multiplatform use in Kotlin. For detailed guidance, refer to the [Room KMP migration guide](https://developer.android.com/training/data-storage/room/room-kmp-migration#set_a_sqlite_driver).

**Important:** Using the `BundledSQLiteDriver` will increase the binary size on both Android and iOS.

## **Update dependencies**

First, add the `room-runtime` and `sqlite-bundled` dependencies to the `libs.versions.toml` file:
    
    
    # Add libraries
    [libraries]
    androidx-room-runtime = { module = "androidx.room:room-runtime", version.ref = "androidx-room" }
    
    androidx-sqlite-bundled = { module = "androidx.sqlite:sqlite-bundled", version.ref = "androidx-sqlite" }
    

Next, update the `build.gradle.kts` of the `:androidApp` module to use these dependencies, and remove use of `libs.androidx.room.ktx`:
    
    
    // Add
    implementation(libs.androidx.room.runtime)
    implementation(libs.androidx.sqlite.bundled)
    // Remove
    implementation(libs.androidx.room.ktx)
    

Now, sync the project in Android Studio.

## **Modify the database module for BundledSQLiteDriver**

Next, modify the database creation logic in the Android app to use the `BundledSQLiteDriver`, making it compatible with KMP while maintaining functionality on Android.

  1. Open the `DatabaseModule.kt` file located at `androidApp/src/main/kotlin/com/example/fruitties/kmptutorial/android/di/DatabaseModule.kt`
  2. Update the `providesAppDatabase` method as in the following snippet:


    
    
    import androidx.sqlite.driver.bundled.BundledSQLiteDriver
    
    @Module
    @InstallIn(SingletonComponent::class)
    internal object DatabaseModule {
    
    ...
    
    @Provides
    @Singleton
    fun providesAppDatabase(@ApplicationContext context: Context): AppDatabase {
        val dbFile = context.getDatabasePath("sharedfruits.db")
        return Room.databaseBuilder<AppDatabase>(context, dbFile.absolutePath)
            .setDriver(BundledSQLiteDriver())
            .build()
    }
    

## **Build and run the Android app**

Now that you switched the Native SQLite driver to the bundled one, let's verify the app builds and everything works correctly before you migrate the database to the `:shared` module.

##  5\. Move database code to the :shared module 

In this step, we'll transfer the Room database setup from the Android app to the `:shared` module, allowing the database to be accessible by both Android and iOS.

## Update the `build.gradle.kts` configuration of the `:shared` **module**

Start by updating the `build.gradle.kts` of the `:shared` module to use Room multiplatform dependencies.

  1. Add the KSP and Room plugins:


    
    
    plugins {
       ...
       // TODO add KSP + ROOM plugins
       alias(libs.plugins.ksp)
       alias(libs.plugins.room)
    }
    

  2. Add the `room-runtime` and `sqlite-bundled` dependencies to the `commonMain` block:


    
    
    sourceSets {
        commonMain {
            // TODO Add KMP dependencies here
            implementation(libs.androidx.room.runtime)
            implementation(libs.androidx.sqlite.bundled)
        }
    }
    

  3. Add KSP configuration for each platform target by adding a new top level `dependencies` block. For ease, you can just add it to the bottom of the file:


    
    
    // Should be its own top level block. For convenience, add at the bottom of the file
    dependencies {
       add("kspAndroid", libs.androidx.room.compiler)
       add("kspIosSimulatorArm64", libs.androidx.room.compiler)
       add("kspIosX64", libs.androidx.room.compiler)
       add("kspIosArm64", libs.androidx.room.compiler)
    }
    

**Note:** KSP dependencies are added with the `add(ksp[Target])` notation in multiplatform projects. [Check the documentation](https://kotlinlang.org/docs/ksp-multiplatform.html#avoid-the-ksp-configuration-on-ksp-1-0-1) for more information.

  4. Also at the top level, add a new block to set the `Room` schema location:


    
    
    // Should be its own top level block. For convenience, add at the bottom of the file
    room {
       schemaDirectory("$projectDir/schemas")
    }
    

  5. Gradle sync the project



## Move Room schema to `:shared` **module**

Move the `androidApp/schemas` directory to the `:shared` module root folder next to the `src/` folder:

From: ![e1ee37a3f3a10b35.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/e1ee37a3f3a10b35.png)

To: ![ba3c9eb617828bac.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/ba3c9eb617828bac.png)

## **Move DAOs and entities**

Now that you added the necessary Gradle dependencies to the KMP shared module, you need to move the DAOs and entities from the `:androidApp` module to the `:shared` module.

This will involve moving files to their respective locations in the `commonMain` source set in the `:shared` module.

### Move `Fruittie` **model**

You can leverage the **Refactor → Move** functionality to switch modules without breaking the imports:

**Note:** Alternatively, you can just drag the file into the appropriate source set in the `:shared` module, but using the refactor functionality is safer because it prevents breaking imports.

  1. Locate the `androidApp/src/main/kotlin/.../model/Fruittie.kt` file, right-click the file, and select **Refactor → Move** (or key **F6**)**:**![c893e12b8bf683ae.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/c893e12b8bf683ae.png)
  2. In the **Move** dialog, select the `...` icon next to the **Destination directory** field. ![1d51c3a410e8f2c3.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/1d51c3a410e8f2c3.png)
  3. Select the **commonMain** source set in the **Choose Destination Directory** dialog and click OK. You may have to disable the **Show only existing source roots** checkbox. ![f61561feb28a6445.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/f61561feb28a6445.png)
  4. Click the **Refactor** button to move the file.



### Move `CartItem` and `CartItemWithFruittie` **models**

For the file `androidApp/.../model/CartItem.kt` you need to follow these steps:

  1. Open the file, right-click the `CartItem` class, and select **Refactor > Move**.
  2. This opens the same **Move** dialog, but in this case you also check the box for the `CartItemWithFruittie` member.
  3. ![a25022cce5cee5e0.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/a25022cce5cee5e0.png)



Continue by selecting the `...` icon and selecting the `commonMain` source set just like you did for the `Fruittie.kt` file.

### Move DAOs and `AppDatabase`

Do the same steps for the following files (you can select all three at the same time):

  * `androidApp/.../database/FruittieDao.kt`
  * `androidApp/.../database/CartDao.kt`
  * `androidApp/.../database/AppDatabase.kt`



**Note:** You can sync and build your app at this point, to verify everything works as expected. In this case you just moved the entities and DAOs to the multiplatform module, but the Room database is still generated in the `androidApp` module.

## Update the shared `AppDatabase` **to work across platforms**

Now that you have the database classes moved to the `:shared` module, you need to adjust them to generate the required implementations on both platforms.

  1. Open the `/shared/src/commonMain/kotlin/com/example/fruitties/kmptutorial/android/database/AppDatabase.kt` file.
  2. Add the following implementation of `RoomDatabaseConstructor`:


    
    
    import androidx.room.RoomDatabaseConstructor
    
    // The Room compiler generates the `actual` implementations.
    @Suppress("NO_ACTUAL_FOR_EXPECT")
    expect object AppDatabaseConstructor : RoomDatabaseConstructor<AppDatabase> {
        override fun initialize(): AppDatabase
    }
    

  3. Annotate the `AppDatabase` class with `@ConstructedBy(AppDatabaseConstructor::class)`:


    
    
    import androidx.room.ConstructedBy
    
    @Database(
        entities = [Fruittie::class, CartItem::class],
        version = 1,
    )
    // TODO Add this line
    @ConstructedBy(AppDatabaseConstructor::class)
    abstract class AppDatabase : RoomDatabase() {
    ...
    

**Note:** You might see an error that there is "_No actual for expect declaration_ " for the `AppDatabaseConstructor`. This will be resolved in the following steps.

![410a3c0c656b6499.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/410a3c0c656b6499.png)

## Move database creation to `:shared` **module**

Next, you move the Android-specific Room setup from the `:androidApp` module to the `:shared` module. This is necessary because in the next step you will remove the `Room` dependency from the `:androidApp` module.

  1. Locate the `androidApp/.../di/DatabaseModule.kt` file.
  2. Select the content of the `providesAppDatabase` function, right-click, and select **Refactor** > **Extract Function to Scope** : ![da4d97319f9a0e8c.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/da4d97319f9a0e8c.png)
  3. Select `DatabaseModule.kt` from the menu. ![5e540a1eec6e3493.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/5e540a1eec6e3493.png) This moves the content to a global `appDatabase` function. Press **Enter** to confirm the function name. ![e2fb113d66704a36.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/e2fb113d66704a36.png)
  4. Make the function public by removing the `private` visibility modifier.
  5. Move the function into the `:shared` module by right-clicking **Refactor** > **Move.**
  6. In the **Move** dialog, select the **...** icon next to the **Destination directory** field. ![e2101005f2ef4747.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/e2101005f2ef4747.png)
  7. In the **Choose Destination Directory** dialog, select the **shared >androidMain** source set and select the **/shared/src/androidMain/** folder, then click **OK.**![73d244941c68dc85.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/73d244941c68dc85.png)
  8. Change the suffix in the **To package** field from `.di` to `.database`![ac5cf30d32871e2c.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/ac5cf30d32871e2c.png)
  9. Click **Refactor**.



**Note:** You're moving the `appDatabase` function to the **androidMain** source set, not to the **commonMain** source set.

## Clean up unneeded code from `:androidApp`

At this point, you moved the Room database to the multiplatform module and none of the Room dependencies are needed in the `:androidApp` module, so you can remove them.

  1. Open the `build.gradle.kts` file in the `:androidApp` module.
  2. Remove the dependencies and configuration as in the following snippet:


    
    
    plugins {
      // TODO Remove 
      alias(libs.plugins.room)
    }
    
    android {
      // TODO Remove
      ksp {
          arg("room.generateKotlin", "true")
      }
    
    dependencies {
      // TODO Keep room-runtime
      implementation(libs.androidx.room.runtime)
    
      // TODO Remove
      implementation(libs.androidx.sqlite.bundled)
      ksp(libs.androidx.room.compiler)
    }
    
    // TODO Remove
    room {
        schemaDirectory("$projectDir/schemas")
    }
    

**Note:** Keep the `room-runtime` dependency so that you can access the DAO classes in `androidApp`. If you introduced a domain layer on top of the DB objects, you wouldn't need to keep this dependency as the whole Room access would be encapsulated within the `:shared` module.

  3. Gradle sync the project.



## **Build and run the Android app**

Run the Fruitties Android app to ensure that the app runs properly and now uses the database from the `:shared` module. If you had cart items added before, then you should see the same items at this point as well even though the Room database is now located in the `:shared` module.

##  6\. Prepare Room for use on iOS 

To further prepare the Room database for the iOS platform, you need to set up some supporting code in the `:shared` module for use in the next step.

## **Enable database creation for iOS app**

The first thing to do is to add an iOS-specific database builder.

  1. Add a new file in the `:shared` module in the `iosMain` source set named `AppDatabase.ios.kt`: ![dcb46ba560298865.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/dcb46ba560298865.png)
  2. Add the following helper functions. These functions will be used by the iOS app to get an instance of the Room database.


    
    
    package com.example.fruitties.kmptutorial.shared
    
    import androidx.room.Room
    import androidx.sqlite.driver.bundled.BundledSQLiteDriver
    import com.example.fruitties.kmptutorial.android.database.AppDatabase
    import kotlinx.cinterop.BetaInteropApi
    import kotlinx.cinterop.ExperimentalForeignApi
    import kotlinx.cinterop.ObjCObjectVar
    import kotlinx.cinterop.alloc
    import kotlinx.cinterop.memScoped
    import kotlinx.cinterop.ptr
    import kotlinx.cinterop.value
    import platform.Foundation.NSDocumentDirectory
    import platform.Foundation.NSError
    import platform.Foundation.NSFileManager
    import platform.Foundation.NSUserDomainMask
    
    fun getPersistentDatabase(): AppDatabase {
        val dbFilePath = documentDirectory() + "/" + "fruits.db"
        return Room.databaseBuilder<AppDatabase>(name = dbFilePath)
           .setDriver(BundledSQLiteDriver())
           .build()
    }
    
    @OptIn(ExperimentalForeignApi::class, BetaInteropApi::class)
    private fun documentDirectory(): String {
        memScoped {
            val errorPtr = alloc<ObjCObjectVar<NSError?>>()
            val documentDirectory = NSFileManager.defaultManager.URLForDirectory(
                directory = NSDocumentDirectory,
                inDomain = NSUserDomainMask,
                appropriateForURL = null,
                create = false,
                error = errorPtr.ptr,
            )
            if (documentDirectory != null) {
                return requireNotNull(documentDirectory.path) {
                    """Couldn't determine the document directory.
                      URL $documentDirectory does not conform to RFC 1808.
                   """.trimIndent()
                }
            } else {
                val error = errorPtr.value
                val localizedDescription = error?.localizedDescription ?: "Unknown error occurred"
                error("Couldn't determine document directory. Error: $localizedDescription")
            }
        }
    }
    

## **Add "Entity" suffix to Room entities**

Because you're adding wrappers for the Room entities in Swift, it's best to have Room entities' names differ from the names of the wrappers. We'll make sure that's the case by adding the _Entity_ suffix to the Room entities using the `@ObjCName` annotation.

Open the `Fruittie.kt` file in the :`shared` module and add the `@ObjCName` annotation to the `Fruittie` entity. Since this annotation is experimental, you may need to add the `@OptIn(ExperimentalObjC::class)` annotation to the file.

### Fruittie.kt
    
    
    import kotlin.experimental.ExperimentalObjCName
    import kotlin.native.ObjCName
    
    @OptIn(ExperimentalObjCName::class)
    @Entity(indices = [Index(value = ["id"], unique = true)])
    @ObjCName("FruittieEntity")
    data class Fruittie(
       ...
    )
    

Then, do the same for the `CartItem` entity in the `CartItem.kt` file.

### CartItem.kt
    
    
    import kotlin.experimental.ExperimentalObjCName
    import kotlin.native.ObjCName
    
    @OptIn(ExperimentalObjCName::class)
    @ObjCName("CartItemEntity")
    @Entity(
       foreignKeys = [
           ForeignKey(
               entity = Fruittie::class,
               parentColumns = ["id"],
               childColumns = ["id"],
               onDelete = ForeignKey.CASCADE,
           ),
       ],
    )
    data class CartItem(@PrimaryKey val id: Long, val count: Int = 1)
    

##  7\. Use Room in the iOS app 

The iOS app is a pre-existing app that uses [Core Data](https://developer.apple.com/documentation/coredata#overview). In this codelab you won't worry about migrating any existing data in the database as this app is just a prototype. If you are migrating a production app to KMP, you will have to write functions to read the current Core Data database and insert those items into the Room database on first launch post-migration.

## **Open the Xcode project**

Open the iOS project in _Xcode_ by navigating to the `/iosApp/` folder and opening `Fruitties.xcodeproj` in the associated app.

![54836291a243ebe9.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/54836291a243ebe9.png)

## **Remove Core Data entity classes**

First, you need to remove the Core Data entity classes to make room for the entity wrappers you'll create later. Depending on the kind of data your application stores in Core Data, you may remove the Core Data entities entirely, or keep them for data migration purposes. For this tutorial you can just remove them, since you won't need to migrate any existing data.

In Xcode:

  1. Go to the Project Navigator.
  2. Go to the Resources folder.
  3. Open the `Fruitties` file.
  4. Click on and delete each entity.



![7ad742d991d76b1c.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/7ad742d991d76b1c.png)

To make these changes available in the code, clean and rebuild the project.

This will fail the build with the following errors, which is expected.

![e3e107bf0387eeab.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/e3e107bf0387eeab.png)

## **Creating entity wrappers**

Next, we'll create entity wrappers for the `Fruittie` and `CartItem` entities to smoothly handle the API differences between Room and Core Data entities.

These wrappers will help us transition from Core Data to Room by minimizing the amount of code that needs to be updated right away. You should aim to replace these wrappers with direct access to the Room entities in the future.

For now, we'll instead create a wrapper for the `FruittieEntity` class, giving it optional properties.

### Create `FruittieEntity` **wrapper**

  1. Create a new Swift file in the `Sources/Repository` directory by right-clicking the directory name and selecting **New File from Template...**![cce140b2fb3c2da8.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/cce140b2fb3c2da8.png)![6a0d4fa4292ddd4f.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/6a0d4fa4292ddd4f.png)
  2. Name it `Fruittie` and ensure that only the Fruitties target is selected, not the test target. ![827b9019b0a32352.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/827b9019b0a32352.png)
  3. Add the following code to the new Fruittie file:


    
    
    import sharedKit
    
    struct Fruittie: Hashable {
       let entity: FruittieEntity
    
       var id: Int64 {
           entity.id
       }
    
       var name: String? {
           entity.name
       }
    
       var fullName: String? {
           entity.fullName
       }
    }
    

The `Fruittie` struct wraps the `FruittieEntity` class, making the properties optional and passing through the entity's properties. Additionally we make the `Fruittie` struct conform to the `Hashable` protocol, so it can be used in SwiftUI's `ForEach` view.

### Create `CartItemEntity` **wrapper**

Next, create a similar wrapper for the `CartItemEntity` class.

Create a new Swift file called `CartItem.swift` in the `Sources/Repository` directory.
    
    
    import sharedKit
    
    struct CartItem: Hashable {
       let entity: CartItemWithFruittie
    
       let fruittie: Fruittie?
    
       var id: Int64 {
           entity.cartItem.id
       }
    
       var count: Int64 {
           Int64(entity.cartItem.count)
       }
    
       init(entity: CartItemWithFruittie) {
           self.entity = entity
           self.fruittie = Fruittie(entity: entity.fruittie)
       }
    }
    

Since the original Core Data `CartItem` class had a `Fruittie` property, we have included a `Fruittie` property in the `CartItem` struct as well. While the `CartItem` class doesn't have any properties that are optional, the `count` property has a different type in the Room entity.

## **Update repositories**

Now that the entity wrappers are in place, you need to update the `DefaultCartRepository` and `DefaultFruittieRepository` to use Room instead of Core Data.

### Update `DefaultCartRepository`

Let's begin with the `DefaultCartRepository` class as it's the simpler of the two.

Open the `CartRepository.swift` file in the `Sources/Repository` directory.

  1. First, replace the `CoreData` import with `sharedKit`:


    
    
    import sharedKit
    

  2. Then remove the `NSManagedObjectContext` property and replace it with a `CartDao` property:


    
    
    // Remove
    private let managedObjectContext: NSManagedObjectContext
    
    // Replace with
    private let cartDao: any CartDao
    

  3. Update the `init` constructor to initialise the new `cartDao` property:


    
    
    init(cartDao: any CartDao) {
        self.cartDao = cartDao
    }
    

  4. Next, update the `addToCart` method. This method needed to pull existing cart items from Core Data, but our Room implementation doesn't require this. Instead it will insert a new item or increment the count of an existing cart item.


    
    
    func addToCart(fruittie: Fruittie) async throws {
        try await cartDao.insertOrIncreaseCount(fruittie: fruittie.entity)
    }
    

  5. Lastly, update the `getCartItems()` method. This method will call the `getAll()` method on the `CartDao` and map the `CartItemWithFruittie` entities to our `CartItem` wrappers.


    
    
    func getCartItems() -> AsyncStream<[CartItem]> {
        return cartDao.getAll().map { entities in
            entities.map(CartItem.init(entity:))
        }.eraseToStream()
    }
    

**Note** : The call to `eraseToStream()` method in the `getCartItems()` method is provided by the `swift-concurrency-extras` library and is used to convert an `AsyncSequence` into an `AsyncStream`.

### Update `DefaultFruittieRepository`

To migrate the `DefaultFruittieRepository` class, we apply similar changes as we did for the `DefaultCartRepository`.

Update the FruittieRepository file to the following:
    
    
    import ConcurrencyExtras
    import sharedKit
    
    protocol FruittieRepository {
        func getData() -> AsyncStream<[Fruittie]>
    }
    
    class DefaultFruittieRepository: FruittieRepository {
        private let fruittieDao: any FruittieDao
        private let api: FruittieApi
    
        init(fruittieDao: any FruittieDao, api: FruittieApi) {
            self.fruittieDao = fruittieDao
            self.api = api
        }
    
        func getData() -> AsyncStream<[Fruittie]> {
            let dao = fruittieDao
            Task {
                let isEmpty = try await dao.count() == 0
                if isEmpty {
                    let response = try await api.getData(pageNumber: 0)
                    let fruitties = response.feed.map {
                        FruittieEntity(
                            id: 0,
                            name: $0.name,
                            fullName: $0.fullName,
                            calories: ""
                        )
                    }
                    _ = try await dao.insert(fruitties: fruitties)
                }
            }
            return dao.getAll().map { entities in
                entities.map(Fruittie.init(entity:))
            }.eraseToStream()
        }
    }
    

## Replace `@FetchRequest` **property wrappers**

We also need to replace the `@FetchRequest` property wrappers in the SwiftUI views. The `@FetchRequest` property wrapper is used to fetch data from Core Data and observe changes, so we can't use it with Room entities. Instead, let's use the UIModel to access the data from the repositories.

  1. Open the `CartView` in the `Sources/UI/CartView.swift` file.
  2. Replace the implementation with the following:


    
    
    import SwiftUI
    
    struct CartView : View {
        @State
        private var expanded = false
    
        @ObservedObject
        private(set) var uiModel: ContentViewModel
    
        var body: some View {
            if (uiModel.cartItems.isEmpty) {
                Text("Cart is empty, add some items").padding()
            } else {
                HStack {
                    Text("Cart has \(uiModel.cartItems.count) items (\(uiModel.cartItems.reduce(0) { $0 + $1.count }))")
                        .padding()
    
                    Spacer()
    
                    Button {
                        expanded.toggle()
                    } label: {
                        if (expanded) {
                            Text("collapse")
                        } else {
                            Text("expand")
                        }
                    }
                    .padding()
                }
                if (expanded) {
                    VStack {
                        ForEach(uiModel.cartItems, id: \.self) { item in
                            Text("\(item.fruittie!.name!): \(item.count)")
                        }
                    }
                }
            }
        }
    }
    

## Update the `ContentView`

Update the `ContentView` in the `Sources/View/ContentView.swift` file to pass the `FruittieUIModel` to the `CartView`.
    
    
    CartView(uiModel: uiModel)
    

## Updating **`DataController`**

The `DataController` class in the iOS application is responsible for setting up the Core Data stack. Since we're moving away from Core Data, we need to update the `DataController` to initialize the Room database instead.

  1. Open the `DataController.swift` file in `Sources/Database`.
  2. Add the `sharedKit` import.
  3. Remove the `CoreData` import.
  4. Instantiate the Room database in the `DataController` class.
  5. Lastly, remove the `loadPersistentStores` method call from the `DataController` initializer.



The final class should look like this:
    
    
    import Combine
    import sharedKit
    
    class DataController: ObservableObject {
        let database = getPersistentDatabase()
        init() {}
    }
    

## **Updating dependency injection**

The `AppContainer` class in the iOS application is responsible for initializing the dependency graph. Since we updated the repositories to use Room instead of Core Data, we need to update the `AppContainer` to pass Room DAOs to the repositories.

  1. Open the `AppContainer.swift` in the `Sources/DI` folder.
  2. Add the `sharedKit` import.
  3. Remove the `managedObjectContext` property from the `AppContainer` class.
  4. Change the `DefaultFruittieRepository` and `DefaultCartRepository` initializations by passing in Room DAOs from the `AppDatabase` instance provided by the `DataController`.



When you're done, the class will look like this:
    
    
    import Combine
    import Foundation
    import sharedKit
    
    class AppContainer: ObservableObject {
        let dataController: DataController
        let api: FruittieApi
        let fruittieRepository: FruittieRepository
        let cartRepository: CartRepository
    
        init() {
            dataController = DataController()
            api = FruittieNetworkApi(
                apiUrl: URL(
                    string:
                        "https://android.github.io/kotlin-multiplatform-samples/fruitties-api"
                )!)
            fruittieRepository = DefaultFruittieRepository(
                fruittieDao: dataController.database.fruittieDao(),
                api: api
            )
            cartRepository = DefaultCartRepository(
                        cartDao: dataController.database.cartDao()
            )
        }
    }
    

Finally, update `FruittiesApp` in `main.swift` to remove the `managedObjectContext`:
    
    
    struct FruittiesApp: App {
        @StateObject
        private var appContainer = AppContainer()
    
        var body: some Scene {
            WindowGroup {
                ContentView(appContainer: appContainer)
            }
        }
    }
    

## **Build and run the iOS app**

Finally, once you build and run the app by pressing ⌘R, the app should start with the database migrated from Core Data to Room.

![5d2ae9438747f8f6.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/5d2ae9438747f8f6.png)

##  8\. Congratulations 

Congratulations! You have successfully migrated standalone Android and iOS apps to a shared data layer using Room KMP.

For reference, here is the comparison of app architectures to see what was achieved:

### **Before**

**Android** | **iOS**  
---|---  
![Architecture diagram of the Android application before KMP integration](https://developer.android.com/static/codelabs/kmp-migrate-room/img/8f9a3dafa1669d1e.png) | ![Architecture diagram of the iOS application before KMP integration](https://developer.android.com/static/codelabs/kmp-migrate-room/img/aba4991e8c672de8.png)  
  
### **Post Migration Architecture**

![bcd8c29b00f67c19.png](https://developer.android.com/static/codelabs/kmp-migrate-room/img/bcd8c29b00f67c19.png)

## **Learn more**

  * Learn which other Jetpack libraries [support KMP](https://developer.android.com/kotlin/multiplatform).
  * Read the Room KMP [documentation](https://developer.android.com/kotlin/multiplatform/room).
  * Read the SQLite KMP [documentation](https://developer.android.com/kotlin/multiplatform/sqlite).
  * Check the official [Kotlin Multiplatform documentation](https://kotlinlang.org/docs/multiplatform-intro.html).



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
