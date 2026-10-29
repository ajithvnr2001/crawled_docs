---
url: https://docs.cloud.google.com/docs/migration/scenarios/container-migration/
title: Containerized application migration \u00a0|\u00a0 Migration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T05:39:35.570320+00:00
---

# Containerized application migration  |  Migration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/migration/scenarios/container-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Guides ](https://docs.cloud.google.com/docs/migration/overview/migrate-modernize-overview)



Send feedback 

#  Containerized application migration Stay organized with collections  Save and categorize content based on your preferences. 

This page provides architectural guidance and operational strategies for migrating existing container workloads or modernizing Java workloads into containers that run on Google Kubernetes Engine (GKE) or Cloud Run.

If you are a cloud architect, application developer, or DevOps engineer, use the information on this page to evaluate containerization pathways, push images to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), and assess and containerize Java workloads by using [Google Cloud Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview).

Before you read this page, you should have an inventory of your containerized and virtualized workloads, and an understanding of your target orchestration and scaling requirements.

## Migration patterns

The following diagram illustrates container modernization paths:

![Flowchart illustrating three container migration paths: deploying existing container images through Artifact Registry, assessing and containerizing Java workloads with Modernization Hub and Antigravity, and migrating serverless functions to Cloud Run.](https://docs.cloud.google.com/docs/migration/images/containerization-patterns.svg)

Each path addresses a specific workload architecture:

  * **Existing container workloads** : if your applications are already packaged as Docker or Open Container Initiative (OCI) images, push them to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) and deploy directly to [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) or [Cloud Run](https://docs.cloud.google.com/run/docs).
  * **Java workloads** : if your Java workloads run on virtual machines, use [Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview) and [Antigravity](https://antigravity.google/) to evaluate transformation paths, refactor environment-specific dependencies, and package Java workloads into containers.
  * **Serverless functions** : if your applications run as AWS Lambda functions, use [Antigravity CLI](https://antigravity.google/product/antigravity-cli) to containerize event handlers into standard HTTP microservices for deployment on [Cloud Run](https://docs.cloud.google.com/run/docs).



## Java workload containerization

[Modernization Hub](https://docs.cloud.google.com/modernize/hub/overview) and AI-assisted refactoring tools help you modernize Java workloads into OCI-compliant container images:

  1. **Refactor and generate manifests** : use [Antigravity](https://antigravity.google/) and the [Antigravity CLI](https://antigravity.google/product/antigravity-cli) to resolve environment-specific blockers and generate standardized Dockerfiles and Kubernetes deployment YAML configurations.
  2. **Deploy to managed runtimes** : build and push container images to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), and run the containerized Java workloads on [GKE](https://docs.cloud.google.com/kubernetes-engine/docs) or [Cloud Run](https://docs.cloud.google.com/run/docs).



## What's next

  * [Mainframe modernization overview](https://docs.cloud.google.com/docs/migration/overview/mainframe-modernization-overview.md)
  * [Migrate containers to GKE](https://docs.cloud.google.com/architecture/migrating-containers-kubernetes-gke)
  * [Migrate Amazon EKS to GKE](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Modernization Hub documentation](https://docs.cloud.google.com/modernize/hub/overview)
  * [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [Cloud Run documentation](https://docs.cloud.google.com/run/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
