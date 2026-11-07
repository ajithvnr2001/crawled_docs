---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/security-bulletins/
title: Security bulletin \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T08:32:47.447512+00:00
---

# Security bulletin  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/security-bulletins/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/resources)



Send feedback 

#  Security bulletin Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/security-bulletins)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/security-bulletins)



To evaluate the security posture of your AlloyDB Omni RPM orchestrator deployments on Red Hat Enterprise Linux (RHEL) and Rocky Linux and plan upgrades, review the security policies, vulnerability scope, and Common Vulnerabilities and Exposures (CVE) disclosure practices on this page.

To receive the latest AlloyDB Omni release notes and security updates in your feed reader, subscribe to the [AlloyDB Omni release notes feed](https://cloud.google.com/feeds/alloydbomni-release-notes.xml).

## Scope and severity filtering

To focus remediation workflows on actionable security advisories and reduce scanner noise, AlloyDB Omni vulnerability summaries and detailed CVE logs follow these reporting policies:

  * Strict Critical and High severity filtering: Vulnerability summary tables and detailed CVE logs report exclusively Critical and High severity CVEs based on National Vulnerability Database (NVD) and upstream vendor severity ratings. Low and Medium severity advisories are excluded from the summary counts and detailed logs. 
  * Version-specific isolation: Detailed CVE logs are organized into dedicated subpages per release version using a standardized 4-column schema with columns for `CVE ID`, `Severity`, `AlloyDB Omni version`, and `Mitigated in`. Within each release log, vulnerabilities remediated in a subsequent release display the mitigating release version in the `Mitigated in` column.



## Vulnerability assessment and refresh policy

Google regularly scans all published AlloyDB Omni RPM orchestrator and database RPM packages against the NVD, Red Hat Security Data, and Go vulnerability databases. Google refreshes the AlloyDB Omni security bulletins when new releases are published: 

  * Fixed CVEs: Vulnerabilities that were present in an earlier AlloyDB Omni RPM orchestrator or database RPM package are mitigated in a subsequent minor or patch release. Google applies security patches to the latest minor version of supported PostgreSQL major version 18, and to the latest supported AlloyDB Omni RPM orchestrator release.
  * Host OS packages for RPM deployments: When you deploy AlloyDB Omni by using the RPM orchestrator, AlloyDB Omni delivers the PostgreSQL database kernel and bundled extension packages. Your host Linux distribution manages system libraries such as `openssl-libs`, `glibc`, `libevent`, `systemd`, and the Linux kernel. Apply host OS security updates regularly by running `sudo dnf update --security` on your RHEL or Rocky Linux hosts.



## FIPS 140-3 compliance and CVE patching

To maintain Federal Information Processing Standards (FIPS) 140-3 compliance while continuously patching security vulnerabilities across minor and patch releases, AlloyDB Omni decouples its inner FIPS-validated cryptographic modules from its outer cryptographic and protocol libraries:

  * FIPS validation for cryptographic modules: The National Institute of Standards and Technology (NIST) Cryptographic Module Validation Program (CMVP) certifies a frozen inner cryptographic module or provider and issues a certificate number. Modifying any instruction inside that validated boundary alters its embedded Hash-based Message Authentication Code (HMAC) integrity checksum and invalidates the certificate.
  * FIPS compliance for deployments: An AlloyDB Omni deployment operates in a FIPS 140-3 compliant mode when it runs on a FIPS-enabled host OS, such as RHEL 9 with the `/proc/sys/crypto/fips_enabled` file set to `1`. In this mode, the deployment routes all security-relevant cryptographic operations through a FIPS-validated module with power-on Known-Answer Tests (KATs) and HMAC integrity checks enabled. It also enforces approved Transport Layer Security (TLS) versions of TLS 1.2 or later, approved cipher suites, and the `scram-sha-256` password authentication method. AlloyDB Omni RPM orchestrator and database RPM packages are FIPS-ready, and your organization is responsible for enabling and verifying FIPS mode on the underlying host OS. For more information, see [Security and FIPS compliance](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/shared-responsibility#security-and-fips-compliance).
  * CVE patching outside the FIPS boundary: Protocol parsing and networking libraries, such as TLS state machines, X.509 and ASN.1 certificate parsing, HTTP/2, and network I/O, reside in the outer layer outside the frozen FIPS module boundary. Because these components sit outside the validated boundary, Google patches outer-layer CVEs across minor and patch releases without modifying the inner cryptographic module or invalidating its NIST CMVP certification. Only a vulnerability inside the low-level cryptographic primitive implementation itself requires an update to the inner FIPS module.

For RPM orchestrator deployments on RHEL or Rocky Linux, the `alloydbomni18` database package dynamically links against the host OS OpenSSL 3 libraries in the `openssl-libs` RPM package and uses the host RHEL 9 OpenSSL FIPS Provider when FIPS mode is enabled on the host kernel. Applying `openssl-libs` security updates on the host OS remediates outer-layer TLS and X.509 vulnerabilities while preserving the certified OpenSSL FIPS Provider boundary. 

## What's next

  * Review the [AlloyDB Omni database version policies](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/db-version-policies).
  * Read the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/release-notes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-06 UTC."],[],[]] 
