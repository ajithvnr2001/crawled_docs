---
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-control-app/
title: Control your app from Macrobenchmark \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:50.363213+00:00
---

# Control your app from Macrobenchmark  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-control-app/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Control your app from Macrobenchmark Stay organized with collections  Save and categorize content based on your preferences. 

Unlike most Android UI tests, Macrobenchmark tests run in a separate process from the app itself. This is necessary to enable things like stopping the app process and compiling from DEX bytecode to machine code.

You can drive your app's state using the [UIAutomator library](https://developer.android.com/training/testing/ui-automator) or other mechanisms that can control the target app from the test process. To expose Compose elements to UI Automator, use `Modifier.testTag`.

**Note:** To let UI Automator map these tags to resource IDs, you must also set the `testTagsAsResourceId` semantics property to `true` on a parent composable.

The following example uses a `LazyColumn` with a `testTag`:
    
    
    @Composable
    fun ProductListScreen() {
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .testTag("my_lazy_column")    ) {
            items(100) { index ->
                ProductItem(index)
            }
        }
    }
    

The test uses the `testTag` to find the `LazyColumn` and fling it:
    
    
    @Test
    fun scrollList() {
        benchmarkRule.measureRepeated(
            packageName = "com.example.myapp",
            metrics = listOf(FrameTimingMetric()),
            iterations = 5,
            setupBlock = {
                uiAutomator {
                    pressHome()
                    startApp("com.example.myapp")
                }
            }
        ) {
            uiAutomator {
                // Find the Composable using its testTag mapped as a viewIdResourceName
                val lazyColumn = onElement { viewIdResourceName == "my_lazy_column" }
    
                // Fling the Compose list down
                repeat(3) {
                    lazyColumn.fling(Direction.DOWN)
                }
            }
        }
    }
    

Your benchmark doesn't have to scroll the UI. Instead, it can run an animation, for example. It also doesn't need to use UI Automator specifically. It collects performance metrics as long as frames are being produced.

**Note:** When accessing UI objects, specify the `packageName`, because the tests run in a separate process.

## Navigate to deep composable destinations

Sometimes you might want to benchmark a specific screen that isn't immediately visible when the app starts, like a details screen or a checkout page deep within your Jetpack Navigation graph.

Because Macrobenchmark runs out-of-process, you can't interact directly with your `NavController` to swap screens. Instead, your benchmark must simulate a user navigating to that part of the app.

Use the `setupBlock` to handle the preparation steps, like clicking through an onboarding flow or a menu button. This way, your `measureBlock` captures the performance metrics of only the target screen.
    
    
    @Test
    fun deepScreenScrollList() {
        benchmarkRule.measureRepeated(
            packageName = "com.example.myapp",
            metrics = listOf(FrameTimingMetric()),
            iterations = 5,
            setupBlock = {
                uiAutomator {
                    // 1. Start the app on the home screen
                    startApp("com.example.myapp")
    
                    // 2. Navigate to the internal screen by clicking a Compose component
                    // (e.g., a card that opens the target list view)
                    val settingsButton = onElement { viewIdResourceName == "go_to_list_button" }
                    settingsButton.click()
    
                    // 3. Wait until the target screen settles and is fully rendered
                    waitForStableInActiveWindow()
                }
            }
        ) {
            uiAutomator {
                // The actual benchmark measurement starts here on the target screen
                val lazyColumn = onElement { viewIdResourceName == "my_lazy_column" }
                lazyColumn.fling(Direction.DOWN)
            }
        }
    }
    

## Additional resources

For more information about testing, see the following resources.

### Documentation

  * [Test your Compose layout](https://developer.android.com/develop/ui/compose/testing)
  * [Interoperability with UiAutomator](https://developer.android.com/develop/ui/compose/testing/interoperability#uiautomator-interop)



### Views content

  * [Control your app from Macrobenchmark (Views)](https://developer.android.com/topic/performance/views/benchmarking/macrobenchmark-control-app-views)



## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Writing a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
  * [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
  * [Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview)



[ Previous arrow_back  Capture the metrics  ](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)

[ Next Adding instrumentation arguments  arrow_forward  ](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
