---
url: https://docs.cloud.google.com/storage/docs/samples/storage-get-bucket-metadata/
title: Get a bucket's metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-02T05:40:32.710556+00:00
---

# Get a bucket's metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-get-bucket-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Get a bucket's metadata Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve metadata from a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enable and use object retention configurations](https://docs.cloud.google.com/storage/docs/using-object-lock)
  * [Get bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata)
  * [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles)
  * [Set up and view CORS configurations](https://docs.cloud.google.com/storage/docs/using-cors)
  * [Use customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)
  * [Using bucket labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> bucket_metadata =
          client.GetBucketMetadata(bucket_name);
      if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
      std::cout << "The metadata for buck<<et "  bucket>_metada<<ta-name()  " is<< "
              <<   *bucket_metadata  "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetBucketMetadataSample
    {
        public Bucket GetBucketMetadata(string bucketName = "your-unique-bucket-name")
        {
            var [storage = Sto](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html)r[ageCli](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)ent.Create();
            var bucket = storage.GetBucket(bucket[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketOptions.html), new GetBucketOptions { Pro[jection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html) = P[roje](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full)ction.Full });
            Console.WriteLine($"Bucket:\t{bucket.Name}");
            Console.WriteL[ine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Acl)($"Acl:\t{bucket.Acl}");
            Console.WriteLine($"Billing:\t{bucket.Billing}");
            Console.WriteLine($"Cors:\t{bucket.Cors}");
            Console.WriteLine($"DefaultEventBasedHold:\t{bucket.DefaultEventBasedHold}");
            Console.WriteLine($"DefaultObjectAcl:\t{bucket.DefaultObjectAcl}");
            Console.WriteLine($"Encryption:\t{bucket.Encryption}");
            if (bucket.Encryption != null)
            {
                Console.WriteLine($"KmsKeyName:\t{bucket.Encryption.DefaultKmsKeyName}");
            }
            Console.WriteLine($"Id:\t{bucket.Id}");
            Console.WriteLine($"Kind:\t{bucket.Kind}");
            Console.WriteLine($"Lifecycle:\t{bucket.Lifecycle}");
            Console.WriteLine($"Location:\t{bucket.Location}");
            Console.WriteLine($"LocationType:\t{bucket.LocationType}");
            Console.WriteLine($"Logging:\t{bucket.Logging}");
            Console.WriteLine($"Metageneration:\t{bucket.Metageneration}");
            Console.WriteLine($"ObjectRetention:\t{bucket.ObjectRetention}");
            Console.WriteLine($"Owner:\t{bucket.Owner}");
            Console.WriteLine($"ProjectNumber:\t{bucket.ProjectNumber}");
            Console.WriteLine($"RetentionPolicy:\t{bucket.RetentionPolicy}");
            Console.WriteLine($"SelfLink:\t{bucket.SelfLink}");
            Console.WriteLine($"StorageClass:\t{bucket.StorageClass}");
            Console.WriteLine($"TimeCreated:\t{bucket.TimeCreated}");
            Console.WriteLine($"Updated:\t{bucket.Updated}");
            Console.WriteLine($"Versioning:\t{bucket.Versioning}");
            Console.WriteLine($"Website:\t{bucket.Website}"[;](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Key));
            Console.WriteLine($"TurboReplication:\t{bucket.Rpo}");
            if (bucket.Labels != null)
            {
                Console.WriteLine("Labels:");
                foreach (var label in bucket.Labels)
                {
                    Console.WriteLine($"{label.Key}:\t{label.Value}");
                }
            }
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // getBucketMetadata gets[ the b](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)ucket metadata.
    func getBucketM[etadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs)(w io.Writer, bucketName string) (*storage.BucketAttrs, error) {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.W[ithTim](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)eout(ctx, time.Second*10)
    	defer cancel()
    	attrs, err := client.Bucket(bucketName).Attrs(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "BucketName: %v\n", attrs.Name)
    	fmt.Fprintf(w, "Location: %v\n", attrs.Location)
    	fmt.Fprintf(w, "LocationType: %v\n", attrs.LocationType)
    	fm[t](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPO).Fprintf(w, "StorageClass: %v\n", attrs.StorageClass)
    	fmt.Fprintf(w, "Turbo replication (RPO): %v\n", attrs.RPO)
    	fmt.Fprintf(w, "TimeCreated: %v\n", attrs.Created)
    	fmt.Fprintf(w, "Metageneration: %v\n", attrs.MetaGeneration)
    	fmt.Fprintf(w, "PredefinedACL: %v\n", attrs.PredefinedACL)
    	if attrs.Encryption != nil {
    		fmt.Fprintf(w, "DefaultKmsKeyName: %v\n", attrs.Encryption.DefaultKMSKeyName)
    	}
    	if attrs.Website != nil {
    		fmt.Fprintf(w, "IndexPage: %v\n", attrs.[Website.MainPag](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy)eSuffix)
    		fmt.Fprintf(w, "NotFoundPage: %v\n", attrs.W[ebsite](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).NotFoundPage)
    	}
    	fmt.Fprintf(w, "DefaultEventBasedHold: %v\n"[, attrs.Default](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy)EventBasedHold)
    	if attrs.RetentionPolicy != nil {
    		fmt.Fprintf(w, "[RetentionEffect](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy)iveTime: %v\n", attrs.RetentionPolicy.EffectiveTime)
    		fmt.Fprintf(w, "RetentionPeriod: %v\n", attrs.RetentionPolicy.RetentionPeriod)
    		fmt.Fprintf(w, "RetentionPolicyIsLocked: %v\n", attrs.RetentionPolicy.IsLocked)
    	}
    	fmt.Fprintf(w, "ObjectRetentionMode: %v\n", attrs.ObjectRetentionMode)
    	fmt.Fprintf(w, "RequesterPays: %v\n", attrs.Request[erPa](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS)ys)
    	fmt.Fprintf(w, "VersioningEnabled: %v\n", attrs.[Vers](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS)ioningEnabled)
    	if attrs.Logging != nil {
    		fmt.Fprintf(w, "LogBucket: %v\n", attrs.Logging.LogBucket)
    		fmt.Fprintf(w, "LogObjectPrefix: %v\n", attrs.Logging.LogObjectPrefix)
    	}
    	if attrs.CORS != nil {
    		fmt.Fprintln(w, "CORS:")
    		for _, v := range attrs.CORS {
    			fmt.Fprintf(w, "\tMaxAge: %v\n", v.MaxAge)
    			fmt.Fprintf(w, "\tMethods: %v\n&quot;, v.Methods)
    			fmt.Fprintf(w, "\tOrigins: %v\n", v.Origins)
    			fmt.Fprintf(w, "\tResponseHeaders: %v\n", v.ResponseHeaders)
    		}
    	}
    	if attrs.Labels != nil {
    		fmt.Fprintf(w, "\n\n\nLabels:")
    		for key, value := range attrs.Labels {
    			fmt.Fprintf(w, "\t%v = %v\n", key, value)
    		}
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Map;
    
    public class GetBucketMetadata {
      public static void getBucketMetadata(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-buck[et-name](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html)";
    
      [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html)Storage storage = StorageOptions.newBuilder().setProjectId[(projectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)).build().getService();
    
        // Select all fields. Fields can be selected individually e.g. Storage.B[ucketF](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html)ield.NAME
        Bucket bucke[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_) =
            storage.get(bucketName, Storage.BucketGetOption.fields(Storage.BucketField.values()));
    
        // Print bucket metadata
        System.out.println("BucketName: " + bucket.getName());
        System.out.println("[;DefaultEventBasedHold: ](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultEventBasedHold__)" + bucket.getDefaultEventBasedHold());
        System.out[.println("Defau](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultKmsKeyName__)ltKmsKeyName: " + bucket.getDefaultKmsKeyName());
        System.out.println("Id: " + bucket.getGe[neratedId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getIndexPage__)());
        System.out.println("IndexPage: " + bucket.getIndexPage());
        System.out.println("Location: &[quot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getLocationType__) + bucket.getLocation());
        System.out.println("LocationType: " + bucket.getLocationType());
        System.out.println("Met[ageneration: &q](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getNotFoundPage__)uot; + bucket.getMetageneration());
        System.out.println("[;NotFoundPage: "](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__) + bucket.getNotFoundPage());
        System.out.println("Re[tentionEffectiveTi](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionPeriod__)me: " + bucket.getRetentionEffectiveTime());
        System.out.[println("Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)Period: " + bucket.getRetentionPeriod());
        System.out.println("RetentionPolicyIsLocked: " + bucket.retentionPolicyIsLocked());
        System.out.println("RequesterPays: " + buc[ket](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributeView.html#com_google_cloud_storage_contrib_nio_CloudStorageFileAttributeView_name__).requesterPays());
        System.out.println("SelfLink: " + bucket.getSelfLink());
        System.out.println("Storage[Class: "](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_versioningEnabled__) + bucket.getStorageClass().name());
        System.out.println("TimeCreated: " + bucket.getCreateTime());
        System.out.println("VersioningEnabled: " + bucket.versioni<ngEnabled());
    >    System.out.println("ObjectRetention: " + bucket.getObjectRetention());
        if (bucket.getLabels() != null) {
          System.out.println("\n\n\nLabels:");
          for (Map.EntryString, String label : bucket.getLabels().entrySet()) {
            System.out.println(label.getKey() + "=" + label.getValue());
          }
        }
        if (bucket.getLifecycleRules() != null) {
          System.out.println("\n\n\nLifecycle Rules:");
          for (BucketInfo.LifecycleRule rule : bucket.getLifecycleRules()) {
            System.out.println(rule);
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Imports the Google Cloud client library
    const {Storage} = require(&[#39;@google-cloud/sto](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)rage');
    
    // Creates a client
    const storag[e](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html) = new Storage();
    
    async function getBucketMetadata() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // The ID of your GCS bucket
      // const bucketName = 'your-unique-bucket-name';
    
      // Get Bucket Metadata
      const [metadata] = await storage.bucket(bucketName).getMetadata();[
    
      ](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.notificationconfig.payloadformat.html)console.log(JSON.stringify(metadata, null, 2));
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get bucket metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_bucket_metadata(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $>storage-bucket($bucketName);
        $info = >$bucket-info();
    
        printf('Bucket Metadata: %s' . PHP_EOL, print_r($info, true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def bucket_metadata(bucket_name):
        """Prints out a bucket's metadata."""
        # bucket_name = 'yo[ur-buck](https://docs.cloud.google.com/python/docs/reference/storage/latest)e[t-name](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)'
    
        storage_client = sto[rage](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket).Client()
        bucket = storage_client.get_bucket(bucket_name)
    
        print(f"ID: {bucket.id}")
        print(f"Name: {bucket.name}")
        print(f"Sto[rage Cla](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)ss: {bucket.storage_class}")
        p[rint](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location_type)(f"Location: {bucket.location}&quo[t;](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_cors))
        print(f"Location Type: {bucket.location_t[ype](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold)}")
        print(f&quot;Cors: {bucket.cors}")
        print(f"Default Event Based Hold: {bucket.default_event_based_hold}")
        print(f"Default KMS Key Name: {bucket.default_kms_key_[name](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration)}")
        p[rint](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention)(f"Metageneration: {bucket.metageneration}")
        print(
            f["Public Access Prevention:](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time) {bucket.iam_configuration.public_access_p[revention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period)}"
        )
        print(f"Retention Effective Time:[ ](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_locked){bucket.retention_policy_effective_time}")
        print(f"Rete[ntion Period: ](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_object_retention_mode){bucket.retention_period}")
        print(f&qu[ot;Retention P](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_requester_pays)olicy Locked: {bucket.retention_policy_locked}")
        print(f"Object Retention Mode: {bucket.object_retention_mode}")
        pr[int](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_versioning_enabled)(f"Requester Pays: {bucket.requester_pays}["](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels))
        print(f"Self Link: {bucket.self_link}")
        print(f"Time Created: {bucket.time_created}")
        print(f"Versioning Enabled: {bucket.versioning_enabled}")
        print(f"Labels: {bucket.labels}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_bucket_metadata bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      stora[ge](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html) = Goo[gle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)::Cloud::Storage.new
      bucket  = storage.bucket bucket_name
    
      puts "ID:                       #{bucket.id}"
      puts "Name:                     #{bucket.name}"
      puts "Storage Class:            #{bucket.storage_class}"
      puts "Location:                 #{bucket.location}"
      puts "Location Type:            #{bucket.location_type}"
      puts "Cors:     [                ](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)#{bucket.cors}"
      puts "Default Event Based H[old: ](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)#{bucket.default_event_based_hold?}"
      puts "D[efault KMS Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) Name:     #{bucket.default_kms_key}"
      p[uts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) "Logging Bucket:           #{bucket.logging_bucket}"
      puts "Logging Prefix:           #{bucket.loggi[ng_prefix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Metageneration:           #{bucket.met[ageneration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}&quot;
      puts "Retention Effective Time: #{bu[cket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html).retention_effective_at}"
      puts "Retention Period:     [    ](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)#{bucket.retention_period}"
      puts "Retention Policy Locked:  #{bucket.retention_policy_locked?}"
      puts "Requester Pays:           #{bucket.requ[ester_pays](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Self Link:                [#{bucket.api](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)_url}"
      puts "Time Created:        [     ](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)#{bucket.created_at}"
      puts "Ve[rsio](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html)ning Enabled:       #{bucket.versioning?}"
      puts "Index Page:               #{bucket.webs[ite_](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html)main}"
      puts "Not[ Found](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html) Page:           #{bucket.website_4[04](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)}"
      pu[ts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html) "Labels:";
      bucket.labels.each do |key, value|
        puts " - #{key} = #{value}"
      end
      puts "Lifecycle Rules:"
      bucket.lifecycle.each do |rule|
        puts "#{rule.action} - #{rule.storage_class} - #{rule.age} - #{rule.matches_storage_class}"
      end
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("successfully obtained bucket metadata {bucket:?}&quot;);
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
