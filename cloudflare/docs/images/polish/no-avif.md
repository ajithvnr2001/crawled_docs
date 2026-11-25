---
url: https://developers.cloudflare.com/images/polish/no-avif/
title: AVIF may be skipped \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.996962+00:00
---

# AVIF may be skipped · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/polish/no-avif/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /[Cloudflare Polish](https://developers.cloudflare.com/images/polish/)
  4. /AVIF may be skipped



# AVIF may be skipped

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPolish never makes files largerAVIF requires a minimum image sizeAVIF does not support animated imagesAVIF conversion may be temporarily unavailableAVIF compression efficiency may vary under high demand

Polish avoids converting images to the AVIF format when such conversion would increase the file size. AVIF also has a few format-specific requirements, and capacity limits that can occasionally cause Polish to skip AVIF conversion for a particular request.

## Polish never makes files larger

When converting an image to AVIF would increase its file size, Polish skips the conversion and keeps the original format. Like WebP, AVIF is less likely to improve on already heavily-compressed or low-quality JPEG images, since there is less redundant data left to remove.

## AVIF requires a minimum image size

AVIF does not support images smaller than 16x16 pixels. If your image is smaller than this, Polish will not produce an AVIF version, and will serve the original format (or WebP, if enabled) instead.

## AVIF does not support animated images

Unlike WebP, AVIF does not support animated images. If the origin image is animated (for example, an animated GIF or animated PNG), Polish will not produce an AVIF version of it.

## AVIF conversion may be temporarily unavailable

AVIF compression is more computationally intensive than Polish's other compression options. During periods of high demand, Polish may be temporarily unable to produce an AVIF version for some requests. When this happens, Polish serves the original format (or a WebP version, if enabled). A subsequent request for the same image may successfully produce an AVIF version once demand decreases.

## AVIF compression efficiency may vary under high demand

To maintain fast response times, Polish may use faster, less exhaustive compression settings for AVIF during periods of high demand. This can result in a larger AVIF file than Polish would otherwise produce, though Polish still only serves AVIF when it is smaller than the original image.

[PreviousTroubleshooting](https://developers.cloudflare.com/images/polish/troubleshooting-polish/)[NextWebP may be skipped](https://developers.cloudflare.com/images/polish/no-webp/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/polish/no-avif.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
