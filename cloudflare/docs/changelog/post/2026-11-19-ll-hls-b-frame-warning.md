---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-ll-hls-b-frame-warning/
title: B-frame detection for Low-Latency HLS live streams \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.767184+00:00
---

# B-frame detection for Low-Latency HLS live streams · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-ll-hls-b-frame-warning/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## B-frame detection for Low-Latency HLS live streams

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Stream](https://developers.cloudflare.com/stream/) now emits a warning when B-frames are detected in Low Latency HLS live broadcasts.

The most common cause of freezing and stuttering in LL-HLS live streams is when encoders include B-frames. These frames can reference content that has not yet been transmitted, stalling preparation for delivery. Therefore, B-Frames are not supported _when LL-HLS is enabled_ for a live input.

Stream sends the warning `ERR_LIVE_INPUT_LLHLS_INCOMPATIBLE` once per live session if applicable. It is reported alongside other error and status events in:

  * Your live input's [**Logs** tab](https://developers.cloudflare.com/stream/stream-live/troubleshooting/#error-codes)
  * [Live webhooks](https://developers.cloudflare.com/stream/stream-live/webhooks/)
  * [GraphQL input events](https://developers.cloudflare.com/stream/getting-analytics/fetching-bulk-analytics/#rtmp-and-srt-input-metrics)



To resolve the warning, turn off B frames in your broadcast application settings. Alternatively, turn off Low-Latency HLS in your live input settings, but playback latency will be higher.

For more information, refer to [Stream live troubleshooting](https://developers.cloudflare.com/stream/stream-live/troubleshooting/#error-codes).
