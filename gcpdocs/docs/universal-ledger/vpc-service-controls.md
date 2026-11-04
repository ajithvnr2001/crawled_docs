---
url: https://docs.cloud.google.com/universal-ledger/vpc-service-controls/
title: Configure VPC Service Controls \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:35:53.138738+00:00
---

# Configure VPC Service Controls  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to configure [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for Universal Ledger to enhance security and help mitigate data exfiltration risks.

VPC Service Controls provides an extra layer of defense for Google Cloud services that is independent of Identity and Access Management (IAM). By configuring a service perimeter, you can restrict access to the Universal Ledger API to authorized requests, such as those originating from within your Virtual Private Cloud networks or authorized IP addresses using the restricted VIP.

## Protect Universal Ledger with a service perimeter

To protect Universal Ledger resources using VPC Service Controls:

  1. **Add the API to the perimeter:** Include the Universal Ledger API (`universalledger.googleapis.com`) in the list of restricted services within your service perimeter. For instructions, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) or [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

  2. **Route requests through the restricted VIP:** Configure private connectivity such that requests to `universalledger.googleapis.com` are routed to the restricted VIP (`restricted.googleapis.com`). For details on configuring DNS records and routes, see [Set up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity).




## Limitations and security considerations

The following sections describe the limitations and security considerations for using VPC Service Controls with Universal Ledger.

### Shared ledger and transaction data

The Universal Ledger API operates on shared, multi-tenant networks where data submitted to the ledger is classified as _Transaction Data_. Under the service-specific terms, Transaction Data—which includes transaction payloads, public keys, and cryptographic signatures—is explicitly excluded from the definition of Customer Data.

Because of the shared nature of the ledger network, Transaction Data submitted to the ledger becomes accessible to all authorized ledger participants. Consequently, this data cannot be restricted or contained by an individual organization's VPC Service Controls perimeter configuration.

### Data exfiltration mitigation

Although VPC Service Controls protects API ingress and egress traffic, it does not enforce data visibility after transactions are committed to the shared ledger.

To help prevent data exfiltration, use IAM deny policies to restrict methods that modify or publish data, such as `universalledger.endpoints.submitTransaction`. This approach blocks unauthorized users from publishing data from inside the perimeter while still permitting read-only queries.

For more information, see the [Universal Ledger entry](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_universal_ledger) in the VPC Service Controls supported products and limitations documentation.

## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Follow best practices in [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).
  * Learn how to [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters).
  * Review [Universal Ledger audit logging](https://docs.cloud.google.com/universal-ledger/audit-logging). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
