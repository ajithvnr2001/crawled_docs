---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akamai/
title: Integrate Akamai with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:56:14.020006+00:00
---

# Integrate Akamai with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akamai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Akamai with Google SecOps

This document explains how to integrate Akamai with Google Security Operations.

## Use cases

The Akamai integration uses Google SecOps capabilities to support the following use cases:

  * **Automate threat blocking at the edge** : Add malicious IP addresses, CIDR blocks, autonomous system numbers, geographic locations, TLS fingerprints, or file hashes identified during investigations to Akamai client lists or network lists to block threats at the network edge.

  * **Manage dynamic access control and allowlists** : Remove benign indicators or expired entries from Akamai client lists and network lists when false positives are resolved or temporary restrictions expire.

  * **Deploy policy updates across environments** : Activate updated client lists and network lists in Akamai staging or production environments directly from automated playbooks and notify stakeholders of activation events.

  * **Audit edge security lists** : Retrieve metadata, item contents, and environment activation statuses for Akamai client lists and network lists to enrich security investigations and verify current enforcement states.




## Before you begin

Before you configure the Akamai integration in Google SecOps, complete the following prerequisite steps:

  1. Create Akamai EdgeGrid API credentials for your Google SecOps instance.

  2. Configure the required API permissions in Akamai for the actions you plan to run.




### Create Akamai EdgeGrid API credentials

The Akamai integration authenticates with the Akamai API using EdgeGrid credentials. Provision a dedicated API client in Akamai Control Center and collect the following credential values required for the integration parameters:

  * `Host` (the base hostname URL for your Akamai API client)
  * `Client Token`
  * `Client Secret`
  * `Access Token`



### Configure API permissions (least privilege)

Grant the Akamai API client only the API service permissions required for the specific actions you plan to run and verify that the API client's access control group scope includes the target client lists and network lists.

**Note:** Grant `Read-Only` access to **Network Lists API v2** to test integration connectivity and run the **Ping** action, even if you only use client list actions.

Refer to the minimal API permissions for Akamai actions in the following table:

Action Name | Akamai API Service | Required Access Level | Endpoint Scope  
---|---|---|---  
**Activate Client List** | Client Lists API v1 and v2 | `Read-Write` | Resolves client list identifiers using `GET /client-list/v1/lists` and activates the target list using `POST /client-list/v2/lists/{listId}/activations`.  
**Activate Network List** | Network Lists API v2 | `Read-Write` | Resolves network list identifiers using `GET /network-list/v2/network-lists` and activates the target list using `POST /network-list/v2/network-lists/{networkListId}/environments/{environment}/activate`.  
**Add Items To Client List** | Client Lists API v1 | `Read-Write` | Retrieves client lists for validation using `GET /client-list/v1/lists` and appends items using `POST /client-list/v1/lists/{listId}/items`.  
**Add Items To Network List** | Network Lists API v2 | `Read-Write` | Resolves network list identifiers using `GET /network-list/v2/network-lists` and appends items using `POST /network-list/v2/network-lists/{networkListId}/append`.  
**Get Client Lists** | Client Lists API v1 | `Read-Only` | Retrieves client lists and their items using `GET /client-list/v1/lists`.  
**Get Network Lists** | Network Lists API v2 | `Read-Only` | Retrieves network lists, list items, and environment activation statuses using `GET /network-list/v2/network-lists`, `GET /network-list/v2/network-lists/{networkListId}`, and `GET /network-list/v2/network-lists/{networkListId}/environments/{environment}/status`.  
**Ping** | Network Lists API v2 | `Read-Only` | Validates API connectivity and credentials using `GET /network-list/v2/network-lists?limit=1`.  
**Remove Items From Client List** | Client Lists API v1 | `Read-Write` | Retrieves client lists for validation using `GET /client-list/v1/lists` and deletes items using `POST /client-list/v1/lists/{listId}/items`.  
**Remove Items From Network List** | Network Lists API v2 | `Read-Write` | Resolves network list identifiers using `GET /network-list/v2/network-lists` and removes individual elements using `DELETE /network-list/v2/network-lists/{networkListId}/elements`.  
  
## Integration parameters

The Akamai integration requires the following parameters:

