---
url: https://developer.android.com/topic/performance/issues/bitmap-memory-usage/
title: Bitmap memory usage \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:19.968323+00:00
---

# Bitmap memory usage  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/issues/bitmap-memory-usage/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Bitmap memory usage Stay organized with collections  Save and categorize content based on your preferences. 

Bitmaps are often the largest memory-consuming objects in an app. Decoding and scaling operations are frequently on the critical path for frame rendering. Optimizing bitmap memory usage provides significant improvements in UI responsiveness, battery life, and overall stability by reducing jank, ANRs, and OOM-related process kills.

**Note:** For information on how Android Play Vitals tracks and reports this issue, see [Bitmap memory usage in Android vitals](https://developer.android.com/google/play/vitals/bitmap-memory-usage).

## Contributors to high bitmap memory usage

**Note:** Bitmap memory usage doesn't always correlate with [anonymous RSS + swap memory usage](https://developer.android.com/topic/performance/issues/memory-usage). This is because bitmap memory usage includes bitmaps allocated on the heap using `malloc` as well as other bitmaps (for example, bitmaps backed by shared memory or graphics buffers), while anonymous RSS + Swap includes only those bitmaps allocated using `malloc`.

Virtual memory that was never used may also be included in the calculation. If you see unexpectedly high bitmap memory usage, verify you're not allocating memory that goes unused.

## Resources

### Analyze bitmaps in Android Studio

#### Android Studio profiling for bitmaps

Use the Memory Profiler to inspect memory allocations in real-time, capture heap dumps, and analyze objects for memory leaks; additionally, use the heap analyzer to detect memory leaks, identify duplicate bitmap allocations, and visualize object retention.

#### Automated leak detection with LeakCanary

Integrate the LeakCanary library to automate the detection of memory leaks in your app. LeakCanary provides automatic heap analysis, identifying objects that should have been garbage collected but are still held in memory, such as bitmaps retained by destroyed components.

### Bitmap Performance Documentation

These resources provide comprehensive guidance on best practices for efficient bitmap handling across different Android components.

  * [Managing Bitmap Memory](https://developer.android.com/topic/performance/graphics/manage-memory)
  * [Optimizing Bitmap Images](https://developer.android.com/develop/ui/compose/graphics/images/optimization)
  * [Manage your app's memory](https://developer.android.com/topic/performance/memory/manage-app-memory)



### Developer checklist for optimizing bitmap memory usage

To optimize bitmap memory efficiency, follow the three core principles: reduce, reuse, and recycle.

  * **Reduce** : Minimize the initial memory footprint when loading or displaying bitmaps.
  * **Reuse** : Implement caching mechanisms to avoid redundant bitmap allocations.
  * **Recycle** : Proactively release resources to allow memory re-allocation for active processes.



The following developer checklist can help you optimize bitmap memory usage.

Core Principle | Area | Description  
---|---|---  
**Reduce** | Eliminate Duplicate Bitmaps | Analyze heap dumps [using the Memory Profiler](https://developer.android.com/topic/performance/memory/manage-app-memory#monitor) to detect redundant bitmap allocations. Refer to the [Managing Bitmap Memory](https://developer.android.com/topic/performance/graphics/manage-memory) guide.  
| Leverage Image Loading Libraries | Use [libraries like Glide and Coil](https://developer.android.com/develop/ui/compose/graphics/images/optimization#bitmap-libraries), to automate threading, caching, and efficient decoding.  
| Implement Downsampling | [Decode images](https://developer.android.com/develop/ui/compose/graphics/images/optimization#downsample) to match target UI container dimensions instead of loading full-resolution assets.  
| Use RGB_565 for Opaque Images | Reduce memory footprint by 50% by [switching from `ARGB_8888` to a 16-bit configuration](https://developer.android.com/develop/ui/compose/graphics/images/optimization#pixel-format) for images without transparency.  
| Prioritize VectorDrawables | Use [vectors for icons and basic graphics](https://developer.android.com/develop/ui/compose/graphics/images/optimization#vectors-bitmap) to ensure sharp scaling with minimal memory overhead.  
| Optimize Server-Side Image Delivery | Configure backend APIs to [serve images tailored to device density](https://www.youtube.com/watch?v=4BlGtrTeCMU&t=1234s) and UI container dimensions.  
| Eliminate Transparent Margins | Avoid allocating memory for "invisible" pixels by using InsetDrawable or layout padding instead of baked-in margins. See [Engineering memory-performant Android apps](https://www.youtube.com/watch?v=fOXJR5qLq54).  
**Reuse** | Configure Optimal Cache Sizes | Tailor memory and disk cache limits based on device RAM and screen resolution. Refer to [Caching Bitmaps](https://developer.android.com/topic/performance/graphics/cache-bitmap).  
**Recycle** | Purge Resources in Background | [Implement `TRIM_MEMORY_BACKGROUND`](https://developer.android.com/topic/performance/memory/manage-app-memory#release) to clear caches and improve process survival during system memory pressure.  
| Release Assets when UI is Hidden | [Use `TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/topic/performance/memory/manage-app-memory#release) to release bitmap caches when the app is no longer visible to the user.  
| Monitor for Memory Leaks | Use LeakCanary and Memory Profiler to find bitmaps retained after their LifecycleOwner is destroyed. Refer to [Manage your app's memory](https://developer.android.com/topic/performance/memory/manage-app-memory).  
  
[ Previous arrow_back  Memory Usage (Anonymous RSS + swap)  ](https://developer.android.com/topic/performance/issues/memory-usage)

[ Next Stuck Partial Wake Locks  arrow_forward  ](https://developer.android.com/topic/performance/issues/stuck-wakelock)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
