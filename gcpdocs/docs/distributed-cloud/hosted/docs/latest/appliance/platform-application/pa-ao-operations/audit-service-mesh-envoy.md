---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-service-mesh-envoy/
title: Service Mesh Envoy access logs \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:59:57.684006+00:00
---

# Service Mesh Envoy access logs  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/audit-service-mesh-envoy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Service Mesh Envoy access logs Stay organized with collections  Save and categorize content based on your preferences. 

Envoy sidecar access logs in Google Distributed Cloud (GDC) air-gapped appliance let you monitor and audit service-to-service traffic across the service mesh. Each JSON log entry captures the user identity, request path, protocol, duration, HTTP response code, response flags, and upstream and downstream connection metadata to help you diagnose request failures.

**JSON representation**
    
    
    {
      "key": string,
      "key": string
    }
    

Fields  
---  
`field_name1` |  `string` Description  
`field_name2` |  `string` Description  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
