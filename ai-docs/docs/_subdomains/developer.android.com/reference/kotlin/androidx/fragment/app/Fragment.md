---
url: https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment/
title: Fragment \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:52.919984+00:00
---

# Fragment  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Fragment

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/Fragment.java+class:androidx.fragment.app.Fragment)

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

* * *

Kotlin |[Java](https://developer.android.com/reference/androidx/fragment/app/Fragment "View this page in Java")
    
    
    class [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment) : [ComponentCallbacks](https://developer.android.com/reference/android/content/ComponentCallbacks.html), [View.OnCreateContextMenuListener](https://developer.android.com/reference/android/view/View.OnCreateContextMenuListener.html), [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner), [ViewModelStoreOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner), [HasDefaultViewModelProviderFactory](https://developer.android.com/reference/kotlin/androidx/lifecycle/HasDefaultViewModelProviderFactory), [SavedStateRegistryOwner](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistryOwner), [ActivityResultCaller](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCaller), [ContextAware](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware)

Known direct subclasses 

[AbstractListDetailFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/AbstractListDetailFragment), [AbstractProgressFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/AbstractProgressFragment), [AmbientModeSupport](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientModeSupport), [BrandedSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BrandedSupportFragment), [ComposableFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableFragment), [DialogFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/DialogFragment), [GuidedStepSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/GuidedStepSupportFragment), [HeadersSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/HeadersSupportFragment), [LeanbackPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackPreferenceDialogFragmentCompat), [LeanbackSettingsFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackSettingsFragmentCompat), [ListFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/ListFragment), [MediaRouteDiscoveryFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteDiscoveryFragment), [NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment), [OnboardingSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/OnboardingSupportFragment), [PdfViewerFragment](https://developer.android.com/reference/kotlin/androidx/pdf/viewer/fragment/PdfViewerFragment), [PlaybackSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/PlaybackSupportFragment), [PreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceFragmentCompat), [PreferenceHeaderFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceHeaderFragmentCompat), [RowsSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/RowsSupportFragment), [SearchSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/SearchSupportFragment)

`[AbstractListDetailFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/AbstractListDetailFragment)` |  A fragment supports adaptive two-pane layout.  
---|---  
`[AbstractProgressFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/AbstractProgressFragment)` |  The base class for `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)`s that handle dynamic feature installation.  
`[AmbientModeSupport](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientModeSupport)` |  **This class is deprecated.** Use `[AmbientLifecycleObserver](https://developer.android.com/reference/kotlin/androidx/wear/ambient/AmbientLifecycleObserver)` instead.  
`[BrandedSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BrandedSupportFragment)` |  Fragment class for managing search and branding using a view that implements `[TitleViewAdapter.Provider](https://developer.android.com/reference/kotlin/androidx/leanback/widget/TitleViewAdapter.Provider)`.  
`[ComposableFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableFragment)` |  This class provides a `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` wrapper around a composable function that is loaded via reflection.  
`[DialogFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/DialogFragment)` |  A fragment that displays a dialog window, floating in the foreground of its activity's window.  
`[GuidedStepSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/GuidedStepSupportFragment)` |  A GuidedStepSupportFragment is used to guide the user through a decision or series of decisions.  
`[HeadersSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/HeadersSupportFragment)` |  An fragment containing a list of row headers.  
`[LeanbackPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackPreferenceDialogFragmentCompat)` |  A fragment that shows `[DialogPreference](https://developer.android.com/reference/kotlin/androidx/preference/DialogPreference)`, for example `[androidx.preference.ListPreference](https://developer.android.com/reference/kotlin/androidx/preference/ListPreference)` or `[androidx.preference.MultiSelectListPreference](https://developer.android.com/reference/kotlin/androidx/preference/MultiSelectListPreference)`.  
`[LeanbackSettingsFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackSettingsFragmentCompat)` |  This fragment provides a container for displaying a `[LeanbackPreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackPreferenceFragmentCompat)`  
`[ListFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/ListFragment)` |  Static library support version of the framework's `[android.app.ListFragment](https://developer.android.com/reference/android/app/ListFragment.html)`.  
`[MediaRouteDiscoveryFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteDiscoveryFragment)` |  Media route discovery fragment.  
`[NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment)` |  NavHostFragment provides an area within your layout for self-contained navigation to occur.  
`[OnboardingSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/OnboardingSupportFragment)` |  An OnboardingSupportFragment provides a common and simple way to build onboarding screen for applications.  
`[PdfViewerFragment](https://developer.android.com/reference/kotlin/androidx/pdf/viewer/fragment/PdfViewerFragment)` |  A Fragment that renders a PDF document.  
`[PlaybackSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/PlaybackSupportFragment)` |  A fragment for displaying playback controls and related content.  
`[PreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceFragmentCompat)` |  A PreferenceFragmentCompat is the entry point to using the Preference library.  
`[PreferenceHeaderFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceHeaderFragmentCompat)` |  `[PreferenceHeaderFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceHeaderFragmentCompat)` implements a two-pane fragment for preferences.  
`[RowsSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/RowsSupportFragment)` |  An ordered set of rows of leanback widgets.  
`[SearchSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/SearchSupportFragment)` |  A fragment to handle searches.  
  
Known indirect subclasses 

[AppCompatDialogFragment](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatDialogFragment), [BaseLeanbackPreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/BaseLeanbackPreferenceFragmentCompat), [BaseSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BaseSupportFragment), [BrowseSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BrowseSupportFragment), [ComposableNavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableNavHostFragment), [DefaultProgressFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/DefaultProgressFragment), [DetailsSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/DetailsSupportFragment), [DynamicNavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/DynamicNavHostFragment), [EditTextPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/EditTextPreferenceDialogFragmentCompat), [EditablePdfViewerFragment](https://developer.android.com/reference/kotlin/androidx/pdf/ink/EditablePdfViewerFragment), [ErrorSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/ErrorSupportFragment), [LeanbackEditTextPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackEditTextPreferenceDialogFragmentCompat), [LeanbackListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackListPreferenceDialogFragmentCompat), [LeanbackPreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackPreferenceFragmentCompat), [ListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/ListPreferenceDialogFragmentCompat), [MediaRouteChooserDialogFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteChooserDialogFragment), [MediaRouteControllerDialogFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteControllerDialogFragment), [MultiSelectListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/MultiSelectListPreferenceDialogFragmentCompat), [PreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceDialogFragmentCompat), [VerticalGridSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/VerticalGridSupportFragment), [VideoSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/VideoSupportFragment)

`[AppCompatDialogFragment](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatDialogFragment)` |  A special version of `[DialogFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/DialogFragment)` which uses an `[AppCompatDialog](https://developer.android.com/reference/kotlin/androidx/appcompat/app/AppCompatDialog)` in place of a platform-styled dialog.  
---|---  
`[BaseLeanbackPreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/BaseLeanbackPreferenceFragmentCompat)` |  This fragment provides a preference fragment with leanback-style behavior, suitable for embedding into broader UI elements.  
`[BaseSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BaseSupportFragment)` |  Base class for leanback Fragments.  
`[BrowseSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/BrowseSupportFragment)` |  A fragment for creating Leanback browse screens.  
`[ComposableNavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableNavHostFragment)` |  A `[NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment)` that adds support for `[ComposableFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableFragment)` instances via `[ComposableFragmentNavigator](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/compose/ComposableFragmentNavigator)`.  
`[DefaultProgressFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/ui/DefaultProgressFragment)` |  The default `[androidx.fragment.app.Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` to display during installation progress.  
`[DetailsSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/DetailsSupportFragment)` |  A fragment for creating Leanback details screens.  
`[DynamicNavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/dynamicfeatures/fragment/DynamicNavHostFragment)` |  The `[NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment)` for dynamic features.  
`[EditTextPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/EditTextPreferenceDialogFragmentCompat)` |   
`[EditablePdfViewerFragment](https://developer.android.com/reference/kotlin/androidx/pdf/ink/EditablePdfViewerFragment)` |  A `[androidx.fragment.app.Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` that extends `[PdfViewerFragment](https://developer.android.com/reference/kotlin/androidx/pdf/viewer/fragment/PdfViewerFragment)` to provide PDF editing capabilities, including annotation and form filling, leveraging the 'androidx.ink' library.  
`[ErrorSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/ErrorSupportFragment)` |  A fragment for displaying an error indication.  
`[LeanbackEditTextPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackEditTextPreferenceDialogFragmentCompat)` |  Implemented a dialog to input text.  
`[LeanbackListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackListPreferenceDialogFragmentCompat)` |  Implemented a dialog to show `[ListPreference](https://developer.android.com/reference/kotlin/androidx/preference/ListPreference)` or `[MultiSelectListPreference](https://developer.android.com/reference/kotlin/androidx/preference/MultiSelectListPreference)`.  
`[LeanbackPreferenceFragmentCompat](https://developer.android.com/reference/kotlin/androidx/leanback/preference/LeanbackPreferenceFragmentCompat)` |  This fragment provides a fully decorated leanback-style preference fragment, including a list background and header.  
`[ListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/ListPreferenceDialogFragmentCompat)` |   
`[MediaRouteChooserDialogFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteChooserDialogFragment)` |  Media route chooser dialog fragment.  
`[MediaRouteControllerDialogFragment](https://developer.android.com/reference/kotlin/androidx/mediarouter/app/MediaRouteControllerDialogFragment)` |  Media route controller dialog fragment.  
`[MultiSelectListPreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/MultiSelectListPreferenceDialogFragmentCompat)` |   
`[PreferenceDialogFragmentCompat](https://developer.android.com/reference/kotlin/androidx/preference/PreferenceDialogFragmentCompat)` |  Abstract base class which presents a dialog associated with a `[DialogPreference](https://developer.android.com/reference/kotlin/androidx/preference/DialogPreference)`.  
`[VerticalGridSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/VerticalGridSupportFragment)` |  A fragment for creating leanback vertical grids.  
`[VideoSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/VideoSupportFragment)` |  Subclass of `[PlaybackSupportFragment](https://developer.android.com/reference/kotlin/androidx/leanback/app/PlaybackSupportFragment)` that is responsible for providing a `[SurfaceView](https://developer.android.com/reference/android/view/SurfaceView.html)` and rendering video.  
  
* * *

Static library support version of the framework's `[android.app.Fragment](https://developer.android.com/reference/android/app/Fragment.html)`. Used to write apps that run on platforms prior to Android 3.0. When running on Android 3.0 or above, this implementation is still used; it does not try to switch to the framework's implementation. See the framework `[android.app.Fragment](https://developer.android.com/reference/android/app/Fragment.html)` documentation for a class overview. 

The main differences when using this support version instead of the framework version are: 

  * Your activity must extend `[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)`
  * You must call `[getSupportFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity#getSupportFragmentManager\(\))` to get the `[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)`



## Summary

### Nested types  
  
---  
`class [Fragment.InstantiationException](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.InstantiationException) : [RuntimeException](https://developer.android.com/reference/java/lang/RuntimeException.html)` Thrown by `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory#instantiate\(java.lang.ClassLoader,java.lang.String\))` when there is an instantiation failure.  
`class [Fragment.SavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.SavedState) : [Parcelable](https://developer.android.com/reference/android/os/Parcelable.html)` State information that has been retrieved from a fragment instance through `[FragmentManager.saveFragmentInstanceState](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#saveFragmentInstanceState\(androidx.fragment.app.Fragment\))`.  
  
### Public constructors  
  
---  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(\))()` Constructor used by the default `[FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory)`.  
`@[ContentView](https://developer.android.com/reference/kotlin/androidx/annotation/ContentView)  
[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(int\))(contentLayoutId: @[LayoutRes](https://developer.android.com/reference/kotlin/androidx/annotation/LayoutRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Alternate constructor that can be called from your default, no argument constructor to provide a default layout that will be inflated by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`.  
  
### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))(listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener))` Add a new `[OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` for receiving a callback for when this class is associated with a `[android.content.Context](https://developer.android.com/reference/android/content/Context.html)`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[dump](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#dump\(java.lang.String,java.io.FileDescriptor,java.io.PrintWriter,java.lang.String\[\]\))(  
prefix: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
fd: [FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor.html)?,  
writer: [PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html),  
args: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>?  
)` Print the Fragments's state into the given stream.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[equals](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#equals\(java.lang.Object\))(o: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Subclasses can not override equals().  
`[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)?` |  `[getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))()` Return the `[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)` this fragment is currently associated with.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[getAllowEnterTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getAllowEnterTransitionOverlap\(\))()` Returns whether the the exit transition and enter transition overlap or not.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[getAllowReturnTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getAllowReturnTransitionOverlap\(\))()` Returns whether the the return transition and reenter transition overlap or not.  
`[Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  `[getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))()` Return the arguments supplied when the fragment was instantiated, if any.  
`[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)` |  `[getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))()` Return a private FragmentManager for placing and managing Fragments inside of this Fragment.  
`[Context](https://developer.android.com/reference/android/content/Context.html)?` |  `[getContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getContext\(\))()` Return the `[Context](https://developer.android.com/reference/android/content/Context.html)` this fragment is currently associated with.  
`[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` |  `@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[getDefaultViewModelCreationExtras](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getDefaultViewModelCreationExtras\(\))()` The default `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` to pass into `[ViewModelProvider.Factory.create](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory#create\(kotlin.reflect.KClass,androidx.lifecycle.viewmodel.CreationExtras\))` when no overriding `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` are provided.  
`[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` |  `[getDefaultViewModelProviderFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getDefaultViewModelProviderFactory\(\))()` The default `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` to use when no custom `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` is provided to the `[ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider)`.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getEnterTransition\(\))()` Returns the Transition that will be used to move Views into the initial scene.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getExitTransition\(\))()` Returns the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack.  
`[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)?` |  `~~[getFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getFragmentManager\(\))~~()` **This function is deprecated.** This has been removed in favor of `getParentFragmentManager()` which throws an `[IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` if the FragmentManager is null.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getHost\(\))()` Return the host object of this fragment.  
`[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  `[getId](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getId\(\))()` Return the identifier this fragment is known by.  
`[LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)` |  `[getLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLayoutInflater\(\))()` Returns the cached LayoutInflater used to inflate Views of this Fragment.  
`[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)` |  `[getLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLifecycle\(\))()` The `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)` of this owner.  
`[LoaderManager](https://developer.android.com/reference/kotlin/androidx/loader/app/LoaderManager)` |  `~~[getLoaderManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLoaderManager\(\))~~()` **This function is deprecated.** Use `[LoaderManager.getInstance(this)](https://developer.android.com/reference/kotlin/androidx/loader/app/LoaderManager#getInstance\(T\))`.  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?` |  `[getParentFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragment\(\))()` Returns the parent Fragment containing this Fragment.  
`[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)` |  `[getParentFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))()` Return the FragmentManager for interacting with fragments associated with this fragment's activity.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getReenterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getReenterTransition\(\))()` Returns the Transition that will be used to move Views in to the scene when returning due to popping a back stack.  
`[Resources](https://developer.android.com/reference/android/content/res/Resources.html)` |  `[getResources](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getResources\(\))()` Return `requireActivity().getResources()`.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `~~[getRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getRetainInstance\(\))~~()` **This function is deprecated.** Instead of retaining the Fragment itself, use a non-retained Fragment and keep retained state in a ViewModel attached to that Fragment.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getReturnTransition\(\))()` Returns the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack.  
`[SavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry)` |  `[getSavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSavedStateRegistry\(\))()` The `[SavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry)` owned by this `[SavedStateRegistryOwner](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistryOwner)`.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSharedElementEnterTransition\(\))()` Returns the Transition that will be used for shared elements transferred into the content Scene.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  `[getSharedElementReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSharedElementReturnTransition\(\))()` Return the Transition that will be used for shared elements transferred back during a pop of the back stack.  
`[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  `[getString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getString\(int\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Return a localized string from the application's package's default string table.  
`[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  `[getString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getString\(int,java.lang.Object...\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), formatArgs: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)!>?)` Return a localized formatted string from the application's package's default string table, substituting the format arguments as defined in `[java.util.Formatter](https://developer.android.com/reference/java/util/Formatter.html)` and `[format](https://developer.android.com/reference/java/lang/String.html#format\(java.lang.String,%20java.lang.Object...\))`.  
`[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?` |  `[getTag](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTag\(\))()` Get the tag name of the fragment, if specified.  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?` |  `~~[getTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetFragment\(\))~~()` **This function is deprecated.** Instead of using a target fragment to pass results, use `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResult\(java.lang.String,android.os.Bundle\))` to deliver results to `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` instances registered by other fragments via `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))`.  
`[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  `~~[getTargetRequestCode](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetRequestCode\(\))~~()` **This function is deprecated.** When using the target fragment replacement of `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))` and `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResult\(java.lang.String,android.os.Bundle\))`, consider using `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` to pass a `requestKey` if you need to support dynamic request keys.  
`[CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html)` |  `[getText](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getText\(int\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Return a localized, styled CharSequence from the application's package's default string table.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `~~[getUserVisibleHint](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getUserVisibleHint\(\))~~()` **This function is deprecated.** Use `[setMaxLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setMaxLifecycle\(androidx.fragment.app.Fragment,androidx.lifecycle.Lifecycle.State\))` instead.  
`[View](https://developer.android.com/reference/android/view/View.html)?` |  `[getView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))()` Get the root view for the fragment's layout (the one returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`), if provided.  
`[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[getViewLifecycleOwner](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwner\(\))()` Get a `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` that represents the `[Fragment's View](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))` lifecycle.  
`[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)!>` |  `[getViewLifecycleOwnerLiveData](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData\(\))()` Retrieve a `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)` which allows you to observe the `[lifecycle of the Fragment's View](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwner\(\))`.  
`[ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore)` |  `[getViewModelStore](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewModelStore\(\))()` Returns the `[ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore)` associated with this Fragment   
`[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  `[hashCode](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#hashCode\(\))()` Subclasses can not override hashCode().  
`java-static [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` |  `~~[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#instantiate\(android.content.Context,java.lang.String\))~~(context: [Context](https://developer.android.com/reference/android/content/Context.html), fname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))` **This function is deprecated.** Use `[getFragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#getFragmentFactory\(\))` and `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory#instantiate\(java.lang.ClassLoader,java.lang.String\))`  
`java-static [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` |  `~~[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#instantiate\(android.content.Context,java.lang.String,android.os.Bundle\))~~(context: [Context](https://developer.android.com/reference/android/content/Context.html), fname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), args: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` **This function is deprecated.** Use `[getFragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#getFragmentFactory\(\))` and `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory#instantiate\(java.lang.ClassLoader,java.lang.String\))`, manually calling `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` on the returned Fragment.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isAdded](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isAdded\(\))()` Return true if the fragment is currently added to its activity.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isDetached](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isDetached\(\))()` Return true if the fragment has been explicitly detached from the UI.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isHidden](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isHidden\(\))()` Return true if the fragment has been hidden.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isInLayout](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isInLayout\(\))()` Return true if the layout is included as part of an activity view hierarchy via the  tag.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isRemoving](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isRemoving\(\))()` Return true if this fragment is currently being removed from its activity.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isResumed](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isResumed\(\))()` Return true if the fragment is in the resumed state.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isStateSaved](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isStateSaved\(\))()` Returns true if this fragment is added and its state has already been saved by its host.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[isVisible](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isVisible\(\))()` Return true if the fragment is currently visible to the user.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
~~[onActivityCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityCreated\(android.os.Bundle\))~~(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` **This function is deprecated.** use `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))` for code touching the view created by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` and `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` for other initialization.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))~~(requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), resultCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/android/content/Intent.html)?)` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
~~[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.app.Activity\))~~(activity: [Activity](https://developer.android.com/reference/android/app/Activity.html))` **This function is deprecated.** See `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))(context: [Context](https://developer.android.com/reference/android/content/Context.html))` Called when a fragment is first attached to its context.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onAttachFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttachFragment\(androidx.fragment.app.Fragment\))~~(childFragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment))` **This function is deprecated.** The responsibility for listening for fragments being attached has been moved to FragmentManager.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onConfigurationChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onConfigurationChanged\(android.content.res.Configuration\))(newConfig: [Configuration](https://developer.android.com/reference/android/content/res/Configuration.html))`  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onContextItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onContextItemSelected\(android.view.MenuItem\))(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html))` This hook is called whenever an item in a context menu is selected.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Called to do initial creation of a fragment.  
`[Animation](https://developer.android.com/reference/android/view/animation/Animation.html)?` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onCreateAnimation](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateAnimation\(int,boolean,int\))(transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Called when a fragment loads an animation.  
`[Animator](https://developer.android.com/reference/android/animation/Animator.html)?` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onCreateAnimator](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateAnimator\(int,boolean,int\))(transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Called when a fragment loads an animator.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onCreateContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateContextMenu\(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo\))(  
menu: [ContextMenu](https://developer.android.com/reference/android/view/ContextMenu.html),  
v: [View](https://developer.android.com/reference/android/view/View.html),  
menuInfo: [ContextMenu.ContextMenuInfo](https://developer.android.com/reference/android/view/ContextMenu.ContextMenuInfo.html)?  
)` Called when a context menu for the `view` is about to be shown.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html), inflater: [MenuInflater](https://developer.android.com/reference/android/view/MenuInflater.html))` **This function is deprecated.** `[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override.  
`[View](https://developer.android.com/reference/android/view/View.html)?` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))(  
inflater: [LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html),  
container: [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)?,  
savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
)` Called to have the fragment instantiate its user interface view.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))()` Called when the fragment is no longer in use.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onDestroyOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyOptionsMenu\(\))~~()` **This function is deprecated.** `[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))()` Called when the view previously created by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` has been detached from the fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onDetach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDetach\(\))()` Called when the fragment is no longer attached to its activity.  
`[LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)` |  `[onGetLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onGetLayoutInflater\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Returns the LayoutInflater used to inflate Views of this Fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onHiddenChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onHiddenChanged\(boolean\))(hidden: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Called when the hidden state (as returned by `[isHidden](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isHidden\(\))` of the fragment or another fragment in its hierarchy has changed.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[UiThread](https://developer.android.com/reference/kotlin/androidx/annotation/UiThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
~~[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.app.Activity,android.util.AttributeSet,android.os.Bundle\))~~(  
activity: [Activity](https://developer.android.com/reference/android/app/Activity.html),  
attrs: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet.html),  
savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
)` **This function is deprecated.** See `[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.content.Context,android.util.AttributeSet,android.os.Bundle\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[UiThread](https://developer.android.com/reference/kotlin/androidx/annotation/UiThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.content.Context,android.util.AttributeSet,android.os.Bundle\))(  
context: [Context](https://developer.android.com/reference/android/content/Context.html),  
attrs: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet.html),  
savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
)` Called when a fragment is being created as part of a view layout inflation, typically from setting the content view of an activity.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onLowMemory](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onLowMemory\(\))()` **This function is deprecated.**  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[onMultiWindowModeChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onMultiWindowModeChanged\(boolean\))(isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Called when the Fragment's activity changes from fullscreen mode to multi-window mode and visa-versa.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onOptionsItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onOptionsItemSelected\(android.view.MenuItem\))~~(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html))` **This function is deprecated.** `[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onOptionsMenuClosed](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onOptionsMenuClosed\(android.view.Menu\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html))` **This function is deprecated.** `[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onPause](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPause\(\))()` Called when the Fragment is no longer resumed.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[onPictureInPictureModeChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPictureInPictureModeChanged\(boolean\))(isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Called by the system when the activity changes to and from picture-in-picture mode.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
~~[onPrepareOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPrepareOptionsMenu\(android.view.Menu\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html))` **This function is deprecated.** `[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onPrimaryNavigationFragmentChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPrimaryNavigationFragmentChanged\(boolean\))(  
isPrimaryNavigationFragment: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)  
)` Callback for when the primary navigation state of this Fragment has changed.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))~~(  
requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>,  
grantResults: [IntArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int-array/index.html)<[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)>  
)` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onResume](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume\(\))()` Called when the fragment is visible to the user and actively running.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onSaveInstanceState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onSaveInstanceState\(android.os.Bundle\))(outState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html))` Called to ask the fragment to save its current dynamic state, so it can later be reconstructed in a new instance if its process is restarted.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onStart](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStart\(\))()` Called when the Fragment is visible to the user.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onStop](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStop\(\))()` Called when the Fragment is no longer started.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))(view: [View](https://developer.android.com/reference/android/view/View.html), savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Called immediately after `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` has returned, but before any saved state has been restored in to the view.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
@[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
[onViewStateRestored](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewStateRestored\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Called when all saved state has been restored into the view hierarchy of the fragment.  
`[Context](https://developer.android.com/reference/android/content/Context.html)?` |  `[peekAvailableContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#peekAvailableContext\(\))()` Get the `[Context](https://developer.android.com/reference/android/content/Context.html)` if it is currently available.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(\))()` Postpone the entering Fragment transition until `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))` or `[executePendingTransactions](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#executePendingTransactions\(\))` has been called.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(long,java.util.concurrent.TimeUnit\))(duration: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), timeUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html))` Postpone the entering Fragment transition for a given amount of time and then call `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))`.  
`[ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher)<I!>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<I, O> [registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))(  
contract: [ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)<I!, O!>,  
callback: [ActivityResultCallback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback)<O!>  
)` Register a request to `[start an activity for result](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int\))`, designated by the given `[contract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.  
`[ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher)<I!>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<I, O> [registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultRegistry,androidx.activity.result.ActivityResultCallback<O>\))(  
contract: [ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)<I!, O!>,  
registry: [ActivityResultRegistry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry),  
callback: [ActivityResultCallback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback)<O!>  
)` Register a request to `[start an activity for result](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int\))`, designated by the given `[contract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[registerForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForContextMenu\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View.html))` Registers a context menu to be shown for the given view (multiple views can show the context menu).  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[removeOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#removeOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))(listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener))` Remove a `[OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` previously added via `[addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))~~(permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)` |  `[requireActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireActivity\(\))()` Return the `[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)` this fragment is currently associated with.  
`[Bundle](https://developer.android.com/reference/android/os/Bundle.html)` |  `[requireArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireArguments\(\))()` Return the arguments supplied when the fragment was instantiated.  
`[Context](https://developer.android.com/reference/android/content/Context.html)` |  `[requireContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireContext\(\))()` Return the `[Context](https://developer.android.com/reference/android/content/Context.html)` this fragment is currently associated with.  
`[FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)` |  `~~[requireFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireFragmentManager\(\))~~()` **This function is deprecated.** This has been renamed to `getParentFragmentManager()` to make it clear that you are accessing the FragmentManager that contains this Fragment and not the FragmentManager associated with child Fragments.  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)` |  `[requireHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireHost\(\))()` Return the host object of this fragment.  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` |  `[requireParentFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireParentFragment\(\))()` Returns the parent Fragment containing this Fragment.  
`[View](https://developer.android.com/reference/android/view/View.html)` |  `[requireView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireView\(\))()` Get the root view for the fragment's layout (the one returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`).  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setAllowEnterTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setAllowEnterTransitionOverlap\(boolean\))(allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Sets whether the the exit transition and enter transition overlap or not.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setAllowReturnTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setAllowReturnTransitionOverlap\(boolean\))(allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Sets whether the the return transition and reenter transition overlap or not.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))(args: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Supply the construction arguments for this fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setEnterSharedElementCallback](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setEnterSharedElementCallback\(androidx.core.app.SharedElementCallback\))(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?)` When custom transitions are used with Fragments, the enter transition callback is called when this Fragment is attached or detached when not popping the back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setEnterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used to move Views into the initial scene.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setExitSharedElementCallback](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setExitSharedElementCallback\(androidx.core.app.SharedElementCallback\))(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?)` When custom transitions are used with Fragments, the exit transition callback is called when this Fragment is attached or detached when popping the back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setExitTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[setHasOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setHasOptionsMenu\(boolean\))~~(hasMenu: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** This method is no longer needed when using a `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` to provide a `[Menu](https://developer.android.com/reference/android/view/Menu.html)` to your activity, which replaces `[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` as the recommended way to provide a consistent, optionally `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)`-aware, and modular way to handle menu creation and item selection.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setInitialSavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setInitialSavedState\(androidx.fragment.app.Fragment.SavedState\))(state: [Fragment.SavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.SavedState)?)` Set the initial saved state that this Fragment should restore itself from when first being constructed, as returned by `[FragmentManager.saveFragmentInstanceState](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#saveFragmentInstanceState\(androidx.fragment.app.Fragment\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setMenuVisibility](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setMenuVisibility\(boolean\))(menuVisible: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` Set a hint for whether this fragment's menu should be visible.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setReenterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setReenterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used to move Views in to the scene when returning due to popping a back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[setRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setRetainInstance\(boolean\))~~(retain: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** Instead of retaining the Fragment itself, use a non-retained Fragment and keep retained state in a ViewModel attached to that Fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setReturnTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementEnterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used for shared elements transferred into the content Scene.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[setSharedElementReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementReturnTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?)` Sets the Transition that will be used for shared elements transferred back during a pop of the back stack.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[setTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setTargetFragment\(androidx.fragment.app.Fragment,int\))~~(fragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` **This function is deprecated.** Instead of using a target fragment to pass results, the fragment requesting a result should use `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))` to register a `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` with a ` requestKey` using its `[parent fragment manager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[setUserVisibleHint](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setUserVisibleHint\(boolean\))~~(isVisibleToUser: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))` **This function is deprecated.** If you are manually calling this method, use `[setMaxLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setMaxLifecycle\(androidx.fragment.app.Fragment,androidx.lifecycle.Lifecycle.State\))` instead.  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `[shouldShowRequestPermissionRationale](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#shouldShowRequestPermissionRationale\(java.lang.String\))(permission: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))` Gets whether you should show UI with rationale before requesting a permission.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[startActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivity\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html))` Call `[startActivity](https://developer.android.com/reference/android/app/Activity.html#startActivity\(android.content.Intent\))` from the fragment's containing Activity.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[startActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivity\(android.content.Intent,android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` Call `[startActivity](https://developer.android.com/reference/android/app/Activity.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` from the fragment's containing Activity.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[startActivityForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivityForResult\(android.content.Intent,int\))~~(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[startActivityForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivityForResult\(android.content.Intent,int,android.os.Bundle\))~~(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?)` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `~~[startIntentSenderForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startIntentSenderForResult\(android.content.IntentSender,int,android.content.Intent,int,int,int,android.os.Bundle\))~~(  
intent: [IntentSender](https://developer.android.com/reference/android/content/IntentSender.html),  
requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
fillInIntent: [Intent](https://developer.android.com/reference/android/content/Intent.html)?,  
flagsMask: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
flagsValues: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
extraFlags: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
)` **This function is deprecated.** This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))()` Begin postponed transitions after `[postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(\))` was called.  
`[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  `[toString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#toString\(\))()`  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[unregisterForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#unregisterForContextMenu\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View.html))` Prevents a context menu to be shown for the given view.  
  
### Extension functions  
  
---  
`[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[registerForAuthenticationResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(androidx.biometric.AuthenticationResultCallback\))(  
resultCallback: [AuthenticationResultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback)  
)` Returns an `[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` that can be used to initiate authentication.  
`[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[registerForAuthenticationResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(java.util.concurrent.Executor,androidx.biometric.AuthenticationResultCallback\))(  
callbackExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html),  
resultCallback: [AuthenticationResultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback)  
)` Returns an `[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` that can be used to initiate authentication.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[clearFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).clearFragmentResult\(kotlin.String\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))` Clears the stored result for the given requestKey.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[clearFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).clearFragmentResultListener\(kotlin.String\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))` Clears the stored `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` for the given requestKey.  
`[ComposeView](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[content](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).content\(kotlin.Function0\))(content: @[Composable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable) () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html))` Wrapper function that handles the setup for creating a custom Fragment that hosts Compose content.  
`[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[findNavController](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).findNavController\(\))()` Find a `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` given a `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)`  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), result: [Bundle](https://developer.android.com/reference/android/os/Bundle.html))` Sets the given result for the `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))`.  
`[Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))(  
requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
listener: (requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), bundle: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)  
)` Sets the `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` for a given `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))`.  
`inline [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)<Args>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<Args : [NavArgs](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgs)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navArgs](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navArgs\(\))()` Returns a `[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)` delegate to access the Fragment's arguments as an `[Args](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.fragment.app.Fragment\).navArgs\(\))` instance.  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[activityViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\))(  
noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))?,  
noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))?  
)` Returns a property delegate to access parent activity's `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`, if `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\))` is specified then `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` returned by it will be used to create `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` first time.  
`[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[createViewModelLazy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).createViewModelLazy\(kotlin.reflect.KClass,kotlin.Function0,kotlin.Function0,kotlin.Function0\))(  
viewModelClass: [KClass](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/index.html)<VM>,  
storeProducer: () -> [ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore),  
extrasProducer: () -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras),  
factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))?  
)` Helper method for creation of `[ViewModelLazy](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelLazy)`, that resolves `null` passed as `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).createViewModelLazy\(kotlin.reflect.KClass,kotlin.Function0,kotlin.Function0,kotlin.Function0\))` to the default factory.  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[viewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).viewModels\(kotlin.Function0,kotlin.Function0,kotlin.Function0\))(  
noinline ownerProducer: () -> [ViewModelStoreOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner),  
noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))?,  
noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))?  
)` Returns a property delegate to access `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` by **default** scoped to this `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)`:  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[hiltNavGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).hiltNavGraphViewModels\(kotlin.Int\))(navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))` Returns a property delegate to access a [HiltViewModel](https://dagger.dev/api/latest/dagger/hilt/android/lifecycle/HiltViewModel) -annotated `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel), VMF : [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[hiltNavGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).hiltNavGraphViewModels\(kotlin.Int,kotlin.Function1\))(  
navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
noinline creationCallback: (VMF) -> VM  
)` Returns a property delegate to access a [HiltViewModel](https://dagger.dev/api/latest/dagger/hilt/android/lifecycle/HiltViewModel) -annotated `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` with an @AssistedInject-annotated constructor that is scoped to a navigation graph present on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))(  
navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))?,  
noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))?  
)` Returns a property delegate to access a `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:  
`inline [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>` |  `@[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
<VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.String,kotlin.Function0,kotlin.Function0\))(  
navGraphRoute: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))?,  
noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))?  
)` Returns a property delegate to access a `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:  
  
