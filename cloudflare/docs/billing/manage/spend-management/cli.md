---
url: https://developers.cloudflare.com/billing/manage/spend-management/cli/
title: Manage spending limits and alerts with the cf CLI \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:52.146186+00:00
---

# Manage spending limits and alerts with the cf CLI · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/manage/spend-management/cli/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /…

Manage

  4. /[Spending limits and alerts](https://developers.cloudflare.com/billing/manage/spend-management/)
  5. /cf CLI



# Manage spending limits and alerts with the cf CLI

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you beginCreate a spending limitCreate an email alertPolicy optionsList and inspect policiesUpdate a policyDelete a policyReview historyResolve errors

Use the [Cloudflare CLI (`cf`)](https://developers.cloudflare.com/cf/) to manage spending limits and email alerts. In the API, each limit or alert is a _spend policy_ that applies to one product across your account.

## Before you begin

  * Review [how spending limits and alerts work](https://developers.cloudflare.com/billing/manage/spend-management/).
  * [Install `cf` and sign in](https://developers.cloudflare.com/cf/get-started/).
  * For API tokens, use **Account** > **Billing** > **Read** to inspect policies, or **Edit** to change them.
  * [Select the account](https://developers.cloudflare.com/cf/get-started/#select-an-account) you want to manage. Use its account ID, rather than a zone ID.



## Create a spending limit

This command sets a $50 spending limit for Workers usage and sends notifications to `billing@example.com`. Replace the email address with your recipient's address. Review [what a Workers limit blocks](https://developers.cloudflare.com/workers/platform/spend-management/) before running it.
    
    
    cf billing spend-policies create \
      --name 'Workers $50 spending limit' \
      --product-id workers \
      --enabled true \
      --threshold-cents 5000 \
      --action usage_block \
      --notification-email billing@example.com

Save the returned policy `id`. To preview the request without creating a policy, add `--dry-run`.

To set a spending limit for Durable Objects, use `--product-id durable_objects` and a descriptive name. You can have one enabled limit per product on an account.

This limit counts spend already recorded in the current billing period. It can block usage shortly after creation if that spend has already reached $50.

## Create an email alert

Use `--action notification` to send email without blocking usage. This command creates a $20 Durable Objects email alert:
    
    
    cf billing spend-policies create \
      --name 'Durable Objects $20 email alert' \
      --product-id durable_objects \
      --enabled true \
      --threshold-cents 2000 \
      --action notification \
      --notification-email billing@example.com

Replace the email address with your recipient's address. This alert can notify you at $16 (80%) and $20 (100%). Durable Objects continues running at both thresholds.

You can create multiple alerts, including alongside a limit.

## Policy options

Provide every required option when creating or updating a policy.

Option | Value  
---|---  
`--name` | Required. A descriptive name, up to 200 bytes.  
`--product-id` | Required. `workers` or `durable_objects`.  
`--enabled` | Required. `true` to evaluate the policy; `false` to turn it off.  
`--threshold-cents` | Required. A positive whole number of US cents. For example, `5000` means $50. Zero is not supported.  
`--action` | Required. `notification` for an email alert, or `usage_block` for a limit.  
`--notification-email` | One email address. Required for alerts; optional for limits. A limit without an address sends no email.  
  
## List and inspect policies

List your account's policies:
    
    
    cf billing spend-policies list

The list includes policies that are turned off and excludes deleted policies.

To inspect one policy, replace `<POLICY_ID>` with its `id`:
    
    
    cf billing spend-policies get <POLICY_ID>

The response includes a `version`. You need the latest version to update or delete a policy.

## Update a policy

Updates replace the whole policy. Provide every required option, even when changing only the limit amount.

Preserve `--notification-email` if you want to keep receiving email. To add email to an existing limit, include this option with your recipient's address.

  1. Fetch the latest policy and its `version`:
         
         cf billing spend-policies get <POLICY_ID>

  2. Update the policy. This example raises the Workers limit to $100. Replace `<POLICY_ID>` with its `id` and `<VERSION>` with the version you just fetched:
         
         cf billing spend-policies update <POLICY_ID> \
           --if-match <VERSION> \
           --name 'Workers $100 spending limit' \
           --product-id workers \
           --enabled true \
           --threshold-cents 10000 \
           --action usage_block \
           --notification-email billing@example.com

  3. Check the returned settings and new `version`.




The `--if-match` option prevents your update from overwriting someone else's newer changes.

Use the same update command with all required options to:

  * Turn a policy off with `--enabled false`.
  * Turn it back on with `--enabled true`.
  * Switch a limit to an alert with `--action notification` and `--notification-email`.
  * Switch an alert to a limit with `--action usage_block`.



Lowering a limit below current spend can trigger a pause. Raising it above current spend, turning it off, or switching it to an alert lifts its block. Changes take time to apply and do not reset recorded spend.

## Delete a policy

Fetch the latest policy version:
    
    
    cf billing spend-policies get <POLICY_ID>

Then delete the policy. Replace `<VERSION>` with the version you just fetched:
    
    
    cf billing spend-policies delete <POLICY_ID> --if-match <VERSION>

Confirm the deletion when prompted. Deleting a limit lifts its block, and further usage can incur charges.

## Review history

The API provides separate history for configuration changes and automatic threshold events. Configuration changes also appear in [Cloudflare's account-wide Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

List configuration changes across the account, including deleted policies:
    
    
    cf billing spend-policies activity --limit 50

Entries include the actor and before and after settings. To retrieve older entries, pass the returned `result_info.cursor` as `<CURSOR>`:
    
    
    cf billing spend-policies activity --limit 50 --cursor '<CURSOR>'

List automatic threshold events for one policy. These events occur when spending reaches a threshold, without a user making an API request:
    
    
    cf billing spend-policies audit <POLICY_ID> --limit 50

Events include `approaching_limit` at 80% and `limit_reached` at 100%. Threshold history does not support pagination and is unavailable after a policy is deleted.

Both history commands default to 50 entries and accept a maximum `--limit` of 100.

A threshold event can be recorded again after a policy update. It records evaluation, rather than confirmation that blocking or email delivery succeeded.

## Resolve errors

HTTP status | What to check  
---|---  
`400` | Check the product, positive integer threshold, required options, and email format.  
`403` | Check your account and Billing Read or Edit permissions.  
`404` | Check the policy ID and account, and confirm that the policy still exists.  
`409` | An enabled limit already exists for that product. Update it, or turn it off before enabling another.  
`412` | Someone changed the policy. Fetch it again, review the new settings, and retry with its current version.  
`428` | Add `--if-match` with the current positive integer version.  
  
[PreviousOverview](https://developers.cloudflare.com/billing/manage/spend-management/)[NextInstant Bank Payments via Link](https://developers.cloudflare.com/billing/payment-methods/instant-bank-payments-link/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/manage/spend-management/cli.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
