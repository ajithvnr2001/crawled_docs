---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-pause-anywhere-cache/
title: Storage Control Pause Anywhere Cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-09T05:48:03.631652+00:00
---

# Storage Control Pause Anywhere Cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-pause-anywhere-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Pause Anywhere Cache Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Pause Anywhere Cache

## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& cache_name) {
      auto anywhere_cache = client.PauseAnywhereCache(cache_name);
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Paused anywhere cache: " << anywhere_cache->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlPauseAnywhereCacheSample
    {
        /// <summary>Pauses an anywhere cache instance in the specified bucket.</summary>
        /// <param name="bucketName">The name of the bucket that owns the anywhere cache instance.</param>
        /// <param name="anywhereCacheId">The unique identifier of the cache instance to pause.</param>
        public AnywhereCache StorageControlPauseAnywhereCache(string bucketName = "your-unique-bucket-name",
            string anywhereCacheId = "us-east1-b")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            // Set project to "_" to signify globally scoped bucket.
            string anywhereCacheName = $"projects/_/buckets/{bucketName}/anywhereCaches/{anywhereCacheId}";
    
            var request = new [PauseAnywhereCacheRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.PauseAnywhereCacheRequest.html)
            {
                Name = anywhereCacheName
            };
    
            [AnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache.html) pausedCache = storageControlClient.[PauseAnywhereCache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_PauseAnywhereCache_Google_Cloud_Storage_Control_V2_AnywhereCacheName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine($"Paused Anywhere Cache Instance: {pausedCache.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.AnywhereCache.html#Google_Cloud_Storage_Control_V2_AnywhereCache_Name)}");
    
            return pausedCache;
        }
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[PauseAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.PauseAnywhereCacheRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class AnywhereCachePause {
    
      public static void anywhereCachePause(String cacheName) throws IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [PauseAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.PauseAnywhereCacheRequest.html) request =
              [PauseAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.PauseAnywhereCacheRequest.html).newBuilder().setName(cacheName).build();
    
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache = storageControl.pauseAnywhereCache(request);
    
          System.out.printf("Paused anywhere cache: %s%n", anywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * Pauses an Anywhere Cache instance.
     *
     * This synchronous function stops the ingestion of new data for a cache that's in a RUNNING state.
     * While PAUSED, you can still read existing data (which resets the TTL), but no new data is ingested.
     * The cache can be returned to the RUNNING state by calling the resume function.
     *
     * @param {string} bucketName The name of the bucket where the cache resides.
     * Example: 'your-gcp-bucket-name'
     * @param {string} cacheName The unique identifier of the cache instance.
     * Example: 'my-anywhere-cache-id'
     */
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callPauseAnywhereCache() {
      const anywhereCachePath = controlClient.[anywhereCachePath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)(
        '_',
        bucketName,
        cacheName
      );
    
      // Create the request
      const request = {
        name: anywhereCachePath,
      };
    
      try {
        // Run request
        const [response] = await controlClient.pauseAnywhereCache(request);
    
        console.log(`Successfully paused anywhere cache: ${response.name}.`);
        console.log(`  Current State: ${response.state}`);
      } catch (error) {
        // Catch and handle potential API errors.
        console.error(
          `Error pausing Anywhere Cache '${cacheName}': ${error.message}`
        );
    
        if (error.code === 5) {
          // NOT_FOUND (gRPC code 5)
          console.error(
            `Please ensure the cache '${cacheName}' exists in bucket '${bucketName}'.`
          );
        } else if (error.code === 9) {
          // FAILED_PRECONDITION (gRPC code 9)
          console.error(
            `Cache '${cacheName}' may not be in a state that allows pausing (e.g., must be RUNNING).`
          );
        }
        throw error;
      }
    }
    
    callPauseAnywhereCache();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\PauseAnywhereCacheRequest;
    
    /**
     * Pauses an Anywhere Cache instance.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $anywhereCacheId Uniquely identifies the cache.
     *        (e.g. 'us-east1-b')
     */
    function pause_anywhere_cache(string $bucketName, string $anywhereCacheId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->anywhereCacheName('_', $bucketName, $anywhereCacheId);
    
        $request = new PauseAnywhereCacheRequest([
            'name' => $formattedName,
        ]);
    
        $response = $storageControlClient->pauseAnywhereCache($request);
    
        printf('Paused anywhere cache: %s', $response->getName());
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    # Pauses a specific Anywhere Cache instance in a Cloud Storage bucket.
    # This operation does not delete the cache; it can be resumed later using
    # the `resume_anywhere_cache` method.
    #
    # @param bucket_name [String] The name of the Cloud Storage bucket.
    # @param anywhere_cache_id [String] The ID of the Anywhere Cache instance to pause.
    #   This is often the zone where the cache is located, e.g., "us-east1-b".
    #
    # @example
    #   pause_anywhere_cache(
    #     bucket_name: "your-unique-bucket-name",
    #     anywhere_cache_id: "us-east1-b"
    #   )
    #
    def pause_anywhere_cache bucket_name:, anywhere_cache_id:
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
      name = "#{parent}/anywhereCaches/#{anywhere_cache_id}"
    
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::PauseAnywhereCacheRequest.new(
        name: name
      )
      # The request pauses the cache, but does not delete it.
      # The cache can be resumed later.
      # The cache is paused in the specified bucket.
      begin
        result = storage_control_client.pause_anywhere_cache request
        puts "Successfully #{result.state&.downcase} anywhereCache - #{result.name}."
      rescue Google::Cloud::Error => e
        puts "Failed to pause AnywhereCache. Error: #{e.message}"
      end
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        cache_id: &str,
    ) -> anyhow::Result<()> {
        let cache = client
            .pause_anywhere_cache()
            .set_name(format!(
                "projects/_/buckets/{bucket_id}/anywhereCaches/{cache_id}"
            ))
            .send()
            .await?;
        println!("Paused anywhere cache: {:?}", cache);
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
