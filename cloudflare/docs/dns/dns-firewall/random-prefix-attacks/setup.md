---
url: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/
title: Protect against random prefix attacks \u00b7 Cloudflare DNS docs
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:09.950629+00:00
---

# Protect against random prefix attacks · Cloudflare DNS docs

> Source: https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DNS](https://developers.cloudflare.com/dns/)
  3. /…

[DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/)

  4. /[Random prefix attack mitigation](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/)
  5. /Setup



# Setup

Last updated Nov 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a mitigation modeIdentify the type of attackRespond to a simple DNS flood Increase cache TTL Cache negative responses Disable ANY queriesRespond to an active random prefix attack 1\. Switch attack mitigation to always-on 2\. Increase cache TTL 3\. Set a rate limit

In order to enable automatic mitigation of [random prefix attacks](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/):

  1. Set up [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/setup/).

  2. Enable attack mitigation on your DNS Firewall cluster.

     1. In the Cloudflare dashboard, go to the **DNS Firewall Clusters** page.

[ Go to **Clusters** ↗ ](https://dash.cloudflare.com/?to=/:account/dns-firewall/clusters)
     2. Select the cluster you want to update, then select **Edit**.

     3. Turn on **Attack mitigation** and choose whether Cloudflare should only mitigate attacks when the upstream is unhealthy.

     4. Select **Save**.

Send a [`PATCH` request](https://developers.cloudflare.com/api/resources/dns_firewall/methods/edit/) to update your DNS Firewall cluster:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `DNS Firewall Write`
Update DNS Firewall Clusterbash
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"attack_mitigation": {
    				"enabled": true,
    				"only_when_upstream_unhealthy": true
    		}
    	}'




Once you turn on attack mitigation, Cloudflare returns a `REFUSED` response to queries that are part of a random prefix attack.

Note

If you do not specify otherwise, Cloudflare automatically sets the `only_when_upstream_unhealthy` parameter to true, which means that Cloudflare will only mitigate attacks when we detect that the upstream is unresponsive (possibly as a result of an attack).

## Choose a mitigation mode

The `only_when_upstream_unhealthy` setting controls when Cloudflare starts blocking queries identified as part of a random prefix attack.

Mode | `only_when_upstream_unhealthy` | When to use  
---|---|---  
**Conditional** (default) | `true` | Steady-state protection. Cloudflare blocks attack traffic only when your upstream nameservers are unresponsive. Reduces the risk of false positives — legitimate queries are less likely to be refused. Recommended for most deployments.  
**Always on** | `false` | Active attack response. Cloudflare blocks identified attack traffic at all times, regardless of upstream health. Use this when your upstream is being overwhelmed. Some legitimate queries for subdomains not seen before may receive a `REFUSED` response.  
  
To check your current cluster configuration before making changes, send a [`GET` request](https://developers.cloudflare.com/api/resources/dns_firewall/methods/get/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`
  * `DNS Firewall Read`

DNS Firewall Cluster Detailsbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

## Identify the type of attack

DNS Firewall provides different levels of protection depending on the type of attack. Before applying mitigations, identify which pattern you are dealing with by inspecting a sample of query names hitting your upstream nameservers.

Attack pattern | Description | DNS Firewall protection  
---|---|---  
**Simple DNS flood** | The same query name, or a small set of names, repeated at high volume. | ✅ Strong — cached responses absorb the traffic. Increase cache TTL values.  
**Random prefix attack** | Random-looking subdomains all ending with the same suffix (for example, `abc123.example.com`, `xyz456.example.com`). | Best-effort — use `attack_mitigation`. Refer to Respond to an active random prefix attack.  
**Random-query attack** | Random subdomains across many different suffixes, or the targeted suffix is on the [Public Suffix List ↗︎](https://publicsuffix.org/) (for example, `co.uk`). | Partial — DNS Firewall can mitigate attacks targeting specific domain apexes. Attacks targeting an entire public suffix (such as `co.uk`) cannot be fully mitigated.  
  
## Respond to a simple DNS flood

If the same query names are being repeated at high volume, Cloudflare's cache is your primary defense. Apply the following settings via API or dashboard to maximise cache absorption.

### Increase cache TTL

Raising the cache TTL lets Cloudflare serve more responses from cache and reduces queries forwarded to your upstream nameservers:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"minimum_cache_ttl": 3600,
    		"maximum_cache_ttl": 21600
    	}'

Note

Increasing cache TTL reduces upstream load but also delays DNS change propagation to end users.

### Cache negative responses

If the attack includes queries for names that do not exist, enable negative response caching to prevent repeated lookups for `NXDOMAIN`, `REFUSED`, and `SERVFAIL` responses from reaching your upstream nameservers:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"negative_cache_ttl": 900
    	}'

### Disable ANY queries

`ANY` queries are frequently used in DNS amplification attacks. If not already disabled, turn them off:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"deprecate_any_requests": true
    	}'

Note

When enabled, DNS Firewall returns a `REFUSED` response to `ANY` queries instead of forwarding them to your upstream nameservers. This prevents `ANY` queries from being used as a DNS amplification vector. Refer to [RFC 8482 ↗︎](https://www.rfc-editor.org/rfc/rfc8482) for background on deprecating the `ANY` query type.

## Respond to an active random prefix attack

If your upstream nameservers are being overwhelmed by a random prefix attack, apply the following steps in order. All changes can be made via API. Rate limit configuration is not available in the dashboard.

### 1\. Switch attack mitigation to always-on

Set `only_when_upstream_unhealthy` to `false` so that Cloudflare blocks identified attack traffic immediately, without waiting for your upstream to become unresponsive:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"attack_mitigation": {
    				"enabled": true,
    				"only_when_upstream_unhealthy": false
    		}
    	}'

### 2\. Increase cache TTL

Raising the cache TTL lets Cloudflare serve more responses from cache, reducing the number of queries forwarded to your upstream nameservers:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"minimum_cache_ttl": 3600,
    		"maximum_cache_ttl": 21600
    	}'

Note

Increasing cache TTL reduces upstream load but also delays DNS change propagation to end users.

### 3\. Set a rate limit

Rate limiting caps the number of uncached queries per second that Cloudflare forwards to your upstream nameservers, applied per data center. Queries that exceed the limit receive a `REFUSED` response. Rate limiting is disabled by default — set a value based on what your nameservers can sustain under normal load:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `DNS Firewall Write`

Update DNS Firewall Clusterbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/dns_firewall/$DNS_FIREWALL_ID" \
    	--request PATCH \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"ratelimit": 1000
    	}'

Note

To disable rate limiting, set `ratelimit` to `null`.

Once the attack subsides, revert `only_when_upstream_unhealthy` to `true` and restore your normal cache TTL values to reduce the risk of false positives.

[PreviousAbout](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/)[NextAnalytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dns/dns-firewall/random-prefix-attacks/setup.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
