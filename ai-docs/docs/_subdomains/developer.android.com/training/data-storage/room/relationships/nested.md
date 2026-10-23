---
url: https://developer.android.com/training/data-storage/room/relationships/nested/
title: Define and query nested relationships \u00a0|\u00a0 App data and files \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:11.198069+00:00
---

# Define and query nested relationships  |  App data and files  |  Android Developers

> Source: https://developer.android.com/training/data-storage/room/relationships/nested/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ App data and files ](https://developer.android.com/training/data-storage)



#  Define and query nested relationships Stay organized with collections  Save and categorize content based on your preferences. 

Sometimes, you might need to query a set of three or more tables that are all related to each other. In that case, you define _nested relationships_ between the tables.

**Caution:** Querying data with nested relationships requires Room to manipulate a large volume of data and can affect performance. Use as few nested relationships as possible in your queries.

Suppose that in the music streaming app example, you want to query all the users, all the playlists for each user, and all the songs in each playlist for each user. Users have a [one-to-many relationship](https://developer.android.com/training/data-storage/room/relationships/one-to-many) with playlists, and playlists have a [many-to-many relationship](https://developer.android.com/training/data-storage/room/relationships/many-to-many) with songs. The following code example shows the classes that represent these entities as well as the cross-reference table for the many-to-many relationship between playlists and songs:
    
    
    @Entity
    data class User(
        @PrimaryKey val userId: Long,
        val name: String,
        val age: Int
    )
    
    @Entity
    data class Playlist(
        @PrimaryKey val playlistId: Long,
        val userCreatorId: Long,
        val playlistName: String
    )
    
    @Entity
    data class Song(
        @PrimaryKey val songId: Long,
        val songName: String,
        val artist: String
    )
    
    @Entity(primaryKeys = ["playlistId", "songId"], indices = [Index("playlistId", "songId")])
    data class PlaylistSongCrossRef(
        val playlistId: Long,
        val songId: Long
    )
    
    [NestedRelationshipsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/nested/NestedRelationshipsSnippets.kt#L32-L57)

First, model the relationship between two of the tables in your set as you normally do, using a data class and the [`@Relation`](https://developer.android.com/reference/kotlin/androidx/room3/Relation) annotation. The following example shows a `PlaylistWithSongs` class that models a many-to-many relationship between the `Playlist` entity class and the `Song` entity class:
    
    
    data class PlaylistWithSongs(
        @Embedded val playlist: Playlist,
        @Relation(
            parentColumns = ["playlistId"],
            entityColumns = ["songId"],
            associateBy = Junction(PlaylistSongCrossRef::class)
        )
        val songs: List<Song>
    )
    
    [NestedRelationshipsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/nested/NestedRelationshipsSnippets.kt#L61-L69)

After you define a data class that represents this relationship, create another data class that models the relationship between another table from your set and the first relationship class, "nesting" the existing relationship within the new one. The following example shows a `UserWithPlaylistsAndSongs` class that models a one-to-many relationship between the `User` entity class and the `PlaylistWithSongs` relationship class:
    
    
    data class UserWithPlaylistsAndSongs(
        @Embedded val user: User,
        @Relation(
            entity = Playlist::class,
            parentColumns = ["userId"],
            entityColumns = ["userCreatorId"]
        )
        val playlists: List<PlaylistWithSongs>
    )
    
    [NestedRelationshipsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/nested/NestedRelationshipsSnippets.kt#L73-L81)

The `UserWithPlaylistsAndSongs` class indirectly models the relationships between all three of the entity classes: `User`, `Playlist`, and `Song`. This is illustrated in figure 1.

![UserWithPlaylistsAndSongs models the relationship between User and
  PlaylistWithSongs, which in turn models the relationship between Playlist
  and Song.](https://developer.android.com/static/images/training/data-storage/room_nested_relationships.png)**Figure 1.** Diagram of relationship classes in the music streaming app example.

If your set has more tables, create a class to model the relationship between each remaining table and the previous relationship class. This process creates a chain of nested relationships among all tables you want to query.

Finally, add a function to the data access object (DAO) class to expose the query function that your app needs. This function requires Room to run multiple queries, so add the [`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transaction) annotation so that the whole operation runs atomically:
    
    
    @Transaction
    @Query("SELECT * FROM User")
    suspend fun getUsersWithPlaylistsAndSongs(): List<UserWithPlaylistsAndSongs>
    
    [NestedRelationshipsSnippets.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/room/src/main/java/com/example/snippets/room/relationships/nested/NestedRelationshipsSnippets.kt#L87-L89)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
