---
url: https://developer.android.com/develop/ui/compose/sharing/send/
title: Send data to other apps \u00a0|\u00a0 Jetpack Compose \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:15.501557+00:00
---

# Send data to other apps  |  Jetpack Compose  |  Android Developers

> Source: https://developer.android.com/develop/ui/compose/sharing/send/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Docs ](https://developer.android.com/develop/ui/compose/documentation)



#  Send data to other apps Stay organized with collections  Save and categorize content based on your preferences. 

Android provides two ways for users to share data between apps:

  * The Android Sharesheet is primarily designed for sending content outside your app or directly to another user. For example, sharing a URL with a friend. 
  * The Android intent resolver is best suited for passing data to the next stage of a well-defined task. For example, opening a PDF from your app and letting users pick their preferred viewer.



## Why use the Android Sharesheet

![](https://developer.android.com/static/images/training/sharing/sharesheet.png)**Figure 1.** The Android Sharesheet.

Use the Android Sharesheet to create consistency for your users across apps. Don't display your app's own list of share targets or create your own Sharesheet variations.

The Android Sharesheet lets users share information with the right person, with relevant app suggestions, all with a single tap. The Sharesheet can suggest targets unavailable to custom solutions and uses a consistent ranking. This is because the Sharesheet can take into account information about app and user activity that is only available to the system.

The Android Sharesheet also has many handy features for developers. For example, you can do the following:

  * Find out when your users complete a share and to where
  * Add custom targets and app targets
  * Provide rich text content previews, starting in Android 10 (API level 29)
  * Exclude targets matching specific component names



## Use the Android Sharesheet

For all types of sharing, create an intent and set its action to `[Intent.ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)`. To display the Android Sharesheet, call `[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser\(android.content.Intent,%20java.lang.CharSequence\))`, passing it your `[Intent](https://developer.android.com/reference/android/content/Intent)` object. It returns a version of your intent that always displays the Android Sharesheet.

### Send text content

The most straightforward and common use of the Android Sharesheet is to send text content from one activity to another. For example, most browsers can share the URL of the currently displayed page as text with another app. This is useful for sharing an article or website with friends through email or social networking. In Jetpack Compose, retrieve the current context using `LocalContext.current` and call `context.startActivity()`. Here's an example of how to do this:
    
    
    fun shareText(context: Context) {
        val sendIntent: Intent = Intent().apply {
            action = ACTION_SEND
            putExtra(Intent.EXTRA_TEXT, "This is my text to send.")
            type = "text/plain"
        }
    
        val shareIntent = Intent.createChooser(sendIntent, null)
        context.startActivity(shareIntent)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L127-L136)

Optionally, you can add extras to include more information, such as email recipients (`[EXTRA_EMAIL](https://developer.android.com/reference/android/content/Intent#EXTRA_EMAIL)`, `[EXTRA_CC](https://developer.android.com/reference/android/content/Intent#EXTRA_CC)`, `[EXTRA_BCC](https://developer.android.com/reference/android/content/Intent#EXTRA_BCC)`), or the email subject (`[EXTRA_SUBJECT](https://developer.android.com/reference/android/content/Intent#EXTRA_SUBJECT)`). 

**Note:** Some email apps, such as Gmail, expect a `[String[]](https://developer.android.com/reference/java/lang/String)` for extras like `EXTRA_EMAIL` and `EXTRA_CC`. Use `[putExtra(String, String[])](https://developer.android.com/reference/android/content/Intent#putExtra\(java.lang.String,%20java.lang.String\[\]\))` to add these to your intent.

### Send binary content

Share binary data using the `[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)` action. Set the appropriate MIME type and place a URI to the data in the extra `[EXTRA_STREAM](https://developer.android.com/reference/android/content/Intent#EXTRA_STREAM)`, as shown in the following example. This is commonly used to share an image but can be used to share any type of binary content.

**Note:** If your goal is to let users select or import photos or videos from their media library into your app, use the [Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker) instead of `ACTION_SEND`. 
    
    
    fun shareBinaryContent(context: Context) {
        val shareIntent: Intent = Intent().apply {
            action = ACTION_SEND
            // Example: content://com.google.android.apps.photos.contentprovider/...
            val imageUri: Uri =
                Uri.parse("content://com.google.android.apps.photos.contentprovider/0/1/mediakey/1")
            putExtra(Intent.EXTRA_STREAM, imageUri)
            type = "image/jpeg"
        }
        context.startActivity(Intent.createChooser(shareIntent, null))
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L140-L150)

The receiving application needs permission to access the data the `[Uri](https://developer.android.com/reference/android/net/Uri)` points to. There are two recommended ways to do this:

  * Store the data in your own `[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)`, making sure that other apps have the correct permission to access your provider. The preferred mechanism for providing access is to use [per-URI permissions](https://developer.android.com/training/permissions/restrict-interactions#uri), which are temporary and only grant access to the receiving application. To create a `ContentProvider` like this, use the `[FileProvider](https://developer.android.com/reference/androidx/core/content/FileProvider)` helper class.
  * Use the system `[MediaStore](https://developer.android.com/reference/android/provider/MediaStore)`. The `MediaStore` is primarily for video, audio, and image MIME types. However, beginning with Android 3.0 (API level 11), it can also store non-media types. For more information, see `[MediaStore.Files](https://developer.android.com/reference/android/provider/MediaStore.Files)`. Files can be inserted into the `MediaStore` using `[scanFile()](https://developer.android.com/reference/android/media/MediaScannerConnection#scanFile\(android.content.Context,%20java.lang.String\[\],%20java.lang.String\[\],%20android.media.MediaScannerConnection.OnScanCompletedListener\))`, after which a `content://`-style `[Uri](https://developer.android.com/reference/android/net/Uri)` suitable for sharing is passed to the provided `[onScanCompleted()](https://developer.android.com/reference/android/media/MediaScannerConnection.OnScanCompletedListener#onScanCompleted\(java.lang.String,%20android.net.Uri\))` callback. Note that once added to the system `MediaStore`, the content is accessible to any app on the device.



### Use the right MIME type

Provide the most specific MIME type available for the data you're sending. For example, use `text/plain` when sharing plain text. Here are a few common MIME types when sending data in Android:

Receivers register for | Senders send  
---|---  
`text/*` | 

  * `text/plain`
  * `text/rtf`
  * `text/html`
  * `text/json`

  
`image/*` | 

  * `image/jpg`
  * `image/png`
  * `image/gif`

  
`video/*` | 

  * `video/mp4`
  * `video/3gp`

  
Supported file extensions | `application/pdf`  
**Caution:** Although you can use a MIME type of `*/*`, avoid doing so because most receiving apps aren't able to receive any kind of content. Ideally, your app must match activities that can handle generic data streams. 

To determine the MIME type dynamically at runtime instead of hardcoding it, use the following methods:

  * For `content://` URIs (such as those provided by `FileProvider` or `MediaStore`), call `[ContentResolver.getType()](https://developer.android.com/reference/android/content/ContentResolver#getType\(android.net.Uri\))`.
  * For file extensions, call `[MimeTypeMap.getSingleton().getMimeTypeFromExtension()](https://developer.android.com/reference/android/webkit/MimeTypeMap#getMimeTypeFromExtension\(java.lang.String\))`.
  * If you use the Storage Access Framework, you can also query `[DocumentFile.getType()](https://developer.android.com/reference/androidx/documentfile/provider/DocumentFile#getType\(\))`.



If you can't determine a specific MIME type, use `application/octet-stream` for generic binary data, or `*/*` as a last resort.

For more information about MIME types, see the [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml) official registry of MIME media types.

The Android Sharesheet might show a content preview, depending on the provided MIME type. Some preview features are only available for specific types.

### Share multiple pieces of content

To share multiple pieces of content, use the `[ACTION_SEND_MULTIPLE](https://developer.android.com/reference/android/content/Intent#ACTION_SEND_MULTIPLE)` action together with a list of URIs pointing to the content. The MIME type varies according to the mix of content you're sharing. For example, if you share three JPEG images, you use the type `"image/jpg"`. For a mixture of image types, use `"image/*"` to match an activity that handles any type of image. While it's possible to share a mix of types, avoid doing this, because it's unclear to the receiver what is intended to be sent. If it's necessary to send multiple types, use `"*/*"`. It's up to the receiving application to parse and process your data. Here's an example:
    
    
    fun shareMultiple(context: Context) {
        val imageUris: ArrayList<Uri> = arrayListOf(
            Uri.parse("content://com.google.android.apps.photos.contentprovider/0/1/mediakey/1"),
            Uri.parse("content://com.google.android.apps.photos.contentprovider/0/1/mediakey/2")
        )
    
        val shareIntent = Intent().apply {
            action = Intent.ACTION_SEND_MULTIPLE
            putParcelableArrayListExtra(Intent.EXTRA_STREAM, imageUris)
            type = "image/*"
        }
        context.startActivity(Intent.createChooser(shareIntent, null))
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L154-L166)

Be sure the provided `[Uri](https://developer.android.com/reference/android/net/Uri)` objects point to data that a receiving application can access.

### Add rich content to text previews

Starting in Android 10 (API level 29), the Android Sharesheet shows a preview of text being shared. In some cases, text that's being shared can be hard to understand. Consider sharing a complicated URL like `https://www.google.com/search?ei=2rRVXcLkJajM0PEPoLy7oA4`. A richer preview can reassure your users what is being shared.

If you're previewing text, you can set a title, a thumbnail image, or both. Add a description to `Intent.EXTRA_TITLE` before calling `Intent.createChooser()`, and add a relevant thumbnail using `ClipData`.

**Note:** The image content URI is provided from a `FileProvider`, usually from a configured `<cache-path>`. For more information, see [Sharing files](https://developer.android.com/training/secure-file-sharing). Be sure to give Sharesheet the right permissions to read any image you want to use as a thumbnail. For more information, see `[Intent.FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION)`.

Here's an example:
    
    
    fun richContentToTextPreviewShares(context: Context) {
        val share = Intent.createChooser(
            Intent().apply {
                action = ACTION_SEND
                putExtra(Intent.EXTRA_TEXT, "https://developer.android.com/training/sharing/")
    
                // (Optional) Here you're setting the title of the content
                putExtra(Intent.EXTRA_TITLE, "Introducing content previews")
    
                // (Optional) Here you're passing a content URI to an image to be displayed
                data =
                    Uri.parse("content://com.google.android.apps.photos.contentprovider/0/1/mediakey/A123456789")
                flags = Intent.FLAG_GRANT_READ_URI_PERMISSION
            },
            null
        )
        context.startActivity(share)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L170-L187)

The preview looks something like this:

![](https://developer.android.com/static/images/training/sharing/sharing_content_preview.png)**Figure 2.** Text content preview on the Android Sharesheet.

### Add custom actions to the sharesheet

![](https://developer.android.com/static/images/training/sharing/sharesheet_custom_actions.png)**Figure 3.** Custom actions on the Android Sharesheet.

On Android 14 (API level 34) and higher, apps can add custom actions to the Android Sharesheet. The custom actions are shown as small action icons at the top of the Android Sharesheet, and apps can specify any `Intent` as the action invoked when the icon is clicked.

To add custom actions on the Android Sharesheet, first create a `[ChooserAction](https://developer.android.com/reference/android/service/chooser/ChooserAction)` with `[ChooserAction.Builder](https://developer.android.com/reference/android/service/chooser/ChooserAction.Builder)`. You can specify a `PendingIntent` as the action invoked when the icon is clicked. Create an array containing all of your custom actions and specify it as `[EXTRA_CHOOSER_CUSTOM_ACTIONS](https://developer.android.com/reference/android/content/Intent#EXTRA_CHOOSER_CUSTOM_ACTIONS)` of the share `Intent`.
    
    
    fun sharesheetCustomActions(context: Context, previewText: String) {
        val sendIntent = Intent(ACTION_SEND)
            .setType("text/plain")
            .putExtra(Intent.EXTRA_TEXT, previewText)
        val shareIntent = Intent.createChooser(sendIntent, null)
        val customActions = arrayOf(
            ChooserAction.Builder(
                Icon.createWithResource(context, R.drawable.ic_logo),
                "Custom",
                PendingIntent.getBroadcast(
                    context,
                    1,
                    Intent(Intent.ACTION_VIEW),
                    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_CANCEL_CURRENT
                )
            ).build()
        )
        shareIntent.putExtra(Intent.EXTRA_CHOOSER_CUSTOM_ACTIONS, customActions)
        context.startActivity(shareIntent)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L191-L210)

### Add custom targets

**Deprecated:** `[ChooserTarget](https://developer.android.com/reference/android/service/chooser/ChooserTarget)` and `[ChooserTargetService](https://developer.android.com/reference/android/service/chooser/ChooserTargetService)` are deprecated starting in Android 11 (API level 30). For Direct Share targets, use `[ShortcutManagerCompat](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat)` (or `[ShortcutManager](https://developer.android.com/reference/android/content/pm/ShortcutManager)`) with the Sharing Shortcuts API instead. For more information, see [Provide Direct Share targets](https://developer.android.com/develop/ui/compose/sharing/direct-share-targets). To provide custom actions on Android 14 (API level 34) and higher, use custom actions instead. 

The Android Sharesheet lets you specify up to two custom activity intents that are listed before the app suggestions using `[Intent.EXTRA_INITIAL_INTENTS](https://developer.android.com/reference/android/content/Intent#EXTRA_INITIAL_INTENTS)`. For Direct Share targets (such as conversations or contacts), publish dynamic shortcuts using `[ShortcutManagerCompat](https://developer.android.com/reference/androidx/core/content/pm/ShortcutManagerCompat)` instead (see [Provide Direct Share targets](https://developer.android.com/develop/ui/compose/sharing/direct-share-targets)):

![](https://developer.android.com/static/images/training/sharing/customshare.png)**Figure 4.** Custom targets on the Android Sharesheet.

Add `Intent.EXTRA_INITIAL_INTENTS` to your share Intent _after_ calling `[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser\(android.content.Intent,%20java.lang.CharSequence\))`:
    
    
    val sendIntent = Intent(ACTION_SEND).apply {
        type = "text/plain"
        putExtra(Intent.EXTRA_TEXT, previewText)
    }
    
    val customIntent = Intent().apply {
        component = ComponentName(context.packageName, "${context.packageName}.CustomActivity")
    }
    
    val shareIntent = Intent.createChooser(sendIntent, null).apply {
        putExtra(
            Intent.EXTRA_INITIAL_INTENTS,
            arrayOf(customIntent)
        )
    }
    context.startActivity(shareIntent)
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L215-L230)

Use this feature with care. Every custom `Intent` that you add reduces the number the system suggests. In general, avoid adding custom targets. A common appropriate example of adding `Intent.EXTRA_INITIAL_INTENTS` is to provide additional actions users can take on shared content. For example, a user shares images and `Intent.EXTRA_INITIAL_INTENTS` is used to let them send a link instead.

### Exclude specific targets by component

You can exclude specific targets by providing `Intent.EXTRA_EXCLUDE_COMPONENTS`. Only do this to remove targets you have control over. A common use case is to hide your app's share targets when your users share from within your app, as their intent is likely to share outside your app.

Add `Intent.EXTRA_EXCLUDE_COMPONENTS` to your intent after calling `Intent.createChooser()`:
    
    
    fun excludeSpecificTargets(context: Context) {
        val share = Intent.createChooser(Intent(ACTION_SEND), null).apply {
            // Only use for components you have control over
            val excludedComponentNames =
                arrayOf(ComponentName("com.example.android", "ExampleClass"))
            putExtra(Intent.EXTRA_EXCLUDE_COMPONENTS, excludedComponentNames)
        }
        context.startActivity(share)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L235-L243)

### Get information about sharing

It can be useful to know when your users are sharing and what target they select. The Android Sharesheet lets you get this information by providing the `ComponentName` of targets your users select using an `IntentSender`.

First create a `PendingIntent` for a `BroadcastReceiver` and supply its `IntentSender` in `Intent.createChooser()`:
    
    
    fun infoAboutSharing(context: Context, requestCode: Int) {
        var share = Intent(ACTION_SEND)
        // ...
        val pi = PendingIntent.getBroadcast(
            context, requestCode,
            Intent(context, ShareBroadcastReceiver::class.java),
            PendingIntent.FLAG_MUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )
        share = Intent.createChooser(share, null, pi.intentSender)
        context.startActivity(share)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L247-L257)

Receive the callback in `MyBroadcastReceiver` and look in `Intent.EXTRA_CHOOSER_RESULT`:
    
    
    override fun onReceive(context: Context?, intent: Intent) {
        val TAG = ShareBroadcastReceiver::class.simpleName
        val chooserResult: ChooserResult? = IntentCompat.getParcelableExtra(
            intent,
            Intent.EXTRA_CHOOSER_RESULT,
            ChooserResult::class.java,
        )
        chooserResult?.let {
            Log.i(TAG,
                "Share callback: isShortcut: ${it.isShortcut}, type: ${typeToString(it.type)}, componentName: ${it.selectedComponent}",
            )
        } ?: Log.i(TAG, "chooserResult is null")
    }
    
    [ShareBroadcastReceiver.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/ShareBroadcastReceiver.kt#L28-L40)

For more information, see the [platform share sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/share).

## Use the Android intent resolver

![](https://developer.android.com/static/images/training/sharing/send_intent.png)**Figure 5.** The `[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)` intent resolver.

The Android intent resolver is best used when sending data to another app as part of a well-defined task flow.

To use the Android intent resolver, create an intent and add extras as you would to call the Android Sharesheet. However, _don't_ call `[Intent.createChooser()](https://developer.android.com/reference/android/content/Intent#createChooser\(android.content.Intent,%20java.lang.CharSequence\))`.

If there are multiple installed applications with filters that match `[ACTION_SEND](https://developer.android.com/reference/android/content/Intent#ACTION_SEND)` and the MIME type, the system displays a disambiguation dialog called the _intent resolver_ that lets the user choose a target to share to. If a single application matches, it runs.

Here's an example of how to use the Android intent resolver to send text:
    
    
    fun intentResolver(context: Context) {
        val sendIntent: Intent = Intent().apply {
            action = ACTION_SEND
            putExtra(Intent.EXTRA_TEXT, "This is my text to send.")
            type = "text/plain"
        }
        context.startActivity(sendIntent)
    }
    
    [SharesheetSnippets.kt](https://github.com/android/snippets/blob/5e7c52581fa2ef5bfeea42d80c178c9996464615/compose/snippets/src/main/java/com/example/compose/snippets/sharesheet/SharesheetSnippets.kt#L284-L291)

## Learn more

For more information about sending data, see [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters).

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
