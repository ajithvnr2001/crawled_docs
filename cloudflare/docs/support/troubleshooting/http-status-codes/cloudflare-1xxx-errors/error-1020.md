---
url: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/
title: Error 1020 \u00b7 Cloudflare Support docs
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:53:09.675183+00:00
---

# Error 1020 · Cloudflare Support docs

> Source: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Support](https://developers.cloudflare.com/support/)
  3. /…

[Troubleshooting](https://developers.cloudflare.com/support/troubleshooting/)[HTTP Status Codes](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/)

  4. /[Cloudflare 1xxx errors](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/)
  5. /Error 1020



# Error 1020

Last updated Oct 14, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError 1020: Access denied Common cause Resolution

## Error 1020: Access denied

This error indicates that a Cloudflare security feature configured by the website owner blocked the request. Cloudflare returns it with an HTTP `403` status code.

### Common cause

A security rule with a _Block_ action matched the request, and the rule has no custom response configured. For example, [API Shield schema validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) and [JWT validation](https://developers.cloudflare.com/api-shield/security/jwt-validation/) can block requests with a 1020 error.

Requests blocked by [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) or [WAF managed rules](https://developers.cloudflare.com/waf/managed-rules/) do not get a 1020 error. These requests get the WAF block response instead. For details, refer to [Different error page for blocked requests](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/#different-error-page-for-blocked-requests).

### Resolution

If you are not the website owner, provide the website owner with a screenshot of the `1020` error message you received.

If you are the website owner:

  1. Retrieve a screenshot of the 1020 error from your customer.

  2. Search the [Security Events log](https://developers.cloudflare.com/waf/analytics/security-events/) (available at **Security** > **Analytics** , in the **Events** tab) for the [Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/) or client IP address from the visitor's 1020 error message. The event shows which security feature and rule blocked the request.

[ Go to **Analytics** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/analytics)

Note

Convert the UTC timestamp of the `1020` error to your local timezone when searching in the Security Events log.

  3. Assess the cause of the block and update the configuration of the security feature or rule that blocked the request.




To customize the 1020 error page that visitors receive, refer to the [custom error rule example for 1020 errors](https://developers.cloudflare.com/rules/custom-errors/example-rules/#custom-html-response-for-cloudflare-1020-errors).

[PreviousError 1019](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1019/)[NextError 1023](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1023/)

Was this helpful?

YesNo
