---
url: https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates/
title: Dataflow templates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:25:33.982753+00:00
---

# Dataflow templates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow templates Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow templates allow you to package a Dataflow pipeline for deployment. Anyone with the correct permissions can then use the template to deploy the packaged pipeline. You can create your own custom Dataflow templates, and Google provides [pre-built templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) for common scenarios. 

## Benefits

Templates have several advantages over directly deploying a pipeline to Dataflow:

  * Templates separate pipeline design from deployment. For example, a developer can create a template, and a data scientist can deploy the template at a later time.
  * Templates can have parameters that let you customize the pipeline when you deploy the template.
  * You can deploy a template by using the Google Cloud console, the Google Cloud CLI, or REST API calls. You don't need a development environment or any pipeline dependencies installed on your local machine.
  * A template is a code artifact that can be stored in a source control repository and used in continuous integration (CI/CD) pipelines.



## Google-provided templates

Google provides a variety of pre-built, open source Dataflow templates that you can use for common scenarios. For more information about the available templates, see [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).

Starting August 4, 2025, Google-managed template jobs run on [Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime) by default. To run your job on standard Dataflow, you must disable Dataflow Prime. To disable Dataflow Prime for Google-managed template jobs, set the `enable_prime` Dataflow service option to `false` (`enable_prime=false`) when you run the template. For more details, see [Disable Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#disable-prime).

## Compare Flex templates and classic templates

Dataflow supports two types of templates: Flex templates, which are newer, and classic templates. If you are creating a new Dataflow template, we recommend creating it as a Flex template.

With a Flex template, the pipeline is packaged as a Docker image in Artifact Registry, along with a template specification file in Cloud Storage. The template specification contains a pointer to the Docker image. When you run the template, the Dataflow service starts a launcher VM, pulls the Docker image, and runs the pipeline. The execution graph is dynamically built based on runtime parameters provided by the user. To use the API to launch a job that uses a Flex template, use the [`projects.locations.flexTemplates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch) method. 

A classic template contains the JSON serialization of a Dataflow job graph. The code for the pipeline must wrap any runtime parameters in the `ValueProvider` interface. This interface allows users to specify parameter values when they deploy the template. To use the API to work with classic templates, see the [`projects.locations.templates`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.templates) API reference documentation.

Flex templates have the following advantages over classic templates:

  * Unlike classic templates, Flex templates don't require the `ValueProvider` interface for input parameters. Not all Dataflow sources and sinks support `ValueProvider`.
  * While classic templates have a static job graph, Flex templates can dynamically construct the job graph. For example, the template might select a different I/O connector based on input parameters.
  * A Flex template can perform preprocessing on a virtual machine (VM) during pipeline construction. For example, it might validate input parameter values.



## Template workflow

Using Dataflow templates involves the following high-level steps: 

  1. Developers set up a development environment and develop their pipeline. The environment includes the Apache Beam SDK and other dependencies.
  2. Depending on the template type (Flex or classic): 
     * For Flex templates, the developers package the pipeline into a Docker image, push the image to Artifact Registry, and upload a template specification file to Cloud Storage.
     * For classic templates, developers run the pipeline, create a template file, and stage the template to Cloud Storage.
  3. Other users submit a request to the Dataflow service to run the template. 
  4. Dataflow creates a pipeline from the template. The pipeline can take as much as five to seven minutes to start running. 



## Inspect and audit template jobs

When you audit running or historical Dataflow template jobs programmatically by using the REST API or the Google Cloud CLI, the default view is a summary view (`JOB_VIEW_SUMMARY`). The summary view omits pipeline execution details, template metadata, and SDK pipeline options. To retrieve template details and environment options, you must explicitly request the full job view.

To inspect template details for a job, use one of the following methods:

### gcloud CLI

To retrieve the full job description including template details, run the [`gcloud dataflow jobs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/describe) command with the `--full` flag:

Before using any of the command data below, make the following replacements: 

  * REGION: the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where the job is running.
  * JOB_ID: the ID of the Dataflow job.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataflow jobs describe JOB_ID --full --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataflow jobs describe JOB_ID --full --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud dataflow jobs describe JOB_ID --full --region=REGION

You should receive a response similar to the following:
    
    
    environment:
      sdkPipelineOptions:
        options:
          templateLocation: gs://BUCKET_NAME/templates/TEMPLATE_NAME
    id: JOB_ID
    name: JOB_NAME
    type: JOB_TYPE_BATCH
    

### REST

To retrieve the full job resource including template details, send an HTTP `GET` request to the [`projects.locations.jobs.get`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/get) method with the `view=JOB_VIEW_ALL` query parameter:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * REGION: the Dataflow [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where the job is running.
  * JOB_ID: the ID of the Dataflow job.



HTTP method and URL: 
    
    
    GET https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/jobs/JOB_ID?view=JOB_VIEW_ALL

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/jobs/JOB_ID?view=JOB_VIEW_ALL"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/jobs/JOB_ID?view=JOB_VIEW_ALL" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "id": "JOB_ID",
      "name": "JOB_NAME",
      "type": "JOB_TYPE_BATCH",
      "environment": {
        "sdkPipelineOptions": {
          "options": {
            "templateLocation": "gs://BUCKET_NAME/templates/TEMPLATE_NAME"
          }
        }
      }
    }
    

### Identify template types

The response payload differs depending on whether the job was created from a Google-provided template or a custom template:

  * **Google-provided templates** : Dataflow automatically attaches predefined labels to the job resource: 
    * `goog-dataflow-provided-template-name`: the name of the template.
    * `goog-dataflow-provided-template-type`: the template type, either `flex` or `legacy` (classic).
    * `goog-dataflow-provided-template-version`: the release version of the template.
  * **Custom templates** : Custom template jobs don't have the `goog-dataflow-provided-*` labels. Both Flex and classic template jobs populate the `templateLocation` option in `environment.sdkPipelineOptions`. To determine the template type for custom jobs when labels are absent, inspect the following fields in the full job response (`JOB_VIEW_ALL`): 
    * **Classic templates** : The `templateLocation` field points directly to the staged template JSON file in Cloud Storage. For example, the path resembles `gs://BUCKET_NAME/templates/TEMPLATE_NAME`. Classic template jobs don't have container launcher image configurations.
    * **Flex templates** : Flex template jobs execute from a launcher container image. Under the `environment` object, Flex template jobs contain launcher container specifications and parameters (such as `flexResourceLimits`). In addition, the staged `templateLocation` Cloud Storage path generated during launch contains the job ID.



### Best practice: attach user labels during launch

Because distinguishing custom template types programmatically requires retrieving and parsing the full `JOB_VIEW_ALL` environment options, we recommend that you attach descriptive user labels when launching your template jobs. For example, attach labels such as `template-type: flex` or `template-type: classic`.

User labels are returned in the default summary view (`JOB_VIEW_SUMMARY`) and in job list operations. User labels let you filter, search, and audit template jobs efficiently across your project without fetching the full execution payload for every job.

To attach labels when launching a template, use the following methods:

  * For Flex templates in the gcloud CLI, use the `--additional-user-labels` flag in the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
  * For classic templates in the gcloud CLI, use the `--labels` flag in the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command.
  * When using the REST API, include the `labels` key-value map in the request body of the launch request.



## Set IAM permissions

Dataflow jobs, including jobs run from templates, use two IAM service accounts:

  * The Dataflow service uses a [Dataflow service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account) to manipulate Google Cloud resources, such as creating VMs.
  * The Dataflow worker VMs use a [worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#worker-service-account) to access your pipeline's files and other resources. This service account needs access to any resources that the pipeline job references, including the source and sink that the template uses. For more information, see [Access Google Cloud resources](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#access-resources).



Ensure that these two service accounts have appropriate roles. For more information, see [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

If your organization uses [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), principals (such as users or service accounts) might be blocked from viewing and running Google-provided templates. For more information and solutions, see [Access Google-provided templates with principal access boundary policies](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#access-templates-pab).

## Apache Beam SDK version requirements

To create your own templates, make sure your Apache Beam SDK version supports template creation.

### Java

To create templates with the Apache Beam SDK 2.x for Java, you must have version 2.0.0-beta3 or higher.

### Python

To create templates with the Apache Beam SDK 2.x for Python, you must have version 2.0.0 or higher.

To run templates with Google Cloud CLI, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads) version 138.0.0 or higher.

## Extend templates

You can build your own templates by extending the [open source](https://github.com/GoogleCloudPlatform/DataflowTemplates) Dataflow templates. For example, for a template that uses a fixed window duration, data that arrives outside of the window might be discarded. To avoid this behavior, use the template code as a base, and modify the code to invoke the [`.withAllowedLateness`](https://beam.apache.org/documentation/programming-guide/#managing-late-data) operation. 

## What's next

  * [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates)
  * [Use Flex Templates to package a pipeline](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates)
  * [Build and run an example Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates)
  * [Create classic templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates)
  * [Run classic templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/running-templates)
  * [Troubleshoot Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
