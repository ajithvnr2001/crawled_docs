---
url: https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/
title: Set up the Allowlisted Domains API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:57:08.881944+00:00
---

# Set up the Allowlisted Domains API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/

[ Skip to main content ](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/)
  * [Deutsch](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=es-419)
  * [Français](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=id)
  * [Italiano](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=ja)
  * [한국어](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/identity/docs)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#before_you_begin)
  * [Install the Python client library](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#install-python)
  * [Enable the API and set up credentials](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#enable)
    * [Create an API key](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#create_an_api_key)
  * [Authenticate as a service account with domain-wide delegation](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#setup-dwd)
    * [Initialize credentials and instantiate a client](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#initialize-credentials)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)


Was this helpful?
Send feedback 
  * On this page
  * [Before you begin](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#before_you_begin)
  * [Install the Python client library](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#install-python)
  * [Enable the API and set up credentials](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#enable)
    * [Create an API key](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#create_an_api_key)
  * [Authenticate as a service account with domain-wide delegation](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#setup-dwd)
    * [Initialize credentials and instantiate a client](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#initialize-credentials)


# Set up the Allowlisted Domains API Stay organized with collections  Save and categorize content based on your preferences.
This page explains how to set up the Allowlisted Domains API before [adding](https://docs.cloud.google.com/identity/docs/how-to/create-allowlisted-domains), [listing and getting](https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains), or [deleting](https://docs.cloud.google.com/identity/docs/how-to/delete-allowlisted-domains) allowlisted domains.
## Before you begin
Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. For instructions, see [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).
## Install the Python client library
To install the Python client library, run the following command:

```
  pip install --upgrade google-api-python-client google-auth \
    google-auth-oauthlib google-auth-httplib2

```

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).
## Enable the API and set up credentials
  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
**Roles required to select or create a project**
     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 
  4. Enable the Cloud Identity API, if it is not already enabled. 
**Roles required to enable APIs**
To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)
  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
**Roles required to select or create a project**
     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 
  7. Enable the Cloud Identity API, if it is not already enabled. 
**Roles required to enable APIs**
To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)
  8. Create a service account: 
     * Ensure that you have the **Create Service Accounts** IAM role (`roles/iam.serviceAccountCreator`) and the **Project IAM Admin** role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
     * In the Google Cloud console, go to the [**Create service account**](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project) page.
     * Select your project.
     * In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.
     * In the **Service account description** field, enter a description. For example, `Service account for quickstart`.
     * Click **Create and continue**.
     * Grant the **Project > Owner** role to the service account. To grant the role, find the **Select a role** list, then select **Project > Owner**.
     * Click **Continue**.
     * Click **Done** to finish creating the service account. Don't close your browser window. You will use it in the next step.
  9. Create a service account key: 
     * In the Google Cloud console, click the email address for the service account that you created.
     * Click **Keys**.
     * Click **Add key** , and then click **Create new key**.
     * Click **Create**. A JSON key file is downloaded to your computer.
     * Click **Close**.


### Create an API key
  1. In the Google Cloud console, go to the [Credentials](https://console.cloud.google.com/apis/credentials) page.
  2. Click **Create Credentials** and select **API key**.
  3. The **API key created** dialog displays your newly created API key. Copy this key for use in your script as the `API_KEY` constant.


## Authenticate as a service account with domain-wide delegation
If you're an administrator managing allowlisted domains, or if you want to provide an account with domain-wide privileges so that it can manage allowlisted domains on behalf of administrators, you should authenticate as a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) and then grant domain-wide privileges to the service account.
For details about setting up domain-wide delegation, see [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106). Review the [best practices](https://support.google.com/a/answer/14437356) to mitigate the security risks associated with using domain-wide delegation.
Provide the following scopes to authorize the service account:
  * **For read and write operations** (`create`, `delete`, `list`, `get`): `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains`
  * **For read-only operations** (`list`, `get`): `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains.readonly`


### Initialize credentials and instantiate a client
When you initialize the credential in your code, specify the email address on which the service account acts by calling `with_subject()` on the credential.
The following example shows how to instantiate a client using service account credentials to interact with the Allowlisted Domains API:
[ Python ](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/#python) More

```
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = [
    'https://www.googleapis.com/auth/cloud-identity.allowlisteddomains.readonly',
    'https://www.googleapis.com/auth/cloud-identity.allowlisteddomains',
]
SERVICE_ACCOUNT_FILE = 'SERVICE_ACCOUNT_CREDENTIAL_FILE'
PROD_DISCOVERY_URL_BASE = (
    'https://cloudidentity.googleapis.com/$discovery/rest'
)
API_KEY = 'YOUR_API_KEY'

def create_service(version, delegated_email):
  """Instantiates a client using service account credentials."""
  credentials = service_account.Credentials.from_service_account_file(
      SERVICE_ACCOUNT_FILE, scopes=SCOPES
  )
  delegated_credentials = credentials.with_subject(delegated_email)
  url = f'{PROD_DISCOVERY_URL_BASE}?version={version}&key={API_KEY}'

  service = googleapiclient.discovery.build(
      serviceName=None,
      version=None,
      credentials=delegated_credentials,
      discoveryServiceUrl=url,
      static_discovery=False,
  )
  return service

```

Replace the following:
  * `SERVICE_ACCOUNT_CREDENTIAL_FILE`: the service account key file that you created earlier in this document
  * `YOUR_API_KEY`: the API key copied from your Google Cloud console Credentials page


Detailed sample code to call the Allowlisted Domains API operations are provided in [Listing and getting allowlisted domains](https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
