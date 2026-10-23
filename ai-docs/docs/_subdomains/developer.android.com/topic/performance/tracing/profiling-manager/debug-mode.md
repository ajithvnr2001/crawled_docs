---
url: https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode/
title: Debug commands for local profiling \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:45.933724+00:00
---

# Debug commands for local profiling  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Debug commands for local profiling Stay organized with collections  Save and categorize content based on your preferences. 

While the most useful way to use `ProfilingManager` is to collect profiles from your public users, you might first need to debug your setup or record local profiles for investigations. You might have noticed that profiles are sometimes not recorded, often due to rate limiting. For more information, see [How rate limiting works](https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected#how-rate-limiting-works).

You can adjust specific debug settings on your local device using `adb` commands. The following settings are available to assist with local profiling.

## Disable the rate limiter

The following command is particularly useful when using `ProfilingManager` locally. It disables both the app process and system rate limiters, instructing `ProfilingManager` to fulfill all profile requests without being throttled.
    
    
    adb shell device_config put profiling_testing rate_limiter.disabled true
    

## Retain unredacted traces

The following command lets you retain unredacted versions of traces in the temporary directory located at `/data/misc/perfetto-traces/profiling/<trace-name>.perfetto-trace-unredacted`. Unredacted traces provide more system-level information than redacted traces, which can be crucial for in-depth investigations.
    
    
    adb shell device_config put profiling_testing delete_temporary_results.disabled true
    

For privacy reasons, this feature is only available for local profiling and is disabled by default.

**Note:** Unredacted traces will likely use more storage space than redacted traces because they collect more comprehensive information.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
