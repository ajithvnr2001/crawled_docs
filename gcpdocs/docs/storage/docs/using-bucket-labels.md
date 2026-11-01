---
url: https://docs.cloud.google.com/storage/docs/using-bucket-labels/
title: Using bucket labels \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:35:49.470231+00:00
---

# Using bucket labels  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-bucket-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Using bucket labels Stay organized with collections  Save and categorize content based on your preferences. 

_Labels_ let you organize your Cloud Storage buckets using key-value metadata pairs. You can add, modify, remove, and view these pairs to categorize your resources. For background information, see [Bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels).

## Required roles

In order to get the required permissions for adding and managing bucket labels, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket.

This [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles) contains the permissions required to add and manage bucket labels. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.buckets.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Add, modify, or remove a bucket's labels

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to add, modify, or remove labels.

  3. In the **Bucket details** page, click the **Configuration** tab.

  4. Click the **Edit** icon (_edit_) for **Labels**.

The label editor window appears.

     1. To add a label, click the _add_box_ **Add label** button, and specify a `key` and a `value` for your label.

     2. To modify an existing label, click its **Value** and a enter a new value.

     3. To remove a label, click the **Trash icon** associated with the label you want to remove.

  5. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To add a new label or update an existing label, use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--update-labels` flag. For example:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --update-labels=KEY_1=VALUE_1

Where

  * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.
  * `KEY_1` is the key name for your label. For example, `pet`.
  * `VALUE_1` is the value for your label. For example, `dog`.



To remove an existing label, use the `-remove-labels` flag. For example:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --remove-labels=KEY_1

You can change multiple labels using the previous commands by including the labels in a comma-separated list within the relevant flag. For example, `--update-labels=blue-key=cyan,red-key=ruby`.

To remove all labels attached to a bucket, use the following command:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --clear-labels

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& label_key, std::string const& label_value) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetLabel(label_key, label_value));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully set lab<<el "  <<label_ke<<y  " to "  labe<<l_value
            <<     &quo>t; on b<<ucket  "  upd<<ated-name()  ".";
      std::cout  " T&he bucket labe>ls are now:";
      for (<<auto con<<st kv : up<<dated-<<labels()) {
        std::cout  &<<quot;\n  "  kv.first  ": "  kv.second;
      }
      std::cout  "\n";
    }

The following sample removes the specified label from a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& label_key) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().ResetLabel(label_key));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully reset lab<<el "  <<label_key  " on bucket << "
     >       <<     updated-name() > ".";
      if (updated-labe<<ls().empty()) {
        std::cout  " The bucket now has no label<<s.\n";
        return;
      }
      std::cout  " T&he bucket labe>ls are now:";
      for (<<auto con<<st kv : up<<dated-<<labels()) {
        std::cout  &<<quot;\n  "  kv.first  ": "  kv.second;
      }
      std::cout  "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class BucketAddLabelSample
    {
        public Bucket BucketAddLabel(
            string bucketName = "your-bucket-name",
            string labelKey = "label-key-to-add",
            string labelValue = "label-value-to-add"[)
        {
         ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) [  var ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)storage = StorageClient.Create();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Labels == null)
            {
                <bucket.Labels >= new Dictionarystring, string();
            }
            bucket.Labels.Add(labelKey, labelValue);
    
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Added label {labelKey} with value {labelValue} to bucket {bucketName}.");
            return bucket;
        }
    }

The following sample removes the specified label from a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketRemoveLabelSample
    {
        public Bucket BucketRemoveLabel(string bucketName = "your-bucket-name", string labelKey = "label-key-to-remove")
        {
      [      ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html)var stor[age](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create) = StorageClient.Create();
            var bucket = storage.GetBucket(bucketName);
    
            if (bu&&cket.Labels != null  bucket.Labels.Keys.Contains(labelKey))
            {
                bucket.Labels.Remove(labelKey);
                bucket = storage.UpdateBucket(bucket);
                Console.WriteLine($"Removed label {labelKey} from bucket {bucketName}.");
            }
            else
            {
                Console.WriteLine($"No such label available on {bucketName}.");
            }
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // addBucketLabel a[dds a ](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)label on a bucket.
    func addBucketLabel(w io.Writer, bucketName, labelName, labelValue string) error {
    	// bucketName := "bucket-name"
    	// labelName := "label-name"
    	// labelValue := "label-value"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	c[tx](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket), cancel := context.WithTimeout(ctx, time.Second*[10)
    	defer cancel()](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate)
    
    	bucket := client.Buck[et](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate_SetLabel)(bucketName)
    	bucketAttrsToUpdate := storage.BucketAttrsToUpdate{}
    	bucketAttrsToUpdate.SetLabel(labelName, labelValue)
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Added label %q with value %q to bucket %v\n", labelName, labelValue, bucketName)
    	return nil
    }
    

The following sample removes the specified label from a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // removeBucketLabel removes[ a lab](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)el on a bucket.
    func removeBucketLabel(w io.Writer, bucketName, labelName string) error {
    	// bucketName := "bucket-name"
    	// labelName := "label-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel[ := co](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)ntext.WithTimeout(ctx, time.Second*10)
    	defer[ cancel()
    
    	bucket ](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate):= client.Bucket(bucketN[ame](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate_DeleteLabel))
    	bucketAttrsToUpdate := storage.BucketAttrsToUpdate{}
    	bucketAttrsToUpdate.DeleteLabel(labelName)
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Removed label %q from bucket %v\n", labelName, bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.HashMap;
    import java.util.Map;
    
    public class AddBucketLabel {
      public static void addBucketLabel(
          String projectId, String bucketName, String labelKey, String labelValue) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The key of the label to add
        // String labelKey = "label-key-to-add";
    
        // The value of the label to add
        // String labelValue = <"label-va>lue-to-add";
    
        M<>apString, String newLabels = new HashMap();
        ne[wLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).put(labelK[ey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html), labelValue);
    
        Storage storage = StorageOptions.newBu[ilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)().setProject[Id](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html)(projectId).build().ge[tSe](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)rvice();
        Bucket b<ucket = storag>e.get(bucketName);
        MapString, String labels = bucket.getLabels();
        if (labels != null) {
          new[Labels](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__).putAll(labels);
        }
        bucket.toBuilder().setLabels(newLabels).build().update();
    
        System.out.println(
            "Added label " + labelKey + " with value &quot; + labelValue + " to bucket " + bucketName + ".");
      }
    }

The following sample removes the specified label from a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.HashMap;
    import java.util.Map;
    
    public class RemoveBucketLabel {
      public static void removeBucketLabel(String projectId, String bucketName, String labelKey) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The key of the label to remove from the bucket
        // String labelKey = "la[bel-key](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html)-to-remove&[quot;;](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html)
    
        Storage storage = StorageOptions.newBuilder().se[tProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)(projectId).<build().getSer>vice();
    
        MapString, Strin<>g labelsToRemove = new HashMap();
        labelsToRem[ove](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html).put(labelKey, null);[
    
     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)   Bucket bucket = st<orage.get(buck>etName);
        MapString, String labels;
        if (bucket.getLabels() == null<>) {
          labels = new HashMap();
        } else {
          labels = new HashMap(bucket.getLabels());
        }
        labels.putAl[l](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)(labelsToRemove);
        bucket.toBuilder().setLabels(labels).build().update();
    
        System.out.println("Removed label " + labelKey + " from bucket " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The key of the label to add
    // const labelKey = 'label-key-to-add';
    
    // The value of the label to add
    // const labelValue = 'label-value-to-add';
    
    // Imports the Google Cloud client library
    con[st](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html) {Storage} = require('@google-cloud/storage');
    
    // Creat[es a cl](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)ient
    const storage = new Storage();
    
    const labels = {
      [labelKey]: labelValue,
    };
    
    async function addBucketLabel() {
      await storage.bucket(bucketName).setMetadata({labels});
      console.log(`Added label to bucket ${bucketName}`);
    }
    
    addBucketLabel().catch(console.error);

The following sample removes the specified label from a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The key of the label to remove from the bucket
    // const labelKey = 'label-key-to-remove';
    
    // Imports the Google Cloud client library
    const {Stor[age](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)} = require('@google-cloud/storage');
    
    // Creates a cli[ent](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)
    const storage = new Storage();
    
    async function removeBucketLabel() {
      const labels = {};
      // To remove a label set the value of the key to null.
      labels[labelKey] = null;
      await storage.bucket(bucketName).setMetadata({labels});
      console.log(`Removed labels from bucket ${bucketName}`);
    }
    
    removeBucketLabel().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Adds or updates a bucket label.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $labelName The name of the label to add.
     *        (e.g. 'label-key-to-add')
     * @param string $labelValue The value of the label to add.
     *        (e.g. 'label-value-to-add')
     */
    function add_bucket_label(string $bucketName, string $labelName, string $labelValue): void
    {
        $storage = new StorageClient();>
        $bucket = $storage-bucket($bucketName);
        $n>ewLabels = [$labelName = $l>abelValue];
        $b>ucket-update(['labels' = $newLabels]);
        printf('Added label %s (%s) to %s' . PHP_EOL, $labelName, $labelValue, $bucketName);
    }

The following sample removes the specified label from a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Removes a label from a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $labelName The name of the label to remove.
     *        (e.g. 'label-key-to-remove')
     */
    function remove_bucket_label(string $bucketName, string $labelName): void
    {
        $storage = new StorageClient();
        $bu>cket = $storage-bucket($bucketName);
        $labels> = [$labelName = nul>l];
        $bucket-up>date(['labels' = $labels]);
        printf('Removed label %s from %s' . PHP_EOL, $labelName, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import pprint
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def add_bucket_label(bucket_name):
        """Add a label to a bucket."""
        # bucket_name = "your-[bucket-](https://docs.cloud.google.com/python/docs/reference/storage/latest)n[ame&qu](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)ot;
    
        storage_client = storag[e](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket).Client()
    
        bucket = storage_client.get_[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)(bucket_name)
        labels = bucket.labels
       [ label](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)s["example"] = "label"
        bucket.labels = labels
        bucket.patch()
    
        print(f&[quot;U](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)pdated labels on {bucket.name}.")
        pprint.pprint(bucket.labels)
    
    

The following sample removes the specified label from a bucket:
    
    
    import pprint
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def remove_bucket_label(bucket_name):
        """Remove a label from a bucket."""
        # bucket_name = "your-[bucket-](https://docs.cloud.google.com/python/docs/reference/storage/latest)n[ame&qu](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)ot;
    
        storage_client = stora[ge](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket).Client()
        bucket = storage_client.get_b[ucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)(bucket_name)
    
        labels = bucket.labels
    
        if "example" in [labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels):
            del labels["example"]
    
        bucket.labels = labels
        bucket.patch()
    
        print(f&[quot;R](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)emoved labels on {bucket.name}.")
        pprint.pprint(bucket.labels)
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    def add_bucket_label bucket_name:, label_key:, label_value:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The key of the label to add
      # label_key = "label-key-to-add"
    
      # The value of the label to add
      # label_value = "label-value-to-add"
    
      require "google/cloud/st[orage&q](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html)u[ot;](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      storage = Google::Cloud::Storage.new
      bucket  = storage.bucket bucket_name
    
      bucket.update do |bucket|
        bucket.labels[label_key] = label_value
      end
    
      puts "Added label #{label_key} with value #{label_value} to #{bucket_name}"
    end

The following sample removes the specified label from a bucket:
    
    
    def remove_bucket_label bucket_name:, label_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The key of the label to remove from the bucket
      # label_key = "label-key-to-remove"
    
      require "google/cloud/storage"[;](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html)
    
      sto[rag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)e = Google::Cloud::Storage.new
      bucket  = storage.bucket bucket_name
    
      bucket.update do |bucket|
        bucket.labels[label_key] = nil
      end
    
      puts "Deleted label #{label_key} from #{bucket_name}"
    end

### Rust

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        label_key: &str,
        label_value: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let mut labels = bucket.labels.clone();
        labels.insert(label_key.to_string(), label_value.to_string());
    
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_labels(labels))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["labels"]))
            .send()
            .await?;
        println!("Successfully added label {label_key}={label_value} to bucket {bucket_id}");
        println!("{:?}", bucket.labels);
        Ok(())
    }

The following sample removes the specified label from a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        label_key: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let mut labels = bucket.labels.clone();
        labels.remove(label_key);
    
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_labels(labels))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["labels"]))
            .send()
            .await?;
        println!("Successfully removed label {label_key} from bucket {bucket_id}");
        println!("{:?}", bucket.labels);
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "labels";: {
             "KEY_1": "VALUE_1"
           }
         }

Where

     * `KEY_1` is the key name for your label. For example, `pet`.
     * `VALUE_1` is the value for your label. For example, `dog`. If you want to remove a key, use `null` in place of `"<var>VALUE_1</var>"`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=labels"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.



You can add, edit, or remove multiple `key:value` pairs in a request.

### XML API

**Note:** A label setting request using the XML API replaces all existing labels applied to the specified bucket with the labels included in the request. If there are labels applied to the bucket that you want to keep, specify them in your request.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the following information:
         
         <Tagging>
           <TagSet>
             <Tag>
               <Key>KEY_1</Key>
               <Value>VALUE_1</Value>
             </Tag>
           </TagSet>
         </Tagging>

Where:

     * `KEY_1` is the key name for your label. For example, `pet`.
     * `VALUE_1` is the value for your label. For example, `dog`.

Note that you can add multiple `<Tag>` elements in a request. If you want to remove all labels on a bucket, use a single, empty `<Tag>` element in the file:
    
    <Tagging>
      <TagSet>
        <Tag>
        </Tag>
      </TagSet>
    </Tagging>

  3. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request and `tagging` query string parameter:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?tagging"

Where:

     * `XML_FILE_NAME` is the path for the XML file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.



## View bucket labels

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose labels you want to view.

  3. Click the **Configuration** tab.




The labels set on the bucket are listed in the **Labels** field.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(labels)"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.

If successful and labels exist for the bucket, the response is similar to the following:
    
    
    labels:
      red-key: ruby
      blue-key: cyan

If successful and labels to not exist for the bucket, the response is similar to the following:
    
    
    null

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the `fields=labels` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=labels"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.




The response looks like the following example:
    
    
    {
      "labels" : {
         (your_label_key): your_label_value
       },
    }

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) request and `tagging` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?tagging"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.




The response looks like the following example:
    
    
    <Tagging>
      <TagSet>
        <Tag>
          <Key>your_label_key</Key>
          <Value>your_label_value</Value>
        </Tag>
      </TagSet>
    </Tagging>

## What's next

  * Learn about [bucket tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags).
  * [Get additional bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
