---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/
title: Patch dataset \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:56:44.618847+00:00
---

# Patch dataset  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/

[ Skip to main content ](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/)
  * [Deutsch](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=de)
  * [Español](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=es-419)
  * [Français](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=id)
  * [Italiano](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=it)
  * [Português](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=ja)
  * [한국어](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fhealthcare-api%2Fdocs%2Fsamples%2Fhealthcare-patch-dataset%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/business-intelligence-color.svg) ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Explore further](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#explore-further)
  * [Code sample](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#code-sample)
  * [What's next](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)


Was this helpful?
#  Patch dataset Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Explore further](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#explore-further)
  * [Code sample](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#code-sample)
  * [What's next](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#whats-next)


Patch a dataset.
## Explore further
For detailed documentation that includes this code sample, see the following: 
  * [Create and manage datasets](https://docs.cloud.google.com/healthcare-api/docs/datasets)


## Code sample
[Go](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#go)[Java](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#java)[Node.js](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#node.js)[Python](https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-dataset/#python) More
Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 
To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import (
	"context"
	"fmt"
	"io"

	healthcare "google.golang.org/api/healthcare/v1"
)

// patchDataset updates (patches) a dataset by updating its timezone..
func patchDataset(w io.Writer, projectID, location, datasetID, newTimeZone string) error {
	ctx := context.Background()

	healthcareService, err := healthcare.NewService(ctx)
	if err != nil {
		return fmt.Errorf("healthcare.NewService: %w", err)
	}

	datasetsService := healthcareService.Projects.Locations.Datasets

	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)

	if _, err := datasetsService.Patch(name, &healthcare.Dataset{
		TimeZone: newTimeZone,
	}).UpdateMask("timeZone").Do(); err != nil {
		return fmt.Errorf("Patch: %w", err)
	}

	fmt.Fprintf(w, "Patched dataset %s with timeZone %s\n", datasetID, newTimeZone)

	return nil
}

```

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 
To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import com.google.api.client.http.HttpRequestInitializer[](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
import com.google.api.client.http.javanet.NetHttpTransport[](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
import com.google.api.client.json.JsonFactory[](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
import com.google.api.client.json.gson.GsonFactory[](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
import com.google.api.services.healthcare.v1.CloudHealthcare;
import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
import com.google.api.services.healthcare.v1.model.Dataset;
import com.google.auth.http.HttpCredentialsAdapter[](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
import com.google.auth.oauth2.GoogleCredentials[](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
import java.io.IOException;
import java.util.Collections;

public class DatasetPatch {
  private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
  private static final JsonFactory JSON_FACTORY = new GsonFactory();
  private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();

  public static void datasetPatch(String datasetName) throws IOException {
    // String datasetName =
    //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");

    // Initialize the client, which will be used to interact with the service.
    CloudHealthcare client = createClient();

    // Fetch the initial state of the dataset.
    Datasets.Get getRequest = client.projects().locations().datasets().get(datasetName);
    Dataset dataset = getRequest.execute();

    // Update the Dataset fields as needed as needed. For a full list of dataset fields, see:
    // https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets#Dataset
    dataset.setTimeZone("America/New_York");

    // Create request and configure any parameters.
    Datasets.Patch request =
        client
            .projects()
            .locations()
            .datasets()
            .patch(datasetName, dataset)
            .setUpdateMask("timeZone");

    // Execute the request and process the results.
    dataset = request.execute();
    System.out.println("Dataset patched: \n" + dataset.toPrettyString());
  }

  private static CloudHealthcare createClient() throws IOException {
    // Use Application Default Credentials (ADC) to authenticate the requests
    // For more information see https://cloud.google.com/docs/authentication/production
    GoogleCredentials credential =
        GoogleCredentials.getApplicationDefault()
            .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));

    // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
    HttpRequestInitializer requestInitializer =
        request -> {
          new HttpCredentialsAdapter(credential).initialize(request);
          request.setConnectTimeout(60000); // 1 minute connect timeout
          request.setReadTimeout(60000); // 1 minute read timeout
        };

    // Build the client for interacting with the service.
    return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
        .setApplicationName("your-application-name")
        .build();
  }
}
```

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 
To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
const google = require('@googleapis/healthcare');
const healthcare = google.healthcare({
  version: 'v1',
  auth: new google.auth.GoogleAuth({
    scopes: ['https://www.googleapis.com/auth/cloud-platform'],
  }),
});

const patchDataset = async () => {
  // TODO(developer): uncomment these lines before running the sample
  // const cloudRegion = 'us-central1';
  // const projectId = 'adjective-noun-123';
  // const datasetId = 'my-dataset';
  // const timeZone = 'UTC';
  const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
  const request = {
    name,
    updateMask: 'timeZone',
    resource: {timeZone: timeZone},
  };

  await healthcare.projects.locations.datasets.patch(request);
  console.log(`Dataset ${datasetId} patched with time zone ${timeZone}`);
};

patchDataset();
```

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 
To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
# Imports the Dict type for runtime type hints.
from typing import Dict

def patch_dataset(
    project_id: str, location: str, dataset_id: str, time_zone: str
) -> Dict[str, str]:
    """Updates dataset metadata.

    See
    https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
    before running the sample.
    See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#patch
    for the Python API reference.

    Args:
      project_id: The project ID or project number of the Google Cloud project you want
          to use.
      location: The name of the dataset's location.
      dataset_id: The ID of the dataset to patch.
      time_zone: The default timezone used by the dataset.

    Returns:
      A dictionary representing the patched Dataset resource.
    """
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    # Imports HttpError from the Google Python API client errors module.
    from googleapiclient.errors import HttpError

    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'
    # location = 'us-central1'
    # dataset_id = 'my-dataset'
    # time_zone = 'GMT'
    dataset_parent = f"projects/{project_id}/locations/{location}"
    dataset_name = f"{dataset_parent}/datasets/{dataset_id}"

    # Sets the time zone
    patch = {"timeZone": time_zone}

    request = (
        client.projects()
        .locations()
        .datasets()
        .patch(name=dataset_name, updateMask="timeZone", body=patch)
    )

    try:
        response = request.execute()
        print(f"Patched dataset {dataset_id} with time zone: {time_zone}")
        return response
    except HttpError as err:
        raise err


```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
