---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/
title: Create a read-only replica \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:44:02.932176+00:00
---

# Create a read-only replica  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/

[ Skip to main content ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/)
  * [Deutsch](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=es-419)
  * [Français](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=id)
  * [Italiano](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=ja)
  * [한국어](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Falloydb%2Fomni%2Flinux%2F18.4.0%2Fdocs%2Fset-up-read-replica%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/alloydb-color.svg) ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#prerequisites)
  * [Configure your primary server for replication](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#configure-primary-for-replication)
  * [Create and configure the replica server](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#configure-replica-server)
  * [Verify replication status on the primary server](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#verify-replication-on-primary)
  * [Scale read workloads using read pools](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#scale-read-pools)
    * [Before you begin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#before-you-begin)
    * [Provision multiple read-only replicas](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#provision-multiple-replicas)


This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)


Was this helpful?
Send feedback 
#  Create a read-only replica Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#prerequisites)
  * [Configure your primary server for replication](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#configure-primary-for-replication)
  * [Create and configure the replica server](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#configure-replica-server)
  * [Verify replication status on the primary server](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#verify-replication-on-primary)
  * [Scale read workloads using read pools](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#scale-read-pools)
    * [Before you begin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#before-you-begin)
    * [Provision multiple read-only replicas](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica/#provision-multiple-replicas)


Select a documentation version:  18.4.0keyboard_arrow_down
  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/set-up-read-replica)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-read-replica)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/set-up-read-replica)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/set-up-read-replica)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-read-replica)

To increase read throughput and availability, you can create an AlloyDB Omni replica server for an existing AlloyDB Omni server. A replica server provides a read-only clone of your primary database server. It continuously updates its own data to reflect changes to your primary server's data. 
The following sections provide steps to configure your AlloyDB Omni primary server for replication, configure the replica server, and verify replication status on the primary server.
## Before you begin
Before you proceed, install and set up AlloyDB Omni using the RPM package. For more information, see [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/deploy-vm). 
## Configure your primary server for replication
  1. Update the network or firewall settings of your primary server's host so that it allows ingress traffic from the replica server's host through the primary server's Postgres port.
  2. Create a replication user:

```
psql -h localhost -U postgres -c "create user REPLICA_USER with replication password 'PASSWORD';
grant pg_read_all_settings to REPLICA_USER;"
```

  3. Add the following lines in the `/DATA_DIR/pg_hba.conf` file of the primary server **before** `host all all all scram-sha-256` that exists in the file:

```
host alloydbmetadata    alloydbmetadata   IP_RANGE trust
host replication        REPLICA_USER    IP_RANGE scram-sha-256

```

Replace the following:
     * `IP_RANGE`: the IP range, in CIDR notation, of the subnet where your replica machine is located. For example, `203.0.113.0/24`.
     * `DATA_DIR`: the data directory path of the primary server.
  4. Restart your primary server:

```
sudo systemctl restart alloydbomni18
```



## Create and configure the replica server
To create and configure an AlloyDB Omni replica server, complete the following steps:
  1. Ensure the replica has network connectivity to the primary server:

```
ping SOURCE_IP
```

Replace `SOURCE_IP` with the IP address of the primary AlloyDB Omni instance to replicate from.
  2. Ensure the replica can connect to the primary server:

```
psql "host=SOURCE_IP user=REPLICA_USER replication=1" -c "IDENTIFY_SYSTEM;"
```

The output should look similar to the following:

```
       systemid       | timeline |  xlogpos  | dbname
 ---------------------+----------+-----------+--------
  7376500460465963036 |        1 | 0/454B670 |
  (1 row)

```

  3. The replica must have a persistent storage location on disk:

```
sudo -u postgres pg_basebackup \
  --pgdata=DATA_DIR \
  --checkpoint=fast \
  --host="SOURCE_IP" \
  --port="SOURCE_PORT" \
  --username=REPLICA_USER \
  --create-slot \
  --write-recovery-conf \
  --slot="SLOT_NAME"
```

Replace the following:
     * `SOURCE_PORT`: the TCP port of the primary AlloyDB Omni instance to replicate from. If you don't provide this value, then AlloyDB Omni applies a default value of `5432`.
     * `SLOT_NAME`: the label for the name of the replication slot.
     * `DATA_DIR`: the data directory path for the replica server.
  4. Start your replica instance:

```
sudo systemctl start alloydbomni18
```



## Verify replication status on the primary server
To verify replication is configured properly, run the following command on the primary server's host:

```
psql -h localhost -U postgres -c "select * from pg_stat_replication"
```

The output table contains one row for every replica connected to your primary database server.
After you set up replication, all inserts, updates, and deletions to rows in your primary database server become readable on your replica within seconds.
## Scale read workloads using read pools
To scale your reporting and read-only requirements, you can provision multiple asynchronous streaming replicas to form a read pool. You can access the read pool by connecting directly to the IP addresses of your replica nodes.
### Before you begin
Make sure you created the `REPLICA_USER` with `REPLICATION` privileges on the primary server. You must also ensure that the primary server's `pg_hba.conf` file is configured to allow replication connections from the IP addresses of your replica nodes.
### Provision multiple read-only replicas
To create multiple replicas, repeat these steps for each replica node you want in the pool.
On each replica node, execute the `pg_basebackup` command, making sure to provide a unique replication slot name for each node:

```
  sudo -u postgres pg_basebackup \
   --pgdata=DATA_DIR \
   --checkpoint=fast \
   --host="SOURCE_IP" \
   --port="SOURCE_PORT" \
   --username=REPLICA_USER \
   --create-slot \
   --write-recovery-conf \
   --slot="UNIQUE_SLOT_NAME_PER_NODE"
   ```
Once the backup is complete, start the database service on each replica:
  ```posix-terminal
  sudo systemctl start alloydbomni18
```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
