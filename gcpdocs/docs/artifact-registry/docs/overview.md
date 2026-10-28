---
url: https://docs.cloud.google.com/artifact-registry/docs/overview/
title: Artifact Registry overview \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:09:41.986397+00:00
---

# Artifact Registry overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/overview/

. [ Skip to main content ](https://docs.cloud.google.com/artifact-registry/docs/overview/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/artifact-registry/docs/overview/)
  * [Deutsch](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=de)
  * [Español](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=es-419)
  * [Français](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=id)
  * [Italiano](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=it)
  * [Português](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=ja)
  * [한국어](https://docs.cloud.google.com/artifact-registry/docs/overview/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fartifact-registry%2Fdocs%2Foverview%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Introduction](https://docs.cloud.google.com/artifact-registry/docs/overview/#introduction)
  * [Dependency management](https://docs.cloud.google.com/artifact-registry/docs/overview/#dependencies)
  * [Software supply chain security](https://docs.cloud.google.com/artifact-registry/docs/overview/#software-supply-chain)
  * [Artifact Registry and Container Registry](https://docs.cloud.google.com/artifact-registry/docs/overview/#transition)
  * [What's next](https://docs.cloud.google.com/artifact-registry/docs/overview/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)


Was this helpful?
Send feedback 
#  Artifact Registry overview Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Introduction](https://docs.cloud.google.com/artifact-registry/docs/overview/#introduction)
  * [Dependency management](https://docs.cloud.google.com/artifact-registry/docs/overview/#dependencies)
  * [Software supply chain security](https://docs.cloud.google.com/artifact-registry/docs/overview/#software-supply-chain)
  * [Artifact Registry and Container Registry](https://docs.cloud.google.com/artifact-registry/docs/overview/#transition)
  * [What's next](https://docs.cloud.google.com/artifact-registry/docs/overview/#whats_next)


Artifact Registry lets you centrally store artifacts and build dependencies as part of an integrated Google Cloud experience.
## Introduction
Artifact Registry provides a single location for storing and managing your packages and Docker container images. You can use Artifact Registry to perform the following tasks:
  * Integrate Artifact Registry with Google Cloud [CI/CD services](https://cloud.google.com/blog/topics/developers-practitioners/devops-and-cicd-google-cloud-explained) or your existing CI/CD tools. 
    * Store artifacts from [Cloud Build](https://docs.cloud.google.com/build/docs).
    * Deploy artifacts to Google Cloud runtimes, including [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs), [Cloud Run](https://docs.cloud.google.com/run/docs), [Compute Engine](https://docs.cloud.google.com/compute/docs), and [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).
    * Identity and Access Management provides consistent credentials and access control.
  * Protect your software supply chain. 
    * Manage container metadata and scan for container vulnerabilities with [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs).
  * [Prewarm images](https://docs.cloud.google.com/artifact-registry/docs/prewarm-images) to reduce cold-start latency for Google Kubernetes Engine workloads using Image streaming.
  * Protect repositories in a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) security perimeter.
  * Create multiple regional repositories within a single Google Cloud project. Group images by team or development stage and control access at the repository level.

Artifact Registry integrates with Cloud Build and other continuous delivery and continuous integration systems to store packages from your builds. You can also store trusted dependencies that you use for builds and deployments. 
## Dependency management
Protecting your software supply chain goes beyond using specific tools. The processes and practices you use to develop, build, and run your software also impact the integrity of your software. To learn more about best practices for dependencies, see [Dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies)
## Software supply chain security
Google Cloud provides a comprehensive and modular set of capabilities and tools that your developers, DevOps, and security teams can use to improve the security posture of your software supply chain.
Artifact Registry provides:
  * Remote repositories to cache dependencies from upstream public sources so that you have greater control over them and can scan them for vulnerabilities, build provenance, and other dependency information.
  * Connector repositories to act as a proxy for upstream sources without caching dependencies. This way, the upstream source is fully auditable and supports policies that prevent artifact caching.
  * Virtual repositories to group remote and private repositories behind a single endpoint. Set a priority on each repository to control search order when downloading or installing an artifact.


You can view security insights about your security posture, build artifacts, and dependencies in Google Cloud console dashboards within Cloud Build, Cloud Run, and GKE.
## Artifact Registry and Container Registry
Artifact Registry expands on the capabilities of Container Registry and is the recommended container registry for Google Cloud. If you use Container Registry, learn about [transitioning from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition-from-gcr) to take advantage of new and improved features. 
## What's next
  * [Docker quickstart](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images)
  * [Go quickstart](https://docs.cloud.google.com/artifact-registry/docs/go/store-go)
  * [Helm quickstart](https://docs.cloud.google.com/artifact-registry/docs/helm/store-helm-charts)
  * [Java quickstart](https://docs.cloud.google.com/artifact-registry/docs/java/store-java)
  * [Node.js quickstart](https://docs.cloud.google.com/artifact-registry/docs/nodejs/store-nodejs)
  * [Python quickstart](https://docs.cloud.google.com/artifact-registry/docs/python/store-python)
  * [Ruby quickstart](https://docs.cloud.google.com/artifact-registry/docs/ruby/quickstart)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
