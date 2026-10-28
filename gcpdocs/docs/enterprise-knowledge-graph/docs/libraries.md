---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/
title: Enterprise Knowledge Graph client libraries \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:56:49.973020+00:00
---

# Enterprise Knowledge Graph client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/

#} [ Skip to main content ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/)
  * [Deutsch](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=es-419)
  * [Français](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=id)
  * [Italiano](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=ja)
  * [한국어](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Install the client library](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#install)
  * [Set up authentication](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#authentication)
  * [Use the client library](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#use)
  * [Additional resources](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#resources)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Reference ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries)


Send feedback 
#  Enterprise Knowledge Graph client libraries Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Install the client library](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#install)
  * [Set up authentication](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#authentication)
  * [Use the client library](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#use)
  * [Additional resources](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#resources)


This page shows how to get started with the Cloud Client Libraries for the Enterprise Knowledge Graph API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.
Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).
## Install the client library
[Python](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#python) More

```
pip install --upgrade google-cloud-enterpriseknowledgegraph
```

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).
## Set up authentication
To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 
For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).
For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:
  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 

```
gcloud init
```

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
  2. If you're using a local shell, then create local authentication credentials for your user account: 

```
gcloud auth application-default login
```

You don't need to do this if you're using Cloud Shell.
If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 


## Use the client library
The following example shows how to use the client library. 
[Python](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#python) More

```

from __future__ import annotations

from collections.abc import Sequence

from google.cloud import enterpriseknowledgegraph as ekg

# TODO(developer): Uncomment these variables before running the sample.
# project_id = 'YOUR_PROJECT_ID'
# location = 'YOUR_GRAPH_LOCATION'      # Values: 'global'
# search_query = 'YOUR_SEARCH_QUERY'
# languages = ['en']                    # Optional: List of ISO 639-1 Codes
# types = ['']                          # Optional: List of schema.org types to return
# limit = 20                            # Optional: Number of entities to return


def search_public_kg_sample(
    project_id: str,
    location: str,
    search_query: str,
    languages: Sequence[str] = None,
    types: Sequence[str] = None,
    limit: int = 20,
):
    # Create a client
    client = ekg.EnterpriseKnowledgeGraphServiceClient()

    # The full resource name of the location
    # e.g. projects/{project_id}/locations/{location}
    parent = client.common_location_path(project=project_id, location=location)

    # Initialize request argument(s)
    request = ekg.SearchPublicKgRequest(
        parent=parent,
        query=search_query,
        languages=languages,
        types=types,
        limit=limit,
    )

    # Make the request
    response = client.search_public_kg(request=request)

    print(f"Search Query: {search_query}\n")

    # Extract and print date from response
    for item in response.item_list_element:
        result = item.get("result")

        print(f"Name: {result.get('name')}")
        print(f"- Description: {result.get('description')}")
        print(f"- Types: {result.get('@type')}\n")

        detailed_description = result.get("detailedDescription")

        if detailed_description:
            print("- Detailed Description:")
            print(f"\t- Article Body: {detailed_description.get('articleBody')}")
            print(f"\t- URL: {detailed_description.get('url')}")
            print(f"\t- License: {detailed_description.get('license')}\n")

        print(f"- Cloud MID: {result.get('@id')}")
        for identifier in result.get("identifier"):
            print(f"\t- {identifier.get('name')}: {identifier.get('value')}")

        print("\n")


```

## Additional resources
[Python](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries/#python) More
The following list contains links to more resources related to the client library for Python:
  * [API reference](https://docs.cloud.google.com/python/docs/reference/enterpriseknowledgegraph/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-python/issues)
  * [`enterprise-knowledge-graph` on Stack Overflow](https://stackoverflow.com/search?q=%5Benterprise-knowledge-graph%5D+%5Bpython%5D)
  * [Source code](https://github.com/GoogleCloudPlatform/google-cloud-python)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
