---
url: https://developer.android.com/reference/android/Manifest.permission
title: Manifest.permission \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:26.950712+00:00
---

# Manifest.permission  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/android/Manifest.permission

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

Summary: Constants | Ctors | Inherited Methods

# Manifest.permission

* * *

[Kotlin](https://developer.android.com/reference/kotlin/android/Manifest.permission "View this page in Kotlin") |Java

` public static final class Manifest.permission `   
` extends [Object](https://developer.android.com/reference/java/lang/Object) ` ` `

[java.lang.Object](https://developer.android.com/reference/java/lang/Object)  
---  
↳ | android.Manifest.permission   
  


* * *

## Summary

### Constants  
  
---  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCEPT_HANDOVER](https://developer.android.com/reference/android/Manifest.permission#ACCEPT_HANDOVER)` Allows a calling app to continue a call which was started in another app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_BACKGROUND_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION)` Allows an app to access location in the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_BIOMETRIC_SENSOR_STRENGTHS](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BIOMETRIC_SENSOR_STRENGTHS)` Allows an application to retrieve the sensor security strengths of the biometric sensors.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_BLOBS_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BLOBS_ACROSS_USERS)` Allows an application to access data blobs across users.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_CHECKIN_PROPERTIES](https://developer.android.com/reference/android/Manifest.permission#ACCESS_CHECKIN_PROPERTIES)` Allows read/write access to the "properties" table in the checkin database, to change values that get uploaded.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)` Allows an app to access approximate location.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)` Allows an app to access precise location.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_HID](https://developer.android.com/reference/android/Manifest.permission#ACCESS_HID)` Required by apps wanting to query for and/or access Human Interface Device (HID) nodes using `[HidManager](https://developer.android.com/reference/android/hardware/hid/HidManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_HIDDEN_PROFILES](https://developer.android.com/reference/android/Manifest.permission#ACCESS_HIDDEN_PROFILES)` Allows applications to access profiles with `android.content.pm.UserProperties#PROFILE_API_VISIBILITY_HIDDEN` user property, e.g.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_LAUNCHER_DATA](https://developer.android.com/reference/android/Manifest.permission#ACCESS_LAUNCHER_DATA)` This permission protects a content provider within home/launcher applications, enabling management of home screen metadata such as shortcut placement, launch intents, and labels.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_LOCAL_NETWORK](https://developer.android.com/reference/android/Manifest.permission#ACCESS_LOCAL_NETWORK)` Required to be able to advertise and connect to local network devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_LOCATION_EXTRA_COMMANDS](https://developer.android.com/reference/android/Manifest.permission#ACCESS_LOCATION_EXTRA_COMMANDS)` Allows an application to access extra location provider commands.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_MEDIA_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION)` Allows an application to access any geographic locations persisted in the user's shared collection.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE)` Allows applications to access information about networks.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_NOTIFICATION_POLICY](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NOTIFICATION_POLICY)` Marker permission for applications that wish to access notification policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCESS_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE)` Allows applications to access information about Wi-Fi networks.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACCOUNT_MANAGER](https://developer.android.com/reference/android/Manifest.permission#ACCOUNT_MANAGER)` Allows applications to call into AccountAuthenticators.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ACTIVITY_RECOGNITION](https://developer.android.com/reference/android/Manifest.permission#ACTIVITY_RECOGNITION)` Allows an application to recognize physical activity.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ADD_VOICEMAIL](https://developer.android.com/reference/android/Manifest.permission#ADD_VOICEMAIL)` Allows an application to add voicemails into the system.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ANSWER_PHONE_CALLS](https://developer.android.com/reference/android/Manifest.permission#ANSWER_PHONE_CALLS)` Allows the app to answer an incoming phone call.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[APPLY_PICTURE_PROFILE](https://developer.android.com/reference/android/Manifest.permission#APPLY_PICTURE_PROFILE)` Allows an app to apply a `[ERROR(/MediaQualityManager.PictureProfile)](https://developer.android.com/)` to a layer via `[ERROR(/MediaCodec.PARAMETER_KEY_PICTURE_PROFILE)](https://developer.android.com/)` and, additionally, system apps via `[ERROR(/SurfaceControl.Transaction#setPictureProfileHandle)](https://developer.android.com/)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BATTERY_STATS](https://developer.android.com/reference/android/Manifest.permission#BATTERY_STATS)` Allows an application to collect battery statistics Protection level: signature|privileged|development   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_ACCESSIBILITY_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_ACCESSIBILITY_SERVICE)` Must be required by an `[AccessibilityService](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_ALTERNATIVE_MESSAGE_TRANSPORT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_ALTERNATIVE_MESSAGE_TRANSPORT_SERVICE)` Permission needed to ensure that only the system process can bind with the `[AlternativeMessageTransportService](https://developer.android.com/reference/android/service/messaging/AlternativeMessageTransportService)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_APPWIDGET](https://developer.android.com/reference/android/Manifest.permission#BIND_APPWIDGET)` Allows an application to tell the AppWidget service which application can access AppWidget's data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_APP_FUNCTION_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_APP_FUNCTION_SERVICE)` Must be required by an `[AppFunctionService](https://developer.android.com/reference/android/app/appfunctions/AppFunctionService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_AUTOFILL_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_AUTOFILL_SERVICE)` Must be required by a `[AutofillService](https://developer.android.com/reference/android/service/autofill/AutofillService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CALL_REDIRECTION_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CALL_REDIRECTION_SERVICE)` Must be required by a `[CallRedirectionService](https://developer.android.com/reference/android/telecom/CallRedirectionService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CARRIER_MESSAGING_CLIENT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CARRIER_MESSAGING_CLIENT_SERVICE)` A subclass of `[CarrierMessagingClientService](https://developer.android.com/reference/android/service/carrier/CarrierMessagingClientService)` must be protected with this permission.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CARRIER_MESSAGING_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CARRIER_MESSAGING_SERVICE)` _This constant was deprecated in API level 23. Use`[BIND_CARRIER_SERVICES](https://developer.android.com/reference/android/Manifest.permission#BIND_CARRIER_SERVICES)` instead_  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CARRIER_SERVICES](https://developer.android.com/reference/android/Manifest.permission#BIND_CARRIER_SERVICES)` The system process that is allowed to bind to services in carrier apps will have this permission.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CHOOSER_TARGET_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CHOOSER_TARGET_SERVICE)` _This constant was deprecated in API level 30. For publishing direct share targets, please follow the instructions in https://developer.android.com/training/sharing/receive.html#providing-direct-share-targets instead._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_COMPANION_DEVICE_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_COMPANION_DEVICE_SERVICE)` Must be required by any `[CompanionDeviceService](https://developer.android.com/reference/android/companion/CompanionDeviceService)`s to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CONDITION_PROVIDER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CONDITION_PROVIDER_SERVICE)` Must be required by a `[ConditionProviderService](https://developer.android.com/reference/android/service/notification/ConditionProviderService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CONTENT_RESTRICTION_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CONTENT_RESTRICTION_SERVICE)` Permission required to bind content restriction service Protection level: signature   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CONTENT_SAFETY_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CONTENT_SAFETY_SERVICE)` Ensures only the platform can bind to the content safety service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CONTROLS](https://developer.android.com/reference/android/Manifest.permission#BIND_CONTROLS)` Allows SystemUI to request third party controls.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_CREDENTIAL_PROVIDER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_CREDENTIAL_PROVIDER_SERVICE)` Must be required by a CredentialProviderService to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_DATA_MIGRATION_FOR_PRIVATECOMPUTE](https://developer.android.com/reference/android/Manifest.permission#BIND_DATA_MIGRATION_FOR_PRIVATECOMPUTE)` Allows the system to bind to an application's data migration service for Private Compute.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_DEVICE_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN)` Must be required by device administration receiver, to ensure that only the system can interact with it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_DREAM_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_DREAM_SERVICE)` Must be required by an `[DreamService](https://developer.android.com/reference/android/service/dreams/DreamService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_INCALL_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_INCALL_SERVICE)` Must be required by a `[InCallService](https://developer.android.com/reference/android/telecom/InCallService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_INPUT_METHOD](https://developer.android.com/reference/android/Manifest.permission#BIND_INPUT_METHOD)` Must be required by an `[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_MIDI_DEVICE_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_MIDI_DEVICE_SERVICE)` Must be required by an `[MidiDeviceService](https://developer.android.com/reference/android/media/midi/MidiDeviceService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_NFC_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NFC_SERVICE)` Must be required by a `[HostApduService](https://developer.android.com/reference/android/nfc/cardemulation/HostApduService)` or `[OffHostApduService](https://developer.android.com/reference/android/nfc/cardemulation/OffHostApduService)` to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_NOTIFICATION_LISTENER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NOTIFICATION_LISTENER_SERVICE)` Must be required by an `[NotificationListenerService](https://developer.android.com/reference/android/service/notification/NotificationListenerService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_PCC_EGRESS_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_PCC_EGRESS_SERVICE)` Allows a system application to bind to the Private Compute Core egress service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_PRINT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_PRINT_SERVICE)` Must be required by a `[PrintService](https://developer.android.com/reference/android/printservice/PrintService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_QUICK_ACCESS_WALLET_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_QUICK_ACCESS_WALLET_SERVICE)` Must be required by a `[QuickAccessWalletService](https://developer.android.com/reference/android/service/quickaccesswallet/QuickAccessWalletService)` to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_QUICK_SETTINGS_TILE](https://developer.android.com/reference/android/Manifest.permission#BIND_QUICK_SETTINGS_TILE)` Allows an application to bind to third party quick settings tiles.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_REMOTEVIEWS](https://developer.android.com/reference/android/Manifest.permission#BIND_REMOTEVIEWS)` Must be required by a `[RemoteViewsService](https://developer.android.com/reference/android/widget/RemoteViewsService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_SCREENING_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_SCREENING_SERVICE)` Must be required by a `[CallScreeningService](https://developer.android.com/reference/android/telecom/CallScreeningService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_TELECOM_CONNECTION_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_TELECOM_CONNECTION_SERVICE)` Must be required by a `[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_TEXT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_TEXT_SERVICE)` Must be required by a TextService (e.g. SpellCheckerService) to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_TV_AD_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_TV_AD_SERVICE)` Must be required by a android.media.tv.ad.TvAdService to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_TV_INPUT](https://developer.android.com/reference/android/Manifest.permission#BIND_TV_INPUT)` Must be required by a `[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)` to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_TV_INTERACTIVE_APP](https://developer.android.com/reference/android/Manifest.permission#BIND_TV_INTERACTIVE_APP)` Must be required by a `[TvInteractiveAppService](https://developer.android.com/reference/android/media/tv/interactive/TvInteractiveAppService)` to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_VISUAL_VOICEMAIL_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VISUAL_VOICEMAIL_SERVICE)` Must be required by a link `[VisualVoicemailService](https://developer.android.com/reference/android/telephony/VisualVoicemailService)` to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_VOICE_INTERACTION](https://developer.android.com/reference/android/Manifest.permission#BIND_VOICE_INTERACTION)` Must be required by a `[VoiceInteractionService](https://developer.android.com/reference/android/service/voice/VoiceInteractionService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_VPN_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VPN_SERVICE)` Must be required by a `[VpnService](https://developer.android.com/reference/android/net/VpnService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_VR_LISTENER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VR_LISTENER_SERVICE)` Must be required by an `[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BIND_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#BIND_WALLPAPER)` Must be required by a `[WallpaperService](https://developer.android.com/reference/android/service/wallpaper/WallpaperService)`, to ensure that only the system can bind to it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH)` Allows applications to connect to paired bluetooth devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADMIN)` Allows applications to discover and pair bluetooth devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH_ADVERTISE](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADVERTISE)` Required to be able to advertise to nearby Bluetooth devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH_CONNECT](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_CONNECT)` Required to be able to connect to paired Bluetooth devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_PRIVILEGED)` Allows applications to pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BLUETOOTH_SCAN](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_SCAN)` Required to be able to discover and pair nearby Bluetooth devices.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BODY_SENSORS](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS)` Allows an application to access data from sensors that the user uses to measure what is happening inside their body, such as heart rate.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BODY_SENSORS_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS_BACKGROUND)` Allows an application to access data from sensors that the user uses to measure what is happening inside their body, such as heart rate.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BROADCAST_PACKAGE_REMOVED](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_PACKAGE_REMOVED)` Allows an application to broadcast a notification that an application package has been removed.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BROADCAST_SMS](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_SMS)` Allows an application to broadcast an SMS receipt notification.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BROADCAST_STICKY](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_STICKY)` Allows an application to broadcast sticky intents.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[BROADCAST_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_WAP_PUSH)` Allows an application to broadcast a WAP PUSH receipt notification.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CALL_COMPANION_APP](https://developer.android.com/reference/android/Manifest.permission#CALL_COMPANION_APP)` Allows an app which implements the `[InCallService](https://developer.android.com/reference/android/telecom/InCallService)` API to be eligible to be enabled as a calling companion app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CALL_PHONE](https://developer.android.com/reference/android/Manifest.permission#CALL_PHONE)` Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CALL_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#CALL_PRIVILEGED)` Allows an application to call any phone number, including emergency numbers, without going through the Dialer user interface for the user to confirm the call being placed.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CAMERA](https://developer.android.com/reference/android/Manifest.permission#CAMERA)` Required to be able to access the camera device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CAPTURE_AUDIO_OUTPUT](https://developer.android.com/reference/android/Manifest.permission#CAPTURE_AUDIO_OUTPUT)` Allows an application to capture audio output.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CAPTURE_KEYBOARD](https://developer.android.com/reference/android/Manifest.permission#CAPTURE_KEYBOARD)` Allows the currently focused application to be able to consume keys before Android system get chance to process system keys and shortcuts.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CHANGE_COMPONENT_ENABLED_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_COMPONENT_ENABLED_STATE)` Allows an application to change whether an application component (other than its own) is enabled or not.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CHANGE_CONFIGURATION](https://developer.android.com/reference/android/Manifest.permission#CHANGE_CONFIGURATION)` Allows an application to modify the current configuration, such as locale.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CHANGE_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_NETWORK_STATE)` Allows applications to change network connectivity state.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CHANGE_WIFI_MULTICAST_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_MULTICAST_STATE)` Allows applications to enter Wi-Fi Multicast mode.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CHANGE_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE)` Allows applications to change Wi-Fi connectivity state.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CLEAR_APP_CACHE](https://developer.android.com/reference/android/Manifest.permission#CLEAR_APP_CACHE)` Allows an application to clear the caches of all installed applications on the device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CONFIGURE_WIFI_DISPLAY](https://developer.android.com/reference/android/Manifest.permission#CONFIGURE_WIFI_DISPLAY)` Allows an application to configure and connect to Wifi displays   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CONTROL_LOCATION_UPDATES](https://developer.android.com/reference/android/Manifest.permission#CONTROL_LOCATION_UPDATES)` Allows enabling/disabling location update notifications from the radio.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS](https://developer.android.com/reference/android/Manifest.permission#CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS)` Allows a browser to invoke the set of query apis to get metadata about credential candidates prepared during the CredentialManager.prepareGetCredential API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS](https://developer.android.com/reference/android/Manifest.permission#CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS)` Allows specifying candidate credential providers to be queried in Credential Manager get flows, or to be preferred as a default in the Credential Manager create flows.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[CREDENTIAL_MANAGER_SET_ORIGIN](https://developer.android.com/reference/android/Manifest.permission#CREDENTIAL_MANAGER_SET_ORIGIN)` Allows a browser to invoke credential manager APIs on behalf of another RP.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DELETE_CACHE_FILES](https://developer.android.com/reference/android/Manifest.permission#DELETE_CACHE_FILES)` Old permission for deleting an app's cache files, no longer used, but signals for us to quietly ignore calls instead of throwing an exception.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DELETE_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#DELETE_PACKAGES)` Allows an application to delete packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DELIVER_COMPANION_MESSAGES](https://developer.android.com/reference/android/Manifest.permission#DELIVER_COMPANION_MESSAGES)` Allows an application to deliver companion messages to system   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DETECT_SCREEN_CAPTURE](https://developer.android.com/reference/android/Manifest.permission#DETECT_SCREEN_CAPTURE)` Allows an application to get notified when a screen capture of its windows is attempted.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DETECT_SCREEN_RECORDING](https://developer.android.com/reference/android/Manifest.permission#DETECT_SCREEN_RECORDING)` Allows an application to get notified when it is being recorded.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DIAGNOSTIC](https://developer.android.com/reference/android/Manifest.permission#DIAGNOSTIC)` Allows applications to RW to diagnostic resources.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DISABLE_KEYGUARD](https://developer.android.com/reference/android/Manifest.permission#DISABLE_KEYGUARD)` Allows applications to disable the keyguard if it is not secure.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[DUMP](https://developer.android.com/reference/android/Manifest.permission#DUMP)` Allows an application to retrieve state dump information from system services.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[ENFORCE_UPDATE_OWNERSHIP](https://developer.android.com/reference/android/Manifest.permission#ENFORCE_UPDATE_OWNERSHIP)` Allows an application to indicate via `[PackageInstaller.SessionParams.setRequestUpdateOwnership(boolean)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequestUpdateOwnership\(boolean\))` that it has the intention of becoming the update owner.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[EXECUTE_APP_ACTION](https://developer.android.com/reference/android/Manifest.permission#EXECUTE_APP_ACTION)` Allows an assistive application to perform actions on behalf of users inside of applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[EXECUTE_APP_FUNCTIONS](https://developer.android.com/reference/android/Manifest.permission#EXECUTE_APP_FUNCTIONS)` Allows an application to perform actions on behalf of users inside of applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[EXPAND_STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#EXPAND_STATUS_BAR)` Allows an application to expand or collapse the status bar.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FACTORY_TEST](https://developer.android.com/reference/android/Manifest.permission#FACTORY_TEST)` Run as a manufacturer test application, running as the root user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_CAMERA](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CAMERA)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "camera".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_CONNECTED_DEVICE](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_CONNECTED_DEVICE)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "connectedDevice".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_DATA_SYNC](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_DATA_SYNC)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "dataSync".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_HEALTH](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_HEALTH)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "health".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_LOCATION)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "location".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_MEDIA_PLAYBACK](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MEDIA_PLAYBACK)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaPlayback".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_MEDIA_PROCESSING](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MEDIA_PROCESSING)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaProcessing".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_MEDIA_PROJECTION](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MEDIA_PROJECTION)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaProjection".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_MICROPHONE](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_MICROPHONE)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "microphone".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_PHONE_CALL](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_PHONE_CALL)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "phoneCall".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_REMOTE_MESSAGING](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_REMOTE_MESSAGING)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "remoteMessaging".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_SPECIAL_USE](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_SPECIAL_USE)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "specialUse".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[FOREGROUND_SERVICE_SYSTEM_EXEMPTED](https://developer.android.com/reference/android/Manifest.permission#FOREGROUND_SERVICE_SYSTEM_EXEMPTED)` Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "systemExempted".   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[GET_ACCOUNTS](https://developer.android.com/reference/android/Manifest.permission#GET_ACCOUNTS)` Allows access to the list of accounts in the Accounts Service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[GET_ACCOUNTS_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#GET_ACCOUNTS_PRIVILEGED)` Allows access to the list of accounts in the Accounts Service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[GET_PACKAGE_SIZE](https://developer.android.com/reference/android/Manifest.permission#GET_PACKAGE_SIZE)` Allows an application to find out the space used by any package.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[GET_TASKS](https://developer.android.com/reference/android/Manifest.permission#GET_TASKS)` _This constant was deprecated in API level 21. No longer enforced._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[GLOBAL_SEARCH](https://developer.android.com/reference/android/Manifest.permission#GLOBAL_SEARCH)` This permission can be used on content providers to allow the global search system to access their data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[HIDE_OVERLAY_WINDOWS](https://developer.android.com/reference/android/Manifest.permission#HIDE_OVERLAY_WINDOWS)` Allows an app to prevent non-system-overlay windows from being drawn on top of it   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[HIGH_SAMPLING_RATE_SENSORS](https://developer.android.com/reference/android/Manifest.permission#HIGH_SAMPLING_RATE_SENSORS)` Allows an app to access sensor data with a sampling rate greater than 200 Hz.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INSTALL_LOCATION_PROVIDER](https://developer.android.com/reference/android/Manifest.permission#INSTALL_LOCATION_PROVIDER)` Allows an application to install a location provider into the Location Manager.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#INSTALL_PACKAGES)` Allows an application to install packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INSTALL_PACKAGES_AS_REGISTERED_APP_STORE](https://developer.android.com/reference/android/Manifest.permission#INSTALL_PACKAGES_AS_REGISTERED_APP_STORE)` Permission to allow installing and updating apps as a registered app store.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INSTALL_SHORTCUT](https://developer.android.com/reference/android/Manifest.permission#INSTALL_SHORTCUT)` Allows an application to install a shortcut in Launcher.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INSTANT_APP_FOREGROUND_SERVICE](https://developer.android.com/reference/android/Manifest.permission#INSTANT_APP_FOREGROUND_SERVICE)` Allows an instant app to create foreground services.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INTERACT_ACROSS_PROFILES](https://developer.android.com/reference/android/Manifest.permission#INTERACT_ACROSS_PROFILES)` Allows interaction across profiles in the same profile group.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[INTERNET](https://developer.android.com/reference/android/Manifest.permission#INTERNET)` Allows applications to open network sockets.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[KILL_BACKGROUND_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#KILL_BACKGROUND_PROCESSES)` Allows an application to call `[ActivityManager.killBackgroundProcesses(String)](https://developer.android.com/reference/android/app/ActivityManager#killBackgroundProcesses\(java.lang.String\))`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE](https://developer.android.com/reference/android/Manifest.permission#LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE)` Allows an application to capture screen content to perform a screenshot using the intent action `[Intent.ACTION_LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE](https://developer.android.com/reference/android/content/Intent#ACTION_LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK](https://developer.android.com/reference/android/Manifest.permission#LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK)` An application needs this permission for `[Settings.ACTION_SETTINGS_EMBED_DEEP_LINK_ACTIVITY](https://developer.android.com/reference/android/provider/Settings#ACTION_SETTINGS_EMBED_DEEP_LINK_ACTIVITY)` to show its `[Activity](https://developer.android.com/reference/android/app/Activity)` embedded in Settings app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[LOADER_USAGE_STATS](https://developer.android.com/reference/android/Manifest.permission#LOADER_USAGE_STATS)` Allows a data loader to read a package's access logs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[LOCATION_HARDWARE](https://developer.android.com/reference/android/Manifest.permission#LOCATION_HARDWARE)` Allows an application to use location features in hardware, such as the geofencing api.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[LOCK_APPS](https://developer.android.com/reference/android/Manifest.permission#LOCK_APPS)` Permission granted to apps holding the `[RoleManager.ROLE_HOME](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_HOME)` role that allows them to enable app lock.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_ASSISTANT_AUDIO](https://developer.android.com/reference/android/Manifest.permission#MANAGE_ASSISTANT_AUDIO)` Allows control of audio behavior related to Assistant experiences, including routing, mode change and volume control of the Assistant audio stream.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_CONTACTS)` Allows an application to manage user's contacts.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_LOCK_STATE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_LOCK_STATE)` Allows financed device kiosk apps to perform actions on the Device Lock service Protection level: internal|role Intended for use by the FINANCED_DEVICE_KIOSK role only.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ACCESSIBILITY](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACCESSIBILITY)` Allows an application to manage policy related to accessibility.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT)` Allows an application to set policy related to account management.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` Allows an application to set device policies outside the current user that are required for securing device ownership without accessing user data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` Allows an application to set device policies outside the current user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL)` Allows an application to set device policies outside the current user that are critical for securing data within the current user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_AIRPLANE_MODE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_AIRPLANE_MODE)` Allows an application to set policy related to airplane mode.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_APPS_CONTROL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_APPS_CONTROL)` Allows an application to manage policy regarding modifying applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_APP_FUNCTIONS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_APP_FUNCTIONS)` Allows an application to manage policy related to AppFunctions.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_APP_RESTRICTIONS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_APP_RESTRICTIONS)` Allows an application to manage application restrictions.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_APP_USER_DATA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_APP_USER_DATA)` Allows an application to manage policy related to application user data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ASSIST_CONTENT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ASSIST_CONTENT)` Allows an application to set policy related to sending assist content to a privileged app such as the Assistant app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_AUDIO_OUTPUT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_AUDIO_OUTPUT)` Allows an application to set policy related to audio output.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_AUTOFILL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_AUTOFILL)` Allows an application to set policy related to autofill.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_BACKUP_SERVICE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_BACKUP_SERVICE)` Allows an application to manage backup service policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL)` Allows an application to manage policy related to block package uninstallation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_BLUETOOTH](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_BLUETOOTH)` Allows an application to set policy related to bluetooth.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_BUGREPORT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_BUGREPORT)` Allows an application to request bugreports with user consent.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_CALLS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_CALLS)` Allows an application to manage calling policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_CAMERA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_CAMERA)` Allows an application to set policy related to restricting a user's ability to use or enable and disable the camera.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_CAMERA_TOGGLE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_CAMERA_TOGGLE)` Allows an application to manage policy related to camera toggle.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_CERTIFICATES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_CERTIFICATES)` Allows an application to set policy related to certificates.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE)` Allows an application to manage policy related to common criteria mode.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_CONTENT_PROTECTION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_CONTENT_PROTECTION)` Allows an application to manage policy related to content protection.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES)` Allows an application to manage debugging features policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_DEFAULT_SMS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_DEFAULT_SMS)` Allows an application to set policy related to the default sms application.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS)` Allows an application to manage policy related to device identifiers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_DISPLAY](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_DISPLAY)` Allows an application to set policy related to the display.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_FACTORY_RESET](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_FACTORY_RESET)` Allows an application to set policy related to factory reset.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_FUN](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_FUN)` Allows an application to set policy related to fun.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_INPUT_METHODS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_INPUT_METHODS)` Allows an application to set policy related to input methods.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES)` Allows an application to manage installing from unknown sources policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES)` Allows an application to set policy related to keeping uninstalled packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_KEYGUARD](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_KEYGUARD)` Allows an application to manage policy related to keyguard features.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_LOCALE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_LOCALE)` Allows an application to set policy related to locale.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_LOCATION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_LOCATION)` Allows an application to set policy related to location.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_LOCK](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_LOCK)` Allows an application to lock a profile or the device with the appropriate cross-user permission.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS)` Allows an application to set policy related to lock credentials.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_LOCK_TASK](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_LOCK_TASK)` Allows an application to manage lock task policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS)` Allows an application to set policy related to subscriptions downloaded by an admin.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_METERED_DATA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_METERED_DATA)` Allows an application to manage policy related to metered data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MICROPHONE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MICROPHONE)` Allows an application to set policy related to restricting a user's ability to use or enable and disable the microphone.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE)` Allows an application to manage policy related to microphone toggle.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MOBILE_NETWORK](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MOBILE_NETWORK)` Allows an application to set policy related to mobile networks.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MODIFY_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MODIFY_USERS)` Allows an application to manage policy preventing users from modifying users.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_MTE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_MTE)` Allows an application to manage policy related to the Memory Tagging Extension (MTE).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION)` Allows an application to set policy related to nearby communications (e.g. Beam and nearby streaming).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_NETWORK_LOGGING](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_NETWORK_LOGGING)` Allows an application to set policy related to network logging.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY)` Allows an application to manage the identity of the managing organization.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_OVERRIDE_APN](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_OVERRIDE_APN)` Allows an application to set policy related to override APNs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PACKAGE_STATE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PACKAGE_STATE)` Allows an application to set policy related to hiding and suspending packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA)` Allows an application to set policy related to physical media.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PRINTING](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PRINTING)` Allows an application to set policy related to printing.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PRIVATE_DNS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PRIVATE_DNS)` Allows an application to set policy related to private DNS.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PROFILES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PROFILES)` Allows an application to set policy related to profiles.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PROFILE_INTERACTION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PROFILE_INTERACTION)` Allows an application to set policy related to interacting with profiles (e.g. Disallowing cross-profile copy and paste).   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_PROXY](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_PROXY)` Allows an application to set a network-independent global HTTP proxy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES)` Allows an application query system updates.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_RESET_PASSWORD](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_RESET_PASSWORD)` Allows an application to force set a new device unlock password or a managed profile challenge on current user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS)` Allows an application to set policy related to restricting the user from configuring private DNS.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS)` Allows an application to set the grant state of runtime permissions on packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND)` Allows an application to set policy related to users running in the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SAFE_BOOT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SAFE_BOOT)` Allows an application to manage safe boot policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SCREEN_CAPTURE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SCREEN_CAPTURE)` Allows an application to set policy related to screen capture.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SCREEN_CONTENT](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SCREEN_CONTENT)` Allows an application to set policy related to the usage of the contents of the screen.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SECURITY_LOGGING](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SECURITY_LOGGING)` Allows an application to set policy related to security logging.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SETTINGS)` Allows an application to set policy related to settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SMS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SMS)` Allows an application to set policy related to sms.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_STATUS_BAR)` Allows an application to set policy related to the status bar.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE)` Allows an application to set support messages for when a user action is affected by an active policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS)` Allows an application to set policy related to suspending personal apps.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SYSTEM_APPS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SYSTEM_APPS)` Allows an application to manage policy related to system apps.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS)` Allows an application to set policy related to system dialogs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_SYSTEM_UPDATES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_SYSTEM_UPDATES)` Allows an application to set policy related to system updates.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_THREAD_NETWORK](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_THREAD_NETWORK)` Allows an application to set policy related to [Thread](https://www.threadgroup.org) network.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_TIME](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_TIME)` Allows an application to manage device policy relating to time.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_UNIVERSAL_CLIPBOARD](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_UNIVERSAL_CLIPBOARD)` Allows an application to manage policy related to Universal Clipboard feature.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING)` Allows an application to set policy related to usb data signalling.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER)` Allows an application to set policy related to usb file transfers.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_USERS)` Allows an application to set policy related to users.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_VPN](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_VPN)` Allows an application to set policy related to VPNs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_WALLPAPER)` Allows an application to set policy related to the wallpaper.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_WIFI](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_WIFI)` Allows an application to set policy related to Wifi.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_WINDOWS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_WINDOWS)` Allows an application to set policy related to windows.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DEVICE_POLICY_WIPE_DATA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_WIPE_DATA)` Allows an application to manage policy related to wiping data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_DOCUMENTS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DOCUMENTS)` Allows an application to manage access to documents, usually as part of a document picker.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE)` Allows an application a broad access to external storage in scoped storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_MEDIA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_MEDIA)` Allows an application to modify and delete media files on this device or any connected storage device without user confirmation.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_ONGOING_CALLS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_ONGOING_CALLS)` Allows to query ongoing call details and manage ongoing calls Protection level: signature|appop   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_OWN_CALLS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_OWN_CALLS)` Allows a calling application which manages its own calls through the self-managed `[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)` APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_PERIPHERAL_CUSTOMIZATION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_PERIPHERAL_CUSTOMIZATION)` Allows an application to manage peripheral customization.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_WIFI_INTERFACES](https://developer.android.com/reference/android/Manifest.permission#MANAGE_WIFI_INTERFACES)` Allows applications to get notified when a Wi-Fi interface request cannot be satisfied without tearing down one or more other interfaces, and provide a decision whether to approve the request or reject it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MANAGE_WIFI_NETWORK_SELECTION](https://developer.android.com/reference/android/Manifest.permission#MANAGE_WIFI_NETWORK_SELECTION)` This permission is used to let OEMs grant their trusted app access to a subset of privileged wifi APIs to improve wifi performance.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MASTER_CLEAR](https://developer.android.com/reference/android/Manifest.permission#MASTER_CLEAR)` Not for use by third-party applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MEDIA_CONTENT_CONTROL](https://developer.android.com/reference/android/Manifest.permission#MEDIA_CONTENT_CONTROL)` Allows an application to know what content is playing and control its playback.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MEDIA_ROUTING_CONTROL](https://developer.android.com/reference/android/Manifest.permission#MEDIA_ROUTING_CONTROL)` Allows an application to control the routing of media apps.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MODIFY_AUDIO_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#MODIFY_AUDIO_SETTINGS)` Allows an application to modify global audio settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MODIFY_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#MODIFY_PHONE_STATE)` Allows modification of the telephony state - power on, mmi, etc.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MOUNT_FORMAT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_FORMAT_FILESYSTEMS)` Allows formatting file systems for removable storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[MOUNT_UNMOUNT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_UNMOUNT_FILESYSTEMS)` Allows mounting and unmounting file systems for removable storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[NEARBY_WIFI_DEVICES](https://developer.android.com/reference/android/Manifest.permission#NEARBY_WIFI_DEVICES)` Required to be able to advertise and connect to nearby devices via Wi-Fi.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[NFC](https://developer.android.com/reference/android/Manifest.permission#NFC)` Allows applications to perform I/O operations over NFC.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[NFC_PREFERRED_PAYMENT_INFO](https://developer.android.com/reference/android/Manifest.permission#NFC_PREFERRED_PAYMENT_INFO)` Allows applications to receive NFC preferred payment service information.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[NFC_TRANSACTION_EVENT](https://developer.android.com/reference/android/Manifest.permission#NFC_TRANSACTION_EVENT)` Allows applications to receive NFC transaction events.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[OVERRIDE_MEDIA_SESSION_OWNER](https://developer.android.com/reference/android/Manifest.permission#OVERRIDE_MEDIA_SESSION_OWNER)` Allows an application to override the owner of a MediaSession.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[OVERRIDE_WIFI_CONFIG](https://developer.android.com/reference/android/Manifest.permission#OVERRIDE_WIFI_CONFIG)` Allows an application to modify any wifi configuration, even if created by another application.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PACKAGE_USAGE_STATS](https://developer.android.com/reference/android/Manifest.permission#PACKAGE_USAGE_STATS)` Allows an application to collect component usage statistics Declaring the permission implies intention to use the API and the user of the device can grant permission through the Settings application.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PERSISTENT_ACTIVITY](https://developer.android.com/reference/android/Manifest.permission#PERSISTENT_ACTIVITY)` _This constant was deprecated in API level 15. This functionality will be removed in the future; please do not use. Allow an application to make its activities persistent._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[POST_NOTIFICATIONS](https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS)` Allows an app to post notifications Protection level: dangerous   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[POST_PROMOTED_NOTIFICATIONS](https://developer.android.com/reference/android/Manifest.permission#POST_PROMOTED_NOTIFICATIONS)` Required for apps to post promoted notifications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROCESS_OUTGOING_CALLS](https://developer.android.com/reference/android/Manifest.permission#PROCESS_OUTGOING_CALLS)` _This constant was deprecated in API level 29. Applications should use`[CallRedirectionService](https://developer.android.com/reference/android/telecom/CallRedirectionService)` instead of the `[Intent.ACTION_NEW_OUTGOING_CALL](https://developer.android.com/reference/android/content/Intent#ACTION_NEW_OUTGOING_CALL)` broadcast._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROVIDE_OWN_AUTOFILL_SUGGESTIONS](https://developer.android.com/reference/android/Manifest.permission#PROVIDE_OWN_AUTOFILL_SUGGESTIONS)` Allows an application to display its suggestions using the autofill framework.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROVIDE_PRIVATE_COMPUTE_SERVICES](https://developer.android.com/reference/android/Manifest.permission#PROVIDE_PRIVATE_COMPUTE_SERVICES)` Allows an application to act as Private Compute Services, which allows the application to communicate with Private Compute Core components.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[PROVIDE_REMOTE_CREDENTIALS](https://developer.android.com/reference/android/Manifest.permission#PROVIDE_REMOTE_CREDENTIALS)` Allows an application to be able to store and retrieve credentials from a remote device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[QUERY_ADVANCED_PROTECTION_MODE](https://developer.android.com/reference/android/Manifest.permission#QUERY_ADVANCED_PROTECTION_MODE)` Allows an application to query the device's advanced protection mode status.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[QUERY_ALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#QUERY_ALL_PACKAGES)` Allows query of any normal app on the device, regardless of manifest declarations.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[QUERY_APP_USAGE](https://developer.android.com/reference/android/Manifest.permission#QUERY_APP_USAGE)` Allows the holder to query app usage stats.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RANGING](https://developer.android.com/reference/android/Manifest.permission#RANGING)` Required to be able to range to devices using generic ranging module.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_ASSISTANT_APP_SEARCH_DATA](https://developer.android.com/reference/android/Manifest.permission#READ_ASSISTANT_APP_SEARCH_DATA)` Allows an application to query over global data in AppSearch that's visible to the ASSISTANT role.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_ASSIST_STRUCTURE_SCREEN_CONTENT](https://developer.android.com/reference/android/Manifest.permission#READ_ASSIST_STRUCTURE_SCREEN_CONTENT)` Allows an assistant application to read screen content in the AssistStructure.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_BASIC_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_BASIC_PHONE_STATE)` Allows read only access to phone state with a non dangerous permission, including the information like cellular network type, software version.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#READ_CALENDAR)` Allows an application to read the user's calendar data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#READ_CALL_LOG)` Allows an application to read the user's call log.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_COLOR_ZONES](https://developer.android.com/reference/android/Manifest.permission#READ_COLOR_ZONES)` Allows an application to read the aggregated color zones on the screen for use cases like TV ambient backlight usages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)` Allows an application to read the user's contacts data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_DROPBOX_DATA](https://developer.android.com/reference/android/Manifest.permission#READ_DROPBOX_DATA)` Allows an application to access the data in Dropbox.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` Allows an application to read from external storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_HOME_APP_SEARCH_DATA](https://developer.android.com/reference/android/Manifest.permission#READ_HOME_APP_SEARCH_DATA)` Allows an application to query over global data in AppSearch that's visible to the HOME role.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_HOME_TIME_ZONE](https://developer.android.com/reference/android/Manifest.permission#READ_HOME_TIME_ZONE)` Allows applications to read the home time zone.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_INPUT_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_INPUT_STATE)` _This constant was deprecated in API level 16. The API that used this permission has been removed._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_LOGS](https://developer.android.com/reference/android/Manifest.permission#READ_LOGS)` Allows an application to read the low-level system log files.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_MEDIA_AUDIO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_AUDIO)` Allows an application to read audio files from external storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)` Allows an application to read image files from external storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO)` Allows an application to read video files from external storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_MEDIA_VISUAL_USER_SELECTED](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VISUAL_USER_SELECTED)` Allows an application to read image or video files from external storage that a user has selected via the permission prompt photo picker.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_NEARBY_STREAMING_POLICY](https://developer.android.com/reference/android/Manifest.permission#READ_NEARBY_STREAMING_POLICY)` Allows an application to read nearby streaming policy.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_PHONE_NUMBERS](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_NUMBERS)` Allows read access to the device's phone number(s), which is exposed to instant applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE)` Allows read only access to phone state, including the current cellular network information, the status of any ongoing calls, and a list of any `[PhoneAccount](https://developer.android.com/reference/android/telecom/PhoneAccount)`s registered on the device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_PRECISE_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_PRECISE_PHONE_STATE)` Allows read only access to precise phone state.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_SMS](https://developer.android.com/reference/android/Manifest.permission#READ_SMS)` Allows an application to read SMS messages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_SETTINGS)` Allows applications to read the sync settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_SYNC_STATS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_STATS)` Allows applications to read the sync stats.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_SYSTEM_PREFERENCES](https://developer.android.com/reference/android/Manifest.permission#READ_SYSTEM_PREFERENCES)` Allows an application to access the Settings Preference services to read settings exposed by the system Settings app and system apps that contribute settings surfaced by the Settings app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_UPDATE_ENGINE_LOGS](https://developer.android.com/reference/android/Manifest.permission#READ_UPDATE_ENGINE_LOGS)` Allows an application to read the update_engine logs Not for use by third-party applications.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[READ_VOICEMAIL](https://developer.android.com/reference/android/Manifest.permission#READ_VOICEMAIL)` Allows an application to read voicemails in the system.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REBOOT](https://developer.android.com/reference/android/Manifest.permission#REBOOT)` Required to be able to reboot the device.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECEIVE_BOOT_COMPLETED](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_BOOT_COMPLETED)` Allows an application to receive the `[Intent.ACTION_BOOT_COMPLETED](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED)` that is broadcast after the system finishes booting.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECEIVE_MMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_MMS)` Allows an application to monitor incoming MMS messages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECEIVE_SENSITIVE_NOTIFICATIONS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_SENSITIVE_NOTIFICATIONS)` Allows apps with a NotificationListenerService to receive notifications with sensitive information Apps with a NotificationListenerService without this permission will not be able to view certain types of sensitive information contained in notifications This permission also allows apps with the SMS permissions to query and receive broadcasts about SMS messages that contain One Time Passwords Protection level: signature|preinstalled|knownSigner|role   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECEIVE_SMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_SMS)` Allows an application to receive SMS messages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECEIVE_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_WAP_PUSH)` Allows an application to receive WAP push messages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RECORD_AUDIO](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO)` Allows an application to record audio.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REORDER_TASKS](https://developer.android.com/reference/android/Manifest.permission#REORDER_TASKS)` Allows an application to change the Z-order of tasks.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REPOSITION_SELF_WINDOWS](https://developer.android.com/reference/android/Manifest.permission#REPOSITION_SELF_WINDOWS)` Allows an application to programmatically move and resize its tasks when the system is in a state that allows such operations, e.g. in a desktop-like environment.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_APP_STREAMING](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_APP_STREAMING)` Allows application to request to be associated with a virtual device capable of streaming Android applications (`[AssociationRequest.DEVICE_PROFILE_APP_STREAMING](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_APP_STREAMING)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION)` Allows application to request to be associated with a vehicle head unit capable of automotive projection (`[AssociationRequest.DEVICE_PROFILE_AUTOMOTIVE_PROJECTION](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_AUTOMOTIVE_PROJECTION)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_COMPUTER](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_COMPUTER)` Allows application to request to be associated with a computer to share functionality and/or data with other devices, such as notifications, photos and media (`[AssociationRequest.DEVICE_PROFILE_COMPUTER](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_COMPUTER)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_GLASSES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_GLASSES)` Allows app to request to be associated with a device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)` as "glasses" Protection level: normal   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_MEDICAL](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_MEDICAL)` Allows application to request to associate with a `[AssociationRequest.DEVICE_PROFILE_MEDICAL](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_MEDICAL)` device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING)` Allows application to request to stream content from an Android host to a nearby device (`[AssociationRequest.DEVICE_PROFILE_NEARBY_DEVICE_STREAMING](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_NEARBY_DEVICE_STREAMING)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_PROFILE_WATCH](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_PROFILE_WATCH)` Allows app to request to be associated with a device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)` as a "watch" Protection level: normal   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_RUN_IN_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)` Allows a companion app to run in the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_SELF_MANAGED](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_SELF_MANAGED)` Allows an application to create a "self-managed" association.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)` Allows a companion app to start a foreground service from the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_COMPANION_USE_DATA_IN_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_USE_DATA_IN_BACKGROUND)` Allows a companion app to use data in the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_DELETE_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_DELETE_PACKAGES)` Allows an application to request deleting packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_IGNORE_BATTERY_OPTIMIZATIONS](https://developer.android.com/reference/android/Manifest.permission#REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)` Permission an application must hold in order to use `[Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#REQUEST_INSTALL_PACKAGES)` Allows an application to request installing packages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE](https://developer.android.com/reference/android/Manifest.permission#REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE)` Allows an application to subscribe to notifications about the presence status change of their associated companion device   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_OBSERVE_DEVICE_UUID_PRESENCE](https://developer.android.com/reference/android/Manifest.permission#REQUEST_OBSERVE_DEVICE_UUID_PRESENCE)` Allows an application to subscribe to notifications about the nearby devices' presence status change base on the UUIDs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[REQUEST_PASSWORD_COMPLEXITY](https://developer.android.com/reference/android/Manifest.permission#REQUEST_PASSWORD_COMPLEXITY)` Allows an application to request the screen lock complexity and prompt users to update the screen lock to a certain complexity level.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RESTART_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#RESTART_PACKAGES)` _This constant was deprecated in API level 15. The`[ActivityManager.restartPackage(String)](https://developer.android.com/reference/android/app/ActivityManager#restartPackage\(java.lang.String\))` API is no longer supported._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[RUN_USER_INITIATED_JOBS](https://developer.android.com/reference/android/Manifest.permission#RUN_USER_INITIATED_JOBS)` Allows applications to use the user-initiated jobs API.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SCHEDULE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)` Allows applications to use exact alarm APIs.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SEND_RESPOND_VIA_MESSAGE](https://developer.android.com/reference/android/Manifest.permission#SEND_RESPOND_VIA_MESSAGE)` Allows an application (Phone) to send a request to other applications to handle the respond-via-message action during incoming calls.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SEND_SMS](https://developer.android.com/reference/android/Manifest.permission#SEND_SMS)` Allows an application to send SMS messages.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_ALARM](https://developer.android.com/reference/android/Manifest.permission#SET_ALARM)` Allows an application to broadcast an Intent to set an alarm for the user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_ALWAYS_FINISH](https://developer.android.com/reference/android/Manifest.permission#SET_ALWAYS_FINISH)` Allows an application to control whether activities are immediately finished when put in the background.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_ANIMATION_SCALE](https://developer.android.com/reference/android/Manifest.permission#SET_ANIMATION_SCALE)` Modify the global animation scaling factor.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_BIOMETRIC_DIALOG_ADVANCED](https://developer.android.com/reference/android/Manifest.permission#SET_BIOMETRIC_DIALOG_ADVANCED)` Allows an application to set the advanced features on BiometricDialog (SystemUI), including logo, logo description, and content view with more options button.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_DEBUG_APP](https://developer.android.com/reference/android/Manifest.permission#SET_DEBUG_APP)` Configure an application for debugging.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_PREFERRED_APPLICATIONS](https://developer.android.com/reference/android/Manifest.permission#SET_PREFERRED_APPLICATIONS)` _This constant was deprecated in API level 15. No longer useful, see`[PackageManager.addPackageToPreferred(String)](https://developer.android.com/reference/android/content/pm/PackageManager#addPackageToPreferred\(java.lang.String\))` for details._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_PROCESS_LIMIT](https://developer.android.com/reference/android/Manifest.permission#SET_PROCESS_LIMIT)` Allows an application to set the maximum number of (not needed) application processes that can be running.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_TIME](https://developer.android.com/reference/android/Manifest.permission#SET_TIME)` Allows applications to set the system time directly.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_TIME_ZONE](https://developer.android.com/reference/android/Manifest.permission#SET_TIME_ZONE)` Allows applications to set the system time zone directly.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER)` Allows applications to set the wallpaper.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SET_WALLPAPER_HINTS](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER_HINTS)` Allows applications to set the wallpaper hints.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SHOW_POWER_MENU](https://developer.android.com/reference/android/Manifest.permission#SHOW_POWER_MENU)` Permission needed to request to show the Power Menu.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SHOW_POWER_MENU_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#SHOW_POWER_MENU_PRIVILEGED)` Permission needed to request to show the Power Menu.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SIGNAL_PERSISTENT_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#SIGNAL_PERSISTENT_PROCESSES)` Allow an application to request that a signal be sent to all persistent processes.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SMS_FINANCIAL_TRANSACTIONS](https://developer.android.com/reference/android/Manifest.permission#SMS_FINANCIAL_TRANSACTIONS)` _This constant was deprecated in API level 31. The API that used this permission is no longer functional._  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[START_FOREGROUND_SERVICES_FROM_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#START_FOREGROUND_SERVICES_FROM_BACKGROUND)` Allows an application to start foreground services from the background at any time.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[START_VIEW_APP_FEATURES](https://developer.android.com/reference/android/Manifest.permission#START_VIEW_APP_FEATURES)` Allows the holder to start the screen with a list of app features.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[START_VIEW_PERMISSION_USAGE](https://developer.android.com/reference/android/Manifest.permission#START_VIEW_PERMISSION_USAGE)` Allows the holder to start the permission usage screen for an app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#STATUS_BAR)` Allows an application to open, close, or disable the status bar and its icons.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE](https://developer.android.com/reference/android/Manifest.permission#SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE)` Allows an application to subscribe to device locked and keyguard locked (i.e., showing) state.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[SYSTEM_ALERT_WINDOW](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)` Allows an app to create windows using the type `[WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY)`, shown on top of all other apps.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[TRANSMIT_IR](https://developer.android.com/reference/android/Manifest.permission#TRANSMIT_IR)` Allows using the device's IR transmitter, if available.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[TURN_SCREEN_ON](https://developer.android.com/reference/android/Manifest.permission#TURN_SCREEN_ON)` Allows an app to turn on the screen on, e.g. with `[PowerManager.ACQUIRE_CAUSES_WAKEUP](https://developer.android.com/reference/android/os/PowerManager#ACQUIRE_CAUSES_WAKEUP)`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[TV_IMPLICIT_ENTER_PIP](https://developer.android.com/reference/android/Manifest.permission#TV_IMPLICIT_ENTER_PIP)` Allows an app to enter Picture-in-Picture mode when the user is not explicitly requesting it.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[UNINSTALL_SHORTCUT](https://developer.android.com/reference/android/Manifest.permission#UNINSTALL_SHORTCUT)` **Don't use this permission in your app.**  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[UPDATE_DEVICE_STATS](https://developer.android.com/reference/android/Manifest.permission#UPDATE_DEVICE_STATS)` Allows an application to update device statistics.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[UPDATE_PACKAGES_WITHOUT_USER_ACTION](https://developer.android.com/reference/android/Manifest.permission#UPDATE_PACKAGES_WITHOUT_USER_ACTION)` Allows an application to indicate via `[PackageInstaller.SessionParams.setRequireUserAction(int)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequireUserAction\(int\))` that user action should not be required for an app update.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_BIOMETRIC](https://developer.android.com/reference/android/Manifest.permission#USE_BIOMETRIC)` Allows an app to use device supported biometric modalities.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)` Allows apps to use exact alarms just like with `[SCHEDULE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)` but without needing to request this permission from the user.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_FINGERPRINT](https://developer.android.com/reference/android/Manifest.permission#USE_FINGERPRINT)` _This constant was deprecated in API level 28. Applications should request`[USE_BIOMETRIC](https://developer.android.com/reference/android/Manifest.permission#USE_BIOMETRIC)` instead_  
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_FULL_SCREEN_INTENT](https://developer.android.com/reference/android/Manifest.permission#USE_FULL_SCREEN_INTENT)` Required for apps targeting `[Build.VERSION_CODES.Q](https://developer.android.com/reference/android/os/Build.VERSION_CODES#Q)` that want to use `[notification full screen intents](https://developer.android.com/reference/android/app/Notification.Builder#setFullScreenIntent\(android.app.PendingIntent,%20boolean\))`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER](https://developer.android.com/reference/android/Manifest.permission#USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER)` Allows to read device identifiers and use ICC based authentication like EAP-AKA.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_LOCATION_BUTTON](https://developer.android.com/reference/android/Manifest.permission#USE_LOCATION_BUTTON)` Allows an app use location button, which grants temporary location permission when a user clicks the button.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_PINNED_WINDOWING_LAYER](https://developer.android.com/reference/android/Manifest.permission#USE_PINNED_WINDOWING_LAYER)` Allows an application to use `[ActivityManager.AppTask.WINDOWING_LAYER_PINNED](https://developer.android.com/reference/android/app/ActivityManager.AppTask#WINDOWING_LAYER_PINNED)` for its Tasks, typically requested via `[ActivityManager.AppTask.requestWindowingLayer(int, Executor, OutcomeReceiver)](https://developer.android.com/reference/android/app/ActivityManager.AppTask#requestWindowingLayer\(int,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver<java.lang.Integer,java.lang.Exception>\))`.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[USE_SIP](https://developer.android.com/reference/android/Manifest.permission#USE_SIP)` Allows an application to use SIP service.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[UWB_RANGING](https://developer.android.com/reference/android/Manifest.permission#UWB_RANGING)` Required to be able to range to devices using ultra-wideband.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[VIBRATE](https://developer.android.com/reference/android/Manifest.permission#VIBRATE)` Allows access to the vibrator.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WAKE_LOCK](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK)` Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_APN_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_APN_SETTINGS)` Allows applications to write the apn settings and read sensitive fields of an existing apn settings like user and password.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALENDAR)` Allows an application to write the user's calendar data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALL_LOG)` Allows an application to write and read the user's call log data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS)` Allows an application to write the user's contacts data.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE)` Allows an application to write to external storage.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_GSERVICES](https://developer.android.com/reference/android/Manifest.permission#WRITE_GSERVICES)` Allows an application to modify the Google service map.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_SECURE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SECURE_SETTINGS)` Allows an application to read or write the secure system settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SETTINGS)` Allows an application to read or write the system settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SYNC_SETTINGS)` Allows applications to write the sync settings.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_SYSTEM_PREFERENCES](https://developer.android.com/reference/android/Manifest.permission#WRITE_SYSTEM_PREFERENCES)` Allows an application to access the Settings Preference services to write settings values exposed by the system Settings app and system apps that contribute settings surfaced in the Settings app.   
`[String](https://developer.android.com/reference/java/lang/String)` |  `[WRITE_VOICEMAIL](https://developer.android.com/reference/android/Manifest.permission#WRITE_VOICEMAIL)` Allows an application to modify and remove existing voicemails in the system.   
  
### Public constructors  
  
---  
` [permission](https://developer.android.com/reference/android/Manifest.permission#permission\(\))() `  
  
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

### ACCEPT_HANDOVER

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCEPT_HANDOVER

Allows a calling app to continue a call which was started in another app. An example is a video calling app that wants to continue a voice call on the user's mobile network.

When the handover of a call from one app to another takes place, there are two devices which are involved in the handover; the initiating and receiving devices. The initiating device is where the request to handover the call was started, and the receiving device is where the handover request is confirmed by the other party.

This permission protects access to the `[TelecomManager.acceptHandover(Uri, int, PhoneAccountHandle)](https://developer.android.com/reference/android/telecom/TelecomManager#acceptHandover\(android.net.Uri,%20int,%20android.telecom.PhoneAccountHandle\))` which the receiving side of the handover uses to accept a handover. 

Protection level: dangerous

Constant Value: "android.permission.ACCEPT_HANDOVER" 

### ACCESS_BACKGROUND_LOCATION

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_BACKGROUND_LOCATION

Allows an app to access location in the background. If you're requesting this permission, you must also request either `[ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)` or `[ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)`. Requesting this permission by itself doesn't give you location access. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.ACCESS_BACKGROUND_LOCATION" 

### ACCESS_BIOMETRIC_SENSOR_STRENGTHS

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_BIOMETRIC_SENSOR_STRENGTHS

Allows an application to retrieve the sensor security strengths of the biometric sensors. 

This permission is currently granted only to the WALLET role, the DEVICE_POLICY_MANAGEMENT role, and the SYSTEM_SHELL role (for easier control during testing).

Constant Value: "android.permission.ACCESS_BIOMETRIC_SENSOR_STRENGTHS" 

### ACCESS_BLOBS_ACROSS_USERS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_BLOBS_ACROSS_USERS

Allows an application to access data blobs across users.

Constant Value: "android.permission.ACCESS_BLOBS_ACROSS_USERS" 

### ACCESS_CHECKIN_PROPERTIES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_CHECKIN_PROPERTIES

Allows read/write access to the "properties" table in the checkin database, to change values that get uploaded. 

Not for use by third-party applications.

Constant Value: "android.permission.ACCESS_CHECKIN_PROPERTIES" 

### ACCESS_COARSE_LOCATION

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_COARSE_LOCATION

Allows an app to access approximate location. Alternatively, you might want `[ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION)`. 

Protection level: dangerous

Constant Value: "android.permission.ACCESS_COARSE_LOCATION" 

### ACCESS_FINE_LOCATION

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_FINE_LOCATION

Allows an app to access precise location. Alternatively, you might want `[ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION)`. 

Protection level: dangerous

Constant Value: "android.permission.ACCESS_FINE_LOCATION" 

### ACCESS_HID

Added in [version 37.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_HID

Required by apps wanting to query for and/or access Human Interface Device (HID) nodes using `[HidManager](https://developer.android.com/reference/android/hardware/hid/HidManager)`. 

Protection level: internal|appop

Constant Value: "android.permission.ACCESS_HID" 

### ACCESS_HIDDEN_PROFILES

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_HIDDEN_PROFILES

Allows applications to access profiles with `android.content.pm.UserProperties#PROFILE_API_VISIBILITY_HIDDEN` user property, e.g. `[UserManager.USER_TYPE_PROFILE_PRIVATE](https://developer.android.com/reference/android/os/UserManager#USER_TYPE_PROFILE_PRIVATE)`. 

Protection level: normal

Constant Value: "android.permission.ACCESS_HIDDEN_PROFILES" 

### ACCESS_LAUNCHER_DATA

Added in [version 36.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_LAUNCHER_DATA

This permission protects a content provider within home/launcher applications, enabling management of home screen metadata such as shortcut placement, launch intents, and labels.

Constant Value: "android.permission.ACCESS_LAUNCHER_DATA" 

### ACCESS_LOCAL_NETWORK

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_LOCAL_NETWORK

Required to be able to advertise and connect to local network devices. 

A [local network](https://developer.android.com/privacy-and-security/local-network-definition) refers to an IP network that utilizes a broadcast-capable network interface, such as Wi-Fi or Ethernet, but excludes cellular (WWAN) or VPN connections. 

Protection level: dangerous

Constant Value: "android.permission.ACCESS_LOCAL_NETWORK" 

### ACCESS_LOCATION_EXTRA_COMMANDS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_LOCATION_EXTRA_COMMANDS

Allows an application to access extra location provider commands. 

Protection level: normal

Constant Value: "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" 

### ACCESS_MEDIA_LOCATION

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_MEDIA_LOCATION

Allows an application to access any geographic locations persisted in the user's shared collection. 

Protection level: dangerous

Constant Value: "android.permission.ACCESS_MEDIA_LOCATION" 

### ACCESS_NETWORK_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_NETWORK_STATE

Allows applications to access information about networks. 

Protection level: normal

Constant Value: "android.permission.ACCESS_NETWORK_STATE" 

### ACCESS_NOTIFICATION_POLICY

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_NOTIFICATION_POLICY

Marker permission for applications that wish to access notification policy. This permission is not supported on managed profiles. 

Protection level: normal

Constant Value: "android.permission.ACCESS_NOTIFICATION_POLICY" 

### ACCESS_WIFI_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCESS_WIFI_STATE

Allows applications to access information about Wi-Fi networks. 

Protection level: normal

Constant Value: "android.permission.ACCESS_WIFI_STATE" 

### ACCOUNT_MANAGER

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACCOUNT_MANAGER

Allows applications to call into AccountAuthenticators. 

Not for use by third-party applications.

Constant Value: "android.permission.ACCOUNT_MANAGER" 

### ACTIVITY_RECOGNITION

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ACTIVITY_RECOGNITION

Allows an application to recognize physical activity. 

Protection level: dangerous

Constant Value: "android.permission.ACTIVITY_RECOGNITION" 

### ADD_VOICEMAIL

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ADD_VOICEMAIL

Allows an application to add voicemails into the system. 

Protection level: dangerous

Constant Value: "com.android.voicemail.permission.ADD_VOICEMAIL" 

### ANSWER_PHONE_CALLS

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ANSWER_PHONE_CALLS

Allows the app to answer an incoming phone call. 

Protection level: dangerous

Constant Value: "android.permission.ANSWER_PHONE_CALLS" 

### APPLY_PICTURE_PROFILE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) APPLY_PICTURE_PROFILE

Allows an app to apply a `[ERROR(/MediaQualityManager.PictureProfile)](https://developer.android.com/)` to a layer via `[ERROR(/MediaCodec.PARAMETER_KEY_PICTURE_PROFILE)](https://developer.android.com/)` and, additionally, system apps via `[ERROR(/SurfaceControl.Transaction#setPictureProfileHandle)](https://developer.android.com/)`.

Constant Value: "android.permission.APPLY_PICTURE_PROFILE" 

### BATTERY_STATS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BATTERY_STATS

Allows an application to collect battery statistics 

Protection level: signature|privileged|development

Constant Value: "android.permission.BATTERY_STATS" 

### BIND_ACCESSIBILITY_SERVICE

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_ACCESSIBILITY_SERVICE

Must be required by an `[AccessibilityService](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_ACCESSIBILITY_SERVICE" 

### BIND_ALTERNATIVE_MESSAGE_TRANSPORT_SERVICE

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_ALTERNATIVE_MESSAGE_TRANSPORT_SERVICE

Permission needed to ensure that only the system process can bind with the `[AlternativeMessageTransportService](https://developer.android.com/reference/android/service/messaging/AlternativeMessageTransportService)`.

Constant Value: "android.permission.BIND_ALTERNATIVE_MESSAGE_TRANSPORT_SERVICE" 

### BIND_APPWIDGET

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_APPWIDGET

Allows an application to tell the AppWidget service which application can access AppWidget's data. The normal user flow is that a user picks an AppWidget to go into a particular host, thereby giving that host application access to the private data from the AppWidget app. An application that has this permission should honor that contract. 

Not for use by third-party applications.

Constant Value: "android.permission.BIND_APPWIDGET" 

### BIND_APP_FUNCTION_SERVICE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_APP_FUNCTION_SERVICE

Must be required by an `[AppFunctionService](https://developer.android.com/reference/android/app/appfunctions/AppFunctionService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_APP_FUNCTION_SERVICE" 

### BIND_AUTOFILL_SERVICE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_AUTOFILL_SERVICE

Must be required by a `[AutofillService](https://developer.android.com/reference/android/service/autofill/AutofillService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_AUTOFILL_SERVICE" 

### BIND_CALL_REDIRECTION_SERVICE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CALL_REDIRECTION_SERVICE

Must be required by a `[CallRedirectionService](https://developer.android.com/reference/android/telecom/CallRedirectionService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_CALL_REDIRECTION_SERVICE" 

### BIND_CARRIER_MESSAGING_CLIENT_SERVICE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CARRIER_MESSAGING_CLIENT_SERVICE

A subclass of `[CarrierMessagingClientService](https://developer.android.com/reference/android/service/carrier/CarrierMessagingClientService)` must be protected with this permission. 

Protection level: signature

Constant Value: "android.permission.BIND_CARRIER_MESSAGING_CLIENT_SERVICE" 

### BIND_CARRIER_MESSAGING_SERVICE

Added in [API level 22](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CARRIER_MESSAGING_SERVICE

**This constant was deprecated in API level 23.**  
Use `[BIND_CARRIER_SERVICES](https://developer.android.com/reference/android/Manifest.permission#BIND_CARRIER_SERVICES)` instead 

Constant Value: "android.permission.BIND_CARRIER_MESSAGING_SERVICE" 

### BIND_CARRIER_SERVICES

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CARRIER_SERVICES

The system process that is allowed to bind to services in carrier apps will have this permission. Carrier apps should use this permission to protect their services that only the system is allowed to bind to. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_CARRIER_SERVICES" 

### BIND_CHOOSER_TARGET_SERVICE

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CHOOSER_TARGET_SERVICE

**This constant was deprecated in API level 30.**  
For publishing direct share targets, please follow the instructions in https://developer.android.com/training/sharing/receive.html#providing-direct-share-targets instead. 

Must be required by a `[ChooserTargetService](https://developer.android.com/reference/android/service/chooser/ChooserTargetService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_CHOOSER_TARGET_SERVICE" 

### BIND_COMPANION_DEVICE_SERVICE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_COMPANION_DEVICE_SERVICE

Must be required by any `[CompanionDeviceService](https://developer.android.com/reference/android/companion/CompanionDeviceService)`s to ensure that only the system can bind to it.

Constant Value: "android.permission.BIND_COMPANION_DEVICE_SERVICE" 

### BIND_CONDITION_PROVIDER_SERVICE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CONDITION_PROVIDER_SERVICE

Must be required by a `[ConditionProviderService](https://developer.android.com/reference/android/service/notification/ConditionProviderService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_CONDITION_PROVIDER_SERVICE" 

### BIND_CONTENT_RESTRICTION_SERVICE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CONTENT_RESTRICTION_SERVICE

Permission required to bind content restriction service 

Protection level: signature

Constant Value: "android.permission.BIND_CONTENT_RESTRICTION_SERVICE" 

### BIND_CONTENT_SAFETY_SERVICE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CONTENT_SAFETY_SERVICE

Ensures only the platform can bind to the content safety service. 

Protection level: signature

Constant Value: "android.permission.BIND_CONTENT_SAFETY_SERVICE" 

### BIND_CONTROLS

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CONTROLS

Allows SystemUI to request third party controls. 

Should only be requested by the System and required by `[ControlsProviderService](https://developer.android.com/reference/android/service/controls/ControlsProviderService)` declarations.

Constant Value: "android.permission.BIND_CONTROLS" 

### BIND_CREDENTIAL_PROVIDER_SERVICE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_CREDENTIAL_PROVIDER_SERVICE

Must be required by a CredentialProviderService to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_CREDENTIAL_PROVIDER_SERVICE" 

### BIND_DATA_MIGRATION_FOR_PRIVATECOMPUTE

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_DATA_MIGRATION_FOR_PRIVATECOMPUTE

Allows the system to bind to an application's data migration service for Private Compute. 

Protection level: signature

Constant Value: "android.permission.BIND_DATA_MIGRATION_FOR_PRIVATECOMPUTE" 

### BIND_DEVICE_ADMIN

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_DEVICE_ADMIN

Must be required by device administration receiver, to ensure that only the system can interact with it. 

Protection level: signature

Constant Value: "android.permission.BIND_DEVICE_ADMIN" 

### BIND_DREAM_SERVICE

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_DREAM_SERVICE

Must be required by an `[DreamService](https://developer.android.com/reference/android/service/dreams/DreamService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_DREAM_SERVICE" 

### BIND_INCALL_SERVICE

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_INCALL_SERVICE

Must be required by a `[InCallService](https://developer.android.com/reference/android/telecom/InCallService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_INCALL_SERVICE" 

### BIND_INPUT_METHOD

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_INPUT_METHOD

Must be required by an `[InputMethodService](https://developer.android.com/reference/android/inputmethodservice/InputMethodService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_INPUT_METHOD" 

### BIND_MIDI_DEVICE_SERVICE

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_MIDI_DEVICE_SERVICE

Must be required by an `[MidiDeviceService](https://developer.android.com/reference/android/media/midi/MidiDeviceService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_MIDI_DEVICE_SERVICE" 

### BIND_NFC_SERVICE

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_NFC_SERVICE

Must be required by a `[HostApduService](https://developer.android.com/reference/android/nfc/cardemulation/HostApduService)` or `[OffHostApduService](https://developer.android.com/reference/android/nfc/cardemulation/OffHostApduService)` to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_NFC_SERVICE" 

### BIND_NOTIFICATION_LISTENER_SERVICE

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_NOTIFICATION_LISTENER_SERVICE

Must be required by an `[NotificationListenerService](https://developer.android.com/reference/android/service/notification/NotificationListenerService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_NOTIFICATION_LISTENER_SERVICE" 

### BIND_PCC_EGRESS_SERVICE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_PCC_EGRESS_SERVICE

Allows a system application to bind to the Private Compute Core egress service. 

Protection level: internal

Constant Value: "android.permission.BIND_PCC_EGRESS_SERVICE" 

### BIND_PRINT_SERVICE

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_PRINT_SERVICE

Must be required by a `[PrintService](https://developer.android.com/reference/android/printservice/PrintService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_PRINT_SERVICE" 

### BIND_QUICK_ACCESS_WALLET_SERVICE

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_QUICK_ACCESS_WALLET_SERVICE

Must be required by a `[QuickAccessWalletService](https://developer.android.com/reference/android/service/quickaccesswallet/QuickAccessWalletService)` to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_QUICK_ACCESS_WALLET_SERVICE" 

### BIND_QUICK_SETTINGS_TILE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_QUICK_SETTINGS_TILE

Allows an application to bind to third party quick settings tiles. 

Should only be requested by the System, should be required by TileService declarations.

Constant Value: "android.permission.BIND_QUICK_SETTINGS_TILE" 

### BIND_REMOTEVIEWS

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_REMOTEVIEWS

Must be required by a `[RemoteViewsService](https://developer.android.com/reference/android/widget/RemoteViewsService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_REMOTEVIEWS" 

### BIND_SCREENING_SERVICE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_SCREENING_SERVICE

Must be required by a `[CallScreeningService](https://developer.android.com/reference/android/telecom/CallScreeningService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_SCREENING_SERVICE" 

### BIND_TELECOM_CONNECTION_SERVICE

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_TELECOM_CONNECTION_SERVICE

Must be required by a `[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_TELECOM_CONNECTION_SERVICE" 

### BIND_TEXT_SERVICE

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_TEXT_SERVICE

Must be required by a TextService (e.g. SpellCheckerService) to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_TEXT_SERVICE" 

### BIND_TV_AD_SERVICE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_TV_AD_SERVICE

Must be required by a android.media.tv.ad.TvAdService to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_TV_AD_SERVICE" 

### BIND_TV_INPUT

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_TV_INPUT

Must be required by a `[TvInputService](https://developer.android.com/reference/android/media/tv/TvInputService)` to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_TV_INPUT" 

### BIND_TV_INTERACTIVE_APP

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_TV_INTERACTIVE_APP

Must be required by a `[TvInteractiveAppService](https://developer.android.com/reference/android/media/tv/interactive/TvInteractiveAppService)` to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_TV_INTERACTIVE_APP" 

### BIND_VISUAL_VOICEMAIL_SERVICE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_VISUAL_VOICEMAIL_SERVICE

Must be required by a link `[VisualVoicemailService](https://developer.android.com/reference/android/telephony/VisualVoicemailService)` to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_VISUAL_VOICEMAIL_SERVICE" 

### BIND_VOICE_INTERACTION

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_VOICE_INTERACTION

Must be required by a `[VoiceInteractionService](https://developer.android.com/reference/android/service/voice/VoiceInteractionService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_VOICE_INTERACTION" 

### BIND_VPN_SERVICE

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_VPN_SERVICE

Must be required by a `[VpnService](https://developer.android.com/reference/android/net/VpnService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_VPN_SERVICE" 

### BIND_VR_LISTENER_SERVICE

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_VR_LISTENER_SERVICE

Must be required by an `[VrListenerService](https://developer.android.com/reference/android/service/vr/VrListenerService)`, to ensure that only the system can bind to it. 

Protection level: signature

Constant Value: "android.permission.BIND_VR_LISTENER_SERVICE" 

### BIND_WALLPAPER

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BIND_WALLPAPER

Must be required by a `[WallpaperService](https://developer.android.com/reference/android/service/wallpaper/WallpaperService)`, to ensure that only the system can bind to it. 

Protection level: signature|privileged

Constant Value: "android.permission.BIND_WALLPAPER" 

### BLUETOOTH

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH

Allows applications to connect to paired bluetooth devices. 

Protection level: normal

Constant Value: "android.permission.BLUETOOTH" 

### BLUETOOTH_ADMIN

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH_ADMIN

Allows applications to discover and pair bluetooth devices. 

Protection level: normal

Constant Value: "android.permission.BLUETOOTH_ADMIN" 

### BLUETOOTH_ADVERTISE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH_ADVERTISE

Required to be able to advertise to nearby Bluetooth devices. 

Protection level: dangerous

Constant Value: "android.permission.BLUETOOTH_ADVERTISE" 

### BLUETOOTH_CONNECT

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH_CONNECT

Required to be able to connect to paired Bluetooth devices. 

Protection level: dangerous

Constant Value: "android.permission.BLUETOOTH_CONNECT" 

### BLUETOOTH_PRIVILEGED

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH_PRIVILEGED

Allows applications to pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access. 

Not for use by third-party applications.

Constant Value: "android.permission.BLUETOOTH_PRIVILEGED" 

### BLUETOOTH_SCAN

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BLUETOOTH_SCAN

Required to be able to discover and pair nearby Bluetooth devices. 

Protection level: dangerous

Constant Value: "android.permission.BLUETOOTH_SCAN" 

### BODY_SENSORS

Added in [API level 20](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BODY_SENSORS

Allows an application to access data from sensors that the user uses to measure what is happening inside their body, such as heart rate. 

Protection level: dangerous

Constant Value: "android.permission.BODY_SENSORS" 

### BODY_SENSORS_BACKGROUND

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BODY_SENSORS_BACKGROUND

Allows an application to access data from sensors that the user uses to measure what is happening inside their body, such as heart rate. If you're requesting this permission, you must also request `[BODY_SENSORS](https://developer.android.com/reference/android/Manifest.permission#BODY_SENSORS)`. Requesting this permission by itself doesn't give you Body sensors access. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.BODY_SENSORS_BACKGROUND" 

### BROADCAST_PACKAGE_REMOVED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BROADCAST_PACKAGE_REMOVED

Allows an application to broadcast a notification that an application package has been removed. 

Not for use by third-party applications.

Constant Value: "android.permission.BROADCAST_PACKAGE_REMOVED" 

### BROADCAST_SMS

Added in [API level 2](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BROADCAST_SMS

Allows an application to broadcast an SMS receipt notification. 

Not for use by third-party applications.

Constant Value: "android.permission.BROADCAST_SMS" 

### BROADCAST_STICKY

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BROADCAST_STICKY

Allows an application to broadcast sticky intents. These are broadcasts whose data is held by the system after being finished, so that clients can quickly retrieve that data without having to wait for the next broadcast. 

Protection level: normal

Constant Value: "android.permission.BROADCAST_STICKY" 

### BROADCAST_WAP_PUSH

Added in [API level 2](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) BROADCAST_WAP_PUSH

Allows an application to broadcast a WAP PUSH receipt notification. 

Not for use by third-party applications.

Constant Value: "android.permission.BROADCAST_WAP_PUSH" 

### CALL_COMPANION_APP

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CALL_COMPANION_APP

Allows an app which implements the `[InCallService](https://developer.android.com/reference/android/telecom/InCallService)` API to be eligible to be enabled as a calling companion app. This means that the Telecom framework will bind to the app's InCallService implementation when there are calls active. The app can use the InCallService API to view information about calls on the system and control these calls. 

Protection level: normal

Constant Value: "android.permission.CALL_COMPANION_APP" 

### CALL_PHONE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CALL_PHONE

Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call. 

**Note:** An app holding this permission can also call carrier MMI codes to change settings such as call forwarding or call waiting preferences.

Protection level: dangerous

Constant Value: "android.permission.CALL_PHONE" 

### CALL_PRIVILEGED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CALL_PRIVILEGED

Allows an application to call any phone number, including emergency numbers, without going through the Dialer user interface for the user to confirm the call being placed. 

Not for use by third-party applications.

Constant Value: "android.permission.CALL_PRIVILEGED" 

### CAMERA

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CAMERA

Required to be able to access the camera device. 

This will automatically enforce the [ uses-feature](https://developer.android.com/guide/topics/manifest/uses-feature-element) manifest element for _all_ camera features. If you do not require all camera features or can properly operate if a camera is not available, then you must modify your manifest as appropriate in order to install on devices that don't support all camera features.

Protection level: dangerous

Constant Value: "android.permission.CAMERA" 

### CAPTURE_AUDIO_OUTPUT

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CAPTURE_AUDIO_OUTPUT

Allows an application to capture audio output. Use the `CAPTURE_MEDIA_OUTPUT` permission if only the `USAGE_UNKNOWN`), `USAGE_MEDIA`) or `USAGE_GAME`) usages are intended to be captured. 

Not for use by third-party applications.

Constant Value: "android.permission.CAPTURE_AUDIO_OUTPUT" 

### CAPTURE_KEYBOARD

Added in [version 36.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CAPTURE_KEYBOARD

Allows the currently focused application to be able to consume keys before Android system get chance to process system keys and shortcuts. 

The keys are always sent to the currently focussed application, this permission allows the focussed application to receive the keys that are normally consumed by the system for shortcuts, allowing it to have custom shortcut behavior primarily for use cases like virtual machine apps where the host OS wants to handle the shortcuts differently. 

Certain shortcuts and system keys like Home, Overview, Power, etc are never sent to the currently focused application and are always consumed by the system. 

User can escape out of the capture mode by long pressing the Escape key or simply navigating out of the application. 

Protection level: normal

**See also:**

  * `[WindowManager.LayoutParams.setKeyboardCaptureEnabled(boolean)](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#setKeyboardCaptureEnabled\(boolean\))`



Constant Value: "android.permission.CAPTURE_KEYBOARD" 

### CHANGE_COMPONENT_ENABLED_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CHANGE_COMPONENT_ENABLED_STATE

Allows an application to change whether an application component (other than its own) is enabled or not. 

Not for use by third-party applications.

Constant Value: "android.permission.CHANGE_COMPONENT_ENABLED_STATE" 

### CHANGE_CONFIGURATION

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CHANGE_CONFIGURATION

Allows an application to modify the current configuration, such as locale. 

Protection level: signature|privileged|development

Constant Value: "android.permission.CHANGE_CONFIGURATION" 

### CHANGE_NETWORK_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CHANGE_NETWORK_STATE

Allows applications to change network connectivity state. 

Protection level: normal

Constant Value: "android.permission.CHANGE_NETWORK_STATE" 

### CHANGE_WIFI_MULTICAST_STATE

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CHANGE_WIFI_MULTICAST_STATE

Allows applications to enter Wi-Fi Multicast mode. 

Protection level: normal

Constant Value: "android.permission.CHANGE_WIFI_MULTICAST_STATE" 

### CHANGE_WIFI_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CHANGE_WIFI_STATE

Allows applications to change Wi-Fi connectivity state. 

Protection level: normal

Constant Value: "android.permission.CHANGE_WIFI_STATE" 

### CLEAR_APP_CACHE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CLEAR_APP_CACHE

Allows an application to clear the caches of all installed applications on the device. 

Protection level: signature|privileged

Constant Value: "android.permission.CLEAR_APP_CACHE" 

### CONFIGURE_WIFI_DISPLAY

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CONFIGURE_WIFI_DISPLAY

Allows an application to configure and connect to Wifi displays

Constant Value: "android.permission.CONFIGURE_WIFI_DISPLAY" 

### CONTROL_LOCATION_UPDATES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CONTROL_LOCATION_UPDATES

Allows enabling/disabling location update notifications from the radio. 

Not for use by third-party applications.

Constant Value: "android.permission.CONTROL_LOCATION_UPDATES" 

### CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS

Allows a browser to invoke the set of query apis to get metadata about credential candidates prepared during the CredentialManager.prepareGetCredential API. 

Protection level: normal

Constant Value: "android.permission.CREDENTIAL_MANAGER_QUERY_CANDIDATE_CREDENTIALS" 

### CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS

Allows specifying candidate credential providers to be queried in Credential Manager get flows, or to be preferred as a default in the Credential Manager create flows. 

Protection level: normal

Constant Value: "android.permission.CREDENTIAL_MANAGER_SET_ALLOWED_PROVIDERS" 

### CREDENTIAL_MANAGER_SET_ORIGIN

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) CREDENTIAL_MANAGER_SET_ORIGIN

Allows a browser to invoke credential manager APIs on behalf of another RP. 

Protection level: normal

Constant Value: "android.permission.CREDENTIAL_MANAGER_SET_ORIGIN" 

### DELETE_CACHE_FILES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DELETE_CACHE_FILES

Old permission for deleting an app's cache files, no longer used, but signals for us to quietly ignore calls instead of throwing an exception. 

Protection level: signature|privileged

Constant Value: "android.permission.DELETE_CACHE_FILES" 

### DELETE_PACKAGES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DELETE_PACKAGES

Allows an application to delete packages. 

Not for use by third-party applications. 

Starting in `[Build.VERSION_CODES.N](https://developer.android.com/reference/android/os/Build.VERSION_CODES#N)`, user confirmation is requested when the application deleting the package is not the same application that installed the package.

Constant Value: "android.permission.DELETE_PACKAGES" 

### DELIVER_COMPANION_MESSAGES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DELIVER_COMPANION_MESSAGES

Allows an application to deliver companion messages to system

Constant Value: "android.permission.DELIVER_COMPANION_MESSAGES" 

### DETECT_SCREEN_CAPTURE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DETECT_SCREEN_CAPTURE

Allows an application to get notified when a screen capture of its windows is attempted. 

Protection level: normal

Constant Value: "android.permission.DETECT_SCREEN_CAPTURE" 

### DETECT_SCREEN_RECORDING

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DETECT_SCREEN_RECORDING

Allows an application to get notified when it is being recorded. 

Protection level: normal

Constant Value: "android.permission.DETECT_SCREEN_RECORDING" 

### DIAGNOSTIC

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DIAGNOSTIC

Allows applications to RW to diagnostic resources. 

Not for use by third-party applications.

Constant Value: "android.permission.DIAGNOSTIC" 

### DISABLE_KEYGUARD

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DISABLE_KEYGUARD

Allows applications to disable the keyguard if it is not secure. 

Protection level: normal

Constant Value: "android.permission.DISABLE_KEYGUARD" 

### DUMP

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) DUMP

Allows an application to retrieve state dump information from system services. 

Not for use by third-party applications.

Constant Value: "android.permission.DUMP" 

### ENFORCE_UPDATE_OWNERSHIP

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) ENFORCE_UPDATE_OWNERSHIP

Allows an application to indicate via `[PackageInstaller.SessionParams.setRequestUpdateOwnership(boolean)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequestUpdateOwnership\(boolean\))` that it has the intention of becoming the update owner. 

Protection level: normal

Constant Value: "android.permission.ENFORCE_UPDATE_OWNERSHIP" 

### EXECUTE_APP_ACTION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) EXECUTE_APP_ACTION

Allows an assistive application to perform actions on behalf of users inside of applications. 

For now, this permission is only granted to the Assistant application selected by the user. 

Protection level: internal|role

Constant Value: "android.permission.EXECUTE_APP_ACTION" 

### EXECUTE_APP_FUNCTIONS

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) EXECUTE_APP_FUNCTIONS

Allows an application to perform actions on behalf of users inside of applications. 

Note that allowlist checks for AppFunctions API access are enforced at runtime. Depending on the metadata in the allowlist, further requirements may apply. 

Protection level: normal

Constant Value: "android.permission.EXECUTE_APP_FUNCTIONS" 

### EXPAND_STATUS_BAR

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) EXPAND_STATUS_BAR

Allows an application to expand or collapse the status bar. 

Protection level: normal

Constant Value: "android.permission.EXPAND_STATUS_BAR" 

### FACTORY_TEST

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FACTORY_TEST

Run as a manufacturer test application, running as the root user. Only available when the device is running in manufacturer test mode. 

Not for use by third-party applications.

Constant Value: "android.permission.FACTORY_TEST" 

### FOREGROUND_SERVICE

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))`. 

Protection level: normal

Constant Value: "android.permission.FOREGROUND_SERVICE" 

### FOREGROUND_SERVICE_CAMERA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_CAMERA

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "camera". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_CAMERA" 

### FOREGROUND_SERVICE_CONNECTED_DEVICE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_CONNECTED_DEVICE

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "connectedDevice". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE" 

### FOREGROUND_SERVICE_DATA_SYNC

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_DATA_SYNC

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "dataSync". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_DATA_SYNC" 

### FOREGROUND_SERVICE_HEALTH

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_HEALTH

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "health". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_HEALTH" 

### FOREGROUND_SERVICE_LOCATION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_LOCATION

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "location". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_LOCATION" 

### FOREGROUND_SERVICE_MEDIA_PLAYBACK

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_MEDIA_PLAYBACK

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaPlayback". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" 

### FOREGROUND_SERVICE_MEDIA_PROCESSING

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_MEDIA_PROCESSING

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaProcessing". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_MEDIA_PROCESSING" 

### FOREGROUND_SERVICE_MEDIA_PROJECTION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_MEDIA_PROJECTION

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "mediaProjection". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_MEDIA_PROJECTION" 

### FOREGROUND_SERVICE_MICROPHONE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_MICROPHONE

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "microphone". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_MICROPHONE" 

### FOREGROUND_SERVICE_PHONE_CALL

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_PHONE_CALL

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "phoneCall". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_PHONE_CALL" 

### FOREGROUND_SERVICE_REMOTE_MESSAGING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_REMOTE_MESSAGING

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "remoteMessaging". 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_REMOTE_MESSAGING" 

### FOREGROUND_SERVICE_SPECIAL_USE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_SPECIAL_USE

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "specialUse". 

Protection level: normal|appop|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_SPECIAL_USE" 

### FOREGROUND_SERVICE_SYSTEM_EXEMPTED

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) FOREGROUND_SERVICE_SYSTEM_EXEMPTED

Allows a regular application to use `[Service.startForeground](https://developer.android.com/reference/android/app/Service#startForeground\(int,%20android.app.Notification\))` with the type "systemExempted". Apps are allowed to use this type only in the use cases listed in `[ServiceInfo.FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED](https://developer.android.com/reference/android/content/pm/ServiceInfo#FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED)`. 

Protection level: normal|instant

Constant Value: "android.permission.FOREGROUND_SERVICE_SYSTEM_EXEMPTED" 

### GET_ACCOUNTS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) GET_ACCOUNTS

Allows access to the list of accounts in the Accounts Service. 

**Note:** Beginning with Android 6.0 (API level 23), if an app shares the signature of the authenticator that manages an account, it does not need `"GET_ACCOUNTS"` permission to read information about that account. On Android 5.1 and lower, all apps need `"GET_ACCOUNTS"` permission to read information about any account.

Protection level: dangerous

Constant Value: "android.permission.GET_ACCOUNTS" 

### GET_ACCOUNTS_PRIVILEGED

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) GET_ACCOUNTS_PRIVILEGED

Allows access to the list of accounts in the Accounts Service. 

Protection level: signature|privileged

Constant Value: "android.permission.GET_ACCOUNTS_PRIVILEGED" 

### GET_PACKAGE_SIZE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) GET_PACKAGE_SIZE

Allows an application to find out the space used by any package. 

Protection level: normal

Constant Value: "android.permission.GET_PACKAGE_SIZE" 

### GET_TASKS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) GET_TASKS

**This constant was deprecated in API level 21.**  
No longer enforced. 

Constant Value: "android.permission.GET_TASKS" 

### GLOBAL_SEARCH

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) GLOBAL_SEARCH

This permission can be used on content providers to allow the global search system to access their data. Typically it used when the provider has some permissions protecting it (which global search would not be expected to hold), and added as a read-only permission to the path in the provider where global search queries are performed. This permission can not be held by regular applications; it is used by applications to protect themselves from everyone else besides global search. 

Protection level: signature|privileged

Constant Value: "android.permission.GLOBAL_SEARCH" 

### HIDE_OVERLAY_WINDOWS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) HIDE_OVERLAY_WINDOWS

Allows an app to prevent non-system-overlay windows from being drawn on top of it

Constant Value: "android.permission.HIDE_OVERLAY_WINDOWS" 

### HIGH_SAMPLING_RATE_SENSORS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) HIGH_SAMPLING_RATE_SENSORS

Allows an app to access sensor data with a sampling rate greater than 200 Hz. 

Protection level: normal

Constant Value: "android.permission.HIGH_SAMPLING_RATE_SENSORS" 

### INSTALL_LOCATION_PROVIDER

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INSTALL_LOCATION_PROVIDER

Allows an application to install a location provider into the Location Manager. 

Not for use by third-party applications.

Constant Value: "android.permission.INSTALL_LOCATION_PROVIDER" 

### INSTALL_PACKAGES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INSTALL_PACKAGES

Allows an application to install packages. 

Not for use by third-party applications.

Constant Value: "android.permission.INSTALL_PACKAGES" 

### INSTALL_PACKAGES_AS_REGISTERED_APP_STORE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INSTALL_PACKAGES_AS_REGISTERED_APP_STORE

Permission to allow installing and updating apps as a registered app store. 

Protection level: role

Constant Value: "android.permission.INSTALL_PACKAGES_AS_REGISTERED_APP_STORE" 

### INSTALL_SHORTCUT

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INSTALL_SHORTCUT

Allows an application to install a shortcut in Launcher. 

In Android O (API level 26) and higher, the `INSTALL_SHORTCUT` broadcast no longer has any effect on your app because it's a private, implicit broadcast. Instead, you should create an app shortcut by using the `[requestPinShortcut()](https://developer.android.com/reference/android/content/pm/ShortcutManager#requestPinShortcut\(android.content.pm.ShortcutInfo,%20android.content.IntentSender\))` method from the `[ShortcutManager](https://developer.android.com/reference/android/content/pm/ShortcutManager)` class. 

Protection level: normal

Constant Value: "com.android.launcher.permission.INSTALL_SHORTCUT" 

### INSTANT_APP_FOREGROUND_SERVICE

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INSTANT_APP_FOREGROUND_SERVICE

Allows an instant app to create foreground services. 

Protection level: signature|development|instant|appop

Constant Value: "android.permission.INSTANT_APP_FOREGROUND_SERVICE" 

### INTERACT_ACROSS_PROFILES

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INTERACT_ACROSS_PROFILES

Allows interaction across profiles in the same profile group.

Constant Value: "android.permission.INTERACT_ACROSS_PROFILES" 

### INTERNET

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) INTERNET

Allows applications to open network sockets. 

Protection level: normal

Constant Value: "android.permission.INTERNET" 

### KILL_BACKGROUND_PROCESSES

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) KILL_BACKGROUND_PROCESSES

Allows an application to call `[ActivityManager.killBackgroundProcesses(String)](https://developer.android.com/reference/android/app/ActivityManager#killBackgroundProcesses\(java.lang.String\))`. 

As of Android version `[Build.VERSION_CODES.UPSIDE_DOWN_CAKE](https://developer.android.com/reference/android/os/Build.VERSION_CODES#UPSIDE_DOWN_CAKE)`, the `[ActivityManager.killBackgroundProcesses(String)](https://developer.android.com/reference/android/app/ActivityManager#killBackgroundProcesses\(java.lang.String\))` is no longer available to third party applications. For backwards compatibility, the background processes of the caller's own package will still be killed when calling this API. If the caller has the system permission `KILL_ALL_BACKGROUND_PROCESSES`, other processes will be killed too. 

Protection level: normal

Constant Value: "android.permission.KILL_BACKGROUND_PROCESSES" 

### LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE

Allows an application to capture screen content to perform a screenshot using the intent action `[Intent.ACTION_LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE](https://developer.android.com/reference/android/content/Intent#ACTION_LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE)`. 

Protection level: internal|role 

Intended for use by ROLE_NOTES only.

Constant Value: "android.permission.LAUNCH_CAPTURE_CONTENT_ACTIVITY_FOR_NOTE" 

### LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK

Added in [API level 32](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK

An application needs this permission for `[Settings.ACTION_SETTINGS_EMBED_DEEP_LINK_ACTIVITY](https://developer.android.com/reference/android/provider/Settings#ACTION_SETTINGS_EMBED_DEEP_LINK_ACTIVITY)` to show its `[Activity](https://developer.android.com/reference/android/app/Activity)` embedded in Settings app.

Constant Value: "android.permission.LAUNCH_MULTI_PANE_SETTINGS_DEEP_LINK" 

### LOADER_USAGE_STATS

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) LOADER_USAGE_STATS

Allows a data loader to read a package's access logs. The access logs contain the set of pages referenced over time. 

Declaring the permission implies intention to use the API and the user of the device can grant permission through the Settings application. 

Protection level: signature|privileged|appop 

A data loader has to be the one which provides data to install an app. 

A data loader has to have both permission:LOADER_USAGE_STATS AND appop:LOADER_USAGE_STATS allowed to be able to access the read logs.

Constant Value: "android.permission.LOADER_USAGE_STATS" 

### LOCATION_HARDWARE

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) LOCATION_HARDWARE

Allows an application to use location features in hardware, such as the geofencing api. 

Not for use by third-party applications.

Constant Value: "android.permission.LOCATION_HARDWARE" 

### LOCK_APPS

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) LOCK_APPS

Permission granted to apps holding the `[RoleManager.ROLE_HOME](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_HOME)` role that allows them to enable app lock. This is also granted to the recents component, which is typically the system launcher, to ensure a consistent user experience. App Lock is a feature that allows users to require authentication before opening apps. 

See `[PackageManager.getEnableAppLockIntentForPackage(String, boolean)](https://developer.android.com/reference/android/content/pm/PackageManager#getEnableAppLockIntentForPackage\(java.lang.String,%20boolean\))` and `[PackageManager.GET_APP_LOCK_INFO](https://developer.android.com/reference/android/content/pm/PackageManager#GET_APP_LOCK_INFO)` for more information about App Lock. 

Protection level: internal|role|recents

Constant Value: "android.permission.LOCK_APPS" 

### MANAGE_ASSISTANT_AUDIO

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_ASSISTANT_AUDIO

Allows control of audio behavior related to Assistant experiences, including routing, mode change and volume control of the Assistant audio stream. 

Protection level: signature|preinstalled|role|appop

Constant Value: "android.permission.MANAGE_ASSISTANT_AUDIO" 

### MANAGE_CONTACTS

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_CONTACTS

Allows an application to manage user's contacts. Intended to be used by a limited number of apps that need full management capabilities. 

Protection level: signature|preinstalled|appop

Constant Value: "android.permission.MANAGE_CONTACTS" 

### MANAGE_DEVICE_LOCK_STATE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_LOCK_STATE

Allows financed device kiosk apps to perform actions on the Device Lock service 

Protection level: internal|role 

Intended for use by the FINANCED_DEVICE_KIOSK role only.

Constant Value: "android.permission.MANAGE_DEVICE_LOCK_STATE" 

### MANAGE_DEVICE_POLICY_ACCESSIBILITY

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ACCESSIBILITY

Allows an application to manage policy related to accessibility. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ACCESSIBILITY" 

### MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT

Allows an application to set policy related to account management. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ACCOUNT_MANAGEMENT" 

### MANAGE_DEVICE_POLICY_ACROSS_USERS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ACROSS_USERS

Allows an application to set device policies outside the current user that are required for securing device ownership without accessing user data. 

Holding this permission allows the use of other held MANAGE_DEVICE_POLICY_* permissions across all users on the device provided they do not grant access to user data. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS" 

### MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL

Allows an application to set device policies outside the current user. 

Fuller form of `[MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` that removes the restriction on accessing user data. 

Holding this permission allows the use of any other held MANAGE_DEVICE_POLICY_* permissions across all users on the device. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL" 

### MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL

Allows an application to set device policies outside the current user that are critical for securing data within the current user. 

Holding this permission allows the use of other held MANAGE_DEVICE_POLICY_* permissions across all users on the device provided they are required for securing data within the current user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL" 

### MANAGE_DEVICE_POLICY_AIRPLANE_MODE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_AIRPLANE_MODE

Allows an application to set policy related to airplane mode. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_AIRPLANE_MODE" 

### MANAGE_DEVICE_POLICY_APPS_CONTROL

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_APPS_CONTROL

Allows an application to manage policy regarding modifying applications. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_APPS_CONTROL" 

### MANAGE_DEVICE_POLICY_APP_FUNCTIONS

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_APP_FUNCTIONS

Allows an application to manage policy related to AppFunctions. 

Protection level: internal|role

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_APP_FUNCTIONS" 

### MANAGE_DEVICE_POLICY_APP_RESTRICTIONS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_APP_RESTRICTIONS

Allows an application to manage application restrictions. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_APP_RESTRICTIONS" 

### MANAGE_DEVICE_POLICY_APP_USER_DATA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_APP_USER_DATA

Allows an application to manage policy related to application user data. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_APP_USER_DATA" 

### MANAGE_DEVICE_POLICY_ASSIST_CONTENT

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ASSIST_CONTENT

Allows an application to set policy related to sending assist content to a privileged app such as the Assistant app. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ASSIST_CONTENT" 

### MANAGE_DEVICE_POLICY_AUDIO_OUTPUT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_AUDIO_OUTPUT

Allows an application to set policy related to audio output. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_AUDIO_OUTPUT" 

### MANAGE_DEVICE_POLICY_AUTOFILL

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_AUTOFILL

Allows an application to set policy related to autofill. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_AUTOFILL" 

### MANAGE_DEVICE_POLICY_BACKUP_SERVICE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_BACKUP_SERVICE

Allows an application to manage backup service policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_BACKUP_SERVICE" 

### MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL

Allows an application to manage policy related to block package uninstallation. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_BLOCK_UNINSTALL" 

### MANAGE_DEVICE_POLICY_BLUETOOTH

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_BLUETOOTH

Allows an application to set policy related to bluetooth. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_BLUETOOTH" 

### MANAGE_DEVICE_POLICY_BUGREPORT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_BUGREPORT

Allows an application to request bugreports with user consent. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_BUGREPORT" 

### MANAGE_DEVICE_POLICY_CALLS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_CALLS

Allows an application to manage calling policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_CALLS" 

### MANAGE_DEVICE_POLICY_CAMERA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_CAMERA

Allows an application to set policy related to restricting a user's ability to use or enable and disable the camera. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_CAMERA" 

### MANAGE_DEVICE_POLICY_CAMERA_TOGGLE

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_CAMERA_TOGGLE

Allows an application to manage policy related to camera toggle. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_CAMERA_TOGGLE" 

### MANAGE_DEVICE_POLICY_CERTIFICATES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_CERTIFICATES

Allows an application to set policy related to certificates. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_CERTIFICATES" 

### MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE

Allows an application to manage policy related to common criteria mode. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_COMMON_CRITERIA_MODE" 

### MANAGE_DEVICE_POLICY_CONTENT_PROTECTION

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_CONTENT_PROTECTION

Allows an application to manage policy related to content protection. 

Protection level: internal|role

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_CONTENT_PROTECTION" 

### MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES

Allows an application to manage debugging features policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_DEBUGGING_FEATURES" 

### MANAGE_DEVICE_POLICY_DEFAULT_SMS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_DEFAULT_SMS

Allows an application to set policy related to the default sms application. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_DEFAULT_SMS" 

### MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS

Allows an application to manage policy related to device identifiers. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_DEVICE_IDENTIFIERS" 

### MANAGE_DEVICE_POLICY_DISPLAY

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_DISPLAY

Allows an application to set policy related to the display. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_DISPLAY" 

### MANAGE_DEVICE_POLICY_FACTORY_RESET

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_FACTORY_RESET

Allows an application to set policy related to factory reset. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_FACTORY_RESET" 

### MANAGE_DEVICE_POLICY_FUN

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_FUN

Allows an application to set policy related to fun. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_FUN" 

### MANAGE_DEVICE_POLICY_INPUT_METHODS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_INPUT_METHODS

Allows an application to set policy related to input methods. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_INPUT_METHODS" 

### MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES

Allows an application to manage installing from unknown sources policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_INSTALL_UNKNOWN_SOURCES" 

### MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES

Allows an application to set policy related to keeping uninstalled packages. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_KEEP_UNINSTALLED_PACKAGES" 

### MANAGE_DEVICE_POLICY_KEYGUARD

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_KEYGUARD

Allows an application to manage policy related to keyguard features. Like whether the camera, notifications are allowed on the secure keyguard screens. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_KEYGUARD" 

### MANAGE_DEVICE_POLICY_LOCALE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_LOCALE

Allows an application to set policy related to locale. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_LOCALE" 

### MANAGE_DEVICE_POLICY_LOCATION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_LOCATION

Allows an application to set policy related to location. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_LOCATION" 

### MANAGE_DEVICE_POLICY_LOCK

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_LOCK

Allows an application to lock a profile or the device with the appropriate cross-user permission. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_LOCK" 

### MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS

Allows an application to set policy related to lock credentials. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_SECURITY_CRITICAL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_LOCK_CREDENTIALS" 

### MANAGE_DEVICE_POLICY_LOCK_TASK

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_LOCK_TASK

Allows an application to manage lock task policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_LOCK_TASK" 

### MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS

Allows an application to set policy related to subscriptions downloaded by an admin. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MANAGED_SUBSCRIPTIONS" 

### MANAGE_DEVICE_POLICY_METERED_DATA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_METERED_DATA

Allows an application to manage policy related to metered data. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_METERED_DATA" 

### MANAGE_DEVICE_POLICY_MICROPHONE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MICROPHONE

Allows an application to set policy related to restricting a user's ability to use or enable and disable the microphone. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MICROPHONE" 

### MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE

Allows an application to manage policy related to microphone toggle. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MICROPHONE_TOGGLE" 

### MANAGE_DEVICE_POLICY_MOBILE_NETWORK

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MOBILE_NETWORK

Allows an application to set policy related to mobile networks. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MOBILE_NETWORK" 

### MANAGE_DEVICE_POLICY_MODIFY_USERS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MODIFY_USERS

Allows an application to manage policy preventing users from modifying users. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MODIFY_USERS" 

### MANAGE_DEVICE_POLICY_MTE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_MTE

Allows an application to manage policy related to the Memory Tagging Extension (MTE). 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_MTE" 

### MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION

Allows an application to set policy related to nearby communications (e.g. Beam and nearby streaming). 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_NEARBY_COMMUNICATION" 

### MANAGE_DEVICE_POLICY_NETWORK_LOGGING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_NETWORK_LOGGING

Allows an application to set policy related to network logging. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_NETWORK_LOGGING" 

### MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY

Allows an application to manage the identity of the managing organization. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_ORGANIZATION_IDENTITY" 

### MANAGE_DEVICE_POLICY_OVERRIDE_APN

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_OVERRIDE_APN

Allows an application to set policy related to override APNs. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_OVERRIDE_APN" 

### MANAGE_DEVICE_POLICY_PACKAGE_STATE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PACKAGE_STATE

Allows an application to set policy related to hiding and suspending packages. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PACKAGE_STATE" 

### MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA

Allows an application to set policy related to physical media. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PHYSICAL_MEDIA" 

### MANAGE_DEVICE_POLICY_PRINTING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PRINTING

Allows an application to set policy related to printing. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PRINTING" 

### MANAGE_DEVICE_POLICY_PRIVATE_DNS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PRIVATE_DNS

Allows an application to set policy related to private DNS. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PRIVATE_DNS" 

### MANAGE_DEVICE_POLICY_PROFILES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PROFILES

Allows an application to set policy related to profiles. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PROFILES" 

### MANAGE_DEVICE_POLICY_PROFILE_INTERACTION

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PROFILE_INTERACTION

Allows an application to set policy related to interacting with profiles (e.g. Disallowing cross-profile copy and paste). 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PROFILE_INTERACTION" 

### MANAGE_DEVICE_POLICY_PROXY

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_PROXY

Allows an application to set a network-independent global HTTP proxy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_PROXY" 

### MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES

Allows an application query system updates. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_QUERY_SYSTEM_UPDATES" 

### MANAGE_DEVICE_POLICY_RESET_PASSWORD

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_RESET_PASSWORD

Allows an application to force set a new device unlock password or a managed profile challenge on current user. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_RESET_PASSWORD" 

### MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS

Allows an application to set policy related to restricting the user from configuring private DNS. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_RESTRICT_PRIVATE_DNS" 

### MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS

Allows an application to set the grant state of runtime permissions on packages. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_RUNTIME_PERMISSIONS" 

### MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND

Allows an application to set policy related to users running in the background. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_RUN_IN_BACKGROUND" 

### MANAGE_DEVICE_POLICY_SAFE_BOOT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SAFE_BOOT

Allows an application to manage safe boot policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SAFE_BOOT" 

### MANAGE_DEVICE_POLICY_SCREEN_CAPTURE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SCREEN_CAPTURE

Allows an application to set policy related to screen capture. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SCREEN_CAPTURE" 

### MANAGE_DEVICE_POLICY_SCREEN_CONTENT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SCREEN_CONTENT

Allows an application to set policy related to the usage of the contents of the screen. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SCREEN_CONTENT" 

### MANAGE_DEVICE_POLICY_SECURITY_LOGGING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SECURITY_LOGGING

Allows an application to set policy related to security logging. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SECURITY_LOGGING" 

### MANAGE_DEVICE_POLICY_SETTINGS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SETTINGS

Allows an application to set policy related to settings. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SETTINGS" 

### MANAGE_DEVICE_POLICY_SMS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SMS

Allows an application to set policy related to sms. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SMS" 

### MANAGE_DEVICE_POLICY_STATUS_BAR

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_STATUS_BAR

Allows an application to set policy related to the status bar. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_STATUS_BAR" 

### MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE

Allows an application to set support messages for when a user action is affected by an active policy. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SUPPORT_MESSAGE" 

### MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS

Allows an application to set policy related to suspending personal apps. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SUSPEND_PERSONAL_APPS" 

### MANAGE_DEVICE_POLICY_SYSTEM_APPS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SYSTEM_APPS

Allows an application to manage policy related to system apps. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SYSTEM_APPS" 

### MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS

Allows an application to set policy related to system dialogs. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SYSTEM_DIALOGS" 

### MANAGE_DEVICE_POLICY_SYSTEM_UPDATES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_SYSTEM_UPDATES

Allows an application to set policy related to system updates. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_SYSTEM_UPDATES" 

### MANAGE_DEVICE_POLICY_THREAD_NETWORK

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_THREAD_NETWORK

Allows an application to set policy related to [Thread](https://www.threadgroup.org) network. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_THREAD_NETWORK" 

### MANAGE_DEVICE_POLICY_TIME

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_TIME

Allows an application to manage device policy relating to time. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_TIME" 

### MANAGE_DEVICE_POLICY_UNIVERSAL_CLIPBOARD

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_UNIVERSAL_CLIPBOARD

Allows an application to manage policy related to Universal Clipboard feature. 

`[MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_UNIVERSAL_CLIPBOARD" 

### MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING

Allows an application to set policy related to usb data signalling. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_USB_DATA_SIGNALLING" 

### MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER

Allows an application to set policy related to usb file transfers. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_USB_FILE_TRANSFER" 

### MANAGE_DEVICE_POLICY_USERS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_USERS

Allows an application to set policy related to users. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_USERS" 

### MANAGE_DEVICE_POLICY_VPN

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_VPN

Allows an application to set policy related to VPNs. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_VPN" 

### MANAGE_DEVICE_POLICY_WALLPAPER

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_WALLPAPER

Allows an application to set policy related to the wallpaper. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_WALLPAPER" 

### MANAGE_DEVICE_POLICY_WIFI

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_WIFI

Allows an application to set policy related to Wifi. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_WIFI" 

### MANAGE_DEVICE_POLICY_WINDOWS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_WINDOWS

Allows an application to set policy related to windows. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS_FULL)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_WINDOWS" 

### MANAGE_DEVICE_POLICY_WIPE_DATA

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DEVICE_POLICY_WIPE_DATA

Allows an application to manage policy related to wiping data. 

`[Manifest.permission.MANAGE_DEVICE_POLICY_ACROSS_USERS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DEVICE_POLICY_ACROSS_USERS)` is required to call APIs protected by this permission on users different to the calling user. 

Protection level: internal|role 

Intended for use by the DEVICE_POLICY_MANAGEMENT role only.

Constant Value: "android.permission.MANAGE_DEVICE_POLICY_WIPE_DATA" 

### MANAGE_DOCUMENTS

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_DOCUMENTS

Allows an application to manage access to documents, usually as part of a document picker. 

This permission should _only_ be held by the platform document management app and the shell (for CTS). This permission cannot be granted to third-party apps.

Constant Value: "android.permission.MANAGE_DOCUMENTS" 

### MANAGE_EXTERNAL_STORAGE

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_EXTERNAL_STORAGE

Allows an application a broad access to external storage in scoped storage. Intended to be used by few apps that need to manage files on behalf of the users. 

Protection level: signature|appop|preinstalled

Constant Value: "android.permission.MANAGE_EXTERNAL_STORAGE" 

### MANAGE_MEDIA

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_MEDIA

Allows an application to modify and delete media files on this device or any connected storage device without user confirmation. Applications must already be granted the `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` or `[MANAGE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE)`} permissions for this permission to take effect. 

Even if applications are granted this permission, if applications want to modify or delete media files, they also must get the access by calling `[MediaStore.createWriteRequest(ContentResolver, Collection)](https://developer.android.com/reference/android/provider/MediaStore#createWriteRequest\(android.content.ContentResolver,%20java.util.Collection<android.net.Uri>\))`, `[MediaStore.createDeleteRequest(ContentResolver, Collection)](https://developer.android.com/reference/android/provider/MediaStore#createDeleteRequest\(android.content.ContentResolver,%20java.util.Collection<android.net.Uri>\))`, or `[MediaStore.createTrashRequest(ContentResolver, Collection, boolean)](https://developer.android.com/reference/android/provider/MediaStore#createTrashRequest\(android.content.ContentResolver,%20java.util.Collection<android.net.Uri>,%20boolean\))`. 

This permission doesn't give read or write access directly. It only prevents the user confirmation dialog for these requests. 

If applications are not granted `[ACCESS_MEDIA_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION)`, the system also pops up the user confirmation dialog for the write request. 

Protection level: signature|appop|preinstalled

Constant Value: "android.permission.MANAGE_MEDIA" 

### MANAGE_ONGOING_CALLS

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_ONGOING_CALLS

Allows to query ongoing call details and manage ongoing calls 

Protection level: signature|appop

Constant Value: "android.permission.MANAGE_ONGOING_CALLS" 

### MANAGE_OWN_CALLS

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_OWN_CALLS

Allows a calling application which manages its own calls through the self-managed `[ConnectionService](https://developer.android.com/reference/android/telecom/ConnectionService)` APIs. See `[PhoneAccount.CAPABILITY_SELF_MANAGED](https://developer.android.com/reference/android/telecom/PhoneAccount#CAPABILITY_SELF_MANAGED)` for more information on the self-managed ConnectionService APIs. 

Protection level: normal

Constant Value: "android.permission.MANAGE_OWN_CALLS" 

### MANAGE_PERIPHERAL_CUSTOMIZATION

Added in [version 37.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_PERIPHERAL_CUSTOMIZATION

Allows an application to manage peripheral customization. 

Protection level: internal|appop

Constant Value: "android.permission.MANAGE_PERIPHERAL_CUSTOMIZATION" 

### MANAGE_WIFI_INTERFACES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_WIFI_INTERFACES

Allows applications to get notified when a Wi-Fi interface request cannot be satisfied without tearing down one or more other interfaces, and provide a decision whether to approve the request or reject it. 

Not for use by third-party applications.

Constant Value: "android.permission.MANAGE_WIFI_INTERFACES" 

### MANAGE_WIFI_NETWORK_SELECTION

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MANAGE_WIFI_NETWORK_SELECTION

This permission is used to let OEMs grant their trusted app access to a subset of privileged wifi APIs to improve wifi performance. Allows applications to manage Wi-Fi network selection related features such as enable or disable global auto-join, modify connectivity scan intervals, and approve Wi-Fi Direct connections. 

Not for use by third-party applications.

Constant Value: "android.permission.MANAGE_WIFI_NETWORK_SELECTION" 

### MASTER_CLEAR

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MASTER_CLEAR

Not for use by third-party applications.

Constant Value: "android.permission.MASTER_CLEAR" 

### MEDIA_CONTENT_CONTROL

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MEDIA_CONTENT_CONTROL

Allows an application to know what content is playing and control its playback. 

Not for use by third-party applications due to privacy of media consumption

Constant Value: "android.permission.MEDIA_CONTENT_CONTROL" 

### MEDIA_ROUTING_CONTROL

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MEDIA_ROUTING_CONTROL

Allows an application to control the routing of media apps. 

Only for use by role COMPANION_DEVICE_WATCH

Constant Value: "android.permission.MEDIA_ROUTING_CONTROL" 

### MODIFY_AUDIO_SETTINGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MODIFY_AUDIO_SETTINGS

Allows an application to modify global audio settings. 

Protection level: normal

Constant Value: "android.permission.MODIFY_AUDIO_SETTINGS" 

### MODIFY_PHONE_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MODIFY_PHONE_STATE

Allows modification of the telephony state - power on, mmi, etc. Does not include placing calls. 

Not for use by third-party applications.

Constant Value: "android.permission.MODIFY_PHONE_STATE" 

### MOUNT_FORMAT_FILESYSTEMS

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MOUNT_FORMAT_FILESYSTEMS

Allows formatting file systems for removable storage. 

Not for use by third-party applications.

Constant Value: "android.permission.MOUNT_FORMAT_FILESYSTEMS" 

### MOUNT_UNMOUNT_FILESYSTEMS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) MOUNT_UNMOUNT_FILESYSTEMS

Allows mounting and unmounting file systems for removable storage. 

Not for use by third-party applications.

Constant Value: "android.permission.MOUNT_UNMOUNT_FILESYSTEMS" 

### NEARBY_WIFI_DEVICES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) NEARBY_WIFI_DEVICES

Required to be able to advertise and connect to nearby devices via Wi-Fi. 

Protection level: dangerous

Constant Value: "android.permission.NEARBY_WIFI_DEVICES" 

### NFC

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) NFC

Allows applications to perform I/O operations over NFC. 

Protection level: normal

Constant Value: "android.permission.NFC" 

### NFC_PREFERRED_PAYMENT_INFO

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) NFC_PREFERRED_PAYMENT_INFO

Allows applications to receive NFC preferred payment service information. 

Protection level: normal

Constant Value: "android.permission.NFC_PREFERRED_PAYMENT_INFO" 

### NFC_TRANSACTION_EVENT

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) NFC_TRANSACTION_EVENT

Allows applications to receive NFC transaction events. 

Protection level: normal

Constant Value: "android.permission.NFC_TRANSACTION_EVENT" 

### OVERRIDE_MEDIA_SESSION_OWNER

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) OVERRIDE_MEDIA_SESSION_OWNER

Allows an application to override the owner of a MediaSession. 

Not for use by third-party applications due to privacy of media applications.

Constant Value: "android.permission.OVERRIDE_MEDIA_SESSION_OWNER" 

### OVERRIDE_WIFI_CONFIG

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) OVERRIDE_WIFI_CONFIG

Allows an application to modify any wifi configuration, even if created by another application. Once reconfigured the original creator cannot make any further modifications. 

Not for use by third-party applications.

Constant Value: "android.permission.OVERRIDE_WIFI_CONFIG" 

### PACKAGE_USAGE_STATS

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PACKAGE_USAGE_STATS

Allows an application to collect component usage statistics 

Declaring the permission implies intention to use the API and the user of the device can grant permission through the Settings application. 

Protection level: signature|privileged|development|appop|retailDemo

Constant Value: "android.permission.PACKAGE_USAGE_STATS" 

### PERSISTENT_ACTIVITY

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PERSISTENT_ACTIVITY

**This constant was deprecated in API level 15.**  
This functionality will be removed in the future; please do not use. Allow an application to make its activities persistent. 

Constant Value: "android.permission.PERSISTENT_ACTIVITY" 

### POST_NOTIFICATIONS

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) POST_NOTIFICATIONS

Allows an app to post notifications 

Protection level: dangerous

Constant Value: "android.permission.POST_NOTIFICATIONS" 

### POST_PROMOTED_NOTIFICATIONS

Added in [version 36.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) POST_PROMOTED_NOTIFICATIONS

Required for apps to post promoted notifications. 

This is required in addition to (not instead of) `[POST_NOTIFICATIONS](https://developer.android.com/reference/android/Manifest.permission#POST_NOTIFICATIONS)`. 

Protection level: normal|appops

Constant Value: "android.permission.POST_PROMOTED_NOTIFICATIONS" 

### PROCESS_OUTGOING_CALLS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROCESS_OUTGOING_CALLS

**This constant was deprecated in API level 29.**  
Applications should use `[CallRedirectionService](https://developer.android.com/reference/android/telecom/CallRedirectionService)` instead of the `[Intent.ACTION_NEW_OUTGOING_CALL](https://developer.android.com/reference/android/content/Intent#ACTION_NEW_OUTGOING_CALL)` broadcast. 

Allows an application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.PROCESS_OUTGOING_CALLS" 

### PROVIDE_OWN_AUTOFILL_SUGGESTIONS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROVIDE_OWN_AUTOFILL_SUGGESTIONS

Allows an application to display its suggestions using the autofill framework. 

For now, this permission is only granted to the Browser application. 

Protection level: internal|role

Constant Value: "android.permission.PROVIDE_OWN_AUTOFILL_SUGGESTIONS" 

### PROVIDE_PRIVATE_COMPUTE_SERVICES

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROVIDE_PRIVATE_COMPUTE_SERVICES

Allows an application to act as Private Compute Services, which allows the application to communicate with Private Compute Core components. 

Protection level: signature|privileged

Constant Value: "android.permission.PROVIDE_PRIVATE_COMPUTE_SERVICES" 

### PROVIDE_REMOTE_CREDENTIALS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) PROVIDE_REMOTE_CREDENTIALS

Allows an application to be able to store and retrieve credentials from a remote device. 

Protection level: signature|privileged|role

Constant Value: "android.permission.PROVIDE_REMOTE_CREDENTIALS" 

### QUERY_ADVANCED_PROTECTION_MODE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) QUERY_ADVANCED_PROTECTION_MODE

Allows an application to query the device's advanced protection mode status.

Constant Value: "android.permission.QUERY_ADVANCED_PROTECTION_MODE" 

### QUERY_ALL_PACKAGES

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) QUERY_ALL_PACKAGES

Allows query of any normal app on the device, regardless of manifest declarations. 

Protection level: normal

Constant Value: "android.permission.QUERY_ALL_PACKAGES" 

### QUERY_APP_USAGE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) QUERY_APP_USAGE

Allows the holder to query app usage stats. 

Protection level: internal|role 

See `[UsageStatsManager.queryAppUsageDuration(AppUsageDurationQuery)](https://developer.android.com/reference/android/app/usage/UsageStatsManager#queryAppUsageDuration\(android.app.usage.AppUsageDurationQuery\))`.

Constant Value: "android.permission.QUERY_APP_USAGE" 

### RANGING

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RANGING

Required to be able to range to devices using generic ranging module. 

Protection level: dangerous

Constant Value: "android.permission.RANGING" 

### READ_ASSISTANT_APP_SEARCH_DATA

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_ASSISTANT_APP_SEARCH_DATA

Allows an application to query over global data in AppSearch that's visible to the ASSISTANT role.

Constant Value: "android.permission.READ_ASSISTANT_APP_SEARCH_DATA" 

### READ_ASSIST_STRUCTURE_SCREEN_CONTENT

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_ASSIST_STRUCTURE_SCREEN_CONTENT

Allows an assistant application to read screen content in the AssistStructure. 

**Note:** Beginning with `[ERROR(C android.os.Build.VERSION_CODES.CINNAMON_BUN /Android C android.os.Build.VERSION_CODES.CINNAMON_BUN)](https://developer.android.com/)` This permission is required by any VoiceInteractionService that wishes to receive screen content in the AssistStructure when the assistant's VoiceInteractionService is invoked either via hotword detection or from the system. If this permission is not held, the AssistStructure will only obtain window data and will omit any screen content from the provided AssistStructure. 

Protection level: normal

Constant Value: "android.permission.READ_ASSIST_STRUCTURE_SCREEN_CONTENT" 

### READ_BASIC_PHONE_STATE

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_BASIC_PHONE_STATE

Allows read only access to phone state with a non dangerous permission, including the information like cellular network type, software version.

Constant Value: "android.permission.READ_BASIC_PHONE_STATE" 

### READ_CALENDAR

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_CALENDAR

Allows an application to read the user's calendar data. 

Protection level: dangerous

Constant Value: "android.permission.READ_CALENDAR" 

### READ_CALL_LOG

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_CALL_LOG

Allows an application to read the user's call log. 

**Note:** If your app uses the `[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)` permission and _both_ your [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) and [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) values are set to 15 or lower, the system implicitly grants your app this permission. If you don't need this permission, be sure your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) is 16 or higher.

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.READ_CALL_LOG" 

### READ_COLOR_ZONES

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_COLOR_ZONES

Allows an application to read the aggregated color zones on the screen for use cases like TV ambient backlight usages. 

Protection level: normal

Constant Value: "android.permission.READ_COLOR_ZONES" 

### READ_CONTACTS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_CONTACTS

Allows an application to read the user's contacts data. 

Protection level: dangerous

Constant Value: "android.permission.READ_CONTACTS" 

### READ_DROPBOX_DATA

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_DROPBOX_DATA

Allows an application to access the data in Dropbox. 

Not for use by third-party applications.

Constant Value: "android.permission.READ_DROPBOX_DATA" 

### READ_EXTERNAL_STORAGE

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_EXTERNAL_STORAGE

Allows an application to read from external storage. 

**Note:** Starting in API level 33, this permission has no effect. If your app accesses other apps' media files, request one or more of these permissions instead: `READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, `READ_MEDIA_AUDIO`. Learn more about the [storage permissions](https://developer.android.com/training/data-storage/shared/media#storage-permission) that are associated with media files.

This permission is enforced starting in API level 19. Before API level 19, this permission is not enforced and all apps still have access to read from external storage. You can test your app with the permission enforced by enabling _Protect USB storage_ under **Developer options** in the Settings app on a device running Android 4.1 or higher.

Also starting in API level 19, this permission is _not_ required to read or write files in your application-specific directories returned by `[Context.getExternalFilesDir(String)](https://developer.android.com/reference/android/content/Context#getExternalFilesDir\(java.lang.String\))` and `[Context.getExternalCacheDir()](https://developer.android.com/reference/android/content/Context#getExternalCacheDir\(\))`.

Starting in API level 29, apps don't need to request this permission to access files in their app-specific directory on external storage, or their own files in the [`MediaStore`](https://developer.android.com/reference/android/provider/MediaStore). Apps shouldn't request this permission unless they need to access other apps' files in the `MediaStore`. Read more about these changes in the [scoped storage](https://developer.android.com/training/data-storage#scoped-storage) section of the developer documentation.

If _both_ your [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) and [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) values are set to 3 or lower, the system implicitly grants your app this permission. If you don't need this permission, be sure your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) is 4 or higher.

This is a soft restricted permission which cannot be held by an app it its full form until the installer on record allowlists the permission. Specifically, if the permission is allowlisted the holder app can access external storage and the visual and aural media collections while if the permission is not allowlisted the holder app can only access to the visual and aural medial collections. Also the permission is immutably restricted meaning that the allowlist state can be specified only at install time and cannot change until the app is installed. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`. 

Protection level: dangerous

Constant Value: "android.permission.READ_EXTERNAL_STORAGE" 

### READ_HOME_APP_SEARCH_DATA

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_HOME_APP_SEARCH_DATA

Allows an application to query over global data in AppSearch that's visible to the HOME role.

Constant Value: "android.permission.READ_HOME_APP_SEARCH_DATA" 

### READ_HOME_TIME_ZONE

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_HOME_TIME_ZONE

Allows applications to read the home time zone. 

Protection level: signature|privileged|role

Constant Value: "android.permission.READ_HOME_TIME_ZONE" 

### READ_INPUT_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_INPUT_STATE

**This constant was deprecated in API level 16.**  
The API that used this permission has been removed. 

Allows an application to retrieve the current state of keys and switches. 

Not for use by third-party applications.

Constant Value: "android.permission.READ_INPUT_STATE" 

### READ_LOGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_LOGS

Allows an application to read the low-level system log files. 

Not for use by third-party applications, because Log entries can contain the user's private information.

Constant Value: "android.permission.READ_LOGS" 

### READ_MEDIA_AUDIO

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_MEDIA_AUDIO

Allows an application to read audio files from external storage. 

This permission is enforced starting in API level `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)`. An app which targets `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` or higher and needs to read audio files from external storage must hold this permission; `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` is not required. For apps with a [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) of `[Build.VERSION_CODES.S_V2](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S_V2)` or lower, the `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` permission is required, instead, to read audio files. 

Protection level: dangerous

Constant Value: "android.permission.READ_MEDIA_AUDIO" 

### READ_MEDIA_IMAGES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_MEDIA_IMAGES

Allows an application to read image files from external storage. 

This permission is enforced starting in API level `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)`. An app which targets `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` or higher and needs to read image files from external storage must hold this permission; `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` is not required. For apps with a [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) of `[Build.VERSION_CODES.S_V2](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S_V2)` or lower, the `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` permission is required, instead, to read image files. 

Protection level: dangerous

Constant Value: "android.permission.READ_MEDIA_IMAGES" 

### READ_MEDIA_VIDEO

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_MEDIA_VIDEO

Allows an application to read video files from external storage. 

This permission is enforced starting in API level `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)`. An app which targets `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` or higher and needs to read video files from external storage must hold this permission; `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` is not required. For apps with a [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) of `[Build.VERSION_CODES.S_V2](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S_V2)` or lower, the `[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE)` permission is required, instead, to read video files. 

Protection level: dangerous

Constant Value: "android.permission.READ_MEDIA_VIDEO" 

### READ_MEDIA_VISUAL_USER_SELECTED

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_MEDIA_VISUAL_USER_SELECTED

Allows an application to read image or video files from external storage that a user has selected via the permission prompt photo picker. Apps can check this permission to verify that a user has decided to use the photo picker, instead of granting access to `[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)` or `[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO)`. It does not prevent apps from accessing the standard photo picker manually. This permission should be requested alongside `[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)` and/or `[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO)`, depending on which type of media is desired. 

This permission will be automatically added to an app's manifest if the app requests `[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)`, `[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO)`, or `[ACCESS_MEDIA_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION)` regardless of target SDK. If an app does not request this permission, then the grant dialog will return `PERMISSION_GRANTED` for `[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)` and/or `[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO)`, but the app will only have access to the media selected by the user. This false grant state will persist until the app goes into the background. 

Protection level: dangerous

Constant Value: "android.permission.READ_MEDIA_VISUAL_USER_SELECTED" 

### READ_NEARBY_STREAMING_POLICY

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_NEARBY_STREAMING_POLICY

Allows an application to read nearby streaming policy. The policy controls whether to allow the device to stream its notifications and apps to nearby devices. Applications that are not the device owner will need this permission to call `[DevicePolicyManager.getNearbyNotificationStreamingPolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getNearbyNotificationStreamingPolicy\(\))` or `[DevicePolicyManager.getNearbyAppStreamingPolicy()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#getNearbyAppStreamingPolicy\(\))`.

Constant Value: "android.permission.READ_NEARBY_STREAMING_POLICY" 

### READ_PHONE_NUMBERS

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_PHONE_NUMBERS

Allows read access to the device's phone number(s), which is exposed to instant applications. 

Protection level: dangerous

Constant Value: "android.permission.READ_PHONE_NUMBERS" 

### READ_PHONE_STATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_PHONE_STATE

Allows read only access to phone state, including the current cellular network information, the status of any ongoing calls, and a list of any `[PhoneAccount](https://developer.android.com/reference/android/telecom/PhoneAccount)`s registered on the device. 

**Note:** If _both_ your [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) and [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) values are set to 3 or lower, the system implicitly grants your app this permission. If you don't need this permission, be sure your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) is 4 or higher. 

Protection level: dangerous

Constant Value: "android.permission.READ_PHONE_STATE" 

### READ_PRECISE_PHONE_STATE

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_PRECISE_PHONE_STATE

Allows read only access to precise phone state. Allows reading of detailed information about phone state for special-use applications such as dialers, carrier applications, or ims applications.

Constant Value: "android.permission.READ_PRECISE_PHONE_STATE" 

### READ_SMS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_SMS

Allows an application to read SMS messages. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.READ_SMS" 

### READ_SYNC_SETTINGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_SYNC_SETTINGS

Allows applications to read the sync settings. 

Protection level: normal

Constant Value: "android.permission.READ_SYNC_SETTINGS" 

### READ_SYNC_STATS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_SYNC_STATS

Allows applications to read the sync stats. 

Protection level: normal

Constant Value: "android.permission.READ_SYNC_STATS" 

### READ_SYSTEM_PREFERENCES

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_SYSTEM_PREFERENCES

Allows an application to access the Settings Preference services to read settings exposed by the system Settings app and system apps that contribute settings surfaced by the Settings app. 

This allows the calling application to read settings values through the host application, agnostic of underlying storage.

Constant Value: "android.permission.READ_SYSTEM_PREFERENCES" 

### READ_UPDATE_ENGINE_LOGS

Added in [version 37.2](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_UPDATE_ENGINE_LOGS

Allows an application to read the update_engine logs 

Not for use by third-party applications.

Constant Value: "android.permission.READ_UPDATE_ENGINE_LOGS" 

### READ_VOICEMAIL

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) READ_VOICEMAIL

Allows an application to read voicemails in the system. 

Protection level: signature|privileged|role

Constant Value: "com.android.voicemail.permission.READ_VOICEMAIL" 

### REBOOT

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REBOOT

Required to be able to reboot the device. 

Not for use by third-party applications.

Constant Value: "android.permission.REBOOT" 

### RECEIVE_BOOT_COMPLETED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECEIVE_BOOT_COMPLETED

Allows an application to receive the `[Intent.ACTION_BOOT_COMPLETED](https://developer.android.com/reference/android/content/Intent#ACTION_BOOT_COMPLETED)` that is broadcast after the system finishes booting. If you don't request this permission, you will not receive the broadcast at that time. Though holding this permission does not have any security implications, it can have a negative impact on the user experience by increasing the amount of time it takes the system to start and allowing applications to have themselves running without the user being aware of them. As such, you must explicitly declare your use of this facility to make that visible to the user. 

Protection level: normal

Constant Value: "android.permission.RECEIVE_BOOT_COMPLETED" 

### RECEIVE_MMS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECEIVE_MMS

Allows an application to monitor incoming MMS messages. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.RECEIVE_MMS" 

### RECEIVE_SENSITIVE_NOTIFICATIONS

Added in [version 36.1](https://developer.android.com/topic/libraries/support-library/revisions)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECEIVE_SENSITIVE_NOTIFICATIONS

Allows apps with a NotificationListenerService to receive notifications with sensitive information 

Apps with a NotificationListenerService without this permission will not be able to view certain types of sensitive information contained in notifications 

This permission also allows apps with the SMS permissions to query and receive broadcasts about SMS messages that contain One Time Passwords 

Protection level: signature|preinstalled|knownSigner|role

Constant Value: "android.permission.RECEIVE_SENSITIVE_NOTIFICATIONS" 

### RECEIVE_SMS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECEIVE_SMS

Allows an application to receive SMS messages. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.RECEIVE_SMS" 

### RECEIVE_WAP_PUSH

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECEIVE_WAP_PUSH

Allows an application to receive WAP push messages. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.RECEIVE_WAP_PUSH" 

### RECORD_AUDIO

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RECORD_AUDIO

Allows an application to record audio. 

Protection level: dangerous

Constant Value: "android.permission.RECORD_AUDIO" 

### REORDER_TASKS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REORDER_TASKS

Allows an application to change the Z-order of tasks. 

Protection level: normal

Constant Value: "android.permission.REORDER_TASKS" 

### REPOSITION_SELF_WINDOWS

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REPOSITION_SELF_WINDOWS

Allows an application to programmatically move and resize its tasks when the system is in a state that allows such operations, e.g. in a desktop-like environment. It is only extended to the `[default browser](https://developer.android.com/reference/android/app/role/RoleManager#ROLE_BROWSER)` and OEM specific signature apps. 

Protection level: signature|role

Constant Value: "android.permission.REPOSITION_SELF_WINDOWS" 

### REQUEST_COMPANION_PROFILE_APP_STREAMING

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_APP_STREAMING

Allows application to request to be associated with a virtual device capable of streaming Android applications (`[AssociationRequest.DEVICE_PROFILE_APP_STREAMING](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_APP_STREAMING)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`. 

Not for use by third-party applications.

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_APP_STREAMING" 

### REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION

Allows application to request to be associated with a vehicle head unit capable of automotive projection (`[AssociationRequest.DEVICE_PROFILE_AUTOMOTIVE_PROJECTION](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_AUTOMOTIVE_PROJECTION)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`. 

Not for use by third-party applications.

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_AUTOMOTIVE_PROJECTION" 

### REQUEST_COMPANION_PROFILE_COMPUTER

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_COMPUTER

Allows application to request to be associated with a computer to share functionality and/or data with other devices, such as notifications, photos and media (`[AssociationRequest.DEVICE_PROFILE_COMPUTER](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_COMPUTER)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`. 

Not for use by third-party applications.

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_COMPUTER" 

### REQUEST_COMPANION_PROFILE_GLASSES

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_GLASSES

Allows app to request to be associated with a device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)` as "glasses" 

Protection level: normal

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_GLASSES" 

### REQUEST_COMPANION_PROFILE_MEDICAL

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_MEDICAL

Allows application to request to associate with a `[AssociationRequest.DEVICE_PROFILE_MEDICAL](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_MEDICAL)` device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`.

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_MEDICAL" 

### REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING

Allows application to request to stream content from an Android host to a nearby device (`[AssociationRequest.DEVICE_PROFILE_NEARBY_DEVICE_STREAMING](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_NEARBY_DEVICE_STREAMING)`) by `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)`. 

Not for use by third-party applications.

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_NEARBY_DEVICE_STREAMING" 

### REQUEST_COMPANION_PROFILE_WATCH

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_PROFILE_WATCH

Allows app to request to be associated with a device via `[CompanionDeviceManager](https://developer.android.com/reference/android/companion/CompanionDeviceManager)` as a "watch" 

Protection level: normal

Constant Value: "android.permission.REQUEST_COMPANION_PROFILE_WATCH" 

### REQUEST_COMPANION_RUN_IN_BACKGROUND

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_RUN_IN_BACKGROUND

Allows a companion app to run in the background. This permission implies `[REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)`, and allows to start a foreground service from the background. If an app does not have to run in the background, but only needs to start a foreground service from the background, consider using `[REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND)`, which is less powerful. 

Protection level: normal

Constant Value: "android.permission.REQUEST_COMPANION_RUN_IN_BACKGROUND" 

### REQUEST_COMPANION_SELF_MANAGED

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_SELF_MANAGED

Allows an application to create a "self-managed" association.

Constant Value: "android.permission.REQUEST_COMPANION_SELF_MANAGED" 

### REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND

Allows a companion app to start a foreground service from the background. 

Protection level: normal

**See also:**

  * `[REQUEST_COMPANION_RUN_IN_BACKGROUND](https://developer.android.com/reference/android/Manifest.permission#REQUEST_COMPANION_RUN_IN_BACKGROUND)`



Constant Value: "android.permission.REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND" 

### REQUEST_COMPANION_USE_DATA_IN_BACKGROUND

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_COMPANION_USE_DATA_IN_BACKGROUND

Allows a companion app to use data in the background. 

Protection level: normal

Constant Value: "android.permission.REQUEST_COMPANION_USE_DATA_IN_BACKGROUND" 

### REQUEST_DELETE_PACKAGES

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_DELETE_PACKAGES

Allows an application to request deleting packages. Apps targeting APIs `[Build.VERSION_CODES.P](https://developer.android.com/reference/android/os/Build.VERSION_CODES#P)` or greater must hold this permission in order to use `[Intent.ACTION_UNINSTALL_PACKAGE](https://developer.android.com/reference/android/content/Intent#ACTION_UNINSTALL_PACKAGE)` or `[PackageInstaller.uninstall(VersionedPackage, IntentSender)](https://developer.android.com/reference/android/content/pm/PackageInstaller#uninstall\(android.content.pm.VersionedPackage,%20android.content.IntentSender\))`. 

Protection level: normal

Constant Value: "android.permission.REQUEST_DELETE_PACKAGES" 

### REQUEST_IGNORE_BATTERY_OPTIMIZATIONS

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_IGNORE_BATTERY_OPTIMIZATIONS

Permission an application must hold in order to use `[Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)`. 

Protection level: normal

Constant Value: "android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS" 

### REQUEST_INSTALL_PACKAGES

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_INSTALL_PACKAGES

Allows an application to request installing packages. Apps targeting APIs greater than 25 must hold this permission in order to use `[Intent.ACTION_INSTALL_PACKAGE](https://developer.android.com/reference/android/content/Intent#ACTION_INSTALL_PACKAGE)`. 

Protection level: signature

Constant Value: "android.permission.REQUEST_INSTALL_PACKAGES" 

### REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE

Allows an application to subscribe to notifications about the presence status change of their associated companion device

Constant Value: "android.permission.REQUEST_OBSERVE_COMPANION_DEVICE_PRESENCE" 

### REQUEST_OBSERVE_DEVICE_UUID_PRESENCE

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_OBSERVE_DEVICE_UUID_PRESENCE

Allows an application to subscribe to notifications about the nearby devices' presence status change base on the UUIDs. 

Not for use by third-party applications.

Constant Value: "android.permission.REQUEST_OBSERVE_DEVICE_UUID_PRESENCE" 

### REQUEST_PASSWORD_COMPLEXITY

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) REQUEST_PASSWORD_COMPLEXITY

Allows an application to request the screen lock complexity and prompt users to update the screen lock to a certain complexity level. 

Protection level: normal

Constant Value: "android.permission.REQUEST_PASSWORD_COMPLEXITY" 

### RESTART_PACKAGES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RESTART_PACKAGES

**This constant was deprecated in API level 15.**  
The `[ActivityManager.restartPackage(String)](https://developer.android.com/reference/android/app/ActivityManager#restartPackage\(java.lang.String\))` API is no longer supported. 

Constant Value: "android.permission.RESTART_PACKAGES" 

### RUN_USER_INITIATED_JOBS

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) RUN_USER_INITIATED_JOBS

Allows applications to use the user-initiated jobs API. For more details see `[JobInfo.Builder.setUserInitiated(boolean)](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setUserInitiated\(boolean\))`. 

Protection level: normal

Constant Value: "android.permission.RUN_USER_INITIATED_JOBS" 

### SCHEDULE_EXACT_ALARM

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SCHEDULE_EXACT_ALARM

Allows applications to use exact alarm APIs. 

This is a special access permission that can be revoked by the system or the user. It should only be used to enable **user-facing features** that require exact alarms. For more details, please go through the associated [developer docs](https://developer.android.com/training/scheduling/alarms#exact). 

Apps need to target API `[Build.VERSION_CODES.S](https://developer.android.com/reference/android/os/Build.VERSION_CODES#S)` or above to be able to request this permission. Note that apps targeting lower API levels do not need this permission to use exact alarm APIs. 

Apps that hold this permission and target API `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` and below always stay in the `[WORKING_SET](https://developer.android.com/reference/android/app/usage/UsageStatsManager#STANDBY_BUCKET_WORKING_SET)` or lower standby bucket. 

If your app relies on exact alarms for core functionality, it can instead request `[USE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#USE_EXACT_ALARM)` once it targets API `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)`. All apps using exact alarms for secondary features (which should still be user facing) should continue using this permission. 

Protection level: signature|privileged|appop

Constant Value: "android.permission.SCHEDULE_EXACT_ALARM" 

### SEND_RESPOND_VIA_MESSAGE

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SEND_RESPOND_VIA_MESSAGE

Allows an application (Phone) to send a request to other applications to handle the respond-via-message action during incoming calls. 

Not for use by third-party applications.

Constant Value: "android.permission.SEND_RESPOND_VIA_MESSAGE" 

### SEND_SMS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SEND_SMS

Allows an application to send SMS messages. 

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.SEND_SMS" 

### SET_ALARM

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_ALARM

Allows an application to broadcast an Intent to set an alarm for the user. 

Protection level: normal

Constant Value: "com.android.alarm.permission.SET_ALARM" 

### SET_ALWAYS_FINISH

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_ALWAYS_FINISH

Allows an application to control whether activities are immediately finished when put in the background. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_ALWAYS_FINISH" 

### SET_ANIMATION_SCALE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_ANIMATION_SCALE

Modify the global animation scaling factor. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_ANIMATION_SCALE" 

### SET_BIOMETRIC_DIALOG_ADVANCED

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_BIOMETRIC_DIALOG_ADVANCED

Allows an application to set the advanced features on BiometricDialog (SystemUI), including logo, logo description, and content view with more options button. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_BIOMETRIC_DIALOG_ADVANCED" 

### SET_DEBUG_APP

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_DEBUG_APP

Configure an application for debugging. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_DEBUG_APP" 

### SET_PREFERRED_APPLICATIONS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_PREFERRED_APPLICATIONS

**This constant was deprecated in API level 15.**  
No longer useful, see `[PackageManager.addPackageToPreferred(String)](https://developer.android.com/reference/android/content/pm/PackageManager#addPackageToPreferred\(java.lang.String\))` for details. 

Constant Value: "android.permission.SET_PREFERRED_APPLICATIONS" 

### SET_PROCESS_LIMIT

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_PROCESS_LIMIT

Allows an application to set the maximum number of (not needed) application processes that can be running. Allows an application to configure the memory limits and budgets of processes other than itself. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_PROCESS_LIMIT" 

### SET_TIME

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_TIME

Allows applications to set the system time directly. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_TIME" 

### SET_TIME_ZONE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_TIME_ZONE

Allows applications to set the system time zone directly. 

Not for use by third-party applications.

Constant Value: "android.permission.SET_TIME_ZONE" 

### SET_WALLPAPER

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_WALLPAPER

Allows applications to set the wallpaper. 

Protection level: normal

Constant Value: "android.permission.SET_WALLPAPER" 

### SET_WALLPAPER_HINTS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SET_WALLPAPER_HINTS

Allows applications to set the wallpaper hints. 

Protection level: normal

Constant Value: "android.permission.SET_WALLPAPER_HINTS" 

### SHOW_POWER_MENU

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SHOW_POWER_MENU

Permission needed to request to show the Power Menu. 

Granted to the current holder of the ASSISTANT role.

Constant Value: "android.permission.SHOW_POWER_MENU" 

### SHOW_POWER_MENU_PRIVILEGED

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SHOW_POWER_MENU_PRIVILEGED

Permission needed to request to show the Power Menu. 

Granted to certain privileged apps.

Constant Value: "android.permission.SHOW_POWER_MENU_PRIVILEGED" 

### SIGNAL_PERSISTENT_PROCESSES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SIGNAL_PERSISTENT_PROCESSES

Allow an application to request that a signal be sent to all persistent processes. 

Not for use by third-party applications.

Constant Value: "android.permission.SIGNAL_PERSISTENT_PROCESSES" 

### SMS_FINANCIAL_TRANSACTIONS

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SMS_FINANCIAL_TRANSACTIONS

**This constant was deprecated in API level 31.**  
The API that used this permission is no longer functional. 

Allows financial apps to read filtered sms messages. Protection level: signature|appop

Constant Value: "android.permission.SMS_FINANCIAL_TRANSACTIONS" 

### START_FOREGROUND_SERVICES_FROM_BACKGROUND

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) START_FOREGROUND_SERVICES_FROM_BACKGROUND

Allows an application to start foreground services from the background at any time. _This permission is not for use by third-party applications_ , with the only exception being if the app is the default SMS app. Otherwise, it's only usable by privileged apps, app verifier app, and apps with any of the EMERGENCY or SYSTEM GALLERY roles.

Constant Value: "android.permission.START_FOREGROUND_SERVICES_FROM_BACKGROUND" 

### START_VIEW_APP_FEATURES

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) START_VIEW_APP_FEATURES

Allows the holder to start the screen with a list of app features. 

Protection level: signature|installer

Constant Value: "android.permission.START_VIEW_APP_FEATURES" 

### START_VIEW_PERMISSION_USAGE

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) START_VIEW_PERMISSION_USAGE

