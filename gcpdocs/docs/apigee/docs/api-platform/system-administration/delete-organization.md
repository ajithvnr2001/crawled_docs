---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/delete-organization/
title: Delete an Apigee organization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:13.348789+00:00
---

# Delete an Apigee organization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/delete-organization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Delete an Apigee organization Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page explains how to fully delete an Apigee organization from a Google Cloud project, including the follow-up steps needed to release networking resources that Apigee does not clean up on its own. The post-deletion cleanup you need to perform depends on how the organization was provisioned: 

  * **Organizations provisioned with VPC peering enabled** also have a Service Networking VPC peering connection between your VPC and the Apigee tenant network. That connection, and any reserved peering range and VPC network associated with it, remain in place after you delete the organization and must be cleaned up separately if you no longer need them. See Follow up: organizations provisioned with VPC peering.

  * **Organizations provisioned with VPC peering disabled** use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) instead of a Service Networking connection, so there is no producer peering to remove. You must still delete the northbound Private Service Connect load balancer that you created when you provisioned the organization — forwarding rule, target HTTPS proxy, URL map, backend service, PSC network endpoint group, SSL certificate, and reserved IP address — or the forwarding rule and reserved IP address continue to incur charges. See Follow up: organizations provisioned without VPC peering.




Before you begin shows how to determine which category your organization falls into. 

**Warning:** Deleting an Apigee organization is destructive. All resources within the organization — including API proxies, environments, environment groups, developers, apps, API products, keystores, key-value maps, and instances — are removed. For paid organizations, the delete is a soft-deletion with a retention window (see Retention window and re-provisioning); for evaluation organizations, the delete is immediate. See [organizations.delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete) for the full behavior. The deletion cannot be undone after the retention window elapses. 

## Before you begin

### Required IAM permissions

  * On the Apigee organization (typically APIGEE_PROJECT_ID): `apigee.organizations.delete`. This permission is included in the `roles/apigee.admin` role, which the [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles) guide describes as the only role that can create, delete, or update organizations.

  * Additionally, if your organization was provisioned with VPC peering enabled and you plan to clean up the Service Networking connection, VPC peering range, or VPC network as described in Follow up: organizations provisioned with VPC peering: on the project that owns the peered VPC network (the _network project_ , which might differ from your Apigee project in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) setup), `servicenetworking.services.deleteConnection`, `compute.globalAddresses.delete`, and `compute.networks.delete`.




### Delete dependent resources first

