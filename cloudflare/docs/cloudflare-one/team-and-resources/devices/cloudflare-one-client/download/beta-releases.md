---
url: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/
title: Download Cloudflare One Client beta releases \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:26.431483+00:00
---

# Download Cloudflare One Client beta releases · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

Team and resources[Devices](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/)[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

  4. /[Downloads](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/)
  5. /Beta releases



# Download Cloudflare One Client beta releases

Last updated Nov 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWindowsmacOSLinux

Cloudflare tests new Cloudflare One Client features and improvements in an unstable beta release before adding them to the [stable release](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/). Beta releases are not recommended for production environments. To get early access to new features, download the latest beta client from the links below.

## Windows

[Download latest beta release](https://downloads.cloudflareclient.com/v1/download/windows/beta)

**OS version** | Windows 10 LTSC, Windows 11, Windows 365 Cloud PC running Windows 11  
---|---  
**Processor** | AMD64 / x86-64 or ARM64 / AArch64  
**.NET Framework version** | 4.7.2 or later  
**vCPU** | 3 minimum, 4 recommended  
**RAM** | 4 GB minimum, 8 GB recommended  
**Disk space** | 250 MiB minimum, 500 MiB recommended  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 1  
  
## Footnotes

  1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




Latest release

**Version:** Windows 2026.9.2663.1**Date:** 2026-11-10**Size:** 68.6 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.9.2663.1)

#### Release notes

This release includes the following highlights:

  * Added automatic endpoint selection for Global Acceleration. When Global Acceleration is enabled for an organization, the client connects to the Global Acceleration endpoints while the device is in the acceleration region and to the standard anycast endpoints otherwise, and reconnects when a network change moves the device between them without requiring action from the user. The Connectivity page shows which tunnel and API endpoints are in use, and users who are allowed to override the selection can choose endpoints in Settings.
  * Added protection against unauthorized modification or uninstallation of the Cloudflare One Client. When enabled, the user will be asked to provide an administrator-generated code when trying to uninstall the client, which will otherwise be blocked. Users, including administrators, also can no longer stop the client service, and attempts to authorize an uninstall with a code or token, whether accepted or rejected, are reported to Cloudflare.
  * Added a Diagnostics page to the client that shows the connection status and health, live tunnel and device metrics, network details and the results of DEX tests in one place. Users can run a speed test from the page that compares performance inside and outside the tunnel while the client is connected. The Troubleshooting tools button collects a full warp-diag bundle, or runs a captive portal test that briefly reconnects Wi-Fi, and saves the result to the Desktop, so users no longer need to run warp-diag from a terminal.
  * The client now shows a banner when the network limits the tunnel MTU to a degraded or critically low value. The banner clears when the MTU recovers or the client disconnects.



**Additional changes and improvements**

  * The client now applies tunnel MTUs between 1147 and 1199 bytes measured by Path MTU Discovery. Previously the client ignored these values and kept a larger MTU, which could drop larger packets on networks such as mobile hotspots while the client showed as connected.
  * When Path MTU Discovery is enabled, the client now accepts larger packets from Cloudflare instead of limiting them to the size it uses for its own outbound packets.
  * When Path MTU Discovery measures an IPv6 path MTU below 1280 bytes, the client now reconnects over IPv4 and keeps preferring IPv4 until the network changes. Previously the client could stay on a smaller tunnel MTU over IPv6 on networks where IPv4 supports larger packets.
  * Access reauthentication requests now trust certificates in the operating system's certificate store, so reauthentication works on networks that perform TLS inspection.
  * For Zero Trust deployments, the client now records a traceroute of the network path outside the tunnel when the tunnel degrades or fails to connect. warp-diag includes the same trace.
  * warp-diag now includes redacted copies of the deployed MDM files and the names, but not the values, of stored registration secrets. It reports a QUIC path MTU only when one was measured.
  * Added the MDM parameters mdm_file_debounce_secs (1–60) and mdm_file_unavailable_debounce_secs (0–300), which set how long the client waits before applying a changed MDM file and before acting on a missing or unreadable one.
  * Added the MDM parameters managed_network_probe_interval_secs (30–300, default 30) and managed_network_probe_count (0 disables probing, 1–10, or -1 to keep probing until a managed network is found; default 1). After a registration or network change finds no managed network, the client now rechecks, so a device doesn't stay on the default profile because of a transient connection failure. Set the count to 0 to keep the previous behavior.
  * Added the `multicast` network policy and MDM setting (`allow` or `drop`, default `drop`). When set to `allow`, the client sends traffic for multicast addresses through the tunnel instead of dropping it, for networks that use multicast ranges for other traffic.
  * In proxy mode for Zero Trust, the client now sends hostnames from HTTP/HTTPS and SOCKS5 requests to Cloudflare for resolution instead of resolving them on the device.
  * The Connectivity page now shows the IPv4 and IPv6 addresses assigned to the tunnel while the client is connected.
  * When the app cannot reach the client service, the home screen now says why (service not running, not accepting connections, not responding, or connection dropped and reconnecting). It shows an error code and a Learn more link instead of "IPC error".
  * The client now shows a notification when an administrator removes the user's selected virtual network, and shows a specific message when the user selects a virtual network that is no longer available.
  * The consumer client home screen now shows when the connection is post-quantum encrypted.
  * `warp-cli target list` now accepts `--hostname` to filter targets by one or more comma-separated hostnames.
  * DEX HTTP tests now send a default User-Agent that identifies the Cloudflare One Client when the test does not configure one.
  * Reduced CPU usage by the Windows Capability Access Manager service (camsvc) caused by the client's Wi-Fi queries.
  * Reduced the client UI's memory usage.
  * The client UI no longer starts WMIC or PowerShell processes to collect memory information for crash reports.
  * Fixed installs failing with error 1603 on devices with Windows App Control (WDAC) policies, because some files inside the installer's custom actions were not signed. All components of the installer are now signed.
  * Fixed the installer asking the user to close running applications during an upgrade, downgrade or uninstall because other programs loaded the client's Visual C++ runtime libraries through the system PATH. The client now loads these libraries from a private folder so that closing other applications is unnecessary.
  * Fixed reinstalling the same version of the client from its MSI removing the updater service, which stopped the client from updating.
  * Fixed the client window appearing blank or white after an upgrade, at sign-in, after waking from sleep, or after a display change.
  * Fixed the client UI freezing and no longer showing status updates after the device woke from sleep.
  * Fixed the client UI looking for one of its libraries in a directory that standard users can create before looking in the installation directory.
  * Fixed a local user being able to crash the client service by sending a crafted query to the local DNS resolver.
  * Fixed the client service restarting when a firewall update for captive portal detection stalled while the device was asleep.
  * Fixed the client service leaking handles to processes after they exited, which could leave those processes listed as running.
  * Fixed the client getting stuck in a disconnected state on Windows on Arm devices because leftover tunnel adapters were not removed.
  * Fixed Windows resetting the Wi-Fi adapter after sign-in or a Wi-Fi restart when the client's firewall rules in Exclude split tunnel mode blocked Windows network connectivity checks. The client now allows those checks.
  * Fixed the client missing some network configuration changes after the first change was detected.
  * Fixed the client being unable to connect after an upgrade, downgrade, and upgrade that switched between consumer and Zero Trust registrations. The client now clears the mismatched registration so the user can register again.
  * Fixed the client continuing to use the previous tunnel protocol after a key rotation for a protocol change failed. The client now retries the rotation the next time it connects.
  * Fixed service token enrollment failing when it ran shortly after the service token was created. The client now retries while the new token becomes available.
  * Fixed the client reconnecting repeatedly when Global Acceleration automatic endpoint selection was enabled on devices in the acceleration region, and fixed the client keeping its previous data center after the selected endpoints changed.
  * Fixed a hostname-based split tunnel entry not taking effect until the next reconnect after its firewall rule failed to apply.
  * Fixed the client service failing to start when a split tunnel address in mdm.xml had no prefix length. A bare IP address is now treated as a single host.
  * Fixed a single malformed element in mdm.xml causing the client to ignore the whole file. warp-diag now includes the file as written.
  * Fixed `warp-cli dns fallback add` accepting an empty domain, which sent all DNS queries to the local resolver instead of Gateway. Fallback domain and split tunnel entries are now normalized, so removing an entry matches regardless of case or a trailing dot.
  * Fixed the DNS proxy caching answers for longer than the TTL of a CNAME record in the chain.
  * Fixed `warp-cli registration license` reporting an error on slow networks even though the license was applied, which left the client registered to a WARP+ account it did not recognize.
  * Fixed `warp-cli debug network` showing an all-zero interface GUID.
  * Fixed Digital Experience Monitoring (DEX) results being reported with timestamps offset from the actual time after the system clock was corrected.



**Known issues**

  * A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While our client includes a mitigation for this issue, users may still experience reduced DNS performance and connectivity check failures.
  * After an administrator removes a virtual network from a device profile or changes its default network, the virtual network list in the client may continue to show the previous networks until the client is restarted. This is a display issue only: the device connects to the networks its profile allows, and selecting a removed network is rejected without changing the connection. The warp-cli vnet command shows the current list. This will be addressed prior to the next GA release.



Previous version history (10)

Windows 2026.9.1555.1

**Version:** Windows 2026.9.1555.1**Date:** 2026-10-22**Size:** 62.8 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.9.1555.1)

