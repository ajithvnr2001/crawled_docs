---
url: https://docs.cloud.google.com/armor/docs/manage-security-policies/
title: Manage Cloud Armor security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:33:26.798954+00:00
---

# Manage Cloud Armor security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/manage-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Manage Cloud Armor security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Google Cloud Armor security policies to filter incoming traffic to your application. Cloud Armor security policies help protect your web applications and services from distributed denial-of-service (DDoS) attacks and other threats from the internet. Enforcing a strong security posture requires managing your security policies through updating, testing, attaching to backend services, and exporting or importing.

To create or view security policies, see [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/create-security-policies). To manage rules within a security policy, see [Manage Cloud Armor security policy rules](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules).

## Manage security policies

The following sections describe how you can update, delete, or test your security policies.

### Update security policies

The steps in this section describe how you can update a Cloud Armor security policy. You can modify the policy's description, modify the default rule, change the target backend service, or add rules.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Find the name of the policy that you want to update in the list of policies and click more_vert**Menu** for that policy.

     * To update the description or the default rule action, select **Edit** , make your changes, and then click **Update**.
     * To add a rule, select **Add rule** , and then follow the steps in [Add rules to a security policy](https://docs.cloud.google.com/armor/docs/create-security-policy-rules#create-rules).
     * To replace the target backend service, select **Apply policy to target** , click **Add Target** , select a target, and then click **Add**.



###  gcloud 

To update a security policy, use the following Google Cloud CLI steps:

  * To update a rule, see [Update a single rule in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules#update-rules).
  * To add a rule, see [Add rules to a security policy](https://docs.cloud.google.com/armor/docs/create-security-policy-rules#create-rules).
  * To delete a rule, see [Delete rules from a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules#delete-rules).
  * To update multiple rules in a single atomic update, see [Atomically update multiple rules in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules#atomic-update).
  * To update non-rule fields (such as the description), see Export security policies and Import security policies.



### Delete security policies

This section describes how you can delete a Cloud Armor security policy. Remove all backend services from the policy before you delete it.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Select the checkbox next to the policy that you want to delete.

  3. In the upper-right corner of the page, click delete**Delete**.




###  gcloud 

Use `gcloud compute security-policies delete NAME`. Replace `NAME` with the name of the security policy:
    
    
    gcloud compute security-policies delete NAME
    

### Test security policies

We recommend that you deploy all new rules in preview mode, then examine your [request logs](https://docs.cloud.google.com/armor/docs/request-logging), to verify that the policies and rules are behaving as expected.

## Attach and remove security policies

The following sections describe how you can attach and remove security policies.

### Attach a security policy to a backend service

Follow the steps in this section to attach a Cloud Armor security policy to a backend service. You can attach a security policy to multiple backend services, but a backend service can have only one of each type of security policy attached to it.

###  Console 

**Caution:** You cannot use the Google Cloud console to attach a security policy to an external proxy Network Load Balancer or classic proxy Network Load Balancer.

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Click **Apply policy to new target**.

  5. Click **Add Target**.

  6. In the **Target** list, select a target, and then click **Add**.




###  gcloud 

When you attach a backend security policy to a backend service, use the `gcloud compute backend-services` command and the `--security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --security-policy my-policy
    

When you attach an edge security policy to a backend service, use the `gcloud compute backend-services` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --edge-security-policy my-policy
    

### Remove a security policy from a backend service

Follow the steps in this section to remove a Cloud Armor security policy from a backend service.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Select the target backend service that you're removing the policy from.

  5. Click **Remove**.

  6. In the **Remove target** message, click **Remove**.




###  gcloud 

When you remove a backend security policy, use the `gcloud compute backend-services` command and the `--security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --security-policy ""
    

When you remove an edge security policy, use the `gcloud compute backend-services` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --edge-security-policy ""
    

### Attach a security policy to a backend bucket

Follow the steps in this section to attach a Cloud Armor edge security policy to a backend bucket. You can attach an edge security policy to multiple backend buckets.

**Note:** You can attach only edge security policies to backend buckets.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Click **Apply policy to new target**.

  5. Click **Add Target**.

  6. In the **Target** list, select a target, and then click **Add**.




###  gcloud 

When you attach an edge security policy to a backend bucket, use the `cloud compute backend-buckets` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-bucket \
        --edge-security-policy my-edge-policy
    

### Remove a security policy from a backend bucket

Follow the steps in this section to remove a Cloud Armor edge security policy from a backend bucket.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Select the target backend service that you're removing the policy from.

  5. Click **Remove**.

  6. In the **Remove target** message, click **Remove**.




###  gcloud 

When you remove an edge security policy from a backend bucket, use the `cloud compute backend-buckets` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-bucket \
        --edge-security-policy ""
    

## Import and export security policies

The following sections describe how you can import and export security policies.

### Export security policies

You can export a Cloud Armor security policy as a YAML or JSON file by using the Google Cloud CLI. This feature provides the following benefits:

  * **Save a copy for version control or backup** : exporting provides a local copy of your policy. Save this copy in source control systems as a backup or to track changes. You can re-import it later to restore a prior version.

  * **Modify and update policies locally** : modify exported policies offline using a text editor. After making changes, re-import the updated policy to apply your modifications to Cloud Armor.




###  gcloud 

  1. In the following command, `NAME` is the name of the security policy. Valid file formats are YAML and JSON. If you don't specify the file format, Cloud Armor uses YAML.
         
         gcloud compute security-policies export NAME \
             --file-name FILE_NAME  \
             --file-format FILE_FORMAT
         

The following example shows the command to export the `my-policy` security policy to the `my-file` file in the YAML format:
         
         gcloud compute security-policies export my-policy \
             --file-name my-file \
             --file-format yaml
          

The following example shows an exported security policy:
         
         description: my description
         fingerprint: PWfLGDWQDLY=
         id: '123'
         name: my-policy
         rules:
         - action: allow
           description: default rule
           match:
               config:
                 srcIpRanges:
                 - '*'
               versionedExpr: SRC_IPS_V1
             preview: false
             priority: 2147483647
           selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
           

  2. Modify the exported file with a text editor, and then import it back to Google Cloud by using the `import` command.




### Import security policies

You import Cloud Armor security policies from a YAML or JSON file by using the Google Cloud CLI. You can't use the `import` command to update an existing policy's rules. Instead, update rules individually by using the [Update a single rule in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules#update-rules) procedure, or all at once by using the [Atomically update multiple rules in a security policy](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules#atomic-update) procedure.

###  gcloud 

To import security policies, use the following `gcloud compute security-policies import NAME` command.
    
    
    gcloud compute security-policies import NAME \
        --file-name FILE_NAME  \
       [--file-format FILE_FORMAT]
    

For example, the following command updates the policy `my-policy` by importing the file `my-file`.
    
    
    gcloud compute security-policies import my-policy \
        --file-name my-file \
        --file-format json
    

Replace `NAME` with the name of the security policy. If you don't provide the file format, the correct format is assumed based on the file structure. If the structure is invalid, the gcloud CLI returns an error message.

If the policy's [fingerprint](https://docs.cloud.google.com/armor/docs/security-policy-overview#fingerprint) is out of date when you import it, Cloud Armor returns an error. This means the policy was modified since you last exported it. To fix this, use the `describe` command on the policy to get the latest fingerprint. You can use `--format=yaml` or `--format=json` with the `describe` command to make comparison easier. Compare the `rules` section of the `describe` output with the `rules` section in your policy file, merge any differences, and then replace the outdated fingerprint in your file with the latest one from the `describe` output.

**Note:** Exporting and importing security policies is useful for version control and local modification but not for migrating a policy from one project to another.

## What's next

  * [Create and view security policies](https://docs.cloud.google.com/armor/docs/create-security-policies)
  * [Create and view security policy rules](https://docs.cloud.google.com/armor/docs/create-security-policy-rules)
  * [Manage security policy rules](https://docs.cloud.google.com/armor/docs/manage-security-policy-rules)
  * [Tune web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