Before you delete the organization, delete the resources that Apigee requires you to remove first:

  * Delete all Apigee instances associated with the organization. See [Delete a managed instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#delete-a-managed-instance).

  * Delete all endpoint attachments associated with the organization. See [Deleting an endpoint attachment](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#deleting-an-endpoint-attachment).




### Back up any data you want to preserve

Back up any organization-scoped data or resources you might need later. After the retention window elapses, data stored in the organization is not recoverable. 

### Determine whether your organization uses VPC peering

The follow-up cleanup you need to do after deleting the organization depends on whether the organization was provisioned with VPC peering enabled. Read the organization's configuration with the [organizations.get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) API before you delete it: 
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION"

This and every other Apigee REST call on this page target the global `apigee.googleapis.com` endpoint. If your organization is in a data residency region, substitute the corresponding regional endpoint in every sample. 

**Important usage note for data residency:** To support data residency, when provisioning or using Apigee you must use a regional endpoint. For more information, see [Use regional endpoints for data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint). 

Look for the `disableVpcPeering` field in the response:

  * If the response contains `"disableVpcPeering": true`, the organization was provisioned without VPC peering. After you delete the organization, follow Follow up: organizations provisioned without VPC peering.

  * If the field is `false` or absent, the organization was provisioned with VPC peering. Record the following two additional values from the same response; you will need them during cleanup:

    * The `authorizedNetwork` field, which identifies the VPC network peered with Apigee. It appears in one of two forms: 
      * A full resource path `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`, which encodes both the network project and the network name. This form is used when the network lives in a different project from your Apigee organization — most commonly in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) setup, where the network is in the host project.
      * Just a network name (for example, `apigee-network`). When only the name is present, the network lives in the same Google Cloud project as your Apigee organization — treat that project (APIGEE_PROJECT_ID) as NETWORK_PROJECT_ID for the cleanup steps.
Note that `authorizedNetwork` is set only on VPC-peered organizations.
    * The name of the global address you originally reserved for the VPC peering range (for example, `apigee-range`). You reserved this address when you first provisioned the organization.

After you delete the organization, follow Follow up: organizations provisioned with VPC peering.




## Delete the Apigee organization

Call the [organizations.delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete) API to delete the organization. The call returns a long-running operation and, for evaluation organizations, performs an immediate deletion; for paid organizations (Subscription or Pay-as-you-go), it performs a soft-deletion subject to the retention window. 
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION"

To use the minimum (24-hour) retention window for a paid organization, append the `retention` query parameter: 
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION?retention=MINIMUM"

The response contains a long-running operation. You can poll it with [organizations.operations.get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations/get). 

## Follow up: organizations provisioned without VPC peering

If the organization's `disableVpcPeering` field is `true`, deleting the organization releases no Service Networking resources, because an organization provisioned without VPC peering never had a Service Networking connection, and there is no producer peering to remove. 

You must still delete the northbound [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) load balancer that you created in your own project when you provisioned the organization. These resources are not owned by Apigee, and `organizations.delete` releases none of them. Delete them in reverse dependency order: 

  1. Forwarding rule
  2. Target HTTPS proxy
  3. URL map
  4. Backend service
  5. PSC network endpoint group
  6. SSL certificate
  7. Reserved IP address

**Caution:** Leaving the forwarding rule and the reserved IP address in place continues to incur charges, and the reserved address continues to hold global IP quota against your project. The PSC network endpoint group is left pointing at a deleted service attachment and must be cleaned up explicitly. 

When the northbound cleanup is complete, proceed to Retention window and re-provisioning. 

## Follow up: organizations provisioned with VPC peering

**Important:** This topic only applies to organizations that were created with VPC peering enabled. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

Deleting the Apigee organization does not release the Service Networking VPC peering connection you established when the organization was provisioned. The connection remains on your VPC network, along with the reserved peering range and any VPC network you dedicated to the peering. If you no longer need these resources, complete the cleanup by following the canonical [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) and [Service Networking](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections) procedures. The rest of this section only supplies the values and warnings specific to an Apigee teardown. 

### Collect the values you need

The following cleanup steps reuse the same handful of values to plug into the procedures in the linked Service Networking and VPC guides. Determine each value once, then set it as a shell variable so you can copy the linked commands verbatim: 

  * **`NETWORK_PROJECT_ID`** — the project that owns the peered VPC network. This is not always the same as your Apigee service project: in a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) setup, the network lives in the host project. Derive it from the `authorizedNetwork` value you recorded in Determine whether your organization uses VPC peering:

    * If `authorizedNetwork` is a full resource path `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`, take NETWORK_PROJECT_ID from that path.
    * If `authorizedNetwork` is only a network name (for example, `apigee-network`), the network lives in the same project as the Apigee organization; use your Apigee project (APIGEE_PROJECT_ID).
  * **`NETWORK_NAME`** — the VPC network name (for example, `apigee-network`). Take it from the full path in `authorizedNetwork`, or use the bare value when `authorizedNetwork` is only a name.

  * **`APIGEE_RANGE_NAME`** — the name of the global address that was allocated for the VPC peering range (for example, `apigee-range`) when the organization was provisioned. You can see the reserved ranges attached to the peering in the `reservedPeeringRanges` list returned by `gcloud services vpc-peerings list`.

  * **`NETWORK_PROJECT_NUMBER`** — the numeric project number for `NETWORK_PROJECT_ID`. The Service Networking REST API requires the project number (not the project ID) in the `consumerNetwork` field:
        
        gcloud projects describe NETWORK_PROJECT_ID \
          --format="value(projectNumber)"




