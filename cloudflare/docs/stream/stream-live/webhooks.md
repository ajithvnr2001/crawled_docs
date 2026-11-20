---
url: https://developers.cloudflare.com/stream/stream-live/webhooks/
title: Receive Live Webhooks \u00b7 Cloudflare Stream docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:41.158048+00:00
---

# Receive Live Webhooks · Cloudflare Stream docs

> Source: https://developers.cloudflare.com/stream/stream-live/webhooks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Stream](https://developers.cloudflare.com/stream/)
  3. /[Stream live video](https://developers.cloudflare.com/stream/stream-live/)
  4. /Receive Live Webhooks



# Receive Live Webhooks

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSubscribe to Stream Live Webhooks

Stream Live offers webhooks to notify your service when an Input connects, disconnects, or encounters an error with Stream Live.

Note

Webhooks works differently for uploaded / on-demand videos. For more information, refer to [Using Webhooks](https://developers.cloudflare.com/stream/manage-video-library/using-webhooks/).

Stream Live Notifications

**Who is it for?**

Customers who are using [Stream](https://developers.cloudflare.com/stream/) and want to receive webhooks with the status of their videos.

**Other options / filters**

You can input Stream Live IDs to receive notifications only about those inputs. If left blank, you will receive a list for all inputs.

The following input states will fire notifications. You can toggle them on or off:

  * `live_input.connected`
  * `live_input.disconnected`

**Included with**

Stream subscription.

**What should you do if you receive one?**

Stream notifications are entirely customizable by the customer. Action will depend on the customizations enabled.

## Subscribe to Stream Live Webhooks

  1. In the Cloudflare dashboard, go to the **Notifications** page.

[ Go to **Notifications** ↗ ](https://dash.cloudflare.com/?to=/:account/notifications)
  2. Select the **Destinations** tab.

  3. On the **Destinations** page under **Webhooks** , select **Create**.

  4. Enter the information for your webhook and select **Save and Test**.

  5. To create the notification, from the **Notifications** page, select the **All Notifications** tab.

  6. Next to **Notifications** , select **Add**.

  7. Under the list of products, locate **Stream** and select **Select**.

  8. Enter a name and optional description.

  9. Under **Webhooks** , select **Add webhook** and select your newly created webhook.

  10. Select **Next**.

  11. By default, you will receive webhook notifications for all Live Inputs. If you only wish to receive webhooks for certain inputs, enter a comma-delimited list of Input IDs in the text field.

  12. When you are done, select **Create**.  
  



Example webhook payloadjson
    
    
    {
      "name": "Live Webhook Test",
      "text": "Notification type: Stream Live Input\nInput ID: eb222fcca08eeb1ae84c981ebe8aeeb6\nEvent type: live_input.disconnected\nUpdated at: 2022-01-13T11:43:41.855717910Z",
      "data": {
        "notification_name": "Stream Live Input",
        "input_id": "eb222fcca08eeb1ae84c981ebe8aeeb6",
        "event_type": "live_input.disconnected",
        "updated_at": "2022-01-13T11:43:41.855717910Z"
      },
      "ts": 1642074233
    }

The `event_type` property of the data object will either be `live_input.connected`, `live_input.disconnected`, or `live_input.errored`.

If there are issues detected with the input, the `event_type` will be `live_input.errored`. Additional data will be under the `live_input_errored` json key and will include a `code` with one of the values listed in [Error codes](https://developers.cloudflare.com/stream/stream-live/troubleshooting/#error-codes).

[PreviousSimulcast (restream) videos](https://developers.cloudflare.com/stream/stream-live/simulcasting/)[NextTroubleshooting a live stream](https://developers.cloudflare.com/stream/stream-live/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/stream/stream-live/webhooks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
