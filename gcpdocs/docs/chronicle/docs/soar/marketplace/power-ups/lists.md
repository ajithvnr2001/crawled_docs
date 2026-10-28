---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/
title: Lists \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:09:54.469726+00:00
---

# Lists  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/

[ Skip to main content ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/)
  * [Deutsch](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=de)
  * [Español](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=es-419)
  * [Français](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=id)
  * [Italiano](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=it)
  * [Português](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=ja)
  * [한국어](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fchronicle%2Fdocs%2Fsoar%2Fmarketplace%2Fpower-ups%2Flists%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/secops-color.svg) ](https://docs.cloud.google.com/chronicle/docs)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Search custom list](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#search-custom-list)
  * [Search for a specified string in an environment custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#search-environment-custom-list)
  * [Is string in custom list](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#is-string-in-custom-list)
  * [ Add string to custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#add-string-to-custom-list)
  * [ Remove string from custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#remove-string-from-custom-list)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)


Was this helpful?
Send feedback 
  * On this page
  * [Search custom list](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#search-custom-list)
  * [Search for a specified string in an environment custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#search-environment-custom-list)
  * [Is string in custom list](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#is-string-in-custom-list)
  * [ Add string to custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#add-string-to-custom-list)
  * [ Remove string from custom list ](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/lists/#remove-string-from-custom-list)


# Lists Stay organized with collections  Save and categorize content based on your preferences.
Supported in:
Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)
This document describes a set of actions to help you manage custom lists. 
## Search custom list
#### Description
Search for a specified string within the records of a custom list. If no values are provided, the search returns all custom list records. 
#### Parameters  
| **Parameter**  | **Type**  | **Default value**  | **Is mandatory**  | **Description**  |  
| --- | --- | --- | --- | --- |  
| String to search  | String  | N/A  | No  | String to search for within the records in a custom list.  |  
| Categories  | String  | N/A  | No  | Custom list category to search within.  |  
#### Example
In this example, the system checks whether `.com` is included in any records in a custom list with the category "Blocked Domains". 
#### Action Configurations  
|  **Parameter**  |  **Value**  |  
| --- | --- |  
| Entities   | All entities   |  
| String to search   | .com   |  
| Categories   | Blocked domains   |  
#### Action Results
  * **Script Result**  
| **Script Result Name**  | **Value Options**  | **Example**  |  
| --- | --- | --- |  
| `Match_records`  |  `true` or `false`  | `true`  |  
  * **JSON Result** 
```
[{
"entityIdentifier": "sample.com", "category": "Blocked Domains", "forDBMigration": false, "environments": ["*"], "id": 1, "creationTimeUnixTimeInMs": 1674846992575, "modificationTimeUnixTimeInMs": 1674846992575
}]
```



* * *
## Search for a specified string in an environment custom list 
#### Description
Search a specified string within the records of the current case environment's custom list. If no values are provided, the search returns all custom lists records. 
#### Parameters  
| **Parameter**  | **Type**  | **Default value**  | **Is mandatory**  | **Description**  |  
| --- | --- | --- | --- | --- |  
| String to search  | String  | N/A  | No  | String to search within the records in a custom list.  |  
| Categories  | String  | N/A  | No  | Category specification within the custom list for searching.  |  
#### Example
In this example, the system checks whether `1.1.1.1` is included in any records in a custom list with the category "vuln_scanner". 
#### Action Configurations  
|  **Parameter**  |  **Value**  |  
| --- | --- |  
| Entities   | All entities   |  
| String to search   |  `1.1.1.1`  |  
| Categories   |  `vuln_scanner`  |  
#### Action Results
  * **Script Result**  
| **Script Result Name**  | **Value Options**  | **Example**  |  
| --- | --- | --- |  
| Match_Records  |  `true` or `false`  | `true`  |  
  * **JSON result** 
```
[
  {
    "entityIdentifier": "1.1.1.1",
    "category": "vuln_scanner",
    "environments": [
      "Default Environment"
    ],
    "id": 5,
    "name": "test",
    "creationTimeUnixTimeInMs": 1673953571935,
    "modificationTimeUnixTimeInMs": 1673953571935
  }
]

```



## Is string in custom list
#### Description
Checks if a string is in a custom list.
#### Parameters  
| **Parameter**  | **Type**  | **Default value**  | **Is mandatory**  | **Description**  |  
| --- | --- | --- | --- | --- |  
| ListItem  | String  | N/A  | Yes  | String to add to a custom list.  |  
| Category  | String  | Allowlist  | Yes  | Custom list category or name.  |  
#### Example
In this example, the system checks whether the IP address `0.0.0.0` exists in a list category named `bad_ips_list`. 
#### Action Configurations  
|  **Parameter**  |  **Value**  |  
| --- | --- |  
| Entities   | All entities   |  
| IdentifierList   |  `0.0.0.0`  |  
| Categories   |  `bad_ips_list`  |  
**Action Results**
  * **Script Result**

  
| **Script Result Name**  | **Value Options**  | **Example**  |  
| --- | --- | --- |  
| NumOf FoundResults  |  `true` or `false`  | `true`  |  
  * **JSON result** 
```
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
```



##  Add string to custom list 
#### Description
Adds a string to a custom list.
**Parameters**  
| **Parameter**  | **Type**  | **Default value**  | **Is mandatory**  | **Description**  |  
| --- | --- | --- | --- | --- |  
| ListItem  | String  | N/A  | Yes  | String to add to a custom list.  |  
| Category  | String  | Allowlist  | Yes  | Custom list category or name.  |  
#### Example
In this example, an IP address of `0.0.0.1` is added to a custom list category named `bad_ips_list`. 
#### Action Configurations  
|  **Parameter**  |  **Value**  |  
| --- | --- |  
| Entities   | All entities   |  
| Listitem   |  `0.0.0.1`  |  
| Categories   |  `bad_ips_list`  |  
#### Action Results
  * **Script Result**  
| **Script Result Name**  | **Value Options**  | **Example**  |  
| --- | --- | --- |  
| NumOf FoundResults  |  `true` or `false`  | `true`  |  
  * **JSON result** 
```
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
```



* * *
##  Remove string from custom list 
#### Description
Removes a string from a custom list.
#### Parameters  
| **Parameter**  | **Type**  | **Default value**  | **Is mandatory**  | **Description**  |  
| --- | --- | --- | --- | --- |  
| Category  | String  | Allowlist  | Yes  | Custom list category or name.  |  
| ListItem  | String  | N/A  | Yes  | String to remove from a custom list.  |  
#### Example
In this example, an IP address `0.0.0.1` is removed from a custom list category named `bad_ips_list`. 
#### Action Configurations  
|  **Parameter**  |  **Value**  |  
| --- | --- |  
| Entities   | All entities   |  
| IdentifierList   |  `0.0.0.1`  |  
| Categories   |  `bad_ips_list`  |  
#### Action Results
  * **Script Result**  
| **Script Result Name**  | **Value Options**  | **Example**  |  
| --- | --- | --- |  
| NumOfFoundResults  |  `true` or `false`  | `true`  |  
  * **JSON result** 
```
{
"Entity" : "0.0.0.0",
"EntityResult" : "true"
}
```



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
