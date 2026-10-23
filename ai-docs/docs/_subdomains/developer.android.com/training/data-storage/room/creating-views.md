---
url: https://developer.android.com/training/data-storage/room/creating-views/
title: Create views into a database \u00a0|\u00a0 App data and files \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:12.596406+00:00
---

# Create views into a database  |  App data and files  |  Android Developers

> Source: https://developer.android.com/training/data-storage/room/creating-views/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ App data and files ](https://developer.android.com/training/data-storage)



#  Create views into a database Stay organized with collections  Save and categorize content based on your preferences. 

The [Room persistence library](https://developer.android.com/training/data-storage/room) supports [SQLite database views](https://www.sqlite.org/lang_createview.html), which let you encapsulate a query in a class. Room refers to these query-backed classes as _views_ , and you can use them as data objects in a [data access object (DAO)](https://developer.android.com/training/data-storage/room/accessing-data).

**Note:** Like [entities](https://developer.android.com/training/data-storage/room/defining-data), you can run `SELECT` statements against views. However, you can't run `INSERT`, `UPDATE`, or `DELETE` statements against views.

## Create a view

To create a view, add the [`@DatabaseView`](https://developer.android.com/reference/kotlin/androidx/room3/DatabaseView) annotation to a class. Set the annotation value to the query that the class represents.

The following code snippet provides an example of a view:
    
    
    @DatabaseView(
        """
        SELECT User.id, User.name, User.departmentId, Department.name AS departmentName
        FROM User INNER JOIN Department ON User.departmentId = Department.id
        """
    )
    data class UserDetail(
        val id: Long,
        val name: String?,
        val departmentId: Long,
        val departmentName: String?
    )
    
    [CreatingViewsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/creatingviews/CreatingViewsSnippets.kt#L43-L54)

## Associate a view with your database

To include this view in your database, add the [`views`](https://developer.android.com/reference/kotlin/androidx/room3/Database#views\(\)) property to your app's `@Database` annotation:
    
    
    @Database(
        entities = [User::class, Department::class],
        views = [UserDetail::class],
        version = 1
    )
    abstract class AppDatabase : RoomDatabase() {
        abstract fun userDao(): UserDao
    }
    
    [CreatingViewsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/creatingviews/CreatingViewsSnippets.kt#L58-L65)

[ Previous arrow_back  Write asynchronous DAO queries  ](https://developer.android.com/training/data-storage/room/async-queries)

[ Next Prepopulate your database  arrow_forward  ](https://developer.android.com/training/data-storage/room/prepopulate)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
