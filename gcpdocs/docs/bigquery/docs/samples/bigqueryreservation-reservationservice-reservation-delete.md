---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-delete/
title: Delete a BigQuery reservation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:08:53.516649+00:00
---

# Delete a BigQuery reservation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservation-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Delete a BigQuery reservation Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a reservation from the BigQuery Reservation API. The reservation must not have any assignments.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigquery.reservation.v1.[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.DeleteReservationRequest.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationName.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html);
    import java.io.IOException;
    
    public class DeleteReservation {
    
      /**
       * Deletes a specified BigQuery reservation. A reservation can only be deleted if it has no
       * active assignments.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the reservation (for example, "us-central1").
       * @param reservationId The ID of the reservation to delete (for example, "example-reservation").
       */
      public static void deleteReservation(String projectId, String location, String reservationId) {
        [ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationName.html) name = [ReservationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationName.html).of(projectId, location, reservationId);
    
        [DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.DeleteReservationRequest.html) request =
            [DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.DeleteReservationRequest.html).newBuilder().setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationName.html#com_google_cloud_bigquery_reservation_v1_ReservationName_toString__)()).build();
    
        try ([ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html) client = [ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html).create()) {
          client.deleteReservation(request);
          System.out.printf("Deleted reservation: %s%n", name);
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) err) {
          System.err.printf(
              "error: reservation '%s' not found in location '%s' for project '%s': %s%n",
              reservationId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to delete reservation '%s' in location '%s' for project '%s': %s%n",
              reservationId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        }
      }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    const {ReservationServiceClient} =
      require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)').v1;
    const {status} = require('google-gax');
    
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    /**
     * Deletes a reservation.
     * A reservation provides computational resource guarantees, in the form of slots, to users.
     * @param {string} projectId The Google Cloud project ID.
     * @param {string} location The geographic location where the reservation resides, for example 'us-central1'.
     * @param {string} reservationId The ID of the reservation to delete, for example 'example-reservation'.
     */
    async function deleteReservation(
      projectId,
      location = 'us-central1',
      reservationId = 'example-reservation',
    ) {
      // Construct the fully-qualified path for the reservation.
      const name = client.[reservationPath](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/v1.reservationserviceclient.html)(projectId, location, reservationId);
    
      const request = {
        name,
      };
    
      try {
        await client.deleteReservation(request);
        console.log(`Deleted reservation: ${reservationId}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.log(
            `Reservation ${reservationId} not found in project ${projectId} location ${location}.`,
          );
        } else {
          console.error(`Error deleting reservation ${reservationId}:`, err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def delete_reservation(project_id: str, location: str, reservation_id: str):
        """Deletes a reservation.
    
        A reservation can only be deleted if it has no assignments.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location of the reservation, for example, "us-central1".
            reservation_id: The ID of the reservation to delete.
        """
        name = client.[reservation_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_path)(project_id, location, reservation_id)
    
        try:
            client.[delete_reservation](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_delete_reservation)(name=name)
            print(f"Deleted reservation: {name}")
        except NotFound:
            print(f"Reservation '{name}' not found.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
