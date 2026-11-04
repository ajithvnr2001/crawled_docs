---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-containers-database-minor-version/
title: Perform a minor version upgrade for AlloyDB Omni using containers \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:07.542777+00:00
---

# Perform a minor version upgrade for AlloyDB Omni using containers  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-containers-database-minor-version/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Perform a minor version upgrade for AlloyDB Omni using containers Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/upgrade-containers-database-minor-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/upgrade-containers-database-minor-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/upgrade-containers-database-minor-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/upgrade-containers-database-minor-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/upgrade-containers-database-minor-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/upgrade-containers-database-minor-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/upgrade-containers-database-minor-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/upgrade-containers-database-minor-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/upgrade-containers-database-minor-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/upgrade-containers-database-minor-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/upgrade-containers-database-minor-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/upgrade-containers-database-minor-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/upgrade-containers-database-minor-version)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-containers-database-minor-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/upgrade-containers-database-minor-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/upgrade-containers-database-minor-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/upgrade-containers-database-minor-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/upgrade-containers-database-minor-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/upgrade-containers-database-minor-version)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-containers-database-minor-version)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/upgrade-containers-database-minor-version)

To apply bug fixes, security patches, and minor enhancements without migrating your data, perform a minor database version upgrade for AlloyDB Omni by replacing the container image with a later minor version image in the same major version track. Minor version upgrades preserve your existing host data directory and configuration files, and let you verify the upgraded installation or roll back to an earlier minor version if needed. 

To upgrade between major PostgreSQL versions, see [Upgrade AlloyDB Omni on a VM](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-vm-alloydb-omni-version). 

