---
url: https://developer.android.com/training/data-storage/room/relationships/one-to-one/
title: Define and query one-to-one relationships \u00a0|\u00a0 App data and files \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:10.662542+00:00
---

# Define and query one-to-one relationships  |  App data and files  |  Android Developers

> Source: https://developer.android.com/training/data-storage/room/relationships/one-to-one/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ App data and files ](https://developer.android.com/training/data-storage)



#  Define and query one-to-one relationships Stay organized with collections  Save and categorize content based on your preferences. 

A _one-to-one relationship_ between two entities is a relationship where each instance of the parent entity corresponds to exactly one instance of the child entity, and the reverse is also true.

For example, consider a music streaming app where the user has a library of songs that they own. Each user has only one library, and each library corresponds to exactly one user. Therefore, there's a one-to-one relationship between the `User` entity and the `Library` entity.

Follow these steps to define and query one-to-one relationships in your database:

  1. **Define the relationship** : Create classes for both entities, and ensure that one references the other's primary key.
  2. **Query the entities** : Model the relationship in a new data class, and create a function to retrieve the related data.



## Define the relationship

To define a one-to-one relationship, first create a class for each of your two entities. One of the entities must include a variable that references the primary key of the other entity.
    
    
    @Entity
    data class User(
        @PrimaryKey val userId: Long,
        val name: String,
        val age: Int
    )
    
    @Entity
    data class Library(
        @PrimaryKey val libraryId: Long,
        val userOwnerId: Long
    )
    
    [OneToOneSimpleSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/onetoone/simple/OneToOneSimpleSnippets.kt#L30-L41)

## Query the entities

To query the list of users and corresponding libraries, you must first model the one-to-one relationship between the two entities.

To model the relationship, create a new data class where each instance holds an instance of the parent entity and the corresponding child entity. Add the [`@Relation`](https://developer.android.com/reference/kotlin/androidx/room3/Relation) annotation to the child entity. Set [`parentColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#parentColumns\(\)) to the name of the parent entity's primary key column, and set [`entityColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#entityColumns\(\)) to the name of the child entity's column that references the parent's primary key.
    
    
    data class UserAndLibrary(
        @Embedded val user: User,
        @Relation(
            parentColumns = ["userId"],
            entityColumns = ["userOwnerId"]
        )
        val library: Library
    )
    
    [OneToOneSimpleSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/onetoone/simple/OneToOneSimpleSnippets.kt#L45-L52)

Finally, add a function to the data access object (DAO) class that returns all instances of the data class that pairs the parent entity with the child entity. Add the [`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transaction) annotation to ensure that Room performs the entire operation atomically, because this function requires Room to run two queries.
    
    
    @Transaction
    @Query("SELECT * FROM User")
    suspend fun getUsersAndLibraries(): List<UserAndLibrary>
    
    [OneToOneSimpleSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/onetoone/simple/OneToOneSimpleSnippets.kt#L58-L60)

### Composite keys

If you define the relationship using composite keys, specify multiple columns in `parentColumns` and `entityColumns`. The order of columns in `parentColumns` must match the order of columns in `entityColumns`.
    
    
    @Entity(primaryKeys = ["firstName", "lastName"])
    data class User(
        val firstName: String,
        val lastName: String,
        val age: Int
    )
    
    @Entity
    data class Library(
        @PrimaryKey val libraryId: Long,
        val userFirstName: String,
        val userLastName: String
    )
    
    data class UserAndLibrary(
        @Embedded val user: User,
        @Relation(
            parentColumns = ["firstName", "lastName"],
            entityColumns = ["userFirstName", "userLastName"]
        )
        val library: Library
    )
    
    [OneToOneCompositeSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/onetoone/composite/OneToOneCompositeSnippets.kt#L27-L48)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
