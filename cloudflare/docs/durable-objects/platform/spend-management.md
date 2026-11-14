---
url: https://developers.cloudflare.com/durable-objects/platform/spend-management/
title: Spending limits \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:52.238961+00:00
---

# Spending limits · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/platform/spend-management/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Platform
  4. /Spending limits



# Spending limits

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCharges counted toward the limitWhat stops at the limitOperations that can continueAlarm recoveryResume Durable Objects

[Set a spending limit](https://developers.cloudflare.com/billing/manage/spend-management/) for Durable Objects. It applies across your account, rather than to one namespace or object.

To configure a limit, follow [Set a spending limit in the dashboard](https://developers.cloudflare.com/billing/manage/spend-management/#set-a-spending-limit-in-the-dashboard) or [Manage spending limits and alerts with the cf CLI](https://developers.cloudflare.com/billing/manage/spend-management/cli/).

## Charges counted toward the limit

The limit counts usage charges after included usage for:

  * Requests and duration.
  * SQLite rows read and written.
  * Key-value storage reads, writes, and deletes.



Stored data charges and the shared Workers Paid subscription fee are excluded. Stored data can continue to incur charges during a pause.

## What stops at the limit

Once the limit takes effect, Cloudflare blocks these operations:

Operation | Behavior  
---|---  
New requests through a Durable Object stub | Rejected.  
SQL queries | Reads and writes are rejected.  
SQLite storage growth | Rejected.  
New alarms through `setAlarm()` | Rejected.  
Pending alarms | Held until the block ends, subject to the seven-day limit described in Alarm recovery.  
  
An affected operation can return `Exceeded the account's spending cap for Durable Objects.` A limit does not delete your objects or their stored data.

## Operations that can continue

A limit does not stop every source of charges:

  * Requests already running can continue to accrue duration charges.
  * Messages on WebSocket connections that are already open are not blocked by the limit.
  * Key-value storage operations in legacy key-value-backed objects are not blocked by the limit, even though their charges count toward it.
  * Existing stored data continues to incur storage charges.



Usage reporting and enforcement also take time. These limits mean that a limit does not guarantee a maximum invoice amount.

## Alarm recovery

Cloudflare holds pending alarms while the limit blocks the object. These holds do not use the alarm's normal retry budget.

Caution

An alarm scheduled more than seven days ago is deleted while held. After restoring service, your application must schedule it again if the work is still needed.

Alarms still within that limit can run once the block ends. Plan for delayed work when restoring service.

## Resume Durable Objects

[Raise the limit above current spend, turn it off, or remove it](https://developers.cloudflare.com/billing/manage/spend-management/#resume-service-or-change-a-limit). Changes can take a few minutes to apply.

The block also expires at the next subscription billing period. An enabled limit remains configured for the new period.

Workers have a [separate limit](https://developers.cloudflare.com/workers/platform/spend-management/). If the Worker that calls your object is also blocked, restore that Worker before retrying the application.

[PreviousChoose a data or storage product ↗︎](https://developers.cloudflare.com/workers/platform/storage-options/)[NextKnown issues](https://developers.cloudflare.com/durable-objects/platform/known-issues/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/platform/spend-management.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
