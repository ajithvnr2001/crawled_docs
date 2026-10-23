---
url: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview/
title: Write a Macrobenchmark \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:49.318513+00:00
---

# Write a Macrobenchmark  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Write a Macrobenchmark Stay organized with collections  Save and categorize content based on your preferences. 

Use the Macrobenchmark library for testing larger use cases of your app, including app startup and complex UI manipulations, such as scrolling a [`LazyColumn`](https://developer.android.com/develop/ui/compose/lists) or running animations. If you want to test smaller areas of your code, see [Microbenchmark](https://developer.android.com/topic/performance/benchmarking/microbenchmark-overview). This page shows how to set up the Macrobenchmark library.

The library outputs benchmarking results to the Android Studio console and to a JSON file with more detail. It also provides trace files that you can load and analyze in Android Studio.

Use the Macrobenchmark library in a continuous integration (CI) environment, as described in [Benchmark in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci).

You can use Macrobenchmark to generate Baseline Profiles. First, set up the Macrobenchmark library, then you can [create a Baseline Profile](https://developer.android.com/topic/performance/baselineprofiles#creating-profile-rules).

Macrobenchmark is the recommended tool for testing UIs created with Jetpack Compose. To learn how to write UI Automator tests that interact with your Compose nodes, see [Interoperability](https://developer.android.com/develop/ui/compose/testing/interoperability).

## Project setup

We recommend you use Macrobenchmark with the latest version of Android Studio.

### Set up the Macrobenchmark module

Macrobenchmarks require a [`com.android.test`](https://developer.android.com/studio/test#use_separate_test_modules_for_instrumented_tests) module—separate from your app code—that is responsible for running the tests that measure your app.

In Android Studio, a template is available to simplify Macrobenchmark module setup. The benchmarking module template automatically creates a module in your project for measuring the app built by an app module, including a sample startup benchmark.

To use the module template to create a new module, do the following:

  1. Right-click your project or module in the **Project** panel in Android Studio, and select **New > Module**.

  2. Select **Benchmark** from the **Templates** pane. You can customize the target app—meaning the app to be benchmarked—as well as the package and module name for the new Macrobenchmark module.

  3. Click **Finish**.


![Benchmark Module template.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_module_bumblebee-R2.png)**Figure 1.** Benchmark module template.

### Set up the app

To benchmark an app—known as the _target_ of the Macrobenchmark—the app must be [`profileable`](https://developer.android.com/studio/profile#profileable-apps), which enables reading detailed trace information without affecting performance. The module wizard adds the [`<profileable>`](https://developer.android.com/guide/topics/manifest/profileable-element) tag automatically to the app's `AndroidManifest.xml` file.

Make sure that the target app includes [`ProfilerInstaller`](https://developer.android.com/jetpack/androidx/releases/profileinstaller) 1.3 or later, which the Macrobenchmark library needs to enable profile capture and reset and shader cache clearing.

Configure the benchmarked app as close to the release version or production as possible. Set it up as non-debuggable and preferably with minification on, which improves performance. You typically do this by creating a copy of the release variant, which performs the same but is signed locally with debug keys. Alternatively, you can use `initWith` to instruct Gradle to do it for you:

### Kotlin
    
    
    buildTypes {
        getByName("release") {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"))
        }
    
        create("benchmark") {
            initWith(getByName("release"))
            signingConfig = signingConfigs.getByName("debug")
        }
    }

### Groovy
    
    
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "keep-rules.pro"
            )
            // In real app, this would use its own release keystore
            signingConfig = signingConfigs.getByName("debug")
            baselineProfile.automaticGenerationDuringBuild = true
        }
    }
    
    [build.gradle.kts](https://github.com/android/performance-samples/blob/58c9ccb9e04706ee2a915604eee5720721601af9/MacrobenchmarkSample/app/build.gradle.kts#L43-L55)

To help ensure that running the benchmark both builds and tests the correct variant of your app, as shown in figure 2, do the following:

  1. Perform a Gradle sync.
  2. Open the **Build Variants** panel.
  3. Select the benchmark variant of both the app and the Macrobenchmark module.

![Select benchmark variant.](https://developer.android.com/static/topic/performance/images/benchmark_images/benchmark_variant-R2.png)**Figure 2.** Select the benchmark variant.**Note:** See the [sample Macrobenchmark module](https://github.com/android/performance-samples/tree/main/MacrobenchmarkSample/macrobenchmark) for reference on how to set up your project to be Macrobenchmark-ready.

### (Optional) Set up multi-module app

If your app has more than one Gradle module, make sure your build scripts know which build variant to compile. Add the `matchingFallbacks` property into the `benchmark` build type of your `:macrobenchmark` and `:app` modules. The rest of your Gradle modules can have the same configuration as before.

### Kotlin
    
    
    create("benchmark") {
        initWith(getByName("release"))
        signingConfig = signingConfigs.getByName("debug")
    
        **matchingFallbacks += listOf("release")
    ** }

### Groovy
    
    
    benchmark {
        initWith buildTypes.release
        signingConfig signingConfigs.debug
    
        **matchingFallbacks = ['release']
    ** }

Without this, the newly added `benchmark` build type causes the build to fail and provides the following error message:
    
    
    > Could not resolve project :shared.
         Required by:
             project :app
          > No matching variant of project :shared was found.
          ...
    

When selecting the build variants in your project, choose `benchmark` for the `:app` and `:macrobenchmark` modules and `release` for any other modules you have in your app, as shown in figure 3:

![Benchmark variants for multi-module project with release and benchmark build types selected.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_variants_multi_modules-R2.png)**Figure 3.** Benchmark variants for multi-module project with release and benchmark build types selected.

For more information, see [Resolve build errors related to variant matching](https://developer.android.com/studio/build/build-variants#resolve_matching_errors).

### (Optional) Set up product flavors

If you have multiple product flavors set in your app, configure the `:macrobenchmark` module so that it knows what product flavor of your app to build and benchmark.

The examples in this page use the two product flavors in the `:app` module, `demo` and `production`, as shown in the following snippet:

### Kotlin
    
    
    flavorDimensions += "environment"
    productFlavors {
        create("demo") {
            dimension = "environment"
            // ...
        }
        create("production") {
            dimension = "environment"
            // ...
        }
    }

### Groovy
    
    
    flavorDimensions 'environment'
    productFlavors {
        demo {
            dimension 'environment'
            // ...
        }
    
        production {
            dimension 'environment'
            // ...
        }
    }

Without this configuration, you might get a build error similar to the one caused by multiple Gradle modules:
    
    
    Could not determine the dependencies of task ':macrobenchmark:connectedBenchmarkAndroidTest'.
    > Could not determine the dependencies of null.
       > Could not resolve all task dependencies for configuration ':macrobenchmark:benchmarkTestedApks'.
          > Could not resolve project :app.
            Required by:
                project :macrobenchmark
             > The consumer was configured to find a runtime of a component, as well as attribute 'com.android.build.api.attributes.BuildTypeAttr' with value 'benchmark', attribute 'com.android.build.api.attributes.AgpVersionAttr' with value '7.3.0'. However we cannot choose between the following variants of project :app:
                 -   demoBenchmarkRuntimeElements
                 -   productionBenchmarkRuntimeElements
               All of them match the consumer attributes:
               ...
    

The two following sections describe ways to configure benchmarking with multiple product flavors.

#### Use missingDimensionStrategy

Specifying `missingDimensionStrategy` in the `defaultConfig` of the `:macrobenchmark` module tells the build system to fallback to the flavor dimension. Specify which dimensions to use if you don't find them in the module. In the following example, the `production` flavor is used as the default dimension:

### Kotlin
    
    
    defaultConfig {
        missingDimensionStrategy("environment", "production")
    }

### Groovy
    
    
    defaultConfig {
        missingDimensionStrategy "environment", "production"
    }

This way, the `:macrobenchmark` module is able to only build and benchmark the specified product flavor, which is helpful if you know that only one product flavor has the proper configuration to be benchmarked.

#### Define product flavors in the :macrobenchmark module

If you want to build and benchmark other product flavors, define them in the `:macrobenchmark` module. Specify it similarly as in the `:app` module, but only assign `productFlavors` to a `dimension`. No other settings are required:

### Kotlin
    
    
    flavorDimensions += "environment"
    productFlavors {
        create("demo") {
            dimension = "environment"
        }
        create("production") {
            dimension = "environment"
        }
    }

### Groovy
    
    
    flavorDimensions 'environment'
    productFlavors {
        demo {
            dimension 'environment'
        }
    
        production {
            dimension 'environment'
        }
    }

After defining and syncing the project, choose the relevant build variant from the **Build Variants** pane, as shown in figure 4:

![Benchmark variants for project with product flavors showing productionBenchmark and release selected.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_variants_product_flavors-R2.png)**Figure 4.** Benchmark variants for the project with product flavors showing "productionBenchmark" and "release" selected.

For more information, see [Resolve build errors related to variant matching](https://developer.android.com/studio/build/build-variants#resolve_matching_errors).

## Create a Macrobenchmark class

Benchmark testing is provided through the [`MacrobenchmarkRule`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule) JUnit4 rule API in the Macrobenchmark library. It contains a [`measureRepeated`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measureRepeated\(kotlin.String,kotlin.collections.List,androidx.benchmark.macro.CompilationMode,androidx.benchmark.macro.StartupMode,kotlin.Int,kotlin.Function1,kotlin.Function1\)) method that lets you specify various conditions on how to run and benchmark the target app.

You need to at least specify the `packageName` of the target app, what `metrics` you want to measure, and how many `iterations` the benchmark must run.

### Kotlin
    
    
    @LargeTest
    @RunWith(AndroidJUnit4::class)
    class SampleStartupBenchmark {
        @get:Rule
        val benchmarkRule = MacrobenchmarkRule()
    
        @Test
        fun startup() = benchmarkRule.measureRepeated(
            packageName = TARGET_PACKAGE,
            metrics = listOf(StartupTimingMetric()),
            iterations = DEFAULT_ITERATIONS,
        ) {
            // starts default launch activity
            uiAutomator { startApp(TARGET_PACKAGE) }
        }
    }
    
    [SampleStartupBenchmark.kt](https://github.com/android/performance-samples/blob/58c9ccb9e04706ee2a915604eee5720721601af9/MacrobenchmarkSample/macrobenchmark/src/main/kotlin/com/example/macrobenchmark/benchmark/startup/SampleStartupBenchmark.kt#L31-L46)

For all the options on customizing your benchmark, see the Customize the benchmarks section.

**Note:** If your `measureBlock` requires interacting with UI elements (such as scrolling a list to measure [`FrameTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/FrameTimingMetric)), use [UI Automator](https://developer.android.com/training/testing/other-components/ui-automator). You can enable [`testTagAsResourceId`](https://developer.android.com/develop/ui/compose/testing/interoperability) to interact with Compose modifiers.

## Benchmark Compose UI interactions

While the previous example measures app startup, you will often want to measure UI performance, such as frame drops ([jank](https://developer.android.com/studio/profile/jank-detection)) while scrolling.

To benchmark a Jetpack Compose application, such as to measure `FrameTimingMetric` while scrolling a `LazyColumn`, you can use UI Automator to interact directly with your Compose nodes, as shown in the following snippet.

**Tip:** To allow UI Automator to find your Compose elements, enable `testTagAsResourceId = true` on the semantics modifier of your top-level Compose element.
    
    
    @LargeTest
    @RunWith(AndroidJUnit4::class)
    class ComposeScrollBenchmark {
        @get:Rule
        val benchmarkRule = MacrobenchmarkRule()
    
        @Test
        fun scrollLazyColumn() = benchmarkRule.measureRepeated(
            packageName = "com.example.compose.app",
            metrics = listOf(FrameTimingMetric()),
            iterations = 5,
            startupMode = StartupMode.WARM,
            setupBlock = { pressHome() }
        ) {
            startActivityAndWait()
    
            // Find the Compose node using the testTag defined in your app
            val lazyColumn = device.findObject(By.res("my_lazy_column"))
    
            // Simulate a scroll gesture to measure FrameTimingMetric
            lazyColumn.setGestureMargin(device.displayWidth / 5)
            lazyColumn.fling(Direction.DOWN)
        }
    }
    

## Run the benchmark

**Note:** Use Android 14 (API level 34) or later to persist state when benchmarking. The Macrobenchmark library fully resets the compilation state for each compile, which on Android versions earlier than 14 requires reinstalling the APK. As a workaround, control app compilation separately and skip compilation using `CompilationMode.Ignore`.

Run the test from within Android Studio to measure the performance of your app on your device. You can run the benchmarks the same way you run any other `@Test` using the gutter action next to your test class or method, as shown in the figure 5.

![Run Macrobenchmark with gutter action next to test class.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_run-R2.png)**Figure 5.** Run Macrobenchmark with the gutter action next to the test class.

You can also run all benchmarks in a Gradle module from the command line by executing the `connectedCheck` command:
    
    
    ./gradlew :macrobenchmark:connectedCheck

You can run a single test by executing the following:
    
    
    ./gradlew :macrobenchmark:connectedCheck -P android.testInstrumentationRunnerArguments.class=com.example.macrobenchmark.startup.SampleStartupBenchmark#startup

**Note:** We discourage running the benchmarks on an emulator, as they don't produce performance numbers representative of the end-user experience.

See [Benchmark in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci) for information on how to run and monitor benchmarks in continuous integration.

### Benchmark results

After a successful benchmark run, metrics are displayed directly in Android Studio and are output for CI usage in a [JSON file](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci#benchmark-data-example). Each measured iteration captures a separate system trace. You can open these trace results by clicking the links in the **Test Results** pane, as shown in the figure 6:

![Macrobenchmark startup results.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_results_startup-R2.png)**Figure 6.** Macrobenchmark startup results.

When the trace is loaded, Android Studio prompts you to select the process to analyze. The selection is pre-populated with the target app process, as shown in figure 7:

![Studio trace process selection.](https://developer.android.com/static/topic/performance/images/benchmark_images/studio_process-R2.png)**Figure 7.** Studio trace process selection.

After the trace file is loaded, Studio shows the results in the [CPU profiler tool](https://developer.android.com/studio/profile/cpu-profiler#system-trace):

![Studio trace.](https://developer.android.com/static/topic/performance/images/benchmark_images/macrobenchmark_trace-R2.png)**Figure 8.** Studio trace.

JSON reports and any profiling traces are also automatically copied from the device to the host. These are written on the host machine in the following location:
    
    
    project_root/module/build/outputs/connected_android_test_additional_output/debugAndroidTest/connected/device_id/
    

### Access trace files manually

If you want to use the [Perfetto](https://ui.perfetto.dev/) tool to analyze a trace file, there are extra steps involved. Perfetto lets you inspect all processes happening across the device during the trace, while Android Studio's CPU profiler limits inspection to a single process.

If you invoke the tests from Android Studio or from the Gradle command line, the trace files are automatically copied from the device to the host. These are written on the host machine in the following location:
    
    
    project_root/module/build/outputs/connected_android_test_additional_output/debugAndroidTest/connected/device_id/TrivialStartupBenchmark_startup[mode=COLD]_iter002.perfetto-trace
    

When you have the trace file in your host system, you can open it in Android Studio with **File > Open** in the menu. This shows the profiler tool view shown in the previous section.

### Configuration errors

If the app is misconfigured—debuggable or non-profileable—Macrobenchmark returns an error rather than reporting an incorrect or incomplete measurement. You can suppress these errors with the [`androidx.benchmark.suppressErrors`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-instrumentation-args#suppresserrors) argument.

Macrobenchmark also returns errors when attempting to measure an emulator or on a low-battery device, which might compromise core availability and clock speed.

## Customize the benchmarks

The [`measureRepeated`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/junit4/MacrobenchmarkRule#measureRepeated\(kotlin.String,kotlin.collections.List,androidx.benchmark.macro.CompilationMode,androidx.benchmark.macro.StartupMode,kotlin.Int,kotlin.Function1,kotlin.Function1\)) function accepts various parameters that influence which metrics the library collects, how your app is started and compiled, or how many iterations the benchmark runs.

### Capture the metrics

Metrics are the main type of information extracted from your benchmarks. The following metrics are available:

  * [`StartupTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupTimingMetric)
  * [`FrameTimingMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/FrameTimingMetric)
  * [`TraceSectionMetric`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/TraceSectionMetric)



For more information about metrics, see [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics).

### Improve trace data with custom events

It can be useful to instrument your app with custom trace events, which are seen with the rest of the trace report and can help point out problems specific to your app. To learn more about creating custom trace events, see [Define custom events](https://developer.android.com/topic/performance/tracing/custom-events).

### CompilationMode

Macrobenchmarks can specify a [`CompilationMode`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode), which defines how much of the app must be pre-compiled from DEX bytecode (the bytecode format within an APK) to machine code (similar to pre-compiled C++).

By default, Macrobenchmarks are run with [`CompilationMode.DEFAULT`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode#DEFAULT\(\)), which installs a Baseline Profile—if available—on Android 7 (API level 24) and later. If you are using Android 6 (API level 23) or earlier, the compilation mode fully compiles the APK as default system behavior.

You can install a Baseline Profile if the target app contains both a Baseline Profile and the [`ProfileInstaller`](https://developer.android.com/jetpack/androidx/releases/profileinstaller) library.

On Android 7 and later, you can customize the `CompilationMode` to affect the amount of on-device pre-compilation to mimic different levels of ahead-of-time (AOT) compilation or JIT caching. See [`CompilationMode.Full`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode.Full), [`CompilationMode.Partial`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode.Partial), [`CompilationMode.None`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode.None), and [`CompilationMode.Ignore`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/CompilationMode.Ignore).

This feature is built on [ART compilation commands](https://source.android.com/devices/tech/dalvik/jit-compiler#force-compilation-of-a-specific-package). Each benchmark clears profile data before it starts, to help ensure non-interference between benchmarks.

### StartupMode

To perform an activity start, you can pass a predefined startup mode: [`COLD`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupMode#COLD), [`WARM`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupMode#WARM), or [`HOT`](https://developer.android.com/reference/kotlin/androidx/benchmark/macro/StartupMode#HOT). This parameter changes how the activity launches and the process state at the start of the test.

**Warning:** If `StartupMode.COLD` is used, the app process is killed between the execution of `setupBlock` and `measureBlock` to allow for app preparation without starting the process. If you need the process to remain active, use `StartupMode.WARM`, which restarts activities without restarting the process, or set `startupMode` to `null` and call `killProcess` within the `setupBlock`.

To learn more about the types of startup, see [App startup time](https://developer.android.com/topic/performance/issues/launch-time).

## Samples

A sample project is available in the [Macrobenchmark Sample](https://github.com/android/performance-samples/tree/main/MacrobenchmarkSample) of the repository on GitHub.

## Provide feedback

To report issues or submit feature requests for Jetpack Macrobenchmark, see the [public issue tracker](https://issuetracker.google.com/issues/new?component=975669&%3Btemplate=1519452&authuser=1).

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Capture Macrobenchmark metrics](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
  * [Create Baseline Profiles {:#creating-profile-rules}](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
  * [Automate measurement with the Macrobenchmark library {:#measuring-optimization}](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)



[ Next Capture the metrics  arrow_forward  ](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 

  * [ ![X](https://developer.android.com/_static/android/images/logo-x.svg) X  ](https://x.com/AndroidDev)

Follow @AndroidDev on X

  * [ ![YouTube](https://www.gstatic.com/images/icons/material/product/2x/youtube_48dp.png) YouTube  ](https://www.youtube.com/user/androiddevelopers)

Check out Android Developers on YouTube

  * [ ![LinkedIn](https://developer.android.com/_static/android/images/logo-linkedin.svg) LinkedIn  ](https://www.linkedin.com/showcase/androiddev)

Connect with the Android Developers community on LinkedIn




  * ### More Android

    * [ Android ](https://www.android.com)
    * [ Android for Enterprise ](https://www.android.com/enterprise/)
    * [ Security ](https://www.android.com/security-center/)
    * [ Source ](https://source.android.com)
    * [ News ](https://developer.android.com/news)
    * [ Blog ](https://android-developers.googleblog.com/)
    * [ Podcasts ](https://developer.android.com/podcasts)
  * ### Discover

    * [ Gaming ](https://developer.android.com/games)
    * [ Machine Learning ](https://developer.android.com/ml)
    * [ Health & Fitness ](https://developer.android.com/health-and-fitness)
    * [ Camera & Media ](https://developer.android.com/media)
    * [ Privacy ](https://developer.android.com/privacy)
    * [ 5G ](https://developer.android.com/training/connectivity/5g)
  * ### Android Devices

    * [ Large screens ](https://developer.android.com/large-screens)
    * [ Wear OS ](https://developer.android.com/wear)
    * [ ChromeOS devices ](https://developer.android.com/chrome-os)
    * [ Android for cars ](https://developer.android.com/cars)
    * [ Android TV ](https://developer.android.com/tv)
  * ### Releases

    * [ Android 17 ](https://developer.android.com/about/versions/17)
    * [ Android 16 ](https://developer.android.com/about/versions/16)
    * [ Android 15 ](https://developer.android.com/about/versions/15)
    * [ Android 14 ](https://developer.android.com/about/versions/14)
    * [ Android 13 ](https://developer.android.com/about/versions/13)
    * [ Android 12 ](https://developer.android.com/about/versions/12)
    * [ Android 11 ](https://developer.android.com/about/versions/11)
  * ### Documentation and Downloads

    * [ Android Studio guide ](https://developer.android.com/studio/intro)
    * [ Developers guides ](https://developer.android.com/guide)
    * [ API reference ](https://developer.android.com/reference)
    * [ Download Studio ](https://developer.android.com/studio)
    * [ Android NDK ](https://developer.android.com/ndk)
  * ### Support

    * [ Report platform bug ](https://issuetracker.google.com/issues/new?component=190923&template=841312)
    * [ Report documentation bug ](https://issuetracker.google.com/issues/new?component=192697)
    * [ Google Play support ](https://support.google.com/googleplay/android-developer)
    * [ Join research studies ](https://g.co/userresearch/androiddeveloperfooter)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/android/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com)
  * [ Chrome ](https://developer.chrome.com/home)
  * [ Firebase ](https://firebase.google.com)
  * [ Google Cloud Platform ](https://cloud.google.com)
  * [ All products ](https://developers.google.com/products/)



  * [ Privacy ](https://policies.google.com/privacy)
  * [ License ](https://developer.android.com/license)
  * [ Brand guidelines ](https://developer.android.com/distribute/marketing-tools/brand-guidelines)
  * Manage cookies 
  * Get news and tips by email [ Subscribe ](https://developer.android.com/updates)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * Türkçe
  * Русский
  * עברית
  * العربيّة
  * فارسی
  * हिंदी
  * বাংলা
  * ภาษาไทย
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


