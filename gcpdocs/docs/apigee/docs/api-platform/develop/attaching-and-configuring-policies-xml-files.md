---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/
title: Attaching and configuring policies in XML files \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:59:32.213283+00:00
---

# Attaching and configuring policies in XML files  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Was this helpful?
Send feedback 
#  Attaching and configuring policies in XML files Stay organized with collections  Save and categorize content based on your preferences.
_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
You can create and edit policies locally, using your favorite text or XML-aware editor or IDE. This topic uses the Quota policy type as an example of how to create, configure, attach, deploy, and test policies.
Most API proxies enforce a quota. Quotas provide control over how often a client app is permitted to invoke an API over a given time interval. In the example below, a Quota policy is configured to limit apps to 1 request per minute. (While this may not be realistic, it does provide a simple way to see the effects of a policy.)
In an API proxy configuration, Policy files are stored as XML files under `/apiproxy/policies` directory.
For example, a policy of type Quota called Quota Policy could be created as a file called `QuotaPolicy.xml` with the following content:

```
<Quota enabled="true" continueOnError="false" name="QuotaPolicy">
    <Allow count="1"/>
    <Interval>1</Interval>
    <TimeUnit>minute</TimeUnit>
</Quota>
```

You can create a text file by hand, or you can generate the policy from an XML schema. All policies have some settings that are specific to the policy type, and some settings that are generic across all policies. 
When you attach policies in the management UI, the API proxy builder generates the policy instance from the XML schema for the policy type you selected. Therefore, you may see elements in the policy configuration that, for clarity, are not always included in documentation. 
All policies define the following attributes:
  * `enabled`: Indicates whether the policy is turned _on_ or _off_. Policies can be enabled/disabled at runtime by changing this setting. A policy that has `enabled` set to `false` is not enforced.
  * `continueOnError`: Defines whether the pipeline should continue processing the message if the policy fails. When enforcing quota policies, errors likely indicate that the quota has been exceeded, and, therefore, this attribute should be set to false.
  * `name`: The name that you give to this policy. This name is unique to this policy instance, and it is used to attach the policy to the flow as a processing step.


In the example above, the elements `Allow`, `Interval`, and `TimeUnit` are specific to the Quota policy. These elements provide settings that API Services enforces on behalf of an API. Other policy types define their own settings, which you can learn about in the [Policy Reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