The instructions on this page apply to standalone single-node deployments and to individual database nodes in multi-node topologies, such as deployments with [read replicas](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/set-up-read-replica) or [high-availability standby nodes](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/high-availability/setup). Review the following considerations based on your setup:

  * **External data directory:** Before you stop and remove a container, confirm that your database data is stored in a persistent host directory mounted into the container (for example, `-v DATA_DIR:/var/lib/postgresql/data`). Removing a container that stores data only inside the container file system deletes your database data. For more information, see [Install AlloyDB Omni using containers](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/deploy-vm#create-directory).
  * **Multi-node topologies:** Always upgrade all replica and standby nodes before you upgrade the primary node. In a high-availability setup, pause automatic failover or failure detection before stopping containers, and perform a switchover to an upgraded standby node before you upgrade the former primary node.
  * **Custom container images with extensions:** If you built a custom container image with third-party extensions such as [PostGIS](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-postgis) or [Orafce](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-orafce), rebuild your custom container image by using the updated minor version base image before you recreate the container.



## Before you begin

Before you upgrade AlloyDB Omni, complete the following steps:

  1. Plan a maintenance window or brief service downtime because replacing the container requires temporarily stopping the database service.
  2. Take a full backup of your database before you begin the upgrade. For more information, see [Back up and restore overview](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/backup-overview).
  3. If you're upgrading a multi-node topology, identify the current primary node and all standby or replica nodes so that you can upgrade the standby and replica nodes first.
  4. Inspect your running container to record its current image, host data directory mount, port mappings, environment variables, and runtime flags so that you can recreate the container with the same configuration:

###  Docker 
         
         docker inspect CONTAINER_NAME

###  Podman 
         
         podman inspect CONTAINER_NAME

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container—for example, `my-omni`.

  5. Check your current AlloyDB Omni database version before upgrading:

###  Docker 
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"

###  Podman 
         
         podman exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"




## Pull the updated container image

Pull the target minor version container image to your host machine:

###  Docker 
    
    
    docker pull IMAGE_URI

###  Podman 
    
    
    podman pull IMAGE_URI

Replace `IMAGE_URI` with the container image URI and minor version tag that you want to upgrade to—for example, `google/alloydbomni:15.7.1` for the Debian image or `google/alloydbomni:15.7.1-ubi9` for the Red Hat Universal Base Image (UBI).

If your deployment uses a custom container image with extensions such as [PostGIS](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-postgis) or [Orafce](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-orafce), update the `FROM` instruction or the `OMNI_VERSION` build argument in your `Dockerfile` to reference the updated minor version tag, and then build the updated custom image before proceeding.

## Upgrade AlloyDB Omni

To upgrade your AlloyDB Omni installation to a later minor version, complete the following steps on each node. In a multi-node topology, complete these steps on each standby or replica node before you upgrade the primary node:

  1. Stop and remove the existing AlloyDB Omni container:

###  Docker 
         
         docker container stop CONTAINER_NAME
         docker container rm CONTAINER_NAME

###  Podman 
         
         podman container stop CONTAINER_NAME
         podman container rm CONTAINER_NAME

Stopping and removing the container doesn't affect your database files in the mounted host data directory.

  2. Recreate and start the AlloyDB Omni container by using the updated minor version image and mounting your existing host data directory:

###  Docker 
         
         docker run -d --name CONTAINER_NAME \
           -e POSTGRES_PASSWORD=PASSWORD \
           -v DATA_DIR:/var/lib/postgresql/data \
           -p HOST_PORT:5432 \
           --restart=always \
           IMAGE_URI

###  Podman 
         
         podman run -d --name CONTAINER_NAME \
           -e POSTGRES_PASSWORD=PASSWORD \
           -v DATA_DIR:/var/lib/postgresql/data \
           -p HOST_PORT:5432 \
           --restart=always \
           IMAGE_URI

Replace the following:

     * `CONTAINER_NAME`: the name of your AlloyDB Omni container—for example, `my-omni`.
     * `PASSWORD`: the password for the container's `postgres` user. When you mount an existing initialized data directory, the container retains the existing password configured in your database.
     * `DATA_DIR`: the host directory path where your existing database data is stored.
     * `HOST_PORT`: the TCP port on the host machine that publishes container port `5432`—for example, `5432`.
     * `IMAGE_URI`: the updated minor version container image URI (or your rebuilt custom image URI)—for example, `google/alloydbomni:15.7.1`.

Use the same base OS image variant (Debian or UBI) as your previous container so that file ownership in your host data directory matches the container's `postgres` user. If your previous container used additional runtime flags, such as `--ulimit`, `--log-driver`, `--shm-size`, or `-v /dev/shm:/dev/shm`, include those flags when you recreate the container. For more information, see [Set up AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/configure-omni).




## Verify the upgrade

After you recreate and start the container, confirm that the database service is running the updated minor version:

  1. Check the status of the AlloyDB Omni container and confirm that its status is `Up`:

###  Docker 
         
         docker ps --filter "name=CONTAINER_NAME"

###  Podman 
         
         podman ps --filter "name=CONTAINER_NAME"

  2. Connect to the database and confirm that the upgraded version is active:

###  Docker 
         
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"

###  Podman 
         
         podman exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"




## Roll back the upgrade

If you need to revert your AlloyDB Omni installation to the earlier minor version, stop and remove the upgraded container and start a container that uses your previous minor version image:

  1. Stop and remove the upgraded AlloyDB Omni container:

###  Docker 
         
         docker container stop CONTAINER_NAME
         docker container rm CONTAINER_NAME

###  Podman 
         
         podman container stop CONTAINER_NAME
         podman container rm CONTAINER_NAME

  2. Recreate and start the container by using your previous minor version image and mounting the same host data directory:

###  Docker 
         
         docker run -d --name CONTAINER_NAME \
           -e POSTGRES_PASSWORD=PASSWORD \
           -v DATA_DIR:/var/lib/postgresql/data \
           -p HOST_PORT:5432 \
           --restart=always \
           ROLLBACK_IMAGE_URI

###  Podman 
         
         podman run -d --name CONTAINER_NAME \
           -e POSTGRES_PASSWORD=PASSWORD \
           -v DATA_DIR:/var/lib/postgresql/data \
           -p HOST_PORT:5432 \
           --restart=always \
           ROLLBACK_IMAGE_URI

Replace the following:

     * `CONTAINER_NAME`: the name of your AlloyDB Omni container—for example, `my-omni`.
     * `PASSWORD`: the password for the container's `postgres` user. When you mount an existing initialized data directory, the container retains the existing password configured in your database.
     * `DATA_DIR`: the host directory path where your existing database data is stored.
     * `HOST_PORT`: the TCP port on the host machine that publishes container port `5432`—for example, `5432`.
     * `ROLLBACK_IMAGE_URI`: the container image URI and minor version tag of your previous installation (or your previous custom image URI)—for example, `google/alloydbomni:15.7.0`.
  3. Confirm that the container is running and that the previous database version is active:

###  Docker 
         
         docker ps --filter "name=CONTAINER_NAME"
         docker exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"

###  Podman 
         
         podman ps --filter "name=CONTAINER_NAME"
         podman exec -it CONTAINER_NAME psql -h localhost -U postgres -c "SELECT version();"




## What's next

* [Upgrade AlloyDB Omni on a VM](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-vm-alloydb-omni-version) * [Set up AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/configure-omni) * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install) * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage) * [Back up and restore overview](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/backup-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
