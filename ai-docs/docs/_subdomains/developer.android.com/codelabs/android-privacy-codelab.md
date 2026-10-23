---
url: https://developer.android.com/codelabs/android-privacy-codelab/
title: Android Privacy Codelab \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:43:31.849186+00:00
---

# Android Privacy Codelab  |  Android Developers

> Source: https://developer.android.com/codelabs/android-privacy-codelab/




#  Android Privacy Codelab Stay organized with collections  Save and categorize content based on your preferences. 

##  1\. Intro 

## What you'll learn

  * Why privacy is becoming increasingly important for users.
  * Android privacy best-practices over the past few releases.
  * How to integrate privacy best-practices into existing apps to make them more privacy-preserving.



## What you'll build

In this codelab, you start with a sample app that allows users to save their photo memories.

It will start with the following screens:

  * Permission Screen - screen that asks the user to grant all the permissions before proceeding to the home screen.
  * Home Screen - screen that displays all the user's existing photo logs, and also allows them to add new photo logs.
  * Add Log Screen - screen that allows the user to create a new photo log. Here, users can browse from existing photos in their library, take a new photo using the camera, and add their current city to the photo log.
  * Camera Screen - screen that allows the user to take a photo and save it to the photo log.



The app is working, but it has many privacy deficiencies that we will improve upon together!

As you progress through the codelab, you will be:

  * ...shown why privacy is important for your apps
  * ...introduced to Android's privacy features and key best practices.
  * ...shown how to implement these best practices in an existing app, by doing the following:
  * Requesting permissions in-context
  * Reducing your app's location access
  * Using the photo picker & other storage improvements
  * Using the data access audit APIs



When you're done, you will have an app that:

  * ...implements the privacy best practices listed above.
  * ...is privacy preserving and protects users by handling their private data with care, which enhances the user experience.



