---
url: https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-analytics-ai/
title: Confidential Computing for data analytics, AI, and federated learning \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:10:16.322278+00:00
---

# Confidential Computing for data analytics, AI, and federated learning  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-analytics-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Computing ](https://docs.cloud.google.com/confidential-computing/docs)



Send feedback 

#  Confidential Computing for data analytics, AI, and federated learning Stay organized with collections  Save and categorize content based on your preferences. 

Confidential Computing lets you collaborate on sensitive data, train AI models, and run federated learning workloads while keeping data encrypted in memory. This document describes industry use cases and reference architectures for confidential analytics, AI, and federated learning on Google Cloud.

## Use cases

The following sections provide examples of Confidential Computing use cases for various industries.

### Healthcare and life sciences

Confidential Computing enables secure data sharing and analysis across organizations while helping to preserve patient privacy. Confidential Computing lets healthcare organizations participate in collaborative research, disease modeling, drug discovery, and personalized treatment plans.

The following table describes some example uses for Confidential Computing in healthcare.

Use case | Description  
---|---  
Disease prediction and early detection | Hospitals train a [federated learning model](https://services.google.com/fh/files/misc/duality_case_study_v3.pdf) to detect cancerous lesions from medical imaging data (for example, MRI scans or CT scans across multiple hospitals or hospital regions) while maintaining patient confidentiality.  
Real-time patient monitoring | Healthcare providers analyze data from wearable health devices and mobile health apps for real-time monitoring and alerts. For example, wearable devices collect data on glucose levels, physical activity, and dietary habits to provide personalized recommendations and early warnings for blood sugar fluctuations.  
Collaborative drug discovery and clinical trials | Pharmaceutical companies and research hospitals pool clinical trial data, genomic sequences, and molecular structures to discover therapies and model drug interactions.  
Autonomous clinical documentation and medical transcription | AI assistants capture clinician-patient conversations to draft clinical summaries, update electronic health records (EHRs), and suggest billing codes.  
Multi-institutional medical AI evaluation and benchmarking | Healthcare institutions and research consortiums [validate proprietary diagnostic models](https://cloud.google.com/blog/products/identity-security/privacy-first-medical-ai-with-medperf-and-google-cloud) across diverse, global patient populations without moving or exposing raw clinical data.  
  
### Financial services

Confidential Computing lets financial institutions create a more secure and resilient financial system.

The following table describes some example uses for Confidential Computing in financial services.

Use case | Description  
---|---  
Fraud detection and anti-money laundering (AML) | Multiple financial institutions [share sensitive transaction flows](https://cloud.google.com/blog/products/identity-security/google-cloud-and-swift-pioneer-advanced-ai-and-federated-learning-tech) and fraud indicators to train machine learning models or deploy analytical agents. By using this collected data, institutions can detect cross-border laundering syndicates and payment fraud without revealing customer account numbers or proprietary transaction records to competitors.  
Credit risk assessment and underwriting | Lenders evaluate commercial or retail credit applications by analyzing sensitive, non-traditional financial data (such as real-time utility payments) without exposing that data to external parties. Running automated underwriting agents in a trusted execution environment (TEE) helps isolate an applicant's financial records and the bank's proprietary risk-scoring algorithms during evaluation.  
Automated financial analysis and regulatory reporting | Autonomous AI agents search internal corporate ledgers, investment portfolios, and material nonpublic information (MNPI) to prepare due diligence memos, audit reports, and regulatory filings.  
  
### Public sector

Confidential Computing lets governments create more transparent, efficient, and effective services, while retaining control and sovereignty of their data.

The following table describes some example uses for Confidential Computing in the public sector.

Use case | Description  
---|---  
Multi-agency confidential analytics | Confidential Computing enables multi-party data analytics across multiple government agencies (for example, health, tax, and education) or across multiple governments in different regions or countries. Confidential computing helps ensure that trust boundaries and data privacy are protected, while enabling data analytics (by using data loss prevention (DLP), large-scale analytics, and policy engines) and AI training and serving.  
Cross-agency investigative analytics and intelligence sharing | Separate government bodies (such as tax, law enforcement, and customs agencies) use Confidential Space to perform joint data analysis. Agencies can cross-reference tax filings, travel manifests, and financial records to identify fraud or national security threats without sharing raw, classified databases across jurisdictional boundaries.  
Digital identity and citizen credential verification | [Public agencies and identity platforms](https://services.google.com/fh/files/misc/self_case_study.pdf) verify official biometric passports and national IDs without storing or exposing citizen personal data. Citizens can cryptographically prove specific attributes (such as nationality, residency, or age eligibility) while raw passport data and biometric signatures remain encrypted in memory and are deleted after proof generation.  
  
### Supply chain

Confidential Computing lets organizations that manage supply chains and sustainability programs collaborate and share insights while helping to maintain data privacy.

The following table describes some example uses for Confidential Computing in supply chains.

Use case | Description  
---|---  
Autonomous multi-party logistics and shipping orchestration | Organizations deploy autonomous AI agents to negotiate shipping rates, coordinate container handoffs, and reroute cargo with external carriers during transit disruptions. Running these logistics agents inside a Confidential VM instance helps protect active shipping manifests, carrier pricing agreements, and carrier API credentials from being exposed in memory to other cloud tenants.  
Real-time supply chain anomaly detection and route optimization | AI agents process real-time telemetry (such as GPS transit logs, warehouse gate sensors, and weather alerts) to optimize shipping lanes. Processing this sensitive operational telemetry inside Confidential Space lets manufacturers and distributors run automated rerouting algorithms without exposing proprietary factory capacities or bottleneck vulnerabilities to external parties.  
Automated customs compliance and trade documentation | AI agents process high-value commercial invoices, bills of lading, and customs declarations to automate border compliance. Isolating these document-parsing agents inside a TEE helps protect sensitive trade secrets while they are being extracted and verified against customs databases.  
  
### Digital advertising

Instead of using third-party cookies, digital advertising increasingly uses privacy-enhanced alternatives that use TEEs to help advertising firms process their data in a secure environment. For example, [Google Ads](https://blog.google/products/ads-commerce/google-confidential-matching-data-privacy/) uses Confidential Computing to help protect first-party data when running campaigns.

You can use [TEEs](https://github.com/googleads/conf-data-processing-architecture-reference/blob/main/docs/TrustedExecutionEnvironmentsArchitecturalReference.md) in the following digital advertising use cases:

  * **Matching algorithms:** Finding correspondences or relationships within datasets.
  * **Attribution:** Linking effects or events back to their likely causes.
  * **Aggregation:** Calculating summaries or statistics from the raw data.



## Reference architectures

You can implement Confidential Computing on Google Cloud to address the following use cases:

  * Confidential analytics
  * Confidential AI
  * Confidential federated learning



The following sections provide more information about the architecture for these use cases, including examples for financial and healthcare businesses.

### Confidential analytics architecture for healthcare institutions

The confidential analytics architecture demonstrates how multiple healthcare institutions (such as healthcare providers, biopharmaceutical companies, and research institutions) can work together to accelerate drug research. This architecture uses Confidential Computing techniques to create a digital clean room for running confidential collaborative analytics.

This architecture has the following benefits:

  * **Enhanced insights:** Collaborative analytics lets health organizations gain broader insights and decrease time to market for enhanced drug discovery.
  * **Data privacy:** Sensitive patient and clinical trial data remains encrypted in transit, at rest, and in memory, and isn't exposed in plaintext to other participants or the cloud provider.
  * **Regulatory compliance:** The architecture helps health institutions comply with data protection regulations by maintaining strict control over their data.
  * **Trust and collaboration:** The architecture enables secure collaboration between competing institutions, fostering a collective effort to discover drugs.



The following diagram shows this architecture.

![Diagram of confidential analytics architecture for healthcare institutions.](https://docs.cloud.google.com/static/confidential-computing/docs/images/confidential-computing-analytics-architecture.svg)

The key components in this architecture include the following:

  * **Confidential Space workload (TEE):** A secure, isolated environment where data and code within the TEE are protected from unauthorized access, even from the underlying operating system or cloud provider.
  * **Collaboration partners:** Each participating health institution has a local environment that acts as an intermediary between the institution's private data and the TEE.
  * **Provider-specific encrypted data:** Each healthcare institution stores its own private, encrypted patient data that includes electronic health records. Each provider releases its data (and access to decryption keys) to the TEE only after validating the attestation claims of the TEE workload. The data is decrypted only inside the attested TEE during processing and remains encrypted in memory.
  * **Analytics client:** Participating health institutions can run confidential queries against their data to gain insights.



### Confidential AI architecture for financial institutions

This architectural pattern demonstrates how financial institutions can collaboratively train a fraud detection model while using fraud labels to preserve the confidentiality of their sensitive transaction data. The architecture uses Confidential Computing techniques to enable secure, multi-party machine learning.

This architecture has the following benefits:

  * **Enhanced fraud detection:** Collaborative training uses a larger, more diverse dataset, leading to a more accurate and effective fraud detection model.
  * **Data privacy:** Sensitive transaction data remains encrypted in transit, at rest, and in memory, and isn't exposed in plaintext to other participants or the cloud provider.
  * **Regulatory compliance:** The architecture helps financial institutions comply with data protection regulations by maintaining strict control over their data.
  * **Trust and collaboration:** This architecture enables secure collaboration between competing institutions, fostering a collective effort to combat financial fraud.



The following diagram shows this architecture.

![Diagram of confidential AI architecture for financial institutions.](https://docs.cloud.google.com/static/confidential-computing/docs/images/confidential-computing-financial-architecture.svg)

The key components of this architecture include the following:

  * **Confidential Space workload (TEE):** A secure, isolated environment where data and code within the TEE are protected from unauthorized access, even from the underlying operating system or cloud provider.
  * **Collaboration partners:** Each participating financial institution has a local environment that acts as an intermediary between the institution's private data and the TEE.
  * **Bank-specific encrypted data:** Each bank holds its own private, encrypted transaction data that includes fraud labels. Each bank releases its data (and access to decryption keys) to the TEE only after validating the attestation claims of the TEE workload. The data is decrypted only inside the attested TEE during processing and remains encrypted in memory.
  * **Proprietary model repository:** A pre-trained fraud detection model that serves as the starting point for collaborative training.
  * **Global fraud-trained model and weights (shown by the outbound green arrows from the TEE to each bank):** The improved fraud detection model, along with its learned weights, is securely exchanged back to the participating banks. They can then deploy this enhanced model locally for fraud detection on their own transactions.



### Confidential federated learning architecture for financial institutions

Federated learning offers an advanced solution for customers who value stringent data privacy and data sovereignty. The confidential federated learning architecture provides a secure, scalable, and efficient way to use data for AI applications. This architecture brings the models to the location where the data is stored, rather than centralizing the data in a single location, thereby reducing the risks associated with data leakage.

This architectural pattern demonstrates how multiple financial institutions can collaboratively train a fraud detection model while preserving the confidentiality of their sensitive transaction data with fraud labels. It uses federated learning along with Confidential Computing techniques to enable secure, multi-party machine learning without training data movement.

This architecture has the following benefits:

  * **Enhanced data privacy and security:** Federated learning enables data privacy and data locality by keeping sensitive data at each site. Additionally, financial institutions can use privacy-preserving techniques such as homomorphic encryption and differential privacy filters to further protect any transferred data (such as the model weights).
  * **Improved accuracy and diversity:** By training with a variety of data sources across different clients, financial institutions can develop a robust and generalizable global model to better represent heterogeneous datasets.
  * **Scalability and network efficiency:** With the ability to perform training at the edge, institutions can scale federated learning globally. Additionally, institutions need to transfer only the model weights rather than entire datasets, which enables efficient use of network resources.



The following diagram shows this architecture.

![Diagram of confidential federated learning architecture.](https://docs.cloud.google.com/static/confidential-computing/docs/images/confidential-computing-fl-architecture.svg)

The key components of this architecture include the following:

  * **Federated server in the TEE cluster:** A secure, isolated environment where the federated learning server orchestrates the collaboration of multiple clients by first sending an initial model to the federated learning clients. The clients perform training on their local datasets, then send the model updates back to the federated learning server for aggregation to form a global model.
  * **Federated learning model repository:** A pre-trained fraud detection model that serves as the starting point for federated learning.
  * **Local application inference engine:** An application that executes tasks, performs local computation and learning with local datasets, and submits results back to the federated learning server for secure aggregation.
  * **Local private data:** Each bank holds its own private, encrypted transaction data that includes fraud labels. This raw data never leaves the bank's local environment, which helps protect data privacy.
  * **Secure aggregation protocol (shown by the inbound dotted blue arrows from each bank to the TEE cluster):** The federated learning server doesn't need to access any individual bank's update to train the model. The server requires only the element-wise weighted averages of the update vectors, taken from a random subset of banks or sites. By using a secure aggregation protocol to compute these weighted averages, the server learns only the aggregated model updates from the selected subset rather than which specific bank contributed a given update. This approach helps preserve the privacy of each participant in the federated learning process.
  * **Global fraud-trained model and aggregated weights (shown by the outbound green arrows from the TEE cluster to each bank):** The improved fraud detection model, along with its learned weights, is securely sent back to the participating banks. The banks can then deploy this enhanced model locally for fraud detection on their own transactions.



## What's next

  * Implement [Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview) and [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) in your environment.
  * Learn more about the [fundamentals of Confidential Computing on Google Cloud](https://codelabs.developers.google.com/codelabs/confidential-space#0).
  * Learn how to [secure an ML model in Confidential Space](https://codelabs.developers.google.com/codelabs/secure-ml-model-confidential-space#0).
  * Read about [privacy-first medical AI with MedPerf and Google Cloud](https://cloud.google.com/blog/products/identity-security/privacy-first-medical-ai-with-medperf-and-google-cloud).
  * Read about [powering the next era of confidential AI](https://cloud.google.com/blog/products/identity-security/powering-the-next-era-of-confidential-ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
