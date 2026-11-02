---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-from-template/
title: Create a VM instance from an instance template \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-02T05:41:14.550873+00:00
---

# Create a VM instance from an instance template  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-from-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a VM instance from an instance template Stay organized with collections  Save and categorize content based on your preferences. 

Use an instance template to create a VM instance in the specified project and zone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)



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
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstanceFromTemplate creates a Compute Engine VM instance from an instance template.
    func createInstanceFromTemplate(w io.Writer, projectID, zone, instanceName, instanceTemplateUrl string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// instanceTemplateUrl := "global/instanceTemplates/your_instance_template"
    
    	ctx := context.Background()
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    		},
    		SourceInstanceTemplate: &instanceTemplateUrl,
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.AttachedDisk;
    import com.google.cloud.compute.v1.AttachedDiskInitializeParams;
    import com.google.cloud.compute.v1.InsertInstanceRequest;
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstanceProperties;
    import com.google.cloud.compute.v1.InstanceTemplate;
    import com.google.cloud.compute.v1.InstanceTemplatesClient;
    import com.google.cloud.compute.v1.InstancesClient;
    import com.google.cloud.compute.v1.Operation;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceFromTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /*  TODO(developer): Replace these variables before running the sample.
            projectId - ID or number of the project you want to use.
            zone - Name of the zone you want to check, for example: us-west3-b
            instanceName - Name of the new instance.
            instanceTemplateURL - URL of the instance template using for creating the new instance.
            It can be a full or partial URL.
            Examples:
            - https://www.googleapis.com/compute/v1/projects/project/global/instanceTemplates/example-instance-template
            - projects/project/global/instanceTemplates/example-instance-template
            - global/instanceTemplates/example-instance-template
         */
        String projectId = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        String instanceTemplateUrl = "instance-template-url";
        createInstanceFromTemplate(projectId, zone, instanceName, instanceTemplateUrl);
      }
    
      // Create a new instance from template in the specified project and zone.
      public static void createInstanceFromTemplate(String projectId, String zone, String instanceName,
          String instanceTemplateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try (InstancesClient instancesClient = InstancesClient.create();
            InstanceTemplatesClient instanceTemplatesClient = InstanceTemplatesClient.create()) {
    
          InstanceTemplate instanceTemplate = instanceTemplatesClient.get(projectId,
              instanceTemplateName);
    
          // Adjust diskType field of the instance template to use the URL formatting 
          // required by instances.insert.diskType
          // For instance template, there is only a name, not URL.
          List<AttachedDisk> reformattedAttachedDisks = new ArrayList<>();
          for (AttachedDisk disk : instanceTemplate.getProperties().getDisksList()) {
            disk = AttachedDisk.newBuilder(disk)
                .setInitializeParams(AttachedDiskInitializeParams
                    .newBuilder(disk.getInitializeParams())
                    .setDiskType(
                        String.format(
                            "zones/%s/diskTypes/%s", zone, disk.getInitializeParams().getDiskType()))
                    .build())
                .build();
    
            reformattedAttachedDisks.add(disk);
          }
    
          // Clear existing disks and set the reformatted disks in the instance template.
          instanceTemplate = InstanceTemplate
              .newBuilder(instanceTemplate)
              .setProperties(InstanceProperties
                  .newBuilder(instanceTemplate.getProperties())
                  .clearDisks()
                  .addAllDisks(reformattedAttachedDisks)
                  .build())
              .build();
    
          InsertInstanceRequest insertInstanceRequest = InsertInstanceRequest.newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(Instance.newBuilder().setName(instanceName).build())
              .setSourceInstanceTemplate(instanceTemplate.getSelfLink()).build();
    
          Operation response = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            System.out.println("Instance creation from template failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance creation from template: Operation Status %s: %s ", instanceName,
                  response.getStatus());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    // const instanceTemplateUrl = 'YOUR_INSTANCE_TEMPLATE_URL'
    
    const compute = require('@google-cloud/compute');
    
    // Create a new instance from template in the specified project and zone.
    async function createInstanceFromTemplate() {
      const instancesClient = new compute.InstancesClient();
    
      console.log(
        `Creating the ${instanceName} instance in ${zone} from template ${instanceTemplateUrl}...`
      );
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
        },
        sourceInstanceTemplate: instanceTemplateUrl,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.ZoneOperationsClient();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance created.');
    }
    
    createInstanceFromTemplate();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
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
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_instance_from_template(
        project_id: str, zone: str, instance_name: str, instance_template_url: str
    ) -> compute_v1.Instance:
        """
        Creates a Compute Engine VM instance from an instance template.
    
        Args:
            project_id: ID or number of the project you want to use.
            zone: Name of the zone you want to check, for example: us-west3-b
            instance_name: Name of the new instance.
            instance_template_url: URL of the instance template used for creating the new instance.
                It can be a full or partial URL.
                Examples:
                - https://www.googleapis.com/compute/v1/projects/project/global/instanceTemplates/example-instance-template
                - projects/project/global/instanceTemplates/example-instance-template
                - global/instanceTemplates/example-instance-template
    
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        instance_insert_request = compute_v1.InsertInstanceRequest()
        instance_insert_request.project = project_id
        instance_insert_request.zone = zone
        instance_insert_request.source_instance_template = instance_template_url
        instance_insert_request.instance_resource.name = instance_name
    
        operation = instance_client.insert(instance_insert_request)
        wait_for_extended_operation(operation, "instance creation")
    
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
