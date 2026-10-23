---
url: https://developers.cloudflare.com/changelog/product/cloudflare-one-client/
title: Cloudflare One Client Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:20.918571+00:00
---

# Cloudflare One Client Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product/cloudflare-one-client/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloud Workload Security

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 12, 2026

## [Cloudflare One Client for Windows (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Cloudflare One Client for macOS (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Cloudflare One Client for Linux (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 7, 2026

## [Cloudflare One Client for macOS (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster connects and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Oct 7, 2026

## [Cloudflare One Client for Windows (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across tunnel reconnections.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved connection reliability on devices with very large hosts files. The client now detects a large hosts file, allows more time for its initial DNS check, and shows a banner letting the user know that connecting may take longer.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * A service recovery mechanism, backed by a Windows scheduled task, now starts the client service on system unlock if it is not already running. This is enabled by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client service failing to restart after an unexpected termination.
  * Fixed the client UI getting stuck in a connecting state after sleep and wake even though the tunnel was connected.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While this release includes a fix to mitigate this issue, users may still experience reduced DNS performance and connectivity check failures.



Oct 7, 2026

## [Cloudflare One Client for Linux (version 2026.8.2100.0)](https://developers.cloudflare.com/changelog/post/2026-10-07-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release includes the following highlights:

  * Traffic to split tunnel excluded resources is no longer briefly blocked while the client is connecting or reconnecting. The client now keeps its learned split tunnel configuration across reconnects.
  * Support for routing non-RFC 1918 local IPv4 networks through the tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Faster tunnel reconnections and lower memory use. The hosts file is now read once and shared across the client’s DNS resolvers instead of being reloaded by each one.
  * Added an MDM setting to prefer IPv4 when resolving hostnames in proxy mode. The setting is off by default.



**Additional changes and improvements**

  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Individual DNS-over-HTTPS queries now time out instead of hanging when the upstream server stops responding.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed the client reconnecting while Emergency Disconnect was active after switching organizations or re-registering.
  * Fixed the client being unable to connect after an upgrade when its stored registration credentials no longer matched its configuration.
  * Fixed the client service restarting unexpectedly when it was slow to respond, such as after waking from sleep.
  * Fixed the client window not appearing on first launch after a fresh install on RHEL 10.
  * Fixed duplicate WARP routing policy rules accumulating on reconnect.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report “No network” after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Sep 30, 2026

## [Cloudflare One Client for Windows (version 2026.8.2033.1)](https://developers.cloudflare.com/changelog/post/2026-09-30-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



For Zero Trust documentation, see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/> For Consumer documentation, see: <https://developers.cloudflare.com/warp-client/>

Sep 29, 2026

## [Cloudflare One Client for Windows (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 29, 2026

## [Cloudflare One Client for macOS (version 2026.8.2028.1)](https://developers.cloudflare.com/changelog/post/2026-09-29-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 21, 2026

## [Cloudflare One Client for macOS (version 2026.8.1755.1)](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 21, 2026

## [Cloudflare One Client for Windows (version 2026.8.1755.1)](https://developers.cloudflare.com/changelog/post/2026-09-21-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Fixed an issue that could briefly block traffic to split tunnel excluded resources while the client was connecting or reconnecting.
  * Improved reauthentication reliability and fixed an issue where a reauthentication could force a new registration.
  * Improved client reaction to the current network lowering its MTU.
  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 9, 2026

## [Cloudflare One Client for macOS (version 2026.8.1290.1)](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * Fixed Extra Logging failing to capture packets across all interfaces.
  * Fixed an issue that could prevent remote diagnostics from completing.
  * Fixed DNS connectivity checks failing on IPv6-only networks.
  * Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.
  * Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Sep 9, 2026

## [Cloudflare One Client for Windows (version 2026.8.1290.1)](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
  * Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
  * Improved API reliability by retrying requests dropped when reusing pooled connections.
  * The client no longer requires the Windows WLAN AutoConfig service to be running.
  * Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
  * Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
  * Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
  * Fixed the client continuing to report 'No network' after a successful manual disconnect.
  * Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
  * Fixed the client UI crashing at startup when it could not write to the Windows registry.
  * Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
  * Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
  * Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
  * Fixed a startup crash when date formatting data for the system locale had not yet loaded.



**Known issues**

  * None



Aug 28, 2026

## [Cloudflare One Client for macOS (version 2026.7.1376.0)](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 28, 2026

## [Cloudflare One Client for Windows (version 2026.7.1376.0)](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

Fixed a rare but critical issue where the client could fail to connect or switch organizations due to an invalid registration after switching installed client versions. Additionally, this hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 28, 2026

## [Cloudflare One Client for Linux (version 2026.7.1377.0)](https://developers.cloudflare.com/changelog/post/2026-08-28-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where a small but noticeable percentage of DNS queries fail across platforms.

Aug 19, 2026

