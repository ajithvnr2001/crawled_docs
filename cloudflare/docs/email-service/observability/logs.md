---
url: https://developers.cloudflare.com/email-service/observability/logs/
title: Activity log \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:38:30.834733+00:00
---

# Activity log · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/observability/logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /Observability
  4. /Activity log



# Activity log

Email sending and routing statuses, authentication details, and message fields

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEmail sending statusesEmail routing statusesEmail details Authentication status Delivery information Message preview

The Email Service Activity log lists sending and routing events. Each event includes delivery and authentication details.

The Activity log allows you to sort through all email activities and check actions taken by Email Service. In the dashboard you can filter the Activity log to a time range between 30 minutes and 30 days, or specify a custom range.

The Activity log surfaces the same per-event data that is also available programmatically through the [`emailSendingAdaptive` and `emailRoutingAdaptive` datasets](https://developers.cloudflare.com/email-service/observability/metrics-analytics/) in the GraphQL Analytics API.

For Email Routing, you can expand an individual email in the Activity log to inspect authentication results ([SPF ↗︎](https://datatracker.ietf.org/doc/html/rfc7208), [DKIM ↗︎](https://datatracker.ietf.org/doc/html/rfc6376), and [DMARC ↗︎](https://datatracker.ietf.org/doc/html/rfc7489)).

## Email sending statuses

For outbound emails sent through Email Service:

  * **Sent** : Email successfully accepted and queued for delivery.
  * **Delivered** : Email successfully delivered to recipient's mail server.
  * **Delivery failed** : Email bounced (hard or soft bounce). This corresponds to the `deliveryFailed` status in the [GraphQL Analytics API](https://developers.cloudflare.com/email-service/observability/metrics-analytics/).
  * **Rejected** : Email was not sent because the recipient is on your account's [suppression list](https://developers.cloudflare.com/email-service/concepts/suppressions/).
  * **Failed** : Email failed to send due to configuration or authentication issues.



## Email routing statuses

For inbound emails processed through Email Routing:

  * **Forwarded** : Email successfully forwarded to destination address.
  * **Handled** : Email processed by a Worker handler.
  * **Dropped** : Email dropped due to filtering rules or configuration.
  * **Rejected** : Email rejected due to SPF, DKIM, or DMARC failures.
  * **Delivery failed** : Email could not be delivered to the destination address.
  * **Error** : Email could not be processed due to an internal error.



## Email details

Select any email in the Activity log to expand its details and view authentication and delivery information.

### Authentication status

Check the status of email authentication protocols:

  * **SPF status** : Shows pass/fail for Sender Policy Framework validation.
  * **DKIM status** : Shows pass/fail for DomainKeys Identified Mail signature verification.
  * **DMARC status** : Shows pass/fail for Domain-based Message Authentication compliance.



### Delivery information

For sent emails, see delivery details:

  * Recipient mail server response.
  * Delivery attempts and timestamps.
  * Bounce reason codes and categories.
  * Final delivery status.



### Message preview

For sent emails, expand the email in the Activity log to open the **Preview** section and inspect the message as it was sent. The preview provides the following tabs:

  * **HTML** : The rendered HTML body.
  * **Text** : The plain text body.
  * **Headers** : The message headers.
  * **Attachments** : Files included with the message.
  * **Raw** : The full raw [RFC 5322 ↗︎](https://datatracker.ietf.org/doc/html/rfc5322) message source.



To make sent messages previewable, turn on [**Email preview**](https://developers.cloudflare.com/email-service/configuration/domains/#email-preview) for the sending domain. Previews cover messages sent while the setting is turned on and are retained for about seven days. New sending domains have **Email preview** turned on automatically.

[PreviousAudit logs](https://developers.cloudflare.com/email-service/observability/audit-logs/)[NextTest email sending locally](https://developers.cloudflare.com/email-service/observability/local-development/sending/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/observability/logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