## Public constructors

### Fragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(\))()

Constructor used by the default `[FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory)`. You must `[set a custom FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentFactory\(androidx.fragment.app.FragmentFactory\))` if you want to use a non-default constructor to ensure that your constructor is called when the fragment is re-instantiated. 

It is strongly recommended to supply arguments with `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` and later retrieved by the Fragment with `[getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))`. These arguments are automatically saved and restored alongside the Fragment. 

Applications should generally not implement a constructor. Prefer `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))` instead. It is the first place application code can run where the fragment is ready to be used - the point where the fragment is actually associated with its context. Some applications may also want to implement `[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.content.Context,android.util.AttributeSet,android.os.Bundle\))` to retrieve attributes from a layout resource, although note this happens when the fragment is attached.

### Fragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[ContentView](https://developer.android.com/reference/kotlin/androidx/annotation/ContentView)  
    [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(int\))(contentLayoutId: @[LayoutRes](https://developer.android.com/reference/kotlin/androidx/annotation/LayoutRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html))

Alternate constructor that can be called from your default, no argument constructor to provide a default layout that will be inflated by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`. 
    
    
    class MyFragment extends Fragment {
      public MyFragment() {
        super(R.layout.fragment_main);
      }
    }

You must `[set a custom FragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentFactory\(androidx.fragment.app.FragmentFactory\))` if you want to use a non-default constructor to ensure that your constructor is called when the fragment is re-instantiated. 

See also  
---  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(\))` |   
`[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` |   
  
## Public functions

### addOnContextAvailableListener

Added in [1.9.1](https://developer.android.com/jetpack/androidx/releases/fragment#1.9.1)
    
    
    fun [addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))(listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Add a new `[OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` for receiving a callback for when this class is associated with a `[android.content.Context](https://developer.android.com/reference/android/content/Context.html)`.

Listeners are triggered in the order they are added when added before the Context is available. Listeners added after the context has been made available will have the Context synchronously delivered to them as part of this call.

Parameters  
---  
`listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` |  The listener that should be added.  
  
See also  
---  
`[removeOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware#removeOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))` |   
  
### dump

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [dump](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#dump\(java.lang.String,java.io.FileDescriptor,java.io.PrintWriter,java.lang.String\[\]\))(  
        prefix: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
        fd: [FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor.html)?,  
        writer: [PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html),  
        args: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>?  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Print the Fragments's state into the given stream.

Parameters  
---  
`prefix: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  Text to print at the front of each line.  
`fd: [FileDescriptor](https://developer.android.com/reference/java/io/FileDescriptor.html)?` |  The raw file descriptor that the dump is being sent to.  
`writer: [PrintWriter](https://developer.android.com/reference/java/io/PrintWriter.html)` |  The PrintWriter to which you should dump your state. This will be closed for you after you return.  
`args: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>?` |  additional arguments to the dump request.  
  
### equals

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [equals](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#equals\(java.lang.Object\))(o: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Subclasses can not override equals().

### getActivity

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))(): [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)?

Return the `[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)` this fragment is currently associated with. May return `null` if the fragment is associated with a `[Context](https://developer.android.com/reference/android/content/Context.html)` instead.

See also  
---  
`[requireActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireActivity\(\))` |   
  
### getAllowEnterTransitionOverlap

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getAllowEnterTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getAllowEnterTransitionOverlap\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether the the exit transition and enter transition overlap or not. When true, the enter transition will start as soon as possible. When false, the enter transition will wait until the exit transition completes before starting.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true when the enter transition should start as soon as possible or false to when it should wait until the exiting transition completes.  
  
### getAllowReturnTransitionOverlap

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getAllowReturnTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getAllowReturnTransitionOverlap\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether the the return transition and reenter transition overlap or not. When true, the reenter transition will start as soon as possible. When false, the reenter transition will wait until the return transition completes before starting.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true to start the reenter transition when possible or false to wait until the return transition completes.  
  
### getArguments

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))(): [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?

Return the arguments supplied when the fragment was instantiated, if any.

### getChildFragmentManager

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))(): [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)

Return a private FragmentManager for placing and managing Fragments inside of this Fragment.

### getContext

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getContext\(\))(): [Context](https://developer.android.com/reference/android/content/Context.html)?

Return the `[Context](https://developer.android.com/reference/android/content/Context.html)` this fragment is currently associated with.

See also  
---  
`[requireContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireContext\(\))` |   
  
### getDefaultViewModelCreationExtras
    
    
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [getDefaultViewModelCreationExtras](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getDefaultViewModelCreationExtras\(\))(): [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)

The default `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` to pass into `[ViewModelProvider.Factory.create](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory#create\(kotlin.reflect.KClass,androidx.lifecycle.viewmodel.CreationExtras\))` when no overriding `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` are provided.

The `[Fragment's arguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))` when this is first called will be used as the defaults to any `[androidx.lifecycle.SavedStateHandle](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle)` passed to a view model created using this extra.

### getDefaultViewModelProviderFactory

Added in [1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)
    
    
    fun [getDefaultViewModelProviderFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getDefaultViewModelProviderFactory\(\))(): [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)

The default `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` to use when no custom `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` is provided to the `[ViewModelProvider](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider)`.

### getEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getEnterTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Returns the Transition that will be used to move Views into the initial scene. The entering Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as entering is governed by changing visibility from `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)` to `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)`.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  the Transition to use to move Views into the initial Scene.  
  
### getExitTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getExitTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Returns the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack. The exiting Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as exiting is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If transition is null, the views will remain unaffected.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  the Transition to use to move Views out of the Scene when the Fragment is being closed not due to popping the back stack.  
  
### getFragmentManager

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)
    
    
    fun ~~[getFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getFragmentManager\(\))~~(): [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)?