Allows the holder to start the permission usage screen for an app. 

Protection level: signature|installer

Constant Value: "android.permission.START_VIEW_PERMISSION_USAGE" 

### STATUS_BAR

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) STATUS_BAR

Allows an application to open, close, or disable the status bar and its icons. 

Not for use by third-party applications.

Constant Value: "android.permission.STATUS_BAR" 

### SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE

Allows an application to subscribe to device locked and keyguard locked (i.e., showing) state. 

Protection level: signature|privileged|module|role 

Intended for use by ROLE_ASSISTANT, VDM, and signature / privileged apps only.

Constant Value: "android.permission.SUBSCRIBE_TO_KEYGUARD_LOCKED_STATE" 

### SYSTEM_ALERT_WINDOW

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) SYSTEM_ALERT_WINDOW

Allows an app to create windows using the type `[WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY)`, shown on top of all other apps. Very few apps should use this permission; these windows are intended for system-level interaction with the user. 

**Note:** If the app targets API level 23 or higher, the app user must explicitly grant this permission to the app through a permission management screen. The app requests the user's approval by sending an intent with action `[Settings.ACTION_MANAGE_OVERLAY_PERMISSION](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_OVERLAY_PERMISSION)`. The app can check whether it has this authorization by calling `[Settings.canDrawOverlays()](https://developer.android.com/reference/android/provider/Settings#canDrawOverlays\(android.content.Context\))`. 