Parameter | Description  
---|---  
`Host` | Required. The base URL of the Akamai API instance, including the `https://` scheme, such as `https://akab-example.luna.akamaiapis.net`. The default value is `https://{host}`.  
`Client Token` | Required. The client token for your Akamai EdgeGrid API client.  
`Client Secret` | Required. The client secret for your Akamai EdgeGrid API client.  
`Access Token` | Required. The access token for your Akamai EdgeGrid API client.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Akamai server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Run a manual action in your case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action). 

### Activate Client List

Use the **Activate Client List** action to activate a specific client list in your Akamai staging or production environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Activate Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to activate. Matching is case-sensitive. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Client List ID` | Optional. The unique identifier of the client list to activate. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Environment` | Optional. The target Akamai environment for the client list activation. The possible values are as follows:

  * `Production`
  * `Staging`

The default value is `Production`.  
`Comment` | Optional. A comment describing the purpose of the client list activation.  
`Notification Recipients` | Optional. A comma-separated list of email addresses to notify when the client list activation completes.  
  
#### Action outputs

The **Activate Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Activate Client List** action:
    
    
    {
      "action": "ACTIVATE",
      "activations": {
        "STAGING": {
          "activationId": 3797405,
          "activationStatus": "PENDING_ACTIVATION"
        }
      },
      "comments": "Activating 235466",
      "createDate": "2026-02-12T15:12:07.952+00:00",
      "createdBy": "4wksaj3wyt23jt2i",
      "listId": "235466_GOOGLESECOPSCLIENTLIST1",
      "notificationRecipients": [
        "12345@email.com"
      ],
      "version": 14
    }
    

##### Output messages