#### Release notes

This release includes the following highlights:

  * Added automatic endpoint selection for Global Acceleration. When Global Acceleration is enabled for an organization, the client connects to the Global Acceleration endpoints while the device is in the acceleration region and to the standard anycast endpoints otherwise, and reconnects when a network change moves the device between them without requiring action from the user. The Connectivity page shows which tunnel and API endpoints are in use, and users who are allowed to override the selection can choose endpoints in Settings.
  * Added protection against unauthorized modification or uninstallation of the Cloudflare One Client. When enabled, the user will be asked to provide an administrator-generated code when trying to uninstall the client, which will otherwise be blocked.
  * The client now shows a banner when the network limits the tunnel MTU to a degraded or critically low value. The banner clears when the MTU recovers or the client disconnects.



**Additional Changes and improvements**

  * The client now applies tunnel MTUs between 1147 and 1199 bytes measured by Path MTU Discovery. Previously the client ignored these values and kept a larger MTU, which could drop larger packets on networks such as mobile hotspots while the client showed as connected.
  * When Path MTU Discovery is enabled, the client now accepts larger packets from Cloudflare instead of limiting them to the size it uses for its own outbound packets.
  * Access reauthentication requests now trust certificates in the operating system's certificate store, so reauthentication works on networks that perform TLS inspection.
  * For Zero Trust deployments, the client now records a traceroute of the network path outside the tunnel when the tunnel degrades or fails to connect. warp-diag includes the same trace.
  * warp-diag now includes redacted copies of the deployed MDM files and the names, but not the values, of stored registration secrets. It reports a QUIC path MTU only when one was measured.
  * Added the MDM parameters mdm_file_debounce_secs (1–60) and mdm_file_unavailable_debounce_secs (0–300), which set how long the client waits before applying a changed MDM file and before acting on a missing or unreadable one.
  * The consumer client home screen now shows when the connection is post-quantum encrypted.
  * The client UI no longer starts WMIC or PowerShell processes to collect memory information for crash reports.
  * Fixed a hostname-based split tunnel entry not taking effect until the next reconnect after its firewall rule failed to apply.
  * Fixed the client window appearing blank or white after an upgrade, at sign-in, after waking from sleep, or after a display change.
  * Fixed the client service restarting when a firewall update for captive portal detection stalled while the device was asleep.
  * Fixed the client getting stuck in a disconnected state on Windows on Arm devices because leftover tunnel adapters were not removed.
  * Fixed the client being unable to connect after an upgrade, downgrade, and upgrade that switched between consumer and Zero Trust registrations. The client now clears the mismatched registration so the user can register again.
  * Fixed the client UI looking for one of its libraries in a directory that standard users can create before looking in the installation directory.
  * Fixed warp-cli registration license reporting an error on slow networks even though the license was applied, which left the client registered to a WARP+ account it did not recognize.
  * Fixed Digital Experience Monitoring (DEX) results being reported with timestamps offset from the actual time after the system clock was corrected.
  * Added the MDM parameters managed_network_probe_interval_secs (30–300, default 30) and managed_network_probe_count (0 disables probing, 1–10, or -1 to keep probing until a managed network is found; default 1). After a registration or network change finds no managed network, the client now rechecks, so a device doesn't stay on the default profile because of a transient connection failure. Set the count to 0 to keep the previous behavior.
  * In proxy mode for Zero Trust, the client now sends hostnames from HTTP/HTTPS and SOCKS5 requests to Cloudflare for resolution instead of resolving them on the device.
  * When the app cannot reach the client service, the home screen now says why (service not running, not accepting connections, not responding, or connection dropped and reconnecting). It shows an error code and a Learn more link instead of "IPC error".
  * Fixed Windows resetting the Wi-Fi adapter after sign-in or a Wi-Fi restart when the client's firewall rules in Exclude split tunnel mode blocked Windows network connectivity checks. The client now allows those checks.
  * Fixed the installer asking the user to close running applications during an upgrade, downgrade or uninstall because other programs loaded the client's Visual C++ runtime libraries through the system PATH. The client now loads these libraries from a private folder so that closing other applications is unnecessary.



