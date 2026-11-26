---
url: https://developers.cloudflare.com/images/polish/troubleshooting-polish/
title: Troubleshooting Polish \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:16.239726+00:00
---

# Troubleshooting Polish · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/polish/troubleshooting-polish/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /[Cloudflare Polish](https://developers.cloudflare.com/images/polish/)
  4. /Troubleshooting



# Troubleshooting Polish

Last updated Nov 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDiagnose PolishCf-Polished status

Use this page to determine why Polish did not process an image or why it served the original format instead of AVIF or WebP.

## Diagnose Polish

Start with these checks to confirm that Polish processed the image and that the request is eligible for the expected output format.

  1. Confirm that `polish` is set to `lossless` or `lossy`.
  2. If you expect AVIF or WebP, confirm that the corresponding setting is `on`.
  3. Purge the image with a single-file cache purge.
  4. Confirm that the request’s `Accept` header includes `image/avif` or `image/webp`.
  5. Inspect the `Cf-Polished` response header.



When Polish processes an image, the `Cf-Polished` response header reports the result.

If the `Cf-Polished` header is absent after you purge the image, confirm that the origin returns an image `Content-Type`, a cacheable `Cache-Control` value, and a supported `Vary` header.

## `Cf-Polished` status

Use the following table to interpret each `Cf-Polished` status and identify the appropriate next steps.

Status | What it means | Recommended action  
---|---|---  
`input_too_large` | The input image is too large or complex to process. | Use a lower-resolution PNG or JPEG image that is smaller than 20 MB and less than 4,000 pixels in any dimension.  
`not_compressed` or `not_needed` | The image was fully optimized at the origin, so Polish did not apply compression. | No action required.  
`webp_bigger` | Polish attempted WebP conversion, but the WebP output was not better than the original. The status appears on the JPEG or PNG response because no WebP version was created. | Refer to [WebP may be skipped](https://developers.cloudflare.com/images/polish/no-webp/).  
`avif_bigger` | Polish attempted AVIF conversion, but the AVIF output was not better than the original. The status appears on the JPEG or PNG response because no AVIF version was created. | Refer to [AVIF may be skipped](https://developers.cloudflare.com/images/polish/no-avif/).  
`avif_overloaded` | Polish could not create an AVIF version because AVIF capacity was temporarily unavailable. The status appears on the JPEG or PNG response. | Retry the request. If the problem continues, refer to [AVIF may be skipped](https://developers.cloudflare.com/images/polish/no-avif/).  
`cannot_optimize` or `internal_error` | The input image is corrupted or incomplete at the origin. | Upload a new version of the image to the origin.  
`format_not_supported` | The input format is unsupported, such as BMP or TIFF, or origin optimization software is incompatible with Polish. | Convert the image to PNG or JPEG, disable the additional origin optimization software, or both.  
`vary_header_present` | The origin returned a `Vary` header with a value other than `accept-encoding`. | Polish works when `accept-encoding` is the only value in the `Vary` header. If the origin converts images to WebP, disable that conversion and let Polish perform it. Polish skips URLs processed by [Images](https://developers.cloudflare.com/images/optimization/transformations/url/).  
  
[PreviousConfigure Polish](https://developers.cloudflare.com/images/polish/configure-polish/)[NextAVIF may be skipped](https://developers.cloudflare.com/images/polish/no-avif/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/polish/troubleshooting-polish.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
