---
url: https://developer.android.com/reference/kotlin/android/app/Activity/
title: Activity \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:48.137345+00:00
---

# Activity  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/kotlin/android/app/Activity/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)

# Activity

* * *

Kotlin |[Java](https://developer.android.com/reference/android/app/Activity "View this page in Java")
    
    
    open class Activity : [ContextThemeWrapper](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html), [ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html), [KeyEvent.Callback](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html), [LayoutInflater.Factory2](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.Factory2.html), [View.OnCreateContextMenuListener](https://developer.android.com/reference/kotlin/android/view/View.OnCreateContextMenuListener.html), [Window.Callback](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html)

[kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)  
---  
↳ | [android.content.Context](https://developer.android.com/reference/kotlin/android/content/Context.html)  
|  ↳ | [android.content.ContextWrapper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html)  
|  |  ↳ | [android.view.ContextThemeWrapper](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html)  
|  |  |  ↳ | android.app.Activity  
Known Direct Subclasses [AccountAuthenticatorActivity](https://developer.android.com/reference/kotlin/android/accounts/AccountAuthenticatorActivity.html), [ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup), [AliasActivity](https://developer.android.com/reference/kotlin/android/app/AliasActivity), [ExpandableListActivity](https://developer.android.com/reference/kotlin/android/app/ExpandableListActivity), [ListActivity](https://developer.android.com/reference/kotlin/android/app/ListActivity), [NativeActivity](https://developer.android.com/reference/kotlin/android/app/NativeActivity) | [AccountAuthenticatorActivity](https://developer.android.com/reference/kotlin/android/accounts/AccountAuthenticatorActivity.html) |  Base class for implementing an Activity that is used to help implement an AbstractAccountAuthenticator.  
---|---  
[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup) |  A screen that contains and runs multiple embedded activities.  
[AliasActivity](https://developer.android.com/reference/kotlin/android/app/AliasActivity) |  Stub activity that launches another activity (and then finishes itself) based on information in its component's manifest meta-data.  
[ExpandableListActivity](https://developer.android.com/reference/kotlin/android/app/ExpandableListActivity) |  An activity that displays an expandable list of items by binding to a data source implementing the ExpandableListAdapter, and exposes event handlers when the user selects an item.  
[ListActivity](https://developer.android.com/reference/kotlin/android/app/ListActivity) |  An activity that displays a list of items by binding to a data source such as an array or Cursor, and exposes event handlers when the user selects an item.  
[NativeActivity](https://developer.android.com/reference/kotlin/android/app/NativeActivity) |  Convenience for implementing an activity that will be implemented purely in native code.  
  
Known Indirect Subclasses [LauncherActivity](https://developer.android.com/reference/kotlin/android/app/LauncherActivity), [PreferenceActivity](https://developer.android.com/reference/kotlin/android/preference/PreferenceActivity.html), [TabActivity](https://developer.android.com/reference/kotlin/android/app/TabActivity) | [LauncherActivity](https://developer.android.com/reference/kotlin/android/app/LauncherActivity) |  Displays a list of all activities which can be performed for a given intent.  
---|---  
[PreferenceActivity](https://developer.android.com/reference/kotlin/android/preference/PreferenceActivity.html) |  This is the base class for an activity to show a hierarchy of preferences to the user.  
[TabActivity](https://developer.android.com/reference/kotlin/android/app/TabActivity) |  For apps developing against `[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, tabs are typically presented in the UI using the new `[ActionBar.newTab()](https://developer.android.com/reference/kotlin/android/app/ActionBar#newTab\(\))` and related APIs for placing tabs within their action bar area.  
  
An activity is a single, focused thing that the user can do. Almost all activities interact with the user, so the Activity class takes care of creating a window for you in which you can place your UI with #setContentView. While activities are often presented to the user as full-screen windows, they can also be used in other ways: as floating windows (via a theme with `[android.R.attr#windowIsFloating](https://developer.android.com/reference/kotlin/android/R.attr.html#windowIsFloating:kotlin.Int)` set), [ Multi-Window mode](https://developer.android.com/guide/topics/ui/multi-window) or embedded into other windows. There are two methods almost all subclasses of Activity will implement: 

  * #onCreate is where you initialize your activity. Most importantly, here you will usually call `setContentView(int)` with a layout resource defining your UI, and using `findViewById` to retrieve the widgets in that UI that you need to interact with programmatically. 
  * `onPause` is where you deal with the user pausing active interaction with the activity. Any changes made by the user should at this point be committed (usually to the `[android.content.ContentProvider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html)` holding the data). In this state the activity is still visible on screen. 



To be of use with android.content.Context#startActivity, all activity classes must have a corresponding `[<activity>](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity:kotlin.IntArray)` declaration in their package's `AndroidManifest.xml`.

Topics covered here: 

  1. Fragments
  2. Activity Lifecycle
  3. Configuration Changes
  4. Starting Activities and Getting Results
  5. Saving Persistent State
  6. Permissions
  7. Process Lifecycle



### Developer Guides

The Activity class is an important part of an application's overall lifecycle, and the way activities are launched and put together is a fundamental part of the platform's application model. For a detailed perspective on the structure of an Android application and how activities behave, please read the [Application Fundamentals](https://developer.android.com/guide/topics/fundamentals.html) and [Tasks and Back Stack](https://developer.android.com/guide/components/tasks-and-back-stack.html) developer guides.

You can also find a detailed discussion about how to create activities in the [Activities](https://developer.android.com/guide/components/activities.html) developer guide.

### Fragments

The androidx.fragment.app.FragmentActivity subclass can make use of the androidx.fragment.app.Fragment class to better modularize their code, build more sophisticated user interfaces for larger screens, and help scale their application between small and large screens.

For more information about using fragments, read the [Fragments](https://developer.android.com/guide/components/fragments.html) developer guide.

### Activity Lifecycle

Activities in the system are managed as [ activity stacks](https://developer.android.com/guide/components/activities/tasks-and-back-stack). When a new activity is started, it is usually placed on the top of the current stack and becomes the running activity -- the previous activity always remains below it in the stack, and will not come to the foreground again until the new activity exits. There can be one or multiple activity stacks visible on screen.

An activity has essentially four states:

  * If an activity is in the foreground of the screen (at the highest position of the topmost stack), it is _active_ or _running_. This is usually the activity that the user is currently interacting with.
  * If an activity has lost focus but is still presented to the user, it is _visible_. It is possible if a new non-full-sized or transparent activity has focus on top of your activity, another activity has higher position in multi-window mode, or the activity itself is not focusable in current windowing mode. Such activity is completely alive (it maintains all state and member information and remains attached to the window manager). 
  * If an activity is completely obscured by another activity, it is _stopped_ or _hidden_. It still retains all state and member information, however, it is no longer visible to the user so its window is hidden and it will often be killed by the system when memory is needed elsewhere.
  * The system can drop the activity from memory by either asking it to finish, or simply killing its process, making it _destroyed_. When it is displayed again to the user, it must be completely restarted and restored to its previous state.



The following diagram shows the important state paths of an activity. The square rectangles represent callback methods you can implement to perform operations when the activity moves between states. The colored ovals are major states the activity can be in.

There are three key loops you may be interested in monitoring within your activity: 

  * The **entire lifetime** of an activity happens between the first call to #onCreate through to a single final call to `onDestroy`. An activity will do all setup of "global" state in onCreate(), and release all remaining resources in onDestroy(). For example, if it has a thread running in the background to download data from the network, it may create that thread in onCreate() and then stop the thread in onDestroy(). 
  * The **visible lifetime** of an activity happens between a call to `onStart` until a corresponding call to `onStop`. During this time the user can see the activity on-screen, though it may not be in the foreground and interacting with the user. Between these two methods you can maintain resources that are needed to show the activity to the user. For example, you can register a `[android.content.BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` in onStart() to monitor for changes that impact your UI, and unregister it in onStop() when the user no longer sees what you are displaying. The onStart() and onStop() methods can be called multiple times, as the activity becomes visible and hidden to the user. 
  * The **foreground lifetime** of an activity happens between a call to `onResume` until a corresponding call to `onPause`. During this time the activity is visible, active and interacting with the user. An activity can frequently go between the resumed and paused states -- for example when the device goes to sleep, when an activity result is delivered, when a new intent is delivered -- so the code in these methods should be fairly lightweight. 



The entire lifecycle of an activity is defined by the following Activity methods. All of these are hooks that you can override to do appropriate work when the activity changes state. All activities will implement #onCreate to do their initial setup; many will also implement `onPause` to commit changes to data and prepare to pause interacting with the user, and `onStop` to handle no longer being visible on screen. You should always call up to your superclass when implementing these methods.
    
    
    public class Activity extends ApplicationContext {
          protected void onCreate(Bundle savedInstanceState);
     
          protected void onStart();
     
          protected void onRestart();
     
          protected void onResume();
     
          protected void onPause();
     
          protected void onStop();
     
          protected void onDestroy();
      }
      

In general the movement through an activity's lifecycle looks like this:

Method | Description | Killable? | Next  
---|---|---|---  
onCreate | Called when the activity is first created. This is where you should do all of your normal static set up: create views, bind data to lists, etc. This method also provides you with a Bundle containing the activity's previously frozen state, if there was one. Always followed by `onStart()`. | No | `onStart()`  
| `onRestart()` | Called after your activity has been stopped, prior to it being started again. Always followed by `onStart()` | No | `onStart()`  
`onStart()` | Called when the activity is becoming visible to the user. Followed by `onResume()` if the activity comes to the foreground, or `onStop()` if it becomes hidden. | No | `onResume()` or `onStop()`  
| `onResume()` | Called when the activity will start interacting with the user. At this point your activity is at the top of its activity stack, with user input going to it. Always followed by `onPause()`. | No | `onPause()`  
`onPause()` | Called when the activity loses foreground state, is no longer focusable or before transition to stopped/hidden or destroyed state. The activity is still visible to user, so it's recommended to keep it visually active and continue updating the UI. Implementations of this method must be very quick because the next activity will not be resumed until this method returns. Followed by either `onResume()` if the activity returns back to the front, or `onStop()` if it becomes invisible to the user. | **Pre-`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)`** | `onResume()` or  
`onStop()`  
`onStop()` | Called when the activity is no longer visible to the user. This may happen either because a new activity is being started on top, an existing one is being brought in front of this one, or this one is being destroyed. This is typically used to stop animations and refreshing the UI, etc. Followed by either `onRestart()` if this activity is coming back to interact with the user, or `onDestroy()` if this activity is going away. | **Yes** | `onRestart()` or  
`onDestroy()`  
`onDestroy()` | The final call you receive before your activity is destroyed. This can happen either because the activity is finishing (someone called `Activity.finish` on it), or because the system is temporarily destroying this instance of the activity to save space. You can distinguish between these two scenarios with the `Activity.isFinishing` method. | **Yes** | _nothing_  
  
Note the "Killable" column in the above table -- for those methods that are marked as being killable, after that method returns the process hosting the activity may be killed by the system _at any time_ without another line of its code being executed. Because of this, you should use the `onPause` method to write any persistent data (such as user edits) to storage. In addition, the method `onSaveInstanceState(Bundle)` is called before placing the activity in such a background state, allowing you to save away any dynamic instance state in your activity into the given Bundle, to be later received in #onCreate if the activity needs to be re-created. See the Process Lifecycle section for more information on how the lifecycle of a process is tied to the activities it is hosting. Note that it is important to save persistent data in `onPause` instead of #onSaveInstanceState because the latter is not part of the lifecycle callbacks, so will not be called in every situation as described in its documentation.

Be aware that these semantics will change slightly between applications targeting platforms starting with `[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` vs. those targeting prior platforms. Starting with Honeycomb, an application is not in the killable state until its `onStop` has returned. This impacts when `onSaveInstanceState(Bundle)` may be called (it may be safely called after `onPause()`) and allows an application to safely wait until `onStop()` to save persistent state.

For applications targeting platforms starting with `[android.os.Build.VERSION_CODES#P](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#P:kotlin.Int)` `onSaveInstanceState(Bundle)` will always be called after `onStop`, so an application may safely perform fragment transactions in `onStop` and will be able to save persistent state later.

For those methods that are not marked as being killable, the activity's process will not be killed by the system starting from the time the method is called and continuing after it returns. Thus an activity is in the killable state, for example, between after `onStop()` to the start of `onResume()`. Keep in mind that under extreme memory pressure the system can kill the application process at any time.

### Configuration Changes

If the configuration of the device (as defined by the `[Resources.Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` class) changes, then anything displaying a user interface will need to update to match that configuration. Because Activity is the primary mechanism for interacting with the user, it includes special support for handling configuration changes.

Unless you specify otherwise, a configuration change (such as a change in screen orientation, language, input devices, etc.) will cause your current activity to be _destroyed_ , going through the normal activity lifecycle process of `onPause`, `onStop`, and `onDestroy` as appropriate. If the activity had been in the foreground or visible to the user, once `onDestroy` is called in that instance then a new instance of the activity will be created, with whatever savedInstanceState the previous instance had generated from #onSaveInstanceState.

This is done because any application resource, including layout files, can change based on any configuration value. Thus the only safe way to handle a configuration change is to re-retrieve all resources, including layouts, drawables, and strings. Because activities must already know how to save their state and re-create themselves from that state, this is a convenient way to have an activity restart itself with a new configuration.

In some special cases, you may want to bypass restarting of your activity based on one or more types of configuration changes. This is done with the `[android:configChanges](https://developer.android.com/reference/kotlin/android/R.attr.html#configChanges:kotlin.Int)` attribute in its manifest. For any types of configuration changes you say that you handle there, you will receive a call to your current activity's `onConfigurationChanged` method instead of being restarted. If a configuration change involves any that you do not handle, however, the activity will still be restarted and `onConfigurationChanged` will not be called.

### Starting Activities and Getting Results

The #startActivity method is used to start a new activity, which will be placed at the top of the activity stack. It takes a single argument, an `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)`, which describes the activity to be executed.

Sometimes you want to get a result back from an activity when it ends. For example, you may start an activity that lets the user pick a person in a list of contacts; when it ends, it returns the person that was selected. To do this, you call the `android.app.Activity.startActivityForResult(Intent,int)` version with a second integer parameter identifying the call. The result will come back through your #onActivityResult method.

When an activity exits, it can call `setResult(int)` to return data back to its parent. It must always supply a result code, which can be the standard results RESULT_CANCELED, RESULT_OK, or any custom values starting at RESULT_FIRST_USER. In addition, it can optionally return back an Intent containing any additional data it wants. All of this information appears back on the parent's `Activity.onActivityResult()`, along with the integer identifier it originally supplied.

If a child activity fails for any reason (such as crashing), the parent activity will receive a result with the code RESULT_CANCELED.
    
    
    public class MyActivity extends Activity {
          ...
     
          static final int PICK_CONTACT_REQUEST = 0;
     
          public boolean onKeyDown(int keyCode, KeyEvent event) {
              if (keyCode == KeyEvent.KEYCODE_DPAD_CENTER) {
                  // When the user center presses, let them pick a contact.
                  startActivityForResult(
                      new Intent(Intent.ACTION_PICK,
                      new Uri("content://contacts")),
                      PICK_CONTACT_REQUEST);
                 return true;
              }
              return false;
          }
     
          protected void onActivityResult(int requestCode, int resultCode,
                  Intent data) {
              if (requestCode == PICK_CONTACT_REQUEST) {
                  if (resultCode == RESULT_OK) {
                      // A contact was picked.  Here we will just display it
                      // to the user.
                      startActivity(new Intent(Intent.ACTION_VIEW, data));
                  }
              }
          }
      }
      

### Saving Persistent State

There are generally two kinds of persistent state that an activity will deal with: shared document-like data (typically stored in a SQLite database using a [content provider](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html)) and internal state such as user preferences.

For content provider data, we suggest that activities use an "edit in place" user model. That is, any edits a user makes are effectively made immediately without requiring an additional confirmation step. Supporting this model is generally a simple matter of following two rules:

  * When creating a new document, the backing database entry or file for it is created immediately. For example, if the user chooses to write a new email, a new entry for that email is created as soon as they start entering data, so that if they go to any other activity after that point this email will now appear in the list of drafts.

  * When an activity's `onPause()` method is called, it should commit to the backing content provider or file any changes the user has made. This ensures that those changes will be seen by any other activity that is about to run. You will probably want to commit your data even more aggressively at key times during your activity's lifecycle: for example before starting a new activity, before finishing your own activity, when the user switches between input fields, etc.




This model is designed to prevent data loss when a user is navigating between activities, and allows the system to safely kill an activity (because system resources are needed somewhere else) at any time after it has been stopped (or paused on platform versions before `[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)`). Note this implies that the user pressing BACK from your activity does _not_ mean "cancel" -- it means to leave the activity with its current contents saved away. Canceling edits in an activity must be provided through some other mechanism, such as an explicit "revert" or "undo" option.

See the [content package](https://developer.android.com/reference/kotlin/android/content/ContentProvider.html) for more information about content providers. These are a key aspect of how different activities invoke and propagate data between themselves.

The Activity class also provides an API for managing internal persistent state associated with an activity. This can be used, for example, to remember the user's preferred initial display in a calendar (day view or week view) or the user's default home page in a web browser.

Activity persistent state is managed with the method `getPreferences`, allowing you to retrieve and modify a set of name/value pairs associated with the activity. To use preferences that are shared across multiple application components (activities, receivers, services, providers), you can use the underlying `[Context.getSharedPreferences()](https://developer.android.com/reference/kotlin/android/content/Context.html#getSharedPreferences\(kotlin.String,%20kotlin.Int\))` method to retrieve a preferences object stored under a specific name. (Note that it is not possible to share settings data across application packages -- for that you will need a content provider.)

Here is an excerpt from a calendar activity that stores the user's preferred view mode in its persistent settings:
    
    
    public class CalendarActivity extends Activity {
          ...
     
          static final int DAY_VIEW_MODE = 0;
          static final int WEEK_VIEW_MODE = 1;
     
          private SharedPreferences mPrefs;
          private int mCurViewMode;
     
          protected void onCreate(Bundle savedInstanceState) {
              super.onCreate(savedInstanceState);
     
              mPrefs = getSharedPreferences(getLocalClassName(), MODE_PRIVATE);
              mCurViewMode = mPrefs.getInt("view_mode", DAY_VIEW_MODE);
          }
     
          protected void onPause() {
              super.onPause();
     
              SharedPreferences.Editor ed = mPrefs.edit();
              ed.putInt("view_mode", mCurViewMode);
              ed.commit();
          }
      }
      

### Permissions

The ability to start a particular Activity can be enforced when it is declared in its manifest's `[<activity>](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity:kotlin.IntArray)` tag. By doing so, other applications will need to declare a corresponding `[<uses-permission>](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestUsesPermission:kotlin.IntArray)` element in their own manifest to be able to start that activity. 

When starting an Activity you can set `[Intent.FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_READ_URI_PERMISSION:kotlin.Int)` and/or `[Intent.FLAG_GRANT_WRITE_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_WRITE_URI_PERMISSION:kotlin.Int)` on the Intent. This will grant the Activity access to the specific URIs in the Intent. Access will remain until the Activity has finished (it will remain across the hosting process being killed and other temporary destruction). As of `[android.os.Build.VERSION_CODES#GINGERBREAD](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#GINGERBREAD:kotlin.Int)`, if the Activity was already created and a new Intent is being delivered to `onNewIntent(Intent)`, any newly granted URI permissions will be added to the existing ones it holds. 

See the [Security and Permissions](https://developer.android.com/guide/topics/security/security.html) document for more information on permissions and security in general. 

### Process Lifecycle

The Android system attempts to keep an application process around for as long as possible, but eventually will need to remove old processes when memory runs low. As described in Activity Lifecycle, the decision about which process to remove is intimately tied to the state of the user's interaction with it. In general, there are four states a process can be in based on the activities running in it, listed here in order of importance. The system will kill less important processes (the last ones) before it resorts to killing more important processes (the first ones). 

  1. The **foreground activity** (the activity at the top of the screen that the user is currently interacting with) is considered the most important. Its process will only be killed as a last resort, if it uses more memory than is available on the device. Generally at this point the device has reached a memory paging state, so this is required in order to keep the user interface responsive. 

  2. A **visible activity** (an activity that is visible to the user but not in the foreground, such as one sitting behind a foreground dialog or next to other activities in multi-window mode) is considered extremely important and will not be killed unless that is required to keep the foreground activity running. 

  3. A **background activity** (an activity that is not visible to the user and has been stopped) is no longer critical, so the system may safely kill its process to reclaim memory for other foreground or visible processes. If its process needs to be killed, when the user navigates back to the activity (making it visible on the screen again), its #onCreate method will be called with the savedInstanceState it had previously supplied in #onSaveInstanceState so that it can restart itself in the same state as the user last left it. 

  4. An **empty process** is one hosting no activities or other application components (such as `[Service](https://developer.android.com/reference/kotlin/android/app/Service)` or `[android.content.BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` classes). These are killed very quickly by the system as memory becomes low. For this reason, any background operation you do outside of an activity must be executed in the context of an activity BroadcastReceiver or Service to ensure that the system knows it needs to keep your process around. 




Sometimes an Activity may need to do a long-running operation that exists independently of the activity lifecycle itself. An example may be a camera application that allows you to upload a picture to a web site. The upload may take a long time, and the application should allow the user to leave the application while it is executing. To accomplish this, your Activity should start a `[Service](https://developer.android.com/reference/kotlin/android/app/Service)` in which the upload takes place. This allows the system to properly prioritize your process (considering it to be more important than other non-visible applications) for the duration of the upload, independent of whether the original activity is paused, stopped, or finished.

## Summary

Nested classes  
---  
abstract |  `[ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback)` Interface for observing screen captures of an `Activity`.  
Constants  
---  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `DEFAULT_KEYS_DIALER` Use with `setDefaultKeyMode` to launch the dialer during default key handling.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `DEFAULT_KEYS_DISABLE` Use with `setDefaultKeyMode` to turn off default handling of keys.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `DEFAULT_KEYS_SEARCH_GLOBAL` Use with `setDefaultKeyMode` to specify that unhandled keystrokes will start a global search (typically web search, but some platforms may define alternate methods for global search)   
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `DEFAULT_KEYS_SEARCH_LOCAL` Use with `setDefaultKeyMode` to specify that unhandled keystrokes will start an application-defined search.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `DEFAULT_KEYS_SHORTCUT` Use with `setDefaultKeyMode` to execute a menu shortcut in default key handling.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `FULLSCREEN_MODE_REQUEST_ENTER` Request type of `requestFullscreenMode(int,OutcomeReceiver)`, to request enter fullscreen mode from multi-window mode.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `FULLSCREEN_MODE_REQUEST_EXIT` Request type of `requestFullscreenMode(int,OutcomeReceiver)`, to request exiting the requested fullscreen mode and restore to the previous multi-window mode.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `OVERRIDE_TRANSITION_CLOSE` Request type of `overrideActivityTransition(int,int,int)` or `overrideActivityTransition(int,int,int,int)`, to override the closing transition.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `OVERRIDE_TRANSITION_OPEN` Request type of `overrideActivityTransition(int,int,int)` or `overrideActivityTransition(int,int,int,int)`, to override the opening transition.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `RESULT_CANCELED` Standard activity result: operation canceled.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `RESULT_FIRST_USER` Start of user-defined activity results.  
static [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `RESULT_OK` Standard activity result: operation succeeded.  
Inherited constants  
---  
From class `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ACCESSIBILITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACCESSIBILITY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.accessibility.AccessibilityManager](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityManager.html)` for giving the user feedback for UI events through the registered event listeners.  
---|---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ACCOUNT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACCOUNT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.accounts.AccountManager](https://developer.android.com/reference/kotlin/android/accounts/AccountManager.html)` for receiving intents at a time of your choosing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ACTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACTIVITY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.ActivityManager](https://developer.android.com/reference/kotlin/android/app/ActivityManager)` for interacting with the global system state.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ADVANCED_PROTECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ADVANCED_PROTECTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.security.advancedprotection.AdvancedProtectionManager](https://developer.android.com/reference/kotlin/android/security/advancedprotection/AdvancedProtectionManager.html)`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ALARM_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ALARM_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.AlarmManager](https://developer.android.com/reference/kotlin/android/app/AlarmManager)` for receiving intents at a time of your choosing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[APPWIDGET_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APPWIDGET_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.appwidget.AppWidgetManager](https://developer.android.com/reference/kotlin/android/appwidget/AppWidgetManager.html)` for accessing AppWidgets.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[APP_FUNCTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APP_FUNCTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[AppFunctionManager](https://developer.android.com/reference/kotlin/android/app/appfunctions/AppFunctionManager)` for executing app functions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[APP_INTERACTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APP_INTERACTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.app.AppInteractionManager](https://developer.android.com/reference/kotlin/android/app/AppInteractionManager)` for managing app interactions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[APP_OPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APP_OPS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.AppOpsManager](https://developer.android.com/reference/kotlin/android/app/AppOpsManager)` for tracking application operations on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[APP_SEARCH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APP_SEARCH_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.app.appsearch.AppSearchManager](https://developer.android.com/reference/kotlin/android/app/appsearch/AppSearchManager)` for indexing and querying app data managed by the system.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[AUDIO_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUDIO_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.AudioManager](https://developer.android.com/reference/kotlin/android/media/AudioManager.html)` for handling management of volume, ringer modes and audio routing.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[AUTHENTICATION_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUTHENTICATION_POLICY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.security.authenticationpolicy.AuthenticationPolicyManager](https://developer.android.com/reference/kotlin/android/security/authenticationpolicy/AuthenticationPolicyManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[AUTOFILL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUTOFILL_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.view.autofill.AutofillManager](https://developer.android.com/reference/kotlin/android/view/autofill/AutofillManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[BATTERY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BATTERY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.BatteryManager](https://developer.android.com/reference/kotlin/android/os/BatteryManager.html)` for managing battery state.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_ABOVE_CLIENT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ABOVE_CLIENT:kotlin.Int)` Flag for #bindService: indicates that the client application binding to this service considers the service to be more important than the app itself. When set, the platform will try to have the out of memory killer kill the app before it kills the service it is bound to, though this is not guaranteed to be the case.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_ADJUST_WITH_ACTIVITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ADJUST_WITH_ACTIVITY:kotlin.Int)` Flag for #bindService: If binding from an activity, allow the target service's process importance to be raised based on whether the activity is visible to the user, regardless whether another flag is used to reduce the amount that the client process's overall importance is used to impact it.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_ALLOW_ACTIVITY_STARTS](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ALLOW_ACTIVITY_STARTS:kotlin.Int)` Flag for #bindService: If binding from an app that is visible, the bound service is allowed to start an activity from background. This was the default behavior before SDK version `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`. Since then, the default behavior changed to disallow the bound service to start a background activity even if the app bound to it is in foreground, unless this flag is specified when binding.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_ALLOW_OOM_MANAGEMENT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ALLOW_OOM_MANAGEMENT:kotlin.Int)` Flag for #bindService: allow the process hosting the bound service to go through its normal memory management. It will be treated more like a running service, allowing the system to (temporarily) expunge the process if low on memory or for some other whim it may have, and being more aggressive about making it a candidate to be killed (and restarted) if running for a long time.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_AUTO_CREATE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_AUTO_CREATE:kotlin.Int)` Flag for #bindService: automatically create the service as long as the binding exists. Note that while this will create the service, its `[android.app.Service#onStartCommand](https://developer.android.com/reference/kotlin/android/app/Service#onStartCommand\(android.content.Intent,%20kotlin.Int,%20kotlin.Int\))` method will still only be called due to an explicit call to `[startService](https://developer.android.com/reference/kotlin/android/content/Context.html#startService\(android.content.Intent\))`. Even without that, though, this still provides you with access to the service object while the service is created.  Note that prior to `[android.os.Build.VERSION_CODES#ICE_CREAM_SANDWICH](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ICE_CREAM_SANDWICH:kotlin.Int)`, not supplying this flag would also impact how important the system consider's the target service's process to be. When set, the only way for it to be raised was by binding from a service in which case it will only be important when that activity is in the foreground. Now to achieve this behavior you must explicitly supply the new flag `[BIND_ADJUST_WITH_ACTIVITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ADJUST_WITH_ACTIVITY:kotlin.Int)`. For compatibility, old applications that don't specify `[BIND_AUTO_CREATE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_AUTO_CREATE:kotlin.Int)` will automatically have the flags `[BIND_WAIVE_PRIORITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_WAIVE_PRIORITY:kotlin.Int)` and `[BIND_ADJUST_WITH_ACTIVITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ADJUST_WITH_ACTIVITY:kotlin.Int)` set for them in order to achieve the same result.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_DEBUG_UNBIND](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_DEBUG_UNBIND:kotlin.Int)` Flag for #bindService: include debugging help for mismatched calls to unbind. When this flag is set, the callstack of the following `[unbindService](https://developer.android.com/reference/kotlin/android/content/Context.html#unbindService\(android.content.ServiceConnection\))` call is retained, to be printed if a later incorrect unbind call is made. Note that doing this requires retaining information about the binding that was made for the lifetime of the app, resulting in a leak -- this should only be used for debugging.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_EXTERNAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_EXTERNAL_SERVICE:kotlin.Int)` Flag for #bindService: The service being bound is an `[isolated](https://developer.android.com/reference/kotlin/android/R.attr.html#isolatedProcess:kotlin.Int)`, `[external](https://developer.android.com/reference/kotlin/android/R.attr.html#externalService:kotlin.Int)` service. This binds the service into the calling application's package, rather than the package in which the service is declared.  When using this flag, the code for the service being bound will execute under the calling application's package name and user ID. Because the service must be an isolated process, it will not have direct access to the application's data, though. The purpose of this flag is to allow applications to provide services that are attributed to the app using the service, rather than the application providing the service.  _This flag is NOT compatible with`[BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html)`. If you need to use `[BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html)`, you must use `[BIND_EXTERNAL_SERVICE_LONG](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_EXTERNAL_SERVICE_LONG:kotlin.Long)` instead._  
`[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` | `[BIND_EXTERNAL_SERVICE_LONG](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_EXTERNAL_SERVICE_LONG:kotlin.Long)` Works in the same way as `[BIND_EXTERNAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_EXTERNAL_SERVICE:kotlin.Int)`, but it's defined as a `long` value that is compatible to `[BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html)`.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_IMPORTANT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_IMPORTANT:kotlin.Int)` Flag for #bindService: this service is very important to the client, so should be brought to the foreground process level when the client is. Normally a process can only be raised to the visibility level by a client, even if that client is in the foreground.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_INCLUDE_CAPABILITIES](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_INCLUDE_CAPABILITIES:kotlin.Int)` Flag for #bindService: If binding from an app that has specific capabilities due to its foreground state such as an activity or foreground service, then this flag will allow the bound app to get the same capabilities, as long as it has the required permissions as well. If binding from a top app and its target SDK version is at or above `[android.os.Build.VERSION_CODES#R](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#R:kotlin.Int)`, the app needs to explicitly use BIND_INCLUDE_CAPABILITIES flag to pass all capabilities to the service so the other app can have while-in-use access such as location, camera, microphone from background. If binding from a top app and its target SDK version is below `[android.os.Build.VERSION_CODES#R](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#R:kotlin.Int)`, BIND_INCLUDE_CAPABILITIES is implicit.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_NOT_FOREGROUND](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_NOT_FOREGROUND:kotlin.Int)` Flag for #bindService: don't allow this binding to raise the target service's process to the foreground scheduling priority. It will still be raised to at least the same memory priority as the client (so that its process will not be killable in any situation where the client is not killable), but for CPU scheduling purposes it may be left in the background. This only has an impact in the situation where the binding client is a foreground process and the target service is in a background process.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_NOT_PERCEPTIBLE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_NOT_PERCEPTIBLE:kotlin.Int)` Flag for #bindService: If binding from an app that is visible or user-perceptible, lower the target service's importance to below the perceptible level. This allows the system to (temporarily) expunge the bound process from memory to make room for more important user-perceptible processes.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_PACKAGE_ISOLATED_PROCESS](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_PACKAGE_ISOLATED_PROCESS:kotlin.Int)` Flag for #bindIsolatedService: Bind the service into a shared isolated process, but only with other isolated services from the same package that declare the same process name.  Specifying this flag allows multiple isolated services defined in the same package to be running in a single shared isolated process. This shared isolated process must be specified since this flag will not work with the default application process.  This flag is different from `[BIND_SHARED_ISOLATED_PROCESS](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_SHARED_ISOLATED_PROCESS:kotlin.Int)` since it only allows binding services from the same package in the same shared isolated process. This also means the shared package isolated process is global, and not scoped to each potential calling app.  The shared isolated process instance is identified by the "android:process" attribute defined by the service. This flag cannot be used without this attribute set.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_SHARED_ISOLATED_PROCESS](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_SHARED_ISOLATED_PROCESS:kotlin.Int)` Flag for #bindIsolatedService: Bind the service into a shared isolated process. Specifying this flag allows multiple isolated services to be running in a single shared isolated process. The shared isolated process instance is identified by the instanceName parameter in `[bindIsolatedService(Intent,int,String,Executor,ServiceConnection)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindIsolatedService\(android.content.Intent,%20kotlin.Int,%20kotlin.String,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))`. Subsequent calls to #bindIsolatedService with the same instanceName will cause the isolated service to be co-located in the same shared isolated process. Note that the shared isolated process is scoped to the calling app; once created, only the calling app can bind additional isolated services into the shared process. However, the services themselves can come from different APKs and therefore different vendors. Only services that set the `[android.R.attr#allowSharedIsolatedProcess](https://developer.android.com/reference/kotlin/android/R.attr.html#allowSharedIsolatedProcess:kotlin.Int)` attribute to `true` are allowed to be bound into a shared isolated process.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[BIND_WAIVE_PRIORITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_WAIVE_PRIORITY:kotlin.Int)` Flag for #bindService: don't impact the scheduling or memory management priority of the target service's hosting process. Allows the service's process to be managed on the background LRU list just like a regular application process in the background.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[BIOMETRIC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIOMETRIC_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.biometrics.BiometricManager](https://developer.android.com/reference/kotlin/android/hardware/biometrics/BiometricManager.html)` for handling biometric and PIN/pattern/password authentication.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[BLOB_STORE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BLOB_STORE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.blob.BlobStoreManager](https://developer.android.com/reference/kotlin/android/app/blob/BlobStoreManager)` for contributing and accessing data blobs from the blob store maintained by the system.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[BLUETOOTH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BLUETOOTH_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.bluetooth.BluetoothManager](https://developer.android.com/reference/kotlin/android/bluetooth/BluetoothManager.html)` for using Bluetooth.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[BUGREPORT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BUGREPORT_SERVICE:kotlin.String)` Service to capture a bugreport.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CAMERA_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CAMERA_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.camera2.CameraManager](https://developer.android.com/reference/kotlin/android/hardware/camera2/CameraManager.html)` for interacting with camera devices.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CAPTIONING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CAPTIONING_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.accessibility.CaptioningManager](https://developer.android.com/reference/kotlin/android/view/accessibility/CaptioningManager.html)` for obtaining captioning properties and listening for changes in captioning preferences.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CARRIER_CONFIG_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CARRIER_CONFIG_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.CarrierConfigManager](https://developer.android.com/reference/kotlin/android/telephony/CarrierConfigManager.html)` for reading carrier configuration values.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CHOOSER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CHOOSER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.service.chooser.ChooserManager](https://developer.android.com/reference/kotlin/android/service/chooser/ChooserManager.html)`.  **Note:** This service is not available on Wear OS, Android TV, or Android Auto devices. On these form factors, calls to `getSystemService` for this service will return `null`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CLIPBOARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CLIPBOARD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.ClipboardManager](https://developer.android.com/reference/kotlin/android/content/ClipboardManager.html)` for accessing and modifying the contents of the global clipboard.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[COMPANION_DEVICE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#COMPANION_DEVICE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.companion.CompanionDeviceManager](https://developer.android.com/reference/kotlin/android/companion/CompanionDeviceManager.html)` for managing companion devices  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CONNECTIVITY_DIAGNOSTICS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONNECTIVITY_DIAGNOSTICS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.ConnectivityDiagnosticsManager](https://developer.android.com/reference/kotlin/android/net/ConnectivityDiagnosticsManager.html)` for performing network connectivity diagnostics as well as receiving network connectivity information from the system.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CONNECTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONNECTIVITY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.ConnectivityManager](https://developer.android.com/reference/kotlin/android/net/ConnectivityManager.html)` for handling management of network connections.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CONSUMER_IR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONSUMER_IR_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.ConsumerIrManager](https://developer.android.com/reference/kotlin/android/hardware/ConsumerIrManager.html)` for transmitting infrared signals from the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CONTACT_KEYS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTACT_KEYS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[E2eeContactKeysManager](https://developer.android.com/reference/kotlin/android/provider/E2eeContactKeysManager.html)` to managing contact keys.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CONTENT_RESTRICTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTENT_RESTRICTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.contentsafety.ContentSafetyManager](https://developer.android.com/reference/kotlin/android/app/contentsafety/ContentSafetyManager)`.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[CONTEXT_IGNORE_SECURITY](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTEXT_IGNORE_SECURITY:kotlin.Int)` Flag for use with `[createPackageContext](https://developer.android.com/reference/kotlin/android/content/Context.html#createPackageContext\(kotlin.String,%20kotlin.Int\))`: ignore any security restrictions on the Context being requested, allowing it to always be loaded. For use with `[CONTEXT_INCLUDE_CODE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTEXT_INCLUDE_CODE:kotlin.Int)` to allow code to be loaded into a process even when it isn't safe to do so. Use with extreme care!  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[CONTEXT_INCLUDE_CODE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTEXT_INCLUDE_CODE:kotlin.Int)` Flag for use with `[createPackageContext](https://developer.android.com/reference/kotlin/android/content/Context.html#createPackageContext\(kotlin.String,%20kotlin.Int\))`: include the application code with the context. This means loading code into the caller's process, so that `[getClassLoader()](https://developer.android.com/reference/kotlin/android/content/Context.html#getClassLoader\(\))` can be used to instantiate the application's classes. Setting this flags imposes security restrictions on what application context you can access; if the requested application can not be safely loaded into your process, java.lang.SecurityException will be thrown. If this flag is not set, there will be no restrictions on the packages that can be loaded, but `[getClassLoader](https://developer.android.com/reference/kotlin/android/content/Context.html#getClassLoader\(\))` will always return the default system class loader.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[CONTEXT_RESTRICTED](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTEXT_RESTRICTED:kotlin.Int)` Flag for use with `[createPackageContext](https://developer.android.com/reference/kotlin/android/content/Context.html#createPackageContext\(kotlin.String,%20kotlin.Int\))`: a restricted context may disable specific features. For instance, a View associated with a restricted context would ignore particular XML attributes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CREDENTIAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CREDENTIAL_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.credentials.CredentialManager](https://developer.android.com/reference/kotlin/android/credentials/CredentialManager.html)` to authenticate a user to your app.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[CROSS_PROFILE_APPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CROSS_PROFILE_APPS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.pm.CrossProfileApps](https://developer.android.com/reference/kotlin/android/content/pm/CrossProfileApps.html)` for cross profile operations.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)` The default device ID, which is the ID of the primary (non-virtual) device.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[DEVICE_ID_INVALID](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_INVALID:kotlin.Int)` Invalid device ID.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DEVICE_LOCK_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_LOCK_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.devicelock.DeviceLockManager](https://developer.android.com/reference/kotlin/android/devicelock/DeviceLockManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DEVICE_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_POLICY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.admin.DevicePolicyManager](https://developer.android.com/reference/kotlin/android/app/admin/DevicePolicyManager)` for working with global device policy management.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DISPLAY_HASH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DISPLAY_HASH_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to access `[android.view.displayhash.DisplayHashManager](https://developer.android.com/reference/kotlin/android/view/displayhash/DisplayHashManager.html)` to handle display hashes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DISPLAY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DISPLAY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.display.DisplayManager](https://developer.android.com/reference/kotlin/android/hardware/display/DisplayManager.html)` for interacting with display devices.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DOMAIN_VERIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DOMAIN_VERIFICATION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to access `[android.content.pm.verify.domain.DomainVerificationManager](https://developer.android.com/reference/kotlin/android/content/pm/verify/domain/DomainVerificationManager.html)` to retrieve approval and user state for declared web domains.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DOWNLOAD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DOWNLOAD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.DownloadManager](https://developer.android.com/reference/kotlin/android/app/DownloadManager)` for requesting HTTP downloads.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[DROPBOX_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DROPBOX_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.DropBoxManager](https://developer.android.com/reference/kotlin/android/os/DropBoxManager.html)` instance for recording diagnostic logs.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[EUICC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#EUICC_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.euicc.EuiccManager](https://developer.android.com/reference/kotlin/android/telephony/euicc/EuiccManager.html)` to manage the device eUICC (embedded SIM).  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[FILE_INTEGRITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#FILE_INTEGRITY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.security.FileIntegrityManager](https://developer.android.com/reference/kotlin/android/security/FileIntegrityManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[FILE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#FILE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.storage.FileManager](https://developer.android.com/reference/kotlin/android/os/storage/FileManager.html)` for handling file operations.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[GAME_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#GAME_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[GameManager](https://developer.android.com/reference/kotlin/android/app/GameManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[GRAMMATICAL_INFLECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#GRAMMATICAL_INFLECTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[GrammaticalInflectionManager](https://developer.android.com/reference/kotlin/android/app/GrammaticalInflectionManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[HARDWARE_PROPERTIES_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HARDWARE_PROPERTIES_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.HardwarePropertiesManager](https://developer.android.com/reference/kotlin/android/os/HardwarePropertiesManager.html)` for accessing the hardware properties service.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[HEALTHCONNECT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HEALTHCONNECT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.health.connect.HealthConnectManager](https://developer.android.com/reference/kotlin/android/health/connect/HealthConnectManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[HID_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HID_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.hid.HidManager](https://developer.android.com/reference/kotlin/android/hardware/hid/HidManager.html)` for interacting with HID devices.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[INPUT_METHOD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#INPUT_METHOD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.inputmethod.InputMethodManager](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager.html)` for accessing input methods.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[INPUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#INPUT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.input.InputManager](https://developer.android.com/reference/kotlin/android/hardware/input/InputManager.html)` for interacting with input devices.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[IPSEC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#IPSEC_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.IpSecManager](https://developer.android.com/reference/kotlin/android/net/IpSecManager.html)` for encrypting Sockets or Networks with IPSec.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[JOB_SCHEDULER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#JOB_SCHEDULER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.job.JobScheduler](https://developer.android.com/reference/kotlin/android/app/job/JobScheduler)` instance for managing occasional background tasks.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[KEYCHAIN_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYCHAIN_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.security.KeyChainManager](https://developer.android.com/reference/kotlin/android/security/KeyChainManager.html)` for managing KeyChain certificates and grants.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[KEYGUARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYGUARD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.KeyguardManager](https://developer.android.com/reference/kotlin/android/app/KeyguardManager)` for controlling keyguard.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[KEYSTORE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYSTORE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.security.keystore.KeyStoreManager](https://developer.android.com/reference/kotlin/android/security/keystore/KeyStoreManager.html)` for accessing [Android Keystore](https://developer.android.com/reference/kotlin/privacy-and-security/keystore) functions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[LAUNCHER_APPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LAUNCHER_APPS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.pm.LauncherApps](https://developer.android.com/reference/kotlin/android/content/pm/LauncherApps.html)` for querying and monitoring launchable apps across profiles of a user.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[LAYOUT_INFLATER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LAYOUT_INFLATER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)` for inflating layout resources in this context.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[LOCALE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LOCALE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.LocaleManager](https://developer.android.com/reference/kotlin/android/app/LocaleManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[LOCATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LOCATION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.location.LocationManager](https://developer.android.com/reference/kotlin/android/location/LocationManager.html)` for controlling location updates.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_COMMUNICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_COMMUNICATION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.MediaCommunicationManager](https://developer.android.com/reference/kotlin/android/media/MediaCommunicationManager.html)` for managing `[android.media.MediaSession2](https://developer.android.com/reference/kotlin/android/media/MediaSession2.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_METRICS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_METRICS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.metrics.MediaMetricsManager](https://developer.android.com/reference/kotlin/android/media/metrics/MediaMetricsManager.html)` for interacting with media metrics on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_PROJECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_PROJECTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.projection.MediaProjectionManager](https://developer.android.com/reference/kotlin/android/media/projection/MediaProjectionManager.html)` instance for managing media projection sessions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_QUALITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_QUALITY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.quality.MediaQualityManager](https://developer.android.com/reference/kotlin/android/media/quality/MediaQualityManager.html)` for standardize picture and audio API parameters.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_ROUTER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_ROUTER_SERVICE:kotlin.String)` Use with #getSystemService to retrieve a `[android.media.MediaRouter](https://developer.android.com/reference/kotlin/android/media/MediaRouter.html)` for controlling and managing routing of media.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEDIA_SESSION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_SESSION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.session.MediaSessionManager](https://developer.android.com/reference/kotlin/android/media/session/MediaSessionManager.html)` for managing media Sessions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MEMORY_BUDGET_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEMORY_BUDGET_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.MemoryBudgetManager](https://developer.android.com/reference/kotlin/android/app/MemoryBudgetManager)` for monitoring memory budgets.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MIDI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MIDI_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.midi.MidiManager](https://developer.android.com/reference/kotlin/android/media/midi/MidiManager.html)` for accessing the MIDI service.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_APPEND](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_APPEND:kotlin.Int)` File creation mode: for use with `[openFileOutput](https://developer.android.com/reference/kotlin/android/content/Context.html#openFileOutput\(kotlin.String,%20kotlin.Int\))`, if the file already exists then write data to the end of the existing file instead of erasing it.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_ENABLE_WRITE_AHEAD_LOGGING](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_ENABLE_WRITE_AHEAD_LOGGING:kotlin.Int)` Database open flag: when set, the database is opened with write-ahead logging enabled by default.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_MULTI_PROCESS](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_MULTI_PROCESS:kotlin.Int)` SharedPreference loading flag: when set, the file on disk will be checked for modification even if the shared preferences instance is already loaded in this process. This behavior is sometimes desired in cases where the application has multiple processes, all writing to the same SharedPreferences file. Generally there are better forms of communication between processes, though.  This was the legacy (but undocumented) behavior in and before Gingerbread (Android 2.3) and this flag is implied when targeting such releases. For applications targeting SDK versions _greater than_ Android 2.3, this flag must be explicitly set if desired.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_NO_LOCALIZED_COLLATORS](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_NO_LOCALIZED_COLLATORS:kotlin.Int)` Database open flag: when set, the database is opened without support for localized collators.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_PRIVATE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_PRIVATE:kotlin.Int)` File creation mode: the default mode, where the created file can only be accessed by the calling application (or all applications sharing the same user ID).  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_WORLD_READABLE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_WORLD_READABLE:kotlin.Int)` File creation mode: allow all other applications to have read access to the created file.  Starting from `[android.os.Build.VERSION_CODES#N](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#N:kotlin.Int)`, attempting to use this mode throws a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[MODE_WORLD_WRITEABLE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_WORLD_WRITEABLE:kotlin.Int)` File creation mode: allow all other applications to have write access to the created file.  Starting from `[android.os.Build.VERSION_CODES#N](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#N:kotlin.Int)`, attempting to use this mode will throw a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[MULTISENSORY_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MULTISENSORY_MANAGER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve the service that plays multisensory feedback.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[NETWORK_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NETWORK_STATS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.usage.NetworkStatsManager](https://developer.android.com/reference/kotlin/android/app/usage/NetworkStatsManager)` for querying network usage stats.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[NFC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NFC_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.nfc.NfcManager](https://developer.android.com/reference/kotlin/android/nfc/NfcManager.html)` for using NFC.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[NOTIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NOTIFICATION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.NotificationManager](https://developer.android.com/reference/kotlin/android/app/NotificationManager)` for informing the user of background events.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[NPU_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NPU_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `android.npumanager.NpuManager`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[NSD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NSD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.nsd.NsdManager](https://developer.android.com/reference/kotlin/android/net/nsd/NsdManager.html)` for handling management of network service discovery  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[OVERLAY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#OVERLAY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.om.OverlayManager](https://developer.android.com/reference/kotlin/android/content/om/OverlayManager.html)` for managing overlay packages.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PCC_SANDBOX_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PCC_SANDBOX_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.privatecompute.PccSandboxManager](https://developer.android.com/reference/kotlin/android/app/privatecompute/PccSandboxManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PEOPLE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PEOPLE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to access a `[PeopleManager](https://developer.android.com/reference/kotlin/android/app/people/PeopleManager)` to interact with your published conversations.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PERFORMANCE_HINT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PERFORMANCE_HINT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.PerformanceHintManager](https://developer.android.com/reference/kotlin/android/os/PerformanceHintManager.html)` for accessing the performance hinting service.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PERSISTENT_DATA_BLOCK_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PERSISTENT_DATA_BLOCK_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.service.persistentdata.PersistentDataBlockManager](https://developer.android.com/reference/kotlin/android/service/persistentdata/PersistentDataBlockManager.html)` instance for interacting with a storage device that lives across factory resets.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[POWER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#POWER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.PowerManager](https://developer.android.com/reference/kotlin/android/os/PowerManager.html)` for controlling power management, including "wake locks," which let you keep the device on while you're running long tasks.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PRINT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PRINT_SERVICE:kotlin.String)` `[android.print.PrintManager](https://developer.android.com/reference/kotlin/android/print/PrintManager.html)` for printing and managing printers and print tasks.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[PROFILING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PROFILING_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.os.ProfilingManager](https://developer.android.com/reference/kotlin/android/os/ProfilingManager.html)`.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[RECEIVER_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_EXPORTED:kotlin.Int)` Flag for #registerReceiver: The receiver can receive broadcasts from other Apps. Has the same behavior as marking a statically registered receiver with "exported=true"  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[RECEIVER_NOT_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_NOT_EXPORTED:kotlin.Int)` Flag for #registerReceiver: The receiver cannot receive broadcasts from other Apps. Has the same behavior as marking a statically registered receiver with "exported=false"  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[RECEIVER_VISIBLE_TO_INSTANT_APPS](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_VISIBLE_TO_INSTANT_APPS:kotlin.Int)` Flag for #registerReceiver: The receiver can receive broadcasts from Instant Apps.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[RESTRICTIONS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#RESTRICTIONS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.RestrictionsManager](https://developer.android.com/reference/kotlin/android/content/RestrictionsManager.html)` for retrieving application restrictions and requesting permissions for restricted operations.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[ROLE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ROLE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.role.RoleManager](https://developer.android.com/reference/kotlin/android/app/role/RoleManager)` for managing roles.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SATELLITE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SATELLITE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.satellite.SatelliteManager](https://developer.android.com/reference/kotlin/android/telephony/satellite/SatelliteManager.html)` for accessing satellite functionality.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SEARCH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SEARCH_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)` for handling searches.  `[Configuration.UI_MODE_TYPE_WATCH](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html#UI_MODE_TYPE_WATCH:kotlin.Int)` does not support `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SECURITY_STATE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SECURITY_STATE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.SecurityStateManager](https://developer.android.com/reference/kotlin/android/os/SecurityStateManager.html)` for accessing the security state manager service.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SENSOR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SENSOR_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.SensorManager](https://developer.android.com/reference/kotlin/android/hardware/SensorManager.html)` for accessing sensors.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SERIAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SERIAL_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.serial.SerialManager](https://developer.android.com/reference/kotlin/android/hardware/serial/SerialManager.html)` for access to serial ports.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SHORTCUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SHORTCUT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.pm.ShortcutManager](https://developer.android.com/reference/kotlin/android/content/pm/ShortcutManager.html)` for accessing the launcher shortcut service.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[STATUS_BAR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#STATUS_BAR_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.StatusBarManager](https://developer.android.com/reference/kotlin/android/app/StatusBarManager)` for interacting with the status bar and quick settings.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[STORAGE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#STORAGE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.storage.StorageManager](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager.html)` for accessing system storage functions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[STORAGE_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#STORAGE_STATS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.usage.StorageStatsManager](https://developer.android.com/reference/kotlin/android/app/usage/StorageStatsManager)` for accessing system storage statistics.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[SYSTEM_HEALTH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SYSTEM_HEALTH_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.health.SystemHealthManager](https://developer.android.com/reference/kotlin/android/os/health/SystemHealthManager.html)` for accessing system health (battery, power, memory, etc) metrics.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TELECOM_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELECOM_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telecom.TelecomManager](https://developer.android.com/reference/kotlin/android/telecom/TelecomManager.html)` to manage telecom-related features of the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TELEPHONY_IMS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_IMS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve an `[android.telephony.ims.ImsManager](https://developer.android.com/reference/kotlin/android/telephony/ims/ImsManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TELEPHONY_PHONE_NUMBER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_PHONE_NUMBER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.PhoneNumberManager](https://developer.android.com/reference/kotlin/android/telephony/PhoneNumberManager.html)` for parsing phone numbers.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TELEPHONY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.TelephonyManager](https://developer.android.com/reference/kotlin/android/telephony/TelephonyManager.html)` for handling management the telephony features of the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TELEPHONY_SUBSCRIPTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_SUBSCRIPTION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.telephony.SubscriptionManager](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionManager.html)` for handling management the telephony subscriptions of the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TETHERING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TETHERING_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.TetheringManager](https://developer.android.com/reference/kotlin/android/net/TetheringManager.html)` for managing tethering functions.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TEXT_CLASSIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TEXT_CLASSIFICATION_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[TextClassificationManager](https://developer.android.com/reference/kotlin/android/view/textclassifier/TextClassificationManager.html)` for text classification services.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TEXT_SERVICES_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TEXT_SERVICES_MANAGER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.textservice.TextServicesManager](https://developer.android.com/reference/kotlin/android/view/textservice/TextServicesManager.html)` for accessing text services.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TIME_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TIME_MANAGER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[TimeManager](https://developer.android.com/reference/kotlin/android/app/time/TimeManager)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TV_AD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TV_AD_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.tv.ad.TvAdManager](https://developer.android.com/reference/kotlin/android/media/tv/ad/TvAdManager.html)` for interacting with TV client-side advertisement services on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TV_INPUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TV_INPUT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.tv.TvInputManager](https://developer.android.com/reference/kotlin/android/media/tv/TvInputManager.html)` for interacting with TV inputs on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[TV_INTERACTIVE_APP_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TV_INTERACTIVE_APP_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.media.tv.interactive.TvInteractiveAppManager](https://developer.android.com/reference/kotlin/android/media/tv/interactive/TvInteractiveAppManager.html)` for interacting with TV interactive applications on the device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[UI_MODE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#UI_MODE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.UiModeManager](https://developer.android.com/reference/kotlin/android/app/UiModeManager)` for controlling UI modes.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[USAGE_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USAGE_STATS_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.app.usage.UsageStatsManager](https://developer.android.com/reference/kotlin/android/app/usage/UsageStatsManager)` for querying device usage stats.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[USB_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USB_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.hardware.usb.UsbManager](https://developer.android.com/reference/kotlin/android/hardware/usb/UsbManager.html)` for access to USB devices (as a USB host) and for controlling this device's behavior as a USB device.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[USER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.UserManager](https://developer.android.com/reference/kotlin/android/os/UserManager.html)` for managing users on devices that support multiple users.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[VIBRATOR_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_MANAGER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.VibratorManager](https://developer.android.com/reference/kotlin/android/os/VibratorManager.html)` for accessing the device vibrators, interacting with individual ones and playing synchronized effects on multiple vibrators.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[VIBRATOR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.os.Vibrator](https://developer.android.com/reference/kotlin/android/os/Vibrator.html)` for interacting with the vibration hardware.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[VIRTUAL_DEVICE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIRTUAL_DEVICE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.companion.virtual.VirtualDeviceManager](https://developer.android.com/reference/kotlin/android/companion/virtual/VirtualDeviceManager.html)` for managing virtual devices. On devices without `[PackageManager.FEATURE_COMPANION_DEVICE_SETUP](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#FEATURE_COMPANION_DEVICE_SETUP:kotlin.String)` system feature the `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` will return `null`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[VPN_MANAGEMENT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VPN_MANAGEMENT_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.VpnManager](https://developer.android.com/reference/kotlin/android/net/VpnManager.html)` to manage profiles for the platform built-in VPN.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WALLPAPER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WALLPAPER_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a com.android.server.WallpaperService for accessing wallpapers.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WEB_APP_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WEB_APP_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.content.pm.webapp.WebAppManager](https://developer.android.com/reference/kotlin/android/content/pm/webapp/WebAppManager.html)`.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WIFI_AWARE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_AWARE_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.wifi.aware.WifiAwareManager](https://developer.android.com/reference/kotlin/android/net/wifi/aware/WifiAwareManager.html)` for handling management of Wi-Fi Aware.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WIFI_P2P_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_P2P_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.wifi.p2p.WifiP2pManager](https://developer.android.com/reference/kotlin/android/net/wifi/p2p/WifiP2pManager.html)` for handling management of Wi-Fi peer-to-peer connections.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WIFI_RTT_RANGING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_RTT_RANGING_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.wifi.rtt.WifiRttManager](https://developer.android.com/reference/kotlin/android/net/wifi/rtt/WifiRttManager.html)` for ranging devices with wifi.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WIFI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.net.wifi.WifiManager](https://developer.android.com/reference/kotlin/android/net/wifi/WifiManager.html)` for handling management of Wi-Fi access.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[WINDOW_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WINDOW_SERVICE:kotlin.String)` Use with `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` to retrieve a `[android.view.WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)` for accessing the system's window manager.  
  
From class `[ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html)` | `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_BACKGROUND](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_BACKGROUND:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process has gone on to the LRU list. This is a good opportunity to clean up resources that can efficiently and quickly be re-built if the user returns to the app.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_COMPLETE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_COMPLETE:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process is nearing the end of the background LRU list, and if more memory isn't found soon it will be killed.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_MODERATE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_MODERATE:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process is around the middle of the background LRU list; freeing memory can help the system keep other processes running later in the list for better overall performance.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_RUNNING_CRITICAL](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_CRITICAL:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process is not an expendable background process, but the device is running extremely low on memory and is about to not be able to keep any background processes running. Your running process should free up as many non-critical resources as it can to allow that memory to be used elsewhere. The next thing that will happen after this is `[onLowMemory()](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html#onLowMemory\(\))` called to report that nothing at all can be kept in the background, a situation that can start to notably impact the user.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_RUNNING_LOW](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_LOW:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process is not an expendable background process, but the device is running low on memory. Your running process should free up unneeded resources to allow that memory to be used elsewhere.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_RUNNING_MODERATE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_MODERATE:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process is not an expendable background process, but the device is running moderately low on memory. Your running process may want to release some unneeded resources for use elsewhere.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[TRIM_MEMORY_UI_HIDDEN](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_UI_HIDDEN:kotlin.Int)` Level for `[onTrimMemory(int)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#onTrimMemory\(kotlin.Int\))`: the process had been showing a user interface, and is no longer doing so. Large allocations with the UI should be released at this point to allow memory to be better managed.  
  
Public constructors  
---  
`Activity()`  
Public methods  
---  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `addContentView(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!, params: [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!)` Add an additional content view to the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `clearOverrideActivityTransition(overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Clears the animations which are set from #overrideActivityTransition.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `closeContextMenu()` Programmatically closes the most recently opened context menu, if showing.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `closeOptionsMenu()` Progammatically closes the options menu.  
open [PendingIntent](https://developer.android.com/reference/kotlin/android/app/PendingIntent)! |  `createPendingResult(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Create a new PendingIntent object which you can hand to others for them to use to send result data back to your #onActivityResult callback.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `dismissDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Dismiss a dialog that was previously shown via `showDialog(int)`.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `dismissKeyboardShortcutsHelper()` Dismiss the Keyboard Shortcuts screen.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchGenericMotionEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called to process generic motion events.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchKeyEvent(event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Called to process key events.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchKeyShortcutEvent(event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Called to process a key shortcut event.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchPopulateAccessibilityEvent(event: [AccessibilityEvent](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityEvent.html)!)` Called to process population of `[AccessibilityEvent](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityEvent.html)`s.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchTouchEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called to process touch screen events.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `dispatchTrackballEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called to process trackball events.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `dump(prefix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), fd: [FileDescriptor](https://developer.android.com/reference/kotlin/java/io/FileDescriptor.html)?, writer: [PrintWriter](https://developer.android.com/reference/kotlin/java/io/PrintWriter.html), args: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>?)` Print the Activity's state into the given stream.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `enterPictureInPictureMode()` Puts the activity in picture-in-picture mode if possible in the current system state.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `enterPictureInPictureMode(params: [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams))` Puts the activity in picture-in-picture mode if possible in the current system state.  
open T |  `findViewById(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Finds a view that was identified by the `android:id` XML attribute that was processed in #onCreate.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finish()` Call this when your activity is done and should be closed.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishActivity(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Force finish another activity that you had previously started with #startActivityForResult.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishActivityFromChild(child: Activity, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` This is called when a child activity of this one calls its finishActivity().  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishAffinity()` Finish this activity as well as all activities immediately below it in the current task that have the same affinity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishAfterTransition()` Reverses the Activity Scene entry Transition and triggers the calling Activity to reverse its exit Transition.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishAndRemoveTask()` Call this when your activity is done and should be closed and the task should be completely removed as a part of finishing the root activity of the task.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `finishFromChild(child: Activity!)` This is called when a child activity of this one calls its `finish` method.  
open [ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)? |  `getActionBar()` Retrieve a reference to this activity's ActionBar.  
[Application](https://developer.android.com/reference/kotlin/android/app/Application)! |  `getApplication()` Return the application that owns this activity.  
open [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)? |  `getCaller()` Returns the ComponentCaller instance of the app that started this activity.  
open [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)? |  `getCallingActivity()` Return the name of the activity that invoked this activity.  
open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)? |  `getCallingPackage()` Return the name of the package that invoked this activity.  
open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getChangingConfigurations()` If this activity is being destroyed because it can not handle a configuration parameter being changed (and thus its `onConfigurationChanged(Configuration)` method is _not_ being called), then you can use this method to discover the set of changes that have occurred while in the process of being destroyed.  
open [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)! |  `getComponentName()` Returns the complete component name of this activity.  
open [Scene](https://developer.android.com/reference/kotlin/android/transition/Scene.html)! |  `getContentScene()` Retrieve the `[Scene](https://developer.android.com/reference/kotlin/android/transition/Scene.html)` representing this window's current content.  
open [TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)! |  `getContentTransitionManager()` Retrieve the `[TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)` responsible for default transitions in this window.  
open [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller) |  `getCurrentCaller()` Returns the ComponentCaller instance of the app that re-launched this activity with a new intent via #onNewIntent or #onActivityResult.  
open [View](https://developer.android.com/reference/kotlin/android/view/View.html)? |  `getCurrentFocus()` Calls `[android.view.Window#getCurrentFocus](https://developer.android.com/reference/kotlin/android/view/Window.html#getCurrentFocus\(\))` on the Window of this Activity to return the currently focused view.  
open [FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)! |  `getFragmentManager()` Return the FragmentManager for interacting with fragments associated with this activity.  
open [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller) |  `getInitialCaller()` Returns the ComponentCaller instance of the app that initially launched this activity.  
open [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)! |  `getIntent()` Returns the intent that started this activity.  
open [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)? |  `getLastNonConfigurationInstance()` Retrieve the non-configuration instance data that was previously returned by `onRetainNonConfigurationInstance()`.  
open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)? |  `getLaunchedFromPackage()` Returns the package name of the app that initially launched this activity.  
open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getLaunchedFromUid()` Returns the uid of the app that initially launched this activity.  
open [LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html) |  `getLayoutInflater()` Convenience for calling `[android.view.Window#getLayoutInflater](https://developer.android.com/reference/kotlin/android/view/Window.html#getLayoutInflater\(\))`.  
open [LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)! |  `getLoaderManager()` Return the LoaderManager for this activity, creating it if needed.  
open [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) |  `getLocalClassName()` Returns class name for this activity with the package prefix removed.  
open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getMaxNumPictureInPictureActions()` Return the number of actions that will be displayed in the picture-in-picture UI when the user interacts with the activity currently in picture-in-picture mode.  
[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getMaxNumPictureInPictureOverlayActions()` Returns the maximum number of overlay actions that will be displayed in the picture-in-picture window.  
[MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)! |  `getMediaController()` Gets the controller which should be receiving media key and volume events while this activity is in the foreground.  
open [MenuInflater](https://developer.android.com/reference/kotlin/android/view/MenuInflater.html) |  `getMenuInflater()` Returns a `[MenuInflater](https://developer.android.com/reference/kotlin/android/view/MenuInflater.html)` with this context.  
open [OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html) |  `getOnBackInvokedDispatcher()` Returns the `[OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html)` instance associated with the window that this activity is attached to.  
Activity! |  `getParent()` Returns the parent `Activity` if this is a child `Activity` of an `[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)`.  
open [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)? |  `getParentActivityIntent()` Obtain an `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)` that will launch an explicit target activity specified by this activity's logical parent.  
open [SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)! |  `getPreferences(mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Retrieve a `[SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)` object for accessing preferences that are private to this activity.  
open [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)? |  `getReferrer()` Return information about who launched this activity.  
open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getRequestedOrientation()` Returns the current requested orientation of the activity, which is either the orientation requested in the app manifest or the last orientation given to `setRequestedOrientation(int)`.  
[SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)! |  `getSearchEvent()` During the onSearchRequested() callbacks, this function will return the `[SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)` that triggered the callback, if it exists.  
[SplashScreen](https://developer.android.com/reference/kotlin/android/window/SplashScreen.html) |  `getSplashScreen()` Get the interface that activity use to talk to the splash screen.  
open [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)! |  `getSystemService(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Return the handle to a system-level service by name.  
open [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getTaskId()` Return the identifier of the task this activity is in.  
[CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)! |  `getTitle()`  
[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getTitleColor()`  
open [VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)! |  `getVoiceInteractor()` Retrieve the active `[VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)` that the user is going through to interact with this activity.  
[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) |  `getVolumeControlStream()` Gets the suggested audio stream whose volume should be changed by the hardware volume controls.  
open [Window](https://developer.android.com/reference/kotlin/android/view/Window.html)! |  `getWindow()` Retrieve the current `[android.view.Window](https://developer.android.com/reference/kotlin/android/view/Window.html)` for the activity.  
open [WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)! |  `getWindowManager()` Retrieve the window manager for showing custom windows.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `hasWindowFocus()` Returns true if this activity's _main_ window currently has window focus.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `invalidateOptionsMenu()` Declare that the options menu has changed, so should be recreated.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isActivityTransitionRunning()` Returns whether there are any activity transitions currently running on this activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isChangingConfigurations()` Check to see whether this activity is in the process of being destroyed in order to be recreated with a new configuration.  
[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isChild()` Whether this is a child `Activity` of an `[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)`.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isDestroyed()` Returns true if the final `onDestroy()` call has been made on the Activity, so this instance is now dead.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isFinishing()` Check to see whether this activity is in the process of finishing, either because you called `finish` on it or someone else has requested that it finished.  
[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isHandoffEnabled()` Returns if Handoff has been enabled for this Activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isImmersive()` Bit indicating that this activity is "immersive" and should not be interrupted by notifications if possible.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isInMultiWindowMode()` Returns true if the activity is currently in multi-window mode.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isInPictureInPictureMode()` Returns true if the activity is currently in picture-in-picture mode.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isLaunchedFromBubble()` Indicates whether this activity is launched from a bubble.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isLocalVoiceInteractionSupported()` Queries whether the currently enabled voice interaction service supports returning a voice interactor for use by the activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isTaskRoot()` Return whether this activity is the root of a task.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isVoiceInteraction()` Check whether this activity is running as part of a voice interaction with the user.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `isVoiceInteractionRoot()` Like `isVoiceInteraction`, but only returns `true` if this is also the root of a voice interaction.  
[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)! |  `managedQuery(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, projection: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!, selection: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, selectionArgs: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!, sortOrder: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Wrapper around `[ContentResolver.query(android.net.Uri,String[],String,String[],String)](https://developer.android.com/reference/kotlin/android/content/ContentResolver.html#query\(android.net.Uri,%20kotlin.Array,%20kotlin.String,%20kotlin.Array,%20kotlin.String\))` that gives the resulting `[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)` to call `startManagingCursor` so that the activity will manage its lifecycle for you.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `moveTaskToBack(nonRoot: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Move the task containing this activity to the back of the activity stack.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `navigateUpTo(upIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Navigate from this activity to the activity specified by upIntent, finishing this activity in the process.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `navigateUpToFromChild(child: Activity!, upIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` This is called when a child activity of this one calls its `navigateUpTo` method.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onActionModeFinished(mode: [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!)` Notifies the activity that an action mode has finished.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onActionModeStarted(mode: [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!)` Notifies the Activity that an action mode has been started.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onActivityReenter(resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Called when an activity you launched with an activity transition exposes this Activity through a returning activity transition, giving you the resultCode and any additional data from it.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onActivityResult(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, caller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller))` Same as `onActivityResult(int,int,Intent)`, but with an extra parameter for the ComponentCaller instance associated with the app that sent the result.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onAttachFragment(fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment)!)` Called when a Fragment is being attached to this activity, immediately after the call to its android.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onAttachedToWindow()` Called when the main window associated with the activity has been attached to the window manager.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onBackPressed()` Called when the activity has detected the user's press of the back key.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onConfigurationChanged(newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html))` Called by the system when the device configuration changes while your activity is running.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onContentChanged()` This hook is called whenever the content view of the screen changes (due to a call to `[Window.setContentView](https://developer.android.com/reference/kotlin/android/view/Window.html#setContentView\(android.view.View,%20android.view.ViewGroup.LayoutParams\))` or `[Window.addContentView](https://developer.android.com/reference/kotlin/android/view/Window.html#addContentView\(android.view.View,%20android.view.ViewGroup.LayoutParams\))`).  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onContextItemSelected(item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html))` This hook is called whenever an item in a context menu is selected.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onContextMenuClosed(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html))` This hook is called whenever the context menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?)` Same as `onCreate(android.os.Bundle)` but called for those activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onCreateContextMenu(menu: [ContextMenu](https://developer.android.com/reference/kotlin/android/view/ContextMenu.html)!, v: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!, menuInfo: [ContextMenu.ContextMenuInfo](https://developer.android.com/reference/kotlin/android/view/ContextMenu.ContextMenuInfo.html)!)` Called when a context menu for the `view` is about to be shown.  
open [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)? |  `onCreateDescription()` Generate a new description for this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onCreateNavigateUpTaskStack(builder: [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!)` Define the synthetic task stack that will be generated during Up navigation from a different task.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onCreateOptionsMenu(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!)` Initialize the contents of the Activity's standard options menu.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onCreatePanelMenu(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html))` Default implementation of `[android.view.Window.Callback#onCreatePanelMenu](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onCreatePanelMenu\(kotlin.Int,%20android.view.Menu\))` for activities.  
open [View](https://developer.android.com/reference/kotlin/android/view/View.html)? |  `onCreatePanelView(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Default implementation of `[android.view.Window.Callback#onCreatePanelView](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onCreatePanelView\(kotlin.Int\))` for activities.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onCreateThumbnail(outBitmap: [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)!, canvas: [Canvas](https://developer.android.com/reference/kotlin/android/graphics/Canvas.html)!)`  
open [View](https://developer.android.com/reference/kotlin/android/view/View.html)? |  `onCreateView(parent: [View](https://developer.android.com/reference/kotlin/android/view/View.html)?, name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html), attrs: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html))` Standard implementation of `[android.view.LayoutInflater.Factory2.onCreateView(View,String,Context,AttributeSet)](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.Factory2.html#onCreateView\(android.view.View,%20kotlin.String,%20android.content.Context,%20android.util.AttributeSet\))` used when inflating with the LayoutInflater returned by #getSystemService.  
open [View](https://developer.android.com/reference/kotlin/android/view/View.html)? |  `onCreateView(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html), attrs: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html))` Standard implementation of `[android.view.LayoutInflater.Factory#onCreateView](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.Factory.html#onCreateView\(kotlin.String,%20android.content.Context,%20android.util.AttributeSet\))` used when inflating with the LayoutInflater returned by #getSystemService.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onDetachedFromWindow()` Called when the main window associated with the activity has been detached from the window manager.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onEnterAnimationComplete()` Activities cannot draw during the period that their windows are animating in.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onGenericMotionEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called when a generic motion event was not handled by any of the views inside of the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onGetDirectActions(cancellationSignal: [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html), callback: [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[DirectAction](https://developer.android.com/reference/kotlin/android/app/DirectAction)!>!>)` Returns the list of direct actions supported by the app.  
open [HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)? |  `onHandoffActivityDataRequested(requestInfo: [HandoffActivityDataRequestInfo](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo))` Retrieves `[HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)` representing this activity, allowing it to be recreated on another device owned by the user.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onKeyDown(keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Called when a key was pressed down and not handled by any of the views inside of the activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onKeyLongPress(keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Default implementation of `[KeyEvent.Callback.onKeyLongPress()](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html#onKeyLongPress\(kotlin.Int,%20android.view.KeyEvent\))`: always returns false (doesn't handle the event).  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onKeyMultiple(keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), repeatCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Default implementation of `[KeyEvent.Callback.onKeyMultiple()](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html#onKeyMultiple\(kotlin.Int,%20kotlin.Int,%20android.view.KeyEvent\))`: always returns false (doesn't handle the event).  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onKeyShortcut(keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Called when a key shortcut event is not handled by any of the views in the Activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onKeyUp(keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!)` Called when a key was released and not handled by any of the views inside of the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onLocalVoiceInteractionStarted()` Callback to indicate that `startLocalVoiceInteraction(Bundle)` has resulted in a voice interaction session being started.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onLocalVoiceInteractionStopped()` Callback to indicate that the local voice interaction has stopped either because it was requested through a call to `stopLocalVoiceInteraction()` or because it was canceled by the user.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onLowMemory()` This is called when the overall system is running low on memory, and actively running processes should trim their memory usage.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onMenuItemSelected(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html))` Default implementation of `[android.view.Window.Callback#onMenuItemSelected](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onMenuItemSelected\(kotlin.Int,%20android.view.MenuItem\))` for activities.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onMenuOpened(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html))` Called when a panel's menu is opened by the user.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onMultiWindowModeChanged(isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called by the system when the activity changes from fullscreen mode to multi-window mode and visa-versa.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onMultiWindowModeChanged(isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html), newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!)` Called by the system when the activity changes from fullscreen mode to multi-window mode and visa-versa.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onNavigateUp()` This method is called whenever the user chooses to navigate Up within your application's activity hierarchy from the action bar.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onNavigateUpFromChild(child: Activity!)` This is called when a child activity of this one attempts to navigate up.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onNewIntent(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), caller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller))` Same as `onNewIntent(Intent)`, but with an extra parameter for the ComponentCaller instance associated with the app that sent the intent.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onOptionsItemSelected(item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html))` This hook is called whenever an item in your options menu is selected.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onOptionsMenuClosed(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!)` This hook is called whenever the options menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPanelClosed(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html))` Default implementation of `[android.view.Window.Callback.onPanelClosed(int,Menu)](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onPanelClosed\(kotlin.Int,%20android.view.Menu\))` for activities.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPerformDirectAction(actionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), arguments: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html), cancellationSignal: [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html), resultListener: [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!>)` This is called to perform an action previously defined by the app.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPictureInPictureModeChanged(isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called by the system when the activity changes to and from picture-in-picture mode.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPictureInPictureModeChanged(isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html), newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!)` Called by the system when the activity changes to and from picture-in-picture mode.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onPictureInPictureRequested()` This method is called by the system in various cases where picture in picture mode should be entered if supported.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPictureInPictureUiStateChanged(pipState: [PictureInPictureUiState](https://developer.android.com/reference/kotlin/android/app/PictureInPictureUiState))` Called by the system when the activity is in PiP and has state changes.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPostCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?)` This is the same as `onPostCreate(Bundle)` but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPrepareNavigateUpTaskStack(builder: [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!)` Prepare the synthetic task stack that will be generated during Up navigation from a different task.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onPrepareOptionsMenu(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!)` Prepare the Screen's standard options menu to be displayed.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onPreparePanel(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)?, menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html))` Default implementation of `[android.view.Window.Callback#onPreparePanel](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onPreparePanel\(kotlin.Int,%20android.view.View,%20android.view.Menu\))` for activities.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onProvideAssistContent(outContent: [AssistContent](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent)!)` This is called when the user is requesting an assist, to provide references to content related to the current activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onProvideAssistData(data: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` This is called when the user is requesting an assist, to build a full `[Intent.ACTION_ASSIST](https://developer.android.com/reference/kotlin/android/content/Intent.html#ACTION_ASSIST:kotlin.String)` Intent with all of the context of the current application.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onProvideKeyboardShortcuts(data: [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[KeyboardShortcutGroup](https://developer.android.com/reference/kotlin/android/view/KeyboardShortcutGroup.html)!>!, menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)?, deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Called when Keyboard Shortcuts are requested for the current window.  
open [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)! |  `onProvideReferrer()` Override to generate the desired referrer for the content currently being shown by the app.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onRequestPermissionsResult(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>, grantResults: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html))` Callback for the result from requesting permissions.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onRequestPermissionsResult(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>, grantResults: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html), deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Callback for the result from requesting permissions.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onRestoreInstanceState(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?)` This is the same as `onRestoreInstanceState(Bundle)` but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.  
open [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)! |  `onRetainNonConfigurationInstance()` Called by the system, as part of destroying an activity due to a configuration change, when it is known that a new instance will immediately be created for the new configuration.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onSaveInstanceState(outState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html), outPersistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html))` This is the same as #onSaveInstanceState but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onSearchRequested()`  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onSearchRequested(searchEvent: [SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)?)` This hook is called when the user signals the desire to start a search.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onStateNotSaved()` Called when an `onResume` is coming up, prior to other pre-resume callbacks such as #onNewIntent and #onActivityResult.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onTopResumedActivityChanged(isTopResumedActivity: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called when activity gets or loses the top resumed position in the system.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onTouchEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called when a touch screen event was not handled by any of the views inside of the activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `onTrackballEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!)` Called when the trackball was moved and not handled by any of the views inside of the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onTrimMemory(level: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onUserInteraction()` Called whenever a key, touch, or trackball event is dispatched to the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onVisibleBehindCanceled()` Called when a translucent activity over this activity is becoming opaque or another activity is being launched.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onWindowAttributesChanged(params: [WindowManager.LayoutParams](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html)!)` This is called whenever the current window attributes change.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onWindowFocusChanged(hasFocus: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called when the current `[Window](https://developer.android.com/reference/kotlin/android/view/Window.html)` of the activity gains or loses focus.  
open [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)? |  `onWindowStartingActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!)` Give the Activity a chance to control the UI for an action mode requested by the system.  
open [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)? |  `onWindowStartingActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!, type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Called when an action mode is being started for this window.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `openContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!)` Programmatically opens the context menu for a particular `view`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `openOptionsMenu()` Programmatically opens the options menu.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `overrideActivityTransition(overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Customizes the animation for activity transitions.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `overrideActivityTransition(overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), backgroundColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Customizes the animation and background color for activity transitions.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `overridePendingTransition(enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Call immediately after one of the flavors of #startActivity(android.content.Intent) or   
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `overridePendingTransition(enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), backgroundColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Call immediately after one of the flavors of #startActivity(android.content.Intent) or   
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `postponeEnterTransition()` Postpone the entering activity transition when Activity was started with `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `recreate()` Cause this Activity to be recreated with a new instance.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `registerActivityLifecycleCallbacks(callback: [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks))` Register an `[Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)` instance that receives lifecycle callbacks for only this Activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `registerComponentCallbacks(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!)` Add a new `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to the base application of the Context, which will be called at the same times as the ComponentCallbacks methods of activities and other components are called.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `registerForContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!)` Registers a context menu to be shown for the given view (multiple views can show the context menu).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `registerScreenCaptureCallback(executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), callback: [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback))` Registers a screen capture callback for this activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `releaseInstance()` Ask that the local app instance of this activity be released to free up its memory.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `removeDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Removes any internal references to a dialog managed by this Activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `reportFullyDrawn()` Report to the system that your app is now fully drawn, for diagnostic and optimization purposes.  
open [DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)! |  `requestDragAndDropPermissions(event: [DragEvent](https://developer.android.com/reference/kotlin/android/view/DragEvent.html)!)` Create `[DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)` object bound to this activity and controlling the access permissions for content URIs associated with the `[DragEvent](https://developer.android.com/reference/kotlin/android/view/DragEvent.html)`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `requestFullscreenMode(request: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), approvalCallback: [OutcomeReceiver](https://developer.android.com/reference/kotlin/android/os/OutcomeReceiver.html)<[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)!, [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!>?)` Request to put the activity into fullscreen.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `requestOpenInBrowserEducation()` Requests to show the “Open in browser” education.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `requestPermissions(permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Requests permissions to be granted to this application.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `requestPermissions(permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Requests permissions to be granted to this application.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `requestShowKeyboardShortcuts()` Request the Keyboard Shortcuts screen to show up.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `requestVisibleBehind(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Activities that want to remain visible behind a translucent activity above them must call this method anytime between the start of `onResume()` and the return from `onPause()`.  
[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `requestWindowFeature(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Enable extended window features.  
T |  `requireViewById(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Finds a view that was identified by the `android:id` XML attribute that was processed in #onCreate, or throws an IllegalArgumentException if the ID is invalid, or there is no matching view in the hierarchy.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `runOnUiThread(action: [Runnable](https://developer.android.com/reference/kotlin/java/lang/Runnable.html)!)` Runs the specified action on the UI thread.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setActionBar(toolbar: [Toolbar](https://developer.android.com/reference/kotlin/android/widget/Toolbar.html)?)` Set a `[Toolbar](https://developer.android.com/reference/kotlin/android/widget/Toolbar.html)` to act as the `[ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)` for this Activity window.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setAllowCrossUidActivitySwitchFromBelow(allowed: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies whether the activities below this one in the task can also start other activities or finish the task.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setContentTransitionManager(tm: [TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)!)` Set the `[TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)` to use for default transitions in this window.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setContentView(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!)` Set the activity content to an explicit view.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setContentView(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!, params: [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!)` Set the activity content to an explicit view.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setContentView(layoutResID: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Set the activity content from a layout resource.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setDefaultKeyMode(mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Select the default key handling for this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setEnterSharedElementCallback(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!)` When `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.view.View,String)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.view.View,%20kotlin.String\))` was used to start an Activity, callback will be called to handle shared elements on the _launched_ Activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setExitSharedElementCallback(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!)` When `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.view.View,String)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.view.View,%20kotlin.String\))` was used to start an Activity, callback will be called to handle shared elements on the _launching_ Activity.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setFeatureDrawable(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), drawable: [Drawable](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable.html)!)` Convenience for calling `[android.view.Window.setFeatureDrawable(int,Drawable)](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawable\(kotlin.Int,%20android.graphics.drawable.Drawable\))`.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setFeatureDrawableAlpha(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), alpha: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Convenience for calling `[android.view.Window#setFeatureDrawableAlpha](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableAlpha\(kotlin.Int,%20kotlin.Int\))`.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setFeatureDrawableResource(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), resId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Convenience for calling `[android.view.Window#setFeatureDrawableResource](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableResource\(kotlin.Int,%20kotlin.Int\))`.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setFeatureDrawableUri(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!)` Convenience for calling `[android.view.Window#setFeatureDrawableUri](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableUri\(kotlin.Int,%20android.net.Uri\))`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setFinishOnTouchOutside(finish: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Sets whether this activity is finished when touched outside its window's bounds.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setHandoffEnabled(handoffEnabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html), handoffActivityParams: [HandoffActivityParams](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams)?)` Sets if Handoff is enabled for this Activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setImmersive(i: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Adjust the current immersive mode setting.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setInheritShowWhenLocked(inheritShowWhenLocked: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies whether this `Activity` should be shown on top of the lock screen whenever the lockscreen is up and this activity has another activity behind it with the showWhenLock attribute set.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setIntent(newIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Changes the intent returned by `getIntent`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setIntent(newIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, newCaller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)?)` Changes the intent returned by `getIntent`, and ComponentCaller returned by `getCaller`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setLocusContext(locusId: [LocusId](https://developer.android.com/reference/kotlin/android/content/LocusId.html)?, bundle: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Sets the `[android.content.LocusId](https://developer.android.com/reference/kotlin/android/content/LocusId.html)` for this activity.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setMediaController(controller: [MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)!)` Sets a `[MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)` to send media keys and volume changes to.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setPictureInPictureParams(params: [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams))` Updates the properties of the picture-in-picture activity, or sets it to be used later when `enterPictureInPictureMode()` is called.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setProgress(progress: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Sets the progress for the progress bars in the title.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setProgressBarIndeterminate(indeterminate: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Sets whether the horizontal progress bar in the title should be indeterminate (the circular is always indeterminate).  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setProgressBarIndeterminateVisibility(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Sets the visibility of the indeterminate progress bar in the title.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setProgressBarVisibility(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Sets the visibility of the progress bar in the title.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setRecentsScreenshotEnabled(enabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` If set to false, this indicates to the system that it should never take a screenshot of the activity to be used as a representation in recents screen.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setRequestedOrientation(requestedOrientation: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Change the desired orientation of this activity.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setResult(resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Call this to set the result that your activity will return to its caller.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setResult(resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Call this to set the result that your activity will return to its caller.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setSecondaryProgress(secondaryProgress: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Sets the secondary progress for the progress bar in the title.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setShouldDockBigOverlays(shouldDockBigOverlays: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies a preference to dock big overlays like the expanded picture-in-picture on TV (see `[PictureInPictureParams.Builder.setExpandedAspectRatio](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams.Builder#setExpandedAspectRatio\(android.util.Rational\))`).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setShowWhenLocked(showWhenLocked: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies whether an `Activity` should be shown on top of the lock screen whenever the lockscreen is up and the activity is resumed.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTaskDescription(taskDescription: [ActivityManager.TaskDescription](https://developer.android.com/reference/kotlin/android/app/ActivityManager.TaskDescription)!)` Sets information describing the task with this activity for presentation inside the Recents System UI.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTheme(resid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Set the base theme for this context.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTitle(titleId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Change the title associated with this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTitle(title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!)` Change the title associated with this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTitleColor(textColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Change the color of the title associated with this activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `setTranslucent(translucent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Convert an activity, which particularly with `[android.R.attr#windowIsTranslucent](https://developer.android.com/reference/kotlin/android/R.attr.html#windowIsTranslucent:kotlin.Int)` or `[android.R.attr#windowIsFloating](https://developer.android.com/reference/kotlin/android/R.attr.html#windowIsFloating:kotlin.Int)` attribute, to a fullscreen opaque activity, or convert it from opaque back to translucent.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setTurnScreenOn(turnScreenOn: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Specifies whether the screen should be turned on when the `Activity` is resumed.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setVisible(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Control whether this activity's main window is visible.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setVolumeControlStream(streamType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Suggests an audio stream whose volume should be changed by the hardware volume controls.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `setVrModeEnabled(enabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html), requestedComponent: [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html))` Enable or disable virtual reality (VR) mode for this Activity.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `shouldDockBigOverlays()` Returns whether big overlays should be docked next to the activity as set by `setShouldDockBigOverlays`.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `shouldShowRequestPermissionRationale(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Gets whether you should show UI with rationale before requesting a permission.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `shouldShowRequestPermissionRationale(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Gets whether you should show UI with rationale before requesting a permission.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `shouldUpRecreateTask(targetIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Returns true if the app should recreate the task when navigating 'up' from this activity by using targetIntent.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `showAssist(args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` Ask to have the current assistant shown to the user.  
[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `showDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Simple version of `showDialog(int,Bundle)` that does not take any arguments.  
[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `showDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` Show a dialog managed by this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `showLockTaskEscapeMessage()` Shows the user the system defined message for telling the user how to exit lock task mode.  
open [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)? |  `startActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!)` Start an action mode of the default type `[ActionMode.TYPE_PRIMARY](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_PRIMARY:kotlin.Int)`.  
open [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)? |  `startActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!, type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Start an action mode of the given type.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivities(intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!)` Same as #startActivities(android.content.Intent[],android.os.Bundle) with no options specified.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivities(intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Launch a new activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Same as #startActivity(android.content.Intent,android.os.Bundle) with no options specified.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Launch a new activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityForResult(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startActivityForResult(Intent,int,Bundle)` with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityForResult(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Launch an activity for which you would like a result when it finished.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityFromChild(child: Activity, intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startActivityFromChild(Activity,Intent,int,Bundle)` with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityFromChild(child: Activity, intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` This is called when a child activity of this one calls its #startActivity or #startActivityForResult method.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityFromFragment(fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment), intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startActivityFromFragment(Fragment,Intent,int,Bundle)` with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startActivityFromFragment(fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment), intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` This is called when a Fragment in this activity calls its android.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `startActivityIfNeeded(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startActivityIfNeeded(Intent,int,Bundle)` with no options.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `startActivityIfNeeded(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` A special variation to launch an activity only if a new activity instance is needed to handle the given Intent.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSender(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling #startIntentSender(android.content.IntentSender,android.content.Intent,int,int,int,android.os.Bundle) with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSender(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Like #startActivity(android.content.Intent,android.os.Bundle), but taking a IntentSender to start; see   
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSenderForResult(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startIntentSenderForResult(IntentSender,int,Intent,int,int,int,Bundle)` with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSenderForResult(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Like `startActivityForResult(Intent,int)`, but allowing you to use a IntentSender to describe the activity to be started.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSenderFromChild(child: Activity!, intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as calling `startIntentSenderFromChild(Activity,IntentSender,int,Intent,int,int,int,Bundle)` with no options.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startIntentSenderFromChild(child: Activity!, intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Like `startActivityFromChild(Activity,Intent,int)`, but taking a IntentSender; see `startIntentSenderForResult(IntentSender,int,Intent,int,int,int)` for more information.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startLocalVoiceInteraction(privateOptions: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` Starts a local voice interaction session.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startLockTask()` Request to put this activity in a mode where the user is locked to a restricted set of applications.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startManagingCursor(c: [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!)` This method allows the activity to take care of managing the given `[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)`'s lifecycle for you based on the activity's lifecycle.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `startNextMatchingActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html))` Same as calling `startNextMatchingActivity(Intent,Bundle)` with no options.  
open [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) |  `startNextMatchingActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Special version of starting an activity, for use when you are replacing other activity components.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startPostponedEnterTransition()` Begin postponed transitions after `postponeEnterTransition()` was called.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `startSearch(initialQuery: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, selectInitialQuery: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html), appSearchData: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, globalSearch: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` This hook is called to launch the search UI.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `stopLocalVoiceInteraction()` Request to terminate the current voice interaction that was previously started using `startLocalVoiceInteraction(Bundle)`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `stopLockTask()` Stop the current task from being locked.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `stopManagingCursor(c: [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!)` Given a Cursor that was previously given to `startManagingCursor`, stop the activity's management of that cursor.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `takeKeyEvents(get: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Request that key events come to this activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `triggerSearch(query: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, appSearchData: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Similar to `startSearch`, but actually fires off the search query after invoking the search dialog.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `unregisterActivityLifecycleCallbacks(callback: [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks))` Unregister an `[Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)` previously registered with `registerActivityLifecycleCallbacks`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `unregisterComponentCallbacks(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!)` Remove a `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` object that was previously registered with `[registerComponentCallbacks(ComponentCallbacks)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerComponentCallbacks\(android.content.ComponentCallbacks\))`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `unregisterForContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!)` Prevents a context menu to be shown for the given view.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `unregisterScreenCaptureCallback(callback: [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback))` Unregisters a screen capture callback for this surface.  
Protected methods  
---  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `attachBaseContext(newBase: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!)` Set the base context for this ContextWrapper.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onActivityResult(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Called when an activity you launched exits, giving you the requestCode you started it with, the resultCode it returned, and any additional data from it.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onApplyThemeResource(theme: [Resources.Theme](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html)!, resid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), first: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called by #setTheme and #getTheme to apply a theme resource to the current Theme object.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onChildTitleChanged(childActivity: Activity!, title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!)`  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Called when the activity is starting.  
open [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)! |  `onCreateDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))`  
open [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)? |  `onCreateDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` Callback for creating dialogs that are managed (saved and restored) for you by the activity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onDestroy()` Perform any final cleanup before an activity is destroyed.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onNewIntent(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` This is called for activities that set launchMode to "singleTop" in their package, or if a client used the `[Intent.FLAG_ACTIVITY_SINGLE_TOP](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_SINGLE_TOP:kotlin.Int)` flag when calling #startActivity.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPause()` Called as part of the activity lifecycle when the user no longer actively interacts with the activity, but it is still visible on screen.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPostCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Called when activity start-up is complete (after `onStart` and #onRestoreInstanceState have been called).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPostResume()` Called when activity resume is complete (after `onResume` has been called).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPrepareDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), dialog: [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!)`  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onPrepareDialog(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), dialog: [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!, args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!)` Provides an opportunity to prepare a managed dialog before it is being shown.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onRestart()` Called after `onStop` when the current activity is being re-displayed to the user (the user has navigated back to it).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onRestoreInstanceState(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html))` This method is called after `onStart` when the activity is being re-initialized from a previously saved state, given here in savedInstanceState.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onResume()` Called after #onRestoreInstanceState, `onRestart`, or `onPause`.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onSaveInstanceState(outState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html))` Called to retrieve per-instance state from an activity before being killed so that the state can be restored in #onCreate or #onRestoreInstanceState (the `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)` populated by this method will be passed to both).  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onStart()` Called after #onCreate — or after `onRestart` when the activity had been stopped, but is now again being displayed to the user.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onStop()` Called when you are no longer visible to the user.  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onTitleChanged(title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!, color: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))`  
open [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) |  `onUserLeaveHint()` Called as part of the activity lifecycle when an activity is about to go into the background as the result of user choice.  
Inherited functions  
---  
From class `[ContextThemeWrapper](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html)` | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[applyOverrideConfiguration](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html#applyOverrideConfiguration\(android.content.res.Configuration\))(overrideConfiguration: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!)` Call to set an "override configuration" on this context -- this is a configuration that replies one or more values of the standard configuration that is applied to the context. See `[Context.createConfigurationContext(Configuration)](https://developer.android.com/reference/kotlin/android/content/Context.html#createConfigurationContext\(android.content.res.Configuration\))` for more information.  This method can only be called once, and must be called before any calls to #getResources() or #getAssets() are made.  
---|---  
`[AssetManager](https://developer.android.com/reference/kotlin/android/content/res/AssetManager.html)!` | `[getAssets](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html#getAssets\(\))()` Returns an AssetManager instance for the application's package.  **Note:** Implementations of this method should return an AssetManager instance that is consistent with the Resources instance returned by `[getResources()](https://developer.android.com/reference/kotlin/android/content/Context.html#getResources\(\))`. For example, they should share the same `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` object.  
`[Resources](https://developer.android.com/reference/kotlin/android/content/res/Resources.html)!` | `[getResources](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html#getResources\(\))()` Returns a Resources instance for the application's package.  **Note:** Implementations of this method should return a Resources instance that is consistent with the AssetManager instance returned by `[getAssets()](https://developer.android.com/reference/kotlin/android/content/Context.html#getAssets\(\))`. For example, they should share the same `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` object.  
`[Resources.Theme](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html)!` | `[getTheme](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html#getTheme\(\))()` Return the Theme object associated with this Context.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[setTheme](https://developer.android.com/reference/kotlin/android/view/ContextThemeWrapper.html#setTheme\(android.content.res.Resources.Theme\))(theme: [Resources.Theme](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html)?)` Set the configure the current theme. If null is provided then the default Theme is returned on the next call to #getTheme()  
  
From class `[ContextWrapper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html)` | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindIsolatedService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindIsolatedService\(android.content.Intent,%20kotlin.Int,%20kotlin.String,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), instanceName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html))` Variation of #bindService that, in the specific case of isolated services, allows the caller to generate multiple instances of a service from a single component declaration. In other words, you can use this to bind to a service that has specified `[android.R.attr#isolatedProcess](https://developer.android.com/reference/kotlin/android/R.attr.html#isolatedProcess:kotlin.Int)` and, in addition to the existing behavior of running in an isolated process, you can also through the arguments here have the system bring up multiple concurrent processes hosting their own instances of that service. The instanceName you provide here identifies the different instances, and you can use `[updateServiceGroup(ServiceConnection,int,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#updateServiceGroup\(android.content.ServiceConnection,%20kotlin.Int,%20kotlin.Int\))` to tell the system how it should manage each of these instances.  
---|---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindService\(android.content.Intent,%20android.content.Context.BindServiceFlags,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), flags: [Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html), executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html))` See `[bindService(Intent,int,Executor,ServiceConnection)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindService\(android.content.Intent,%20kotlin.Int,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))` Call `[BindServiceFlags.of(long)](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html#of\(kotlin.Long\))` to obtain a BindServiceFlags object.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindService\(android.content.Intent,%20android.content.ServiceConnection,%20android.content.Context.BindServiceFlags\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), flags: [Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html))` See `[bindService(Intent,ServiceConnection,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindService\(android.content.Intent,%20android.content.ServiceConnection,%20kotlin.Int\))` Call `[BindServiceFlags.of(long)](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html#of\(kotlin.Long\))` to obtain a BindServiceFlags object.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindService\(android.content.Intent,%20android.content.ServiceConnection,%20kotlin.Int\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Connects to an application service, creating it if needed. This defines a dependency between your application and the service. The given conn will receive the service object when it is created and be told if it dies and restarts. The service will be considered required by the system only for as long as the calling context exists. For example, if this Context is an Activity that is stopped, the service will not be required to continue running until the Activity is resumed.  If the service does not support binding, it may return `null` from its `[onBind()](https://developer.android.com/reference/kotlin/android/app/Service#onBind\(android.content.Intent\))` method. If it does, then the ServiceConnection's `[onNullBinding()](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html#onNullBinding\(android.content.ComponentName\))` method will be invoked instead of `[onServiceConnected()](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html#onServiceConnected\(android.content.ComponentName,%20android.os.IBinder\))`.  **Note:** This method _cannot_ be called from a `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` component. A pattern you can use to communicate from a BroadcastReceiver to a Service is to call `[startService](https://developer.android.com/reference/kotlin/android/content/Context.html#startService\(android.content.Intent\))` with the arguments containing the command to be sent, with the service calling its `[android.app.Service#stopSelf(int)](https://developer.android.com/reference/kotlin/android/app/Service#stopSelf\(kotlin.Int\))` method when done executing that command. See the API demo App/Service/Service Start Arguments Controller for an illustration of this. It is okay, however, to use this method from a BroadcastReceiver that has been registered with #registerReceiver, since the lifetime of this BroadcastReceiver is tied to another object (the one that registered it). This method only accepts a int type flag, to pass in a long type flag, call `[bindService(Intent,ServiceConnection,BindServiceFlags)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindService\(android.content.Intent,%20android.content.ServiceConnection,%20android.content.Context.BindServiceFlags\))` instead.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindService\(android.content.Intent,%20kotlin.Int,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html))` Same as `[bindService(Intent, ServiceConnection, int)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindService\(android.content.Intent,%20android.content.ServiceConnection,%20kotlin.Int\))` with executor to control ServiceConnection callbacks.  This method only accepts a 32 bits flag, to pass in a 64 bits flag, call `[bindService(Intent,BindServiceFlags,Executor,ServiceConnection)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindService\(android.content.Intent,%20android.content.Context.BindServiceFlags,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))` instead.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindServiceAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindServiceAsUser\(android.content.Intent,%20android.content.ServiceConnection,%20android.content.Context.BindServiceFlags,%20android.os.UserHandle\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), flags: [Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html), user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html))` See `[bindServiceAsUser(Intent,ServiceConnection,int,UserHandle)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindServiceAsUser\(android.content.Intent,%20android.content.ServiceConnection,%20kotlin.Int,%20android.os.UserHandle\))` Call `[BindServiceFlags.of(long)](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html#of\(kotlin.Long\))` to obtain a BindServiceFlags object.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindServiceAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#bindServiceAsUser\(android.content.Intent,%20android.content.ServiceConnection,%20kotlin.Int,%20android.os.UserHandle\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html))` Binds to a service in the given `user` in the same manner as #bindService.  Requires that one of the following conditions are met: 

  * caller has `android.Manifest.permission.INTERACT_ACROSS_USERS_FULL`
  * caller has `android.Manifest.permission.INTERACT_ACROSS_USERS` and is the same package as the `service` (determined by its component's package) and the Android version is at least `[android.os.Build.VERSION_CODES#TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)`
  * caller has `android.Manifest.permission.INTERACT_ACROSS_USERS` and is in same profile group as the given `user`
  * caller has `android.Manifest.permission.INTERACT_ACROSS_PROFILES` and is in same profile group as the given `user` and is the same package as the `service`

  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkCallingOrSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingOrSelfPermission\(kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Determine whether the calling process of an IPC _or you_ have been granted a particular permission. This is the same as `[checkCallingPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#checkCallingPermission\(kotlin.String\))`, except it grants your own permissions if you are not currently processing an IPC. Use with care!  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkCallingOrSelfUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingOrSelfUriPermission\(android.net.Uri,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether the calling process of an IPC _or you_ has been granted permission to access a specific URI. This is the same as `[checkCallingUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#checkCallingUriPermission\(android.net.Uri,%20kotlin.Int\))`, except it grants your own permissions if you are not currently processing an IPC. Use with care!  
`[IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)` | `[checkCallingOrSelfUriPermissions](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingOrSelfUriPermissions\(kotlin.collections.MutableList,%20kotlin.Int\))(uris: [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!>, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether the calling process of an IPC _or you_ has been granted permission to access a list of URIs. This is the same as `[checkCallingUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#checkCallingUriPermission\(android.net.Uri,%20kotlin.Int\))`, except it grants your own permissions if you are not currently processing an IPC. Use with care!  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkCallingPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingPermission\(kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Determine whether the calling process of an IPC you are handling has been granted a particular permission. This is basically the same as calling `[checkPermission(String,int,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#checkPermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int\))` with the pid and uid returned by `[android.os.Binder#getCallingPid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingPid\(\))` and `[android.os.Binder#getCallingUid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingUid\(\))`. One important difference is that if you are not currently processing an IPC, this function will always fail. This is done to protect against accidentally leaking permissions; you can use `[checkCallingOrSelfPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#checkCallingOrSelfPermission\(kotlin.String\))` to avoid this protection.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkCallingUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingUriPermission\(android.net.Uri,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether the calling process and uid has been granted permission to access a specific URI. This is basically the same as calling `[checkUriPermission(Uri,int,int,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#checkUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))` with the pid and uid returned by `[android.os.Binder#getCallingPid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingPid\(\))` and `[android.os.Binder#getCallingUid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingUid\(\))`. One important difference is that if you are not currently processing an IPC, this function will always fail.  
`[IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)` | `[checkCallingUriPermissions](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkCallingUriPermissions\(kotlin.collections.MutableList,%20kotlin.Int\))(uris: [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!>, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether the calling process and uid has been granted permission to access a list of URIs. This is basically the same as calling `[checkUriPermissions(List,int,int,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#checkUriPermissions\(kotlin.collections.MutableList,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))` with the pid and uid returned by `[android.os.Binder#getCallingPid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingPid\(\))` and `[android.os.Binder#getCallingUid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingUid\(\))`. One important difference is that if you are not currently processing an IPC, this function will always fail.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkContentUriPermissionFull](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkContentUriPermissionFull\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html), pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether a particular process and uid has been granted permission to access a specific content URI.  Unlike `[checkUriPermission(Uri,int,int,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#checkUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))`, this method checks for general access to the URI's content provider, as well as explicitly granted permissions. Note, this check will throw an `[IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` for non-content URIs.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkPermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether the given permission is allowed for a particular process and user ID running in the system.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Determine whether _you_ have been granted a particular permission.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether a particular process and uid has been granted permission to access a specific URI. This only checks for permissions that have been explicitly granted -- if the given process/uid has more general access to the URI's content provider then this check will always fail.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[checkUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkUriPermission\(android.net.Uri,%20kotlin.String,%20kotlin.String,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)?, readPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, writePermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Check both a Uri and normal permission. This allows you to perform both `[checkPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#checkPermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int\))` and #checkUriPermission in one call.  
`[IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)` | `[checkUriPermissions](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkUriPermissions\(kotlin.collections.MutableList,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(uris: [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!>, pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Determine whether a particular process and uid has been granted permission to access a list of URIs. This only checks for permissions that have been explicitly granted -- if the given process/uid has more general access to the URI's content provider then this check will always fail. **Note:** On SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, calling this method from a secondary-user's context will incorrectly return `[PackageManager.PERMISSION_DENIED](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#PERMISSION_DENIED:kotlin.Int)` for all {code uris}.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[clearWallpaper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#clearWallpaper\(\))()`  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[createAttributionContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createAttributionContext\(kotlin.String\))(attributionTag: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Return a new Context object for the current Context but attribute to a different tag. In complex apps attribution tagging can be used to distinguish between separate logical parts.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[createConfigurationContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createConfigurationContext\(android.content.res.Configuration\))(overrideConfiguration: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html))` Return a new Context object for the current Context but whose resources are adjusted to match the given Configuration. Each call to this method returns a new instance of a Context object; Context objects are not shared, however common state (ClassLoader, other Resources for the same configuration) may be so the Context itself can be fairly lightweight.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[createContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createContext\(android.content.ContextParams\))(contextParams: [ContextParams](https://developer.android.com/reference/kotlin/android/content/ContextParams.html))` Creates a context with specific properties and behaviors.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[createContextForSplit](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createContextForSplit\(kotlin.String\))(splitName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Return a new Context object for the given split name. The new Context has a ClassLoader and Resources object that can access the split's and all of its dependencies' code/resources. Each call to this method returns a new instance of a Context object; Context objects are not shared, however common state (ClassLoader, other Resources for the same split) may be so the Context itself can be fairly lightweight.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[createDeviceContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createDeviceContext\(kotlin.Int\))(deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Returns a new `Context` object from the current context but with device association given by the `deviceId`. Each call to this method returns a new instance of a context object. Context objects are not shared; however, common state (such as the `[ClassLoader](https://developer.android.com/reference/kotlin/java/lang/ClassLoader.html)` and other resources for the same configuration) can be shared, so the `Context` itself is lightweight.  Applications that run on virtual devices may use this method to access the default device capabilities and functionality (by passing `[Context.DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)`. Similarly, applications running on the default device may access the functionality of virtual devices.  Note that the newly created instance will be associated with the same display as the parent Context, regardless of the device ID passed here.   
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[createDeviceProtectedStorageContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createDeviceProtectedStorageContext\(\))()` Return a new Context object for the current Context but whose storage APIs are backed by device-protected storage.  On devices with direct boot, data stored in this location is encrypted with a key tied to the physical device, and it can be accessed immediately after the device has booted successfully, both _before and after_ the user has authenticated with their credentials (such as a lock pattern or PIN).  Because device-protected data is available without user authentication, you should carefully limit the data you store using this Context. For example, storing sensitive authentication tokens or passwords in the device-protected area is strongly discouraged.  If the underlying device does not have the ability to store device-protected and credential-protected data using different keys, then both storage areas will become available at the same time. They remain as two distinct storage locations on disk, and only the window of availability changes.  Each call to this method returns a new instance of a Context object; Context objects are not shared, however common state (ClassLoader, other Resources for the same configuration) may be so the Context itself can be fairly lightweight.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[createDisplayContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createDisplayContext\(android.view.Display\))(display: [Display](https://developer.android.com/reference/kotlin/android/view/Display.html))` Returns a new `Context` object from the current context but with resources adjusted to match the metrics of `display`. Each call to this method returns a new instance of a context object. Context objects are not shared; however, common state (such as the `[ClassLoader](https://developer.android.com/reference/kotlin/java/lang/ClassLoader.html)` and other resources for the same configuration) can be shared, so the `Context` itself is lightweight.  **Note:** This `Context` is **not** expected to be updated with new configuration if the underlying display configuration changes and the cached `Resources` it returns could be stale. It is suggested to use `[android.hardware.display.DisplayManager.DisplayListener](https://developer.android.com/reference/kotlin/android/hardware/display/DisplayManager.DisplayListener.html)` to listen for changes and re-create an instance if necessary.  This `Context` is **not** a UI context, do not use it to access UI components or obtain a `[WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)` instance.  To obtain an instance of `[WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)` configured to show windows on the given display, call `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))` on the returned display context, then call `[getSystemService(String)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(kotlin.String\))` or `[getSystemService(Class)](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(java.lang.Class\))` on the returned window context.   
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[createPackageContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createPackageContext\(kotlin.String,%20kotlin.Int\))(packageName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Return a new Context object for the given application name. This Context is the same as what the named application gets when it is launched, containing the same resources and class loader. Each call to this method returns a new instance of a Context object; Context objects are not shared, however they share common state (Resources, ClassLoader, etc) so the Context instance itself is fairly lightweight.  Throws `[android.content.pm.PackageManager.NameNotFoundException](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.NameNotFoundException.html)` if there is no application with the given package name.  Throws `[java.lang.SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` if the Context requested can not be loaded into the caller's process for security reasons (see `[CONTEXT_INCLUDE_CODE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTEXT_INCLUDE_CODE:kotlin.Int)` for more information}.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[createWindowContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createWindowContext\(android.view.Display,%20kotlin.Int,%20android.os.Bundle\))(display: [Display](https://developer.android.com/reference/kotlin/android/view/Display.html), type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Creates a `Context` for a non-`activity` window on the given `[Display](https://developer.android.com/reference/kotlin/android/view/Display.html)`.  Similar to `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))`, but the `display` is passed in, instead of implicitly using the `[original Context's Display](https://developer.android.com/reference/kotlin/android/content/Context.html#getDisplay\(\))`.   
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[createWindowContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))(type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Creates a Context for a non-activity window.  A window context is a context that can be used to add non-activity windows, such as `[android.view.WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html#TYPE_APPLICATION_OVERLAY:kotlin.Int)`. A window context must be created from a context that has an associated `[Display](https://developer.android.com/reference/kotlin/android/view/Display.html)`, such as `Activity` or a context created with `[createDisplayContext(Display)](https://developer.android.com/reference/kotlin/android/content/Context.html#createDisplayContext\(android.view.Display\))`.  The window context is created with the appropriate `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` for the area of the display that the windows created with it can occupy; it must be used when `[inflating](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)` views, such that they can be inflated with proper `[Resources](https://developer.android.com/reference/kotlin/android/content/res/Resources.html)`. Below is a sample code to **add an application overlay window on the primary display:**
    
    
    ...
      final DisplayManager dm = anyContext.getSystemService(DisplayManager.class);
      final Display primaryDisplay = dm.getDisplay(DEFAULT_DISPLAY);
      final Context windowContext = anyContext.createDisplayContext(primaryDisplay)
              .createWindowContext(TYPE_APPLICATION_OVERLAY, null);
      final View overlayView = Inflater.from(windowContext).inflate(someLayoutXml, null);
     
      // WindowManager.LayoutParams initialization
      ...
      // The types used in addView and createWindowContext must match.
      mParams.type = TYPE_APPLICATION_OVERLAY;
      ...
     
      windowContext.getSystemService(WindowManager.class).addView(overlayView, mParams);
      

This context's configuration and resources are adjusted to an area of the display where the windows with provided type will be added. **Note that all windows associated with the same context will have an affinity and can only be moved together between different displays or areas on a display.** If there is a need to add different window types, or non-associated windows, separate Contexts should be used.  Creating a window context is an expensive operation. Misuse of this API may lead to a huge performance drop. The best practice is to use the same window context when possible. An approach is to create one window context with specific window type and display and use it everywhere it's needed.  After `[Build.VERSION_CODES.S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, window context provides the capability to receive configuration changes for existing token by overriding the `[token](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html#token:android.os.IBinder)` of the `[android.view.WindowManager.LayoutParams](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html)` passed in `[WindowManager.addView(View,LayoutParams)](https://developer.android.com/reference/kotlin/android/view/ViewManager.html#addView\(android.view.View,%20android.view.ViewGroup.LayoutParams\))`. This is useful when an application needs to attach its window to an existing activity for window token sharing use-case.  Note that the window context in `[Build.VERSION_CODES.R](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#R:kotlin.Int)` didn't have this capability. This is a no-op for the window context in `[Build.VERSION_CODES.R](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#R:kotlin.Int)`.  Below is sample code to **attach an existing token to a window context:**
    
    
    final DisplayManager dm = anyContext.getSystemService(DisplayManager.class);
      final Display primaryDisplay = dm.getDisplay(DEFAULT_DISPLAY);
      final Context windowContext = anyContext.createWindowContext(primaryDisplay,
              TYPE_APPLICATION, null);
     
      // Get an existing token.
      final IBinder existingToken = activity.getWindow().getAttributes().token;
     
      // The types used in addView() and createWindowContext() must match.
      final WindowManager.LayoutParams params = new WindowManager.LayoutParams(TYPE_APPLICATION);
      params.token = existingToken;
     
      // After WindowManager#addView(), the server side will extract the provided token from
      // LayoutParams#token (existingToken in the sample code), and switch to propagate
      // configuration changes from the node associated with the provided token.
      windowContext.getSystemService(WindowManager.class).addView(overlayView, mParams);
      

After `[Build.VERSION_CODES.S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, window context provides the capability to listen to its `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` changes by calling `[registerComponentCallbacks(ComponentCallbacks)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerComponentCallbacks\(android.content.ComponentCallbacks\))`, while other kinds of `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` will register the `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to `[its](https://developer.android.com/reference/kotlin/android/content/Context.html#getApplicationContext\(\))`. Note that window context only propagate `[ComponentCallbacks.onConfigurationChanged(Configuration)](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html#onConfigurationChanged\(android.content.res.Configuration\))` callback. `[ComponentCallbacks.onLowMemory()](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html#onLowMemory\(\))` or other callbacks in `[ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html)` won't be invoked.  Note that using `[android.app.Application](https://developer.android.com/reference/kotlin/android/app/Application)` or `[android.app.Service](https://developer.android.com/reference/kotlin/android/app/Service)` context for UI-related queries may result in layout or continuity issues on devices with variable screen sizes (e.g. foldables) or in multi-window modes, since these non-UI contexts may not reflect the `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` changes for the visual container.   
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!` | `[databaseList](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#databaseList\(\))()` Returns an array of strings naming the private databases associated with this Context's application package.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[deleteDatabase](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#deleteDatabase\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Delete an existing private SQLiteDatabase associated with this Context's application package.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[deleteFile](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#deleteFile\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Delete the given private file associated with this Context's application package.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[deleteSharedPreferences](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#deleteSharedPreferences\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Delete an existing shared preferences file.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceCallingOrSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceCallingOrSelfPermission\(kotlin.String,%20kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` If neither you nor the calling process of an IPC you are handling has been granted a particular permission, throw a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`. This is the same as `[enforceCallingPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#enforceCallingPermission\(kotlin.String,%20kotlin.String\))`, except it grants your own permissions if you are not currently processing an IPC. Use with care!  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceCallingOrSelfUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceCallingOrSelfUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.String\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` If the calling process of an IPC _or you_ has not been granted permission to access a specific URI, throw `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`. This is the same as `[enforceCallingUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#enforceCallingUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.String\))`, except it grants your own permissions if you are not currently processing an IPC. Use with care!  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceCallingPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceCallingPermission\(kotlin.String,%20kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` If the calling process of an IPC you are handling has not been granted a particular permission, throw a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`. This is basically the same as calling `[enforcePermission(String,int,int,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#enforcePermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))` with the pid and uid returned by `[android.os.Binder#getCallingPid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingPid\(\))` and `[android.os.Binder#getCallingUid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingUid\(\))`. One important difference is that if you are not currently processing an IPC, this function will always throw the SecurityException. This is done to protect against accidentally leaking permissions; you can use `[enforceCallingOrSelfPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#enforceCallingOrSelfPermission\(kotlin.String,%20kotlin.String\))` to avoid this protection.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceCallingUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceCallingUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.String\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` If the calling process and uid has not been granted permission to access a specific URI, throw `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`. This is basically the same as calling `[enforceUriPermission(Uri,int,int,int,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#enforceUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))` with the pid and uid returned by `[android.os.Binder#getCallingPid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingPid\(\))` and `[android.os.Binder#getCallingUid](https://developer.android.com/reference/kotlin/android/os/Binder.html#getCallingUid\(\))`. One important difference is that if you are not currently processing an IPC, this function will always throw a SecurityException.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforcePermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforcePermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` If the given permission is not allowed for a particular process and user ID running in the system, throw a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceUriPermission\(android.net.Uri,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` If a particular process and uid has not been granted permission to access a specific URI, throw `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)`. This only checks for permissions that have been explicitly granted -- if the given process/uid has more general access to the URI's content provider then this check will always fail.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[enforceUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#enforceUriPermission\(android.net.Uri,%20kotlin.String,%20kotlin.String,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)?, readPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, writePermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, pid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), uid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Enforce both a Uri and normal permission. This allows you to perform both `[enforcePermission](https://developer.android.com/reference/kotlin/android/content/Context.html#enforcePermission\(kotlin.String,%20kotlin.Int,%20kotlin.Int,%20kotlin.String\))` and #enforceUriPermission in one call.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!` | `[fileList](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#fileList\(\))()` Returns an array of strings naming the private files associated with this Context's application package.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[getApplicationContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getApplicationContext\(\))()` Return the context of the single, global Application object of the current process. This generally should only be used if you need a Context whose lifecycle is separate from the current context, that is tied to the lifetime of the process rather than the current component.  Consider for example how this interacts with `[registerReceiver(BroadcastReceiver,IntentFilter)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))`: 

  * If used from an Activity context, the receiver is being registered within that activity. This means that you are expected to unregister before the activity is done being destroyed; in fact if you do not do so, the framework will clean up your leaked registration as it removes the activity and log an error. Thus, if you use the Activity context to register a receiver that is static (global to the process, not associated with an Activity instance) then that registration will be removed on you at whatever point the activity you used is destroyed. 
  * If used from the Context returned here, the receiver is being registered with the global state associated with your application. Thus it will never be unregistered for you. This is necessary if the receiver is associated with static data, not a particular component. However using the ApplicationContext elsewhere can easily lead to serious leaks if you forget to unregister, unbind, etc. 

  
`[ApplicationInfo](https://developer.android.com/reference/kotlin/android/content/pm/ApplicationInfo.html)!` | `[getApplicationInfo](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getApplicationInfo\(\))()` Return the full application info for this context's package.  
`[AttributionSource](https://developer.android.com/reference/kotlin/android/content/AttributionSource.html)` | `[getAttributionSource](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getAttributionSource\(\))()`  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` | `[getAttributionTag](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getAttributionTag\(\))()` Attribution can be used in complex apps to logically separate parts of the app. E.g. a blogging app might also have a instant messaging app built in. In this case two separate tags can for used each sub-feature.  
`[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!` | `[getBaseContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getBaseContext\(\))()`  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getCacheDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getCacheDir\(\))()` Returns the absolute path to the application specific cache directory on the filesystem.  The system will automatically delete files in this directory as disk space is needed elsewhere on the device. The system will always delete older files first, as reported by `[File.lastModified()](https://developer.android.com/reference/kotlin/java/io/File.html#lastModified\(\))`. If desired, you can exert more control over how files are deleted using `[StorageManager.setCacheBehaviorGroup(File,boolean)](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager.html#setCacheBehaviorGroup\(java.io.File,%20kotlin.Boolean\))` and `[StorageManager.setCacheBehaviorTombstone(File,boolean)](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager.html#setCacheBehaviorTombstone\(java.io.File,%20kotlin.Boolean\))`.  Apps are strongly encouraged to keep their usage of cache space below the quota returned by `[StorageManager.getCacheQuotaBytes(java.util.UUID)](https://developer.android.com/reference/kotlin/android/os/storage/StorageManager.html#getCacheQuotaBytes\(java.util.UUID\))`. If your app goes above this quota, your cached files will be some of the first to be deleted when additional disk space is needed. Conversely, if your app stays under this quota, your cached files will be some of the last to be deleted when additional disk space is needed.  Note that your cache quota will change over time depending on how frequently the user interacts with your app, and depending on how much system-wide disk space is used.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  Apps require no extra permissions to read or write to the returned path, since this path lives in their private storage.  
`[ClassLoader](https://developer.android.com/reference/kotlin/java/lang/ClassLoader.html)!` | `[getClassLoader](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getClassLoader\(\))()` Return a class loader you can use to retrieve classes in this package.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getCodeCacheDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getCodeCacheDir\(\))()` Returns the absolute path to the application specific cache directory on the filesystem designed for storing cached code.  The system will delete any files stored in this location both when your specific application is upgraded, and when the entire platform is upgraded.  This location is optimal for storing compiled or optimized code generated by your application at runtime.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  Apps require no extra permissions to read or write to the returned path, since this path lives in their private storage.  
`[ContentResolver](https://developer.android.com/reference/kotlin/android/content/ContentResolver.html)!` | `[getContentResolver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getContentResolver\(\))()` Return a ContentResolver instance for your application's package.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getDataDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getDataDir\(\))()` Returns the absolute path to the directory on the filesystem where all private files belonging to this app are stored. Apps should not use this path directly; they should instead use `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))`, `[getCacheDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getCacheDir\(\))`, `[getDir(String,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#getDir\(kotlin.String,%20kotlin.Int\))`, or other storage APIs on this class.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  No additional permissions are required for the calling app to read or write files under the returned path.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getDatabasePath](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getDatabasePath\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the absolute path on the filesystem where a database created with #openOrCreateDatabase is stored.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[getDeviceId](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getDeviceId\(\))()` Gets the device ID this context is associated with. Applications can use this method to determine whether they are running on a virtual device and identify that device. The device ID of the host device is `[Context.DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)` If the underlying device ID is changed by the system, for example, when an `Activity` is moved to a different virtual device, applications can register to listen to changes by calling `[Context.registerDeviceIdChangeListener(Executor,IntConsumer)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerDeviceIdChangeListener\(java.util.concurrent.Executor,%20java.util.function.IntConsumer\))`.  This method will only return a reliable value for this instance if it was created with `[Context.createDeviceContext(int)](https://developer.android.com/reference/kotlin/android/content/Context.html#createDeviceContext\(kotlin.Int\))`, or if this instance is a UI or Display Context. Contexts created with `[Context.createDeviceContext(int)](https://developer.android.com/reference/kotlin/android/content/Context.html#createDeviceContext\(kotlin.Int\))` will have an explicit device association, which will never change, even if the underlying device is closed or is removed. UI Contexts and Display Contexts are already associated with a display, so if the device association is not explicitly given, `[Context.getDeviceId()](https://developer.android.com/reference/kotlin/android/content/Context.html#getDeviceId\(\))` will return the ID of the device associated with the associated display. The system can assign an arbitrary device id value for Contexts not logically associated with a device.   
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getDir\(kotlin.String,%20kotlin.Int\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Retrieve, creating if needed, a new directory in which the application can place its own custom data files. You can use the returned File object to create and access files in this directory. Note that files created through a File object will only be accessible by your own application; you can only set the mode of the entire directory, not of individual files.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  Apps require no extra permissions to read or write to the returned path, since this path lives in their private storage.  
`[Display](https://developer.android.com/reference/kotlin/android/view/Display.html)!` | `[getDisplay](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getDisplay\(\))()` Get the display this context is associated with. Applications should use this method with `android.app.Activity` or a context associated with a `[Display](https://developer.android.com/reference/kotlin/android/view/Display.html)` via `[createDisplayContext(Display)](https://developer.android.com/reference/kotlin/android/content/Context.html#createDisplayContext\(android.view.Display\))` to get a display object associated with a Context, or `[android.hardware.display.DisplayManager#getDisplay](https://developer.android.com/reference/kotlin/android/hardware/display/DisplayManager.html#getDisplay\(kotlin.Int\))` to get a display object by id.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)?` | `[getExternalCacheDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getExternalCacheDir\(\))()` Returns absolute path to application-specific directory on the primary shared/external storage device where the application can place cache files it owns. These files are internal to the application, and not typically visible to the user as media.  This is like `[getCacheDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getCacheDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * The platform does not always monitor the space available in shared storage, and thus may not automatically delete these files. Apps should always manage the maximum space used in this location. Currently the only time files here will be deleted by the platform is when running on `[android.os.Build.VERSION_CODES#JELLY_BEAN_MR1](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#JELLY_BEAN_MR1:kotlin.Int)` or later and `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))` returns true. 
  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

If a shared storage device is emulated (as determined by `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))`), its contents are backed by a private user data partition, which means there is little benefit to storing data here instead of the private directory returned by `[getCacheDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getCacheDir\(\))`.  Starting in `[android.os.Build.VERSION_CODES#KITKAT](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#KITKAT:kotlin.Int)`, no permissions are required to read or write to the returned path; it's always accessible to the calling app. This only applies to paths generated for package name of the calling application. To access paths belonging to other packages, `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` and/or `[android.Manifest.permission#READ_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#READ_EXTERNAL_STORAGE:kotlin.String)` are required.  On devices with multiple users (as described by `[UserManager](https://developer.android.com/reference/kotlin/android/os/UserManager.html)`), each user has their own isolated shared storage. Applications only have access to the shared storage for the user they're running as.  The returned path may change over time if different shared storage media is inserted, so only relative paths should be persisted.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[File](https://developer.android.com/reference/kotlin/java/io/File.html)!>!` | `[getExternalCacheDirs](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getExternalCacheDirs\(\))()` Returns absolute paths to application-specific directories on all shared/external storage devices where the application can place cache files it owns. These files are internal to the application, and not typically visible to the user as media.  This is like `[getCacheDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getCacheDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * The platform does not always monitor the space available in shared storage, and thus may not automatically delete these files. Apps should always manage the maximum space used in this location. Currently the only time files here will be deleted by the platform is when running on `[android.os.Build.VERSION_CODES#JELLY_BEAN_MR1](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#JELLY_BEAN_MR1:kotlin.Int)` or later and `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))` returns true. 
  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

If a shared storage device is emulated (as determined by `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))`), its contents are backed by a private user data partition, which means there is little benefit to storing data here instead of the private directory returned by `[getCacheDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getCacheDir\(\))`.  Shared storage devices returned here are considered a stable part of the device, including physical media slots under a protective cover. The returned paths do not include transient devices, such as USB flash drives connected to handheld devices.  An application may store data on any or all of the returned devices. For example, an app may choose to store large files on the device with the most available space, as measured by `[StatFs](https://developer.android.com/reference/kotlin/android/os/StatFs.html)`.  No additional permissions are required for the calling app to read or write files under the returned path. Write access outside of these paths on secondary external storage devices is not available.  The returned paths may change over time if different shared storage media is inserted, so only relative paths should be persisted.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)?` | `[getExternalFilesDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getExternalFilesDir\(kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Returns the absolute path to the directory on the primary shared/external storage device where the application can place persistent files it owns. These files are internal to the applications, and not typically visible to the user as media.  This is like `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

If a shared storage device is emulated (as determined by `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))`), its contents are backed by a private user data partition, which means there is little benefit to storing data here instead of the private directories returned by `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))`, etc.  Starting in `[android.os.Build.VERSION_CODES#KITKAT](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#KITKAT:kotlin.Int)`, no permissions are required to read or write to the returned path; it's always accessible to the calling app. This only applies to paths generated for package name of the calling application. To access paths belonging to other packages, `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` and/or `[android.Manifest.permission#READ_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#READ_EXTERNAL_STORAGE:kotlin.String)` are required.  On devices with multiple users (as described by `[UserManager](https://developer.android.com/reference/kotlin/android/os/UserManager.html)`), each user has their own isolated shared storage. Applications only have access to the shared storage for the user they're running as.  The returned path may change over time if different shared storage media is inserted, so only relative paths should be persisted.  Here is an example of typical code to manipulate a file in an application's shared storage:  If you supply a non-null type to this function, the returned file will be a path to a sub-directory of the given type. Though these files are not automatically scanned by the media scanner, you can explicitly add them to the media database with `[MediaScannerConnection.scanFile](https://developer.android.com/reference/kotlin/android/media/MediaScannerConnection.html#scanFile\(android.content.Context,%20kotlin.Array,%20kotlin.Array,%20android.media.MediaScannerConnection.OnScanCompletedListener\))`. Note that this is not the same as `[Environment.getExternalStoragePublicDirectory()](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStoragePublicDirectory\(kotlin.String\))`, which provides directories of media shared by all applications. The directories returned here are owned by the application, and their contents will be removed when the application is uninstalled. Unlike `[Environment.getExternalStoragePublicDirectory()](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStoragePublicDirectory\(kotlin.String\))`, the directory returned here will be automatically created for you.  Here is an example of typical code to manipulate a picture in an application's shared storage and add it to the media database:   
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[File](https://developer.android.com/reference/kotlin/java/io/File.html)!>!` | `[getExternalFilesDirs](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getExternalFilesDirs\(kotlin.String\))(type: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns absolute paths to application-specific directories on all shared/external storage devices where the application can place persistent files it owns. These files are internal to the application, and not typically visible to the user as media.  This is like `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

If a shared storage device is emulated (as determined by `[Environment.isExternalStorageEmulated(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#isExternalStorageEmulated\(java.io.File\))`), its contents are backed by a private user data partition, which means there is little benefit to storing data here instead of the private directories returned by `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))`, etc.  Shared storage devices returned here are considered a stable part of the device, including physical media slots under a protective cover. The returned paths do not include transient devices, such as USB flash drives connected to handheld devices.  An application may store data on any or all of the returned devices. For example, an app may choose to store large files on the device with the most available space, as measured by `[StatFs](https://developer.android.com/reference/kotlin/android/os/StatFs.html)`.  No additional permissions are required for the calling app to read or write files under the returned path. Write access outside of these paths on secondary external storage devices is not available.  The returned path may change over time if different shared storage media is inserted, so only relative paths should be persisted.  
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[File](https://developer.android.com/reference/kotlin/java/io/File.html)!>!` | `[getExternalMediaDirs](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getExternalMediaDirs\(\))()` Returns absolute paths to application-specific directories on all shared/external storage devices where the application can place media files. These files are scanned and made available to other apps through `[MediaStore](https://developer.android.com/reference/kotlin/android/provider/MediaStore.html)`.  This is like `[getExternalFilesDirs](https://developer.android.com/reference/kotlin/android/content/Context.html#getExternalFilesDirs\(kotlin.String\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

Shared storage devices returned here are considered a stable part of the device, including physical media slots under a protective cover. The returned paths do not include transient devices, such as USB flash drives connected to handheld devices.  An application may store data on any or all of the returned devices. For example, an app may choose to store large files on the device with the most available space, as measured by `[StatFs](https://developer.android.com/reference/kotlin/android/os/StatFs.html)`.  No additional permissions are required for the calling app to read or write files under the returned path. Write access outside of these paths on secondary external storage devices is not available.  The returned paths may change over time if different shared storage media is inserted, so only relative paths should be persisted.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getFileStreamPath](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getFileStreamPath\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Returns the absolute path on the filesystem where a file created with `[openFileOutput](https://developer.android.com/reference/kotlin/android/content/Context.html#openFileOutput\(kotlin.String,%20kotlin.Int\))` is stored.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getFilesDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getFilesDir\(\))()` Returns the absolute path to the directory on the filesystem where files created with `[openFileOutput](https://developer.android.com/reference/kotlin/android/content/Context.html#openFileOutput\(kotlin.String,%20kotlin.Int\))` are stored.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  No additional permissions are required for the calling app to read or write files under the returned path.  
`[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)!` | `[getMainExecutor](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getMainExecutor\(\))()` Return an `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)` that will run enqueued tasks on the main thread associated with this context. This is the thread used to dispatch calls to application components (activities, services, etc).  
`[Looper](https://developer.android.com/reference/kotlin/android/os/Looper.html)!` | `[getMainLooper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getMainLooper\(\))()` Return the Looper for the main thread of the current process. This is the thread used to dispatch calls to application components (activities, services, etc).  By definition, this method returns the same result as would be obtained by calling `[Looper.getMainLooper()](https://developer.android.com/reference/kotlin/android/os/Looper.html#getMainLooper\(\))`.   
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getNoBackupFilesDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getNoBackupFilesDir\(\))()` Returns the absolute path to the directory on the filesystem similar to `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))`. The difference is that files placed under this directory will be excluded from automatic backup to remote storage. See `[BackupAgent](https://developer.android.com/reference/kotlin/android/app/backup/BackupAgent)` for a full discussion of the automatic backup mechanism in Android.  The returned path may change over time if the calling app is moved to an adopted storage device, so only relative paths should be persisted.  No additional permissions are required for the calling app to read or write files under the returned path.  
`[File](https://developer.android.com/reference/kotlin/java/io/File.html)!` | `[getObbDir](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getObbDir\(\))()` Return the primary shared/external storage directory where this application's OBB files (if there are any) can be found. Note if the application does not have any OBB files, this directory may not exist.  This is like `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

Starting in `[android.os.Build.VERSION_CODES#KITKAT](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#KITKAT:kotlin.Int)`, no permissions are required to read or write to the path that this method returns. However, starting from `[android.os.Build.VERSION_CODES#M](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#M:kotlin.Int)`, to read the OBB expansion files, you must declare the `[android.Manifest.permission#READ_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#READ_EXTERNAL_STORAGE:kotlin.String)` permission in the app manifest and ask for permission at runtime as follows:  `<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="23" />` Starting from `[android.os.Build.VERSION_CODES#N](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#N:kotlin.Int)`, `[android.Manifest.permission#READ_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#READ_EXTERNAL_STORAGE:kotlin.String)` permission is not required, so don’t ask for this permission at runtime. To handle both cases, your app must first try to read the OBB file, and if it fails, you must request `[android.Manifest.permission#READ_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#READ_EXTERNAL_STORAGE:kotlin.String)` permission at runtime.  The following code snippet shows how to do this: 
    
    
    File obb = new File(obb_filename);
      boolean open_failed = false;
     
      try {
          BufferedReader br = new BufferedReader(new FileReader(obb));
          open_failed = false;
          ReadObbFile(br);
      } catch (IOException e) {
          open_failed = true;
      }
     
      if (open_failed) {
          // request READ_EXTERNAL_STORAGE permission before reading OBB file
          ReadObbFileWithPermission();
      }
      

On devices with multiple users (as described by `[UserManager](https://developer.android.com/reference/kotlin/android/os/UserManager.html)`), multiple users may share the same OBB storage location. Applications should ensure that multiple instances running under different users don't interfere with each other.   
`[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[File](https://developer.android.com/reference/kotlin/java/io/File.html)!>!` | `[getObbDirs](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getObbDirs\(\))()` Returns absolute paths to application-specific directories on all shared/external storage devices where the application's OBB files (if there are any) can be found. Note if the application does not have any OBB files, these directories may not exist.  This is like `[getFilesDir()](https://developer.android.com/reference/kotlin/android/content/Context.html#getFilesDir\(\))` in that these files will be deleted when the application is uninstalled, however there are some important differences: 

  * Shared storage may not always be available, since removable media can be ejected by the user. Media state can be checked using `[Environment.getExternalStorageState(File)](https://developer.android.com/reference/kotlin/android/os/Environment.html#getExternalStorageState\(java.io.File\))`. 
  * There is no security enforced with these files. For example, any application holding `[android.Manifest.permission#WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#WRITE_EXTERNAL_STORAGE:kotlin.String)` can write to these files. 

Shared storage devices returned here are considered a stable part of the device, including physical media slots under a protective cover. The returned paths do not include transient devices, such as USB flash drives connected to handheld devices.  An application may store data on any or all of the returned devices. For example, an app may choose to store large files on the device with the most available space, as measured by `[StatFs](https://developer.android.com/reference/kotlin/android/os/StatFs.html)`.  No additional permissions are required for the calling app to read or write files under the returned path. Write access outside of these paths on secondary external storage devices is not available.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[getOpPackageName](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getOpPackageName\(\))()` Return the package name that should be used for `[android.app.AppOpsManager](https://developer.android.com/reference/kotlin/android/app/AppOpsManager)` calls from this context, so that app ops manager's uid verification will work with the name.  This is not generally intended for third party application developers.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` | `[getPackageCodePath](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getPackageCodePath\(\))()` Return the full path to this context's primary Android package. The Android package is a ZIP file which contains application's primary code and assets.  Note: this is not generally useful for applications, since they should not be directly accessing the file system.  
`[PackageManager](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html)!` | `[getPackageManager](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getPackageManager\(\))()` Return PackageManager instance to find global package information.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` | `[getPackageName](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getPackageName\(\))()` Return the name of this application's package.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!` | `[getPackageResourcePath](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getPackageResourcePath\(\))()` Return the full path to this context's primary Android package. The Android package is a ZIP file which contains the application's primary resources.  Note: this is not generally useful for applications, since they should not be directly accessing the file system.  
`[ContextParams](https://developer.android.com/reference/kotlin/android/content/ContextParams.html)?` | `[getParams](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getParams\(\))()` Return the set of parameters which this Context was created with, if it was created via `[createContext(ContextParams)](https://developer.android.com/reference/kotlin/android/content/Context.html#createContext\(android.content.ContextParams\))`.  
`[SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)!` | `[getSharedPreferences](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getSharedPreferences\(kotlin.String,%20kotlin.Int\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Retrieve and hold the contents of the preferences file 'name', returning a SharedPreferences through which you can retrieve and modify its values. Only one instance of the SharedPreferences object is returned to any callers for the same name, meaning they will see each other's edits as soon as they are made.  This method is thread-safe.  If the preferences directory does not already exist, it will be created when this method is called.  If a preferences file by this name does not exist, it will be created when you retrieve an editor (`[SharedPreferences.edit()](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html#edit\(\))`) and then commit changes (`[SharedPreferences.Editor.commit()](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.Editor.html#commit\(\))` or `[SharedPreferences.Editor.apply()](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.Editor.html#apply\(\))`).  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` | `[getSystemServiceName](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getSystemServiceName\(java.lang.Class\))(serviceClass: [Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)<*>)` Gets the name of the system-level service that is represented by the specified class.  
`[Drawable](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable.html)!` | `[getWallpaper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getWallpaper\(\))()`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[getWallpaperDesiredMinimumHeight](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getWallpaperDesiredMinimumHeight\(\))()`  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[getWallpaperDesiredMinimumWidth](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getWallpaperDesiredMinimumWidth\(\))()`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[grantUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#grantUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))(toPackage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Grant permission to access a specific Uri to another package, regardless of whether that package has general permission to access the Uri's content provider. This can be used to grant specific, temporary permissions, typically in response to user interaction (such as the user opening an attachment that you would like someone else to display).  Normally you should use `[Intent.FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_READ_URI_PERMISSION:kotlin.Int)` or `[Intent.FLAG_GRANT_WRITE_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_WRITE_URI_PERMISSION:kotlin.Int)` with the Intent being used to start an activity instead of this function directly. If you use this function directly, you should be sure to call #revokeUriPermission when the target should no longer be allowed to access it.  To succeed, the content provider owning the Uri must have set the `[grantUriPermissions](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestProvider_grantUriPermissions:kotlin.Int)` attribute in its manifest or included the `[<grant-uri-permissions>](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestGrantUriPermission:kotlin.IntArray)` tag.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[isDeviceProtectedStorage](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#isDeviceProtectedStorage\(\))()` Indicates if the storage APIs of this Context are backed by device-protected storage.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[isRestricted](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#isRestricted\(\))()` Indicates whether this Context is restricted.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[isUiContext](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#isUiContext\(\))()` Returns `true` if the context is a UI context which can access UI components such as `[WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)`, `[LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)` or `[WallpaperManager](https://developer.android.com/reference/kotlin/android/app/WallpaperManager)`. Accessing UI components from non-UI contexts throws `[android.os.strictmode.Violation](https://developer.android.com/reference/kotlin/android/os/strictmode/Violation.html)` if `[android.os.StrictMode.VmPolicy.Builder#detectIncorrectContextUse()](https://developer.android.com/reference/kotlin/android/os/StrictMode.VmPolicy.Builder.html#detectIncorrectContextUse\(\))` is enabled.  Examples of UI contexts are an `Activity`, a context created from `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))` or `[InputMethodService](https://developer.android.com/reference/kotlin/android/inputmethodservice/InputMethodService.html)` Note that even if it is allowed programmatically, it is not suggested to override this method to bypass `[android.os.strictmode.IncorrectContextUseViolation](https://developer.android.com/reference/kotlin/android/os/strictmode/IncorrectContextUseViolation.html)` verification.   
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[moveDatabaseFrom](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#moveDatabaseFrom\(android.content.Context,%20kotlin.String\))(sourceContext: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!, name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Move an existing database file from the given source storage context to this context. This is typically used to migrate data between storage locations after an upgrade, such as migrating to device protected storage.  The database must be closed before being moved.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[moveSharedPreferencesFrom](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#moveSharedPreferencesFrom\(android.content.Context,%20kotlin.String\))(sourceContext: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!, name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Move an existing shared preferences file from the given source storage context to this context. This is typically used to migrate data between storage locations after an upgrade, such as moving to device protected storage.  
`[FileInputStream](https://developer.android.com/reference/kotlin/java/io/FileInputStream.html)!` | `[openFileInput](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#openFileInput\(kotlin.String\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!)` Open a private file associated with this Context's application package for reading.  
`[FileOutputStream](https://developer.android.com/reference/kotlin/java/io/FileOutputStream.html)!` | `[openFileOutput](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#openFileOutput\(kotlin.String,%20kotlin.Int\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Open a private file associated with this Context's application package for writing. Creates the file if it doesn't already exist.  No additional permissions are required for the calling app to read or write the returned file.  
`[SQLiteDatabase](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase.html)!` | `[openOrCreateDatabase](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#openOrCreateDatabase\(kotlin.String,%20kotlin.Int,%20android.database.sqlite.SQLiteDatabase.CursorFactory\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), factory: [SQLiteDatabase.CursorFactory](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase.CursorFactory.html)!)` Open a new private SQLiteDatabase associated with this Context's application package. Create the database file if it doesn't exist.  
`[SQLiteDatabase](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase.html)!` | `[openOrCreateDatabase](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#openOrCreateDatabase\(kotlin.String,%20kotlin.Int,%20android.database.sqlite.SQLiteDatabase.CursorFactory,%20android.database.DatabaseErrorHandler\))(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), factory: [SQLiteDatabase.CursorFactory](https://developer.android.com/reference/kotlin/android/database/sqlite/SQLiteDatabase.CursorFactory.html)!, errorHandler: [DatabaseErrorHandler](https://developer.android.com/reference/kotlin/android/database/DatabaseErrorHandler.html)?)` Open a new private SQLiteDatabase associated with this Context's application package. Creates the database file if it doesn't exist.  Accepts input param: a concrete instance of `[DatabaseErrorHandler](https://developer.android.com/reference/kotlin/android/database/DatabaseErrorHandler.html)` to be used to handle corruption when sqlite reports database corruption.   
`[Drawable](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable.html)!` | `[peekWallpaper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#peekWallpaper\(\))()`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[rebindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#rebindService\(android.content.ServiceConnection,%20android.content.Context.BindServiceFlags\))(conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), flags: [Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html))` Rebind an application service with updated bind service flags  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[registerComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerComponentCallbacks\(android.content.ComponentCallbacks\))(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!)` Add a new `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to the base application of the Context, which will be called at the same times as the ComponentCallbacks methods of activities and other components are called. Note that you _must_ be sure to use `[unregisterComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unregisterComponentCallbacks\(android.content.ComponentCallbacks\))` when appropriate in the future; this will not be removed for you.  After `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)`, the `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` will be registered to `[the base Context](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getBaseContext\(\))`, and can be only used after `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`. Users can still call to `getApplicationContext().registerComponentCallbacks(ComponentCallbacks)` to add `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to the base application.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[registerDeviceIdChangeListener](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerDeviceIdChangeListener\(java.util.concurrent.Executor,%20java.util.function.IntConsumer\))(executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), listener: [IntConsumer](https://developer.android.com/reference/kotlin/java/util/function/IntConsumer.html))` Adds a new device ID changed listener to the `Context`, which will be called when the device association is changed by the system.  The callback can be called when an app is moved to a different device and the `Context` is not explicitly associated with a specific device.  When an application receives a device id update callback, this Context is guaranteed to also have an updated display ID(if any) and `[Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)`.   
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?` | `[registerReceiver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))(receiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, filter: [IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html)!)` Register a BroadcastReceiver to be run in the main activity thread. The receiver will be called with any broadcast Intent that matches filter, in the main application thread.  The system may broadcast Intents that are "sticky" -- these stay around after the broadcast has finished, to be sent to any later registrations. If your IntentFilter matches one of these sticky Intents, that Intent will be returned by this function **and** sent to your receiver as if it had just been broadcast.  There may be multiple sticky Intents that match filter, in which case each of these will be sent to receiver. In this case, only one of these can be returned directly by the function; which of these that is returned is arbitrarily decided by the system.  If you know the Intent you are registering for is sticky, you can supply null for your receiver. In this case, no receiver is registered -- the function simply returns the sticky Intent that matches filter. In the case of multiple matches, the same rules as described above apply.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  As of `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, the system can [place context-registered broadcasts in a queue while the app is in the ](https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14)[cached state](https://developer.android.com/guide/components/activities/process-lifecycle). When the app leaves the cached state, such as returning to the foreground, the system delivers any queued broadcasts. Multiple instances of certain broadcasts might be merged into one broadcast.  As of `[android.os.Build.VERSION_CODES#ICE_CREAM_SANDWICH](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ICE_CREAM_SANDWICH:kotlin.Int)`, receivers registered with this method will correctly respect the `[Intent.setPackage(String)](https://developer.android.com/reference/kotlin/android/content/Intent.html#setPackage\(kotlin.String\))` specified for an Intent being broadcast. Prior to that, it would be ignored and delivered to all matching registered receivers. Be careful if using this for security. For apps targeting `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, either `[RECEIVER_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_EXPORTED:kotlin.Int)` or `[RECEIVER_NOT_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_NOT_EXPORTED:kotlin.Int)` must be specified if the receiver is not being registered for [system broadcasts](https://developer.android.com/guide/components/broadcasts#system-broadcasts) or a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` will be thrown. See `[registerReceiver(BroadcastReceiver,IntentFilter,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.Int\))` to register a receiver with flags.  Note: this method _cannot be called from a`[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` component;_ that is, from a BroadcastReceiver that is declared in an application's manifest. It is okay, however, to call this method from another BroadcastReceiver that has itself been registered at run time with #registerReceiver, since the lifetime of such a registered BroadcastReceiver is tied to the object that registered it.  
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?` | `[registerReceiver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.Int\))(receiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, filter: [IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html)!, flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Register to receive intent broadcasts, with the receiver optionally being exposed to Instant Apps. See `[registerReceiver(BroadcastReceiver,IntentFilter)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))` for more information. By default Instant Apps cannot interact with receivers in other applications, this allows you to expose a receiver that Instant Apps can interact with.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  As of `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, the system can [place context-registered broadcasts in a queue while the app is in the ](https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14)[cached state](https://developer.android.com/guide/components/activities/process-lifecycle). When the app leaves the cached state, such as returning to the foreground, the system delivers any queued broadcasts. Multiple instances of certain broadcasts might be merged into one broadcast.  As of `[android.os.Build.VERSION_CODES#ICE_CREAM_SANDWICH](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ICE_CREAM_SANDWICH:kotlin.Int)`, receivers registered with this method will correctly respect the `[Intent.setPackage(String)](https://developer.android.com/reference/kotlin/android/content/Intent.html#setPackage\(kotlin.String\))` specified for an Intent being broadcast. Prior to that, it would be ignored and delivered to all matching registered receivers. Be careful if using this for security.  
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?` | `[registerReceiver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.String,%20android.os.Handler\))(receiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, filter: [IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html)!, broadcastPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?)` Register to receive intent broadcasts, to run in the context of scheduler. See `[registerReceiver(BroadcastReceiver,IntentFilter)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))` for more information. This allows you to enforce permissions on who can broadcast intents to your receiver, or have the receiver run in a different thread than the main application thread.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  As of `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, the system can [place context-registered broadcasts in a queue while the app is in the ](https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14)[cached state](https://developer.android.com/guide/components/activities/process-lifecycle). When the app leaves the cached state, such as returning to the foreground, the system delivers any queued broadcasts. Multiple instances of certain broadcasts might be merged into one broadcast.  As of `[android.os.Build.VERSION_CODES#ICE_CREAM_SANDWICH](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ICE_CREAM_SANDWICH:kotlin.Int)`, receivers registered with this method will correctly respect the `[Intent.setPackage(String)](https://developer.android.com/reference/kotlin/android/content/Intent.html#setPackage\(kotlin.String\))` specified for an Intent being broadcast. Prior to that, it would be ignored and delivered to all matching registered receivers. Be careful if using this for security. For apps targeting `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, either `[RECEIVER_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_EXPORTED:kotlin.Int)` or `[RECEIVER_NOT_EXPORTED](https://developer.android.com/reference/kotlin/android/content/Context.html#RECEIVER_NOT_EXPORTED:kotlin.Int)` must be specified if the receiver is not being registered for [system broadcasts](https://developer.android.com/guide/components/broadcasts#system-broadcasts) or a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` will be thrown. See `[registerReceiver(BroadcastReceiver,IntentFilter,String,Handler,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.String,%20android.os.Handler,%20kotlin.Int\))` to register a receiver with flags.  
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?` | `[registerReceiver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.String,%20android.os.Handler,%20kotlin.Int\))(receiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, filter: [IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html)!, broadcastPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Register to receive intent broadcasts, to run in the context of scheduler. See `[registerReceiver(BroadcastReceiver,IntentFilter,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.Int\))` and `[registerReceiver(BroadcastReceiver,IntentFilter,String,Handler)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter,%20kotlin.String,%20android.os.Handler\))` for more information.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  As of `[android.os.Build.VERSION_CODES#UPSIDE_DOWN_CAKE](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#UPSIDE_DOWN_CAKE:kotlin.Int)`, the system can [place context-registered broadcasts in a queue while the app is in the ](https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14)[cached state](https://developer.android.com/guide/components/activities/process-lifecycle). When the app leaves the cached state, such as returning to the foreground, the system delivers any queued broadcasts. Multiple instances of certain broadcasts might be merged into one broadcast.  As of `[android.os.Build.VERSION_CODES#ICE_CREAM_SANDWICH](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ICE_CREAM_SANDWICH:kotlin.Int)`, receivers registered with this method will correctly respect the `[Intent.setPackage(String)](https://developer.android.com/reference/kotlin/android/content/Intent.html#setPackage\(kotlin.String\))` specified for an Intent being broadcast. Prior to that, it would be ignored and delivered to all matching registered receivers. Be careful if using this for security.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[removeStickyBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#removeStickyBroadcast\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Remove the data previously sent with #sendStickyBroadcast, so that it is as if the sticky broadcast had never happened.   
Requires `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[removeStickyBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#removeStickyBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!)` Version of `[removeStickyBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#removeStickyBroadcast\(android.content.Intent\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.  You must hold the `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)` permission in order to use this API. If you do not hold that permission, `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` will be thrown.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS and `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[revokeSelfPermissionsOnKill](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#revokeSelfPermissionsOnKill\(kotlin.collections.MutableCollection\))(permissions: [MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>)` Triggers the revocation of one or more permissions for the calling package. A package is only able to revoke runtime permissions. If a permission is not currently granted, it is ignored and will not get revoked (even if later granted by the user). Ultimately, you should never make assumptions about a permission status as users may grant or revoke them at any time.  Background permissions which have no corresponding foreground permission still granted once the revocation is effective will also be revoked.  The revocation happens asynchronously and kills all processes running in the calling UID. It will be triggered once it is safe to do so. In particular, it will not be triggered as long as the package remains in the foreground, or has any active manifest components (e.g. when another app is accessing a content provider in the package).  If you want to revoke the permissions right away, you could call `System.exit()` in `Handler.postDelayed` with a delay to allow completion of async IPC, But `System.exit()` could affect other apps that are accessing your app at the moment. For example, apps accessing a content provider in your app will all crash.  Note that the settings UI shows a permission group as granted as long as at least one permission in the group is granted. If you want the user to observe the revocation in the settings, you should revoke every permission in the target group. To learn the current list of permissions in a group, you may use `[PackageManager.getGroupOfPlatformPermission(String,Executor,Consumer)](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#getGroupOfPlatformPermission\(kotlin.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer\))` and `[PackageManager.getPlatformPermissionsForGroup(String,Executor,Consumer)](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#getPlatformPermissionsForGroup\(kotlin.String,%20java.util.concurrent.Executor,%20java.util.function.Consumer\))`. This list of permissions may evolve over time, so it is recommended to check whether it contains any permission you wish to retain before trying to revoke an entire group.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[revokeUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#revokeUriPermission\(android.net.Uri,%20kotlin.Int\))(uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Remove all permissions to access a particular content provider Uri that were previously added with `[grantUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#grantUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))` or _any other_ mechanism. The given Uri will match all previously granted Uris that are the same or a sub-path of the given Uri. That is, revoking "content://foo/target" will revoke both "content://foo/target" and "content://foo/target/sub", but not "content://foo". It will not remove any prefix grants that exist at a higher level.  Prior to `[android.os.Build.VERSION_CODES#LOLLIPOP](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#LOLLIPOP:kotlin.Int)`, if you did not have regular permission access to a Uri, but had received access to it through a specific Uri permission grant, you could not revoke that grant with this function and a `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` would be thrown. As of `[android.os.Build.VERSION_CODES#LOLLIPOP](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#LOLLIPOP:kotlin.Int)`, this function will not throw a security exception, but will remove whatever permission grants to the Uri had been given to the app (or none). Unlike `[revokeUriPermission(String,Uri,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#revokeUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))`, this method impacts all permission grants matching the given Uri, for any package they had been granted to, through any mechanism this had happened (such as indirectly through the clipboard, activity launch, service start, etc). That means this can be potentially dangerous to use, as it can revoke grants that another app could be strongly expecting to stick around.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[revokeUriPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#revokeUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))(targetPackage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!, uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!, modeFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Remove permissions to access a particular content provider Uri that were previously added with `[grantUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#grantUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))` for a specific target package. The given Uri will match all previously granted Uris that are the same or a sub-path of the given Uri. That is, revoking "content://foo/target" will revoke both "content://foo/target" and "content://foo/target/sub", but not "content://foo". It will not remove any prefix grants that exist at a higher level.  Unlike `[revokeUriPermission(Uri,int)](https://developer.android.com/reference/kotlin/android/content/Context.html#revokeUriPermission\(android.net.Uri,%20kotlin.Int\))`, this method will _only_ revoke permissions that had been explicitly granted through `[grantUriPermission](https://developer.android.com/reference/kotlin/android/content/Context.html#grantUriPermission\(kotlin.String,%20android.net.Uri,%20kotlin.Int\))` and only for the package specified. Any matching grants that have happened through other mechanisms (clipboard, activity launching, service starting, etc) will not be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcast\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Broadcast the given intent to all interested BroadcastReceivers. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run. No results are propagated from receivers and receivers can not abort the broadcast. If you want to allow receivers to propagate results or abort the broadcast, you must send an ordered broadcast using `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcast\(android.content.Intent,%20kotlin.String\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Broadcast the given intent to all interested BroadcastReceivers, allowing an optional required permission to be enforced. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run. No results are propagated from receivers and receivers can not abort the broadcast. If you want to allow receivers to propagate results or abort the broadcast, you must send an ordered broadcast using `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcast\(android.content.Intent,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Broadcast the given intent to all interested BroadcastReceivers, allowing an optional required permission to be enforced. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run. No results are propagated from receivers and receivers can not abort the broadcast. If you want to allow receivers to propagate results or abort the broadcast, you must send an ordered broadcast using `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!)` Version of `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle,%20kotlin.String\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!, receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Version of `[sendBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent,%20kotlin.String\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.Int,%20kotlin.String,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.String,%20android.os.Bundle,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, receiverAppOp: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?)` Broadcast the given intent to all interested BroadcastReceivers, delivering them one at a time to allow more preferred receivers to consume the broadcast before it is delivered to less preferred receivers. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))` that allows you to receive data back from the broadcast. This is accomplished by supplying your own BroadcastReceiver when calling, which will be treated as a final receiver at the end of the broadcast -- its `[BroadcastReceiver.onReceive](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html#onReceive\(android.content.Context,%20android.content.Intent\))` method will be called with the result values collected from the other receivers. The broadcast will be serialized in the same way as calling `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  Like `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))`, this method is asynchronous; it will return before resultReceiver.onReceive() is called.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Broadcast the given intent to all interested BroadcastReceivers, delivering them one at a time to allow more preferred receivers to consume the broadcast before it is delivered to less preferred receivers. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20android.os.Bundle,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))` that allows you to receive data back from the broadcast. This is accomplished by supplying your own BroadcastReceiver when calling, which will be treated as a final receiver at the end of the broadcast -- its `[BroadcastReceiver.onReceive](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html#onReceive\(android.content.Context,%20android.content.Intent\))` method will be called with the result values collected from the other receivers. The broadcast will be serialized in the same way as calling `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  Like `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))`, this method is asynchronous; it will return before resultReceiver.onReceive() is called.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, receiverAppOp: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of `[sendOrderedBroadcast(Intent,String,BroadcastReceiver,Handler,int,String,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))` that allows you to specify the App Op to enforce restrictions on which receivers the broadcast will be sent to.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendOrderedBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendOrderedBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!, receiverPermission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of `[sendOrderedBroadcast(Intent,String,BroadcastReceiver,Handler,int,String,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendStickyBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendStickyBroadcast\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Perform a `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))` that is "sticky," meaning the Intent you are sending stays around after the broadcast is complete, so that others can quickly retrieve that data through the return value of `[registerReceiver(BroadcastReceiver,IntentFilter)](https://developer.android.com/reference/kotlin/android/content/Context.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))`. In all other ways, this behaves the same as `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))`.   
Requires `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendStickyBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendStickyBroadcast\(android.content.Intent,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Perform a `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcast\(android.content.Intent\))` that is "sticky," meaning the Intent you are sending stays around after the broadcast is complete, so that others can quickly retrieve that data through the return value of `[registerReceiver(BroadcastReceiver,IntentFilter)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerReceiver\(android.content.BroadcastReceiver,%20android.content.IntentFilter\))`. In all other ways, this behaves the same as `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendBroadcast\(android.content.Intent\))`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendStickyBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendStickyBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!)` Version of `[sendStickyBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendStickyBroadcast\(android.content.Intent\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS and `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendStickyOrderedBroadcast](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendStickyOrderedBroadcast\(android.content.Intent,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of #sendStickyBroadcast that allows you to receive data back from the broadcast. This is accomplished by supplying your own BroadcastReceiver when calling, which will be treated as a final receiver at the end of the broadcast -- its `[BroadcastReceiver.onReceive](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html#onReceive\(android.content.Context,%20android.content.Intent\))` method will be called with the result values collected from the other receivers. The broadcast will be serialized in the same way as calling `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  Like `[sendBroadcast(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcast\(android.content.Intent\))`, this method is asynchronous; it will return before resultReceiver.onReceive() is called. Note that the sticky data stored is only the data you initially supply to the broadcast, not the result of any changes made by the receivers.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.   
Requires `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendStickyOrderedBroadcastAsUser](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#sendStickyOrderedBroadcastAsUser\(android.content.Intent,%20android.os.UserHandle,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, user: [UserHandle](https://developer.android.com/reference/kotlin/android/os/UserHandle.html)!, resultReceiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)?, scheduler: [Handler](https://developer.android.com/reference/kotlin/android/os/Handler.html)?, initialCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), initialData: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, initialExtras: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Version of `[sendStickyOrderedBroadcast(Intent,BroadcastReceiver,Handler,int,String,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendStickyOrderedBroadcast\(android.content.Intent,%20android.content.BroadcastReceiver,%20android.os.Handler,%20kotlin.Int,%20kotlin.String,%20android.os.Bundle\))` that allows you to specify the user the broadcast will be sent to. This is not available to applications that are not pre-installed on the system image.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.   
Requires android.Manifest.permission.INTERACT_ACROSS_USERS and `[android.Manifest.permission#BROADCAST_STICKY](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#BROADCAST_STICKY:kotlin.String)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[setWallpaper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#setWallpaper\(android.graphics.Bitmap\))(bitmap: [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)!)`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[setWallpaper](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#setWallpaper\(java.io.InputStream\))(data: [InputStream](https://developer.android.com/reference/kotlin/java/io/InputStream.html)!)`  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[shouldShowRequestPermissionRationale](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#shouldShowRequestPermissionRationale\(kotlin.String\))(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Gets whether you should show UI with rationale before requesting a permission. If the permission does not exist on this SDK level or is not visible to this app, the method will return `false`.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startActivities](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startActivities\(kotlin.Array\))(intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!)` Same as `[startActivities(Intent[],Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivities\(kotlin.Array,%20android.os.Bundle\))` with no options specified.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startActivities](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startActivities\(kotlin.Array,%20android.os.Bundle\))(intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Launch multiple new activities. This is generally the same as calling `[startActivity(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent\))` for the first Intent in the array, that activity during its creation calling `[startActivity(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent\))` for the second entry, etc. Note that unlike that approach, generally none of the activities except the last in the array will be created at this point, but rather will be created when the user first visits them (due to pressing back from the activity on top).  This method throws `[ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found for _any_ given Intent. In this case the state of the activity stack is undefined (some Intents in the list may be on it, some not), so you probably want to avoid such situations.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startActivity](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startActivity\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Same as `[startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` with no options specified.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startActivity](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startActivity\(android.content.Intent,%20android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!, options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Launch a new activity. You will not receive any information about when the activity exits.  Note that if this method is being called from outside of an `android.app.Activity` Context, then the Intent must include the `[Intent.FLAG_ACTIVITY_NEW_TASK](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_NEW_TASK:kotlin.Int)` launch flag. This is because, without being started from an existing Activity, there is no existing task in which to place the new activity and thus it needs to be placed in its own separate task.  This method throws `[ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.  
`[ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)?` | `[startForegroundService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startForegroundService\(android.content.Intent\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Similar to `[startService(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#startService\(android.content.Intent\))`, but with an implicit promise that the Service will call `[startForeground(int, android.app.Notification)](https://developer.android.com/reference/kotlin/android/app/Service#startForeground\(kotlin.Int,%20android.app.Notification\))` once it begins running. The service is given an amount of time comparable to the ANR interval to do this, otherwise the system will automatically crash the process, in which case an internal exception `ForegroundServiceDidNotStartInTimeException` is logged on logcat on devices running SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)` or later. On older Android versions, an internal exception `RemoteServiceException` is logged instead, with a corresponding message.  Unlike the ordinary `[startService(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#startService\(android.content.Intent\))`, this method can be used at any time, regardless of whether the app hosting the service is in a foreground state.  **Note:** Beginning with SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, apps targeting SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)` or higher are not allowed to start foreground services from the background. See [ Behavior changes: Apps targeting Android 12 ](https://developer.android.com/reference/kotlin/about/versions/12/behavior-changes-12) for more details.   
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[startInstrumentation](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startInstrumentation\(android.content.ComponentName,%20kotlin.String,%20android.os.Bundle\))(className: [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html), profileFile: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?, arguments: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Start executing an `[android.app.Instrumentation](https://developer.android.com/reference/kotlin/android/app/Instrumentation)` class. The given Instrumentation component will be run by killing its target application (if currently running), starting the target process, instantiating the instrumentation component, and then letting it drive the application.  This function is not synchronous -- it returns as soon as the instrumentation has started and while it is running.  Instrumentation is normally only allowed to run against a package that is either unsigned or signed with a signature that the the instrumentation package is also signed with (ensuring the target trusts the instrumentation).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startIntentSender](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startIntentSender\(android.content.IntentSender,%20android.content.Intent,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int\))(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Same as `[startIntentSender(IntentSender,Intent,int,int,int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startIntentSender\(android.content.IntentSender,%20android.content.Intent,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20android.os.Bundle\))` with no options specified.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[startIntentSender](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startIntentSender\(android.content.IntentSender,%20android.content.Intent,%20kotlin.Int,%20kotlin.Int,%20kotlin.Int,%20android.os.Bundle\))(intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!, fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?, flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?)` Like `[startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))`, but taking a IntentSender to start. If the IntentSender is for an activity, that activity will be started as if you had called the regular `[startActivity(Intent)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent\))` here; otherwise, its associated action will be executed (such as sending a broadcast) as if you had called android.content.IntentSender#sendIntent on it.  
`[ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)?` | `[startService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#startService\(android.content.Intent\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Request that a given application service be started. The Intent should either contain the complete class name of a specific service implementation to start, or a specific package name to target. If the Intent is less specified, it logs a warning about this. In this case any of the multiple matching services may be used. If this service is not already running, it will be instantiated and started (creating a process for it if needed); if it is running then it remains running.  Every call to this method will result in a corresponding call to the target service's `[android.app.Service#onStartCommand](https://developer.android.com/reference/kotlin/android/app/Service#onStartCommand\(android.content.Intent,%20kotlin.Int,%20kotlin.Int\))` method, with the intent given here. This provides a convenient way to submit jobs to a service without having to bind and call on to its interface.  Using startService() overrides the default service lifetime that is managed by #bindService: it requires the service to remain running until `[stopService](https://developer.android.com/reference/kotlin/android/content/Context.html#stopService\(android.content.Intent\))` is called, regardless of whether any clients are connected to it. Note that calls to startService() do not nest: no matter how many times you call startService(), a single call to `[stopService](https://developer.android.com/reference/kotlin/android/content/Context.html#stopService\(android.content.Intent\))` will stop it.  The system attempts to keep running services around as much as possible. The only time they should be stopped is if the current foreground application is using so many resources that the service needs to be killed. If any errors happen in the service's process, it will automatically be restarted.  This function will throw `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` if you do not have permission to start the given service.  **Note:** Each call to startService() results in significant work done by the system to manage service lifecycle surrounding the processing of the intent, which can take multiple milliseconds of CPU time. Due to this cost, startService() should not be used for frequent intent delivery to a service, and only for scheduling significant work. Use #bindService for high frequency calls.  Beginning with SDK Version `[android.os.Build.VERSION_CODES#O](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O:kotlin.Int)`, apps targeting SDK Version `[android.os.Build.VERSION_CODES#O](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O:kotlin.Int)` or higher are not allowed to start background services from the background. See [ Background Execution Limits](https://developer.android.com/reference/kotlin/about/versions/oreo/background) for more details. **Note:** Beginning with SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, apps targeting SDK Version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)` or higher are not allowed to start foreground services from the background. See [ Behavior changes: Apps targeting Android 12 ](https://developer.android.com/reference/kotlin/about/versions/12/behavior-changes-12) for more details.   
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[stopService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#stopService\(android.content.Intent\))(name: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!)` Request that a given application service be stopped. If the service is not running, nothing happens. Otherwise it is stopped. Note that calls to startService() are not counted -- this stops the service no matter how many times it was started.  If the service is running as a foreground service when it is stopped, its associated notification will be removed. To avoid this, apps can use `[stopForeground(STOP_FOREGROUND_DETACH)](https://developer.android.com/reference/kotlin/android/app/Service#stopForeground\(kotlin.Int\))` to decouple the notification from the service's lifecycle before stopping it. Note that if a stopped service still has `[ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html)` objects bound to it with the `[BIND_AUTO_CREATE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_AUTO_CREATE:kotlin.Int)` set, it will not be destroyed until all of these bindings are removed. See the `[android.app.Service](https://developer.android.com/reference/kotlin/android/app/Service)` documentation for more details on a service's lifecycle.  This function will throw `[SecurityException](https://developer.android.com/reference/kotlin/java/lang/SecurityException.html)` if you do not have permission to stop the given service.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[unbindService](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unbindService\(android.content.ServiceConnection\))(conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html))` Disconnect from an application service. You will no longer receive calls as the service is restarted, and the service is now allowed to stop at any time.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[unregisterComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unregisterComponentCallbacks\(android.content.ComponentCallbacks\))(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!)` Remove a `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` object that was previously registered with `[registerComponentCallbacks(ComponentCallbacks)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerComponentCallbacks\(android.content.ComponentCallbacks\))`.  After `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)`, the `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` will be unregistered to `[the base Context](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getBaseContext\(\))`, and can be only used after `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[unregisterDeviceIdChangeListener](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unregisterDeviceIdChangeListener\(java.util.function.IntConsumer\))(listener: [IntConsumer](https://developer.android.com/reference/kotlin/java/util/function/IntConsumer.html))` Removes a device ID changed listener from the Context. It's a no-op if the listener is not already registered.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[unregisterReceiver](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unregisterReceiver\(android.content.BroadcastReceiver\))(receiver: [BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)!)` Unregister a previously registered BroadcastReceiver. _All_ filters that have been registered for this BroadcastReceiver will be removed.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[updateServiceBindings](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#updateServiceBindings\(kotlin.collections.MutableCollection\))(params: [MutableCollection](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-collection/index.html)<[Context.UpdateBindingParams](https://developer.android.com/reference/kotlin/android/content/Context.UpdateBindingParams.html)!>)` Perform a batch update of existing bindings. Existing bindings can be rebound with an updated set of flags, or unbound. Only flags returned from `[getUpdateableFlags](https://developer.android.com/reference/kotlin/android/content/Context.html#getUpdateableFlags\(\))` may be added or removed.  This API behaves as if the `[rebindService(ServiceConnection,BindServiceFlags)](https://developer.android.com/reference/kotlin/android/content/Context.html#rebindService\(android.content.ServiceConnection,%20android.content.Context.BindServiceFlags\))` and `[unbindService(ServiceConnection)](https://developer.android.com/reference/kotlin/android/content/Context.html#unbindService\(android.content.ServiceConnection\))` API are called in the same order as the params are iterated.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[updateServiceGroup](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#updateServiceGroup\(android.content.ServiceConnection,%20kotlin.Int,%20kotlin.Int\))(conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html), group: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), importance: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` For a service previously bound with #bindService or a related method, change how the system manages that service's process in relation to other processes. This doesn't modify the original bind flags that were passed in when binding, but adjusts how the process will be managed in some cases based on those flags. Currently only works on isolated processes (will be ignored for non-isolated processes).  Note that this call does not take immediate effect, but will be applied the next time the impacted process is adjusted for some other reason. Typically you would call this before then calling a new #bindIsolatedService on the service of interest, with that binding causing the process to be shuffled accordingly.  
  
From class `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` | `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `[bindIsolatedService](https://developer.android.com/reference/kotlin/android/content/Context.html#bindIsolatedService\(android.content.Intent,%20android.content.Context.BindServiceFlags,%20kotlin.String,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))(service: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), flags: [Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html), instanceName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html), executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html), conn: [ServiceConnection](https://developer.android.com/reference/kotlin/android/content/ServiceConnection.html))` See `[bindIsolatedService(Intent,int,String,Executor,ServiceConnection)](https://developer.android.com/reference/kotlin/android/content/Context.html#bindIsolatedService\(android.content.Intent,%20kotlin.Int,%20kotlin.String,%20java.util.concurrent.Executor,%20android.content.ServiceConnection\))` Call `[BindServiceFlags.of(long)](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html#of\(kotlin.Long\))` to obtain a BindServiceFlags object.  
---|---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | `[getColor](https://developer.android.com/reference/kotlin/android/content/Context.html#getColor\(kotlin.Int\))(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Returns a color associated with a particular resource ID and styled for the current theme.  
`[ColorStateList](https://developer.android.com/reference/kotlin/android/content/res/ColorStateList.html)` | `[getColorStateList](https://developer.android.com/reference/kotlin/android/content/Context.html#getColorStateList\(kotlin.Int\))(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Returns a color state list associated with a particular resource ID and styled for the current theme.  
`[Drawable](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable.html)?` | `[getDrawable](https://developer.android.com/reference/kotlin/android/content/Context.html#getDrawable\(kotlin.Int\))(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Returns a drawable object associated with a particular resource ID and styled for the current theme.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[getString](https://developer.android.com/reference/kotlin/android/content/Context.html#getString\(kotlin.Int\))(resId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Returns a localized string from the application's package's default string table.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | `[getString](https://developer.android.com/reference/kotlin/android/content/Context.html#getString\(kotlin.Int,%20kotlin.Any\))(resId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), vararg formatArgs: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!)` Returns a localized formatted string from the application's package's default string table, substituting the format arguments as defined in `[java.util.Formatter](https://developer.android.com/reference/kotlin/java/util/Formatter.html)` and java.lang.String#format.  
`T` | `[getSystemService](https://developer.android.com/reference/kotlin/android/content/Context.html#getSystemService\(java.lang.Class\))(serviceClass: [Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)<T>)` Return the handle to a system-level service by class.  Currently available classes are: `[android.view.WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)`, `[android.view.LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)`, `[android.app.ActivityManager](https://developer.android.com/reference/kotlin/android/app/ActivityManager)`, `[android.os.PowerManager](https://developer.android.com/reference/kotlin/android/os/PowerManager.html)`, `[android.app.AlarmManager](https://developer.android.com/reference/kotlin/android/app/AlarmManager)`, `[android.app.NotificationManager](https://developer.android.com/reference/kotlin/android/app/NotificationManager)`, `[android.app.KeyguardManager](https://developer.android.com/reference/kotlin/android/app/KeyguardManager)`, `[android.location.LocationManager](https://developer.android.com/reference/kotlin/android/location/LocationManager.html)`, `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)`, `[android.os.Vibrator](https://developer.android.com/reference/kotlin/android/os/Vibrator.html)`, `[android.net.ConnectivityManager](https://developer.android.com/reference/kotlin/android/net/ConnectivityManager.html)`, `[android.net.wifi.WifiManager](https://developer.android.com/reference/kotlin/android/net/wifi/WifiManager.html)`, `[android.media.AudioManager](https://developer.android.com/reference/kotlin/android/media/AudioManager.html)`, `[android.media.MediaRouter](https://developer.android.com/reference/kotlin/android/media/MediaRouter.html)`, `[android.telephony.TelephonyManager](https://developer.android.com/reference/kotlin/android/telephony/TelephonyManager.html)`, `[android.telephony.SubscriptionManager](https://developer.android.com/reference/kotlin/android/telephony/SubscriptionManager.html)`, `[android.view.inputmethod.InputMethodManager](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager.html)`, `[android.app.UiModeManager](https://developer.android.com/reference/kotlin/android/app/UiModeManager)`, `[android.app.DownloadManager](https://developer.android.com/reference/kotlin/android/app/DownloadManager)`, `[android.os.BatteryManager](https://developer.android.com/reference/kotlin/android/os/BatteryManager.html)`, `[android.app.job.JobScheduler](https://developer.android.com/reference/kotlin/android/app/job/JobScheduler)`, `[android.app.usage.NetworkStatsManager](https://developer.android.com/reference/kotlin/android/app/usage/NetworkStatsManager)`, `[android.content.pm.verify.domain.DomainVerificationManager](https://developer.android.com/reference/kotlin/android/content/pm/verify/domain/DomainVerificationManager.html)`, `[android.view.displayhash.DisplayHashManager](https://developer.android.com/reference/kotlin/android/view/displayhash/DisplayHashManager.html)` `[android.security.authenticationpolicy.AuthenticationPolicyManager](https://developer.android.com/reference/kotlin/android/security/authenticationpolicy/AuthenticationPolicyManager.html)`.  Note: System services obtained via this API may be closely associated with the Context in which they are obtained from. In general, do not share the service objects between various different contexts (Activities, Applications, Services, Providers, etc.)  Note: Instant apps, for which `[PackageManager.isInstantApp()](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#isInstantApp\(\))` returns true, don't have access to the following system services: `[DEVICE_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_POLICY_SERVICE:kotlin.String)`, #FINGERPRINT_SERVICE, `[KEYGUARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYGUARD_SERVICE:kotlin.String)`, `[SHORTCUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SHORTCUT_SERVICE:kotlin.String)`, `[USB_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USB_SERVICE:kotlin.String)`, `[WALLPAPER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WALLPAPER_SERVICE:kotlin.String)`, `[WIFI_P2P_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_P2P_SERVICE:kotlin.String)`, `[WIFI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_SERVICE:kotlin.String)`, `[WIFI_AWARE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_AWARE_SERVICE:kotlin.String)`. For these services this method will return `null`. Generally, if you are running as an instant app you should always check whether the result of this method is `null`.   
`[CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)` | `[getText](https://developer.android.com/reference/kotlin/android/content/Context.html#getText\(kotlin.Int\))(resId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Return a localized, styled CharSequence from the application's package's default string table.  
`[Context.BindServiceFlags](https://developer.android.com/reference/kotlin/android/content/Context.BindServiceFlags.html)` | `[getUpdateableFlags](https://developer.android.com/reference/kotlin/android/content/Context.html#getUpdateableFlags\(\))()` Gets the list of bind flags that may be updated (i.e. added or removed) for an existing connection. Includes: 

  * `[BIND_NOT_FOREGROUND](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_NOT_FOREGROUND:kotlin.Int)`
  * `[BIND_ABOVE_CLIENT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ABOVE_CLIENT:kotlin.Int)`
  * `[BIND_ALLOW_OOM_MANAGEMENT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ALLOW_OOM_MANAGEMENT:kotlin.Int)`
  * `[BIND_WAIVE_PRIORITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_WAIVE_PRIORITY:kotlin.Int)`
  * `[BIND_IMPORTANT](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_IMPORTANT:kotlin.Int)`
  * `[BIND_ADJUST_WITH_ACTIVITY](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_ADJUST_WITH_ACTIVITY:kotlin.Int)`
  * `[BIND_NOT_PERCEPTIBLE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIND_NOT_PERCEPTIBLE:kotlin.Int)`

  
`[TypedArray](https://developer.android.com/reference/kotlin/android/content/res/TypedArray.html)` | `[obtainStyledAttributes](https://developer.android.com/reference/kotlin/android/content/Context.html#obtainStyledAttributes\(android.util.AttributeSet,%20kotlin.IntArray\))(set: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html)?, attrs: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html))` Retrieve styled attribute information in this Context's theme. See `[android.content.res.Resources.Theme.obtainStyledAttributes(AttributeSet,int[],int,int)](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html#obtainStyledAttributes\(android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int\))` for more information.  
`[TypedArray](https://developer.android.com/reference/kotlin/android/content/res/TypedArray.html)` | `[obtainStyledAttributes](https://developer.android.com/reference/kotlin/android/content/Context.html#obtainStyledAttributes\(android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int\))(set: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html)?, attrs: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html), defStyleAttr: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), defStyleRes: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html))` Retrieve styled attribute information in this Context's theme. See `[android.content.res.Resources.Theme.obtainStyledAttributes(AttributeSet,int[],int,int)](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html#obtainStyledAttributes\(android.util.AttributeSet,%20kotlin.IntArray,%20kotlin.Int,%20kotlin.Int\))` for more information.  
`[TypedArray](https://developer.android.com/reference/kotlin/android/content/res/TypedArray.html)` | `[obtainStyledAttributes](https://developer.android.com/reference/kotlin/android/content/Context.html#obtainStyledAttributes\(kotlin.Int,%20kotlin.IntArray\))(resid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html), attrs: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html))` Retrieve styled attribute information in this Context's theme. See `[android.content.res.Resources.Theme#obtainStyledAttributes(int,int[])](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html#obtainStyledAttributes\(kotlin.Int,%20kotlin.IntArray\))` for more information.  
`[TypedArray](https://developer.android.com/reference/kotlin/android/content/res/TypedArray.html)` | `[obtainStyledAttributes](https://developer.android.com/reference/kotlin/android/content/Context.html#obtainStyledAttributes\(kotlin.IntArray\))(attrs: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html))` Retrieve styled attribute information in this Context's theme. See `[android.content.res.Resources.Theme#obtainStyledAttributes(int[])](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html#obtainStyledAttributes\(kotlin.IntArray\))` for more information.  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[revokeSelfPermissionOnKill](https://developer.android.com/reference/kotlin/android/content/Context.html#revokeSelfPermissionOnKill\(kotlin.String\))(permName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` Triggers the asynchronous revocation of a runtime permission. If the permission is not currently granted, nothing happens (even if later granted by the user).  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[sendBroadcastWithMultiplePermissions](https://developer.android.com/reference/kotlin/android/content/Context.html#sendBroadcastWithMultiplePermissions\(android.content.Intent,%20kotlin.Array\))(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html), receiverPermissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>)` Broadcast the given intent to all interested BroadcastReceivers, allowing an array of required permissions to be enforced. This call is asynchronous; it returns immediately, and you will continue executing while the receivers are run. No results are propagated from receivers and receivers can not abort the broadcast. If you want to allow receivers to propagate results or abort the broadcast, you must send an ordered broadcast using `[sendOrderedBroadcast(Intent,String)](https://developer.android.com/reference/kotlin/android/content/Context.html#sendOrderedBroadcast\(android.content.Intent,%20kotlin.String\))`.  See `[BroadcastReceiver](https://developer.android.com/reference/kotlin/android/content/BroadcastReceiver.html)` for more information on Intent broadcasts.  
  
From class `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[onConfigurationChanged](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html#onConfigurationChanged\(android.content.res.Configuration\))(newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html))` Called by the system when the device configuration changes while your component is running. Note that, unlike activities, other components are never restarted when a configuration changes: they must always deal with the results of the change, such as by re-retrieving resources.  At the time that this function has been called, your Resources object will have been updated to return resource values matching the new configuration.  For more information, read [Handling Runtime Changes](https://developer.android.com/guide/topics/resources/runtime-changes.html).  
---|---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[onLowMemory](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html#onLowMemory\(\))()` This is called when the overall system is running low on memory, and actively running processes should trim their memory usage. While the exact point at which this will be called is not defined, generally it will happen when all background process have been killed. That is, before reaching the point of killing processes hosting service and foreground UI that we would like to avoid killing.  
  
From class `[Callback](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html)` | `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` | `[onPointerCaptureChanged](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onPointerCaptureChanged\(kotlin.Boolean\))(hasCapture: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html))` Called when pointer capture is enabled or disabled for the current window.  
---|---  
  
Properties  
---  
static [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)! |  `FOCUSED_STATE_SET`  
  
## Constants

### DEFAULT_KEYS_DIALER

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val DEFAULT_KEYS_DIALER: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Use with `setDefaultKeyMode` to launch the dialer during default key handling.
    
    
    Value: 1

**See Also**

  * `#setDefaultKeyMode`



### DEFAULT_KEYS_DISABLE

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val DEFAULT_KEYS_DISABLE: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Use with `setDefaultKeyMode` to turn off default handling of keys.
    
    
    Value: 0

**See Also**

  * `#setDefaultKeyMode`



### DEFAULT_KEYS_SEARCH_GLOBAL

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val DEFAULT_KEYS_SEARCH_GLOBAL: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Use with `setDefaultKeyMode` to specify that unhandled keystrokes will start a global search (typically web search, but some platforms may define alternate methods for global search) 

See `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)` for more details.
    
    
    Value: 4

**See Also**

  * `#setDefaultKeyMode`



### DEFAULT_KEYS_SEARCH_LOCAL

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val DEFAULT_KEYS_SEARCH_LOCAL: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Use with `setDefaultKeyMode` to specify that unhandled keystrokes will start an application-defined search. (If the application or activity does not actually define a search, the keys will be ignored.) 

See `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)` for more details.
    
    
    Value: 3

**See Also**

  * `#setDefaultKeyMode`



### DEFAULT_KEYS_SHORTCUT

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val DEFAULT_KEYS_SHORTCUT: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Use with `setDefaultKeyMode` to execute a menu shortcut in default key handling. 

That is, the user does not need to hold down the menu key to execute menu shortcuts.
    
    
    Value: 2

**See Also**

  * `#setDefaultKeyMode`



### FULLSCREEN_MODE_REQUEST_ENTER

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val FULLSCREEN_MODE_REQUEST_ENTER: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Request type of `requestFullscreenMode(int,OutcomeReceiver)`, to request enter fullscreen mode from multi-window mode.
    
    
    Value: 1

### FULLSCREEN_MODE_REQUEST_EXIT

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val FULLSCREEN_MODE_REQUEST_EXIT: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Request type of `requestFullscreenMode(int,OutcomeReceiver)`, to request exiting the requested fullscreen mode and restore to the previous multi-window mode.
    
    
    Value: 0

### OVERRIDE_TRANSITION_CLOSE

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val OVERRIDE_TRANSITION_CLOSE: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Request type of `overrideActivityTransition(int,int,int)` or `overrideActivityTransition(int,int,int,int)`, to override the closing transition.
    
    
    Value: 1

### OVERRIDE_TRANSITION_OPEN

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val OVERRIDE_TRANSITION_OPEN: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Request type of `overrideActivityTransition(int,int,int)` or `overrideActivityTransition(int,int,int,int)`, to override the opening transition.
    
    
    Value: 0

### RESULT_CANCELED

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val RESULT_CANCELED: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Standard activity result: operation canceled.
    
    
    Value: 0

### RESULT_FIRST_USER

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val RESULT_FIRST_USER: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Start of user-defined activity results.
    
    
    Value: 1

### RESULT_OK

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    static val RESULT_OK: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Standard activity result: operation succeeded.
    
    
    Value: -1

## Public constructors

### Activity
    
    
    Activity()

## Public methods

### addContentView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun addContentView(  
        view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!,   
        params: [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add an additional content view to the activity. Added after any existing ones in the activity -- existing views are NOT removed.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The desired content to display.  
`params` | [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!: Layout parameters for the view.  
  
### clearOverrideActivityTransition

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun clearOverrideActivityTransition(overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Clears the animations which are set from #overrideActivityTransition.

Parameters  
---  
`overrideType` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): `OVERRIDE_TRANSITION_OPEN` clear the animation set for starting a new activity. `OVERRIDE_TRANSITION_CLOSE` clear the animation set for finishing an activity.   
Value is one of the following: 

  * `OVERRIDE_TRANSITION_OPEN`
  * `OVERRIDE_TRANSITION_CLOSE`

  
  
**See Also**

  * `#overrideActivityTransition(int,int,int)`
  * `#overrideActivityTransition(int,int,int,int)`



### closeContextMenu

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun closeContextMenu(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Programmatically closes the most recently opened context menu, if showing.

### closeOptionsMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun closeOptionsMenu(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Progammatically closes the options menu. If the options menu is already closed, this method does nothing.

### createPendingResult

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun createPendingResult(  
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html),   
        flags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [PendingIntent](https://developer.android.com/reference/kotlin/android/app/PendingIntent)!

Create a new PendingIntent object which you can hand to others for them to use to send result data back to your #onActivityResult callback. The created object will be either one-shot (becoming invalid after a result is sent back) or multiple (allowing any number of results to be sent through it).

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Private request code for the sender that will be associated with the result data when it is returned. The sender can not modify this value, allowing you to identify incoming results.  
`data` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): Default data to supply in the result, which may be modified by the sender.   
This value cannot be `null`.  
`flags` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): May be `[PendingIntent.FLAG_ONE_SHOT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_ONE_SHOT:kotlin.Int)`, `[PendingIntent.FLAG_NO_CREATE](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_NO_CREATE:kotlin.Int)`, `[PendingIntent.FLAG_CANCEL_CURRENT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_CANCEL_CURRENT:kotlin.Int)`, `[PendingIntent.FLAG_UPDATE_CURRENT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_UPDATE_CURRENT:kotlin.Int)`, or any of the flags as supported by `[Intent.fillIn()](https://developer.android.com/reference/kotlin/android/content/Intent.html#fillIn\(android.content.Intent,%20kotlin.Int\))` to control which unspecified parts of the intent that can be supplied when the actual send happens.   
Value is either `0` or a combination of the following: 

  * `[android.app.PendingIntent#FLAG_ONE_SHOT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_ONE_SHOT:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_NO_CREATE](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_NO_CREATE:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_CANCEL_CURRENT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_CANCEL_CURRENT:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_UPDATE_CURRENT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_UPDATE_CURRENT:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_IMMUTABLE](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_IMMUTABLE:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_MUTABLE](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_MUTABLE:kotlin.Int)`
  * `[android.app.PendingIntent#FLAG_ALLOW_UNSAFE_IMPLICIT_INTENT](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_ALLOW_UNSAFE_IMPLICIT_INTENT:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_ACTION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_ACTION:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_DATA](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_DATA:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_CATEGORIES](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_CATEGORIES:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_COMPONENT](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_COMPONENT:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_PACKAGE](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_PACKAGE:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_SOURCE_BOUNDS](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_SOURCE_BOUNDS:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_SELECTOR](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_SELECTOR:kotlin.Int)`
  * `[android.content.Intent#FILL_IN_CLIP_DATA](https://developer.android.com/reference/kotlin/android/content/Intent.html#FILL_IN_CLIP_DATA:kotlin.Int)`

  
Return  
---  
`[PendingIntent](https://developer.android.com/reference/kotlin/android/app/PendingIntent)!` | Returns an existing or new PendingIntent matching the given parameters. May return null only if `[PendingIntent.FLAG_NO_CREATE](https://developer.android.com/reference/kotlin/android/app/PendingIntent#FLAG_NO_CREATE:kotlin.Int)` has been supplied.  
  
**See Also**

  * `[android.app.PendingIntent](https://developer.android.com/reference/kotlin/android/app/PendingIntent)`



### dismissDialog

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~dismissDialog~~(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Dismiss a dialog that was previously shown via `showDialog(int)`.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id of the managed dialog.  
Exceptions  
---  
`java.lang.IllegalArgumentException` | if the id was not previously shown via `showDialog(int)`.  
  
**See Also**

  * `#onCreateDialog(int,android.os.Bundle)`
  * `#onPrepareDialog(int,android.app.Dialog,android.os.Bundle)`
  * `#showDialog(int)`
  * `#removeDialog(int)`



### dismissKeyboardShortcutsHelper

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun dismissKeyboardShortcutsHelper(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Dismiss the Keyboard Shortcuts screen.

### dispatchGenericMotionEvent

Added in [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchGenericMotionEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process generic motion events. You can override this to intercept all generic motion events before they are dispatched to the window. Be sure to call this implementation for generic motion events that should be handled normally.

Parameters  
---  
`event` | The generic motion event.  
`ev` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The generic motion event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true if this event was consumed.  
  
**See Also**

  * `#onGenericMotionEvent(android.view.MotionEvent)`



### dispatchKeyEvent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchKeyEvent(event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process key events. You can override this to intercept all key events before they are dispatched to the window. Be sure to call this implementation for key events that should be handled normally.

Parameters  
---  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: The key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true if this event was consumed.  
  
### dispatchKeyShortcutEvent

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchKeyShortcutEvent(event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process a key shortcut event. You can override this to intercept all key shortcut events before they are dispatched to the window. Be sure to call this implementation for key shortcut events that should be handled normally.

Parameters  
---  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: The key shortcut event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if this event was consumed.  
  
### dispatchPopulateAccessibilityEvent

Added in [API level 4](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchPopulateAccessibilityEvent(event: [AccessibilityEvent](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process population of `[AccessibilityEvent](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityEvent.html)`s.

Parameters  
---  
`event` | [AccessibilityEvent](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityEvent.html)!: The event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true if event population was completed.  
  
### dispatchTouchEvent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchTouchEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process touch screen events. You can override this to intercept all touch screen events before they are dispatched to the window. Be sure to call this implementation for touch screen events that should be handled normally.

Parameters  
---  
`event` | The touch screen event.  
`ev` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The touch screen event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true if this event was consumed.  
  
**See Also**

  * `#onTouchEvent(android.view.MotionEvent)`



### dispatchTrackballEvent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dispatchTrackballEvent(ev: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called to process trackball events. You can override this to intercept all trackball events before they are dispatched to the window. Be sure to call this implementation for trackball events that should be handled normally.

Parameters  
---  
`event` | The trackball event.  
`ev` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The trackball event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true if this event was consumed.  
  
**See Also**

  * `#onTrackballEvent(android.view.MotionEvent)`



### dump

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun dump(  
        prefix: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),   
        fd: [FileDescriptor](https://developer.android.com/reference/kotlin/java/io/FileDescriptor.html)?,   
        writer: [PrintWriter](https://developer.android.com/reference/kotlin/java/io/PrintWriter.html),   
        args: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Print the Activity's state into the given stream. This gets invoked if you run `adb shell dumpsys activity <activity_component_name>`. 

This method won't be called if the app targets `[android.os.Build.VERSION_CODES#TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)` or later if the dump request starts with one of the following arguments: 

  * \--autofill 
  * \--contentcapture 
  * \--translation 
  * \--list-dumpables 
  * \--dump-dumpable 

Parameters  
---  
`prefix` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): Desired prefix to prepend at each line of output.   
This value cannot be `null`.  
`fd` | [FileDescriptor](https://developer.android.com/reference/kotlin/java/io/FileDescriptor.html)?: The raw file descriptor that the dump is being sent to.   
This value may be `null`.  
`writer` | [PrintWriter](https://developer.android.com/reference/kotlin/java/io/PrintWriter.html): The PrintWriter to which you should dump your state. This will be closed for you after you return.   
This value cannot be `null`.  
`args` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>?: additional arguments to the dump request.   
This value may be `null`.  
  
### enterPictureInPictureMode

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~enterPictureInPictureMode~~(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Deprecated in Java._

Puts the activity in picture-in-picture mode if possible in the current system state. Any prior calls to `setPictureInPictureParams(PictureInPictureParams)` will still apply when entering picture-in-picture through this call.

**See Also**

  * `#enterPictureInPictureMode(android.app.PictureInPictureParams)`
  * `[android.R.attr#supportsPictureInPicture](https://developer.android.com/reference/kotlin/android/R.attr.html#supportsPictureInPicture:kotlin.Int)`



### enterPictureInPictureMode

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun enterPictureInPictureMode(params: [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Puts the activity in picture-in-picture mode if possible in the current system state. The set parameters in `params` will be combined with the parameters from prior calls to `setPictureInPictureParams(PictureInPictureParams)`. The system may disallow entering picture-in-picture in various cases, including when the activity is not visible, if the screen is locked or if the user has an activity pinned. 

By default, system calculates the dimension of picture-in-picture window based on the given `params`. See [Picture-in-picture Support](https://developer.android.com/guide/topics/ui/picture-in-picture) on how to override this behavior.

Parameters  
---  
`params` | [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams): non-null parameters to be combined with previously set parameters when entering picture-in-picture.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if the system successfully put this activity into picture-in-picture mode or was already in picture-in-picture mode (see `isInPictureInPictureMode()`). If the device does not support picture-in-picture, return false.  
  
**See Also**

  * `[android.R.attr#supportsPictureInPicture](https://developer.android.com/reference/kotlin/android/R.attr.html#supportsPictureInPicture:kotlin.Int)`
  * `[android.app.PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams)`



### findViewById

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun <T : [View](https://developer.android.com/reference/kotlin/android/view/View.html)!> findViewById(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): T

Finds a view that was identified by the `android:id` XML attribute that was processed in #onCreate. 

**Note:** In most cases -- depending on compiler support -- the resulting view is automatically cast to the target class type. If the target class type is unconstrained, an explicit cast may be necessary.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): the ID to search for  
Return  
---  
`T` | a view with given ID if found, or `null` otherwise  
  
**See Also**

  * `[android.view.View#findViewById(int)](https://developer.android.com/reference/kotlin/android/view/View.html#findViewById\(kotlin.Int\))`
  * `#requireViewById(int)`



### finish

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun finish(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Call this when your activity is done and should be closed. The ActivityResult is propagated back to whoever launched you via onActivityResult().

### finishActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun finishActivity(requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Force finish another activity that you had previously started with #startActivityForResult.

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The request code of the activity that you had given to startActivityForResult(). If there are multiple activities started with this request code, they will all be finished.  
  
### finishActivityFromChild

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~finishActivityFromChild~~(  
        child: Activity,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`finishActivity(int)` instead._

This is called when a child activity of this one calls its finishActivity().

Parameters  
---  
`child` | Activity: The activity making the call.   
This value cannot be `null`.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Request code that had been used to start the activity.  
  
### finishAffinity

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun finishAffinity(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Finish this activity as well as all activities immediately below it in the current task that have the same affinity. This is typically used when an application can be launched on to another task (such as from an ACTION_VIEW of a content type it understands) and the user has used the up navigation to switch out of the current task and in to its own task. In this case, if the user has navigated down into any other activities of the second application, all of those should be removed from the original task as part of the task switch. 

Note that this finish does _not_ allow you to deliver results to the previous activity, and an exception will be thrown if you are trying to do so.

### finishAfterTransition

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun finishAfterTransition(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Reverses the Activity Scene entry Transition and triggers the calling Activity to reverse its exit Transition. When the exit Transition completes, `finish()` is called. If no entry Transition was used, finish() is called immediately and the Activity exit Transition is run.

**See Also**

  * `[android.app.ActivityOptions#makeSceneTransitionAnimation(android.app.Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`



### finishAndRemoveTask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun finishAndRemoveTask(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Call this when your activity is done and should be closed and the task should be completely removed as a part of finishing the root activity of the task.

### finishFromChild

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~finishFromChild~~(child: Activity!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`finish()` instead._

This is called when a child activity of this one calls its `finish` method. The default implementation simply calls finish() on this activity (the parent), finishing the entire group.

Parameters  
---  
`child` | Activity!: The activity making the call.  
  
**See Also**

  * `#finish`



### getActionBar

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getActionBar(): [ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)?

Retrieve a reference to this activity's ActionBar.

Return  
---  
`[ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)?` | The Activity's ActionBar, or null if it does not have one.  
  
### getApplication

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getApplication(): [Application](https://developer.android.com/reference/kotlin/android/app/Application)!

Return the application that owns this activity.

### getCaller

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getCaller(): [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)?

Returns the ComponentCaller instance of the app that started this activity. 

To keep the ComponentCaller instance for future use, call `setIntent(Intent,ComponentCaller)`, and use this method to retrieve it. 

Note that in #onNewIntent, this method will return the original ComponentCaller. You can use `setIntent(Intent,ComponentCaller)` to update it to the new ComponentCaller.

Return  
---  
`[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)?` | `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` instance corresponding to the intent from `getIntent()`, or `null` if the activity was not launched with that intent  
  
**See Also**

  * `[android.app.ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)`
  * `#getIntent`
  * `#setIntent(android.content.Intent,android.app.ComponentCaller)`



### getCallingActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getCallingActivity(): [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)?

Return the name of the activity that invoked this activity. This is who the data in #setResult will be sent to. You can use this information to validate that the recipient is allowed to receive the data. 

Note: if the calling activity is not expecting a result (that is it did not use the #startActivityForResult form that includes a request code), then the calling package will be null.

Return  
---  
`[ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)?` | The ComponentName of the activity that will receive your reply, or null if none.  
  
### getCallingPackage

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getCallingPackage(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Return the name of the package that invoked this activity. This is who the data in #setResult will be sent to. You can use this information to validate that the recipient is allowed to receive the data. 

Note: if the calling activity is not expecting a result (that is it did not use the #startActivityForResult form that includes a request code), then the calling package will be null.

Note: prior to `[android.os.Build.VERSION_CODES#JELLY_BEAN_MR2](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#JELLY_BEAN_MR2:kotlin.Int)`, the result from this method was unstable. If the process hosting the calling package was no longer running, it would return null instead of the proper package name. You can use `getCallingActivity()` and retrieve the package name from that instead.

Return  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` | The package of the activity that will receive your reply, or null if none.  
  
### getChangingConfigurations

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getChangingConfigurations(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

If this activity is being destroyed because it can not handle a configuration parameter being changed (and thus its `onConfigurationChanged(Configuration)` method is _not_ being called), then you can use this method to discover the set of changes that have occurred while in the process of being destroyed. Note that there is no guarantee that these will be accurate (other changes could have happened at any time), so you should only use this as an optimization hint.

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | Returns a bit field of the configuration parameters that are changing, as defined by the `[android.content.res.Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)` class.  
  
### getComponentName

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getComponentName(): [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)!

Returns the complete component name of this activity.

Return  
---  
`[ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)!` | Returns the complete component name for this activity  
  
### getContentScene

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getContentScene(): [Scene](https://developer.android.com/reference/kotlin/android/transition/Scene.html)!

Retrieve the `[Scene](https://developer.android.com/reference/kotlin/android/transition/Scene.html)` representing this window's current content. Requires `[Window.FEATURE_CONTENT_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_CONTENT_TRANSITIONS:kotlin.Int)`. 

This method will return null if the current content is not represented by a Scene.

Return  
---  
`[Scene](https://developer.android.com/reference/kotlin/android/transition/Scene.html)!` | Current Scene being shown or null  
  
### getContentTransitionManager

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getContentTransitionManager(): [TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)!

Retrieve the `[TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)` responsible for default transitions in this window. Requires `[Window.FEATURE_CONTENT_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_CONTENT_TRANSITIONS:kotlin.Int)`. 

This method will return non-null after content has been initialized (e.g. by using #setContentView) if `[Window.FEATURE_CONTENT_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_CONTENT_TRANSITIONS:kotlin.Int)` has been granted.

Return  
---  
`[TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)!` | This window's content TransitionManager or null if none is set.  
  
### getCurrentCaller

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getCurrentCaller(): [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)

Returns the ComponentCaller instance of the app that re-launched this activity with a new intent via #onNewIntent or #onActivityResult. 

Note that this method only works within the #onNewIntent and #onActivityResult methods. If you call this method outside #onNewIntent and #onActivityResult, it will throw an `[IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)`. 

You can also retrieve the caller if you override `onNewIntent(Intent,ComponentCaller)` or `onActivityResult(int,int,Intent,ComponentCaller)`. 

To keep the ComponentCaller instance for future use, call `setIntent(Intent,ComponentCaller)`, and use `getCaller` to retrieve it.

Return  
---  
`[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` | `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` instance.   
This value cannot be `null`.  
Exceptions  
---  
`java.lang.IllegalStateException` | if the caller is `null`, indicating the method was called outside #onNewIntent  
  
**See Also**

  * `[android.app.ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)`
  * `#setIntent(android.content.Intent,android.app.ComponentCaller)`
  * `#getCaller`



### getCurrentFocus

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getCurrentFocus(): [View](https://developer.android.com/reference/kotlin/android/view/View.html)?

Calls `[android.view.Window#getCurrentFocus](https://developer.android.com/reference/kotlin/android/view/Window.html#getCurrentFocus\(\))` on the Window of this Activity to return the currently focused view.

Return  
---  
`[View](https://developer.android.com/reference/kotlin/android/view/View.html)?` | View The current View with focus or null.  
  
**See Also**

  * `#getWindow`
  * `[android.view.Window#getCurrentFocus](https://developer.android.com/reference/kotlin/android/view/Window.html#getCurrentFocus\(\))`



### getFragmentManager

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~getFragmentManager~~(): [FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)!

**Deprecated:**_Use androidx.fragment.app.FragmentActivity#getSupportFragmentManager()_

Return the FragmentManager for interacting with fragments associated with this activity.

### getInitialCaller

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getInitialCaller(): [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)

Returns the ComponentCaller instance of the app that initially launched this activity. 

Note that calls to #onNewIntent and #setIntent have no effect on the returned value of this method.

Return  
---  
`[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` | `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` instance.   
This value cannot be `null`.  
  
**See Also**

  * `[android.app.ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)`



### getIntent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getIntent(): [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!

Returns the intent that started this activity. 

To keep the Intent instance for future use, call `setIntent(Intent)`, and use this method to retrieve it. 

Note that in #onNewIntent, this method will return the original Intent. You can use `setIntent(Intent)` to update it to the new Intent.

Return  
---  
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!` | `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)` instance that started this activity, or that was kept for future use  
  
### getLastNonConfigurationInstance

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getLastNonConfigurationInstance(): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?

Retrieve the non-configuration instance data that was previously returned by `onRetainNonConfigurationInstance()`. This will be available from the initial #onCreate and `onStart` calls to the new instance, allowing you to extract any useful dynamic state from the previous instance. 

Note that the data you retrieve here should _only_ be used as an optimization for handling configuration changes. You should always be able to handle getting a null pointer back, and an activity must still be able to restore itself to its previous state (through the normal `onSaveInstanceState(Bundle)` mechanism) even if this function returns null. 

**Note:** For most cases you should use the `[Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment)` API `[Fragment.setRetainInstance(boolean)](https://developer.android.com/reference/kotlin/android/app/Fragment#setRetainInstance\(kotlin.Boolean\))` instead; this is also available on older platforms through the Android support libraries.

Return  
---  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)?` | the object previously returned by `onRetainNonConfigurationInstance()`  
  
### getLaunchedFromPackage

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getLaunchedFromPackage(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

Returns the package name of the app that initially launched this activity. 

In order to receive the launching app's package name, at least one of the following has to be met: 

  * The app must call `[ActivityOptions.setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))` with a value of `true` and launch this activity with the resulting `ActivityOptions`. 
  * The launched activity has the same uid as the launching app. 
  * The launched activity is running in a package that is signed with the same key used to sign the platform (typically only system packages such as Settings will meet this requirement). 
  * Starting in `[Build.VERSION_CODES.CINNAMON_BUN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#CINNAMON_BUN:kotlin.Int)`, the activity was launched directly with `Activity.startActivityForResult(Intent,int)`. 

. These are the same requirements for `getLaunchedFromUid()`; if any of these are met, then these methods can be used to obtain the uid and package name of the launching app. If none are met, then `null` is returned. 

Note, if an activity is launched via `startActivityForResult(Intent,int)` but the launch is intercepted and forwarded by an intermediate app using `[Intent.FLAG_ACTIVITY_FORWARD_RESULT](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_FORWARD_RESULT:kotlin.Int)`, the identity of the intermediate app will not be implicitly shared. In this forwarding scenario, the intermediate app must explicitly opt-in using `[ActivityOptions.setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))`. 

Prior to `[android.os.Build.VERSION_CODES#CINNAMON_BUN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#CINNAMON_BUN:kotlin.Int)`, the launching app's identity was not implicitly shared for any result-based launches and could only be retrieved via `getCallingPackage()`

Return  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` | the package name of the launching app or null if the current activity cannot access the identity of the launching app  
  
**See Also**

  * `[android.app.ActivityOptions#setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))`
  * `#getLaunchedFromUid()`



### getLaunchedFromUid

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getLaunchedFromUid(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Returns the uid of the app that initially launched this activity. 

In order to receive the launching app's uid, at least one of the following has to be met: 

  * The app must call `[ActivityOptions.setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))` with a value of `true` and launch this activity with the resulting `ActivityOptions`. 
  * The launched activity has the same uid as the launching app. 
  * The launched activity is running in a package that is signed with the same key used to sign the platform (typically only system packages such as Settings will meet this requirement). 
  * Starting in `[Build.VERSION_CODES.CINNAMON_BUN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#CINNAMON_BUN:kotlin.Int)`, the activity was launched directly with `Activity.startActivityForResult(Intent,int)`. 

. These are the same requirements for `getLaunchedFromPackage()`; if any of these are met, then these methods can be used to obtain the uid and package name of the launching app. If none are met, then `[Process.INVALID_UID](https://developer.android.com/reference/kotlin/android/os/Process.html#INVALID_UID:kotlin.Int)` is returned. 

Note, if an activity is launched via `startActivityForResult(Intent,int)` but the launch is intercepted and forwarded by an intermediate app using `[Intent.FLAG_ACTIVITY_FORWARD_RESULT](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_FORWARD_RESULT:kotlin.Int)`, the identity of the intermediate app will not be implicitly shared. In this forwarding scenario, the intermediate app must explicitly opt-in using `[ActivityOptions.setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))`. 

Prior to `[android.os.Build.VERSION_CODES#CINNAMON_BUN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#CINNAMON_BUN:kotlin.Int)`, the launching app's identity was not implicitly shared for any result-based launches and could only be retrieved via `getCallingPackage()`

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | the uid of the launching app or `[Process.INVALID_UID](https://developer.android.com/reference/kotlin/android/os/Process.html#INVALID_UID:kotlin.Int)` if the current activity cannot access the identity of the launching app  
  
**See Also**

  * `[android.app.ActivityOptions#setShareIdentityEnabled(boolean)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#setShareIdentityEnabled\(kotlin.Boolean\))`
  * `#getLaunchedFromPackage()`



### getLayoutInflater

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getLayoutInflater(): [LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)

Convenience for calling `[android.view.Window#getLayoutInflater](https://developer.android.com/reference/kotlin/android/view/Window.html#getLayoutInflater\(\))`.

Return  
---  
`[LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)` | This value cannot be `null`.  
  
### getLoaderManager

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~getLoaderManager~~(): [LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)!

**Deprecated:**_Use androidx.fragment.app.FragmentActivity#getSupportLoaderManager()_

Return the LoaderManager for this activity, creating it if needed.

### getLocalClassName

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getLocalClassName(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)

Returns class name for this activity with the package prefix removed. This is the default name used to read and write settings.

Return  
---  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` | The local class name.   
This value cannot be `null`.  
  
### getMaxNumPictureInPictureActions

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getMaxNumPictureInPictureActions(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Return the number of actions that will be displayed in the picture-in-picture UI when the user interacts with the activity currently in picture-in-picture mode. This number may change if the global configuration changes (ie. if the device is plugged into an external display), but will always be at least three.

### getMaxNumPictureInPictureOverlayActions

Added in [API level 37.2](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getMaxNumPictureInPictureOverlayActions(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Returns the maximum number of overlay actions that will be displayed in the picture-in-picture window. 

Any overlay actions set via `[PictureInPictureParams.Builder.setOverlayActions(List,RemoteAction)](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams.Builder#setOverlayActions\(kotlin.collections.MutableList,%20android.app.RemoteAction\))` that exceed this number will not be shown.

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | the maximum number of overlay actions.  
  
**See Also**

  * `[android.app.PictureInPictureParams.Builder#setOverlayActions(java.util.List,android.app.RemoteAction)](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams.Builder#setOverlayActions\(kotlin.collections.MutableList,%20android.app.RemoteAction\))`



### getMediaController

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getMediaController(): [MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)!

Gets the controller which should be receiving media key and volume events while this activity is in the foreground.

Return  
---  
`[MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)!` | The controller which should receive events.  
  
**See Also**

  * `#setMediaController(android.media.session.MediaController)`



### getMenuInflater

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getMenuInflater(): [MenuInflater](https://developer.android.com/reference/kotlin/android/view/MenuInflater.html)

Returns a `[MenuInflater](https://developer.android.com/reference/kotlin/android/view/MenuInflater.html)` with this context.

Return  
---  
`[MenuInflater](https://developer.android.com/reference/kotlin/android/view/MenuInflater.html)` | This value cannot be `null`.  
  
### getOnBackInvokedDispatcher

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getOnBackInvokedDispatcher(): [OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html)

Returns the `[OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html)` instance associated with the window that this activity is attached to.

Return  
---  
`[OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html)` | This value cannot be `null`.  
Exceptions  
---  
`java.lang.IllegalStateException` | if this Activity is not visual.  
  
### getParent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~getParent~~(): Activity!

**Deprecated:**_`[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)` is deprecated._

Returns the parent `Activity` if this is a child `Activity` of an `[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)`.

### getParentActivityIntent

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getParentActivityIntent(): [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?

Obtain an `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)` that will launch an explicit target activity specified by this activity's logical parent. The logical parent is named in the application's manifest by the `[parentActivityName](https://developer.android.com/reference/kotlin/android/R.attr.html#parentActivityName:kotlin.Int)` attribute. Activity subclasses may override this method to modify the Intent returned by super.getParentActivityIntent() or to implement a different mechanism of retrieving the parent intent entirely.

Return  
---  
`[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?` | a new Intent targeting the defined parent of this activity or null if there is no valid parent.  
  
### getPreferences

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getPreferences(mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)!

Retrieve a `[SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)` object for accessing preferences that are private to this activity. This simply calls the underlying `[getSharedPreferences(String,int)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getSharedPreferences\(kotlin.String,%20kotlin.Int\))` method by passing in this activity's class name as the preferences name.

Parameters  
---  
`mode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Operating mode. Use `[MODE_PRIVATE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_PRIVATE:kotlin.Int)` for the default operation.   
Value is either `0` or a combination of the following: 

  * `[android.content.Context#MODE_PRIVATE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_PRIVATE:kotlin.Int)`
  * `[android.content.Context#MODE_WORLD_READABLE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_WORLD_READABLE:kotlin.Int)`
  * `[android.content.Context#MODE_WORLD_WRITEABLE](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_WORLD_WRITEABLE:kotlin.Int)`
  * `[android.content.Context#MODE_MULTI_PROCESS](https://developer.android.com/reference/kotlin/android/content/Context.html#MODE_MULTI_PROCESS:kotlin.Int)`

  
Return  
---  
`[SharedPreferences](https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html)!` | Returns the single SharedPreferences instance that can be used to retrieve and modify the preference values.  
  
### getReferrer

Added in [API level 22](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getReferrer(): [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)?

Return information about who launched this activity. If the launching Intent contains an `[Intent.EXTRA_REFERRER](https://developer.android.com/reference/kotlin/android/content/Intent.html#EXTRA_REFERRER:kotlin.String)`, that will be returned as-is; otherwise, if known, an `[android-app:](https://developer.android.com/reference/kotlin/android/content/Intent.html#URI_ANDROID_APP_SCHEME:kotlin.Int)` referrer URI containing the package name that started the Intent will be returned. This may return null if no referrer can be identified -- it is neither explicitly specified, nor is it known which application package was involved. 

If called while inside the handling of #onNewIntent, this function will return the referrer that submitted that new intent to the activity only after `setIntent(Intent)` is called with the provided intent.

Note that this is _not_ a security feature -- you can not trust the referrer information, applications can spoof it.

### getRequestedOrientation

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getRequestedOrientation(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Returns the current requested orientation of the activity, which is either the orientation requested in the app manifest or the last orientation given to `setRequestedOrientation(int)`. **Note:**

  * To improve the layout of apps on form factors with smallest width >= 600dp, the system ignores calls to this method for apps that target Android 16 (API level 36) or higher.
  * Device manufacturers can configure devices to ignore calls to this method to improve the layout of orientation-restricted apps.
  * On devices with Android 16 (API level 36) or higher installed, virtual device owners (select trusted and privileged apps) can optimize app layout on displays they manage by ignoring calls to this method. See also [ Companion app streaming](https://source.android.com/docs/core/permissions/app-streaming).



See [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode).

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | Returns an orientation constant as used in `[ActivityInfo.screenOrientation](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#screenOrientation:kotlin.Int)`.   
Value is one of the following: 

  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_UNSPECIFIED](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_UNSPECIFIED:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_BEHIND](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_BEHIND:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_NOSENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_NOSENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_REVERSE_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_REVERSE_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_REVERSE_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_REVERSE_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_FULL_SENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_FULL_SENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_FULL_USER](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_FULL_USER:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_LOCKED](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_LOCKED:kotlin.Int)`

  
  
### getSearchEvent

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getSearchEvent(): [SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)!

During the onSearchRequested() callbacks, this function will return the `[SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)` that triggered the callback, if it exists.

Return  
---  
`[SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)!` | SearchEvent The SearchEvent that triggered the #onSearchRequested callback.  
  
### getSplashScreen

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getSplashScreen(): [SplashScreen](https://developer.android.com/reference/kotlin/android/window/SplashScreen.html)

Get the interface that activity use to talk to the splash screen.

Return  
---  
`[SplashScreen](https://developer.android.com/reference/kotlin/android/window/SplashScreen.html)` | This value cannot be `null`.  
  
**See Also**

  * `[android.window.SplashScreen](https://developer.android.com/reference/kotlin/android/window/SplashScreen.html)`



### getSystemService

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getSystemService(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!

Return the handle to a system-level service by name. The class of the returned object varies by the requested name. Currently available names are: 

`[WINDOW_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WINDOW_SERVICE:kotlin.String)` ("window") 
    The top-level window manager in which you can place custom windows. The returned object is a `[android.view.WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)`. Must only be obtained from a visual context such as Activity or a Context created with `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))`, which are adjusted to the configuration and visual bounds of an area on screen. 
`[LAYOUT_INFLATER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LAYOUT_INFLATER_SERVICE:kotlin.String)` ("layout_inflater") 
    A `[android.view.LayoutInflater](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.html)` for inflating layout resources in this context. Must only be obtained from a visual context such as Activity or a Context created with `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))`, which are adjusted to the configuration and visual bounds of an area on screen. 
`[ACTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACTIVITY_SERVICE:kotlin.String)` ("activity") 
    A `[android.app.ActivityManager](https://developer.android.com/reference/kotlin/android/app/ActivityManager)` for interacting with the global activity state of the system. 
`[WALLPAPER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WALLPAPER_SERVICE:kotlin.String)` ("wallpaper") 
    A `[android.service.wallpaper.WallpaperService](https://developer.android.com/reference/kotlin/android/service/wallpaper/WallpaperService.html)` for accessing wallpapers in this context. Must only be obtained from a visual context such as Activity or a Context created with `[createWindowContext(int,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#createWindowContext\(kotlin.Int,%20android.os.Bundle\))`, which are adjusted to the configuration and visual bounds of an area on screen. 
`[POWER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#POWER_SERVICE:kotlin.String)` ("power") 
    A `[android.os.PowerManager](https://developer.android.com/reference/kotlin/android/os/PowerManager.html)` for controlling power management. 
`[ALARM_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ALARM_SERVICE:kotlin.String)` ("alarm") 
    A `[android.app.AlarmManager](https://developer.android.com/reference/kotlin/android/app/AlarmManager)` for receiving intents at the time of your choosing. 
`[NOTIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NOTIFICATION_SERVICE:kotlin.String)` ("notification") 
    A `[android.app.NotificationManager](https://developer.android.com/reference/kotlin/android/app/NotificationManager)` for informing the user of background events. 
`[KEYGUARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYGUARD_SERVICE:kotlin.String)` ("keyguard") 
    A `[android.app.KeyguardManager](https://developer.android.com/reference/kotlin/android/app/KeyguardManager)` for controlling keyguard. 
`[LOCATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LOCATION_SERVICE:kotlin.String)` ("location") 
    A `[android.location.LocationManager](https://developer.android.com/reference/kotlin/android/location/LocationManager.html)` for controlling location (e.g., GPS) updates. 
`[SEARCH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SEARCH_SERVICE:kotlin.String)` ("search") 
    A `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)` for handling search. 
`[VIBRATOR_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_MANAGER_SERVICE:kotlin.String)` ("vibrator_manager") 
    A `[android.os.VibratorManager](https://developer.android.com/reference/kotlin/android/os/VibratorManager.html)` for accessing the device vibrators, interacting with individual ones and playing synchronized effects on multiple vibrators. 
`[MULTISENSORY_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MULTISENSORY_MANAGER_SERVICE:kotlin.String)` ("multisensory_manager") 
    A `[android.os.multisensory.MultisensoryManager](https://developer.android.com/reference/kotlin/android/os/multisensory/MultisensoryManager.html)` for delivering audio-haptic feedback in the Multisensory Design System 
`[VIBRATOR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_SERVICE:kotlin.String)` ("vibrator") 
    A `[android.os.Vibrator](https://developer.android.com/reference/kotlin/android/os/Vibrator.html)` for interacting with the vibrator hardware. 
`[CONNECTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONNECTIVITY_SERVICE:kotlin.String)` ("connectivity") 
    A `[ConnectivityManager](https://developer.android.com/reference/kotlin/android/net/ConnectivityManager.html)` for handling management of network connections. 
`[IPSEC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#IPSEC_SERVICE:kotlin.String)` ("ipsec") 
    A `[IpSecManager](https://developer.android.com/reference/kotlin/android/net/IpSecManager.html)` for managing IPSec on sockets and networks. 
`[WIFI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_SERVICE:kotlin.String)` ("wifi") 
    A `[WifiManager](https://developer.android.com/reference/kotlin/android/net/wifi/WifiManager.html)` for management of Wi-Fi connectivity. On releases before Android 7, it should only be obtained from an application context, and not from any other derived context to avoid memory leaks within the calling process. 
`[WIFI_AWARE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_AWARE_SERVICE:kotlin.String)` ("wifiaware") 
    A `[WifiAwareManager](https://developer.android.com/reference/kotlin/android/net/wifi/aware/WifiAwareManager.html)` for management of Wi-Fi Aware discovery and connectivity. 
`[WIFI_P2P_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_P2P_SERVICE:kotlin.String)` ("wifip2p") 
    A `[WifiP2pManager](https://developer.android.com/reference/kotlin/android/net/wifi/p2p/WifiP2pManager.html)` for management of Wi-Fi Direct connectivity. 
`[INPUT_METHOD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#INPUT_METHOD_SERVICE:kotlin.String)` ("input_method") 
    An `[InputMethodManager](https://developer.android.com/reference/kotlin/android/view/inputmethod/InputMethodManager.html)` for management of input methods. 
`[UI_MODE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#UI_MODE_SERVICE:kotlin.String)` ("uimode") 
    An `[android.app.UiModeManager](https://developer.android.com/reference/kotlin/android/app/UiModeManager)` for controlling UI modes. 
`[DOWNLOAD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DOWNLOAD_SERVICE:kotlin.String)` ("download") 
    A `[android.app.DownloadManager](https://developer.android.com/reference/kotlin/android/app/DownloadManager)` for requesting HTTP downloads 
`[BATTERY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BATTERY_SERVICE:kotlin.String)` ("batterymanager") 
    A `[android.os.BatteryManager](https://developer.android.com/reference/kotlin/android/os/BatteryManager.html)` for managing battery state 
`[JOB_SCHEDULER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#JOB_SCHEDULER_SERVICE:kotlin.String)` ("taskmanager") 
    A `[android.app.job.JobScheduler](https://developer.android.com/reference/kotlin/android/app/job/JobScheduler)` for managing scheduled tasks 
`[NETWORK_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NETWORK_STATS_SERVICE:kotlin.String)` ("netstats") 
    A `[NetworkStatsManager](https://developer.android.com/reference/kotlin/android/app/usage/NetworkStatsManager)` for querying network usage statistics. 
`[HARDWARE_PROPERTIES_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HARDWARE_PROPERTIES_SERVICE:kotlin.String)` ("hardware_properties") 
    A `[android.os.HardwarePropertiesManager](https://developer.android.com/reference/kotlin/android/os/HardwarePropertiesManager.html)` for accessing hardware properties. 
`[DOMAIN_VERIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DOMAIN_VERIFICATION_SERVICE:kotlin.String)` ("domain_verification") 
    A `[android.content.pm.verify.domain.DomainVerificationManager](https://developer.android.com/reference/kotlin/android/content/pm/verify/domain/DomainVerificationManager.html)` for accessing web domain approval state. 
`[DISPLAY_HASH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DISPLAY_HASH_SERVICE:kotlin.String)` ("display_hash") 
    A `[android.view.displayhash.DisplayHashManager](https://developer.android.com/reference/kotlin/android/view/displayhash/DisplayHashManager.html)` for management of display hashes. 
`[AUTHENTICATION_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUTHENTICATION_POLICY_SERVICE:kotlin.String)` ("authentication_policy") 
    A `[android.security.authenticationpolicy.AuthenticationPolicyManager](https://developer.android.com/reference/kotlin/android/security/authenticationpolicy/AuthenticationPolicyManager.html)` for managing authentication related policies on the device. 

Note: System services obtained via this API may be closely associated with the Context in which they are obtained from. In general, do not share the service objects between various different contexts (Activities, Applications, Services, Providers, etc.) 

Note: Instant apps, for which `[PackageManager.isInstantApp()](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#isInstantApp\(\))` returns true, don't have access to the following system services: `[DEVICE_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_POLICY_SERVICE:kotlin.String)`, #FINGERPRINT_SERVICE, `[KEYGUARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYGUARD_SERVICE:kotlin.String)`, `[SHORTCUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SHORTCUT_SERVICE:kotlin.String)`, `[USB_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USB_SERVICE:kotlin.String)`, `[WALLPAPER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WALLPAPER_SERVICE:kotlin.String)`, `[WIFI_P2P_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_P2P_SERVICE:kotlin.String)`, `[WIFI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_SERVICE:kotlin.String)`, `[WIFI_AWARE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_AWARE_SERVICE:kotlin.String)`. For these services this method will return `null`. Generally, if you are running as an instant app you should always check whether the result of this method is `null`. 

Note: When implementing this method, keep in mind that new services can be added on newer Android releases, so if you're looking for just the explicit names mentioned above, make sure to return `null` when you don't recognize the name — if you throw a `[RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html)` exception instead, your app might break on new Android releases.

Parameters  
---  
`name` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): Value is one of the following: 

  * `[android.content.Context#POWER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#POWER_SERVICE:kotlin.String)`
  * `[android.content.Context#WINDOW_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WINDOW_SERVICE:kotlin.String)`
  * `[android.content.Context#LAYOUT_INFLATER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LAYOUT_INFLATER_SERVICE:kotlin.String)`
  * `[android.content.Context#ACCOUNT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACCOUNT_SERVICE:kotlin.String)`
  * `[android.content.Context#ACTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACTIVITY_SERVICE:kotlin.String)`
  * `[android.content.Context#ALARM_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ALARM_SERVICE:kotlin.String)`
  * `[android.content.Context#NOTIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NOTIFICATION_SERVICE:kotlin.String)`
  * `[android.content.Context#ACCESSIBILITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ACCESSIBILITY_SERVICE:kotlin.String)`
  * `[android.content.Context#CAPTIONING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CAPTIONING_SERVICE:kotlin.String)`
  * `[android.content.Context#KEYGUARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#KEYGUARD_SERVICE:kotlin.String)`
  * `[android.content.Context#LOCATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LOCATION_SERVICE:kotlin.String)`
  * `[android.content.Context#HEALTHCONNECT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HEALTHCONNECT_SERVICE:kotlin.String)`
  * `[android.content.Context#SEARCH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SEARCH_SERVICE:kotlin.String)`
  * `[android.content.Context#SENSOR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SENSOR_SERVICE:kotlin.String)`
  * `[android.content.Context#STORAGE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#STORAGE_SERVICE:kotlin.String)`
  * `[android.content.Context#STORAGE_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#STORAGE_STATS_SERVICE:kotlin.String)`
  * `[android.content.Context#WALLPAPER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WALLPAPER_SERVICE:kotlin.String)`
  * `[android.content.Context#VIBRATOR_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_MANAGER_SERVICE:kotlin.String)`
  * `[android.content.Context#MULTISENSORY_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MULTISENSORY_MANAGER_SERVICE:kotlin.String)`
  * `[android.content.Context#VIBRATOR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIBRATOR_SERVICE:kotlin.String)`
  * `[android.content.Context#CONNECTIVITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONNECTIVITY_SERVICE:kotlin.String)`
  * `[android.content.Context#TETHERING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TETHERING_SERVICE:kotlin.String)`
  * `[android.content.Context#IPSEC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#IPSEC_SERVICE:kotlin.String)`
  * `[android.content.Context#VPN_MANAGEMENT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VPN_MANAGEMENT_SERVICE:kotlin.String)`
  * `[android.content.Context#NETWORK_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NETWORK_STATS_SERVICE:kotlin.String)`
  * `[android.content.Context#WIFI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_SERVICE:kotlin.String)`
  * `[android.content.Context#WIFI_AWARE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_AWARE_SERVICE:kotlin.String)`
  * `[android.content.Context#WIFI_P2P_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_P2P_SERVICE:kotlin.String)`
  * `[android.content.Context#WIFI_RTT_RANGING_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WIFI_RTT_RANGING_SERVICE:kotlin.String)`
  * `[android.content.Context#NSD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NSD_SERVICE:kotlin.String)`
  * `[android.content.Context#AUDIO_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUDIO_SERVICE:kotlin.String)`
  * `[android.content.Context#BIOMETRIC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BIOMETRIC_SERVICE:kotlin.String)`
  * `[android.content.Context#AUTHENTICATION_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#AUTHENTICATION_POLICY_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_ROUTER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_ROUTER_SERVICE:kotlin.String)`
  * `[android.content.Context#TELEPHONY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_SERVICE:kotlin.String)`
  * `[android.content.Context#TELEPHONY_SUBSCRIPTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_SUBSCRIPTION_SERVICE:kotlin.String)`
  * `[android.content.Context#TELEPHONY_PHONE_NUMBER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELEPHONY_PHONE_NUMBER_SERVICE:kotlin.String)`
  * `[android.content.Context#CARRIER_CONFIG_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CARRIER_CONFIG_SERVICE:kotlin.String)`
  * `[android.content.Context#EUICC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#EUICC_SERVICE:kotlin.String)`
  * `[android.content.Context#TELECOM_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TELECOM_SERVICE:kotlin.String)`
  * `[android.content.Context#CLIPBOARD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CLIPBOARD_SERVICE:kotlin.String)`
  * `[android.content.Context#INPUT_METHOD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#INPUT_METHOD_SERVICE:kotlin.String)`
  * `[android.content.Context#TEXT_SERVICES_MANAGER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TEXT_SERVICES_MANAGER_SERVICE:kotlin.String)`
  * `[android.content.Context#TEXT_CLASSIFICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TEXT_CLASSIFICATION_SERVICE:kotlin.String)`
  * `[android.content.Context#APPWIDGET_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APPWIDGET_SERVICE:kotlin.String)`
  * `[android.content.Context#DROPBOX_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DROPBOX_SERVICE:kotlin.String)`
  * `[android.content.Context#DEVICE_POLICY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_POLICY_SERVICE:kotlin.String)`
  * `[android.content.Context#UI_MODE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#UI_MODE_SERVICE:kotlin.String)`
  * `[android.content.Context#DOWNLOAD_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DOWNLOAD_SERVICE:kotlin.String)`
  * `[android.content.Context#NFC_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NFC_SERVICE:kotlin.String)`
  * `[android.content.Context#BLUETOOTH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BLUETOOTH_SERVICE:kotlin.String)`
  * `[android.content.Context#USB_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USB_SERVICE:kotlin.String)`
  * `[android.content.Context#LAUNCHER_APPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LAUNCHER_APPS_SERVICE:kotlin.String)`
  * `[android.content.Context#SERIAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SERIAL_SERVICE:kotlin.String)`
  * `[android.content.Context#INPUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#INPUT_SERVICE:kotlin.String)`
  * `[android.content.Context#DISPLAY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DISPLAY_SERVICE:kotlin.String)`
  * `[android.content.Context#USER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USER_SERVICE:kotlin.String)`
  * `[android.content.Context#RESTRICTIONS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#RESTRICTIONS_SERVICE:kotlin.String)`
  * `[android.content.Context#APP_OPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#APP_OPS_SERVICE:kotlin.String)`
  * `[android.content.Context#ROLE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ROLE_SERVICE:kotlin.String)`
  * `[android.content.Context#CAMERA_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CAMERA_SERVICE:kotlin.String)`
  * `[android.content.Context#PRINT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PRINT_SERVICE:kotlin.String)`
  * `[android.content.Context#CONSUMER_IR_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONSUMER_IR_SERVICE:kotlin.String)`
  * `[android.content.Context#TV_INTERACTIVE_APP_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TV_INTERACTIVE_APP_SERVICE:kotlin.String)`
  * `[android.content.Context#TV_INPUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#TV_INPUT_SERVICE:kotlin.String)`
  * `[android.content.Context#USAGE_STATS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#USAGE_STATS_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_SESSION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_SESSION_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_COMMUNICATION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_COMMUNICATION_SERVICE:kotlin.String)`
  * `[android.content.Context#BATTERY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#BATTERY_SERVICE:kotlin.String)`
  * `[android.content.Context#JOB_SCHEDULER_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#JOB_SCHEDULER_SERVICE:kotlin.String)`
  * `[android.content.Context#PERSISTENT_DATA_BLOCK_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#PERSISTENT_DATA_BLOCK_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_PROJECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_PROJECTION_SERVICE:kotlin.String)`
  * `[android.content.Context#MIDI_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MIDI_SERVICE:kotlin.String)`
  * `[android.content.Context#HARDWARE_PROPERTIES_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HARDWARE_PROPERTIES_SERVICE:kotlin.String)`
  * `[android.content.Context#SHORTCUT_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SHORTCUT_SERVICE:kotlin.String)`
  * `[android.content.Context#SYSTEM_HEALTH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SYSTEM_HEALTH_SERVICE:kotlin.String)`
  * `[android.content.Context#COMPANION_DEVICE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#COMPANION_DEVICE_SERVICE:kotlin.String)`
  * `[android.content.Context#VIRTUAL_DEVICE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#VIRTUAL_DEVICE_SERVICE:kotlin.String)`
  * `[android.content.Context#CROSS_PROFILE_APPS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CROSS_PROFILE_APPS_SERVICE:kotlin.String)`
  * `[android.content.Context#LOCALE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#LOCALE_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_METRICS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_METRICS_SERVICE:kotlin.String)`
  * `[android.content.Context#DISPLAY_HASH_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DISPLAY_HASH_SERVICE:kotlin.String)`
  * `[android.content.Context#CREDENTIAL_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CREDENTIAL_SERVICE:kotlin.String)`
  * `[android.content.Context#DEVICE_LOCK_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_LOCK_SERVICE:kotlin.String)`
  * `[android.content.Context#GRAMMATICAL_INFLECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#GRAMMATICAL_INFLECTION_SERVICE:kotlin.String)`
  * `[android.content.Context#SECURITY_STATE_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#SECURITY_STATE_SERVICE:kotlin.String)`
  * `[android.content.Context#CONTACT_KEYS_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#CONTACT_KEYS_SERVICE:kotlin.String)`
  * `[android.content.Context#MEDIA_QUALITY_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEDIA_QUALITY_SERVICE:kotlin.String)`
  * `[android.content.Context#ADVANCED_PROTECTION_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#ADVANCED_PROTECTION_SERVICE:kotlin.String)`
  * `[android.content.Context#NPU_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#NPU_SERVICE:kotlin.String)`
  * `[android.content.Context#WEB_APP_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#WEB_APP_SERVICE:kotlin.String)`
  * `[android.content.Context#HID_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#HID_SERVICE:kotlin.String)`
  * `[android.content.Context#MEMORY_BUDGET_SERVICE](https://developer.android.com/reference/kotlin/android/content/Context.html#MEMORY_BUDGET_SERVICE:kotlin.String)`
.   
This value cannot be `null`.
  
Return  
---  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!` | The service or `null` if the name does not exist.  
  
### getTaskId

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getTaskId(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Return the identifier of the task this activity is in. This identifier will remain the same for the lifetime of the activity.

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | Task identifier, an opaque integer.  
  
### getTitle

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getTitle(): [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!

### getTitleColor

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getTitleColor(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

### getVoiceInteractor

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getVoiceInteractor(): [VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)!

Retrieve the active `[VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)` that the user is going through to interact with this activity.

### getVolumeControlStream

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun getVolumeControlStream(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)

Gets the suggested audio stream whose volume should be changed by the hardware volume controls.

Return  
---  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | The suggested audio stream type whose volume should be changed by the hardware volume controls.  
  
**See Also**

  * `#setVolumeControlStream(int)`



### getWindow

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getWindow(): [Window](https://developer.android.com/reference/kotlin/android/view/Window.html)!

Retrieve the current `[android.view.Window](https://developer.android.com/reference/kotlin/android/view/Window.html)` for the activity. This can be used to directly access parts of the Window API that are not available through Activity/Screen.

Return  
---  
`[Window](https://developer.android.com/reference/kotlin/android/view/Window.html)!` | Window The current window, or null if the activity is not visual.  
  
### getWindowManager

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun getWindowManager(): [WindowManager](https://developer.android.com/reference/kotlin/android/view/WindowManager.html)!

Retrieve the window manager for showing custom windows.

### hasWindowFocus

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun hasWindowFocus(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if this activity's _main_ window currently has window focus. Note that this is not the same as the view itself having focus.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if this activity's main window currently has window focus.  
  
**See Also**

  * `#onWindowAttributesChanged(android.view.WindowManager.LayoutParams)`



### invalidateOptionsMenu

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun invalidateOptionsMenu(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Declare that the options menu has changed, so should be recreated. The `onCreateOptionsMenu(Menu)` method will be called the next time it needs to be displayed.

### isActivityTransitionRunning

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isActivityTransitionRunning(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns whether there are any activity transitions currently running on this activity. A return value of `true` can mean that either an enter or exit transition is running, including whether the background of the activity is animating as a part of that transition.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if a transition is currently running on this activity, false otherwise.  
  
### isChangingConfigurations

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isChangingConfigurations(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Check to see whether this activity is in the process of being destroyed in order to be recreated with a new configuration. 

This is often used in `onStop` to determine whether the state needs to be cleaned up or will be passed on to the next instance of the activity via `onRetainNonConfigurationInstance()`. However, if the activity has already been in the background as stopped, and then gets recreated with different configuration, there won't be another `onPause` or `onStop` with this API returning `true`.

For example, if an activity that is not handling size configuration change is first minimized, and then get rotated with the display, it should first receive `onPause` and `onStop` with this API returning `false`, and then receive `onDestroy` with this API returning `true`.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If the activity is being torn down in order to be recreated with a new configuration, returns true; else returns false.  
  
### isChild

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~isChild~~(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_`[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)` is deprecated._

Whether this is a child `Activity` of an `[ActivityGroup](https://developer.android.com/reference/kotlin/android/app/ActivityGroup)`.

### isDestroyed

Added in [API level 17](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isDestroyed(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if the final `onDestroy()` call has been made on the Activity, so this instance is now dead.

### isFinishing

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isFinishing(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Check to see whether this activity is in the process of finishing, either because you called `finish` on it or someone else has requested that it finished. 

This is often used in `onPause` to determine whether the activity is simply pausing or completely finishing. However, if the finish request is made after the activity has already been paused/stopped, there won't be another `onPause` or `onStop` with this API returning `true`.

For example, if an activity is first minimized, and then gets killed in background, it should first receive `onPause` and `onStop` with this API returning `false`, and then receive `onDestroy` with this API returning `true`.

**See Also**

  * `#finish`



### isHandoffEnabled

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun isHandoffEnabled(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns if Handoff has been enabled for this Activity. See `setHandoffEnabled` to change if Handoff is enabled on this Activity. When Handoff is enabled, the user may request this Activity to be sent to other devices that they owe. The system will request data from this Activity to recreate it on the other device. TODO (b/412338142): Add link to onHandoffActivityDataRequested once method is added.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Whether Handoff is enabled for the Activity  
  
### isImmersive

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isImmersive(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Bit indicating that this activity is "immersive" and should not be interrupted by notifications if possible. This value is initially set by the manifest property `android:immersive` but may be changed at runtime by `setImmersive`.

**See Also**

  * `#setImmersive(boolean)`
  * `[android.content.pm.ActivityInfo#FLAG_IMMERSIVE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#FLAG_IMMERSIVE:kotlin.Int)`



### isInMultiWindowMode

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isInMultiWindowMode(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if the activity is currently in multi-window mode. 

See [ Support multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode) for recommendations on how to handle different multi-window scenarios such as split-screen.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if the activity is in multi-window mode.  
  
**See Also**

  * `[android.R.attr#resizeableActivity](https://developer.android.com/reference/kotlin/android/R.attr.html#resizeableActivity:kotlin.Int)`



### isInPictureInPictureMode

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isInPictureInPictureMode(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if the activity is currently in picture-in-picture mode.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if the activity is in picture-in-picture mode.  
  
**See Also**

  * `[android.R.attr#supportsPictureInPicture](https://developer.android.com/reference/kotlin/android/R.attr.html#supportsPictureInPicture:kotlin.Int)`



### isLaunchedFromBubble

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isLaunchedFromBubble(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Indicates whether this activity is launched from a bubble. A bubble is a floating shortcut on the screen that expands to show an activity. If your activity can be used normally or as a bubble, you might use this method to check if the activity is bubbled to modify any behaviour that might be different between the normal activity and the bubbled activity. For example, if you normally cancel the notification associated with the activity when you open the activity, you might not want to do that when you're bubbled as that would remove the bubble. **Note:** This method will return `false` for app Bubbles. See https://developer.android.com/develop/ui/compose/layouts/adaptive/support-bubbles and only applicable to chat bubbles. 

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `true` if the activity is launched from a bubble.  
  
**See Also**

  * `[android.app.Notification.Builder#setBubbleMetadata(android.app.Notification.BubbleMetadata)](https://developer.android.com/reference/kotlin/android/app/Notification.Builder#setBubbleMetadata\(android.app.Notification.BubbleMetadata\))`
  * `[android.app.Notification.BubbleMetadata.Builder#Builder(java.lang.String)](https://developer.android.com/reference/kotlin/android/app/Notification.BubbleMetadata.Builder#Builder\(kotlin.String\))`



### isLocalVoiceInteractionSupported

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isLocalVoiceInteractionSupported(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Queries whether the currently enabled voice interaction service supports returning a voice interactor for use by the activity. This is valid only for the duration of the activity.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | whether the current voice interaction service supports local voice interaction  
  
### isTaskRoot

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isTaskRoot(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Return whether this activity is the root of a task. The root is the first activity in a task.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if this is the root activity, else false.  
  
### isVoiceInteraction

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isVoiceInteraction(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Check whether this activity is running as part of a voice interaction with the user. If true, it should perform its interaction with the user through the `[VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)` returned by `getVoiceInteractor`.

### isVoiceInteractionRoot

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun isVoiceInteractionRoot(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Like `isVoiceInteraction`, but only returns `true` if this is also the root of a voice interaction. That is, returns `true` if this activity was directly started by the voice interaction service as the initiation of a voice interaction. Otherwise, for example if it was started by another activity while under voice interaction, returns `false`. If the activity `[launchMode](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity_launchMode:kotlin.Int)` is `singleTask`, it forces the activity to launch in a new task, separate from the one that started it. Therefore, there is no longer a relationship between them, and `isVoiceInteractionRoot()` return `false` in this case.

### managedQuery

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~managedQuery~~(  
        uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!,   
        projection: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!,   
        selection: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!,   
        selectionArgs: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!,   
        sortOrder: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!  
    ): [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!

**Deprecated:**_Use`[CursorLoader](https://developer.android.com/reference/kotlin/android/content/CursorLoader.html)` instead._

Wrapper around `[ContentResolver.query(android.net.Uri,String[],String,String[],String)](https://developer.android.com/reference/kotlin/android/content/ContentResolver.html#query\(android.net.Uri,%20kotlin.Array,%20kotlin.String,%20kotlin.Array,%20kotlin.String\))` that gives the resulting `[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)` to call `startManagingCursor` so that the activity will manage its lifecycle for you. _If you are targeting`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, consider instead using `[LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)` instead, available via `getLoaderManager()`._

**Warning:** Do not call android.database.Cursor#close() on a cursor obtained using this method, because the activity will do that for you at the appropriate time. However, if you call `stopManagingCursor` on a cursor from a managed query, the system _will not_ automatically close the cursor and, in that case, you must call android.database.Cursor#close().

Parameters  
---  
`uri` | [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!: The URI of the content provider to query.  
`projection` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!: List of columns to return.  
`selection` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!: SQL WHERE clause.  
`selectionArgs` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>!: The arguments to selection, if any ?s are pesent  
`sortOrder` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!: SQL ORDER BY clause.  
Return  
---  
`[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!` | The Cursor that was returned by query().  
  
**See Also**

  * `[android.content.ContentResolver#query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)](https://developer.android.com/reference/kotlin/android/content/ContentResolver.html#query\(android.net.Uri,%20kotlin.Array,%20kotlin.String,%20kotlin.Array,%20kotlin.String\))`
  * `#startManagingCursor`



### moveTaskToBack

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun moveTaskToBack(nonRoot: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Move the task containing this activity to the back of the activity stack. The activity's order within the task is unchanged.

Parameters  
---  
`nonRoot` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): If false then this only works if the activity is the root of a task; if true it will work for any activity in a task.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If the task was moved (or it was already at the back) true is returned, else false.  
  
### navigateUpTo

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun navigateUpTo(upIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Navigate from this activity to the activity specified by upIntent, finishing this activity in the process. If the activity indicated by upIntent already exists in the task's history, this activity and all others before the indicated activity in the history stack will be finished. 

If the indicated activity does not appear in the history stack, this will finish each activity in this task until the root activity of the task is reached, resulting in an "in-app home" behavior. This can be useful in apps with a complex navigation hierarchy when an activity may be reached by a path not passing through a canonical parent activity.

This method should be used when performing up navigation from within the same task as the destination. If up navigation should cross tasks in some cases, see `shouldUpRecreateTask(Intent)`.

Parameters  
---  
`upIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: An intent representing the target destination for up navigation  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if up navigation successfully reached the activity indicated by upIntent and upIntent was delivered to it. false if an instance of the indicated activity could not be found and this activity was simply finished normally.  
  
### navigateUpToFromChild

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~navigateUpToFromChild~~(  
        child: Activity!,   
        upIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_Use`navigateUpTo(Intent)` instead._

This is called when a child activity of this one calls its `navigateUpTo` method. The default implementation simply calls navigateUpTo(upIntent) on this activity (the parent).

Parameters  
---  
`child` | Activity!: The activity making the call.  
`upIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: An intent representing the target destination for up navigation  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if up navigation successfully reached the activity indicated by upIntent and upIntent was delivered to it. false if an instance of the indicated activity could not be found and this activity was simply finished normally.  
  
### onActionModeFinished

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onActionModeFinished(mode: [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Notifies the activity that an action mode has finished. Activity subclasses overriding this method should call the superclass implementation.   
If you override this method you _must_ call through to the superclass implementation.

Parameters  
---  
`mode` | [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!: The action mode that just finished.  
  
### onActionModeStarted

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onActionModeStarted(mode: [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Notifies the Activity that an action mode has been started. Activity subclasses overriding this method should call the superclass implementation.   
If you override this method you _must_ call through to the superclass implementation.

Parameters  
---  
`mode` | [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)!: The new action mode.  
  
### onActivityReenter

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onActivityReenter(  
        resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when an activity you launched with an activity transition exposes this Activity through a returning activity transition, giving you the resultCode and any additional data from it. This method will only be called if the activity set a result code other than `RESULT_CANCELED` and it supports activity transitions with `[Window.FEATURE_ACTIVITY_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_ACTIVITY_TRANSITIONS:kotlin.Int)`. 

The purpose of this function is to let the called Activity send a hint about its state so that this underlying Activity can prepare to be exposed. A call to this method does not guarantee that the called Activity has or will be exiting soon. It only indicates that it will expose this Activity's Window and it has some data to pass to prepare it.

Parameters  
---  
`resultCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The integer result code returned by the child activity through its setResult().  
`data` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: An Intent, which can return result data to the caller (various data can be attached to Intent "extras").  
  
### onActivityResult

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onActivityResult(  
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        caller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as `onActivityResult(int,int,Intent)`, but with an extra parameter for the ComponentCaller instance associated with the app that sent the result. 

If you want to retrieve the caller without overriding this method, call `getCurrentCaller` inside your existing `onActivityResult(int,int,Intent)`. 

Note that you should only override one #onActivityResult method.

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The integer request code originally supplied to startActivityForResult(), allowing you to identify who this result came from.  
`resultCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The integer result code returned by the child activity through its setResult().  
`data` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: An Intent, which can return result data to the caller (various data can be attached to Intent "extras").   
This value may be `null`.  
`caller` | [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller): The `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` instance associated with the app that sent the intent.   
This value cannot be `null`.  
  
### onAttachFragment

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onAttachFragment~~(fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use androidx.fragment.app.FragmentActivity#onAttachFragment(androidx.fragment.app.Fragment)_

Called when a Fragment is being attached to this activity, immediately after the call to its android.app.Fragment#onAttach method and before `[Fragment.onCreate()](https://developer.android.com/reference/kotlin/android/app/Fragment#onCreate\(android.os.Bundle\))`.

### onAttachedToWindow

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onAttachedToWindow(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when the main window associated with the activity has been attached to the window manager. See `[View.onAttachedToWindow()](https://developer.android.com/reference/kotlin/android/view/View.html#onAttachedToWindow\(\))` for more information.

**See Also**

  * `[android.view.View#onAttachedToWindow](https://developer.android.com/reference/kotlin/android/view/View.html#onAttachedToWindow\(\))`



### onBackPressed

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onBackPressed~~(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`[OnBackInvokedCallback](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedCallback.html)` or `androidx.activity.OnBackPressedCallback` to handle back navigation instead. 

Starting from Android 13 (API level 33), back event handling is moving to an ahead-of-time model and `Activity.onBackPressed()` and `[KeyEvent.KEYCODE_BACK](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html#KEYCODE_BACK:kotlin.Int)` should not be used to handle back events (back gesture or back button click). Instead, an `[OnBackInvokedCallback](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedCallback.html)` should be registered using `Activity.getOnBackInvokedDispatcher()` `[.registerOnBackInvokedCallback(priority, callback)](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html#registerOnBackInvokedCallback\(kotlin.Int,%20android.window.OnBackInvokedCallback\))`.

_

Called when the activity has detected the user's press of the back key. The default implementation depends on the platform version: 

  * On platform versions prior to `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, it finishes the current activity, but you can override this to do whatever you want. 
  * Starting with platform version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)`, for activities that are the root activity of the task and also declare an `[android.content.IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html)` with `[Intent.ACTION_MAIN](https://developer.android.com/reference/kotlin/android/content/Intent.html#ACTION_MAIN:kotlin.String)` and `[Intent.CATEGORY_LAUNCHER](https://developer.android.com/reference/kotlin/android/content/Intent.html#CATEGORY_LAUNCHER:kotlin.String)` in the manifest, the current activity and its task will be moved to the back of the activity stack instead of being finished. Other activities will simply be finished. 
  * If you target version `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)` and override this method, we strongly recommend to call through to the superclass implementation after you finish handling navigation within the app. 
  * If you target version `[android.os.Build.VERSION_CODES#TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)` or later, you should not use this method but register an `[OnBackInvokedCallback](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedCallback.html)` on an `[OnBackInvokedDispatcher](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedDispatcher.html)` that you can retrieve using `getOnBackInvokedDispatcher()`. You should also set `android:enableOnBackInvokedCallback="true"` in the application manifest. 

Alternatively, you can use `androidx.activity.ComponentActivity#getOnBackPressedDispatcher()` for backward compatibility. 




**See Also**

  * `#moveTaskToBack(boolean)`



### onConfigurationChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onConfigurationChanged(newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called by the system when the device configuration changes while your activity is running. Note that this will only be called if you have selected configurations you would like to handle with the `[android.R.attr#configChanges](https://developer.android.com/reference/kotlin/android/R.attr.html#configChanges:kotlin.Int)` attribute in your manifest. If any configuration change occurs that is not selected to be reported by that attribute, then instead of reporting it the system will stop and restart the activity (to have it launched with the new configuration). The only exception is if a size-based configuration is not large enough to be considered significant, in which case the system will not recreate the activity and will instead call this method. For details on this see the documentation on [size-based config change](https://developer.android.com/guide/topics/resources/runtime-changes.html). 

At the time that this function has been called, your Resources object will have been updated to return resource values matching the new configuration.

Parameters  
---  
`newConfig` | [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html): The new device configuration.   
This value cannot be `null`.  
  
### onContentChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onContentChanged(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This hook is called whenever the content view of the screen changes (due to a call to `[Window.setContentView](https://developer.android.com/reference/kotlin/android/view/Window.html#setContentView\(android.view.View,%20android.view.ViewGroup.LayoutParams\))` or `[Window.addContentView](https://developer.android.com/reference/kotlin/android/view/Window.html#addContentView\(android.view.View,%20android.view.ViewGroup.LayoutParams\))`).

### onContextItemSelected

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onContextItemSelected(item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

This hook is called whenever an item in a context menu is selected. The default implementation simply returns false to have the normal processing happen (calling the item's Runnable or sending a message to its Handler as appropriate). You can use this method for any items for which you would like to do processing without those other facilities. 

Use `[MenuItem.getMenuInfo()](https://developer.android.com/reference/kotlin/android/view/MenuItem.html#getMenuInfo\(\))` to get extra information set by the View that added this menu item. 

Derived classes should call through to the base class for it to perform the default menu handling.

Parameters  
---  
`item` | [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html): The context menu item that was selected.   
This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return false to allow normal context menu processing to proceed, true to consume it here.  
  
### onContextMenuClosed

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onContextMenuClosed(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This hook is called whenever the context menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).

Parameters  
---  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html): The context menu that is being closed.   
This value cannot be `null`.  
  
### onCreate

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreate(  
        savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?,   
        persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as `onCreate(android.os.Bundle)` but called for those activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.

Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: if the activity is being re-initialized after previously being shut down then this Bundle contains the data it most recently supplied in #onSaveInstanceState. **_Note: Otherwise it is null._**  
`persistentState` | [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?: if the activity is being re-initialized after previously being shut down, powered off or updated to a new version then this Bundle contains the data it most recently supplied to outPersistentState in #onSaveInstanceState. **_Note: Otherwise it is null._**  
  
**See Also**

  * `#onCreate(android.os.Bundle)`
  * `#onStart`



### onCreateContextMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateContextMenu(  
        menu: [ContextMenu](https://developer.android.com/reference/kotlin/android/view/ContextMenu.html)!,   
        v: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!,   
        menuInfo: [ContextMenu.ContextMenuInfo](https://developer.android.com/reference/kotlin/android/view/ContextMenu.ContextMenuInfo.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when a context menu for the `view` is about to be shown. Unlike `onCreateOptionsMenu(Menu)`, this will be called every time the context menu is about to be shown and should be populated for the view (or item inside the view for `[AdapterView](https://developer.android.com/reference/kotlin/android/widget/AdapterView.html)` subclasses, this can be found in the `menuInfo`)). 

Use `onContextItemSelected(android.view.MenuItem)` to know when an item has been selected. 

It is not safe to hold onto the context menu after this method returns.

Parameters  
---  
`menu` | [ContextMenu](https://developer.android.com/reference/kotlin/android/view/ContextMenu.html)!: The context menu that is being built  
`v` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The view for which the context menu is being built  
`menuInfo` | [ContextMenu.ContextMenuInfo](https://developer.android.com/reference/kotlin/android/view/ContextMenu.ContextMenuInfo.html)!: Extra information about the item for which the context menu should be shown. This information will vary depending on the class of v.  
  
### onCreateDescription

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateDescription(): [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)?

Generate a new description for this activity. This method is called before stopping the activity and can, if desired, return some textual description of its current state to be displayed to the user. 

The default implementation returns null, which will cause you to inherit the description from the previous activity. If all activities return null, generally the label of the top activity will be used as the description.

Return  
---  
`[CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)?` | A description of what the user is doing. It should be short and sweet (only a few words).  
  
**See Also**

  * `#onStop`



### onCreateNavigateUpTaskStack

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateNavigateUpTaskStack(builder: [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Define the synthetic task stack that will be generated during Up navigation from a different task. 

The default implementation of this method adds the parent chain of this activity as specified in the manifest to the supplied `[TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)`. Applications may choose to override this method to construct the desired task stack in a different way.

This method will be invoked by the default implementation of `onNavigateUp()` if `shouldUpRecreateTask(Intent)` returns true when supplied with the intent returned by `getParentActivityIntent()`.

Applications that wish to supply extra Intent parameters to the parent stack defined by the manifest should override `onPrepareNavigateUpTaskStack(TaskStackBuilder)`.

Parameters  
---  
`builder` | [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!: An empty TaskStackBuilder - the application should add intents representing the desired task stack  
  
### onCreateOptionsMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateOptionsMenu(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Initialize the contents of the Activity's standard options menu. You should place your menu items in to menu. 

This is only called once, the first time the options menu is displayed. To update the menu every time it is displayed, see `onPrepareOptionsMenu`. 

The default implementation populates the menu with standard system menu items. These are placed in the `[Menu.CATEGORY_SYSTEM](https://developer.android.com/reference/kotlin/android/view/Menu.html#CATEGORY_SYSTEM:kotlin.Int)` group so that they will be correctly ordered with application-defined menu items. Deriving classes should always call through to the base implementation. 

You can safely hold on to menu (and any items created from it), making modifications to it as desired, until the next time onCreateOptionsMenu() is called. 

When you add items to the menu, you can implement the Activity's `onOptionsItemSelected` method to handle them there.

Parameters  
---  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!: The options menu in which you place your items.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | You must return true for the menu to be displayed; if you return false it will not be shown.  
  
**See Also**

  * `#onPrepareOptionsMenu`
  * `#onOptionsItemSelected`



### onCreatePanelMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreatePanelMenu(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Default implementation of `[android.view.Window.Callback#onCreatePanelMenu](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onCreatePanelMenu\(kotlin.Int,%20android.view.Menu\))` for activities. This calls through to the new `onCreateOptionsMenu` method for the `[android.view.Window#FEATURE_OPTIONS_PANEL](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_OPTIONS_PANEL:kotlin.Int)` panel, so that subclasses of Activity don't need to deal with feature codes.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The panel being created.  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html): This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean You must return true for the panel to be displayed; if you return false it will not be shown.  
  
### onCreatePanelView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreatePanelView(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [View](https://developer.android.com/reference/kotlin/android/view/View.html)?

Default implementation of `[android.view.Window.Callback#onCreatePanelView](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onCreatePanelView\(kotlin.Int\))` for activities. This simply returns null so that all panel sub-windows will have the default menu behavior.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Which panel is being created.  
Return  
---  
`[View](https://developer.android.com/reference/kotlin/android/view/View.html)?` | view The top-level view to place in the panel.  
  
### onCreateThumbnail

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onCreateThumbnail~~(  
        outBitmap: [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)!,   
        canvas: [Canvas](https://developer.android.com/reference/kotlin/android/graphics/Canvas.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_Method doesn't do anything and will be removed in the future._

### onCreateView

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateView(  
        parent: [View](https://developer.android.com/reference/kotlin/android/view/View.html)?,   
        name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),   
        context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html),   
        attrs: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html)  
    ): [View](https://developer.android.com/reference/kotlin/android/view/View.html)?

Standard implementation of `[android.view.LayoutInflater.Factory2.onCreateView(View,String,Context,AttributeSet)](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.Factory2.html#onCreateView\(android.view.View,%20kotlin.String,%20android.content.Context,%20android.util.AttributeSet\))` used when inflating with the LayoutInflater returned by #getSystemService. This implementation handles tags to embed fragments inside of the activity.

Parameters  
---  
`parent` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)?: This value may be `null`.  
`name` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): This value cannot be `null`.  
`context` | [Context](https://developer.android.com/reference/kotlin/android/content/Context.html): This value cannot be `null`.  
`attrs` | [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html): This value cannot be `null`.  
Return  
---  
`[View](https://developer.android.com/reference/kotlin/android/view/View.html)?` | This value may be `null`.  
  
**See Also**

  * `[android.view.Window#getLayoutInflater](https://developer.android.com/reference/kotlin/android/view/Window.html#getLayoutInflater\(\))`



### onCreateView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onCreateView(  
        name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),   
        context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html),   
        attrs: [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html)  
    ): [View](https://developer.android.com/reference/kotlin/android/view/View.html)?

Standard implementation of `[android.view.LayoutInflater.Factory#onCreateView](https://developer.android.com/reference/kotlin/android/view/LayoutInflater.Factory.html#onCreateView\(kotlin.String,%20android.content.Context,%20android.util.AttributeSet\))` used when inflating with the LayoutInflater returned by #getSystemService. This implementation does nothing and is for pre-`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` apps. Newer apps should use `onCreateView(View,String,Context,AttributeSet)`.

Parameters  
---  
`name` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): This value cannot be `null`.  
`context` | [Context](https://developer.android.com/reference/kotlin/android/content/Context.html): This value cannot be `null`.  
`attrs` | [AttributeSet](https://developer.android.com/reference/kotlin/android/util/AttributeSet.html): This value cannot be `null`.  
Return  
---  
`[View](https://developer.android.com/reference/kotlin/android/view/View.html)?` | This value may be `null`.  
  
**See Also**

  * `[android.view.Window#getLayoutInflater](https://developer.android.com/reference/kotlin/android/view/Window.html#getLayoutInflater\(\))`



### onDetachedFromWindow

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onDetachedFromWindow(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when the main window associated with the activity has been detached from the window manager. See `[View.onDetachedFromWindow()](https://developer.android.com/reference/kotlin/android/view/View.html#onDetachedFromWindow\(\))` for more information.

**See Also**

  * `[android.view.View#onDetachedFromWindow](https://developer.android.com/reference/kotlin/android/view/View.html#onDetachedFromWindow\(\))`



### onEnterAnimationComplete

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onEnterAnimationComplete(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Activities cannot draw during the period that their windows are animating in. In order to know when it is safe to begin drawing they can override this method which will be called when the entering animation has completed.

### onGenericMotionEvent

Added in [API level 12](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onGenericMotionEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a generic motion event was not handled by any of the views inside of the activity. 

Generic motion events describe joystick movements, hover events from mouse or stylus devices, trackpad touches, scroll wheel movements and other motion events not handled by `onTouchEvent(MotionEvent)` or `onTrackballEvent(MotionEvent)`. The `[source](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html#getSource\(\))` of the motion event specifies the class of input that was received. Implementations of this method must examine the bits in the source before processing the event. 

Generic motion events with source class `[android.view.InputDevice#SOURCE_CLASS_POINTER](https://developer.android.com/reference/kotlin/android/view/InputDevice.html#SOURCE_CLASS_POINTER:kotlin.Int)` are delivered to the view under the pointer. All other generic motion events are delivered to the focused view. 

See `[View.onGenericMotionEvent(MotionEvent)](https://developer.android.com/reference/kotlin/android/view/View.html#onGenericMotionEvent\(android.view.MotionEvent\))` for an example of how to handle this event. 

Parameters  
---  
`event` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The generic motion event being processed.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Return true if you have consumed the event, false if you haven't. The default implementation always returns false.  
  
### onGetDirectActions

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onGetDirectActions(  
        cancellationSignal: [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html),   
        callback: [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[DirectAction](https://developer.android.com/reference/kotlin/android/app/DirectAction)!>!>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Returns the list of direct actions supported by the app. 

You should return the list of actions that could be executed in the current context, which is in the current state of the app. If the actions that could be executed by the app changes you should report that via calling `[VoiceInteractor.notifyDirectActionsChanged()](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor#notifyDirectActionsChanged\(\))`. 

To get the voice interactor you need to call `getVoiceInteractor()` which would return non `null` only if there is an ongoing voice interaction session. You can also detect when the voice interactor is no longer valid because the voice interaction session that is backing is finished by calling `[VoiceInteractor.registerOnDestroyedCallback(Executor,Runnable)](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor#registerOnDestroyedCallback\(java.util.concurrent.Executor,%20java.lang.Runnable\))`. 

This method will be called only after `onStart()` and before `onStop()`. 

You should pass to the callback the currently supported direct actions which cannot be `null` or contain `null` elements. 

You should return the action list as soon as possible to ensure the consumer, for example the assistant, is as responsive as possible which would improve user experience of your app.

Parameters  
---  
`cancellationSignal` | [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html): A signal to cancel the operation in progress.   
This value cannot be `null`.  
`callback` | [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[DirectAction](https://developer.android.com/reference/kotlin/android/app/DirectAction)!>!>: The callback to send the action list. The actions list cannot contain `null` elements. You can call this on any thread.  
  
### onHandoffActivityDataRequested

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onHandoffActivityDataRequested(requestInfo: [HandoffActivityDataRequestInfo](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo)): [HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)?

Retrieves `[HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)` representing this activity, allowing it to be recreated on another device owned by the user. The system automatically handles calling #onHandoffActivityDataRequested. This will only be called if `isHandoffEnabled` is `true` for this activity. If `isHandoffEnabled` is `true`, the activity is expected to return a non-null value. Returning `null` will present an error to the user indicating Handoff unexpectedly failed. If the current activity is in the foreground on the current device, the app's icon representing this activity will be shown on other nearby devices owned by the user. If the user selects this icon, the system will call this method to retrieve the data needed to recreate this activity on another device. When this activity is stopped, the system will call this method to retrieve `[HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)` for caching. This allows the user to hand this activity off to another device even if it is not currently running. In these situations, `[HandoffActivityDataRequestInfo.isActiveRequest](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo#isActiveRequest\(\))` will be `false`.

Parameters  
---  
`requestInfo` | [HandoffActivityDataRequestInfo](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo): the request info for the activity data.   
This value cannot be `null`.  
Return  
---  
`[HandoffActivityData](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData)?` | the activity data for handoff.  
  
### onKeyDown

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onKeyDown(  
        keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a key was pressed down and not handled by any of the views inside of the activity. So, for example, key presses while the cursor is inside a TextView will not trigger the event (unless it is a navigation to another object) because TextView handles its own key presses. 

If the focused view didn't want this event, this method is called. 

The default implementation takes care of `[KeyEvent.KEYCODE_BACK](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html#KEYCODE_BACK:kotlin.Int)` by calling `onBackPressed()`, though the behavior varies based on the application compatibility mode: for `[android.os.Build.VERSION_CODES#ECLAIR](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#ECLAIR:kotlin.Int)` or later applications, it will set up the dispatch to call `onKeyUp` where the action will be performed; for earlier applications, it will perform the action immediately in on-down, as those versions of the platform behaved. This implementation will also take care of `[KeyEvent.KEYCODE_ESCAPE](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html#KEYCODE_ESCAPE:kotlin.Int)` by finishing the activity if it would be closed by touching outside of it. 

Other additional default key handling may be performed if configured with `setDefaultKeyMode`.

Parameters  
---  
`keyCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The value in event.getKeyCode().  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: Description of the key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Return `true` to prevent this event from being propagated further, or `false` to indicate that you have not handled this event and it should continue to be propagated.  
  
**See Also**

  * `#onKeyUp`
  * `[android.view.KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)`



### onKeyLongPress

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onKeyLongPress(  
        keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Default implementation of `[KeyEvent.Callback.onKeyLongPress()](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html#onKeyLongPress\(kotlin.Int,%20android.view.KeyEvent\))`: always returns false (doesn't handle the event). To receive this callback, you must return true from onKeyDown for the current event stream.

Parameters  
---  
`keyCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The value in event.getKeyCode().  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: Description of the key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If you handled the event, return true. If you want to allow the event to be handled by the next receiver, return false.  
  
**See Also**

  * `[android.view.KeyEvent.Callback#onKeyLongPress(int,android.view.KeyEvent)](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html#onKeyLongPress\(kotlin.Int,%20android.view.KeyEvent\))`



### onKeyMultiple

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onKeyMultiple(  
        keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        repeatCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Default implementation of `[KeyEvent.Callback.onKeyMultiple()](https://developer.android.com/reference/kotlin/android/view/KeyEvent.Callback.html#onKeyMultiple\(kotlin.Int,%20kotlin.Int,%20android.view.KeyEvent\))`: always returns false (doesn't handle the event).

Parameters  
---  
`keyCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The value in event.getKeyCode().  
`count` | Number of pairs as returned by event.getRepeatCount().  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: Description of the key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If you handled the event, return true. If you want to allow the event to be handled by the next receiver, return false.  
  
### onKeyShortcut

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onKeyShortcut(  
        keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a key shortcut event is not handled by any of the views in the Activity. Override this method to implement global key shortcuts for the Activity. Key shortcuts can also be implemented by setting the `[shortcut](https://developer.android.com/reference/kotlin/android/view/MenuItem.html#setShortcut\(kotlin.Char,%20kotlin.Char\))` property of menu items.

Parameters  
---  
`keyCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The value in event.getKeyCode().  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: Description of the key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | True if the key shortcut was handled.  
  
### onKeyUp

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onKeyUp(  
        keyCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        event: [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a key was released and not handled by any of the views inside of the activity. So, for example, key presses while the cursor is inside a TextView will not trigger the event (unless it is a navigation to another object) because TextView handles its own key presses. 

The default implementation handles KEYCODE_BACK to stop the activity and go back.

Parameters  
---  
`keyCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The value in event.getKeyCode().  
`event` | [KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)!: Description of the key event.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Return `true` to prevent this event from being propagated further, or `false` to indicate that you have not handled this event and it should continue to be propagated.  
  
**See Also**

  * `#onKeyDown`
  * `[android.view.KeyEvent](https://developer.android.com/reference/kotlin/android/view/KeyEvent.html)`



### onLocalVoiceInteractionStarted

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onLocalVoiceInteractionStarted(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Callback to indicate that `startLocalVoiceInteraction(Bundle)` has resulted in a voice interaction session being started. You can now retrieve a voice interactor using `getVoiceInteractor()`.

### onLocalVoiceInteractionStopped

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onLocalVoiceInteractionStopped(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Callback to indicate that the local voice interaction has stopped either because it was requested through a call to `stopLocalVoiceInteraction()` or because it was canceled by the user. The previously acquired `[VoiceInteractor](https://developer.android.com/reference/kotlin/android/app/VoiceInteractor)` is no longer valid after this.

### onLowMemory

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onLowMemory(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called when the overall system is running low on memory, and actively running processes should trim their memory usage. While the exact point at which this will be called is not defined, generally it will happen when all background process have been killed. That is, before reaching the point of killing processes hosting service and foreground UI that we would like to avoid killing.

### onMenuItemSelected

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onMenuItemSelected(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Default implementation of `[android.view.Window.Callback#onMenuItemSelected](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onMenuItemSelected\(kotlin.Int,%20android.view.MenuItem\))` for activities. This calls through to the new `onOptionsItemSelected` method for the `[android.view.Window#FEATURE_OPTIONS_PANEL](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_OPTIONS_PANEL:kotlin.Int)` panel, so that subclasses of Activity don't need to deal with feature codes.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The panel that the menu is in.  
`item` | [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html): This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return true to finish processing of selection, or false to perform the normal menu handling (calling its Runnable or sending a Message to its target Handler).  
  
### onMenuOpened

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onMenuOpened(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a panel's menu is opened by the user. This may also be called when the menu is changing from one type to another (for example, from the icon menu to the expanded menu).

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The panel that the menu is in.  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html): This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | The default implementation returns true.  
  
### onMultiWindowModeChanged

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onMultiWindowModeChanged~~(isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`onMultiWindowModeChanged(boolean,Configuration)` instead._

Called by the system when the activity changes from fullscreen mode to multi-window mode and visa-versa.

Parameters  
---  
`isInMultiWindowMode` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): True if the activity is in multi-window mode.  
  
**See Also**

  * `[android.R.attr#resizeableActivity](https://developer.android.com/reference/kotlin/android/R.attr.html#resizeableActivity:kotlin.Int)`



### onMultiWindowModeChanged

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onMultiWindowModeChanged(  
        isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html),   
        newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called by the system when the activity changes from fullscreen mode to multi-window mode and visa-versa. This method provides the same configuration that will be sent in the following `onConfigurationChanged(Configuration)` call after the activity enters this mode.

Parameters  
---  
`isInMultiWindowMode` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): True if the activity is in multi-window mode.  
`newConfig` | [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!: The new configuration of the activity with the state `isInMultiWindowMode`.  
  
**See Also**

  * `[android.R.attr#resizeableActivity](https://developer.android.com/reference/kotlin/android/R.attr.html#resizeableActivity:kotlin.Int)`



### onNavigateUp

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onNavigateUp(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

This method is called whenever the user chooses to navigate Up within your application's activity hierarchy from the action bar. 

If the attribute `[parentActivityName](https://developer.android.com/reference/kotlin/android/R.attr.html#parentActivityName:kotlin.Int)` was specified in the manifest for this activity or an activity-alias to it, default Up navigation will be handled automatically. If any activity along the parent chain requires extra Intent arguments, the Activity subclass should override the method `onPrepareNavigateUpTaskStack(TaskStackBuilder)` to supply those arguments.

See [Tasks and Back Stack](https://developer.android.com/guide/components/tasks-and-back-stack.html) from the developer guide and [Navigation](https://developer.android.com/design/patterns/navigation.html) from the design guide for more information about navigating within your app.

See the `[TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)` class and the Activity methods `getParentActivityIntent()`, `shouldUpRecreateTask(Intent)`, and `navigateUpTo(Intent)` for help implementing custom Up navigation. The AppNavigation sample application in the Android SDK is also available for reference.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if Up navigation completed successfully and this Activity was finished, false otherwise.  
  
### onNavigateUpFromChild

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onNavigateUpFromChild~~(child: Activity!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_Use`onNavigateUp()` instead._

This is called when a child activity of this one attempts to navigate up. The default implementation simply calls onNavigateUp() on this activity (the parent).

Parameters  
---  
`child` | Activity!: The activity making the call.  
  
### onNewIntent

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onNewIntent(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html),   
        caller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as `onNewIntent(Intent)`, but with an extra parameter for the ComponentCaller instance associated with the app that sent the intent. 

If you want to retrieve the caller without overriding this method, call `getCurrentCaller` inside your existing `onNewIntent(Intent)`. 

Note that you should only override one #onNewIntent method.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): The new intent that was used to start the activity.   
This value cannot be `null`.  
`caller` | [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller): The `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` instance associated with the app that sent the intent.   
This value cannot be `null`.  
  
**See Also**

  * `[android.app.ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)`
  * `#onNewIntent(android.content.Intent)`
  * `#getCurrentCaller`
  * `#setIntent(android.content.Intent,android.app.ComponentCaller)`
  * `#getCaller`



### onOptionsItemSelected

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onOptionsItemSelected(item: [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

This hook is called whenever an item in your options menu is selected. The default implementation simply returns false to have the normal processing happen (calling the item's Runnable or sending a message to its Handler as appropriate). You can use this method for any items for which you would like to do processing without those other facilities. 

Derived classes should call through to the base class for it to perform the default menu handling.

Parameters  
---  
`item` | [MenuItem](https://developer.android.com/reference/kotlin/android/view/MenuItem.html): The menu item that was selected.   
This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean Return false to allow normal menu processing to proceed, true to consume it here.  
  
**See Also**

  * `#onCreateOptionsMenu`



### onOptionsMenuClosed

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onOptionsMenuClosed(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This hook is called whenever the options menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).

Parameters  
---  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!: The options menu as last shown or first initialized by onCreateOptionsMenu().  
  
### onPanelClosed

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPanelClosed(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Default implementation of `[android.view.Window.Callback.onPanelClosed(int,Menu)](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onPanelClosed\(kotlin.Int,%20android.view.Menu\))` for activities. This calls through to `onOptionsMenuClosed(Menu)` method for the `[android.view.Window#FEATURE_OPTIONS_PANEL](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_OPTIONS_PANEL:kotlin.Int)` panel, so that subclasses of Activity don't need to deal with feature codes. For context menus (`[Window.FEATURE_CONTEXT_MENU](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_CONTEXT_MENU:kotlin.Int)`), the `onContextMenuClosed(Menu)` will be called.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The panel that is being displayed.  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html): This value cannot be `null`.  
  
### onPerformDirectAction

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPerformDirectAction(  
        actionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),   
        arguments: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html),   
        cancellationSignal: [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html),   
        resultListener: [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!>  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called to perform an action previously defined by the app. Apps also have access to `getVoiceInteractor()` to follow up on the action.

Parameters  
---  
`actionId` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): The ID for the action you previously reported via `onGetDirectActions(CancellationSignal,Consumer)`.   
This value cannot be `null`.  
`arguments` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html): Any additional arguments provided by the caller that are specific to the given action.   
This value cannot be `null`.  
`cancellationSignal` | [CancellationSignal](https://developer.android.com/reference/kotlin/android/os/CancellationSignal.html): A signal to cancel the operation in progress.   
This value cannot be `null`.  
`resultListener` | [Consumer](https://developer.android.com/reference/kotlin/java/util/function/Consumer.html)<[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!>: The callback to provide the result back to the caller. You can call this on any thread. The result bundle is action specific.   
This value cannot be `null`.  
  
**See Also**

  * `#onGetDirectActions(android.os.CancellationSignal,java.util.function.Consumer)`



### onPictureInPictureModeChanged

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onPictureInPictureModeChanged~~(isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`onPictureInPictureModeChanged(boolean,Configuration)` instead._

Called by the system when the activity changes to and from picture-in-picture mode.

Parameters  
---  
`isInPictureInPictureMode` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): True if the activity is in picture-in-picture mode.  
  
**See Also**

  * `[android.R.attr#supportsPictureInPicture](https://developer.android.com/reference/kotlin/android/R.attr.html#supportsPictureInPicture:kotlin.Int)`



### onPictureInPictureModeChanged

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPictureInPictureModeChanged(  
        isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html),   
        newConfig: [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called by the system when the activity changes to and from picture-in-picture mode. This method provides the same configuration that will be sent in the following `onConfigurationChanged(Configuration)` call after the activity enters this mode.

Parameters  
---  
`isInPictureInPictureMode` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): True if the activity is in picture-in-picture mode.  
`newConfig` | [Configuration](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html)!: The new configuration of the activity with the state `isInPictureInPictureMode`.  
  
**See Also**

  * `[android.R.attr#supportsPictureInPicture](https://developer.android.com/reference/kotlin/android/R.attr.html#supportsPictureInPicture:kotlin.Int)`



### onPictureInPictureRequested

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPictureInPictureRequested(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

This method is called by the system in various cases where picture in picture mode should be entered if supported. 

It is up to the app developer to choose whether to call `enterPictureInPictureMode(PictureInPictureParams)` at this time. For example, the system will call this method when the activity is being put into the background, so the app developer might want to switch an activity into PIP mode instead.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `true` if the activity received this callback regardless of if it acts on it or not. If `false`, the framework will assume the app hasn't been updated to leverage this callback and will in turn send a legacy callback of `onUserLeaveHint()` for the app to enter picture-in-picture mode.  
  
### onPictureInPictureUiStateChanged

Added in [API level 31](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPictureInPictureUiStateChanged(pipState: [PictureInPictureUiState](https://developer.android.com/reference/kotlin/android/app/PictureInPictureUiState)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called by the system when the activity is in PiP and has state changes. Compare to `onPictureInPictureModeChanged(boolean,Configuration)`, which is only called when PiP mode changes (meaning, enters or exits PiP), this can be called at any time while the activity is in PiP mode. Therefore, all invocation can only happen after `onPictureInPictureModeChanged(boolean,Configuration)` is called with true, and before `onPictureInPictureModeChanged(boolean,Configuration)` is called with false. You would not need to worry about cases where this is called and the activity is not in Picture-In-Picture mode. For managing cases where the activity enters/exits Picture-in-Picture (e.g. resources clean-up on exit), use `onPictureInPictureModeChanged(boolean,Configuration)`. The default state is everything declared in `[PictureInPictureUiState](https://developer.android.com/reference/kotlin/android/app/PictureInPictureUiState)` is false, such as `[PictureInPictureUiState.isStashed()](https://developer.android.com/reference/kotlin/android/app/PictureInPictureUiState#isStashed\(\))`.

Parameters  
---  
`pipState` | [PictureInPictureUiState](https://developer.android.com/reference/kotlin/android/app/PictureInPictureUiState): the new Picture-in-Picture state.   
This value cannot be `null`.  
  
### onPostCreate

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPostCreate(  
        savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?,   
        persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is the same as `onPostCreate(Bundle)` but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`.

Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: The data most recently supplied in #onSaveInstanceState   
This value may be `null`.  
`persistentState` | [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?: The data coming from the PersistableBundle first saved in `onSaveInstanceState(Bundle,PersistableBundle)`.   
This value may be `null`.  
  
**See Also**




### onPrepareNavigateUpTaskStack

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPrepareNavigateUpTaskStack(builder: [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Prepare the synthetic task stack that will be generated during Up navigation from a different task. 

This method receives the `[TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)` with the constructed series of Intents as generated by `onCreateNavigateUpTaskStack(TaskStackBuilder)`. If any extra data should be added to these intents before launching the new task, the application should override this method and add that data here.

Parameters  
---  
`builder` | [TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)!: A TaskStackBuilder that has been populated with Intents by onCreateNavigateUpTaskStack.  
  
### onPrepareOptionsMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPrepareOptionsMenu(menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Prepare the Screen's standard options menu to be displayed. This is called right before the menu is shown, every time it is shown. You can use this method to efficiently enable/disable items or otherwise dynamically modify the contents. 

The default implementation updates the system menu items based on the activity's state. Deriving classes should always call through to the base class implementation.

Parameters  
---  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)!: The options menu as last shown or first initialized by onCreateOptionsMenu().  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | You must return true for the menu to be displayed; if you return false it will not be shown.  
  
**See Also**

  * `#onCreateOptionsMenu`



### onPreparePanel

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onPreparePanel(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)?,   
        menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Default implementation of `[android.view.Window.Callback#onPreparePanel](https://developer.android.com/reference/kotlin/android/view/Window.Callback.html#onPreparePanel\(kotlin.Int,%20android.view.View,%20android.view.Menu\))` for activities. This calls through to the new `onPrepareOptionsMenu` method for the `[android.view.Window#FEATURE_OPTIONS_PANEL](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_OPTIONS_PANEL:kotlin.Int)` panel, so that subclasses of Activity don't need to deal with feature codes.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The panel that is being displayed.  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)?: This value may be `null`.  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html): This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | boolean You must return true for the panel to be displayed; if you return false it will not be shown.  
  
### onProvideAssistContent

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onProvideAssistContent(outContent: [AssistContent](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called when the user is requesting an assist, to provide references to content related to the current activity. Before being called, the `outContent` Intent is filled with the base Intent of the activity (the Intent returned by `getIntent()`). The Intent's extras are stripped of any types that are not valid for `[PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)` or non-framework Parcelables, and the flags `[Intent.FLAG_GRANT_WRITE_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_WRITE_URI_PERMISSION:kotlin.Int)` and `[Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_PERSISTABLE_URI_PERMISSION:kotlin.Int)` are cleared from the Intent. 

Custom implementation may adjust the content intent to better reflect the top-level context of the activity, and fill in its ClipData with additional content of interest that the user is currently viewing. For example, an image gallery application that has launched in to an activity allowing the user to swipe through pictures should modify the intent to reference the current image they are looking it; such an application when showing a list of pictures should add a ClipData that has references to all of the pictures currently visible on screen.

Parameters  
---  
`outContent` | [AssistContent](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent)!: The assist content to return.  
  
### onProvideAssistData

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onProvideAssistData(data: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called when the user is requesting an assist, to build a full `[Intent.ACTION_ASSIST](https://developer.android.com/reference/kotlin/android/content/Intent.html#ACTION_ASSIST:kotlin.String)` Intent with all of the context of the current application. You can override this method to place into the bundle anything you would like to appear in the `[Intent.EXTRA_ASSIST_CONTEXT](https://developer.android.com/reference/kotlin/android/content/Intent.html#EXTRA_ASSIST_CONTEXT:kotlin.String)` part of the assist Intent. 

This function will be called after any global assist callbacks that had been registered with `[Application.registerOnProvideAssistDataListener](https://developer.android.com/reference/kotlin/android/app/Application#registerOnProvideAssistDataListener\(android.app.Application.OnProvideAssistDataListener\))`.

### onProvideKeyboardShortcuts

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onProvideKeyboardShortcuts(  
        data: [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[KeyboardShortcutGroup](https://developer.android.com/reference/kotlin/android/view/KeyboardShortcutGroup.html)!>!,   
        menu: [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)?,   
        deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when Keyboard Shortcuts are requested for the current window.

Parameters  
---  
`data` | [MutableList](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)<[KeyboardShortcutGroup](https://developer.android.com/reference/kotlin/android/view/KeyboardShortcutGroup.html)!>!: The data list to populate with shortcuts.  
`menu` | [Menu](https://developer.android.com/reference/kotlin/android/view/Menu.html)?: The current menu, which may be null.  
`deviceId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id for the connected device the shortcuts should be provided for.  
  
### onProvideReferrer

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onProvideReferrer(): [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!

Override to generate the desired referrer for the content currently being shown by the app. The default implementation returns null, meaning the referrer will simply be the android-app: of the package name of this activity. Return a non-null Uri to have that supplied as the `[Intent.EXTRA_REFERRER](https://developer.android.com/reference/kotlin/android/content/Intent.html#EXTRA_REFERRER:kotlin.String)` of any activities started from it.

### onRequestPermissionsResult

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onRequestPermissionsResult(  
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>,   
        grantResults: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Callback for the result from requesting permissions. This method is invoked for every call on #requestPermissions 

**Note:** It is possible that the permissions request interaction with the user is interrupted. In this case you will receive empty permissions and results arrays which should be treated as a cancellation. 

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The request code passed in #requestPermissions.  
`permissions` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>: The requested permissions. Never null.  
`grantResults` | [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html): The grant results for the corresponding permissions which is either `[android.content.pm.PackageManager#PERMISSION_GRANTED](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#PERMISSION_GRANTED:kotlin.Int)` or `[android.content.pm.PackageManager#PERMISSION_DENIED](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#PERMISSION_DENIED:kotlin.Int)`. Never null.  
  
**See Also**




### onRequestPermissionsResult

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onRequestPermissionsResult(  
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>,   
        grantResults: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html),   
        deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Callback for the result from requesting permissions. This method is invoked for every call on #requestPermissions. 

**Note:** It is possible that the permissions request interaction with the user is interrupted. In this case you will receive empty permissions and results arrays which should be treated as a cancellation. 

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The request code passed in #requestPermissions.  
`permissions` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>: The requested permissions. Never null.  
`grantResults` | [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html): The grant results for the corresponding permissions which is either `[android.content.pm.PackageManager#PERMISSION_GRANTED](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#PERMISSION_GRANTED:kotlin.Int)` or `[android.content.pm.PackageManager#PERMISSION_DENIED](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#PERMISSION_DENIED:kotlin.Int)`. Never null.  
`deviceId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The deviceId for which permissions were requested. The primary/physical device is assigned `[Context.DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)`, and virtual devices are assigned unique device Ids.  
  
**See Also**




### onRestoreInstanceState

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onRestoreInstanceState(  
        savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?,   
        persistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is the same as `onRestoreInstanceState(Bundle)` but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`. The `[android.os.PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)` passed came from the restored PersistableBundle first saved in `onSaveInstanceState(Bundle,PersistableBundle)`. 

This method is called between `onStart` and #onPostCreate. 

If this method is called `onRestoreInstanceState(Bundle)` will not be called. 

At least one of `savedInstanceState` or `persistentState` will not be null.

Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: the data most recently supplied in #onSaveInstanceState or null.  
`persistentState` | [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)?: the data most recently supplied in #onSaveInstanceState or null.  
  
**See Also**

  * `#onRestoreInstanceState(android.os.Bundle)`
  * `#onResume`



### onRetainNonConfigurationInstance

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onRetainNonConfigurationInstance(): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!

Called by the system, as part of destroying an activity due to a configuration change, when it is known that a new instance will immediately be created for the new configuration. You can return any object you like here, including the activity instance itself, which can later be retrieved by calling `getLastNonConfigurationInstance()` in the new activity instance. _If you are targeting`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, consider instead using a `[Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment)` with `[Fragment.setRetainInstance(boolean](https://developer.android.com/reference/kotlin/android/app/Fragment#setRetainInstance\(kotlin.Boolean\))`._

This function is called purely as an optimization, and you must not rely on it being called. When it is called, a number of guarantees will be made to help optimize configuration switching: 

  * The function will be called between `onStop` and `onDestroy`. 
  * A new instance of the activity will _always_ be immediately created after this one's `onDestroy()` is called. In particular, _no_ messages will be dispatched during this time (when the returned object does not have an activity to be associated with). 
  * The object you return here will _always_ be available from the `getLastNonConfigurationInstance()` method of the following activity instance as described there. 



These guarantees are designed so that an activity can use this API to propagate extensive state from the old to new activity instance, from loaded bitmaps, to network connections, to evenly actively running threads. Note that you should _not_ propagate any data that may change based on the configuration, including any data loaded from resources such as strings, layouts, or drawables. 

The guarantee of no message handling during the switch to the next activity simplifies use with active objects. For example if your retained state is an `[android.os.AsyncTask](https://developer.android.com/reference/kotlin/android/os/AsyncTask.html)` you are guaranteed that its call back functions (like `[android.os.AsyncTask#onPostExecute](https://developer.android.com/reference/kotlin/android/os/AsyncTask.html#onPostExecute\(android.os.AsyncTask.Result\))`) will not be called from the call here until you execute the next instance's `onCreate(Bundle)`. (Note however that there is of course no such guarantee for `[android.os.AsyncTask#doInBackground](https://developer.android.com/reference/kotlin/android/os/AsyncTask.html#doInBackground\(android.os.AsyncTask.Params\))` since that is running in a separate thread.) 

**Note:** For most cases you should use the `[Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment)` API `[Fragment.setRetainInstance(boolean)](https://developer.android.com/reference/kotlin/android/app/Fragment#setRetainInstance\(kotlin.Boolean\))` instead; this is also available on older platforms through the Android support libraries.

Return  
---  
`[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)!` | any Object holding the desired state to propagate to the next activity instance  
  
### onSaveInstanceState

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onSaveInstanceState(  
        outState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html),   
        outPersistentState: [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is the same as #onSaveInstanceState but is called for activities created with the attribute `[android.R.attr#persistableMode](https://developer.android.com/reference/kotlin/android/R.attr.html#persistableMode:kotlin.Int)` set to `persistAcrossReboots`. The `[android.os.PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html)` passed in will be saved and presented in `onCreate(Bundle,PersistableBundle)` the first time that this activity is restarted following the next device reboot or after an update.

Parameters  
---  
`outState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html): Bundle in which to place your saved state.   
This value cannot be `null`.  
`outPersistentState` | [PersistableBundle](https://developer.android.com/reference/kotlin/android/os/PersistableBundle.html): State which will be saved across reboots and updates.   
This value cannot be `null`.  
  
**See Also**

  * `#onSaveInstanceState(android.os.Bundle)`
  * `#onRestoreInstanceState(android.os.Bundle,android.os.PersistableBundle)`
  * `#onPause`



### onSearchRequested

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onSearchRequested(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if search launched, false if activity refuses (blocks)  
  
**See Also**

  * `#onSearchRequested(android.view.SearchEvent)`



### onSearchRequested

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onSearchRequested(searchEvent: [SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)?): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

This hook is called when the user signals the desire to start a search. 

You can use this function as a simple way to launch the search UI, in response to a menu item, search button, or other widgets within your activity. Unless overridden, calling this function is the same as calling `startSearch(null, false, null, false)`, which launches search for the current activity as specified in its manifest, see `[SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)`. 

You can override this function to force global search, e.g. in response to a dedicated search key, or to block search entirely (by simply returning false). 

Note: when running in a `[Configuration.UI_MODE_TYPE_TELEVISION](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html#UI_MODE_TYPE_TELEVISION:kotlin.Int)` or `[Configuration.UI_MODE_TYPE_WATCH](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html#UI_MODE_TYPE_WATCH:kotlin.Int)`, the default implementation changes to simply return false and you must supply your own custom implementation if you want to support search.

Parameters  
---  
`searchEvent` | [SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)?: The `[SearchEvent](https://developer.android.com/reference/kotlin/android/view/SearchEvent.html)` that signaled this search.   
This value may be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns `true` if search launched, and `false` if the activity does not respond to search. The default implementation always returns `true`, except when in `[Configuration.UI_MODE_TYPE_TELEVISION](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html#UI_MODE_TYPE_TELEVISION:kotlin.Int)` mode where it returns false.  
  
**See Also**

  * `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)`



### onStateNotSaved

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onStateNotSaved~~(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_starting with`[android.os.Build.VERSION_CODES#P](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#P:kotlin.Int)` onSaveInstanceState is called after `onStop`, so this hint isn't accurate anymore: you should consider your state not saved in between `onStart` and `onStop` callbacks inclusively._

Called when an `onResume` is coming up, prior to other pre-resume callbacks such as #onNewIntent and #onActivityResult. This is primarily intended to give the activity a hint that its state is no longer saved -- it will generally be called after #onSaveInstanceState and prior to the activity being resumed/started again.

### onTopResumedActivityChanged

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onTopResumedActivityChanged(isTopResumedActivity: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when activity gets or loses the top resumed position in the system. 

Starting with `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` multiple activities can be resumed at the same time in multi-window and multi-display modes. This callback should be used instead of `onResume()` as an indication that the activity can try to open exclusive-access devices like camera.

It will always be delivered after the activity was resumed and before it is paused. In some cases it might be skipped and activity can go straight from `onResume()` to `onPause()` without receiving the top resumed state.

Parameters  
---  
`isTopResumedActivity` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` if it's the topmost resumed activity in the system, `false` otherwise. A call with this as `true` will always be followed by another one with `false`.  
  
**See Also**

  * `#onResume()`
  * `#onPause()`
  * `#onWindowFocusChanged(boolean)`



### onTouchEvent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onTouchEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when a touch screen event was not handled by any of the views inside of the activity. This is most useful to process touch events that happen outside of your window bounds, where there is no view to receive it.

Parameters  
---  
`event` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The touch screen event being processed.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Return true if you have consumed the event, false if you haven't.  
  
### onTrackballEvent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onTrackballEvent(event: [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Called when the trackball was moved and not handled by any of the views inside of the activity. So, for example, if the trackball moves while focus is on a button, you will receive a call here because buttons do not normally do anything with trackball events. The call here happens _before_ trackball movements are converted to DPAD key events, which then get sent back to the view hierarchy, and will be processed at the point for things like focus navigation.

Parameters  
---  
`event` | [MotionEvent](https://developer.android.com/reference/kotlin/android/view/MotionEvent.html)!: The trackball event being processed.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Return true if you have consumed the event, false if you haven't. The default implementation always returns false.  
  
### onTrimMemory

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onTrimMemory(level: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process. You should never compare to exact values of the level, since new intermediate values may be added -- you will typically want to compare if the value is greater or equal to a level you are interested in. 

To retrieve the processes current trim level at any point, you can use `[ActivityManager.getMyMemoryState(RunningAppProcessInfo)](https://developer.android.com/reference/kotlin/android/app/ActivityManager#getMyMemoryState\(android.app.ActivityManager.RunningAppProcessInfo\))`.

Parameters  
---  
`level` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The context of the trim, giving a hint of the amount of trimming the application may like to perform.   
Value is one of the following: 

  * `[TRIM_MEMORY_COMPLETE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_COMPLETE:kotlin.Int)`
  * `[TRIM_MEMORY_MODERATE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_MODERATE:kotlin.Int)`
  * `[TRIM_MEMORY_BACKGROUND](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_BACKGROUND:kotlin.Int)`
  * `[TRIM_MEMORY_UI_HIDDEN](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_UI_HIDDEN:kotlin.Int)`
  * `[TRIM_MEMORY_RUNNING_CRITICAL](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_CRITICAL:kotlin.Int)`
  * `[TRIM_MEMORY_RUNNING_LOW](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_LOW:kotlin.Int)`
  * `[TRIM_MEMORY_RUNNING_MODERATE](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html#TRIM_MEMORY_RUNNING_MODERATE:kotlin.Int)`

  
  
### onUserInteraction

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onUserInteraction(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called whenever a key, touch, or trackball event is dispatched to the activity. Implement this method if you wish to know that the user has interacted with the device in some way while your activity is running. This callback and `onUserLeaveHint` are intended to help activities manage status bar notifications intelligently; specifically, for helping activities determine the proper time to cancel a notification. 

All calls to your activity's `onUserLeaveHint` callback will be accompanied by calls to `onUserInteraction`. This ensures that your activity will be told of relevant user activity such as pulling down the notification pane and touching an item there. 

Note that this callback will be invoked for the touch down action that begins a touch gesture, but may not be invoked for the touch-moved and touch-up actions that follow.

**See Also**

  * `#onUserLeaveHint()`



### onVisibleBehindCanceled

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~onVisibleBehindCanceled~~(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_This method's functionality is no longer supported as of`[android.os.Build.VERSION_CODES#O](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O:kotlin.Int)` and will be removed in a future release._

Called when a translucent activity over this activity is becoming opaque or another activity is being launched. Activities that override this method must call `super.onVisibleBehindCanceled()` or a SuperNotCalledException will be thrown. 

When this method is called the activity has 500 msec to release any resources it may be using while visible in the background. If the activity has not returned from this method in 500 msec the system will destroy the activity and kill the process in order to recover the resources for another process. Otherwise `onStop()` will be called following return.   
If you override this method you _must_ call through to the superclass implementation.

**See Also**

  * `#requestVisibleBehind(boolean)`



### onWindowAttributesChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onWindowAttributesChanged(params: [WindowManager.LayoutParams](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called whenever the current window attributes change.

### onWindowFocusChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onWindowFocusChanged(hasFocus: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when the current `[Window](https://developer.android.com/reference/kotlin/android/view/Window.html)` of the activity gains or loses focus. This is the best indicator of whether this activity is the entity with which the user actively interacts. The default implementation clears the key tracking state, so should always be called. 

Note that this provides information about global focus state, which is managed independently of activity lifecycle. As such, while focus changes will generally have some relation to lifecycle changes (an activity that is stopped will not generally get window focus), you should not rely on any particular order between the callbacks here and those in the other lifecycle methods such as `onResume`. 

As a general rule, however, a foreground activity will have window focus... unless it has displayed other dialogs or popups that take input focus, in which case the activity itself will not have focus when the other windows have it. Likewise, the system may display system-level windows (such as the status bar notification panel or a system alert) which will temporarily take window input focus without pausing the foreground activity. 

Starting with `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` there can be multiple resumed activities at the same time in multi-window mode, so resumed state does not guarantee window focus even if there are no overlays above. 

If the intent is to know when an activity is the topmost active, the one the user interacted with last among all activities but not including non-activity windows like dialogs and popups, then `onTopResumedActivityChanged(boolean)` should be used. On platform versions prior to `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)`, `onResume` is the best indicator.

Parameters  
---  
`hasFocus` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): Whether the window of this activity has focus.  
  
**See Also**

  * `#hasWindowFocus()`
  * `#onResume`
  * `[android.view.View#onWindowFocusChanged(boolean)](https://developer.android.com/reference/kotlin/android/view/View.html#onWindowFocusChanged\(kotlin.Boolean\))`
  * `#onTopResumedActivityChanged(boolean)`



### onWindowStartingActionMode

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onWindowStartingActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!): [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?

Give the Activity a chance to control the UI for an action mode requested by the system. 

Note: If you are looking for a notification callback that an action mode has been started for this activity, see `onActionModeStarted(ActionMode)`.

Parameters  
---  
`callback` | [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!: The callback that should control the new action mode  
Return  
---  
`[ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?` | The new action mode, or `null` if the activity does not want to provide special handling for this action mode. (It will be handled by the system.)  
  
### onWindowStartingActionMode

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun onWindowStartingActionMode(  
        callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!,   
        type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?

Called when an action mode is being started for this window. Gives the callback an opportunity to handle the action mode in its own unique and beautiful way. If this method returns null the system can choose a way to present the mode or choose not to start the mode at all.

Parameters  
---  
`callback` | [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!: Callback to control the lifecycle of this action mode  
`type` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): One of `[ActionMode.TYPE_PRIMARY](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_PRIMARY:kotlin.Int)` or `[ActionMode.TYPE_FLOATING](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_FLOATING:kotlin.Int)`.  
Return  
---  
`[ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?` | This value may be `null`.  
  
### openContextMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun openContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Programmatically opens the context menu for a particular `view`. The `view` should have been added via `registerForContextMenu(View)`.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The view to show the context menu for.  
  
### openOptionsMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun openOptionsMenu(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Programmatically opens the options menu. If the options menu is already open, this method does nothing.

### overrideActivityTransition

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun overrideActivityTransition(  
        overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Customizes the animation for activity transitions. 

This method provides a robust way to override transition animations at runtime and can be called at any point in the activity's lifecycle. It is particularly useful for handling predictive back animations, for which `overridePendingTransition(int,int)` is not suitable.

The specified animations will be applied only when this activity is at the top of the task stack during the transition. For example, to customize the opening animation for an Activity B started from Activity A, call this method in B's `onCreate` with `overrideType = OVERRIDE_TRANSITION_OPEN`. To customize the closing animation when returning from B to A, call this method in B with `overrideType = OVERRIDE_TRANSITION_CLOSE`.

**Animation Precedence:**

  * Animations set by `overridePendingTransition(int,int)` have the highest priority.
  * Animations set by this method have higher priority than those defined by `[Window.setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`.



**Predictive Back Animation:**

When predictive back is enabled (see `enableOnBackInvokedCallback` in the manifest), the system may control the preview phase of the back animation. The custom transition defined by `enterAnim` and `exitAnim` is then applied only after the back gesture is committed.

**Limitations:**

  * This method, along with `overridePendingTransition(int,int)` and `[Window.setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`, is ignored if the activity is started with `[ActivityOptions.makeSceneTransitionAnimation(Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`.
  * As of Android 11, this method cannot be used to customize cross-task transitions.

Parameters  
---  
`overrideType` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The type of transition to override. Must be either `OVERRIDE_TRANSITION_OPEN` for entering transitions or `OVERRIDE_TRANSITION_CLOSE` for exiting transitions.   
Value is one of the following: 

  * `OVERRIDE_TRANSITION_OPEN`
  * `OVERRIDE_TRANSITION_CLOSE`

  
`enterAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The resource ID of the animation for the incoming activity. Use 0 for no animation.  
`exitAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The resource ID of the animation for the outgoing activity. Use 0 for no animation.  
  
**See Also**

  * `#overrideActivityTransition(int,int,int,int)`
  * `#clearOverrideActivityTransition(int)`
  * `[android.window.OnBackInvokedCallback](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedCallback.html)`
  * `#overridePendingTransition(int,int)`
  * `[android.view.Window#setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`
  * `[android.app.ActivityOptions#makeSceneTransitionAnimation(android.app.Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`



### overrideActivityTransition

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun overrideActivityTransition(  
        overrideType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        backgroundColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Customizes the animation and background color for activity transitions. 

This method provides a robust way to override transition animations at runtime and can be called at any point in the activity's lifecycle. It is particularly useful for handling predictive back animations, for which `overridePendingTransition(int,int)` is not suitable.

The specified animations will be applied only when this activity is at the top of the task stack during the transition. For example, to customize the opening animation for an Activity B started from Activity A, call this method in B's `onCreate` with `overrideType = OVERRIDE_TRANSITION_OPEN`. To customize the closing animation when returning from B to A, call this method in B with `overrideType = OVERRIDE_TRANSITION_CLOSE`.

**Animation Precedence:**

  * Animations set by `overridePendingTransition(int,int)` have the highest priority.
  * Animations set by this method have higher priority than those defined by `[Window.setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`.



**Predictive Back Animation:**

When predictive back is enabled (see `enableOnBackInvokedCallback` in the manifest), the system may control the preview phase of the back animation. The custom transition defined by `enterAnim` and `exitAnim` is then applied only after the back gesture is committed.

**Limitations:**

  * This method, along with `overridePendingTransition(int,int)` and `[Window.setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`, is ignored if the activity is started with `[ActivityOptions.makeSceneTransitionAnimation(Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`.
  * As of Android 11, this method cannot be used to customize cross-task transitions.

Parameters  
---  
`overrideType` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The type of transition to override. Must be either `OVERRIDE_TRANSITION_OPEN` for entering transitions or `OVERRIDE_TRANSITION_CLOSE` for exiting transitions.   
Value is one of the following: 

  * `OVERRIDE_TRANSITION_OPEN`
  * `OVERRIDE_TRANSITION_CLOSE`

  
`enterAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The resource ID of the animation for the incoming activity. Use 0 for no animation.  
`exitAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The resource ID of the animation for the outgoing activity. Use 0 for no animation.  
`backgroundColor` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The background color to display during the animation. Set to `[Color.TRANSPARENT](https://developer.android.com/reference/kotlin/android/graphics/Color.html#TRANSPARENT:kotlin.Int)` to use the default background color.  
  
**See Also**

  * `#overrideActivityTransition(int,int,int)`
  * `#clearOverrideActivityTransition(int)`
  * `[android.window.OnBackInvokedCallback](https://developer.android.com/reference/kotlin/android/window/OnBackInvokedCallback.html)`
  * `#overridePendingTransition(int,int)`
  * `[android.view.Window#setWindowAnimations(int)](https://developer.android.com/reference/kotlin/android/view/Window.html#setWindowAnimations\(kotlin.Int\))`
  * `[android.app.ActivityOptions#makeSceneTransitionAnimation(android.app.Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`



### overridePendingTransition

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~overridePendingTransition~~(  
        enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`overrideActivityTransition(int,int,int)`} instead._

Call immediately after one of the flavors of #startActivity(android.content.Intent) or `finish` to specify an explicit transition animation to perform next. 

As of `[android.os.Build.VERSION_CODES#JELLY_BEAN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#JELLY_BEAN:kotlin.Int)` an alternative to using this with starting activities is to supply the desired animation information through a `[ActivityOptions](https://developer.android.com/reference/kotlin/android/app/ActivityOptions)` bundle to #startActivity(android.content.Intent,android.os.Bundle) or a related function. This allows you to specify a custom animation even when starting an activity from outside the context of the current top activity. 

Af of `[android.os.Build.VERSION_CODES#S](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#S:kotlin.Int)` application can only specify a transition animation when the transition happens within the same task. System default animation is used for cross-task transition animations.

Parameters  
---  
`enterAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): A resource ID of the animation resource to use for the incoming activity. Use 0 for no animation.  
`exitAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): A resource ID of the animation resource to use for the outgoing activity. Use 0 for no animation.  
  
### overridePendingTransition

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~overridePendingTransition~~(  
        enterAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        exitAnim: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        backgroundColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`overrideActivityTransition(int,int,int,int)`} instead._

Call immediately after one of the flavors of #startActivity(android.content.Intent) or `finish` to specify an explicit transition animation to perform next. 

As of `[android.os.Build.VERSION_CODES#JELLY_BEAN](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#JELLY_BEAN:kotlin.Int)` an alternative to using this with starting activities is to supply the desired animation information through a `[ActivityOptions](https://developer.android.com/reference/kotlin/android/app/ActivityOptions)` bundle to #startActivity(android.content.Intent,android.os.Bundle) or a related function. This allows you to specify a custom animation even when starting an activity from outside the context of the current top activity.

Parameters  
---  
`enterAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): A resource ID of the animation resource to use for the incoming activity. Use 0 for no animation.  
`exitAnim` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): A resource ID of the animation resource to use for the outgoing activity. Use 0 for no animation.  
`backgroundColor` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The background color to use for the background during the animation if the animation requires a background. Set to 0 to not override the default color.  
  
### postponeEnterTransition

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun postponeEnterTransition(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Postpone the entering activity transition when Activity was started with `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`. 

This method gives the Activity the ability to delay starting the entering and shared element transitions until all data is loaded. Until then, the Activity won't draw into its window, leaving the window transparent. This may also cause the returning animation to be delayed until data is ready. This method should be called in `onCreate(android.os.Bundle)` or in `onActivityReenter(int,android.content.Intent)`. `startPostponedEnterTransition()` must be called to allow the Activity to start the transitions. If the Activity did not use `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.util.Pair[])](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.util.Pair\))`, then this method does nothing.

### recreate

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun recreate(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Cause this Activity to be recreated with a new instance. This results in essentially the same flow as when the Activity is created due to a configuration change -- the current instance will go through its lifecycle to `onDestroy` and a new instance then created after it.

### registerActivityLifecycleCallbacks

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun registerActivityLifecycleCallbacks(callback: [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Register an `[Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)` instance that receives lifecycle callbacks for only this Activity. 

In relation to any `[Application registered callbacks](https://developer.android.com/reference/kotlin/android/app/Application#registerActivityLifecycleCallbacks\(android.app.Application.ActivityLifecycleCallbacks\))`, the callbacks registered here will always occur nested within those callbacks. This means: 

  * Pre events will first be sent to Application registered callbacks, then to callbacks registered here.
  * `[Application.ActivityLifecycleCallbacks.onActivityCreated(Activity,Bundle)](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks#onActivityCreated\(android.app.Activity,%20android.os.Bundle\))`, `[Application.ActivityLifecycleCallbacks.onActivityStarted(Activity)](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks#onActivityStarted\(android.app.Activity\))`, and `[Application.ActivityLifecycleCallbacks.onActivityResumed(Activity)](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks#onActivityResumed\(android.app.Activity\))` will be sent first to Application registered callbacks, then to callbacks registered here. For all other events, callbacks registered here will be sent first.
  * Post events will first be sent to callbacks registered here, then to Application registered callbacks.



If multiple callbacks are registered here, they receive events in a first in (up through `[Application.ActivityLifecycleCallbacks.onActivityPostResumed](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks#onActivityPostResumed\(android.app.Activity\))`, last out ordering. 

It is strongly recommended to register this in the constructor of your Activity to ensure you get all available callbacks. As this callback is associated with only this Activity, it is not usually necessary to `unregister` it unless you specifically do not want to receive further lifecycle callbacks.

Parameters  
---  
`callback` | [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks): The callback instance to register.   
This value cannot be `null`.  
  
### registerComponentCallbacks

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun registerComponentCallbacks(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Add a new `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to the base application of the Context, which will be called at the same times as the ComponentCallbacks methods of activities and other components are called. Note that you _must_ be sure to use `[unregisterComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#unregisterComponentCallbacks\(android.content.ComponentCallbacks\))` when appropriate in the future; this will not be removed for you. 

After `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)`, the `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` will be registered to `[the base Context](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getBaseContext\(\))`, and can be only used after `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`. Users can still call to `getApplicationContext().registerComponentCallbacks(ComponentCallbacks)` to add `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` to the base application.

Parameters  
---  
`callback` | [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!: The interface to call. This can be either a `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` or `[ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html)` interface.  
Exceptions  
---  
`java.lang.IllegalStateException` | if this method calls before `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`  
  
### registerForContextMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun registerForContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Registers a context menu to be shown for the given view (multiple views can show the context menu). This method will set the `[OnCreateContextMenuListener](https://developer.android.com/reference/kotlin/android/view/View.OnCreateContextMenuListener.html)` on the view to this activity, so `onCreateContextMenu(ContextMenu,View,ContextMenuInfo)` will be called when it is time to show the context menu.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The view that should show a context menu.  
  
**See Also**

  * `#unregisterForContextMenu(android.view.View)`



### registerScreenCaptureCallback

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun registerScreenCaptureCallback(  
        executor: [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html),   
        callback: [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Registers a screen capture callback for this activity. The callback will be triggered when a screen capture of this activity is attempted. This callback will be executed on the thread of the passed `executor`. For details, see `[ScreenCaptureCallback.onScreenCaptured](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback#onScreenCaptured\(\))`.   
Requires `[android.Manifest.permission#DETECT_SCREEN_CAPTURE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#DETECT_SCREEN_CAPTURE:kotlin.String)`

Parameters  
---  
`executor` | [Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html): This value cannot be `null`.   
Callback and listener events are dispatched through this `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)`, providing an easy way to control which thread is used. To dispatch events through the main thread of your application, you can use `[Context.getMainExecutor()](https://developer.android.com/reference/kotlin/android/content/Context.html#getMainExecutor\(\))`. Otherwise, provide an `[Executor](https://developer.android.com/reference/kotlin/java/util/concurrent/Executor.html)` that dispatches to an appropriate thread.  
`callback` | [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback): This value cannot be `null`.  
  
### releaseInstance

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun releaseInstance(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Ask that the local app instance of this activity be released to free up its memory. This is asking for the activity to be destroyed, but does **not** finish the activity -- a new instance of the activity will later be re-created if needed due to the user navigating back to it.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns true if the activity was in a state that it has started the process of destroying its current instance; returns false if for any reason this could not be done: it is currently visible to the user, it is already being destroyed, it is being finished, it hasn't yet saved its state, etc.  
  
### removeDialog

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~removeDialog~~(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Removes any internal references to a dialog managed by this Activity. If the dialog is showing, it will dismiss it as part of the clean up. 

This can be useful if you know that you will never show a dialog again and want to avoid the overhead of saving and restoring it in the future. 

As of `[android.os.Build.VERSION_CODES#GINGERBREAD](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#GINGERBREAD:kotlin.Int)`, this function will not throw an exception if you try to remove an ID that does not currently have an associated dialog.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id of the managed dialog.  
  
**See Also**

  * `#onCreateDialog(int,android.os.Bundle)`
  * `#onPrepareDialog(int,android.app.Dialog,android.os.Bundle)`
  * `#showDialog(int)`
  * `#dismissDialog(int)`



### reportFullyDrawn

Added in [API level 19](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun reportFullyDrawn(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Report to the system that your app is now fully drawn, for diagnostic and optimization purposes. The system may adjust optimizations to prioritize work that happens before reportFullyDrawn is called, to improve app startup. Misrepresenting the startup window by calling reportFullyDrawn too late or too early may decrease application and startup performance.

This is also used to help instrument application launch times, so that the app can report when it is fully in a usable state; without this, the only thing the system itself can determine is the point at which the activity's window is _first_ drawn and displayed. To participate in app launch time measurement, you should always call this method after first launch (when `onCreate(android.os.Bundle)` is called), at the point where you have entirely drawn your UI and populated with all of the significant data. You can safely call this method any time after first launch as well, in which case it will simply be ignored. 

If this method is called before the activity's window is _first_ drawn and displayed as measured by the system, the reported time here will be shifted to the system measured time.

### requestDragAndDropPermissions

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun requestDragAndDropPermissions(event: [DragEvent](https://developer.android.com/reference/kotlin/android/view/DragEvent.html)!): [DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)!

Create `[DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)` object bound to this activity and controlling the access permissions for content URIs associated with the `[DragEvent](https://developer.android.com/reference/kotlin/android/view/DragEvent.html)`.

Parameters  
---  
`event` | [DragEvent](https://developer.android.com/reference/kotlin/android/view/DragEvent.html)!: Drag event  
Return  
---  
`[DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)!` | The `[DragAndDropPermissions](https://developer.android.com/reference/kotlin/android/view/DragAndDropPermissions.html)` object used to control access to the content URIs. Null if no content URIs are associated with the event or if permissions could not be granted.  
  
### requestFullscreenMode

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun requestFullscreenMode(  
        request: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        approvalCallback: [OutcomeReceiver](https://developer.android.com/reference/kotlin/android/os/OutcomeReceiver.html)<[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)!, [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!>?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Request to put the activity into fullscreen. The requester must be pinned or the top-most activity of the focused display which can be verified using `onTopResumedActivityChanged(boolean)`. The request should also be a response to a user input. When getting fullscreen and receiving corresponding `onConfigurationChanged(Configuration)` and `onMultiWindowModeChanged(boolean,Configuration)`, the activity should relayout itself and the system bars' visibilities can be controlled as usual fullscreen apps. Calling it again with the exit request can restore the activity to the previous status. This will only happen when it got into fullscreen through this API.

Parameters  
---  
`request` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Can be `FULLSCREEN_MODE_REQUEST_ENTER` or `FULLSCREEN_MODE_REQUEST_EXIT` to indicate this request is to get fullscreen or get restored.   
Value is one of the following: 

  * `FULLSCREEN_MODE_REQUEST_EXIT`
  * `FULLSCREEN_MODE_REQUEST_ENTER`

  
`approvalCallback` | [OutcomeReceiver](https://developer.android.com/reference/kotlin/android/os/OutcomeReceiver.html)<[Void](https://developer.android.com/reference/kotlin/java/lang/Void.html)!, [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html)!>?: Optional callback, use `null` when not necessary. When the request is approved or rejected, the callback will be triggered. This will happen before any configuration change. The callback will be dispatched on the main thread except on devices with API level 36.1 or lower, where the behavior is undefined. If the request is rejected, the Throwable provided will be an `[IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html)` with a detailed message can be retrieved by `[Throwable.getMessage()](https://developer.android.com/reference/kotlin/java/lang/Throwable.html#getMessage\(\))`.  
  
### requestOpenInBrowserEducation

Added in [API level 36](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun requestOpenInBrowserEducation(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Requests to show the “Open in browser” education. “Open in browser” is a feature within the app header that allows users to switch from an app to the web. The feature is made available when an application is opened by a user clicking a link or when a link is provided by an application. Links can be provided by calling `[AssistContent.setSessionTransferUri](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent#setSessionTransferUri\(android.net.Uri\))` or `[AssistContent.setWebUri](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent#setWebUri\(android.net.Uri\))`. 

This method should be utilized when an activity wants to nudge the user to switch to the web application in cases where the web may provide the user with a better experience. Note that this method does not guarantee that the education will be shown. 

The number of times that the "Open in browser" education can be triggered by this method is limited per application, and, when shown, the education appears above the app's content. For these reasons, developers should use this method sparingly when it is least disruptive to the user to show the education and when it is optimal to switch the user to a browser session. Before requesting to show the education, developers should assert that they have set a link that can be used by the "Open in browser" feature through either `[AssistContent.setSessionTransferUri](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent#setSessionTransferUri\(android.net.Uri\))` or `[AssistContent.setWebUri](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent#setWebUri\(android.net.Uri\))` so that users are navigated to a relevant page if they choose to switch to the browser. If a URI is not set using either method, "Open in browser" will utilize a generic link if available which will direct users to the homepage of the site associated with the app. The generic link is provided for a limited number of applications by the system and cannot be edited by developers. If none of these options contains a valid URI, the user will not be provided with the option to switch to the browser and the education will not be shown if requested.

**See Also**

  * `[android.app.assist.AssistContent#setSessionTransferUri](https://developer.android.com/reference/kotlin/android/app/assist/AssistContent#setSessionTransferUri\(android.net.Uri\))`



### requestPermissions

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun requestPermissions(  
        permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Requests permissions to be granted to this application. These permissions must be requested in your manifest, they should not be granted to your app, and they should have protection level `[dangerous](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_DANGEROUS:kotlin.Int)`, regardless whether they are declared by the platform or a third-party app. 

Normal permissions `[android.content.pm.PermissionInfo#PROTECTION_NORMAL](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_NORMAL:kotlin.Int)` are granted at install time if requested in the manifest. Signature permissions `[android.content.pm.PermissionInfo#PROTECTION_SIGNATURE](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_SIGNATURE:kotlin.Int)` are granted at install time if requested in the manifest and the signature of your app matches the signature of the app declaring the permissions. 

Call #shouldShowRequestPermissionRationale before calling this API to check if the system recommends to show a rationale UI before asking for a permission. 

If your app does not have the requested permissions the user will be presented with UI for accepting them. After the user has accepted or rejected the requested permissions you will receive a callback on #onRequestPermissionsResult reporting whether the permissions were granted or not. 

Note that requesting a permission does not guarantee it will be granted and your app should be able to run without having this permission. 

This method may start an activity allowing the user to choose which permissions to grant and which to reject. Hence, you should be prepared that your activity may be paused and resumed. Further, granting some permissions may require a restart of you application. In such a case, the system will recreate the activity stack before delivering the result to #onRequestPermissionsResult. 

When checking whether you have a permission you should use `[checkSelfPermission(String)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`. 

You cannot request a permission if your activity sets `[noHistory](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity_noHistory:kotlin.Int)` to `true` because in this case the activity would not receive result callbacks including #onRequestPermissionsResult. 

The [ permissions samples](https://github.com/android/platform-samples/tree/main/samples/privacy/permissions) repo demonstrates how to use this method to request permissions at run time. 

Parameters  
---  
`permissions` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>: The requested permissions. Must be non-null and not empty.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Application specific request code to match with a result reported to #onRequestPermissionsResult. Should be >= 0.  
Exceptions  
---  
`java.lang.IllegalArgumentException` | if requestCode is negative.  
  
**See Also**

  * `[#checkSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`



### requestPermissions

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun requestPermissions(  
        permissions: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Requests permissions to be granted to this application. These permissions must be requested in your manifest, they should not be granted to your app, and they should have protection level `[dangerous](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_DANGEROUS:kotlin.Int)`, regardless whether they are declared by the platform or a third-party app. 

Normal permissions `[android.content.pm.PermissionInfo#PROTECTION_NORMAL](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_NORMAL:kotlin.Int)` are granted at install time if requested in the manifest. Signature permissions `[android.content.pm.PermissionInfo#PROTECTION_SIGNATURE](https://developer.android.com/reference/kotlin/android/content/pm/PermissionInfo.html#PROTECTION_SIGNATURE:kotlin.Int)` are granted at install time if requested in the manifest and the signature of your app matches the signature of the app declaring the permissions. 

Call #shouldShowRequestPermissionRationale before calling this API to check if the system recommends to show a rationale UI before asking for a permission. 

If your app does not have the requested permissions the user will be presented with UI for accepting them. After the user has accepted or rejected the requested permissions you will receive a callback on #onRequestPermissionsResult reporting whether the permissions were granted or not. 

Note that requesting a permission does not guarantee it will be granted and your app should be able to run without having this permission. 

This method may start an activity allowing the user to choose which permissions to grant and which to reject. Hence, you should be prepared that your activity may be paused and resumed. Further, granting some permissions may require a restart of you application. In such a case, the system will recreate the activity stack before delivering the result to #onRequestPermissionsResult. 

When checking whether you have a permission you should use `[checkSelfPermission(String)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`. 

You cannot request a permission if your activity sets `[noHistory](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity_noHistory:kotlin.Int)` to `true` because in this case the activity would not receive result callbacks including #onRequestPermissionsResult. 

The [ permissions samples](https://github.com/android/platform-samples/tree/main/samples/privacy/permissions) repo demonstrates how to use this method to request permissions at run time. 

Parameters  
---  
`permissions` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!>: The requested permissions. Must be non-null and not empty.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Application specific request code to match with a result reported to #onRequestPermissionsResult. Should be >= 0.  
`deviceId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The app is requesting permissions for this device. The primary/physical device is assigned `[Context.DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)`, and virtual devices are assigned unique device Ids.  
Exceptions  
---  
`java.lang.IllegalArgumentException` | if requestCode is negative.  
  
**See Also**

  * `[#checkSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`
  * `[android.content.Context#DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)`



### requestShowKeyboardShortcuts

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun requestShowKeyboardShortcuts(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Request the Keyboard Shortcuts screen to show up. This will trigger `onProvideKeyboardShortcuts` to retrieve the shortcuts for the foreground activity.

### requestVisibleBehind

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~requestVisibleBehind~~(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_This method's functionality is no longer supported as of`[android.os.Build.VERSION_CODES#O](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O:kotlin.Int)` and will be removed in a future release._

Activities that want to remain visible behind a translucent activity above them must call this method anytime between the start of `onResume()` and the return from `onPause()`. If this call is successful then the activity will remain visible after `onPause()` is called, and is allowed to continue playing media in the background. 

The actions of this call are reset each time that this activity is brought to the front. That is, every time `onResume()` is called the activity will be assumed to not have requested visible behind. Therefore, if you want this activity to continue to be visible in the background you must call this method again. 

Only fullscreen opaque activities may make this call. I.e. this call is a nop for dialog and translucent activities. 

Under all circumstances, the activity must stop playing and release resources prior to or within a call to `onVisibleBehindCanceled()` or if this call returns false. 

False will be returned any time this method is called between the return of onPause and the next call to onResume.

Parameters  
---  
`visible` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): true to notify the system that the activity wishes to be visible behind other translucent activities, false to indicate otherwise. Resources must be released when passing false to this method.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | the resulting visibiity state. If true the activity will remain visible beyond `onPause()` if the next activity is translucent or not fullscreen. If false then the activity may not count on being visible behind other translucent activities, and must stop any media playback and release resources. Returning false may occur in lieu of a call to `onVisibleBehindCanceled()` so the return value must be checked.  
  
**See Also**

  * `#onVisibleBehindCanceled()`



### requestWindowFeature

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun requestWindowFeature(featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Enable extended window features. This is a convenience for calling `[getWindow().requestFeature()](https://developer.android.com/reference/kotlin/android/view/Window.html#requestFeature\(kotlin.Int\))`.

Parameters  
---  
`featureId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The desired feature as defined in `[android.view.Window](https://developer.android.com/reference/kotlin/android/view/Window.html)`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns true if the requested feature is supported and now enabled.  
  
**See Also**

  * `[android.view.Window#requestFeature](https://developer.android.com/reference/kotlin/android/view/Window.html#requestFeature\(kotlin.Int\))`



### requireViewById

Added in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun <T : [View](https://developer.android.com/reference/kotlin/android/view/View.html)!> requireViewById(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): T

Finds a view that was identified by the `android:id` XML attribute that was processed in #onCreate, or throws an IllegalArgumentException if the ID is invalid, or there is no matching view in the hierarchy. 

**Note:** In most cases -- depending on compiler support -- the resulting view is automatically cast to the target class type. If the target class type is unconstrained, an explicit cast may be necessary.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): the ID to search for  
Return  
---  
`T` | a view with given ID.   
This value cannot be `null`.  
  
**See Also**

  * `[android.view.View#requireViewById(int)](https://developer.android.com/reference/kotlin/android/view/View.html#requireViewById\(kotlin.Int\))`
  * `#findViewById(int)`



### runOnUiThread

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun runOnUiThread(action: [Runnable](https://developer.android.com/reference/kotlin/java/lang/Runnable.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Runs the specified action on the UI thread. If the current thread is the UI thread, then the action is executed immediately. If the current thread is not the UI thread, the action is posted to the event queue of the UI thread.

Parameters  
---  
`action` | [Runnable](https://developer.android.com/reference/kotlin/java/lang/Runnable.html)!: the action to run on the UI thread  
  
### setActionBar

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setActionBar(toolbar: [Toolbar](https://developer.android.com/reference/kotlin/android/widget/Toolbar.html)?): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set a `[Toolbar](https://developer.android.com/reference/kotlin/android/widget/Toolbar.html)` to act as the `[ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)` for this Activity window. 

When set to a non-null value the `getActionBar()` method will return an `[ActionBar](https://developer.android.com/reference/kotlin/android/app/ActionBar)` object that can be used to control the given toolbar as if it were a traditional window decor action bar. The toolbar's menu will be populated with the Activity's options menu and the navigation button will be wired through the standard `[home](https://developer.android.com/reference/kotlin/android/R.id.html#home:kotlin.Int)` menu select action.

In order to use a Toolbar within the Activity's window content the application must not request the window feature `[FEATURE_ACTION_BAR](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_ACTION_BAR:kotlin.Int)`.

Parameters  
---  
`toolbar` | [Toolbar](https://developer.android.com/reference/kotlin/android/widget/Toolbar.html)?: Toolbar to set as the Activity's action bar, or `null` to clear it  
  
### setAllowCrossUidActivitySwitchFromBelow

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setAllowCrossUidActivitySwitchFromBelow(allowed: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies whether the activities below this one in the task can also start other activities or finish the task. 

Starting from Target SDK Level `[android.os.Build.VERSION_CODES#VANILLA_ICE_CREAM](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#VANILLA_ICE_CREAM:kotlin.Int)`, apps may be blocked from starting new activities or finishing their task unless the top activity of such task belong to the same UID for security reasons. 

Setting this flag to `true` will allow the launching app to ignore the restriction if this activity is on top. Apps matching the UID of this activity are always exempt.

Parameters  
---  
`allowed` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to disable the UID restrictions; `false` to revert back to the default behaviour  
  
### setContentTransitionManager

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setContentTransitionManager(tm: [TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the `[TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)` to use for default transitions in this window. Requires `[Window.FEATURE_CONTENT_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_CONTENT_TRANSITIONS:kotlin.Int)`.

Parameters  
---  
`tm` | [TransitionManager](https://developer.android.com/reference/kotlin/android/transition/TransitionManager.html)!: The TransitionManager to use for scene changes.  
  
### setContentView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setContentView(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the activity content to an explicit view. This view is placed directly into the activity's view hierarchy. It can itself be a complex view hierarchy. When calling this method, the layout parameters of the specified view are ignored. Both the width and the height of the view are set by default to `[ViewGroup.LayoutParams.MATCH_PARENT](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html#MATCH_PARENT:kotlin.Int)`. To use your own layout parameters, invoke `setContentView(android.view.View,android.view.ViewGroup.LayoutParams)` instead.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The desired content to display.  
  
**See Also**

  * `#setContentView(int)`
  * `#setContentView(android.view.View,android.view.ViewGroup.LayoutParams)`



### setContentView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setContentView(  
        view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!,   
        params: [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the activity content to an explicit view. This view is placed directly into the activity's view hierarchy. It can itself be a complex view hierarchy.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The desired content to display.  
`params` | [ViewGroup.LayoutParams](https://developer.android.com/reference/kotlin/android/view/ViewGroup.LayoutParams.html)!: Layout parameters for the view.  
  
**See Also**

  * `#setContentView(android.view.View)`
  * `#setContentView(int)`



### setContentView

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setContentView(layoutResID: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the activity content from a layout resource. The resource will be inflated, adding all top-level views to the activity.

Parameters  
---  
`layoutResID` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Resource ID to be inflated.  
  
**See Also**

  * `#setContentView(android.view.View)`
  * `#setContentView(android.view.View,android.view.ViewGroup.LayoutParams)`



### setDefaultKeyMode

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setDefaultKeyMode(mode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Select the default key handling for this activity. This controls what will happen to key events that are not otherwise handled. The default mode (`DEFAULT_KEYS_DISABLE`) will simply drop them on the floor. Other modes allow you to launch the dialer (`DEFAULT_KEYS_DIALER`), execute a shortcut in your options menu without requiring the menu key be held down (`DEFAULT_KEYS_SHORTCUT`), or launch a search (`DEFAULT_KEYS_SEARCH_LOCAL` and `DEFAULT_KEYS_SEARCH_GLOBAL`). 

Note that the mode selected here does not impact the default handling of system keys, such as the "back" and "menu" keys, and your activity and its views always get a first chance to receive and handle all application keys.

Parameters  
---  
`mode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The desired default key mode constant.   
Value is one of the following: 

  * `DEFAULT_KEYS_DISABLE`
  * `DEFAULT_KEYS_DIALER`
  * `DEFAULT_KEYS_SHORTCUT`
  * `DEFAULT_KEYS_SEARCH_LOCAL`
  * `DEFAULT_KEYS_SEARCH_GLOBAL`

  
  
**See Also**

  * `#onKeyDown`



### setEnterSharedElementCallback

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setEnterSharedElementCallback(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

When `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.view.View,String)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.view.View,%20kotlin.String\))` was used to start an Activity, callback will be called to handle shared elements on the _launched_ Activity. This requires `[Window.FEATURE_ACTIVITY_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_ACTIVITY_TRANSITIONS:kotlin.Int)`.

Parameters  
---  
`callback` | [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!: Used to manipulate shared element transitions on the launched Activity.  
  
### setExitSharedElementCallback

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setExitSharedElementCallback(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

When `[android.app.ActivityOptions.makeSceneTransitionAnimation(Activity,android.view.View,String)](https://developer.android.com/reference/kotlin/android/app/ActivityOptions#makeSceneTransitionAnimation\(android.app.Activity,%20android.view.View,%20kotlin.String\))` was used to start an Activity, callback will be called to handle shared elements on the _launching_ Activity. Most calls will only come when returning from the started Activity. This requires `[Window.FEATURE_ACTIVITY_TRANSITIONS](https://developer.android.com/reference/kotlin/android/view/Window.html#FEATURE_ACTIVITY_TRANSITIONS:kotlin.Int)`.

Parameters  
---  
`callback` | [SharedElementCallback](https://developer.android.com/reference/kotlin/android/app/SharedElementCallback)!: Used to manipulate shared element transitions on the launching Activity.  
  
### setFeatureDrawable

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setFeatureDrawable(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        drawable: [Drawable](https://developer.android.com/reference/kotlin/android/graphics/drawable/Drawable.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Convenience for calling `[android.view.Window.setFeatureDrawable(int,Drawable)](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawable\(kotlin.Int,%20android.graphics.drawable.Drawable\))`.

### setFeatureDrawableAlpha

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setFeatureDrawableAlpha(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        alpha: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Convenience for calling `[android.view.Window#setFeatureDrawableAlpha](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableAlpha\(kotlin.Int,%20kotlin.Int\))`.

### setFeatureDrawableResource

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setFeatureDrawableResource(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        resId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Convenience for calling `[android.view.Window#setFeatureDrawableResource](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableResource\(kotlin.Int,%20kotlin.Int\))`.

### setFeatureDrawableUri

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setFeatureDrawableUri(  
        featureId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        uri: [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Convenience for calling `[android.view.Window#setFeatureDrawableUri](https://developer.android.com/reference/kotlin/android/view/Window.html#setFeatureDrawableUri\(kotlin.Int,%20android.net.Uri\))`.

### setFinishOnTouchOutside

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setFinishOnTouchOutside(finish: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets whether this activity is finished when touched outside its window's bounds.

### setHandoffEnabled

Added in [API level 37](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setHandoffEnabled(  
        handoffEnabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html),   
        handoffActivityParams: [HandoffActivityParams](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets if Handoff is enabled for this Activity. See `isHandoffEnabled` to get if Handoff is currently enabled on this Activity. If Handoff is enabled, this Activity will only be eligible to be handed off to other devices if it is the topmost Activity in its Task. Callers may specify optional parameters to specify when Handoff is appropriate for the current activity. See `[HandoffActivityParams](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams)` for more details.

Parameters  
---  
`handoffActivityParams` | [HandoffActivityParams](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams)?: Configuration parameters for Handoff.   
This value may be `null`.  
  
### setImmersive

Added in [API level 18](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setImmersive(i: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Adjust the current immersive mode setting. Note that changing this value will have no effect on the activity's `[android.content.pm.ActivityInfo](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html)` structure; that is, if `android:immersive` is set to `true` in the application's manifest entry for this activity, the `[ActivityInfo.flags](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#flags:kotlin.Int)` member will always have its `[FLAG_IMMERSIVE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#FLAG_IMMERSIVE:kotlin.Int)` bit set.

**See Also**

  * `#isImmersive()`
  * `[android.content.pm.ActivityInfo#FLAG_IMMERSIVE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#FLAG_IMMERSIVE:kotlin.Int)`



### setInheritShowWhenLocked

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setInheritShowWhenLocked(inheritShowWhenLocked: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies whether this `Activity` should be shown on top of the lock screen whenever the lockscreen is up and this activity has another activity behind it with the showWhenLock attribute set. That is, this activity is only visible on the lock screen if there is another activity with the showWhenLock attribute visible at the same time on the lock screen. A use case for this is permission dialogs, that should only be visible on the lock screen if their requesting activity is also visible. This value can be set as a manifest attribute using android.R.attr#inheritShowWhenLocked.

Parameters  
---  
`inheritShowWhenLocked` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to show the `Activity` on top of the lock screen when this activity has another activity behind it with the showWhenLock attribute set; `false` otherwise.  
  
**See Also**

  * `#setShowWhenLocked(boolean)`
  * `[android.R.attr#inheritShowWhenLocked](https://developer.android.com/reference/kotlin/android/R.attr.html#inheritShowWhenLocked:kotlin.Int)`



### setIntent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setIntent(newIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Changes the intent returned by `getIntent`. This holds a reference to the given intent; it does not copy it. Often used in conjunction with `onNewIntent(Intent)`.

Parameters  
---  
`newIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The new Intent object to return from `getIntent`  
  
**See Also**

  * `#getIntent`
  * `#onNewIntent(android.content.Intent)`



### setIntent

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setIntent(  
        newIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        newCaller: [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Changes the intent returned by `getIntent`, and ComponentCaller returned by `getCaller`. This holds references to the given intent, and ComponentCaller; it does not copy them. Often used in conjunction with `onNewIntent(Intent)`. To retrieve the caller from `onNewIntent(Intent)`, use `getCurrentCaller`, otherwise override `onNewIntent(Intent,ComponentCaller)`.

Parameters  
---  
`newIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: The new Intent object to return from `getIntent`   
This value may be `null`.  
`newCaller` | [ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)?: The new `[ComponentCaller](https://developer.android.com/reference/kotlin/android/app/ComponentCaller)` object to return from `getCaller`   
This value may be `null`.  
  
**See Also**

  * `#getIntent`
  * `#onNewIntent(android.content.Intent,android.app.ComponentCaller)`
  * `#getCaller`



### setLocusContext

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setLocusContext(  
        locusId: [LocusId](https://developer.android.com/reference/kotlin/android/content/LocusId.html)?,   
        bundle: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets the `[android.content.LocusId](https://developer.android.com/reference/kotlin/android/content/LocusId.html)` for this activity. The locus id helps identify different instances of the same `Activity` class. 

For example, a locus id based on a specific conversation could be set on a conversation app's chat `Activity`. The system can then use this locus id along with app's contents to provide ranking signals in various UI surfaces including sharing, notifications, shortcuts and so on. 

It is recommended to set the same locus id in the shortcut's locus id using `[setLocusId](https://developer.android.com/reference/kotlin/android/content/pm/ShortcutInfo.Builder.html#setLocusId\(android.content.LocusId\))` so that the system can learn appropriate ranking signals linking the activity's locus id with the matching shortcut.

Parameters  
---  
`locusId` | [LocusId](https://developer.android.com/reference/kotlin/android/content/LocusId.html)?: a unique, stable id that identifies this `Activity` instance. LocusId is an opaque ID that links this Activity's state to different Android concepts: `[setLocusId](https://developer.android.com/reference/kotlin/android/content/pm/ShortcutInfo.Builder.html#setLocusId\(android.content.LocusId\))`. LocusID is null by default or if you explicitly reset it.  
`bundle` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: extras set or updated as part of this locus context. This may help provide additional metadata such as URLs, conversation participants specific to this `Activity`'s context. Bundle can be null if additional metadata is not needed. Bundle should always be null for null locusId.  
  
**See Also**

  * `[android.view.contentcapture.ContentCaptureManager](https://developer.android.com/reference/kotlin/android/view/contentcapture/ContentCaptureManager.html)`
  * `[android.view.contentcapture.ContentCaptureContext](https://developer.android.com/reference/kotlin/android/view/contentcapture/ContentCaptureContext.html)`



### setMediaController

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setMediaController(controller: [MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets a `[MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)` to send media keys and volume changes to. 

The controller will be tied to the window of this Activity. Media key and volume events which are received while the Activity is in the foreground will be forwarded to the controller and used to invoke transport controls or adjust the volume. This may be used instead of or in addition to `setVolumeControlStream` to affect a specific session instead of a specific stream. 

It is not guaranteed that the hardware volume controls will always change this session's volume (for example, if a call is in progress, its stream's volume may be changed instead). To reset back to the default use null as the controller.

Parameters  
---  
`controller` | [MediaController](https://developer.android.com/reference/kotlin/android/media/session/MediaController.html)!: The controller for the session which should receive media keys and volume changes.  
  
### setPictureInPictureParams

Added in [API level 26](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setPictureInPictureParams(params: [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Updates the properties of the picture-in-picture activity, or sets it to be used later when `enterPictureInPictureMode()` is called.

Parameters  
---  
`params` | [PictureInPictureParams](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams): the new parameters for the picture-in-picture.   
This value cannot be `null`.  
  
### setProgress

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~setProgress~~(progress: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_No longer supported starting in API 21._

Sets the progress for the progress bars in the title. 

In order for the progress bar to be shown, the feature must be requested via `requestWindowFeature(int)`.

Parameters  
---  
`progress` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The progress for the progress bar. Valid ranges are from 0 to 10000 (both inclusive). If 10000 is given, the progress bar will be completely filled and will fade out.  
  
### setProgressBarIndeterminate

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~setProgressBarIndeterminate~~(indeterminate: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_No longer supported starting in API 21._

Sets whether the horizontal progress bar in the title should be indeterminate (the circular is always indeterminate). 

In order for the progress bar to be shown, the feature must be requested via `requestWindowFeature(int)`.

Parameters  
---  
`indeterminate` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): Whether the horizontal progress bar should be indeterminate.  
  
### setProgressBarIndeterminateVisibility

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~setProgressBarIndeterminateVisibility~~(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_No longer supported starting in API 21._

Sets the visibility of the indeterminate progress bar in the title. 

In order for the progress bar to be shown, the feature must be requested via `requestWindowFeature(int)`.

Parameters  
---  
`visible` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): Whether to show the progress bars in the title.  
  
### setProgressBarVisibility

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~setProgressBarVisibility~~(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_No longer supported starting in API 21._

Sets the visibility of the progress bar in the title. 

In order for the progress bar to be shown, the feature must be requested via `requestWindowFeature(int)`.

Parameters  
---  
`visible` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): Whether to show the progress bars in the title.  
  
### setRecentsScreenshotEnabled

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setRecentsScreenshotEnabled(enabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

If set to false, this indicates to the system that it should never take a screenshot of the activity to be used as a representation in recents screen. By default, this value is `true`. 

Note that the system may use the window background of the theme instead to represent the window when it is not running. 

Also note that in comparison to `[android.view.WindowManager.LayoutParams#FLAG_SECURE](https://developer.android.com/reference/kotlin/android/view/WindowManager.LayoutParams.html#FLAG_SECURE:kotlin.Int)`, this only affects the behavior when the activity's screenshot would be used as a representation when the activity is not in a started state, i.e. in Overview. The system may still take screenshots of the activity in other contexts; for example, when the user takes a screenshot of the entire screen, or when the active `[android.service.voice.VoiceInteractionService](https://developer.android.com/reference/kotlin/android/service/voice/VoiceInteractionService.html)` requests a screenshot via `[android.service.voice.VoiceInteractionSession#SHOW_WITH_SCREENSHOT](https://developer.android.com/reference/kotlin/android/service/voice/VoiceInteractionSession.html#SHOW_WITH_SCREENSHOT:kotlin.Int)`.

Parameters  
---  
`enabled` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to enable recents screenshots; `false` otherwise.  
  
### setRequestedOrientation

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setRequestedOrientation(requestedOrientation: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Change the desired orientation of this activity. If the activity is currently in the foreground or otherwise impacting the screen orientation, the screen is immediately changed (possibly causing the activity to be restarted). Otherwise, the new orientation is used the next time the activity is visible. **Note:**

  * To improve the layout of apps on form factors with smallest width >= 600dp, the system ignores calls to this method for apps that target Android 16 (API level 36) or higher.
  * Device manufacturers can configure devices to ignore calls to this method to improve the layout of orientation-restricted apps.
  * On devices with Android 16 (API level 36) or higher installed, virtual device owners (select trusted and privileged apps) can optimize app layout on displays they manage by ignoring calls to this method. See also [ Companion app streaming](https://source.android.com/docs/core/permissions/app-streaming).



See [Device compatibility mode](https://developer.android.com/guide/practices/device-compatibility-mode).

Parameters  
---  
`requestedOrientation` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): An orientation constant as used in `[ActivityInfo.screenOrientation](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#screenOrientation:kotlin.Int)`.   
Value is one of the following: 

  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_UNSPECIFIED](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_UNSPECIFIED:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_BEHIND](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_BEHIND:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_NOSENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_NOSENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_SENSOR_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_SENSOR_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_REVERSE_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_REVERSE_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_REVERSE_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_REVERSE_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_FULL_SENSOR](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_FULL_SENSOR:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER_LANDSCAPE](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER_LANDSCAPE:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_USER_PORTRAIT](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_USER_PORTRAIT:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_FULL_USER](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_FULL_USER:kotlin.Int)`
  * `[android.content.pm.ActivityInfo#SCREEN_ORIENTATION_LOCKED](https://developer.android.com/reference/kotlin/android/content/pm/ActivityInfo.html#SCREEN_ORIENTATION_LOCKED:kotlin.Int)`

  
  
### setResult

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setResult(resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Call this to set the result that your activity will return to its caller.

Parameters  
---  
`resultCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The result code to propagate back to the originating activity, often RESULT_CANCELED or RESULT_OK  
  
**See Also**

  * `#RESULT_CANCELED`
  * `#RESULT_OK`
  * `#RESULT_FIRST_USER`
  * `#setResult(int,android.content.Intent)`



### setResult

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setResult(  
        resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Call this to set the result that your activity will return to its caller. 

As of `[android.os.Build.VERSION_CODES#GINGERBREAD](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#GINGERBREAD:kotlin.Int)`, the Intent you supply here can have `[Intent.FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_READ_URI_PERMISSION:kotlin.Int)` and/or `[Intent.FLAG_GRANT_WRITE_URI_PERMISSION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_GRANT_WRITE_URI_PERMISSION:kotlin.Int)` set. This will grant the Activity receiving the result access to the specific URIs in the Intent. Access will remain until the Activity has finished (it will remain across the hosting process being killed and other temporary destruction) and will be added to any existing set of URI permissions it already holds.

Parameters  
---  
`resultCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The result code to propagate back to the originating activity, often RESULT_CANCELED or RESULT_OK  
`data` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The data to propagate back to the originating activity.  
  
**See Also**

  * `#RESULT_CANCELED`
  * `#RESULT_OK`
  * `#RESULT_FIRST_USER`
  * `#setResult(int)`



### setSecondaryProgress

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~setSecondaryProgress~~(secondaryProgress: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_No longer supported starting in API 21._

Sets the secondary progress for the progress bar in the title. This progress is drawn between the primary progress (set via `setProgress(int)` and the background. It can be ideal for media scenarios such as showing the buffering progress while the default progress shows the play progress. 

In order for the progress bar to be shown, the feature must be requested via `requestWindowFeature(int)`.

Parameters  
---  
`secondaryProgress` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The secondary progress for the progress bar. Valid ranges are from 0 to 10000 (both inclusive).  
  
### setShouldDockBigOverlays

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setShouldDockBigOverlays(shouldDockBigOverlays: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies a preference to dock big overlays like the expanded picture-in-picture on TV (see `[PictureInPictureParams.Builder.setExpandedAspectRatio](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams.Builder#setExpandedAspectRatio\(android.util.Rational\))`). Docking puts the big overlay side-by-side next to this activity, so that both windows are fully visible to the user. 

If unspecified, whether the overlay window will be docked or not, will be defined by the system. 

If specified, the system will try to respect the preference, but it may be overridden by a user preference.

Parameters  
---  
`shouldDockBigOverlays` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): indicates that big overlays should be docked next to the activity instead of overlay its content  
  
**See Also**

  * `[android.app.PictureInPictureParams.Builder#setExpandedAspectRatio](https://developer.android.com/reference/kotlin/android/app/PictureInPictureParams.Builder#setExpandedAspectRatio\(android.util.Rational\))`
  * `#shouldDockBigOverlays`



### setShowWhenLocked

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setShowWhenLocked(showWhenLocked: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies whether an `Activity` should be shown on top of the lock screen whenever the lockscreen is up and the activity is resumed. Normally an activity will be transitioned to the stopped state if it is started while the lockscreen is up, but with this flag set the activity will remain in the resumed state visible on-top of the lock screen. This value can be set as a manifest attribute using `[android.R.attr#showWhenLocked](https://developer.android.com/reference/kotlin/android/R.attr.html#showWhenLocked:kotlin.Int)`.

Parameters  
---  
`showWhenLocked` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to show the `Activity` on top of the lock screen; `false` otherwise.  
  
**See Also**

  * `#setTurnScreenOn(boolean)`
  * `[android.R.attr#turnScreenOn](https://developer.android.com/reference/kotlin/android/R.attr.html#turnScreenOn:kotlin.Int)`
  * `[android.R.attr#showWhenLocked](https://developer.android.com/reference/kotlin/android/R.attr.html#showWhenLocked:kotlin.Int)`



### setTaskDescription

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTaskDescription(taskDescription: [ActivityManager.TaskDescription](https://developer.android.com/reference/kotlin/android/app/ActivityManager.TaskDescription)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Sets information describing the task with this activity for presentation inside the Recents System UI. When `[ActivityManager.getRecentTasks](https://developer.android.com/reference/kotlin/android/app/ActivityManager#getRecentTasks\(kotlin.Int,%20kotlin.Int\))` is called, the activities of each task are traversed in order from the topmost activity to the bottommost. The traversal continues for each property until a suitable value is found. For each task the taskDescription will be returned in `[android.app.ActivityManager.TaskDescription](https://developer.android.com/reference/kotlin/android/app/ActivityManager.TaskDescription)`.

Parameters  
---  
`taskDescription` | [ActivityManager.TaskDescription](https://developer.android.com/reference/kotlin/android/app/ActivityManager.TaskDescription)!: The TaskDescription properties that describe the task with this activity  
  
**See Also**

  * `[android.app.ActivityManager#getRecentTasks](https://developer.android.com/reference/kotlin/android/app/ActivityManager#getRecentTasks\(kotlin.Int,%20kotlin.Int\))`
  * `[android.app.ActivityManager.TaskDescription](https://developer.android.com/reference/kotlin/android/app/ActivityManager.TaskDescription)`



### setTheme

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTheme(resid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the base theme for this context. Note that this should be called before any views are instantiated in the Context (for example before calling android.app.Activity#setContentView or android.view.LayoutInflater#inflate).

Parameters  
---  
`resid` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The style resource describing the theme.  
  
### setTitle

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTitle(titleId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Change the title associated with this activity. If this is a top-level activity, the title for its window will change. If it is an embedded activity, the parent can do whatever it wants with it.

### setTitle

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTitle(title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Change the title associated with this activity. If this is a top-level activity, the title for its window will change. If it is an embedded activity, the parent can do whatever it wants with it.

### setTitleColor

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~setTitleColor~~(textColor: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use action bar styles instead._

Change the color of the title associated with this activity. 

This method is deprecated starting in API Level 11 and replaced by action bar styles. For information on styling the Action Bar, read the [Action Bar](https://developer.android.com/%20guide/topics/ui/actionbar.html) developer guide.

### setTranslucent

Added in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTranslucent(translucent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Convert an activity, which particularly with `[android.R.attr#windowIsTranslucent](https://developer.android.com/reference/kotlin/android/R.attr.html#windowIsTranslucent:kotlin.Int)` or `[android.R.attr#windowIsFloating](https://developer.android.com/reference/kotlin/android/R.attr.html#windowIsFloating:kotlin.Int)` attribute, to a fullscreen opaque activity, or convert it from opaque back to translucent.

Parameters  
---  
`translucent` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` convert from opaque to translucent. `false` convert from translucent to opaque.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | The result of setting translucency. Return `true` if set successfully, `false` otherwise.  
  
### setTurnScreenOn

Added in [API level 27](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setTurnScreenOn(turnScreenOn: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Specifies whether the screen should be turned on when the `Activity` is resumed. Normally an activity will be transitioned to the stopped state if it is started while the screen if off, but with this flag set the activity will cause the screen to turn on if the activity will be visible and resumed due to the screen coming on. The screen will not be turned on if the activity won't be visible after the screen is turned on. This flag is normally used in conjunction with the `[android.R.attr#showWhenLocked](https://developer.android.com/reference/kotlin/android/R.attr.html#showWhenLocked:kotlin.Int)` flag to make sure the activity is visible after the screen is turned on when the lockscreen is up. In addition, if this flag is set and the activity calls `[KeyguardManager.requestDismissKeyguard(Activity,KeyguardManager.KeyguardDismissCallback)](https://developer.android.com/reference/kotlin/android/app/KeyguardManager#requestDismissKeyguard\(android.app.Activity,%20android.app.KeyguardManager.KeyguardDismissCallback\))` the screen will turn on.

Parameters  
---  
`turnScreenOn` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to turn on the screen; `false` otherwise.  
  
**See Also**

  * `#setShowWhenLocked(boolean)`
  * `[android.R.attr#turnScreenOn](https://developer.android.com/reference/kotlin/android/R.attr.html#turnScreenOn:kotlin.Int)`
  * `[android.R.attr#showWhenLocked](https://developer.android.com/reference/kotlin/android/R.attr.html#showWhenLocked:kotlin.Int)`
  * `[android.app.KeyguardManager#isDeviceSecure()](https://developer.android.com/reference/kotlin/android/app/KeyguardManager#isDeviceSecure\(\))`



### setVisible

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setVisible(visible: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Control whether this activity's main window is visible. This is intended only for the special case of an activity that is not going to show a UI itself, but can't just finish prior to onResume() because it needs to wait for a service binding or such. Setting this to false allows you to prevent your UI from being shown during that time. 

The default value for this is taken from the `[android.R.attr#windowNoDisplay](https://developer.android.com/reference/kotlin/android/R.attr.html#windowNoDisplay:kotlin.Int)` attribute of the activity's theme.

### setVolumeControlStream

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun setVolumeControlStream(streamType: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Suggests an audio stream whose volume should be changed by the hardware volume controls. 

The suggested audio stream will be tied to the window of this Activity. Volume requests which are received while the Activity is in the foreground will affect this stream. 

It is not guaranteed that the hardware volume controls will always change this stream's volume (for example, if a call is in progress, its stream's volume may be changed instead). To reset back to the default, use `[AudioManager.USE_DEFAULT_STREAM_TYPE](https://developer.android.com/reference/kotlin/android/media/AudioManager.html#USE_DEFAULT_STREAM_TYPE:kotlin.Int)`.

Parameters  
---  
`streamType` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The type of the audio stream whose volume should be changed by the hardware volume controls.  
  
### setVrModeEnabled

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun setVrModeEnabled(  
        enabled: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html),   
        requestedComponent: [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Enable or disable virtual reality (VR) mode for this Activity. 

VR mode is a hint to Android system to switch to a mode optimized for VR applications while this Activity has user focus.

It is recommended that applications additionally declare `[android.R.attr#enableVrMode](https://developer.android.com/reference/kotlin/android/R.attr.html#enableVrMode:kotlin.Int)` in their manifest to allow for smooth activity transitions when switching between VR activities.

If the requested `[android.service.vr.VrListenerService](https://developer.android.com/reference/kotlin/android/service/vr/VrListenerService.html)` component is not available, VR mode will not be started. Developers can handle this case as follows:
    
    
    String servicePackage = "com.whatever.app";
      String serviceClass = "com.whatever.app.MyVrListenerService";
     
      // Name of the component of the VrListenerService to start.
      ComponentName serviceComponent = new ComponentName(servicePackage, serviceClass);
     
      try {
         setVrModeEnabled(true, myComponentName);
      } catch (PackageManager.NameNotFoundException e) {
             List<ApplicationInfo> installed = getPackageManager().getInstalledApplications(0);
             boolean isInstalled = false;
             for (ApplicationInfo app : installed) {
                 if (app.packageName.equals(servicePackage)) {
                     isInstalled = true;
                     break;
                 }
             }
             if (isInstalled) {
                 // Package is installed, but not enabled in Settings.  Let user enable it.
                 startActivity(new Intent(Settings.ACTION_VR_LISTENER_SETTINGS));
             } else {
                 // Package is not installed.  Send an intent to download this.
                 sentIntentToLaunchAppStore(servicePackage);
             }
      }
      

Parameters  
---  
`enabled` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` to enable this mode.  
`requestedComponent` | [ComponentName](https://developer.android.com/reference/kotlin/android/content/ComponentName.html): the name of the component to use as a `[android.service.vr.VrListenerService](https://developer.android.com/reference/kotlin/android/service/vr/VrListenerService.html)` while VR mode is enabled.   
This value cannot be `null`.  
Exceptions  
---  
`android.content.pm.PackageManager.NameNotFoundException` | if the given component to run as a `[android.service.vr.VrListenerService](https://developer.android.com/reference/kotlin/android/service/vr/VrListenerService.html)` is not installed, or has not been enabled in user settings.  
  
**See Also**

  * `[android.content.pm.PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE](https://developer.android.com/reference/kotlin/android/content/pm/PackageManager.html#FEATURE_VR_MODE_HIGH_PERFORMANCE:kotlin.String)`
  * `[android.service.vr.VrListenerService](https://developer.android.com/reference/kotlin/android/service/vr/VrListenerService.html)`
  * `[android.provider.Settings#ACTION_VR_LISTENER_SETTINGS](https://developer.android.com/reference/kotlin/android/provider/Settings.html#ACTION_VR_LISTENER_SETTINGS:kotlin.String)`
  * `[android.R.attr#enableVrMode](https://developer.android.com/reference/kotlin/android/R.attr.html#enableVrMode:kotlin.Int)`



### shouldDockBigOverlays

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun shouldDockBigOverlays(): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns whether big overlays should be docked next to the activity as set by `setShouldDockBigOverlays`.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | `true` if big overlays should be docked next to the activity instead of overlay its content  
  
**See Also**

  * `#setShouldDockBigOverlays`



### shouldShowRequestPermissionRationale

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun shouldShowRequestPermissionRationale(permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Gets whether you should show UI with rationale before requesting a permission.

Parameters  
---  
`permission` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): A permission your app wants to request.   
This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Whether you should show permission rationale UI.  
  
**See Also**

  * `[#checkSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`



### shouldShowRequestPermissionRationale

Added in [API level 35](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun shouldShowRequestPermissionRationale(  
        permission: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html),   
        deviceId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Gets whether you should show UI with rationale before requesting a permission.

Parameters  
---  
`permission` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html): A permission your app wants to request.   
This value cannot be `null`.  
`deviceId` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The app is requesting permissions for this device. The primary/physical device is assigned `[Context.DEVICE_ID_DEFAULT](https://developer.android.com/reference/kotlin/android/content/Context.html#DEVICE_ID_DEFAULT:kotlin.Int)`, and virtual devices are assigned unique device Ids.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Whether you should show permission rationale UI.  
  
**See Also**

  * `[#checkSelfPermission](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#checkSelfPermission\(kotlin.String\))`



### shouldUpRecreateTask

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun shouldUpRecreateTask(targetIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns true if the app should recreate the task when navigating 'up' from this activity by using targetIntent. 

If this method returns false the app can trivially call `navigateUpTo(Intent)` using the same parameters to correctly perform up navigation. If this method returns false, the app should synthesize a new task stack by using `[TaskStackBuilder](https://developer.android.com/reference/kotlin/android/app/TaskStackBuilder)` or another similar mechanism to perform up navigation.

Parameters  
---  
`targetIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: An intent representing the target destination for up navigation  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | true if navigating up should recreate a new task stack, false if the same task should be used for the destination  
  
### showAssist

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun showAssist(args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Ask to have the current assistant shown to the user. This only works if the calling activity is the current foreground activity. It is the same as calling `[VoiceInteractionService.showSession](https://developer.android.com/reference/kotlin/android/service/voice/VoiceInteractionService.html#showSession\(android.os.Bundle,%20kotlin.Int\))` and requesting all of the possible context. The receiver will always see `[android.service.voice.VoiceInteractionSession#SHOW_SOURCE_APPLICATION](https://developer.android.com/reference/kotlin/android/service/voice/VoiceInteractionSession.html#SHOW_SOURCE_APPLICATION:kotlin.Int)` set.

Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns true if the assistant was successfully invoked, else false. For example false will be returned if the caller is not the current top activity.  
  
### showDialog

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~showDialog~~(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Simple version of `showDialog(int,Bundle)` that does not take any arguments. Simply calls `showDialog(int,Bundle)` with null arguments.

### showDialog

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    fun ~~showDialog~~(  
        id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Show a dialog managed by this activity. A call to `onCreateDialog(int,Bundle)` will be made with the same id the first time this is called for a given id. From thereafter, the dialog will be automatically saved and restored. _If you are targeting`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, consider instead using a `[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` instead._

Each time a dialog is shown, `onPrepareDialog(int,Dialog,Bundle)` will be made to provide an opportunity to do any timely preparation.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id of the managed dialog.  
`args` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!: Arguments to pass through to the dialog. These will be saved and restored for you. Note that if the dialog is already created, `onCreateDialog(int,Bundle)` will not be called with the new arguments but `onPrepareDialog(int,Dialog,Bundle)` will be. If you need to rebuild the dialog, call `removeDialog(int)` first.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns true if the Dialog was created; false is returned if it is not created because `onCreateDialog(int,Bundle)` returns false.  
  
**See Also**

  * `[android.app.Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)`
  * `#onCreateDialog(int,android.os.Bundle)`
  * `#onPrepareDialog(int,android.app.Dialog,android.os.Bundle)`
  * `#dismissDialog(int)`
  * `#removeDialog(int)`



### showLockTaskEscapeMessage

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun showLockTaskEscapeMessage(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Shows the user the system defined message for telling the user how to exit lock task mode. The task containing this activity must be in lock task mode at the time of this call for the message to be displayed.

### startActionMode

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActionMode(callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!): [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?

Start an action mode of the default type `[ActionMode.TYPE_PRIMARY](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_PRIMARY:kotlin.Int)`.

Parameters  
---  
`callback` | [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!: Callback that will manage lifecycle events for this action mode  
Return  
---  
`[ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?` | The ActionMode that was started, or null if it was canceled  
  
**See Also**

  * `[android.view.ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)`



### startActionMode

Added in [API level 23](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActionMode(  
        callback: [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!,   
        type: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?

Start an action mode of the given type.

Parameters  
---  
`callback` | [ActionMode.Callback](https://developer.android.com/reference/kotlin/android/view/ActionMode.Callback.html)!: Callback that will manage lifecycle events for this action mode  
`type` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): One of `[ActionMode.TYPE_PRIMARY](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_PRIMARY:kotlin.Int)` or `[ActionMode.TYPE_FLOATING](https://developer.android.com/reference/kotlin/android/view/ActionMode.html#TYPE_FLOATING:kotlin.Int)`.  
Return  
---  
`[ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)?` | The ActionMode that was started, or null if it was canceled  
  
**See Also**

  * `[android.view.ActionMode](https://developer.android.com/reference/kotlin/android/view/ActionMode.html)`



### startActivities

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivities(intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as #startActivities(android.content.Intent[],android.os.Bundle) with no options specified.

Parameters  
---  
`intents` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!: The intents to start.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivities

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivities(  
        intents: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!,   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Launch a new activity. You will not receive any information about when the activity exits. This implementation overrides the base version, providing information about the activity performing the launch. Because of this additional information, the `[Intent.FLAG_ACTIVITY_NEW_TASK](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_NEW_TASK:kotlin.Int)` launch flag is not required; if not specified, the new activity will be added to the task of the caller. 

This method throws `[android.content.ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.

Parameters  
---  
`intents` | [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)<[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!>!: The intents to start.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as #startActivity(android.content.Intent,android.os.Bundle) with no options specified.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivity

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivity(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Launch a new activity. You will not receive any information about when the activity exits. This implementation overrides the base version, providing information about the activity performing the launch. Because of this additional information, the `[Intent.FLAG_ACTIVITY_NEW_TASK](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_NEW_TASK:kotlin.Int)` launch flag is not required; if not specified, the new activity will be added to the task of the caller. 

This method throws `[android.content.ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityForResult

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivityForResult(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as calling `startActivityForResult(Intent,int,Bundle)` with no options.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityForResult

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivityForResult(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Launch an activity for which you would like a result when it finished. When this activity exits, your onActivityResult() method will be called with the given requestCode. Using a negative requestCode is the same as calling #startActivity (the activity is not launched as a sub-activity). 

Note that this method should only be used with Intent protocols that are defined to return a result. In other protocols (such as `[Intent.ACTION_MAIN](https://developer.android.com/reference/kotlin/android/content/Intent.html#ACTION_MAIN:kotlin.String)` or `[Intent.ACTION_VIEW](https://developer.android.com/reference/kotlin/android/content/Intent.html#ACTION_VIEW:kotlin.String)`), you may not get the result when you expect. For example, if the activity you are launching uses `[Intent.FLAG_ACTIVITY_NEW_TASK](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_NEW_TASK:kotlin.Int)`, it will not run in your task and thus you will immediately receive a cancel result. 

As a special case, if you call startActivityForResult() with a requestCode >= 0 during the initial onCreate(Bundle savedInstanceState)/onResume() of your activity, then your window will not be displayed until a result is returned back from the started activity. This is to avoid visible flickering when redirecting to another activity. 

This method throws `[android.content.ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityFromChild

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startActivityFromChild~~(  
        child: Activity,   
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`androidx.fragment.app.FragmentActivity#startActivityFromFragment( androidx.fragment.app.Fragment,Intent,int)`_

Same as calling `startActivityFromChild(Activity,Intent,int,Bundle)` with no options.

Parameters  
---  
`child` | Activity: The activity making the call.   
This value cannot be `null`.  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Reply request code. < 0 if reply is not requested.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityFromChild

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startActivityFromChild~~(  
        child: Activity,   
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`androidx.fragment.app.FragmentActivity#startActivityFromFragment( androidx.fragment.app.Fragment,Intent,int,Bundle)`_

This is called when a child activity of this one calls its #startActivity or #startActivityForResult method. 

This method throws `[android.content.ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.

Parameters  
---  
`child` | Activity: The activity making the call.   
This value cannot be `null`.  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Reply request code. < 0 if reply is not requested.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityFromFragment

Added in [API level 11](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startActivityFromFragment~~(  
        fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment),   
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`androidx.fragment.app.FragmentActivity#startActivityFromFragment( androidx.fragment.app.Fragment,Intent,int)`_

Same as calling `startActivityFromFragment(Fragment,Intent,int,Bundle)` with no options.

Parameters  
---  
`fragment` | [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment): The fragment making the call.   
This value cannot be `null`.  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Reply request code. < 0 if reply is not requested.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityFromFragment

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 28](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startActivityFromFragment~~(  
        fragment: [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment),   
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`androidx.fragment.app.FragmentActivity#startActivityFromFragment( androidx.fragment.app.Fragment,Intent,int,Bundle)`_

This is called when a Fragment in this activity calls its android.app.Fragment#startActivity or android.app.Fragment#startActivityForResult method. 

This method throws `[android.content.ActivityNotFoundException](https://developer.android.com/reference/kotlin/android/content/ActivityNotFoundException.html)` if there was no Activity found to run the given Intent.

Parameters  
---  
`fragment` | [Fragment](https://developer.android.com/reference/kotlin/android/app/Fragment): The fragment making the call.   
This value cannot be `null`.  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The intent to start.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Reply request code. < 0 if reply is not requested.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Exceptions  
---  
`android.content.ActivityNotFoundException` |   
  
**See Also**




### startActivityIfNeeded

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivityIfNeeded(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html),   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Same as calling `startActivityIfNeeded(Intent,int,Bundle)` with no options.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): The intent to start.   
This value cannot be `null`.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits, as described in #startActivityForResult.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If a new activity was launched then true is returned; otherwise false is returned and you must handle the Intent yourself.  
  
**See Also**




### startActivityIfNeeded

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startActivityIfNeeded(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html),   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

A special variation to launch an activity only if a new activity instance is needed to handle the given Intent. In other words, this is just like `startActivityForResult(Intent,int)` except: if you are using the `[Intent.FLAG_ACTIVITY_SINGLE_TOP](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_SINGLE_TOP:kotlin.Int)` flag, or singleTask or singleTop `[launchMode](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity_launchMode:kotlin.Int)`, and the activity that handles intent is the same as your currently running activity, then a new instance is not needed. In this case, instead of the normal behavior of calling #onNewIntent this function will return and you can handle the Intent yourself. 

This function can only be called from a top-level activity; if it is called from a child activity, a runtime exception will be thrown.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): The intent to start.   
This value cannot be `null`.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits, as described in #startActivityForResult.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | If a new activity was launched then true is returned; otherwise false is returned and you must handle the Intent yourself.  
  
**See Also**




### startIntentSender

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startIntentSender(  
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as calling #startIntentSender(android.content.IntentSender,android.content.Intent,int,int,int,android.os.Bundle) with no options.

Parameters  
---  
`intent` | [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!: The IntentSender to launch.  
`fillInIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: If non-null, this will be provided as the intent parameter to android.content.IntentSender#sendIntent.  
`flagsMask` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Intent flags in the original IntentSender that you would like to change.  
`flagsValues` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Desired values for any bits set in flagsMask  
`extraFlags` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Always set to 0.  
  
### startIntentSender

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startIntentSender(  
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Like #startActivity(android.content.Intent,android.os.Bundle), but taking a IntentSender to start; see `startIntentSenderForResult(IntentSender,int,Intent,int,int,int,Bundle)` for more information.

Parameters  
---  
`intent` | [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!: The IntentSender to launch.  
`fillInIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: If non-null, this will be provided as the intent parameter to android.content.IntentSender#sendIntent.  
`flagsMask` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Intent flags in the original IntentSender that you would like to change.  
`flagsValues` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Desired values for any bits set in flagsMask  
`extraFlags` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Always set to 0.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details. If options have also been supplied by the IntentSender, options given here will override any that conflict with those given by the IntentSender.   
This value may be `null`.  
  
### startIntentSenderForResult

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startIntentSenderForResult(  
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Same as calling `startIntentSenderForResult(IntentSender,int,Intent,int,int,int,Bundle)` with no options.

Parameters  
---  
`intent` | [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!: The IntentSender to launch.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits.  
`fillInIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: If non-null, this will be provided as the intent parameter to android.content.IntentSender#sendIntent.  
`flagsMask` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Intent flags in the original IntentSender that you would like to change.  
`flagsValues` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Desired values for any bits set in flagsMask  
`extraFlags` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Always set to 0.  
  
### startIntentSenderForResult

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startIntentSenderForResult(  
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Like `startActivityForResult(Intent,int)`, but allowing you to use a IntentSender to describe the activity to be started. If the IntentSender is for an activity, that activity will be started as if you had called the regular `startActivityForResult(Intent,int)` here; otherwise, its associated action will be executed (such as sending a broadcast) as if you had called android.content.IntentSender#sendIntent on it.

Parameters  
---  
`intent` | [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!: The IntentSender to launch.  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): If >= 0, this code will be returned in onActivityResult() when the activity exits; If < 0, no result will return when the activity exits.  
`fillInIntent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)?: If non-null, this will be provided as the intent parameter to android.content.IntentSender#sendIntent.  
`flagsMask` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Intent flags in the original IntentSender that you would like to change.  
`flagsValues` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Desired values for any bits set in flagsMask  
`extraFlags` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): Always set to 0.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details. If options have also been supplied by the IntentSender, options given here will override any that conflict with those given by the IntentSender.   
This value may be `null`.  
  
### startIntentSenderFromChild

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startIntentSenderFromChild~~(  
        child: Activity!,   
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`startIntentSenderForResult(IntentSender,int,Intent,int,int,int)` instead._

Same as calling `startIntentSenderFromChild(Activity,IntentSender,int,Intent,int,int,int,Bundle)` with no options.

### startIntentSenderFromChild

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 30](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startIntentSenderFromChild~~(  
        child: Activity!,   
        intent: [IntentSender](https://developer.android.com/reference/kotlin/android/content/IntentSender.html)!,   
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        fillInIntent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!,   
        flagsMask: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        flagsValues: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        extraFlags: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use`startIntentSenderForResult(IntentSender,int,Intent,int,int,int,Bundle)` instead._

Like `startActivityFromChild(Activity,Intent,int)`, but taking a IntentSender; see `startIntentSenderForResult(IntentSender,int,Intent,int,int,int)` for more information.

Parameters  
---  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: This value may be `null`.  
  
### startLocalVoiceInteraction

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startLocalVoiceInteraction(privateOptions: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Starts a local voice interaction session. When ready, `onLocalVoiceInteractionStarted()` is called. You can pass a bundle of private options to the registered voice interaction service.

Parameters  
---  
`privateOptions` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!: a Bundle of private arguments to the current voice interaction service  
  
### startLockTask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startLockTask(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Request to put this activity in a mode where the user is locked to a restricted set of applications. 

If `[DevicePolicyManager.isLockTaskPermitted(String)](https://developer.android.com/reference/kotlin/android/app/admin/DevicePolicyManager#isLockTaskPermitted\(kotlin.String\))` returns `true` for this component, the current task will be launched directly into LockTask mode. Only apps allowlisted by `[DevicePolicyManager.setLockTaskPackages(ComponentName,String[])](https://developer.android.com/reference/kotlin/android/app/admin/DevicePolicyManager#setLockTaskPackages\(android.content.ComponentName,%20kotlin.Array\))` can be launched while LockTask mode is active. The user will not be able to leave this mode until this activity calls `stopLockTask()`. Calling this method while the device is already in LockTask mode has no effect. 

Otherwise, the current task will be launched into screen pinning mode. In this case, the system will prompt the user with a dialog requesting permission to use this mode. The user can exit at any time through instructions shown on the request dialog. Calling `stopLockTask()` will also terminate this mode. 

**Note:** this method can only be called when the activity is foreground. That is, between `onResume()` and `onPause()`.

**See Also**

  * `#stopLockTask()`
  * `[android.R.attr#lockTaskMode](https://developer.android.com/reference/kotlin/android/R.attr.html#lockTaskMode:kotlin.Int)`



### startManagingCursor

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~startManagingCursor~~(c: [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[android.content.CursorLoader](https://developer.android.com/reference/kotlin/android/content/CursorLoader.html)` class with `[LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)` instead; this is also available on older platforms through the Android compatibility package._

This method allows the activity to take care of managing the given `[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)`'s lifecycle for you based on the activity's lifecycle. That is, when the activity is stopped it will automatically call `[Cursor.deactivate](https://developer.android.com/reference/kotlin/android/database/Cursor.html#deactivate\(\))` on the given Cursor, and when it is later restarted it will call `[Cursor.requery](https://developer.android.com/reference/kotlin/android/database/Cursor.html#requery\(\))` for you. When the activity is destroyed, all managed Cursors will be closed automatically. _If you are targeting`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, consider instead using `[LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)` instead, available via `getLoaderManager()`._

**Warning:** Do not call android.database.Cursor#close() on cursor obtained from `managedQuery`, because the activity will do that for you at the appropriate time. However, if you call `stopManagingCursor` on a cursor from a managed query, the system _will not_ automatically close the cursor and, in that case, you must call android.database.Cursor#close().

Parameters  
---  
`c` | [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!: The Cursor to be managed.  
  
**See Also**

  * `#managedQuery(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)`
  * `#stopManagingCursor`



### startNextMatchingActivity

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startNextMatchingActivity(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Same as calling `startNextMatchingActivity(Intent,Bundle)` with no options.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): The intent to dispatch to the next activity. For correct behavior, this must be the same as the Intent that started your own activity; the only changes you can make are to the extras inside of it.   
This value cannot be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns a boolean indicating whether there was another Activity to start: true if there was a next activity to start, false if there wasn't. In general, if true is returned you will then want to call finish() on yourself.  
  
### startNextMatchingActivity

Added in [API level 16](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startNextMatchingActivity(  
        intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html),   
        options: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Special version of starting an activity, for use when you are replacing other activity components. You can use this to hand the Intent off to the next Activity that can handle it. You typically call this in #onCreate with the Intent returned by `getIntent`. Note: For security reasons, the caller identity propagated to the next activity will reflect this intermediary app's identity unless it shares the same UID as the original caller. The receiving activity should validate the immediate caller rather than assuming the original intent sender is preserved.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html): The intent to dispatch to the next activity. For correct behavior, this must be the same as the Intent that started your own activity; the only changes you can make are to the extras inside of it.   
This value cannot be `null`.  
`options` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: Additional options for how the Activity should be started. See `[android.content.Context.startActivity(Intent,Bundle)](https://developer.android.com/reference/kotlin/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` Context.startActivity(Intent, Bundle)} for more details.   
This value may be `null`.  
Return  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | Returns a boolean indicating whether there was another Activity to start: true if there was a next activity to start, false if there wasn't. In general, if true is returned you will then want to call finish() on yourself.  
  
### startPostponedEnterTransition

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startPostponedEnterTransition(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Begin postponed transitions after `postponeEnterTransition()` was called. If postponeEnterTransition() was called, you must call startPostponedEnterTransition() to have your Activity start drawing.

### startSearch

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun startSearch(  
        initialQuery: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?,   
        selectInitialQuery: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html),   
        appSearchData: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?,   
        globalSearch: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This hook is called to launch the search UI. 

It is typically called from onSearchRequested(), either directly from Activity.onSearchRequested() or from an overridden version in any given Activity. If your goal is simply to activate search, it is preferred to call onSearchRequested(), which may have been overridden elsewhere in your Activity. If your goal is to inject specific data such as context data, it is preferred to _override_ onSearchRequested(), so that any callers to it will benefit from the override. 

Note: when running in a `[Configuration.UI_MODE_TYPE_WATCH](https://developer.android.com/reference/kotlin/android/content/res/Configuration.html#UI_MODE_TYPE_WATCH:kotlin.Int)`, use of this API is not supported.

Parameters  
---  
`initialQuery` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?: Any non-null non-empty string will be inserted as pre-entered text in the search query box.  
`selectInitialQuery` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): If true, the initial query will be preselected, which means that any further typing will replace it. This is useful for cases where an entire pre-formed query is being inserted. If false, the selection point will be placed at the end of the inserted query. This is useful when the inserted query is text that the user entered, and the user would expect to be able to keep typing. _This parameter is only meaningful if initialQuery is a non-empty string._  
`appSearchData` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: An application can insert application-specific context here, in order to improve quality or specificity of its own searches. This data will be returned with SEARCH intent(s). Null if no extra data is required.   
This value may be `null`.  
`globalSearch` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): If false, this will only launch the search that has been specifically defined by the application (which is usually defined as a local search). If no default search is defined in the current application or activity, global search will be launched. If true, this will always launch a platform-global (e.g. web-based) search instead.  
  
**See Also**

  * `[android.app.SearchManager](https://developer.android.com/reference/kotlin/android/app/SearchManager)`



### stopLocalVoiceInteraction

Added in [API level 24](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun stopLocalVoiceInteraction(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Request to terminate the current voice interaction that was previously started using `startLocalVoiceInteraction(Bundle)`. When the interaction is terminated, `onLocalVoiceInteractionStopped()` will be called.

### stopLockTask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun stopLockTask(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Stop the current task from being locked. 

Called to end the LockTask or screen pinning mode started by `startLockTask()`. This can only be called by activities that have called `startLockTask()` previously. 

**Note:** If the device is in LockTask mode that is not initially started by this activity, then calling this method will not terminate the LockTask mode, but only finish its own task. The device will remain in LockTask mode, until the activity which started the LockTask mode calls this method, or until its allowlist authorization is revoked by `[DevicePolicyManager.setLockTaskPackages(ComponentName,String[])](https://developer.android.com/reference/kotlin/android/app/admin/DevicePolicyManager#setLockTaskPackages\(android.content.ComponentName,%20kotlin.Array\))`.

**See Also**

  * `#startLockTask()`
  * `[android.R.attr#lockTaskMode](https://developer.android.com/reference/kotlin/android/R.attr.html#lockTaskMode:kotlin.Int)`
  * `[android.app.ActivityManager#getLockTaskModeState()](https://developer.android.com/reference/kotlin/android/app/ActivityManager#getLockTaskModeState\(\))`



### stopManagingCursor

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun ~~stopManagingCursor~~(c: [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[android.content.CursorLoader](https://developer.android.com/reference/kotlin/android/content/CursorLoader.html)` class with `[LoaderManager](https://developer.android.com/reference/kotlin/android/app/LoaderManager)` instead; this is also available on older platforms through the Android compatibility package._

Given a Cursor that was previously given to `startManagingCursor`, stop the activity's management of that cursor. 

**Warning:** After calling this method on a cursor from a managed query, the system _will not_ automatically close the cursor and you must call android.database.Cursor#close().

Parameters  
---  
`c` | [Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)!: The Cursor that was being managed.  
  
**See Also**

  * `#startManagingCursor`



### takeKeyEvents

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun takeKeyEvents(get: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Request that key events come to this activity. Use this if your activity has no views with focus, but the activity still wants a chance to process key events.

**See Also**

  * `[android.view.Window#takeKeyEvents](https://developer.android.com/reference/kotlin/android/view/Window.html#takeKeyEvents\(kotlin.Boolean\))`



### triggerSearch

Added in [API level 5](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun triggerSearch(  
        query: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!,   
        appSearchData: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Similar to `startSearch`, but actually fires off the search query after invoking the search dialog. Made available for testing purposes.

Parameters  
---  
`query` | [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)!: The query to trigger. If empty, the request will be ignored.  
`appSearchData` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: An application can insert application-specific context here, in order to improve quality or specificity of its own searches. This data will be returned with SEARCH intent(s). Null if no extra data is required.   
This value may be `null`.  
  
### unregisterActivityLifecycleCallbacks

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun unregisterActivityLifecycleCallbacks(callback: [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Unregister an `[Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks)` previously registered with `registerActivityLifecycleCallbacks`. It will not receive any further callbacks.

Parameters  
---  
`callback` | [Application.ActivityLifecycleCallbacks](https://developer.android.com/reference/kotlin/android/app/Application.ActivityLifecycleCallbacks): The callback instance to unregister.   
This value cannot be `null`.  
  
**See Also**

  * `#registerActivityLifecycleCallbacks`



### unregisterComponentCallbacks

Added in [API level 14](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun unregisterComponentCallbacks(callback: [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Remove a `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` object that was previously registered with `[registerComponentCallbacks(ComponentCallbacks)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#registerComponentCallbacks\(android.content.ComponentCallbacks\))`. 

After `[Build.VERSION_CODES.TIRAMISU](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#TIRAMISU:kotlin.Int)`, the `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` will be unregistered to `[the base Context](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#getBaseContext\(\))`, and can be only used after `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`

Parameters  
---  
`callback` | [ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)!: The interface to call. This can be either a `[ComponentCallbacks](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks.html)` or `[ComponentCallbacks2](https://developer.android.com/reference/kotlin/android/content/ComponentCallbacks2.html)` interface.  
Exceptions  
---  
`java.lang.IllegalStateException` | if this method calls before `[attachBaseContext(Context)](https://developer.android.com/reference/kotlin/android/content/ContextWrapper.html#attachBaseContext\(android.content.Context\))`  
  
### unregisterForContextMenu

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun unregisterForContextMenu(view: [View](https://developer.android.com/reference/kotlin/android/view/View.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Prevents a context menu to be shown for the given view. This method will remove the `[OnCreateContextMenuListener](https://developer.android.com/reference/kotlin/android/view/View.OnCreateContextMenuListener.html)` on the view.

Parameters  
---  
`view` | [View](https://developer.android.com/reference/kotlin/android/view/View.html)!: The view that should stop showing a context menu.  
  
**See Also**

  * `#registerForContextMenu(android.view.View)`



### unregisterScreenCaptureCallback

Added in [API level 34](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    open fun unregisterScreenCaptureCallback(callback: [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Unregisters a screen capture callback for this surface.   
Requires `[android.Manifest.permission#DETECT_SCREEN_CAPTURE](https://developer.android.com/reference/kotlin/android/Manifest.permission.html#DETECT_SCREEN_CAPTURE:kotlin.String)`

Parameters  
---  
`callback` | [Activity.ScreenCaptureCallback](https://developer.android.com/reference/kotlin/android/app/Activity.ScreenCaptureCallback): This value cannot be `null`.  
  
## Protected methods

### attachBaseContext

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun attachBaseContext(newBase: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Set the base context for this ContextWrapper. All calls will then be delegated to the base context. Throws IllegalStateException if a base context has already been set.

Parameters  
---  
`base` | The new base context for this wrapper.  
  
### onActivityResult

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onActivityResult(  
        requestCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        resultCode: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        data: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when an activity you launched exits, giving you the requestCode you started it with, the resultCode it returned, and any additional data from it. The resultCode will be `RESULT_CANCELED` if the activity explicitly returned that, didn't return any result, or crashed during its operation. 

An activity can never receive a result in the resumed state. You can count on `onResume` being called after this method, though not necessarily immediately after. If the activity was resumed, it will be paused and the result will be delivered, followed by `onResume`. If the activity wasn't in the resumed state, then the result will be delivered, with `onResume` called sometime later when the activity becomes active again. 

This method is never invoked if your activity sets `[noHistory](https://developer.android.com/reference/kotlin/android/R.styleable.html#AndroidManifestActivity_noHistory:kotlin.Int)` to `true`.

Parameters  
---  
`requestCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The integer request code originally supplied to startActivityForResult(), allowing you to identify who this result came from.  
`resultCode` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The integer result code returned by the child activity through its setResult().  
`data` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: An Intent, which can return result data to the caller (various data can be attached to Intent "extras").  
  
**See Also**

  * `#createPendingResult`
  * `#setResult(int)`



### onApplyThemeResource

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onApplyThemeResource(  
        theme: [Resources.Theme](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html)!,   
        resid: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        first: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called by #setTheme and #getTheme to apply a theme resource to the current Theme object. May be overridden to change the default (simple) behavior. This method will not be called in multiple threads simultaneously.

Parameters  
---  
`theme` | [Resources.Theme](https://developer.android.com/reference/kotlin/android/content/res/Resources.Theme.html)!: the theme being modified  
`resId` | the style resource being applied to theme  
`first` | [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html): `true` if this is the first time a style is being applied to theme  
  
### onChildTitleChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onChildTitleChanged(  
        childActivity: Activity!,   
        title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### onCreate

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when the activity is starting. This is where most initialization should go: calling `setContentView(int)` to inflate the activity's UI, using `findViewById` to programmatically interact with widgets in the UI, calling `managedQuery(android.net.Uri,String[],String,String[],String)` to retrieve cursors for data being displayed, etc. 

You can call `finish` from within this function, in which case onDestroy() will be immediately called after #onCreate without any of the rest of the activity lifecycle (`onStart`, `onResume`, `onPause`, etc.) executing. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
This method must be called from the main thread of your app.   
If you override this method you _must_ call through to the superclass implementation. Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: If the activity is being re-initialized after previously being shut down then this Bundle contains the data it most recently supplied in #onSaveInstanceState. **_Note: Otherwise it is null._**  
  
**See Also**

  * `#onStart`



### onCreateDialog

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun ~~onCreateDialog~~(id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)): [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!

**Deprecated:**_Old no-arguments version of`onCreateDialog(int,Bundle)`._

### onCreateDialog

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun ~~onCreateDialog~~(  
        id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!  
    ): [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)?

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Callback for creating dialogs that are managed (saved and restored) for you by the activity. The default implementation calls through to `onCreateDialog(int)` for compatibility. _If you are targeting`[android.os.Build.VERSION_CODES#HONEYCOMB](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#HONEYCOMB:kotlin.Int)` or later, consider instead using a `[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` instead._

If you use `showDialog(int)`, the activity will call through to this method the first time, and hang onto it thereafter. Any dialog that is created by this method will automatically be saved and restored for you, including whether it is showing. 

If you would like the activity to manage saving and restoring dialogs for you, you should override this method and handle any ids that are passed to #showDialog. 

If you would like an opportunity to prepare your dialog before it is shown, override `onPrepareDialog(int,Dialog,Bundle)`.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id of the dialog.  
`args` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!: The dialog arguments provided to `showDialog(int,Bundle)`.  
Return  
---  
`[Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)?` | The dialog. If you return null, the dialog will not be created.  
  
**See Also**

  * `#onPrepareDialog(int,android.app.Dialog,android.os.Bundle)`
  * `#showDialog(int,android.os.Bundle)`
  * `#dismissDialog(int)`
  * `#removeDialog(int)`



### onDestroy

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onDestroy(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Perform any final cleanup before an activity is destroyed. This can happen either because the activity is finishing (someone called `finish` on it), or because the system is temporarily destroying this instance of the activity to save space. You can distinguish between these two scenarios with the `isFinishing` method. 

_Note: do not count on this method being called as a place for saving data! For example, if an activity is editing data in a content provider, those edits should be committed in either`onPause` or #onSaveInstanceState, not here._ This method is usually implemented to free resources like threads that are associated with an activity, so that a destroyed activity does not leave such things around while the rest of its application is still running. There are situations where the system will simply kill the activity's hosting process without calling this method (or any others) in it, so it should not be used to do things that are intended to remain around after the process goes away. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onPause`
  * `#onStop`
  * `#finish`
  * `#isFinishing`



### onNewIntent

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onNewIntent(intent: [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This is called for activities that set launchMode to "singleTop" in their package, or if a client used the `[Intent.FLAG_ACTIVITY_SINGLE_TOP](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_SINGLE_TOP:kotlin.Int)` flag when calling #startActivity. In either case, when the activity is re-launched while at the top of the activity stack instead of a new instance of the activity being started, onNewIntent() will be called on the existing instance with the Intent that was used to re-launch it. 

An activity can never receive a new intent in the resumed state. You can count on `onResume` being called after this method, though not necessarily immediately after the completion of this callback. If the activity was resumed, it will be paused and new intent will be delivered, followed by `onResume`. If the activity wasn't in the resumed state, then new intent can be delivered immediately, with `onResume()` called sometime later when activity becomes active again. 

Note that `getIntent` still returns the original Intent. You can use `setIntent(Intent)` to update it to this new Intent.

Parameters  
---  
`intent` | [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)!: The new intent that was used to start the activity  
  
**See Also**

  * `#getIntent`
  * `#setIntent(android.content.Intent)`
  * `#onResume`



### onPause

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onPause(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called as part of the activity lifecycle when the user no longer actively interacts with the activity, but it is still visible on screen. The counterpart to `onResume`

When activity B is launched in front of activity A, this callback will be invoked on A. B will not be created until A's `onPause` returns, so be sure to not do anything lengthy here. 

This callback is mostly used for saving any persistent state the activity is editing, to present a "edit in place" model to the user and making sure nothing is lost if there are not enough resources to start the new activity without first killing this one. This is also a good place to stop things that consume a noticeable amount of CPU in order to make the switch to the next activity as fast as possible. 

On platform versions prior to `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` this is also a good place to try to close exclusive-access devices or to release access to singleton resources. Starting with `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` there can be multiple resumed activities in the system at the same time, so `onTopResumedActivityChanged(boolean)` should be used for that purpose instead. 

If an activity is launched on top, after receiving this call you will usually receive a following call to `onStop` (after the next activity has been resumed and displayed above). However in some cases there will be a direct call back to `onResume` without going through the stopped state. An activity can also rest in paused state in some cases when in multi-window mode, still visible to user. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onResume`
  * `#onStop`



### onPostCreate

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onPostCreate(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when activity start-up is complete (after `onStart` and #onRestoreInstanceState have been called). Applications will generally not implement this method; it is intended for system classes to do final initialization after application code has run. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)?: If the activity is being re-initialized after previously being shut down then this Bundle contains the data it most recently supplied in #onSaveInstanceState. **_Note: Otherwise it is null._**  
  
**See Also**




### onPostResume

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onPostResume(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when activity resume is complete (after `onResume` has been called). Applications will generally not implement this method; it is intended for system classes to do final setup after application resume code has run. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onResume`



### onPrepareDialog

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun ~~onPrepareDialog~~(  
        id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        dialog: [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Old no-arguments version of`onPrepareDialog(int,Dialog,Bundle)`._

### onPrepareDialog

Added in [API level 8](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)  
Deprecated in [API level 15](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun ~~onPrepareDialog~~(  
        id: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html),   
        dialog: [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!,   
        args: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**Deprecated:**_Use the new`[DialogFragment](https://developer.android.com/reference/kotlin/android/app/DialogFragment)` class with `[FragmentManager](https://developer.android.com/reference/kotlin/android/app/FragmentManager)` instead; this is also available on older platforms through the Android compatibility package._

Provides an opportunity to prepare a managed dialog before it is being shown. The default implementation calls through to `onPrepareDialog(int,Dialog)` for compatibility. 

Override this if you need to update a managed dialog based on the state of the application each time it is shown. For example, a time picker dialog might want to be updated with the current time. You should call through to the superclass's implementation. The default implementation will set this Activity as the owner activity on the Dialog.

Parameters  
---  
`id` | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html): The id of the managed dialog.  
`dialog` | [Dialog](https://developer.android.com/reference/kotlin/android/app/Dialog)!: The dialog.  
`args` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)!: The dialog arguments provided to `showDialog(int,Bundle)`.  
  
**See Also**

  * `#onCreateDialog(int,android.os.Bundle)`
  * `#showDialog(int)`
  * `#dismissDialog(int)`
  * `#removeDialog(int)`



### onRestart

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onRestart(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called after `onStop` when the current activity is being re-displayed to the user (the user has navigated back to it). It will be followed by `onStart` and then `onResume`

For activities that are using raw `[Cursor](https://developer.android.com/reference/kotlin/android/database/Cursor.html)` objects (instead of creating them through `managedQuery(android.net.Uri,String[],String,String[],String)`, this is usually the place where the cursor should be requeried (because you had deactivated it in `onStop`. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onStop`
  * `#onStart`
  * `#onResume`



### onRestoreInstanceState

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onRestoreInstanceState(savedInstanceState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

This method is called after `onStart` when the activity is being re-initialized from a previously saved state, given here in savedInstanceState. Most implementations will simply use #onCreate to restore their state, but it is sometimes convenient to do it here after all of the initialization has been done or to allow subclasses to decide whether to use your default implementation. The default implementation of this method performs a restore of any view state that had previously been frozen by #onSaveInstanceState. 

This method is called between `onStart` and #onPostCreate. This method is called only when recreating an activity; the method isn't invoked if `onStart` is called for any other reason.

Parameters  
---  
`savedInstanceState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html): the data most recently supplied in #onSaveInstanceState.   
This value cannot be `null`.  
  
**See Also**

  * `#onResume`



### onResume

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onResume(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called after #onRestoreInstanceState, `onRestart`, or `onPause`. This is usually a hint for your activity to start interacting with the user, which is a good indicator that the activity became active and ready to receive input. This sometimes could also be a transit state toward another resting state. For instance, an activity may be relaunched to `onPause` due to configuration changes and the activity was visible, but wasn't the top-most activity of an activity task. `onResume` is guaranteed to be called before `onPause` in this case which honors the activity lifecycle policy and the activity eventually rests in `onPause`

On platform versions prior to `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` this is also a good place to try to open exclusive-access devices or to get access to singleton resources. Starting with `[android.os.Build.VERSION_CODES#Q](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#Q:kotlin.Int)` there can be multiple resumed activities in the system simultaneously, so `onTopResumedActivityChanged(boolean)` should be used for that purpose instead. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onRestart`
  * `#onPostResume`
  * `#onPause`
  * `#onTopResumedActivityChanged(boolean)`



### onSaveInstanceState

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onSaveInstanceState(outState: [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called to retrieve per-instance state from an activity before being killed so that the state can be restored in #onCreate or #onRestoreInstanceState (the `[Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)` populated by this method will be passed to both). 

This method is called before an activity may be killed so that when it comes back some time in the future it can restore its state. For example, if activity B is launched in front of activity A, and at some point activity A is killed to reclaim resources, activity A will have a chance to save the current state of its user interface via this method so that when the user returns to activity A, the state of the user interface can be restored via #onCreate or #onRestoreInstanceState. 

Do not confuse this method with activity lifecycle callbacks such as `onPause`, which is always called when the user no longer actively interacts with an activity, or `onStop` which is called when activity becomes invisible. One example of when `onPause` and `onStop` is called and not this method is when a user navigates back from activity B to activity A: there is no need to call #onSaveInstanceState on B because that particular instance will never be restored, so the system avoids calling it. An example when `onPause` is called and not #onSaveInstanceState is when activity B is launched in front of activity A: the system may avoid calling #onSaveInstanceState on activity A if it isn't killed during the lifetime of B since the state of the user interface of A will stay intact. 

The default implementation takes care of most of the UI per-instance state for you by calling `[android.view.View#onSaveInstanceState()](https://developer.android.com/reference/kotlin/android/view/View.html#onSaveInstanceState\(\))` on each view in the hierarchy that has an id, and by saving the id of the currently focused view (all of which is restored by the default implementation of #onRestoreInstanceState). If you override this method to save additional information not captured by each individual view, you will likely want to call through to the default implementation, otherwise be prepared to save all of the state of each view yourself. 

If called, this method will occur after `onStop` for applications targeting platforms starting with `[android.os.Build.VERSION_CODES#P](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#P:kotlin.Int)`. For applications targeting earlier platform versions this method will occur before `onStop` and there are no guarantees about whether it will occur before or after `onPause`.

Parameters  
---  
`outState` | [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html): Bundle in which to place your saved state.   
This value cannot be `null`.  
  
**See Also**

  * `#onPause`



### onStart

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onStart(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called after #onCreate — or after `onRestart` when the activity had been stopped, but is now again being displayed to the user. It will usually be followed by `onResume`. This is a good place to begin drawing visual elements, running animations, etc. 

You can call `finish` from within this function, in which case `onStop` will be immediately called after `onStart` without the lifecycle transitions in-between (`onResume`, `onPause`, etc.) executing. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onStop`
  * `#onResume`



### onStop

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onStop(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called when you are no longer visible to the user. You will next receive either `onRestart`, `onDestroy`, or nothing, depending on later user activity. This is a good place to stop refreshing UI, running animations and other visual things. 

_Derived classes must call through to the super class's implementation of this method. If they do not, an exception will be thrown._

.   
If you override this method you _must_ call through to the superclass implementation. 

**See Also**

  * `#onRestart`
  * `#onResume`
  * `#onDestroy`



### onTitleChanged

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onTitleChanged(  
        title: [CharSequence](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-char-sequence/index.html)!,   
        color: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)  
    ): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

### onUserLeaveHint

Added in [API level 3](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected open fun onUserLeaveHint(): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Called as part of the activity lifecycle when an activity is about to go into the background as the result of user choice. For example, when the user presses the Home key, `onUserLeaveHint` will be called, but when an incoming phone call causes the in-call Activity to be automatically brought to the foreground, `onUserLeaveHint` will not be called on the activity being interrupted. In cases when it is invoked, this method is called right before the activity's `onPause` callback. 

This callback and `onUserInteraction` are intended to help activities manage status bar notifications intelligently; specifically, for helping activities determine the proper time to cancel a notification.

**See Also**

  * `#onUserInteraction()`
  * `[android.content.Intent#FLAG_ACTIVITY_NO_USER_ACTION](https://developer.android.com/reference/kotlin/android/content/Intent.html#FLAG_ACTIVITY_NO_USER_ACTION:kotlin.Int)`



## Properties

### FOCUSED_STATE_SET

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#ApiLevels)
    
    
    protected static val FOCUSED_STATE_SET: [IntArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int-array/index.html)!

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-28 UTC."],[],[]] 