**Known issues**

A Windows DNS client regression may cause connectivity check failures on systems containing large hosts files. While our client includes a mitigation for this issue, users may still experience reduced DNS performance and connectivity check failures.

For Zero Trust documentation please see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/> For Consumer documentation please see: <https://developers.cloudflare.com/warp-client/>

Windows 2026.8.2033.1

**Version:** Windows 2026.8.2033.1**Date:** 2026-09-30**Size:** 60.1 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.8.2033.1)

#### Release notes

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

Windows 2026.8.2028.1

**Version:** Windows 2026.8.2028.1**Date:** 2026-09-29**Size:** 60.1 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.8.2028.1)

#### Release notes

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



Windows 2026.8.1755.1

**Version:** Windows 2026.8.1755.1**Date:** 2026-09-21**Size:** 60.1 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.8.1755.1)

#### Release notes

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



Windows 2026.8.1290.1

**Version:** Windows 2026.8.1290.1**Date:** 2026-09-09**Size:** 74.3 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.8.1290.1)

#### Release notes

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



Windows 2026.7.1210.1

**Version:** Windows 2026.7.1210.1**Date:** 2026-07-31**Size:** 59.5 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.7.1210.1)

#### Release notes

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



Windows 2026.5.1155.1

**Version:** Windows 2026.5.1155.1**Date:** 2026-05-29**Size:** 56 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.5.1155.1)

#### Release notes

This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

  * Right click context menu to access the most common client actions quickly
  * Built-in captive portal login experience



