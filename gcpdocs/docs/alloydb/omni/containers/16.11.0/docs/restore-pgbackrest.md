---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/
title: Restore an AlloyDB Omni cluster using pgBackRest \u00a0|\u00a0 AlloyDB Omni using containers: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:52:55.563785+00:00
---

# Restore an AlloyDB Omni cluster using pgBackRest  |  AlloyDB Omni using containers: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#prerequisites)
  * [Stop your AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#stop-container)
  * [Create idle AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#create-idle-container)
  * [Remove your data directory](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#remove-data-directory)
  * [Validate that your backups are visible](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#validate-backups)
  * [Restore your backup](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#restore-backup)
  * [Remove idle AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#remove-idle-container)
  * [Create AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#create-container)
  * [Validate that AlloyDB Omni started](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#validate-start)
  * [Other options](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#other)


This page documents AlloyDB Omni version **16.11.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/overview)


Send feedback 
#  Restore an AlloyDB Omni cluster using pgBackRest Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#prerequisites)
  * [Stop your AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#stop-container)
  * [Create idle AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#create-idle-container)
  * [Remove your data directory](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#remove-data-directory)
  * [Validate that your backups are visible](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#validate-backups)
  * [Restore your backup](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#restore-backup)
  * [Remove idle AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#remove-idle-container)
  * [Create AlloyDB Omni container](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#create-container)
  * [Validate that AlloyDB Omni started](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#validate-start)
  * [Other options](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#other)


Select a documentation version:  16.11.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/restore-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/restore-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/restore-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/restore-pgbackrest)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/restore-pgbackrest)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/restore-pgbackrest)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/restore-pgbackrest)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/restore-pgbackrest)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/restore-pgbackrest)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/restore-pgbackrest)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/restore-pgbackrest)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/restore-pgbackrest)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/restore-pgbackrest)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/restore-pgbackrest)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/restore-pgbackrest)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/restore-pgbackrest)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/restore-pgbackrest)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/restore-pgbackrest)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/restore-pgbackrest)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/restore-pgbackrest)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/restore-pgbackrest)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/restore-pgbackrest)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/restore-pgbackrest)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [pgBackRest](https://pgbackrest.org/), the open-source backup solution included with the AlloyDB Omni container. 
Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the pgBackRest manual](https://pgbackrest.org/user-guide-index.html) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.
For more information about configuring pgBackRest to work with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/set-up-pgbackrest).
For Kubernetes-based information, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/backup-kubernetes).
## Before you begin
Before restoring an AlloyDB Omni cluster, ensure that you have the following:
  * [Set up and configured pgBackRest](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/set-up-pgbackrest) for your AlloyDB Omni instance.
  * Sufficient disk space on destination file system to store the restored AlloyDB Omni database cluster.
  * Same major version of AlloyDB Omni used for the restoration container as the original source container.
To check your version of PostgreSQL, run the following command:
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker exec -u postgres CONTAINER_NAME psql -c "SELECT version();"

```

```
docker exec -u postgres CONTAINER_NAME psql -c "SELECT version();"

```

```
podman exec -u postgres CONTAINER_NAME psql -c "SELECT version();"

```

```
podman exec -u postgres CONTAINER_NAME psql -c "SELECT version();"

```

Replace the following variable:
    * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
To check your version of pgBackRest, run the following command:
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker exec -u postgres CONTAINER_NAME pgbackrest version

```

```
docker exec -u postgres CONTAINER_NAME pgbackrest version

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest version

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest version

```

Replace the following variable:
    * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
If your target container has a different version of PostgreSQL, pgBackRest, or both, then you need to create a new target container with a matching version. If this is not possible, then you need to use an alternative method, such as the PostgreSQL included `pg_dump` or `pg_dumpall` utilities to copy your databases across versions.


## Stop your AlloyDB Omni container
To simulate your AlloyDB Omni database cluster not being available, stop the container.
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker stop CONTAINER_NAME
docker rm CONTAINER_NAME
```

```
docker stop CONTAINER_NAME
docker rm CONTAINER_NAME
```

```
podman stop CONTAINER_NAME
podman rm CONTAINER_NAME
```

```
podman stop CONTAINER_NAME
podman rm CONTAINER_NAME
```

Replace the following variable:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.


## Create idle AlloyDB Omni container
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
google/alloydbomni:latest sleep infinity

```

```
docker run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
google/alloydbomni:latest sleep infinity

```

```
podman run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
docker.io/google/alloydbomni:latest sleep infinity

```

```
podman run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
docker.io/google/alloydbomni:latest sleep infinity

```

Replace the following variables:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `BACKUP_DIR`: External directory path that your backups are stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.


## Remove your data directory
To clear your AlloyDB Omni database cluster, remove the data directory.
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"

```

```
docker exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"

```

```
podman exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"

```

```
podman exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"

```

Replace the following variable:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.


## Validate that your backups are visible
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
info

```

```
docker exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
info

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
info

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
info

```

Replace the following variables:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`.


## Restore your backup
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
restore

```

```
docker exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
restore

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
restore

```

```
podman exec -u postgres CONTAINER_NAME pgbackrest \
--config-path=/var/lib/postgresql/backups \
--stanza=STANZA_NAME \
restore

```

Replace the following variables:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`.


## Remove idle AlloyDB Omni container
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker kill CONTAINER_NAME
docker rm CONTAINER_NAME
```

```
docker kill CONTAINER_NAME
docker rm CONTAINER_NAME
```

```
podman kill CONTAINER_NAME
podman rm CONTAINER_NAME
```

```
podman kill CONTAINER_NAME
podman rm CONTAINER_NAME
```

Replace the following variable:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.


## Create AlloyDB Omni container
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
google/alloydbomni:latest

```

```
docker run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
google/alloydbomni:latest

```

```
podman run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
docker.io/google/alloydbomni:latest

```

```
podman run -d --name CONTAINER_NAME \
-v DATA_DIR:/var/lib/postgresql/data \
-v BACKUP_DIR:/var/lib/postgresql/backups \
-p HOST_PORT:5432 \
--restart=always \
docker.io/google/alloydbomni:latest

```

Replace the following variables:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `BACKUP_DIR`: External directory path that your backups are stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.


## Validate that AlloyDB Omni started
[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootful)[Docker](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#docker-rootless)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootful)[Podman](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest/#podman-rootless) More

```
docker logs -f CONTAINER_NAME

```

```
docker logs -f CONTAINER_NAME

```

```
podman logs -f CONTAINER_NAME

```

```
podman logs -f CONTAINER_NAME

```

Replace the following variable:
  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.


## Other options
The pgBackRest `restore` command is very flexible, with an array of options and features that you can control through passing in different command-line options. For a complete guide to performing restores, see [Restore](https://pgbackrest.org/user-guide.html#restore).
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
