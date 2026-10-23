---
url: https://developers.cloudflare.com/waf/tools/user-agent-blocking/
title: User Agent Blocking \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:48.997298+00:00
---

# User Agent Blocking · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/user-agent-blocking/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Additional tools
  4. /User Agent Blocking



# User Agent Blocking

Last updated Aug 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/user-agent-blocking/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilityCreate a User Agent Blocking ruleChallenge actionsRelated resources

User Agent Blocking allows you to block specific browser or web application [`User-Agent` request headers ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent). User agent rules apply to the entire domain instead of individual subdomains.

User agent rules are applied after [zone lockdown rules](https://developers.cloudflare.com/waf/tools/zone-lockdown/). If you allow an IP address via Zone Lockdown, it will skip any user agent rules.

Note

Cloudflare recommends that you use [custom rules](https://developers.cloudflare.com/waf/custom-rules/) instead of user agent rules to block specific user agents.

For example, a custom rule equivalent to the user agent example rule provided in this page could have the following configuration:

  * **Expression** : `http.user_agent eq "BadBot/1.0.2 (+http://bad.bot)"`
  * **Action** : (a block or challenge action)



## Availability

Cloudflare User Agent Blocking is available on all plans. The **User agent rules** option appears only if you have configured at least one user agent rule.

The number of available user agent rules depends on your Cloudflare plan.

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Number of rules | 10 | 50 | 250 | 1,000  
  
## Create a User Agent Blocking rule

Note

The **User agent rules** option appears only if you have configured at least one user agent rule. Cloudflare recommends that you use [custom rules](https://developers.cloudflare.com/waf/custom-rules/) instead of user agent rules.

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Select **Create rule** > **User agent rules**.

  3. Enter a descriptive name for the rule in **Name/Description**.

  4. In **Action** , select the action to perform: _Block_ , _Non-Interactive Challenge_ , _Managed Challenge_ , or _Interactive Challenge_.

  5. Enter a user agent value in **User Agent** (wildcards such as `*` are not supported). For example, to block the Bad Bot web spider, enter `BadBot/1.0.2 (+http://bad.bot)`.

  6. Select **Save and Deploy blocking rule**.




Issue a `POST` request for the [Create a User Agent Blocking rule](https://developers.cloudflare.com/api/resources/firewall/subresources/ua_rules/methods/create/) operation similar to the following:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Firewall Services Write`

Create a User Agent Blocking rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/firewall/ua_rules" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"description": "Block Bad Bot web spider",
    		"mode": "block",
    		"configuration": {
    				"target": "ua",
    				"value": "BadBot/1.0.2 (+http://bad.bot)"
    		}
    	}'

## Challenge actions

When a User Agent Blocking rule uses a challenge action such as _Managed Challenge_ , the visitor must pass a challenge page. After passing the challenge, a `cf_clearance` cookie is set. The duration of this cookie is controlled by the [Challenge Passage](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/) setting.

## Related resources

  * [Secure your application](https://developers.cloudflare.com/learning-paths/application-security/account-security/)
  * [Cloudflare Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/)



[PreviousHotlink Protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/)[NextZone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/user-agent-blocking.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