**Additional Changes and improvements**

  * The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
  * Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See [VNET availability](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability) for details.
  * Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the [announcement blog](https://blog.cloudflare.com/mandatory-authentication-mfa/) and [documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/) for details.
  * Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
  * Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
  * The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
  * Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.
  * Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
  * The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.
  * Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.
  * Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.



**Known issues**

  * An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
  * Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.
  * Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.
  * DNS resolution may be broken when the following conditions are all true: 
    * The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while the client is connected.  
To work around this issue, please reconnect the client by selecting "disconnect" and then "connect" in the client user interface.



Windows 2026.3.566.1

**Version:** Windows 2026.3.566.1**Date:** 2026-03-10**Size:** 51.4 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.3.566.1)

#### Release notes

This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the [Cloudflare Community forum](https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362) and let us know.

**Changes and improvements**

  * Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
  * Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
  * Added monitoring for tunnel statistics collection timeouts.
  * Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.
  * Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.
  * Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.
  * Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.
  * Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.
  * Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
  * Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.
  * Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.
  * Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.



**Known issues**

  * The client may unexpectedly terminate during captive portal login. To work around this issue, use a web browser to authenticate with the captive portal and then re-launch the client.
  * An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.
  * The client may become stuck in a `Connecting` state. To resolve this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface. Alternatively, change the client's operation mode.
  * The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.
  * Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.
  * For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 version KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.
  * Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.
  * DNS resolution may be broken when the following conditions are all true: 
    * The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while the client is connected. To work around this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface.



Windows 2026.1.89.1

**Version:** Windows 2026.1.89.1**Date:** 2026-01-27**Size:** 137 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2026.1.89.1)

#### Release notes

This release contains minor fixes, improvements, and new features.

**Changes and improvements**

  * Improvements to [multi-user mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/). Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.
  * Added a new feature to [manage NetBIOS over TCP/IP](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip) functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in [device profile settings](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/).
  * Fixed an issue causing failure of the [local network exclusion](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion) feature when configured with a timeout of `0`.
  * Improvement for the Windows [client certificate posture check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/) to ensure logged results are from checks that run once users log in.
  * Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.



**Known issues**

  * For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.

  * Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.

  * DNS resolution may be broken when the following conditions are all true:

    * WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while WARP is connected.

To work around this issue, reconnect the WARP client by toggling off and back on.




Windows 2025.10.118.1

**Version:** Windows 2025.10.118.1**Date:** 2025-12-09**Size:** 136 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/windows/version/2025.10.118.1)

#### Release notes

This release contains minor fixes and improvements.

