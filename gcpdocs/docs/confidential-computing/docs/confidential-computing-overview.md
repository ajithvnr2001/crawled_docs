---
url: https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview/
title: Confidential Computing overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:39.100348+00:00
---

# Confidential Computing overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Computing ](https://docs.cloud.google.com/confidential-computing/docs)



Send feedback 

#  Confidential Computing overview Stay organized with collections  Save and categorize content based on your preferences. 

Confidential Computing helps protect your data in use by keeping it encrypted in memory during processing. Combined with encryption for data at rest and in transit, Confidential VM helps keep your data protected throughout its lifecycle.

A confidential computing environment implements the protection of data in use with a hardware-based trusted execution environment (TEE). A TEE is an isolated area within a processor that helps protect the confidentiality and integrity of code and data loaded inside it. A TEE acts as a safe room for sensitive operations, which mitigates risk to data even if the underlying host system is compromised. This security standard is defined by the [Confidential Computing Consortium](https://confidentialcomputing.io/).

## Example use cases

You can use confidential computing to help achieve the following:

  * **Enhanced privacy** : Perform analysis on sensitive datasets and help protect generative AI workloads (such as user prompts) without exposing data to the host infrastructure, cloud operators, or AI platform providers.

  * **Secure collaboration** : Jointly train machine learning models, run federated learning, or query shared data in a safe room without revealing individual proprietary datasets or intellectual property to other participating parties.

  * **Improved data security** : Mitigate the risk of data breaches during processing by protecting sensitive runtime assets like API keys, session memory, and model reasoning. This mitigation helps you to comply with regulations like the Health Insurance Portability and Accountability Act (HIPAA), the General Data Protection Regulation (GDPR), or digital sovereignty mandates.

  * **Increased trust and transparency** : Provide verifiable proof through cryptographic attestation that calculations, models, and AI agent workloads are running unmodified inside a secure environment.

  * **Intellectual property protection** : Protect the intellectual property of creators when running proprietary models.




## How a confidential computing environment works

Confidential computing environments have the following properties:

  * **Runtime encryption** : The processor keeps all confidential computing environment data encrypted in memory. Any system component or hardware attacker that attempts to read active data directly from memory sees only encrypted data. For supported GPU machine types, runtime encryption extends from the CPU to attached GPUs through NVIDIA Confidential Computing using encrypted PCIe channels.

  * **Isolation** : The processor blocks software-based access to the confidential computing environment. The host operating system, hypervisor, and other applications can't read or modify the confidential computing environment.

  * **Attestation** : [Remote attestation](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview) checks the trustworthiness of the confidential computing environment by verifying its hardware and software integrity.

  * **Data lifecycle security** : For supported machine types, hardware-backed data protection during processing helps ensure that sensitive inputs, intermediate states, and temporary variables are isolated from ingestion to destruction in memory.

  * **Confidential live migration** : For supported machine types, the platform can migrate active Confidential VM instances or nodes to new physical hosts without interruption. Memory remains encrypted, and the platform exchanges cryptographic keys only after verifying that the destination host provides an authorized, attested TEE.




## Confidential VM services

Google Cloud offers the following Confidential VM products:

  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)

  * [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)

  * [Google Cloud Attestation](https://docs.cloud.google.com/confidential-computing/docs/attestation)

  * [Split-trust encryption tool](https://docs.cloud.google.com/confidential-computing/docs/split-trust-encryption-tool)




Confidential VM is also available in the following products:

  * [Dataflow](https://docs.cloud.google.com/dataflow/docs/reference/service-options)

  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/confidential-compute)

  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)

  * [Gemini Enterprise Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-confidential-computing)




## Impact of confidential computing on trust boundaries

Confidential computing on Google Cloud lets you reduce your [trust boundary](https://en.wikipedia.org/wiki/Trust_boundary) so that fewer resources have access to your confidential data. For example, in a Google Cloud environment without Confidential VM, Google Cloud infrastructure and the guest OS are within the trust boundary. In a Google Cloud environment that uses Confidential VM without Confidential Space, the guest OS is within the trust boundary, but the cloud infrastructure isn't.

Elements | Within trust boundary without using Confidential VM | Within trust boundary when using Confidential VM | Within trust boundary when using Confidential Space  
---|---|---|---  
Cloud stack and administrators | Yes | No | No  
BIOS and firmware | Yes | No | No  
Host OS and hypervisor | Yes | No | No  
VM guest administrator | Yes | Yes | No  
VM guest OS | Yes | Yes | Yes, measured and attested  
Applications, models, and AI agents | Yes | Yes | Yes, measured and attested  
Proprietary model weights and algorithms | Yes | Yes | Yes  
Confidential data and prompts | Yes | Yes | Yes  
  
## What's next

  * Learn about [confidential computing for data analytics, AI, and federated learning](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-analytics-ai).
  * Learn about [Google Cloud Attestation](https://docs.cloud.google.com/confidential-computing/docs/attestation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
