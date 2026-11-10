---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-grant-view-access/
title: Grant view access \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T06:00:30.985867+00:00
---

# Grant view access  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-grant-view-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Grant view access Stay organized with collections  Save and categorize content based on your preferences. 

Authorize and grant access to a view.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // updateViewDelegated demonstrates the setup of an authorized view, which allows access to a view's results
    // without the caller having direct access to the underlying source data.
    func updateViewDelegated(projectID, srcDatasetID, viewDatasetID, viewID string) error {
    	// projectID := "my-project-id"
    	// srcDatasetID := "sourcedata"
    	// viewDatasetID := "views"
    	// viewID := "myview"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	srcDataset := client.Dataset(srcDatasetID)
    	viewDataset := client.Dataset(viewDatasetID)
    	view := viewDataset.Table(viewID)
    
    	// First, we'll add a group to the ACL for the dataset containing the view.  This will allow users within
    	// that group to query the view, but they must have direct access to any tables referenced by the view.
    	vMeta, err := viewDataset.Metadata(ctx)
    	if err != nil {
    		return err
    	}
    	vUpdateMeta := bigquery.DatasetMetadataToUpdate{
    		Access: append(vMeta.Access, &bigquery.AccessEntry{
    			Role:       bigquery.ReaderRole,
    			EntityType: bigquery.GroupEmailEntity,
    			Entity:     "example-analyst-group@google.com",
    		}),
    	}
    	if _, err := viewDataset.Update(ctx, vUpdateMeta, vMeta.ETag); err != nil {
    		return err
    	}
    
    	// Now, we'll authorize a specific view against a source dataset, delegating access enforcement.
    	// Once this has been completed, members of the group previously added to the view dataset's ACL
    	// no longer require access to the source dataset to successfully query the view.
    	srcMeta, err := srcDataset.Metadata(ctx)
    	if err != nil {
    		return err
    	}
    	srcUpdateMeta := bigquery.DatasetMetadataToUpdate{
    		Access: append(srcMeta.Access, &bigquery.AccessEntry{
    			EntityType: bigquery.ViewEntity,
    			View:       view,
    		}),
    	}
    	if _, err := srcDataset.Update(ctx, srcUpdateMeta, srcMeta.ETag); err != nil {
    		return err
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.Acl;
    import com.google.cloud.bigquery.BigQuery;
    import com.google.cloud.bigquery.BigQueryException;
    import com.google.cloud.bigquery.BigQueryOptions;
    import com.google.cloud.bigquery.Dataset;
    import com.google.cloud.bigquery.Table;
    import java.util.ArrayList;
    import java.util.List;
    
    // Sample to grant view access on dataset
    public class GrantViewAccess {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String srcDatasetId = "MY_DATASET_ID";
        String viewDatasetId = "MY_VIEW_DATASET_ID";
        String viewId = "MY_VIEW_ID";
        grantViewAccess(srcDatasetId, viewDatasetId, viewId);
      }
    
      public static void grantViewAccess(String srcDatasetId, String viewDatasetId, String viewId) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
          Dataset srcDataset = bigquery.getDataset(srcDatasetId);
          Dataset viewDataset = bigquery.getDataset(viewDatasetId);
          Table view = viewDataset.get(viewId);
          // First, we'll add a group to the ACL for the dataset containing the view. This will allow
          // users within that group to query the view, but they must have direct access to any tables
          // referenced by the view.
          List<Acl> viewAcl = new ArrayList<>(viewDataset.getAcl());
          viewAcl.add(Acl.of(new Acl.Group("example-analyst-group@google.com"), Acl.Role.READER));
          viewDataset.toBuilder().setAcl(viewAcl).build().update();
          // Now, we'll authorize a specific view against a source dataset, delegating access
          // enforcement. Once this has been completed, members of the group previously added to the
          // view dataset's ACL no longer require access to the source dataset to successfully query the
          // view
          List<Acl> srcAcl = new ArrayList<>(srcDataset.getAcl());
          srcAcl.add(Acl.of(new Acl.View(view.getTableId())));
          srcDataset.toBuilder().setAcl(srcAcl).build().update();
          System.out.println("Grant view access successfully");
        } catch (BigQueryException e) {
          System.out.println("Grant view access was not success. \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import bigquery
    
    client = bigquery.Client()
    
    # To use a view, the analyst requires ACLs to both the view and the source
    # table. Create an authorized view to allow an analyst to use a view
    # without direct access permissions to the source table.
    view_dataset_id = "my-project.my_view_dataset"
    # Make an API request to get the view dataset ACLs.
    view_dataset = client.get_dataset(view_dataset_id)
    
    analyst_group_email = "example-analyst-group@google.com"
    access_entries = view_dataset.access_entries
    access_entries.append(
        bigquery.AccessEntry("READER", "groupByEmail", analyst_group_email)
    )
    view_dataset.access_entries = access_entries
    
    # Make an API request to update the ACLs property of the view dataset.
    view_dataset = client.update_dataset(view_dataset, ["access_entries"])
    print(f"Access to view: {view_dataset.access_entries}")
    
    # Group members of "data_analysts@example.com" now have access to the view,
    # but they require access to the source table to use it. To remove this
    # restriction, authorize the view to access the source dataset.
    source_dataset_id = "my-project.my_source_dataset"
    # Make an API request to set the source dataset ACLs.
    source_dataset = client.get_dataset(source_dataset_id)
    
    view_reference = {
        "projectId": "my-project",
        "datasetId": "my_view_dataset",
        "tableId": "my_authorized_view",
    }
    access_entries = source_dataset.access_entries
    access_entries.append(bigquery.AccessEntry(None, "view", view_reference))
    source_dataset.access_entries = access_entries
    
    # Make an API request to update the ACLs property of the source dataset.
    source_dataset = client.update_dataset(source_dataset, ["access_entries"])
    print(f"Access to source: {source_dataset.access_entries}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
