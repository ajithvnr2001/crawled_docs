---
url: https://docs.cloud.google.com/bigtable/docs/managing-backups/
title: Manage backups \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:59:33.186002+00:00
---

# Manage backups  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/managing-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage backups

Bigtable backups help you protect your tables against accidental data loss, corruption, or disaster scenarios. You can create, copy, restore, and monitor these backups using the Google Cloud console, the Google Cloud CLI, or the Cloud Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

## Before you begin

Before you begin, review [Backups](https://docs.cloud.google.com/bigtable/docs/backups), and see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview) for features that are available only in Enterprise Plus edition.

Make sure that you or the user account that you are using have the [required permissions](https://docs.cloud.google.com/bigtable/docs/backups#access-control) for the action you need to perform.

If you plan to use the gcloud CLI, [install the gcloud CLI for Bigtable](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk).

## Use automated backup

You can use the gcloud CLI or the Google Cloud console to enable automated backup. By default, automated backup creates a daily standard backup of your table with a retention period of seven days. You can customize an automated backup policy in the following ways:

  * Configure hot automated backups on SSD instances by specifying a keep-hot duration from 24 hours to 10 days. This required setting determines how long each daily backup remains hot before transitioning to a standard backup. Hot automated backups also have a default retention period of seven days. For more information, see the Configure hot automated backups section of this document.
  * Modify the backup retention period up to 90 days. For more information, see the Update an automated backup policy section of this document.
  * Select specific cluster locations where automated backup is enabled. This option is available only in Enterprise Plus edition. For more information, see the Configure automated backup cluster locations section of this document.

**Note:** Automated backup policies created before December 17, 2024 are configured for a default retention period of three days.

The steps to delete, update, copy, and restore a backup are the same whether the backup is created manually or as a result of automated backup.

You can extend the expiration date of a backup or backup copy. For more information, see Modify a backup or backup copy.

If you plan to enable automated backup, consider the following factors:

  * If a cluster is added to an instance that contains a table with automated backup enabled, daily backups aren't created on the added cluster. To create daily backups on all clusters, including the newly added cluster, disable automated backup for the table, and then re-enable automated backup.
  * If a table with automated backup enabled is deleted and subsequently undeleted, you need to re-enable automated backup on the recovered table.
  * Restoring an automated backup of a table doesn't automatically enable automated backup on the restored table. You need to manually enable automated backup.



### Enable automated backup

You can enable automated backup by using the Google Cloud console or the Google Cloud CLI. When you enable automated backup with default settings, Bigtable creates a daily standard backup of the table on each cluster in the instance and retains it for seven days.

Backups that Bigtable creates as part of automated backup are assigned IDs that begin with `auto`. For example, a table with an ID of `my-table` has an automated backup ID like `auto.my-table.c7x3.20230220-145537`, where `my-table` is the truncated table ID, `c7x3` is the unique hash ID, and `20230220-145537` is the date and time in UTC format.

To create a table with automated backup enabled, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table that you want to back up.

  3. In the Bigtable navigation menu, click **Tables**.

The **Tables** page displays a list of tables in the instance.

  4. To enable automated daily backup with default settings, in the **Automated backup** column for the table, click **Enable**.

It can take up to an hour for Bigtable to start creating backups.

  5. Optional: To enable automated backup with custom settings, such as hot automated backups on SSD instances, do the following:

     1. In the row for the table, click edit **Edit**.
     2. In the **Configure automated backup** section, select **Enable automated backup** .

You can also update an existing policy later to change the backup type, retention period, or, in the Enterprise Plus edition, cluster locations. For more information, see the Update an automated backup policy and Configure hot automated backups sections of this document.




###  gcloud 

To enable automated backup for a table, run the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command. For more information about enabling automated backup when creating a table, see [Create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table).

After the automated backup policy is enabled for a table, the updated configuration can take up to an hour to take effect.
    
    
    gcloud bigtable tables update TABLE_ID \
    --instance=INSTANCE_ID \
    --enable-automated-backup
    

Replace the following:

  * `TABLE_ID`: the ID of the table that you want to back up
  * `INSTANCE_ID`: the permanent identifier for the instance 

**Warning:** The `--enable-automated-backup` flag enables automated backups with default settings. Using this flag to update a table that already has automated backup enabled overwrites any previously configured retention period or keep-hot duration, sets the retention period to seven days, and reverts the policy to creating standard backups. In Enterprise Plus edition, Bigtable reverts the backups to all clusters in the table's instance even if you enabled them only in specific locations.

Optional: You can update the automated backup policy to specify a custom retention period or configure hot automated backups on SSD instances. In Enterprise Plus edition, you can enable automated backups for clusters in specific locations. For more information, see the Update an automated backup policy and Configure hot automated backups sections of this document.

### Disable automated backup

After the automated backup policy is disabled for a table, the updated configuration can take up to an hour to take effect. Backups that were created before the policy change are retained until they expire, unless you delete them.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table whose automated backup you want to disable.

  3. In the Bigtable navigation menu, click **Tables**.

The **Tables** page displays a list of tables in the instance.

  4. In the row for the table whose automated backup you want to disable, click edit **Edit**.

  5. In the **Edit table** pane, in the **Configure automated backup** section, clear **Enable automated backup**.

  6. Click **Save**.




###  gcloud 

To disable automated backup for a table, run the [`gcloud bigtable instances tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command.
    
    
    gcloud bigtable instances tables update TABLE_ID \
    --instance=INSTANCE_ID \
    --disable-automated-backup
    

Replace the following:

  * `TABLE_ID`: the ID of the table
  * `INSTANCE_ID`: the permanent identifier for the instance 



### View automated backup policy

You can view a table's automated backup policy by using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table whose automated backup policy you want to view.

  3. In the Bigtable navigation menu, click **Tables**.

On the **Tables** page, the **Automated backup** column shows **Not enabled** if automated backup isn't enabled, or shows the backup type (**Standard** or **Hot**) if automated backup is enabled. In Enterprise Plus edition, if automated backups are configured for specific clusters, the column also lists **Zones backed up**. You can also view this summary on the table overview page by clicking the table ID.

  4. Optional: To view the full policy configuration, in the row for the table, click edit **Edit**.

In the **Edit table** pane, the **Configure automated backup** section displays the **Backup type** setting (and the **Set hot to standard** duration if **Hot** is selected), the **Retention period** , and the **Select clusters to back up** setting. To close the pane without making changes, click **Cancel**.




###  gcloud 

To view the automated backup policy for a table, run the [`gcloud bigtable instances tables describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/describe) command:
    
    
    gcloud bigtable instances tables describe TABLE_ID \
        --instance=INSTANCE_ID
    

Replace the following:

  * `TABLE_ID`: the ID of the table
  * `INSTANCE_ID`: the permanent identifier for the instance 



The output looks similar to the following:
    
    
    automatedBackupPolicy:
      frequency: 86400s
      keepHotDuration: 172800s
      retentionPeriod: 604800s
      locations: us-central1-a,us-east1-b,europe-west1-c
    columnFamilies:
      my-family: {}
    createTime: '2023-02-07T20:10:55.613546Z'
    granularity: MILLIS
    name: projects/my-project/instances/my-instance/tables/my-table
    updateTime: '2023-02-07T20:10:55.613546Z'
    

Note the following:

  * The `automatedBackupPolicy` field is absent when automated backup isn't enabled for a table.
  * The `keepHotDuration` field is present only when you configure the policy to create hot automated backups. When present, it indicates how long each automated backup remains hot before transitioning to a standard backup. If the policy creates standard backups (default), then the field isn't present.
  * The `retentionPeriod` field indicates the retention period of automatically created backups. You can modify the retention period for an individual backup to up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition, starting from the backup creation time. To update the backup retention period, see Modify a backup or backup copy.
  * The `locations` field is present only when automated backups for clusters in specific locations are enabled in Enterprise Plus edition. When present, it indicates the list of cluster locations where automated backups are enabled. If automated backups are enabled in all locations (default), then the field isn't present.



### Update an automated backup policy

Automated backup policy changes don't apply retroactively to existing backups. New backup policy settings apply only to subsequent backups.

You can configure a custom retention period of up to 90 days in both Enterprise and Enterprise Plus editions. On SSD instances, you can configure hot automated backups by specifying a keep-hot duration, which sets how long automated backups remain hot before transitioning to standard backups. In Enterprise Plus edition, you can also select specific cluster locations for automated backups. For more information about hot automated backups, see Configure hot automated backups.

To update the retention period or expiration date of an existing backup, including an automated backup, see Modify a backup or backup copy.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table whose automated backup policy you want to update.

  3. In the Bigtable navigation menu, click **Tables**.

The **Tables** page displays a list of tables in the instance.

  4. In the row for the table that you want to update, click edit **Edit**.

  5. In the **Edit table** pane, in the **Configure automated backup** section, make sure that **Enable automated backup** is selected, and then update any of the following settings:

     * In the **Backup type** section, select **Standard** or **Hot**. You can't select **Hot** on HDD instances or on tables with tiered storage enabled. If you select **Hot** , then in the **Set hot to standard** field, to specify the number of days that each automated backup remains hot before automatically transitioning to a standard backup, enter an integer from 1 to 10 (up to the retention period).
     * In the **Backup configuration** section, in the **Retention period** field, enter an integer from 3 to 90 to specify the number of days that Bigtable retains backups (up to 90 days).
     * The Enterprise Plus edition: in the **Backup configuration** section, in the **Select clusters to back up** list, select the clusters where you want Bigtable to create daily backups, and then click **OK**.
  6. Click **Save**.




###  gcloud 

To modify a table's automated backup policy, use the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command with one or more of the following flags:

  * `--automated-backup-retention-period`: sets a custom retention period
  * `--automated-backup-keep-hot-duration`: on SSD instances, configures Bigtable to create hot automated backups and specifies how long they remain hot before transitioning to standard backups
  * `--automated-backup-locations`: in Enterprise Plus edition, enables automated backup only for clusters in the specified locations

**Caution:** When you update a table's automated backup configuration, you only need to specify the flags for the parameters that you want to change; omitted parameters retain their existing values. However, passing the `--enable-automated-backup` flag resets all automated backup policy parameters to their default values.
    
    
    gcloud bigtable tables update TABLE_ID \
        --instance=INSTANCE_ID \
        --automated-backup-retention-period=RETENTION_PERIOD \
        --automated-backup-keep-hot-duration=KEEP_HOT_DURATION \
        --automated-backup-locations=BACKUP_LOCATIONS
    

Replace the following:

  * `TABLE_ID`: the ID of the table that has automated backup
  * `INSTANCE_ID`: the permanent identifier for the instance 
  * `RETENTION_PERIOD`: a period of up to 90 days. The value must be expressed as a number with a unit of `m`, `h`, or `d` (minutes, hours, or days), such as `15d` for 15 days.

_Examples_ : `72h` or `15d`

  * `KEEP_HOT_DURATION`: the amount of time that automated backups remain hot before transitioning to standard backups, from `24h` (1 day) to `10d` (10 days), not exceeding the policy's retention period. Express the value as a number with a unit of `s`, `m`, `h`, or `d` (seconds, minutes, hours, or days). Bigtable supports this flag only on SSD instances and on tables without tiered storage enabled.

_Examples_ : `24h` or `2d`

  * `BACKUP_LOCATIONS`: a comma-separated list of cluster locations where you want to enable automated backup. If not set, then the backups default to all clusters in the table's instance.

_Example_ : `us-central1-a,us-east1-b,europe-west1-c`




### Configure hot automated backups

You can configure hot automated backups by using the Google Cloud console or the Google Cloud CLI when you create a table, enable automated backup, or update an automated backup policy. When you configure hot automated backups, you specify a keep-hot duration that determines how long each daily backup remains hot before transitioning to a standard backup. For example, to keep only your most recent daily backup hot, set the keep-hot duration to 24 hours (1 day) so that each daily backup transitions to a standard backup after the next daily backup is created. For more information about configuring automated backup when you create a table, see [Create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#create-table).

Consider the following requirements and limitations when you configure hot automated backups:

  * The table must be in an SSD instance. Bigtable doesn't support hot automated backups on HDD instances.
  * Bigtable doesn't support hot automated backups for tables with tiered storage enabled. For more information, see [Tiered storage overview](https://docs.cloud.google.com/bigtable/docs/tiered-storage).
  * The keep-hot duration must be at least 24 hours (`24h` or `1d`, or 1 day in the Google Cloud console) and at most 10 days (`10d`), and it can't exceed the policy's retention period.
  * To enable hot automated backups for a table on a cluster that uses more than 400 TB of SSD storage, contact [Cloud Customer Care](https://docs.cloud.google.com/bigtable/docs/support/getting-support). For more information, see [Backups limits](https://docs.cloud.google.com/bigtable/quotas#backups).




###  Console 

To configure hot automated backups for an existing table:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the SSD instance that contains the table that you want to configure.

  3. In the Bigtable navigation menu, click **Tables**.

The **Tables** page displays a list of tables in the instance.

  4. In the row for the table, click edit **Edit**.

  5. In the **Edit table** pane, in the **Configure automated backup** section, make sure that the **Enable automated backup** checkbox is selected.

  6. In the **Backup type** section, select **Hot**.

  7. In the **Set hot to standard** field, enter an integer from 1 to 10 to specify the number of days that each automated backup remains hot before automatically transitioning to a standard backup. The default is 3 days. This value can't exceed the number of days in the **Retention period** field.

  8. Optional: In the **Backup configuration** section, enter an integer from 3 to 90 in the **Retention period** field, or, in Enterprise Plus edition, select specific clusters in the **Select clusters to back up** list and then click **OK**.

  9. Click **Save**.




To stop keeping subsequent automated backups hot and revert the policy to creating standard backups, open the **Edit table** pane for the table, select **Standard** in the **Backup type** section, and then click **Save**. Changing the backup type doesn't affect backups that were already created. Existing hot backups remain hot until their transition period expires.

###  gcloud 

To configure hot automated backups for a table, run the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command by using the `--automated-backup-keep-hot-duration` flag:
    
    
    gcloud bigtable tables update TABLE_ID \
        --instance=INSTANCE_ID \
        --automated-backup-keep-hot-duration=KEEP_HOT_DURATION
    

Replace the following:

  * `TABLE_ID`: the ID of the table to configure
  * `INSTANCE_ID`: the permanent identifier for the instance 
  * `KEEP_HOT_DURATION`: the amount of time that automated backups remain hot before transitioning to standard backups, from `24h` (1 day) to `10d` (10 days), not exceeding the policy's retention period. Express the value as a number with a unit of `s`, `m`, `h`, or `d` (seconds, minutes, hours, or days), such as `24h` or `2d`. If automated backup isn't already enabled on the table, then you must also include the `--automated-backup-retention-period` flag when you run the `gcloud bigtable tables update` command. Otherwise, the command fails with a missing retention period error.



To stop keeping automated backups hot and revert the policy to creating standard backups, run the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command by using the `--clear-automated-backup-keep-hot-duration` flag. Clearing the keep-hot duration doesn't affect backups that were already created. Existing hot backups remain hot until their keep-hot duration expires and they transition to standard backups.
    
    
    gcloud bigtable tables update TABLE_ID \
        --instance=INSTANCE_ID \
        --clear-automated-backup-keep-hot-duration
    

Replace the following:

  * `TABLE_ID`: the ID of the table to configure
  * `INSTANCE_ID`: the permanent identifier for the instance 

**Caution:** When you update a table's automated backup configuration, you only need to specify the flags for the parameters that you want to change. Omitted parameters retain their existing values. However, passing the `--enable-automated-backup` flag resets all automated backup policy parameters to their default values.

### Configure automated backup cluster locations

**Note:** This feature is available only in Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

By default, when you enable automated backup for a table in an instance that has multiple clusters, Bigtable creates a daily backup on every cluster in the instance. In Enterprise Plus edition, you can selectively configure automated backup to create daily backups on clusters in specific locations.

You can configure automated backup cluster locations when you create a table, enable automated backup, or update an automated backup policy.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table that you want to configure.

  3. In the Bigtable navigation menu, click **Tables**.

  4. On the **Tables** page, in the row for the table, click edit **Edit**.

  5. In the **Edit table** pane, in the **Configure automated backup** section, make sure that **Enable automated backup** is selected.

  6. In the **Backup configuration** section, in the **Select clusters to back up** list, select the clusters where you want Bigtable to create daily backups, and then click **OK**.

  7. Click **Save**.




To revert to creating daily backups on all clusters in the instance, open the **Edit table** pane for the table, select all clusters in the **Select clusters to back up** list, click **OK** , and then click **Save**.

###  gcloud 

To specify cluster locations for automated backup, run the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command by using the `--automated-backup-locations` flag:
    
    
    gcloud bigtable tables update TABLE_ID \
        --instance=INSTANCE_ID \
        --automated-backup-locations=BACKUP_LOCATIONS
    

Replace the following:

  * `TABLE_ID`: the ID of the table to configure
  * `INSTANCE_ID`: the permanent identifier for the instance 
  * `BACKUP_LOCATIONS`: a comma-separated list of cluster locations where you want to enable automated backup, such as `us-central1-a,us-east1-b`



To remove custom automated backup locations and revert to creating backups in all cluster locations of the instance, run the [`gcloud bigtable tables update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/update) command by using the `--clear-automated-backup-locations` flag:
    
    
    gcloud bigtable tables update TABLE_ID \
        --instance=INSTANCE_ID \
        --clear-automated-backup-locations
    

Replace the following:

  * `TABLE_ID`: the ID of the table to configure
  * `INSTANCE_ID`: the permanent identifier for the instance 

**Caution:** When you update a table's automated backup configuration, you only need to specify the flags for the parameters that you want to change. Omitted parameters retain their existing values. However, passing the `--enable-automated-backup` flag resets all automated backup policy parameters to their default values.

### View event logs

When automated backup is enabled, Bigtable emits a system event logs when a backup is created. It also emits an event log if backup creation is delayed.

To view automated backup system event logs on the Bigtable cluster overview page in the console, do the following:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance ID.

  3. Click the cluster ID.

If automated backup event logs were created in the last hour, they are displayed in the **Logs** pane.

  4. Optional: To view older event logs, click the arrow next to **1 Hour** and select another time range.




To view automated backup system event logs in the Logs Explorer, follow these steps:

  1. Navigate to the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

Select the appropriate Google Cloud project.

  2. To view backup creation events, enter the following in the **Query** field:
         
         resource.type="audited_resource" resource.labels.service="bigtableadmin.googleapis.com"
         resource.labels.method="CreateAutomatedBackup"
         

  3. Click **Run query**.

  4. To view backup delay events, enter the following in the **Query** field:
         
         resource.type="audited_resource" resource.labels.service="bigtableadmin.googleapis.com"
         resource.labels.method="DelayedAutomatedBackup"
         

  5. Click **Run query**.

The query result includes a message similar to the following:
         
         Automated backup is delayed for table ab-test on cluster my-cluster-staging-c1.
         




## Create a standard backup

You can create a standard backup of a table by using the Google Cloud CLI, the console, or one of the Bigtable client libraries. You can also enable automated backup to let Bigtable create a daily standard backup for you. For more information, see Enable automated backup.

###  Console 

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table you want to back up.

  3. In the left navigation pane, click **Backups**.

  4. Click **Create backup**.

  5. In the **Table ID** list, select the table that you want to back up. (If you click **Create backup** from the more_vert **Table action** menu on the table overview page, then Bigtable populates the table.)

  6. If you use replication, then select the **Cluster ID** for the cluster. (If you click **Create backup** next to a cluster ID on the cluster overview page, then Bigtable populates the table and the cluster.)

  7. Enter a unique ID for the backup.

  8. In the **Backup type** section, select **Standard**.

  9. Set an expiration date by selecting one of the options.

  10. Click **Create**.

The Google Cloud console displays the **Backups** page filtered to show the backup and its details.

  11. Optional: To view the status of the backup, click the **Activity** tab.

After Bigtable finishes backing up your data, the **Backup complete** status appears in the **Status** column.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. View the list of backups for the instance that contains the table you want to back up, so that you can choose a backup ID that isn't already in use on the intended cluster:
         
         gcloud bigtable backups list --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID
         

Replace the following:

     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
  3. View the list of tables to confirm the ID of the table you want to back up:
         
         gcloud bigtable instances tables list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance .

  4. Run the [`gcloud bigtable instances backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/backups/create) command to create a backup from the table, providing either an expiration date or a retention period:
         
         gcloud bigtable backups create BACKUP_ID --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID \
           --table=TABLE_ID \
           --expiration-date=EXPIRATION_DATE \
           --retention-period=RETENTION_PERIOD
         

Replace the following:

     * `BACKUP_ID`: the ID that you assign to the backup
     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
     * `TABLE_ID`: the ID of the table to be backed up
     * `EXPIRATION_DATE`: a date in the future, up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition. The value must be formatted as a "Zulu" UTC timestamp, accurate to nanoseconds—for example, `2022-10-02T15:01:23.045123456Z`.
     * `RETENTION_PERIOD`: a period of up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition. The value must be expressed as a number with a unit of `m`, `h`, or `d` (minutes, hours, or days), such as `36h` or `15d`.

The command accepts the following optional flag: 

     * `--async`: returns the operation ID to the terminal before the operation is complete. This is helpful if you want to check the status of the operation.
  5. View the list of backups to see if your backup has been created:
         
         gcloud bigtable backups list --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID
         

Replace the following:

     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
  6. If the backup is not listed, check the status of the operation.

A status of `Ready` indicates the backup is complete.




## Create a hot backup

You can create a hot backup on demand by using the Google Cloud console or the Google Cloud CLI. You can also configure hot automated backups to let Bigtable create a daily hot backup for you. For more information, see Configure hot automated backups.

You can't create a hot backup for a table that has tiered storage ([Preview](https://cloud.google.com/products#product-launch-stages)) enabled. For more information, see [Tiered storage overview](https://docs.cloud.google.com/bigtable/docs/tiered-storage).

###  Console 

You can create a hot backup of a table using the Google Cloud console as follows:

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table that you want to back up.

  3. In the left navigation pane, click **Backups**.

  4. Click **Create backup**.

  5. In the **Table ID** list, select the table that you want to back up. (If you click **Create backup** from the more_vert **Table action** menu on the table overview page, then Bigtable populates the table.)

  6. If you use replication, then select the **Cluster ID** for the cluster. (If you click **Create backup** next to a cluster ID on the cluster overview page, then Bigtable populates the table and the cluster.)

  7. In the **Backup ID** field, enter a unique ID for the backup.

  8. In the **Backup type** section, select **Hot**.

  9. In the **Set hot to standard** list, select one of the following options:

     * To keep the backup hot until it expires, select **Never**.
     * To convert the hot backup to standard after three days, select **3 days**.
     * To specify a custom date and time for when you want to convert the hot backup to standard, select **Custom**. This value must be at least 24 hours after the time when Bigtable creates the backup.
  10. Click **Create**.

The Google Cloud console displays the **Backups** page filtered to show the backup and its details.

  11. Optional: To view the status of the backup, click the **Activity** tab.

After Bigtable finishes backing up your data, the **Backup complete** status appears in the **Status** column.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. View the list of backups for the instance that contains the table you want to back up, so that you can choose a backup ID that isn't already in use on the intended cluster:
         
         gcloud bigtable backups list --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID
         

Replace the following:

     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
  3. View the list of tables to confirm the ID of the table you want to back up:
         
         gcloud bigtable instances tables list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance .

  4. Run the [`gcloud bigtable instances backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/backups/create) command to create a hot backup of the table, providing either an expiration date _or_ a retention period:
         
         gcloud bigtable backups create BACKUP_ID --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID \
           --table=TABLE_ID \
           --expiration-date=EXPIRATION_DATE \
           --retention-period=RETENTION_PERIOD \
           --backup-type=HOT
         

Replace the following:

     * `BACKUP_ID`: the ID that you assign to the backup
     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
     * `TABLE_ID`: the ID of the table to be backed up
     * `EXPIRATION_DATE`: a date in the future that is 90 days or less in Enterprise edition or 365 days or less in Enterprise Plus edition. The date must be formatted as a "Zulu" UTC timestamp, accurate to nanoseconds—for example, `2022-10-02T15:01:23.045123456Z`.
     * `RETENTION_PERIOD`: a period of up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition, expressed as a number with a unit of `m`, `h`, or `d` (minutes, hours, or days), such as `36h` or `89d`.

The command accepts the following optional flags: 

     * `--hot-to-standard-time=HOT_TO_STANDARD_TIME`: the date and time when Bigtable converts the backup from a hot backup to a standard backup, formatted as a "Zulu" UTC timestamp (for example, `2024-08-02T15:01:23.045123456Z`) or as a relative duration (for example, `+P30D` for 30 days; see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)). This value must be at least 24 hours after the backup creation time.
     * `--async`: returns the operation ID to the terminal before the operation is complete. This is helpful if you want to check the status of the operation.
  5. View the list of backups to see if your backup has been created:
         
         gcloud bigtable backups list --instance=INSTANCE_ID \
           --cluster=CLUSTER_ID
         

Replace the following:

     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
  6. If the backup is not listed, check the status of the operation.

A status of `Ready` indicates the backup is complete.




## Restore from a backup

A new table restored from a backup doesn't have automated backup enabled even if the source table did. If you want automated backup on the new table, you must enable it.

The steps to restore from a backup are the same whether the backup is standard or hot. Bigtable restores a hot backup to production performance more quickly than a standard backup.

###  Console 

You can't restore to a different project using the Google Cloud console. If you need to do so, use the gcloud CLI instead.

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the backup you want to restore.

  3. In the left navigation pane, click **Backups**.

  4. Click **Restore** for the backup that you want to restore.

  5. Select the instance that you want to restore to.

Instances that don't have enough storage for the new table are unavailable. If you don't have permission to create a table in an instance, the instance is unavailable. Mouse over the help icon for more information.

If you restore from a backup that is protected by CMEK, the destination instance must be CMEK-protected as well.

If you restore from a backup of a table with [microsecond timestamp granularity](https://docs.cloud.google.com/bigtable/docs/data-types#timestamp_granularity), the destination instance must be an Enterprise Plus instance.

You are not able to restore to a different project using the Google Cloud console. If you need to, use the gcloud CLI instead.

  6. Enter a unique ID for the table that will be created from the backup. You are not able to change this ID later.

  7. Click **Restore**.

The console displays the **Tables** page filtered to show the new table.

The console displays the restore status for each cluster. When the status column for all clusters shows **Ready** the table has been restored and replicated to all clusters in the instance.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. View the list of backups for the instance that contains the backup, to verify the backup exists:
         
         gcloud bigtable backups list --instance=INSTANCE_ID_SOURCE \
             --cluster=CLUSTER_ID
         

Replace the following:

     * `INSTANCE_ID_SOURCE`: the permanent ID for the source instance
     * `CLUSTER_ID`: the permanent identifier for the cluster 
  3. View the list of tables in the destination instance, so you can choose an ID for the new table that is not already in use:
         
         gcloud bigtable instances tables list --instances=INSTANCE_ID_DESTINATION
         

Replace `INSTANCE_ID_DESTINATION` with the permanent ID for the destination instance.

  4. Run the [`gcloud bigtable instances tables restore`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/tables/restore) command to restore from the backup to a new table:
         
         gcloud bigtable instances tables restore \
             --source=projects/PROJECT_ID_SOURCE/instances/INSTANCE_ID_SOURCE/clusters/CLUSTER_ID/backups/BACKUP_ID \
             --destination=TABLE_ID_NEW \
             --destination-instance=INSTANCE_ID_DESTINATION
         

Replace the following:

     * `PROJECT_ID_SOURCE`: the ID of the project containing the backup to be restored from
     * `INSTANCE_ID_SOURCE`: the permanent ID for the source instance
     * `CLUSTER_ID`: the permanent identifier for the cluster 
     * `BACKUP_ID`: the ID of the backup that you want to restore from
     * `TABLE_ID_NEW`: the ID for the new table
     * `INSTANCE_ID_DESTINATION`: the permanent ID for the destination instance

The command accepts the following optional flags: 

     * `--project=PROJECT_ID_DESTINATION`: the ID of the project where you want to restore to. If you don't specify this option, the backup is restored to a new table in the same instance where it was created.
     * `--async`: returns the operation ID to the terminal before the operation is complete. This is helpful if you want to check the status of the operation.
  5. View the list of tables to see if your table has been created:
         
         gcloud bigtable instances tables list --instances=INSTANCE_ID_DESTINATION
         

Replace `INSTANCE_ID_DESTINATION` with the permanent ID for the destination instance.

  6. If the backup is not listed, check the status of the operation.




## Create a copy of a backup

**Important:** A copy of a backup is always a standard backup, even if the source is a hot backup.

###  Console 
    
    
    You are not able to create a copy of a backup in a different project
    using the console. If you need to do so, use the
    gcloud CLI instead.
    

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the backup you want to copy.

  3. In the left navigation pane, click **Backups**.

  4. For the backup that you want to copy, expand the More menu next to the word **Restore** , and then click **Copy**.

  5. Click **Copy** for the backup that you want to make a copy of.

If the backup is a copy of another backup, then **Copy** is not available.

  6. Select the destination instance.

You are not able to create a copy of a backup in a different project using the console. If you need to do so, use the gcloud CLI instead.

Instances that don't have enough storage for the backup copy are unavailable. If you don't have permission to create a backup in an instance, the instance is unavailable. Hold the pointer over the help icon for more information.

If you copy a backup that is protected by CMEK, the destination instance must be CMEK-protected as well.

  7. Select the destination cluster.

Like any backup, a backup copy is stored on only one cluster in an instance, even if that instance uses replication.

  8. Enter a unique ID for the copy that will be created from the backup. You are not able to change this ID later.

  9. Set an expiration time for the backup copy, providing a value for **Time** and selecting a **Unit** from the drop-down menu.

  10. Click **Copy**.

  11. To view your copy, click **View copy**.

The console displays the **Backups** page for the destination instance, filtered for the backup copy just created. When the status column shows **Ready** the copy is complete and ready for further operations.




### gcloud

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. View the list of backups for the source instance that contains the backup, to verify that the backup that you want to copy exists:
         
         gcloud bigtable backups list --instance=INSTANCE_ID_SOURCE \
             --cluster=CLUSTER_ID_SOURCE
         

Replace the following:

     * `INSTANCE_ID_SOURCE`: the permanent ID for the source instance
     * `CLUSTER_ID_SOURCE`: the ID of the cluster where the source backup is stored
  3. View the list of backups in the destination instance, so you can choose an ID for the copy that is not already in use:
         
         gcloud bigtable backups list --instances=INSTANCE_ID_DESTINATION
         

Replace `INSTANCE_ID_DESTINATION` with the permanent ID for the destination instance.

  4. Run the [`gcloud bigtable backups copy`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/backups/copy) command to create the backup copy:
         
         gcloud bigtable backups copy \
             --source-project=PROJECT_ID_SOURCE \
             --source-instance=INSTANCE_ID_SOURCE \
             --source-cluster=CLUSTER_ID_SOURCE \
             --source-backup=BACKUP_ID_SOURCE \
             --destination-project=PROJECT_ID_DESTINATION \
             --destination-instance=INSTANCE_ID_DESTINATION \
             --destination-cluster=CLUSTER_ID_DESTINATION \
             --destination-backup=BACKUP_ID_DESTINATION
         

Append the command with one of the following:

     * `--retention-period=RETENTION_PERIOD`
     * `--expiration-date=EXPIRATION_DATE`

Replace the following:

     * `PROJECT_ID_SOURCE`: the project containing the backup to be copied
     * `INSTANCE_ID_SOURCE`: the permanent ID for the source instance
     * `CLUSTER_ID_SOURCE`: the ID of the cluster where the source backup is stored
     * `BACKUP_ID_SOURCE`: the ID of the backup to copy
     * `PROJECT_ID_DESTINATION`: the project where you want to put the copy
     * `INSTANCE_ID_DESTINATION`: the permanent ID for the destination instance
     * `CLUSTER_ID_DESTINATION`: the ID of the cluster in the destination instance that you want to store the copy
     * `BACKUP_ID_DESTINATION`: the ID you assign to the copy of the backup
     * `RETENTION_PERIOD`: the time to live for the backup copy, expressed as a number and a unit (`d` or `h`). Must be at least 6 hours and at most 30 days from the time the source backup was created. Examples include `5d` for five days or `15h` for 15 hours. Use either this or an expiration date.
     * `EXPIRATION_DATE`: the date and time to let the backup copy expire, formatted like `2022-09-01T10:00:00.0Z`. Must be at least 6 hours and at most 30 days from the time the source backup was created.

The command accepts the following optional flag: 

     * `--async`: returns the operation ID to the terminal before the operation is complete. This is helpful if you want to check the status of the operation.

If a timeout message is returned, the backup might have been successful and the copy might have been created.

  5. View the list of backups to see if your copy has been created:
         
         gcloud bigtable backups list --instances=INSTANCE_ID_DESTINATION
         

Replace `INSTANCE_ID_DESTINATION` with the permanent ID for the destination instance.

  6. If the backup is not listed, check the status of the operation.




In the rare event that a backup copy operation fails because of capacity limitations, try again with a different destination cluster. If that operation also fails, contact Support.

## Check the status of an operation

###  Console 

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the backup.

  3. In the left navigation pane, click **Backups**.

  4. On the **Backups** page, click **Activity**. The status column displays the current status for each operation.




Operation statuses when restoring a table include the following:

  * Waiting to copy
  * Restoring backup
  * Initializing
  * Ready-optimizing
  * Ready



Operation statuses when creating a backup include the following:

  * Creating backup
  * Backup complete



Operation statuses when copying a backup include the following:

  * Copying backup
  * Copied backup



###  gcloud 

To check the status of a backup or restore operation, you need the unique ID of the operation. The following is an example of an operation ID:
    
    
    `instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635`
    

After you run a command to create a backup or restore to a new table using the option `--async`, the terminal displays the operation ID.

  1. Copy the operation ID.

  2. Run the [`gcloud bigtable operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/operations/describe) command:
         
         gcloud bigtable operations describe OPERATION_ID
         

Replace `OPERATION_ID` with the operation ID that you copied.

Example:
         
         gcloud bigtable operations describe \
             instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635
         

You can execute this command every few moments until the value for `DONE` is `TRUE`.




If you don't know the operation ID, either because you didn't just execute the command or you are in a different terminal window, you can view a list of operations for the instance and determine which operation you want to check.

  1. View a list of recent operation activity for the instance that contains the table you are backing up or restoring to:
         
         gcloud bigtable operations list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance .

The terminal displays a list of operations in columns labeled `NAME`, `START_TIME`, `END_TIME`, and `DONE`. The value in the `NAME` column is the operation ID.

  2. Beginning with the first item on the list, copy the operation ID.

  3. Use [`gcloud bigtable operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/operations/describe) to view metadata for the operation:
         
         gcloud bigtable operations describe OPERATION_ID
         

Replace `OPERATION_ID` with the operation ID that you copied.

Example:
         
         gcloud bigtable operations describe \
             instances/instance-name/tables/table-name/locations/us-east1-b/operations/917168358249360635
         

  4. If the metadata for an operation **shows a value for`backupInfo`**, you have found the correct operation, and you can repeat this command every so often until the value for `DONE` is `TRUE`.

If the metadata does not show a value for `backupInfo`, check the next operation from the list of operations displayed in Step 1.




## Modify a backup or backup copy

You can modify the expiration date or retention period of an existing backup, whether created manually or by an automated backup policy, or a backup copy. In Enterprise edition, you can extend the expiration date of a backup to up to 90 days from the backup creation time. In Enterprise Plus edition, you can extend the expiration date to up to 365 days from the backup creation time. You can also convert a hot backup to a standard backup.

###  Console 

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the backup.

  3. In the left navigation pane, click **Backups**.

  4. To change the backup expiration date and time of a backup, follow these steps:

     1. For the backup that you want to modify, click the more_vert menu next to **Restore** , and then click **Edit**.

     2. In the **Backup expiration** section, set the date and time, and then click **Save**.

  5. To set the hot-to-standard transition date and time of a hot backup, follow these steps:

     1. For the hot backup that you want to modify, click the more_vert menu next to **Restore** , and then click **Edit**.

     2. In the **Update hot to standard** section, set the date and time, and then click **Save**.




###  gcloud 

The gcloud CLI lets you modify the expiration date or period for a backup or backup copy. You can also convert a hot backup to a standard backup.

  1. View a list of backups:
         
         gcloud bigtable backups list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance .

The terminal displays a list of backups.

  2. Note the backup and cluster IDs for the backup you need to update.

  3. Run the [`gcloud bigtable backups update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/backups/update) command to add a new expiration date or retention period or to convert a hot backup to a standard backup:
         
         gcloud bigtable backups update BACKUP_ID \
             --instance=INSTANCE_ID \
             --cluster=CLUSTER_ID \
             --expiration-date=EXPIRATION_DATE \
             --retention-period=RETENTION_PERIOD
         

Replace the following:

     * `BACKUP_ID`: the unique ID for a backup
     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 
     * `EXPIRATION_DATE`: a date in the future, up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition. The value must be formatted as a "Zulu" UTC timestamp, accurate to nanoseconds—for example, `2019-10-02T15:01:23.045123456Z`.
     * `RETENTION_PERIOD`: for backups, a period of up to 90 days in Enterprise edition or up to 365 days in Enterprise Plus edition. For backup copies, a period of up to 30 days. The value must be expressed as a number with a unit of `m`, `h`, or `d` (minutes, hours, or days)—for example, `36h` or `89d`.

The command accepts the following optional flag: 

     * `--hot-to-standard-time=HOT_TO_STANDARD_TIME`: the date and time when Bigtable should convert the backup from a hot backup to a standard backup. This value must be at least 24 hours after the backup creation time—for example, `2024-08-02T15:01:23.045123456Z`.

You can alternatively provide a relative duration date and time, such as `+P30D` for 30 days. For more information, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).

  4. Run the [`gcloud bigtable instances backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/backups/describe) command to verify that you have successfully updated the expiration:
         
         gcloud bigtable backups describe BACKUP_ID \
             --instance=INSTANCE_ID \
             --cluster=CLUSTER_ID
         

Replace the following:

     * `BACKUP_ID`: the unique ID for a backup
     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the permanent identifier for the cluster 



## Delete a backup

If you want to delete a backup after creating a copy of it, check the status to verify that the copy operation is complete.

###  Console 

  1. In the Google Cloud console, go to the Bigtable **Instances** page.

[Open the instance list](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the backup.

  3. In the left navigation pane, click **Backups**.

  4. For the backup you need to delete, expand the More menu next to the word **Restore** , then click **Delete**.

  5. Enter the backup ID in the **Confirm deletion** field, then click **Delete**.




###  gcloud 

  1. View a list of backups:
         
         gcloud bigtable backups list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance .

The terminal displays a list of backups.

  2. Note the backup ID and the ID of the cluster it is stored on.

  3. Run the [`gcloud bigtable instances backups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/backups/delete) command:
         
         gcloud bigtable backups delete BACKUP_ID \
             --instance=INSTANCE_ID \
             --cluster=CLUSTER_ID
         

Replace the following:

     * `BACKUP_ID`: the backup ID that you noted
     * `INSTANCE_ID`: the permanent identifier for the instance 
     * `CLUSTER_ID`: the cluster ID that you noted



## What's next

  * Read more about [backups](https://docs.cloud.google.com/bigtable/docs/backups).
  * Learn how to [import and export](https://docs.cloud.google.com/bigtable/docs/import-export) Bigtable data.
  * Review the Bigtable section of [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