Whenever a linked procedure asks for a network, network project, or consumer network, substitute these values. 

### Warnings that apply to an Apigee teardown

**The Service Networking connection and the reserved peering range can be shared with other Google Cloud services.** Every Google Cloud service on the network that uses [Private Services Access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) — [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access), [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/networking), [AlloyDB](https://docs.cloud.google.com/alloydb/docs/configure-connectivity), [Filestore](https://docs.cloud.google.com/filestore/docs/networking/private-services-access), and Apigee — shares one Service Networking connection per VPC and can share allocated ranges within it. Deleting the connection removes producer peering for all of these services, and releasing a range takes back IP space they might still be using. 

Before you release either resource, use [How much of my allocation is being used?](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#how_much_of_my_allocation_is_being_used) in the Configure private services access guide to verify who is using it. If you cannot confirm that only Apigee used the resource, leave it in place.

### Complete the cleanup

Follow the linked procedures, substituting the variables from Collect the values you need: 

  * **Delete the Service Networking connection.** Follow [Delete a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#removing-connection). Because you already deleted the Apigee organization in Delete the Apigee organization, the guide's prerequisite of removing the service instance is satisfied for evaluation organizations, which are deleted immediately. For paid organizations the delete is a soft-deletion, and the connection delete succeeds only once the retention window has elapsed — see Retention window and re-provisioning, or delete the organization with `?retention=MINIMUM` to shorten the window to 24 hours. When the procedure asks for the network and network project, use `NETWORK_NAME` and `NETWORK_PROJECT_ID`; when the underlying [`services.connections.deleteConnection`](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/deleteConnection) REST call asks for `consumerNetwork`, use `projects/NETWORK_PROJECT_NUMBER/global/networks/NETWORK_NAME`.

  * **(Optional) Release the reserved peering range.** Follow [Delete an allocated IP address range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#deleting-allocation), using `APIGEE_RANGE_NAME` and `NETWORK_PROJECT_ID`. The reserved range is a customer-owned resource that persists after the Apigee organization and the Service Networking connection are deleted; leaving it in place does not disrupt any Google Cloud service.

  * **(Optional) Delete the VPC network.** If you routed northbound traffic through a managed instance group or an internal load balancer in this network, delete those resources first, or the network delete fails with a dependent-resource error: forwarding rule, target proxy, URL map, backend service, managed instance group, instance template, health check, firewall rules, and reserved address. Then follow [Delete a network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_a_network) in the VPC networks guide, using `NETWORK_NAME` and `NETWORK_PROJECT_ID`.


**Note:** If the connection delete fails with a "service producer resources are still in use" error, either another Private Services Access producer on this network is still holding the connection, or your Apigee organization is still within its retention window and its producer-side resources have not yet been fully released. In the first case, use [How much of my allocation is being used?](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#how_much_of_my_allocation_is_being_used) to identify which producer, and do not force the deletion. In the second case, wait for the retention window to elapse (or delete the organization with `?retention=MINIMUM` to shorten the window to 24 hours) before retrying. 

## Retention window and re-provisioning

As documented in the [organizations.delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/delete) reference: 

  * Apigee deletes evaluation organizations immediately.
  * Apigee soft-deletes paid organizations (Subscription or Pay-as-you-go) with a default 7-day retention window. During the retention window, you can restore the organization by filing a support ticket with Apigee. Passing `?retention=MINIMUM` on the delete request shortens the window to 24 hours.
  * You cannot recreate an Apigee organization in the same Google Cloud project during the retention window.



## What's next

Apigee references:

  * [Introduction to provisioning Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro)
  * [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options) (VPC peering vs. Private Service Connect)
  * [Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges)
  * [Using shared VPC networks](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs)



Service Networking and Private Services Access references:

  * [Private services access overview](https://docs.cloud.google.com/vpc/docs/private-services-access)
  * [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access)
  * [Getting started with Service Networking](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started)
  * [Service Networking API reference: `services.connections`](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections)
  * [Network Analyzer: Private services access IP address utilization summary](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization#psa-ip-allocation-ratio-summary)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
