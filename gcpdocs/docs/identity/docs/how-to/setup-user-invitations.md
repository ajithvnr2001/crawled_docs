---
url: https://docs.cloud.google.com/identity/docs/how-to/setup-user-invitations/
title: Set up the User Invitation API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T16:29:50.284475+00:00
---

# Set up the User Invitation API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup-user-invitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up the User Invitation API

This page explains how to set up the Cloud Identity User Invitation API.

## Enable the API and set up credentials

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  4. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Service Account Token Creator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Service Account Token Creator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  7. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Service Account Token Creator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Service Account Token Creator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 




## Install the Python client library

To install the Python client library, run the following command:
    
    
      pip install --upgrade google-api-python-client google-auth \
        google-auth-oauthlib google-auth-httplib2
    

For more information about setting up your Python development environment, see the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).

## Authenticate and instantiate a client

To call the User Invitation API as a service account, you must use domain-wide delegation (DWD). You can authenticate the service account using Application Default Credentials (ADC) or a service account key.

To authenticate as an administrator without DWD, use end-user OAuth 2.0 credentials with the `https://www.googleapis.com/auth/cloud-identity.userinvitations` scope instead. For more information, see [Using OAuth 2.0 for web server applications](https://developers.google.com/identity/protocols/oauth2/web-server#obtainingaccesstokens).

**Warning:** Domain-wide delegation (DWD) is a powerful privilege that lets a service account impersonate any user in your domain with the allowed scopes. Use DWD only when absolutely necessary, because it can pose a security risk. Whenever possible, grant specific Cloud Identity roles directly to the service account instead. The User Invitation API doesn't support granting a role to a service account, so service accounts require DWD. See [domain-wide delegation best practices](https://knowledge.workspace.google.com/admin/apps/domain-wide-delegation-best-practices). 

### Set up domain-wide delegation

To use domain-wide delegation, you must grant the service account authority to impersonate an administrator. Audit logs show any service account actions as the impersonated user.

For instructions, see [Delegate domain-wide authority to your service account](https://developers.google.com/admin-sdk/directory/v1/guides/delegation#delegate_domain-wide_authority_to_your_service_account).

To authorize the service account, provide the following scope:

  * `https://www.googleapis.com/auth/cloud-identity.userinvitations`



### Instantiate a client

To instantiate a client, choose an authentication method. We recommend using Application Default Credentials (ADC) if your code is running on Google Cloud or using Workload Identity Federation.

###  ADC 
    
    
    from google.auth import iam
    from google.auth.transport import requests
    import google.auth
    from google.oauth2 import service_account
    
    INITIAL_SCOPES = ['https://www.googleapis.com/auth/iam']
    CI_SCOPES = ['https://www.googleapis.com/auth/cloud-identity.userinvitations']
    TOKEN_URI = "https://accounts.google.com/o/oauth2/token"
    
    def create_delegated_credentials(
      user_email: str
    ) -> google.auth.credentials.Credentials:
      """Creates delegated credentials for the user.
    
      Args:
        user_email: The administrator email to call as.
    
      Returns:
        The delegated credentials for the user.
      """
    
      # Fetch application default credentials (ADC)
      credentials, _ = google.auth.default(scopes=INITIAL_SCOPES)
    
      # Populate account information
      request = requests.Request()
      credentials.refresh(request)
    
      # Create an IAM signer
      signer = iam.Signer(request, credentials,
                          credentials.service_account_email)
    
      # Create domain-wide delegated (DWD) credentials
      delegated_credentials = service_account.Credentials(
          signer=signer,
          service_account_email=credentials.service_account_email,
          token_uri=TOKEN_URI,
          scopes=CI_SCOPES,
          subject=user_email
      )
    
      return delegated_credentials
    

###  Service account key 
    
    
    from google.oauth2 import service_account
    import googleapiclient.discovery
    
    SCOPES = ['https://www.googleapis.com/auth/cloud-identity.userinvitations']
    SERVICE_ACCOUNT_FILE = '/path/to/service-account-file.json'
    
    def create_service():
      credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
      delegated_credentials = credentials.with_subject('user@altostrat.com')
    
      service_name = 'cloudidentity'
      api_version = 'v1'
      service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials)
    
      return service
    

After running this code, you can begin making calls to the User Invitation API.

## What's next

  * [Create and manage user invitations](https://docs.cloud.google.com/identity/docs/how-to/manage-user-invitations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
