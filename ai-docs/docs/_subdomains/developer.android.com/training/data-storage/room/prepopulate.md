---
url: https://developer.android.com/training/data-storage/room/prepopulate/
title: Prepopulate your Room database \u00a0|\u00a0 App data and files \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:14.370907+00:00
---

# Prepopulate your Room database  |  App data and files  |  Android Developers

> Source: https://developer.android.com/training/data-storage/room/prepopulate/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ App data and files ](https://developer.android.com/training/data-storage)



#  Prepopulate your Room database Stay organized with collections  Save and categorize content based on your preferences. 

If you want your app to start with a database that's already loaded with a specific set of data, you can prepopulate the database. In Room, you can use APIs to prepopulate a database at initialization with contents from a prepackaged database file in the device's file system.

**Note:** [In-memory Room databases](https://developer.android.com/reference/kotlin/androidx/room3/Room#inmemorydatabasebuilder) don't support prepopulating the database using [`createFromAsset`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromasset) or [`createFromFile`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromfile).

## Prepopulate from an app asset

To prepopulate a Room database from a prepackaged database file that's located anywhere in your app's `assets/` directory, call the [`createFromAsset`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromasset) function from your `RoomDatabase.Builder` object before calling [`build`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#build):
    
    
    Room.databaseBuilder<AppDatabase>(appContext, "sample.db")
        .createFromAsset("database/myapp.db")
        .build()
    
    [PrepopulateSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/prepopulate/PrepopulateSnippets.kt#L37-L39)

The `createFromAsset` function accepts a string argument that contains a relative path from the `assets/` directory to the prepackaged database file.

**Note:** When prepopulating from an asset, Room validates the database to ensure that its schema matches the schema of the prepackaged database. To use your database's schema as a reference when you create the prepackaged database file, [export the schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schemas).

## Prepopulate from the file system

To prepopulate a Room database from a prepackaged database file that's located anywhere in the device's file system _except_ your app's `assets/` directory, call the [`createFromFile`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromfile) function from your `RoomDatabase.Builder` object before calling [`build`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#build):
    
    
    Room.databaseBuilder<AppDatabase>(appContext, "sample.db")
        .createFromFile(File("mypath"))
        .build()
    
    [PrepopulateSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/prepopulate/PrepopulateSnippets.kt#L43-L45)

The `createFromFile` function accepts a [`File`](https://developer.android.com/reference/java/io/File) argument for the prepackaged database file. Room creates a copy of the designated file rather than opening it directly, so make sure your app has read permissions on the file.

**Note:** When prepopulating from the file system, Room validates the database to ensure that its schema matches the schema of the prepackaged database. To use your database's schema as a reference when you create the prepackaged database file, [export the schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schemas).

## Handle migrations that include prepackaged databases

Prepackaged database files can also change the way your Room database handles fallback migrations. Ordinarily, when [destructive migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#handle-missing-migrations) are enabled and Room must perform a migration without a migration path, Room drops all tables in the database and creates an empty database with the specified schema for the target version. However, if you include a prepackaged database file with the same number as the target version, Room populates the newly recreated database with the contents of the prepackaged database file after performing the destructive migration.

For more information about Room database migrations, see [Migrate your Room database](https://developer.android.com/training/data-storage/room/migrating-db-versions).

The following sections present a few examples of how this works in practice.

### Example: Fallback migration with a prepackaged database

Suppose the following:

  * Your app defines a Room database on version 3.
  * The database instance that's already installed on the device is on version 2.
  * There's a prepackaged database file that's on version 3.
  * There's no implemented migration path from version 2 to version 3.
  * Destructive migrations are enabled.


    
    
    // Database class definition declaring version 3.
    @Database(entities = [SampleEntity::class], version = 3)
    abstract class FallbackAppDatabase : RoomDatabase() {
        // ...
    }
    
    fun createFallbackDb(appContext: Context) {
        Room.databaseBuilder<FallbackAppDatabase>(appContext, "sample.db")
            .createFromAsset("database/myapp.db")
            .fallbackToDestructiveMigration()
            .build()
    }
    
    [PrepopulateSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/prepopulate/PrepopulateSnippets.kt#L50-L61)

Here's what happens in this situation:

  1. Because the database defined in your app is on version 3 and the database instance already installed on the device is on version 2, a migration is necessary.
  2. Because there's no implemented migration plan from version 2 to version 3, the migration is a fallback migration.
  3. Because you call the [`fallbackToDestructiveMigration`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#fallbacktodestructivemigration) builder function, the fallback migration is destructive. Room drops the database instance that's installed on the device.
  4. Because there's a prepackaged database file that's on version 3, Room recreates the database and populates it using the contents of the prepackaged database file. If your prepackaged database file is on version 2, Room determines that it doesn't match the target version and doesn't use it for the fallback migration.



### Example: Implemented migration with a prepackaged database

Suppose instead that your app implements a migration path from version 2 to version 3:
    
    
    // Database class definition declaring version 3.
    @Database(entities = [SampleEntity::class], version = 3)
    abstract class ImplementedAppDatabase : RoomDatabase() {
        // ...
    }
    
    // Migration path definition from version 2 to version 3.
    val MIGRATION_2_3 = object : Migration(2, 3) {
        override suspend fun migrate(connection: SQLiteConnection) {
            // ...
        }
    }
    
    fun createImplementedDb(appContext: Context) {
        Room.databaseBuilder<ImplementedAppDatabase>(appContext, "sample.db")
            .createFromAsset("database/myapp.db")
            .addMigrations(MIGRATION_2_3)
            .build()
    }
    
    [PrepopulateSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/prepopulate/PrepopulateSnippets.kt#L65-L83)

Here's what happens in this situation:

  1. Because the database defined in your app is on version 3 and the database already installed on the device is on version 2, a migration is necessary.
  2. Because there's an implemented migration path from version 2 to version 3, Room runs the defined [`migrate`](https://developer.android.com/reference/kotlin/androidx/room3/migration/Migration#migrate) function to update the database instance on the device to version 3, preserving the data that's already in the database. Room doesn't use the prepackaged database file, because Room uses prepackaged database files only in the case of a fallback migration.



### Example: Multi-step migration with a prepackaged database

Prepackaged database files can also affect migrations that consist of multiple steps. Consider the following case:

  * Your app defines a Room database on version 4.
  * The database instance that's already installed on the device is on version 2.
  * There's a prepackaged database file that's on version 3.
  * There's an implemented migration path from version 3 to version 4, but not from version 2 to version 3.
  * Destructive migrations are enabled.


    
    
    // Database class definition declaring version 4.
    @Database(entities = [SampleEntity::class], version = 4)
    abstract class MultiStepAppDatabase : RoomDatabase() {
        // ...
    }
    
    val MIGRATION_3_4 = object : Migration(3, 4) {
        override suspend fun migrate(connection: SQLiteConnection) {
            // ...
        }
    }
    
    fun createMultiStepDb(appContext: Context) {
        Room.databaseBuilder<MultiStepAppDatabase>(appContext, "sample.db")
            .createFromAsset("database/myapp.db")
            .addMigrations(MIGRATION_3_4)
            .fallbackToDestructiveMigration()
            .build()
    }
    
    [PrepopulateSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/prepopulate/PrepopulateSnippets.kt#L87-L105)

Here's what happens in this situation:

  1. Because the database defined in your app is on version 4 and the database instance already installed on the device is on version 2, a migration is necessary.
  2. Because there's no implemented migration path from version 2 to version 3, the migration is a fallback migration.
  3. Because you call the [`fallbackToDestructiveMigration`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#fallbacktodestructivemigration) builder function, the fallback migration is destructive. Room drops the database instance on the device.
  4. Because there's a prepackaged database file that's on version 3, Room recreates the database and populates it using the contents of the prepackaged database file.
  5. The database installed on the device is now on version 3. Because it's still lower than the version defined in your app, another migration is necessary.
  6. Because there's an implemented migration path from version 3 to version 4, Room runs the defined [`migrate`](https://developer.android.com/reference/kotlin/androidx/room3/migration/Migration#migrate) function to update the database instance on the device to version 4, preserving the data that was copied over from the version 3 prepackaged database file.



[ Previous arrow_back  Create views into a database  ](https://developer.android.com/training/data-storage/room/creating-views)

[ Next Migrate your database  arrow_forward  ](https://developer.android.com/training/data-storage/room/migrating-db-versions)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