The **Activate Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully activated the client list in Akamai.` | The action succeeded.  
`Error executing action "Activate Client List". Reason: Provide a value in "Client List Name" or "Client List ID" parameter.` | The action failed. Provide a valid identifier in either the `Client List Name` or `Client List ID` parameter.  
`Error executing action "Activate Client List". Reason: "CLIENT_LIST_IDENTIFIER" client list wasn't found in Akamai.` | The action failed. Verify that the specified client list name or ID exists in Akamai and that the name matches the exact case if searching by `Client List Name`.  
`Error executing action "Activate Client List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify that the target client list has items ready for activation, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Activate Client List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Activate Network List

Use the **Activate Network List** action to activate a specific network list in your Akamai staging or production environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Activate Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to activate. Matching is case-sensitive. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Network List ID` | Optional. The unique identifier of the network list to activate. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Environment` | Optional. The target Akamai environment for the network list activation. The possible values are as follows:

  * `Production`
  * `Staging`

The default value is `Production`.  
`Comment` | Optional. A comment describing the purpose of the network list activation.  
`Notification Recipients` | Optional. A comma-separated list of email addresses to notify when the network list activation completes.  
  
#### Action outputs

The **Activate Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Activate Network List** action:
    
    
    {
      "activationId": 12345,
      "activationComments": "Allow IPs of new employees who joined this week",
      "activationStatus": "PENDING_ACTIVATION",
      "syncPoint": 5,
      "uniqueId": "25614_GENERALLIST",
      "fast": false,
      "dispatchCount": 1,
      "links": {
        "appendItems": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
          "method": "POST"
        },
        "retrieve": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
        },
        "statusInProduction": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
        },
        "statusInStaging": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
        },
        "syncPointHistory": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
        },
        "update": {
          "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
          "method": "PUT"
        },
        "activationDetails": {
          "href": "/network-list/v2/network-lists/activations/12345/"
        }
      }
    }
    

##### Output messages

The **Activate Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully activated the network list in Akamai.` | The action succeeded.  
`Error executing action "Activate Network List". Reason: Provide a value in "Network List Name" or "Network List ID" parameter.` | The action failed. Provide a valid identifier in either the `Network List Name` or `Network List ID` parameter.  
`Error executing action "Activate Network List". Reason: "NETWORK_LIST_IDENTIFIER" network list wasn't found in Akamai.` | The action failed. Verify that the specified network list name or ID exists in Akamai and that the name matches the exact case if searching by `Network List Name`.  
`Error executing action "Activate Network List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify that your API credentials have write access to the Network Lists API, or review your input parameters.  
  
##### Script result

The following table lists the value for the script result output when using the **Activate Network List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Items To Client List

Use the **Add Items To Client List** action to add one or more items (such as IP addresses, geographic locations, autonomous system numbers, TLS fingerprints, or file hashes) to an existing client list in Akamai.

The action processes each item individually and reports a `status` of `added`, `duplicated` (if the item is already present on the list), or `failed` in the JSON result. Adding items updates the client list in Akamai, but changes don't take effect at the Akamai edge until you run the **Activate Client List** action for the target environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Items To Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to update. Matching is case-insensitive. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Client List ID` | Optional. The unique identifier of the client list to update. Matching is case-insensitive. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Item Value` | Required. A comma-separated list of item values to add to the client list.  
`Item Description` | Optional. A description to associate with the added items.  
`Item Expiration Date` | Optional. The expiration date for the added items in ISO 8601 format, such as `YYYY-MM-DDTHH:MM:SSZ` or `YYYY-MM-DDTHH:MM:SS+00:00`.  
`Item Tags` | Optional. A comma-separated list of tags to associate with the added items.  
  
#### Action outputs

The **Add Items To Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Add Items To Client List** action:
    
    
    [
      {
        "createDate": "2026-03-20T09:54:11.410+00:00",
        "createdBy": "4wksaj3wyt23jt2i",
        "description": "Blocked IP indicator",
        "expirationDate": "2026-04-05T19:29:02.320+00:00",
        "tags": [],
        "type": "IP",
        "updateDate": "2026-03-20T09:54:11.410+00:00",
        "updatedBy": "4wksaj3wyt23jt2i",
        "value": "192.0.2.1",
        "status": "added"
      },
      {
        "value": "192.0.2.3",
        "status": "duplicated"
      },
      {
        "value": "192.0.2.TT",
        "status": "failed",
        "error": "Validation failed: append[0].value: Item of type IP has an invalid value 192.0.2.TT"
      }
    ]
    

##### Output messages

The **Add Items To Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated client list in Akamai.` | The action succeeded. All specified items were either added to the client list (`"status": "added"`) or already existed on the list (`"status": "duplicated"`).  
`One or more items were not added. See JSON results for details.` | The action failed to add one or more specified items (`"status": "failed"`). If at least one item in the batch was added or already existed on the list, `is_success` remains `true`. If all items failed, `is_success` is `false`. Review the JSON result output to inspect the `error` details for each failed item, and verify that each value in the `Item Value` parameter matches the data type of the target client list.  
`Error executing action "Add Items To Client List". Reason: provide a value in "Client List Name" or "Client List ID" parameter.` | The action failed. Provide a valid identifier in either the `Client List Name` or `Client List ID` parameter.  
`Error executing action "Add Items To Client List". Reason: "CLIENT_LIST_IDENTIFIER" client list wasn't found in Akamai.` | The action failed. Verify that the specified client list name or ID exists in Akamai and that your API credentials have permission to access client lists.  
`Error executing action "Add Items To Client List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify that the `Item Expiration Date` parameter uses a valid ISO 8601 format, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Items To Client List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Items To Network List

Use the **Add Items To Network List** action to append one or more items (such as IP addresses, CIDR blocks, or geographic locations) to an existing network list in Akamai.

Adding items updates the network list in Akamai, but changes don't take effect at the Akamai edge until you run the **Activate Network List** action for the target environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Items To Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to update. Matching is case-sensitive. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Network List ID` | Optional. The unique identifier of the network list to update. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Items` | Required. A comma-separated list of items to add to the network list.  
  
#### Action outputs

The **Add Items To Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Add Items To Network List** action:
    
    
    {
      "networkListType": "networkListResponse",
      "accessControlGroup": "KSD\nwith ION 3-13H1234",
      "name": "General List",
      "elementCount": 3011,
      "readOnly": false,
      "shared": false,
      "syncPoint": 22,
      "type": "IP",
      "uniqueId": "25614_GENERALLIST",
      "links": {
        "activateInProduction": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
          "method": "POST"
        },
        "activateInStaging": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
          "method": "POST"
        },
        "appendItems": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST",
          "method": "POST"
        },
        "retrieve": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST"
        },
        "statusInProduction": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
        },
        "statusInStaging": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
        },
        "update": {
          "href": "/network-list/v2/network-lists/25614_GENERALLIST",
          "method": "PUT"
        }
      }
    }
    

##### Output messages

The **Add Items To Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated network list 'NETWORK_LIST_IDENTIFIER' in Akamai.` | The action succeeded.  
`Failed to update network list 'NETWORK_LIST_IDENTIFIER' in Akamai.` | The action failed. Verify that the values in the `Items` parameter are valid for the target network list type and that the list isn't read-only.  
`Error executing action "Add Items To Network List". Reason: Provide a value in "Network List Name" or "Network List ID" parameter.` | The action failed. Provide a valid identifier in either the `Network List Name` or `Network List ID` parameter.  
`Error executing action "Add Items To Network List". Reason: "NETWORK_LIST_IDENTIFIER" network list wasn't found in Akamai.` | The action failed. Verify that the specified network list name or ID exists in Akamai and that the name matches the exact case if searching by `Network List Name`.  
`Error executing action "Add Items To Network List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify the format of the `Items` parameter, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Items To Network List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Client Lists

Use the **Get Client Lists** action to retrieve metadata and item contents for client lists configured in Akamai.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Client Lists** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. A comma-separated list of client list names to retrieve. Matching is case-sensitive. If you don't provide `Client List Name` or `Client List ID`, the action returns all available client lists up to the specified limit.  
`Client List ID` | Optional. A comma-separated list of client list IDs to retrieve. Matching is case-insensitive. If you don't provide `Client List Name` or `Client List ID`, the action returns all available client lists up to the specified limit.  
`Include Items` | Optional. If selected, the action returns information about the items inside each matching client list. The action returns this information only when you provide a value in either `Client List Name` or `Client List ID`.  
`Type` | Optional. The type of client list to search for. If set to `Select One`, the action searches across all client list types. The possible values are as follows:

  * `Select One`
  * `IP`
  * `GEO`
  * `ASN`
  * `TLS Fingerprint`
  * `File Hash`

The default value is `Select One`.  
`Max Client Lists To Return` | Required. The maximum number of client lists to return. The maximum value is `100`. The default value is `100`.  
`Max Client List Items To Return` | Required. The maximum number of items to return for each client list. The maximum value is `100`. The default value is `100`.  
  
#### Action outputs

The **Get Client Lists** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Client Lists** action:
    
    
    [
      {
        "contractId": "K-0N7RAK71",
        "createDate": "2023-04-05T18:20:42.090+00:00",
        "createdBy": "jsmith",
        "deprecated": false,
        "groupId": 32145,
        "groupName": "Acme IT Group",
        "items": [
          {
            "createDate": "2023-04-05T18:20:42.892+00:00",
            "createdBy": "jkowalski",
            "description": "Canada - North America",
            "expirationDate": "2023-12-31T23:59:19.700+00:00",
            "productionStatus": "INACTIVE",
            "stagingStatus": "INACTIVE",
            "tags": [
              "allowlist1"
            ],
            "type": "GEO",
            "updateDate": "2023-04-05T18:20:42.892+00:00",
            "updatedBy": "mrossi",
            "value": "CA"
          }
        ],
        "itemsCount": 3,
        "listId": "1234_NORTHAMERICAGEOALLOWLIST",
        "listType": "CL",
        "name": "NorthAmericaGeoAllowlist",
        "notes": "GEO code allowlist",
        "productionActivationStatus": "INACTIVE",
        "readOnly": false,
        "shared": false,
        "stagingActivationStatus": "INACTIVE",
        "tags": [
          "allowlist2"
        ],
        "type": "GEO",
        "updateDate": "2023-04-05T18:20:42.090+00:00",
        "updatedBy": "jdupont",
        "version": 1
      }
    ]
    

##### Output messages

The **Get Client Lists** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned client lists from Akamai.` | The action succeeded.  
`No clients lists were found for the provided criteria in Akamai.` | The action failed. Verify that the specified client list names or IDs exist in Akamai, match the selected `Type` filter, and use the exact case when searching by `Client List Name`.  
`Error executing action "Get Client Lists". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify that the maximum return parameters are between `1` and `100`, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Client Lists** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Network Lists

Use the **Get Network Lists** action to retrieve metadata, item contents, and activation statuses for network lists configured in Akamai.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Network Lists** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. A comma-separated list of network list names to retrieve. Matching is case-sensitive. If you don't provide `Network List Name` or `Network List ID`, the action returns all available network lists up to the specified limit.  
`Network List ID` | Optional. A comma-separated list of network list IDs to retrieve. Matching is case-insensitive. If you don't provide `Network List Name` or `Network List ID`, the action returns all available network lists up to the specified limit.  
`Include Items` | Optional. If selected, the action returns the items contained inside each network list.  
`Include Activation Status` | Optional. If selected, the action returns the activation status for each matching network list. The action returns this information only when you provide a value in either `Network List Name` or `Network List ID`.  
`Activation Environment` | Optional. The environment for which to return the network list activation status when you select `Include Activation Status` and provide a specific `Network List Name` or `Network List ID`. The possible values are as follows:

  * `Both`
  * `Production`
  * `Staging`

The default value is `Both`.  
`Max Network Lists To Return` | Required. The maximum number of network lists to return. The maximum value is `100`. The default value is `100`.  
`Max Network List Items To Return` | Required. The maximum number of items to return for each network list. The maximum value is `100`. The default value is `100`.  
  
#### Action outputs

The **Get Network Lists** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Network Lists** action:
    
    
    [
      {
        "networkListType": "networkListResponse",
        "accessControlGroup": "KSD\nwith ION 3-13H1234",
        "name": "General List",
        "elementCount": 3011,
        "readOnly": false,
        "shared": false,
        "syncPoint": 22,
        "type": "IP",
        "uniqueId": "25614_GENERALLIST",
        "links": {
          "activateInProduction": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
            "method": "POST"
          },
          "activateInStaging": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
            "method": "POST"
          },
          "appendItems": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST",
            "method": "POST"
          },
          "retrieve": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST"
          },
          "statusInProduction": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
          },
          "statusInStaging": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
          },
          "update": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST",
            "method": "PUT"
          }
        },
        "Activation_STAGING": {
          "activationId": 12345,
          "activationComments": "Allow IPs of new employees who joined this week",
          "activationStatus": "PENDING_ACTIVATION",
          "syncPoint": 5,
          "uniqueId": "25614_GENERALLIST",
          "fast": false,
          "dispatchCount": 1,
          "links": {
            "appendItems": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
              "method": "POST"
            },
            "retrieve": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
            },
            "statusInProduction": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
            },
            "statusInStaging": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
            },
            "syncPointHistory": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
            },
            "update": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
              "method": "PUT"
            },
            "activationDetails": {
              "href": "/network-list/v2/network-lists/activations/12345/"
            }
          }
        },
        "Activation_PRODUCTION": {
          "activationId": 12345,
          "activationComments": "Allow IPs of new employees who joined this week",
          "activationStatus": "PENDING_ACTIVATION",
          "syncPoint": 5,
          "uniqueId": "25614_GENERALLIST",
          "fast": false,
          "dispatchCount": 1,
          "links": {
            "appendItems": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/append",
              "method": "POST"
            },
            "retrieve": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST"
            },
            "statusInProduction": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
            },
            "statusInStaging": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
            },
            "syncPointHistory": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST/sync-points/5/history"
            },
            "update": {
              "href": "/networklist-api/rest/v2/network-lists/25614_GENERALLIST",
              "method": "PUT"
            },
            "activationDetails": {
              "href": "/network-list/v2/network-lists/activations/12345/"
            }
          }
        }
      }
    ]
    

##### Output messages

The **Get Network Lists** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned network lists from Akamai.` | The action succeeded.  
`No network lists were found for the provided criteria in Akamai.` | The action failed. Verify that the specified network list names or IDs exist in Akamai and that the names match the exact case when searching by `Network List Name`.  
`Error executing action "Get Network Lists". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify that the maximum return parameters are between `1` and `100`, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Network Lists** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test connectivity and validate your authentication credentials with the Akamai server.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Akamai server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Akamai server! Error is ERROR_REASON` | The action failed. Verify that the `Host` URL is reachable, check that your Akamai EdgeGrid tokens and secret are valid, and confirm that the API client has access to the Network Lists API.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Items From Client List