**Changes and improvements**

  * The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
  * [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.
  * Fixed an issue where sending large messages to the WARP daemon by Inter-Process Communication (IPC) could cause WARP to crash and result in service interruptions.



**Known issues**

  * For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum [Windows 11 24H2 KB5062553](https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd) or higher for resolution.

  * Devices with KB5055523 installed may receive a warning about `Win32/ClickFix.ABA` being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to [version 1.429.19.0](https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0) or later.

  * DNS resolution may be broken when the following conditions are all true:

    * WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.
    * A custom DNS server address is configured on the primary network adapter.
    * The custom DNS server address on the primary network adapter is changed while WARP is connected.

To work around this issue, reconnect the WARP client by toggling off and back on.




## macOS

[Download latest beta release](https://downloads.cloudflareclient.com/v1/download/macos/beta)

**OS version** | Sequoia 15.1+ (15.0.x is not supported), Tahoe 26.0+, Golden Gate 27.0+  
---|---  
**Processor** | Intel or M series  
**CPU cores** | 3 minimum, 4 recommended  
**RAM** | 8 GB minimum  
**Disk space** | 1 GiB minimum  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 1  
  
All supported Mac models meet the CPU and RAM requirements, so only disk space may be a constraint.

## Footnotes

  1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




Latest release

**Version:** macOS 2026.9.2663.1**Date:** 2026-11-10**Size:** 179 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.9.2663.1)

#### Release notes

This release includes the following highlights:

  * macOS 15.0 is now the minimum supported version. This release does not run on macOS 14.
  * Added automatic endpoint selection for Global Acceleration. When Global Acceleration is enabled for an organization, the client connects to the Global Acceleration endpoints while the device is in the acceleration region and to the standard anycast endpoints otherwise, and reconnects when a network change moves the device between them without requiring action from the user. The Connectivity page shows which tunnel and API endpoints are in use, and users who are allowed to override the selection can choose endpoints in Settings.
  * Added a Diagnostics page to the client that shows the connection status and health, live tunnel and device metrics, network details and the results of DEX tests in one place. Users can run a speed test from the page that compares performance inside and outside the tunnel while the client is connected. The Troubleshooting tools button collects a full warp-diag bundle, or runs a captive portal test that briefly reconnects Wi-Fi, and saves the result to the Desktop, so users no longer need to run warp-diag from a terminal.
  * The client now shows a banner when the network limits the tunnel MTU to a degraded or critically low value. The banner clears when the MTU recovers or the client disconnects.



**Additional changes and improvements**

  * The client now applies tunnel MTUs between 1147 and 1199 bytes measured by Path MTU Discovery. Previously the client ignored these values and kept a larger MTU, which could drop larger packets on networks such as mobile hotspots while the client showed as connected.
  * When Path MTU Discovery is enabled, the client now accepts larger packets from Cloudflare instead of limiting them to the size it uses for its own outbound packets.
  * When Path MTU Discovery measures an IPv6 path MTU below 1280 bytes, the client now reconnects over IPv4 and keeps preferring IPv4 until the network changes. Previously the client could stay on a smaller tunnel MTU over IPv6 on networks where IPv4 supports larger packets.
  * Access reauthentication requests now trust certificates in the operating system's certificate store, so reauthentication works on networks that perform TLS inspection.
  * For Zero Trust deployments, the client now records a traceroute of the network path outside the tunnel when the tunnel degrades or fails to connect. warp-diag includes the same trace.
  * warp-diag now includes redacted copies of the deployed MDM files and reports a QUIC path MTU only when one was measured.
  * Added the MDM parameters managed_network_probe_interval_secs (30–300, default 30) and managed_network_probe_count (0 disables probing, 1–10, or -1 to keep probing until a managed network is found; default 1). After a registration or network change finds no managed network, the client now rechecks, so a device doesn't stay on the default profile because of a transient connection failure. Set the count to 0 to keep the previous behavior.
  * Added the `multicast` network policy and MDM setting (`allow` or `drop`, default `drop`). When set to `allow`, the client sends traffic for multicast addresses through the tunnel instead of dropping it, for networks that use multicast ranges for other traffic.
  * In proxy mode for Zero Trust, the client now sends hostnames from HTTP/HTTPS and SOCKS5 requests to Cloudflare for resolution, instead of resolving them on the device.
  * The Connectivity page now shows the IPv4 and IPv6 addresses assigned to the tunnel while the client is connected.
  * When the app cannot reach the client service, the home screen now says why (service not running, not accepting connections, not responding, or connection dropped and reconnecting). It shows an error code and a Learn more link instead of "IPC error".
  * The client now shows a notification when an administrator removes the user's selected virtual network, and shows a specific message when the user selects a virtual network that is no longer available.
  * The consumer client home screen now shows when the connection is post-quantum encrypted.
  * `warp-cli target list` now accepts `--hostname` to filter targets by one or more comma-separated hostnames.
  * DEX HTTP tests now send a default User-Agent that identifies the Cloudflare One Client when the test does not configure one.
  * The client's background services now start only when their binaries are signed by Cloudflare, so replacing the application bundle cannot run other code with the services' privileges.
  * Reduced the client UI's memory usage on the home screen.
  * Fixed a managed registration being removed when the MDM configuration file was briefly missing or unreadable. The client now keeps the last applied policy for 20 seconds after the file becomes unavailable. The new MDM parameters mdm_file_debounce_secs (1–60) and mdm_file_unavailable_debounce_secs (0–300) change how long the client waits before applying a changed file and before acting on a missing one.
  * Fixed an upgrade sometimes leaving the client without a running service when the previous service was slow to stop. The installer now waits up to 10 seconds for the old service to be removed before starting the new one.
  * Fixed the client UI not showing onboarding on first launch while a notification permission request was pending.
  * Fixed the client UI crashing when the Mac woke from sleep or a display configuration changed.
  * Fixed the client UI freezing and no longer showing status updates after the Mac woke from sleep.
  * Fixed DNS queries failing for a short time after the Mac woke from sleep. The client now replaces stale connections to the DNS resolver during its wake connectivity check.
  * Fixed the client continuing to use the previous tunnel protocol after a key rotation for a protocol change failed. The client now retries the rotation the next time it connects.
  * Fixed service token enrollment failing when it ran shortly after the service token was created. The client now retries while the new token becomes available.
  * Fixed the client reconnecting repeatedly when Global Acceleration automatic endpoint selection was enabled on devices in the acceleration region, and fixed the client keeping its previous data center after the selected endpoints changed.
  * Fixed a hostname-based split tunnel entry not taking effect until the next reconnect after its firewall rule failed to apply.
  * Fixed split tunnel updates for hostname-based entries failing when the client tried to remove a route that macOS had not installed.
  * Fixed `warp-cli dns fallback add` accepting an empty domain, which sent all DNS queries to the local resolver instead of Gateway. Fallback domain and split tunnel entries are now normalized, so removing an entry matches regardless of case or a trailing dot.
  * Fixed the DNS proxy caching answers for longer than the TTL of a CNAME record in the chain.
  * Fixed `warp-cli registration license` reporting an error on slow networks even though the license was applied, which left the client registered to a WARP+ account it did not recognize.
  * Fixed Digital Experience Monitoring (DEX) results being reported with timestamps offset from the actual time after the system clock was corrected.
  * Fixed the OS version detail stored for a device keeping an outdated value, including the text "Usage: sw_vers…" reported by client versions 2023.5.587.1 through 2024.12.760.0. The client now clears the value the next time it connects.



**Known issues**

  * After an administrator removes a virtual network from a device profile or changes its default network, the virtual network list in the client may continue to show the previous networks until the client is restarted. This is a display issue only: the device connects to the networks its profile allows, and selecting a removed network is rejected without changing the connection. The warp-cli vnet command shows the current list. This will be addressed prior to the next GA release.



Previous version history (10)

macOS 2026.9.1555.1

**Version:** macOS 2026.9.1555.1**Date:** 2026-10-22**Size:** 171 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.9.1555.1)

