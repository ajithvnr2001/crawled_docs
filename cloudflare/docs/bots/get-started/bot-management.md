---
url: https://developers.cloudflare.com/bots/get-started/bot-management/
title: Bot Management \u00b7 Cloudflare bot solutions docs
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:09.834782+00:00
---

# Bot Management · Cloudflare bot solutions docs

> Source: https://developers.cloudflare.com/bots/get-started/bot-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Bots](https://developers.cloudflare.com/bots/)
  3. /Get started
  4. /Bot Management



# Bot Management

Last updated Nov 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable Bot Management for EnterpriseSetup Enable the latest Machine Learning version Configure AI bot policies Deploy custom rule templates

Bot Management for Enterprise is a paid add-on that provides sophisticated bot protection for your domain. Customers can identify automated traffic, take appropriate action, and view detailed analytics within the dashboard.

This Enterprise product provides the most flexibility to customers by:

  * Generating a [bot score](https://developers.cloudflare.com/bots/concepts/bot-score/) of 1-99 for every request. Scores below 30 are commonly associated with bot traffic. This lets you write targeted rules instead of applying blanket actions to all detected bots.
  * Allowing customers to take action on this score with [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [`Workers`](https://developers.cloudflare.com/workers/runtime-apis/request/#incomingrequestcfproperties). For example, you can challenge low-scoring requests on your login page while allowing them on your public blog.
  * Allowing customers to view this score in Bot Analytics or Logs, so you can analyze bot traffic patterns and tune your rules over time.



* * *

## Enable Bot Management for Enterprise

Bot Management is automatically enabled and always active for Enterprise zones entitled with the add-on.

To review the Bot Management configuration:

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic**.

  3. Go to **Bot management** and select the edit icon to review the following configurations:

     * **JavaScript Detections** : For more details, refer to [JavaScript detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/).
     * **JavaScript Detections for API traffic**
     * **Auto-update machine learning model** : For more details, refer to Enable the latest Machine Learning version.



Bot Management does not block or challenge traffic on its own. To act on bot traffic, create [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) based on bot score, as described in Deploy custom rule templates.

Note

If you are not seeing Bot Management enabled on your zone or if you still see **Add Bot Management** on the Cloudflare dashboard, contact your account team for the proper entitlements.

* * *

## Setup

Cloudflare recommends that you deploy the following basic settings and customize them according to the traffic in your zone.

### Enable the latest Machine Learning version

Enterprise customers with auto-updates to the machine learning model turned on get Adaptive Intelligence. To check or change the setting:

  1. In the Cloudflare dashboard, go to the **Security Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. Filter by **Bot traffic**.

  3. Go to **Bot Management**.

  4. Under **Configurations** , select the edit icon for **Auto-update machine learning** and turn it on.




### Configure AI bot policies

Refer to [Block AI bots](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/).

Note

You can view blocked AI bot traffic via [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/).

### Deploy custom rule templates

Bot Management assigns a bot score to every request, but you must create custom rules to block or challenge automated traffic. Cloudflare provides [rule templates ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules?template=bot_traffic) to get started. You can also reach these templates from the **Bot management** setting in **Security Settings** by selecting **View bot traffic templates**.

Customize the templates as needed, for example to add path-specific protection, adjust score thresholds, or combine bot score with other fields.

These templates use wirefilter expression syntax. In these expressions, `eq` means equals, `le` means less than or equal to, `ge` means greater than or equal to, and `not` excludes matching traffic.

  * [Definite Bots template ↗︎](https://dash.cloudflare.com/?to=/:account/:zone:/security/security-rules/custom-rules/create?template=Definitely%20Bots): Targets malicious bot traffic while ignoring verified bots and routes delivering static content.
        
        (cf.bot_management.score eq 1 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)

  * [Likely Bots template ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules/custom-rules/create?template=Likely%20Bots): Targets traffic likely to be malicious bots while ignoring verified bots and routes with static content. It may contain a small amount of non-bot traffic.
        
        (cf.bot_management.score ge 2 and cf.bot_management.score le 29 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)

  * (Optional) [JavaScript detections template ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules/custom-rules/create?template=JavaScript%20Verified%20URLs): You must first enable JavaScript Detections from Security Settings, then set up a [managed challenge](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge). Make sure to add a method and URI path. JavaScript detections improves security for URLs that should only expect JavaScript-enabled clients.
        
        (not cf.bot_management.js_detection.passed and http.request.method eq "" and http.request.uri.path in {""})




[PreviousSuper Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/)[NextOverview](https://developers.cloudflare.com/bots/concepts/bot/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/bots/get-started/bot-management.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
