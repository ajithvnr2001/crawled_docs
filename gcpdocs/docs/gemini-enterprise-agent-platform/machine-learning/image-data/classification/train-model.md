---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model/
title: Train an image classification model \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:34:19.306253+00:00
---

# Train an image classification model  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/train-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Train an image classification model Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to train an AutoML classification model from an image dataset using either the Google Cloud console or the Agent Platform API.

## Train an AutoML model

###  Google Cloud console 

  1. In the Google Cloud console, in the Agent Platform section, go to the **Datasets** page.

[Go to the Datasets page](https://console.cloud.google.com/agent-platform/datasets)

  2. Click the name of the dataset you want to use to train your model to open its details page.

  3. Click **Train new model**.

  4. For the training method, select radio_button_checked**AutoML**.

  5. Click **Continue**.

  6. Enter a name for the model.

  7. If you want manually set how your training data is split, expand **Advanced options** and select a data split option. For more information, see [About data splits for AutoML models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use). 

  8. Click **Start Training**. 

Model training can take many hours, depending on the size and complexity of your data and your training budget, if you specified one. You can close this tab and return to it later. You will receive an email when your model has completed training.




###  API 

Select the tab below for your objective:

### Classification

Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers). .
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * `fractionSplit`: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * MODELTYPE†: The type of Cloud-hosted model to train. The options are: 
    * `CLOUD` (default)
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Cloud models the budget must be: 8,000 - 800,000 milli node hours (inclusive). The default value is 192,000 which represents one day in wall time, assuming 8 nodes are used. 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "multiLabel": "false",
        "modelType": ["MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "CLOUD",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html);
    import com.google.cloud.aiplatform.v1.[EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html);
    import com.google.cloud.aiplatform.v1.[FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html);
    import com.google.cloud.aiplatform.v1.[FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html);
    import com.google.cloud.aiplatform.v1.[InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).[ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html);
    import com.google.cloud.aiplatform.v1.[PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html);
    import com.google.cloud.aiplatform.v1.[PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html);
    import com.google.cloud.aiplatform.v1.[TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html);
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageClassificationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html);
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageClassificationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html).ModelType;
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    
    public class CreateTrainingPipelineImageClassificationSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String trainingPipelineDisplayName = "YOUR_TRAINING_PIPELINE_DISPLAY_NAME";
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        String modelDisplayName = "YOUR_MODEL_DISPLAY_NAME";
        createTrainingPipelineImageClassificationSample(
            project, trainingPipelineDisplayName, datasetId, modelDisplayName);
      }
    
      static void createTrainingPipelineImageClassificationSample(
          String project, String trainingPipelineDisplayName, String datasetId, String modelDisp[layName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html))
          throws IOException {
        PipelineServiceSet[tings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) pipelineServiceSettings =
            PipelineServiceSettings.newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to s[afely clean up any re](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html)maining background resources.
       [ ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html)try (PipelineServiceClient pipelineServiceClient =
            PipelineServiceClient.create(pipelineServiceSettings)) {
          String location = "us-central1";
          String trainingTaskDefinition =
              "gs://google-cloud-aiplatform/schema/trainingjob/de[finition/&qu](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html)ot;
                [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html)+ "automl_image_classification_1.0.0[.yaml"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html);
          LocationName locationName = LocationName.of(project, loca[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html));
    
          AutoMlImageClassificationInputs autoMlImageClassificationInputs =
              AutoMlImageClassificationInputs.newBuilder()
                  .setModelType(ModelType.CLOUD)
                  .setMultiLabel(false)
                  .setBudgetMilliNod[eHours](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)(8000)
                  .setDisableEarlyStopping([false)
            ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)      .build()[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.Builder.html#com_google_cloud_aiplatform_v1_InputDataConfig_Builder_setDatasetId_java_lang_String_)
    
          InputDataConfig trainingInputD[ataCo](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)nfig =
      [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)   InputDataConfig.newBuilder().setDatasetId(datasetId).build([);](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)
          Model model = Model.newBuilder().setD[isplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)(modelDisplayName).build();
          TrainingPipeline trainingPipeline =
              TrainingPipeli[ne](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskDefinition_java_lang_String_).newBuilder()
                  .setDisplayName(trainingPipelineDis[playName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskInputs_com_google_protobuf_Value_))
                [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).setTrainingT[askDefi](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html#com_google_cloud_aiplatform_util_ValueConverter_toValue_com_google_protobuf_Message_)nition(trainingTaskDefinition)
                  .setT[rainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setInputDataConfig_com_google_cloud_aiplatform_v1_InputDataConfig_)(ValueConverter.toValue(autoMlImageClassif[icationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setModelToUpload_com_google_cloud_aiplatform_v1_Model_)))
                  .setInputDataConfig(train[ingInputDataConf](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)ig)
                  .setModelToUpload(model)
                  .build();
    
          TrainingPipeline trainingPipelineResponse =
              pipelineServiceClient.createTrainingPipeline(locationName, trainingPipeline);
    
          System.out.println("Create Training Pipeline I[mage Cl](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getName__)assification Response");
          System.out.format("Name: %s\n"[, trainingPipe](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getDisplayName__)lineResponse.getName());
          System.out.format("Display Name: %s\n", trainingPipelineRe[sponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskDefinition__).getDisplayName());
    
          System.out.format(
              "Training Task Definition %s\n", trainingPipelin[eResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskInputs__).getTrainingTaskDefinition());
          System.out.format(
              "Training Task Inputs: %s\n", tra[iningPipelineResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskMetadata__).getTrainingTaskInputs());
          System.out.format(
              "Tra[ining Ta](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getState__)sk Metadata: %s\n", trainingPipelineResponse.getTrainingTaskMetadata())[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getCreateTime__)
          System.out.format("State: %s\n", trainingPipelineResponse.getState([));](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getStartTime__)
    
          System.out.format("Create Time: %s\n", trainingPipelineResponse[.getCreate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getEndTime__)Time());
          System.out.format("StartTime %s\n", trainingPipeli[neResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getUpdateTime__).getStartTime());
          System.out.format("End Time: %s\n", tra[iningPipelin](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getLabelsMap__)eResponse.ge[tEndTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)());
          System.out.format("Update Time: %s\[n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getInputDataConfig__), trainingPipelineResponse.getUpdateTime());
          System.out.format("Labels: %s\n", trainingPipelineResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getDatasetId__)());
    
          InputDataConfig inputDataConfig = trainingPipelineResponse.ge[tInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getAnnotationsFilter__)();
          System[.out.println(](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html)"Input Data Config");
     [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFractionSplit__)System.out.format("Dataset Id: %s", inputDataConfig.getDatasetId());
          System.out.format("Annotations Fil[ter: %s\n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTrainingFraction__), inputDataConfig.getAnnotationsFilter());
    
          FractionSplit fractionSpli[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getValidationFraction__) = inputDataConfig.getFractionSplit();
          System.out.println("Fraction Split&q[uot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTestFraction__));
          System.out.for[mat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html)("Training Fraction: %s\n", f[ractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFilterSplit__).getTrainingFraction());
          System.out.format("Validation Fraction: %s\n", fractionSplit.getVali[dationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTrainingFilter__)());
          System.out.format("Test Fraction: %s\n", fractionS[plit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getValidationFilter__).getTestFraction());
    
          FilterSplit filterSplit = inputDataConfig.getFilt[erSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTestFilter__)();
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html).println(&quot;Filter Split");
          System[.out.format("](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getPredefinedSplit__)Training Filter: %s\n", filterSplit.getTrainingFilter());
          System.out.format("Validation[ Filte](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html#com_google_cloud_aiplatform_v1_PredefinedSplit_getKey__)r: %s\n"[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html), filterSplit.getValidationFilter());
          Sys[tem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getTimestampSplit__).out.format(&quot;Test Filter: %s\n", filterSplit.getTestFilter());
    
          PredefinedSplit predefinedSplit = inputDataConfig[.getPredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTrainingFraction__)();
          System.out.println("Predefined Split");
          System.[out.format("Key:](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getValidationFraction__) %s\n", predefinedSplit.getKey());
    
          TimestampSplit times[tampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTestFraction__) = inputDataConfig.getTimestampSplit();
          System.out.printl[n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getKey__)(&quot;Timestamp [Split](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)");
          System.out.format("Tra[ining Fraction: ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getModelToUpload__)%s\n", timestampSplit.getTrainingFraction());
          System.out.format("Validation Fraction:[ %s\n&q](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getName__)uot;, timestampSplit.getValidationFraction());
          System.out.f[ormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDisplayName__)("Test Fraction: %s\n", timestampSplit.getTestFraction());
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDescription__)System.out.format("Key: %s\n", timestampSplit.getKey());
    
          Model model[Response](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadataSchemaUri__) = trainingPipelineResponse.getModelToUpload();
          System.out.println(["Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadata__) To Upload");
          System.out.format("Name: %s\n", mod[elResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getTrainingPipeline__).getName());
          System.out.format("Display Name: %s\n", model[Response](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getArtifactUri__).getDisplayName());
          System.out.format("Description: %s\n", modelResponse.getDescription());
    
          Sy[stem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedDeploymentResourcesTypesList__).out.format("Metadata Schema Uri: %s\n", modelResponse.getMetadataSchemaUri());
          System.out.format("Metadata: %s\n",[ modelResponse.getMetadata());
        ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedInputStorageFormatsList__)  System.out.format("Training Pipeline: %s\n", modelResponse.getTrainingPipeline());
          Syste[m](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedOutputStorageFormatsList__).out.format("Artifact Uri: %s\n", modelResponse.getArtifactUri());
    
          System.out.forma[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getCreateTime__)(
              "Supported Deployment Resources Types: %s\n",
            [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getUpdateTime__)modelResponse.getSupportedDeploymentResourcesTypesList());
          System[.out.format(](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getLabelsMap__)
              &[quot;Supported ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html)Input Storage Formats: %s\n"[,
              modelR](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getPredictSchemata__)esponse.getSupportedInputStorageFormatsList());
          System.out.format(
              "Supported Output Storage Forma[ts: %s\n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getInstanceSchemaUri__),
              modelResponse.getSupportedOutputStorageFormatsList());
    
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getParametersSchemaUri__).format("Create Time: %s\n", modelResponse.getCreateTime());
          System.out.format(&[quot;Update Time: %s\n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getPredictionSchemaUri__)", modelResp[onse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html).getUpdateTime());
          System.out.fo[rmat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedExportFormatsList__)("Labels: %sn\n";, modelResponse.getLabelsMap());
    
          PredictSchemata predictSchemata = modelResponse.getPredictSchemata();
          System.out.println(&[quot;Predict Schem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html)ata");
          System.out.format(["Instance S](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getContainerSpec__)chema Uri: %s\n", predictSchemata.getInstanceSchemaUri());
          System.out.format("Parameters Schem[a Uri: %s\n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getImageUri__)", predictSchemata.getParametersSchemaUri());
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getCommandList__).format(&quot;Prediction Schema Uri: %s\n", predictSchemata.getPredic[tionSchemaU](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getArgsList__)ri());
    
          for (ExportFormat exportFormat : modelResponse.getSupport[edExportFormats](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPredictRoute__)List()) {
            System.out.println("Supported Export Format&quo[t;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getHealthRoute__));
            System.out.format(["](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html)Id: %s\n", exportFormat.[getId());
    ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getEnvList__)      }
    
          ModelContainerSpec modelContainerSpec = modelResponse.getContainerSpec();
          System.out.println("Container Spec");
          System.out.format("Image Ur[i: %](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html)s\n", modelContainerSp[ec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPortsList__).getImageUri());
          System.out.format("Command: %s\n", modelContainerSpec.getCommandList());
          System.out.format("Args: %s\n&q[uot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html), modelContainerSpec.getArgsList());
          Sys[tem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDeployedModelsList__).out.format("Predict Route: %s\n", modelContainerSpec.getPredictRoute());
          System.out.format("Health Route: %s\n", modelContainerSpec.getHealthRoute());
    
          for (EnvVar envVar : modelContainerSpec.getEnvList()) {
            System[.out.p](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html)rintln("Env");
            Sy[stem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getError__).out.format("Name: %s\n", envVar.getName());
            System.out.format("V[alue: %](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getCode__)s\n", envVar.getValue());
          }
    
          for (Po[rt](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getMessage__) port : modelContainerSpec.getPortsList()) {
            System.out.println("Port");
            System.out.format("Container Port: %s\n", port.getContainerPort());
          }
    
          for (DeployedModelRef deployedModelRef : modelResponse.getDeployedModelsList()) {
            System.out.println("Deployed Model");
            System.out.format("Endpoint: %s\n", deployedModelRef.getEndpoint());
            System.out.format("Deployed Model Id: %s\n", deployedModelRef.getDeployedModelId());
          }
    
          Status status = trainingPipelineResponse.getError();
          System.out.println("Error");
          System.out.format("Code: %s\n", status.getCode());
          System.out.format("Message: %s\n", status.getMessage());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * (Not necessary if passing values as arguments)
     */
    /*
    const datasetId = 'YOUR DATASET';
    const modelDisplayName = 'NEW MODEL NAME;
    const trainingPipelineDisplayName = 'NAME FOR TRAINING PIPELINE';
    const project = 'YOUR PROJECT ID';
    const location = 'us-central1';
      */
    // Imports the Google Cloud Pipeline Service Client [library](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)
    const aiplatform = require('@google-cloud/aiplatform');
    
    const {definition} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.trainingjob;
    const ModelType = definition.AutoMlImageClassificationInputs.ModelType;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const {PipelineServiceClient}[ = aiplatform.v1;
    con](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)st pipelineServiceClient = new PipelineServiceClient(clientOptions);
    
    async function createTrainingPipelineImageClassification() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      // Values should match the input expected by your model.
      const trainingTaskInputsMessage =
        new definition.AutoMlImageClassificationInputs({
          multiLabel: true,
          modelType: ModelType.CLOUD,
          budgetMilliNodeHours: 8000,
          disableEarlyStopping: false,
        });
    
      const trainingTaskInputs = trainingTaskInputsMessage.toValue();
    
      const trainingTaskDefinition =
        'gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml';
    
      const modelToUpload = {displayName: modelDisplayName};
      const inputDataConfig = {datasetId};
      const trainingPipeline = {
        displayName: trainingPipelineDisplayName,
        trainingTaskDefinition,
        trainingTaskInputs,
        inputDataConfig,
        modelToUpload,
      };
      const request = {parent, trainingPipeline};
    
      // Create training pipeline request
      const [response] =
        await pipelineServiceClient.createTrainingPipeline(request);
    
      console.log('Create training pipeline image classification response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    
    createTrainingPipelineImageClassification();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def create_training_pipeline_image_classification_sample(
        project: str,
        location: str,
        display_name: str,
        dataset_id: str,
        model_display_name: Optional[str] = None,
        model_type: str = "CLOUD",
        multi_label: bool = False,
        training_fraction_split: float = 0.8,
        validation_fraction_split: float = 0.1,
        test_fraction_split: float = 0.1,
        budget_milli_node_hours: int = 8000,
        disable_early_stopping: bool = False,
        sync: bool = True,
    ):
        aiplatform.init(project=project, location=location)
    
        job = aiplatform.AutoMLImageTrainingJob(
            display_name=display_name,
            model_type=model_type,
            prediction_type="classification",
            multi_label=multi_label,
        )
    
        my_image_ds = aiplatform.ImageDataset(dataset_id)
    
        model = job.run(
            dataset=my_image_ds,
            model_display_name=model_display_name,
            training_fraction_split=training_fraction_split,
            validation_fraction_split=validation_fraction_split,
            test_fraction_split=test_fraction_split,
            budget_milli_node_hours=budget_milli_node_hours,
            disable_early_stopping=disable_early_stopping,
            sync=sync,
        )
    
        model.wait()
    
        print(model.display_name)
        print(model.resource_name)
        print(model.uri)
        return model
    
    

### Classification

Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: .
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * `fractionSplit`: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * MODELTYPE†: The type of Cloud-hosted model to train. The options are: 
    * `CLOUD` (default)
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Cloud models the budget must be: 8,000 - 800,000 milli node hours (inclusive). The default value is 192,000 which represents one day in wall time, assuming 8 nodes are used. 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "multiLabel": "true",
        "modelType": ["MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "CLOUD",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.util.[ValueConverter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html);
    import com.google.cloud.aiplatform.v1.[DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html);
    import com.google.cloud.aiplatform.v1.[EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html);
    import com.google.cloud.aiplatform.v1.[FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html);
    import com.google.cloud.aiplatform.v1.[FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html);
    import com.google.cloud.aiplatform.v1.[InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).[ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html);
    import com.google.cloud.aiplatform.v1.[PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html);
    import com.google.cloud.aiplatform.v1.[PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html);
    import com.google.cloud.aiplatform.v1.[TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html);
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageClassificationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html);
    import com.google.cloud.aiplatform.v1.schema.trainingjob.definition.[AutoMlImageClassificationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html).ModelType;
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    
    public class CreateTrainingPipelineImageClassificationSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String trainingPipelineDisplayName = "YOUR_TRAINING_PIPELINE_DISPLAY_NAME";
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        String modelDisplayName = "YOUR_MODEL_DISPLAY_NAME";
        createTrainingPipelineImageClassificationSample(
            project, trainingPipelineDisplayName, datasetId, modelDisplayName);
      }
    
      static void createTrainingPipelineImageClassificationSample(
          String project, String trainingPipelineDisplayName, String datasetId, String modelDisp[layName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html))
          throws IOException {
        PipelineServiceSet[tings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) pipelineServiceSettings =
            PipelineServiceSettings.newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to s[afely clean up any re](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html)maining background resources.
       [ ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html)try (PipelineServiceClient pipelineServiceClient =
            PipelineServiceClient.create(pipelineServiceSettings)) {
          String location = "us-central1";
          String trainingTaskDefinition =
              "gs://google-cloud-aiplatform/schema/trainingjob/de[finition/&qu](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html)ot;
                [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html)+ "automl_image_classification_1.0.0[.yaml"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html);
          LocationName locationName = LocationName.of(project, loca[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageClassificationInputs.html));
    
          AutoMlImageClassificationInputs autoMlImageClassificationInputs =
              AutoMlImageClassificationInputs.newBuilder()
                  .setModelType(ModelType.CLOUD)
                  .setMultiLabel(false)
                  .setBudgetMilliNod[eHours](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)(8000)
                  .setDisableEarlyStopping([false)
            ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)      .build()[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.Builder.html#com_google_cloud_aiplatform_v1_InputDataConfig_Builder_setDatasetId_java_lang_String_)
    
          InputDataConfig trainingInputD[ataCo](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)nfig =
      [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)   InputDataConfig.newBuilder().setDatasetId(datasetId).build([);](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)
          Model model = Model.newBuilder().setD[isplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)(modelDisplayName).build();
          TrainingPipeline trainingPipeline =
              TrainingPipeli[ne](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskDefinition_java_lang_String_).newBuilder()
                  .setDisplayName(trainingPipelineDis[playName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setTrainingTaskInputs_com_google_protobuf_Value_))
                [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html).setTrainingT[askDefi](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.util.ValueConverter.html#com_google_cloud_aiplatform_util_ValueConverter_toValue_com_google_protobuf_Message_)nition(trainingTaskDefinition)
                  .setT[rainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setInputDataConfig_com_google_cloud_aiplatform_v1_InputDataConfig_)(ValueConverter.toValue(autoMlImageClassif[icationInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.Builder.html#com_google_cloud_aiplatform_v1_TrainingPipeline_Builder_setModelToUpload_com_google_cloud_aiplatform_v1_Model_)))
                  .setInputDataConfig(train[ingInputDataConf](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html)ig)
                  .setModelToUpload(model)
                  .build();
    
          TrainingPipeline trainingPipelineResponse =
              pipelineServiceClient.createTrainingPipeline(locationName, trainingPipeline);
    
          System.out.println("Create Training Pipeline I[mage Cl](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getName__)assification Response");
          System.out.format("Name: %s\n"[, trainingPipe](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getDisplayName__)lineResponse.getName());
          System.out.format("Display Name: %s\n", trainingPipelineRe[sponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskDefinition__).getDisplayName());
    
          System.out.format(
              "Training Task Definition %s\n", trainingPipelin[eResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskInputs__).getTrainingTaskDefinition());
          System.out.format(
              "Training Task Inputs: %s\n", tra[iningPipelineResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskMetadata__).getTrainingTaskInputs());
          System.out.format(
              "Tra[ining Ta](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getState__)sk Metadata: %s\n", trainingPipelineResponse.getTrainingTaskMetadata())[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getCreateTime__)
          System.out.format("State: %s\n", trainingPipelineResponse.getState([));](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getStartTime__)
    
          System.out.format("Create Time: %s\n", trainingPipelineResponse[.getCreate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getEndTime__)Time());
          System.out.format("StartTime %s\n", trainingPipeli[neResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getUpdateTime__).getStartTime());
          System.out.format("End Time: %s\n", tra[iningPipelin](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getLabelsMap__)eResponse.ge[tEndTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html)());
          System.out.format("Update Time: %s\[n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getInputDataConfig__), trainingPipelineResponse.getUpdateTime());
          System.out.format("Labels: %s\n", trainingPipelineResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getDatasetId__)());
    
          InputDataConfig inputDataConfig = trainingPipelineResponse.ge[tInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getAnnotationsFilter__)();
          System[.out.println(](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html)"Input Data Config");
     [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFractionSplit__)System.out.format("Dataset Id: %s", inputDataConfig.getDatasetId());
          System.out.format("Annotations Fil[ter: %s\n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTrainingFraction__), inputDataConfig.getAnnotationsFilter());
    
          FractionSplit fractionSpli[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getValidationFraction__) = inputDataConfig.getFractionSplit();
          System.out.println("Fraction Split&q[uot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTestFraction__));
          System.out.for[mat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html)("Training Fraction: %s\n", f[ractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFilterSplit__).getTrainingFraction());
          System.out.format("Validation Fraction: %s\n", fractionSplit.getVali[dationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTrainingFilter__)());
          System.out.format("Test Fraction: %s\n", fractionS[plit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getValidationFilter__).getTestFraction());
    
          FilterSplit filterSplit = inputDataConfig.getFilt[erSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTestFilter__)();
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html).println(&quot;Filter Split");
          System[.out.format("](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getPredefinedSplit__)Training Filter: %s\n", filterSplit.getTrainingFilter());
          System.out.format("Validation[ Filte](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html#com_google_cloud_aiplatform_v1_PredefinedSplit_getKey__)r: %s\n"[;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html), filterSplit.getValidationFilter());
          Sys[tem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getTimestampSplit__).out.format(&quot;Test Filter: %s\n", filterSplit.getTestFilter());
    
          PredefinedSplit predefinedSplit = inputDataConfig[.getPredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTrainingFraction__)();
          System.out.println("Predefined Split");
          System.[out.format("Key:](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getValidationFraction__) %s\n", predefinedSplit.getKey());
    
          TimestampSplit times[tampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTestFraction__) = inputDataConfig.getTimestampSplit();
          System.out.printl[n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getKey__)(&quot;Timestamp [Split](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html)");
          System.out.format("Tra[ining Fraction: ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getModelToUpload__)%s\n", timestampSplit.getTrainingFraction());
          System.out.format("Validation Fraction:[ %s\n&q](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getName__)uot;, timestampSplit.getValidationFraction());
          System.out.f[ormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDisplayName__)("Test Fraction: %s\n", timestampSplit.getTestFraction());
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDescription__)System.out.format("Key: %s\n", timestampSplit.getKey());
    
          Model model[Response](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadataSchemaUri__) = trainingPipelineResponse.getModelToUpload();
          System.out.println(["Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadata__) To Upload");
          System.out.format("Name: %s\n", mod[elResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getTrainingPipeline__).getName());
          System.out.format("Display Name: %s\n", model[Response](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getArtifactUri__).getDisplayName());
          System.out.format("Description: %s\n", modelResponse.getDescription());
    
          Sy[stem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedDeploymentResourcesTypesList__).out.format("Metadata Schema Uri: %s\n", modelResponse.getMetadataSchemaUri());
          System.out.format("Metadata: %s\n",[ modelResponse.getMetadata());
        ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedInputStorageFormatsList__)  System.out.format("Training Pipeline: %s\n", modelResponse.getTrainingPipeline());
          Syste[m](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedOutputStorageFormatsList__).out.format("Artifact Uri: %s\n", modelResponse.getArtifactUri());
    
          System.out.forma[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getCreateTime__)(
              "Supported Deployment Resources Types: %s\n",
            [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getUpdateTime__)modelResponse.getSupportedDeploymentResourcesTypesList());
          System[.out.format(](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getLabelsMap__)
              &[quot;Supported ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html)Input Storage Formats: %s\n"[,
              modelR](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getPredictSchemata__)esponse.getSupportedInputStorageFormatsList());
          System.out.format(
              "Supported Output Storage Forma[ts: %s\n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getInstanceSchemaUri__),
              modelResponse.getSupportedOutputStorageFormatsList());
    
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getParametersSchemaUri__).format("Create Time: %s\n", modelResponse.getCreateTime());
          System.out.format(&[quot;Update Time: %s\n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getPredictionSchemaUri__)", modelResp[onse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html).getUpdateTime());
          System.out.fo[rmat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedExportFormatsList__)("Labels: %sn\n";, modelResponse.getLabelsMap());
    
          PredictSchemata predictSchemata = modelResponse.getPredictSchemata();
          System.out.println(&[quot;Predict Schem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html)ata");
          System.out.format(["Instance S](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getContainerSpec__)chema Uri: %s\n", predictSchemata.getInstanceSchemaUri());
          System.out.format("Parameters Schem[a Uri: %s\n](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getImageUri__)", predictSchemata.getParametersSchemaUri());
          System.o[ut](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getCommandList__).format(&quot;Prediction Schema Uri: %s\n", predictSchemata.getPredic[tionSchemaU](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getArgsList__)ri());
    
          for (ExportFormat exportFormat : modelResponse.getSupport[edExportFormats](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPredictRoute__)List()) {
            System.out.println("Supported Export Format&quo[t;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getHealthRoute__));
            System.out.format(["](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html)Id: %s\n", exportFormat.[getId());
    ](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getEnvList__)      }
    
          ModelContainerSpec modelContainerSpec = modelResponse.getContainerSpec();
          System.out.println("Container Spec");
          System.out.format("Image Ur[i: %](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html)s\n", modelContainerSp[ec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPortsList__).getImageUri());
          System.out.format("Command: %s\n", modelContainerSpec.getCommandList());
          System.out.format("Args: %s\n&q[uot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html), modelContainerSpec.getArgsList());
          Sys[tem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDeployedModelsList__).out.format("Predict Route: %s\n", modelContainerSpec.getPredictRoute());
          System.out.format("Health Route: %s\n", modelContainerSpec.getHealthRoute());
    
          for (EnvVar envVar : modelContainerSpec.getEnvList()) {
            System[.out.p](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html)rintln("Env");
            Sy[stem](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getError__).out.format("Name: %s\n", envVar.getName());
            System.out.format("V[alue: %](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getCode__)s\n", envVar.getValue());
          }
    
          for (Po[rt](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getMessage__) port : modelContainerSpec.getPortsList()) {
            System.out.println("Port");
            System.out.format("Container Port: %s\n", port.getContainerPort());
          }
    
          for (DeployedModelRef deployedModelRef : modelResponse.getDeployedModelsList()) {
            System.out.println("Deployed Model");
            System.out.format("Endpoint: %s\n", deployedModelRef.getEndpoint());
            System.out.format("Deployed Model Id: %s\n", deployedModelRef.getDeployedModelId());
          }
    
          Status status = trainingPipelineResponse.getError();
          System.out.println("Error");
          System.out.format("Code: %s\n", status.getCode());
          System.out.format("Message: %s\n", status.getMessage());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * (Not necessary if passing values as arguments)
     */
    /*
    const datasetId = 'YOUR DATASET';
    const modelDisplayName = 'NEW MODEL NAME;
    const trainingPipelineDisplayName = 'NAME FOR TRAINING PIPELINE';
    const project = 'YOUR PROJECT ID';
    const location = 'us-central1';
      */
    // Imports the Google Cloud Pipeline Service Client [library](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)
    const aiplatform = require('@google-cloud/aiplatform');
    
    const {definition} =
      aiplatform.protos.google.cloud.aiplatform.v1.schema.trainingjob;
    const ModelType = definition.AutoMlImageClassificationInputs.ModelType;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const {PipelineServiceClient}[ = aiplatform.v1;
    con](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)st pipelineServiceClient = new PipelineServiceClient(clientOptions);
    
    async function createTrainingPipelineImageClassification() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
    
      // Values should match the input expected by your model.
      const trainingTaskInputsMessage =
        new definition.AutoMlImageClassificationInputs({
          multiLabel: true,
          modelType: ModelType.CLOUD,
          budgetMilliNodeHours: 8000,
          disableEarlyStopping: false,
        });
    
      const trainingTaskInputs = trainingTaskInputsMessage.toValue();
    
      const trainingTaskDefinition =
        'gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml';
    
      const modelToUpload = {displayName: modelDisplayName};
      const inputDataConfig = {datasetId};
      const trainingPipeline = {
        displayName: trainingPipelineDisplayName,
        trainingTaskDefinition,
        trainingTaskInputs,
        inputDataConfig,
        modelToUpload,
      };
      const request = {parent, trainingPipeline};
    
      // Create training pipeline request
      const [response] =
        await pipelineServiceClient.createTrainingPipeline(request);
    
      console.log('Create training pipeline image classification response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    
    createTrainingPipelineImageClassification();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def create_training_pipeline_image_classification_sample(
        project: str,
        location: str,
        display_name: str,
        dataset_id: str,
        model_display_name: Optional[str] = None,
        model_type: str = "CLOUD",
        multi_label: bool = False,
        training_fraction_split: float = 0.8,
        validation_fraction_split: float = 0.1,
        test_fraction_split: float = 0.1,
        budget_milli_node_hours: int = 8000,
        disable_early_stopping: bool = False,
        sync: bool = True,
    ):
        aiplatform.init(project=project, location=location)
    
        job = aiplatform.AutoMLImageTrainingJob(
            display_name=display_name,
            model_type=model_type,
            prediction_type="classification",
            multi_label=multi_label,
        )
    
        my_image_ds = aiplatform.ImageDataset(dataset_id)
    
        model = job.run(
            dataset=my_image_ds,
            model_display_name=model_display_name,
            training_fraction_split=training_fraction_split,
            validation_fraction_split=validation_fraction_split,
            test_fraction_split=test_fraction_split,
            budget_milli_node_hours=budget_milli_node_hours,
            disable_early_stopping=disable_early_stopping,
            sync=sync,
        )
    
        model.wait()
    
        print(model.display_name)
        print(model.resource_name)
        print(model.uri)
        return model
    
    

## Control the data split using REST

You can control how your training data is split between the training, validation, and test sets. When using the Agent Platform API, use the [`Split` object](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#InputDataConfig) to determine your data split. The `Split` object can be included in the `InputConfig` object as one of several object types, each of which provides a different way to split the training data. You can select one method only.

  * `FractionSplit`: 
    * TRAINING_FRACTION: The fraction of the training data to be used for the training set. 
    * VALIDATION_FRACTION: The fraction of the training data to be used for the validation set. Not used for video data. 
    * TEST_FRACTION: The fraction of the training data to be used for the test set. 

If any of the fractions are specified, all must be specified. The fractions must add up to 1.0. The [default values for the fractions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#default) differ depending on your data type. [Learn more](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#percentages). 
    
    "fractionSplit": {
      "trainingFraction": TRAINING_FRACTION,
      "validationFraction": VALIDATION_FRACTION,
      "testFraction": TEST_FRACTION
    },
    

  * `FilterSplit`: 
    * TRAINING_FILTER: Data items that match this filter are used for the training set. 
    * VALIDATION_FILTER: Data items that match this filter are used for the validation set. Must be "-" for video data. 
    * TEST_FILTER: Data items that match this filter are used for the test set. 



These filters can be used with the `ml_use` label, or with any labels you apply to your data. Learn more about using [the ml-use label](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#ml-use) and [other labels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/ml-use#filter) to filter your data. 

The following example shows how to use the `filterSplit` object with the `ml_use` label, with the validation set included: 
    
    
    "filterSplit": {
    "trainingFilter": "labels.aiplatform.googleapis.com/ml_use=training",
    "validationFilter": "labels.aiplatform.googleapis.com/ml_use=validation",
    "testFilter": "labels.aiplatform.googleapis.com/ml_use=test"
    }
    

[ Previous arrow_back  Create dataset  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/create-dataset)

[ Next Evaluate model  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/image-data/classification/evaluate-model)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