## What you'll need

  * [The latest stable version of Android Studio](https://developer.android.com/studio/index.html).



Nice to have

  * Familiarity with the following Architecture Components: [ViewModel](https://developer.android.com/reference/androidx/lifecycle/ViewModel) and the architecture suggested in the [Guide to App Architecture](https://developer.android.com/topic/libraries/architecture/guide.html).
  * Familiarity with [Jetpack Compose](https://developer.android.com/jetpack/compose). For an introduction to Compose, check out the [Jetpack Compose Tutorial](https://developer.android.com/jetpack/compose/tutorial?continue=https%3A%2F%2Fdeveloper.android.com%2Fcourses%2Fpathways%2Fcompose%23article-https%3A%2F%2Fdeveloper.android.com%2Fjetpack%2Fcompose%2Ftutorial).



##  2\. Why is Privacy Important? 

Research shows that people are wary about their privacy. A [survey conducted by the Pew Research Institute](https://www.pewresearch.org/fact-tank/2020/04/14/half-of-americans-have-decided-not-to-use-a-product-or-service-because-of-privacy-concerns/) found that 84% of Americans feel that they have little to no control over the data collected by them by companies and apps. Their main point of frustration is not knowing what is happening to their data beyond the direct use. For example, they worry that the data is used for other purposes, such as to create profiles for targeted advertisement, or even sold to other parties. And once the data is out there, there seems to be no way of removing it.

This concern for privacy is already significantly impacting peoples' decisions about which services or apps to use. In fact, that same Pew Research Institute study found that over half (52%) of US adults decided not to use a product or service because of privacy concerns, such as being worried about how much data is being collected about them.

Therefore, enhancing and demonstrating your app's privacy is essential to improving the experience of your apps for your users, and research shows that it likely can help you grow your user base as well.

Many of the features and best practices that we will cover in this codelab are directly related to reducing the amount of data that your app accesses or enhancing your users' sense of control over their private data. Both of these enhancements directly address the concerns that users shared in the research we saw earlier.

##  3\. Set up Your Environment 

To get you started as quickly as possible, we have prepared a starter project for you to build on. In this step, you will download the code for the entire codelab, including the starter project, and then run the starter app on your emulator or device.

If you have git installed, you can simply run the command below. To check whether git is installed, type `git –version` the terminal or command line and verify that it executes correctly.

`git clone https://github.com/android/privacy-codelab`

If you do not have git, you can click the [link to download](https://github.com/android/privacy-codelab/archive/main.zip) all the code for this codelab.

To setup the codelab:

  1. Open the project in the `PhotoLog_Start` directory in Android Studio.
  2. Run the `PhotoLog_Start` run configuration on a device or emulator running Android 12 (S) or later.



![d98ce953b749b2be.png](https://developer.android.com/static/codelabs/android-privacy-codelab/img/d98ce953b749b2be.png)

You should see a screen asking you to grant permissions to run the app! This means you have successfully set up the environment.

##  4\. Best Practice: Request Permissions In-Context 

Many of you know that runtime permissions are essential to unlocking many key functionalities that are important to having a great user experience, but did you know that when and how your app requests the permissions also has a significant impact on user experience?

Let's take a look at how the `PhotoLog_Start` app requests permissions, to show you why it doesn't have an optimal permissions model:

  1. Right after launch, the user immediately receives permission prompts asking them to grant multiple permissions. This likely confuses users and may cause them to lose trust in our app or uninstall it in the worst case!
  2. The app doesn't let users proceed until all permissions are granted. Users may not trust our app enough on launch to grant access to all of this sensitive information.



As you probably guessed, the list above represents the set of improvements we will make together to improve the app's permission request process! Let's jump into it.

We can see that Android's [best practice recommendations](https://developer.android.com/training/permissions/requesting#principles) say that we should request permissions in-context the first time the users start interacting with a feature. This is because if an app requests permission to enable a feature that the user is already interacting with, the request doesn't come as a surprise for users. This results in a better user experience. In the PhotoLog app, we should wait until the first time users click on the camera or location buttons before we request permissions.

First, let's remove the permissions screen that forces users to approve all permissions before going to the home page. This logic is currently defined in `MainActivity.kt`, so let's navigate there:
    
    
    val startNavigation =
       if (permissionManager.hasAllPermissions) {
           Screens.Home.route
       } else {
           Screens.Permissions.route
       }
    

It checks if the user has granted all of the permissions before allowing them to move to the home page. As mentioned before, that is not following our best practices for user experience. Let's change it to the following code, enabling users to interact with our app without having all permissions granted:
    
    
    val startNavigation = Screens.Home.route
    

Now that we no longer need the permissions screen anymore, we can also delete this line from NavHost:
    
    
    composable(Screens.Permissions.route) { PermissionScreen(navController) }
    

Next, remove this line from the Screens class:
    
    
    object Permissions : Screens("permissions")
    

Finally, we can delete the PermissionsScreen.kt file as well.

Now, delete and re-install your app, which is one way to reset the previously-granted permissions! You should be able to go to the home screen immediately now, but when you press the camera or location buttons in the "Add Log" screen, nothing happens because the app no longer has the logic to request permissions from the user. Let's fix that.

## Add Logic to Request Camera Permission

We will begin with the camera permission. Based on the code samples we see in the [requesting permissions documentation](https://developer.android.com/training/permissions/requesting), we'll want to register the permissions callback first in order to use the `RequestPermission()` contract.

Let's evaluate the logic we need:

  * If the user accepts the permission, we'll want to register the permission with the viewModel, and also navigate to the camera screen if the user hasn't yet reached the limit for the number of photos already added.
  * If the user denies the permission, we can inform them that the feature is not working since the permission has been denied.



To execute this logic, we can add this code block to: _`// TODO: Step 1. Register ActivityResult to request Camera permission`_
    
    
    val requestCameraPermission =
       rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted ->
           if (isGranted) {
               viewModel.onPermissionChange(CAMERA, isGranted)
               canAddPhoto {
                   navController.navigate(Screens.Camera.route)
               }
           }
           else {
               coroutineScope.launch {
                   snackbarHostState.showSnackbar("Camera currently disabled due to denied permission.")
               }
           }
       }
    

Now we want to verify that the app has the camera permission before navigating to the camera screen, and to request the permission if the user hasn't granted it yet. To implement this logic, we can add the following code block to: _`// TODO: Step 2. Check& request for Camera permission before navigating to the camera screen`_
    
    
    canAddPhoto {
       when {
           state.hasCameraAccess -> navController.navigate(Screens.Camera.route)
           // TODO: Step 4. Trigger rationale screen for Camera if needed
           else -> requestCameraPermission.launch(CAMERA)
       }
    }
    

Now, try running the app again and click on the camera icon in the "Add Log" screen. You should see a dialog that requests the camera permission. Congratulations! This is much better than asking users to approve all the permissions before they've even tried out the app, right?

But can we do better? Yes! We can check if the system recommends that we show a rationale to explain why our app needs access to the camera. This helps to potentially increase opt-in rates for the permission and also preserve your apps' ability to request the permission again at a more opportune time.

To do that, let's build a rationale screen that explains why our app needs access to the user's camera. Do this by adding the following code block to: _`// TODO: Step 3. Add explanation dialog for Camera permission`_
    
    
    var showExplanationDialogForCameraPermission by remember { mutableStateOf(false) }
    if (showExplanationDialogForCameraPermission) {
       CameraExplanationDialog(
           onConfirm = {
               requestCameraPermission.launch(CAMERA)
               showExplanationDialogForCameraPermission = false
           },
           onDismiss = { showExplanationDialogForCameraPermission = false },
       )
    }
    

Now that we have the dialog itself, we just have to check whether we should show the rationale before requesting the camera permission. We do this by calling ActivityCompat's `shouldShowRequestPermissionRationale()` API. If it returns true, we just have to set `showExplanationDialogForCameraPermission` to true as well to display the explanation dialog.

Let's add the following code block between the `state.hasCameraAccess` case and the `else` case, or where the following TODO was previously added in the instructions : _`// TODO: Step 4. Add explanation dialog for Camera permission`_
    
    
    ActivityCompat.shouldShowRequestPermissionRationale(context.getActivity(),
               CAMERA) -> showExplanationDialogForCameraPermission = true
    

Your complete logic for the camera button should now look like this:
    
    
    canAddPhoto {
       when {
           state.hasCameraAccess -> navController.navigate(Screens.Camera.route)
           ActivityCompat.shouldShowRequestPermissionRationale(context.getActivity(),
               CAMERA) -> showExplanationDialogForCameraPermission = true
           else -> requestCameraPermission.launch(CAMERA)
       }
    }
    

Congrats! We've finished handling the camera permission while following all of Android's best practices! Go ahead, delete & re-install the app once again, and try pressing the camera button from the "Add Log" page. If you deny the permission, the app doesn't block you from using the other functionalities like opening the photo album.

However, the next time you click on the camera icon after denying the permission, you should see the explanation prompt that we just added!* Notice that the system permission prompt only shows up after the user clicks "continue" on the explanation prompt, and if the user clicks "not now," we let them use the app without any further interruptions. This helps the app avoid additional permission denials from the user and preserves our ability to request the permission again at a different time, when the user may be more ready to grant it.

  * note: the exact behavior of `shouldShowRequestPermissionRationale()` API is an internal implementation detail and is subject to change.



## Add Logic to Request Location Permission

Now, let's do the same for location. We can first register the ActivityResult for the location permissions by adding the following code block to: _`// TODO: Step 5. Register ActivityResult to request Location permissions`_
    
    
    val requestLocationPermissions =
       rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted ->
           if (isGranted) {
               viewModel.onPermissionChange(ACCESS_COARSE_LOCATION, isGranted)
               viewModel.onPermissionChange(ACCESS_FINE_LOCATION, isGranted)
               viewModel.fetchLocation()
           }
           else {
               coroutineScope.launch {
                   snackbarHostState.showSnackbar("Location currently disabled due to denied permission.")
               }
           }
       }
    

After that, we can go ahead and add the explanation dialog for location permissions by adding the following code block to: _`// TODO: Step 6. Add explanation dialog for Location permissions`_
    
    
    var showExplanationDialogForLocationPermission by remember { mutableStateOf(false) }
    if (showExplanationDialogForLocationPermission) {
       LocationExplanationDialog(
           onConfirm = {
               // TODO: Step 10. Change location request to only request COARSE location.
               requestLocationPermissions.launch(arrayOf(ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION))
               showExplanationDialogForLocationPermission = false
           },
           onDismiss = { showExplanationDialogForLocationPermission = false },
       )
    }
    

Next, let's go ahead and check, explain (if necessary), and request the location permissions. If the permission is granted, we can fetch the location and populate the photo log. Let's go ahead and add the following code block to: _`// TODO: Step 7. Check, request, and explain Location permissions`_
    
    
    when {
       state.hasLocationAccess -> viewModel.fetchLocation()
       ActivityCompat.shouldShowRequestPermissionRationale(context.getActivity(),
           ACCESS_COARSE_LOCATION) ||    
       ActivityCompat.shouldShowRequestPermissionRationale(
           context.getActivity(), ACCESS_FINE_LOCATION) ->
           showExplanationDialogForLocationPermission = true
       else -> requestLocationPermissions.launch(arrayOf(ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION))
    }
    

And there you have it, we are done with the permissions section of this codelab! Go ahead and try resetting your app and see the results.

Summary of how we've improved the user experience and the benefits for your app:

  * Request permissions in-context (when users are interacting with the feature) instead of immediately after app launch → Reduce confusion and user dropout.
  * Create explanation screens to explain to users why our app needs access to permissions → Increase transparency for users.
  * Leverage the shouldShowRequestPermissionRationale() API to determine when the system believes your app should show an explanation screen → Increase permission acceptance rates & decreases odds of permanent permission denial.



##  5\. Best Practice: Reduce Your App's Location Access 

Location is one of the most sensitive permissions, and that's why Android features it in the [Privacy Dashboard](https://developer.android.com/training/permissions/explaining-access#privacy-dashboard).

As a quick recap, in Android 12 we've provided users with additional controls for location. Users now have a clear choice to share less accurate location data to apps by selecting **approximate location** instead of **precise location** when apps request location access.

Approximate location provides the app with an estimate of the user's location within 3 square kilometers, which should be enough precision for many of your app's features. We encourage all developers whose apps need location access to review your use case, and only request `ACCESS_FINE_LOCATION` if the user is actively engaging with a feature that requires their precise location.

![ea5cc51fce3f219e.png](https://developer.android.com/static/codelabs/android-privacy-codelab/img/ea5cc51fce3f219e.png)

Graphic to visualize coarse location estimate range centered in downtown Los Angeles, California.

Approximate location access is definitely enough for our PhotoLog app, as we only need the user's city to remind them where the "memory" is from. However, the app is currently requesting both `ACCESS_COARSE_LOCATION` and `ACCESS_FINE_LOCATION` from the user. Let's change that.

First, we'll need to edit the activity result for location and provide the `ActivityResultContracts.RequestPermission()` function as a parameter instead of `ActivityResultContracts.RequestMultiplePermissions()`, to reflect the fact that we are only going to request `ACCESS_COARSE_LOCATION`.

Let's replace the current requestLocationsPermissions object (denoted by _`// TODO: Step 8. Change activity result to only request Coarse Location`_) with the following code block instead:
    
    
    val requestLocationPermissions =
       rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { isGranted ->
           if (isGranted) {
               viewModel.onPermissionChange(ACCESS_COARSE_LOCATION, isGranted)
           }
       }
    

Next, we will change the `launch()` methods to only request `ACCESS_COARSE_LOCATION` instead of both location permissions.

Let's replace:
    
    
    requestLocationPermissions.launch(arrayOf(ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION))
    

...with:
    
    
    requestLocationPermissions.launch(ACCESS_COARSE_LOCATION)
    

There are two instances of the `launch()` methods in PhotoLog we'll need to change, one is in the `onConfirm()` logic in the `LocationExplanationDialog` denoted by _`// TODO: Step 9. Change location request to only request COARSE location`_ , and one in the "Location" list item denoted by _`// TODO: Step 10. Change location request to only request COARSE location`_

Lastly, now that we are no longer requesting the `ACCESS_FINE_LOCATION` permission for PhotoLog, let's go ahead and remove this section from the onPermissionChange() method in AddLogViewModel.kt:
    
    
    Manifest.permission.ACCESS_FINE_LOCATION -> {
       uiState = uiState.copy(hasLocationAccess = isGranted)
    }
    

And don't forget to also remove the `ACCESS_FINE_LOCATION` from the app's Manifest:
    
    
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    

Now we are done with the location section of the codelab! Go ahead and uninstall/re-install your app and see the results!

##  6\. Best Practice: Minimize Use of Storage Permissions 

It's common for apps to work with photos stored on a device. To let users pick the desired images and videos, these apps often implement their own file pickers, which requires the apps to request permission for broad storage access. Users don't like to grant access to all their pictures, and developers don't like to maintain an independent file picker.

Android 13 introduces the photo picker: a tool to provide a way for the user to select media files without needing to grant an app with access to the user's entire media library. It's also backported to Android 11 & 12 with the help of [Google Play System Updates](https://support.google.com/product-documentation/answer/11412553).

For the feature in our PhotoLog app, we will use the [`PickMultipleVisualMedia`](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.PickMultipleVisualMedia) ActivityResultContract. It will use the Android Photo Picker when present on the device and relies on the [`ACTION_OPEN_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#action_open_document) intent on older devices.

First, let's register our ActivityResultContract in the `AddLogScreen` file. To do this, add the following code block after this line: _`// TODO: Step 11. Register ActivityResult to launch the Photo Picker`_
    
    
    val pickImage = rememberLauncherForActivityResult(
       PickMultipleVisualMedia(MAX_LOG_PHOTOS_LIMIT),
        viewModel::onPhotoPickerSelect
    )
    

Note: `MAX_LOG_PHOTOS_LIMIT` here represents the max limit of photos we chose to set when adding them to a log (in this case, it's 3).

Now we need to replace the internal picker that was in the app by the Android Photo Picker. Add the following code after the block: _`// TODO: Step 12. Replace the below line showing our internal UI by launching the Android Photo Picker instead`_
    
    
    pickImage.launch(PickVisualMediaRequest(PickVisualMedia.ImageOnly))
    

By adding these two lines of code, we now get a permissionless way to access the device's photos that provides a much nicer UX and doesn't require code maintenance!

Since PhotoLog no longer requires the legacy photo grid and storage permissions for accessing photos, we should now remove all the code containing our legacy photo grid, from the storage permission entry in the manifest to the logic behind it, as it's not needed anymore in our app.

##  7\. Recommended: Use Data Access Audit APIs in Debug Builds 

Do you have a big app with lots of features and collaborators (or you expect it to be in the future!) that makes it hard to track what kind of user data the app is accessing? Did you know that even if the data accesses come from APIs or SDKs that were used at one point but are now just lingering around in your app, your app will still be accountable for the data access?

We understand it's difficult to track all the places where your apps are accessing private data, including all the included SDKs and other dependencies. Therefore, to help you provide more transparency into how your app and its dependencies access private data from users, Android 11 introduces data access auditing. This API allows developers to perform specific actions—such as printing to a log file—each time one of the following events occurs:

  * Your app's code accesses private data.
  * Code in a dependent library or SDK accesses private data.



First, let's go over the basics of how the data access audit API works on Android. To adopt data access auditing, we'll register an instance of `AppOpsManager.OnOpNotedCallback` (requires targeting Android 11+).

We also need to override the three methods in the callback, which will be invoked by the system when the app accesses user data in different ways. These are:

  * `onNoted()` \- called when an app invokes **synchronous** (two-way binding) **APIs** that access user data. These are typically API calls that don't require a callback.
  * `onAsyncNoted()` \- called when an app invokes **asynchronous** (one-way binding) **APIs** that access user data. These are typically API calls that require callbacks, and the data access occurs when the callback is invoked.
  * `onSelfNoted()` \- _quite unlikely_ , happens when an app passes its own UID into [noteOp()](https://developer.android.com/reference/android/app/AppOpsManager#noteOp\(java.lang.String,%20int,%20java.lang.String,%20java.lang.String,%20java.lang.String\)) for example.



Now let's determine which of these methods applies for our PhotoLog app's data accesses. PhotoLog mainly accesses user data in two places, once when we activate the camera and another time when we access the user's location. These are both asynchronous API calls since both of them are relatively resource-intensive, and so we will expect the system to invoke `onAsyncNoted()` when we access the respective user data.

Let's walk through how to adopt the data access audit APIs for PhotoLog!

First, we will need to create an instance of ​​`AppOpsManager.OnOpNotedCallback()`, and override the three methods above.

For all three methods in the object, let's go ahead and log the particular operation that accessed private user data. This operation will contain more information on what kind of user data was accessed. In addition, since we expect `onAsyncNoted()` to get called when our app accesses camera and location info, let's do something special and log a map emoji for location access and a camera emoji for camera access. To do this, we can add the following code block to: _`// TODO: Step 1. Create Data Access Audit Listener Object`_
    
    
    @RequiresApi(Build.VERSION_CODES.R)
    object DataAccessAuditListener : AppOpsManager.OnOpNotedCallback() {
       // For the purposes of this codelab, we are just logging to console,
       // but you can also integrate other logging and reporting systems here to track
       // your app's private data access.
       override fun onNoted(op: SyncNotedAppOp) {
           Log.d("DataAccessAuditListener","Sync Private Data Accessed: ${op.op}")
       }
    
       override fun onSelfNoted(op: SyncNotedAppOp) {
           Log.d("DataAccessAuditListener","Self Private Data accessed: ${op.op}")
       }
    
       override fun onAsyncNoted(asyncNotedAppOp: AsyncNotedAppOp) {
           var emoji = when (asyncNotedAppOp.op) {
               OPSTR_COARSE_LOCATION -> "\uD83D\uDDFA"
               OPSTR_CAMERA -> "\uD83D\uDCF8"
               else -> "?"
           }
    
           Log.d("DataAccessAuditListener", "Async Private Data ($emoji) Accessed: 
           ${asyncNotedAppOp.op}")
       }
    }
    

We will then need to implement the callback logic we just created. For best results, we'll want to do that as early as possible since the system will only start tracking data access _after_ we register the callback. To register the callback, we can add the following code block to: _`// TODO: Step 2. Register Data Access Audit Callback`_`.`
    
    
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
       val appOpsManager = getSystemService(AppOpsManager::class.java) as AppOpsManager
       appOpsManager.setOnOpNotedCallback(mainExecutor, DataAccessAuditListener)
    }
    

##  8\. Wrapping Up 

Let's do a recap of what we've covered! We...

  * ...explored why privacy is important for your apps.
  * ...were introduced to Android's privacy features.
  * ...implementing many key privacy best practices for apps, by:
  * Requesting permissions in-context
  * Reducing your app's location access
  * Using the photo picker & other storage improvements
  * Using the data access audit APIs
  * ...implemented these best practices in an existing app to enhance its privacy.



We hope you enjoyed our journey as we improved the privacy and user experience of PhotoLog, and learned many concepts along the way!

## To find our reference code (optional):

If you haven't already, you can take a look at the solution code for the codelab in the `PhotoLog_End` folder. If you've followed the instructions of this codelab closely, the code in the `PhotoLog_Start` folder should be identical to that in the `PhotoLog_End` folder.

## Learn more

That's it! To learn more about the best practices we covered above, check out the [Android Privacy Landing Page](https://developer.android.com/design-for-safety).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
