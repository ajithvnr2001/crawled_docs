---
url: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker/
title: Set up a worker for profile uploading \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:45.246854+00:00
---

# Set up a worker for profile uploading  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/tracing/profiling-manager/upload-worker/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Set up a worker for profile uploading Stay organized with collections  Save and categorize content based on your preferences. 

ProfilingManager saves traces locally on the device. While you can retrieve these files using ADB for local debugging, collecting field data requires uploading them to a server.

Trace files can be large (often several MBs). To avoid negatively affecting the user experience or consuming mobile data, you should schedule uploads to occur in the background, preferably when the device is on an unmetered network (Wi-Fi), charging and idle.

## Set up a WorkManager upload job

`ProfilingManager` is cloud-agnostic; you can upload traces to any infrastructure you choose. The following example demonstrates how to use [`WorkManager`](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started) to schedule an upload job that avoids user disruption.

## Code example to setup an upload job

Here's an example on how you can set up a job that is not disruptive to the user to upload traces to your server.

### Add WorkManager dependencies

Besides your existing `ProfilingManager` dependencies, add these Jetpack libraries to your `build.gradle.kts` file. `WorkManager` needs them.

### Kotlin
    
    
       dependencies {
           implementation("androidx.work:work-runtime:2.12.0")
       }
       

### Groovy
    
    
       dependencies {
           implementation 'androidx.work:work-runtime:2.12.0'
       }
       

### Code snippet

This code shows how to set up a job for uploading traces. The job should be setup when the `ProfilingResult` is received by your app. The profiling section is omitted in this section but an example can be found in [Record a system trace](https://developer.android.com/topic/performance/tracing/profiling-manager/how-to-capture#record-system-trace).

**Note:** The actual upload logic is not included. `ProfilingManager` works with any cloud platform. Use this setup as a starting point, then add the specific upload details for your app's cloud service.

### Kotlin
    
    
    class TraceUploadWorker(context: Context, workerParams: WorkerParameters) : Worker(context, workerParams) {
        override fun doWork(): Result {
            // Perform your uploading work here
            Log.d("ProfileTest", "Uploading trace: " + inputData.getString("PROFILE_PATH"))
    
            return Result.success()
        }
    }
    
    fun setupProfileUploadWorker(profileFilepath: String?) {
        val workMgr = WorkManager.getInstance(applicationContext)
        val workRequestBuilder = OneTimeWorkRequest.Builder(TraceUploadWorker::class)
    
        val constraints = Constraints.Builder()
            .setRequiredNetworkType(NetworkType.UNMETERED)
            .setRequiresDeviceIdle(true)
            .setRequiresCharging(true)
            .build()
        workRequestBuilder.setConstraints(constraints)
    
        val inputDataBuilder = Data.Builder()
        inputDataBuilder.putString("PROFILE_PATH", profileFilepath)
        workRequestBuilder.setInputData(inputDataBuilder.build())
    
        workMgr.enqueue(workRequestBuilder.build())
    }
    
    [ProfilingManagerKotlinSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/misc/src/main/java/com/example/snippets/profiling/ProfilingManagerKotlinSnippets.kt#L143-L168)

### Java
    
    
    public static class TraceUploadWorker extends Worker {
    
      public TraceUploadWorker(
          @androidx.annotation.NonNull Context context,
          @androidx.annotation.NonNull WorkerParameters workerParams) {
        super(context, workerParams);
      }
    
      @androidx.annotation.NonNull
      @Override
      public Result doWork() {
        // Perform your uploading work here
        Log.d("ProfileTest", "Uploading trace: " + getInputData().getString("PROFILE_PATH"));
    
        return Result.success();
      }
    }
    
    public void setupProfileUploadWorker(String profileFilepath) {
      WorkManager workMgr = WorkManager.getInstance(getApplicationContext());
      OneTimeWorkRequest.Builder workRequestBuilder = new OneTimeWorkRequest.Builder(
          TraceUploadWorker.class);
    
      Constraints constraints = new Constraints.Builder()
          .setRequiredNetworkType(NetworkType.UNMETERED)
          .setRequiresDeviceIdle(true)
          .build();
      workRequestBuilder.setConstraints(constraints);
    
      Data.Builder inputDataBuilder = new Data.Builder();
      inputDataBuilder.putString("PROFILE_PATH", profileFilepath);
      workRequestBuilder.setInputData(inputDataBuilder.build());
    
      workMgr.enqueue(workRequestBuilder.build());
    }
    
    [ProfilingManagerJavaSnippets.java](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/misc/src/main/java/com/example/snippets/profiling/ProfilingManagerJavaSnippets.java#L224-L258)

### Code walkthrough

The code does the following:

  * **Define the worker** : Create a `TraceUploadWorker` class extending `Worker`. Implement the `doWork()` method to handle the actual file upload logic using your preferred backend SDK or HTTP client.

  * **Request profiling** : Use `SystemTraceRequestBuilder` to configure the trace (duration, buffer policy) and `Profiling.requestProfiling` to start it.

  * **Schedule the work** :

    * Create a `OneTimeWorkRequest` for your worker.

    * Set constraints: Use `setRequiredNetworkType(NetworkType.UNMETERED)`, `setRequiresDeviceIdle(true)` and `setRequiresCharging(true)` to ensure the upload only happens when the user is on Wi-Fi, charging and not actively using the device. This is important to avoid disruption to the user with the upload job.

    * Pass data: Use `setInputData` to pass the trace path to the worker.

    * Enqueue: Submit the request to WorkManager by calling `WorkManager#enqueue`.




## Next Steps

After uploading traces, you can analyze them individually or perform [bulk trace analysis](https://developer.android.com/topic/performance/tracing/profiling-manager/bulk-trace-analysis). For guidance on setting up a scalable analysis pipeline, refer to [Deploying Bigtrace on Kubernetes](https://perfetto.dev/docs/deployment/deploying-bigtrace-on-kubernetes).

**Note:** You can delete profile files from the device after uploading them if they are no longer needed, as `ProfilingManager` no longer manages these files.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