Protection level: signature|setup|appop|installer|pre23|development

Constant Value: "android.permission.SYSTEM_ALERT_WINDOW" 

### TRANSMIT_IR

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) TRANSMIT_IR

Allows using the device's IR transmitter, if available. 

Protection level: normal

Constant Value: "android.permission.TRANSMIT_IR" 

### TURN_SCREEN_ON

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) TURN_SCREEN_ON

Allows an app to turn on the screen on, e.g. with `[PowerManager.ACQUIRE_CAUSES_WAKEUP](https://developer.android.com/reference/android/os/PowerManager#ACQUIRE_CAUSES_WAKEUP)`. 

Intended to only be used by home automation apps.

Constant Value: "android.permission.TURN_SCREEN_ON" 

### TV_IMPLICIT_ENTER_PIP

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) TV_IMPLICIT_ENTER_PIP

Allows an app to enter Picture-in-Picture mode when the user is not explicitly requesting it. This includes using `[ERROR(/PictureInPictureParams.Builder#setAutoEnterEnabled)](https://developer.android.com/)` as well as lifecycle methods such as `[ERROR(/Activity#onUserLeaveHint)](https://developer.android.com/)` and `[ERROR(/Activity#onPause)](https://developer.android.com/)` to enter PiP when the user leaves the app. This permission should only be used for certain PiP [usage types](https://developer.android.com/training/tv/get-started/multitasking#usage-types).

Constant Value: "android.permission.TV_IMPLICIT_ENTER_PIP" 

### UNINSTALL_SHORTCUT

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) UNINSTALL_SHORTCUT

