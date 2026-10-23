---
url: https://developer.android.com/tools/sqlite3/
title: sqlite3 \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:42.230007+00:00
---

# sqlite3  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/tools/sqlite3/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ SDK tools guides ](https://developer.android.com/tools)



#  sqlite3 Stay organized with collections  Save and categorize content based on your preferences. 

From a remote shell to your device or from your host machine, use the [`sqlite3`](https://www.sqlite.org/) command-line program to manage SQLite databases created by Android applications. The `sqlite3` tool includes many useful commands, such as `.dump` to print out the contents of a table and `.schema` to print the SQL CREATE statement for an existing table. The tool also gives you the ability to execute SQLite commands on the fly.

Refer to the [SQLite documentation](https://sqlite.org/docs.html) for full details. For additional documentation, visit [`sqlite3`](https://sqlite.org/cli.html) and the [SQL language specification](https://sqlite.org/lang.html) supported by SQLite.

To use `sqlite3` from a remote shell:

  1. Enter a remote shell by entering the following command: 
         
         adb [-d|-e|-s {<serialNumber>}] shell

  2. From the remote shell, start the `sqlite3` tool by entering the following command: 
         
         sqlite3

You can also optionally specify a full path to a database that you want to explore. Emulator/device instances store SQLite databases in the directory `/data/data/<package_name>/databases/`.

  3. Once you invoke `sqlite3`, you can issue commands in the shell. To exit and return to the adb remote shell, enter `exit` or press Control+D.



For example:
    
    
    $ adb -s emulator-5554 shell
    # sqlite3 /data/data/com.example.google.rss.rssexample/databases/rssitems.db
    SQLite version 3.3.12
    Enter ".help" for instructions
    _.... enter commands, then quit..._
    # sqlite> .exit
    

**Note:** You need root access to the file system to view files within the `/data/data` directory hierarchy. 

To use `sqlite3` locally, instead of within a shell, pull the database file from the device and start `sqlite3`:

  1. Copy a database file from your device to your host machine: 
         
         adb pull <database-file-on-device>
         

  2. Start the `sqlite3` tool, specifying the database file: 
         
         sqlite3 <database-file-on-host>
         




Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2023-04-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-04-12 UTC."],[],[]] 