#### Release notes

This release includes the following highlights:

  * macOS 15.0 is now the minimum supported version. This release does not run on macOS 14.
  * Added automatic endpoint selection for Global Acceleration. When Global Acceleration is enabled for an organization, the client connects to the Global Acceleration endpoints while the device is in the acceleration region and to the standard anycast endpoints otherwise, and reconnects when a network change moves the device between them without requiring action from the user.. The Connectivity page shows which tunnel and API endpoints are in use, and users who are allowed to override the selection can choose endpoints in Settings.
  * The client now shows a banner when the network limits the tunnel MTU to a degraded or critically low value. The banner clears when the MTU recovers or the client disconnects.



**Additional Changes and improvements**

  * The client now applies tunnel MTUs between 1147 and 1199 bytes measured by Path MTU Discovery. Previously the client ignored these values and kept a larger MTU, which could drop larger packets on networks such as mobile hotspots while the client showed as connected.
  * When Path MTU Discovery is enabled, the client now accepts larger packets from Cloudflare instead of limiting them to the size it uses for its own outbound packets.
  * Access reauthentication requests now trust certificates in the operating system's certificate store, so reauthentication works on networks that perform TLS inspection.
  * For Zero Trust deployments, the client now records a traceroute of the network path outside the tunnel when the tunnel degrades or fails to connect. warp-diag includes the same trace.
  * warp-diag now includes redacted copies of the deployed MDM files and reports a QUIC path MTU only when one was measured.
  * The consumer client home screen now shows when the connection is post-quantum encrypted.
  * Fixed a managed registration being removed when the MDM configuration file was briefly missing or unreadable. The client now keeps the last applied policy for 20 seconds after the file becomes unavailable. The new MDM parameters mdm_file_debounce_secs (1–60) and mdm_file_unavailable_debounce_secs (0–300) change how long the client waits before applying a changed file and before acting on a missing one.
  * Fixed a hostname-based split tunnel entry not taking effect until the next reconnect after its firewall rule failed to apply.
  * Fixed split tunnel updates for hostname-based entries failing when the client tried to remove a route that macOS had not installed.
  * Fixed the client UI not showing onboarding on first launch while a notification permission request was pending.
  * Fixed warp-cli registration license reporting an error on slow networks even though the license was applied, which left the client registered to a WARP+ account it did not recognize.
  * Fixed Digital Experience Monitoring (DEX) results being reported with timestamps offset from the actual time after the system clock was corrected.
  * Fixed an upgrade sometimes leaving the client without a running service when the previous service was slow to stop. The installer now waits up to 10 seconds for the old service to be removed before starting the new one.
  * Fixed the OS version detail stored for a device keeping an outdated value, including the text "Usage: sw_vers…" reported by client versions 2023.5.587.1 through 2024.12.760.0. The client now clears the value the next time it connects.
  * Added the MDM parameters managed_network_probe_interval_secs (30–300, default 30) and managed_network_probe_count (0 disables probing, 1–10, or -1 to keep probing until a managed network is found; default 1). After a registration or network change finds no managed network, the client now rechecks, so a device doesn't stay on the default profile because of a transient connection failure. Set the count to 0 to keep the previous behavior.
  * In proxy mode for Zero Trust, the client now sends hostnames from HTTP/HTTPS and SOCKS5 requests to Cloudflare for resolution, instead of resolving them on the device.
  * When the app cannot reach the client service, the home screen now says why (service not running, not accepting connections, not responding, or connection dropped and reconnecting). It shows an error code and a Learn more link instead of "IPC error".



**Known issues**

None.

For Zero Trust documentation please see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/> For Consumer documentation please see: <https://developers.cloudflare.com/warp-client/>

macOS 2026.8.2028.1

**Version:** macOS 2026.8.2028.1**Date:** 2026-09-29**Size:** 166 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.8.2028.1)

#### Release notes

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



macOS 2026.8.1755.1

**Version:** macOS 2026.8.1755.1**Date:** 2026-09-21**Size:** 166 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.8.1755.1)

#### Release notes

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



macOS 2026.8.1290.1

**Version:** macOS 2026.8.1290.1**Date:** 2026-09-09**Size:** 165 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.8.1290.1)

#### Release notes

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



macOS 2026.7.1210.1

**Version:** macOS 2026.7.1210.1**Date:** 2026-07-31**Size:** 153 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.7.1210.1)

#### Release notes

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



macOS 2026.6.782.1

**Version:** macOS 2026.6.782.1**Date:** 2026-06-24**Size:** 152 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.6.782.1)

#### Release notes

This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.

**Additional changes and improvements**