**Don't use this permission in your app.**  
This permission is no longer supported.

Constant Value: "com.android.launcher.permission.UNINSTALL_SHORTCUT" 

### UPDATE_DEVICE_STATS

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) UPDATE_DEVICE_STATS

Allows an application to update device statistics. 

Not for use by third-party applications.

Constant Value: "android.permission.UPDATE_DEVICE_STATS" 

### UPDATE_PACKAGES_WITHOUT_USER_ACTION

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) UPDATE_PACKAGES_WITHOUT_USER_ACTION

Allows an application to indicate via `[PackageInstaller.SessionParams.setRequireUserAction(int)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setRequireUserAction\(int\))` that user action should not be required for an app update. 

Protection level: normal

Constant Value: "android.permission.UPDATE_PACKAGES_WITHOUT_USER_ACTION" 

### USE_BIOMETRIC

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_BIOMETRIC

Allows an app to use device supported biometric modalities. 

Protection level: normal

Constant Value: "android.permission.USE_BIOMETRIC" 

### USE_EXACT_ALARM

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_EXACT_ALARM

Allows apps to use exact alarms just like with `[SCHEDULE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM)` but without needing to request this permission from the user. 

**This is only intended for use by apps that rely on exact alarms for their core functionality.** You should continue using `SCHEDULE_EXACT_ALARM` if your app needs exact alarms for a secondary feature that users may or may not use within your app. 

