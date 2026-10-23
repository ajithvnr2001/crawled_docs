---
url: https://developer.android.com/reference/android/content/pm/PackageManager/
title: PackageManager \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:30.041402+00:00
---

# PackageManager  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/android/content/pm/PackageManager/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

Summary: Nested Classes | Constants | Fields | Ctors | Methods | Inherited Methods

# PackageManager

* * *

[Kotlin](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager "View this page in Kotlin") |Java

` public abstract class PackageManager `   
` extends [Object](https://developer.android.com/reference/java/lang/Object) ` ` `

[java.lang.Object](https://developer.android.com/reference/java/lang/Object)  
---  
↳ | android.content.pm.PackageManager   
Known direct subclasses [MockPackageManager](https://developer.android.com/reference/android/test/mock/MockPackageManager) | [MockPackageManager](https://developer.android.com/reference/android/test/mock/MockPackageManager) |  _This class was deprecated in API level 24. Use a mocking framework like[Mockito](https://github.com/mockito/mockito). New tests should be written using the [Android Testing Support Library](https://developer.android.com/tools/testing-support-library)._  
---|---  
  
  


* * *

Class for retrieving various kinds of information related to the application packages that are currently installed on the device. You can find this class through `[Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager\(\))`. 

**Note:** If your app targets Android 11 (API level 30) or higher, the methods in this class each return a filtered list of apps. Learn more about how to [manage package visibility](https://developer.android.com/training/basics/intents/package-visibility). 

## Summary

### Nested classes  
  
---  
` class` |  `[PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags)` Specific flags used for retrieving application info.   
` class` |  `[PackageManager.ComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentEnabledSetting)` The class containing the enabled setting of a package component.   
` class` |  `[PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags)` Specific flags used for retrieving component info.   
` class` |  `[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` This exception is thrown when a given package, application, or component name cannot be found.   
` interface` |  `[PackageManager.OnChecksumsReadyListener](https://developer.android.com/reference/android/content/pm/PackageManager.OnChecksumsReadyListener)` Listener that gets notified when checksums are available.   
` class` |  `[PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags)` Specific flags used for retrieving package info.   
` class` |  `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` A property value set within the manifest.   
` class` |  `[PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags)` Specific flags used for retrieving resolve info.   
  
### Constants  
  
---  
`int` |  `[CERT_INPUT_RAW_X509](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_RAW_X509)` Certificate input bytes: the input bytes represent an encoded X.509 Certificate which could be generated using an `CertificateFactory`  
`int` |  `[CERT_INPUT_SHA256](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_SHA256)` Certificate input bytes: the input bytes represent the SHA256 output of an encoded X.509 Certificate.   
`int` |  `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)` Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application is in its default enabled state (as specified in its manifest).   
`int` |  `[COMPONENT_ENABLED_STATE_DISABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED)` Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application has been explicitly disabled, regardless of what it has specified in its manifest.   
`int` |  `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)` Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` only: This application should be considered, until the point where the user actually wants to use it.   
`int` |  `[COMPONENT_ENABLED_STATE_DISABLED_USER](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_USER)` Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` only: The user has explicitly disabled the application, regardless of what it has specified in its manifest.   
`int` |  `[COMPONENT_ENABLED_STATE_ENABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_ENABLED)` Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application has been explictily enabled, regardless of what it has specified in its manifest.   
`int` |  `[DELETE_ARCHIVE](https://developer.android.com/reference/android/content/pm/PackageManager#DELETE_ARCHIVE)` Flag parameter for `[PackageInstaller.uninstall(VersionedPackage,int,IntentSender)](https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall\(android.content.pm.VersionedPackage,%20int,%20android.content.IntentSender\))` to indicate that the deletion is an archival.   
`int` |  `[DONT_KILL_APP](https://developer.android.com/reference/android/content/pm/PackageManager#DONT_KILL_APP)` Flag parameter for `[setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))` to indicate that you don't want to kill the app containing the component.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[EXTRA_VERIFICATION_ID](https://developer.android.com/reference/android/content/pm/PackageManager#EXTRA_VERIFICATION_ID)` Extra field name for the ID of a package pending verification.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[EXTRA_VERIFICATION_RESULT](https://developer.android.com/reference/android/content/pm/PackageManager#EXTRA_VERIFICATION_RESULT)` Extra field name for the result of a verification, either `[VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)`, or `[VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports running activities on secondary displays.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_APP_WIDGETS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_APP_WIDGETS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports app widgets.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUDIO_LOW_LATENCY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUDIO_LOW_LATENCY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's audio pipeline is low-latency, more suitable for audio applications sensitive to delays or lag in sound input or output.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUDIO_OUTPUT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUDIO_OUTPUT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes at least one form of audio output, as defined in the Android Compatibility Definition Document (CDD) [section 7.8 Audio](https://source.android.com/compatibility/android-cdd#7_8_audio).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUDIO_PRO](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUDIO_PRO)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has professional audio level of functionality and performance.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))` which indicates whether head tracking for spatial audio operates with low-latency, as defined by the CDD criteria for the feature.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUTOFILL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUTOFILL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports autofill of user credentials, addresses, credit cards, etc via integration with `[autofill providers](https://developer.android.com/reference/android/service/autofill/AutofillService)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_AUTOMOTIVE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUTOMOTIVE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to showing UI on a vehicle headunit.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_BACKUP](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BACKUP)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can perform backup and restore operations on installed applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_BLUETOOTH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BLUETOOTH)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via Bluetooth.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_BLUETOOTH_LE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BLUETOOTH_LE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via Bluetooth Low Energy radio.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of ranging with other devices using channel sounding via Bluetooth Low Energy radio.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a camera facing away from the screen.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_ANY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_ANY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has at least one camera pointing in some direction, or can support an external or a `[virtual](https://developer.android.com/reference/android/companion/virtual/VirtualDevice)` camera being connected to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_AR](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AR)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[MOTION_TRACKING](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MOTION_TRACKING)` capability level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_AUTOFOCUS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AUTOFOCUS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's camera supports auto-focus.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[manual post-processing](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_POST_PROCESSING)` capability level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[manual sensor](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_SENSOR)` capability level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_CAPABILITY_RAW](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_RAW)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[RAW](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_RAW)` capability level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_CONCURRENT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CONCURRENT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's main front and back cameras can stream concurrently as described in `[CameraManager.getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds\(\))`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_EXTERNAL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_EXTERNAL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can support having an external camera connected to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_FLASH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_FLASH)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's camera supports flash.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_FRONT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_FRONT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a front facing camera.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CAMERA_LEVEL_FULL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_LEVEL_FULL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[full hardware](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL)` capability level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CANT_SAVE_STATE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CANT_SAVE_STATE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports the `[R.attr.cantSaveState](https://developer.android.com/reference/android/R.attr#cantSaveState)` API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_COMPANION_DEVICE_SETUP](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_COMPANION_DEVICE_SETUP)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports `[associating](https://developer.android.com/reference/android/companion/CompanionDeviceManager#associate\(android.companion.AssociationRequest,%20android.companion.CompanionDeviceManager.Callback,%20android.os.Handler\))` with devices via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CONNECTION_SERVICE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CONNECTION_SERVICE)` _This constant was deprecated in API level 33. use`[FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)` instead._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CONSUMER_IR](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CONSUMER_IR)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with consumer IR devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CONTROLS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CONTROLS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports a system interface for the user to select and bind device control services provided by applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_CREDENTIALS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CREDENTIALS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports retrieval of user credentials, via integration with credential providers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_DEVICE_ADMIN](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_DEVICE_ADMIN)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports device policy enforcement via device admins.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_DEVICE_ID_ATTESTATION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_DEVICE_ID_ATTESTATION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a KeyMint (or Keymaster) implementation that supports device ID attestation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_DEVICE_LOCK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_DEVICE_LOCK)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports locking (for example, by a financing provider in case of a missed payment).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_EMBEDDED](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_EMBEDDED)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device for IoT and may not have an UI.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_ETHERNET](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_ETHERNET)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This device supports ethernet.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_EXPANDED_PICTURE_IN_PICTURE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_EXPANDED_PICTURE_IN_PICTURE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports expanded picture-in-picture multi-window mode.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FACE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FACE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to perform face authentication.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FAKETOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events that supports distinct tracking of two or more fingers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events that supports tracking a hand of fingers (5 or more fingers) fully independently.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FINGERPRINT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FINGERPRINT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to detect a fingerprint.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_FREEFORM_WINDOW_MANAGEMENT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FREEFORM_WINDOW_MANAGEMENT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports freeform window management.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_GAMEPAD](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_GAMEPAD)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has all of the inputs necessary to be considered a compatible game controller, or includes a compatible game controller in the box.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_HARDWARE_KEYSTORE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_HARDWARE_KEYSTORE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device implements the Android Keystore backed by an isolated execution environment.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_HIFI_SENSORS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_HIFI_SENSORS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports high fidelity sensor processing capabilities.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_HOME_SCREEN](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_HOME_SCREEN)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports a home screen that is replaceable by third party applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_IDENTITY_CREDENTIAL_HARDWARE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device supports `[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)` implemented in secure hardware at the given feature version.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device supports `[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)` implemented in secure hardware with direct access at the given feature version.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_INPUT_METHODS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_INPUT_METHODS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports adding new input methods implemented with the `[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)` API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_IPSEC_TUNNELS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IPSEC_TUNNELS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has the requisite kernel support for multinetworking-capable IPsec tunnels.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_IPSEC_TUNNEL_MIGRATION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IPSEC_TUNNEL_MIGRATION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has the requisite kernel support for migrating IPsec tunnels to new source/destination addresses.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_IRIS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IRIS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to perform iris authentication.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_KEYSTORE_APP_ATTEST_KEY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_APP_ATTEST_KEY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can create application-specific attestation keys.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_KEYSTORE_LIMITED_USE_KEY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_LIMITED_USE_KEY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can enforce limited use key in hardware with any max usage count (including count equals to 1).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_KEYSTORE_SINGLE_USE_KEY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_SINGLE_USE_KEY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can only enforce limited use key in hardware with max usage count equals to 1.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LEANBACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports leanback UI.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LEANBACK_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK_ONLY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports only leanback UI.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LIVE_TV](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LIVE_TV)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports live TV and can display contents from TV inputs implemented with the `[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)` API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LIVE_WALLPAPER](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LIVE_WALLPAPER)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports live wallpapers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LOCATION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LOCATION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports one or more methods of reporting current location.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LOCATION_GPS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LOCATION_GPS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Global Positioning System receiver and can report precise location.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_LOCATION_NETWORK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LOCATION_NETWORK)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can report location with coarse accuracy using a network-based geolocation system.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_MANAGED_USERS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_MANAGED_USERS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports creating secondary users and managed profiles via `[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_MICROPHONE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_MICROPHONE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can record audio via a microphone.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_MIDI](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_MIDI)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a full implementation of the android.media.midi.* APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NEURAL_PROCESSING_UNIT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NEURAL_PROCESSING_UNIT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This device has a NPU (Neural Processing Unit) or similar hardware for accelerating AI workloads.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can communicate using Near-Field Communications (NFC), acting as a reader.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC_BEAM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_BEAM)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The Beam API is enabled on the device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC_HOST_CARD_EMULATION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports host- based NFC card emulation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC_HOST_CARD_EMULATION_NFCF](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION_NFCF)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports host- based NFC-F card emulation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports eSE- based NFC card emulation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports uicc- based NFC card emulation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_OPENGLES_DEQP_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_OPENGLES_DEQP_LEVEL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the feature version specifies a date such that the device is known to pass the OpenGLES dEQP test suite associated with that date.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_OPENGLES_EXTENSION_PACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_OPENGLES_EXTENSION_PACK)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports the OpenGL ES [ Android Extension Pack](http://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_PC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PC)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to be primarily used with keyboard, mouse or touchpad.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_PICTURE_IN_PICTURE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PICTURE_IN_PICTURE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports picture-in-picture multi-window mode.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_PRINTING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PRINTING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports printing.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_RAM_LOW](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_RAM_LOW)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's `[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice\(\))` method returns true.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_RAM_NORMAL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_RAM_NORMAL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's `[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice\(\))` method returns false.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SCREEN_LANDSCAPE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_LANDSCAPE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports landscape orientation screens.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SCREEN_PORTRAIT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_PORTRAIT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports portrait orientation screens.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SECURELY_REMOVES_USERS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SECURELY_REMOVES_USERS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports secure removal of users.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SECURE_LOCK_SCREEN](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SECURE_LOCK_SCREEN)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a secure implementation of keyguard, meaning the device supports PIN, pattern and password as defined in Android CDD   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SECURITY_MODEL_COMPATIBLE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SECURITY_MODEL_COMPATIBLE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is compatible with Android's security model.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_ACCELEROMETER](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an accelerometer.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a limited axes accelerometer.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an uncalibrated limited axes accelerometer.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_AMBIENT_TEMPERATURE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_AMBIENT_TEMPERATURE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an ambient temperature sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_BAROMETER](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_BAROMETER)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a barometer (air pressure sensor.)   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_COMPASS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_COMPASS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a magnetometer (compass).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports exposing head tracker sensors from peripheral devices via the dynamic sensors API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_GYROSCOPE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a gyroscope.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a limited axes gyroscope.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an uncalibrated limited axes gyroscope.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_HEADING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEADING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a heading sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_HEART_RATE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a heart rate monitor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_HEART_RATE_ECG](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE_ECG)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The heart rate sensor on this device is an Electrocardiogram.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_HINGE_ANGLE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HINGE_ANGLE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hinge angle sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_LIGHT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_LIGHT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a light sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_PROXIMITY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_PROXIMITY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a proximity sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_RELATIVE_HUMIDITY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_RELATIVE_HUMIDITY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a relative humidity sensor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_STEP_COUNTER](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_COUNTER)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hardware step counter.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SENSOR_STEP_DETECTOR](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_DETECTOR)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hardware step detector.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SE_OMAPI_ESE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_ESE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable eSE-based secure elements.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SE_OMAPI_SD](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_SD)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable SD-based secure elements.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SE_OMAPI_UICC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_UICC)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable UICC-based secure elements.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SIP](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SIP)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The SIP API is enabled on the device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_SIP_VOIP](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SIP_VOIP)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports SIP-based VOIP.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_STRONGBOX_KEYSTORE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_STRONGBOX_KEYSTORE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`, `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`, and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device implements the Android Keystore backed by a dedicated secure processor referred to as [ StrongBox](https://source.android.com/security/best-practices/hardware#strongbox-keymaster).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telecom Service APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a telephony radio with data communication support.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_CALLING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CALLING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for calling service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_CDMA](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CDMA)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a CDMA telephony stack.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_DATA)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for data service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_EUICC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports embedded subscriptions on eUICCs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_EUICC_MEP](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC_MEP)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports multiple enabled profiles on eUICCs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_GSM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_GSM)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a GSM telephony stack.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_IMS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_IMS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports attaching to IMS implementations using the ImsService API in telephony.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_MBMS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MBMS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports cell-broadcast reception using the MBMS APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_MESSAGING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MESSAGING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for SMS and MMS.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for the radio access.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for the subscription.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TELEVISION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEVISION)` _This constant was deprecated in API level 21. use`[FEATURE_LEANBACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)` instead._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_THREAD_NETWORK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_THREAD_NETWORK)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via [Thread](https://www.threadgroup.org) networking protocol.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TOUCHSCREEN](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's display has a touch screen.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TOUCHSCREEN_MULTITOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen supports multitouch sufficient for basic two-finger gesture detection.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen is capable of tracking two or more fingers fully independently.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen is capable of tracking a full hand of fingers fully independently -- that is, 5 or more simultaneous independent pointers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_USB_ACCESSORY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_USB_ACCESSORY)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports connecting to USB accessories.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_USB_HOST](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_USB_HOST)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports connecting to USB devices as the USB host.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_UWB](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_UWB)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via ultra wideband.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VERIFIED_BOOT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VERIFIED_BOOT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports verified boot.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VR_HEADTRACKING](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_HEADTRACKING)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device implements headtracking suitable for a VR device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VR_MODE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE)` _This constant was deprecated in API level 28. use`[FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)` instead._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device implements an optimized mode for virtual reality (VR) applications that handles stereoscopic rendering of notifications, disables most monocular system UI components while a VR application has user focus and meets extra CDD requirements to provide a high-quality VR experience.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VULKAN_DEQP_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_DEQP_LEVEL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the feature version specifies a date such that the device is known to pass the Vulkan dEQP test suite associated with that date.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VULKAN_HARDWARE_COMPUTE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_COMPUTE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the Vulkan native API will enumerate at least one `VkPhysicalDevice`, and the feature version will indicate what level of optional compute features that device supports beyond the Vulkan 1.0 requirements.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VULKAN_HARDWARE_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the Vulkan native API will enumerate at least one `VkPhysicalDevice`, and the feature version will indicate what level of optional hardware features limits it supports.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_VULKAN_HARDWARE_VERSION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_VERSION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the feature version will indicate the highest `VkPhysicalDeviceProperties::apiVersion` supported by the physical devices that support the hardware level indicated by `[FEATURE_VULKAN_HARDWARE_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports showing location-based suggestions for wallet cards provided by the default payment app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WATCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WATCH)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to showing UI on a watch.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WEBVIEW](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WEBVIEW)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a full implementation of the android.webkit.* APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WIFI](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WIFI)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports WiFi (802.11) networking.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WIFI_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WIFI_AWARE)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Aware.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WIFI_DIRECT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WIFI_DIRECT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Direct networking.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WIFI_PASSPOINT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WIFI_PASSPOINT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Passpoint and all Passpoint related APIs in `[WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager)` are supported.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WIFI_RTT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WIFI_RTT)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi RTT (IEEE 802.11mc).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FEATURE_WINDOW_MAGNIFICATION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WINDOW_MAGNIFICATION)` Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports window magnification.   
`int` |  `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)` Permission whitelist flag: permissions whitelisted by the installer.   
`int` |  `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)` Permission whitelist flag: permissions whitelisted by the system.   
`int` |  `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)` Permission whitelist flag: permissions whitelisted by the system when upgrading from an OS version where the permission was not restricted to an OS version where the permission is restricted.   
`int` |  `[GET_ACTIVITIES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ACTIVITIES)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about activities in the package in `[PackageInfo.activities](https://developer.android.com/reference/android/content/pm/PackageInfo#activities)`.   
`long` |  `[GET_APP_LOCK_INFO](https://developer.android.com/reference/android/content/pm/PackageManager#GET_APP_LOCK_INFO)` `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)`, `[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)`, and `[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` flag: return the `[ApplicationInfo.isAppLockSupported](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockSupported)` and `[ApplicationInfo.isAppLockEnabled](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockEnabled)` associated with an application.   
`int` |  `[GET_ATTRIBUTIONS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS)` _This constant was deprecated in API level 34. Use`[GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)` to avoid unintended sign extension. Operations with this flag may cause unintended results and potential `[RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException)`._  
`long` |  `[GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return all attributions declared in the package manifest   
`int` |  `[GET_CONFIGURATIONS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_CONFIGURATIONS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about hardware preferences in `[PackageInfo.configPreferences](https://developer.android.com/reference/android/content/pm/PackageInfo#configPreferences)`, and requested features in `[PackageInfo.reqFeatures](https://developer.android.com/reference/android/content/pm/PackageInfo#reqFeatures)` and `[PackageInfo.featureGroups](https://developer.android.com/reference/android/content/pm/PackageInfo#featureGroups)`.   
`int` |  `[GET_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_DISABLED_COMPONENTS)` _This constant was deprecated in API level 24. replaced with`[MATCH_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COMPONENTS)`_  
`int` |  `[GET_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_DISABLED_UNTIL_USED_COMPONENTS)` _This constant was deprecated in API level 24. replaced with`[MATCH_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTIL_USED_COMPONENTS)`._  
`int` |  `[GET_GIDS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_GIDS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return the `[group ids](https://developer.android.com/reference/android/content/pm/PackageInfo#gids)` that are associated with an application.   
`int` |  `[GET_INSTRUMENTATION](https://developer.android.com/reference/android/content/pm/PackageManager#GET_INSTRUMENTATION)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about instrumentation in the package in `[PackageInfo.instrumentation](https://developer.android.com/reference/android/content/pm/PackageInfo#instrumentation)`.   
`int` |  `[GET_INTENT_FILTERS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_INTENT_FILTERS)` _This constant was deprecated in API level 31. The platform does not support getting`[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)`s for the package._  
`int` |  `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)` `[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)` flag: return the `[ComponentInfo.metaData](https://developer.android.com/reference/android/content/pm/PackageItemInfo#metaData)` data `[Bundle](https://developer.android.com/reference/android/os/Bundle)`s that are associated with a component.   
`int` |  `[GET_PERMISSIONS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_PERMISSIONS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about permissions in the package in `[PackageInfo.permissions](https://developer.android.com/reference/android/content/pm/PackageInfo#permissions)`.   
`int` |  `[GET_PROVIDERS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_PROVIDERS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about content providers in the package in `[PackageInfo.providers](https://developer.android.com/reference/android/content/pm/PackageInfo#providers)`.   
`int` |  `[GET_RECEIVERS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_RECEIVERS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about intent receivers in the package in `[PackageInfo.receivers](https://developer.android.com/reference/android/content/pm/PackageInfo#receivers)`.   
`int` |  `[GET_RESOLVED_FILTER](https://developer.android.com/reference/android/content/pm/PackageManager#GET_RESOLVED_FILTER)` `[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` flag: return the IntentFilter that was matched for a particular ResolveInfo in `[ResolveInfo.filter](https://developer.android.com/reference/android/content/pm/ResolveInfo#filter)`.   
`int` |  `[GET_SERVICES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SERVICES)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about services in the package in `[PackageInfo.services](https://developer.android.com/reference/android/content/pm/PackageInfo#services)`.   
`int` |  `[GET_SHARED_LIBRARY_FILES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SHARED_LIBRARY_FILES)` `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` flag: return the `[paths to the shared libraries](https://developer.android.com/reference/android/content/pm/ApplicationInfo#sharedLibraryFiles)` that are associated with an application.   
`int` |  `[GET_SIGNATURES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SIGNATURES)` _This constant was deprecated in API level 28. use`GET_SIGNING_CERTIFICATES` instead_  
`int` |  `[GET_SIGNING_CERTIFICATES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SIGNING_CERTIFICATES)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return the signing certificates associated with this package.   
`int` |  `[GET_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_UNINSTALLED_PACKAGES)` _This constant was deprecated in API level 24. replaced with`[MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)`_  
`int` |  `[GET_URI_PERMISSION_PATTERNS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_URI_PERMISSION_PATTERNS)` `[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` flag: return the `[URI permission patterns](https://developer.android.com/reference/android/content/pm/ProviderInfo#uriPermissionPatterns)` that are associated with a content provider.   
`int` |  `[INSTALL_REASON_DEVICE_RESTORE](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_REASON_DEVICE_RESTORE)` Code indicating that this package was installed as part of restoring from another device.   
`int` |  `[INSTALL_REASON_DEVICE_SETUP](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_REASON_DEVICE_SETUP)` Code indicating that this package was installed as part of device setup.   
`int` |  `[INSTALL_REASON_POLICY](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_REASON_POLICY)` Code indicating that this package was installed due to enterprise policy.   
`int` |  `[INSTALL_REASON_UNKNOWN](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_REASON_UNKNOWN)` Code indicating that the reason for installing this package is unknown.   
`int` |  `[INSTALL_REASON_USER](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_REASON_USER)` Code indicating that the package installation was initiated by the user.   
`int` |  `[INSTALL_SCENARIO_BULK](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_SCENARIO_BULK)` Installation scenario indicating a bulk operation with the desired result of a fully optimized application.   
`int` |  `[INSTALL_SCENARIO_BULK_SECONDARY](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_SCENARIO_BULK_SECONDARY)` Installation scenario indicating a bulk operation that prioritizes minimal system health impact over application optimization.   
`int` |  `[INSTALL_SCENARIO_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_SCENARIO_DEFAULT)` A value to indicate the lack of CUJ information, disabling all installation scenario logic.   
`int` |  `[INSTALL_SCENARIO_FAST](https://developer.android.com/reference/android/content/pm/PackageManager#INSTALL_SCENARIO_FAST)` Installation scenario providing the fastest "install button to launch" experience possible.   
`int` |  `[MATCH_ALL](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_ALL)` Querying flag: if set and if the platform is doing any filtering of the results, then the filtering will not happen.   
`int` |  `[MATCH_APEX](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_APEX)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include APEX packages that are currently installed.   
`long` |  `[MATCH_ARCHIVED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_ARCHIVED_PACKAGES)` Flag parameter to also retrieve some information about archived packages.   
`int` |  `[MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)` Resolution and querying flag: if set, only filters that support the `[Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)` will be considered for matching.   
`int` |  `[MATCH_DIRECT_BOOT_AUTO](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AUTO)` Querying flag: automatically match components based on their Direct Boot awareness and the current user state.   
`int` |  `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` Querying flag: match components which are direct boot _aware_ in the returned info, regardless of the current user state.   
`int` |  `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)` Querying flag: match components which are direct boot _unaware_ in the returned info, regardless of the current user state.   
`int` |  `[MATCH_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COMPONENTS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include disabled components in the returned info.   
`int` |  `[MATCH_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTIL_USED_COMPONENTS)` `[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include disabled components which are in that state only because of `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)` in the returned info.   
`int` |  `[MATCH_SYSTEM_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_SYSTEM_ONLY)` Querying flag: include only components from applications that are marked with `[ApplicationInfo.FLAG_SYSTEM](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM)`.   
`int` |  `[MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)` Flag parameter to retrieve some information about all applications (even uninstalled ones) which have data directories.   
`long` |  `[MAXIMUM_VERIFICATION_TIMEOUT](https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATION_TIMEOUT)` Can be used as the `millisecondsToDelay` argument for `[PackageManager.extendVerificationTimeout](https://developer.android.com/reference/android/content/pm/PackageManager#extendVerificationTimeout\(int,%20int,%20long\))`.   
`int` |  `[PERMISSION_DENIED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_DENIED)` Permission check result: this is returned by `[checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission\(java.lang.String,%20java.lang.String\))` if the permission has not been granted to the given package.   
`int` |  `[PERMISSION_GRANTED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_GRANTED)` Permission check result: this is returned by `[checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission\(java.lang.String,%20java.lang.String\))` if the permission has been granted to the given package.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT)` Application level `[PackageManager .Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` for an app to inform the system that the app can be opted-in or opted-out from the compatibility treatment that rotates camera output by 90 degrees on landscape sensors on devices known to have compatibility issues.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_MEDIA_CAPABILITIES](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_MEDIA_CAPABILITIES)` <application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the XML resource ID containing an application's media capabilities XML file For example: <application> <property android:name="android.media.PROPERTY_MEDIA_CAPABILITIES" android:resource="@xml/media_capabilities"> <application>  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_NATIVE_SERVICE_FUNCTION_NAME](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_NATIVE_SERVICE_FUNCTION_NAME)` Service level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag for native services specifying the symbol name of the entry point function for the service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_NATIVE_SERVICE_LIBRARY_NAME](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_NATIVE_SERVICE_LIBRARY_NAME)` Service level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag for native services specifying the name of the library to be loaded to the process that hosts the service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES)` <application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the XML resource ID containing the declaration of the self-certified network capabilities used by the application.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_SPECIAL_USE_FGS_SUBTYPE](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_SPECIAL_USE_FGS_SUBTYPE)` <service> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the actual use case of the service if it's foreground service with the type `[ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SPECIAL_USE)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROPERTY_USE_RESTRICTED_BACKUP_MODE](https://developer.android.com/reference/android/content/pm/PackageManager#PROPERTY_USE_RESTRICTED_BACKUP_MODE)` <application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying whether the app should be put into the "restricted" backup mode when it's started for backup and restore operations.   
`int` |  `[SIGNATURE_FIRST_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_FIRST_NOT_SIGNED)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if the first package is not signed but the second is.   
`int` |  `[SIGNATURE_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_MATCH)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if all signatures on the two packages match.   
`int` |  `[SIGNATURE_NEITHER_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NEITHER_SIGNED)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if neither of the two packages is signed.   
`int` |  `[SIGNATURE_NO_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NO_MATCH)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if not all signatures on both packages match.   
`int` |  `[SIGNATURE_SECOND_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_SECOND_NOT_SIGNED)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if the second package is not signed but the first is.   
`int` |  `[SIGNATURE_UNKNOWN_PACKAGE](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_UNKNOWN_PACKAGE)` Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if either of the packages are not valid.   
`int` |  `[SYNCHRONOUS](https://developer.android.com/reference/android/content/pm/PackageManager#SYNCHRONOUS)` Flag parameter for `[setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))` to indicate that the given user's package restrictions state will be serialised to disk after the component state has been updated.   
`int` |  `[VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` Used as the `verificationCode` argument for `[PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))` to indicate that the calling package verifier allows the installation to proceed.   
`int` |  `[VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)` Used as the `verificationCode` argument for `[PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))` to indicate the calling package verifier does not vote to allow the installation to proceed.   
`int` |  `[VERSION_CODE_HIGHEST](https://developer.android.com/reference/android/content/pm/PackageManager#VERSION_CODE_HIGHEST)` Constant for specifying the highest installed package version code.   
  
### Fields  
  
---  
` public static final [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)>` |  `[TRUST_ALL](https://developer.android.com/reference/android/content/pm/PackageManager#TRUST_ALL)` Trust any Installer to provide checksums for the package.   
` public static final [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)>` |  `[TRUST_NONE](https://developer.android.com/reference/android/content/pm/PackageManager#TRUST_NONE)` Don't trust any Installer to provide checksums for the package.   
  
### Public constructors  
  
---  
` [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager#PackageManager\(\))() ` _This constructor is deprecated. Do not instantiate or subclass - obtain an instance from`[Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager\(\))`_  
  
### Public methods  
  
---  
` abstract void` |  ` [addPackageToPreferred](https://developer.android.com/reference/android/content/pm/PackageManager#addPackageToPreferred\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` _This method was deprecated in API level 15. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` abstract boolean` |  ` [addPermission](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo) info) ` Add a new dynamic permission to the system.   
` abstract boolean` |  ` [addPermissionAsync](https://developer.android.com/reference/android/content/pm/PackageManager#addPermissionAsync\(android.content.pm.PermissionInfo\))([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo) info) ` Like `[addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))` but asynchronously persists the package manager state after returning from the call, allowing it to return quicker and batch a series of adds at the expense of no guarantee the added permission will be retained if the device is rebooted before it is written.   
` abstract void` |  ` [addPreferredActivity](https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity\(android.content.IntentFilter,%20int,%20android.content.ComponentName\[\],%20android.content.ComponentName\))([IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) filter, int match, [ComponentName[]](https://developer.android.com/reference/android/content/ComponentName) set, [ComponentName](https://developer.android.com/reference/android/content/ComponentName) activity) ` _This method was deprecated in API level 15. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` boolean` |  ` [addWhitelistedRestrictedPermission](https://developer.android.com/reference/android/content/pm/PackageManager#addWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, [String](https://developer.android.com/reference/java/lang/String) permName, int whitelistFlags) ` Adds a whitelisted restricted permission for an app.   
` boolean` |  ` [canPackageQuery](https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) sourcePackageName, [String](https://developer.android.com/reference/java/lang/String) targetPackageName) ` Returns `true` if the source package is able to query for details about the target package.   
` boolean[]` |  ` [canPackageQuery](https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery\(java.lang.String,%20java.lang.String\[\]\))([String](https://developer.android.com/reference/java/lang/String) sourcePackageName, [String[]](https://developer.android.com/reference/java/lang/String) targetPackageNames) ` Same as `[canPackageQuery(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery\(java.lang.String,%20java.lang.String\))` but accepts an array of target packages to be queried.   
` abstract boolean` |  ` [canRequestPackageInstalls](https://developer.android.com/reference/android/content/pm/PackageManager#canRequestPackageInstalls\(\))() ` Checks whether the calling package is allowed to request package installs through package installer.   
` abstract [String[]](https://developer.android.com/reference/java/lang/String)` |  ` [canonicalToCurrentPackageNames](https://developer.android.com/reference/android/content/pm/PackageManager#canonicalToCurrentPackageNames\(java.lang.String\[\]\))([String[]](https://developer.android.com/reference/java/lang/String) packageNames) ` Map from a packages canonical name to the current name in use on the device.   
` abstract int` |  ` [checkPermission](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) permName, [String](https://developer.android.com/reference/java/lang/String) packageName) ` Check whether a particular package has been granted a particular permission.   
` abstract int` |  ` [checkSignatures](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName1, [String](https://developer.android.com/reference/java/lang/String) packageName2) ` Compare the signatures of two packages to determine if the same signature appears in both of them.   
` abstract int` |  ` [checkSignatures](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))(int uid1, int uid2) ` Like `[checkSignatures(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(java.lang.String,%20java.lang.String\))`, but takes UIDs of the two packages to be checked.   
` abstract void` |  ` [clearInstantAppCookie](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))() ` Clears the instant application cookie for the calling app.   
` abstract void` |  ` [clearPackagePreferredActivities](https://developer.android.com/reference/android/content/pm/PackageManager#clearPackagePreferredActivities\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` _This method was deprecated in API level 29. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` abstract [String[]](https://developer.android.com/reference/java/lang/String)` |  ` [currentToCanonicalPackageNames](https://developer.android.com/reference/android/content/pm/PackageManager#currentToCanonicalPackageNames\(java.lang.String\[\]\))([String[]](https://developer.android.com/reference/java/lang/String) packageNames) ` Map from the current package names in use on the device to whatever the current canonical name of that package is.   
` abstract void` |  ` [extendVerificationTimeout](https://developer.android.com/reference/android/content/pm/PackageManager#extendVerificationTimeout\(int,%20int,%20long\))(int id, int verificationCodeAtTimeout, long millisecondsToDelay) ` Allows a package listening to the `[package verification broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)` to extend the default timeout for a response and declare what action to perform after the timeout occurs.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityBanner](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner\(android.content.ComponentName\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName) ` Retrieve the banner associated with an activity.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityBanner](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner\(android.content.Intent\))([Intent](https://developer.android.com/reference/android/content/Intent) intent) ` Retrieve the banner associated with an Intent.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon\(android.content.Intent\))([Intent](https://developer.android.com/reference/android/content/Intent) intent) ` Retrieve the icon associated with an Intent.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon\(android.content.ComponentName\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName) ` Retrieve the icon associated with an activity.   
` abstract [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` |  ` [getActivityInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo\(android.content.ComponentName,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, int flags) ` Retrieve all of the information we know about a particular activity class.   
` [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` |  ` [getActivityInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[getActivityInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo\(android.content.ComponentName,%20int\))`.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityLogo](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo\(android.content.Intent\))([Intent](https://developer.android.com/reference/android/content/Intent) intent) ` Retrieve the logo associated with an Intent.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getActivityLogo](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo\(android.content.ComponentName\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName) ` Retrieve the logo associated with an activity.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)>` |  ` [getAllPermissionGroups](https://developer.android.com/reference/android/content/pm/PackageManager#getAllPermissionGroups\(int\))(int flags) ` Retrieve all of the known permission groups in the system.   
` int` |  ` [getAppUidForPrivateComputeCoreUid](https://developer.android.com/reference/android/content/pm/PackageManager#getAppUidForPrivateComputeCoreUid\(int\))(int pccUid) ` Maps a Private Compute Core (PCC) UID to its corresponding application UID.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationBanner](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Retrieve the banner associated with an application.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationBanner](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info) ` Retrieve the banner associated with an application.   
` abstract int` |  ` [getApplicationEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationEnabledSetting\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Return the enabled setting for an application.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info) ` Retrieve the icon associated with an application.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Retrieve the icon associated with an application.   
` [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` |  ` [getApplicationInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo\(java.lang.String,%20android.content.pm.PackageManager.ApplicationInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) packageName, [PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags) flags) ` See `[getApplicationInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo\(java.lang.String,%20int\))`.   
` abstract [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` |  ` [getApplicationInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int flags) ` Retrieve all of the information we know about a particular package/application.   
` abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` |  ` [getApplicationLabel](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLabel\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info) ` Return the label to use for this application.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationLogo](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Retrieve the logo associated with an application.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getApplicationLogo](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info) ` Retrieve the logo associated with an application.   
` [ArchivedPackageInfo](https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo)` |  ` [getArchivedPackage](https://developer.android.com/reference/android/content/pm/PackageManager#getArchivedPackage\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Return archived package info for the package or null if the package is not installed.   
` [CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` |  ` [getBackgroundPermissionOptionLabel](https://developer.android.com/reference/android/content/pm/PackageManager#getBackgroundPermissionOptionLabel\(\))() ` Gets the localized label that corresponds to the option in settings for granting background access.   
` abstract [ChangedPackages](https://developer.android.com/reference/android/content/pm/ChangedPackages)` |  ` [getChangedPackages](https://developer.android.com/reference/android/content/pm/PackageManager#getChangedPackages\(int\))(int sequenceNumber) ` Returns the names of the packages that have been changed [eg.   
` abstract int` |  ` [getComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager#getComponentEnabledSetting\(android.content.ComponentName\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) componentName) ` Return the enabled setting for a package component (activity, receiver, service, provider).   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getDefaultActivityIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getDefaultActivityIcon\(\))() ` Return the generic icon for an activity that is used when no specific icon is defined.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getDrawable](https://developer.android.com/reference/android/content/pm/PackageManager#getDrawable\(java.lang.String,%20int,%20android.content.pm.ApplicationInfo\))([String](https://developer.android.com/reference/java/lang/String) packageName, int resid, [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo) ` Retrieve an image from a package.   
` [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` |  ` [getEnableAppLockIntentForPackage](https://developer.android.com/reference/android/content/pm/PackageManager#getEnableAppLockIntentForPackage\(java.lang.String,%20boolean\))([String](https://developer.android.com/reference/java/lang/String) packageName, boolean enabled) ` Returns a `[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` to launch an `[Activity](https://developer.android.com/reference/android/app/Activity)` that allows the caller to set App Lock for the specified package.   
` void` |  ` [getGroupOfPlatformPermission](https://developer.android.com/reference/android/content/pm/PackageManager#getGroupOfPlatformPermission\(java.lang.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer<java.lang.String>\))([String](https://developer.android.com/reference/java/lang/String) permissionName, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) executor, [Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[String](https://developer.android.com/reference/java/lang/String)> callback) ` Get the platform-defined permission group of a particular permission, if the permission is a platform-defined permission.   
` [InstallSourceInfo](https://developer.android.com/reference/android/content/pm/InstallSourceInfo)` |  ` [getInstallSourceInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Retrieves information about how a package was installed or updated.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)>` |  ` [getInstalledApplications](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(int\))(int flags) ` Return a List of all application packages that are installed for the current user.   
` [List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)>` |  ` [getInstalledApplications](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(android.content.pm.PackageManager.ApplicationInfoFlags\))([PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags) flags) ` See `[getInstalledApplications(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(int\))`  
` [List](https://developer.android.com/reference/java/util/List)<[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)>` |  ` [getInstalledModules](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledModules\(int\))(int flags) ` Return a List of all modules that are installed.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` |  ` [getInstalledPackages](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(int\))(int flags) ` Return a List of all packages that are installed for the current user.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` |  ` [getInstalledPackages](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(android.content.pm.PackageManager.PackageInfoFlags\))([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getInstalledPackages(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(int\))`.   
` abstract [String](https://developer.android.com/reference/java/lang/String)` |  ` [getInstallerPackageName](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageName\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` _This method was deprecated in API level 30. use`[getInstallSourceInfo(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo\(java.lang.String\))` instead_  
` abstract byte[]` |  ` [getInstantAppCookie](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))() ` Gets the instant application cookie for this app.   
` abstract int` |  ` [getInstantAppCookieMaxBytes](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))() ` Gets the maximum size in bytes of the cookie data an instant app can store on the device.   
` abstract [InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)` |  ` [getInstrumentationInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getInstrumentationInfo\(android.content.ComponentName,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) className, int flags) ` Retrieve all of the information we know about a particular instrumentation class.   
` abstract [Intent](https://developer.android.com/reference/android/content/Intent)` |  ` [getLaunchIntentForPackage](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPackage\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Returns a "good" intent to launch a front-door activity in a package.   
` [IntentSender](https://developer.android.com/reference/android/content/IntentSender)` |  ` [getLaunchIntentSenderForPackage](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderForPackage\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Returns an `[IntentSender](https://developer.android.com/reference/android/content/IntentSender)` that can be used to launch a front-door activity in a package.   
` abstract [Intent](https://developer.android.com/reference/android/content/Intent)` |  ` [getLeanbackLaunchIntentForPackage](https://developer.android.com/reference/android/content/pm/PackageManager#getLeanbackLaunchIntentForPackage\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Return a "good" intent to launch a front-door Leanback activity in a package, for use for example to implement an "open" button when browsing through packages.   
` [List](https://developer.android.com/reference/java/util/List)<[MemoryBudgetInfo](https://developer.android.com/reference/android/content/pm/MemoryBudgetInfo)>` |  ` [getMemoryBudgets](https://developer.android.com/reference/android/content/pm/PackageManager#getMemoryBudgets\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info) ` Return the memory budgets for the application described by the given `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)`.   
` [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)>` |  ` [getMimeGroup](https://developer.android.com/reference/android/content/pm/PackageManager#getMimeGroup\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) mimeGroup) ` Gets all MIME types contained by MIME group.   
` [ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)` |  ` [getModuleInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getModuleInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int flags) ` Retrieve information for a particular module.   
` abstract [String](https://developer.android.com/reference/java/lang/String)` |  ` [getNameForUid](https://developer.android.com/reference/android/content/pm/PackageManager#getNameForUid\(int\))(int uid) ` Retrieve the official name associated with a uid.   
` [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageArchiveInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) archiveFilePath, int flags) ` Retrieve overall information about an application package defined in a package archive file Use `[getPackageArchiveInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.   
` [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageArchiveInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) archiveFilePath, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackageArchiveInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20int\))`.   
` abstract int[]` |  ` [getPackageGids](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Return an array of all of the POSIX secondary group IDs that have been assigned to the given package.   
` abstract int[]` |  ` [getPackageGids](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int flags) ` Return an array of all of the POSIX secondary group IDs that have been assigned to the given package.   
` int[]` |  ` [getPackageGids](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) packageName, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackageGids(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String,%20int\))`.   
` abstract [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int flags) ` Retrieve overall information about an application package that is installed on the system.   
` [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) packageName, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackageInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(java.lang.String,%20int\))`  
` [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(android.content.pm.VersionedPackage,%20android.content.pm.PackageManager.PackageInfoFlags\))([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage) versionedPackage, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackageInfo(VersionedPackage,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(android.content.pm.VersionedPackage,%20int\))`  
` abstract [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` |  ` [getPackageInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(android.content.pm.VersionedPackage,%20int\))([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage) versionedPackage, int flags) ` Retrieve overall information about an application package that is installed on the system.   
` abstract [PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller)` |  ` [getPackageInstaller](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInstaller\(\))() ` Return interface that offers the ability to install, upgrade, and remove applications on the device.   
` int` |  ` [getPackageUid](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) packageName, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackageUid(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid\(java.lang.String,%20int\))`.   
` abstract int` |  ` [getPackageUid](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int flags) ` Return the UID associated with the given package name.   
` abstract [String[]](https://developer.android.com/reference/java/lang/String)` |  ` [getPackagesForUid](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesForUid\(int\))(int uid) ` Retrieve the names of all packages that are associated with a particular user id.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` |  ` [getPackagesHoldingPermissions](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions\(java.lang.String\[\],%20int\))([String[]](https://developer.android.com/reference/java/lang/String) permissions, int flags) ` Return a List of all installed packages that are currently holding any of the given permissions.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` |  ` [getPackagesHoldingPermissions](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions\(java.lang.String\[\],%20android.content.pm.PackageManager.PackageInfoFlags\))([String[]](https://developer.android.com/reference/java/lang/String) permissions, [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getPackagesHoldingPermissions(String[],int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions\(java.lang.String\[\],%20int\))`.   
` abstract [PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)` |  ` [getPermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPermissionGroupInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) groupName, int flags) ` Retrieve all of the information we know about a particular group of permissions.   
` abstract [PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)` |  ` [getPermissionInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getPermissionInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) permName, int flags) ` Retrieve all of the information we know about a particular permission.   
` void` |  ` [getPlatformPermissionsForGroup](https://developer.android.com/reference/android/content/pm/PackageManager#getPlatformPermissionsForGroup\(java.lang.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer<java.util.List<java.lang.String>>\))([String](https://developer.android.com/reference/java/lang/String) permissionGroupName, [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) executor, [Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[List](https://developer.android.com/reference/java/util/List)<[String](https://developer.android.com/reference/java/lang/String)>> callback) ` Get the platform-defined permissions which belong to a particular permission group.   
` abstract int` |  ` [getPreferredActivities](https://developer.android.com/reference/android/content/pm/PackageManager#getPreferredActivities\(java.util.List<android.content.IntentFilter>,%20java.util.List<android.content.ComponentName>,%20java.lang.String\))([List](https://developer.android.com/reference/java/util/List)<[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)> outFilters, [List](https://developer.android.com/reference/java/util/List)<[ComponentName](https://developer.android.com/reference/android/content/ComponentName)> outActivities, [String](https://developer.android.com/reference/java/lang/String) packageName) ` _This method was deprecated in API level 29. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` |  ` [getPreferredPackages](https://developer.android.com/reference/android/content/pm/PackageManager#getPreferredPackages\(int\))(int flags) ` _This method was deprecated in API level 29. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` |  ` [getProperty](https://developer.android.com/reference/android/content/pm/PackageManager#getProperty\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName, [String](https://developer.android.com/reference/java/lang/String) packageName) ` Returns the property defined in the given package's <application> tag.   
` [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` |  ` [getProperty](https://developer.android.com/reference/android/content/pm/PackageManager#getProperty\(java.lang.String,%20android.content.ComponentName\))([String](https://developer.android.com/reference/java/lang/String) propertyName, [ComponentName](https://developer.android.com/reference/android/content/ComponentName) component) ` Returns the property defined in the given component declaration.   
` abstract [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` |  ` [getProviderInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo\(android.content.ComponentName,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, int flags) ` Retrieve all of the information we know about a particular content provider class.   
` [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` |  ` [getProviderInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[getProviderInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo\(android.content.ComponentName,%20int\))`.   
` abstract [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` |  ` [getReceiverInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo\(android.content.ComponentName,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, int flags) ` Retrieve all of the information we know about a particular receiver class.   
` [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` |  ` [getReceiverInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[getReceiverInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo\(android.content.ComponentName,%20int\))`.   
` abstract [Resources](https://developer.android.com/reference/android/content/res/Resources)` |  ` [getResourcesForActivity](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForActivity\(android.content.ComponentName\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName) ` Retrieve the resources associated with an activity.   
` abstract [Resources](https://developer.android.com/reference/android/content/res/Resources)` |  ` [getResourcesForApplication](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplication\(android.content.pm.ApplicationInfo\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) app) ` Retrieve the resources for an application.   
` abstract [Resources](https://developer.android.com/reference/android/content/res/Resources)` |  ` [getResourcesForApplication](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplication\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Retrieve the resources associated with an application.   
` [Resources](https://developer.android.com/reference/android/content/res/Resources)` |  ` [getResourcesForApplication](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplication\(android.content.pm.ApplicationInfo,%20android.content.res.Configuration\))([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) app, [Configuration](https://developer.android.com/reference/android/content/res/Configuration) configuration) ` Retrieve the resources for an application for the provided configuration.   
` [ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)` |  ` [getServiceInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[getServiceInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo\(android.content.ComponentName,%20int\))`.   
` abstract [ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)` |  ` [getServiceInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo\(android.content.ComponentName,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, int flags) ` Retrieve all of the information we know about a particular service class.   
` [List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>` |  ` [getSharedLibraries](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries\(android.content.pm.PackageManager.PackageInfoFlags\))([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags) ` See `[getSharedLibraries(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries\(int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>` |  ` [getSharedLibraries](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries\(int\))(int flags) ` Get a list of shared libraries on the device.   
` [Bundle](https://developer.android.com/reference/android/os/Bundle)` |  ` [getSuspendedPackageAppExtras](https://developer.android.com/reference/android/content/pm/PackageManager#getSuspendedPackageAppExtras\(\))() ` Returns a `[Bundle](https://developer.android.com/reference/android/os/Bundle)` of extras that was meant to be sent to the calling app when it was suspended.   
` boolean` |  ` [getSyntheticAppDetailsActivityEnabled](https://developer.android.com/reference/android/content/pm/PackageManager#getSyntheticAppDetailsActivityEnabled\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Return whether a synthetic app details activity will be generated if the app has no enabled launcher activity.   
` abstract [FeatureInfo[]](https://developer.android.com/reference/android/content/pm/FeatureInfo)` |  ` [getSystemAvailableFeatures](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))() ` Get a list of features that are available on the system.   
` abstract [String[]](https://developer.android.com/reference/java/lang/String)` |  ` [getSystemSharedLibraryNames](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemSharedLibraryNames\(\))() ` Get a list of shared libraries that are available on the system.   
` int` |  ` [getTargetSdkVersion](https://developer.android.com/reference/android/content/pm/PackageManager#getTargetSdkVersion\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) `  
` abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` |  ` [getText](https://developer.android.com/reference/android/content/pm/PackageManager#getText\(java.lang.String,%20int,%20android.content.pm.ApplicationInfo\))([String](https://developer.android.com/reference/java/lang/String) packageName, int resid, [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo) ` Retrieve text from a package.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getUserBadgedDrawableForDensity](https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedDrawableForDensity\(android.graphics.drawable.Drawable,%20android.os.UserHandle,%20android.graphics.Rect,%20int\))([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable, [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user, [Rect](https://developer.android.com/reference/android/graphics/Rect) badgeLocation, int badgeDensity) ` If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a badged copy of the given drawable allowing the user to distinguish it from the original drawable.   
` abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` |  ` [getUserBadgedIcon](https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedIcon\(android.graphics.drawable.Drawable,%20android.os.UserHandle\))([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable, [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user) ` If the target user is a managed profile, then this returns a badged copy of the given icon to be able to distinguish it from the original icon.   
` abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` |  ` [getUserBadgedLabel](https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedLabel\(java.lang.CharSequence,%20android.os.UserHandle\))([CharSequence](https://developer.android.com/reference/java/lang/CharSequence) label, [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user) ` If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a copy of the label with badging for accessibility services like talkback.   
` static [SigningInfo](https://developer.android.com/reference/android/content/pm/SigningInfo)` |  ` [getVerifiedSigningInfo](https://developer.android.com/reference/android/content/pm/PackageManager#getVerifiedSigningInfo\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) path, int minAppSigningSchemeVersion) ` Verifies and returns the [app signing](https://source.android.com/docs/security/features/apksigning) information of the file at the given path.   
` [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)>` |  ` [getWhitelistedRestrictedPermissions](https://developer.android.com/reference/android/content/pm/PackageManager#getWhitelistedRestrictedPermissions\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int whitelistFlag) ` Gets the restricted permissions that have been whitelisted and the app is allowed to have them granted in their full form.   
` abstract [XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser)` |  ` [getXml](https://developer.android.com/reference/android/content/pm/PackageManager#getXml\(java.lang.String,%20int,%20android.content.pm.ApplicationInfo\))([String](https://developer.android.com/reference/java/lang/String) packageName, int resid, [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo) ` Retrieve an XML file from a package.   
` boolean` |  ` [hasSigningCertificate](https://developer.android.com/reference/android/content/pm/PackageManager#hasSigningCertificate\(int,%20byte\[\],%20int\))(int uid, byte[] certificate, int type) ` Searches the set of signing certificates by which the package(s) for the given uid has proven to have been signed.   
` boolean` |  ` [hasSigningCertificate](https://developer.android.com/reference/android/content/pm/PackageManager#hasSigningCertificate\(java.lang.String,%20byte\[\],%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, byte[] certificate, int type) ` Searches the set of signing certificates by which the given package has proven to have been signed.   
` abstract boolean` |  ` [hasSystemFeature](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) featureName) ` Check whether the given feature name is one of the available features as returned by `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`.   
` abstract boolean` |  ` [hasSystemFeature](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) featureName, int version) ` Check whether the given feature name and version is one of the available features as returned by `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`.   
` boolean` |  ` [isAppArchivable](https://developer.android.com/reference/android/content/pm/PackageManager#isAppArchivable\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Returns true if an app is archivable.   
` boolean` |  ` [isAutoRevokeWhitelisted](https://developer.android.com/reference/android/content/pm/PackageManager#isAutoRevokeWhitelisted\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Checks whether an application is exempt from having its permissions be automatically revoked when the app is unused for an extended period of time.   
` boolean` |  ` [isAutoRevokeWhitelisted](https://developer.android.com/reference/android/content/pm/PackageManager#isAutoRevokeWhitelisted\(\))() ` **Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API.   
` boolean` |  ` [isDefaultApplicationIcon](https://developer.android.com/reference/android/content/pm/PackageManager#isDefaultApplicationIcon\(android.graphics.drawable.Drawable\))([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable) ` Returns if the provided drawable represents the default activity icon provided by the system.   
` boolean` |  ` [isDeviceUpgrading](https://developer.android.com/reference/android/content/pm/PackageManager#isDeviceUpgrading\(\))() ` Returns true if the device is upgrading, such as first boot after OTA.   
` abstract boolean` |  ` [isInstantApp](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))() ` Gets whether this application is an instant app.   
` abstract boolean` |  ` [isInstantApp](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Gets whether the given package is an instant app.   
` boolean` |  ` [isPackageStopped](https://developer.android.com/reference/android/content/pm/PackageManager#isPackageStopped\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Query if an app is currently stopped.   
` boolean` |  ` [isPackageSuspended](https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` Query if an app is currently suspended.   
` boolean` |  ` [isPackageSuspended](https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended\(\))() ` Apps can query this to know if they have been suspended.   
` abstract boolean` |  ` [isPermissionRevokedByPolicy](https://developer.android.com/reference/android/content/pm/PackageManager#isPermissionRevokedByPolicy\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) permName, [String](https://developer.android.com/reference/java/lang/String) packageName) ` Checks whether a particular permissions has been revoked for a package by policy.   
` abstract boolean` |  ` [isSafeMode](https://developer.android.com/reference/android/content/pm/PackageManager#isSafeMode\(\))() ` Return whether the device has been booted into safe mode.   
` <T> T` |  ` [parseAndroidManifest](https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest\(java.io.File,%20java.util.function.Function<android.content.res.XmlResourceParser,T>\))([File](https://developer.android.com/reference/java/io/File) apkFile, [Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction) ` Retrieve AndroidManifest.xml information for the given application apk file.   
` <T> T` |  ` [parseAndroidManifest](https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest\(android.os.ParcelFileDescriptor,%20java.util.function.Function<android.content.res.XmlResourceParser,T>\))([ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor) apkFileDescriptor, [Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction) ` Similar to `[parseAndroidManifest(File,Function)](https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest\(java.io.File,%20java.util.function.Function<android.content.res.XmlResourceParser,T>\))`, but accepting a file descriptor instead of a File object.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` |  ` [queryActivityProperty](https://developer.android.com/reference/android/content/pm/PackageManager#queryActivityProperty\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName) ` Returns the property definition for all <activity> and <activity-alias> tags.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` |  ` [queryApplicationProperty](https://developer.android.com/reference/android/content/pm/PackageManager#queryApplicationProperty\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName) ` Returns the property definition for all <application> tags.   
` [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryBroadcastReceivers](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[queryBroadcastReceivers(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers\(android.content.Intent,%20int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryBroadcastReceivers](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Retrieve all receivers that can handle a broadcast of the given intent.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)>` |  ` [queryContentProviders](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders\(java.lang.String,%20int,%20int\))([String](https://developer.android.com/reference/java/lang/String) processName, int uid, int flags) ` Retrieve content provider information.   
` [List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)>` |  ` [queryContentProviders](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders\(java.lang.String,%20int,%20android.content.pm.PackageManager.ComponentInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) processName, int uid, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[queryContentProviders(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders\(java.lang.String,%20int,%20int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)>` |  ` [queryInstrumentation](https://developer.android.com/reference/android/content/pm/PackageManager#queryInstrumentation\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) targetPackage, int flags) ` Retrieve information about available instrumentation code.   
` [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentActivities](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[queryIntentActivities(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentActivities](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Retrieve all activities that can be performed for the given intent.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentActivityOptions](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions\(android.content.ComponentName,%20android.content.Intent\[\],%20android.content.Intent,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) caller, [Intent[]](https://developer.android.com/reference/android/content/Intent) specifics, [Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Retrieve a set of activities that should be presented to the user as similar options.   
` [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentActivityOptions](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions\(android.content.ComponentName,%20java.util.List<android.content.Intent>,%20android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) caller, [List](https://developer.android.com/reference/java/util/List)<[Intent](https://developer.android.com/reference/android/content/Intent)> specifics, [Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[queryIntentActivityOptions(ComponentName,Intent[],Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions\(android.content.ComponentName,%20android.content.Intent\[\],%20android.content.Intent,%20int\))`.   
` [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentContentProviders](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[queryIntentContentProviders(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders\(android.content.Intent,%20int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentContentProviders](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Retrieve all providers that can match the given intent.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentServices](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Retrieve all services that can match the given intent.   
` [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` |  ` [queryIntentServices](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[queryIntentServices(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices\(android.content.Intent,%20int\))`.   
` abstract [List](https://developer.android.com/reference/java/util/List)<[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)>` |  ` [queryPermissionsByGroup](https://developer.android.com/reference/android/content/pm/PackageManager#queryPermissionsByGroup\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) permissionGroup, int flags) ` Query for all of the permissions associated with a particular group.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` |  ` [queryProviderProperty](https://developer.android.com/reference/android/content/pm/PackageManager#queryProviderProperty\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName) ` Returns the property definition for all <provider> tags.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` |  ` [queryReceiverProperty](https://developer.android.com/reference/android/content/pm/PackageManager#queryReceiverProperty\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName) ` Returns the property definition for all <receiver> tags.   
` [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` |  ` [queryServiceProperty](https://developer.android.com/reference/android/content/pm/PackageManager#queryServiceProperty\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) propertyName) ` Returns the property definition for all <service> tags.   
` void` |  ` [relinquishUpdateOwnership](https://developer.android.com/reference/android/content/pm/PackageManager#relinquishUpdateOwnership\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) targetPackage) ` Attempt to relinquish the update ownership of the given package.   
` abstract void` |  ` [removePackageFromPreferred](https://developer.android.com/reference/android/content/pm/PackageManager#removePackageFromPreferred\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) packageName) ` _This method was deprecated in API level 15. This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use`[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`._  
` abstract void` |  ` [removePermission](https://developer.android.com/reference/android/content/pm/PackageManager#removePermission\(java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) permName) ` Removes a permission that was previously added with `[addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))`.   
` boolean` |  ` [removeWhitelistedRestrictedPermission](https://developer.android.com/reference/android/content/pm/PackageManager#removeWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, [String](https://developer.android.com/reference/java/lang/String) permName, int whitelistFlags) ` Removes a whitelisted restricted permission for an app.   
` void` |  ` [requestChecksums](https://developer.android.com/reference/android/content/pm/PackageManager#requestChecksums\(java.lang.String,%20boolean,%20int,%20java.util.List<java.security.cert.Certificate>,%20android.content.pm.PackageManager.OnChecksumsReadyListener\))([String](https://developer.android.com/reference/java/lang/String) packageName, boolean includeSplits, int required, [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> trustedInstallers, [PackageManager.OnChecksumsReadyListener](https://developer.android.com/reference/android/content/pm/PackageManager.OnChecksumsReadyListener) onChecksumsReadyListener) ` Requests the checksums for APKs within a package.   
` [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` |  ` [resolveActivity](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[resolveActivity(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20int\))`.   
` abstract [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` |  ` [resolveActivity](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Determine the best action to perform for a given Intent.   
` [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` |  ` [resolveContentProvider](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider\(java.lang.String,%20android.content.pm.PackageManager.ComponentInfoFlags\))([String](https://developer.android.com/reference/java/lang/String) authority, [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags) ` See `[resolveContentProvider(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider\(java.lang.String,%20int\))`.   
` abstract [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` |  ` [resolveContentProvider](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) authority, int flags) ` Find a single content provider by its authority.   
` abstract [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` |  ` [resolveService](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20int\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, int flags) ` Determine the best service to handle for a given Intent.   
` [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` |  ` [resolveService](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))([Intent](https://developer.android.com/reference/android/content/Intent) intent, [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags) ` See `[resolveService(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20int\))`.   
` abstract void` |  ` [setApplicationCategoryHint](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationCategoryHint\(java.lang.String,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int categoryHint) ` Provide a hint of what the `[ApplicationInfo.category](https://developer.android.com/reference/android/content/pm/ApplicationInfo#category)` value should be for the given package.   
` abstract void` |  ` [setApplicationEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))([String](https://developer.android.com/reference/java/lang/String) packageName, int newState, int flags) ` Set the enabled setting for an application This setting will override any enabled state which may have been set by the application in its manifest.   
` boolean` |  ` [setAutoRevokeWhitelisted](https://developer.android.com/reference/android/content/pm/PackageManager#setAutoRevokeWhitelisted\(java.lang.String,%20boolean\))([String](https://developer.android.com/reference/java/lang/String) packageName, boolean whitelisted) ` Marks an application exempt from having its permissions be automatically revoked when the app is unused for an extended period of time.   
` abstract void` |  ` [setComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))([ComponentName](https://developer.android.com/reference/android/content/ComponentName) componentName, int newState, int flags) ` Set the enabled setting for a package component (activity, receiver, service, provider).   
` void` |  ` [setComponentEnabledSettings](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSettings\(java.util.List<android.content.pm.PackageManager.ComponentEnabledSetting>\))([List](https://developer.android.com/reference/java/util/List)<[PackageManager.ComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentEnabledSetting)> settings) ` Set the enabled settings for package components such as activities, receivers, services and providers.   
` abstract void` |  ` [setInstallerPackageName](https://developer.android.com/reference/android/content/pm/PackageManager#setInstallerPackageName\(java.lang.String,%20java.lang.String\))([String](https://developer.android.com/reference/java/lang/String) targetPackage, [String](https://developer.android.com/reference/java/lang/String) installerPackageName) ` Change the installer associated with a given package.   
` void` |  ` [setMimeGroup](https://developer.android.com/reference/android/content/pm/PackageManager#setMimeGroup\(java.lang.String,%20java.util.Set<java.lang.String>\))([String](https://developer.android.com/reference/java/lang/String) mimeGroup, [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> mimeTypes) ` Sets MIME group's MIME types.   
` abstract void` |  ` [updateInstantAppCookie](https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie\(byte\[\]\))(byte[] cookie) ` Updates the instant application cookie for the calling app.   
` abstract void` |  ` [verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))(int id, int verificationCode) ` Allows a package listening to the `[package verification broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)` to respond to the package manager.   
  
### Inherited methods  
  
---  
From class ` [java.lang.Object](https://developer.android.com/reference/java/lang/Object) ` | ` [Object](https://developer.android.com/reference/java/lang/Object)` |  ` [clone](https://developer.android.com/reference/java/lang/Object#clone\(\))() ` Creates and returns a copy of this object.   
---|---  
` boolean` |  ` [equals](https://developer.android.com/reference/java/lang/Object#equals\(java.lang.Object\))([Object](https://developer.android.com/reference/java/lang/Object) obj) ` Indicates whether some other object is "equal to" this one.   
` void` |  ` [finalize](https://developer.android.com/reference/java/lang/Object#finalize\(\))() ` Called by the garbage collector on an object when garbage collection determines that there are no more references to the object.   
` final [Class](https://developer.android.com/reference/java/lang/Class)<?>` |  ` [getClass](https://developer.android.com/reference/java/lang/Object#getClass\(\))() ` Returns the runtime class of this `Object`.   
` int` |  ` [hashCode](https://developer.android.com/reference/java/lang/Object#hashCode\(\))() ` Returns a hash code value for the object.   
` final void` |  ` [notify](https://developer.android.com/reference/java/lang/Object#notify\(\))() ` Wakes up a single thread that is waiting on this object's monitor.   
` final void` |  ` [notifyAll](https://developer.android.com/reference/java/lang/Object#notifyAll\(\))() ` Wakes up all threads that are waiting on this object's monitor.   
` [String](https://developer.android.com/reference/java/lang/String)` |  ` [toString](https://developer.android.com/reference/java/lang/Object#toString\(\))() ` Returns a string representation of the object.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(long,%20int\))(long timeoutMillis, int nanos) ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_ , or until a certain amount of real time has elapsed.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(long\))(long timeoutMillis) ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_ , or until a certain amount of real time has elapsed.   
` final void` |  ` [wait](https://developer.android.com/reference/java/lang/Object#wait\(\))() ` Causes the current thread to wait until it is awakened, typically by being _notified_ or _interrupted_.   
  
## Constants

### CERT_INPUT_RAW_X509

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int CERT_INPUT_RAW_X509

Certificate input bytes: the input bytes represent an encoded X.509 Certificate which could be generated using an `CertificateFactory`

Constant Value: 0 (0x00000000) 

### CERT_INPUT_SHA256

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int CERT_INPUT_SHA256

Certificate input bytes: the input bytes represent the SHA256 output of an encoded X.509 Certificate.

Constant Value: 1 (0x00000001) 

### COMPONENT_ENABLED_STATE_DEFAULT

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int COMPONENT_ENABLED_STATE_DEFAULT

Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application is in its default enabled state (as specified in its manifest). 

Explicitly setting the component state to this value restores it's enabled state to whatever is set in the manifest.

Constant Value: 0 (0x00000000) 

### COMPONENT_ENABLED_STATE_DISABLED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int COMPONENT_ENABLED_STATE_DISABLED

Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application has been explicitly disabled, regardless of what it has specified in its manifest.

Constant Value: 2 (0x00000002) 

### COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED

Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` only: This application should be considered, until the point where the user actually wants to use it. This means that it will not normally show up to the user (such as in the launcher), but various parts of the user interface can use `[GET_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_DISABLED_UNTIL_USED_COMPONENTS)` to still see it and allow the user to select it (as for example an IME, device admin, etc). Such code, once the user has selected the app, should at that point also make it enabled. This option currently **can not** be used with `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`.

Constant Value: 4 (0x00000004) 

### COMPONENT_ENABLED_STATE_DISABLED_USER

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int COMPONENT_ENABLED_STATE_DISABLED_USER

Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` only: The user has explicitly disabled the application, regardless of what it has specified in its manifest. Because this is due to the user's request, they may re-enable it if desired through the appropriate system UI. This option currently **cannot** be used with `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`.

Constant Value: 3 (0x00000003) 

### COMPONENT_ENABLED_STATE_ENABLED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int COMPONENT_ENABLED_STATE_ENABLED

Flag for `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))` and `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`: This component or application has been explictily enabled, regardless of what it has specified in its manifest.

Constant Value: 1 (0x00000001) 

### DELETE_ARCHIVE

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int DELETE_ARCHIVE

Flag parameter for `[PackageInstaller.uninstall(VersionedPackage,int,IntentSender)](https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall\(android.content.pm.VersionedPackage,%20int,%20android.content.IntentSender\))` to indicate that the deletion is an archival. This flag is only for internal usage as part of `[PackageInstaller.requestArchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive\(java.lang.String,%20android.content.IntentSender\))`.

Constant Value: 16 (0x00000010) 

### DONT_KILL_APP

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int DONT_KILL_APP

Flag parameter for `[setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))` to indicate that you don't want to kill the app containing the component. Be careful when you set this since changing component states can make the containing application's behavior unpredictable.

Constant Value: 1 (0x00000001) 

### EXTRA_VERIFICATION_ID

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) EXTRA_VERIFICATION_ID

Extra field name for the ID of a package pending verification. Passed to a package verifier and is used to call back to `[PackageManager.verifyPendingInstall(int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))`

Constant Value: "android.content.pm.extra.VERIFICATION_ID" 

### EXTRA_VERIFICATION_RESULT

Added in [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) EXTRA_VERIFICATION_RESULT

Extra field name for the result of a verification, either `[VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)`, or `[VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`. Passed to package verifiers after a package is verified.

Constant Value: "android.content.pm.extra.VERIFICATION_RESULT" 

### FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_ACTIVITIES_ON_SECONDARY_DISPLAYS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports running activities on secondary displays. Displays here refers to both physical and virtual displays. Disabling this feature can impact support for application projection use-cases and support for virtual devices on the device.

Constant Value: "android.software.activities_on_secondary_displays" 

### FEATURE_APP_WIDGETS

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_APP_WIDGETS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports app widgets.

Constant Value: "android.software.app_widgets" 

### FEATURE_AUDIO_LOW_LATENCY

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUDIO_LOW_LATENCY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's audio pipeline is low-latency, more suitable for audio applications sensitive to delays or lag in sound input or output.

Constant Value: "android.hardware.audio.low_latency" 

### FEATURE_AUDIO_OUTPUT

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUDIO_OUTPUT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes at least one form of audio output, as defined in the Android Compatibility Definition Document (CDD) [section 7.8 Audio](https://source.android.com/compatibility/android-cdd#7_8_audio).

Constant Value: "android.hardware.audio.output" 

### FEATURE_AUDIO_PRO

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUDIO_PRO

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has professional audio level of functionality and performance.

Constant Value: "android.hardware.audio.pro" 

### FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUDIO_SPATIAL_HEADTRACKING_LOW_LATENCY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))` which indicates whether head tracking for spatial audio operates with low-latency, as defined by the CDD criteria for the feature.

Constant Value: "android.hardware.audio.spatial.headtracking.low_latency" 

### FEATURE_AUTOFILL

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUTOFILL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports autofill of user credentials, addresses, credit cards, etc via integration with `[autofill providers](https://developer.android.com/reference/android/service/autofill/AutofillService)`.

Constant Value: "android.software.autofill" 

### FEATURE_AUTOMOTIVE

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_AUTOMOTIVE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to showing UI on a vehicle headunit. A headunit here is defined to be inside a vehicle that may or may not be moving. A headunit uses either a primary display in the center console and/or additional displays in the instrument cluster or elsewhere in the vehicle. Headunit display(s) have limited size and resolution. The user will likely be focused on driving so limiting driver distraction is a primary concern. User input can be a variety of hard buttons, touch, rotary controllers and even mouse- like interfaces.

Constant Value: "android.hardware.type.automotive" 

### FEATURE_BACKUP

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_BACKUP

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can perform backup and restore operations on installed applications.

Constant Value: "android.software.backup" 

### FEATURE_BLUETOOTH

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_BLUETOOTH

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via Bluetooth.

Constant Value: "android.hardware.bluetooth" 

### FEATURE_BLUETOOTH_LE

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_BLUETOOTH_LE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via Bluetooth Low Energy radio.

Constant Value: "android.hardware.bluetooth_le" 

### FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_BLUETOOTH_LE_CHANNEL_SOUNDING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of ranging with other devices using channel sounding via Bluetooth Low Energy radio.

Constant Value: "android.hardware.bluetooth_le.channel_sounding" 

### FEATURE_CAMERA

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a camera facing away from the screen.

Constant Value: "android.hardware.camera" 

### FEATURE_CAMERA_ANY

Added in [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_ANY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has at least one camera pointing in some direction, or can support an external or a `[virtual](https://developer.android.com/reference/android/companion/virtual/VirtualDevice)` camera being connected to it.

Constant Value: "android.hardware.camera.any" 

### FEATURE_CAMERA_AR

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_AR

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[MOTION_TRACKING](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MOTION_TRACKING)` capability level.

Constant Value: "android.hardware.camera.ar" 

### FEATURE_CAMERA_AUTOFOCUS

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_AUTOFOCUS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's camera supports auto-focus.

Constant Value: "android.hardware.camera.autofocus" 

### FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[manual post-processing](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_POST_PROCESSING)` capability level.

Constant Value: "android.hardware.camera.capability.manual_post_processing" 

### FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[manual sensor](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_MANUAL_SENSOR)` capability level.

Constant Value: "android.hardware.camera.capability.manual_sensor" 

### FEATURE_CAMERA_CAPABILITY_RAW

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_CAPABILITY_RAW

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[RAW](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_RAW)` capability level.

Constant Value: "android.hardware.camera.capability.raw" 

### FEATURE_CAMERA_CONCURRENT

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_CONCURRENT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's main front and back cameras can stream concurrently as described in `[CameraManager.getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds\(\))`. 

While `[CameraManager.getConcurrentCameraIds()](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getConcurrentCameraIds\(\))` and associated APIs are only available on API level 30 or newer, this feature flag may be advertised by devices on API levels below 30. If present on such a device, the same guarantees hold: The main front and main back camera can be used at the same time, with guaranteed stream configurations as defined in the table for concurrent streaming at `[CameraDevice.createCaptureSession(android.hardware.camera2.params.SessionConfiguration)](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#createCaptureSession\(android.hardware.camera2.params.SessionConfiguration\))`. 

Constant Value: "android.hardware.camera.concurrent" 

### FEATURE_CAMERA_EXTERNAL

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_EXTERNAL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can support having an external camera connected to it. The external camera may not always be connected or available to applications to use.

Constant Value: "android.hardware.camera.external" 

### FEATURE_CAMERA_FLASH

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_FLASH

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's camera supports flash.

Constant Value: "android.hardware.camera.flash" 

### FEATURE_CAMERA_FRONT

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_FRONT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a front facing camera.

Constant Value: "android.hardware.camera.front" 

### FEATURE_CAMERA_LEVEL_FULL

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CAMERA_LEVEL_FULL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: At least one of the cameras on the device supports the `[full hardware](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#INFO_SUPPORTED_HARDWARE_LEVEL)` capability level.

Constant Value: "android.hardware.camera.level.full" 

### FEATURE_CANT_SAVE_STATE

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CANT_SAVE_STATE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports the `[R.attr.cantSaveState](https://developer.android.com/reference/android/R.attr#cantSaveState)` API.

Constant Value: "android.software.cant_save_state" 

### FEATURE_COMPANION_DEVICE_SETUP

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_COMPANION_DEVICE_SETUP

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports `[associating](https://developer.android.com/reference/android/companion/CompanionDeviceManager#associate\(android.companion.AssociationRequest,%20android.companion.CompanionDeviceManager.Callback,%20android.os.Handler\))` with devices via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.

Constant Value: "android.software.companion_device_setup" 

### FEATURE_CONNECTION_SERVICE

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CONNECTION_SERVICE

**This constant was deprecated in API level 33.**  
use `[FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)` instead. 

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The Connection Service API is enabled on the device.

Constant Value: "android.software.connectionservice" 

### FEATURE_CONSUMER_IR

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CONSUMER_IR

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with consumer IR devices.

Constant Value: "android.hardware.consumerir" 

### FEATURE_CONTROLS

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CONTROLS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports a system interface for the user to select and bind device control services provided by applications.

**See also:**

  * `[ControlsProviderService](https://developer.android.com/reference/android/service/controls/ControlsProviderService)`



Constant Value: "android.software.controls" 

### FEATURE_CREDENTIALS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_CREDENTIALS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports retrieval of user credentials, via integration with credential providers.

Constant Value: "android.software.credentials" 

### FEATURE_DEVICE_ADMIN

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_DEVICE_ADMIN

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports device policy enforcement via device admins.

Constant Value: "android.software.device_admin" 

### FEATURE_DEVICE_ID_ATTESTATION

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_DEVICE_ID_ATTESTATION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a KeyMint (or Keymaster) implementation that supports device ID attestation. See [the public documentation](https://source.android.com/docs/security/features/keystore/attestation#id-attestation) for more information about device ID attestation.

**See also:**

  * `[DevicePolicyManager.isDeviceIdAttestationSupported](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#isDeviceIdAttestationSupported\(\))`



Constant Value: "android.software.device_id_attestation" 

### FEATURE_DEVICE_LOCK

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_DEVICE_LOCK

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports locking (for example, by a financing provider in case of a missed payment).

Constant Value: "android.software.device_lock" 

### FEATURE_EMBEDDED

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_EMBEDDED

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device for IoT and may not have an UI. An embedded device is defined as a full stack Android device with or without a display and no user-installable apps.

Constant Value: "android.hardware.type.embedded" 

### FEATURE_ETHERNET

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_ETHERNET

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This device supports ethernet.

Constant Value: "android.hardware.ethernet" 

### FEATURE_EXPANDED_PICTURE_IN_PICTURE

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_EXPANDED_PICTURE_IN_PICTURE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports expanded picture-in-picture multi-window mode.

**See also:**

  * `[PictureInPictureParams.Builder.setExpandedAspectRatio(Rational)](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder#setExpandedAspectRatio\(android.util.Rational\))`



Constant Value: "android.software.expanded_picture_in_picture" 

### FEATURE_FACE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FACE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to perform face authentication.

Constant Value: "android.hardware.biometrics.face" 

### FEATURE_FAKETOUCH

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FAKETOUCH

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events. For instance, the device might use a mouse or remote control to drive a cursor, and emulate basic touch pointer events like down, up, drag, etc. All devices that support android.hardware.touchscreen or a sub-feature are presumed to also support faketouch.

Constant Value: "android.hardware.faketouch" 

### FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT

Added in [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events that supports distinct tracking of two or more fingers. This is an extension of `[FEATURE_FAKETOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)` for input devices with this capability. Note that unlike a distinct multitouch screen as defined by `[FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT)`, these kinds of input devices will not actually provide full two-finger gestures since the input is being transformed to cursor movement on the screen. That is, single finger gestures will move a cursor; two-finger swipes will result in single-finger touch events; other two-finger gestures will result in the corresponding two-finger touch event.

Constant Value: "android.hardware.faketouch.multitouch.distinct" 

### FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND

Added in [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FAKETOUCH_MULTITOUCH_JAZZHAND

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device does not have a touch screen, but does support touch emulation for basic events that supports tracking a hand of fingers (5 or more fingers) fully independently. This is an extension of `[FEATURE_FAKETOUCH](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH)` for input devices with this capability. Note that unlike a multitouch screen as defined by `[FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND)`, not all two finger gestures can be detected due to the limitations described for `[FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FAKETOUCH_MULTITOUCH_DISTINCT)`.

Constant Value: "android.hardware.faketouch.multitouch.jazzhand" 

### FEATURE_FINGERPRINT

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FINGERPRINT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to detect a fingerprint.

Constant Value: "android.hardware.fingerprint" 

### FEATURE_FREEFORM_WINDOW_MANAGEMENT

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_FREEFORM_WINDOW_MANAGEMENT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports freeform window management. Windows have title bars and can be moved and resized.

Constant Value: "android.software.freeform_window_management" 

### FEATURE_GAMEPAD

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_GAMEPAD

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has all of the inputs necessary to be considered a compatible game controller, or includes a compatible game controller in the box.

Constant Value: "android.hardware.gamepad" 

### FEATURE_HARDWARE_KEYSTORE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_HARDWARE_KEYSTORE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device implements the Android Keystore backed by an isolated execution environment. The version indicates which features are implemented in the isolated execution environment: 

  * 500: Hardware support for ML-DSA signature generation. 
  * 400: Inclusion of module information (via tag MODULE_HASH) in the attestation record. 
  * 300: Ability to include a second IMEI in the ID attestation record, see `[DevicePolicyManager.ID_TYPE_IMEI](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI)`. 
  * 200: Hardware support for Curve 25519 (including both Ed25519 signature generation and X25519 key agreement). 
  * 100: Hardware support for ECDH (see `[KeyAgreement](https://developer.android.com/reference/javax/crypto/KeyAgreement)`) and support for app-generated attestation keys (see `[android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias\(java.lang.String\))`). 
  * 41: Hardware enforcement of device-unlocked keys (see `[KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired\(boolean\))`). 
  * 40: Support for wrapped key import (see `[WrappedKeyEntry](https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)`), optional support for ID attestation (see `[KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setDevicePropertiesAttestationIncluded\(boolean\))`), attestation (see `[KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestationChallenge\(byte\[\]\))`), AES, HMAC, ECDSA and RSA support where the secret or private key never leaves secure hardware, and support for requiring user authentication before a key can be used. 

This feature version is guaranteed to be set for all devices launching with Android 12 and may be set on devices launching with an earlier version. If the feature version is set, it will at least have the value 40. If it's not set the device may have a version of hardware-backed keystore but it may not support all features listed above. 

Constant Value: "android.hardware.hardware_keystore" 

### FEATURE_HIFI_SENSORS

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_HIFI_SENSORS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports high fidelity sensor processing capabilities.

Constant Value: "android.hardware.sensor.hifi_sensors" 

### FEATURE_HOME_SCREEN

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_HOME_SCREEN

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports a home screen that is replaceable by third party applications.

Constant Value: "android.software.home_screen" 

### FEATURE_IDENTITY_CREDENTIAL_HARDWARE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_IDENTITY_CREDENTIAL_HARDWARE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device supports `[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)` implemented in secure hardware at the given feature version. 

Known feature versions include: 

  * `202009`: corresponds to the features included in the Identity Credential API shipped in Android 11. 
  * `202101`: corresponds to the features included in the Identity Credential API shipped in Android 12. 
  * `202201`: corresponds to the features included in the Identity Credential API shipped in Android 13. 



Constant Value: "android.hardware.identity_credential" 

### FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device supports `[IdentityCredentialStore](https://developer.android.com/reference/android/security/identity/IdentityCredentialStore)` implemented in secure hardware with direct access at the given feature version. See `[FEATURE_IDENTITY_CREDENTIAL_HARDWARE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE)` for known feature versions.

Constant Value: "android.hardware.identity_credential_direct_access" 

### FEATURE_INPUT_METHODS

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_INPUT_METHODS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports adding new input methods implemented with the `[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)` API.

Constant Value: "android.software.input_methods" 

### FEATURE_IPSEC_TUNNELS

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_IPSEC_TUNNELS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has the requisite kernel support for multinetworking-capable IPsec tunnels. 

This feature implies that the device supports XFRM Interfaces (CONFIG_XFRM_INTERFACE), or VTIs with kernel patches allowing updates of output/set mark via UPDSA.

Constant Value: "android.software.ipsec_tunnels" 

### FEATURE_IPSEC_TUNNEL_MIGRATION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_IPSEC_TUNNEL_MIGRATION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has the requisite kernel support for migrating IPsec tunnels to new source/destination addresses. 

This feature implies that the device supports XFRM Migration (CONFIG_XFRM_MIGRATE) and has the kernel fixes to support cross-address-family IPsec tunnel migration

Constant Value: "android.software.ipsec_tunnel_migration" 

### FEATURE_IRIS

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_IRIS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has biometric hardware to perform iris authentication.

Constant Value: "android.hardware.biometrics.iris" 

### FEATURE_KEYSTORE_APP_ATTEST_KEY

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_KEYSTORE_APP_ATTEST_KEY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can create application-specific attestation keys. See `[KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias\(java.lang.String\))`.

Constant Value: "android.hardware.keystore.app_attest_key" 

### FEATURE_KEYSTORE_LIMITED_USE_KEY

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_KEYSTORE_LIMITED_USE_KEY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can enforce limited use key in hardware with any max usage count (including count equals to 1).

Constant Value: "android.hardware.keystore.limited_use_key" 

### FEATURE_KEYSTORE_SINGLE_USE_KEY

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_KEYSTORE_SINGLE_USE_KEY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Keystore implementation that can only enforce limited use key in hardware with max usage count equals to 1.

Constant Value: "android.hardware.keystore.single_use_key" 

### FEATURE_LEANBACK

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LEANBACK

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports leanback UI. This is typically used in a living room television experience, but is a software feature unlike `[FEATURE_TELEVISION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEVISION)`. Devices running with this feature will use resources associated with the "television" UI mode.

Constant Value: "android.software.leanback" 

### FEATURE_LEANBACK_ONLY

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LEANBACK_ONLY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports only leanback UI. Only applications designed for this experience should be run, though this is not enforced by the system.

Constant Value: "android.software.leanback_only" 

### FEATURE_LIVE_TV

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LIVE_TV

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports live TV and can display contents from TV inputs implemented with the `[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)` API.

Constant Value: "android.software.live_tv" 

### FEATURE_LIVE_WALLPAPER

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LIVE_WALLPAPER

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports live wallpapers.

Constant Value: "android.software.live_wallpaper" 

### FEATURE_LOCATION

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LOCATION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports one or more methods of reporting current location.

Constant Value: "android.hardware.location" 

### FEATURE_LOCATION_GPS

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LOCATION_GPS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a Global Positioning System receiver and can report precise location.

Constant Value: "android.hardware.location.gps" 

### FEATURE_LOCATION_NETWORK

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_LOCATION_NETWORK

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can report location with coarse accuracy using a network-based geolocation system.

Constant Value: "android.hardware.location.network" 

### FEATURE_MANAGED_USERS

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_MANAGED_USERS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports creating secondary users and managed profiles via `[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)`.

Constant Value: "android.software.managed_users" 

### FEATURE_MICROPHONE

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_MICROPHONE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can record audio via a microphone.

Constant Value: "android.hardware.microphone" 

### FEATURE_MIDI

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_MIDI

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a full implementation of the android.media.midi.* APIs.

Constant Value: "android.software.midi" 

### FEATURE_NEURAL_PROCESSING_UNIT

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NEURAL_PROCESSING_UNIT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This device has a NPU (Neural Processing Unit) or similar hardware for accelerating AI workloads.

Constant Value: "android.hardware.npu" 

### FEATURE_NFC

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device can communicate using Near-Field Communications (NFC), acting as a reader.

Constant Value: "android.hardware.nfc" 

### FEATURE_NFC_BEAM

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC_BEAM

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The Beam API is enabled on the device.

Constant Value: "android.sofware.nfc.beam" 

### FEATURE_NFC_HOST_CARD_EMULATION

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC_HOST_CARD_EMULATION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports host- based NFC card emulation.

Constant Value: "android.hardware.nfc.hce" 

### FEATURE_NFC_HOST_CARD_EMULATION_NFCF

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC_HOST_CARD_EMULATION_NFCF

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports host- based NFC-F card emulation.

Constant Value: "android.hardware.nfc.hcef" 

### FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports eSE- based NFC card emulation.

Constant Value: "android.hardware.nfc.ese" 

### FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports uicc- based NFC card emulation.

Constant Value: "android.hardware.nfc.uicc" 

### FEATURE_OPENGLES_DEQP_LEVEL

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_OPENGLES_DEQP_LEVEL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the feature version specifies a date such that the device is known to pass the OpenGLES dEQP test suite associated with that date. The date is encoded as follows: 

  * Year in bits 31-16
  * Month in bits 15-8
  * Day in bits 7-0



Example: 2021-03-01 is encoded as 0x07E50301, and would indicate that the device passes the OpenGL ES dEQP test suite version that was current on 2021-03-01.

Constant Value: "android.software.opengles.deqp.level" 

### FEATURE_OPENGLES_EXTENSION_PACK

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_OPENGLES_EXTENSION_PACK

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports the OpenGL ES [ Android Extension Pack](http://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt).

Constant Value: "android.hardware.opengles.aep" 

### FEATURE_PC

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_PC

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to be primarily used with keyboard, mouse or touchpad. This includes traditional desktop computers, laptops and variants such as convertibles or detachables. Due to the larger screen, the device will most likely use the `[FEATURE_FREEFORM_WINDOW_MANAGEMENT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FREEFORM_WINDOW_MANAGEMENT)` feature as well.

Constant Value: "android.hardware.type.pc" 

### FEATURE_PICTURE_IN_PICTURE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_PICTURE_IN_PICTURE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports picture-in-picture multi-window mode.

Constant Value: "android.software.picture_in_picture" 

### FEATURE_PRINTING

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_PRINTING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports printing.

Constant Value: "android.software.print" 

### FEATURE_RAM_LOW

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_RAM_LOW

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's `[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice\(\))` method returns true.

Constant Value: "android.hardware.ram.low" 

### FEATURE_RAM_NORMAL

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_RAM_NORMAL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's `[ActivityManager.isLowRamDevice()](https://developer.android.com/reference/android/app/ActivityManager#isLowRamDevice\(\))` method returns false.

Constant Value: "android.hardware.ram.normal" 

### FEATURE_SCREEN_LANDSCAPE

Added in [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SCREEN_LANDSCAPE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports landscape orientation screens. For backwards compatibility, you can assume that if neither this nor `[FEATURE_SCREEN_PORTRAIT](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_PORTRAIT)` is set then the device supports both portrait and landscape.

Constant Value: "android.hardware.screen.landscape" 

### FEATURE_SCREEN_PORTRAIT

Added in [API level 13](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SCREEN_PORTRAIT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports portrait orientation screens. For backwards compatibility, you can assume that if neither this nor `[FEATURE_SCREEN_LANDSCAPE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SCREEN_LANDSCAPE)` is set then the device supports both portrait and landscape.

Constant Value: "android.hardware.screen.portrait" 

### FEATURE_SECURELY_REMOVES_USERS

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SECURELY_REMOVES_USERS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports secure removal of users. When a user is deleted the data associated with that user is securely deleted and no longer available.

Constant Value: "android.software.securely_removes_users" 

### FEATURE_SECURE_LOCK_SCREEN

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SECURE_LOCK_SCREEN

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a secure implementation of keyguard, meaning the device supports PIN, pattern and password as defined in Android CDD

Constant Value: "android.software.secure_lock_screen" 

### FEATURE_SECURITY_MODEL_COMPATIBLE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SECURITY_MODEL_COMPATIBLE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is compatible with Android's security model. 

See sections 2 and 9 in the [Android CDD](https://source.android.com/compatibility/android-cdd) for more details.

Constant Value: "android.hardware.security.model.compatible" 

### FEATURE_SENSOR_ACCELEROMETER

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_ACCELEROMETER

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an accelerometer.

Constant Value: "android.hardware.sensor.accelerometer" 

### FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a limited axes accelerometer.

Constant Value: "android.hardware.sensor.accelerometer_limited_axes" 

### FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an uncalibrated limited axes accelerometer.

Constant Value: "android.hardware.sensor.accelerometer_limited_axes_uncalibrated" 

### FEATURE_SENSOR_AMBIENT_TEMPERATURE

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_AMBIENT_TEMPERATURE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an ambient temperature sensor.

Constant Value: "android.hardware.sensor.ambient_temperature" 

### FEATURE_SENSOR_BAROMETER

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_BAROMETER

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a barometer (air pressure sensor.)

Constant Value: "android.hardware.sensor.barometer" 

### FEATURE_SENSOR_COMPASS

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_COMPASS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a magnetometer (compass).

Constant Value: "android.hardware.sensor.compass" 

### FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_DYNAMIC_HEAD_TRACKER

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports exposing head tracker sensors from peripheral devices via the dynamic sensors API.

Constant Value: "android.hardware.sensor.dynamic.head_tracker" 

### FEATURE_SENSOR_GYROSCOPE

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_GYROSCOPE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a gyroscope.

Constant Value: "android.hardware.sensor.gyroscope" 

### FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a limited axes gyroscope.

Constant Value: "android.hardware.sensor.gyroscope_limited_axes" 

### FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes an uncalibrated limited axes gyroscope.

Constant Value: "android.hardware.sensor.gyroscope_limited_axes_uncalibrated" 

### FEATURE_SENSOR_HEADING

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_HEADING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a heading sensor.

Constant Value: "android.hardware.sensor.heading" 

### FEATURE_SENSOR_HEART_RATE

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_HEART_RATE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a heart rate monitor.

Constant Value: "android.hardware.sensor.heartrate" 

### FEATURE_SENSOR_HEART_RATE_ECG

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_HEART_RATE_ECG

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The heart rate sensor on this device is an Electrocardiogram.

Constant Value: "android.hardware.sensor.heartrate.ecg" 

### FEATURE_SENSOR_HINGE_ANGLE

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_HINGE_ANGLE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hinge angle sensor.

Constant Value: "android.hardware.sensor.hinge_angle" 

### FEATURE_SENSOR_LIGHT

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_LIGHT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a light sensor.

Constant Value: "android.hardware.sensor.light" 

### FEATURE_SENSOR_PROXIMITY

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_PROXIMITY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a proximity sensor.

Constant Value: "android.hardware.sensor.proximity" 

### FEATURE_SENSOR_RELATIVE_HUMIDITY

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_RELATIVE_HUMIDITY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a relative humidity sensor.

Constant Value: "android.hardware.sensor.relative_humidity" 

### FEATURE_SENSOR_STEP_COUNTER

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_STEP_COUNTER

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hardware step counter.

Constant Value: "android.hardware.sensor.stepcounter" 

### FEATURE_SENSOR_STEP_DETECTOR

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SENSOR_STEP_DETECTOR

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device includes a hardware step detector.

Constant Value: "android.hardware.sensor.stepdetector" 

### FEATURE_SE_OMAPI_ESE

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SE_OMAPI_ESE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable eSE-based secure elements.

Constant Value: "android.hardware.se.omapi.ese" 

### FEATURE_SE_OMAPI_SD

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SE_OMAPI_SD

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable SD-based secure elements.

Constant Value: "android.hardware.se.omapi.sd" 

### FEATURE_SE_OMAPI_UICC

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SE_OMAPI_UICC

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Open Mobile API capable UICC-based secure elements.

Constant Value: "android.hardware.se.omapi.uicc" 

### FEATURE_SIP

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SIP

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The SIP API is enabled on the device.

Constant Value: "android.software.sip" 

### FEATURE_SIP_VOIP

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_SIP_VOIP

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports SIP-based VOIP.

Constant Value: "android.software.sip.voip" 

### FEATURE_STRONGBOX_KEYSTORE

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_STRONGBOX_KEYSTORE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`, `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`, and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the device implements the Android Keystore backed by a dedicated secure processor referred to as [ StrongBox](https://source.android.com/security/best-practices/hardware#strongbox-keymaster). If this feature has a version, the version number indicates which features are implemented in StrongBox: 

  * 400: Inclusion of module information (via tag MODULE_HASH) in the attestation record. 
  * 300: Ability to include a second IMEI in the ID attestation record, see `[DevicePolicyManager.ID_TYPE_IMEI](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#ID_TYPE_IMEI)`. 
  * 200: No new features for StrongBox (the Android Keystore environment backed by an isolated execution environment has gained support for Curve 25519 in this version, but the implementation backed by a dedicated secure processor is not expected to implement it). 
  * 100: Hardware support for ECDH (see `[KeyAgreement](https://developer.android.com/reference/javax/crypto/KeyAgreement)`) and support for app-generated attestation keys (see `[android.security.keystore.KeyGenParameterSpec.Builder.setAttestKeyAlias(String)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestKeyAlias\(java.lang.String\))`). 
  * 41: Hardware enforcement of device-unlocked keys (see `[KeyGenParameterSpec.Builder.setUnlockedDeviceRequired(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setUnlockedDeviceRequired\(boolean\))`). 
  * 40: Support for wrapped key import (see `[WrappedKeyEntry](https://developer.android.com/reference/android/security/keystore/WrappedKeyEntry)`), optional support for ID attestation (see `[KeyGenParameterSpec.Builder.setDevicePropertiesAttestationIncluded(boolean)](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setDevicePropertiesAttestationIncluded\(boolean\))`), attestation (see `[KeyGenParameterSpec.Builder.setAttestationChallenge(byte[])](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder#setAttestationChallenge\(byte\[\]\))`), AES, HMAC, ECDSA and RSA support where the secret or private key never leaves secure hardware, and support for requiring user authentication before a key can be used. 

If a device has StrongBox, this feature version number is guaranteed to be set for all devices launching with Android 12 and may be set on devices launching with an earlier version. If the feature version is set, it will at least have the value 40. If it's not set the device may have StrongBox but it may not support all features listed above. 

Constant Value: "android.hardware.strongbox_keystore" 

### FEATURE_TELECOM

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELECOM

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telecom Service APIs.

Constant Value: "android.software.telecom" 

### FEATURE_TELEPHONY

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a telephony radio with data communication support.

Constant Value: "android.hardware.telephony" 

### FEATURE_TELEPHONY_CALLING

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_CALLING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for calling service. 

This feature should only be defined if `[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)`, `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)`, and `[FEATURE_TELECOM](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)` have been defined.

Constant Value: "android.hardware.telephony.calling" 

### FEATURE_TELEPHONY_CDMA

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_CDMA

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a CDMA telephony stack. 

This feature should only be defined if `[FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)` has been defined.

Constant Value: "android.hardware.telephony.cdma" 

### FEATURE_TELEPHONY_DATA

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_DATA

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for data service. 

This feature should only be defined if both `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)` and `[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)` have been defined.

Constant Value: "android.hardware.telephony.data" 

### FEATURE_TELEPHONY_EUICC

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_EUICC

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports embedded subscriptions on eUICCs. This feature should only be defined if `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)` has been defined.

Constant Value: "android.hardware.telephony.euicc" 

### FEATURE_TELEPHONY_EUICC_MEP

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_EUICC_MEP

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports multiple enabled profiles on eUICCs. 

Devices declaring this feature must have an implementation of the `[UiccCardInfo.getPorts](https://developer.android.com/reference/android/telephony/UiccCardInfo#getPorts\(\))`, `[UiccCardInfo.isMultipleEnabledProfilesSupported](https://developer.android.com/reference/android/telephony/UiccCardInfo#isMultipleEnabledProfilesSupported\(\))` and `[(with portIndex)](https://developer.android.com/reference/android/telephony/euicc/EuiccManager#switchToSubscription\(int,%20android.app.PendingIntent\))`. This feature should only be defined if `[FEATURE_TELEPHONY_EUICC](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC)` have been defined.

Constant Value: "android.hardware.telephony.euicc.mep" 

### FEATURE_TELEPHONY_GSM

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_GSM

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a GSM telephony stack. 

This feature should only be defined if `[FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)` has been defined.

Constant Value: "android.hardware.telephony.gsm" 

### FEATURE_TELEPHONY_IMS

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_IMS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports attaching to IMS implementations using the ImsService API in telephony. 

This feature should only be defined if `[FEATURE_TELEPHONY_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_DATA)` has been defined.

Constant Value: "android.hardware.telephony.ims" 

### FEATURE_TELEPHONY_MBMS

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_MBMS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports cell-broadcast reception using the MBMS APIs. 

This feature should only be defined if both `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)` and `[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)` have been defined.

Constant Value: "android.hardware.telephony.mbms" 

### FEATURE_TELEPHONY_MESSAGING

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_MESSAGING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for SMS and MMS. 

This feature should only be defined if both `[FEATURE_TELEPHONY_SUBSCRIPTION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)` and `[FEATURE_TELEPHONY_RADIO_ACCESS](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)` have been defined.

Constant Value: "android.hardware.telephony.messaging" 

### FEATURE_TELEPHONY_RADIO_ACCESS

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_RADIO_ACCESS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for the radio access. 

This feature should only be defined if `[FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)` has been defined.

Constant Value: "android.hardware.telephony.radio.access" 

### FEATURE_TELEPHONY_SUBSCRIPTION

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEPHONY_SUBSCRIPTION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Telephony APIs for the subscription. 

This feature should only be defined if `[FEATURE_TELEPHONY](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)` has been defined.

Constant Value: "android.hardware.telephony.subscription" 

### FEATURE_TELEVISION

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TELEVISION

**This constant was deprecated in API level 21.**  
use `[FEATURE_LEANBACK](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)` instead. 

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to showing UI on a television. Television here is defined to be a typical living room television experience: displayed on a big screen, where the user is sitting far away from it, and the dominant form of input will be something like a DPAD, not through touch or mouse.

Constant Value: "android.hardware.type.television" 

### FEATURE_THREAD_NETWORK

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_THREAD_NETWORK

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via [Thread](https://www.threadgroup.org) networking protocol.

Constant Value: "android.hardware.thread_network" 

### FEATURE_TOUCHSCREEN

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TOUCHSCREEN

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's display has a touch screen.

Constant Value: "android.hardware.touchscreen" 

### FEATURE_TOUCHSCREEN_MULTITOUCH

Added in [API level 7](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TOUCHSCREEN_MULTITOUCH

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen supports multitouch sufficient for basic two-finger gesture detection.

Constant Value: "android.hardware.touchscreen.multitouch" 

### FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen is capable of tracking two or more fingers fully independently.

Constant Value: "android.hardware.touchscreen.multitouch.distinct" 

### FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_TOUCHSCREEN_MULTITOUCH_JAZZHAND

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device's touch screen is capable of tracking a full hand of fingers fully independently -- that is, 5 or more simultaneous independent pointers.

Constant Value: "android.hardware.touchscreen.multitouch.jazzhand" 

### FEATURE_USB_ACCESSORY

Added in [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_USB_ACCESSORY

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports connecting to USB accessories.

Constant Value: "android.hardware.usb.accessory" 

### FEATURE_USB_HOST

Added in [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_USB_HOST

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports connecting to USB devices as the USB host.

Constant Value: "android.hardware.usb.host" 

### FEATURE_UWB

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_UWB

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device is capable of communicating with other devices via ultra wideband.

Constant Value: "android.hardware.uwb" 

### FEATURE_VERIFIED_BOOT

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VERIFIED_BOOT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports verified boot.

Constant Value: "android.software.verified_boot" 

### FEATURE_VR_HEADTRACKING

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VR_HEADTRACKING

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device implements headtracking suitable for a VR device.

Constant Value: "android.hardware.vr.headtracking" 

### FEATURE_VR_MODE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VR_MODE

**This constant was deprecated in API level 28.**  
use `[FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)` instead. 

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device implements an optimized mode for virtual reality (VR) applications that handles stereoscopic rendering of notifications, and disables most monocular system UI components while a VR application has user focus. Devices declaring this feature must include an application implementing a `[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)` that can be targeted by VR applications via `[Activity.setVrModeEnabled(boolean, ComponentName)](https://developer.android.com/reference/android/app/Activity#setVrModeEnabled\(boolean,%20android.content.ComponentName\))`.

Constant Value: "android.software.vr.mode" 

### FEATURE_VR_MODE_HIGH_PERFORMANCE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VR_MODE_HIGH_PERFORMANCE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device implements an optimized mode for virtual reality (VR) applications that handles stereoscopic rendering of notifications, disables most monocular system UI components while a VR application has user focus and meets extra CDD requirements to provide a high-quality VR experience. Devices declaring this feature must include an application implementing a `[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)` that can be targeted by VR applications via `[Activity.setVrModeEnabled(boolean, ComponentName)](https://developer.android.com/reference/android/app/Activity#setVrModeEnabled\(boolean,%20android.content.ComponentName\))`. and must meet CDD requirements to provide a high-quality VR experience.

Constant Value: "android.hardware.vr.high_performance" 

### FEATURE_VULKAN_DEQP_LEVEL

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VULKAN_DEQP_LEVEL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the feature version specifies a date such that the device is known to pass the Vulkan dEQP test suite associated with that date. The date is encoded as follows: 

  * Year in bits 31-16
  * Month in bits 15-8
  * Day in bits 7-0



Example: 2019-03-01 is encoded as 0x07E30301, and would indicate that the device passes the Vulkan dEQP test suite version that was current on 2019-03-01.

Constant Value: "android.software.vulkan.deqp.level" 

### FEATURE_VULKAN_HARDWARE_COMPUTE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VULKAN_HARDWARE_COMPUTE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the Vulkan native API will enumerate at least one `VkPhysicalDevice`, and the feature version will indicate what level of optional compute features that device supports beyond the Vulkan 1.0 requirements. 

Compute level 0 indicates: 

  * The `VK_KHR_variable_pointers` extension and `VkPhysicalDeviceVariablePointerFeaturesKHR::variablePointers` feature are supported.
  * `VkPhysicalDeviceLimits::maxPerStageDescriptorStorageBuffers` is at least 16.



Constant Value: "android.hardware.vulkan.compute" 

### FEATURE_VULKAN_HARDWARE_LEVEL

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VULKAN_HARDWARE_LEVEL

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the Vulkan native API will enumerate at least one `VkPhysicalDevice`, and the feature version will indicate what level of optional hardware features limits it supports. 

Level 0 includes the base Vulkan requirements as well as: 

  * `VkPhysicalDeviceFeatures::textureCompressionETC2`



Level 1 additionally includes: 

  * `VkPhysicalDeviceFeatures::fullDrawIndexUint32`
  * `VkPhysicalDeviceFeatures::imageCubeArray`
  * `VkPhysicalDeviceFeatures::independentBlend`
  * `VkPhysicalDeviceFeatures::geometryShader`
  * `VkPhysicalDeviceFeatures::tessellationShader`
  * `VkPhysicalDeviceFeatures::sampleRateShading`
  * `VkPhysicalDeviceFeatures::textureCompressionASTC_LDR`
  * `VkPhysicalDeviceFeatures::fragmentStoresAndAtomics`
  * `VkPhysicalDeviceFeatures::shaderImageGatherExtended`
  * `VkPhysicalDeviceFeatures::shaderUniformBufferArrayDynamicIndexing`
  * `VkPhysicalDeviceFeatures::shaderSampledImageArrayDynamicIndexing`



Constant Value: "android.hardware.vulkan.level" 

### FEATURE_VULKAN_HARDWARE_VERSION

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_VULKAN_HARDWARE_VERSION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))`: If this feature is supported, the Vulkan implementation on this device is hardware accelerated, and the feature version will indicate the highest `VkPhysicalDeviceProperties::apiVersion` supported by the physical devices that support the hardware level indicated by `[FEATURE_VULKAN_HARDWARE_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL)`. The feature version uses the same encoding as Vulkan version numbers: 

  * Major version number in bits 31-22
  * Minor version number in bits 21-12
  * Patch version number in bits 11-0

A version of 1.1.0 or higher also indicates: 
  * The `VK_ANDROID_external_memory_android_hardware_buffer` extension is supported.
  * `SYNC_FD` external semaphore and fence handles are supported.
  * `VkPhysicalDeviceSamplerYcbcrConversionFeatures::samplerYcbcrConversion` is supported.

A subset of devices that support Vulkan 1.1 do so via software emulation. For more information, see [Vulkan Design Guidelines](https://developer.android.com/ndk/guides/graphics/design-notes). 

Constant Value: "android.hardware.vulkan.version" 

### FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports showing location-based suggestions for wallet cards provided by the default payment app.

Constant Value: "android.software.wallet_location_based_suggestions" 

### FEATURE_WATCH

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WATCH

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: This is a device dedicated to showing UI on a watch. A watch here is defined to be a device worn on the body, perhaps on the wrist. The user is very close when interacting with the device.

Constant Value: "android.hardware.type.watch" 

### FEATURE_WEBVIEW

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WEBVIEW

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device has a full implementation of the android.webkit.* APIs. Devices lacking this feature will not have a functioning WebView implementation.

Constant Value: "android.software.webview" 

### FEATURE_WIFI

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WIFI

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports WiFi (802.11) networking.

Constant Value: "android.hardware.wifi" 

### FEATURE_WIFI_AWARE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WIFI_AWARE

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Aware.

Constant Value: "android.hardware.wifi.aware" 

### FEATURE_WIFI_DIRECT

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WIFI_DIRECT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Direct networking.

Constant Value: "android.hardware.wifi.direct" 

### FEATURE_WIFI_PASSPOINT

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WIFI_PASSPOINT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi Passpoint and all Passpoint related APIs in `[WifiManager](https://developer.android.com/reference/android/net/wifi/WifiManager)` are supported. Refer to `[WifiManager.addOrUpdatePasspointConfiguration](https://developer.android.com/reference/android/net/wifi/WifiManager#addOrUpdatePasspointConfiguration\(android.net.wifi.hotspot2.PasspointConfiguration\))` for more info.

Constant Value: "android.hardware.wifi.passpoint" 

### FEATURE_WIFI_RTT

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WIFI_RTT

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports Wi-Fi RTT (IEEE 802.11mc).

Constant Value: "android.hardware.wifi.rtt" 

### FEATURE_WINDOW_MAGNIFICATION

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FEATURE_WINDOW_MAGNIFICATION

Feature for `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))` and `[hasSystemFeature(String)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\))`: The device supports window magnification.

**See also:**

  * `[MagnificationConfig.MAGNIFICATION_MODE_WINDOW](https://developer.android.com/reference/android/accessibilityservice/MagnificationConfig#MAGNIFICATION_MODE_WINDOW)`



Constant Value: "android.software.window_magnification" 

### FLAG_PERMISSION_WHITELIST_INSTALLER

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int FLAG_PERMISSION_WHITELIST_INSTALLER

Permission whitelist flag: permissions whitelisted by the installer. Permissions can also be whitelisted by the system, on upgrade, or on role grant. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Constant Value: 2 (0x00000002) 

### FLAG_PERMISSION_WHITELIST_SYSTEM

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int FLAG_PERMISSION_WHITELIST_SYSTEM

Permission whitelist flag: permissions whitelisted by the system. Permissions can also be whitelisted by the installer, on upgrade, or on role grant. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Constant Value: 1 (0x00000001) 

### FLAG_PERMISSION_WHITELIST_UPGRADE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int FLAG_PERMISSION_WHITELIST_UPGRADE

Permission whitelist flag: permissions whitelisted by the system when upgrading from an OS version where the permission was not restricted to an OS version where the permission is restricted. Permissions can also be whitelisted by the installer, the system, or on role grant. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Constant Value: 4 (0x00000004) 

### GET_ACTIVITIES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_ACTIVITIES

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about activities in the package in `[PackageInfo.activities](https://developer.android.com/reference/android/content/pm/PackageInfo#activities)`.

Constant Value: 1 (0x00000001) 

### GET_APP_LOCK_INFO

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final long GET_APP_LOCK_INFO

`[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)`, `[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)`, and `[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` flag: return the `[ApplicationInfo.isAppLockSupported](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockSupported)` and `[ApplicationInfo.isAppLockEnabled](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockEnabled)` associated with an application. 

The caller should have the `[Manifest.permission.LOCK_APPS](https://developer.android.com/reference/android/Manifest.permission#LOCK_APPS)` permission, or a `[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` will be thrown. This flag cannot be used with `[GET_ATTRIBUTIONS](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS)`, if the caller wishes to retrieve attributions, they must use `[GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)`.

Constant Value: 34359738368 (0x0000000800000000) 

### GET_ATTRIBUTIONS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_ATTRIBUTIONS

**This constant was deprecated in API level 34.**  
Use `[GET_ATTRIBUTIONS_LONG](https://developer.android.com/reference/android/content/pm/PackageManager#GET_ATTRIBUTIONS_LONG)` to avoid unintended sign extension. Operations with this flag may cause unintended results and potential `[RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException)`. 

Constant Value: -2147483648 (0x80000000) 

### GET_ATTRIBUTIONS_LONG

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final long GET_ATTRIBUTIONS_LONG

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return all attributions declared in the package manifest

Constant Value: 2147483648 (0x0000000080000000) 

### GET_CONFIGURATIONS

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_CONFIGURATIONS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about hardware preferences in `[PackageInfo.configPreferences](https://developer.android.com/reference/android/content/pm/PackageInfo#configPreferences)`, and requested features in `[PackageInfo.reqFeatures](https://developer.android.com/reference/android/content/pm/PackageInfo#reqFeatures)` and `[PackageInfo.featureGroups](https://developer.android.com/reference/android/content/pm/PackageInfo#featureGroups)`.

Constant Value: 16384 (0x00004000) 

### GET_DISABLED_COMPONENTS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_DISABLED_COMPONENTS

**This constant was deprecated in API level 24.**  
replaced with `[MATCH_DISABLED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_COMPONENTS)`

Constant Value: 512 (0x00000200) 

### GET_DISABLED_UNTIL_USED_COMPONENTS

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_DISABLED_UNTIL_USED_COMPONENTS

**This constant was deprecated in API level 24.**  
replaced with `[MATCH_DISABLED_UNTIL_USED_COMPONENTS](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DISABLED_UNTIL_USED_COMPONENTS)`. 

Constant Value: 32768 (0x00008000) 

### GET_GIDS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_GIDS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return the `[group ids](https://developer.android.com/reference/android/content/pm/PackageInfo#gids)` that are associated with an application. This applies for any API returning a PackageInfo class, either directly or nested inside of another.

Constant Value: 256 (0x00000100) 

### GET_INSTRUMENTATION

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_INSTRUMENTATION

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about instrumentation in the package in `[PackageInfo.instrumentation](https://developer.android.com/reference/android/content/pm/PackageInfo#instrumentation)`.

Constant Value: 16 (0x00000010) 

### GET_INTENT_FILTERS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_INTENT_FILTERS

**This constant was deprecated in API level 31.**  
The platform does not support getting `[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)`s for the package. 

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about the intent filters supported by the activity.

Constant Value: 32 (0x00000020) 

### GET_META_DATA

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_META_DATA

`[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)` flag: return the `[ComponentInfo.metaData](https://developer.android.com/reference/android/content/pm/PackageItemInfo#metaData)` data `[Bundle](https://developer.android.com/reference/android/os/Bundle)`s that are associated with a component. This applies for any API returning a ComponentInfo subclass.

Constant Value: 128 (0x00000080) 

### GET_PERMISSIONS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_PERMISSIONS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about permissions in the package in `[PackageInfo.permissions](https://developer.android.com/reference/android/content/pm/PackageInfo#permissions)`.

Constant Value: 4096 (0x00001000) 

### GET_PROVIDERS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_PROVIDERS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about content providers in the package in `[PackageInfo.providers](https://developer.android.com/reference/android/content/pm/PackageInfo#providers)`.

Constant Value: 8 (0x00000008) 

### GET_RECEIVERS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_RECEIVERS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about intent receivers in the package in `[PackageInfo.receivers](https://developer.android.com/reference/android/content/pm/PackageInfo#receivers)`.

Constant Value: 2 (0x00000002) 

### GET_RESOLVED_FILTER

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_RESOLVED_FILTER

`[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` flag: return the IntentFilter that was matched for a particular ResolveInfo in `[ResolveInfo.filter](https://developer.android.com/reference/android/content/pm/ResolveInfo#filter)`.

Constant Value: 64 (0x00000040) 

### GET_SERVICES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_SERVICES

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about services in the package in `[PackageInfo.services](https://developer.android.com/reference/android/content/pm/PackageInfo#services)`.

Constant Value: 4 (0x00000004) 

### GET_SHARED_LIBRARY_FILES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_SHARED_LIBRARY_FILES

`[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` flag: return the `[paths to the shared libraries](https://developer.android.com/reference/android/content/pm/ApplicationInfo#sharedLibraryFiles)` that are associated with an application. This applies for any API returning an ApplicationInfo class, either directly or nested inside of another.

Constant Value: 1024 (0x00000400) 

### GET_SIGNATURES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_SIGNATURES

**This constant was deprecated in API level 28.**  
use `GET_SIGNING_CERTIFICATES` instead 

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return information about the signatures included in the package.

Constant Value: 64 (0x00000040) 

### GET_SIGNING_CERTIFICATES

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_SIGNING_CERTIFICATES

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: return the signing certificates associated with this package. Each entry is a signing certificate that the package has proven it is authorized to use, usually a past signing certificate from which it has rotated.

Constant Value: 134217728 (0x08000000) 

### GET_UNINSTALLED_PACKAGES

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_UNINSTALLED_PACKAGES

**This constant was deprecated in API level 24.**  
replaced with `[MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)`

Constant Value: 8192 (0x00002000) 

### GET_URI_PERMISSION_PATTERNS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int GET_URI_PERMISSION_PATTERNS

`[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` flag: return the `[URI permission patterns](https://developer.android.com/reference/android/content/pm/ProviderInfo#uriPermissionPatterns)` that are associated with a content provider. This applies for any API returning a ProviderInfo class, either directly or nested inside of another.

Constant Value: 2048 (0x00000800) 

### INSTALL_REASON_DEVICE_RESTORE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_REASON_DEVICE_RESTORE

Code indicating that this package was installed as part of restoring from another device.

Constant Value: 2 (0x00000002) 

### INSTALL_REASON_DEVICE_SETUP

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_REASON_DEVICE_SETUP

Code indicating that this package was installed as part of device setup.

Constant Value: 3 (0x00000003) 

### INSTALL_REASON_POLICY

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_REASON_POLICY

Code indicating that this package was installed due to enterprise policy.

Constant Value: 1 (0x00000001) 

### INSTALL_REASON_UNKNOWN

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_REASON_UNKNOWN

Code indicating that the reason for installing this package is unknown.

Constant Value: 0 (0x00000000) 

### INSTALL_REASON_USER

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_REASON_USER

Code indicating that the package installation was initiated by the user.

Constant Value: 4 (0x00000004) 

### INSTALL_SCENARIO_BULK

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_SCENARIO_BULK

Installation scenario indicating a bulk operation with the desired result of a fully optimized application. If the system is busy or resources are scarce the system will perform less work to avoid impacting system health. Examples of bulk installation scenarios might include device restore, background updates of multiple applications, or user-triggered updates for all applications. The decision to use BULK or BULK_SECONDARY should be based on the desired user experience. BULK_SECONDARY operations may take less time to complete but, when they do, will produce less optimized applications. The device state (e.g. memory usage or battery status) should not be considered when making this decision as those factors are taken into account by the Package Manager when acting on the installation scenario.

Constant Value: 2 (0x00000002) 

### INSTALL_SCENARIO_BULK_SECONDARY

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_SCENARIO_BULK_SECONDARY

Installation scenario indicating a bulk operation that prioritizes minimal system health impact over application optimization. The application may undergo additional optimization if the system is idle and system resources are abundant. The more elements of a bulk operation that are marked BULK_SECONDARY, the faster the entire bulk operation will be. See the comments for INSTALL_SCENARIO_BULK for more information.

Constant Value: 3 (0x00000003) 

### INSTALL_SCENARIO_DEFAULT

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_SCENARIO_DEFAULT

A value to indicate the lack of CUJ information, disabling all installation scenario logic.

Constant Value: 0 (0x00000000) 

### INSTALL_SCENARIO_FAST

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int INSTALL_SCENARIO_FAST

Installation scenario providing the fastest "install button to launch" experience possible.

Constant Value: 1 (0x00000001) 

### MATCH_ALL

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_ALL

Querying flag: if set and if the platform is doing any filtering of the results, then the filtering will not happen. This is a synonym for saying that all results should be returned. 

_This flag should be used with extreme care._

Constant Value: 131072 (0x00020000) 

### MATCH_APEX

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_APEX

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include APEX packages that are currently installed. In APEX terminology, this corresponds to packages that are currently active, i.e. mounted and available to other processes of the OS. In particular, this flag alone will not match APEX files that are staged for activation at next reboot.

Constant Value: 1073741824 (0x40000000) 

### MATCH_ARCHIVED_PACKAGES

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final long MATCH_ARCHIVED_PACKAGES

Flag parameter to also retrieve some information about archived packages. Packages can be archived through `[PackageInstaller.requestArchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive\(java.lang.String,%20android.content.IntentSender\))` and do not have any APKs stored on the device, but do keep the data directory. 

Note: Archived apps are a subset of apps returned by `[MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)`. 

Note: this flag may cause less information about currently installed applications to be returned. 

Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to see uninstalled packages.

Constant Value: 4294967296 (0x0000000100000000) 

### MATCH_DEFAULT_ONLY

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DEFAULT_ONLY

Resolution and querying flag: if set, only filters that support the `[Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)` will be considered for matching. This is a synonym for including the CATEGORY_DEFAULT in your supplied Intent.

Constant Value: 65536 (0x00010000) 

### MATCH_DIRECT_BOOT_AUTO

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DIRECT_BOOT_AUTO

Querying flag: automatically match components based on their Direct Boot awareness and the current user state. 

Since the default behavior is to automatically apply the current user state, this is effectively a sentinel value that doesn't change the output of any queries based on its presence or absence. 

Instead, this value can be useful in conjunction with `[StrictMode.VmPolicy.Builder.detectImplicitDirectBoot()](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectImplicitDirectBoot\(\))` to detect when a caller is relying on implicit automatic matching, instead of confirming the explicit behavior they want, using a combination of these flags: 

  * `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)`
  * `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)`
  * `[MATCH_DIRECT_BOOT_AUTO](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AUTO)`



Constant Value: 268435456 (0x10000000) 

### MATCH_DIRECT_BOOT_AWARE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DIRECT_BOOT_AWARE

Querying flag: match components which are direct boot _aware_ in the returned info, regardless of the current user state. 

When neither `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` nor `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)` are specified, the default behavior is to match only runnable components based on the user state. For example, when a user is started but credentials have not been presented yet, the user is running "locked" and only `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` components are returned. Once the user credentials have been presented, the user is running "unlocked" and both `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` and `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)` components are returned.

**See also:**

  * `[UserManager.isUserUnlocked()](https://developer.android.com/reference/android/os/UserManager#isUserUnlocked\(\))`



Constant Value: 524288 (0x00080000) 

### MATCH_DIRECT_BOOT_UNAWARE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DIRECT_BOOT_UNAWARE

Querying flag: match components which are direct boot _unaware_ in the returned info, regardless of the current user state. 

When neither `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` nor `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)` are specified, the default behavior is to match only runnable components based on the user state. For example, when a user is started but credentials have not been presented yet, the user is running "locked" and only `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` components are returned. Once the user credentials have been presented, the user is running "unlocked" and both `[MATCH_DIRECT_BOOT_AWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_AWARE)` and `[MATCH_DIRECT_BOOT_UNAWARE](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DIRECT_BOOT_UNAWARE)` components are returned.

**See also:**

  * `[UserManager.isUserUnlocked()](https://developer.android.com/reference/android/os/UserManager#isUserUnlocked\(\))`



Constant Value: 262144 (0x00040000) 

### MATCH_DISABLED_COMPONENTS

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DISABLED_COMPONENTS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include disabled components in the returned info.

Constant Value: 512 (0x00000200) 

### MATCH_DISABLED_UNTIL_USED_COMPONENTS

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_DISABLED_UNTIL_USED_COMPONENTS

`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` flag: include disabled components which are in that state only because of `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)` in the returned info. Note that if you set this flag, applications that are in this disabled state will be reported as enabled.

Constant Value: 32768 (0x00008000) 

### MATCH_SYSTEM_ONLY

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_SYSTEM_ONLY

Querying flag: include only components from applications that are marked with `[ApplicationInfo.FLAG_SYSTEM](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_SYSTEM)`.

Constant Value: 1048576 (0x00100000) 

### MATCH_UNINSTALLED_PACKAGES

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int MATCH_UNINSTALLED_PACKAGES

Flag parameter to retrieve some information about all applications (even uninstalled ones) which have data directories. This state could have resulted if applications have been deleted with flag `DELETE_KEEP_DATA` with a possibility of being replaced or reinstalled in future. 

Note: this flag may cause less information about currently installed applications to be returned. 

Note: use of this flag requires the android.permission.QUERY_ALL_PACKAGES permission to see uninstalled packages.

Constant Value: 8192 (0x00002000) 

### MAXIMUM_VERIFICATION_TIMEOUT

Added in [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final long MAXIMUM_VERIFICATION_TIMEOUT

Can be used as the `millisecondsToDelay` argument for `[PackageManager.extendVerificationTimeout](https://developer.android.com/reference/android/content/pm/PackageManager#extendVerificationTimeout\(int,%20int,%20long\))`. This is the maximum time `PackageManager` waits for the verification agent to return (in milliseconds).

Constant Value: 3600000 (0x000000000036ee80) 

### PERMISSION_DENIED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int PERMISSION_DENIED

Permission check result: this is returned by `[checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission\(java.lang.String,%20java.lang.String\))` if the permission has not been granted to the given package.

Constant Value: -1 (0xffffffff) 

### PERMISSION_GRANTED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int PERMISSION_GRANTED

Permission check result: this is returned by `[checkPermission(String, String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkPermission\(java.lang.String,%20java.lang.String\))` if the permission has been granted to the given package.

Constant Value: 0 (0x00000000) 

### PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT

Application level `[PackageManager .Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` for an app to inform the system that the app can be opted-in or opted-out from the compatibility treatment that rotates camera output by 90 degrees on landscape sensors on devices known to have compatibility issues. 

The treatment is disabled by default but device manufacturers can enable the treatment using their discretion to improve camera compatibility. With this property set to `false`, the rotation will not be applied. A value of `true` will ensure that rotation is applied, provided it is enabled for the device. In most cases, if rotation is the desired behavior this property need not be set. However, if your app experiences stretching or incorrect rotation on these devices, explicitly setting this to `true` may resolve that behavior. Apps should set this to `false` if there is confidence that the app handles `[CameraCharacteristics.SENSOR_ORIENTATION](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#SENSOR_ORIENTATION)` correctly. See [ the documentation for best practice.](https://developer.android.com/training/camera2/camera-preview)

**Syntax:**
    
    
    <application>
      <property
        android:name="android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT"
        android:value="true|false"/>
    </application>
    

Constant Value: "android.camera.PROPERTY_COMPAT_OVERRIDE_LANDSCAPE_TO_PORTRAIT" 

### PROPERTY_MEDIA_CAPABILITIES

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_MEDIA_CAPABILITIES

<application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the XML resource ID containing an application's media capabilities XML file For example: <application> <property android:name="android.media.PROPERTY_MEDIA_CAPABILITIES" android:resource="@xml/media_capabilities"> <application>

Constant Value: "android.media.PROPERTY_MEDIA_CAPABILITIES" 

### PROPERTY_NATIVE_SERVICE_FUNCTION_NAME

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_NATIVE_SERVICE_FUNCTION_NAME

Service level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag for native services specifying the symbol name of the entry point function for the service. If not specified, the system executes `ANativeService_onCreate`. 

Example: 
    
    
    <service android:isolatedProcess="true"
                      android:nativeService="true">
      <property
        android:name="android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME"
        android:value="native_service_createService"/>
    </service>
    

Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_FUNCTION_NAME" 

### PROPERTY_NATIVE_SERVICE_LIBRARY_NAME

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_NATIVE_SERVICE_LIBRARY_NAME

Service level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag for native services specifying the name of the library to be loaded to the process that hosts the service. If not specified, the system tries to load `libmain.so`. 

Example: 
    
    
    <service android:isolatedProcess="true"
                      android:nativeService="true">
      <property
        android:name="android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME"
        android:value="libnativeservice.so"/>
    </service>
    

Constant Value: "android.app.PROPERTY_NATIVE_SERVICE_LIBRARY_NAME" 

### PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES

<application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the XML resource ID containing the declaration of the self-certified network capabilities used by the application. 

Starting from Android 14, usage of some network capabilities in `[ConnectivityManager.requestNetwork(NetworkRequest, PendingIntent)](https://developer.android.com/reference/android/net/ConnectivityManager#requestNetwork\(android.net.NetworkRequest,%20android.app.PendingIntent\))` require the application to declare its usage of that particular capability in this resource. Only some capabilities require a declaration. Please look up the specific capability you want to use in `[NetworkCapabilities](https://developer.android.com/reference/android/net/NetworkCapabilities)` to see if it needs declaration in this property. For example: <application> <property android:name="android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES" android:resource="@xml/self_certified_network_capabilities"> <application>

The detail format of self_certified_network_capabilities.xml is described in `[NetworkRequest](https://developer.android.com/reference/android/net/NetworkRequest)`

Constant Value: "android.net.PROPERTY_SELF_CERTIFIED_NETWORK_CAPABILITIES" 

### PROPERTY_SPECIAL_USE_FGS_SUBTYPE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_SPECIAL_USE_FGS_SUBTYPE

<service> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying the actual use case of the service if it's foreground service with the type `[ServiceInfo.FOREGROUND_SERVICE_TYPE_SPECIAL_USE](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SPECIAL_USE)`. 

For example: <service> <property android:name="android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE" android:value="foo"/> </service>

Constant Value: "android.app.PROPERTY_SPECIAL_USE_FGS_SUBTYPE" 

### PROPERTY_USE_RESTRICTED_BACKUP_MODE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROPERTY_USE_RESTRICTED_BACKUP_MODE

<application> level `[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` tag specifying whether the app should be put into the "restricted" backup mode when it's started for backup and restore operations. 

See [ for information about restricted mode](https://developer.android.com/identity/data/autobackup#ImplementingBackupAgent). 

Starting with Android 16 apps may not be started in restricted mode based on this property. 

**Syntax:**
    
    
    <application>
      <property
        android:name="android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE"
        android:value="true|false"/>
    </application>
    

If this property is set, the operating system will respect it for now (see Note below). If it's not set, the behavior depends on the SDK level that the app is targeting. For apps targeting SDK level `[Build.VERSION_CODES.VANILLA_ICE_CREAM](https://developer.android.com/reference/android/os/Build.VERSION_CODES#VANILLA_ICE_CREAM)` or lower, the property defaults to `true`. For apps targeting SDK level `[Build.VERSION_CODES.BAKLAVA](https://developer.android.com/reference/android/os/Build.VERSION_CODES#BAKLAVA)` or higher, the operating system will make a decision dynamically. 

Note: It's not recommended to set this property to `true` unless absolutely necessary. In a future Android version, this property may be deprecated in favor of removing restricted mode completely.

Constant Value: "android.app.backup.PROPERTY_USE_RESTRICTED_BACKUP_MODE" 

### SIGNATURE_FIRST_NOT_SIGNED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_FIRST_NOT_SIGNED

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if the first package is not signed but the second is.

Constant Value: -1 (0xffffffff) 

### SIGNATURE_MATCH

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_MATCH

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if all signatures on the two packages match.

Constant Value: 0 (0x00000000) 

### SIGNATURE_NEITHER_SIGNED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_NEITHER_SIGNED

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if neither of the two packages is signed.

Constant Value: 1 (0x00000001) 

### SIGNATURE_NO_MATCH

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_NO_MATCH

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if not all signatures on both packages match.

Constant Value: -3 (0xfffffffd) 

### SIGNATURE_SECOND_NOT_SIGNED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_SECOND_NOT_SIGNED

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if the second package is not signed but the first is.

Constant Value: -2 (0xfffffffe) 

### SIGNATURE_UNKNOWN_PACKAGE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SIGNATURE_UNKNOWN_PACKAGE

Signature check result: this is returned by `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))` if either of the packages are not valid.

Constant Value: -4 (0xfffffffc) 

### SYNCHRONOUS

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int SYNCHRONOUS

Flag parameter for `[setComponentEnabledSetting(android.content.ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))` to indicate that the given user's package restrictions state will be serialised to disk after the component state has been updated. Note that this is synchronous disk access, so calls using this flag should be run on a background thread.

Constant Value: 2 (0x00000002) 

### VERIFICATION_ALLOW

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int VERIFICATION_ALLOW

Used as the `verificationCode` argument for `[PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))` to indicate that the calling package verifier allows the installation to proceed.

Constant Value: 1 (0x00000001) 

### VERIFICATION_REJECT

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int VERIFICATION_REJECT

Used as the `verificationCode` argument for `[PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))` to indicate the calling package verifier does not vote to allow the installation to proceed.

Constant Value: -1 (0xffffffff) 

### VERSION_CODE_HIGHEST

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final int VERSION_CODE_HIGHEST

Constant for specifying the highest installed package version code.

Constant Value: -1 (0xffffffff) 

## Fields

### TRUST_ALL

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> TRUST_ALL

Trust any Installer to provide checksums for the package.

**See also:**

  * `[requestChecksums(String, boolean, int, List, OnChecksumsReadyListener)](https://developer.android.com/reference/android/content/pm/PackageManager#requestChecksums\(java.lang.String,%20boolean,%20int,%20java.util.List<java.security.cert.Certificate>,%20android.content.pm.PackageManager.OnChecksumsReadyListener\))`



### TRUST_NONE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> TRUST_NONE

Don't trust any Installer to provide checksums for the package. This effectively disables optimized Installer-enforced checksums.

**See also:**

  * `[requestChecksums(String, boolean, int, List, OnChecksumsReadyListener)](https://developer.android.com/reference/android/content/pm/PackageManager#requestChecksums\(java.lang.String,%20boolean,%20int,%20java.util.List<java.security.cert.Certificate>,%20android.content.pm.PackageManager.OnChecksumsReadyListener\))`



## Public constructors

### PackageManager

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public PackageManager ()

**This constructor is deprecated.**  
Do not instantiate or subclass - obtain an instance from `[Context.getPackageManager](https://developer.android.com/reference/android/content/Context#getPackageManager\(\))`

## Public methods

### addPackageToPreferred

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void addPackageToPreferred ([String](https://developer.android.com/reference/java/lang/String) packageName)

**This method was deprecated in API level 15.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
  
### addPermission

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean addPermission ([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo) info)

Add a new dynamic permission to the system. For this to work, your package must have defined a permission tree through the `[<permission-tree>](https://developer.android.com/reference/android/R.styleable#AndroidManifestPermissionTree)` tag in its manifest. A package can only add permissions to trees that were defined by either its own package or another with the same user id; a permission is in a tree if it matches the name of the permission tree + ".": for example, "com.foo.bar" is a member of the permission tree "com.foo". 

It is good to make your permission tree name descriptive, because you are taking possession of that entire set of permission names. Thus, it must be under a domain you control, with a suffix that will not match any normal permissions that may be declared in any applications that are part of that domain. 

New permissions must be added before any .apks are installed that use those permissions. Permissions you add through this method are remembered across reboots of the device. If the given permission already exists, the info you supply here will be used to update it.

Parameters  
---  
`info` |  `PermissionInfo`: Description of the permission to be added.   
This value cannot be `null`.  
Returns  
---  
`boolean` | Returns true if a new permission was created, false if an existing one was updated.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you are not allowed to add the given permission name.  
  
**See also:**

  * `[removePermission(String)](https://developer.android.com/reference/android/content/pm/PackageManager#removePermission\(java.lang.String\))`



### addPermissionAsync

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean addPermissionAsync ([PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo) info)

Like `[addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))` but asynchronously persists the package manager state after returning from the call, allowing it to return quicker and batch a series of adds at the expense of no guarantee the added permission will be retained if the device is rebooted before it is written.

Parameters  
---  
`info` |  `PermissionInfo`: This value cannot be `null`.  
Returns  
---  
`boolean` |   
  
### addPreferredActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void addPreferredActivity ([IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) filter, 
                    int match, 
                    [ComponentName[]](https://developer.android.com/reference/android/content/ComponentName) set, 
                    [ComponentName](https://developer.android.com/reference/android/content/ComponentName) activity)

**This method was deprecated in API level 15.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Add a new preferred activity mapping to the system. This will be used to automatically select the given activity component when `[Context.startActivity()](https://developer.android.com/reference/android/content/Context#startActivity\(android.content.Intent\))` finds multiple matching activities and also matches the given filter.

Parameters  
---  
`filter` |  `IntentFilter`: The set of intents under which this activity will be made preferred.   
This value cannot be `null`.  
`match` |  `int`: The IntentFilter match category that this preference applies to.  
`set` |  `ComponentName`: The set of activities that the user was picking from when this preference was made.   
This value may be `null`.  
`activity` |  `ComponentName`: The component name of the activity that is to be preferred.   
This value cannot be `null`.  
  
### addWhitelistedRestrictedPermission

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean addWhitelistedRestrictedPermission ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [String](https://developer.android.com/reference/java/lang/String) permName, 
                    int whitelistFlags)

Adds a whitelisted restricted permission for an app. 

Permissions can be hard restricted which means that the app cannot hold them or soft restricted where the app can hold the permission but in a weaker form. Whether a permission is `[hard restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)` or `[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)` depends on the permission declaration. Whitelisting a hard restricted permission allows for the to hold that permission and whitelisting a soft restricted permission allows the app to hold the permission in its full, unrestricted form. 

There are four whitelists: 
  1. one for cases where the system permission policy whitelists a permission This list corresponds to the `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)` flag. Can only be modified by pre-installed holders of a dedicated permission. 
  2. one for cases where the system whitelists the permission when upgrading from an OS version in which the permission was not restricted to an OS version in which the permission is restricted. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)` flag. Can be modified by pre-installed holders of a dedicated permission. The installer on record can only remove permissions from this whitelist. 
  3. one for cases where the installer of the package whitelists a permission. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)` flag. Can be modified by pre-installed holders of a dedicated permission or the installer on record. 



You need to specify the whitelists for which to set the whitelisted permissions which will clear the previous whitelisted permissions and replace them with the provided ones. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Parameters  
---  
`packageName` |  `String`: The app for which to get whitelisted permissions.   
This value cannot be `null`.  
`permName` |  `String`: The whitelisted permission to add.   
This value cannot be `null`.  
`whitelistFlags` |  `int`: The whitelists to which to add. Passing multiple flags updates all specified whitelists.   
Value is either `0` or a combination of the following: 

  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`

  
Returns  
---  
`boolean` | Whether the permission was added to the whitelist.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you try to modify a whitelist that you have no access to.  
  
**See also:**

  * `[getWhitelistedRestrictedPermissions(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getWhitelistedRestrictedPermissions\(java.lang.String,%20int\))`
  * `[removeWhitelistedRestrictedPermission(String,String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#removeWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))`
  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`



### canPackageQuery

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean canPackageQuery ([String](https://developer.android.com/reference/java/lang/String) sourcePackageName, 
                    [String](https://developer.android.com/reference/java/lang/String) targetPackageName)

Returns `true` if the source package is able to query for details about the target package. Applications that share details about other applications should use this API to determine if those details should be withheld from callers that do not otherwise have visibility of them. 

Note: The caller must be able to query for details about the source and target package. A `[NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` is thrown if it isn't.

Parameters  
---  
`sourcePackageName` |  `String`: The source package that would receive details about the target package.   
This value cannot be `null`.  
`targetPackageName` |  `String`: The target package whose details would be shared with the source package.   
This value cannot be `null`.  
Returns  
---  
`boolean` | `true` if the source package is able to query for details about the target package.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if either a given package can not be found on the system, or if the caller is not able to query for details about the source or target package.  
  
### canPackageQuery

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean[] canPackageQuery ([String](https://developer.android.com/reference/java/lang/String) sourcePackageName, 
                    [String[]](https://developer.android.com/reference/java/lang/String) targetPackageNames)

Same as `[canPackageQuery(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#canPackageQuery\(java.lang.String,%20java.lang.String\))` but accepts an array of target packages to be queried.

Parameters  
---  
`sourcePackageName` |  `String`: The source package that would receive details about the target package.   
This value cannot be `null`.  
`targetPackageNames` |  `String`: An array of target packages whose details would be shared with the source package.   
This value cannot be `null`.  
Returns  
---  
`boolean[]` | An array of booleans where each member specifies whether the source package is able to query for details about the target package given by the corresponding value at the same index in the array of target packages.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if either a given package can not be found on the system, or if the caller is not able to query for details about the source or target packages.  
  
### canRequestPackageInstalls

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean canRequestPackageInstalls ()

Checks whether the calling package is allowed to request package installs through package installer. Apps are encouraged to call this API before launching the package installer via intent `[Intent.ACTION_INSTALL_PACKAGE](https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE)`. Starting from Android O, the user can explicitly choose what external sources they trust to install apps on the device. If this API returns false, the install request will be blocked by the package installer and a dialog will be shown to the user with an option to launch settings to change their preference. An application must target Android O or higher and declare permission `[Manifest.permission.REQUEST_INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES)` in order to use this API.

Returns  
---  
`boolean` | true if the calling package is trusted by the user to request install packages on the device, false otherwise.  
  
**See also:**

  * `[Intent.ACTION_INSTALL_PACKAGE](https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE)`
  * `[Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_UNKNOWN_APP_SOURCES)`



### canonicalToCurrentPackageNames

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String[]](https://developer.android.com/reference/java/lang/String) canonicalToCurrentPackageNames ([String[]](https://developer.android.com/reference/java/lang/String) packageNames)

Map from a packages canonical name to the current name in use on the device.

Parameters  
---  
`packageNames` |  `String`: Array of new names to be mapped.   
This value cannot be `null`.  
Returns  
---  
`[String[]](https://developer.android.com/reference/java/lang/String)` | Returns an array of the same size as the original, containing the current name for each package.  
  
### checkPermission

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int checkPermission ([String](https://developer.android.com/reference/java/lang/String) permName, 
                    [String](https://developer.android.com/reference/java/lang/String) packageName)

Check whether a particular package has been granted a particular permission. 

**Note:** This API returns the underlying permission state as-is and is mostly intended for permission managing system apps. To perform an access check for a certain app, please use the `[Context.checkPermission](https://developer.android.com/reference/android/content/Context#checkPermission\(java.lang.String,%20int,%20int\))` APIs instead.

Parameters  
---  
`permName` |  `String`: The name of the permission you are checking for.   
This value cannot be `null`.  
`packageName` |  `String`: The name of the package you are checking against.   
This value cannot be `null`.  
Returns  
---  
`int` | If the package has the permission, PERMISSION_GRANTED is returned. If it does not have the permission, PERMISSION_DENIED is returned.   
Value is one of the following: 

  * `[PERMISSION_GRANTED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_GRANTED)`
  * `[PERMISSION_DENIED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_DENIED)`

  
  
**See also:**

  * `[PERMISSION_GRANTED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_GRANTED)`
  * `[PERMISSION_DENIED](https://developer.android.com/reference/android/content/pm/PackageManager#PERMISSION_DENIED)`



### checkSignatures

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int checkSignatures ([String](https://developer.android.com/reference/java/lang/String) packageName1, 
                    [String](https://developer.android.com/reference/java/lang/String) packageName2)

Compare the signatures of two packages to determine if the same signature appears in both of them. If they do contain the same signature, then they are allowed special privileges when working with each other: they can share the same user-id, run instrumentation against each other, etc.

Parameters  
---  
`packageName1` |  `String`: First package name whose signature will be compared.   
This value cannot be `null`.  
`packageName2` |  `String`: Second package name whose signature will be compared.   
This value cannot be `null`.  
Returns  
---  
`int` | Returns an integer indicating whether all signatures on the two packages match. The value is >= 0 (`[SIGNATURE_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_MATCH)`) if all signatures match or < 0 if there is not a match (`[SIGNATURE_NO_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NO_MATCH)` or `[SIGNATURE_UNKNOWN_PACKAGE](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_UNKNOWN_PACKAGE)`).   
Value is one of the following: 

  * `[SIGNATURE_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_MATCH)`
  * `[SIGNATURE_NEITHER_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NEITHER_SIGNED)`
  * `[SIGNATURE_FIRST_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_FIRST_NOT_SIGNED)`
  * `[SIGNATURE_SECOND_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_SECOND_NOT_SIGNED)`
  * `[SIGNATURE_NO_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NO_MATCH)`
  * `[SIGNATURE_UNKNOWN_PACKAGE](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_UNKNOWN_PACKAGE)`

  
  
**See also:**

  * `[checkSignatures(int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(int,%20int\))`



### checkSignatures

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int checkSignatures (int uid1, 
                    int uid2)

Like `[checkSignatures(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(java.lang.String,%20java.lang.String\))`, but takes UIDs of the two packages to be checked. This can be useful, for example, when doing the check in an IPC, where the UID is the only identity available. It is functionally identical to determining the package associated with the UIDs and checking their signatures.

Parameters  
---  
`uid1` |  `int`: First UID whose signature will be compared.  
`uid2` |  `int`: Second UID whose signature will be compared.  
Returns  
---  
`int` | Returns an integer indicating whether all signatures on the two packages match. The value is >= 0 (`[SIGNATURE_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_MATCH)`) if all signatures match or < 0 if there is not a match (`[SIGNATURE_NO_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NO_MATCH)` or `[SIGNATURE_UNKNOWN_PACKAGE](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_UNKNOWN_PACKAGE)`).   
Value is one of the following: 

  * `[SIGNATURE_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_MATCH)`
  * `[SIGNATURE_NEITHER_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NEITHER_SIGNED)`
  * `[SIGNATURE_FIRST_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_FIRST_NOT_SIGNED)`
  * `[SIGNATURE_SECOND_NOT_SIGNED](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_SECOND_NOT_SIGNED)`
  * `[SIGNATURE_NO_MATCH](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_NO_MATCH)`
  * `[SIGNATURE_UNKNOWN_PACKAGE](https://developer.android.com/reference/android/content/pm/PackageManager#SIGNATURE_UNKNOWN_PACKAGE)`

  
  
**See also:**

  * `[checkSignatures(String,String)](https://developer.android.com/reference/android/content/pm/PackageManager#checkSignatures\(java.lang.String,%20java.lang.String\))`



### clearInstantAppCookie

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void clearInstantAppCookie ()

Clears the instant application cookie for the calling app.

**See also:**

  * `[isInstantApp()](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))`
  * `[isInstantApp(String)](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))`
  * `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`
  * `[getInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))`
  * `[clearInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))`



### clearPackagePreferredActivities

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void clearPackagePreferredActivities ([String](https://developer.android.com/reference/java/lang/String) packageName)

**This method was deprecated in API level 29.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Remove all preferred activity mappings, previously added with `[addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity\(android.content.IntentFilter,%20int,%20android.content.ComponentName\[\],%20android.content.ComponentName\))`, from the system whose activities are implemented in the given package name. An application can only clear its own package(s).

Parameters  
---  
`packageName` |  `String`: The name of the package whose preferred activity mappings are to be removed.   
This value cannot be `null`.  
  
### currentToCanonicalPackageNames

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String[]](https://developer.android.com/reference/java/lang/String) currentToCanonicalPackageNames ([String[]](https://developer.android.com/reference/java/lang/String) packageNames)

Map from the current package names in use on the device to whatever the current canonical name of that package is.

Parameters  
---  
`packageNames` |  `String`: Array of current names to be mapped.   
This value cannot be `null`.  
Returns  
---  
`[String[]](https://developer.android.com/reference/java/lang/String)` | Returns an array of the same size as the original, containing the canonical name for each package.  
  
### extendVerificationTimeout

Added in [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void extendVerificationTimeout (int id, 
                    int verificationCodeAtTimeout, 
                    long millisecondsToDelay)

Allows a package listening to the `[package verification broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)` to extend the default timeout for a response and declare what action to perform after the timeout occurs. The response must include the `verificationCodeAtTimeout` which is one of `[PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` or `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`. This method can be called multiple times, but the total amount of time extension time will be limited to `[PackageManager.MAXIMUM_VERIFICATION_TIMEOUT](https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATION_TIMEOUT)`. If the method is called multiple times with different `verificationCodeAtTimeout`, then previous `verificationCodeAtTimeout` will be ignored and only the latest one will take effect. If this method is called after calling `[PackageManager.verifyPendingInstall](https://developer.android.com/reference/android/content/pm/PackageManager#verifyPendingInstall\(int,%20int\))`, it may nullify the result set by verifyPendingInstall.

Parameters  
---  
`id` |  `int`: pending package identifier as passed via the `[PackageManager.EXTRA_VERIFICATION_ID](https://developer.android.com/reference/android/content/pm/PackageManager#EXTRA_VERIFICATION_ID)` Intent extra.  
`verificationCodeAtTimeout` |  `int`: either `[PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` or `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`. If `verificationCodeAtTimeout` is neither `[PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` or `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`, then `verificationCodeAtTimeout` will default to `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`.  
`millisecondsToDelay` |  `long`: the amount of time requested for the timeout. Must be positive and less than `[PackageManager.MAXIMUM_VERIFICATION_TIMEOUT](https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATION_TIMEOUT)`. If `millisecondsToDelay` is out of bounds, `millisecondsToDelay` will be set to the closest in bounds value; namely, 0 or `[PackageManager.MAXIMUM_VERIFICATION_TIMEOUT](https://developer.android.com/reference/android/content/pm/PackageManager#MAXIMUM_VERIFICATION_TIMEOUT)`.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if the caller does not have the PACKAGE_VERIFICATION_AGENT permission.  
  
### getActivityBanner

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityBanner ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName)

Retrieve the banner associated with an activity. Given the full name of an activity, retrieves the information about it and calls `[ComponentInfo.loadIcon()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon\(android.content.pm.PackageManager\))` to return its banner. If the activity cannot be found, NameNotFoundException is thrown. 

The returned drawable is subject to the same size capping limits as described in `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`.

Parameters  
---  
`activityName` |  `ComponentName`: Name of the activity whose banner is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the banner, or null if the activity has no banner specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given activity could not be loaded.  
  
**See also:**

  * `[getActivityBanner(Intent)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner\(android.content.Intent\))`



### getActivityBanner

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityBanner ([Intent](https://developer.android.com/reference/android/content/Intent) intent)

Retrieve the banner associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityBanner(intent.getClassName()). Otherwise it resolves the intent's component and returns the banner associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

Parameters  
---  
`intent` |  `Intent`: The intent for which you would like to retrieve a banner.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the banner, or null if the activity has no banner specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for application matching the given intent could not be loaded.  
  
**See also:**

  * `[getActivityBanner(ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityBanner\(android.content.ComponentName\))`



### getActivityIcon

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityIcon ([Intent](https://developer.android.com/reference/android/content/Intent) intent)

Retrieve the icon associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityIcon(intent.getClassName()). Otherwise it resolves the intent's component and returns the icon associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

Parameters  
---  
`intent` |  `Intent`: The intent for which you would like to retrieve an icon.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the icon, or the default activity icon if it could not be found. Does not return null.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for application matching the given intent could not be loaded.  
  
**See also:**

  * `[getActivityIcon(ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon\(android.content.ComponentName\))`



### getActivityIcon

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityIcon ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName)

Retrieve the icon associated with an activity. Given the full name of an activity, retrieves the information about it and calls `[ComponentInfo.loadIcon()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadIcon\(android.content.pm.PackageManager\))` to return its icon. If the activity cannot be found, NameNotFoundException is thrown. 

The returned drawable is subject to the same size capping limits as described in `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`.

Parameters  
---  
`activityName` |  `ComponentName`: Name of the activity whose icon is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the icon, or the default activity icon if it could not be found. Does not return null.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given activity could not be loaded.  
  
**See also:**

  * `[getActivityIcon(Intent)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon\(android.content.Intent\))`



### getActivityInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo) getActivityInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    int flags)

Retrieve all of the information we know about a particular activity class. Use `[getActivityInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed.

Parameters  
---  
`component` |  `ComponentName`: The full component name (i.e. com.google.apps.contacts/com.google.apps.contacts. ContactsList) of an Activity class.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` | An `[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` containing information about the activity.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getActivityInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo) getActivityInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[getActivityInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityInfo\(android.content.ComponentName,%20int\))`.

Parameters  
---  
`component` |  `ComponentName`: This value cannot be `null`.  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getActivityLogo

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityLogo ([Intent](https://developer.android.com/reference/android/content/Intent) intent)

Retrieve the logo associated with an Intent. If intent.getClassName() is set, this simply returns the result of getActivityLogo(intent.getClassName()). Otherwise it resolves the intent's component and returns the logo associated with the resolved component. If intent.getClassName() cannot be found or the Intent cannot be resolved to a component, NameNotFoundException is thrown.

Parameters  
---  
`intent` |  `Intent`: The intent for which you would like to retrieve a logo.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the logo, or null if the activity has no logo specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for application matching the given intent could not be loaded.  
  
**See also:**

  * `[getActivityLogo(ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo\(android.content.ComponentName\))`



### getActivityLogo

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getActivityLogo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName)

Retrieve the logo associated with an activity. Given the full name of an activity, retrieves the information about it and calls `[ComponentInfo.loadLogo()](https://developer.android.com/reference/android/content/pm/PackageItemInfo#loadLogo\(android.content.pm.PackageManager\))` to return its logo. If the activity cannot be found, NameNotFoundException is thrown. 

The returned drawable is subject to the same size capping limits as described in `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`.

Parameters  
---  
`activityName` |  `ComponentName`: Name of the activity whose logo is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the logo or null if the activity has no logo specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given activity could not be loaded.  
  
**See also:**

  * `[getActivityLogo(Intent)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityLogo\(android.content.Intent\))`



### getAllPermissionGroups

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)> getAllPermissionGroups (int flags)

Retrieve all of the known permission groups in the system.

Parameters  
---  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)>` | Returns a list of `[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)` containing information about all of the known permission groups.   
This value cannot be `null`.  
  
### getAppUidForPrivateComputeCoreUid

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public int getAppUidForPrivateComputeCoreUid (int pccUid)

Maps a Private Compute Core (PCC) UID to its corresponding application UID.

Parameters  
---  
`pccUid` |  `int`: The PCC UID to map.  
Returns  
---  
`int` | The corresponding application UID, or `[ERROR(Process.INVALID_UID/java.lang.Process#INVALID_UID Process.INVALID_UID)](https://developer.android.com/)` if the provided UID is not a valid PCC UID or no mapping exists.  
  
### getApplicationBanner

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationBanner ([String](https://developer.android.com/reference/java/lang/String) packageName)

Retrieve the banner associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationIcon() to return its banner. If the application cannot be found, NameNotFoundException is thrown. 

The returned drawable is subject to the same size capping limits as described in `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`.

Parameters  
---  
`packageName` |  `String`: Name of the package whose application banner is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the banner or null if the application has no banner specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded.  
  
**See also:**

  * `[getApplicationBanner(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner\(android.content.pm.ApplicationInfo\))`



### getApplicationBanner

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationBanner ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info)

Retrieve the banner associated with an application.

Parameters  
---  
`info` |  `ApplicationInfo`: Information about application being queried.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the banner or null if the application has no banner specified.  
  
**See also:**

  * `[getApplicationBanner(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationBanner\(java.lang.String\))`



### getApplicationEnabledSetting

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int getApplicationEnabledSetting ([String](https://developer.android.com/reference/java/lang/String) packageName)

Return the enabled setting for an application. This returns the last value set by `[setApplicationEnabledSetting(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setApplicationEnabledSetting\(java.lang.String,%20int,%20int\))`; in most cases this value will be `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)` since the value originally specified in the manifest has not been modified.

Parameters  
---  
`packageName` |  `String`: The package name of the application to retrieve.   
This value cannot be `null`.  
Returns  
---  
`int` | Returns the current enabled state for the application.   
Value is one of the following: 

  * `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)`
  * `[COMPONENT_ENABLED_STATE_ENABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_ENABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_USER](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_USER)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)`

  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the named package does not exist.  
  
### getApplicationIcon

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationIcon ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info)

Retrieve the icon associated with an application. If it has not defined an icon, the default app icon is returned. Does not return null. 

Note: The returned drawable's dimensions are capped to a maximum size of `2048 x 2048` pixels. If the resource's intrinsic dimensions exceed this limit, it will be downsampled automatically, preserving its aspect ratio.

Parameters  
---  
`info` |  `ApplicationInfo`: Information about application being queried.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the icon, or the default application icon if it could not be found.  
  
**See also:**

  * `[getApplicationIcon(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(java.lang.String\))`



### getApplicationIcon

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationIcon ([String](https://developer.android.com/reference/java/lang/String) packageName)

Retrieve the icon associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationIcon() to return its icon. If the application cannot be found, NameNotFoundException is thrown. 

Note: The returned drawable's dimensions are capped to a maximum size of `2048 x 2048` pixels. If the resource's intrinsic dimensions exceed this limit, it will be downsampled automatically, preserving its aspect ratio.

Parameters  
---  
`packageName` |  `String`: Name of the package whose application icon is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the icon, or the default application icon if it could not be found. Does not return null.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded.  
  
**See also:**

  * `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`



### getApplicationInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) getApplicationInfo ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags) flags)

See `[getApplicationInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo\(java.lang.String,%20int\))`.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.ApplicationInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getApplicationInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) getApplicationInfo ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int flags)

Retrieve all of the information we know about a particular package/application. Use `[getApplicationInfo(String,ApplicationInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationInfo\(java.lang.String,%20android.content.pm.PackageManager.ApplicationInfoFlags\))` when long flags are needed.

Parameters  
---  
`packageName` |  `String`: The full name (i.e. com.google.apps.contacts) of an application.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` | An `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` containing information about the package. If flag `MATCH_UNINSTALLED_PACKAGES` is set and if the package is not found in the list of installed applications, the application information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getApplicationLabel

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence) getApplicationLabel ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info)

Return the label to use for this application.

Parameters  
---  
`info` |  `ApplicationInfo`: The `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` of the application to get the label of.   
This value cannot be `null`.  
Returns  
---  
`[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` | Returns a `[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` containing the label associated with this application, or its name the item does not have a label.   
This value cannot be `null`.  
  
### getApplicationLogo

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationLogo ([String](https://developer.android.com/reference/java/lang/String) packageName)

Retrieve the logo associated with an application. Given the name of the application's package, retrieves the information about it and calls getApplicationLogo() to return its logo. If the application cannot be found, NameNotFoundException is thrown. 

The returned drawable is subject to the same size capping limits as described in `[getApplicationIcon(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationIcon\(android.content.pm.ApplicationInfo\))`.

Parameters  
---  
`packageName` |  `String`: Name of the package whose application logo is to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the logo, or null if no application logo has been specified.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded.  
  
**See also:**

  * `[getApplicationLogo(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo\(android.content.pm.ApplicationInfo\))`



### getApplicationLogo

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getApplicationLogo ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info)

Retrieve the logo associated with an application. If it has not specified a logo, this method returns null.

Parameters  
---  
`info` |  `ApplicationInfo`: Information about application being queried.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns the image of the logo, or null if no logo is specified by the application.  
  
**See also:**

  * `[getApplicationLogo(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getApplicationLogo\(java.lang.String\))`



### getArchivedPackage

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ArchivedPackageInfo](https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo) getArchivedPackage ([String](https://developer.android.com/reference/java/lang/String) packageName)

Return archived package info for the package or null if the package is not installed.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[ArchivedPackageInfo](https://developer.android.com/reference/android/content/pm/ArchivedPackageInfo)` |   
  
**See also:**

  * `[PackageInstaller.installPackageArchived](https://developer.android.com/reference/android/content/pm/PackageInstaller#installPackageArchived\(android.content.pm.ArchivedPackageInfo,%20android.content.pm.PackageInstaller.SessionParams,%20android.content.IntentSender\))`



### getBackgroundPermissionOptionLabel

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [CharSequence](https://developer.android.com/reference/java/lang/CharSequence) getBackgroundPermissionOptionLabel ()

Gets the localized label that corresponds to the option in settings for granting background access. 

The intended use is for apps to reference this label in its instruction for users to grant a background permission.

Returns  
---  
`[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` | the localized label that corresponds to the settings option for granting background access.   
This value cannot be `null`.  
  
### getChangedPackages

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ChangedPackages](https://developer.android.com/reference/android/content/pm/ChangedPackages) getChangedPackages (int sequenceNumber)

Returns the names of the packages that have been changed [eg. added, removed or updated] since the given sequence number. 

If no packages have been changed, returns `null`. 

The sequence number starts at `0` and is reset every boot.

Parameters  
---  
`sequenceNumber` |  `int`: The first sequence number for which to retrieve package changes.   
Value is 0 or greater  
Returns  
---  
`[ChangedPackages](https://developer.android.com/reference/android/content/pm/ChangedPackages)` |   
  
**See also:**

  * `[Settings.Global.BOOT_COUNT](https://developer.android.com/reference/android/provider/Settings.Global#BOOT_COUNT)`



### getComponentEnabledSetting

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int getComponentEnabledSetting ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) componentName)

Return the enabled setting for a package component (activity, receiver, service, provider). This returns the last value set by `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`; in most cases this value will be `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)` since the value originally specified in the manifest has not been modified.

Parameters  
---  
`componentName` |  `ComponentName`: The component to retrieve.   
This value cannot be `null`.  
Returns  
---  
`int` | Returns the current enabled state for the component.   
Value is one of the following: 

  * `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)`
  * `[COMPONENT_ENABLED_STATE_ENABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_ENABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_USER](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_USER)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)`

  
  
### getDefaultActivityIcon

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getDefaultActivityIcon ()

Return the generic icon for an activity that is used when no specific icon is defined.

Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Drawable Image of the icon.   
This value cannot be `null`.  
  
### getDrawable

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getDrawable ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int resid, 
                    [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo)

Retrieve an image from a package. This is a low-level API used by the various package manager info structures (such as `[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)` to implement retrieval of their associated icon.

Parameters  
---  
`packageName` |  `String`: The name of the package that this icon is coming from. Cannot be null.  
`resid` |  `int`: The resource identifier of the desired image. Cannot be 0.  
`appInfo` |  `ApplicationInfo`: Overall information about packageName. This may be null, in which case the application information will be retrieved for you if needed; if you already have this information around, it can be much more efficient to supply it here.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | Returns a Drawable holding the requested image. Returns null if an image could not be found for any reason.  
  
### getEnableAppLockIntentForPackage

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) getEnableAppLockIntentForPackage ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    boolean enabled)

Returns a `[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` to launch an `[Activity](https://developer.android.com/reference/android/app/Activity)` that allows the caller to set App Lock for the specified package. Returns null if the App Lock state of the package cannot be set, either because App Lock is not supported for that package, or because it is already set to that value. 

App Lock is a feature that allows users to add authentication as a requirement to open individual apps, even if the device is unlocked. When App Lock is enabled for an app, the system performs the following protections: 

  * Requires authentication using device credentials (e.g. PIN, pattern, or password) or Class 3 biometrics, whenever the user attempts to open the app (including after reinstallation), or share information to it via the Sharesheet.
  * Redacts sensitive content of notifications sent by the app.
  * Removes the app's widgets and shortcuts from the home screen.
  * Displays a locked view of the app in Recents to prevent content leakage.
  * Hides the app's Direct Share targets from the Sharesheet.



Once authenticated, an App Lock enabled app remains unlocked while it is visible in the foreground. The app will remain unlocked for a short grace period after the user navigates away, after which the system will re-lock it. Additionally, all App Lock enabled apps are immediately locked whenever the device is locked. 

Before calling this API to avoid getting a null `[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` callers should first verify that App Lock is supported for the specified package by first checking `[ApplicationInfo.isAppLockSupported](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockSupported)`, or if it's already at the target state for that package by checking `[ApplicationInfo.isAppLockEnabled](https://developer.android.com/reference/android/content/pm/ApplicationInfo#isAppLockEnabled)`. The `[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` resolves to an activity, which allows the user to enroll a device credential if one isn't enrolled, and then requires authentication before setting the App Lock enablement state as enabled or disabled.   
Requires `[Manifest.permission.LOCK_APPS](https://developer.android.com/reference/android/Manifest.permission#LOCK_APPS)`

Parameters  
---  
`packageName` |  `String`: the package to enable or disable App Lock.   
This value cannot be `null`.  
`enabled` |  `boolean`: true when the user would like to enable App Lock for the given package, false otherwise  
Returns  
---  
`[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` | a `[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)` to launch an activity to set App Lock for the passed in package. If the package does not support App Lock or the package's App Lock state is already in the passed in state, return null.  
  
### getGroupOfPlatformPermission

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void getGroupOfPlatformPermission ([String](https://developer.android.com/reference/java/lang/String) permissionName, 
                    [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) executor, 
                    [Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[String](https://developer.android.com/reference/java/lang/String)> callback)

Get the platform-defined permission group of a particular permission, if the permission is a platform-defined permission.

Parameters  
---  
`permissionName` |  `String`: the permission whose group is desired.   
This value cannot be `null`.  
`executor` |  `Executor`: the `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)` on which to invoke the callback.   
This value cannot be `null`.   
Callback and listener events are dispatched through this `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)`, providing an easy way to control which thread is used. To dispatch events through the main thread of your application, you can use `[Context.getMainExecutor()](https://developer.android.com/reference/android/content/Context#getMainExecutor\(\))`. Otherwise, provide an `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)` that dispatches to an appropriate thread.  
`callback` |  `Consumer`: the callback which will receive the name of the permission group this permission belongs to, or `null` if it has no group, is not a platform-defined permission, or there was an exception  
  
### getInstallSourceInfo

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [InstallSourceInfo](https://developer.android.com/reference/android/content/pm/InstallSourceInfo) getInstallSourceInfo ([String](https://developer.android.com/reference/java/lang/String) packageName)

Retrieves information about how a package was installed or updated. 

If the calling application does not hold the INSTALL_PACKAGES permission then the result will always return `null` from `[InstallSourceInfo.getOriginatingPackageName()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getOriginatingPackageName\(\))`. 

If the package that requested the install has been uninstalled, then information about it will only be returned from `[InstallSourceInfo.getInitiatingPackageName()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageName\(\))` and `[InstallSourceInfo.getInitiatingPackageSigningInfo()](https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageSigningInfo\(\))` if the calling package is requesting its own install information and is not an instant app.

Parameters  
---  
`packageName` |  `String`: The name of the package to query.   
This value cannot be `null`.  
Returns  
---  
`[InstallSourceInfo](https://developer.android.com/reference/android/content/pm/InstallSourceInfo)` |   
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if the given package name is not available to the caller.  
  
### getInstalledApplications

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)> getInstalledApplications (int flags)

Return a List of all application packages that are installed for the current user. If flag GET_UNINSTALLED_PACKAGES has been set, a list of all applications including those deleted with `DELETE_KEEP_DATA` (partially installed apps with data directory) will be returned. Use `[getInstalledApplications(ApplicationInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(android.content.pm.PackageManager.ApplicationInfoFlags\))` when long flags are needed.

Parameters  
---  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)>` | A List of ApplicationInfo objects, one for each installed application. In the unlikely case there are no installed packages, an empty list is returned. If flag `MATCH_UNINSTALLED_PACKAGES` is set, the application information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).   
This value cannot be `null`.  
  
### getInstalledApplications

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)> getInstalledApplications ([PackageManager.ApplicationInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ApplicationInfoFlags) flags)

See `[getInstalledApplications(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications\(int\))`

Parameters  
---  
`flags` |  `PackageManager.ApplicationInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)>` | This value cannot be `null`.  
  
### getInstalledModules

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)> getInstalledModules (int flags)

Return a List of all modules that are installed.

Parameters  
---  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[MATCH_ALL](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_ALL)`

  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)>` | A `[List](https://developer.android.com/reference/java/util/List)` of `[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)` objects, one for each installed module, containing information about the module. In the unlikely case there are no installed modules, an empty list is returned.   
This value cannot be `null`.  
  
### getInstalledPackages

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getInstalledPackages (int flags)

Return a List of all packages that are installed for the current user. Use `[getInstalledPackages(PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` | A List of PackageInfo objects, one for each installed package, containing information about the package. In the unlikely case there are no installed packages, an empty list is returned. If flag `MATCH_UNINSTALLED_PACKAGES` is set, the package information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).   
This value cannot be `null`.  
  
### getInstalledPackages

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getInstalledPackages ([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getInstalledPackages(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages\(int\))`.

Parameters  
---  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` | This value cannot be `null`.  
  
### getInstallerPackageName

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String](https://developer.android.com/reference/java/lang/String) getInstallerPackageName ([String](https://developer.android.com/reference/java/lang/String) packageName)

**This method was deprecated in API level 30.**  
use `[getInstallSourceInfo(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallSourceInfo\(java.lang.String\))` instead 

Retrieve the package name of the application that installed a package. This identifies which market the package came from.

Parameters  
---  
`packageName` |  `String`: The name of the package to query.   
This value cannot be `null`.  
Returns  
---  
`[String](https://developer.android.com/reference/java/lang/String)` | This value may be `null`.  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the given package name is not installed  
  
### getInstantAppCookie

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract byte[] getInstantAppCookie ()

Gets the instant application cookie for this app. Non instant apps and apps that were instant but were upgraded to normal apps can still access this API. For instant apps this cookie is cached for some time after uninstall while for normal apps the cookie is deleted after the app is uninstalled. The cookie is always present while the app is installed.

Returns  
---  
`byte[]` | The cookie.   
This value cannot be `null`.  
  
**See also:**

  * `[isInstantApp()](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))`
  * `[isInstantApp(String)](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))`
  * `[updateInstantAppCookie(byte[])](https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie\(byte\[\]\))`
  * `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`
  * `[clearInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))`



### getInstantAppCookieMaxBytes

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int getInstantAppCookieMaxBytes ()

Gets the maximum size in bytes of the cookie data an instant app can store on the device.

Returns  
---  
`int` | The max cookie size in bytes.  
  
**See also:**

  * `[isInstantApp()](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))`
  * `[isInstantApp(String)](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))`
  * `[updateInstantAppCookie(byte[])](https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie\(byte\[\]\))`
  * `[getInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))`
  * `[clearInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))`



### getInstrumentationInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo) getInstrumentationInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) className, 
                    int flags)

Retrieve all of the information we know about a particular instrumentation class.

Parameters  
---  
`className` |  `ComponentName`: The full name (i.e. com.google.apps.contacts.InstrumentList) of an Instrumentation class.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)` | An `[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)` object containing information about the instrumentation.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getLaunchIntentForPackage

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Intent](https://developer.android.com/reference/android/content/Intent) getLaunchIntentForPackage ([String](https://developer.android.com/reference/java/lang/String) packageName)

Returns a "good" intent to launch a front-door activity in a package. This is used, for example, to implement an "open" button when browsing through packages. The current implementation looks first for a main activity in the category `[Intent.CATEGORY_INFO](https://developer.android.com/reference/android/content/Intent#CATEGORY_INFO)`, and next for a main activity in the category `[Intent.CATEGORY_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LAUNCHER)`. Returns `null` if neither are found. 

Consider using `[getLaunchIntentSenderForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderForPackage\(java.lang.String\))` if the caller is not allowed to query for the `packageName`.

Parameters  
---  
`packageName` |  `String`: The name of the package to inspect.   
This value cannot be `null`.  
Returns  
---  
`[Intent](https://developer.android.com/reference/android/content/Intent)` | A fully-qualified `[Intent](https://developer.android.com/reference/android/content/Intent)` that can be used to launch the main activity in the package. Returns `null` if the package does not contain such an activity, or if _packageName_ is not recognized.  
  
**See also:**

  * `[getLaunchIntentSenderForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentSenderForPackage\(java.lang.String\))`



### getLaunchIntentSenderForPackage

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [IntentSender](https://developer.android.com/reference/android/content/IntentSender) getLaunchIntentSenderForPackage ([String](https://developer.android.com/reference/java/lang/String) packageName)

Returns an `[IntentSender](https://developer.android.com/reference/android/content/IntentSender)` that can be used to launch a front-door activity in a package. This is used, for example, to implement an "open" button when browsing through packages. The current implementation is the same with `[getLaunchIntentForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPackage\(java.lang.String\))`. Instead of returning the `[Intent](https://developer.android.com/reference/android/content/Intent)`, it returns the `[IntentSender](https://developer.android.com/reference/android/content/IntentSender)` which is not restricted by the package visibility. 

The caller can invoke `[IntentSender.sendIntent(Context,int,Intent,IntentSender.OnFinished,Handler)](https://developer.android.com/reference/android/content/IntentSender#sendIntent\(android.content.Context,%20int,%20android.content.Intent,%20android.content.IntentSender.OnFinished,%20android.os.Handler\))` to launch the activity. An `[IntentSender.SendIntentException](https://developer.android.com/reference/android/content/IntentSender.SendIntentException)` is thrown if the package does not contain such an activity, or if _packageName_ is not recognized.

Parameters  
---  
`packageName` |  `String`: The name of the package to inspect.   
This value cannot be `null`.  
Returns  
---  
`[IntentSender](https://developer.android.com/reference/android/content/IntentSender)` | Returns a `[IntentSender](https://developer.android.com/reference/android/content/IntentSender)` to launch the activity.   
This value cannot be `null`.  
  
**See also:**

  * `[getLaunchIntentForPackage(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getLaunchIntentForPackage\(java.lang.String\))`



### getLeanbackLaunchIntentForPackage

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Intent](https://developer.android.com/reference/android/content/Intent) getLeanbackLaunchIntentForPackage ([String](https://developer.android.com/reference/java/lang/String) packageName)

Return a "good" intent to launch a front-door Leanback activity in a package, for use for example to implement an "open" button when browsing through packages. The current implementation will look for a main activity in the category `[Intent.CATEGORY_LEANBACK_LAUNCHER](https://developer.android.com/reference/android/content/Intent#CATEGORY_LEANBACK_LAUNCHER)`, or return null if no main leanback activities are found.

Parameters  
---  
`packageName` |  `String`: The name of the package to inspect.   
This value cannot be `null`.  
Returns  
---  
`[Intent](https://developer.android.com/reference/android/content/Intent)` | Returns either a fully-qualified Intent that can be used to launch the main Leanback activity in the package, or null if the package does not contain such an activity.  
  
### getMemoryBudgets

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[MemoryBudgetInfo](https://developer.android.com/reference/android/content/pm/MemoryBudgetInfo)> getMemoryBudgets ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) info)

Return the memory budgets for the application described by the given `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)`.

Parameters  
---  
`info` |  `ApplicationInfo`: The `[ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo)` of the application to query.   
This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[MemoryBudgetInfo](https://developer.android.com/reference/android/content/pm/MemoryBudgetInfo)>` | This value cannot be `null`.  
  
### getMimeGroup

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> getMimeGroup ([String](https://developer.android.com/reference/java/lang/String) mimeGroup)

Gets all MIME types contained by MIME group. Libraries should use a reverse-DNS prefix followed by a ':' character and library-specific group name to avoid namespace collisions, e.g. "com.example:myFeature".

Parameters  
---  
`mimeGroup` |  `String`: MIME group to retrieve.   
This value cannot be `null`.  
Returns  
---  
`[Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)>` | MIME types contained by the MIME group.   
This value cannot be `null`.  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the MIME group was not declared in the manifest.  
  
### getModuleInfo

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo) getModuleInfo ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int flags)

Retrieve information for a particular module.

Parameters  
---  
`packageName` |  `String`: The name of the module.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 


  
Returns  
---  
`[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)` | A `[ModuleInfo](https://developer.android.com/reference/android/content/pm/ModuleInfo)` object containing information about the module.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a module with the given name cannot be found on the system.  
  
### getNameForUid

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String](https://developer.android.com/reference/java/lang/String) getNameForUid (int uid)

Retrieve the official name associated with a uid. This name is guaranteed to never change, though it is possible for the underlying uid to be changed. That is, if you are storing information about uids in persistent storage, you should use the string returned by this function instead of the raw uid.

Parameters  
---  
`uid` |  `int`: The uid for which you would like to retrieve a name.  
Returns  
---  
`[String](https://developer.android.com/reference/java/lang/String)` | Returns a unique name for the given uid, or null if the uid is not currently assigned.  
  
### getPackageArchiveInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageArchiveInfo ([String](https://developer.android.com/reference/java/lang/String) archiveFilePath, 
                    int flags)

Retrieve overall information about an application package defined in a package archive file Use `[getPackageArchiveInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`archiveFilePath` |  `String`: The path to the archive file.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | A PackageInfo object containing information about the package archive. If the package could not be parsed, returns null.  
  
### getPackageArchiveInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageArchiveInfo ([String](https://developer.android.com/reference/java/lang/String) archiveFilePath, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackageArchiveInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20int\))`.

Parameters  
---  
`archiveFilePath` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | This value may be `null`.  
  
### getPackageGids

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String) packageName)

Return an array of all of the POSIX secondary group IDs that have been assigned to the given package. 

Note that the same package may have different GIDs under different `[UserHandle](https://developer.android.com/reference/android/os/UserHandle)` on the same device.

Parameters  
---  
`packageName` |  `String`: The full name (i.e. com.google.apps.contacts) of the desired package.   
This value cannot be `null`.  
Returns  
---  
`int[]` | Returns an int array of the assigned GIDs, or null if there are none.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if no such package is available to the caller.  
  
### getPackageGids

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int flags)

Return an array of all of the POSIX secondary group IDs that have been assigned to the given package. 

Note that the same package may have different GIDs under different `[UserHandle](https://developer.android.com/reference/android/os/UserHandle)` on the same device. Use `[getPackageGids(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`packageName` |  `String`: The full name (i.e. com.google.apps.contacts) of the desired package.   
This value cannot be `null`.  
`flags` |  `int`  
Returns  
---  
`int[]` | Returns an int array of the assigned gids, or null if there are none.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if no such package is available to the caller.  
  
### getPackageGids

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public int[] getPackageGids ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackageGids(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageGids\(java.lang.String,%20int\))`.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`int[]` | This value may be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getPackageInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageInfo ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int flags)

Retrieve overall information about an application package that is installed on the system. Use `[getPackageInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`packageName` |  `String`: The full name (i.e. com.google.apps.contacts) of the desired package.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | A PackageInfo object containing information about the package. If flag `MATCH_UNINSTALLED_PACKAGES` is set and if the package is not found in the list of installed applications, the package information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if no such package is available to the caller.  
  
### getPackageInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageInfo ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackageInfo(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(java.lang.String,%20int\))`

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getPackageInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageInfo ([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage) versionedPackage, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackageInfo(VersionedPackage,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(android.content.pm.VersionedPackage,%20int\))`

Parameters  
---  
`versionedPackage` |  `VersionedPackage`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getPackageInfo

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo) getPackageInfo ([VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage) versionedPackage, 
                    int flags)

Retrieve overall information about an application package that is installed on the system. This method can be used for retrieving information about packages for which multiple versions can be installed at the time. Currently only packages hosting static shared libraries can have multiple installed versions. The method can also be used to get info for a package that has a single version installed by passing `[VERSION_CODE_HIGHEST](https://developer.android.com/reference/android/content/pm/PackageManager#VERSION_CODE_HIGHEST)` in the `[VersionedPackage](https://developer.android.com/reference/android/content/pm/VersionedPackage)` constructor. Use `[getPackageInfo(VersionedPackage,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageInfo\(android.content.pm.VersionedPackage,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`versionedPackage` |  `VersionedPackage`: The versioned package for which to query.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)` | A PackageInfo object containing information about the package. If flag `MATCH_UNINSTALLED_PACKAGES` is set and if the package is not found in the list of installed applications, the package information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if no such package is available to the caller.  
  
### getPackageInstaller

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller) getPackageInstaller ()

Return interface that offers the ability to install, upgrade, and remove applications on the device.

Returns  
---  
`[PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller)` | This value cannot be `null`.  
  
### getPackageUid

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public int getPackageUid ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackageUid(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid\(java.lang.String,%20int\))`.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`int` |   
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getPackageUid

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int getPackageUid ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int flags)

Return the UID associated with the given package name. 

Note that the same package will have different UIDs under different `[UserHandle](https://developer.android.com/reference/android/os/UserHandle)` on the same device. Use `[getPackageUid(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageUid\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`packageName` |  `String`: The full name (i.e. com.google.apps.contacts) of the desired package.   
This value cannot be `null`.  
`flags` |  `int`  
Returns  
---  
`int` | Returns an integer UID who owns the given package name.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if no such package is available to the caller.  
  
### getPackagesForUid

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String[]](https://developer.android.com/reference/java/lang/String) getPackagesForUid (int uid)

Retrieve the names of all packages that are associated with a particular user id. In most cases, this will be a single package name, the package that has been assigned that user id. Where there are multiple packages sharing the same user id through the "sharedUserId" mechanism, all packages with that id will be returned.

Parameters  
---  
`uid` |  `int`: The user id for which you would like to retrieve the associated packages.  
Returns  
---  
`[String[]](https://developer.android.com/reference/java/lang/String)` | Returns an array of one or more packages assigned to the user id, or null if there are no known packages with the given id.  
  
### getPackagesHoldingPermissions

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPackagesHoldingPermissions ([String[]](https://developer.android.com/reference/java/lang/String) permissions, 
                    int flags)

Return a List of all installed packages that are currently holding any of the given permissions. Use `[getPackagesHoldingPermissions(String[],PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions\(java.lang.String\[\],%20android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`permissions` |  `String`: This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` | A List of PackageInfo objects, one for each installed package that holds any of the permissions that were provided, containing information about the package. If no installed packages hold any of the permissions, an empty list is returned. If flag `MATCH_UNINSTALLED_PACKAGES` is set, the package information is retrieved from the list of uninstalled applications (which includes installed applications as well as applications with data directory i.e. applications which had been deleted with `DELETE_KEEP_DATA` flag set).   
This value cannot be `null`.  
  
### getPackagesHoldingPermissions

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPackagesHoldingPermissions ([String[]](https://developer.android.com/reference/java/lang/String) permissions, 
                    [PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getPackagesHoldingPermissions(String[],int)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackagesHoldingPermissions\(java.lang.String\[\],%20int\))`.

Parameters  
---  
`permissions` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` | This value cannot be `null`.  
  
### getPermissionGroupInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo) getPermissionGroupInfo ([String](https://developer.android.com/reference/java/lang/String) groupName, 
                    int flags)

Retrieve all of the information we know about a particular group of permissions.

Parameters  
---  
`groupName` |  `String`: The fully qualified name (i.e. com.google.permission_group.APPS) of the permission you are interested in.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)` | Returns a `[PermissionGroupInfo](https://developer.android.com/reference/android/content/pm/PermissionGroupInfo)` containing information about the permission.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getPermissionInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo) getPermissionInfo ([String](https://developer.android.com/reference/java/lang/String) permName, 
                    int flags)

Retrieve all of the information we know about a particular permission.

Parameters  
---  
`permName` |  `String`: The fully qualified name (i.e. com.google.permission.LOGIN) of the permission you are interested in.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)` | Returns a `[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)` containing information about the permission.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getPlatformPermissionsForGroup

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void getPlatformPermissionsForGroup ([String](https://developer.android.com/reference/java/lang/String) permissionGroupName, 
                    [Executor](https://developer.android.com/reference/java/util/concurrent/Executor) executor, 
                    [Consumer](https://developer.android.com/reference/java/util/function/Consumer)<[List](https://developer.android.com/reference/java/util/List)<[String](https://developer.android.com/reference/java/lang/String)>> callback)

Get the platform-defined permissions which belong to a particular permission group.

Parameters  
---  
`permissionGroupName` |  `String`: the permission group whose permissions are desired.   
This value cannot be `null`.  
`executor` |  `Executor`: the `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)` on which to invoke the callback.   
This value cannot be `null`.   
Callback and listener events are dispatched through this `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)`, providing an easy way to control which thread is used. To dispatch events through the main thread of your application, you can use `[Context.getMainExecutor()](https://developer.android.com/reference/android/content/Context#getMainExecutor\(\))`. Otherwise, provide an `[Executor](https://developer.android.com/reference/java/util/concurrent/Executor)` that dispatches to an appropriate thread.  
`callback` |  `Consumer`: the callback which will receive a list of the platform-defined permissions in the group, or empty if the group is not a valid platform-defined permission group, or there was an exception.   
This value cannot be `null`.  
  
### getPreferredActivities

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract int getPreferredActivities ([List](https://developer.android.com/reference/java/util/List)<[IntentFilter](https://developer.android.com/reference/android/content/IntentFilter)> outFilters, 
                    [List](https://developer.android.com/reference/java/util/List)<[ComponentName](https://developer.android.com/reference/android/content/ComponentName)> outActivities, 
                    [String](https://developer.android.com/reference/java/lang/String) packageName)

**This method was deprecated in API level 29.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Retrieve all preferred activities, previously added with `[addPreferredActivity(IntentFilter, int, ComponentName, ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#addPreferredActivity\(android.content.IntentFilter,%20int,%20android.content.ComponentName\[\],%20android.content.ComponentName\))`, that are currently registered with the system.

Parameters  
---  
`outFilters` |  `List`: A required list in which to place the filters of all of the preferred activities.   
This value cannot be `null`.  
`outActivities` |  `List`: A required list in which to place the component names of all of the preferred activities.   
This value cannot be `null`.  
`packageName` |  `String`: An optional package in which you would like to limit the list. If null, all activities will be returned; if non-null, only those activities in the given package are returned.  
Returns  
---  
`int` | Returns the total number of registered preferred activities (the number of distinct IntentFilter records, not the number of unique activity components) that were found.  
  
### getPreferredPackages

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)> getPreferredPackages (int flags)

**This method was deprecated in API level 29.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Retrieve the list of all currently configured preferred packages. The first package on the list is the most preferred, the last is the least preferred.

Parameters  
---  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageInfo](https://developer.android.com/reference/android/content/pm/PackageInfo)>` | A List of PackageInfo objects, one for each preferred application, in order of preference.   
This value cannot be `null`.  
  
### getProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property) getProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName, 
                    [String](https://developer.android.com/reference/java/lang/String) packageName)

Returns the property defined in the given package's <application> tag.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if either the given package is not installed or if the given property is not defined within the <application> tag.  
  
### getProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property) getProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName, 
                    [ComponentName](https://developer.android.com/reference/android/content/ComponentName) component)

Returns the property defined in the given component declaration.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
`component` |  `ComponentName`: This value cannot be `null`.  
Returns  
---  
`[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if either the given component does not exist or if the given property is not defined within the component declaration.  
  
### getProviderInfo

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo) getProviderInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    int flags)

Retrieve all of the information we know about a particular content provider class. Use `[getProviderInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed.

Parameters  
---  
`component` |  `ComponentName`: The full component name (i.e. com.google.providers.media/com.google.providers.media. MediaProvider) of a ContentProvider class.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` | A `[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` object containing information about the provider.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getProviderInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo) getProviderInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[getProviderInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getProviderInfo\(android.content.ComponentName,%20int\))`.

Parameters  
---  
`component` |  `ComponentName`: This value cannot be `null`.  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getReceiverInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo) getReceiverInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    int flags)

Retrieve all of the information we know about a particular receiver class. Use `[getReceiverInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed.

Parameters  
---  
`component` |  `ComponentName`: The full component name (i.e. com.google.apps.calendar/com.google.apps.calendar. CalendarAlarm) of a Receiver class.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` | An `[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` containing information about the receiver.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getReceiverInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo) getReceiverInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[getReceiverInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getReceiverInfo\(android.content.ComponentName,%20int\))`.

Parameters  
---  
`component` |  `ComponentName`: This value cannot be `null`.  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ActivityInfo](https://developer.android.com/reference/android/content/pm/ActivityInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getResourcesForActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Resources](https://developer.android.com/reference/android/content/res/Resources) getResourcesForActivity ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) activityName)

Retrieve the resources associated with an activity. Given the full name of an activity, retrieves the information about it and calls getResources() to return its application's resources. If the activity cannot be found, NameNotFoundException is thrown.

Parameters  
---  
`activityName` |  `ComponentName`: Name of the activity whose resources are to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Resources](https://developer.android.com/reference/android/content/res/Resources)` | Returns the application's Resources.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded.  
  
**See also:**

  * `[getResourcesForApplication(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplication\(android.content.pm.ApplicationInfo\))`



### getResourcesForApplication

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Resources](https://developer.android.com/reference/android/content/res/Resources) getResourcesForApplication ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) app)

Retrieve the resources for an application. Throws NameNotFoundException if the package is no longer installed.

Parameters  
---  
`app` |  `ApplicationInfo`: Information about the desired application.   
This value cannot be `null`.  
Returns  
---  
`[Resources](https://developer.android.com/reference/android/content/res/Resources)` | Returns the application's Resources.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded (most likely because it was uninstalled).  
  
### getResourcesForApplication

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Resources](https://developer.android.com/reference/android/content/res/Resources) getResourcesForApplication ([String](https://developer.android.com/reference/java/lang/String) packageName)

Retrieve the resources associated with an application. Given the full package name of an application, retrieves the information about it and calls getResources() to return its application's resources. If the appPackageName cannot be found, NameNotFoundException is thrown.

Parameters  
---  
`packageName` |  `String`: Package name of the application whose resources are to be retrieved.   
This value cannot be `null`.  
Returns  
---  
`[Resources](https://developer.android.com/reference/android/content/res/Resources)` | Returns the application's Resources.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded.  
  
**See also:**

  * `[getResourcesForApplication(ApplicationInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#getResourcesForApplication\(android.content.pm.ApplicationInfo\))`



### getResourcesForApplication

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [Resources](https://developer.android.com/reference/android/content/res/Resources) getResourcesForApplication ([ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) app, 
                    [Configuration](https://developer.android.com/reference/android/content/res/Configuration) configuration)

Retrieve the resources for an application for the provided configuration.

Parameters  
---  
`app` |  `ApplicationInfo`: Information about the desired application.   
This value cannot be `null`.  
`configuration` |  `Configuration`: Overridden configuration when loading the Resources.   
This value may be `null`.  
Returns  
---  
`[Resources](https://developer.android.com/reference/android/content/res/Resources)` | Returns the application's Resources.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | Thrown if the resources for the given application could not be loaded (most likely because it was uninstalled).  
  
### getServiceInfo

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo) getServiceInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[getServiceInfo(ComponentName,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo\(android.content.ComponentName,%20int\))`.

Parameters  
---  
`component` |  `ComponentName`: This value cannot be `null`.  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)` | This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` |   
  
### getServiceInfo

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo) getServiceInfo ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) component, 
                    int flags)

Retrieve all of the information we know about a particular service class. Use `[getServiceInfo(ComponentName,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getServiceInfo\(android.content.ComponentName,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed.

Parameters  
---  
`component` |  `ComponentName`: The full component name (i.e. com.google.apps.media/com.google.apps.media. BackgroundPlayback) of a Service class.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)` | A `[ServiceInfo](https://developer.android.com/reference/android/content/pm/ServiceInfo)` object containing information about the service.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if the component cannot be found on the system.  
  
### getSharedLibraries

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)> getSharedLibraries ([PackageManager.PackageInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.PackageInfoFlags) flags)

See `[getSharedLibraries(int)](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries\(int\))`.

Parameters  
---  
`flags` |  `PackageManager.PackageInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>` | This value cannot be `null`.  
  
### getSharedLibraries

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)> getSharedLibraries (int flags)

Get a list of shared libraries on the device. Use `[getSharedLibraries(PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getSharedLibraries\(android.content.pm.PackageManager.PackageInfoFlags\))` when long flags are needed.

Parameters  
---  
`flags` |  `int`: To filter the libraries to return.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[SharedLibraryInfo](https://developer.android.com/reference/android/content/pm/SharedLibraryInfo)>` | The shared library list.   
This value cannot be `null`.  
  
**See also:**

  * `[MATCH_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_UNINSTALLED_PACKAGES)`



### getSuspendedPackageAppExtras

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [Bundle](https://developer.android.com/reference/android/os/Bundle) getSuspendedPackageAppExtras ()

Returns a `[Bundle](https://developer.android.com/reference/android/os/Bundle)` of extras that was meant to be sent to the calling app when it was suspended. An app with the permission `android.permission.SUSPEND_APPS` can supply this to the system at the time of suspending an app. 

This is the same `[Bundle](https://developer.android.com/reference/android/os/Bundle)` that is sent along with the broadcast `[Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)`, whenever the app is suspended. The contents of this `[Bundle](https://developer.android.com/reference/android/os/Bundle)` are a contract between the suspended app and the suspending app. 

Note: These extras are optional, so if no extras were supplied to the system, this method will return `null`, even when the calling app has been suspended.

Returns  
---  
`[Bundle](https://developer.android.com/reference/android/os/Bundle)` | A `[Bundle](https://developer.android.com/reference/android/os/Bundle)` containing the extras for the app, or `null` if the package is not currently suspended.  
  
**See also:**

  * `[isPackageSuspended()](https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended\(\))`
  * `[Intent.ACTION_MY_PACKAGE_UNSUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)`
  * `[Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)`
  * `[Intent.EXTRA_SUSPENDED_PACKAGE_EXTRAS](https://developer.android.com/reference/android/content/Intent#EXTRA_SUSPENDED_PACKAGE_EXTRAS)`



### getSyntheticAppDetailsActivityEnabled

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean getSyntheticAppDetailsActivityEnabled ([String](https://developer.android.com/reference/java/lang/String) packageName)

Return whether a synthetic app details activity will be generated if the app has no enabled launcher activity.

Parameters  
---  
`packageName` |  `String`: The package name of the app.   
This value cannot be `null`.  
Returns  
---  
`boolean` | Returns the enabled state for the synthetic app details activity.  
  
### getSystemAvailableFeatures

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [FeatureInfo[]](https://developer.android.com/reference/android/content/pm/FeatureInfo) getSystemAvailableFeatures ()

Get a list of features that are available on the system.

Returns  
---  
`[FeatureInfo[]](https://developer.android.com/reference/android/content/pm/FeatureInfo)` | An array of FeatureInfo classes describing the features that are available on the system, or null if there are none(!!).  
  
### getSystemSharedLibraryNames

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [String[]](https://developer.android.com/reference/java/lang/String) getSystemSharedLibraryNames ()

Get a list of shared libraries that are available on the system.

Returns  
---  
`[String[]](https://developer.android.com/reference/java/lang/String)` | An array of shared library names that are available on the system, or null if none are installed.  
  
### getTargetSdkVersion

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public int getTargetSdkVersion ([String](https://developer.android.com/reference/java/lang/String) packageName)

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`int` | The target SDK version for the given package name.   
Value is 0 or greater  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
  
### getText

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence) getText ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int resid, 
                    [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo)

Retrieve text from a package. This is a low-level API used by the various package manager info structures (such as `[ComponentInfo](https://developer.android.com/reference/android/content/pm/ComponentInfo)` to implement retrieval of their associated labels and other text.

Parameters  
---  
`packageName` |  `String`: The name of the package that this text is coming from. Cannot be null.  
`resid` |  `int`: The resource identifier of the desired text. Cannot be 0.  
`appInfo` |  `ApplicationInfo`: Overall information about packageName. This may be null, in which case the application information will be retrieved for you if needed; if you already have this information around, it can be much more efficient to supply it here.  
Returns  
---  
`[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` | Returns a CharSequence holding the requested text. Returns null if the text could not be found for any reason.  
  
### getUserBadgedDrawableForDensity

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getUserBadgedDrawableForDensity ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable, 
                    [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user, 
                    [Rect](https://developer.android.com/reference/android/graphics/Rect) badgeLocation, 
                    int badgeDensity)

If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a badged copy of the given drawable allowing the user to distinguish it from the original drawable. The caller can specify the location in the bounds of the drawable to be badged where the badge should be applied as well as the density of the badge to be used. 

If the original drawable is a BitmapDrawable and the backing bitmap is mutable as per `[Bitmap.isMutable()](https://developer.android.com/reference/android/graphics/Bitmap#isMutable\(\))`, the badging is performed in place and the original drawable is returned. 

Parameters  
---  
`drawable` |  `Drawable`: The drawable to badge.   
This value cannot be `null`.  
`user` |  `UserHandle`: The target user.   
This value cannot be `null`.  
`badgeLocation` |  `Rect`: Where in the bounds of the badged drawable to place the badge. If it's `null`, the badge is applied on top of the entire drawable being badged.  
`badgeDensity` |  `int`: The optional desired density for the badge as per `[DisplayMetrics.densityDpi](https://developer.android.com/reference/android/util/DisplayMetrics#densityDpi)`. If it's not positive, the density of the display is used.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | A drawable that combines the original drawable and a badge as determined by the system.   
This value cannot be `null`.  
  
### getUserBadgedIcon

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) getUserBadgedIcon ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable, 
                    [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user)

If the target user is a managed profile, then this returns a badged copy of the given icon to be able to distinguish it from the original icon. For badging an arbitrary drawable use `[getUserBadgedDrawableForDensity(android.graphics.drawable.Drawable,UserHandle,android.graphics.Rect,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getUserBadgedDrawableForDensity\(android.graphics.drawable.Drawable,%20android.os.UserHandle,%20android.graphics.Rect,%20int\))`. 

If the original drawable is a BitmapDrawable and the backing bitmap is mutable as per `[Bitmap.isMutable()](https://developer.android.com/reference/android/graphics/Bitmap#isMutable\(\))`, the badging is performed in place and the original drawable is returned. 

Parameters  
---  
`drawable` |  `Drawable`: The drawable to badge.   
This value cannot be `null`.  
`user` |  `UserHandle`: The target user.   
This value cannot be `null`.  
Returns  
---  
`[Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable)` | A drawable that combines the original icon and a badge as determined by the system.   
This value cannot be `null`.  
  
### getUserBadgedLabel

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [CharSequence](https://developer.android.com/reference/java/lang/CharSequence) getUserBadgedLabel ([CharSequence](https://developer.android.com/reference/java/lang/CharSequence) label, 
                    [UserHandle](https://developer.android.com/reference/android/os/UserHandle) user)

If the target user is a managed profile of the calling user or the caller is itself a managed profile, then this returns a copy of the label with badging for accessibility services like talkback. E.g. passing in "Email" and it might return "Work Email" for Email in the work profile.

Parameters  
---  
`label` |  `CharSequence`: The label to change.   
This value cannot be `null`.  
`user` |  `UserHandle`: The target user.   
This value cannot be `null`.  
Returns  
---  
`[CharSequence](https://developer.android.com/reference/java/lang/CharSequence)` | A label that combines the original label and a badge as determined by the system.   
This value cannot be `null`.  
  
### getVerifiedSigningInfo

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static [SigningInfo](https://developer.android.com/reference/android/content/pm/SigningInfo) getVerifiedSigningInfo ([String](https://developer.android.com/reference/java/lang/String) path, 
                    int minAppSigningSchemeVersion)

Verifies and returns the [app signing](https://source.android.com/docs/security/features/apksigning) information of the file at the given path. This operation takes a few milliseconds. Unlike `[getPackageArchiveInfo(String,PackageInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#getPackageArchiveInfo\(java.lang.String,%20android.content.pm.PackageManager.PackageInfoFlags\))` with `[GET_SIGNING_CERTIFICATES](https://developer.android.com/reference/android/content/pm/PackageManager#GET_SIGNING_CERTIFICATES)`, this method does not require the file to be a package archive file.

Parameters  
---  
`path` |  `String`: This value cannot be `null`.  
`minAppSigningSchemeVersion` |  `int`: Value is one of the following: 

  * `[SigningInfo.VERSION_JAR](https://developer.android.com/reference/android/content/pm/SigningInfo#VERSION_JAR)`
  * `[SigningInfo.VERSION_SIGNING_BLOCK_V2](https://developer.android.com/reference/android/content/pm/SigningInfo#VERSION_SIGNING_BLOCK_V2)`
  * `[SigningInfo.VERSION_SIGNING_BLOCK_V3](https://developer.android.com/reference/android/content/pm/SigningInfo#VERSION_SIGNING_BLOCK_V3)`
  * `[SigningInfo.VERSION_SIGNING_BLOCK_V4](https://developer.android.com/reference/android/content/pm/SigningInfo#VERSION_SIGNING_BLOCK_V4)`

  
Returns  
---  
`[SigningInfo](https://developer.android.com/reference/android/content/pm/SigningInfo)` | This value cannot be `null`.  
Throws  
---  
`[SigningInfoException](https://developer.android.com/reference/android/content/pm/SigningInfoException)` | if the verification fails  
  
### getWhitelistedRestrictedPermissions

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> getWhitelistedRestrictedPermissions ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int whitelistFlag)

Gets the restricted permissions that have been whitelisted and the app is allowed to have them granted in their full form. 

Permissions can be hard restricted which means that the app cannot hold them or soft restricted where the app can hold the permission but in a weaker form. Whether a permission is `[hard restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)` or `[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)` depends on the permission declaration. Whitelisting a hard restricted permission allows for the to hold that permission and whitelisting a soft restricted permission allows the app to hold the permission in its full, unrestricted form. 

There are four allowlists: 
  1. one for cases where the system permission policy whitelists a permission This list corresponds to the`[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)` flag. Can only be accessed by pre-installed holders of a dedicated permission. 
  2. one for cases where the system whitelists the permission when upgrading from an OS version in which the permission was not restricted to an OS version in which the permission is restricted. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)` flag. Can be accessed by pre-installed holders of a dedicated permission or the installer on record. 
  3. one for cases where the installer of the package whitelists a permission. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)` flag. Can be accessed by pre-installed holders of a dedicated permission or the installer on record. 



**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Parameters  
---  
`packageName` |  `String`: The app for which to get whitelisted permissions.   
This value cannot be `null`.  
`whitelistFlag` |  `int`: The flag to determine which whitelist to query. Only one flag can be passed.s.   
Value is either `0` or a combination of the following: 

  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`

  
Returns  
---  
`[Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)>` | The whitelisted permissions that are on any of the whitelists you query for.   
This value cannot be `null`.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you try to access a whitelist that you have no access to.  
  
**See also:**

  * `[addWhitelistedRestrictedPermission(String,String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#addWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))`
  * `[removeWhitelistedRestrictedPermission(String,String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#removeWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))`
  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`



### getXml

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser) getXml ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int resid, 
                    [ApplicationInfo](https://developer.android.com/reference/android/content/pm/ApplicationInfo) appInfo)

Retrieve an XML file from a package. This is a low-level API used to retrieve XML meta data.

Parameters  
---  
`packageName` |  `String`: The name of the package that this xml is coming from. Cannot be null.  
`resid` |  `int`: The resource identifier of the desired xml. Cannot be 0.  
`appInfo` |  `ApplicationInfo`: Overall information about packageName. This may be null, in which case the application information will be retrieved for you if needed; if you already have this information around, it can be much more efficient to supply it here.  
Returns  
---  
`[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser)` | Returns an XmlPullParser allowing you to parse out the XML data. Returns null if the xml resource could not be found for any reason.  
  
### hasSigningCertificate

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean hasSigningCertificate (int uid, 
                    byte[] certificate, 
                    int type)

Searches the set of signing certificates by which the package(s) for the given uid has proven to have been signed. For multiple packages sharing the same uid, this will return the signing certificates found in the signing history of the "newest" package, where "newest" indicates the package with the newest signing certificate in the shared uid group. This method should be used instead of `getPackageInfo` with `GET_SIGNATURES` since it takes into account the possibility of signing certificate rotation, except in the case of packages that are signed by multiple certificates, for which signing certificate rotation is not supported. This method is analogous to using `getPackagesForUid` followed by `getPackageInfo` with `GET_SIGNING_CERTIFICATES`, selecting the `PackageInfo` of the newest-signed bpackage , and finally searching through the resulting `signingInfo` field to see if the desired certificate is there.

Parameters  
---  
`uid` |  `int`: uid whose signing certificates to check  
`certificate` |  `byte`: signing certificate for which to search.   
This value cannot be `null`.  
`type` |  `int`: representation of the `certificate`   
Value is one of the following: 

  * `[CERT_INPUT_RAW_X509](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_RAW_X509)`
  * `[CERT_INPUT_SHA256](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_SHA256)`

  
Returns  
---  
`boolean` | true if this package was or is signed by exactly the certificate `certificate`  
  
### hasSigningCertificate

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean hasSigningCertificate ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    byte[] certificate, 
                    int type)

Searches the set of signing certificates by which the given package has proven to have been signed. This should be used instead of `getPackageInfo` with `GET_SIGNATURES` since it takes into account the possibility of signing certificate rotation, except in the case of packages that are signed by multiple certificates, for which signing certificate rotation is not supported. This method is analogous to using `getPackageInfo` with `GET_SIGNING_CERTIFICATES` and then searching through the resulting `signingInfo` field to see if the desired certificate is present.

Parameters  
---  
`packageName` |  `String`: package whose signing certificates to check.   
This value cannot be `null`.  
`certificate` |  `byte`: signing certificate for which to search.   
This value cannot be `null`.  
`type` |  `int`: representation of the `certificate`   
Value is one of the following: 

  * `[CERT_INPUT_RAW_X509](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_RAW_X509)`
  * `[CERT_INPUT_SHA256](https://developer.android.com/reference/android/content/pm/PackageManager#CERT_INPUT_SHA256)`

  
Returns  
---  
`boolean` | true if this package was or is signed by exactly the certificate `certificate`  
  
### hasSystemFeature

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean hasSystemFeature ([String](https://developer.android.com/reference/java/lang/String) featureName)

Check whether the given feature name is one of the available features as returned by `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`. This tests for the presence of _any_ version of the given feature name; use `[hasSystemFeature(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String,%20int\))` to check for a minimum version.

Parameters  
---  
`featureName` |  `String`: This value cannot be `null`.  
Returns  
---  
`boolean` | Returns true if the devices supports the feature, else false.  
  
### hasSystemFeature

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean hasSystemFeature ([String](https://developer.android.com/reference/java/lang/String) featureName, 
                    int version)

Check whether the given feature name and version is one of the available features as returned by `[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\))`. Since features are defined to always be backwards compatible, this returns true if the available feature version is greater than or equal to the requested version.

Parameters  
---  
`featureName` |  `String`: This value cannot be `null`.  
`version` |  `int`  
Returns  
---  
`boolean` | Returns true if the devices supports the feature, else false.  
  
### isAppArchivable

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isAppArchivable ([String](https://developer.android.com/reference/java/lang/String) packageName)

Returns true if an app is archivable.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`boolean` |   
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if the given package name is not available to the caller.  
  
**See also:**

  * `[PackageInstaller.requestArchive](https://developer.android.com/reference/android/content/pm/PackageInstaller#requestArchive\(java.lang.String,%20android.content.IntentSender\))`



### isAutoRevokeWhitelisted

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isAutoRevokeWhitelisted ([String](https://developer.android.com/reference/java/lang/String) packageName)

Checks whether an application is exempt from having its permissions be automatically revoked when the app is unused for an extended period of time. Only the installer on record that installed the given package, or a holder of `WHITELIST_AUTO_REVOKE_PERMISSIONS` is allowed to call this. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Parameters  
---  
`packageName` |  `String`: The app for which to set exemption.   
This value cannot be `null`.  
Returns  
---  
`boolean` | Whether the app is whitelisted.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you you have no access to this.  
  
**See also:**

  * `[setAutoRevokeWhitelisted(String, boolean)](https://developer.android.com/reference/android/content/pm/PackageManager#setAutoRevokeWhitelisted\(java.lang.String,%20boolean\))`



### isAutoRevokeWhitelisted

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isAutoRevokeWhitelisted ()

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Returns  
---  
`boolean` | whether this package is whitelisted from having its runtime permission be auto-revoked if unused for an extended period of time.  
  
### isDefaultApplicationIcon

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isDefaultApplicationIcon ([Drawable](https://developer.android.com/reference/android/graphics/drawable/Drawable) drawable)

Returns if the provided drawable represents the default activity icon provided by the system. PackageManager silently returns a default application icon for any package/activity if the app itself does not define one or if the system encountered any error when loading the icon. Developers can use this to check implement app specific logic around retrying or caching.

Parameters  
---  
`drawable` |  `Drawable`: This value cannot be `null`.  
Returns  
---  
`boolean` | true if the drawable represents the default activity icon, false otherwise  
  
**See also:**

  * `[getDefaultActivityIcon()](https://developer.android.com/reference/android/content/pm/PackageManager#getDefaultActivityIcon\(\))`
  * `[getActivityIcon(ComponentName)](https://developer.android.com/reference/android/content/pm/PackageManager#getActivityIcon\(android.content.ComponentName\))`
  * `[LauncherActivityInfo.getIcon(int)](https://developer.android.com/reference/android/content/pm/LauncherActivityInfo#getIcon\(int\))`



### isDeviceUpgrading

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isDeviceUpgrading ()

Returns true if the device is upgrading, such as first boot after OTA.

Returns  
---  
`boolean` |   
  
### isInstantApp

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean isInstantApp ()

Gets whether this application is an instant app.

Returns  
---  
`boolean` | Whether caller is an instant app.  
  
**See also:**

  * `[isInstantApp(String)](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))`
  * `[updateInstantAppCookie(byte[])](https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie\(byte\[\]\))`
  * `[getInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))`
  * `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`



### isInstantApp

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean isInstantApp ([String](https://developer.android.com/reference/java/lang/String) packageName)

Gets whether the given package is an instant app.

Parameters  
---  
`packageName` |  `String`: The package to check.   
This value cannot be `null`.  
Returns  
---  
`boolean` | Whether the given package is an instant app.  
  
**See also:**

  * `[isInstantApp()](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))`
  * `[updateInstantAppCookie(byte[])](https://developer.android.com/reference/android/content/pm/PackageManager#updateInstantAppCookie\(byte\[\]\))`
  * `[getInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))`
  * `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`
  * `[clearInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))`



### isPackageStopped

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isPackageStopped ([String](https://developer.android.com/reference/java/lang/String) packageName)

Query if an app is currently stopped.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`boolean` | `true` if the given package is stopped, `false` otherwise  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if the package could not be found.  
  
**See also:**

  * `[ApplicationInfo.FLAG_STOPPED](https://developer.android.com/reference/android/content/pm/ApplicationInfo#FLAG_STOPPED)`



### isPackageSuspended

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isPackageSuspended ([String](https://developer.android.com/reference/java/lang/String) packageName)

Query if an app is currently suspended.

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
Returns  
---  
`boolean` | `true` if the given package is suspended, `false` otherwise  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if the package could not be found.  
  
**See also:**

  * `[isPackageSuspended()](https://developer.android.com/reference/android/content/pm/PackageManager#isPackageSuspended\(\))`



### isPackageSuspended

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean isPackageSuspended ()

Apps can query this to know if they have been suspended. A system app with the permission `android.permission.SUSPEND_APPS` can put any app on the device into a suspended state. 

While in this state, the application's notifications will be hidden, any of its started activities will be stopped and it will not be able to show toasts or dialogs or play audio. When the user tries to launch a suspended app, the system will, instead, show a dialog to the user informing them that they cannot use this app while it is suspended. 

When an app is put into this state, the broadcast action `[Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)` will be delivered to any of its broadcast receivers that included this action in their intent-filters, _including manifest receivers._ Similarly, a broadcast action `[Intent.ACTION_MY_PACKAGE_UNSUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)` is delivered when a previously suspended app is taken out of this state. Apps are expected to use these to gracefully deal with transitions to and from this state.

Returns  
---  
`boolean` | `true` if the calling package has been suspended, `false` otherwise.  
  
**See also:**

  * `[getSuspendedPackageAppExtras()](https://developer.android.com/reference/android/content/pm/PackageManager#getSuspendedPackageAppExtras\(\))`
  * `[Intent.ACTION_MY_PACKAGE_SUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_SUSPENDED)`
  * `[Intent.ACTION_MY_PACKAGE_UNSUSPENDED](https://developer.android.com/reference/android/content/Intent#ACTION_MY_PACKAGE_UNSUSPENDED)`



### isPermissionRevokedByPolicy

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean isPermissionRevokedByPolicy ([String](https://developer.android.com/reference/java/lang/String) permName, 
                    [String](https://developer.android.com/reference/java/lang/String) packageName)

Checks whether a particular permissions has been revoked for a package by policy. Typically the device owner or the profile owner may apply such a policy. The user cannot grant policy revoked permissions, hence the only way for an app to get such a permission is by a policy change.

Parameters  
---  
`permName` |  `String`: The name of the permission you are checking for.   
This value cannot be `null`.  
`packageName` |  `String`: The name of the package you are checking against.   
This value cannot be `null`.  
Returns  
---  
`boolean` | Whether the permission is restricted by policy.  
  
### isSafeMode

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract boolean isSafeMode ()

Return whether the device has been booted into safe mode.

Returns  
---  
`boolean` |   
  
### parseAndroidManifest

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public T parseAndroidManifest ([File](https://developer.android.com/reference/java/io/File) apkFile, 
                    [Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction)

Retrieve AndroidManifest.xml information for the given application apk file. 

Example: 
    
    
    Bundle result;
    try {
        result = getContext().getPackageManager().parseAndroidManifest(apkFile,
                xmlResourceParser -> {
                    Bundle bundle = new Bundle();
                    // Search the start tag
                    int type;
                    while ((type = xmlResourceParser.next()) != XmlPullParser.START_TAG
                            && type != XmlPullParser.END_DOCUMENT) {
                    }
                    if (type != XmlPullParser.START_TAG) {
                        return bundle;
                    }
    
                    // Start to read the tags and attributes from the xmlResourceParser
                    if (!xmlResourceParser.getName().equals("manifest")) {
                        return bundle;
                    }
                    String packageName = xmlResourceParser.getAttributeValue(null, "package");
                    bundle.putString("package", packageName);
    
                    // Continue to read the tags and attributes from the xmlResourceParser
    
                    return bundle;
                });
    } catch (IOException e) {
    }
    

Note: When the parserFunction is invoked, the client can read the AndroidManifest.xml information by the XmlResourceParser object. After leaving the parserFunction, the XmlResourceParser object will be closed. The caller should also handle the exception for calling this method.   
This method may take several seconds to complete, so it should only be called from a worker thread. Parameters  
---  
`apkFile` |  `File`: The file of an application apk.   
This value cannot be `null`.  
`parserFunction` |  `Function`: The parserFunction will be invoked with the XmlResourceParser object after getting the AndroidManifest.xml of an application package.   
This value cannot be `null`.  
Returns  
---  
`T` | Returns the result of the `[Function.apply(Object)](https://developer.android.com/reference/java/util/function/Function#apply\(T\))`.  
Throws  
---  
`[IOException](https://developer.android.com/reference/java/io/IOException)` | if the AndroidManifest.xml of an application package cannot be read or accessed.  
  
### parseAndroidManifest

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public T parseAndroidManifest ([ParcelFileDescriptor](https://developer.android.com/reference/android/os/ParcelFileDescriptor) apkFileDescriptor, 
                    [Function](https://developer.android.com/reference/java/util/function/Function)<[XmlResourceParser](https://developer.android.com/reference/android/content/res/XmlResourceParser), T> parserFunction)

Similar to `[parseAndroidManifest(File,Function)](https://developer.android.com/reference/android/content/pm/PackageManager#parseAndroidManifest\(java.io.File,%20java.util.function.Function<android.content.res.XmlResourceParser,T>\))`, but accepting a file descriptor instead of a File object.   
This method may take several seconds to complete, so it should only be called from a worker thread.

Parameters  
---  
`apkFileDescriptor` |  `ParcelFileDescriptor`: The file descriptor of an application apk. The parserFunction will be invoked with the XmlResourceParser object after getting the AndroidManifest.xml of an application package.   
This value cannot be `null`.  
`parserFunction` |  `Function`: This value cannot be `null`.  
Returns  
---  
`T` | Returns the result of the `[Function.apply(Object)](https://developer.android.com/reference/java/util/function/Function#apply\(T\))`.  
Throws  
---  
`[IOException](https://developer.android.com/reference/java/io/IOException)` | if the AndroidManifest.xml of an application package cannot be read or accessed.  
  
### queryActivityProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryActivityProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName)

Returns the property definition for all <activity> and <activity-alias> tags. 

If the property is not defined with any <activity> and <activity-alias> tag, returns and empty list.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` | This value cannot be `null`.  
  
### queryApplicationProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryApplicationProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName)

Returns the property definition for all <application> tags. 

If the property is not defined with any <application> tag, returns and empty list.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` | This value cannot be `null`.  
  
### queryBroadcastReceivers

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryBroadcastReceivers ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[queryBroadcastReceivers(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | This value cannot be `null`.  
  
### queryBroadcastReceivers

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryBroadcastReceivers ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Retrieve all receivers that can handle a broadcast of the given intent. Use `[queryBroadcastReceivers(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryBroadcastReceivers\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`intent` |  `Intent`: The desired intent as per resolveActivity().   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | Returns a List of ResolveInfo objects containing one entry for each matching receiver, ordered from best to worst. If there are no matching receivers, returns an empty list.   
This value cannot be `null`.  
  
### queryContentProviders

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)> queryContentProviders ([String](https://developer.android.com/reference/java/lang/String) processName, 
                    int uid, 
                    int flags)

Retrieve content provider information. 

_Note: unlike most other methods, an empty result set is indicated by a null return instead of an empty list._ Use `[queryContentProviders(String,int,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders\(java.lang.String,%20int,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed.

Parameters  
---  
`processName` |  `String`: If non-null, limits the returned providers to only those that are hosted by the given process. If null, all content providers are returned.  
`uid` |  `int`: If processName is non-null, this is the required uid owning the requested content providers.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)>` | A list of `[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` objects containing one entry for each provider either matching processName or, if processName is null, all known content providers. _If there are no matching providers, null is returned._  
  
### queryContentProviders

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)> queryContentProviders ([String](https://developer.android.com/reference/java/lang/String) processName, 
                    int uid, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[queryContentProviders(String,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryContentProviders\(java.lang.String,%20int,%20int\))`.

Parameters  
---  
`processName` |  `String`: This value may be `null`.  
`uid` |  `int`  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)>` | This value cannot be `null`.  
  
### queryInstrumentation

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)> queryInstrumentation ([String](https://developer.android.com/reference/java/lang/String) targetPackage, 
                    int flags)

Retrieve information about available instrumentation code. May be used to retrieve either all instrumentation code, or only the code targeting a particular package.

Parameters  
---  
`targetPackage` |  `String`: If null, all instrumentation is returned; only the instrumentation targeting this package name is returned.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)>` | A list of `[InstrumentationInfo](https://developer.android.com/reference/android/content/pm/InstrumentationInfo)` objects containing one entry for each matching instrumentation. If there are no instrumentation available, returns an empty list.   
This value cannot be `null`.  
  
### queryIntentActivities

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivities ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[queryIntentActivities(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | This value cannot be `null`.  
  
### queryIntentActivities

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivities ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Retrieve all activities that can be performed for the given intent. Use `[queryIntentActivities(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`intent` |  `Intent`: The desired intent as per resolveActivity().   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned. The most important is `[MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)`, to limit the resolution to only those activities that support the `[Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)`. Or, set `[MATCH_ALL](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_ALL)` to prevent any filtering of the results.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | Returns a List of ResolveInfo objects containing one entry for each matching activity, ordered from best to worst. In other words, the first item is what would be returned by `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. If there are no matching activities, an empty list is returned.   
This value cannot be `null`.  
  
### queryIntentActivityOptions

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivityOptions ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) caller, 
                    [Intent[]](https://developer.android.com/reference/android/content/Intent) specifics, 
                    [Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Retrieve a set of activities that should be presented to the user as similar options. This is like `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`, except it also allows you to supply a list of more explicit Intents that you would like to resolve to particular options, and takes care of returning the final ResolveInfo list in a reasonable order, with no duplicates, based on those inputs. Use `[queryIntentActivityOptions(ComponentName,List,Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions\(android.content.ComponentName,%20java.util.List<android.content.Intent>,%20android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`caller` |  `ComponentName`: The class name of the activity that is making the request. This activity will never appear in the output list. Can be null.  
`specifics` |  `Intent`: An array of Intents that should be resolved to the first specific results. Can be null.  
`intent` |  `Intent`: The desired intent as per resolveActivity().   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned. The most important is `[MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)`, to limit the resolution to only those activities that support the `[Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | Returns a List of ResolveInfo objects containing one entry for each matching activity. The list is ordered first by all of the intents resolved in specifics and then any additional activities that can handle intent but did not get included by one of the specifics intents. If there are no matching activities, an empty list is returned.   
This value cannot be `null`.  
  
### queryIntentActivityOptions

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentActivityOptions ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) caller, 
                    [List](https://developer.android.com/reference/java/util/List)<[Intent](https://developer.android.com/reference/android/content/Intent)> specifics, 
                    [Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[queryIntentActivityOptions(ComponentName,Intent[],Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivityOptions\(android.content.ComponentName,%20android.content.Intent\[\],%20android.content.Intent,%20int\))`.

Parameters  
---  
`caller` |  `ComponentName`: This value may be `null`.  
`specifics` |  `List`: This value may be `null`.  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | This value cannot be `null`.  
  
### queryIntentContentProviders

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentContentProviders ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[queryIntentContentProviders(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | This value cannot be `null`.  
  
### queryIntentContentProviders

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentContentProviders ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Retrieve all providers that can match the given intent. Use `[queryIntentContentProviders(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentContentProviders\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`intent` |  `Intent`: An intent containing all of the desired specification (action, data, type, category, and/or component).   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | Returns a List of ResolveInfo objects containing one entry for each matching provider, ordered from best to worst. If there are no matching services, returns an empty list.   
This value cannot be `null`.  
  
### queryIntentServices

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentServices ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Retrieve all services that can match the given intent. Use `[queryIntentServices(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`intent` |  `Intent`: The desired intent as per resolveService().   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | Returns a List of ResolveInfo objects containing one entry for each matching service, ordered from best to worst. In other words, the first item is what would be returned by `[resolveService(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. If there are no matching services, returns an empty list.   
This value cannot be `null`.  
  
### queryIntentServices

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)> queryIntentServices ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[queryIntentServices(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentServices\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)>` | This value cannot be `null`.  
  
### queryPermissionsByGroup

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [List](https://developer.android.com/reference/java/util/List)<[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)> queryPermissionsByGroup ([String](https://developer.android.com/reference/java/lang/String) permissionGroup, 
                    int flags)

Query for all of the permissions associated with a particular group.

Parameters  
---  
`permissionGroup` |  `String`: The fully qualified name (i.e. com.google.permission.LOGIN) of the permission group you are interested in. Use `null` to find all of the permissions not associated with a group.  
`flags` |  `int`: Additional option flags to modify the data returned.   
Value is either `0` or 

  * `[GET_META_DATA](https://developer.android.com/reference/android/content/pm/PackageManager#GET_META_DATA)`

  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)>` | Returns a list of `[PermissionInfo](https://developer.android.com/reference/android/content/pm/PermissionInfo)` containing information about all of the permissions in the given group.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a group with the given name cannot be found on the system.  
  
### queryProviderProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryProviderProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName)

Returns the property definition for all <provider> tags. 

If the property is not defined with any <provider> tag, returns and empty list.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` | This value cannot be `null`.  
  
### queryReceiverProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryReceiverProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName)

Returns the property definition for all <receiver> tags. 

If the property is not defined with any <receiver> tag, returns and empty list.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` | This value cannot be `null`.  
  
### queryServiceProperty

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)> queryServiceProperty ([String](https://developer.android.com/reference/java/lang/String) propertyName)

Returns the property definition for all <service> tags. 

If the property is not defined with any <service> tag, returns and empty list.

Parameters  
---  
`propertyName` |  `String`: This value cannot be `null`.  
Returns  
---  
`[List](https://developer.android.com/reference/java/util/List)<[PackageManager.Property](https://developer.android.com/reference/android/content/pm/PackageManager.Property)>` | This value cannot be `null`.  
  
### relinquishUpdateOwnership

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void relinquishUpdateOwnership ([String](https://developer.android.com/reference/java/lang/String) targetPackage)

Attempt to relinquish the update ownership of the given package. Only the current update owner of the given package can use this API.

Parameters  
---  
`targetPackage` |  `String`: The installed package whose update owner will be changed.   
This value cannot be `null`.  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the given package is invalid.  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you are not the current update owner of the given package.  
  
**See also:**

  * `[PackageInstaller.SessionParams.setRequestUpdateOwnership](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequestUpdateOwnership\(boolean\))`



### removePackageFromPreferred

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void removePackageFromPreferred ([String](https://developer.android.com/reference/java/lang/String) packageName)

**This method was deprecated in API level 15.**  
This function no longer does anything. It is the platform's responsibility to assign preferred activities and this cannot be modified directly. To determine the activities resolved by the platform, use `[resolveActivity(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` or `[queryIntentActivities(Intent, ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#queryIntentActivities\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))`. To configure an app to be responsible for a particular role and to check current role holders, see `[RoleManager](https://developer.android.com/reference/android/app/role/RoleManager)`. 

Parameters  
---  
`packageName` |  `String`: This value cannot be `null`.  
  
### removePermission

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void removePermission ([String](https://developer.android.com/reference/java/lang/String) permName)

Removes a permission that was previously added with `[addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))`. The same ownership rules apply \-- you are only allowed to remove permissions that you are allowed to add.

Parameters  
---  
`permName` |  `String`: The name of the permission to remove.   
This value cannot be `null`.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you are not allowed to remove the given permission name.  
  
**See also:**

  * `[addPermission(PermissionInfo)](https://developer.android.com/reference/android/content/pm/PackageManager#addPermission\(android.content.pm.PermissionInfo\))`



### removeWhitelistedRestrictedPermission

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean removeWhitelistedRestrictedPermission ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    [String](https://developer.android.com/reference/java/lang/String) permName, 
                    int whitelistFlags)

Removes a whitelisted restricted permission for an app. 

Permissions can be hard restricted which means that the app cannot hold them or soft restricted where the app can hold the permission but in a weaker form. Whether a permission is `[hard restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_HARD_RESTRICTED)` or `[soft restricted](https://developer.android.com/reference/android/content/pm/PermissionInfo#FLAG_SOFT_RESTRICTED)` depends on the permission declaration. Whitelisting a hard restricted permission allows for the to hold that permission and whitelisting a soft restricted permission allows the app to hold the permission in its full, unrestricted form. 

There are four whitelists: 
  1. one for cases where the system permission policy whitelists a permission This list corresponds to the `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)` flag. Can only be modified by pre-installed holders of a dedicated permission. 
  2. one for cases where the system whitelists the permission when upgrading from an OS version in which the permission was not restricted to an OS version in which the permission is restricted. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)` flag. Can be modified by pre-installed holders of a dedicated permission. The installer on record can only remove permissions from this whitelist. 
  3. one for cases where the installer of the package whitelists a permission. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)` flag. Can be modified by pre-installed holders of a dedicated permission or the installer on record. 
  4. one for cases where the system exempts the permission when upgrading from an OS version in which the permission was not restricted to an OS version in which the permission is restricted. This list corresponds to the `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)` flag. Can be modified by pre-installed holders of a dedicated permission. The installer on record can only remove permissions from this allowlist. 



You need to specify the whitelists for which to set the whitelisted permissions which will clear the previous whitelisted permissions and replace them with the provided ones. 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Parameters  
---  
`packageName` |  `String`: The app for which to get whitelisted permissions.   
This value cannot be `null`.  
`permName` |  `String`: The whitelisted permission to remove.   
This value cannot be `null`.  
`whitelistFlags` |  `int`: The whitelists from which to remove. Passing multiple flags updates all specified whitelists.   
Value is either `0` or a combination of the following: 

  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`

  
Returns  
---  
`boolean` | Whether the permission was removed from the whitelist.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you try to modify a whitelist that you have no access to.  
  
**See also:**

  * `[getWhitelistedRestrictedPermissions(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#getWhitelistedRestrictedPermissions\(java.lang.String,%20int\))`
  * `[addWhitelistedRestrictedPermission(String,String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#addWhitelistedRestrictedPermission\(java.lang.String,%20java.lang.String,%20int\))`
  * `[FLAG_PERMISSION_WHITELIST_SYSTEM](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_SYSTEM)`
  * `[FLAG_PERMISSION_WHITELIST_UPGRADE](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_UPGRADE)`
  * `[FLAG_PERMISSION_WHITELIST_INSTALLER](https://developer.android.com/reference/android/content/pm/PackageManager#FLAG_PERMISSION_WHITELIST_INSTALLER)`



### requestChecksums

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void requestChecksums ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    boolean includeSplits, 
                    int required, 
                    [List](https://developer.android.com/reference/java/util/List)<[Certificate](https://developer.android.com/reference/java/security/cert/Certificate)> trustedInstallers, 
                    [PackageManager.OnChecksumsReadyListener](https://developer.android.com/reference/android/content/pm/PackageManager.OnChecksumsReadyListener) onChecksumsReadyListener)

Requests the checksums for APKs within a package. The checksums will be returned asynchronously via onChecksumsReadyListener. By default returns all readily available checksums: \- enforced by platform, \- enforced by installer. If caller needs a specific checksum kind, they can specify it as required. **Caution: Android can not verify installer-provided checksums. Make sure you specify trusted installers.**

Parameters  
---  
`packageName` |  `String`: whose checksums to return.   
This value cannot be `null`.  
`includeSplits` |  `boolean`: whether to include checksums for non-base splits.  
`required` |  `int`: explicitly request the checksum types. May incur significant CPU/memory/disk usage.   
Value is either `0` or a combination of the following: 

  * `[Checksum.TYPE_WHOLE_MERKLE_ROOT_4K_SHA256](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_WHOLE_MERKLE_ROOT_4K_SHA256)`
  * `[Checksum.TYPE_WHOLE_MD5](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_WHOLE_MD5)`
  * `[Checksum.TYPE_WHOLE_SHA1](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_WHOLE_SHA1)`
  * `[Checksum.TYPE_WHOLE_SHA256](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_WHOLE_SHA256)`
  * `[Checksum.TYPE_WHOLE_SHA512](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_WHOLE_SHA512)`
  * `[Checksum.TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_PARTIAL_MERKLE_ROOT_1M_SHA256)`
  * `[Checksum.TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512](https://developer.android.com/reference/android/content/pm/Checksum#TYPE_PARTIAL_MERKLE_ROOT_1M_SHA512)`

  
`trustedInstallers` |  `List`: for checksums enforced by installer, which installers are to be trusted. `[TRUST_ALL](https://developer.android.com/reference/android/content/pm/PackageManager#TRUST_ALL)` will return checksums from any installer, `[TRUST_NONE](https://developer.android.com/reference/android/content/pm/PackageManager#TRUST_NONE)` disables optimized installer-enforced checksums, otherwise the list has to be non-empty list of certificates.   
This value cannot be `null`.  
`onChecksumsReadyListener` |  `PackageManager.OnChecksumsReadyListener`: called once when the results are available.   
This value cannot be `null`.  
Throws  
---  
`[PackageManager.NameNotFoundException](https://developer.android.com/reference/android/content/pm/PackageManager.NameNotFoundException)` | if a package with the given name cannot be found on the system.  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the list of trusted installer certificates is empty.  
`[CertificateEncodingException](https://developer.android.com/reference/java/security/cert/CertificateEncodingException)` | if an encoding error occurs for trustedInstallers.  
  
### resolveActivity

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo) resolveActivity ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[resolveActivity(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` | This value may be `null`.  
  
### resolveActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo) resolveActivity ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Determine the best action to perform for a given Intent. This is how `[Intent.resolveActivity](https://developer.android.com/reference/android/content/Intent#resolveActivity\(android.content.pm.PackageManager\))` finds an activity if a class has not been explicitly specified. 

_Note:_ if using an implicit Intent (without an explicit ComponentName specified), be sure to consider whether to set the `[MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)` only flag. You need to do so to resolve the activity in the same way that `[android.content.Context.startActivity(Intent)](https://developer.android.com/reference/android/content/Context#startActivity\(android.content.Intent\))` and `[Intent.resolveActivity(PackageManager)](https://developer.android.com/reference/android/content/Intent#resolveActivity\(android.content.pm.PackageManager\))` do. 

Use `[resolveActivity(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveActivity\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed. Parameters  
---  
`intent` |  `Intent`: An intent containing all of the desired specification (action, data, type, category, and/or component).   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned. The most important is `[MATCH_DEFAULT_ONLY](https://developer.android.com/reference/android/content/pm/PackageManager#MATCH_DEFAULT_ONLY)`, to limit the resolution to only those activities that support the `[Intent.CATEGORY_DEFAULT](https://developer.android.com/reference/android/content/Intent#CATEGORY_DEFAULT)`.  
Returns  
---  
`[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` | Returns a ResolveInfo object containing the final activity intent that was determined to be the best action. Returns null if no matching activity was found. If multiple matching activities are found and there is no default set, returns a ResolveInfo object containing something else, such as the activity resolver.  
  
### resolveContentProvider

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo) resolveContentProvider ([String](https://developer.android.com/reference/java/lang/String) authority, 
                    [PackageManager.ComponentInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentInfoFlags) flags)

See `[resolveContentProvider(String,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider\(java.lang.String,%20int\))`.

Parameters  
---  
`authority` |  `String`: This value cannot be `null`.  
`flags` |  `PackageManager.ComponentInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` | This value may be `null`.  
  
### resolveContentProvider

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo) resolveContentProvider ([String](https://developer.android.com/reference/java/lang/String) authority, 
                    int flags)

Find a single content provider by its authority. 

Example:
    
    
    Uri uri = Uri.parse("content://com.example.app.provider/table1");
    ProviderInfo info = packageManager.resolveContentProvider(uri.getAuthority(), flags);
    

Use `[resolveContentProvider(String,ComponentInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveContentProvider\(java.lang.String,%20android.content.pm.PackageManager.ComponentInfoFlags\))` when long flags are needed. Parameters  
---  
`authority` |  `String`: The authority of the provider to find.   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` | A `[ProviderInfo](https://developer.android.com/reference/android/content/pm/ProviderInfo)` object containing information about the provider. If a provider was not found, returns null.  
  
### resolveService

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo) resolveService ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    int flags)

Determine the best service to handle for a given Intent. Use `[resolveService(Intent,ResolveInfoFlags)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20android.content.pm.PackageManager.ResolveInfoFlags\))` when long flags are needed.

Parameters  
---  
`intent` |  `Intent`: An intent containing all of the desired specification (action, data, type, category, and/or component).   
This value cannot be `null`.  
`flags` |  `int`: Additional option flags to modify the data returned.  
Returns  
---  
`[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` | Returns a ResolveInfo object containing the final service intent that was determined to be the best action. Returns null if no matching service was found.  
  
### resolveService

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public [ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo) resolveService ([Intent](https://developer.android.com/reference/android/content/Intent) intent, 
                    [PackageManager.ResolveInfoFlags](https://developer.android.com/reference/android/content/pm/PackageManager.ResolveInfoFlags) flags)

See `[resolveService(Intent,int)](https://developer.android.com/reference/android/content/pm/PackageManager#resolveService\(android.content.Intent,%20int\))`.

Parameters  
---  
`intent` |  `Intent`: This value cannot be `null`.  
`flags` |  `PackageManager.ResolveInfoFlags`: This value cannot be `null`.  
Returns  
---  
`[ResolveInfo](https://developer.android.com/reference/android/content/pm/ResolveInfo)` | This value may be `null`.  
  
### setApplicationCategoryHint

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void setApplicationCategoryHint ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int categoryHint)

Provide a hint of what the `[ApplicationInfo.category](https://developer.android.com/reference/android/content/pm/ApplicationInfo#category)` value should be for the given package. 

This hint can only be set by the app which installed this package, as determined by `[getInstallerPackageName(String)](https://developer.android.com/reference/android/content/pm/PackageManager#getInstallerPackageName\(java.lang.String\))`.

Parameters  
---  
`packageName` |  `String`: the package to change the category hint for.   
This value cannot be `null`.  
`categoryHint` |  `int`: the category hint to set.   
Value is one of the following: 

  * `[ApplicationInfo.CATEGORY_UNDEFINED](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_UNDEFINED)`
  * `[ApplicationInfo.CATEGORY_GAME](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_GAME)`
  * `[ApplicationInfo.CATEGORY_AUDIO](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_AUDIO)`
  * `[ApplicationInfo.CATEGORY_VIDEO](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_VIDEO)`
  * `[ApplicationInfo.CATEGORY_IMAGE](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_IMAGE)`
  * `[ApplicationInfo.CATEGORY_SOCIAL](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_SOCIAL)`
  * `[ApplicationInfo.CATEGORY_NEWS](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_NEWS)`
  * `[ApplicationInfo.CATEGORY_MAPS](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_MAPS)`
  * `[ApplicationInfo.CATEGORY_PRODUCTIVITY](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_PRODUCTIVITY)`
  * `[ApplicationInfo.CATEGORY_ACCESSIBILITY](https://developer.android.com/reference/android/content/pm/ApplicationInfo#CATEGORY_ACCESSIBILITY)`

  
  
### setApplicationEnabledSetting

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void setApplicationEnabledSetting ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    int newState, 
                    int flags)

Set the enabled setting for an application This setting will override any enabled state which may have been set by the application in its manifest. It also overrides the enabled state set in the manifest for any of the application's components. It does not override any enabled state set by `[setComponentEnabledSetting(ComponentName, int, int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))` for any of the application's components.

Parameters  
---  
`packageName` |  `String`: The package name of the application to enable.   
This value cannot be `null`.  
`newState` |  `int`: The new enabled state for the application.   
Value is one of the following: 

  * `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)`
  * `[COMPONENT_ENABLED_STATE_ENABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_ENABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_USER](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_USER)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)`

  
`flags` |  `int`: Optional behavior flags.   
Value is either `0` or a combination of the following: 

  * `[DONT_KILL_APP](https://developer.android.com/reference/android/content/pm/PackageManager#DONT_KILL_APP)`
  * `[SYNCHRONOUS](https://developer.android.com/reference/android/content/pm/PackageManager#SYNCHRONOUS)`

  
  
### setAutoRevokeWhitelisted

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public boolean setAutoRevokeWhitelisted ([String](https://developer.android.com/reference/java/lang/String) packageName, 
                    boolean whitelisted)

Marks an application exempt from having its permissions be automatically revoked when the app is unused for an extended period of time. Only the installer on record that installed the given package is allowed to call this. Packages start in whitelisted state, and it is the installer's responsibility to un-whitelist the packages it installs, unless auto-revoking permissions from that package would cause breakages beyond having to re-request the permission(s). 

**Note:** In retrospect it would have been preferred to use more inclusive terminology when naming this API. Similar APIs added will refrain from using the term "whitelist". 

Parameters  
---  
`packageName` |  `String`: The app for which to set exemption.   
This value cannot be `null`.  
`whitelisted` |  `boolean`: Whether the app should be whitelisted.  
Returns  
---  
`boolean` | whether any change took effect.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if you you have no access to modify this.  
  
**See also:**

  * `[isAutoRevokeWhitelisted()](https://developer.android.com/reference/android/content/pm/PackageManager#isAutoRevokeWhitelisted\(\))`



### setComponentEnabledSetting

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void setComponentEnabledSetting ([ComponentName](https://developer.android.com/reference/android/content/ComponentName) componentName, 
                    int newState, 
                    int flags)

Set the enabled setting for a package component (activity, receiver, service, provider). This setting will override any enabled state which may have been set by the component in its manifest. 

Consider using `[setComponentEnabledSettings(List)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSettings\(java.util.List<android.content.pm.PackageManager.ComponentEnabledSetting>\))` if multiple components need to be updated atomically.

Parameters  
---  
`componentName` |  `ComponentName`: The component to enable.   
This value cannot be `null`.  
`newState` |  `int`: The new enabled state for the component.   
Value is one of the following: 

  * `[COMPONENT_ENABLED_STATE_DEFAULT](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DEFAULT)`
  * `[COMPONENT_ENABLED_STATE_ENABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_ENABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_USER](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_USER)`
  * `[COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED](https://developer.android.com/reference/android/content/pm/PackageManager#COMPONENT_ENABLED_STATE_DISABLED_UNTIL_USED)`

  
`flags` |  `int`: Optional behavior flags.   
Value is either `0` or a combination of the following: 

  * `[DONT_KILL_APP](https://developer.android.com/reference/android/content/pm/PackageManager#DONT_KILL_APP)`
  * `[SYNCHRONOUS](https://developer.android.com/reference/android/content/pm/PackageManager#SYNCHRONOUS)`

  
  
### setComponentEnabledSettings

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void setComponentEnabledSettings ([List](https://developer.android.com/reference/java/util/List)<[PackageManager.ComponentEnabledSetting](https://developer.android.com/reference/android/content/pm/PackageManager.ComponentEnabledSetting)> settings)

Set the enabled settings for package components such as activities, receivers, services and providers. This setting will override any enabled state which may have been set by the component in its manifest. 

This api accepts a list of component changes, and applies them all atomically. The application can use this api if components have dependencies and need to be updated atomically. 

The permission is not required if target components are running under the same uid with the caller.

Parameters  
---  
`settings` |  `List`: The list of component enabled settings to update. Note that an `[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` is thrown if the duplicated component name is in the list or there's a conflict `[DONT_KILL_APP](https://developer.android.com/reference/android/content/pm/PackageManager#DONT_KILL_APP)` flag between different components in the same package.   
This value cannot be `null`.  
  
**See also:**

  * `[setComponentEnabledSetting(ComponentName,int,int)](https://developer.android.com/reference/android/content/pm/PackageManager#setComponentEnabledSetting\(android.content.ComponentName,%20int,%20int\))`



### setInstallerPackageName

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void setInstallerPackageName ([String](https://developer.android.com/reference/java/lang/String) targetPackage, 
                    [String](https://developer.android.com/reference/java/lang/String) installerPackageName)

Change the installer associated with a given package. There are limitations on how the installer package can be changed; in particular: 

  * A SecurityException will be thrown if installerPackageName is not signed with the same certificate as the calling application. 
  * A SecurityException will be thrown if targetPackage already has an installer package, and that installer package is not signed with the same certificate as the calling application. 

Parameters  
---  
`targetPackage` |  `String`: The installed package whose installer will be changed.   
This value cannot be `null`.  
`installerPackageName` |  `String`: The package name of the new installer. May be null to clear the association.  
  
### setMimeGroup

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public void setMimeGroup ([String](https://developer.android.com/reference/java/lang/String) mimeGroup, 
                    [Set](https://developer.android.com/reference/java/util/Set)<[String](https://developer.android.com/reference/java/lang/String)> mimeTypes)

Sets MIME group's MIME types. Libraries should use a reverse-DNS prefix followed by a ':' character and library-specific group name to avoid namespace collisions, e.g. "com.example:myFeature".

Parameters  
---  
`mimeGroup` |  `String`: MIME group to modify.   
This value cannot be `null`.  
`mimeTypes` |  `Set`: new MIME types contained by MIME group.   
This value cannot be `null`.  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the MIME group was not declared in the manifest.  
  
### updateInstantAppCookie

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void updateInstantAppCookie (byte[] cookie)

Updates the instant application cookie for the calling app. Non instant apps and apps that were instant but were upgraded to normal apps can still access this API. For instant apps this cookie is cached for some time after uninstall while for normal apps the cookie is deleted after the app is uninstalled. The cookie is always present while the app is installed. The cookie size is limited by `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`. Passing `null` or an empty array clears the cookie. 

Parameters  
---  
`cookie` |  `byte`: The cookie data.   
This value may be `null`.  
Throws  
---  
`[IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException)` | if the array exceeds max cookie size.  
  
**See also:**

  * `[isInstantApp()](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(\))`
  * `[isInstantApp(String)](https://developer.android.com/reference/android/content/pm/PackageManager#isInstantApp\(java.lang.String\))`
  * `[getInstantAppCookieMaxBytes()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookieMaxBytes\(\))`
  * `[getInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#getInstantAppCookie\(\))`
  * `[clearInstantAppCookie()](https://developer.android.com/reference/android/content/pm/PackageManager#clearInstantAppCookie\(\))`



### verifyPendingInstall

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public abstract void verifyPendingInstall (int id, 
                    int verificationCode)

Allows a package listening to the `[package verification broadcast](https://developer.android.com/reference/android/content/Intent#ACTION_PACKAGE_NEEDS_VERIFICATION)` to respond to the package manager. The response must include the `verificationCode` which is one of `[PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` or `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`.

Parameters  
---  
`id` |  `int`: pending package identifier as passed via the `[PackageManager.EXTRA_VERIFICATION_ID](https://developer.android.com/reference/android/content/pm/PackageManager#EXTRA_VERIFICATION_ID)` Intent extra.  
`verificationCode` |  `int`: either `[PackageManager.VERIFICATION_ALLOW](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_ALLOW)` or `[PackageManager.VERIFICATION_REJECT](https://developer.android.com/reference/android/content/pm/PackageManager#VERIFICATION_REJECT)`.  
Throws  
---  
`[SecurityException](https://developer.android.com/reference/java/lang/SecurityException)` | if the caller does not have the PACKAGE_VERIFICATION_AGENT permission.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-28 UTC."],[],[]] 

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
  * Polski
  * Português – Brasil
  * Tiếng Việt
  * 中文 – 简体
  * 日本語
  * 한국어


