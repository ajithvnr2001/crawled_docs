---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/db-version-policies/
title: Database version policies \u00a0|\u00a0 AlloyDB Omni using RPM: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:54:17.005139+00:00
---

# Database version policies  |  AlloyDB Omni using RPM: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/db-version-policies/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/resources)



Send feedback 

#  Database version policies Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/db-version-policies)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/db-version-policies)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/db-version-policies)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/db-version-policies)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/db-version-policies)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/db-version-policies)



To plan database upgrades and keep your deployments running on supported PostgreSQL releases, review the support, retirement, and compatibility policies for AlloyDB Omni major and minor versions.

For information about AlloyDB for PostgreSQL version policies, see [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

## AlloyDB Omni version policies

Every version of AlloyDB Omni is compatible with a specific version of PostgreSQL, as detailed in Support policy.

Because AlloyDB Omni is software that you install and run yourself, you are responsible for regularly updating your AlloyDB Omni installation. Learn about the latest versions of AlloyDB Omni in the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/release-notes).

For AlloyDB Omni, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility. Some AlloyDB Omni releases are updates to AlloyDB Omni itself, independent of updates to PostgreSQL support. These releases include bug fixes and security updates and are reflected in an incremental increase of the third number in the release version. For example, the `2` in `18.1.2` indicates an update to AlloyDB Omni.

## Support policy

Google provides support for AlloyDB Omni versions based on the following timelines:

Version type | Support period  
---|---  
Major versions | Supported for 5 years from the initial release date, matching the community support lifecycle of the underlying PostgreSQL version.  
Minor versions | Supported for 1.5 years from their specific release date.  
  
## Major version support timeline

The general availability (GA) dates serve as the initial release dates for calculating the 5-year support window. The following table lists the GA dates and end-of-support dates for AlloyDB Omni PostgreSQL major versions:

PostgreSQL major version | GA date | End-of-support date  
---|---|---  
18 | April 9, 2026 | April 9, 2031  
17 | December 15, 2025 | December 15, 2030  
  
After a version exceeds its support period, it is considered retired. Google doesn't process support tickets for retired versions and recommends that you upgrade to a supported version to continue receiving assistance.

## Supported PostgreSQL versions

For the Common Vulnerabilities and Exposures (CVEs) tracked across database releases, see the [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/security-bulletins).

The following table lists the AlloyDB Omni minor versions, their compatible PostgreSQL versions, release dates, 1.5-year end-of-support dates, and support status:

AlloyDB Omni version | PostgreSQL version | Release date | End-of-support date | Status  
---|---|---|---|---  
18.4.0 | 18.4 | October 14, 2026 | April 14, 2028 | Supported  
18.3.0 | 18.3 | September 8, 2026 | March 8, 2028 | Supported  
18.1.1 | 18.1 | May 27, 2026 | November 27, 2027 | Supported  
18.1.0 | 18.1 | April 7, 2026 | October 7, 2027 | Supported  
17.5.0 | 17.5 | December 16, 2025 | June 16, 2027 | Supported  
  
## Patch policy

To help maintain the security and stability of your environment, Google applies patches for critical bugs and vulnerabilities according to the following policy:

  * Google applies patches only to the latest minor version of each supported major version.
  * If you encounter an issue on an older minor version, you must upgrade to the latest available minor version of that major version to receive the fix.
  * For information about CVEs addressed in AlloyDB Omni RPM packages, see [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/security-bulletins).



## Upgrade and compatibility

AlloyDB Omni version numbers use the format `MAJOR_VERSION.MINOR_VERSION.OMNI_PATCH_VERSION` to indicate the supported PostgreSQL version. The major and minor version numbers match the version of the underlying PostgreSQL engine, and the third number represents the AlloyDB Omni patch version.

The following table summarizes the upgrade and compatibility policies for AlloyDB Omni:

Policy category | Description  
---|---  
Major version timing | Google aims to support new PostgreSQL major versions within eight months of the release of the first minor release, version x.1, of a new PostgreSQL major version.  
Minor version timing | Google aims to release support for new PostgreSQL minor versions every quarter. Because AlloyDB Omni is software that you install and run yourself, you must download and install the binaries that include upgraded PostgreSQL minor version compatibility.  
Security updates | Google aims to release fixes within one month of a PostgreSQL community security release.  
Upgrade path | 

  * You can skip minor or patch versions during an upgrade if the version gap doesn't exceed the 1.5-year support period.
  * You can roll back only to the version that you used immediately before the upgrade.

  
  
## Data protection

AlloyDB Omni doesn't perform automatic backups before an upgrade. You are responsible for taking a manual backup of your data before triggering an upgrade process.

## What's next

  * Review the [AlloyDB Omni security bulletin](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/security-bulletins).
  * Read the [AlloyDB for PostgreSQL database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