Keep in mind that this is a powerful permission and app stores may enforce policies to audit and review the use of this permission. Such audits may involve removal from the app store if the app is found to be misusing this permission. 

Apps need to target API `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/android/os/Build.VERSION_CODES#TIRAMISU)` or above to be able to request this permission. Note that only one of `USE_EXACT_ALARM` or `SCHEDULE_EXACT_ALARM` should be requested on a device. If your app is already using `SCHEDULE_EXACT_ALARM` on older SDKs but needs `USE_EXACT_ALARM` on SDK 33 and above, then `SCHEDULE_EXACT_ALARM` should be declared with a max-sdk attribute, like: 
    
    
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM"
    	 android:maxSdkVersion="32" />
    

Apps that hold this permission, always stay in the `[WORKING_SET](https://developer.android.com/reference/android/app/usage/UsageStatsManager#STANDBY_BUCKET_WORKING_SET)` or lower standby bucket.

Constant Value: "android.permission.USE_EXACT_ALARM" 

### USE_FINGERPRINT

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)   
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_FINGERPRINT

**This constant was deprecated in API level 28.**  
Applications should request `[USE_BIOMETRIC](https://developer.android.com/reference/android/Manifest.permission#USE_BIOMETRIC)` instead 

Allows an app to use fingerprint hardware. 

