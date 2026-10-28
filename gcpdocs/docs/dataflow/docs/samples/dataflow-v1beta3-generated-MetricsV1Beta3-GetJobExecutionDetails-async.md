---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/
title: Get job execution details (async) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:01:42.163357+00:00
---

# Get job execution details (async)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/

[ Skip to main content ](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/)
  * [Deutsch](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=de)
  * [Español](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=es-419)
  * [Français](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=id)
  * [Italiano](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=it)
  * [Português](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=ja)
  * [한국어](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdataflow%2Fdocs%2Fsamples%2Fdataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/dataflow/docs)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Code sample](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#code-sample)
  * [What's next](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)


Was this helpful?
#  Get job execution details (async) Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Code sample](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#code-sample)
  * [What's next](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#whats-next)


Demonstrates how to asynchronously request detailed information about the execution status of the job.
## Code sample
[C#](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#c)[Java](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#java)[Node.js](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#node.js)[Python](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobExecutionDetails-async/#python) More
To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
using System;
using System.Threading.Tasks;

public sealed partial class GeneratedMetricsV1Beta3ClientSnippets
{
    /// <summary>Snippet for GetJobExecutionDetailsAsync</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public async Task GetJobExecutionDetailsRequestObjectAsync()
    {
        // Create client
        [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html) metricsV1Beta3Client = await [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_CreateAsync_System_Threading_CancellationToken_)();
        // Initialize request argument(s)
        [GetJobExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobExecutionDetailsRequest.html) request = new [GetJobExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobExecutionDetailsRequest.html)
        {
            ProjectId = "",
            JobId = "",
            Location = "",
        };
        // Make the request
        PagedAsyncEnumerable<JobExecutionDetails, StageSummary> response = metricsV1Beta3Client.[GetJobExecutionDetailsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobExecutionDetailsAsync_Google_Cloud_Dataflow_V1Beta3_GetJobExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);

        // Iterate over all response items, lazily performing RPCs as required
        await foreach ([StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary.html) item in response)
        {
            // Do something with each item
            Console.WriteLine(item);
        }

        // Or iterate over pages (of server-defined size), performing one RPC per page
        await foreach ([JobExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobExecutionDetails.html) page in response.AsRawResponses())
        {
            // Do something with each page of items
            Console.WriteLine("A page of results:");
            foreach ([StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary.html) item in page)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
        }

        // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
        int pageSize = 10;
        Page<StageSummary> singlePage = await response.ReadPageAsync(pageSize);
        // Do something with the page of items
        Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
        foreach ([StageSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageSummary.html) item in singlePage)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
        // Store the pageToken, for when the next page is required.
        string nextPageToken = singlePage.NextPageToken;
    }
}
```

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import com.google.api.core.ApiFuture[](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
import com.google.dataflow.v1beta3.GetJobExecutionDetailsRequest;
import com.google.dataflow.v1beta3.MetricsV1Beta3Client;
import com.google.dataflow.v1beta3.StageSummary;

public class AsyncGetJobExecutionDetails {

  public static void main(String[] args) throws Exception {
    asyncGetJobExecutionDetails();
  }

  public static void asyncGetJobExecutionDetails() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (MetricsV1Beta3Client metricsV1Beta3Client = MetricsV1Beta3Client.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
      GetJobExecutionDetailsRequest request =
          GetJobExecutionDetailsRequest.newBuilder()
              .setProjectId("projectId-894832108")
              .setJobId("jobId101296568")
              .setLocation("location1901043637")
              .setPageSize(883849137)
              .setPageToken("pageToken873572522")
              .build();
      ApiFuture<StageSummary> future =
          metricsV1Beta3Client.getJobExecutionDetailsPagedCallable().futureCall(request);
      // Do something.
      for (StageSummary element : future.get().iterateAll()) {
        // doThingsWith(element);
      }
    }
  }
}
```

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
/**
 * This snippet has been automatically generated and should be regarded as a code template only.
 * It will require modifications to work.
 * It may require correct/in-range values for request initialization.
 * TODO(developer): Uncomment these variables before running the sample.
 */
/**
 *  A project id.
 */
// const projectId = 'abc123'
/**
 *  The job to get execution details for.
 */
// const jobId = 'abc123'
/**
 *  The regional endpoint 
 *  (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that
 *  contains the job specified by job_id.
 */
// const location = 'abc123'
/**
 *  If specified, determines the maximum number of stages to
 *  return.  If unspecified, the service may choose an appropriate
 *  default, or may return an arbitrarily large number of results.
 */
// const pageSize = 1234
/**
 *  If supplied, this should be the value of next_page_token returned
 *  by an earlier call. This will cause the next page of results to
 *  be returned.
 */
// const pageToken = 'abc123'

// Imports the Dataflow library
const {MetricsV1Beta3Client} = require('@google-cloud/dataflow[](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)').v1beta3;

// Instantiates a client
const dataflowClient = new [MetricsV1Beta3Client](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)();

async function callGetJobExecutionDetails() {
  // Construct request
  const request = {
  };

  // Run request
  const iterable = dataflowClient.[getJobExecutionDetailsAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/v1beta3.metricsv1beta3client.html)(request);
  for await (const response of iterable) {
      console.log(response);
  }
}

callGetJobExecutionDetails();
```

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest)


async def sample_get_job_execution_details():
    # Create a client
    client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[MetricsV1Beta3AsyncClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html)()

    # Initialize request argument(s)
    request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetJobExecutionDetailsRequest.html)()

    # Make the request
    page_result = client.[get_job_execution_details](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html#google_cloud_dataflow_v1beta3_services_metrics_v1_beta3_MetricsV1Beta3AsyncClient_get_job_execution_details)(request=request)

    # Handle the response
    async for response in page_result:
        print(response)


```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