**This function is deprecated.**  


This has been removed in favor of `getParentFragmentManager()` which throws an `[IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` if the FragmentManager is null. Check if `[isAdded](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isAdded\(\))` returns `false` to determine if the FragmentManager is `null`.

Return the FragmentManager for interacting with fragments associated with this fragment's activity. Note that this will be non-null slightly before `[getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))`, during the time from when the fragment is placed in a `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction)` until it is committed and attached to its activity. 

If this Fragment is a child of another Fragment, the FragmentManager returned here will be the parent's `[getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))`.

See also  
---  
`[getParentFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))` |   
  
### getHost

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getHost\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Return the host object of this fragment. May return `null` if the fragment isn't currently being hosted.

See also  
---  
`[requireHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireHost\(\))` |   
  
### getId

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getId](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getId\(\))(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Return the identifier this fragment is known by. This is either the android:id value supplied in a layout or the container view ID supplied when adding the fragment.

### getLayoutInflater

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLayoutInflater\(\))(): [LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)

Returns the cached LayoutInflater used to inflate Views of this Fragment. If `[onGetLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onGetLayoutInflater\(android.os.Bundle\))` has not been called `[onGetLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onGetLayoutInflater\(android.os.Bundle\))` will be called with a `null` argument and that value will be cached. 

The cached LayoutInflater will be replaced immediately prior to `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` and cleared immediately after `[onDetach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDetach\(\))`.

Returns  
---  
`[LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)` |  The LayoutInflater used to inflate Views of this Fragment.  
  
### getLifecycle

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLifecycle\(\))(): [Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)

The `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)` of this owner.

Overriding this method is no longer supported and this method will be made `final` in a future version of Fragment.

### getLoaderManager

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun ~~[getLoaderManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getLoaderManager\(\))~~(): [LoaderManager](https://developer.android.com/reference/kotlin/androidx/loader/app/LoaderManager)

**This function is deprecated.**  


Use `[LoaderManager.getInstance(this)](https://developer.android.com/reference/kotlin/androidx/loader/app/LoaderManager#getInstance\(T\))`.

Return the LoaderManager for this fragment.

### getParentFragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getParentFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragment\(\))(): [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?

Returns the parent Fragment containing this Fragment. If this Fragment is attached directly to an Activity, returns null.

### getParentFragmentManager

Added in [1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)
    
    
    fun [getParentFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))(): [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)

Return the FragmentManager for interacting with fragments associated with this fragment's activity. Note that this will be available slightly before `[getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))`, during the time from when the fragment is placed in a `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction)` until it is committed and attached to its activity. 

If this Fragment is a child of another Fragment, the FragmentManager returned here will be the parent's `[getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))`.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if not associated with a transaction or host.  
  
### getReenterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getReenterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getReenterTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Returns the Transition that will be used to move Views in to the scene when returning due to popping a back stack. The entering Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as exiting is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If nothing is set, the default will be to use the same transition as `[getExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getExitTransition\(\))`.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  the Transition to use to move Views into the scene when reentering from a previously-started Activity due to popping the back stack.  
  
### getResources

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getResources](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getResources\(\))(): [Resources](https://developer.android.com/reference/android/content/res/Resources.html)

Return `requireActivity().getResources()`.

### getRetainInstance

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[getRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getRetainInstance\(\))~~(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

**This function is deprecated.**  


Instead of retaining the Fragment itself, use a non-retained Fragment and keep retained state in a ViewModel attached to that Fragment. The ViewModel's constructor and its onCleared() callback provide the signal for initial creation and final destruction of the retained state.

Returns `true` if this fragment instance's state will be retained across configuration changes, and `false` if it will not.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  whether or not this fragment instance will be retained.  
  
See also  
---  
`[setRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setRetainInstance\(boolean\))` |   
  
### getReturnTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getReturnTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Returns the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack. The exiting Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as entering is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If nothing is set, the default will be to use the same transition as `[getEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getEnterTransition\(\))`.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  the Transition to use to move Views out of the Scene when the Fragment is preparing to close due to popping the back stack.  
  
### getSavedStateRegistry

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getSavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSavedStateRegistry\(\))(): [SavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry)

The `[SavedStateRegistry](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistry)` owned by this `[SavedStateRegistryOwner](https://developer.android.com/reference/kotlin/androidx/savedstate/SavedStateRegistryOwner)`.

### getSharedElementEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSharedElementEnterTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Returns the Transition that will be used for shared elements transferred into the content Scene. Typical Transitions will affect size and location, such as `[android.transition.ChangeBounds](https://developer.android.com/reference/android/transition/ChangeBounds.html)`. A null value will cause transferred shared elements to blink to the final position.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use for shared elements transferred into the content Scene.  
  
### getSharedElementReturnTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getSharedElementReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getSharedElementReturnTransition\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Return the Transition that will be used for shared elements transferred back during a pop of the back stack. This Transition acts in the leaving Fragment. Typical Transitions will affect size and location, such as `[android.transition.ChangeBounds](https://developer.android.com/reference/android/transition/ChangeBounds.html)`. A null value will cause transferred shared elements to blink to the final position. If no value is set, the default will be to use the same value as `[setSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementEnterTransition\(java.lang.Object\))`.

Returns  
---  
`[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use for shared elements transferred out of the content Scene.  
  
### getString

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getString\(int\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Return a localized string from the application's package's default string table.

Parameters  
---  
`resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Resource id for the string  
  
### getString
    
    
    fun [getString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getString\(int,java.lang.Object...\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), formatArgs: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)!>?): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Return a localized formatted string from the application's package's default string table, substituting the format arguments as defined in `[java.util.Formatter](https://developer.android.com/reference/java/util/Formatter.html)` and `[format](https://developer.android.com/reference/java/lang/String.html#format\(java.lang.String,%20java.lang.Object...\))`.