Protection level: normal

Constant Value: "android.permission.USE_FINGERPRINT" 

### USE_FULL_SCREEN_INTENT

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_FULL_SCREEN_INTENT

Required for apps targeting `[Build.VERSION_CODES.Q](https://developer.android.com/reference/android/os/Build.VERSION_CODES#Q)` that want to use `[notification full screen intents](https://developer.android.com/reference/android/app/Notification.Builder#setFullScreenIntent\(android.app.PendingIntent,%20boolean\))`. 

Protection level: normal

Constant Value: "android.permission.USE_FULL_SCREEN_INTENT" 

### USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER

Allows to read device identifiers and use ICC based authentication like EAP-AKA. Often required in authentication to access the carrier's server and manage services of the subscriber. 

Protection level: signature|appop

Constant Value: "android.permission.USE_ICC_AUTH_WITH_DEVICE_IDENTIFIER" 

### USE_LOCATION_BUTTON

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_LOCATION_BUTTON

Allows an app use location button, which grants temporary location permission when a user clicks the button. 

Protection level: normal

Constant Value: "android.permission.USE_LOCATION_BUTTON" 

### USE_PINNED_WINDOWING_LAYER

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_PINNED_WINDOWING_LAYER

Allows an application to use `[ActivityManager.AppTask.WINDOWING_LAYER_PINNED](https://developer.android.com/reference/android/app/ActivityManager.AppTask#WINDOWING_LAYER_PINNED)` for its Tasks, typically requested via `[ActivityManager.AppTask.requestWindowingLayer(int, Executor, OutcomeReceiver)](https://developer.android.com/reference/android/app/ActivityManager.AppTask#requestWindowingLayer\(int,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver<java.lang.Integer,java.lang.Exception>\))`. 

