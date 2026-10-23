---
url: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected/
title: Profiling limitations \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:44.974730+00:00
---

# Profiling limitations  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/tracing/profiling-manager/will-my-profile-always-be-collected/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Profiling limitations Stay organized with collections  Save and categorize content based on your preferences. 

There are multiple situations where the profile collection might not go as expected:

  * The profile collection fails due to an internal error. If this happens, the [`ProfilingResult`](https://developer.android.com/reference/android/os/ProfilingResult) API tells you about the errors.
  * The profile collection fails due to rate limiting. For more information, see How rate limiting works
  * The profile collection succeeds, but the app isn't immediately notified. This can happen if the app crashes during long profile collections. If the app closes, the system automatically stops and saves the profile. The app is informed about the collected profile when it restarts and registers a general listener with `ProfilingManager`.



## How rate limiting works

`ProfilingManager` includes a rate limiter for both individual apps and the entire system. The rate limiter prevents apps from using too many system resources by recording too many profiles, because a full profiling session uses a lot of resources.

**Key Point:** You can tell if your app has been rate-limited by checking the `ProfilingResult`. You will see either the `ERROR_FAILED_RATE_LIMIT_PROCESS` or `ERROR_FAILED_RATE_LIMIT_SYSTEM` error.

Both the app and system rate limiters assign a cost to each type of profile collected, because some profiles are more resource-intensive than others. The app limiter controls how much an individual app can record based on its total cost. The system limiter, however, controls the total cost of all profiles recorded by all apps.

The rate limiter sets a total cost that each app can use (this cost is the same for all apps). Each profile uses a part of this total cost, depending on its type.

The rate limiter uses three time periods:

  * **Per Hour:** There's a maximum cost allowed per hour.
  * **Per Day:** There's a maximum cost allowed per day.
  * **Per Week:** There's a maximum cost allowed per week.



The rate limiter sets a total cost that can be used within each of these periods. For example, an app might be allowed to record X profiles per hour, Y per day, and Z per week. If your app reaches its limit in any of these periods, future profile requests will result in an `ERROR_FAILED_RATE_LIMIT_PROCESS` error.

These time periods work similarly for system-level rate limiting. However, the system rate limiter is a global limit shared by all apps. This limit is set separately from the individual app quotas, but every profile contributes to it, using the same hourly, daily, and weekly periods. If this global limit is reached, you will receive the `ERROR_FAILED_RATE_LIMIT_SYSTEM` error.

**Tip:** For local profiling, you can [disable the rate limiter](https://developer.android.com/topic/performance/tracing/profiling-manager/debug-mode#disable-rate-limiter).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
