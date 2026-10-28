---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-import-from-source/
title: Import from the source Mongo database \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:25:18.860868+00:00
---

# Import from the source Mongo database  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-import-from-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Import from the source Mongo database

This page describes the first stage of the [migration process](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-data) where you use a Datastream stream to capture the contents of your MongoDB-compatible source database and transfer them into a Cloud Storage bucket.

## Create YAML configuration files for the stream

In addition to usual command-line flags, creating a stream requires two configuration files in the YAML format:

  * The `mongo_source_config.yaml` file configures the selection of specific resources for migration, such as the database name. Mongo connectivity parameters such as the hostname, username, and password are all properties of the connection profile. However, the database (and any specific collections within that database) are a property of the stream.

  * The `gcs_dst_config.yaml` file configures the data placement within Cloud Storage. The Cloud Storage bucket and the root path within the bucket are properties of the connection profile. However, the data format and the data placement within the Cloud Storage bucket structure are a property of the stream.




The following command examples create these files and populate them with values from the [environment variables](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-configure-env-vars) that you've set earlier. As an alternative, you can create these files in any text editor and substitute the values manually.
    
    
    echo "$(cat <<EOF
    includeObjects:
      databases:
      - database: ${MONGODB_DATABASE_NAME}
    EOF
    )" > mongo_source_config.yaml
    
    echo "$(cat <<EOF
    path: "/${GCS_BUCKET_SUB_PATH}"
    avroFileFormat: {}
    EOF
    )" > gcs_dst_config.yaml
    

The previous example configures the full contents of $MONGODB_DATABASE_NAME for migration. It is also possible to limit the migration to specific collections within the database. For example, to migrate only the collections `users` and `chats` use the following:
    
    
    includeObjects:
      databases:
      - database: ${MONGODB_DATABASE_NAME}
        collections:
          - collection: users
          - collection: chats
    

## Create a Datastream stream

Next, create a stream that connects the source and the destination:

The stream label `json_canonical_mode=true` ensures that Datastream properly handles MongoDB document events that contain non-standard values like `Infinity` or `NaN`.
    
    
    gcloud datastream streams create "$DATASTREAM_NAME" \
    --display-name="$DATASTREAM_NAME" \
    --location="$LOCATION" \
    --source="$SRC_CONNECTION_PROFILE_NAME" \
    --destination="$DST_CONNECTION_PROFILE_NAME" \
    --mongodb-source-config=./mongo_source_config.yaml \
    --gcs-destination-config=./gcs_dst_config.yaml \
    --labels="json_canonical_mode=true" \
    --backfill-all
    

For more information about monitoring the Datastream stream creation, see [Troubleshooting](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-troubleshooting).

## Activate the Datastream stream

Finally, activate the new stream.

As the stream begins pulling data and streaming changes from the Mongo source, you can observe new directories and files created in the Cloud Storage bucket, under the path configured in the connection profile and the stream.

**Important:** At this point your MongoDB-compatible source database is **still the source of truth** for your application workloads. The database must continue to receive queries and updates until the migration [reaches a specific milestone](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-traffic) described later.

To activate the stream, run the following command:
    
    
    gcloud datastream streams update "$DATASTREAM_NAME" \
    --location="$LOCATION" \
    --state=RUNNING \
    --update-mask=state
    

## What's next

Proceed to [Write data into the destination database](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-write-to-destination).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
