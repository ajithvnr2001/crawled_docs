---
url: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/
title: Network Security API \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:44:10.431397+00:00
---

# Network Security API  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)
  * [ Reference ](https://docs.cloud.google.com/ull-solution/participants/apis)



Send feedback 

#  Network Security API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: networksecurity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1>
  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networksecurity.googleapis.com`



## REST Resource: [v1beta1.organizations.locations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations/list)` |  `GET /v1beta1/{name=organizations/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.organizations.locations.operations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations.operations/cancel)` |  `POST /v1beta1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations.operations/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations.operations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/organizations.locations.operations/list)` |  `GET /v1beta1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.ullMirroringCollectors](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors)

Methods  
---  
`[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/ullMirroringCollectors`   
Creates a new UllMirroringCollector in a given project and location.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*}`   
Deletes a single UllMirroringCollector.  
`[disable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/disable)` |  `POST /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*}:disable`   
Disables a single UllMirroringCollector.  
`[enable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/enable)` |  `POST /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*}:enable`   
Enables a single UllMirroringCollector.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/get)` |  `GET /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*}`   
Gets details of a single UllMirroringCollector.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/ullMirroringCollectors`   
Lists UllMirroringCollectors in a given project and location.  
`[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/patch)` |  `PATCH /v1beta1/{ullMirroringCollector.name=projects/*/locations/*/ullMirroringCollectors/*}`   
Updates a single UllMirroringCollector.  
  
## REST Resource: [v1beta1.projects.locations.ullMirroringCollectors.rules](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules)

Methods  
---  
`[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/ullMirroringCollectors/*}/rules`   
Creates a new UllMirroringCollectorRule for a given UllMirroringCollector.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Deletes a single UllMirroringCollectorRule for a given UllMirroringCollector.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/get)` |  `GET /v1beta1/{name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Gets details of a single UllMirroringCollectorRule.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/ullMirroringCollectors/*}/rules`   
Lists UllMirroringCollectorRules for a given UllMirroringCollector.  
`[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/patch)` |  `PATCH /v1beta1/{ullMirroringCollectorRule.name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Updates a single UllMirroringCollectorRule.  
  
## REST Resource: [v1.organizations.locations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations/get)` |  `GET /v1/{name=organizations/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations/list)` |  `GET /v1/{name=organizations/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.organizations.locations.operations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations.operations/cancel)` |  `POST /v1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations.operations/delete)` |  `DELETE /v1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations.operations/get)` |  `GET /v1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/organizations.locations.operations/list)` |  `GET /v1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.ullMirroringCollectors](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors)

Methods  
---  
`[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/create)` |  `POST /v1/{parent=projects/*/locations/*}/ullMirroringCollectors`   
Creates a new UllMirroringCollector in a given project and location.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/delete)` |  `DELETE /v1/{name=projects/*/locations/*/ullMirroringCollectors/*}`   
Deletes a single UllMirroringCollector.  
`[disable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/disable)` |  `POST /v1/{name=projects/*/locations/*/ullMirroringCollectors/*}:disable`   
Disables a single UllMirroringCollector.  
`[enable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/enable)` |  `POST /v1/{name=projects/*/locations/*/ullMirroringCollectors/*}:enable`   
Enables a single UllMirroringCollector.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/get)` |  `GET /v1/{name=projects/*/locations/*/ullMirroringCollectors/*}`   
Gets details of a single UllMirroringCollector.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/list)` |  `GET /v1/{parent=projects/*/locations/*}/ullMirroringCollectors`   
Lists UllMirroringCollectors in a given project and location.  
`[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors/patch)` |  `PATCH /v1/{ullMirroringCollector.name=projects/*/locations/*/ullMirroringCollectors/*}`   
Updates a single UllMirroringCollector.  
  
## REST Resource: [v1.projects.locations.ullMirroringCollectors.rules](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules)

Methods  
---  
`[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules/create)` |  `POST /v1/{parent=projects/*/locations/*/ullMirroringCollectors/*}/rules`   
Creates a new UllMirroringCollectorRule for a given UllMirroringCollector.  
`[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules/delete)` |  `DELETE /v1/{name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Deletes a single UllMirroringCollectorRule for a given UllMirroringCollector.  
`[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules/get)` |  `GET /v1/{name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Gets details of a single UllMirroringCollectorRule.  
`[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules/list)` |  `GET /v1/{parent=projects/*/locations/*/ullMirroringCollectors/*}/rules`   
Lists UllMirroringCollectorRules for a given UllMirroringCollector.  
`[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1/projects.locations.ullMirroringCollectors.rules/patch)` |  `PATCH /v1/{ullMirroringCollectorRule.name=projects/*/locations/*/ullMirroringCollectors/*/rules/*}`   
Updates a single UllMirroringCollectorRule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
