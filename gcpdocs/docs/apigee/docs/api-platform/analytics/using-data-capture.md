---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/
title: Collecting custom data with the DataCapture policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:53:18.415486+00:00
---

# Collecting custom data with the DataCapture policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Create a Data Collector REST resource](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#create-a-data-collector-rest-resource)
  * [Specify the data to collect](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#specify-the-data-to-collect)
  * [Creating a custom report from data collected with DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#creating-a-custom-report-from-data-collected-with-datacapture)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)


Send feedback 
#  Collecting custom data with the DataCapture policy Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Create a Data Collector REST resource](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#create-a-data-collector-rest-resource)
  * [Specify the data to collect](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#specify-the-data-to-collect)
  * [Creating a custom report from data collected with DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#creating-a-custom-report-from-data-collected-with-datacapture)


_This page applies to**Apigee** and **Apigee hybrid**._
_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)
In addition to the [usual API data collected by Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview#what-kind-of-data-is-collected-and-analyzed), you can also collect custom data using the [DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) policy. There are two main steps required, as described in the following sections:
  1. [Create a Data Collector REST resource](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#create-a-data-collector-rest-resource).
  2. [Specify the data you want to collect ](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-data-capture/#specify-the-data-to-collect) using the DataCapture policy's `<Collect>` element.


## Create a Data Collector REST resource
To use the `DataCapture` policy, you must first create a [ Data Collector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.datacollectors) REST resource. To do so, send an API request like the following:

```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -X POST -H "content-type:application/json" \
  -d '
{
  "name": "dc_my_custom_data",
  "description": "Collects data for analysis.",
  "type": "STRING",
}' \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/datacollectors"
```

This creates a resource named `dc_my_custom_data`, which you can use with the `DataCapture` policy.
## Specify the data to collect
You can specify the data to collect using the DataCapture policy's [ `<Collect>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#collect) element. There are various ways to do this, as shown in the [Examples](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#examples) section in the DataCapure reference page. One way is to specify a [flow variable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference), which stores data passed in API requests and responses. For example, you could collect data that customers enter in a web page form using the flow variable `message.formparam.param_name.values`, where `param_name` is the name of a parameter in the form. Suppose the form has a parameter named `payment_amount`. The corresponding flow variable would be `message.formparam.payment_amount.values`.
The following code specifies this variable by the `ref` attribute of the `<Collect>` element.

```
<DataCapture name="capturepayment">
    <Capture>
        <DataCollector>dc_my_custom_data</DataCollector>
        <Collect ref="message.form_param.payment_amount.values" >
    </Capture>
</DataCapture>
```

With this setting, the data entered in the form's `payment_amount` field will be collected by DataCapture and stored in a variable named `dc_my_custom_data`.
## Creating a custom report from data collected with DataCapture
Once you have set up data collection with the DataCapture policy, you can use the data to create a custom report by the procedure described in [Adding a custom report](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#add). To do so, when you select a metric for the report, as shown in [ step 4 of the procedure](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#step4), choose the variable that has the same name as the Data Collector REST resource you created for DataCapture—for example, `dc_my_custom_data`.
You can also use the same variable as a dimension in a custom report. Since dimensions group data by the values of the variable, it is usually preferable for the variable to be a string that only takes on a limited number of values.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
