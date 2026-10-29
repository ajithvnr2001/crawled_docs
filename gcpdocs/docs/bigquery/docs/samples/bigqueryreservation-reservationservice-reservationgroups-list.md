---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservationgroups-list/
title: List reservation groups \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:08:55.037506+00:00
---

# List reservation groups  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservationgroups-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  List reservation groups Stay organized with collections  Save and categorize content based on your preferences. 

Lists all BigQuery reservation groups within a specified project and location.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.reservation.v1.[ListReservationGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ListReservationGroupsRequest.html);
    import com.google.cloud.bigquery.reservation.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html);
    import java.io.IOException;
    
    public class ListReservationGroups {
    
      /**
       * Lists all BigQuery reservation groups in a given project and location. A reservation group is
       * a container for reservations.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the reservation groups (for example, "us-central1").
       */
      public static void listReservationGroups(String projectId, String location) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html).of(projectId, location);
    
        [ListReservationGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ListReservationGroupsRequest.html) request =
            [ListReservationGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ListReservationGroupsRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html#com_google_cloud_bigquery_reservation_v1_LocationName_toString__)()).build();
    
        try ([ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html) client = [ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html).create()) {
          System.out.printf("Listed reservation groups for parent: '%s'%n", parent);
          for ([ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html) group : client.listReservationGroups(request).iterateAll()) {
            System.out.printf("  Reservation group: %s%n", group.getName());
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: parent resource '%s' not found: %s%n", parent, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to list reservation groups in '%s': %s%n", parent, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('@grpc/grpc-js');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Lists all reservation groups for a project in a specified location.
     * A reservation group is a container for reservations.
     *
     * @param {string} projectId Google Cloud project ID (for example, 'example-project-id').
     * @param {string} location Google Cloud location (for example, 'us-central1').
     */
    async function listReservationGroups(projectId, location = 'us-central1') {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      try {
        const [reservationGroups] = await client.listReservationGroups(request);
    
        if (reservationGroups.length === 0) {
          console.log(
            `No reservation groups found in project ${projectId} at location ${location}.`,
          );
          return;
        }
    
        console.log(
          `Reservation groups in project ${projectId} at location ${location}:`,
        );
        for (const group of reservationGroups) {
          console.log(`  ${group.name}`);
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(`Project or location not found: ${request.parent}`);
        } else {
          console.error('Error listing reservation groups:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def list_reservation_groups(project_id: str, location: str):
        """Lists all reservation groups for the project in the specified location.
    
        A reservation group is a container for reservations. This sample shows
        how to list all reservation groups within a specific project and location.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation groups, for example, "us-central1".
        """
        parent = f"projects/{project_id}/locations/{location}"
    
        try:
            page_result = client.[list_reservation_groups](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_list_reservation_groups)(parent=parent)
            print(f"Listed reservation groups for parent: '{parent}'")
            for group in page_result:
                print(f"  Reservation group: {group.name}")
        except google.api_core.exceptions.NotFound:
            print(f"Parent resource '{parent}' was not found.")
        except google.api_core.exceptions.GoogleAPICallError as e:
            print(
                f"Could not list reservation groups. Please check your permissions. Error: {e}"
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