Granting this permission allows an app to request its task be placed above normal application windows. 

To ensure system integrity and a consistent user experience, the system imposes several restrictions on tasks using this layer. These may include, but are not limited to: 

  * Forcing the task to be completely opaque and display system decorations.
  * Strictly limiting the number of tasks in this layer (e.g., only one at a time).
  * Limiting the application's control over the task's initial size and position.
  * Making the task non-movable programmatically (including restrictions on workarounds like resizing).
  * Providing users with immediate settings access to disable the feature.



See the API documentation for `[ActivityManager.AppTask.requestWindowingLayer(int, Executor, OutcomeReceiver)](https://developer.android.com/reference/android/app/ActivityManager.AppTask#requestWindowingLayer\(int,%20java.util.concurrent.Executor,%20android.os.OutcomeReceiver<java.lang.Integer,java.lang.Exception>\))` for the full documentation. 

Protection level: normal

Constant Value: "android.permission.USE_PINNED_WINDOWING_LAYER" 

### USE_SIP

Added in [API level 9](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) USE_SIP

Allows an application to use SIP service. 

Protection level: dangerous

Constant Value: "android.permission.USE_SIP" 

### UWB_RANGING

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) UWB_RANGING

Required to be able to range to devices using ultra-wideband. 

Protection level: dangerous