This release also introduces multiple fixes and improvements including:

  * Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.
  * Path MTU Discovery (PMTUD) is now enabled by default.
  * Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.
  * Users can now register with team names in any case format without errors.
  * New UI fixes 
    * Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.
    * Added a re-auth button and banner to the home screen so users don't miss it when their session expires.
    * Added clear error messaging when the Cloudflare certificate needs to be installed.
    * Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.
    * New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.
    * Added ability to configure proxy mode for consumer users.
    * Added back the option to quit for consumer users.



**Known issues**

  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.



macOS 2026.5.1155.1

**Version:** macOS 2026.5.1155.1**Date:** 2026-05-29**Size:** 143 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.5.1155.1)

#### Release notes

This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:

  * Right click context menu to access the most common client actions quickly
  * Built-in captive portal login experience



**Additional Changes and improvements**

  * The client now applies DNS search suffixes configured in your [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles) / [network policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/network-policies). Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See [DNS search suffixes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) for details.
  * Administrators can now control which virtual networks (VNETs) are available to which users via WARP device profile settings in the Zero Trust dashboard. Previously, every VNET in the organization was visible to every device; you can now scope the VNET picker per profile so users only see the networks relevant to them. See [VNET availability](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#vnet-availability) for details.
  * Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.
  * Added new warp-cli debug commands for interactive connection diagnosis. See [Extra debug logging](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging) for details.
  * The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.
  * Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated [Cloudflare One MDM documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs) for details.
  * Client Certificate device-posture checks now support template variables (e.g. `${serial_number}`, `${device_uuid}`) in the Subject Alternative Name field, matching what the documentation has always claimed. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.
  * Fixed the in-client captive-portal browser rendering a blank "Success" page on some airline Wi-Fi networks (United inflight Wi-Fi was the reported case). The browser now reliably loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.
  * Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.



**Known issues**

  * Registration may hang at "Checking your organization configuration" due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.
  * Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via `warp-cli tunnel ip` and `warp-cli tunnel host`. UI support will be added in a future release.



macOS 2026.3.566.1

**Version:** macOS 2026.3.566.1**Date:** 2026-03-10**Size:** 128 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.3.566.1)

#### Release notes

This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the [Cloudflare Community forum](https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362) and let us know.

**Changes and improvements**

  * Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.
  * Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.
  * Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.
  * Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.
  * Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.
  * Added monitoring for tunnel statistics collection timeouts.
  * Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.
  * Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.



**Known issues**

  * The client may become stuck in a `Connecting` state. To resolve this issue, reconnect the client by selecting **Disconnect** and then **Connect** in the client user interface. Alternatively, change the client's operation mode.
  * The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.
  * Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.



macOS 2026.1.89.1

**Version:** macOS 2026.1.89.1**Date:** 2026-01-27**Size:** 115 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2026.1.89.1)

#### Release notes

This release contains minor fixes and improvements.

**Changes and improvements**

  * Fixed an issue causing failure of the [local network exclusion](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion) feature when configured with a timeout of `0`.
  * Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.



macOS 2025.10.118.1

**Version:** macOS 2025.10.118.1**Date:** 2025-12-09**Size:** 111 MB

