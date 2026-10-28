---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/upgrade-linux-database-minor-version/
title: Perform a minor version upgrade for AlloyDB Omni using RPM \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:05:13.370857+00:00
---

# Perform a minor version upgrade for AlloyDB Omni using RPM  |  AlloyDB Omni using RPM: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/upgrade-linux-database-minor-version/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  Perform a minor version upgrade for AlloyDB Omni using RPM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/upgrade-linux-database-minor-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/upgrade-linux-database-minor-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/upgrade-linux-database-minor-version)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/upgrade-linux-database-minor-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/upgrade-linux-database-minor-version)

This page describes how to perform a minor database version upgrade for AlloyDB Omni by using Red Hat Package Manager (RPM), verify the upgraded installation, and roll back to an earlier minor version if needed. Minor version upgrades update the database binaries in place and preserve existing configuration and data files without requiring data migration. 

The instructions on this page apply to standalone single-node deployments and to individual database nodes in multi-node topologies, such as deployments with [read replicas](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/set-up-read-replica) or [high-availability standby nodes](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/high-availability/setup). Look for the following considerations based on your setup:

  * **Multi-node topologies:** Always upgrade all replica and standby nodes before you upgrade the primary node. In a high-availability setup, perform a switchover to an upgraded standby node before you upgrade the former primary node.
  * **Monitoring agent (`alloydbomni_monitor`):** If you installed the optional [`alloydbomni_monitor` package](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/manage#install-monitor), upgrade `alloydbomni_monitor` alongside `alloydbomni18` on each host.



## Before you begin

  1. Plan a maintenance window or brief service downtime, because upgrading the package requires temporarily stopping the database service.
  2. We recommend that you take a full backup of your database before you begin the upgrade. For more information, see [Back up and restore overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/backup-overview).
  3. If you're upgrading a multi-node topology, identify the current primary node and all standby or replica nodes so that you can upgrade the standby and replica nodes first.
  4. Verify your current AlloyDB Omni database version before upgrading:
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -W -c "SELECT version();"




## Check for available updates

Update your local package cache and check for later versions of the `alloydbomni18` package:
    
    
    sudo dnf makecache
    sudo dnf check-update alloydbomni18

If you installed the `alloydbomni_monitor` package, check for available updates to the monitoring agent as well:
    
    
    sudo dnf check-update alloydbomni_monitor

### Verify a private repository

Optional: If you manage packages through a private YUM repository or in an environment without internet access, you can run the following commands to inspect your repository configuration and check which package versions are available:

  1. Set the `REPOID` environment variable to the ID of your private repository:
         
         export REPOID=REPO_ID

Replace `REPO_ID` with the repository ID of your private YUM repository—for example, `alloydbomni`.

  2. Check which repository provided your current AlloyDB Omni installation:
         
         sudo dnf list installed alloydbomni18

  3. List all enabled repositories and their repository IDs:
         
         sudo dnf repolist

  4. View metadata for your private repository:
         
         sudo dnf repoinfo $REPOID

  5. List all versions of the `alloydbomni18` package that are available in your repositories:
         
         sudo dnf --showduplicates list available alloydbomni18




## Upgrade AlloyDB Omni

To upgrade your AlloyDB Omni installation to a later minor version, follow these steps on each node. In a multi-node topology, complete these steps on each standby or replica node before upgrading the primary node:

  1. Stop the AlloyDB Omni database service:
         
         sudo systemctl stop alloydbomni18

If you installed the `alloydbomni_monitor` service, stop it as well:
         
         sudo systemctl stop alloydbomni_monitor

  2. Install the updated AlloyDB Omni RPM package:
         
         sudo dnf upgrade -y alloydbomni18

This command updates the AlloyDB Omni packages and binaries while leaving your database data directory intact.

If you installed the `alloydbomni_monitor` package, upgrade it alongside the database package:
         
         sudo dnf upgrade -y alloydbomni_monitor

  3. Start the AlloyDB Omni `systemd` service:
         
         sudo systemctl start alloydbomni18

If you stopped the `alloydbomni_monitor` service, start it again:
         
         sudo systemctl start alloydbomni_monitor




## Verify the upgrade

After you upgrade the RPM packages and start the services, verify that the database service is running the updated version:

  1. Check the status of the AlloyDB Omni service and confirm that it is `active (running)`:
         
         sudo systemctl status alloydbomni18

If you upgraded `alloydbomni_monitor`, confirm that the monitor service is also `active (running)`:
         
         sudo systemctl status alloydbomni_monitor

  2. Connect to the database and verify that the upgraded version is active:
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -W -c "SELECT version();"




## Roll back the upgrade

If you need to revert your AlloyDB Omni installation to the earlier minor version, follow these steps:

  1. Stop the AlloyDB Omni database service:
         
         sudo systemctl stop alloydbomni18

If you installed the `alloydbomni_monitor` service, stop it as well:
         
         sudo systemctl stop alloydbomni_monitor

  2. List all available versions of the `alloydbomni18` package and identify the exact version string of your previous installation:
         
         sudo dnf --showduplicates list alloydbomni18

  3. Downgrade the `alloydbomni18` package to your previous version:
         
         sudo dnf downgrade -y alloydbomni18-ROLLBACK_VERSION

Replace `ROLLBACK_VERSION` with the exact version string of your previous installation—for example, `18.1.0-3.rhel9`.

If you also need to downgrade `alloydbomni_monitor`, list its available versions and downgrade to the previous monitor package version:
         
         sudo dnf --showduplicates list alloydbomni_monitor
         sudo dnf downgrade -y alloydbomni_monitor-MONITOR_ROLLBACK_VERSION

Replace `MONITOR_ROLLBACK_VERSION` with the previous `alloydbomni_monitor` package version string.

  4. Start the AlloyDB Omni `systemd` service:
         
         sudo systemctl start alloydbomni18

If you stopped the `alloydbomni_monitor` service, start it again:
         
         sudo systemctl start alloydbomni_monitor

  5. Verify that the AlloyDB Omni service is active and running the previous version:
         
         sudo systemctl status alloydbomni18
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -W -c "SELECT version();"




## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/manage)
  * [Back up and restore overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/backup-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
