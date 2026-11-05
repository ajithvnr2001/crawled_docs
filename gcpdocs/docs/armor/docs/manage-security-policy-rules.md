---
url: https://docs.cloud.google.com/armor/docs/manage-security-policy-rules/
title: Manage Cloud Armor security policy rules \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:54:52.812934+00:00
---

# Manage Cloud Armor security policy rules  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/manage-security-policy-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Manage Cloud Armor security policy rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage rules within your Google Cloud Armor security policies, including updating individual rules, atomically updating multiple rules, and deleting rules.

To create new rules or view existing rules in a security policy, see [Create and view Cloud Armor security policy rules](https://docs.cloud.google.com/armor/docs/create-security-policy-rules). To manage the security policy container itself, see [Manage Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/manage-security-policies).

## Manage security policy rules

The following sections describe how you can update or delete security policy rules.

### Update a single rule in a security policy

This section describes how you can update a single rule in a Cloud Armor security policy. To atomically update multiple rules, see Atomically update multiple rules in a security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. Click the **Rules** tab.

  4. Next to the rule that you want to update, click edit**Edit**. The **Edit rule** page is displayed.

  5. Make your changes, and then click **Update**.




###  gcloud 

Use the following command to update a rule. You can update only one security policy at a time:
    
    
    gcloud compute security-policies rules update PRIORITY [ \
        --security-policy POLICY_NAME  \
        --description DESCRIPTION  \
        --src-ip-ranges IP_RANGES  | --expression EXPRESSION \
        --action=[ allow | deny-403 | deny-404 | deny-502 ]  \
        --preview
      ]
      

For example, the following command updates a rule with a priority of 1111 to allow traffic from the IP address range 192.0.2.0/24:
    
    
    gcloud compute security-policies rules update 1111 \
        --security-policy my-policy \
        --description "allow traffic from 192.0.2.0/24" \
        --src-ip-ranges "192.0.2.0/24" \
        --action "allow"
    

For more information about the preceding command, see [`gcloud compute security-policies rules update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/update).

To update the priority of a rule, use the REST API. See [`securityPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patchRule).

### Atomically update multiple rules in a security policy

You can use the atomic update feature to apply changes to multiple rules in a single update. Single-rule updates might cause unintended behavior like errors because old and new rules might overlap for a short period.

To atomically update multiple rules, export the current security policy to a JSON or YAML file, and then modify it. Use the modified file to create a security policy, and then switch the security policy for the backend services.

###  gcloud 

  1. Export the policy to update, as shown in the following example:
         
         gcloud compute security-policies export my-policy \
             --file-name my-file \
             --file-format yaml
         

The exported policy looks similar to the following example:
         
         description: my description
             fingerprint: PWfLGDWQDLY=
             id: '123'
             name: my-policy
             rules:
             - action: deny(404)
               description: my-rule-1
               match:
                 expr:
                   expression: evaluatePreconfiguredWaf('xss-v422-stable')
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 1
             - action: allow
               description: my-rule-2
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.4'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2
             - action: deny
               description: default rule
               kind: compute#securityPolicyRule
               match:
                 config:
                   srcIpRanges:
                   - '*'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2147483647
             selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
         

  2. Use a text editor to modify the policy. For example, you can modify the priorities of existing rules and add a rule:
         
         description: my description
             fingerprint: PWfLGDWQDLY=
             id: '123'
             name: my-policy
             rules:
             - action: deny(404)
               description: my-rule-1
               match:
                 expr:
                   expression: evaluatePreconfiguredWaf('xss-v422-stable')
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 1
             - action: allow
               description: my-new-rule
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.1'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 10
             - action: allow
               description: my-rule-2
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.4'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 11
             - action: deny
               description: default rule
               kind: compute#securityPolicyRule
               match:
                 config:
                   srcIpRanges:
                   - '*'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2147483647
             selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
         

  3. Create a new Cloud Armor security policy and specify the modified filename and format, as shown in the following example:
         
         gcloud compute security-policies create new-policy \
             --file-name modified-policy \
             --file-format yaml
         

  4. Remove the old security policy from the relevant backend service, as shown in the following example:
         
         gcloud compute backend-services update my-backend \
             --security-policy ""
         

  5. Add the new security policy to the backend service, as shown in the following example:
         
         gcloud compute backend-services update my-backend \
             --security-policy new-policy
         

  6. If the old policy is unused, delete it:
         
         gcloud compute security-policies delete my-policy
         




### Delete rules from a security policy

Follow the steps in this section to delete rules from a Cloud Armor security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. On the **Rules** tab, select the checkbox next to the rule that you want to delete.

  4. Click delete**Delete**.




###  gcloud 

Use the following command to remove a rule. You can modify only one security policy at a time, but you can delete multiple rules at once:
    
    
    gcloud compute security-policies rules delete PRIORITY [...] [
        --security-policy POLICY_NAME \
      ]
    

For example:
    
    
    gcloud compute security-policies rules delete 1000 \
        --security-policy my-policy
    

## What's next

  * [Create and view security policies](https://docs.cloud.google.com/armor/docs/create-security-policies)
  * [Create and view security policy rules](https://docs.cloud.google.com/armor/docs/create-security-policy-rules)
  * [Manage security policies](https://docs.cloud.google.com/armor/docs/manage-security-policies)
  * [Tune web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
