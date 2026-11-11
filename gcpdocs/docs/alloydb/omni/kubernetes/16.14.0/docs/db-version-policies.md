---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/db-version-policies/
title: Database version policies \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.14.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:48:00.987714+00:00
---

# Database version policies  |  AlloyDB Omni using the container orchestrator: 16.14.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/db-version-policies/

This page documents AlloyDB Omni version **16.14.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/resources)



Send feedback 

#  Database version policies Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.14.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/db-version-policies)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/db-version-policies)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/db-version-policies)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/db-version-policies)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/db-version-policies)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/db-version-policies)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/db-version-policies)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/db-version-policies)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/db-version-policies)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/db-version-policies)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/db-version-policies)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/db-version-policies)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/db-version-policies)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/db-version-policies)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/db-version-policies)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/db-version-policies)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/db-version-policies)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/db-version-policies)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/db-version-policies)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/db-version-policies)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/db-version-policies)



To plan database upgrades and keep your deployments running on supported PostgreSQL releases, review the support, retirement, and compatibility policies for AlloyDB Omni major and minor versions and the AlloyDB Omni Kubernetes operator.

For information about AlloyDB for PostgreSQL version policies, see [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

## AlloyDB Omni version policies

Every version of AlloyDB Omni is compatible with a specific version of PostgreSQL, as detailed in Support policy.

Because AlloyDB Omni is software that you install and run yourself, you are responsible for regularly updating your AlloyDB Omni installation. Learn about the latest versions of AlloyDB Omni in the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/release-notes).

For AlloyDB Omni, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility. Some AlloyDB Omni releases are updates to AlloyDB Omni itself, independent of updates to PostgreSQL support. These releases include bug fixes and security updates and are reflected in an incremental increase of the third number in the release version. For example, the `2` in `18.1.2` indicates an update to AlloyDB Omni.

## Support policy

Google provides support for AlloyDB Omni versions and the AlloyDB Omni operator based on the following timelines:

Version type | Support period  
---|---  
Major versions | Supported for 5 years from the initial release date, matching the community support lifecycle of the underlying PostgreSQL version.  
Minor versions | Supported for 1.5 years from their specific release date.  
Kubernetes operator versions | Supported for 1 year from their specific release date. For operator release and end-of-support dates, see Supported Kubernetes operator versions and the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/release-notes).  
  
## Major version support timeline

The general availability (GA) dates serve as the initial release dates for calculating the 5-year support window. The following table lists the GA dates and end-of-support dates for AlloyDB Omni PostgreSQL major versions:

PostgreSQL major version | GA date | End-of-support date  
---|---|---  
18 | April 9, 2026 | April 9, 2031  
17 | December 15, 2025 | December 15, 2030  
16 | April 8, 2025 | April 8, 2030  
15 | October 11, 2023 | October 11, 2028  
  
After a version exceeds its support period, it is considered retired. Google doesn't process support tickets for retired versions and recommends that you upgrade to a supported version to continue receiving assistance.

## Supported PostgreSQL versions

For the Common Vulnerabilities and Exposures (CVEs) tracked across database releases, see the [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/docs/security-bulletins). Because the AlloyDB Omni operator manages database clusters up to 1 year old, database versions older than 1 year are retired on Kubernetes deployments. For more information, see Supported Kubernetes operator versions.

The following table lists the AlloyDB Omni minor versions, their compatible PostgreSQL versions, release dates, 1.5-year end-of-support dates, and support status:

AlloyDB Omni version | PostgreSQL version | Release date | End-of-support date | Status  
---|---|---|---|---  
18.4.0 | 18.4 | October 13, 2026 | April 13, 2028 | Supported  
18.3.0 | 18.3 | July 15, 2026 | January 15, 2028 | Supported  
18.1.0 | 18.1 | April 9, 2026 | October 9, 2027 | Supported  
17.10.0 | 17.10 | October 13, 2026 | April 13, 2028 | Supported  
17.9.0 | 17.9 | July 15, 2026 | January 15, 2028 | Supported  
17.7.0 | 17.7 | April 9, 2026 | October 9, 2027 | Supported  
17.5.0 | 17.5 | December 15, 2025 | June 15, 2027 | Supported  
16.14.0 | 16.14 | October 13, 2026 | April 13, 2028 | Supported  
16.13.0 | 16.13 | July 15, 2026 | January 15, 2028 | Supported  
16.11.0 | 16.11 | April 9, 2026 | October 9, 2027 | Supported  
16.9.0 | 16.9 | December 15, 2025 | June 15, 2027 | Supported  
16.8.0 | 16.8 | July 23, 2025 | January 23, 2027 | Retired  
16.3.0 | 16.3 | April 8, 2025 | October 8, 2026 | Retired  
15.18.0 | 15.18 | October 13, 2026 | April 13, 2028 | Supported  
15.17.0 | 15.17 | July 15, 2026 | January 15, 2028 | Supported  
15.15.0 | 15.15 | April 9, 2026 | October 9, 2027 | Supported  
15.13.0 | 15.13 | December 15, 2025 | June 15, 2027 | Supported  
15.12.0 | 15.12 | July 23, 2025 | January 23, 2027 | Retired  
15.7.1 | 15.7 | April 8, 2025 | October 8, 2026 | Retired  
15.7.0 | 15.7 | November 8, 2024 | May 8, 2026 | Retired  
  
## Supported Kubernetes operator versions