## [Cloudflare One Client for Windows (version 2026.7.1343.0)](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
  * When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.



**Additional changes and improvements**

  * Fixed a process leak in the Windows GUI that could exhaust system resources during IPC client-creation failures.
  * Fixed being unable to switch organizations when the client was stuck in the "Device not in organization" state.
  * Fixed an issue where Microsoft Defender would falsely flag the Cloudflare One Client installation as malicious when installing with Intune.
  * Made the Windows domain-joined posture check more reliable.
  * A DNS search domain parsing failure no longer prevents connection.
  * Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
  * Fixed missing certificate error display due to a race condition.
  * Fixed empty black window after transitioning from docked dual displays to undocked/internal display.



**Known issues**

  * If a user upgrades to version 2026.7.1343.0, downgrades to an earlier version, re-registers, and then upgrades back to 2026.7.1343.0, the client might fail to connect or switch organizations. To resolve this issue, run `warp-cli registration delete` or `warp-cli registration delete-all`.



Aug 19, 2026

## [Cloudflare One Client for macOS (version 2026.7.1343.0)](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
  * When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.



**Additional changes and improvements**

  * Fixed the client not allowing login to another organization when currently showing "Device not in organization."
  * A DNS search domain parsing failure no longer prevents connection.
  * Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
  * Fixed missing certificate error display due to a race condition.
  * Fixed crash when trying to connect to captive portal on Wi-Fi.
  * Fixed empty black window after transitioning from docked dual displays to undocked/internal display.



**Known issues**

  * None



Aug 19, 2026

## [Cloudflare One Client for Linux (version 2026.7.1343.0)](https://developers.cloudflare.com/changelog/post/2026-08-19-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release introduces multiple features from our previous beta release into stable release, including:

  * When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.
  * When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.



**Additional changes and improvements**

  * Fixed the client not allowing login to another organization when currently showing "Device not in organization."
  * A DNS search domain parsing failure no longer prevents connection.
  * Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.
  * Fixed missing certificate error display due to a race condition.
  * Fixed empty black window after transitioning from docked dual displays to undocked/internal display.
  * Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



Aug 10, 2026

## [Cloudflare One Client for Windows (version 2026.6.905.0)](https://developers.cloudflare.com/changelog/post/2026-08-10-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.

Jul 31, 2026

## [Cloudflare One Client for Windows (version 2026.7.1210.1)](https://developers.cloudflare.com/changelog/post/2026-07-31-warp-windows-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.
  * Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.
  * A [DNS search domain](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) parsing failure no longer prevents connection.
  * Fixed a [MASQUE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) issue where the tunnel could stall while uploading at a high rate.
  * Fixed being unable to [switch organizations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/) when the client was stuck in the "Device not in organization" state.
  * Fixed the Home Screen dropdown popup not anchoring correctly.
  * Fixed a crash during dialog dismissal.
  * Increased tolerance for configurations with a large number of [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.
  * Fixed a networking issue where IPv6 multicast routes were being assigned to the WARP tunnel interface.
  * Fixed fatal errors on UI load on Windows 10.
  * Fixed a crash during Windows notification initialization.
  * Made the Windows [domain-joined posture check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/) more reliable.
  * Fixed orphaned credentials left behind on multi-user uninstall.
  * A successful re-authentication will cause the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) to be re-evaluated.
  * Improved [dashboard-managed client updates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) by running the updater only when needed.



Jul 31, 2026

## [Cloudflare One Client for macOS (version 2026.7.1210.1)](https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

  * Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.
  * Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.
  * A [DNS search domain](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) parsing failure no longer prevents connection.
  * Fixed a [MASQUE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) issue where the tunnel could stall while uploading at a high rate.
  * Fixed being unable to [switch organizations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/) when the client was stuck in the "Device not in organization" state.
  * Fixed the Home Screen dropdown popup not anchoring correctly.
  * Fixed a crash during dialog dismissal.
  * Increased tolerance for configurations with a large number of [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.
  * Fixed the WARP client stealing window focus (for example, during reauth).
  * Fixed a client crash when connecting to a captive portal over Wi-Fi.
  * Fixed the system tray icon showing "disconnected" while the UI showed "connected".
  * A successful re-authentication will cause the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) to be re-evaluated.
  * Improved [dashboard-managed client updates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) by running the updater only when needed.



Jul 21, 2026

## [Cloudflare One Client for Windows (version 2026.6.880.0)](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

Jul 21, 2026

## [Cloudflare One Client for macOS (version 2026.6.880.0)](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

Jul 21, 2026

## [Cloudflare One Client for Linux (version 2026.6.880.0)](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-linux-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Linux Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

← Prev

1[2](https://developers.cloudflare.com/changelog/product/cloudflare-one-client/2/)[3](https://developers.cloudflare.com/changelog/product/cloudflare-one-client/3/)

[Next →](https://developers.cloudflare.com/changelog/product/cloudflare-one-client/2/)
