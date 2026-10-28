---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/
title: DNS setup quickstart \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:59:52.863835+00:00
---

# DNS setup quickstart  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [ Create a managed zone and record set ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#create-a-managed-zone-and-record-set)
  * [ Add your DNS servers to Cloud DNS ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#add-your-dns-servers-to-cloud-dns)
  * [ Configure your domain to use the Google Cloud name servers ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#configure-your-domain-to-use-the-google-cloud-name-servers)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  DNS setup quickstart Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [ Create a managed zone and record set ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#create-a-managed-zone-and-record-set)
  * [ Add your DNS servers to Cloud DNS ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#add-your-dns-servers-to-cloud-dns)
  * [ Configure your domain to use the Google Cloud name servers ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart/#configure-your-domain-to-use-the-google-cloud-name-servers)


Version 1.16 keyboard_arrow_down
Supported versions:
  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/dns-quickstart.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/dns-quickstart.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/dns-quickstart.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/dns-quickstart.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)
Unsupported versions:
  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/dns-quickstart.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/dns-quickstart.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/dns-quickstart.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/dns-quickstart.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/dns-quickstart.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/dns-quickstart.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/dns-quickstart.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/dns-quickstart.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/dns-quickstart.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/dns-quickstart.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/dns-quickstart.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/dns-quickstart.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/dns-quickstart.html)


This topic offers an example showing how to use [Google Cloud DNS](https://cloud.google.com/dns) to configure a DNS zone with a record set that points to your Apigee hybrid ingress IP address. 
##  Create a managed zone and record set 
This section explains how to create a DNS zone and record set in Google Cloud DNS. 
  1. Create a managed zone and record set for your domain. This is the address you will use to make API proxy calls to hybrid. 
    1. Create a managed public zone. For instructions, see [ Create a managed public zone](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_managed_public_zone).
    2. Create a new record set with the following selections. For instructions, see [Create a new record](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name#create_a_new_record). 
       * **DNS Name** : The name of the endpoint external API calls communicate with, like `           api-services` or `example-endpoint`
       * **Resource Record Type** : **A**
       * **TTL** and **TTL Unit** : Accept defaults
       * **IP Address** : The static IP you created
  2. In the **Zone details** view, copy the DNS name of the **A** record you just created and save it to a **`DOMAIN`**environment variable. Be careful to not include the period at the end.
![DNS name environment variable highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/copy-dns-name.png)

```
export DOMAIN=dns_name_of_record
```

##  Add your DNS servers to Cloud DNS 
In this step, you copy the DNS servers from your domain to [Google Cloud DNS](https://cloud.google.com/dns/). Doing so allows Google Cloud to manage the DNS for your Google Cloud Project. 
  3. The **Zone details** view lists four DNS servers as the NS data for your new zone. Copy the DNS record data as shown in the following example: 
![Zone details, DNS servers highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/copy-dns-records.png)


##  Configure your domain to use the Google Cloud name servers 
Go to your domain registrar and edit your domain's DNS settings to use the Google Cloud Name servers. 
The following screenshot shows an example of entering the Google Cloud name servers in [Google Domains](https://domains.google.com): 
![Google domain, Use custom name servers highlighted](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/hybrid-dns-fields.png)
Google Cloud DNS now manages the DNS records for your domain. 
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
