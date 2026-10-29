---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservationgroup-create/
title: Create a reservation group \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T10:08:37.764937+00:00
---

# Create a reservation group  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-reservationservice-reservationgroup-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create a reservation group Stay organized with collections  Save and categorize content based on your preferences. 

Create a reservation group in a specific project and location. A reservation group is a container for BigQuery reservations.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.bigquery.reservation.v1.[CreateReservationGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.CreateReservationGroupRequest.html);
    import com.google.cloud.bigquery.reservation.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html);
    import com.google.cloud.bigquery.reservation.v1.[ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html);
    import java.io.IOException;
    
    public class CreateReservationGroup {
    
      /**
       * Creates a new BigQuery reservation group in a given project and location. A reservation group
       * is a container for reservations.
       *
       * @param projectId The Google Cloud project ID (for example, "example-project-id").
       * @param location The geographic location of the reservation group (for example, "us-central1").
       * @param reservationGroupId The ID of the reservation group to create (for example,
       *     "example-reservation-group").
       */
      public static void createReservationGroup(
          String projectId, String location, String reservationGroupId) {
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html).of(projectId, location);
        [ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html) reservationGroup = [ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html).newBuilder().build();
    
        [CreateReservationGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.CreateReservationGroupRequest.html) request =
            [CreateReservationGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.CreateReservationGroupRequest.html).newBuilder()
                .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.LocationName.html#com_google_cloud_bigquery_reservation_v1_LocationName_toString__)())
                .[setReservationGroupId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.CreateReservationGroupRequest.Builder.html#com_google_cloud_bigquery_reservation_v1_CreateReservationGroupRequest_Builder_setReservationGroupId_java_lang_String_)(reservationGroupId)
                .setReservationGroup(reservationGroup)
                .build();
    
        try ([ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html) client = [ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html).create()) {
          [ReservationGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html) response = client.createReservationGroup(request);
          System.out.printf("Created reservation group: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationGroup.html#com_google_cloud_bigquery_reservation_v1_ReservationGroup_getName__)());
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) err) {
          System.err.printf(
              "error: reservation group '%s' already exists in location '%s' for project '%s': %s%n",
              reservationGroupId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
        } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) | IOException err) {
          System.err.printf(
              "error: failed to create reservation group '%s' in location '%s' for project '%s': %s%n",
              reservationGroupId, location, projectId, err.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
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
     * Creates a new reservation group.
     * A reservation group is a container for reservations. This can be useful for
     * managing reservations for different teams or workloads.
     *
     * @param projectId Google Cloud project ID, for example 'example-project-id'.
     * @param location The Google Cloud location where the reservation group will be created, for example 'us-central1'.
     * @param reservationGroupId The ID to use for the reservation group, for example 'example-reservation-group'.
     */
    async function createReservationGroup(projectId,
      location = 'us-central1',
      reservationGroupId = 'example-group-reservation',) {
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        reservationGroupId,
        reservationGroup: {},
      };
    
      try {
        const [reservationGroup] = await client.createReservationGroup(request);
        console.log(`Created reservation group: ${reservationGroup.name}`);
      } catch (err) {
        if (err.code === status.ALREADY_EXISTS) {
          console.log(
            `Reservation group '${reservationGroupId}' already exists in project '${projectId}' in location '${location}'.`,
          );
        } else {
          console.error('Error creating reservation group:', err);
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.api_core import exceptions
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    
    client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)()
    
    
    def create_reservation_group(project_id: str, location: str, reservation_group_id: str):
        """Creates a reservation group.
    
        A reservation group is a container for reservations.
    
        Args:
            project_id: The Google Cloud project ID.
            location: The geographic location where the reservation group should be created.
            reservation_group_id: The ID of the reservation group to create.
                It must only contain lower case alphanumeric characters or dashes.
                It must start with a letter and must not end with a dash.
                Its maximum length is 64 characters.
        """
        parent = f"projects/{project_id}/locations/{location}"
        reservation_group = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[types](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.html).[ReservationGroup](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.ReservationGroup.html)()
    
        request = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[CreateReservationGroupRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.CreateReservationGroupRequest.html)(
            parent=parent,
            reservation_group_id=reservation_group_id,
            reservation_group=reservation_group,
        )
    
        try:
            response = client.[create_reservation_group](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_create_reservation_group)(request=request)
            print(f"Created reservation group: {response.name}")
        except exceptions.AlreadyExists:
            full_reservation_group_name = client.[reservation_group_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_reservation_group_path)(
                project_id, location, reservation_group_id
            )
            print(f"Reservation group '{full_reservation_group_name}' already exists.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
