---
url: https://developers.cloudflare.com/cloudflare-network-firewall/about/analytics/
title: Cloudflare Network Firewall Analytics \u00b7 Cloudflare Network Firewall docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:49.113186+00:00
---

# Cloudflare Network Firewall Analytics · Cloudflare Network Firewall docs

> Source: https://developers.cloudflare.com/cloudflare-network-firewall/about/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/)
  3. /[About](https://developers.cloudflare.com/cloudflare-network-firewall/about/)
  4. /Analytics



# Analytics

Last updated Nov 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGraphQL Analytics GraphQL nodes by phase Verdict and outcome Default samples

## GraphQL Analytics

Use the GraphQL Analytics API to view data for packets passing through Cloudflare's network. For more information about using the GraphQL Analytics API and getting started, refer to [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) and [Querying Cloudflare Network Firewall Samples with GraphQL](https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-network-firewall-samples/).

Refer to the [Network Firewall GraphQL Analytics tutorial](https://developers.cloudflare.com/cloudflare-network-firewall/tutorials/graphql-analytics/) for sample queries for each Network Firewall phase.

### GraphQL nodes by phase

Each [Network Firewall phase](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/#network-layer) reports to a GraphQL node.

Phase | Rules | GraphQL node  
---|---|---  
`magic_transit` | Custom rules | `magicFirewallNetworkAnalyticsAdaptiveGroups`  
`magic_transit_managed` | Managed rules | `magicFirewallNetworkAnalyticsAdaptiveGroups`  
`magic_transit_ids_managed` | IDS | `magicIDPSNetworkAnalyticsAdaptiveGroups`  
`magic_transit_ratelimit` | Rate limiting (beta) | `magicFirewallRateLimitNetworkAnalyticsAdaptiveGroups`  
  
### Verdict and outcome

Use `verdict` and `outcome` values to filter GraphQL queries. The `verdict` describes the rule evaluation or detection. For example, when a packet matches a drop rule expression, `verdict` is set to `drop`. The `outcome` describes the action that the system took. Samples matching a drop rule set `outcome` to `drop`. If the rule is disabled, the packet is not dropped, so `outcome` is set to `pass`.

Each phase uses these values slightly differently.

#### Custom and managed rules

For packets matching custom rules, the values depend on the rule's status and action:

  * A disabled custom rule has `verdict=drop` and `outcome=pass`, regardless of its action.
  * An enabled rule with the `block` action has `verdict=drop` and `outcome=drop`.
  * An enabled rule with the `skip` action has `verdict=pass` and `outcome=pass`.



Managed rules use the rule's default action, or the action set by an override. The `block` and `skip` actions use the same values as enabled custom rules.

A managed rule with the `log` action has `verdict=drop` and `outcome=pass`. Disabled managed rules do not produce matching-rule samples.

#### IDS

The Intrusion Detection System (IDS) detects signatures but does not block packets.

  * If a packet matches an IDS signature, `verdict=drop` and `outcome=pass`.
  * If a packet matches no signatures, `verdict=pass` and `outcome=pass`.



#### Rate limiting

Each rate limiting (beta) rule sets a rate threshold in packets or bits, and drops packets over that threshold. The only available action is `block`, and a rule can be enabled or disabled.

  * Packets matching a disabled rule (`enabled=false`) have `verdict=drop` and `outcome=pass`.
  * Packets matching a rule and under the threshold have `verdict=pass` and `outcome=pass`.
  * Packets matching a rule and over the threshold have `verdict=drop` and `outcome=drop`.



### Default samples

Custom and managed rules also sample packets that match no enabled rule. These default samples have an empty `ruleId`, and show which traffic no rule matched. To count all packets that custom and managed rules allowed, add the samples that matched an enabled `skip` rule to the default samples.

Rate limiting also produces default samples, which estimate all packets that left the rate limiting phase without being dropped. Use only these samples to count packets that rate limiting allowed. A packet can match several rate limiting rules and stay under the threshold of each one. Each match can produce a sample with `verdict=pass`, so counting those samples counts the packet more than once.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-network-firewall/about/)[NextIDS](https://developers.cloudflare.com/cloudflare-network-firewall/about/ids/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-network-firewall/about/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