[ Download ](https://downloads.cloudflareclient.com/v1/download/macos/version/2025.10.118.1)

#### Release notes

This release contains minor fixes and improvements.

**Changes and improvements**

  * The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
  * [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.



## Linux

**OS version** | RHEL 9 1, RHEL 10, Debian 12, Debian 13, Fedora 43, Fedora 44, Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 26.04 LTS  
---|---  
**Processor** | AMD64 / x86-64 or ARM64 / AArch64  
**vCPU** | 3 minimum, 4 recommended  
**RAM without a desktop** | 1 GB minimum, 2 GB recommended (for example, Ubuntu Server)  
**RAM with a desktop** | 4 GB minimum, 8 GB recommended (for example, Ubuntu GNOME)  
**Disk space** | 250 MiB minimum, 500 MiB recommended  
**Network interface type** | Wi-Fi or LAN  
**MTU** | 1381 bytes recommended 2  
  
## Footnotes

  1. On RHEL 9 and later, enable the [Extra Packages for Enterprise Linux (EPEL) ↗︎](https://docs.fedoraproject.org/en-US/epel/) repository before installing `cloudflare-warp`. EPEL provides dependencies required by the client UI. For the RHEL commands, refer to [Getting started with EPEL ↗︎](https://docs.fedoraproject.org/en-US/epel/getting-started/). ↩

  2. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) ↩




Latest release

**Version:** Linux 2026.9.2663.1**Date:** 2026-11-10**Size:** 84.2 MB

cloudflare-warpcloudflare-mesh

AlmaLinux / RHEL 10 (arm64)AlmaLinux / RHEL 10 (x86-64)AlmaLinux / RHEL 9 (arm64)AlmaLinux / RHEL 9 (x86-64)Debian 12 (arm64)Debian 12 (x86-64)Debian 13 (arm64)Debian 13 (x86-64)Fedora 43 (arm64)Fedora 43 (x86-64)Fedora 44 (arm64)Fedora 44 (x86-64)Ubuntu 22.04 (arm64)Ubuntu 22.04 (x86-64)Ubuntu 24.04 (arm64)Ubuntu 24.04 (x86-64)Ubuntu 26.04 (arm64)Ubuntu 26.04 (x86-64)

[ Download ](https://downloads.cloudflareclient.com/v1/download/almalinux10-arm/version/2026.9.2663.1)

#### Release notes

This beta release includes the following highlights:

  * Added automatic endpoint selection for Global Acceleration. When Global Acceleration is enabled for an organization, the client connects to the Global Acceleration endpoints while the device is in the acceleration region and to the standard anycast endpoints otherwise, and reconnects when a network change moves the device between them without requiring action from the user. The Connectivity page shows which tunnel and API endpoints are in use, and users who are allowed to override the selection can choose endpoints in Settings.
  * Added a Diagnostics page to the client that shows the connection status and health, live tunnel and device metrics, network details and the results of DEX tests in one place. Users can run a speed test from the page that compares performance inside and outside the tunnel while the client is connected. The Troubleshooting tools button collects a full warp-diag bundle, or runs a captive portal test that briefly reconnects Wi-Fi, and saves the result to the Desktop, so users no longer need to run warp-diag from a terminal.
  * The client now shows a banner when the network limits the tunnel MTU to a degraded or critically low value. The banner clears when the MTU recovers or the client disconnects.



**Additional changes and improvements**

  * The client now applies tunnel MTUs between 1147 and 1199 bytes measured by Path MTU Discovery. Previously the client ignored these values and kept a larger MTU, which could drop larger packets on networks such as mobile hotspots while the client showed as connected.
  * When Path MTU Discovery is enabled, the client now accepts larger packets from Cloudflare instead of limiting them to the size it uses for its own outbound packets.
  * When Path MTU Discovery measures an IPv6 path MTU below 1280 bytes, the client now reconnects over IPv4 and keeps preferring IPv4 until the network changes. Previously the client could stay on a smaller tunnel MTU over IPv6 on networks where IPv4 supports larger packets.
  * Access reauthentication requests now trust certificates in the operating system's certificate store, so reauthentication works on networks that perform TLS inspection.
  * For Zero Trust deployments, the client now records a traceroute of the network path outside the tunnel when the tunnel degrades or fails to connect. warp-diag includes the same trace.
  * Added the MDM parameters managed_network_probe_interval_secs (30–300, default 30) and managed_network_probe_count (0 disables probing, 1–10, or -1 to keep probing until a managed network is found; default 1). After a registration or network change finds no managed network, the client now rechecks, so a device doesn't stay on the default profile because of a transient connection failure. Set the count to 0 to keep the previous behavior.
  * Added the `multicast` network policy and MDM setting (`allow` or `drop`, default `drop`). When set to `allow`, the client sends traffic for multicast addresses through the tunnel instead of dropping it, for networks that use multicast ranges for other traffic.
  * In proxy mode for Zero Trust, the client now sends hostnames from HTTP/HTTPS and SOCKS5 requests to Cloudflare for resolution, instead of resolving them on the device.
  * The Connectivity page now shows the IPv4 and IPv6 addresses assigned to the tunnel while the client is connected.
  * When the app cannot reach the client service, the home screen now says why (service not running, not accepting connections, not responding, or connection dropped and reconnecting). It shows an error code and a Learn more link instead of "IPC error".
  * The client now shows a notification when an administrator removes the user's selected virtual network, and shows a specific message when the user selects a virtual network that is no longer available.
  * The consumer client home screen now shows when the connection is post-quantum encrypted.
  * `warp-cli target list` now accepts `--hostname` to filter targets by one or more comma-separated hostnames.
  * DEX HTTP tests now send a default User-Agent that identifies the Cloudflare One Client when the test does not configure one.
  * Reduced the client UI's memory usage on the home screen.
  * Fixed the client continuing to use the previous tunnel protocol after a key rotation for a protocol change failed. The client now retries the rotation the next time it connects.
  * Fixed service token enrollment failing when it ran shortly after the service token was created. The client now retries while the new token becomes available.
  * Fixed the client reconnecting repeatedly when Global Acceleration automatic endpoint selection was enabled on devices in the acceleration region, and fixed the client keeping its previous data center after the selected endpoints changed.
  * Fixed a hostname-based split tunnel entry not taking effect until the next reconnect after its firewall rule failed to apply.
  * Fixed `warp-cli dns fallback add` accepting an empty domain, which sent all DNS queries to the local resolver instead of Gateway. Fallback domain and split tunnel entries are now normalized, so removing an entry matches regardless of case or a trailing dot.
  * Fixed the DNS proxy caching answers for longer than the TTL of a CNAME record in the chain.
  * Fixed `warp-cli registration license` reporting an error on slow networks even though the license was applied, which left the client registered to a WARP+ account it did not recognize.
  * Fixed Digital Experience Monitoring (DEX) results being reported with timestamps offset from the actual time after the system clock was corrected.



**Known issues**

  * When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.



For Zero Trust documentation, see: <https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/>  
For Consumer documentation, see: <https://developers.cloudflare.com/warp-client/>

[PreviousLTS releases](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/)[NextUpdate the client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/update/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
