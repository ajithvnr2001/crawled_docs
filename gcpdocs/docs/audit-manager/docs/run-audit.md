---
url: https://docs.cloud.google.com/audit-manager/docs/run-audit/
title: Schedule or run an audit \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:18:21.050647+00:00
---

# Schedule or run an audit  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/run-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Schedule or run an audit Stay organized with collections  Save and categorize content based on your preferences. 

Audits let you collect the evidence that you require to assess your Google Cloud organization against [supported frameworks](https://docs.cloud.google.com/audit-manager/docs/overview#supported_compliance). You can schedule an audit to run at a regular interval or run an on-demand audit.

An audit is a long-running operation that might take a few hours. The duration depends on the number of resources within the audit scope, which is the organization, project, or folder that you previously enrolled.

You can create a schedule for a specific framework and resource combination only if an active or paused schedule doesn't already exist for that combination.

## Before you begin

  * To get the permissions that you need to run or schedule an audit, ask your administrator to grant you one of the following Identity and Access Management (IAM) roles:

    * [Audit Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.admin) (`roles/auditmanager.admin`)
    * [Audit Manager Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.auditor) (`roles/auditmanager.auditor`)
  * [Enroll your organization, project, or folder](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) for auditing.




## Schedule and run an audit

You can create a schedule to run an audit on a recurring basis or run an on-demand audit.

### Console

  1. In the Google Cloud console, go to the **Run assessment** page in Audit Manager.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager/auditreports/create)

  2. In the **Choose resource and region** section, do the following:

     1. Select the organization, folder, or project that you want to audit.

     2. Select the location where you want to process the audit assessment. For the list of supported locations, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations).

     3. Click **Next**.

  3. In the **Choose regulation** section, select the framework that you want to audit your resource against and then click **Next**. For information about supported frameworks, see [Supported frameworks](https://docs.cloud.google.com/audit-manager/docs/overview#supported_compliance).

  4. Optional: If the **Configure Parameters** section appears, complete the following:

     1. Click **Modify Configuration**.

     2. In the **Configure parameters** window, add the required parameters for the cloud controls. For more information about the parameters, see [Compliance Manager cloud control reference](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls) and [Assured Workloads cloud controls](https://docs.cloud.google.com/assured-workloads/docs/cloud-control-reference).

     3. Click **Save**.

  5. Optional: In the **View Assessment Plan** section, you can download an ODS file that contains information about the audit scope based on the framework that you selected. To download the file, click the link, and click **Next**.

  6. In the **Choose storage bucket** section, select the storage bucket where you want to save the audit report and evidence, and then click **Done**. If your bucket isn't listed, ask your administrator to [enroll your resource](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) with your storage bucket.

  7. Optional: In the **Schedule** section, set any of the following:

     * How often to repeat the audit (daily, weekly, monthly, quarterly, or annually).

     * The time period to include in the audit. If you choose **Never ending** , the audit continues to run from the start date that you specify until you manually stop it.

  8. To start the audit, click **Run Audit** or **Run Scheduled Audit**.

You can view the status of an on-demand audit on the **View assessments** page or view your scheduled audits on the **Schedules** tab of the **Audit management** page.




### gcloud

#### Optional: Generate an audit assessment

Before you run an audit, you can generate an audit assessment, or scope, that includes a detailed task breakdown for the audit based on the framework that you choose.

The [ `gcloud audit-manager audit-scopes generate`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-scopes/generate) command generates an audit scope.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organization`, `folder`, and `project`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.
  * OUTPUT_DIRECTORY: the directory where the output must be stored. For example: `reports`.
  * OUTPUT_FILENAME: the name of the output file. Don't include the file extension in the filename. For example: `scopeReport`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION \
        --compliance-framework=FRAMEWORK \
        --report-format=AUDIT_REPORT_FORMAT \
        --output-directory=OUTPUT_DIRECTORY \
        --output-file-name=OUTPUT_FILENAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION `
        --compliance-framework=FRAMEWORK `
        --report-format=AUDIT_REPORT_FORMAT `
        --output-directory=OUTPUT_DIRECTORY `
        --output-file-name=OUTPUT_FILENAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION ^
        --compliance-framework=FRAMEWORK ^
        --report-format=AUDIT_REPORT_FORMAT ^
        --output-directory=OUTPUT_DIRECTORY ^
        --output-file-name=OUTPUT_FILENAME

#### Run an on-demand audit

The [ `gcloud audit-manager audit-reports generate`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-reports/generate) command runs an audit.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organization`, `folder`, and `project`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION \
        --compliance-framework=FRAMEWORK \
        --report-format=AUDIT_REPORT_FORMAT \
        --gcs-uri=BUCKET_URI

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION `
        --compliance-framework=FRAMEWORK `
        --report-format=AUDIT_REPORT_FORMAT `
        --gcs-uri=BUCKET_URI

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION ^
        --compliance-framework=FRAMEWORK ^
        --report-format=AUDIT_REPORT_FORMAT ^
        --gcs-uri=BUCKET_URI

You should receive a response similar to the following:
    
    
    done: false
    name: projects/10398413/locations/987234/operations/operation-1726842525305-6228ddb4dca96-78a6db59-f9dd9a24
    
    

#### Schedule an audit

The [ `gcloud audit-manager audit-schedules create`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-schedules/create) command creates an audit schedule.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organization`, `folder`, and `project`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only OpenDocument Format (ODF) is supported: `odf`. 
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * FREQUENCY: the frequency of scheduled audit runs. Valid values are `daily`, `weekly`, `monthly`, `quarterly`, and `annually`. For example: `weekly`. 
  * SCHEDULE_START_TIME: the date and time when the first audit run starts, in RFC 3339 format. For example: `2026-10-25T10:00:00Z`. 
  * DISPLAY_NAME: optional. A display name for the audit schedule. For example: `NIST 800-53 Weekly Audit`. 
  * SCHEDULE_END_TIME: optional. The date and time when the audit schedule stops, in RFC 3339 format. For example: `2027-10-25T10:00:00Z`. 
  * TIME_ZONE: optional. The time zone for the audit schedule in IANA format. Audit Manager uses this value to interpret the start time and end time. If not specified, the default is `UTC`. For example: `America/New_York`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules create \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION \
        --audit-schedule-id=AUDIT_SCHEDULE_ID \
        --compliance-framework=FRAMEWORK \
        --report-format=AUDIT_REPORT_FORMAT \
        --gcs-uri=BUCKET_URI \
        --start-time=SCHEDULE_START_TIME \
        --frequency=FREQUENCY \
        --display-name="DISPLAY_NAME" \
        --end-time=SCHEDULE_END_TIME \
        --time-zone=TIME_ZONE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules create `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION `
        --audit-schedule-id=AUDIT_SCHEDULE_ID `
        --compliance-framework=FRAMEWORK `
        --report-format=AUDIT_REPORT_FORMAT `
        --gcs-uri=BUCKET_URI `
        --start-time=SCHEDULE_START_TIME `
        --frequency=FREQUENCY `
        --display-name="DISPLAY_NAME" `
        --end-time=SCHEDULE_END_TIME `
        --time-zone=TIME_ZONE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules create ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION ^
        --audit-schedule-id=AUDIT_SCHEDULE_ID ^
        --compliance-framework=FRAMEWORK ^
        --report-format=AUDIT_REPORT_FORMAT ^
        --gcs-uri=BUCKET_URI ^
        --start-time=SCHEDULE_START_TIME ^
        --frequency=FREQUENCY ^
        --display-name="DISPLAY_NAME" ^
        --end-time=SCHEDULE_END_TIME ^
        --time-zone=TIME_ZONE

You should receive a response similar to the following:
    
    
    complianceFramework: builtin-cis-v8
    gcsUri: gs://my-bucket
    name: projects/834/locations/us-central1/auditSchedules/my-schedule-id
    reportFormat: AUDIT_REPORT_FORMAT_ODF
    scheduleConfig:
      frequency: weekly
      startTime: '2026-10-25T10:00:00Z'
    state: SCHEDULE_STATE_ACTIVE
    

### REST

#### Optional: Generate an audit assessment

Before you run an audit, you can generate an audit assessment, or scope, that includes a detailed task breakdown for the audit based on the framework that you choose.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate

Request JSON body: 
    
    
    
    {
      "compliance_framework" : "FRAMEWORK",
      "report_format" : "AUDIT_REPORT_FORMAT"
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate"

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
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    
      "scope_report_contents": "980u43nrf090834uhbkfehf......",
      "name" : "folders/8767234/locations/us-west"
    }
    
    

The response includes the following information:

  * `scope_report_contents`: the byte format of the report contents, which you must convert to OpenDocument Format (ODF) before review.
  * `name`: a unique string identifier of the applicable resource.



#### Run an on-demand audit

To run an on-demand audit, send a `POST` request to the `auditReport:generate` endpoint.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate

Request JSON body: 
    
    
    
    {
      "destination" : {
        "gcs_uri" : "BUCKET_URI"
      },
      "compliance_framework" : "FRAMEWORK",
      "report_format" : "AUDIT_REPORT_FORMAT"
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate"

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
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/834/projects/10398413/locations/987234/operations/098234",
      "done": false
    }
    
    

The response includes the following information:

  * `name`: a unique string identifier for the audit assessment operation request. Use this identifier to track the progress of the audit assessment. For example: `projects/PROJECT_ID/locations/LOCATION/operations/098234UNIQUE_ID`.
  * `done`: a boolean flag that indicates whether the audit assessment is complete. This flag is set to `false` when the process starts and changes to `true` when the audit assessment completes.



#### Schedule an audit

To schedule a recurring audit, send a `POST` request to the `auditSchedules` endpoint.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in the Google Cloud console. 
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.
  * FREQUENCY: the frequency of scheduled audit runs. Valid values are `DAILY`, `WEEKLY`, `MONTHLY`, `QUARTERLY`, and `ANNUALLY`. For example: `WEEKLY`. 
  * SCHEDULE_START_TIME: the date and time when the first audit run starts, in RFC 3339 format. For example: `2026-10-25T10:00:00Z`. 
  * DISPLAY_NAME: optional. A display name for the audit schedule. For example: `NIST 800-53 Weekly Audit`. 
  * SCHEDULE_END_TIME: optional. The date and time when the audit schedule stops, in RFC 3339 format. For example: `2027-10-25T10:00:00Z`. 
  * TIME_ZONE: optional. The time zone for the audit schedule in IANA format. Audit Manager uses this value to interpret the start time and end time. If not specified, the default is `UTC`. For example: `America/New_York`. 



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules?auditScheduleId=AUDIT_SCHEDULE_ID

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "gcsUri": "BUCKET_URI",
      "complianceFramework": "FRAMEWORK",
      "reportFormat": "AUDIT_REPORT_FORMAT",
      "scheduleConfig": {
        "startTime": "SCHEDULE_START_TIME",
        "endTime": "SCHEDULE_END_TIME",
        "frequency": "FREQUENCY",
        "timeZone": "TIME_ZONE"
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
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules?auditScheduleId=AUDIT_SCHEDULE_ID"

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
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules?auditScheduleId=AUDIT_SCHEDULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/834/locations/us-central1/auditSchedules/my-schedule-id",
      "displayName": "My first audit schedule",
      "gcsUri": "gs://my-bucket",
      "complianceFramework": "builtin-cis-v8",
      "reportFormat": "AUDIT_REPORT_FORMAT_ODF",
      "scheduleConfig": {
        "startTime": "2026-10-25T10:00:00Z",
        "endTime": "2027-10-25T10:00:00Z",
        "frequency": "WEEKLY",
        "timeZone": "America/New_York"
      },
      "state": "SCHEDULE_STATE_ACTIVE",
      "createTime": "2026-10-25T13:27:00Z",
      "updateTime": "2026-10-25T13:27:00Z"
    }
    

## View scheduled audits

You can view details about your scheduled audits, including the scope, framework, and schedule configuration.

### Console

  1. In the Google Cloud console, go to the **Audit management** page in Audit Manager.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager/manageaudits)

  2. In the **Schedules** tab, view the list of scheduled audits.




### gcloud

#### View a list of scheduled audits

To view a list of scheduled audits, run the [ `gcloud audit-manager audit-schedules list`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-schedules/list) command.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organization`, `folder`, and `project`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules list \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules list `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules list ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION

You should receive a response similar to the following:
    
    
    ┌────────────┬────────────┬──────────────┬────────────┬────────────┬───────────────┬─────────────────┬─────────────┬─────────────┬───────────────┬───────────────────┬───────────────┐
    │     ID     │ FRAMEWORK  │ DISPLAY_NAME │   STATE    │  GCS_URI   │ REPORT_FORMAT │ SCHEDULE_CONFIG │ CREATE_TIME │ UPDATE_TIME │ NEXT_RUN_TIME │ LAST_TRIGGER_TIME │ ERROR_MESSAGE │
    ├────────────┼────────────┼──────────────┼────────────┼────────────┼───────────────┼─────────────────┼─────────────┼─────────────┼───────────────┼───────────────────┼───────────────┤
    │ my-schedul │ builtin-ci │ My first aud │ SCHEDULE_S │ gs://my-bu │ AUDIT_REPORT_ │ {'frequency':   │ 2026-10-25T │ 2026-10-25T │               │                   │               │
    │ e-id       │ s-v8       │ it schedule  │ TATE_ACTIV │ cket       │ FORMAT_ODF    │ 'weekly',       │ 13:27:00Z   │ 13:27:00Z   │               │                   │               │
    │            │            │              │ E          │            │               │ 'startTime':    │             │             │               │                   │               │
    │            │            │              │            │            │               │ '2026-10-25T10: │             │             │               │                   │               │
    │            │            │              │            │            │               │ 00:00Z'}        │             │             │               │                   │               │
    └────────────┴────────────┴──────────────┴────────────┴────────────┴───────────────┴─────────────────┴─────────────┴─────────────┴───────────────┴───────────────────┴───────────────┘
    

#### View details about a scheduled audit

To view details about a specific scheduled audit, run the [ `gcloud audit-manager audit-schedules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-schedules/describe) command.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules describe \
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules describe `
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules describe ^
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID

You should receive a response similar to the following:
    
    
    complianceFramework: builtin-cis-v8
    gcsUri: gs://my-bucket
    name: projects/834/locations/us-central1/auditSchedules/my-schedule-id
    reportFormat: AUDIT_REPORT_FORMAT_ODF
    scheduleConfig:
      frequency: weekly
      startTime: '2026-10-25T10:00:00Z'
    state: SCHEDULE_STATE_ACTIVE
    

### REST

#### View a list of scheduled audits

To view a list of scheduled audits, send a `GET` request to the `auditSchedules` endpoint.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 



HTTP method and URL: 
    
    
    GET https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "auditSchedules": [
        {
          "name": "projects/834/locations/us-central1/auditSchedules/my-schedule-id",
          "displayName": "My first audit schedule",
          "gcsUri": "gs://my-bucket",
          "complianceFramework": "builtin-cis-v8",
          "reportFormat": "AUDIT_REPORT_FORMAT_ODF",
          "scheduleConfig": {
            "startTime": "2026-10-25T10:00:00Z",
            "endTime": "2027-10-25T10:00:00Z",
            "frequency": "WEEKLY",
            "timeZone": "America/New_York"
          },
          "state": "SCHEDULE_STATE_ACTIVE",
          "createTime": "2026-10-25T13:27:00Z",
          "updateTime": "2026-10-25T13:27:00Z"
        }
      ]
    }
    

#### View details about a scheduled audit

To view details about a specific scheduled audit, send a `GET` request to the `auditSchedules` endpoint and specify the schedule ID.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 



HTTP method and URL: 
    
    
    GET https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/834/locations/us-central1/auditSchedules/my-schedule-id",
      "displayName": "My first audit schedule",
      "gcsUri": "gs://my-bucket",
      "complianceFramework": "builtin-cis-v8",
      "reportFormat": "AUDIT_REPORT_FORMAT_ODF",
      "scheduleConfig": {
        "startTime": "2026-10-25T10:00:00Z",
        "endTime": "2027-10-25T10:00:00Z",
        "frequency": "WEEKLY",
        "timeZone": "America/New_York"
      },
      "state": "SCHEDULE_STATE_ACTIVE",
      "createTime": "2026-10-25T13:27:00Z",
      "updateTime": "2026-10-25T13:27:00Z"
    }
    

