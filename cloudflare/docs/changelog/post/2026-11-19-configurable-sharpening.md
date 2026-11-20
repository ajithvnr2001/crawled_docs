---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-configurable-sharpening/
title: Apply Gaussian sharpening with Images \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.520971+00:00
---

# Apply Gaussian sharpening with Images · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-configurable-sharpening/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Apply Gaussian sharpening with Images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Images](https://developers.cloudflare.com/images/) lets developers resize, adjust, and manipulate images at scale through a broad set of [optimizations](https://developers.cloudflare.com/images/optimization/features/), including image adjustments such as [`sharpen`](https://developers.cloudflare.com/images/optimization/features/#sharpen), [`brightness`](https://developers.cloudflare.com/images/optimization/features/#brightness), [`contrast`](https://developers.cloudflare.com/images/optimization/features/#contrast), and [`gamma`](https://developers.cloudflare.com/images/optimization/features/#gamma).

The [`sharpen`](https://developers.cloudflare.com/images/optimization/features/#sharpen) parameter now supports Gaussian sharpening, in addition to the existing box-filter sharpening. Sharpening makes fine details appear crisper by increasing the pixel-to-pixel contrast along edges, where adjacent pixels differ in brightness or color. Scalar values such as `sharpen=5` continue to use the box filter.

Different images benefit from different types and levels of sharpening. Text may need strong edge definition for readability; product photography often uses a subtler effect to avoid emphasizing grain; and illustrations with bold, clean lines and large areas of solid color can benefit from emphasizing larger edges and object outlines.

Both box and Gaussian sharpening use unsharp masking, a technique that first creates a blurred version of the source image and subtracts it from the original to isolate edge details. Sharpening then adds a controlled amount of that detail back to the source along these boundaries, improving the perceived clarity of an image.

Each filter uses a different method to produce the blur used for this comparison. The existing box filter produces a uniform blur by averaging each pixel with its eight surrounding pixels, weighing all nine equally. A Gaussian filter gives more weight to pixels closer to the center and provides more control to help prevent sharpening from treating unintended parts of an image as edges.

Box sharpening offers a simple, predictable configuration for direct, crisp effects on text, screenshots, and simple graphics. Gaussian sharpening can produce smoother transitions for photography and offers more control over which details are emphasized.

To use Gaussian sharpening, set the `mode` setting to `gaussian`, then configure its behavior using the additional `amount`, `sigma`, and `threshold` settings:

  * **Amount** adjusts how strongly Images increases contrast around identified edges. It accepts values from `0` to `10`.
  * **Sigma** controls the spread of the Gaussian blur, which determines how far the sharpening effect extends around an edge. It accepts values greater than `0` and up to `5`.
  * **Threshold** (optional) excludes pixel differences below a specified value, which can reduce sharpening of low-contrast noise, grain, or smooth areas. It accepts integers from `0` to `255`.



Together, these settings let you tailor the sharpening effect to your content.

In the URL interface, these settings are grouped beneath the `sharpen` parameter:
    
    
    sharpen=(mode=gaussian,amount=1,sigma=1.5,threshold=0)

The same structure maps directly to the `cf.image` object in a [Workers](https://developers.cloudflare.com/workers/) `fetch()` subrequest:
    
    
    cf: {
    	image: {
    		sharpen: {
    			mode: "gaussian",
    			amount: 1,
    			sigma: 1.5,
    			threshold: 0,
    		},
    	},
    }

When using the [Images binding](https://developers.cloudflare.com/images/optimization/binding/), pass the structured `sharpen` object directly to `.transform()`:
    
    
    const result = await env.IMAGES.input(source.body)
    	.transform({
    		sharpen: {
    			mode: "gaussian",
    			amount: 2,
    			sigma: 1.5,
    			threshold: 0,
    		},
    	})
    	.output({ format: "image/avif" });
    
    return result.response();

Refer to [`sharpen`](https://developers.cloudflare.com/images/optimization/features/#sharpen).
