---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/
title: Ingress mTLS CA cert invalid \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:59:29.945866+00:00
---

# Ingress mTLS CA cert invalid  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/

[ Skip to main content ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/)
  * [Deutsch](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=de)
  * [Español](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=es-419)
  * [Français](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=id)
  * [Italiano](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=it)
  * [Português](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=ja)
  * [한국어](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/apigee-color.svg) ](https://docs.cloud.google.com/apigee/docs)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Symptom](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#symptom)
  * [Error messages](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#error-messages)
  * [Possible causes](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#possible-causes)
  * [Cause: Ingress mTLS CA certificate is not PEM-encoded](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#not-pem)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#diagnosis)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#resolution)
  * [Cause: Ingress mTLS CA certificate is malformed](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#malformed)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#diagnosis_1)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#resolution_1)
  * [Must gather diagnostic information](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#must-gather-diagnostic-information)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)


Send feedback 
#  Ingress mTLS CA cert invalid Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Symptom](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#symptom)
  * [Error messages](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#error-messages)
  * [Possible causes](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#possible-causes)
  * [Cause: Ingress mTLS CA certificate is not PEM-encoded](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#not-pem)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#diagnosis)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#resolution)
  * [Cause: Ingress mTLS CA certificate is malformed](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#malformed)
    * [Diagnosis](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#diagnosis_1)
    * [Resolution](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#resolution_1)
  * [Must gather diagnostic information](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#must-gather-diagnostic-information)


_This page applies to**Apigee** and **Apigee hybrid**._
_There is no equivalent[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/get-started) documentation for this topic._
## Symptom
An `ApigeeIssue` with `Reason` `AIS_INGRESS_MTLS_CA_CERT_INVALID` is shown when viewing resources in the `apigee` namespace. 
## Error messages
After running `kubectl -n apigee get apigeeissues`, an error like the following is displayed: 

```
NAME                                    SEVERITY   REASON                             DOCUMENTATION                                                                                  AGE
ca-cert-invalid-my-org-my-virtualhost   ERROR      AIS_INGRESS_MTLS_CA_CERT_INVALID   https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_MTLS_CA_CERT_INVALID   5h18m
```

## Possible causes  
| Cause  | Description  |  
| --- | --- |  
| [Ingress mTLS CA certificate is not PEM-encoded](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#not-pem)  | The configured ingress mTLS CA certificate is not PEM-encoded.  |  
| [Ingress mTLS CA certificate is malformed](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ca-cert-invalid/#malformed)  | The configured ingress mTLS CA certificate is malformed.  |  
## Cause: Ingress mTLS CA certificate is not PEM-encoded
The ingress mTLS CA certificate stored in the Kubernetes secret referenced by an `ApigeeRouteConfig` is missing the PEM-encoding text blocks (or they are malformed). 
### Diagnosis
Run the following command: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `ca-cert-invalid-my-org-my-virtualhost`. 
The output should look similar to the following: 

```
Name:         ca-cert-invalid-my-org-my-virtualhost
Namespace:    apigee
Labels:       ais-reason=AIS_INGRESS_MTLS_CA_CERT_INVALID
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
  Details:        CA certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is not PEM encoded
  Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_MTLS_CA_CERT_INVALID
  Reason:         AIS_INGRESS_MTLS_CA_CERT_INVALID
  Severity:       ERROR
Events:           <none>
```

```
Spec:
  Details:        CA certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is not PEM encoded
```

The contents of `Spec.Details` explains the name of the `ApigeeRouteConfig` that refers to the Kubernetes secret containing the ingress mTLS CA certificate which is not PEM-encoded. 
### Resolution
  1. Use `kubectl describe` to display the name of the `ApigeeRouteConfig` which has the ingress mTLS CA cert which is not PEM-encoded: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `ca-cert-invalid-my-org-my-virtualhost`. 
In this example, the `ApigeeRouteConfig` `my-org-my-virtualhost` is referencing the secret `my-org-my-virtualhost`. 
  2. Determine the `virtualhost` name from the `ApigeeRouteConfig`. 
The `ApigeeRouteConfig`'s name is in the format: `<Apigee organization>-<virtualhost name>`. 
In this example, `my-org` is the Apigee organization and the virtualhost name is `my-virtualhost`. 
  3. Find the corresponding virtualhost in your `overrides.yaml`.

```
virtualhosts:
...
- name: my-virtualhost
  selector:
    app: apigee-ingressgateway
  caCertPath: ./certs/ca.pem
  sslCertPath: ./certs/vhost.pem
  sslKeyPath: ./certs/vhost.key
...
```

  4. Validate the contents of the file provided via the path declared in `caCertPath`. Ensure the content contains the required starting and ending certificate blocks. For example: 

```
-----BEGIN CERTIFICATE-----
MIIDYTCCAkmgAwIBAgIUSXeU0pQYRFzYlqZpKhNNJdBLFBIwDQYJKoZIhvcNAQEL
... <contents omitted> ...
eWJyaWQuZTJlLmFwaWdlZWtzLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
MMM=
-----END CERTIFICATE-----
```

  5. Once the contents and format of the file have been fixed, apply the change to the virtualhost: 

```
helm upgrade ENV_GROUP_NAME apigee-virtualhost/ \
  --namespace apigee \
  --set envgroup=ENV_GROUP_NAME \
  -f overrides.yaml
```



## Cause: Ingress mTLS CA certificate is malformed
The ingress mTLS CA certificate stored in the Kubernetes secret referenced by an `ApigeeRouteConfig` is malformed. 
### Diagnosis
Run the following command: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `ca-cert-invalid-my-org-my-virtualhost`. 
The output should look similar to the following: 

```
Name:         ca-cert-invalid-my-org-my-virtualhost
Namespace:    apigee
Labels:       ais-reason=AIS_INGRESS_MTLS_CA_CERT_INVALID
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
  Details:        CA certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is invalid
  Documentation:  https://cloud.google.com/apigee/docs/hybrid/troubleshooting/AIS_INGRESS_MTLS_CA_CERT_INVALID
  Reason:         AIS_INGRESS_MTLS_CA_CERT_INVALID
  Severity:       ERROR
Events:           <none>
```

```
Spec:
  Details:        CA certificate in secret "my-org-my-virtualhost" for ApigeeRouteConfig "my-org-my-virtualhost" is invalid
```

The contents of `Spec.Details` explains the name of the `ApigeeRouteConfig` that refers to the Kubernetes secret containing the ingress mTLS CA certificate which is malformed and failed to parse. 
### Resolution
  1. Use `kubectl describe` to display the name of the `ApigeeRouteConfig` which has the ingress mTLS CA cert which is malformed: 

```
kubectl -n apigee describe apigeeissue ISSUE_NAME
```

Where ISSUE_NAME is the name of the issue. For example, `ca-cert-invalid-my-org-my-virtualhost`. 
In this example, the `ApigeeRouteConfig` `my-org-my-virtualhost` is referencing the secret `my-org-my-virtualhost`. 
  2. Determine the `virtualhost` name from the `ApigeeRouteConfig`. 
The `ApigeeRouteConfig`'s name is in the format: `<Apigee organization>-<virtualhost name>`. 
In this example, `my-org` is the Apigee organization and the virtualhost name is `my-virtualhost`. 
  3. Find the corresponding virtualhost in your `overrides.yaml`.

```
virtualhosts:
...
- name: my-virtualhost
  selector:
    app: apigee-ingressgateway
  caCertPath: ./certs/ca.pem
  sslCertPath: ./certs/vhost.pem
  sslKeyPath: ./certs/vhost.key
...
```

  4. Validate the contents of the file provided via the path declared in `caCertPath`. Ensure the contents contain the entire certificate. For example: 

```
-----BEGIN CERTIFICATE-----
MIIDYTCCAkmgAwIBAgIUSXeU0pQYRFzYlqZpKhNNJdBLFBIwDQYJKoZIhvcNAQEL
BQAwQDE+MDwGA1UEAww1bWF4bWlsbGlvbi1oeWJyaWQtc3RhZ2luZy1kZXYuaHli
... <contents omitted> ...
0TPPaik8U9dtFXMGT1DJkjPRPO0Jw5rlU8DKlNA/Kkv52aKJZNwB/cwmvoa/BFji
PIPa9wY=
-----END CERTIFICATE-----
```

  5. Once the contents and format of the file have been fixed, apply the change to the virtualhost: 

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
  4. (optional) File referenced by `caCertPath` for the affected virtualhost. 


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
