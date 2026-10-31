---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc/
title: AI Co-Builder: Arc \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:48:05.567887+00:00
---

# AI Co-Builder: Arc  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  AI Co-Builder: Arc Stay organized with collections  Save and categorize content based on your preferences. 

_AI Co-Builder: Arc_ (or just Arc) is a coding agent built directly in CX Agent Studio. It is equipped with all of the skills necessary to build agent applications:

  * Multi-agent architectures
  * Instructions
  * Tool implementations (for instance: OpenAPI tools and Python tools)
  * Callback implementations
  * Guardrails
  * Versions



To use Arc, click the **Arc** icon at the top of the agent builder, then provide your prompt to the agent.

## Uploading files

You can attach files to a message to give Arc more context: a product requirements document, a sample data file, details of external services that need to be called, or an archive of existing configuration.

Arc handles files in three ways, depending on the format:

How it is used | Formats | What happens  
---|---|---  
Read directly | PDF, PNG, JPG, JPEG, WAV, OGG | The file is provided to the model as-is.  
Read as text | TXT, MD, JSON, CSV, HTML, JS, XML, RTF, CSS | The file's text is added to your message. Only the first 262,144 characters are included; ask Arc to read further if the file is longer.  
Unpacked | ZIP | The archive is extracted and its text files become searchable. The archive itself is not sent to the model, and non-text entries inside it are listed but not read. To let Arc read a non-text file that is inside a ZIP archive (a PDF or an image, for example) upload that file directly instead.  
  
The following file limitations apply:

  * Up to 5 files per message
  * Maximum file size of 20 MB
  * Maximum ZIP archive size of 500 MB



## File storage

Uploads go to a Cloud Storage bucket in your own project, under the `agent-assist-uploads/` prefix. The bucket is in the Cloud Storage location that matches the location of your agent application, and all of your agent applications in that location share it:

Agent application location | Bucket name | Bucket location  
---|---|---  
`us` | `PROJECT_ID-agent-assist-artifacts-us` | `US` multi-region  
`eu` | `PROJECT_ID-agent-assist-artifacts-eu` | `EU` multi-region  
  