## Update scheduled audits

You can pause, resume, and stop recurring audits. To change a schedule, you must delete the existing scheduled audit and then create a new scheduled audit.

### Console

  1. In the Google Cloud console, go to the **Audit management** page in Audit Manager.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager/manageaudits)

  2. In the **Schedules** tab, find the scheduled audit that you want to update.

  3. Do one of the following:

     * To pause an audit schedule, click pause **Pause schedule**.

     * To restart an audit that you paused, click play_circle_filled **Resume schedule**.

     * To delete a scheduled audit, click stop **Stop schedule**.




### gcloud

To pause, resume, or delete an audit schedule, run the [ `gcloud audit-manager audit-schedules update`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-schedules/update) command to update the state of the schedule.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 
  * SCHEDULE_STATE: the target state for the audit schedule. Set to one of the following: 
    * `paused`: to pause an active schedule.
    * `active`: to resume a paused schedule.
    * `deleted`: to stop and delete a schedule.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules update \
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID \
        --state=SCHEDULE_STATE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules update `
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID `
        --state=SCHEDULE_STATE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-schedules update ^
        RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID ^
        --state=SCHEDULE_STATE

You should receive a response similar to the following:
    
    
    complianceFramework: builtin-cis-v8
    gcsUri: gs://my-bucket
    name: projects/834/locations/us-central1/auditSchedules/my-schedule-id
    reportFormat: AUDIT_REPORT_FORMAT_ODF
    scheduleConfig:
      frequency: daily
      startTime: '2026-02-25T10:00:00Z'
    state: SCHEDULE_STATE_PAUSED
    

