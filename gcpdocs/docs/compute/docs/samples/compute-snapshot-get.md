---
url: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-get/
title: Get a snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:42:41.115769+00:00
---

# Get a snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Get a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This sample retrieves information about a snapshot.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // getSnapshot prints a name of a disk snapshot in the specified project.
    func getSnapshot(w io.Writer, projectID, snapshotName string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    
    	ctx := context.Background()
    	snapshotsClient, err := compute.NewSnapshotsRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	reqSnapshot := &computepb.GetSnapshotRequest{
    		Project:  projectID,
    		Snapshot: snapshotName,
    	}
    
    	snapshot, err := snapshotsClient.Get(ctx, reqSnapshot)
    	if err != nil {
    		return fmt.Errorf("unable to get snapshot: %w", err)
    	}
    
    	fmt.Fprintf(w, "Found snapshot: %s\n", snapshot.GetName())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package compute.disks;
    
    import com.google.cloud.compute.v1.Snapshot;
    import com.google.cloud.compute.v1.SnapshotsClient;
    import java.io.IOException;
    
    public class GetSnapshot {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the snapshot to look up.
        String snapshotName = "YOUR_SNAPSHOT_NAME";
    
        getSnapshot(projectId, snapshotName);
      }
    
      // Get information about a snapshot.
      public static void getSnapshot(String projectId, String snapshotName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
          Snapshot snapshot = snapshotsClient.get(projectId, snapshotName);
          System.out.printf("Retrieved the snapshot: %s", snapshot.getName());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import compute_v1
    
    
    def get_snapshot(project_id: str, snapshot_name: str) -> compute_v1.Snapshot:
        """
        Get information about a Snapshot.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            snapshot_name: the name of the snapshot you want to look up.
    
        Returns:
            A Snapshot object.
        """
    
        snapshot_client = compute_v1.SnapshotsClient()
    
        return snapshot_client.get(project=project_id, snapshot=snapshot_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
