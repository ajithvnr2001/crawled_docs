---
url: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/troubleshooting/
title: Troubleshoot Cloudflare Mesh connectivity \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:20.183479+00:00
---

# Troubleshoot Cloudflare Mesh connectivity · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/troubleshooting/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

NetworksConnectors

  4. /[Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/)
  5. /Troubleshooting



# Troubleshoot Cloudflare Mesh connectivity

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewIdentify the failing connectionNode or device shows offlineParticipant is online, but its Mesh IP is unreachableMesh IP works, but a private subnet does notOne site can reach the other, but not vice versaPrivate IP works, but the hostname does notConnection fails only for large packetsCheck logs

Use this guide when a Mesh node or client device is offline, a Mesh IP does not respond, or traffic between private subnets fails. A participant marked **Online** is connected to Cloudflare. That status does not confirm the service or return path works.

## Identify the failing connection

  1. In the Cloudflare dashboard, go to **Networking** > **Mesh**. Check the source and destination participant status and record the destination Mesh IP.

[ Go to **Mesh** ↗ ](https://dash.cloudflare.com/?to=/:account/mesh)
  2. From the source device, test a service that you know is listening on the destination. For example, test SSH on TCP port `22`. On macOS or Linux, install `nc` if it is not already available:
         
         nc -vz <DESTINATION-IP> 22
         
         Test-NetConnection <DESTINATION-IP> -Port 22

  3. Replace `<DESTINATION-IP>` with the Mesh IP of a participant or the private IP of a host behind a node. Use your service's port if it differs from `22`. Choose the symptom that matches the failed test.




Do not use `ping` as the only test. It requires the [ICMP Gateway proxy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/proxy/), even when TCP or UDP traffic works.

## Node or device shows offline

An offline participant cannot carry Mesh traffic. First check its Cloudflare One Client connection:

  1. On a Linux node, run:
         
         warp-cli status

  2. If the output does not show `Status update: Connected`, run `warp-cli connect` and check its status again.

  3. If it still does not connect, verify that the host can reach the [required Cloudflare One Client IPs and ports](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/). Review the [client diagnostic logs](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/) for enrollment or connection errors.




For a laptop or phone that cannot enroll or connect, follow [Troubleshoot the Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/). If a container node connects as a regular client device, verify its connector token and persistent registration state in [Run Mesh in containers](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#troubleshooting).

## Participant is online, but its Mesh IP is unreachable

The connection to Cloudflare is healthy, but traffic may bypass the Mesh tunnel or be blocked before reaching the service:

  1. Confirm both participants are enrolled in the same Cloudflare One account and use the destination's assigned Mesh IP. Check [Required account settings](https://developers.cloudflare.com/mesh/get-started/#required-account-settings), including unique device IPs and allowing Cloudflare One traffic to reach enrolled devices.
  2. On the source and destination, check the applied [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/). Mesh nodes must use Traffic and DNS mode. In Split Tunnels **Include mode** , include `100.96.0.0/12`. In **Exclude mode** , make sure neither that range nor a parent such as `100.64.0.0/10` is excluded. Use your custom device IP range if you changed the default.
  3. Confirm that the [Gateway proxy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/proxy/) is on for the test protocol. ICMP is optional, but TCP or UDP proxying must be on for those services.
  4. Confirm the destination service listens on the Mesh IP or all interfaces and that its host firewall allows the source Mesh IP and port. Review [Gateway network policies](https://developers.cloudflare.com/cloudflare-one/traffic-controls/network-policies/) and [Network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network) for a blocked request.



A service bound only to the host's separate local-network IP will not accept a connection to its Mesh IP. If the IP responds but the application fails, check the service configuration and port before changing Mesh routes.

## Mesh IP works, but a private subnet does not

Reaching a node by Mesh IP does not make the hosts behind it reachable. A routed subnet also requires a CIDR route, forwarding, and a return path:

  1. On the destination node's **Routes** tab, confirm that a [CIDR route](https://developers.cloudflare.com/mesh/features/routes/#add-a-route) covers the private destination IP and points to that node.

  2. On the source participant, confirm that the destination CIDR routes through Cloudflare in its [Split Tunnels](https://developers.cloudflare.com/mesh/features/routes/#configure-split-tunnels/) settings. If the source is a host behind another node, confirm its router sends the destination CIDR to the local node.

  3. On the destination Linux node, check IPv4 forwarding:
         
         sysctl net.ipv4.ip_forward

If the result is `0`, follow [Make IP forwarding persistent](https://developers.cloudflare.com/mesh/best-practices/#make-ip-forwarding-persistent/). Cloud virtual machines may also need [provider-specific forwarding settings](https://developers.cloudflare.com/mesh/best-practices/#cloud-vpc-deployments/).

  4. On the destination node, check that UFW, firewalld, nftables, or another host firewall allows forwarded traffic between the Cloudflare One Client and local network interfaces. Check cloud firewall rules or security groups as well.

  5. Check the destination host firewall and return route. For a source with a Mesh IP, route the Mesh device IP range through the destination node. For a source on another private subnet, route that remote subnet through the destination node. If the node is the local default gateway, separate static return routes are not needed.




Container nodes can use [source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat/) instead of return routes to Mesh IP clients. Check the container setting before changing the router.

## One site can reach the other, but not vice versa

Site-to-site traffic needs the same configuration in both directions. A route at one site does not automatically configure the other:

  1. Confirm each node advertises **its own** local subnet as a CIDR route.
  2. Confirm each node's effective Split Tunnel configuration sends the **other** site's subnet through Cloudflare.
  3. Confirm each site router sends traffic for the remote subnet to its **local node IP**. Check the reverse route for responses on both sites.
  4. Check each node's forwarding firewall rules in both directions.
  5. Test a listening service from a host behind each node. Check both destination firewalls and Gateway network policies if only one direction fails.



For a complete two-site example, refer to [Connect two private networks with Cloudflare Mesh](https://developers.cloudflare.com/mesh/guides/connect-sites/).

## Private IP works, but the hostname does not

CIDR routing does not create DNS records. Confirm the hostname resolves to the correct private IP and that the client can reach the DNS resolver. Test the private IP first to isolate DNS from network routing.

For a [Mesh hostname route](https://developers.cloudflare.com/mesh/features/routes/#hostname-routes), also confirm that the node uses MASQUE and that the client sends the DNS query to Cloudflare Gateway instead of using Local Domain Fallback. Follow the hostname-route DNS instructions for your resolver arrangement.

## Connection fails only for large packets

Encapsulation can cause larger packets to exceed the available path maximum transmission unit (MTU). If a small service request works but larger responses stall, follow the [MTU and packet fragmentation recommendations](https://developers.cloudflare.com/mesh/best-practices/#mtu-and-packet-fragmentation/).

## Check logs

Use [Gateway Network logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network) to inspect the source, destination, port, and policy action. If a failed attempt has no entry, check Split Tunnels and the [Gateway traffic logging setting](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#selective-logging/) before changing policies. To diagnose a node that cannot connect, collect [Cloudflare One Client diagnostic logs](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/).

[PreviousPlatform](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/platform/)[NextOverview](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/networks/connectors/cloudflare-mesh/troubleshooting/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