Because the AlloyDB Omni operator is supported for 1 year and manages database clusters up to 1 year old, running a database cluster on Kubernetes requires both a supported database version and a supported operator version. For the full matrix of compatible control plane agent versions, see [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/choose-compatible-versions#compatibility-table). For CVEs tracked across operator and control plane container images, see the [AlloyDB Omni on Kubernetes security bulletin](https://docs.cloud.google.com/alloydb/omni/docs/security-bulletins).

The following table lists the AlloyDB Omni operator versions, their release dates, 1-year end-of-support dates, compatible AlloyDB Omni database versions, and support status:

AlloyDB Omni operator version | Release date | End-of-support date | Compatible AlloyDB Omni database versions | Status  
---|---|---|---|---  
1.9.0 (recommended) | October 13, 2026 | October 13, 2027 | 18.4.0, 17.10.0, 16.14.0, 15.18.0 (recommended)  
18.3.0, 17.9.0, 16.13.0, 15.17.0  
18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.8.2 | October 5, 2026 | October 5, 2027 | 18.3.0, 17.9.0, 16.13.0, 15.17.0  
18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.8.1 | August 25, 2026 | August 25, 2027 | 18.3.0, 17.9.0, 16.13.0, 15.17.0  
18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.8.0 | July 15, 2026 | July 15, 2027 | 18.3.0, 17.9.0, 16.13.0, 15.17.0  
18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.7.1 | June 3, 2026 | June 3, 2027 | 18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.7.0 | April 9, 2026 | April 9, 2027 | 18.1.0, 17.7.0, 16.11.0, 15.15.0  
17.5.0, 16.9.0, 15.13.0 | Supported  
1.6.3 | March 5, 2026 | March 5, 2027 | 17.5.0, 16.9.0, 15.13.0  
16.8.0, 15.12.0  
15.7.1 | Supported  
1.6.2 | February 25, 2026 | February 25, 2027 | 17.5.0, 16.9.0, 15.13.0  
16.8.0, 15.12.0  
15.7.1 | Supported  
1.6.1 | February 13, 2026 | February 13, 2027 | 17.5.0, 16.9.0, 15.13.0  
16.8.0, 15.12.0  
15.7.1 | Supported  
1.6.0 | December 15, 2025 | December 15, 2026 | 17.5.0, 16.9.0, 15.13.0  
16.8.0, 15.12.0  
15.7.1 | Supported  
1.5.0 | July 23, 2025 | July 23, 2026 | 16.8.0, 15.12.0  
16.3.0, 15.7.1 | Retired  
1.4.1 | May 27, 2025 | May 27, 2026 | 16.3.0, 15.7.1  
15.7.0 | Retired  
1.4.0 | April 8, 2025 | April 8, 2026 | 16.3.0, 15.7.1  
15.7.0 | Retired  
  
## Patch policy

To help maintain the security and stability of your environment, Google applies patches for critical bugs and vulnerabilities according to the following policy:

  * Google applies patches only to the latest minor version of each supported major version.
  * If you encounter an issue on an older minor version, you must upgrade to the latest available minor version of that major version to receive the fix.
  * Starting with AlloyDB Omni 16.9.0, 17.5.0, and 18.1.0, Google publishes database container images on both Red Hat Universal Base Image 9 (UBI 9) and Debian 12 (`bookworm`) tracks. UBI 9 images use the `-ubi9` tag suffix for standalone container pulls and are used by default in Kubernetes deployments. When a newer minor or patch version is released, Google marks superseded container image digests as deprecated. Always pull images that correspond to the latest supported release.
  * For information about CVEs addressed in AlloyDB Omni database container images and the AlloyDB Omni operator, see [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/docs/security-bulletins).



## Upgrade and compatibility

AlloyDB Omni version numbers use the format `MAJOR_VERSION.MINOR_VERSION.OMNI_PATCH_VERSION` to indicate the supported PostgreSQL version. The major and minor version numbers match the version of the underlying PostgreSQL engine, and the third number represents the AlloyDB Omni patch version.

The following table summarizes the upgrade and compatibility policies for AlloyDB Omni:

Policy category | Description  
---|---  
Major version timing | Google aims to support new PostgreSQL major versions within eight months of the release of the first minor release, version x.1, of a new PostgreSQL major version. For AlloyDB Omni in Google Distributed Cloud, Google aims to support compatibility with a new major PostgreSQL version within four months of its availability in AlloyDB Omni.  
Minor version timing | Google aims to release support for new PostgreSQL minor versions every quarter. Because AlloyDB Omni is software that you install and run yourself, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility.  
Upgrade order | For Kubernetes deployments, you must upgrade the AlloyDB Omni operator before upgrading your database clusters (data planes).  
Security updates | Google aims to release fixes within one month of a PostgreSQL community security release.  
Operator compatibility | For Kubernetes deployments, the operator is designed to manage data plane clusters up to 1 year old.  
Upgrade path | 

  * You can skip minor or patch versions during an upgrade if the version gap doesn't exceed the 1.5-year support period, or the 1-year operator compatibility period for AlloyDB Omni operator deployments.
  * You can roll back only to the version that you used immediately before the upgrade.

  
  
## Data protection

The AlloyDB Omni operator doesn't perform automatic backups before an upgrade. You are responsible for taking a manual backup of your data before triggering an upgrade process.

## What's next

  * Review the [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/docs/security-bulletins).
  * [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/choose-compatible-versions).
  * Read the [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 
