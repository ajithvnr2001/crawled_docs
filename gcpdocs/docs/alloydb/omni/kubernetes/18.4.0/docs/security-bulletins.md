---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/security-bulletins/
title: Security bulletin \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:59:07.765495+00:00
---

# Security bulletin  |  AlloyDB Omni using the container orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/security-bulletins/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/resources)



Send feedback 

#  Security bulletin Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/security-bulletins)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/security-bulletins)



To evaluate the security posture of your AlloyDB Omni Kubernetes deployments and plan control plane and database cluster upgrades, review the security policies, operator architecture, role-based access control (RBAC) and security contexts, and Common Vulnerabilities and Exposures (CVE) disclosure practices on this page.

To receive the latest AlloyDB Omni release notes and security updates in your feed reader, subscribe to the [AlloyDB Omni release notes feed](https://cloud.google.com/feeds/alloydbomni-release-notes.xml).

## Operator architecture and security contexts

AlloyDB Omni on Kubernetes decouples the Kubernetes control plane from the database engine pods that process application queries:

  * Control plane and operator components: Each AlloyDB Omni operator release comprises 10 container images built on Red Hat Universal Base Image 9 (UBI 9): 
    * `operator/fleet-operator`: Fleet-level Kubernetes controller that reconciles `DBCluster` and fleet custom resources
    * `operator/local-operator`: Instance-level Kubernetes controller that manages local database pod lifecycles and communicates only with the trusted cluster-internal Kubernetes API server
    * `alloydbomni-operator-catalog` and `alloydbomni-operator-olm-bundle`: Red Hat OpenShift Operator Lifecycle Manager (OLM) catalog index and declarative bundle metadata images
    * `operator/dbinit` and `operator/backupinit`: Ephemeral initialization containers for database bootstrapping, backup, and restore workflows
    * `operator/alloydbomni-monitor` (replaces `monitoring-agent`), `operator/g-pgbouncer`, `operator/logrotate`, and `operator/node-manager`: Companion sidecar and node management containers for health probing, connection pooling, log rotation, and storage management
  * RBAC and security contexts: The AlloyDB Omni operator uses scoped Kubernetes `Role` and `ClusterRole` permissions to reconcile custom resources within target namespaces and runs control plane and sidecar workloads with restricted container security contexts.
  * Database engine pods: Database instances managed by the operator run the standalone AlloyDB Omni database kernel container images. To verify which database kernel versions are supported for your operator version, see [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/choose-compatible-versions#compatibility-table). 



## Scope and severity filtering

To focus remediation workflows on actionable security advisories and reduce scanner noise, AlloyDB Omni vulnerability summaries and detailed CVE logs follow these reporting policies:

  * Strict Critical and High severity filtering: Vulnerability summary tables and detailed CVE logs report exclusively Critical and High severity CVEs based on National Vulnerability Database (NVD) and upstream vendor severity ratings. Low and Medium severity advisories are excluded from the summary counts and detailed logs. 
  * Decoupled control plane and database kernel reporting: Control plane bulletins under AlloyDB Omni on Kubernetes report vulnerabilities specific to the 10 AlloyDB Omni operator and sidecar container images. 
  * Version-specific isolation: Detailed CVE logs are organized into dedicated subpages per release version using a standardized 4-column schema with columns for `CVE ID`, `Severity`, `Impacted images`, and `Mitigated in`. Within each release log, vulnerabilities remediated in a subsequent release display the mitigating release version in the `Mitigated in` column.



## Vulnerability assessment and refresh policy

Google regularly scans all published AlloyDB Omni container images against the NVD, Red Hat Security Data, Debian Security Tracker, and Go vulnerability databases. Google refreshes the AlloyDB Omni security bulletins when new releases are published: 

  * Fixed CVEs: Vulnerabilities that were present in an earlier AlloyDB Omni operator control plane container image are mitigated in a subsequent operator release. Google applies security patches to the latest supported AlloyDB Omni operator release and to the latest minor version of supported PostgreSQL major versions 18, 17, 16, and 15.
  * Superseded container images: When a new AlloyDB Omni operator release mitigates CVEs from an earlier release, Google marks superseded container image digests as deprecated. Always deploy operator and control plane agent images that correspond to the latest supported release.



## FIPS 140-3 compliance and CVE patching

To maintain Federal Information Processing Standards (FIPS) 140-3 compliance while continuously patching security vulnerabilities across minor and patch releases, AlloyDB Omni decouples its inner FIPS-validated cryptographic modules from its outer cryptographic and protocol libraries:

  * FIPS validation for cryptographic modules: The National Institute of Standards and Technology (NIST) Cryptographic Module Validation Program (CMVP) certifies a frozen inner cryptographic module or provider and issues a certificate number. Modifying any instruction inside that validated boundary alters its embedded Hash-based Message Authentication Code (HMAC) integrity checksum and invalidates the certificate.
  * FIPS compliance for deployments: An AlloyDB Omni deployment operates in a FIPS 140-3 compliant mode when it runs on a FIPS-enabled host OS, such as Red Hat Enterprise Linux (RHEL) 9 with the `/proc/sys/crypto/fips_enabled` file set to `1`. In this mode, the deployment routes all security-relevant cryptographic operations through a FIPS-validated module with power-on Known-Answer Tests (KATs) and HMAC integrity checks enabled. It also enforces approved Transport Layer Security (TLS) versions of TLS 1.2 or later, approved cipher suites, and the `scram-sha-256` password authentication method. AlloyDB Omni operator container images and Red Hat UBI 9 database container images (`-ubi9`) are FIPS-ready, and your organization is responsible for enabling and verifying FIPS mode on the underlying host OS. For more information, see [Security and FIPS compliance](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/shared-responsibility#security-and-fips-compliance).
  * CVE patching outside the FIPS boundary: Protocol parsing and networking libraries, such as TLS state machines, X.509 and ASN.1 certificate parsing, HTTP/2, and network I/O, reside in the outer layer outside the frozen FIPS module boundary. Because these components sit outside the validated boundary, Google patches outer-layer CVEs across minor and patch releases without modifying the inner cryptographic module or invalidating its NIST CMVP certification. Only a vulnerability inside the low-level cryptographic primitive implementation itself requires an update to the inner FIPS module.

The following table describes the cryptographic stacks across the AlloyDB Omni operator control plane and sidecar container images, including the frozen inner FIPS boundary and the outer cryptographic and protocol layer that is patched across releases: Cryptographic stack | Control plane container images | Binaries | Inner FIPS-validated module or provider | Outer cryptographic and protocol layer  
---|---|---|---|---  
Go built-in FIPS with the `GOFIPS140=v1.0.0` build setting  |  `operator/fleet-operator`  
`operator/local-operator`  
`operator/logrotate`  
`operator/node-manager`  
`operator/dbinit`  
`operator/backupinit` |  `/operator`  
`/local`  
`/logrotate`  
`/nodemgr`  
`dbinit`  
`dbdaemon`  
`credfetcher`  
`backupinit`  
`backupdaemon` |  Go Cryptographic Module `v1.0.0`, NIST CMVP Certificate #5247  |  Go standard library packages `crypto/tls`, `crypto/x509`, and `net/http`, external Go packages such as `golang.org/x/crypto`, and the Go runtime and compiler   
OpenSSL 3 | `operator/g-pgbouncer` | `/usr/bin/pgbouncer` | RHEL 9 OpenSSL FIPS Provider |  `/lib64/libssl.so.3` and `/lib64/libcrypto.so.3` in the `openssl-libs` RPM package, and the `pgbouncer` C binary   
BoringSSL and BoringCrypto | `operator/alloydbomni-monitor` |  `/monitoring_agent` Go binary built with `boringcrypto` | Google BoringCrypto Module (BCM) |  Go `crypto/tls`, `crypto/x509`, and `net/http` packages for `monitoring_agent`  
  
## What's next

  * [Choose compatible Kubernetes operator and database cluster versions](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/choose-compatible-versions).
  * Review the [AlloyDB Omni database version policies](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/db-version-policies).
  * Read the [AlloyDB Omni release notes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/release-notes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
