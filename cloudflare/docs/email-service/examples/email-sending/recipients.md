---
url: https://developers.cloudflare.com/email-service/examples/email-sending/recipients/
title: Specify recipients \u00b7 Cloudflare Email Service docs
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:27.357943+00:00
---

# Specify recipients · Cloudflare Email Service docs

> Source: https://developers.cloudflare.com/email-service/examples/email-sending/recipients/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Email Service](https://developers.cloudflare.com/email-service/)
  3. /…

Examples

  4. /Email sending
  5. /Specify recipients



# Specify recipients

Specify multiple recipients, CC and BCC, and named addresses when sending with Email Service.

Last updated Nov 11, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMultiple recipientsCC and BCCNamed recipientsMixed plain and named recipientsNext steps

Email Service lets you specify recipients in several ways — multiple recipients, CC and BCC, and named addresses — using the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/), the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/), or [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/). The combined number of addresses across `to`, `cc`, and `bcc` must not exceed 50. See [Limits](https://developers.cloudflare.com/email-service/platform/limits/).

## Multiple recipients
    
    
    const response = await env.EMAIL.send({
    	to: ["customer@example.com", "accounts@example.com"],
    	from: { email: "orders@yourdomain.com", name: "Orders" },
    	subject: "Order #12345 confirmed",
    	html: "<h1>Your order is confirmed</h1>",
    	text: "Your order is confirmed.",
    });
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": ["customer@example.com", "accounts@example.com"],
        "from": { "address": "orders@yourdomain.com", "name": "Orders" },
        "subject": "Order #12345 confirmed",
        "html": "<h1>Your order is confirmed</h1>",
        "text": "Your order is confirmed."
      }'

List every recipient in the `To` header and pass one `--mail-rcpt` flag per address.
    
    
    cat > mail.txt <<EOF
    From: Orders <orders@yourdomain.com>
    To: customer@example.com, accounts@example.com
    Subject: Order #12345 confirmed
    
    Your order is confirmed.
    EOF
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "orders@yourdomain.com" \
      --mail-rcpt "customer@example.com" \
      --mail-rcpt "accounts@example.com" \
      --upload-file mail.txt

## CC and BCC
    
    
    const response = await env.EMAIL.send({
    	to: "customer@example.com",
    	cc: ["manager@example.com"],
    	bcc: ["archive@example.com"],
    	from: "orders@yourdomain.com",
    	replyTo: "support@yourdomain.com",
    	subject: "Order Confirmation #12345",
    	html: "<h1>Your order is confirmed</h1>",
    	text: "Your order is confirmed",
    });
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": "customer@example.com",
        "cc": ["manager@example.com"],
        "bcc": ["archive@example.com"],
        "from": "orders@yourdomain.com",
        "reply_to": "support@yourdomain.com",
        "subject": "Order Confirmation #12345",
        "html": "<h1>Your order is confirmed</h1>",
        "text": "Your order is confirmed"
      }'

Add a `Cc` header for CC recipients. BCC recipients are added as `--mail-rcpt` flags but omitted from the headers.
    
    
    cat > mail.txt <<EOF
    From: orders@yourdomain.com
    To: customer@example.com
    Cc: manager@example.com
    Reply-To: support@yourdomain.com
    Subject: Order Confirmation #12345
    
    Your order is confirmed
    EOF
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "orders@yourdomain.com" \
      --mail-rcpt "customer@example.com" \
      --mail-rcpt "manager@example.com" \
      --mail-rcpt "archive@example.com" \
      --upload-file mail.txt

## Named recipients

Provide a display name alongside the address for the sender and recipients.
    
    
    const response = await env.EMAIL.send({
    	to: { email: "jane@example.com", name: "Jane Doe" },
    	from: { email: "support@yourdomain.com", name: "Support Team" },
    	subject: "Welcome!",
    	html: "<h1>Thanks for joining!</h1>",
    	text: "Thanks for joining!",
    });
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": { "address": "jane@example.com", "name": "Jane Doe" },
        "from": { "address": "support@yourdomain.com", "name": "Support Team" },
        "subject": "Welcome!",
        "html": "<h1>Thanks for joining!</h1>",
        "text": "Thanks for joining!"
      }'

Use the `Display Name <address>` form in the `From` and `To` headers.
    
    
    cat > mail.txt <<EOF
    From: Support Team <support@yourdomain.com>
    To: Jane Doe <jane@example.com>
    Subject: Welcome!
    
    Thanks for joining!
    EOF
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "support@yourdomain.com" \
      --mail-rcpt "jane@example.com" \
      --upload-file mail.txt

## Mixed plain and named recipients

Combine plain addresses and named addresses in the same `to` field.
    
    
    const response = await env.EMAIL.send({
    	to: ["plain@example.com", { email: "jane@example.com", name: "Jane Doe" }],
    	from: "support@yourdomain.com",
    	subject: "Support request #12345 updated",
    	html: "<h1>Your support request was updated</h1>",
    	text: "Your support request was updated.",
    });
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/email/sending/send" \
      --header "Authorization: Bearer <API_TOKEN>" \
      --header "Content-Type: application/json" \
      --data '{
        "to": [
          "plain@example.com",
          { "address": "jane@example.com", "name": "Jane Doe" }
        ],
        "from": "support@yourdomain.com",
        "subject": "Support request #12345 updated",
        "html": "<h1>Your support request was updated</h1>",
        "text": "Your support request was updated."
      }'
    
    
    cat > mail.txt <<EOF
    From: support@yourdomain.com
    To: plain@example.com, Jane Doe <jane@example.com>
    Subject: Support request #12345 updated
    
    Your support request was updated.
    EOF
    
    curl --ssl-reqd \
      --url "smtps://smtp.mx.cloudflare.net:465" \
      --user "api_token:<API_TOKEN>" \
      --mail-from "support@yourdomain.com" \
      --mail-rcpt "plain@example.com" \
      --mail-rcpt "jane@example.com" \
      --upload-file mail.txt

## Next steps

  * [Workers API](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/) — full `send()` reference.
  * [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) — send over HTTPS.
  * [SMTP](https://developers.cloudflare.com/email-service/api/send-emails/smtp/) — send from any SMTP-capable client.
  * [Email attachments](https://developers.cloudflare.com/email-service/examples/email-sending/email-attachments/) — send PDFs, inline images, and uploads.



[PreviousSuppression lists](https://developers.cloudflare.com/email-service/concepts/suppressions/)[NextUser signup flow](https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/email-service/examples/email-sending/recipients.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
