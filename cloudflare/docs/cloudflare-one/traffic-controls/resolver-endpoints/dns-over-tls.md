---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-over-tls/
title: DNS over TLS (DoT) \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-13T08:46:36.881099+00:00
---

# DNS over TLS (DoT) · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-over-tls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

  4. /[Resolver endpoints](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/)
  5. /DNS over TLS (DoT)



# DNS over TLS (DoT)

Last updated Oct 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure DoT queries 1\. Obtain your DoT hostname 2\. Configure your DoT client

By default, DNS is sent over a plaintext connection. DNS over TLS (DoT) is a standard for encrypting DNS queries to keep them secure and private. DoT uses the same security protocol, TLS, that HTTPS websites use to encrypt and authenticate communications.

Cloudflare supports DoT on standard port `853` over TLS 1.2 and TLS 1.3 in compliance with [RFC7858 ↗︎](https://tools.ietf.org/html/rfc7858).

## Configure DoT queries

### 1\. Obtain your DoT hostname

Each Gateway DNS location has a unique DoT hostname. DNS locations and corresponding DoT hostnames have policies associated with them.

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Traffic controls** > **Resolver endpoints**.
  2. Under **DNS locations** , [add a new location](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/) or select an existing location from the list.
  3. Under **DoT endpoint** , copy the value in **DoT addresses**.



The DoT hostname contains your unique location name. For example, if the DoT hostname is `9y65g5srsm.cloudflare-gateway.com`, the location name is `9y65g5srsm`.

### 2\. Configure your DoT client

To configure a DoT client such as `dig`, specify the IP address and the DoT hostname for your location in your query. For example:
    
    
    Hostname: 9y65g5srsm.cloudflare-gateway.com
    IP address: 162.159.36.5

Alternatively, you can use the generic DoT endpoint (`dns.cloudflare-gateway.com`) and include an `OPT` record with code `65011`. You can select a specific location for the value of the `OPT` record. For example:
    
    
    Hostname: dns.cloudflare-gateway.com
    IP address: 162.159.36.5
    OPT Record:
      - Code: 65011
      - Value: 9y65g5srsm

Some stub resolvers support DoT natively. For example, you can configure Unbound to send a DoT query:
    
    
    # Unbound TLS Config
    tls-cert-bundle: "/etc/ssl/cert.pem"
    # Forwarding Config
    forward-zone:
     name: "."
     forward-tls-upstream: yes
     forward-addr: 162.159.36.5@853#9y65g5srsm.cloudflare-gateway.com
     forward-addr: 2001:db8:abcd::1234#9y65g5srsm.cloudflare-gateway.com

[PreviousResolver endpoints](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/)[NextDNS resolver IPs and hostnames](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns-resolver-ips/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/resolver-endpoints/dns-over-tls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
