---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-backup/
title: Create a backup \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:22:28.429483+00:00
---

# Create a backup  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-create-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Create a backup Stay organized with collections  Save and categorize content based on your preferences. 

Creates a table backup.

## Code sample

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import datetime
    
    from google.cloud import bigtable_admin_v2
    
    client = bigtable_admin_v2.[BigtableTableAdminClient](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.overlay.services.bigtable_table_admin.BigtableTableAdminClient.html)()
    cluster_path = client.[cluster_path](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.overlay.services.bigtable_table_admin.BigtableTableAdminClient.html#google_cloud_bigtable_admin_v2_overlay_services_bigtable_table_admin_BigtableTableAdminClient_cluster_path)(project_id, instance_id, cluster_id)
    table_path = client.[table_path](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.overlay.services.bigtable_table_admin.BigtableTableAdminClient.html#google_cloud_bigtable_admin_v2_overlay_services_bigtable_table_admin_BigtableTableAdminClient_table_path)(project_id, instance_id, table_id)
    
    # Backups must expire between 6 hours and 90 days after they are created
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        hours=8
    )
    print("Creating backup {} of table {}...".format(backup_id, table_id))
    operation = client.[create_backup](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.overlay.services.bigtable_table_admin.BigtableTableAdminClient.html#google_cloud_bigtable_admin_v2_overlay_services_bigtable_table_admin_BigtableTableAdminClient_create_backup)(
        parent=cluster_path,
        backup_id=backup_id,
        backup=bigtable_admin_v2.[Backup](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.types.Backup.html)(
            source_table=table_path, expire_time=expire_time
        ),
    )
    backup = operation.result()
    print("Created backup {}.".format(backup.name.split("/")[-1]))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