Parameters  
---  
`resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Resource id for the format string  
`formatArgs: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)!>?` |  The format arguments that will be used for substitution.  
  
### getTag

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getTag](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTag\(\))(): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Get the tag name of the fragment, if specified.

### getTargetFragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[getTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetFragment\(\))~~(): [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?

**This function is deprecated.**  


Instead of using a target fragment to pass results, use `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResult\(java.lang.String,android.os.Bundle\))` to deliver results to `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` instances registered by other fragments via `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))`.

Return the target fragment set by `[setTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setTargetFragment\(androidx.fragment.app.Fragment,int\))`.

### getTargetRequestCode

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[getTargetRequestCode](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getTargetRequestCode\(\))~~(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

**This function is deprecated.**  


When using the target fragment replacement of `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))` and `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResult\(java.lang.String,android.os.Bundle\))`, consider using `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` to pass a `requestKey` if you need to support dynamic request keys.

Return the target request code set by `[setTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setTargetFragment\(androidx.fragment.app.Fragment,int\))`.

### getText

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getText](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getText\(int\))(resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html)

Return a localized, styled CharSequence from the application's package's default string table.

Parameters  
---  
`resId: @[StringRes](https://developer.android.com/reference/kotlin/androidx/annotation/StringRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Resource id for the CharSequence text  
  
### getUserVisibleHint

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun ~~[getUserVisibleHint](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getUserVisibleHint\(\))~~(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

**This function is deprecated.**  


Use `[setMaxLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setMaxLifecycle\(androidx.fragment.app.Fragment,androidx.lifecycle.Lifecycle.State\))` instead.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  The current value of the user-visible hint on this fragment.  
  
See also  
---  
`[setUserVisibleHint](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setUserVisibleHint\(boolean\))` |   
  
### getView

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))(): [View](https://developer.android.com/reference/android/view/View.html)?

Get the root view for the fragment's layout (the one returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`), if provided.

Returns  
---  
`[View](https://developer.android.com/reference/android/view/View.html)?` |  The fragment's root view, or null if it has no layout.  
  
### getViewLifecycleOwner

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [getViewLifecycleOwner](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwner\(\))(): [LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)

Get a `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` that represents the `[Fragment's View](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))` lifecycle. In most cases, this mirrors the lifecycle of the Fragment itself, but in cases of `[detached](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#detach\(androidx.fragment.app.Fragment\))` Fragments, the lifecycle of the Fragment can be considerably longer than the lifecycle of the View itself. 

Namely, the lifecycle of the Fragment's View is: 

  1. `[created](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_CREATE)` after `[onViewStateRestored](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewStateRestored\(android.os.Bundle\))`
  2. `[started](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_START)` after `[onStart](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStart\(\))`
  3. `[resumed](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_RESUME)` after `[onResume](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume\(\))`
  4. `[paused](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_PAUSE)` before `[onPause](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPause\(\))`
  5. `[stopped](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_STOP)` before `[onStop](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStop\(\))`
  6. `[destroyed](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.Event#ON_DESTROY)` before `[onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))`

The first method where it is safe to access the view lifecycle is `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` under the condition that you must return a non-null view (an IllegalStateException will be thrown if you access the view lifecycle but don't return a non-null view). 

The view lifecycle remains valid through the call to `[onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))`, after which `[getView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))` will return null, the view lifecycle will be destroyed, and this method will throw an IllegalStateException. Consider using `[getViewLifecycleOwnerLiveData](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData\(\))` or `[runOnCommit](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#runOnCommit\(java.lang.Runnable\))` to receive a callback for when the Fragment's view lifecycle is available. 

This should only be called on the main thread. 

Overriding this method is no longer supported and this method will be made `final` in a future version of Fragment.

Returns  
---  
`[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` |  A `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` that represents the `[Fragment's View](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))` lifecycle.  
  
Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if the `[Fragment's View is null](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))`.  
  
### getViewLifecycleOwnerLiveData

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getViewLifecycleOwnerLiveData](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData\(\))(): [LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)!>

Retrieve a `[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)` which allows you to observe the `[lifecycle of the Fragment's View](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwner\(\))`. 

This will be set to the new `[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)` after `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` returns a non-null View and will set to null after `[onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))`. 

Overriding this method is no longer supported and this method will be made `final` in a future version of Fragment.

Returns  
---  
`[LiveData](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData)<[LifecycleOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner)!>` |  A LiveData that changes in sync with `[getViewLifecycleOwner](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewLifecycleOwner\(\))`.  
  
### getViewModelStore

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [getViewModelStore](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getViewModelStore\(\))(): [ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore)

Returns the `[ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore)` associated with this Fragment 

Overriding this method is no longer supported and this method will be made `final` in a future version of Fragment.

Returns  
---  
`[ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore)` |  a `ViewModelStore`  
  
Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if called before the Fragment is attached i.e., before onAttach().  
  
### hashCode

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [hashCode](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#hashCode\(\))(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Subclasses can not override hashCode().

### instantiate

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    java-static fun ~~[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#instantiate\(android.content.Context,java.lang.String\))~~(context: [Context](https://developer.android.com/reference/android/content/Context.html), fname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

**This function is deprecated.**  


Use `[getFragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#getFragmentFactory\(\))` and `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory#instantiate\(java.lang.ClassLoader,java.lang.String\))`

Like `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#instantiate\(android.content.Context,java.lang.String,android.os.Bundle\))` but with a null argument Bundle.

### instantiate

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    java-static fun ~~[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#instantiate\(android.content.Context,java.lang.String,android.os.Bundle\))~~(context: [Context](https://developer.android.com/reference/android/content/Context.html), fname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), args: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

**This function is deprecated.**  


Use `[getFragmentFactory](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#getFragmentFactory\(\))` and `[instantiate](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentFactory#instantiate\(java.lang.ClassLoader,java.lang.String\))`, manually calling `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` on the returned Fragment.

Create a new instance of a Fragment with the given class name. This is the same as calling its empty constructor, setting the `[ClassLoader](https://developer.android.com/reference/java/lang/ClassLoader.html)` on the supplied arguments, then calling `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))`.

Parameters  
---  
`context: [Context](https://developer.android.com/reference/android/content/Context.html)` |  The calling context being used to instantiate the fragment. This is currently just used to get its ClassLoader.  
`fname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  The class name of the fragment to instantiate.  
`args: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  Bundle of arguments to supply to the fragment, which it can retrieve with `[getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))`. May be null.  
  
Returns  
---  
`[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` |  Returns a new fragment instance.  
  
Throws  
---  
`[androidx.fragment.app.Fragment.InstantiationException](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.InstantiationException)` |  If there is a failure in instantiating the given fragment class. This is a runtime exception; it is not normally expected to happen.  
  
### isAdded

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isAdded](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isAdded\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the fragment is currently added to its activity.

### isDetached

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isDetached](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isDetached\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the fragment has been explicitly detached from the UI. That is, `[FragmentTransaction.detach(Fragment)](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#detach\(androidx.fragment.app.Fragment\))` has been used on it.

### isHidden

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isHidden](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isHidden\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the fragment has been hidden. This includes the case if the fragment is hidden because its parent is hidden. By default fragments are shown. You can find out about changes to this state with `[onHiddenChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onHiddenChanged\(boolean\))`. Note that the hidden state is orthogonal to other states -- that is, to be visible to the user, a fragment must be both started and not hidden.

### isInLayout

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isInLayout](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isInLayout\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the layout is included as part of an activity view hierarchy via the  tag. This will always be true when fragments are created through the  tag, _except_ in the case where an old fragment is restored from a previous state and it does not appear in the layout of the current state.

### isRemoving

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isRemoving](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isRemoving\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if this fragment is currently being removed from its activity. This is _not_ whether its activity is finishing, but rather whether it is in the process of being removed from its activity.

### isResumed

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isResumed](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isResumed\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the fragment is in the resumed state. This is true for the duration of `[onResume](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume\(\))` and `[onPause](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPause\(\))` as well.

### isStateSaved

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isStateSaved](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isStateSaved\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true if this fragment is added and its state has already been saved by its host. Any operations that would change saved state should not be performed if this method returns true, and some operations such as `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` will fail.

Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true if this fragment's state has already been saved by its host  
  
### isVisible

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [isVisible](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isVisible\(\))(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Return true if the fragment is currently visible to the user. This means it: (1) has been added, (2) has its view attached to the window, and (3) is not hidden.

### onActivityCreated

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun ~~[onActivityCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityCreated\(android.os.Bundle\))~~(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


use `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))` for code touching the view created by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` and `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` for other initialization. To get a callback specifically when a Fragment activity's `[onCreate](https://developer.android.com/reference/android/app/Activity.html#onCreate\(android.os.Bundle\))` is called, register a `[androidx.lifecycle.LifecycleObserver](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleObserver)` on the Activity's `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)` in `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))`, removing it when it receives the `[CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED)` callback.

Called when the fragment's activity has been created and this fragment's view hierarchy instantiated. It can be used to do final initialization once these pieces are in place, such as retrieving views or restoring state. It is also useful for fragments that use `[setRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setRetainInstance\(boolean\))` to retain their instance, as this callback tells the fragment when it is fully associated with the new activity instance. This is called after `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` and before `[onViewStateRestored](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewStateRestored\(android.os.Bundle\))`.

Parameters  
---  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If the fragment is being re-created from a previous saved state, this is the state.  
  
### onActivityResult

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))~~(requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), resultCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), data: [Intent](https://developer.android.com/reference/android/content/Intent.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` with the appropriate `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and handling the result in the `[callback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback#onActivityResult\(O\))`.

Receive the result from a previous call to `[startActivityForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivityForResult\(android.content.Intent,int\))`. This follows the related Activity API as described there in `[onActivityResult](https://developer.android.com/reference/android/app/Activity.html#onActivityResult\(int,%20int,%20android.content.Intent\))`.

Parameters  
---  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The integer request code originally supplied to startActivityForResult(), allowing you to identify who this result came from.  
`resultCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The integer result code returned by the child activity through its setResult().  
`data: [Intent](https://developer.android.com/reference/android/content/Intent.html)?` |  An Intent, which can return result data to the caller (various data can be attached to Intent "extras").  
  
### onAttach

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun ~~[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.app.Activity\))~~(activity: [Activity](https://developer.android.com/reference/android/app/Activity.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


See `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))`.

Called when a fragment is first attached to its activity. `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` will be called after this.

### onAttach

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))(context: [Context](https://developer.android.com/reference/android/content/Context.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when a fragment is first attached to its context. `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` will be called after this.

### onAttachFragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onAttachFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttachFragment\(androidx.fragment.app.Fragment\))~~(childFragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


The responsibility for listening for fragments being attached has been moved to FragmentManager. You can add a listener to `[getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))` the child FragmentManager} by calling `[addFragmentOnAttachListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#addFragmentOnAttachListener\(androidx.fragment.app.FragmentOnAttachListener\))` in `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))` to get callbacks when a child fragment is attached.

Called when a fragment is attached as a child of this fragment. 

This is called after the attached fragment's `onAttach` and before the attached fragment's `onCreate` if the fragment has not yet had a previous call to `onCreate`.

Parameters  
---  
`childFragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)` |  child fragment being attached  
  
### onConfigurationChanged

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onConfigurationChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onConfigurationChanged\(android.content.res.Configuration\))(newConfig: [Configuration](https://developer.android.com/reference/android/content/res/Configuration.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

### onContextItemSelected

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onContextItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onContextItemSelected\(android.view.MenuItem\))(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

This hook is called whenever an item in a context menu is selected. The default implementation simply returns false to have the normal processing happen (calling the item's Runnable or sending a message to its Handler as appropriate). You can use this method for any items for which you would like to do processing without those other facilities. 

Use `[getMenuInfo](https://developer.android.com/reference/android/view/MenuItem.html#getMenuInfo\(\))` to get extra information set by the View that added this menu item. 

Derived classes should call through to the base class for it to perform the default menu handling.

Parameters  
---  
`item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)` |  The context menu item that was selected.  
  
Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  boolean Return false to allow normal context menu processing to proceed, true to consume it here.  
  
### onCreate

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called to do initial creation of a fragment. This is called after `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.app.Activity\))` and before `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`. 

Note that this can be called while the fragment's activity is still in the process of being created. As such, you can not rely on things like the activity's content view hierarchy being initialized at this point. If you want to do work once the activity itself is created, add a `[androidx.lifecycle.LifecycleObserver](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleObserver)` on the activity's Lifecycle, removing it when it receives the `[CREATED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#CREATED)` callback. 

Any restored child fragments will be created before the base `Fragment.onCreate` method returns.

Parameters  
---  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If the fragment is being re-created from a previous saved state, this is the state.  
  
### onCreateAnimation

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onCreateAnimation](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateAnimation\(int,boolean,int\))(transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Animation](https://developer.android.com/reference/android/view/animation/Animation.html)?

Called when a fragment loads an animation. Note that if `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int\))` was called with `[Animator](https://developer.android.com/reference/android/animation/Animator.html)` resources instead of `[Animation](https://developer.android.com/reference/android/view/animation/Animation.html)` resources, `nextAnim` will be an animator resource.

Parameters  
---  
`transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The value set in `[setTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setTransition\(int\))` or 0 if not set.  
`enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `true` when the fragment is added/attached/shown or `false` when the fragment is removed/detached/hidden.  
`nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The resource set in `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int\))`, `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int,int,int\))`, or 0 if neither was called. The value will depend on the current operation.  
  
### onCreateAnimator

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onCreateAnimator](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateAnimator\(int,boolean,int\))(transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Animator](https://developer.android.com/reference/android/animation/Animator.html)?

Called when a fragment loads an animator. This will be called when `[onCreateAnimation](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateAnimation\(int,boolean,int\))` returns null. Note that if `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int\))` was called with `[Animation](https://developer.android.com/reference/android/view/animation/Animation.html)` resources instead of `[Animator](https://developer.android.com/reference/android/animation/Animator.html)` resources, `nextAnim` will be an animation resource.

Parameters  
---  
`transit: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The value set in `[setTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setTransition\(int\))` or 0 if not set.  
`enter: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `true` when the fragment is added/attached/shown or `false` when the fragment is removed/detached/hidden.  
`nextAnim: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The resource set in `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int\))`, `[setCustomAnimations](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setCustomAnimations\(int,int,int,int\))`, or 0 if neither was called. The value will depend on the current operation.  
  
### onCreateContextMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onCreateContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateContextMenu\(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo\))(  
        menu: [ContextMenu](https://developer.android.com/reference/android/view/ContextMenu.html),  
        v: [View](https://developer.android.com/reference/android/view/View.html),  
        menuInfo: [ContextMenu.ContextMenuInfo](https://developer.android.com/reference/android/view/ContextMenu.ContextMenuInfo.html)?  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when a context menu for the `view` is about to be shown. Unlike `[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))`, this will be called every time the context menu is about to be shown and should be populated for the view (or item inside the view for `[AdapterView](https://developer.android.com/reference/android/widget/AdapterView.html)` subclasses, this can be found in the `menuInfo`)). 

Use `[onContextItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onContextItemSelected\(android.view.MenuItem\))` to know when an item has been selected. 

The default implementation calls up to `[Activity.onCreateContextMenu](https://developer.android.com/reference/android/app/Activity.html#onCreateContextMenu\(android.view.ContextMenu,%20android.view.View,%20android.view.ContextMenu.ContextMenuInfo\))`, though you can not call this implementation if you don't want that behavior. 

It is not safe to hold onto the context menu after this method returns.

### onCreateOptionsMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html), inflater: [MenuInflater](https://developer.android.com/reference/android/view/MenuInflater.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


`[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override. As this provides a consistent, optionally `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)`-aware, and modular way to handle menu creation and item selection, replace usages of this method with one or more calls to `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity#addMenuProvider\(androidx.core.view.MenuProvider\))` in your Activity's `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` method, having each provider override `[onCreateMenu](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider#onCreateMenu\(android.view.Menu,android.view.MenuInflater\))` to create their menu items.

Initialize the contents of the Fragment host's standard options menu. You should place your menu items in to menu. For this method to be called, you must have first called `[setHasOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setHasOptionsMenu\(boolean\))`. See `[Activity.onCreateOptionsMenu](https://developer.android.com/reference/android/app/Activity.html#onCreateOptionsMenu\(android.view.Menu\))` for more information.

Parameters  
---  
`menu: [Menu](https://developer.android.com/reference/android/view/Menu.html)` |  The options menu in which you place your items.  
  
See also  
---  
`[setHasOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setHasOptionsMenu\(boolean\))` |   
`[onPrepareOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPrepareOptionsMenu\(android.view.Menu\))` |   
`[onOptionsItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onOptionsItemSelected\(android.view.MenuItem\))` |   
  
