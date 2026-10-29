---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Confidential Space \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:13.900605+00:00
---

# Security bulletins  |  Confidential Space  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Resources ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/get-support)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Confidential Space.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://docs.cloud.google.com/feeds/confidential-space-security-bulletins.xml`



## GCP-2026-071

**Published:** 2026-10-28

### Description

Description | Severity | Notes  
---|---|---  
Google has been notified of compromised private keys associated with third-party eMudhra (emSign) subordinate Certificate Authority (CA) certificates. These certificates are present in operating system certificate stores, including Container-Optimized OS (COS), which is used by Confidential Space.  For full details of the vulnerability, see the original [security bulletin](https://docs.cloud.google.com/support/bulletins#gcp-2026-071). 

#### What should I do?

We recommend updating to the latest Confidential Space image (261001) immediately. This image removes the compromised CA certificates from the OS trust store.  Google Cloud changes how it treats images older than version 261001 after the following dates: 

  * **November 9, 2026** :
    * Google Cloud Attestation stops sending attestation tokens to Confidential Space images older than version 260701. 
    * Intel Trust Authority stops sending attestation tokens to Confidential Space images older than version 261001. 
  * **January 11, 2027** : The `STABLE` [ support attribute](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images#image-lifecycle) is removed from Confidential Space image versions 260701–261000. 

You can run the following gcloud CLI command to identify which Confidential Space image you are running across your VM instances: 
    
    
    gcloud compute disks list \
        --filter="sourceImage ~ 'confidential-space'" \
        --format="table(name, users[0], sourceImage)"

#### How to update workloads

  * **Zero-downtime migration (recommended)** : If you're running live production workloads, you can use Managed Instance Groups (MIGs) to update your environment. Read more about [ deploying Confidential Space workloads with MIGs](https://codelabs.developers.google.com/codelabs/confidential-space-mig). 
  * **Manual recreation** :
    1. Stop and delete your active Confidential Space VM instances. 
    2. [ Create new Confidential Space VM instances](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads) with the `--image-family=confidential-space` flag to use the latest image. 



#### How to update relying parties

We recommend adding the following [ access policy](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources#attestation-policy) to check for newer versions of the Confidential Space image: 
    
    
    int(assertion.swversion[0]) >= 260701

| Medium | 

  * [CVE-2026-111943](https://nvd.nist.gov/vuln/detail/CVE-2026-111943)

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
