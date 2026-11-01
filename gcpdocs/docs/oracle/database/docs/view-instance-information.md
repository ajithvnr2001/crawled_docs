---
url: https://docs.cloud.google.com/oracle/database/docs/view-instance-information/
title: View Exadata Infrastructure instance information \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:38:46.052263+00:00
---

# View Exadata Infrastructure instance information  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-instance-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  View Exadata Infrastructure instance information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the instance information for an Exadata Infrastructure instance.

## Before you begin

  * [Set up your Google Cloud project](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * Confirm that you have the required roles necessary to create an instance: `cloudExadataInfrastructureAdmin`.

For more information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View instance information

### Console

  1. Go to the **Exadata Database Service** page in the Google Cloud console.

[Go to Exadata Database Service](https://console.cloud.google.com/oracle/exadata/)

  2. In the **Exadata Infrastructure** section, click the display name of the instance to view instance information for.

You'll be redirected to the instance's details page.




### gcloud

Use the `gcloud oracle-database cloud-exadata-infrastructures describe` command to view Instance information for your Exadata Infrastructure instance.
    
    
     gcloud oracle-database cloud-exadata-infrastructures describe INSTANCE_ID
     --location=REGION_ID
    

Replace the following:

  * INSTANCE_ID: the identifier for the instance that you want to view information for.
  * REGION_ID: the region for the instance that you want to view information for.



### C#
    
    
    using Google.Cloud.OracleDatabase.V1;
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedOracleDatabaseClientSnippets
    {
        /// <summary>Snippet for GetCloudExadataInfrastructureAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task GetCloudExadataInfrastructureAsync()
        {
            // Create client
            OracleDatabaseClient oracleDatabaseClient = await OracleDatabaseClient.CreateAsync();
            // Initialize request argument(s)
            string name = "projects/[PROJECT]/locations/[LOCATION]/cloudExadataInfrastructures/[CLOUD_EXADATA_INFRASTRUCTURE]";
            // Make the request
            CloudExadataInfrastructure response = await oracleDatabaseClient.GetCloudExadataInfrastructureAsync(name);
        }
    }

### Go
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &oracledatabasepb.GetCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetCloudExadataInfrastructureRequest.
    	}
    	resp, err := c.GetCloudExadataInfrastructure(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java
    
    
    import com.google.api.core.ApiFuture;
    import com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure;
    import com.google.cloud.oracledatabase.v1.CloudExadataInfrastructureName;
    import com.google.cloud.oracledatabase.v1.GetCloudExadataInfrastructureRequest;
    import com.google.cloud.oracledatabase.v1.OracleDatabaseClient;
    
    public class AsyncGetCloudExadataInfrastructure {
    
      public static void main(String[] args) throws Exception {
        asyncGetCloudExadataInfrastructure();
      }
    
      public static void asyncGetCloudExadataInfrastructure() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (OracleDatabaseClient oracleDatabaseClient = OracleDatabaseClient.create()) {
          GetCloudExadataInfrastructureRequest request =
              GetCloudExadataInfrastructureRequest.newBuilder()
                  .setName(
                      CloudExadataInfrastructureName.of(
                              "[PROJECT]", "[LOCATION]", "[CLOUD_EXADATA_INFRASTRUCTURE]")
                          .toString())
                  .build();
          ApiFuture<CloudExadataInfrastructure> future =
              oracleDatabaseClient.getCloudExadataInfrastructureCallable().futureCall(request);
          // Do something.
          CloudExadataInfrastructure response = future.get();
        }
      }
    }

### Node.js
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The name of the Cloud Exadata Infrastructure in the following
     *  format:
     *  projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.
     */
    // const name = 'abc123'
    
    // Imports the Oracledatabase library
    const {OracleDatabaseClient} = require('@google-cloud/oracledatabase').v1;
    
    // Instantiates a client
    const oracledatabaseClient = new OracleDatabaseClient();
    
    async function callGetCloudExadataInfrastructure() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await oracledatabaseClient.getCloudExadataInfrastructure(request);
      console.log(response);
    }
    
    callGetCloudExadataInfrastructure();

### PHP
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\OracleDatabase\V1\Client\OracleDatabaseClient;
    use Google\Cloud\OracleDatabase\V1\CloudExadataInfrastructure;
    use Google\Cloud\OracleDatabase\V1\GetCloudExadataInfrastructureRequest;
    
    /**
     * Gets details of a single Exadata Infrastructure.
     *
     * @param string $formattedName The name of the Cloud Exadata Infrastructure in the following
     *                              format:
     *                              projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}. Please see
     *                              {@see OracleDatabaseClient::cloudExadataInfrastructureName()} for help formatting this field.
     */
    function get_cloud_exadata_infrastructure_sample(string $formattedName): void
    {
        // Create a client.
        $oracleDatabaseClient = new OracleDatabaseClient();
    
        // Prepare the request message.
        $request = (new GetCloudExadataInfrastructureRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var CloudExadataInfrastructure $response */
            $response = $oracleDatabaseClient->getCloudExadataInfrastructure($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedName = OracleDatabaseClient::cloudExadataInfrastructureName(
            '[PROJECT]',
            '[LOCATION]',
            '[CLOUD_EXADATA_INFRASTRUCTURE]'
        );
    
        get_cloud_exadata_infrastructure_sample($formattedName);
    }

### Python
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import oracledatabase_v1
    
    
    def sample_get_cloud_exadata_infrastructure():
        # Create a client
        client = oracledatabase_v1.OracleDatabaseClient()
    
        # Initialize request argument(s)
        request = oracledatabase_v1.GetCloudExadataInfrastructureRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.get_cloud_exadata_infrastructure(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby
    
    
    require "google/cloud/oracle_database/v1"
    
    ##
    # Snippet for the get_cloud_exadata_infrastructure call in the OracleDatabase service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::OracleDatabase::V1::OracleDatabase::Client#get_cloud_exadata_infrastructure.
    #
    def get_cloud_exadata_infrastructure
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::OracleDatabase::V1::OracleDatabase::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::OracleDatabase::V1::GetCloudExadataInfrastructureRequest.new
    
      # Call the get_cloud_exadata_infrastructure method.
      result = client.get_cloud_exadata_infrastructure request
    
      # The returned object is of type Google::Cloud::OracleDatabase::V1::CloudExadataInfrastructure.
      p result
    end

## What's next

  * Learn how to [create](https://docs.cloud.google.com/oracle/database/docs/create-instances) or [delete](https://docs.cloud.google.com/oracle/database/docs/delete-instances) an instance.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance.
  * [Use monitoring metrics](https://docs.cloud.google.com/oracle/database/docs/monitoring-metrics) to monitor your instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
