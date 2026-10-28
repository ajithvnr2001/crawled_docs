---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/
title: Get job metrics \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:03:17.140118+00:00
---

# Get job metrics  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/

[ Skip to main content ](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/)
  * [Deutsch](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=de)
  * [Español](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=es-419)
  * [Français](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=id)
  * [Italiano](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=it)
  * [Português](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=ja)
  * [한국어](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdataflow%2Fdocs%2Fsamples%2Fdataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/dataflow/docs)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Code sample](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#code-sample)
  * [What's next](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)


Was this helpful?
#  Get job metrics Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Code sample](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#code-sample)
  * [What's next](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#whats-next)


Demonstrates how to get a collection of metrics describing the progress of a job.
## Code sample
[C#](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#c)[Go](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#go)[Java](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#java)[Python](https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-sync/#python) More
To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);

public sealed partial class GeneratedMetricsV1Beta3ClientSnippets
{
    /// <summary>Snippet for GetJobMetrics</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void GetJobMetricsRequestObject()
    {
        // Create client
        [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html) metricsV1Beta3Client = [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_Create)();
        // Initialize request argument(s)
        [GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest.html) request = new [GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest.html)
        {
            ProjectId = "",
            JobId = "",
            StartTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)(),
            Location = "",
        };
        // Make the request
        [JobMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobMetrics.html) response = metricsV1Beta3Client.[GetJobMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobMetrics_Google_Cloud_Dataflow_V1Beta3_GetJobMetricsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    }
}
```

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```

//go:build examples

package main

import (
	"context"

	dataflow "cloud.google.com/go/dataflow/apiv1beta3"
	dataflowpb "cloud.google.com/go/dataflow/apiv1beta3/dataflowpb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := dataflow.NewMetricsV1Beta3Client(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &dataflowpb.GetJobMetricsRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/dataflow/apiv1beta3/dataflowpb#GetJobMetricsRequest.
	}
	resp, err := c.GetJobMetrics(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}

```

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

```
import com.google.dataflow.v1beta3.GetJobMetricsRequest;
import com.google.dataflow.v1beta3.JobMetrics;
import com.google.dataflow.v1beta3.MetricsV1Beta3Client;
import com.google.protobuf.Timestamp[](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);

public class SyncGetJobMetrics {

  public static void main(String[] args) throws Exception {
    syncGetJobMetrics();
  }

  public static void syncGetJobMetrics() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (MetricsV1Beta3Client metricsV1Beta3Client = MetricsV1Beta3Client.create()) {
      GetJobMetricsRequest request =
          GetJobMetricsRequest.newBuilder()
              .setProjectId("projectId-894832108")
              .setJobId("jobId101296568")
              .setStartTime([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().build())
              .setLocation("location1901043637")
              .build();
      JobMetrics response = metricsV1Beta3Client.getJobMetrics(request);
    }
  }
}
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


def sample_get_job_metrics():
    # Create a client
    client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[MetricsV1Beta3Client](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3Client.html)()

    # Initialize request argument(s)
    request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetJobMetricsRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetJobMetricsRequest.html)()

    # Make the request
    response = client.[get_job_metrics](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3Client.html#google_cloud_dataflow_v1beta3_services_metrics_v1_beta3_MetricsV1Beta3Client_get_job_metrics)(request=request)

    # Handle the response
    print(response)


```

## What's next
To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 
Was this helpful?
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
