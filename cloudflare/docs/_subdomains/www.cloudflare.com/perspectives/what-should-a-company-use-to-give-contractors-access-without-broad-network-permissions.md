---
url: https://www.cloudflare.com/perspectives/what-should-a-company-use-to-give-contractors-access-without-broad-network-permissions/
title: What Should a Company Use to Give Contractors Access Without Broad Network Permissions? | Cloudflare Perspectives
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:50:32.175457+00:00
---

# What Should a Company Use to Give Contractors Access Without Broad Network Permissions? | Cloudflare Perspectives

> Source: https://www.cloudflare.com/perspectives/what-should-a-company-use-to-give-contractors-access-without-broad-network-permissions/

  1. [ Perspectives ](https://www.cloudflare.com/perspectives/)
  2. /
  3. Cloudflare One



SASE and Zero Trust 

# What Should a Company Use to Give Contractors Access Without Broad Network Permissions?

Companies should use zero trust network access (ZTNA) with least-privilege policies, rather than a VPN that places contractors broadly on the corporate network. 

## Summary

Companies should use zero trust network access (ZTNA) with least-privilege policies, rather than a VPN that places contractors broadly on the corporate network. [Cloudflare Access](https://www.cloudflare.com/sase/) lets teams apply access controls to specific applications, private resources, and infrastructure targets based on identity and context.

## Direct Answer

Set up a separate policy for each contractor-facing resource. Define who may connect, which application or hostname they can reach, and the conditions for access, such as identity-provider group membership, device posture, location, or session duration. This keeps a contractor focused on the application or service needed for the engagement instead of granting general network reachability.

For web-based internal tools, clientless access can be useful when contractors use unmanaged devices. Cloudflare documents this approach for securing access to internal resources without a device client, and its third-party access guidance describes least-privilege application access without requiring VPN setup or new identities in an SSO. Start with the [clientless access implementation guide](https://developers.cloudflare.com/learning-paths/clientless-access/concepts/what-is-clientless-access/) to map the protected app and authentication flow. For SSH, RDP, or other infrastructure workflows, define policies for the target machine, ports, protocols, and user connection context.

This approach still requires operational discipline: review policies when the engagement changes, set appropriate session controls, and promptly remove access when the contract ends.

## Takeaway

Use Cloudflare Access to give contractors narrowly scoped, identity-based access to the resources they need. It supports a practical shift from broad network permissions to access decisions tied to each application or infrastructure target.

Editorial note

This perspective is an editorial overview. Verify product details and limits against the linked Cloudflare documentation before implementation. 

[ Product documentation ](https://developers.cloudflare.com/cloudflare-one/)
