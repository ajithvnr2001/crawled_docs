---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites/
title: Review deployment requirements \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T08:30:14.588260+00:00
---

# Review deployment requirements  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review deployment requirements

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the technical and environmental requirements necessary to deploy a Google Security Operations Remote Agent. The Remote Agent acts as a bridge, letting your Google Security Operations platform communicate with security tools and devices within your local environment.

## Before you begin

Before proceeding with the installation, confirm that you meet the following prerequisites:

  * **Email configuration (optional)** : Configure the email (SMTP/IMAP) integration in the Content Hub only if you require the installation package to be sent by email. If configured, use **Shared Instances** on the **Configure** page.
  * **Server accessibility** : The Agent server must be accessible to both the Google SecOps Publisher and the target security tools within the corresponding environment.



### Technical requirements

Review the following hardware and operating system requirements for the server hosting the Remote Agent:

Requirement | Basic deployment | Scaled-up deployment  
---|---|---  
CPU | 4 cores | 8 cores  
RAM | 8 GB | 16 GB  
Storage | 100 GB | 100 GB  
  
## Supported operating systems

Following are the prerequisites for the end customer server (for Remote Agent manual installation only):

  * Clean Centos 7.9
  * Red Hat Enterprise Linux (RHEL) 8.7
  * Debian 12



If your infrastructure requires RHEL 9 or 10 (or later), deploy the Remote Agent using a supported container engine ([Podman](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman) or [Docker](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker)) rather than the manual installer.

## Supported container engines

The Remote Agent supports the following container engines:

  * **Podman** (recommended for all new installations)
  * **Docker**



Containerized deployments run a prebuilt container image (based on Debian 12 for Remote Agent versions later than 2.5.0.4) and are supported on hosts running RHEL 9 or 10 (or later), as well as RHEL 8 and Debian 12.

## Network and firewall requirements

When you configure firewall rules for the Remote Agent host, meet the following outbound connectivity requirements:

  * Allow outbound HTTPS traffic on TCP port `443` to your Google SecOps instance, Publisher, and locational API endpoints. For the list of required domains, see [Network access and domain allowlist](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui#network-access-and-domain-allowlist). If your firewall policy doesn't allow wildcard domain entries (such as `*.backstory.chronicle.security`, `*.siemplify-soar.com`, or `*-chronicle.googleapis.com`), use the tenant-specific SOAR URL, Publisher hostname (`SERVER_API_ROOT`), and locational API endpoint (`<var>REGION</var>-chronicle.googleapis.com`, configured in `ONE_PLATFORM_URL_DOMAIN`) provided when your tenant is provisioned. The regional endpoint format (`chronicle.<var>REGION</var>.rep.googleapis.com`) isn't supported for Remote Agent control-plane connectivity.
  * Allow outbound HTTPS traffic on TCP port `443` to the required Google Cloud authentication endpoints: `oauth2.googleapis.com` (for service account authentication), `sts.googleapis.com`, and `iamcredentials.googleapis.com` (for [Workload Identity Federation](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/authenticate-remote-agent-with-workload-identity-federation)). For more information, including Private Service Connect configuration, see [Network and Private Service Connect requirements](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google#network-and-psc-requirements).
  * Allow outbound HTTPS traffic on TCP port `443` to the container registries used for Podman or Docker deployments. Required registries include `*.pkg.dev` (such as `us-docker.pkg.dev`) and `gcr.io` for Artifact Registry, or `docker.io`.
  * Bypass SSL/TLS inspection on application-layer proxies and Deep Packet Inspection (DPI) firewalls for Remote Agent traffic. This prevents proxies from interrupting TLS handshakes with your Publisher and Google SecOps API endpoints.



## Hardened environments and OS security policies

Host OS hardening and security enforcement mechanisms—such as **SELinux** in `Enforcing` mode, **AppArmor** , or endpoint security software—can cause Remote Agent tasks to fail when the security policy blocks OS commands executed by the agent.

If you deploy the Remote Agent on a hardened host, you must exempt the Remote Agent from these security enforcement policies so that it can run required OS commands:

  * For containerized deployments (Docker or Podman), exempt the Remote Agent container when starting it for the first time by adding `--security-opt label=disable` (for SELinux) or `--security-opt apparmor=unconfined` (for AppArmor) to your `docker run` or `podman run` command.
  * Configure custom SELinux policy rules, AppArmor profiles, or endpoint security and antivirus exemptions for the Remote Agent directories (`/opt/SiemplifyAgent`, `/home/siemplify_agent/agent_source`, and `/var/log/SiemplifyAgent`) and executables (`/usr/local/bin/python3.11`, `/usr/local/bin/pip3`, and `/usr/bin/supervisord`).
  * Alternatively, set SELinux to `Permissive` mode on the host machine by setting `SELINUX=permissive` in `/etc/selinux/config` (or temporarily running `sudo setenforce 0`) if targeted policy exemptions aren't configured.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
