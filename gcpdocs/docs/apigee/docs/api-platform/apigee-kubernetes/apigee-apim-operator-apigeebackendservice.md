---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/
title: Create an ApigeeBackendService \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:48:42.458284+00:00
---

# Create an ApigeeBackendService  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fapigee%2Fdocs%2Fapi-platform%2Fapigee-kubernetes%2Fapigee-apim-operator-apigeebackendservice%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#before-you-begin)
  * [Required roles](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#required-roles)
  * [Create the ApigeeBackendService Resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#create-the-apigeebackendservice-resource)
    * [Create an ApigeeBackendService](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#apigee-backend-service)
    * [Create a GCPTrafficExtension resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#gcp-traffic-extension)
  * [Next Steps](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#next-steps)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Was this helpful?
Send feedback 
#  Create an ApigeeBackendService Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#before-you-begin)
  * [Required roles](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#required-roles)
  * [Create the ApigeeBackendService Resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#create-the-apigeebackendservice-resource)
    * [Create an ApigeeBackendService](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#apigee-backend-service)
    * [Create a GCPTrafficExtension resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#gcp-traffic-extension)
  * [Next Steps](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice/#next-steps)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
This page describes how to create an `ApigeeBackendService` and the required traffic extension on the Google Kubernetes Engine (GKE) Gateway running in your cluster.
This approach is an alternative to using the `APIMExtensionPolicy` to identify the Apigee data plane as the Policy Decision Point (PDP) for the GKE Gateway. When you create an `ApigeeBackendService`, the Apigee Operator for Kubernetes automatically creates an `APIMExtensionPolicy` with the same name and namespace as the `ApigeeBackendService`. This is the backing `APIMExtensionPolicy`.
We recommend this approach if you create and manage [Cloud Load Balancing traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) and want to add Apigee as an extension in your [traffic extension](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcp-extensions) resource. You must use the `ApigeeBackendService` if the Apigee traffic extension works in conjunction with other traffic extensions.
## Before you begin
Before you begin this task, complete the following steps: 
  * Confirm that your GKE implementation uses GKE version 1.34.x or later.
  * Confirm that your GKE cluster has a Workload Identity configured. See [Create a workload identity](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#create-workload-identity) for the required steps.
  * Confirm that your cluster has a GKE Gateway configured and working. See [Deploying gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways) for more details. 
  * Install the Apigee Operator for Kubernetes. See [Install Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install) for installation instructions.


## Required roles
If you assigned the required roles to your service account as described in [ Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install#required-roles), no additional IAM roles or permissions are necessary to complete these tasks.
You can authorize actions on resources in your Google Kubernetes Engine cluster using the built-in role-based access control (RBAC) mechanism in Kubernetes. For more information, see [ Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
## Create the ApigeeBackendService Resource
To configure a traffic service extension on your GKE Gateway, create two main resources: 
  * **ApigeeBackendService:** This custom resource specifies the Apigee data plane as the Policy Decision Point (PDP) and configures network details for Private Service Connect Network Endpoint Groups (NEGs).
  * **GCPTrafficExtension:** This GKE Gateway API resource defines the extension chain, including how traffic directs to the ApigeeBackendService.


### Create an `ApigeeBackendService`
The `ApigeeBackendService` resource specifies the Apigee data plane as the PDP for a `GCPTrafficExtension`. 
To create an `ApigeeBackendService`: 
  1. Create a YAML file named `apigee-backend-service.yaml` with the following content:

```
# apigee-backend-service.yaml
kind: ApigeeBackendService
apiVersion:  apim.googleapis.com/v1
metadata:
  name: my-apigee-extension-backend-service
spec:
  apigeeEnv: ENV_NAME # optional for Apigee, required for hybrid
  defaultSecurityEnabled: SECURITY_ENABLED
  locations: # required field
  - name: REGION_NAME_1
    network: NETWORK_NAME_1
    subnet: SUBNET_NAME_1
  - name: REGION_NAME_2
    network: NETWORK_NAME_2
    subnet: SUBNET_NAME_2
```

Where: 
     * ENV_NAME is the Apigee environment to use. This is similar to the `apigeeEnv` field in the `APIMExtensionPolicy`. This field is optional for Apigee and required for hybrid.
     * SECURITY_ENABLED (Optional) specifies whether default Apigee policies for API key validation and Quota checks are automatically enabled. Defaults to `true` if not specified.
     * REGION_NAME_1 specifies the region where you deploy the GKE Gateway. 
     * NETWORK_NAME_1 and SUBNET_NAME_1 specify the full resource URIs of the network and subnetworkwhere the Private Service Connect NEGs are created. For example, `projects/my-project/global/networks/my-default` and `projects/my-project/regions/us-central1/subnetworks/my-default`. Typically, these are the same as the network and subnetwork of the GKE cluster.
     * REGION_NAME_2, NETWORK_NAME_2, and SUBNET_NAME_2 are optional. You need them if you deploy the Apigee traffic extension in multiple regions.
  2. Apply the YAML file to your cluster in the `default` namespace: 
```
kubectl apply -f apigee-backend-service.yaml
```

  3. Confirm that the `ApigeeBackendService` created successfully: 
```
kubectl get apigeebackendservice
```

The output should look similar to the following:

```
NAMESPACE   NAME                          STATE     ERRORMESSAGE
default     default-ext-lb1-apim-policy   CREATED   
```



When you create an `ApigeeBackendService`, the Apigee Operator for Kubernetes automatically creates an `APIMExtensionPolicy` with the same name and namespace as the `ApigeeBackendService`. This is the backing `APIMExtensionPolicy`.
If `defaultSecurityEnabled` is set to `true`, the Apigee Operator for Kubernetes automatically adds the default API key and Quota policies to the `APIMExtensionPolicy`. To add additional policies, see [Add policies to the GKE Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies).
### Create a `GCPTrafficExtension` resource
The`GCPTrafficExtension` resource defines an extension for Apigee and references the `ApigeeBackendService` created in the previous step as its `backendRef`. For more details on configuring a `GCPTrafficExtension`, see [Configure service extensions](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-the-gateways).
The `supportedEvents` field specifies which parts of the request and response lifecycle are exposed to the extension. The Apigee Operator for Kubernetes supports the following events: 
  * `RequestHeaders`
  * `RequestBody`
  * `RequestTrailers`
  * `ResponseHeaders`
  * `ResponseBody`
  * `ResponseTrailers`

For policies that require inspecting or modifying the request or response body (e.g., JSONThreatProtection), you must include `RequestBody` and `ResponseBody` in the `supportedEvents` list. For more information on supported events, see the [Cloud Load Balancing traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) documentation. 
To create a `GCPTrafficExtension`: 
  1. Create a YAML file named `gcp-traffic-extension.yaml` with the following content: 
```
# gcp-traffic-extension.yaml
kind: GCPTrafficExtension
apiVersion: networking.gke.io/v1
metadata:
  name: my-apigee-extension
spec:
  targetRefs:
  - group: "gateway.networking.k8s.io"
    kind: Gateway
    name: GATEWAY_NAME  # Replace with your GKE Gateway name
  extensionChains:
  - name: EXTENSION_CHAIN_NAME
    matchCondition:
      celExpressions:
      - celMatcher: request.path.startsWith("/")
    extensions:
    - name: EXTENSION_NAME
      metadata:
        # This metadata label must match the name of the ApigeeBackendService
        apigee-extension-processor : APIGEE_BACKEND_SERVICE_NAME
      failOpen: false
      supportedEvents:
      - SUPPORTED_EVENT1
      - SUPPORTED_EVENT2
      timeout: 1s
      requestBodySendMode: FullDuplexStreamed
      backendRef: # References the ApigeeBackendService by kind and name
        kind: ApigeeBackendService
        name: APIGEE_BACKEND_SERVICE_NAME
        Port: 443
```

Where: 
     * GATEWAY_NAME is the name of the GKE Gateway to which the extension applies.
     * EXTENSION_CHAIN_NAME is the name of the extension chain.
     * EXTENSION_NAME is the name of the traffic service extension.
     * APIGEE_BACKEND_SERVICE_NAME is the name of the `ApigeeBackendService` created earlier. This label inside the `extensions` block **must** match the `metadata.name` of the `ApigeeBackendService` created earlier.
     * The `supportedEvents` field specifies which parts of the request and response lifecycle are exposed to the extension. The Apigee Operator for Kubernetes supports the following events: 
       * `RequestHeaders`
       * `RequestBody`
       * `RequestTrailers`
       * `ResponseHeaders`
       * `ResponseBody`
       * `ResponseTrailers`
For policies that require inspecting or modifying the request or response body (e.g., JSONThreatProtection), you must include `RequestBody` and `ResponseBody` in the `supportedEvents` list. For more information on supported events, see the [Cloud Load Balancing traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) documentation.
  2. Apply the YAML file to your cluster: 
```
kubectl apply -f gcp-traffic-extension.yaml
```



## Next Steps
  * [Enable security and quota enforcement](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-security-quota)
  * [Add policies to the GKE Gateway](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-add-policies).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
