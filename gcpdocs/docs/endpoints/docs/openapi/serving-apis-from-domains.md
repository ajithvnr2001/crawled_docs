---
url: https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/
title: Serving an API from your domain name \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:08:13.540814+00:00
---

# Serving an API from your domain name  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/

[ Skip to main content ](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/)
  * [Deutsch](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=de)
  * [Español](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=es-419)
  * [Français](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=id)
  * [Italiano](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=it)
  * [Português](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=ja)
  * [한국어](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#before_you_begin)
  * [Configure your API project to use your domain name](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#configure_your_api_project_to_use_your_domain_name)
  * [What's next](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)


Send feedback 
#  Serving an API from your domain name Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#before_you_begin)
  * [Configure your API project to use your domain name](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#configure_your_api_project_to_use_your_domain_name)
  * [What's next](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#whats_next)


OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/serving-apis-from-domains)
This page shows how to serve an API from a custom domain that you own, for example, `example.com`.
As an alternative to using your own domain name, you can use a domain name managed by Google. See [Using a domain managed by Google](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints#using_a_domain_managed_by_google) for more information.
## Before you begin
  * Obtain a domain name from a domain name registrar if you don't already have a domain name to use for your API.
  * [Verify domain ownership](https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name).
  * [Name your API host name](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints) with your domain name.
  * If you are using SSL with your domain, obtain and upload your SSL certificate.
  * [Deploy your API and Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).


## Configure your API project to use your domain name
Follow the instructions in the appropriate tab.
[App Engine](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#app-engine)[Compute Engine](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#compute-engine)[GKE](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains/#gke) More
To set your API project to use your verified domain, follow the instructions provided in [Adding a custom domain for your application](https://docs.cloud.google.com/appengine/docs/flexible/python/using-custom-domains-and-ssl)
The recommended way to serve an API from Compute Engine instances is to use a load balancer across an instance group. You need to reserve an external IP address for the domain name and use that external IP address for the load balancer.
To serve the API from a domain name:
  1. Reserve at least one static external IP address in your project:  

[Go to the External IP Addresses page](https://console.cloud.google.com/networking/addresses/add)
    1. Assign any name you want to the reserved IP address
    2. For **Type** , click **Global**.
    3. For **Attached to** , click **None**. You attach the IP address to a load balancer later.
  2. Visit your domain provider account and edit your domain settings. You must create an _A record_ that contains your API name, for example, `myapi.example.com` with the external IP address in its data field
  3. Create an instance group that includes the instances running your API and Extensible Service Proxy (ESP:  

[Go to the Create a New Instance group page](https://console.cloud.google.com/compute/instanceGroups/add)
    1. Assign any name you want for the group and add a description.
    2. From the **Zone** list, click the zone used by your API instance.
    3. In the **Instance definition** list, click **Select existing instances**
    4. In the **VM Instances** field, add the VM instance running the API.
    5. Click **Create**.
  4. Create and configure an HTTP(S) load balancer:  

[Go to the Create a New HTTP(S) load balancer page](https://console.cloud.google.com/networking/loadbalancing/http/add)
    1. Click **Define a Backend Service** > **Create or select a backend service**.  
![Backend configuration](https://docs.cloud.google.com/static/endpoints/docs/images/backend-service.png)
    2. Assign any name and description you want for this backend service configuration.
    3. In the **Protocol** field, select the protocol you want to support through the load balancer, **HTTP** or **HTTPS**.
    4. In the **Instance group** list, click your instance group.
    5. In the **Port Numbers** field, enter `8080`.
    6. Click **Health check** to configure health checks:
       * Enter a name for the health check configuration.
       * Assign the port `8080`.
       * To accept the remaining default values, click **Save**.
    7. For now, accept the defaults for the rest of the configuration. You can make changes later as needed, such as additional ports.
    8. You don't need to set anything in the **Host and path rules** ; you can forward everything to your backend API by using the default **Any unmatched** filters. This means that all traffic into the load balancer is directed to the API on the port `8080` (the default port) as defined in the preceding steps.
    9. Click **Frontend configuration**.  
![Frontend configuration](https://docs.cloud.google.com/static/endpoints/docs/images/frontend-config.png)
       * In the **Protocol** field, select the protocol you want to support through the load balancer, **HTTP** or **HTTPS**.
       * In the **IP** list, click the external IP address you created earlier.
       * For the HTTPS protocol, you need to use SSL. In the **Certificate** list, click the certificate you want.
       * Optionally, if you want to support another protocol, click **Add frontend IP and port** , specify the protocol, the same external IP address, and a different port.
    10. To create the fully configured load balancer, click **Create**. If the **Create** button isn't enabled, check the components you just configured: a checkmark should appear beside each of the configuration components. A missing checkmark means you haven't completed the configuration.
    11. After your DNS changes propagate, requests are sent to your API by using the load balancer.


To serve an API over a domain for Google Kubernetes Engine (GKE), you need to expose ESP as a service, by using the returned external IP address for your domain's DNS settings. Note that GKE automatically does load balancing for you.
To expose your API as a service:
  1. If you don't have one already, [Configure a Kubernetes service](https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/) for your API backends. Create a service configuration file, `service.yaml`, with content similar to the following: 
```
            apiVersion: v1
            kind: Service
            metadata:
              name: echo
            spec:
              ports:
              - port: 80
                targetPort: 8081
                protocol: TCP
              selector:
                app: echo-app
              type: LoadBalancer
              
```

     * Change the `selector` label to match your backend labels (`app: echo-app` in this example)
     * Make sure the `targetPort` matches the port used by ESP configured in your API backends. ESP uses port `8081` by default.
  2. Deploy the Kubernetes service:  

```
            kubectl apply -f service.yaml
            
```

  3. View the external IP address assigned to your exposed service:  

```
            kubectl get services
            
```
The output displays an `EXTERNAL-IP` address similar to the following:  

```
            NAME         CLUSTER-IP     EXTERNAL-IP      PORT(S)    AGE
            hello-node   10.X.XXX.202   10X.XXX.XX.123   8080/TCP   1m
      
```

  4. Change the generated external IP from ephemeral to static.  

[Go to the External IP Addresses page](https://console.cloud.google.com/networking/addresses/list)
    1. Select your external IP address from the list.
    2. In the **Type** list, click **Static**.
  5. Visit your domain provider account and edit your domain settings. You must create an _A record_ that contains your API name, for example, `myapi.example.com`, with the external IP address in its data field.


## What's next
  * [Serving multiple APIs from a domain](https://docs.cloud.google.com/endpoints/docs/openapi/deploying-apis-subdomains)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
