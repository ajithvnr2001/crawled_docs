---
url: https://developer.android.com/codelabs/exoplayer-intro/
title: Media streaming with ExoPlayer \u00a0|\u00a0 Android media \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:35:12.499061+00:00
---

# Media streaming with ExoPlayer  |  Android media  |  Android Developers

> Source: https://developer.android.com/codelabs/exoplayer-intro/

  * [ Android Developers ](https://developer.android.com/)
  * [ Essentials ](https://developer.android.com/get-started)
  * [ Camera & media dev center ](https://developer.android.com/media)
  * [ Guides ](https://developer.android.com/media/guides)



#  Media streaming with ExoPlayer Stay organized with collections  Save and categorize content based on your preferences. 

##  1\. Before you begin 

**Note:** This codelab has been updated to use Jetpack Media3, the new home for ExoPlayer. Learn more about Media3 and ExoPlayer in our blog post, [Media3 is ready to play!](https://android-developers.googleblog.com/2023/03/media3-is-ready-to-play.html)

![5b481fba585c2691.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/5b481fba585c2691.png)

Screenshot: The YouTube Android app, which uses ExoPlayer as its video player.

[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer) is an app-level media player built on top of low-level media APIs in Android. It is an [open source project](https://github.com/androidx/media) used by Google apps, including YouTube and Google TV. ExoPlayer is highly customizable and extensible, making it capable of many advanced use cases. It [supports a variety of media formats](https://developer.android.com/guide/topics/media/exoplayer/supported-formats), including adaptive formats such as DASH and SmoothStreaming.

## Prerequisites

  * Moderate knowledge of Android development and Android Studio



## What you'll do

  * Create an [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) instance, which prepares and plays media from a variety of sources.
  * Integrate ExoPlayer with the app's activity lifecycle to support backgrounding, foregrounding, and playback resumption in a single or multi-window environment.
  * Use [`MediaItem`](https://developer.android.com/reference/androidx/media3/common/MediaItem) instances to create a playlist.
  * Play adaptive video streams, which adapt the media quality to the available bandwidth.
  * Register event listeners to monitor playback state and show how listeners can be used to measure the quality of playback.
  * Use standard ExoPlayer UI components, then customize them to your app's style.



## What you'll need

  * The latest stable version of [Android Studio](https://developer.android.com/studio/index.html), and knowledge of how to use it. Make sure your Android Studio, Android SDK, and Gradle plugin are up to date.
  * An Android device with JellyBean (4.1) or higher, ideally with Nougat (7.1) or higher as it supports multiple windows.



**Note:** This codelab is focused on ExoPlayer. Non-relevant concepts and code blocks are glossed over and are provided for you to simply copy and paste.

##  2\. Get set up 

## Get the code

To get started, download the Android Studio project:

[file_downloadDownload zip](https://github.com/android/codelab-exoplayer-intro/archive/main.zip)

Alternatively, you can clone the GitHub repository:
    
    
    git clone https://github.com/android/codelab-exoplayer-intro.git
    

## Directory structure

Cloning or unzipping provides you with a root folder (`codelab-exoplayer-intro`), which contains a single gradle project with an app module, and multiple [modules](https://developer.android.com/studio/projects#ApplicationModules); one for each step of this codelab, along with all the resources you need.

## Import the project

  1. Start Android Studio.
  2. Choose **File** > **New** > **Import Project** *.*
  3. Select the root `build.gradle` file.



![128162a042143d68.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/128162a042143d68.png)

Screenshot: Project structure when importing

After the build finishes, you'll see six modules: the `app` module (of type _application_) and five modules with names `exoplayer-codelab-N` (where `N` is `00` to `04,` each of type _library_). The `app` module is actually empty, having only a manifest. Everything from the currently specified `exoplayer-codelab-N` module is merged when the app is built using a gradle dependency in `app/build.gradle`.

### app/build.gradle
    
    
    dependencies {
       implementation project(":exoplayer-codelab-00")
    }
    

**Note:** You can switch to the starting state of any step in this codelab by changing `exoplayer-codelab-00` to `explayer-codelab-N`, where `N` is the step number. After doing so, do `File -> Sync Project With Gradle Files`.

Your media player Activity is kept in the `exoplayer-codelab-N` module. The reason for keeping it in a separate library module is so you can share it among APKs targeting different platforms, such as mobile and Android TV. It also allows you to take advantage of features, such as [Dynamic Delivery](https://developer.android.com/studio/projects/dynamic-delivery), which allow your media playback feature to be installed only when the user needs it.

  4. Deploy and run the app to check everything is fine. The app should fill the screen with a black background.



![a674d5014bb3f798.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/a674d5014bb3f798.png)

Screenshot: Blank app running

##  3\. Stream! 

## Add ExoPlayer dependency

ExoPlayer is part of the [Jetpack Media3 library](https://developer.android.com/jetpack/androidx/releases/media3). Each release is uniquely identified by a string with the following format:
    
    
    androidx.media3:media3-exoplayer:X.X.X
    

You can add ExoPlayer to your project simply by importing its classes and UI components. It's pretty small, having a [shrunken footprint](https://developer.android.com/guide/topics/media/exoplayer/shrinking) of about 70-to-300 kB depending on the included features and supported formats. The ExoPlayer library is split into modules to allow developers to import only the functionality they need. For more information about ExoPlayer's modular structure, see [Add ExoPlayer modules](https://developer.android.com/guide/topics/media/exoplayer/hello-world#add-exoplayer-modules).

  1. Open the `build.gradle` file of the `exoplayer-codelab-00` module.
  2. Add the following lines to the `dependencies` section and sync the project.



### exoplayer-codelab-00/build.gradle
    
    
    def mediaVersion = "1.8.0"
    dependencies {
        [...]
       
        implementation "androidx.media3:media3-exoplayer:$mediaVersion"
        implementation "androidx.media3:media3-ui:$mediaVersion"
        implementation "androidx.media3:media3-exoplayer-dash:$mediaVersion"
    }
    

The below code snippet lists the imports that would be used in this codelab. You can choose to add them right away or subsequently as the codelab progresses.

### PlayerActivity.kt
    
    
    import android.util.Log
    import android.annotation.SuppressLint
    
    import androidx.media3.exoplayer.ExoPlayer
    import androidx.media3.common.Player
    import androidx.media3.common.MediaItem
    import androidx.media3.common.MimeTypes
    
    import androidx.core.view.WindowCompat
    import androidx.core.view.WindowInsetsCompat
    import androidx.core.view.WindowInsetsControllerCompat
    

## Add the `PlayerView element`

  1. Open the layout resource file `activity_player.xml` from the `exoplayer-codelab-00` module.
  2. Place the cursor inside the `FrameLayout` element.
  3. Start typing `<PlayerView` and let Android Studio autocomplete the `PlayerView` element.
  4. Use `match_parent` for the `width` and `height`.
  5. Declare the id as `video_view`.



### activity_player.xml
    
    
    <androidx.media3.ui.PlayerView
       android:id="@+id/video_view"
       android:layout_width="match_parent"
       android:layout_height="match_parent"/>
    

Going forward, you refer to this UI element as the video view.

  6. In the `PlayerActivity`, you can now obtain a reference to the view tree created from the XML file you just edited.



### PlayerActivity.kt
    
    
    private val viewBinding by lazy(LazyThreadSafetyMode.NONE) {
        ActivityPlayerBinding.inflate(layoutInflater)
    }
    

**Note:**`by lazy(LazyThreadSafetyMode.NONE) { ... }` is a kotlin delegate for lazy initializing a value the first time it is used. In our case, this is in the `onCreate` callback of the activity.

You can read more about the `lazy` delegate [here](https://kotlinlang.org/docs/delegated-properties.html#lazy-properties).

  7. Set the root of your view tree as the content view of your Activity. Also check to see that the `videoView` property is visible on your `viewBinding` reference, and that its type is `PlayerView`.


    
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(viewBinding.root)
    }
    

## Create an ExoPlayer

To play streaming media, you need an [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) object. The simplest way of creating one is to use the [`ExoPlayer.Builder`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer.Builder) class. As the name suggests, this uses the [builder pattern](https://en.wikipedia.org/wiki/Builder_pattern) to build an [`ExoPlayer`](https://developer.android.com/reference/androidx/media3/exoplayer/ExoPlayer) instance.

`ExoPlayer` is a convenient, all-purpose implementation of the `Player` interface.

Add a private method `initializePlayer` to create your `ExoPlayer`.

### PlayerActivity.kt
    
    
    private var player: ExoPlayer? = null
    
    [...]
    
    private fun initializePlayer() {
        player = ExoPlayer.Builder(this)
            .build()
            .also { exoPlayer ->
                viewBinding.videoView.player = exoPlayer
            }
    }
    

Create a `ExoPlayer.Builder` using your context, then call `build` to create your `ExoPlayer` object. This is then assigned to `player`, which you need to declare as a member field. You then use the `viewBinding.videoView.player` mutable property to bind the `player` to its corresponding view.

## Create a media item

Your `player` now needs some content to play. For this, you create a [`MediaItem`](https://developer.android.com/reference/androidx/media3/common/MediaItem). There are many different types of `MediaItem`, but you start by creating one for an MP3 file on the internet.

The simplest way to create a `MediaItem` is to use `MediaItem.fromUri`, which accepts the URI of a media file. Add the `MediaItem` to the `player` using `player.setMediaItem`.

  1. Add the following code to `initializePlayer` inside the `also` block:



### PlayerActivity.kt
    
    
    private fun initializePlayer() {
        [...]
            .also { exoPlayer ->
                [...]
    
                val mediaItem = MediaItem.fromUri(getString(R.string.media_url_mp3))
                exoPlayer.setMediaItem(mediaItem)
            }
    }
    

Note that `R.string.media_url_mp3` is defined as <https://storage.googleapis.com/exoplayer-test-media-0/play.mp3> in `strings.xml`.

## Playing nice with the Activity lifecycle

Our `player` can hog a lot of resources including memory, CPU, network connections and hardware codecs. Many of these resources are in short supply, particularly for hardware codecs where there may only be one. It's important that you release those resources for other apps to use when you're not using them, such as when your app is put into the background.

Put another way, your player's lifecycle should be tied to the [lifecycle of your app](https://developer.android.com/guide/components/activities/activity-lifecycle.html). To implement this, you need to override the four methods of `PlayerActivity`: `onStart`, `onResume`, `onPause`, and `onStop`.

  1. With `PlayerActivity` open, click **Code menu** > **Override methods...**.
  2. Select `onStart`, `onResume`, `onPause`, and `onStop`.
  3. Initialize the player in the `onStart` or `onResume` callback depending on the API level.



### PlayerActivity.kt
    
    
    public override fun onStart() {
        super.onStart()
        if (Build.VERSION.SDK_INT > 23) {
            initializePlayer()
        }
    }
    
    public override fun onResume() {
        super.onResume()
        hideSystemUi()
        if (Build.VERSION.SDK_INT <= 23 || player == null) {
            initializePlayer()
        }
    }
    

Android API level 24 and higher supports [multiple windows](https://developer.android.com/guide/topics/ui/multi-window). As your app can be visible, but not active in split window mode, you need to initialize the player in `onStart`. Android API level 23 and lower requires you to wait as long as possible until you grab resources, so you wait until `onResume` before initializing the player.

  4. Add the `hideSystemUi` method.



### PlayerActivity.kt
    
    
    @SuppressLint("InlinedApi")
    private fun hideSystemUi() {
        WindowCompat.setDecorFitsSystemWindows(window, false)
        WindowInsetsControllerCompat(window, viewBinding.videoView).let { controller ->
            controller.hide(WindowInsetsCompat.Type.systemBars())
            controller.systemBarsBehavior = WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
        }
    }
    

`hideSystemUi` is a helper method called in `onResume`, which allows you to have a full-screen experience.

  5. Release resources with `releasePlayer` (which you create shortly) in `onPause` and `onStop`.



### PlayerActivity.kt
    
    
    public override fun onPause() {
        super.onPause()
        if (Build.VERSION.SDK_INT <= 23) {
            releasePlayer()
        }
    }
    
    public override fun onStop() {
        super.onStop()
        if (Build.VERSION.SDK_INT > 23) {
            releasePlayer()
        }
    }
    

With API Level 23 and lower, there is no guarantee of `onStop` being called, so you have to release the player as early as possible in `onPause`. With API Level 24 and higher (which brought multi- and split-window mode), `onStop` is guaranteed to be called. In the paused state, your activity is still visible, so you wait to release the player until `onStop`.

You now need to create a `releasePlayer` method, which frees the player's resources and destroys it.

  6. Add the following code to the activity:



### PlayerActivity.kt
    
    
    private var playWhenReady = true
    private var currentItem = 0
    private var playbackPosition = 0L
    [...]
    
    private fun releasePlayer() {
        player?.let { exoPlayer ->
            playbackPosition = exoPlayer.currentPosition
            currentItem = exoPlayer.currentMediaItemIndex
            playWhenReady = exoPlayer.playWhenReady
            exoPlayer.release()
        }
        player = null
    }
    

Before you release and destroy the player, store the following information:

  * Play/pause state from [`playWhenReady`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlayWhenReady\(\)).
  * Current playback position from [`currentPosition`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentPosition\(\)).
  * Current media item index from [`currentMediaItemIndex`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getCurrentMediaItemIndex\(\)).



This allows you to resume playback from where the user left off. All you need to do is supply this state information when you initialize your player.

## Final preparation

All you need to do now is to supply the state information you saved in `releasePlayer` to your player during initialization.

  1. Add the following to `initializePlayer`:



### PlayerActivity.kt
    
    
    private fun initializePlayer() {
        [...]
        // Instead of exoPlayer.setMediaItem(mediaItem)
        exoPlayer.setMediaItems(listOf(mediaItem), currentItem, playbackPosition)
        exoPlayer.playWhenReady = playWhenReady
        exoPlayer.prepare()
    }
    

Here's what's happening:

  * [`playWhenReady`](https://developer.android.com/reference/androidx/media3/common/Player#setPlayWhenReady\(boolean\)) tells the player whether to start playing as soon as all resources for playback have been acquired. Because `playWhenReady` is initially `true`, playback starts automatically the first time the app is run.
  * [`seekTo`](https://developer.android.com/reference/androidx/media3/common/Player#seekTo\(int,long\)) tells the player to seek to a certain position within a specific media item. Both `currentItem` and `playbackPosition` are initialized to zero so that playback starts from the very start the first time the app is run.
  * [`prepare`](https://developer.android.com/reference/androidx/media3/common/Player#prepare\(\)) tells the player to acquire all the resources required for playback.



## Play audio

Finally, you are done! Start the app to play the MP3 file and see the embedded artwork.

![c5db1d3782d44450.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/c5db1d3782d44450.png)

Screenshot: The app playing a single track.

## Test the activity lifecycle

This is a good point at which to test whether the app works in all the different states of the activity lifecycle.

  1. Start another app and put your app in the foreground again. Does it resume at the correct position?
  2. Pause the app, and move it to the background and then to the foreground again. Does it stick to a paused state when backgrounded in paused state?
  3. Rotate the app. How does it behave if you change the orientation from portrait to landscape and back?



## Play video

If you want to play video, it's as easy as modifying the media item URI to an MP4 file.

  1. Change the URI in the `initializePlayer` method to `R.string.media_url_mp4`.
  2. Start the app again and test the behavior after being backgrounded with video playback as well.



### PlayerActivity.kt
    
    
    private fun initializePlayer() {
        [...]
        val mediaItem = MediaItem.fromUri(getString(R.string.media_url_mp4))
        [...]
    }
    

The `PlayerView` does it all. Instead of the artwork, the video is rendered full screen.

![7d2a8278e36f0f4b.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/7d2a8278e36f0f4b.png)

Screenshot: The app playing video.

You rock! You just created an app for full-screen media streaming on Android, complete with lifecycle management, saved state, and UI controls!

##  4\. Create a playlist 

**Note:** You can continue updating your current project or return to a known working state by importing the project from `exoplayer-intro/exoplayer-codelab-01`.

Your current app plays a single media file, but what if you want to play more than one media file, one after the other? For that, you need a playlist.

[Playlists](https://developer.android.com/guide/topics/media/exoplayer/playlists) can be created by adding more `MediaItem` objects to your `player` using [`addMediaItem`](https://developer.android.com/reference/androidx/media3/common/Player#addMediaItem\(androidx.media3.common.MediaItem\)). This allows seamless playback and buffering is handled in the background so the user doesn't see a buffering spinner when changing media items.

  1. Add the following code to `initializePlayer`:



### PlayerActivity.kt
    
    
    private void initializePlayer() {
        [...]
        val mediaItem = MediaItem.fromUri(getString(R.string.media_url_mp4)) // Existing code
    
        val secondMediaItem = MediaItem.fromUri(getString(R.string.media_url_mp3))
        // Update setMediaItems to include secondMediaItem
        exoPlayer.setMediaItems(listOf(mediaItem, secondMediaItem), currentItem, playbackPosition)
        [...]
    }
    

Check how the player controls behave. You can use ![d92346ced6303230.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/d92346ced6303230.png)and ![e9346dea9156c627.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/e9346dea9156c627.png) to navigate the sequence of media items.

![8385e35505ef5983.png](https://developer.android.com/static/codelabs/exoplayer-intro/img/8385e35505ef5983.png)

Screenshot: Playback controls showing a next and previous button

A playlist can be modified by calling methods like [addMediaItem(MediaItem item)](https://developer.android.com/reference/androidx/media3/common/Player#addMediaItem\(androidx.media3.common.MediaItem\)), [moveMediaItem(int fromIndex, int toIndex)](https://developer.android.com/reference/androidx/media3/common/Player#moveMediaItem\(int,int\)), and [removeMediaItem(int index)](https://developer.android.com/reference/androidx/media3/common/Player#removeMediaItem\(int\)) directly on the player. Playlist modifications can be performed when the player is in any state, including before the player is prepared and while media is currently playing.

That's pretty handy! For more information, see the developer documentation on [Media Items](https://developer.android.com/guide/topics/media/exoplayer/media-items) and [Playlists](https://developer.android.com/guide/topics/media/exoplayer/playlists), and [this article](https://medium.com/google-exoplayer/a-top-level-playlist-api-for-exoplayer-abe0a24edb55) about the Playlist API.

##  5\. Adaptive streaming 

**Note:** You can continue updating your current project or return to a known working state by importing the project from `exoplayer-intro/exoplayer-codelab-02`.

[Adaptive streaming](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming) is a technique for streaming media by varying the quality of the stream based on the available network bandwidth. This allows the user to experience the best-quality media that their bandwidth allows.

Typically, the same media content is split into multiple tracks with different qualities (bit rates and resolutions). The player chooses a track based on the available network bandwidth.

Each track is split into chunks of a given duration, typically between 2 and 10 seconds. This allows the player to quickly switch between tracks as available bandwidth changes. The player is responsible for stitching these chunks together for seamless playback.

## Adaptive track selection

At the heart of adaptive streaming is selecting the most appropriate track for the current environment. Update your app to play adaptive streaming media by using adaptive [track selection](https://developer.android.com/guide/topics/media/exoplayer/track-selection).

  1. Update `initializePlayer` with the following code:



### PlayerActivity.kt
    
    
    private fun initializePlayer() {
        player = ExoPlayer.Builder(this)
            .build()
            .also { exoPlayer ->
                // Update the track selection parameters to only pick standard definition tracks
                exoPlayer.trackSelectionParameters = exoPlayer.trackSelectionParameters
                        .buildUpon()
                        .setMaxVideoSizeSd()
                        .build()
                [...]
            }
    }
    

Here, we've updated the default `trackSelector` to only pick tracks of [standard definition](https://en.wikipedia.org/wiki/Standard-definition_television) or lower—a good way of saving your user's data at the expense of quality.

## Build an adaptive MediaItem

[DASH](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP) is a widely used adaptive streaming format. To stream DASH content, you need to create a `MediaItem` as before. However, this time, we must use a `MediaItem.Builder` rather than `fromUri`.

This is because `fromUri` uses the file extension to determine the underlying media format but our DASH URI does not have a file extension so we must supply a [MIME type](https://en.wikipedia.org/wiki/Media_type) of `APPLICATION_MPD` when constructing the `MediaItem`.

`MediaItem.Builder` allows you to create `MediaItem` instances with a number of additional properties, including:

  * The MIME type of the media content.
  * Protected content properties including the DRM type, license server URI and license request headers.
  * Side-loaded subtitle files to use during playback.
  * Clipping start and end positions.
  * An advert tag URI for advert insertion.



See the [Media items](https://developer.android.com/guide/topics/media/exoplayer/media-items) developer guide for more details.

  1. Update `initializePlayer` as follows:



### PlayerActivity.kt
    
    
    private void initializePlayer() {
        [...]
    
        // Replace this line...
        val mediaItem = MediaItem.fromUri(getString(R.string.media_url_mp4));
    
        // ... with this
         val mediaItem = MediaItem.Builder()
             .setUri(getString(R.string.media_url_dash))
             .setMimeType(MimeTypes.APPLICATION_MPD)
             .build()
    
        // Remove the following line
        val secondMediaItem = MediaItem.fromUri(getString(R.string.media_url_mp3))
    
        // Remove secondMediaItem from setMediaItems
        exoPlayer.setMediaItems(listOf(mediaItem), currentItem, playbackPosition)
    }
    

  2. Restart the app and see adaptive video streaming with DASH in action. It's pretty easy with ExoPlayer!



**Note:** You are now streaming DASH and using available bandwidth to select tracks. To see this in action, you can:

  1. Tap double shift to open **Search Everywhere**.
  2. Find the `AdaptiveTrackSelection` class.
  3. In the class, find `updateSelectedTrack` — this method is called when the track is updated.
  4. Put a breakpoint on the line starting with `newSelectedIndex == previousSelectedIndex`.
  5. Start your app in debug mode.



Watch how the breakpoint is hit each time the track selector needs to decide which track to use.

## Other adaptive streaming formats

[HLS](https://en.wikipedia.org/wiki/HTTP_Live_Streaming) (`MimeTypes.APPLICATION_M3U8`) and [SmoothStreaming](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming#Microsoft_Smooth_Streaming) (`MimeTypes.APPLICATION_SS`) are other commonly used adaptive streaming formats, both of which are supported by ExoPlayer. For more examples of constructing other adaptive media sources, see [the ExoPlayer demo app](https://github.com/androidx/media/blob/release/demos/main/src/main/java/androidx/media3/demo/main/SampleChooserActivity.java#L404).

##  6\. Listening for events 

**Note:** You can continue updating your current project or return to a known working state by importing the project from `exoplayer-intro/exoplayer-codelab-03`.

In the previous steps, you learned how to stream progressive and adaptive media streams. ExoPlayer is doing a lot of work for you behind the scenes, including the following:

  * Allocating memory
  * Downloading container files
  * Extracting metadata from the container
  * Decoding data
  * Rendering video, audio, and text to the screen and loudspeakers



Sometimes, it's useful to know what ExoPlayer is doing at runtime in order to understand and improve the playback experience for your users.

For example, you might want to reflect playback state changes in the user interface by doing the following:

  * Displaying a loading spinner when the player goes into a buffering state
  * Showing an overlay with "watch next" options when the track has ended



ExoPlayer offers [several listener interfaces](https://developer.android.com/guide/topics/media/exoplayer/listening-to-player-events) that provide callbacks for useful events. You use a listener to log what state the player is in.

## Listen up

**Note:** When implementing interfaces, it's tempting to put all the interface methods in your `PlayerActivity` class. However, this can result in lengthy code, which is difficult to read and maintain. A better solution is to use a factory function to generate an anonymous class of the interface to listen for events. This keeps your API clean and tidy.

  1. Create a `TAG` constant outside the `PlayerActivity` class, which you use for logging later.



### PlayerActivity.kt
    
    
    private const val TAG = "PlayerActivity"
    

  2. Implement the [`Player.Listener`](https://developer.android.com/reference/androidx/media3/common/Player.Listener) interface in a factory function outside the `PlayerActivity` class. This is used to inform you about important player events, including errors and playback state changes.
  3. Override `onPlaybackStateChanged` by adding the following code:



### PlayerActivity.kt
    
    
    private fun playbackStateListener() = object : Player.Listener {
        override fun onPlaybackStateChanged(playbackState: Int) {
            val stateString: String = when (playbackState) {
                ExoPlayer.STATE_IDLE -> "ExoPlayer.STATE_IDLE      -"
                ExoPlayer.STATE_BUFFERING -> "ExoPlayer.STATE_BUFFERING -"
                ExoPlayer.STATE_READY -> "ExoPlayer.STATE_READY     -"
                ExoPlayer.STATE_ENDED -> "ExoPlayer.STATE_ENDED     -"
                else -> "UNKNOWN_STATE             -"
            }
            Log.d(TAG, "changed state to $stateString")
        }
    }
    

**Note:** The properties that can be monitored through the `Player.Listener` normally have a corresponding getter method that can be used on the `Player` implementation. For example [`player.playbackState`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player#getPlaybackState\(\)) corresponds to [`onPlaybackStateChanged()`](https://developer.android.com/reference/kotlin/androidx/media3/common/Player.Listener#onPlaybackStateChanged\(int\)).

  4. Declare a private member of type `Player.Listener` in the `PlayerActivity`.



### PlayerActivity.kt
    
    
    class PlayerActivity : AppCompatActivity() {
        [...]
    
        private val playbackStateListener: Player.Listener = playbackStateListener()
    }
    

`onPlaybackStateChanged` is called when the playback state changes. The new state is given by the `playbackState` parameter.

The player can be in one of the following four states:

**State** | **Description**  
---|---  
`ExoPlayer.STATE_IDLE` | The player has been instantiated, but has not yet been prepared.  
`ExoPlayer.STATE_BUFFERING` | The player is not able to play from the current position because not enough data has been buffered.  
`ExoPlayer.STATE_READY` | The player can immediately play from the current position. This means the player will start playing media automatically if the player's [playWhenReady](https://developer.android.com/reference/androidx/media3/common/Player#getPlayWhenReady\(\)) property is `true`. If it is `false`, the player is paused.  
`ExoPlayer.STATE_ENDED` | The player has finished playing the media.  
  
**Note:** How do you know if your player is actually playing media? Well, all of the following conditions must be met:

  * playback state is `STATE_READY.`
  * `playWhenReady` is `true.`
  * playback is not suppressed for some other reason (for example, loss of [audio focus](https://developer.android.com/guide/topics/media-apps/audio-focus)).



Luckily, ExoPlayer provides a convenience method `ExoPlayer.isPlaying` for exactly this purpose! Or, if you want to be kept informed when `isPlaying` changes, you can listen for [`onIsPlayingChanged`](https://developer.android.com/reference/androidx/media3/common/Player.Listener#onIsPlayingChanged\(boolean\)).

## Register your listener

To have your callbacks called, you need to register your `playbackStateListener` with the player. Do that in `initializePlayer`.

  1. Register the listener before the play is prepared.



### PlayerActivity.kt
    
    
    private void initializePlayer() {
        [...]
        exoPlayer.playWhenReady = playWhenReady
        exoPlayer.addListener(playbackStateListener) // Add this line
        exoPlayer.prepare()
        [...]
    }
    

Again, you need to tidy up to avoid dangling references from the player which could cause a memory leak.

  2. Remove the listener in `releasePlayer`:



### PlayerActivity.kt
    
    
    private void releasePlayer() {
        player?.let { exoPlayer ->
            [...]
            exoPlayer.removeListener(playbackStateListener)
            exoPlayer.release()
        }
        player = null
    }
    

  3. Open logcat and run the app.
  4. Use the UI controls to seek forward / backward in the video. You could also try putting the app in the background, and bringing it back to foreground. In both the cases, you should see the playback state change in the logs.



## More events and analytics

ExoPlayer offers a number of other listeners, which are useful in understanding the user's playback experience. There are listeners for audio and video, as well as an [`AnalyticsListener`](https://developer.android.com/reference/androidx/media3/exoplayer/analytics/AnalyticsListener), which contains the callbacks from all the listeners. Some of the most important methods are the following:

  * [`onRenderedFirstFrame`](https://developer.android.com/reference/androidx/media3/exoplayer/analytics/AnalyticsListener#onRenderedFirstFrame\(androidx.media3.exoplayer.analytics.AnalyticsListener.EventTime,java.lang.Object,long\)) is called when the first frame of a video is rendered. With this, you can calculate how long the user had to wait to see meaningful content on the screen.
  * [`onDroppedVideoFrames`](https://developer.android.com/reference/androidx/media3/exoplayer/analytics/AnalyticsListener#onDroppedVideoFrames\(androidx.media3.exoplayer.analytics.AnalyticsListener.EventTime,int,long\)) is called when video frames have been dropped. Dropped frames indicate that playback is janky and the user experience is likely to be poor.
  * [`onAudioUnderrun`](https://developer.android.com/reference/androidx/media3/exoplayer/analytics/AnalyticsListener#onAudioUnderrun\(androidx.media3.exoplayer.analytics.AnalyticsListener.EventTime,int,long,long\)) is called when there has been an audio underrun. Underruns cause audible glitches in the sound and are more noticeable than dropped video frames.



`AnalyticsListener` can be added to the `player` with [`addListener`](https://developer.android.com/reference/androidx/media3/common/Player#addListener\(androidx.media3.common.Player.Listener\)). There are corresponding methods for the audio and video listeners as well.

The `Player.Listener` interface also includes the more general [`onEvents`](https://developer.android.com/reference/androidx/media3/common/Player.Listener#onEvents\(androidx.media3.common.Player,androidx.media3.common.Player.Events\)) callback that is triggered for any state change in the player. Some cases in which you may find this useful include when responding to multiple changes in state at the same time or when responding the same way to multiple different state changes. Check the reference documentation for more examples of when you might want to use the `onEvents` callback instead of individual state change callbacks.

Think about what events are important to your app and your users. For more information, see [Listening to playback events](https://developer.android.com/guide/topics/media/exoplayer/listening-to-player-events#listening_to_playback_events). That's it for event listeners!

##  7\. Congratulations 

**Note:** You can see the project in a complete state by importing the project from `exoplayer-intro/exoplayer-codelab-04`.

Congratulations! You learned a lot about integrating ExoPlayer with your app.

## Learn more

To learn more about ExoPlayer, check out [the developer guide](https://developer.android.com/guide/topics/media/exoplayer) and [source code](https://github.com/androidx/media), and subscribe to the [Android Developers blog](https://android-developers.googleblog.com/) to be among the first to hear about the latest updates!

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
