---
url: https://developers.cloudflare.com/changelog/post/2026-11-23-expanded-metadata-preservation/
title: Expanded support for EXIF, XMP, and IPTC-IIM metadata in Images \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:00.192288+00:00
---

# Expanded support for EXIF, XMP, and IPTC-IIM metadata in Images · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-23-expanded-metadata-preservation/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 23, 2026

## Expanded support for EXIF, XMP, and IPTC-IIM metadata in Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

In [Images](https://developers.cloudflare.com/images/), the [`metadata` parameter](https://developers.cloudflare.com/images/optimization/features/#metadata) now supports Extensible Metadata Platform (XMP) metadata preservation and expands Exchangeable Image File Format (EXIF) metadata preservation to additional image formats. It can also preserve selected legacy Information Interchange Model (IPTC-IIM) metadata from JPEG sources, mapping it to XMP when converting to compatible formats.

This release does not change existing [Content Credentials](https://developers.cloudflare.com/images/optimization/preserve-content-credentials/) support, which can provide tamper-evident provenance and disclose how AI contributed to an image.

#### What changed

Previously, Images preserved EXIF metadata only for JPEG-to-JPEG optimizations, and did not preserve XMP or IPTC-IIM metadata. You can now keep EXIF and XMP metadata when both the source and output formats support the corresponding metadata type. For JPEG sources, you can also retain selected legacy IPTC-IIM attribution and rights metadata.

EXIF, XMP, and IPTC-IIM carry complementary information about an image. For example, publishers can retain copyright and attribution, and photographers can display capture settings alongside images on portfolio sites. E-commerce and digital asset management workflows can carry product details, captions, and internal asset information into optimized images without reattaching that information.

EXIF, XMP, and IPTC-IIM support varies by source and output format:

Format | Read from source | Write to output  
---|---|---  
JPEG | EXIF, XMP, and IPTC-IIM | EXIF, XMP, and IPTC-IIM  
PNG | EXIF and XMP | EXIF and XMP  
WebP | EXIF and XMP | EXIF and XMP  
AVIF | EXIF and XMP | EXIF  
HEIC | EXIF and XMP | Not an output format  
GIF | Not supported | XMP  
TIFF | Not supported | Not an output format  
  
For example, you can convert a high-resolution JPEG to WebP while keeping both EXIF and XMP metadata.

With `metadata=keep`, JPEG outputs retain the original IPTC-IIM metadata. For PNG, WebP, and GIF outputs, Images maps supported IPTC-IIM fields to XMP. If the source already contains XMP, Images preserves that XMP without merging the IPTC-IIM fields.

#### How it works

Use `metadata` to control how Images handles supported metadata in re-encoded outputs. The default remains `copyright`, so existing requests may now preserve an EXIF copyright tag in PNG, WebP, or AVIF outputs when the source contains one.

The following URL transformation converts a JPEG source to WebP and requests metadata preservation:
    
    
    https://example.com/cdn-cgi/image/format=webp,metadata=keep/source.jpg

Use the same setting in a [Worker `fetch()`](https://developers.cloudflare.com/images/optimization/transformations/transform-via-workers/) subrequest:
    
    
    export default {
    	async fetch() {
    		return fetch("https://example.com/source.jpg", {
    			cf: {
    				image: {
    					format: "webp",
    					metadata: "keep",
    				},
    			},
    		});
    	},
    };
    
    
    export default {
    	async fetch() {
    		return fetch("https://example.com/source.jpg", {
    			cf: {
    				image: {
    					format: "webp",
    					metadata: "keep",
    				},
    			},
    		});
    	},
    };

Refer to the [`metadata` parameter](https://developers.cloudflare.com/images/optimization/features/#metadata).
