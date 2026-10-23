---
url: https://developer.android.com/topic/performance/tracing/custom-events/
title: Define custom events \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:46.964754+00:00
---

# Define custom events  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/tracing/custom-events/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Define custom events Stay organized with collections  Save and categorize content based on your preferences. 

System tracing shows you information about processes only at the system level, so it's sometimes difficult to know which of your app or game's methods are executing at a given time relative to system events.

Jetpack provides a tracing API that you can use to label a particular section of code. This information is then reported in traces captured on the device. [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) captures traces with custom trace points automatically.

When using [Perfetto](https://developer.android.com/topic/performance/tracing) to capture system traces, make sure your application is configured as `profileable`. This way, your app's custom trace events appear in the system trace report.
    
    
    fun loadAndProcessData() {
        trace("loadAndProcessData") {
            val data = trace("queryDatabase") {
                queryDatabase()
            }
            trace("processData") {
                processData(data)
            }
        }
    }
    

The [trace function](https://developer.android.com/jetpack/androidx/releases/tracing) automatically ends the trace when the lambda completes. This removes the risk of forgetting to end the tracing.

You can also use an NDK API for custom trace events. To learn about using this API for your native code, see [Custom trace events in native code](https://developer.android.com/topic/performance/tracing/custom-events-native).

## Additional resources

### Views content

  * [Define custom events (Views)](https://developer.android.com/topic/performance/views/tracing/custom-events-views)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [App startup time](https://developer.android.com/topic/performance/issues/launch-time)
  * [Slow rendering](https://developer.android.com/topic/performance/issues/render)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