If the bucket does not exist, the console creates it when you upload a file, as the signed-in user, who needs the `storage.buckets.create` permission; the [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#customer-engagement-suite-service-account) creates it when Arc generates files for a conversation. Uploading a file requires the `storage.objects.create` permission.

Arc creates the bucket with the following settings:

  * A [lifecycle rule](https://docs.cloud.google.com/storage/docs/lifecycle) deletes files automatically 63 days after upload.
  * [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) and [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) are enabled.
  * The labels `goog-drz-ces-app-id` and `goog-drz-ces-app-location` hold the ID and the location of the agent application that caused Arc to create the bucket.



If the bucket already exists in your project, Arc uses it as it is, and its own lifecycle policy applies. Arc does not check or change its location, labels, or default key.

**Caution:** Bucket names are unique across Cloud Storage. If another project owns the name, Arc cannot create the bucket. Arc cannot store files for the agent application until the name is released.

### Organization policy and encryption keys

If you restrict resource locations with the [`constraints/gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) organization policy constraint, the policy must allow the location of the bucket, for example the `in:eu-locations` value group for the `EU` multi-region. Otherwise, Arc cannot create the bucket and uploads fail.

If your project uses [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/cmek), Arc creates the bucket with your key for the location of the agent application as its default key, and it does not create the bucket if it cannot use the key. To let Cloud Storage use the key:

  * Create the key in the key location that matches the bucket location: `us` for the `US` multi-region and `europe` for the `EU` multi-region.
  * Grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the key to the Cloud Storage service agent of your project, `service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`. The following command creates the service agent if it does not exist yet and grants it the role:
        
        gcloud storage service-agent --project=PROJECT_ID --authorize-cmek=KEY_RESOURCE
        

Replace `PROJECT_ID` with your project ID and `KEY_RESOURCE` with the full resource name of the key.




### Create the bucket in advance

You can create the bucket yourself, for example if the people who use Arc don't have the `storage.buckets.create` permission. Use the name and the location from the table earlier in this section, and give the bucket the same settings that Arc would. First, save the following lifecycle rule in a file named `lifecycle-63d.json`:
    
    
    {"rule": [{"action": {"type": "Delete"}, "condition": {"age": 63}}]}
    

Then create the bucket and add the labels and the lifecycle rule:
    
    
    gcloud storage buckets create gs://PROJECT_ID-agent-assist-artifacts-LOCATION \
        --project=PROJECT_ID --location=LOCATION --default-storage-class=STANDARD \
        --uniform-bucket-level-access --public-access-prevention
    gcloud storage buckets update gs://PROJECT_ID-agent-assist-artifacts-LOCATION \
        --update-labels=goog-drz-ces-app-id=APP_ID,goog-drz-ces-app-location=LOCATION \
        --lifecycle-file=lifecycle-63d.json
    

For a project that uses CMEK, first give the service agent access to the key, as described in the previous section. Then add the `--default-encryption-key` flag to the `create` command to make the key the default key of the bucket:
    
    
    gcloud storage buckets create gs://PROJECT_ID-agent-assist-artifacts-LOCATION \
        --project=PROJECT_ID --location=LOCATION --default-storage-class=STANDARD \
        --uniform-bucket-level-access --public-access-prevention \
        --default-encryption-key=KEY_RESOURCE
    

Replace `PROJECT_ID` with your project ID, `LOCATION` with `us` or `eu`, `APP_ID` with the ID of one of your agent applications in that location, and `KEY_RESOURCE` with the full resource name of the key.

### Files uploaded before location-aware storage

Arc started storing files in the location of the agent application in MONTH YEAR. If you set up Arc after that, you can skip this section.

Before Arc stored files in the location of the agent application, it kept every uploaded file in a single bucket, `PROJECT_ID-agent-assist-artifacts`, in the `US` multi-region, for agent applications in every location. The name of that bucket has no location suffix.

To tell which files are which, check the bucket that holds them:

  * Files uploaded before location-aware storage are in the `PROJECT_ID-agent-assist-artifacts` bucket.
  * Files uploaded since then are in the bucket for the location of the agent application, `PROJECT_ID-agent-assist-artifacts-LOCATION`, as listed in the table in File storage. The notice that Arc shows after your first upload names the bucket. Before you send a message, you can hold the pointer over an attached file to see where the file is stored.



Conversations that started before location-aware storage keep saving the files that Arc generates for them in the `PROJECT_ID-agent-assist-artifacts` bucket. Arc does not change the bucket or move its files, so its lifecycle rule still deletes files 75 days after upload, and the bucket empties by itself once those conversations stop using it. Files that you attach go to the bucket for the location of the agent application, whichever conversation you attach them to.

To keep the files that you uploaded to those conversations for longer, copy them to a bucket of your own that does not delete files automatically:
    
    
    gcloud storage cp -r gs://PROJECT_ID-agent-assist-artifacts/agent-assist-uploads \
        gs://ARCHIVE_BUCKET/
    

Replace `ARCHIVE_BUCKET` with a bucket in a location that meets your requirements. The copy is only an archive; those conversations keep reading from the `PROJECT_ID-agent-assist-artifacts` bucket.

Delete the `PROJECT_ID-agent-assist-artifacts` bucket once 60 days have passed since the last of those conversations was used; Arc deletes a conversation 60 days after its last activity. To delete the bucket and the files in it, run the following command:
    
    
    gcloud storage rm -r gs://PROJECT_ID-agent-assist-artifacts
    

## Chain of thought

While processing, Arc provides its chain of thought in sections. You can expand any of these sections to get detail on the agent reasoning.

## Select context

Within the prompt dialog, you can click the **Select context** button, then add select items that Arc should use for additional context in your prompt. For example, you can click this button, followed by a particular agent in the agent builder, then ask Arc to explain the agent to you.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