Constant Value: "android.permission.UWB_RANGING" 

### VIBRATE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) VIBRATE

Allows access to the vibrator. 

Protection level: normal

Constant Value: "android.permission.VIBRATE" 

### WAKE_LOCK

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WAKE_LOCK

Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. 

Protection level: normal

Constant Value: "android.permission.WAKE_LOCK" 

### WRITE_APN_SETTINGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_APN_SETTINGS

Allows applications to write the apn settings and read sensitive fields of an existing apn settings like user and password. 

Not for use by third-party applications.

Constant Value: "android.permission.WRITE_APN_SETTINGS" 

### WRITE_CALENDAR

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_CALENDAR

Allows an application to write the user's calendar data. 

Protection level: dangerous

Constant Value: "android.permission.WRITE_CALENDAR" 

### WRITE_CALL_LOG

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_CALL_LOG

Allows an application to write and read the user's call log data. 

**Note:** If your app uses the `[WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS)` permission and _both_ your [`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min) and [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) values are set to 15 or lower, the system implicitly grants your app this permission. If you don't need this permission, be sure your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) is 16 or higher.

Protection level: dangerous 

This is a hard restricted permission which cannot be held by an app until the installer on record allowlists the permission. For more details see `[PackageInstaller.SessionParams.setWhitelistedRestrictedPermissions(Set)](https://developer.android.com/reference/android/content/pm/PackageInstaller.SessionParams#setWhitelistedRestrictedPermissions\(java.util.Set<java.lang.String>\))`.

Constant Value: "android.permission.WRITE_CALL_LOG" 

### WRITE_CONTACTS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_CONTACTS

Allows an application to write the user's contacts data. 

Protection level: dangerous

Constant Value: "android.permission.WRITE_CONTACTS" 

### WRITE_EXTERNAL_STORAGE

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_EXTERNAL_STORAGE

Allows an application to write to external storage. 

**Note:** If your app targets `[Build.VERSION_CODES.R](https://developer.android.com/reference/android/os/Build.VERSION_CODES#R)` or higher, this permission has no effect. 

If your app is on a device that runs API level 19 or higher, you don't need to declare this permission to read and write files in your application-specific directories returned by `[Context.getExternalFilesDir(String)](https://developer.android.com/reference/android/content/Context#getExternalFilesDir\(java.lang.String\))` and `[Context.getExternalCacheDir()](https://developer.android.com/reference/android/content/Context#getExternalCacheDir\(\))`. 

Learn more about how to [modify media files](https://developer.android.com/training/data-storage/shared/media#update-other-apps-files) that your app doesn't own, and how to [modify non-media files](https://developer.android.com/training/data-storage/shared/documents-files) that your app doesn't own. 

If your app is a file manager and needs broad access to external storage files, then the system must place your app on an allowlist so that you can successfully request the MANAGE_EXTERNAL_STORAGE permission. Learn more about the appropriate use cases for [`minSdkVersion`](https://developer.android.com/training/data-storage/manage-all-files>managing%20all%20files%20on%20a%20storage%0Adevice</a>.%0A<p>If%20<em>both</em>%20your%20<a%20href=) and [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) values are set to 3 or lower, the system implicitly grants your app this permission. If you don't need this permission, be sure your [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target) is 4 or higher. 

Protection level: dangerous

Constant Value: "android.permission.WRITE_EXTERNAL_STORAGE" 

### WRITE_GSERVICES

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_GSERVICES

Allows an application to modify the Google service map. 

Not for use by third-party applications.

Constant Value: "android.permission.WRITE_GSERVICES" 

### WRITE_SECURE_SETTINGS

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_SECURE_SETTINGS

Allows an application to read or write the secure system settings. 

Not for use by third-party applications.

Constant Value: "android.permission.WRITE_SECURE_SETTINGS" 

### WRITE_SETTINGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_SETTINGS

Allows an application to read or write the system settings. 

**Note:** If the app targets API level 23 or higher, the app user must explicitly grant this permission to the app through a permission management screen. The app requests the user's approval by sending an intent with action `[Settings.ACTION_MANAGE_WRITE_SETTINGS](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_WRITE_SETTINGS)`. The app can check whether it has this authorization by calling `[Settings.System.canWrite()](https://developer.android.com/reference/android/provider/Settings.System#canWrite\(android.content.Context\))`. 

Protection level: signature|preinstalled|appop|pre23

Constant Value: "android.permission.WRITE_SETTINGS" 

### WRITE_SYNC_SETTINGS

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_SYNC_SETTINGS

Allows applications to write the sync settings. 

Protection level: normal

Constant Value: "android.permission.WRITE_SYNC_SETTINGS" 

### WRITE_SYSTEM_PREFERENCES

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_SYSTEM_PREFERENCES

Allows an application to access the Settings Preference services to write settings values exposed by the system Settings app and system apps that contribute settings surfaced in the Settings app. 

This allows the calling application to write settings values through the host application, agnostic of underlying storage. 

Protection Level: signature|privileged|appop

Constant Value: "android.permission.WRITE_SYSTEM_PREFERENCES" 

### WRITE_VOICEMAIL

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)
    
    
    public static final [String](https://developer.android.com/reference/java/lang/String) WRITE_VOICEMAIL

Allows an application to modify and remove existing voicemails in the system. 

Protection level: signature|privileged|role

Constant Value: "com.android.voicemail.permission.WRITE_VOICEMAIL" 

## Public constructors

### permission
    
    
    public permission ()

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
