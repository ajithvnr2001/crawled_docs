---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alexa/
title: Integrate Alexa with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:46:16.082812+00:00
---

# Integrate Alexa with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/alexa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Alexa with Google SecOps

**Important:** Amazon retired the Alexa Web Information Service on December 15, 2022\. Live requests from this integration fail because the service is no longer active.

This document explains how to integrate Alexa with Google Security Operations.

**Note:** This integration appears as _Amazon Alexa Rank Indicator_ in the Google SecOps Content Hub and as _Alexa_ in playbooks.

## Use cases

The Alexa integration uses Google SecOps capabilities to support the following use cases:

  * **URL popularity enrichment** : Add global website traffic rankings to URLs in cases to distinguish established websites from unfamiliar domains.
  * **Suspicious domain triage** : Automatically flag low-traffic domains as suspicious during phishing or malware investigations.
  * **Automated alert escalation** : Route playbooks when a domain falls below your popularity threshold so analysts can prioritize suspicious URLs.



## Before you begin

Before you configure the Alexa integration in Google SecOps, complete the following prerequisite steps:

  1. Create AWS access key credentials for your Google SecOps instance.
  2. Configure least-privilege access permissions in AWS Identity and Access Management.
  3. Verify network connectivity between Google SecOps and Alexa Web Information Service.



### Create AWS access key credentials

To connect to Alexa Web Information Service, create a dedicated IAM user in AWS instead of using root account credentials, and generate an access key pair for the integration parameters:

  * `Access key id`: The access key ID for your dedicated AWS IAM user.
  * `Secret access key`: The secret access key paired with the access key ID. Save this key when you create it, because AWS doesn't let you view an existing secret key again later.



For instructions on creating IAM user access keys, refer to the [AWS Identity and Access Management documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access_keys.html).

### Configure least-privilege access permissions

Grant your dedicated IAM user only the permissions needed to query Alexa Web Information Service instead of full administrative access. Refer to the [AWS Identity and Access Management documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) for details on attaching policies.

The following table lists the minimal AWS permissions required for each action:

Action | AWS service | Required permission | Description  
---|---|---|---  
**Get URL Rank** | `awis` | `awis:UrlInfo` | Retrieves website traffic rankings for URLs.  
**Ping** | `awis` | `awis:UrlInfo` | Tests the connection and verifies your AWS credentials.  
  
### Verify network connectivity

Verify that your Google SecOps instance or remote agent allows outbound HTTPS traffic to the Alexa Web Information Service endpoint listed in the following table:

Destination host | Default port | Direction | Protocol  
---|---|---|---  
`awis.us-west-1.amazonaws.com` | `443` | Outbound | HTTPS  
  
## Integration parameters

The Alexa integration requires the following parameters:

Parameter | Description  
---|---  
`Access key id` | Required. The AWS access key ID used to connect to Alexa Web Information Service.  
`Secret access key` | Required. The AWS secret access key associated with the `Access key id`.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Run a manual action in your case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case#run-manual-action). 

### Get URL Rank

Use the **Get URL Rank** action to check the global traffic rank of URLs and identify unfamiliar or low-traffic websites that might be suspicious.

This action runs on the `URL` Google SecOps entity.

#### Action inputs

The **Get URL Rank** action requires the following parameters:

Parameter | Description  
---|---  
`Threshold` | Required. The rank limit used to flag unfamiliar websites, such as `100000`. Websites with a rank number higher than this value have less traffic and are marked as suspicious.  
  
#### Action outputs

The **Get URL Rank** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment

The **Get URL Rank** action supports the following entity enrichment:

Enrichment field name | Description  
---|---  
`Alexa_Rank` | The website's global traffic rank in Alexa.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get URL Rank** action:
    
    
    [
      {
        "EntityResult": {
          "TrafficData": [
            {
              "text": "          ",
              "DataUrl": [
                {
                  "text": "domain.com",
                  "type": "canonical"
                }
              ],
              "Rank": [
                {
                  "text": "5"
                }
              ]
            }
          ],
          "text": "        ",
          "Request": [
            {
              "text": "          ",
              "Arguments": [
                {
                  "text": "            ",
                  "Argument": [
                    {
                      "text": "              ",
                      "Name": [
                        {
                          "text": "url"
                        }
                      ],
                      "Value": [
                        {
                          "text": "domain.com"
                        }
                      ]
                    },
                    {
                      "text": "              ",
                      "Name": [
                        {
                          "text": "responsegroup"
                        }
                      ],
                      "Value": [
                        {
                          "text": "Rank"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        "Entity": "domain.com"
      }
    ]
    

##### Output messages

The **Get URL Rank** action provides the following output messages:

Output message | Message description  
---|---  
`Following domains were enriched by Alexa.` `ENTITY_ID: Rank: RANK` | The action succeeded.  
`No entities were enriched.` | The action failed. Make sure the case includes at least one valid URL.  
`Request Error: (ERROR_CODE)` | The action failed. Check that your AWS credentials are correct, your IAM user has permission to query Alexa Web Information Service, and your network can reach the service.  
  
##### Script result

The following table lists the value for the script result output when using the **Get URL Rank** action:

Script result name | Value  
---|---  
`is_risky` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connection to Alexa and verify that your AWS credentials work.

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
Entity enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Connected Successfully` | The action succeeded.  
`test_connectivity Error: (ERROR_REASON)` | The action failed. Check that your AWS credentials are correct, your IAM user has permission to query Alexa Web Information Service, and your network can reach the service.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_succeed` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
