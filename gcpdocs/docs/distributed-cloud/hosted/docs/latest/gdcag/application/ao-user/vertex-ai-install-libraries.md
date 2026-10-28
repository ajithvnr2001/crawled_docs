---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries/
title: Install Vertex AI client libraries \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T08:22:11.122094+00:00
---

# Install Vertex AI client libraries  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install Vertex AI client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through installing Vertex AI client libraries for Google Distributed Cloud (GDC) air-gapped, which let you interact with various Vertex AI services from your application and development environment. You can learn about the types of client libraries available for Vertex AI APIs and the steps for installing them from the tar file. 

This page is for application developers within application operator groups responsible for setting up their application and development environments to enable AI features. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Each Vertex AI service provides an API. While you can interact directly with these APIs through raw server requests, client libraries simplify programmatic access from supported languages on Distributed Cloud. They reduce the necessary code required, especially when working in environments like a JupyterLab notebook.

You can install a Vertex AI client library using these methods:

  * Extract the library file directly from the tar file.
  * Use a JupyterLab notebook to import the library.
  * Import a client library from a notebook. For information, see [Manage notebooks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench).



## Vertex AI client libraries

Vertex AI offers different versions of client libraries for CentOS and Ubuntu operating systems.

The naming conventions of Vertex AI client libraries in the tar file are based on the operating system, the service name, and the version. The filenames adhere to the following format:
    
    
    OS-google-cloud-SERVICE-VERSION.tar.gz
    

Replace the following:

  * `OS`: the name of the operating system where you want to install the client library. Allowed values are `centos` and `ubuntu`.
  * `SERVICE`: the name of the Vertex AI service from which you want to download the client library. The following are the allowed values:

    * `aiplatform`: the Vertex AI Platform client library.
    * `speech`: the Speech-to-Text client library.
    * `translate`: the Vertex AI Translation client library.
    * `vision`: the OCR client library.
  * `VERSION`: the version number of the client library, such as `3.8.0`.




The following table contains the Vertex AI client libraries that Distributed Cloud supports:

Vertex AI service | Operating system | Filename  
---|---|---  
OCR | Centos | `centos-google-cloud-vision-3.0.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-vision-3.0.0.tar.gz`  
Speech-to-Text | Centos | `centos-google-cloud-speech-2.15.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-speech-2.15.0.tar.gz`  
Vertex AI Translation | Centos | `centos-google-cloud-translate-3.8.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-translate-3.8.0.tar.gz`  
Vertex AI Platform | Centos | `centos-google-cloud-aiplatform-1.34.0.tar.gz`  
Ubuntu | `ubuntu-google-cloud-aiplatform-1.34.0.tar.gz`  
**Important:** You must install the Vertex AI Platform client library to use Generative AI models like Text Embedding and Text Embedding Multilingual.

## Before you begin

Before downloading the tar file and extracting client libraries, follow these steps:

  1. [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).

  2. Authenticate with gdcloud CLI:
         
         gdcloud auth login
         

For more information about how to authenticate with your configured identity provider, see [the gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth).

  3. Verify that you have installed Python 3.7 to 3.10. The client library tarballs contain wheels for `cp37` to `cp310`.




## Install a client library

After completing the prerequisites, follow these steps to download the tar file, and use the tar file to install a client library:

  1. Download the client library you want to install:
         
         wget https://GDC_URL/.well-known/static/client-libraries/CLIENT_LIBRARY
         

Replace the following:

     * `GDC_URL`: the URL of GDC Console for your organization.
     * `CLIENT_LIBRARY`: the filename of the client library you want to download.
  2. Extract the library file:
         
         tar -zxf CLIENT_LIBRARY
         

Extracting `OS-google-cloud-SERVICE-VERSION.tar.gz` (for example, `centos-google-cloud-speech-2.15.0.tar.gz`) creates the `LIBRARY_NAME` directory (for example, `google-cloud-speech`, without the `OS-` prefix or `-VERSION` suffix).

  3. Install the client library in Distributed Cloud:
         
         pip install -r LIBRARY_NAME/requirements.txt --no-index --find-links LIBRARY_NAME
         

Replace `LIBRARY_NAME` with the extracted library directory name, such as `google-cloud-speech`.

  4. If you installed the Speech-to-Text client library, verify the installation and version (`2.15.0`):

**Note:** Speech-to-Text API calls on Distributed Cloud must import `from google.cloud import speech_v1p1beta1 as speech` because the API gateway routes the `google.cloud.speech.v1p1beta1.Speech` service. Importing `from google.cloud import speech` defaults to `speech_v1`, and API calls with `speech_v1` return `501 MethodNotImplemented`.
         
         from google.cloud import speech_v1p1beta1 as speech
         
         print(speech.__version__)
         

The output displays the installed version:
         
         2.15.0
         

  5. Import the client library using a Python script. The following example shows a code snippet of a Python script that imports the Vertex AI Translation client library to illustrate what importing libraries looks like:
         
         from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
         from google.api_core.client_options import ClientOptions
         import google.auth
         from google.auth.transport import requests
         
         creds, _ = google.auth.default()
         creds = creds.with_gdch_audience("https://ENDPOINT:443")
         creds.refresh(requests.Request())
         client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)(
             credentials=creds, client_options=ClientOptions(api_endpoint="ENDPOINT:443"))
         response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text)(request={
             "parent": "projects/PROJECT_ID", "target_language_code": "ru",
             "mime_type": "text/plain", "contents": ["Hello"]})
         print(response.translations[0].translated_text)
         

Replace the following:

     * `ENDPOINT`: the Vertex AI Translation endpoint that you use for your organization, without the `https://` prefix or `:443` port. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT_ID`: your project ID.

For more information about making Vertex AI Translation requests, [learn about translation features](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation) or [translate text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation).

**Note:** The `google-cloud-translate` 3.8.0 client library doesn't expose the `s3_source` field, so it can't create glossaries or translate documents from storage buckets. Instead, use the REST API to [create a glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-glossary#create-glossary) or [translate documents from a bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translate-docs#translate-bucket).
  6. Save the Python script with a name, such as `translation-service.py`.

  7. Run the Python script:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `translation-service.py`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
