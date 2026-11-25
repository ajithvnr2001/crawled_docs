---
url: https://developers.cloudflare.com/changelog/post/2026-11-24-email-sending-workers-free/
title: Email Sending is now available on the Workers Free plan \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.265303+00:00
---

# Email Sending is now available on the Workers Free plan · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-24-email-sending-workers-free/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 24, 2026

## Email Sending is now available on the Workers Free plan

[Email Service](https://developers.cloudflare.com/email-service/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/) is now available on the Workers Free plan for sending to the [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/destination-addresses/) in your account.

You can now onboard [sending domains](https://developers.cloudflare.com/email-service/configuration/domains/), send for free to [verified destination addresses](https://developers.cloudflare.com/email-service/configuration/destination-addresses/) during development and testing, and upgrade to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) when going to production to send to arbitrary addresses. Use the Workers binding, the REST API, or SMTP to send alerts, reports, and notifications to your own team without a paid plan.

Sends to verified destination addresses are free on every plan. They do not count toward the monthly quota or the daily sending limits.

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		try {
    			await env.EMAIL.send({
    				from: "alerts@yourdomain.com",
    				to: "oncall@example.com", // A verified destination address
    				subject: "Disk usage above 90%",
    				text: "Disk usage on db-1 is above 90%.",
    			});
    		} catch (error) {
    			if (error.code === "E_RECIPIENT_PLAN_RESTRICTED") {
    				return new Response("Recipient is not a verified destination address", {
    					status: 403,
    				});
    			}
    			throw error;
    		}
    
    		return new Response("Alert sent");
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		try {
    			await env.EMAIL.send({
    				from: "alerts@yourdomain.com",
    				to: "oncall@example.com", // A verified destination address
    				subject: "Disk usage above 90%",
    				text: "Disk usage on db-1 is above 90%.",
    			});
    		} catch (error) {
    			if (error.code === "E_RECIPIENT_PLAN_RESTRICTED") {
    				return new Response("Recipient is not a verified destination address", {
    					status: 403,
    				});
    			}
    			throw error;
    		}
    
    		return new Response("Alert sent");
    	},
    } satisfies ExportedHandler<Env>;

To send to any recipient, upgrade to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/). Refer to [Limits](https://developers.cloudflare.com/email-service/platform/limits/#verified-destination-addresses) and [Pricing](https://developers.cloudflare.com/email-service/platform/pricing/) for details.

#### Verified sends now appear in Email Sending

Messages that you send from a sending domain to verified destination addresses now count as Email Sending traffic.

Before, the capability to send to verified destination addresses was an Email Routing feature, and these messages were recorded as Email Routing traffic. This change moves this capability to Email Sending, with support for all Email Sending features:

  * The [Activity log](https://developers.cloudflare.com/email-service/observability/logs/) and [Email Sending analytics](https://developers.cloudflare.com/email-service/observability/metrics-analytics/). These messages no longer appear in Email Routing analytics.
  * [Email Sending events](https://developers.cloudflare.com/email-service/reference/event-subscriptions/), such as `message.delivered` and `message.bounced`, published to your event subscriptions.



To find these messages in the [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/), filter the Email Sending datasets on the new `isVerifiedRecipient` field. Messages sent from a domain that has only Email Routing configured are unchanged.
