---
url: https://docs.cloud.google.com/compute/docs/samples/compute-delete-protection-get/
title: Get the deletion protection status of a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:58:48.379815+00:00
---

# Get the deletion protection status of a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-delete-protection-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Get the deletion protection status of a VM Stay organized with collections  Save and categorize content based on your preferences. 

Determine whether deletion protection is enabled for a specified VM.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Prevent accidental VM deletion](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion)



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
    
    // getDeleteProtection prints the state of delete protection flag of given instance.
    func getDeleteProtection(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance %s has DeleteProtection value: %v", instanceName, instance.GetDeletionProtection())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstancesClient;
    import java.io.IOException;
    
    public class GetDeleteProtection {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the new virtual machine.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
        getDeleteProtection(projectId, zone, instanceName);
      }
    
      // Returns the state of delete protection flag of given instance.
      public static boolean getDeleteProtection(String projectId, String zone,
          String instanceName) throws IOException {
    
        try (InstancesClient instancesClient = InstancesClient.create()) {
          Instance instance = instancesClient.get(projectId, zone, instanceName);
          boolean deleteProtection = instance.getDeletionProtection();
          System.out.printf("Retrieved Delete Protection setting for instance: %s : %s", instanceName,
              deleteProtection);
    
          return deleteProtection;
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
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('@google-cloud/compute');
    
    // Print the state of delete protection flag of given instance.
    async function getDeleteProtection() {
      const instancesClient = new compute.InstancesClient();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      console.log(
        `Instance ${instanceName} has deletionProtection value: ${instance.deletionProtection}`
      );
    }
    
    getDeleteProtection();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import compute_v1
    
    
    def get_delete_protection(project_id: str, zone: str, instance_name: str) -> bool:
        """
        Returns the state of delete protection flag of given instance.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            instance_name: name of the virtual machine to check.
        Returns:
            The boolean value of the delete protection setting.
        """
        instance_client = compute_v1.InstancesClient()
        instance = instance_client.get(
            project=project_id, zone=zone, instance=instance_name
        )
        return instance.deletion_protection
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