Use the **Remove Items From Client List** action to remove one or more items from an existing client list in Akamai.

The action processes each item individually and reports a `status` of `removed`, `doesn't exist` (if the item isn't present on the list), or `failed` in the JSON result. Removing items updates the client list in Akamai, but changes don't take effect at the Akamai edge until you run the **Activate Client List** action for the target environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Items From Client List** action requires the following parameters:

Parameter | Description  
---|---  
`Client List Name` | Optional. The name of the client list to update. Matching is case-insensitive. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Client List ID` | Optional. The unique identifier of the client list to update. Matching is case-insensitive. You must provide either `Client List Name` or `Client List ID`. If you provide both, the action uses `Client List ID`.  
`Item Value` | Required. A comma-separated list of item values to remove from the client list.  
  
#### Action outputs

The **Remove Items From Client List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Remove Items From Client List** action:
    
    
    [
      {
        "value": "192.0.2.1",
        "status": "doesn't exist"
      },
      {
        "value": "192.0.2.4",
        "status": "removed"
      },
      {
        "value": "192.0.2.4E",
        "status": "failed",
        "error": "Validation failed: delete[0].value: Item of type IP has an invalid value 192.0.2.4E"
      }
    ]
    

##### Output messages

The **Remove Items From Client List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated client list in Akamai.` | The action succeeded. All specified items were either removed from the client list (`"status": "removed"`) or were already absent from the list (`"status": "doesn't exist"`).  
`One or more items were not removed. See JSON results for details.` | The action failed to remove one or more specified items (`"status": "failed"`). If at least one item in the batch had a status of `removed` or `doesn't exist`, `is_success` remains `true`. If all items failed, `is_success` is `false`. Review the JSON result output to inspect the `error` details for each failed item, and verify that each value in the `Item Value` parameter is valid for the target client list.  
`Error executing action "Remove Items From Client List". Reason: provide a value in "Client List Name" or "Client List ID" parameter.` | The action failed. Provide a valid identifier in either the `Client List Name` or `Client List ID` parameter.  
`Error executing action "Remove Items From Client List". Reason: "CLIENT_LIST_IDENTIFIER" client list wasn't found in Akamai.` | The action failed. Verify that the specified client list name or ID exists in Akamai and that your API credentials have permission to access client lists.  
`Error executing action "Remove Items From Client List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify the format of the `Item Value` parameter, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Items From Client List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Items From Network List

Use the **Remove Items From Network List** action to remove one or more items from an existing network list in Akamai.

Removing items updates the network list in Akamai, but changes don't take effect at the Akamai edge until you run the **Activate Network List** action for the target environment.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Items From Network List** action requires the following parameters:

Parameter | Description  
---|---  
`Network List Name` | Optional. The name of the network list to update. Matching is case-sensitive. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Network List ID` | Optional. The unique identifier of the network list to update. You must provide either `Network List Name` or `Network List ID`. If you provide both, the action uses `Network List ID`.  
`Items` | Required. A comma-separated list of items to remove from the network list.  
  
#### Action outputs

The **Remove Items From Network List** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Remove Items From Network List** action:
    
    
    [
      {
        "networkListType": "networkListResponse",
        "accessControlGroup": "KSD\nwith ION 3-13H1234",
        "name": "General List",
        "elementCount": 3010,
        "readOnly": false,
        "shared": false,
        "syncPoint": 23,
        "type": "IP",
        "uniqueId": "25614_GENERALLIST",
        "links": {
          "activateInProduction": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/activate",
            "method": "POST"
          },
          "activateInStaging": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/activate",
            "method": "POST"
          },
          "appendItems": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST",
            "method": "POST"
          },
          "retrieve": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST"
          },
          "statusInProduction": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/PRODUCTION/status"
          },
          "statusInStaging": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST/environments/STAGING/status"
          },
          "update": {
            "href": "/network-list/v2/network-lists/25614_GENERALLIST",
            "method": "PUT"
          }
        }
      }
    ]
    

##### Output messages

The **Remove Items From Network List** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated network list in Akamai.` | The action succeeded. When you specify multiple items in the `Items` parameter, the action succeeds if it removes at least one item from the network list.  
`None of the provided items were found in the network list in Akamai.` | The action failed to remove any of the specified items. Verify that the values specified in the `Items` parameter exist in the target network list.  
`No valid items provided for removal. Please provide a comma-separated list of items.` | The action failed. Provide one or more valid, comma-separated values in the `Items` parameter.  
`Error executing action "Remove Items From Network List". Reason: provide a value in "Network List Name" or "Network List ID" parameter.` | The action failed. Provide a valid identifier in either the `Network List Name` or `Network List ID` parameter.  
`Error executing action "Remove Items From Network List". Reason: "NETWORK_LIST_IDENTIFIER" network list wasn't found in Akamai.` | The action failed. Verify that the specified network list name or ID exists in Akamai and that the name matches the exact case if searching by `Network List Name`.  
`Error executing action "Remove Items From Network List". Reason: ERROR_REASON` | The action failed. Check the connection to the Akamai server, verify the format of the `Items` parameter, or review your API credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Items From Network List** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