### REST

To pause, resume, or delete an audit schedule, send a `PATCH` request to update the `state` field of the audit schedule.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`. 
  * RESOURCE_ID: the resource ID of the organization, project, or folder. For example: `8767234`. 
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`. 
  * AUDIT_SCHEDULE_ID: the ID of the audit schedule. For example: `my-schedule-id`. To find the ID of an existing schedule, see the **Audit management** page in the Google Cloud console. 
  * SCHEDULE_STATE: the target state for the audit schedule. Set to one of the following: 
    * `SCHEDULE_STATE_PAUSED`: to pause an active schedule.
    * `SCHEDULE_STATE_ACTIVE`: to resume a paused schedule.
    * `SCHEDULE_STATE_DELETED`: to stop and delete a schedule. 



HTTP method and URL: 
    
    
    PATCH https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID?updateMask=state

Request JSON body: 
    
    
    {
      "state": "SCHEDULE_STATE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID?updateMask=state"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditSchedules/AUDIT_SCHEDULE_ID?updateMask=state" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/834/locations/us-central1/auditSchedules/my-schedule-id",
      "displayName": "My first audit schedule",
      "gcsUri": "gs://my-bucket",
      "complianceFramework": "builtin-cis-v8",
      "reportFormat": "AUDIT_REPORT_FORMAT_ODF",
      "scheduleConfig": {
        "startTime": "2026-02-25T10:00:00Z",
        "endTime": "2027-02-25T10:00:00Z",
        "frequency": "DAILY",
        "timeZone": "America/New_York"
      },
      "state": "SCHEDULE_STATE_PAUSED",
      "createTime": "2026-02-25T13:27:00Z",
      "updateTime": "2026-09-11T18:15:00Z"
    }
    

## What's next

  * [Get the status of an audit](https://docs.cloud.google.com/audit-manager/docs/audit-status)
  * [Troubleshoot run audit issues](https://docs.cloud.google.com/audit-manager/docs/troubleshoot-run-audit-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
