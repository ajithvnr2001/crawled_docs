---
url: https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/
title: Configure private UI access \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:14:45.354912+00:00
---

# Configure private UI access  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=de)
  * [Español](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=it)
  * [Português](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini%2Fenterprise%2Fdocs%2Fprivate-ui-access%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#before_you_begin)
  * [Configure Private Service Connect](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-psc)
  * [Configure network routing](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-network-routing)
  * [Update DNS settings](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#update-dns-settings)
  * [Configure proxies, firewalls, and TLS inspection](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-proxies)
  * [About securing your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#vpc-service-controls)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)


Was this helpful?
Send feedback 
#  Configure private UI access Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#before_you_begin)
  * [Configure Private Service Connect](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-psc)
  * [Configure network routing](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-network-routing)
  * [Update DNS settings](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#update-dns-settings)
  * [Configure proxies, firewalls, and TLS inspection](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#configure-proxies)
  * [About securing your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#vpc-service-controls)


By default, users access Gemini Enterprise interfaces for features such as agents, the assistant, and Gemini Notebook Enterprise, through the public internet. To meet organizational security requirements, you can establish private UI access using hybrid networking solutions like Cloud VPN or Cloud Interconnect.
To configure private connectivity to Gemini Enterprise, you must route Google Cloud API traffic through a Private Service Connect (PSC) endpoint. This allows users to access Gemini Enterprise interfaces through an internal IP address within your Virtual Private Cloud (VPC), avoiding the public internet.
![Reference
  architecture using VPC Service Controls to provide private access to
  Gemini Enterprise UIs.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/private-ui-access.png) Reference architecture using VPC Service Controls to provide private access to Gemini Enterprise UIs.
In this reference architecture, on-premises or multi-cloud users connect to a [PSC endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints), which enables access to Google APIs through a user-defined internal IP address within your Google Cloud Virtual Private Cloud. In addition, you must configure your internal DNS to resolve Gemini Enterprise domains to the IP address of the PSC endpoint.
## Before you begin
Before configuring private UI access, ensure that you have the following:
  * A Google Cloud Virtual Private Cloud network connected to your on-premises network through Cloud Router, using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * Permissions to create Private Service Connect endpoints and manage Cloud Router custom routes.


## Configure Private Service Connect
Private and restricted virtual IP addresses (VIPs) used for Private Google Access don't support private access to the Gemini Enterprise UI. To ensure full functionality, you must resolve the Gemini Enterprise domains to a Private Service Connect endpoint configured with the `all-apis` bundle.
  1. Create a new PSC endpoint in the same Virtual Private Cloud as the Cloud Router used for hybrid networking.
  2. Target the **All Google APIs** API bundle. This bundle provides access to most Google APIs, including `*.googleapis.com` service endpoints. The **VPC-SC** API bundle doesn't support all Gemini Enterprise domains.


## Configure network routing
The PSC endpoint uses a `/32` IP address that doesn't originate from a standard VPC subnet and won't be visible from on-premises or multi-cloud networks. You must configure your Cloud Router to advertise the IP address. For more information about IP address requirements for Private Service Connect endpoints, see [IP address requirements](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#ip-address-requirements).
  1. Identify the IP address that you assigned to your PSC endpoint.
  2. In your Cloud Router configuration, create a custom route for the IP address. For more information about specifying custom advertised routes on a Cloud Router, see [Advertise custom address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).
  3. Update on-premises or multi-cloud firewalls to permit outbound traffic to the IP address.


## Update DNS settings
Finally, update your DNS settings to resolve the Gemini Enterprise domains using the PSC endpoint. For more information, see [Create DNS records by using default DNS names](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default).
  1. Configure internal on-premises or cloud network DNS records to resolve the following Gemini Enterprise domains to the internal IP address of the PSC endpoint:
     * `content-discoveryengine.googleapis.com`
     * `content-discoveryengine.mtls.googleapis.com`
     * `content-eu-discoveryengine.googleapis.com`
     * `content-eu-discoveryengine.mtls.googleapis.com`
     * `content-global-discoveryengine.googleapis.com`
     * `content-global-discoveryengine.mtls.googleapis.com`
     * `content-us-discoveryengine.googleapis.com`
     * `content-us-discoveryengine.mtls.googleapis.com`
     * `content-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-us-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-eu-webchannel-assistant-discoveryengine.googleapis.com`
     * `discoveryengine.googleapis.com`
     * `discoveryengine.mtls.googleapis.com`
     * `discoveryengine.clients6.google.com`
     * `eu-discoveryengine.clients6.google.com`
     * `us-discoveryengine.clients6.google.com`
     * `eu-discoveryengine.googleapis.com`
     * `eu-discoveryengine.mtls.googleapis.com`
     * `global-discoveryengine.googleapis.com`
     * `global-discoveryengine.mtls.googleapis.com`
     * `us-discoveryengine.googleapis.com`
     * `us-discoveryengine.mtls.googleapis.com`
     * `vertexaisearch.cloud.google.com`
     * `vertexaisearch.cloud.google`
     * `notebooklm.cloud.google.com`
     * `notebooklm.cloud.google`
     * `auth.cloud.google`
     * `payments.cloud.google`
     * `accounts.googleapis.com`
  2. If your environment requires strict data exfiltration protection boundaries, configure the `discoveryengine.googleapis.com` domain to the VPC-SC bundle IP address.


## Configure proxies, firewalls, and TLS inspection
If your users access Gemini Enterprise through a corporate proxy, secure web gateway, or firewall, configure these devices so that they don't block, buffer, or time out Gemini Enterprise traffic. These requirements apply whether users connect through the public internet or through a Private Service Connect endpoint.
If you don't configure these devices correctly, users might see the following symptoms:
  * The assistant stays in the **Thinking...** state and then displays the whole answer at once, instead of streaming the answer as it's generated.
  * Requests consistently fail after a fixed duration, such as 20, 30, or 60 seconds, with errors such as `HTTP 499` or `HTTP 504`.
  * The web app works on some networks, such as a home network, but not on the corporate network.


To avoid these issues, do the following:
  1. Allow outbound HTTPS traffic on port `443` to all of the Gemini Enterprise domains listed in [Update DNS settings](https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/#update-dns-settings). Allow the `global`, `us`, and `eu` domains even if your app uses a single location, because the web app can call more than one of these endpoints.
  2. Exclude the following streaming domains from TLS (SSL) inspection and from response buffering or content scanning. The assistant streams its answers over these connections, and devices that hold the response until it's complete cause delays and timeouts.
     * `content-discoveryengine.googleapis.com`
     * `content-us-discoveryengine.googleapis.com`
     * `content-eu-discoveryengine.googleapis.com`
     * `content-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-us-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-eu-webchannel-assistant-discoveryengine.googleapis.com`
     * `discoveryengine.clients6.google.com`
     * `us-discoveryengine.clients6.google.com`
     * `eu-discoveryengine.clients6.google.com`
  3. Set the idle and read timeouts on proxies, load balancers, and firewalls in the request path to at least 300 seconds. Complex requests, such as requests that use several connectors or agents, can take several minutes to complete.
  4. If you call the Gemini Enterprise API from your own applications, set the client request timeout to at least 300 seconds and use streaming methods where available.


## About securing your app with VPC Service Controls
For advanced security, you can implement VPC Service Controls (VPC-SC) to prevent data exfiltration from managed services like Gemini Enterprise and BigQuery. Unlike Identity and Access Management, which controls _who_ can access data, VPC-SC controls dictate _where_ data can be accessed and moved.
If considering this approach, keep the following in mind:
  * While optional, using VPC Service Controls is a best practice for blocking public access to Google services exposed through `googleapis.com`.
  * Among other implications, services (such as `discoveryengine.googleapis.com`) that are added to a VPC-SC perimeter are blocked to all public access, including access through the Google Cloud console.
  * To allow access to protected services within a VPC-SC perimeter, admins must explicitly allow ingress, by using [VPC-SC ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) or [defining access levels using Access Context Manager](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls#access-context-manager).


For more information about securing your Gemini Enterprise app using VPC-SC and Access Context Manager, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
