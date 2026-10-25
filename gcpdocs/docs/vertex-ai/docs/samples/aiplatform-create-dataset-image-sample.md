---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-dataset-image-sample/
title: Create a dataset for image \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-25T05:44:07.833642+00:00
---

# Create a dataset for image  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-dataset-image-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a dataset for image Stay organized with collections  Save and categorize content based on your preferences. 

Creates a dataset for image using the create_dataset method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a dataset for training image classification models](https://docs.cloud.google.com/vertex-ai/docs/image-data/classification/create-dataset)
  * [Create a dataset for training image object detection models](https://docs.cloud.google.com/vertex-ai/docs/image-data/object-detection/create-dataset)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.cloud.aiplatform.v1.CreateDatasetOperationMetadata;
    import com.google.cloud.aiplatform.v1.Dataset;
    import com.google.cloud.aiplatform.v1.DatasetServiceClient;
    import com.google.cloud.aiplatform.v1.DatasetServiceSettings;
    import com.google.cloud.aiplatform.v1.LocationName;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDatasetImageSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String datasetDisplayName = "YOUR_DATASET_DISPLAY_NAME";
        createDatasetImageSample(project, datasetDisplayName);
      }
    
      static void createDatasetImageSample(String project, String datasetDisplayName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        DatasetServiceSettings datasetServiceSettings =
            DatasetServiceSettings.newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (DatasetServiceClient datasetServiceClient =
            DatasetServiceClient.create(datasetServiceSettings)) {
          String location = "us-central1";
          String metadataSchemaUri =
              "gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml";
          LocationName locationName = LocationName.of(project, location);
          Dataset dataset =
              Dataset.newBuilder()
                  .setDisplayName(datasetDisplayName)
                  .setMetadataSchemaUri(metadataSchemaUri)
                  .build();
    
          OperationFuture<Dataset, CreateDatasetOperationMetadata> datasetFuture =
              datasetServiceClient.createDatasetAsync(locationName, dataset);
          System.out.format("Operation name: %s\n", datasetFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          Dataset datasetResponse = datasetFuture.get(120, TimeUnit.SECONDS);
    
          System.out.println("Create Image Dataset Response");
          System.out.format("Name: %s\n", datasetResponse.getName());
          System.out.format("Display Name: %s\n", datasetResponse.getDisplayName());
          System.out.format("Metadata Schema Uri: %s\n", datasetResponse.getMetadataSchemaUri());
          System.out.format("Metadata: %s\n", datasetResponse.getMetadata());
          System.out.format("Create Time: %s\n", datasetResponse.getCreateTime());
          System.out.format("Update Time: %s\n", datasetResponse.getUpdateTime());
          System.out.format("Labels: %s\n", datasetResponse.getLabelsMap());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const datasetDisplayName = "YOUR_DATASTE_DISPLAY_NAME";
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Dataset Service Client library
    const {DatasetServiceClient} = require('@google-cloud/aiplatform');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const datasetServiceClient = new DatasetServiceClient(clientOptions);
    
    async function createDatasetImage() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
      // Configure the dataset resource
      const dataset = {
        displayName: datasetDisplayName,
        metadataSchemaUri:
          'gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml',
      };
      const request = {
        parent,
        dataset,
      };
    
      // Create Dataset Request
      const [response] = await datasetServiceClient.createDataset(request);
      console.log(`Long running operation: ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      const result = response.result;
    
      console.log('Create dataset image response');
      console.log(`Name : ${result.name}`);
      console.log(`Display name : ${result.displayName}`);
      console.log(`Metadata schema uri : ${result.metadataSchemaUri}`);
      console.log(`Metadata : ${JSON.stringify(result.metadata)}`);
      console.log(`Labels : ${JSON.stringify(result.labels)}`);
    }
    createDatasetImage();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def create_dataset_image_sample(
        project: str,
        display_name: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 300,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.DatasetServiceClient(client_options=client_options)
        dataset = {
            "display_name": display_name,
            "metadata_schema_uri": "gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml",
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.create_dataset(parent=parent, dataset=dataset)
        print("Long running operation:", response.operation.name)
        create_dataset_response = response.result(timeout=timeout)
        print("create_dataset_response:", create_dataset_response)
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_vertex_ai_dataset" "image_dataset" {
      display_name        = "image-dataset"
      metadata_schema_uri = "gs://google-cloud-aiplatform/schema/dataset/metadata/image_1.0.0.yaml"
      region              = "us-central1"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
