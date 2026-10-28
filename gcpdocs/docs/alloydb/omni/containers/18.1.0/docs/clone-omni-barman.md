---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/
title: Restore an AlloyDB Omni cluster using Barman \u00a0|\u00a0 AlloyDB Omni using containers: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:29:57.399387+00:00
---

# Restore an AlloyDB Omni cluster using Barman  |  AlloyDB Omni using containers: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Fcontainers%2F18.1.0%2Fdocs%2Fclone-omni-barman%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#prerequisites)
  * [Recover using a specific backup](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#specific)
  * [Recover to a specific point in time](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#pitr)


This page documents AlloyDB Omni version **18.1.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)


Was this helpful?
Send feedback 
#  Restore an AlloyDB Omni cluster using Barman Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#prerequisites)
  * [Recover using a specific backup](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#specific)
  * [Recover to a specific point in time](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#pitr)


Select a documentation version:  18.1.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/clone-omni-barman)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/clone-omni-barman)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/clone-omni-barman)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/clone-omni-barman)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/clone-omni-barman)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/clone-omni-barman)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/clone-omni-barman)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/clone-omni-barman)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/clone-omni-barman)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/clone-omni-barman)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/clone-omni-barman)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/clone-omni-barman)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/clone-omni-barman)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/clone-omni-barman)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/clone-omni-barman)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/clone-omni-barman)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/clone-omni-barman)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/clone-omni-barman)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/clone-omni-barman)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/clone-omni-barman)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/clone-omni-barman)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/clone-omni-barman)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/clone-omni-barman)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [Barman](https://pgbarman.org/), an open-source database backup server. 
Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the Barman manual](https://docs.pgbarman.org/release/latest/) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.
For more information about configuring Barman to work with AlloyDB Omni, see [Set up Barman for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-configure-barman).
## Before you begin
Before restoring your AlloyDB Omni data, you need the following:
  * A target database server, running the same major version of AlloyDB Omni as the source database server. For more information about installing AlloyDB Omni, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/deploy-vm).
The target server can be the same machine as the source server.
  * The `rsync` utility, installed on the target server.
  * A Barman backup server, with at least one valid Barman backup of the source AlloyDB Omni database on it.
  * SSH connectivity between the Barman backup server and the target server.
  * SSH keys set up to allow the `barman` user on the Barman server to authenticate with the target server as its `postgres` user without a password.
  * Enough free disk space on the target server to hold the restored database.


## Recover using a specific backup
  1. On the target server, stop AlloyDB Omni:
[ Docker ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#docker)[ Podman ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#podman) More

```
 docker stop CONTAINER_NAME
```

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it—for example, `my-omni`.

```
 podman stop CONTAINER_NAME
```

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it—for example, `my-omni`.
  2. On the Barman server, choose a backup to restore from. To see available backups, run [the `barman list-backups` command](https://docs.pgbarman.org/release/3.18.0/user_guide/catalog.html#list-backups). To see details about a particular backup, run [the `barman show-backup` command](https://docs.pgbarman.org/release/3.18.0/user_guide/catalog.html#show-backup).
  3. To recover the chosen backup into the target AlloyDB Omni server, run [the `barman recover` command](https://docs.pgbarman.org/release/3.18.0/user_guide/recovery.html).
When running the command, include the following:
     * Use [the remote recovery option](https://docs.pgbarman.org/release/3.18.0/user_guide/recovery.html#remote-recovery).
     * Specify the target server's data directory as the destination directory.
The following command demonstrates an example use of `barman recover` with AlloyDB Omni:

```
barman recover --remote-ssh-command "ssh postgres@TARGET_IP" TARGET_LABEL BACKUP_ID DATA_PATH
```

Replace the following:
     * `TARGET_IP`: the IP address of the target server.
     * `TARGET_LABEL`: the label that you assigned to the server in Barman's configuration file.
     * `BACKUP_ID`: the ID of the backup to restore from, identified in a previous step—for example, `20230810T210200`.
     * `DATA_PATH`: the path to the `data` subdirectory of the target server's data directory—for example, `/home/your-username/alloydb-data/data/18`.


  1. On the AlloyDB Omni target database server, start the service:
[ Docker ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#docker)[ Podman ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/clone-omni-barman/#podman) More

```
docker start CONTAINER_NAME
```

```
podman start CONTAINER_NAME
```



After the service restarts, connect to your AlloyDB Omni server. You should see your restored databases and data.
## Recover to a specific point in time
To perform a point-in-time recovery, follow the same steps listed in the previous section, with one modification. When you run the `barman recover` command, you must also specify one of the Barman [point-in-time recovery options](https://docs.pgbarman.org/release/3.18.0/user_guide/recovery.html#point-in-time-recovery).
The following command demonstrates an example use of `barman recover` with AlloyDB Omni with a point-in-time recovery option:

```
barman recover --remote-ssh-command "ssh postgres@TARGET_IP" TARGET_LABEL BACKUP_ID --target-time="TARGET_TIMESTAMP" DATA_PATH
```

Replace the following:
  * `TARGET_IP`: the IP address of the target server.
  * `TARGET_LABEL`: the label that you assigned to the server in Barman's configuration file.
  * `BACKUP_ID`: the ID of the backup to restore from, identified in a previous step—for example, `20230810T210200`.
  * `TARGET_TIMESTAMP`: the time to restore to, in any [PostgreSQL `timestamp` format](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-INPUT-TIME-STAMPS) that specifies both a date and a time—for example, `2024-02-06 00:00:00`.
  * `DATA_PATH`: the path to the `data` subdirectory of the target server's data directory—for example, `/home/your-username/alloydb-data/data/18`.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
