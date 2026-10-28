---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/
title: Virtual host missing selector \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:57:55.842042+00:00
---

# Virtual host missing selector  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Symptom](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#symptom)
  * [Error messages](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#error-messages)
  * [Cause: Virtualhost is missing ingress selector](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#cause:-virtualhost-is-missing-ingress-selector)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#diagnosis)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#resolution)
  * [Must gather diagnostic information](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#must-gather-diagnostic-information)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)


Was this helpful?
Send feedback 
#  Virtual host missing selector Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Symptom](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#symptom)
  * [Error messages](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#error-messages)
  * [Cause: Virtualhost is missing ingress selector](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#cause:-virtualhost-is-missing-ingress-selector)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#diagnosis)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#resolution)
  * [Must gather diagnostic information](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/vh-missing-selector/#must-gather-diagnostic-information)


_This page applies to**Apigee** and **Apigee hybrid**._
_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._
## Symptom
An `ApigeeIssue` with `Reason` `AIS_VIRTUALHOST_MISSING_SELECTOR` is shown when viewing resources in the `apigee` namespace. 
## Error messages
After running `kubectl -n apigee get apigeeissues`, an error like the following is displayed: 

```
NAME                                           SEVERITY   REASON                             DOCUMENTATION                                                                                  AGE
vhost-missing-selector-my-org-my-virtualhost   ERROR      AIS_VIRTUALHOST_MISSING_SELECTOR   https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_VIRTUALHOST_MISSING_SELECTOR   5h18m
```

## Cause: Virtualhost is missing ingress selector
A virtualhost declared in `overrides.yaml` does not have the ingress selector field set. 
### Diagnosis
Run the following command: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-selector-my-org-my-virtualhost`. 
The output should look similar to the following: 

```
Name:         vhost-missing-selector-my-org-my-virtualhost
Namespace:    apigee
Labels:       ais-reason=AIS_VIRTUALHOST_MISSING_SELECTOR
Annotations:  <none>
API Version:  apigee.cloud.google.com/v1alpha1
Kind:         ApigeeIssue
Metadata:
  Creation Timestamp:  2023-06-12T17:03:43Z
  Generation:          1
  Owner References:
    API Version:     apigee.cloud.google.com/v1alpha2
    Kind:            ApigeeOrganization
    Name:            my-org
    UID:             7e83a52c-ce00-4bed-98be-55835ada1817
  Resource Version:  3281563
  UID:               adc775c2-376d-4bf9-9860-500b2b2b8273
Spec:
  Details:        Expected ingress selector in ApigeeRouteConfig "my-org-my-virtualhost". Environment Group/virtual host "my-virtualhost" is missing an ingress selector.
  Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_VIRTUALHOST_MISSING_SELECTOR
  Reason:         AIS_VIRTUALHOST_MISSING_SELECTOR
  Severity:       WARNING
Events:           <none>
```

```
Spec:
  Details:        Expected ingress selector in ApigeeRouteConfig "my-org-my-virtualhost". Environment Group/virtual host "my-virtualhost" is missing an ingress selector.
```

The contents of `Spec.Details` explains the name of the virtualhost which is missing the ingress selector. 
### Resolution
  1. Use `kubectl describe` to check the details of the issue: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `vhost-missing-selector-my-org-my-virtualhost`. 
  2. Determine the `virtualhost` name from the `Spec.Details` field. 
In this example, the virtualhost is called `my-virtualhost`. 
  3. Find the corresponding virtualhost in your `overrides.yaml`.

```
virtualhosts:
...
- name: my-virtualhost
  sslCertPath: ./certs/vhost.pem
  sslKeyPath: ./certs/vhost.key
...
```

  4. Update the virtualhost and add the ingress selector: 

```
virtualhosts:
...
- name: my-virtualhost
  selector:
    app: apigee-ingressgateway
  sslCertPath: ./certs/vhost.pem
  sslKeyPath: ./certs/vhost.key
...
```

  5. Apply the change to the virtualhost:

```
helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
  --namespace apigee \
  --set envgroup=ENV_GROUP_NAME \
  -f overrides.yaml
```



## Must gather diagnostic information
If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 
  1. The Google Cloud Project ID.
  2. The name of the Apigee hybrid organization.
  3. The `Spec.Details` field of the `ApigeeIssue`.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