### onCreateView

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))(  
        inflater: [LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html),  
        container: [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)?,  
        savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
    ): [View](https://developer.android.com/reference/android/view/View.html)?

Called to have the fragment instantiate its user interface view. This is optional, and non-graphical fragments can return null. This will be called between `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` and `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))`. 

A default View can be returned by calling `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#Fragment\(int\))` in your constructor. Otherwise, this method returns null. 

It is recommended to **only** inflate the layout in this method and move logic that operates on the returned View to `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))`. 

If you return a View from here, you will later be called in `[onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))` when the view is being released.

Parameters  
---  
`inflater: [LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)` |  The LayoutInflater object that can be used to inflate any views in the fragment,  
`container: [ViewGroup](https://developer.android.com/reference/android/view/ViewGroup.html)?` |  If non-null, this is the parent view that the fragment's UI should be attached to. The fragment should not add the view itself, but this can be used to generate the LayoutParams of the view.  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If non-null, this fragment is being re-constructed from a previous saved state as given here.  
  
Returns  
---  
`[View](https://developer.android.com/reference/android/view/View.html)?` |  Return the View for the fragment's UI, or null.  
  
### onDestroy

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the fragment is no longer in use. This is called after `[onStop](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStop\(\))` and before `[onDetach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDetach\(\))`.

### onDestroyOptionsMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onDestroyOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyOptionsMenu\(\))~~(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


`[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override. Each `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` then provides a consistent, optionally `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)`-aware, and modular way to handle menu item selection for the menu items created by that provider. Replace usages of this method with one or more calls to `[removeMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#removeMenuProvider\(androidx.core.view.MenuProvider\))` in your Activity's `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` method, whenever it is necessary to remove the individual `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)`. If a `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` was added with Lifecycle-awareness, this removal will happen automatically.

Called when this fragment's option menu items are no longer being included in the overall options menu. Receiving this call means that the menu needed to be rebuilt, but this fragment's items were not included in the newly built menu (its `[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` was not called).

### onDestroyView

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onDestroyView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroyView\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the view previously created by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` has been detached from the fragment. The next time the fragment needs to be displayed, a new view will be created. This is called after `[onStop](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStop\(\))` and before `[onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))`. It is called _regardless_ of whether `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` returned a non-null view. Internally it is called after the view's state has been saved but before it has been removed from its parent.

### onDetach

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onDetach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDetach\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the fragment is no longer attached to its activity. This is called after `[onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))`.

### onGetLayoutInflater

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [onGetLayoutInflater](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onGetLayoutInflater\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)

Returns the LayoutInflater used to inflate Views of this Fragment. The default implementation will throw an exception if the Fragment is not attached.

Parameters  
---  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If the fragment is being re-created from a previous saved state, this is the state.  
  
Returns  
---  
`[LayoutInflater](https://developer.android.com/reference/android/view/LayoutInflater.html)` |  The LayoutInflater used to inflate Views of this Fragment.  
  
### onHiddenChanged

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onHiddenChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onHiddenChanged\(boolean\))(hidden: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the hidden state (as returned by `[isHidden](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isHidden\(\))` of the fragment or another fragment in its hierarchy has changed. Fragments start out not hidden; this will be called whenever the fragment changes state from that.

Parameters  
---  
`hidden: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  True if the fragment is now hidden, false otherwise.  
  
### onInflate

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[UiThread](https://developer.android.com/reference/kotlin/androidx/annotation/UiThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun ~~[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.app.Activity,android.util.AttributeSet,android.os.Bundle\))~~(  
        activity: [Activity](https://developer.android.com/reference/android/app/Activity.html),  
        attrs: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet.html),  
        savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


See `[onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.content.Context,android.util.AttributeSet,android.os.Bundle\))`.

Called when a fragment is being created as part of a view layout inflation, typically from setting the content view of an activity.

### onInflate

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[UiThread](https://developer.android.com/reference/kotlin/androidx/annotation/UiThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onInflate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onInflate\(android.content.Context,android.util.AttributeSet,android.os.Bundle\))(  
        context: [Context](https://developer.android.com/reference/android/content/Context.html),  
        attrs: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet.html),  
        savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when a fragment is being created as part of a view layout inflation, typically from setting the content view of an activity. This may be called immediately after the fragment is created from a `[FragmentContainerView](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentContainerView)` in a layout file. Note this is _before_ the fragment's `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))` has been called; all you should do here is parse the attributes and save them away. 

This is called _the first time_ the fragment is inflated. If it is being inflated into a new instance with saved state, this method will not be called a second time for the restored state fragment.

Here is a typical implementation of a fragment that can take parameters both through attributes supplied here as well from `[getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))`:
    
    
    public static class MyFragment extends Fragment {
        CharSequence mLabel;
    
        /**
         * Create a new instance of MyFragment that will be initialized
         * with the given arguments.
         */
        static MyFragment newInstance(CharSequence label) {
            MyFragment f = new MyFragment();
            Bundle b = new Bundle();
            b.putCharSequence("label", label);
            f.setArguments(b);
            return f;
        }
    
        /**
         * Parse attributes during inflation from a view hierarchy into the
         * arguments we handle.
         */
        @Override
        public void onInflate(@NonNull Context context, @NonNull AttributeSet attrs,
                @Nullable Bundle savedInstanceState) {
            super.onInflate(context, attrs, savedInstanceState);
    
            TypedArray a = context.obtainStyledAttributes(attrs,
                    R.styleable.FragmentArguments);
            mLabel = a.getText(R.styleable.FragmentArguments_android_label);
            a.recycle();
        }
    
        /**
         * During creation, if arguments have been supplied to the fragment
         * then parse those out.
         */
        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
    
            Bundle args = getArguments();
            if (args != null) {
                CharSequence label = args.getCharSequence("label");
                if (label != null) {
                    mLabel = label;
                }
            }
        }
    
        /**
         * Create the view for this fragment, using the arguments given to it.
         */
        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            View v = inflater.inflate(R.layout.hello_world, container, false);
            View tv = v.findViewById(R.id.text);
            ((TextView)tv).setText(mLabel != null ? mLabel : "(no label)");
            ViewCompat.setBackground(
                    tv, ContextCompat.getDrawable(getContext(), android.R.drawable.gallery_thumb));
            return v;
        }
    }

Note that parsing the XML attributes uses a "styleable" resource. The declaration for the styleable used here is:
    
    
    <declare-styleable name="FragmentArguments">
        <attr name="android:label" />
    </declare-styleable>

The fragment can then be declared within its activity's content layout through a tag like this:
    
    
    <androidx.fragment.app.FragmentContainerView
            class="com.example.android.supportv4.app.FragmentArgumentsSupport$MyFragment"
            android:id="@+id/embedded"
            android:layout_width="0px" android:layout_height="wrap_content"
            android:layout_weight="1"
            android:label="@string/fragment_arguments_embedded" />

This fragment can also be created dynamically from arguments given at runtime in the arguments Bundle; here is an example of doing so at creation of the containing activity:
    
    
    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fragment_arguments_support);
    
        if (savedInstanceState == null) {
            // First-time init; create fragment to embed in activity.
            FragmentTransaction ft = getSupportFragmentManager().beginTransaction();
            Fragment newFragment = MyFragment.newInstance("From Arguments");
            ft.add(R.id.created, newFragment);
            ft.commit();
        }
    }

Parameters  
---  
`context: [Context](https://developer.android.com/reference/android/content/Context.html)` |  The Activity that is inflating this fragment.  
`attrs: [AttributeSet](https://developer.android.com/reference/android/util/AttributeSet.html)` |  The attributes at the tag where the fragment is being created.  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If the fragment is being re-created from a previous saved state, this is the state.  
  
### onLowMemory

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onLowMemory](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onLowMemory\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


### onMultiWindowModeChanged

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [onMultiWindowModeChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onMultiWindowModeChanged\(boolean\))(isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the Fragment's activity changes from fullscreen mode to multi-window mode and visa-versa. This is generally tied to `[onMultiWindowModeChanged](https://developer.android.com/reference/android/app/Activity.html#onMultiWindowModeChanged\(boolean\))` of the containing Activity.

Parameters  
---  
`isInMultiWindowMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  True if the activity is in multi-window mode.  
  
### onOptionsItemSelected

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onOptionsItemSelected](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onOptionsItemSelected\(android.view.MenuItem\))~~(item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

**This function is deprecated.**  


`[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override. Each `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` then provides a consistent, optionally `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)`-aware, and modular way to handle menu item selection for the menu items created by that provider. Replace usages of this method with one or more calls to `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` in your Activity's `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` method, delegating menu item selection to the individual `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` that created the menu items you wish to handle.

This hook is called whenever an item in your options menu is selected. The default implementation simply returns false to have the normal processing happen (calling the item's Runnable or sending a message to its Handler as appropriate). You can use this method for any items for which you would like to do processing without those other facilities. 

Derived classes should call through to the base class for it to perform the default menu handling.

Parameters  
---  
`item: [MenuItem](https://developer.android.com/reference/android/view/MenuItem.html)` |  The menu item that was selected.  
  
Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  boolean Return false to allow normal menu processing to proceed, true to consume it here.  
  
See also  
---  
`[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` |   
  
### onOptionsMenuClosed

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onOptionsMenuClosed](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onOptionsMenuClosed\(android.view.Menu\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


`[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override. The `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` interface uses a single `[onCreateMenu](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider#onCreateMenu\(android.view.Menu,android.view.MenuInflater\))` method for managing both the creation and preparation of menu items. Replace usages of this method with one or more calls to `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` in your Activity's `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` method, overriding `[onMenuClosed](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider#onMenuClosed\(android.view.Menu\))` to delegate menu closing to the individual `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` that created the menu.

This hook is called whenever the options menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).

Parameters  
---  
`menu: [Menu](https://developer.android.com/reference/android/view/Menu.html)` |  The options menu as last shown or first initialized by onCreateOptionsMenu().  
  
### onPause

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onPause](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPause\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the Fragment is no longer resumed. This is generally tied to `[Activity.onPause](https://developer.android.com/reference/android/app/Activity.html#onPause\(\))` of the containing Activity's lifecycle.

### onPictureInPictureModeChanged

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [onPictureInPictureModeChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPictureInPictureModeChanged\(boolean\))(isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called by the system when the activity changes to and from picture-in-picture mode. This is generally tied to `[onPictureInPictureModeChanged](https://developer.android.com/reference/android/app/Activity.html#onPictureInPictureModeChanged\(boolean\))` of the containing Activity.

Parameters  
---  
`isInPictureInPictureMode: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  True if the activity is in picture-in-picture mode.  
  
### onPrepareOptionsMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun ~~[onPrepareOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPrepareOptionsMenu\(android.view.Menu\))~~(menu: [Menu](https://developer.android.com/reference/android/view/Menu.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


`[androidx.activity.ComponentActivity](https://developer.android.com/reference/kotlin/androidx/activity/ComponentActivity)` now implements `[MenuHost](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost)`, an interface that allows any component, including your activity itself, to add menu items by calling `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` without forcing all components through this single method override. The `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` interface uses a single `[onCreateMenu](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider#onCreateMenu\(android.view.Menu,android.view.MenuInflater\))` method for managing both the creation and preparation of menu items. Replace usages of this method with one or more calls to `[addMenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuHost#addMenuProvider\(androidx.core.view.MenuProvider\))` in your Activity's `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` method, moving any preparation of menu items to `[onPrepareMenu](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider#onPrepareMenu\(android.view.Menu\))`.

Prepare the Fragment host's standard options menu to be displayed. This is called right before the menu is shown, every time it is shown. You can use this method to efficiently enable/disable items or otherwise dynamically modify the contents. See `[Activity.onPrepareOptionsMenu](https://developer.android.com/reference/android/app/Activity.html#onPrepareOptionsMenu\(android.view.Menu\))` for more information.

Parameters  
---  
`menu: [Menu](https://developer.android.com/reference/android/view/Menu.html)` |  The options menu as last shown or first initialized by onCreateOptionsMenu().  
  
See also  
---  
`[setHasOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setHasOptionsMenu\(boolean\))` |   
`[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` |   
  
### onPrimaryNavigationFragmentChanged

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onPrimaryNavigationFragmentChanged](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPrimaryNavigationFragmentChanged\(boolean\))(  
        isPrimaryNavigationFragment: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Callback for when the primary navigation state of this Fragment has changed. This can be the result of the `[getParentFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))` containing FragmentManager} having its primary navigation fragment changed via `[setPrimaryNavigationFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setPrimaryNavigationFragment\(androidx.fragment.app.Fragment\))` or due to the primary navigation fragment changing in a parent FragmentManager.

Parameters  
---  
`isPrimaryNavigationFragment: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  True if and only if this Fragment and any `[parent fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragment\(\))` is set as the primary navigation fragment via `[setPrimaryNavigationFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setPrimaryNavigationFragment\(androidx.fragment.app.Fragment\))`.  
  
### onRequestPermissionsResult

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))~~(  
        requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>,  
        grantResults: [IntArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int-array/index.html)<[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)>  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` passing in a `[RequestMultiplePermissions](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.RequestMultiplePermissions)` object for the `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and handling the result in the `[callback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback#onActivityResult\(O\))`.

Callback for the result from requesting permissions. This method is invoked for every call on `[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))`. 

**Note:** It is possible that the permissions request interaction with the user is interrupted. In this case you will receive empty permissions and results arrays which should be treated as a cancellation. 

Parameters  
---  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The request code passed in `[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))`.  
`permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>` |  The requested permissions. Never null.  
`grantResults: [IntArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int-array/index.html)<[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)>` |  The grant results for the corresponding permissions which is either `[PERMISSION_GRANTED](https://developer.android.com/reference/android/content/pm/PackageManager.html#PERMISSION_GRANTED)` or `[PERMISSION_DENIED](https://developer.android.com/reference/android/content/pm/PackageManager.html#PERMISSION_DENIED)`. Never null.  
  
See also  
---  
`[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))` |   
  
### onResume

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onResume](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the fragment is visible to the user and actively running. This is generally tied to `[Activity.onResume](https://developer.android.com/reference/android/app/Activity.html#onResume\(\))` of the containing Activity's lifecycle.

### onSaveInstanceState

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onSaveInstanceState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onSaveInstanceState\(android.os.Bundle\))(outState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called to ask the fragment to save its current dynamic state, so it can later be reconstructed in a new instance if its process is restarted. If a new instance of the fragment later needs to be created, the data you place in the Bundle here will be available in the Bundle given to `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))`, `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`, and `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))`. 

This corresponds to `[Activity.onSaveInstanceState(Bundle)](https://developer.android.com/reference/android/app/Activity.html#onSaveInstanceState\(android.os.Bundle\))` and most of the discussion there applies here as well. Note however: _this method may be called at any time before`[onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))`_. There are many situations where a fragment may be mostly torn down (such as when placed on the back stack with no UI showing), but its state will not be saved until its owning activity actually needs to save its state.

Parameters  
---  
`outState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)` |  Bundle in which to place your saved state.  
  
### onStart

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onStart](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStart\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the Fragment is visible to the user. This is generally tied to `[Activity.onStart](https://developer.android.com/reference/android/app/Activity.html#onStart\(\))` of the containing Activity's lifecycle.

### onStop

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onStop](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStop\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when the Fragment is no longer started. This is generally tied to `[Activity.onStop](https://developer.android.com/reference/android/app/Activity.html#onStop\(\))` of the containing Activity's lifecycle.

### onViewCreated

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun [onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))(view: [View](https://developer.android.com/reference/android/view/View.html), savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called immediately after `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` has returned, but before any saved state has been restored in to the view. This gives subclasses a chance to initialize themselves once they know their view hierarchy has been completely created. The fragment's view hierarchy is not however attached to its parent at this point.

Parameters  
---  
`view: [View](https://developer.android.com/reference/android/view/View.html)` |  The View returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`.  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If non-null, this fragment is being re-constructed from a previous saved state as given here.  
  
### onViewStateRestored

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    @[CallSuper](https://developer.android.com/reference/kotlin/androidx/annotation/CallSuper)  
    fun [onViewStateRestored](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewStateRestored\(android.os.Bundle\))(savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Called when all saved state has been restored into the view hierarchy of the fragment. This can be used to do initialization based on saved state that you are letting the view hierarchy track itself, such as whether check box widgets are currently checked. This is called after `[onViewCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onViewCreated\(android.view.View,android.os.Bundle\))` and before `[onStart](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onStart\(\))`.

Parameters  
---  
`savedInstanceState: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  If the fragment is being re-created from a previous saved state, this is the state.  
  
### peekAvailableContext

Added in [1.9.1](https://developer.android.com/jetpack/androidx/releases/fragment#1.9.1)
    
    
    fun [peekAvailableContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#peekAvailableContext\(\))(): [Context](https://developer.android.com/reference/android/content/Context.html)?

Get the `[Context](https://developer.android.com/reference/android/content/Context.html)` if it is currently available. If this returns `null`, you can use `[addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))` to receive a callback for when it available.

Returns  
---  
`[Context](https://developer.android.com/reference/android/content/Context.html)?` |  the Context if it is currently available.  
  
### postponeEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Postpone the entering Fragment transition until `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))` or `[executePendingTransactions](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#executePendingTransactions\(\))` has been called. 

This method gives the Fragment the ability to delay Fragment animations until all data is loaded. Until then, the added, shown, and attached Fragments will be INVISIBLE and removed, hidden, and detached Fragments won't be have their Views removed. The transaction runs when all postponed added Fragments in the transaction have called `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))`. 

This method should be called before being added to the FragmentTransaction or in `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))`, `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))`, or `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`}. `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))` must be called to allow the Fragment to start the transitions. 

When a FragmentTransaction is started that may affect a postponed FragmentTransaction, based on which containers are in their operations, the postponed FragmentTransaction will have its start triggered. The early triggering may result in faulty or nonexistent animations in the postponed transaction. FragmentTransactions that operate only on independent containers will not interfere with each other's postponement. 

Calling postponeEnterTransition on Fragments with a null View will not postpone the transition.

See also  
---  
`[postponeEnterTransition](https://developer.android.com/reference/android/app/Activity.html#postponeEnterTransition\(\))` |   
`[setReorderingAllowed](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setReorderingAllowed\(boolean\))` |   
  
### postponeEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(long,java.util.concurrent.TimeUnit\))(duration: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), timeUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Postpone the entering Fragment transition for a given amount of time and then call `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))`. 

This method gives the Fragment the ability to delay Fragment animations for a given amount of time. Until then, the added, shown, and attached Fragments will be INVISIBLE and removed, hidden, and detached Fragments won't be have their Views removed. The transaction runs when all postponed added Fragments in the transaction have called `[startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))`. 

This method should be called before being added to the FragmentTransaction or in `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))`, `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.content.Context\))`, or `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`}. 

When a FragmentTransaction is started that may affect a postponed FragmentTransaction, based on which containers are in their operations, the postponed FragmentTransaction will have its start triggered. The early triggering may result in faulty or nonexistent animations in the postponed transaction. FragmentTransactions that operate only on independent containers will not interfere with each other's postponement. 

Calling postponeEnterTransition on Fragments with a null View will not postpone the transition.

Parameters  
---  
`duration: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)` |  The length of the delay in `timeUnit` units  
`timeUnit: [TimeUnit](https://developer.android.com/reference/java/util/concurrent/TimeUnit.html)` |  The units of time for `duration`  
  
See also  
---  
`[postponeEnterTransition](https://developer.android.com/reference/android/app/Activity.html#postponeEnterTransition\(\))` |   
`[setReorderingAllowed](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setReorderingAllowed\(boolean\))` |   
  
### registerForActivityResult

Added in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun <I, O> [registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))(  
        contract: [ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)<I!, O!>,  
        callback: [ActivityResultCallback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback)<O!>  
    ): [ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher)<I!>

Register a request to `[start an activity for result](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int\))`, designated by the given `[contract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.

This creates a record in the `[registry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry)` associated with this caller, managing request code, as well as conversions to/from `[Intent](https://developer.android.com/reference/android/content/Intent.html)` under the hood.

This _must_ be called unconditionally, as part of initialization path, typically as a field initializer of an Activity or Fragment.

If the host of this fragment is an `[ActivityResultRegistryOwner](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistryOwner)` the `[ActivityResultRegistry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry)` of the host will be used. Otherwise, this will use the registry of the Fragment's Activity.

### registerForActivityResult

Added in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun <I, O> [registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultRegistry,androidx.activity.result.ActivityResultCallback<O>\))(  
        contract: [ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)<I!, O!>,  
        registry: [ActivityResultRegistry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry),  
        callback: [ActivityResultCallback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback)<O!>  
    ): [ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher)<I!>

Register a request to `[start an activity for result](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int\))`, designated by the given `[contract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.

This creates a record in the given `[registry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry)`, managing request code, as well as conversions to/from `[Intent](https://developer.android.com/reference/android/content/Intent.html)` under the hood.

This _must_ be called unconditionally, as part of initialization path, typically as a field initializer of an Activity or Fragment.

Parameters  
---  
`<I>` |  the type of the input(if any) required to call the activity  
`<O>` |  the type of output returned as an activity result  
`contract: [ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)<I!, O!>` |  the contract, specifying conversions to/from `[Intent](https://developer.android.com/reference/android/content/Intent.html)`s  
`registry: [ActivityResultRegistry](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultRegistry)` |  the registry where to hold the record.  
`callback: [ActivityResultCallback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback)<O!>` |  the callback to be called on the main thread when activity result is available  
  
Returns  
---  
`[ActivityResultLauncher](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultLauncher)<I!>` |  the launcher that can be used to start the activity or dispose of the prepared call.  
  
### registerForContextMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [registerForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForContextMenu\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Registers a context menu to be shown for the given view (multiple views can show the context menu). This method will set the `[OnCreateContextMenuListener](https://developer.android.com/reference/android/view/View.OnCreateContextMenuListener.html)` on the view to this fragment, so `[onCreateContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateContextMenu\(android.view.ContextMenu,android.view.View,android.view.ContextMenu.ContextMenuInfo\))` will be called when it is time to show the context menu.

Parameters  
---  
`view: [View](https://developer.android.com/reference/android/view/View.html)` |  The view that should show a context menu.  
  
See also  
---  
`[unregisterForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#unregisterForContextMenu\(android.view.View\))` |   
  
### removeOnContextAvailableListener

Added in [1.9.1](https://developer.android.com/jetpack/androidx/releases/fragment#1.9.1)
    
    
    fun [removeOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#removeOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))(listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Remove a `[OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` previously added via `[addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))`.

Parameters  
---  
`listener: [OnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/OnContextAvailableListener)` |  The listener that should be removed.  
  
See also  
---  
`[addOnContextAvailableListener](https://developer.android.com/reference/kotlin/androidx/activity/contextaware/ContextAware#addOnContextAvailableListener\(androidx.activity.contextaware.OnContextAvailableListener\))` |   
  
### requestPermissions

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))~~(permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` passing in a `[RequestMultiplePermissions](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.RequestMultiplePermissions)` object for the `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and handling the result in the `[callback](https://developer.android.com/reference/kotlin/androidx/activity/result/ActivityResultCallback#onActivityResult\(O\))`.

Requests permissions to be granted to this application. These permissions must be requested in your manifest, they should not be granted to your app, and they should have protection level `[#PROTECTION_DANGEROUS dangerous](https://developer.android.com/reference/android/content/pm/PermissionInfo.html)`, regardless whether they are declared by the platform or a third-party app. 

Normal permissions `[PROTECTION_NORMAL](https://developer.android.com/reference/android/content/pm/PermissionInfo.html#PROTECTION_NORMAL)` are granted at install time if requested in the manifest. Signature permissions `[PROTECTION_SIGNATURE](https://developer.android.com/reference/android/content/pm/PermissionInfo.html#PROTECTION_SIGNATURE)` are granted at install time if requested in the manifest and the signature of your app matches the signature of the app declaring the permissions. 

Call `[shouldShowRequestPermissionRationale](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#shouldShowRequestPermissionRationale\(java.lang.String\))` before calling this API to check if the system recommends to show a rationale dialog before asking for a permission. 

If your app does not have the requested permissions the user will be presented with UI for accepting them. After the user has accepted or rejected the requested permissions you will receive a callback on `[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))` reporting whether the permissions were granted or not. 

Note that requesting a permission does not guarantee it will be granted and your app should be able to run without having this permission. 

This method may start an activity allowing the user to choose which permissions to grant and which to reject. Hence, you should be prepared that your activity may be paused and resumed. Further, granting some permissions may require a restart of you application. In such a case, the system will recreate the activity stack before delivering the result to `[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))`. 

When checking whether you have a permission you should use `[checkSelfPermission](https://developer.android.com/reference/android/content/Context.html#checkSelfPermission\(java.lang.String\))`. 

Calling this API for permissions already granted to your app would show UI to the user to decide whether the app can still hold these permissions. This can be useful if the way your app uses the data guarded by the permissions changes significantly. 

Parameters  
---  
`permissions: [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)!>` |  The requested permissions.  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Application specific request code to match with a result reported to `[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))`. Must be between 0 and 65535 to be considered valid. If given requestCode is greater than 65535, an IllegalArgumentException would be thrown.  
  
See also  
---  
`[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))` |   
`[checkSelfPermission](https://developer.android.com/reference/android/content/Context.html#checkSelfPermission\(java.lang.String\))` |   
  
### requireActivity

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireActivity\(\))(): [FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)

Return the `[FragmentActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentActivity)` this fragment is currently associated with.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if not currently associated with an activity or if associated only with a context.  
  
See also  
---  
`[getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))` |   
  
### requireArguments

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireArguments\(\))(): [Bundle](https://developer.android.com/reference/android/os/Bundle.html)

Return the arguments supplied when the fragment was instantiated.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if no arguments were supplied to the Fragment.  
  
See also  
---  
`[getArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getArguments\(\))` |   
  
### requireContext

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireContext\(\))(): [Context](https://developer.android.com/reference/android/content/Context.html)

Return the `[Context](https://developer.android.com/reference/android/content/Context.html)` this fragment is currently associated with.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if not currently associated with a context.  
  
See also  
---  
`[getContext](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getContext\(\))` |   
  
### requireFragmentManager

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)
    
    
    fun ~~[requireFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireFragmentManager\(\))~~(): [FragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager)

**This function is deprecated.**  


This has been renamed to `getParentFragmentManager()` to make it clear that you are accessing the FragmentManager that contains this Fragment and not the FragmentManager associated with child Fragments.

Return the FragmentManager for interacting with fragments associated with this fragment's activity. Note that this will be available slightly before `[getActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getActivity\(\))`, during the time from when the fragment is placed in a `[FragmentTransaction](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction)` until it is committed and attached to its activity. 

If this Fragment is a child of another Fragment, the FragmentManager returned here will be the parent's `[getChildFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getChildFragmentManager\(\))`.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if not associated with a transaction or host.  
  
See also  
---  
`[getParentFragmentManager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))` |   
  
### requireHost

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireHost\(\))(): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)

Return the host object of this fragment.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if not currently associated with a host.  
  
See also  
---  
`[getHost](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getHost\(\))` |   
  
### requireParentFragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireParentFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireParentFragment\(\))(): [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)

Returns the parent Fragment containing this Fragment.

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if this Fragment is attached directly to an Activity or other Fragment host.  
  
See also  
---  
`[getParentFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragment\(\))` |   
  
### requireView

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [requireView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requireView\(\))(): [View](https://developer.android.com/reference/android/view/View.html)

Get the root view for the fragment's layout (the one returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`).

Throws  
---  
`[java.lang.IllegalStateException](https://developer.android.com/reference/java/lang/IllegalStateException.html)` |  if no view was returned by `[onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))`.  
  
See also  
---  
`[getView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getView\(\))` |   
  
### setAllowEnterTransitionOverlap

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setAllowEnterTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setAllowEnterTransitionOverlap\(boolean\))(allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets whether the the exit transition and enter transition overlap or not. When true, the enter transition will start as soon as possible. When false, the enter transition will wait until the exit transition completes before starting.

Parameters  
---  
`allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true to start the enter transition when possible or false to wait until the exiting transition completes.  
  
### setAllowReturnTransitionOverlap

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setAllowReturnTransitionOverlap](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setAllowReturnTransitionOverlap\(boolean\))(allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets whether the the return transition and reenter transition overlap or not. When true, the reenter transition will start as soon as possible. When false, the reenter transition will wait until the return transition completes before starting.

Parameters  
---  
`allow: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true to start the reenter transition when possible or false to wait until the return transition completes.  
  
### setArguments

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))(args: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Supply the construction arguments for this fragment. The arguments supplied here will be retained across fragment destroy and creation. 

This method cannot be called if the fragment is added to a FragmentManager and if `[isStateSaved](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#isStateSaved\(\))` would return true.

### setEnterSharedElementCallback

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setEnterSharedElementCallback](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setEnterSharedElementCallback\(androidx.core.app.SharedElementCallback\))(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

When custom transitions are used with Fragments, the enter transition callback is called when this Fragment is attached or detached when not popping the back stack.

Parameters  
---  
`callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?` |  Used to manipulate the shared element transitions on this Fragment when added not as a pop from the back stack.  
  
### setEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setEnterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used to move Views into the initial scene. The entering Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as entering is governed by changing visibility from `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)` to `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)`. If `transition` is null, entering Views will remain unaffected.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use to move Views into the initial Scene. `transition` must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setExitSharedElementCallback

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setExitSharedElementCallback](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setExitSharedElementCallback\(androidx.core.app.SharedElementCallback\))(callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

When custom transitions are used with Fragments, the exit transition callback is called when this Fragment is attached or detached when popping the back stack.

Parameters  
---  
`callback: [SharedElementCallback](https://developer.android.com/reference/kotlin/androidx/core/app/SharedElementCallback)?` |  Used to manipulate the shared element transitions on this Fragment when added as a pop from the back stack.  
  
### setExitTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setExitTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack. The exiting Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as exiting is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If transition is null, the views will remain unaffected.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use to move Views out of the Scene when the Fragment is being closed not due to popping the back stack. `transition`must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setHasOptionsMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.5.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0)
    
    
    fun ~~[setHasOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setHasOptionsMenu\(boolean\))~~(hasMenu: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method is no longer needed when using a `[MenuProvider](https://developer.android.com/reference/kotlin/androidx/core/view/MenuProvider)` to provide a `[Menu](https://developer.android.com/reference/android/view/Menu.html)` to your activity, which replaces `[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` as the recommended way to provide a consistent, optionally `[Lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle)`-aware, and modular way to handle menu creation and item selection.

Report that this fragment would like to participate in populating the options menu by receiving a call to `[onCreateOptionsMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateOptionsMenu\(android.view.Menu,android.view.MenuInflater\))` and related methods.

Parameters  
---  
`hasMenu: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  If true, the fragment has menu items to contribute.  
  
### setInitialSavedState

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setInitialSavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setInitialSavedState\(androidx.fragment.app.Fragment.SavedState\))(state: [Fragment.SavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.SavedState)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Set the initial saved state that this Fragment should restore itself from when first being constructed, as returned by `[FragmentManager.saveFragmentInstanceState](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#saveFragmentInstanceState\(androidx.fragment.app.Fragment\))`.

Parameters  
---  
`state: [Fragment.SavedState](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment.SavedState)?` |  The state the fragment should be restored from.  
  
### setMenuVisibility

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setMenuVisibility](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setMenuVisibility\(boolean\))(menuVisible: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Set a hint for whether this fragment's menu should be visible. This is useful if you know that a fragment has been placed in your view hierarchy so that the user can not currently seen it, so any menu items it has should also not be shown.

Parameters  
---  
`menuVisible: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  The default is true, meaning the fragment's menu will be shown as usual. If false, the user will not see the menu.  
  
### setReenterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setReenterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setReenterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used to move Views in to the scene when returning due to popping a back stack. The entering Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as exiting is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If transition is null, the views will remain unaffected. If nothing is set, the default will be to use the same transition as `[getExitTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getExitTransition\(\))`.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use to move Views into the scene when reentering from a previously-started Activity due to popping the back stack. `transition`must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setRetainInstance

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[setRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setRetainInstance\(boolean\))~~(retain: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


Instead of retaining the Fragment itself, use a non-retained Fragment and keep retained state in a ViewModel attached to that Fragment. The ViewModel's constructor and its onCleared() callback provide the signal for initial creation and final destruction of the retained state.

Control whether a fragment instance is retained across Activity re-creation (such as from a configuration change). If set, the fragment lifecycle will be slightly different when an activity is recreated: 

  * `[onDestroy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDestroy\(\))` will not be called (but `[onDetach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onDetach\(\))` still will be, because the fragment is being detached from its current activity). 
  * `[onCreate](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreate\(android.os.Bundle\))` will not be called since the fragment is not being re-created. 
  * `[onAttach](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onAttach\(android.app.Activity\))` and `[onActivityCreated](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityCreated\(android.os.Bundle\))`**will** still be called. 



Parameters  
---  
`retain: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  `true` to retain this fragment instance across configuration changes, `false` otherwise.  
  
See also  
---  
`[getRetainInstance](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getRetainInstance\(\))` |   
  
### setReturnTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setReturnTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack. The exiting Views will be those that are regular Views or ViewGroups that have `[isTransitionGroup](https://developer.android.com/reference/android/view/ViewGroup.html#isTransitionGroup\(\))` return true. Typical Transitions will extend `[android.transition.Visibility](https://developer.android.com/reference/android/transition/Visibility.html)` as entering is governed by changing visibility from `[VISIBLE](https://developer.android.com/reference/android/view/View.html#VISIBLE)` to `[INVISIBLE](https://developer.android.com/reference/android/view/View.html#INVISIBLE)`. If `transition` is null, entering Views will remain unaffected. If nothing is set, the default will be to use the same value as set in `[setEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setEnterTransition\(java.lang.Object\))`.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use to move Views out of the Scene when the Fragment is preparing to close due to popping the back stack. `transition` must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setSharedElementEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementEnterTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used for shared elements transferred into the content Scene. Typical Transitions will affect size and location, such as `[android.transition.ChangeBounds](https://developer.android.com/reference/android/transition/ChangeBounds.html)`. A null value will cause transferred shared elements to blink to the final position.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use for shared elements transferred into the content Scene. `transition` must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setSharedElementReturnTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [setSharedElementReturnTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementReturnTransition\(java.lang.Object\))(transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the Transition that will be used for shared elements transferred back during a pop of the back stack. This Transition acts in the leaving Fragment. Typical Transitions will affect size and location, such as `[android.transition.ChangeBounds](https://developer.android.com/reference/android/transition/ChangeBounds.html)`. A null value will cause transferred shared elements to blink to the final position. If no value is set, the default will be to use the same value as `[setSharedElementEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setSharedElementEnterTransition\(java.lang.Object\))`.

Parameters  
---  
`transition: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?` |  The Transition to use for shared elements transferred out of the content Scene. `transition` must be an `[android.transition.Transition](https://developer.android.com/reference/android/transition/Transition.html)` or `[androidx.transition.Transition](https://developer.android.com/reference/kotlin/androidx/transition/Transition)`.  
  
### setTargetFragment

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[setTargetFragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setTargetFragment\(androidx.fragment.app.Fragment,int\))~~(fragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?, requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


Instead of using a target fragment to pass results, the fragment requesting a result should use `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResultListener\(java.lang.String,androidx.lifecycle.LifecycleOwner,androidx.fragment.app.FragmentResultListener\))` to register a `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` with a ` requestKey` using its `[parent fragment manager](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#getParentFragmentManager\(\))`. The fragment delivering a result should then call `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#setFragmentResult\(java.lang.String,android.os.Bundle\))` using the same `requestKey`. Consider using `[setArguments](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setArguments\(android.os.Bundle\))` to pass the `requestKey` if you need to support dynamic request keys.

Optional target for this fragment. This may be used, for example, if this fragment is being started by another, and when done wants to give a result back to the first. The target set here is retained across instances via `[FragmentManager.putFragment()](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#putFragment\(android.os.Bundle,java.lang.String,androidx.fragment.app.Fragment\))`.

Parameters  
---  
`fragment: [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)?` |  The fragment that is the target of this one.  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Optional request code, for convenience if you are going to call back with `[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))`.  
  
### setUserVisibleHint

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun ~~[setUserVisibleHint](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#setUserVisibleHint\(boolean\))~~(isVisibleToUser: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


If you are manually calling this method, use `[setMaxLifecycle](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentTransaction#setMaxLifecycle\(androidx.fragment.app.Fragment,androidx.lifecycle.Lifecycle.State\))` instead. If overriding this method, behavior implemented when passing in `true` should be moved to `[onResume](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onResume\(\))`, and behavior implemented when passing in `false` should be moved to `[onPause](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onPause\(\))`.

Set a hint to the system about whether this fragment's UI is currently visible to the user. This hint defaults to true and is persistent across fragment instance state save and restore. 

An app may set this to false to indicate that the fragment's UI is scrolled out of visibility or is otherwise not directly visible to the user. This may be used by the system to prioritize operations such as fragment lifecycle updates or loader ordering behavior.

**Note:** This method may be called outside of the fragment lifecycle. and thus has no ordering guarantees with regard to fragment lifecycle method calls.

Parameters  
---  
`isVisibleToUser: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  true if this fragment's UI is currently visible to the user (default), false if it is not.  
  
### shouldShowRequestPermissionRationale

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [shouldShowRequestPermissionRationale](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#shouldShowRequestPermissionRationale\(java.lang.String\))(permission: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Gets whether you should show UI with rationale before requesting a permission.

Parameters  
---  
`permission: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  A permission your app wants to request.  
  
Returns  
---  
`[Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)` |  Whether you should show permission rationale UI.  
  
See also  
---  
`[checkSelfPermission](https://developer.android.com/reference/android/content/Context.html#checkSelfPermission\(java.lang.String\))` |   
`[requestPermissions](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#requestPermissions\(java.lang.String\[\],int\))` |   
`[onRequestPermissionsResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onRequestPermissionsResult\(int,java.lang.String\[\],int\[\]\))` |   
  
### startActivity

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [startActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivity\(android.content.Intent\))(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Call `[startActivity](https://developer.android.com/reference/android/app/Activity.html#startActivity\(android.content.Intent\))` from the fragment's containing Activity.

### startActivity

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [startActivity](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivity\(android.content.Intent,android.os.Bundle\))(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Call `[startActivity](https://developer.android.com/reference/android/app/Activity.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` from the fragment's containing Activity.

### startActivityForResult

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[startActivityForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivityForResult\(android.content.Intent,int\))~~(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` passing in a `[StartActivityForResult](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.StartActivityForResult)` object for the `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.

Call `[startActivityForResult](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int\))` from the fragment's containing Activity.

Parameters  
---  
`intent: [Intent](https://developer.android.com/reference/android/content/Intent.html)` |  The intent to start.  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The request code to be returned in `[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))` when the activity exits. Must be between 0 and 65535 to be considered valid. If given requestCode is greater than 65535, an IllegalArgumentException would be thrown.  
  
### startActivityForResult

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[startActivityForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startActivityForResult\(android.content.Intent,int,android.os.Bundle\))~~(intent: [Intent](https://developer.android.com/reference/android/content/Intent.html), requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` passing in a `[StartActivityForResult](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.StartActivityForResult)` object for the `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.

Call `[startActivityForResult](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult\(android.content.Intent,%20int,%20android.os.Bundle\))` from the fragment's containing Activity.

Parameters  
---  
`intent: [Intent](https://developer.android.com/reference/android/content/Intent.html)` |  The intent to start.  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The request code to be returned in `[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))` when the activity exits. Must be between 0 and 65535 to be considered valid. If given requestCode is greater than 65535, an IllegalArgumentException would be thrown.  
`options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  Additional options for how the Activity should be started. See `[startActivity](https://developer.android.com/reference/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` for more details. This value may be null.  
  
### startIntentSenderForResult

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)

Deprecated in [1.3.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0)
    
    
    fun ~~[startIntentSenderForResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startIntentSenderForResult\(android.content.IntentSender,int,android.content.Intent,int,int,int,android.os.Bundle\))~~(  
        intent: [IntentSender](https://developer.android.com/reference/android/content/IntentSender.html),  
        requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        fillInIntent: [Intent](https://developer.android.com/reference/android/content/Intent.html)?,  
        flagsMask: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        flagsValues: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        extraFlags: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  


This method has been deprecated in favor of using the Activity Result API which brings increased type safety via an `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)` and the prebuilt contracts for common intents available in `[androidx.activity.result.contract.ActivityResultContracts](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts)`, provides hooks for testing, and allow receiving results in separate, testable classes independent from your fragment. Use `[registerForActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForActivityResult\(androidx.activity.result.contract.ActivityResultContract<I,O>,androidx.activity.result.ActivityResultCallback<O>\))` passing in a `[StartIntentSenderForResult](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContracts.StartIntentSenderForResult)` object for the `[ActivityResultContract](https://developer.android.com/reference/kotlin/androidx/activity/result/contract/ActivityResultContract)`.

Call `[startIntentSenderForResult](https://developer.android.com/reference/android/app/Activity.html#startIntentSenderForResult\(android.content.IntentSender,%20int,%20android.content.Intent,%20int,%20int,%20int,%20android.os.Bundle\))` from the fragment's containing Activity.

Parameters  
---  
`intent: [IntentSender](https://developer.android.com/reference/android/content/IntentSender.html)` |  The IntentSender to launch.  
`requestCode: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  The request code to be returned in `[onActivityResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onActivityResult\(int,int,android.content.Intent\))` when the activity exits. Must be between 0 and 65535 to be considered valid. If given requestCode is greater than 65535, an IllegalArgumentException would be thrown.  
`fillInIntent: [Intent](https://developer.android.com/reference/android/content/Intent.html)?` |  If non-null, this will be provided as the intent parameter to `[sendIntent](https://developer.android.com/reference/android/content/IntentSender.html#sendIntent\(android.content.Context,%20int,%20android.content.Intent,%20android.content.IntentSender.OnFinished,%20android.os.Handler\))`. This value may be null.  
`flagsMask: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Intent flags in the original IntentSender that you would like to change.  
`flagsValues: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Desired values for any bits set in `flagsMask`.  
`extraFlags: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  Always set to 0.  
`options: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)?` |  Additional options for how the Activity should be started. See `[startActivity](https://developer.android.com/reference/android/content/Context.html#startActivity\(android.content.Intent,%20android.os.Bundle\))` for more details. This value may be null.  
  
Throws  
---  
`[android.content.IntentSender.SendIntentException](https://developer.android.com/reference/android/content/IntentSender.SendIntentException.html)` |   
  
### startPostponedEnterTransition

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [startPostponedEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#startPostponedEnterTransition\(\))(): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Begin postponed transitions after `[postponeEnterTransition](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#postponeEnterTransition\(\))` was called. If postponeEnterTransition() was called, you must call startPostponedEnterTransition() or `[executePendingTransactions](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#executePendingTransactions\(\))` to complete the FragmentTransaction. If postponement was interrupted with `[executePendingTransactions](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentManager#executePendingTransactions\(\))`, before `startPostponedEnterTransition()`, animations may not run or may execute improperly.

See also  
---  
`[startPostponedEnterTransition](https://developer.android.com/reference/android/app/Activity.html#startPostponedEnterTransition\(\))` |   
  
### toString
    
    
    fun [toString](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#toString\(\))(): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

### unregisterForContextMenu

Added in [1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0)
    
    
    fun [unregisterForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#unregisterForContextMenu\(android.view.View\))(view: [View](https://developer.android.com/reference/android/view/View.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Prevents a context menu to be shown for the given view. This method will remove the `[OnCreateContextMenuListener](https://developer.android.com/reference/android/view/View.OnCreateContextMenuListener.html)` on the view.

Parameters  
---  
`view: [View](https://developer.android.com/reference/android/view/View.html)` |  The view that should stop showing a context menu.  
  
See also  
---  
`[registerForContextMenu](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#registerForContextMenu\(android.view.View\))` |   
  
## Extension functions

### Fragment.registerForAuthenticationResult

Artifact: [androidx.biometric:biometric](https://developer.android.com/jetpack/androidx/releases/biometric)

[View Source](https://cs.android.com/search?q=file:androidx/biometric/AuthenticationExtensions.kt+function:registerForAuthenticationResult)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[registerForAuthenticationResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(androidx.biometric.AuthenticationResultCallback\))(  
        resultCallback: [AuthenticationResultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback)  
    ): [AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)

Returns an `[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` that can be used to initiate authentication.

A success or error result will be delivered to `[AuthenticationResultCallback.onAuthResult](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback#onAuthResult\(androidx.biometric.AuthenticationResult\))` and (one or more) failures will be delivered to `[AuthenticationResultCallback.onAuthAttemptFailed](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback#onAuthAttemptFailed\(\))`, which is set by `[resultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/package-summary#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(androidx.biometric.AuthenticationResultCallback\))`. The callback will be executed on the main thread.

This _must_ be called unconditionally, as part of initialization path, typically as a field initializer of an Fragment.

Note that if multiple calls to this method are made within a single Fragment or Activity, only the callback registered by the last invocation will be saved and receive authentication results. This can result in unexpected behavior if you intend to manage multiple independent authentication flows. It is strongly recommended to avoid multiple calls to this method in such scenarios.
    
    
    import androidx.biometric.AuthenticationRequest
    import androidx.biometric.AuthenticationRequest.Biometric
    import androidx.biometric.AuthenticationRequest.Companion.biometricRequest
    import androidx.biometric.AuthenticationResult
    import androidx.biometric.PromptContentItemBulletedText
    import androidx.biometric.registerForAuthenticationResult
    import androidx.fragment.app.Fragment
    
    class MyFragmentForCredentialOnlyAuth : Fragment() {
        val requestAuthentication =
            registerForAuthenticationResult { result: AuthenticationResult ->
                when (result) {
                    // Handle successful authentication
                    is AuthenticationResult.Success -> {
                        Log.i(TAG, "onAuthenticationSucceeded with type ${result.authType}")
                    }
                    // Handle authentication error, e.g. user cancellation, lockout errors, etc
                    is AuthenticationResult.Error -> {
                        Log.i(
                            TAG,
                            "onAuthenticationError " +
                                "with error code: ${result.errorCode} " +
                                "and error string: ${result.errString}",
                        )
                    }
                    // Handle fallback option clicks
                    is AuthenticationResult.CustomFallbackSelected -> {
                        Log.i(TAG, "fallback is selected, text: ${result.fallback.text}")
                    }
                }
            }
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            val authRequest =
                biometricRequest(title = "Title", Biometric.Fallback.DeviceCredential) {
                    setSubtitle("Subtitle")
                    setContent(
                        AuthenticationRequest.BodyContent.VerticalList(
                            "Vertical list description",
                            listOf(
                                PromptContentItemBulletedText("test item1"),
                                PromptContentItemBulletedText("test item2"),
                            ),
                        )
                    )
                    setMinStrength(Biometric.Strength.Class3(/*optional: cryptoObject*/ ))
                    setIsConfirmationRequired(true)
                }
    
            Button(context).setOnClickListener { requestAuthentication.launch(authRequest) }
        }
    }

See also  
---  
`[registerForAuthenticationResult](https://developer.android.com/reference/kotlin/androidx/biometric/package-summary#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(java.util.concurrent.Executor,androidx.biometric.AuthenticationResultCallback\))` |  (Executor, AuthenticationResultCallback)  
  
### Fragment.registerForAuthenticationResult

Artifact: [androidx.biometric:biometric](https://developer.android.com/jetpack/androidx/releases/biometric)

[View Source](https://cs.android.com/search?q=file:androidx/biometric/AuthenticationExtensions.kt+function:registerForAuthenticationResult)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[registerForAuthenticationResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(java.util.concurrent.Executor,androidx.biometric.AuthenticationResultCallback\))(  
        callbackExecutor: [Executor](https://developer.android.com/reference/java/util/concurrent/Executor.html),  
        resultCallback: [AuthenticationResultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback)  
    ): [AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)

Returns an `[AuthenticationResultLauncher](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultLauncher)` that can be used to initiate authentication.

A success or error result will be delivered to `[AuthenticationResultCallback.onAuthResult](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback#onAuthResult\(androidx.biometric.AuthenticationResult\))` and (one or more) failures will be delivered to `[AuthenticationResultCallback.onAuthAttemptFailed](https://developer.android.com/reference/kotlin/androidx/biometric/AuthenticationResultCallback#onAuthAttemptFailed\(\))`, which is set by `[resultCallback](https://developer.android.com/reference/kotlin/androidx/biometric/package-summary#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(java.util.concurrent.Executor,androidx.biometric.AuthenticationResultCallback\))`. The callback will be executed on the thread provided by the `[callbackExecutor](https://developer.android.com/reference/kotlin/androidx/biometric/package-summary#\(androidx.fragment.app.Fragment\).registerForAuthenticationResult\(java.util.concurrent.Executor,androidx.biometric.AuthenticationResultCallback\))`.

This _must_ be called unconditionally, as part of initialization path, typically as a field initializer of an Fragment.

Note that if multiple calls to this method are made within a single Fragment or Activity, only the callback registered by the last invocation will be saved and receive authentication results. This can result in unexpected behavior if you intend to manage multiple independent authentication flows. It is strongly recommended to avoid multiple calls to this method in such scenarios.
    
    
    import androidx.biometric.AuthenticationRequest
    import androidx.biometric.AuthenticationRequest.Biometric
    import androidx.biometric.AuthenticationRequest.Companion.biometricRequest
    import androidx.biometric.AuthenticationResult
    import androidx.biometric.PromptContentItemBulletedText
    import androidx.biometric.registerForAuthenticationResult
    import androidx.fragment.app.Fragment
    
    class MyFragmentForCredentialOnlyAuth : Fragment() {
        val requestAuthentication =
            registerForAuthenticationResult { result: AuthenticationResult ->
                when (result) {
                    // Handle successful authentication
                    is AuthenticationResult.Success -> {
                        Log.i(TAG, "onAuthenticationSucceeded with type ${result.authType}")
                    }
                    // Handle authentication error, e.g. user cancellation, lockout errors, etc
                    is AuthenticationResult.Error -> {
                        Log.i(
                            TAG,
                            "onAuthenticationError " +
                                "with error code: ${result.errorCode} " +
                                "and error string: ${result.errString}",
                        )
                    }
                    // Handle fallback option clicks
                    is AuthenticationResult.CustomFallbackSelected -> {
                        Log.i(TAG, "fallback is selected, text: ${result.fallback.text}")
                    }
                }
            }
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            val authRequest =
                biometricRequest(title = "Title", Biometric.Fallback.DeviceCredential) {
                    setSubtitle("Subtitle")
                    setContent(
                        AuthenticationRequest.BodyContent.VerticalList(
                            "Vertical list description",
                            listOf(
                                PromptContentItemBulletedText("test item1"),
                                PromptContentItemBulletedText("test item2"),
                            ),
                        )
                    )
                    setMinStrength(Biometric.Strength.Class3(/*optional: cryptoObject*/ ))
                    setIsConfirmationRequired(true)
                }
    
            Button(context).setOnClickListener { requestAuthentication.launch(authRequest) }
        }
    }

### Fragment.clearFragmentResult

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/Fragment.kt+function:clearFragmentResult)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[clearFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).clearFragmentResult\(kotlin.String\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Clears the stored result for the given requestKey.

This clears a result that was previously set a call to `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))`.

If this is called with a requestKey that is not associated with any result, this method does nothing.

Parameters  
---  
`requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  key used to identify the result  
  
### Fragment.clearFragmentResultListener

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/Fragment.kt+function:clearFragmentResultListener)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[clearFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).clearFragmentResultListener\(kotlin.String\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Clears the stored `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` for the given requestKey.

This clears a `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` that was previously set a call to `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))`.

If this is called with a requestKey that is not associated with any `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)`, this method does nothing.

Parameters  
---  
`requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  key used to identify the result  
  
### Fragment.content

Artifact: [androidx.fragment:fragment-compose](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/compose/Fragment.kt+function:content)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[content](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).content\(kotlin.Function0\))(content: @[Composable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable) () -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)): [ComposeView](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ComposeView)

Wrapper function that handles the setup for creating a custom Fragment that hosts Compose content. It automatically sets the `[ViewCompositionStrategy](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ViewCompositionStrategy)` to `[ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed)`.

It should be used as part of the implementation of `[Fragment.onCreateView](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#onCreateView\(android.view.LayoutInflater,android.view.ViewGroup,android.os.Bundle\))` and requires a context meaning the fragment must be attached to a FragmentManager.
    
    
    class ExampleFragment : Fragment() {  
        override fun onCreateView(  
            inflater: LayoutInflater,  
            container: ViewGroup?,  
            savedInstanceState: Bundle?  
       ) = content {  
            val viewModel: ExampleViewModel = viewModel()  
            // put your @Composable content here  
        }  
    }

### Fragment.findNavController

Artifact: [androidx.navigation:navigation-fragment](https://developer.android.com/jetpack/androidx/releases/navigation)

[View Source](https://cs.android.com/search?q=file:androidx/navigation/fragment/Fragment.kt+function:findNavController)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[findNavController](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).findNavController\(\))(): [NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)

Find a `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` given a `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)`

Calling this on a Fragment that is not a `[NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment)` or within a `[NavHostFragment](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment)` will result in an `[IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)`

### Fragment.setFragmentResult

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/Fragment.kt+function:setFragmentResult)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))(requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), result: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the given result for the `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))`. This result will be delivered to a `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` that is called given to `[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))` with the same `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))`. If no `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` with the same key is set or the Lifecycle associated with the listener is not at least `[androidx.lifecycle.Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED)`, the result is stored until one becomes available, or `[clearFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).clearFragmentResult\(kotlin.String\))` is called with the same requestKey.

Parameters  
---  
`requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  key used to identify the result  
`result: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)` |  the result to be passed to another fragment.  
  
### Fragment.setFragmentResultListener

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/Fragment.kt+function:setFragmentResultListener)
    
    
    fun [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[setFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))(  
        requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
        listener: (requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), bundle: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)  
    ): [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)

Sets the `[FragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener)` for a given `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))`. Once this Fragment is at least in the `[androidx.lifecycle.Lifecycle.State.STARTED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#STARTED)` state, any results set by `[setFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResult\(kotlin.String,android.os.Bundle\))` using the same `[requestKey](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).setFragmentResultListener\(kotlin.String,kotlin.Function2\))` will be delivered to the `[FragmentResultListener.onFragmentResult](https://developer.android.com/reference/kotlin/androidx/fragment/app/FragmentResultListener#onFragmentResult\(java.lang.String,android.os.Bundle\))` callback. The callback will remain active until this Fragment reaches the `[androidx.lifecycle.Lifecycle.State.DESTROYED](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State#DESTROYED)` state or `[clearFragmentResultListener](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).clearFragmentResultListener\(kotlin.String\))` is called with the same requestKey.

Parameters  
---  
`requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  requestKey used to store the result  
`listener: (requestKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), bundle: [Bundle](https://developer.android.com/reference/android/os/Bundle.html)) -> [Unit](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-unit/index.html)` |  listener for result changes.  
  
### Fragment.navArgs

Artifact: [androidx.navigation:navigation-fragment](https://developer.android.com/jetpack/androidx/releases/navigation)

[View Source](https://cs.android.com/search?q=file:androidx/navigation/fragment/FragmentNavArgsLazy.kt+function:navArgs)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <Args : [NavArgs](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgs)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navArgs](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navArgs\(\))(): [NavArgsLazy](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgsLazy)<Args>

Returns a `[Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)` delegate to access the Fragment's arguments as an `[Args](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#\(androidx.fragment.app.Fragment\).navArgs\(\))` instance.

It is strongly recommended that this method only be used when the Fragment is created by `[androidx.navigation.NavController.navigate](https://developer.android.com/reference/kotlin/androidx/navigation/NavController#navigate\(kotlin.Int\))` with the corresponding `[androidx.navigation.NavDirections](https://developer.android.com/reference/kotlin/androidx/navigation/NavDirections)` object, which ensures that the required arguments are present.
    
    
    class MyFragment : Fragment() {  
        val args: MyFragmentArgs by navArgs()  
    }

This property can be accessed only after the Fragment's constructor.

### Fragment.activityViewModels

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/FragmentViewModelLazy.kt+function:activityViewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[activityViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\))(  
        noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null,  
        noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access parent activity's `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`, if `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\))` is specified then `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` returned by it will be used to create `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` first time. Otherwise, the activity's default factory will be used.
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MyViewModel by activityViewModels()  
    }

This property can be accessed only after this Fragment is attached i.e., after Fragment.onAttach(), and access prior to that will result in IllegalArgumentException.

### Fragment.createViewModelLazy

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/FragmentViewModelLazy.kt+function:createViewModelLazy)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[createViewModelLazy](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).createViewModelLazy\(kotlin.reflect.KClass,kotlin.Function0,kotlin.Function0,kotlin.Function0\))(  
        viewModelClass: [KClass](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/-k-class/index.html)<VM>,  
        storeProducer: () -> [ViewModelStore](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStore),  
        extrasProducer: () -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras) = { defaultViewModelCreationExtras },  
        factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Helper method for creation of `[ViewModelLazy](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelLazy)`, that resolves `null` passed as `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).createViewModelLazy\(kotlin.reflect.KClass,kotlin.Function0,kotlin.Function0,kotlin.Function0\))` to the default factory.

This method also takes a `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)` producer that provides default extras to the created `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`.

### Fragment.viewModels

Artifact: [androidx.fragment:fragment](https://developer.android.com/jetpack/androidx/releases/fragment)

[View Source](https://cs.android.com/search?q=file:androidx/fragment/app/FragmentViewModelLazy.kt+function:viewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[viewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).viewModels\(kotlin.Function0,kotlin.Function0,kotlin.Function0\))(  
        noinline ownerProducer: () -> [ViewModelStoreOwner](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelStoreOwner) = { this },  
        noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null,  
        noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` by **default** scoped to this `[Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment)`:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MyViewModel by viewModels()  
    }

Custom `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` can be defined via `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).viewModels\(kotlin.Function0,kotlin.Function0,kotlin.Function0\))` parameter, factory returned by it will be used to create `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MyViewModel by viewModels { myFactory }  
    }

Default scope may be overridden with parameter `[ownerProducer](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).viewModels\(kotlin.Function0,kotlin.Function0,kotlin.Function0\))`:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MyViewModel by viewModels ({requireParentFragment()})  
    }

This property can be accessed only after this Fragment is attached i.e., after Fragment.onAttach(), and access prior to that will result in IllegalArgumentException.

### Fragment.hiltNavGraphViewModels

Artifact: [androidx.hilt:hilt-navigation-fragment](https://developer.android.com/jetpack/androidx/releases/hilt)

[View Source](https://cs.android.com/search?q=file:androidx/hilt/navigation/fragment/HiltNavGraphViewModelLazy.kt+function:hiltNavGraphViewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[hiltNavGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).hiltNavGraphViewModels\(kotlin.Int\))(navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access a [HiltViewModel](https://dagger.dev/api/latest/dagger/hilt/android/lifecycle/HiltViewModel) -annotated `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MainViewModel by hiltNavGraphViewModels(R.navigation.main)  
    }

This property can be accessed only after this NavGraph is on the NavController back stack, and an attempt access prior to that will result in an IllegalArgumentException.

Parameters  
---  
`navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  ID of a NavGraph that exists on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack  
  
### Fragment.hiltNavGraphViewModels

Artifact: [androidx.hilt:hilt-navigation-fragment](https://developer.android.com/jetpack/androidx/releases/hilt)

[View Source](https://cs.android.com/search?q=file:androidx/hilt/navigation/fragment/HiltNavGraphViewModelLazy.kt+function:hiltNavGraphViewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel), VMF : [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[hiltNavGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).hiltNavGraphViewModels\(kotlin.Int,kotlin.Function1\))(  
        navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        noinline creationCallback: (VMF) -> VM  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access a [HiltViewModel](https://dagger.dev/api/latest/dagger/hilt/android/lifecycle/HiltViewModel) -annotated `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` with an @AssistedInject-annotated constructor that is scoped to a navigation graph present on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MainViewModel by hiltNavGraphViewModels(R.navigation.main) { factory: MainViewModelFactory ->  
            factory.create(...)  
        }  
    }

This property can be accessed only after this NavGraph is on the NavController back stack, and an attempt access prior to that will result in an IllegalArgumentException.

Parameters  
---  
`navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  ID of a NavGraph that exists on the `[androidx.navigation.NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack  
`noinline creationCallback: (VMF) -> VM` |  callback that takes an @AssistedFactory-annotated factory and creates a HiltViewModel using @AssistedInject-annotated constructor.  
  
### Fragment.navGraphViewModels

Artifact: [androidx.navigation:navigation-fragment](https://developer.android.com/jetpack/androidx/releases/navigation)

[View Source](https://cs.android.com/search?q=file:androidx/navigation/NavGraphViewModelLazy.kt+function:navGraphViewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))(  
        navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html),  
        noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null,  
        noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access a `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MainViewModel by navGraphViewModels(R.id.main)  
    }

Custom `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` can be defined via `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))` parameter, factory returned by it will be used to create `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`:
    
    
    class MyFragment : Fragment() {  
        val viewmodel: MainViewModel by navGraphViewModels(R.id.main) { myFactory }  
    }

This property can be accessed only after this NavGraph is on the NavController back stack, and an attempt access prior to that will result in an IllegalArgumentException.

Parameters  
---  
`navGraphId: @[IdRes](https://developer.android.com/reference/kotlin/androidx/annotation/IdRes) [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)` |  ID of a NavGraph that exists on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack  
`noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null` |  lambda that will be called during initialization to return `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)`. If none is provided, this will use the extras from the `[NavBackStackEntry](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry)` referenced by the `[navGraphId](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))`.  
`noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null` |  lambda that will be called during initialization to return `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)`. If none is provided, this will use the factory from the `[NavBackStackEntry](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry)` referenced by the `[navGraphId](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\))`.  
  
### Fragment.navGraphViewModels

Artifact: [androidx.navigation:navigation-fragment](https://developer.android.com/jetpack/androidx/releases/navigation)

[View Source](https://cs.android.com/search?q=file:androidx/navigation/NavGraphViewModelLazy.kt+function:navGraphViewModels)
    
    
    @[MainThread](https://developer.android.com/reference/kotlin/androidx/annotation/MainThread)  
    inline fun <VM : [ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)> [Fragment](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment).[navGraphViewModels](https://developer.android.com/reference/kotlin/androidx/fragment/app/Fragment#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.String,kotlin.Function0,kotlin.Function0\))(  
        navGraphRoute: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html),  
        noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null,  
        noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null  
    ): [Lazy](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-lazy/index.html)<VM>

Returns a property delegate to access a `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)` scoped to a navigation graph present on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack:
    
    
    class MyFragment : Fragment() {  
        val viewModel: MainViewModel by navGraphViewModels("main")  
    }

Custom `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)` can be defined via `[factoryProducer](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.String,kotlin.Function0,kotlin.Function0\))` parameter, factory returned by it will be used to create `[ViewModel](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel)`:
    
    
    class MyFragment : Fragment() {  
        val viewModel: MainViewModel by navGraphViewModels("main") { myFactory }  
    }

This property can be accessed only after this NavGraph is on the NavController back stack, and an attempt access prior to that will result in an IllegalArgumentException.

Parameters  
---  
`navGraphRoute: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)` |  `[NavDestination.route](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination#route\(\))` of a NavGraph that exists on the `[NavController](https://developer.android.com/reference/kotlin/androidx/navigation/NavController)` back stack. If a `[NavDestination](https://developer.android.com/reference/kotlin/androidx/navigation/NavDestination)` with the given route does not exist on the back stack, an `[IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)` will be thrown.  
`noinline extrasProducer: (() -> [CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras))? = null` |  lambda that will be called during initialization to return `[CreationExtras](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/CreationExtras)`. If none is provided, this will use the extras from the `[NavBackStackEntry](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry)` referenced by the `[navGraphRoute](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.String,kotlin.Function0,kotlin.Function0\))`.  
`noinline factoryProducer: (() -> [ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory))? = null` |  lambda that will be called during initialization to return `[ViewModelProvider.Factory](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModelProvider.Factory)`. If none is provided, this will use the factory from the `[NavBackStackEntry](https://developer.android.com/reference/kotlin/androidx/navigation/NavBackStackEntry)` referenced by the `[navGraphRoute](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.String,kotlin.Function0,kotlin.Function0\))`.  
  
Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
