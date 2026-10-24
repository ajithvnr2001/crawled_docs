---
url: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-delete-by-filter/
title: Delete snapshots by filter \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T05:49:24.227887+00:00
---

# Delete snapshots by filter  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-delete-by-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Delete snapshots by filter Stay organized with collections  Save and categorize content based on your preferences. 

This sample deletes all snapshots in a project that meet the filter criteria.

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
    	"google.golang.org/api/iterator"
    )
    
    // Deletes ALL disk snapshots in the project that match the filter
    func deleteByFilter(w io.Writer, projectID, filter string) error {
    	// projectID := "your_project_id"
    	// filter := ""
    	// Learn more about filters:
    	// https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.List[SnapshotsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)
    
    	ctx := context.Background()
    	snapshotsClient, err := compute.NewSnapshotsRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer s&napshotsClient.Close()
    
    	// List snapshots in the project with th&e filter applied
    	req := computepb.ListSnapshotsRequest{
    		Project: projectID,
    		Filter:  filter,
    	}
    	it := snapshotsClient.List(ctx, req)
    
    	// It[erat](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done)e over the list of snapshots
    	for {
    		snapshot, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if e&rr != nil {
    			return err
    		}
    
    		// Delete each snapshot that matches the filter[
    		r](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name)eq := computepb.DeleteSnapshotRequest{
    			Project:  projectID,
    			Snapshot: *snapshot.Name,
    		}
    
    		op, err := snapshotsClient.Delete(ctx, req)
    		if err != nil {
    			return fmt.Errorf("unable to delete snapshot: %w", err)
    		}
    
    		if err = op.Wait(ctx); err != nil {
    			return fmt.Errorf(&q[uot;](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name)unable to wait for the operation: %w", err)
    		}
    
    		fmt.Fprintf(w, "Snapshot %s deleted\n", *snapshot.Name)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package compute.disks;
    
    import com.google.cloud.compute.v1.[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteSnapshotsByFilter {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Filter to be applied when looking for snapshots for deletion. Learn more about filters here:
        // https://cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest
        String filter = "FILTER";
    
        deleteSnapshotsByFilter(projectId, filter);
      }
    
      // Deletes all snapshots in project that meet the filter criteria.
      public static void deleteSnapshotsByFilter(String projectId, String filter)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background [resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html)
        try (SnapshotsClien[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = SnapshotsClient.create()) {
          // Create the List Snap[shot request.](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html)
          ListSnapshotsRequest lis[tSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html) = ListSnapshotsRequest.newBuilder()
              .setProject(projectId)
              .setFilter(filter)
              .build();
    
          // Iterate through the resultant snapshots and dele[te them.](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html)
          for (Snapshot snapshot : snapshotsClient.list(listSnapshotsRequest).iter[ateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html)()) {
            Operation operation = snapshotsClient.deleteAsync(projectId, snapshot.getName())
                .get(3, TimeUnit.MINUTES);
    
      [      ](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)if (operation.hasE[rror](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() || opera[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).getStatus() != Status.DONE) {
    [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)     throw new Error("Snapshot delet[ion fail](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)ed!" + operation.getError());
            }
            System.out.printf("Snapshot deleted: %s", snapshot.getName());
          }
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int> = 300
    ) - Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)>
    
        return result
    
    
    def delete_snapshot(project_id: str, snapshot_name: str) - None:
        """
        Delete a snapshot of a disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want[ to use.](https://docs.cloud.google.com/python/docs/reference/compute/latest)
      [      snapshot_](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)name: name of the snapshot to delet[e.](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_delete)
        """
    
        snapshot_client = compute_v1.SnapshotsClient()
        operation = snapshot_client.delete(project=project_id, snapshot=snapshot_name)
    
        wait_for>_extended_operation(operation, "snapshot deletion")
    
    
    def list_snapshots(project_id: str, filter_: str = "") - Iterable[compute_v1.Snapshot]:
        """
        List snapshots from a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            filter_: filter to be applied when listing snapshots. Learn more about filters here:
                https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.type[s.ListSnap](https://docs.cloud.google.com/python/docs/reference/compute/latest)s[hotsRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)
    
        Returns:
          [  An itera](https://docs.cloud.google.com/python/docs/reference/compute/latest)b[le containing all Sn](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListSnapshotsRequest.html)apshots that match the provided filter.
        """
    
        snapshot_client = compute[_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_list).SnapshotsClient()
        request = compute_v1.ListSnapshotsRequest()
        request.project = project_id
        request.filter = filter_
    
        return snapshot_client.list(request)
    
    
    def delete_snapshots_by_filter(project_id: str, filter: str):
        """
        Deletes all snapshots in project that meet the filter criteria.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            filter: filter to be applied when looking for snapshots for deletion.
        """
        for snapshot in list_snapshots(project_id, filter):
            delete_snapshot(project_id, snapshot.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
