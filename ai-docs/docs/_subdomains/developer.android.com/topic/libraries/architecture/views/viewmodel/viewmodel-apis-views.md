---
url: https://developer.android.com/topic/libraries/architecture/views/viewmodel/viewmodel-apis-views/
title: ViewModel Scoping APIs (Views) \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:41:26.420107+00:00
---

# ViewModel Scoping APIs (Views)  |  Android Developers

> Source: https://developer.android.com/topic/libraries/architecture/views/viewmodel/viewmodel-apis-views/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ UI ](https://developer.android.com/develop/ui)
  * [ Views ](https://developer.android.com/develop/ui/views/layout/declaring-layout)
  * [ Guides ](https://developer.android.com/topic/architecture/views/recommendations-views)



Stay organized with collections  Save and categorize content based on your preferences. 

# ViewModel Scoping APIs (Views) Part of [Android Jetpack](https://developer.android.com/jetpack).

[ Concepts and Jetpack Compose implementationarrow_forward ](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-apis)

Scope is key to using ViewModels effectively. Each ViewModel is scoped to an object that implements the [`ViewModelStoreOwner`](https://developer.android.com/reference/androidx/lifecycle/ViewModelStoreOwner) interface. There are several APIs that allow you to more easily manage the scope of your ViewModels.

**Note:** For more information on scope and ViewModel lifecycle, see the [ViewModel Overview](https://developer.android.com/topic/libraries/architecture/viewmodel#scope).

The `ViewModelProvider.get()` method lets you obtain an instance of a ViewModel scoped to any `ViewModelStoreOwner`. For Kotlin users, there are different extension functions available for the most common use cases. All Kotlin extension function implementations use the ViewModelProvider API under the hood.

## ViewModels scoped to the closest ViewModelStoreOwner

You can scope a ViewModel to an Activity, Fragment, or destination of a Navigation graph. The [`viewModels()`](https://developer.android.com/reference/kotlin/androidx/activity/package-summary#\(androidx.activity.ComponentActivity\)) extension functions provided by the Activity, Fragment, and Navigation libraries allow you to get an instance of the ViewModel scoped to the closest `ViewModelStoreOwner`.

### Views
    
    
    import androidx.activity.viewModels
    
    class MyActivity : AppCompatActivity() {
        // ViewModel API available in activity.activity-ktx
        // The ViewModel is scoped to `this` Activity
        val viewModel: MyViewModel by viewModels()
    }
    
    import androidx.fragment.app.viewModels
    
    class MyFragment : Fragment() {
        // ViewModel API available in fragment.fragment-ktx
        // The ViewModel is scoped to `this` Fragment
        val viewModel: MyViewModel by viewModels()
    }

### Views
    
    
    import androidx.lifecycle.ViewModelProvider;
    
    public class MyActivity extends AppCompatActivity {
        // The ViewModel is scoped to `this` Activity
        MyViewModel viewModel = new ViewModelProvider(this).get(MyViewModel.class);
    }
    
    public class MyFragment extends Fragment {
        // The ViewModel is scoped to `this` Fragment
        MyViewModel viewModel = new ViewModelProvider(this).get(MyViewModel.class);
    }

## ViewModels scoped to any ViewModelStoreOwner

The `ComponentActivity.viewModels()` and `Fragment.viewModels()` functions in the View system take an optional `ownerProducer` parameter that you can use to specify which `ViewModelStoreOwner` the instance of the ViewModel is scoped to. The following sample shows how to get an instance of a ViewModel scoped to the parent fragment:

### Views
    
    
    import androidx.fragment.app.viewModels
    
    class MyFragment : Fragment() {
    
        // ViewModel API available in fragment.fragment-ktx
        // The ViewModel is scoped to the parent of `this` Fragment
        val viewModel: SharedViewModel by viewModels(
            ownerProducer = { requireParentFragment() }
        )
    }

### Views
    
    
    import androidx.lifecycle.ViewModelProvider;
    
    public class MyFragment extends Fragment {
    
        SharedViewModel viewModel;
    
        @Override
        public void onViewCreated(View view, Bundle savedInstanceState) {
            // The ViewModel is scoped to the parent of `this` Fragment
            viewModel = new ViewModelProvider(requireParentFragment())
                .get(SharedViewModel.class);
        }
    }

Getting an Activity-scoped ViewModel from a Fragment is a common use case. When doing so, you can use the [`activityViewModels()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/package-summary#\(androidx.fragment.app.Fragment\).activityViewModels\(kotlin.Function0,kotlin.Function0\)) Views extension function. If you're not using Views and Kotlin, you can use the same APIs as above and by passing the right owner.

### Views
    
    
    import androidx.fragment.app.activityViewModels
    
    class MyFragment : Fragment() {
    
        // ViewModel API available in fragment.fragment-ktx
        // The ViewModel is scoped to the host Activity
        val viewModel: SharedViewModel by activityViewModels()
    }

### Views
    
    
    import androidx.lifecycle.ViewModelProvider;
    
    public class MyFragment extends Fragment {
    
        SharedViewModel viewModel;
    
        @Override
        public void onViewCreated(View view, Bundle savedInstanceState) {
            // The ViewModel is scoped to the host Activity
            viewModel = new ViewModelProvider(requireActivity())
                .get(SharedViewModel.class);
        }
    }

## ViewModels scoped to the Navigation graph

Navigation graphs are also ViewModel store owners. If you're using [Navigation Fragment](https://developer.android.com/guide/navigation), you can get an instance of a ViewModel scoped to a Navigation graph with the [`navGraphViewModels(graphId)`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#\(androidx.fragment.app.Fragment\).navGraphViewModels\(kotlin.Int,kotlin.Function0,kotlin.Function0\)) Views extension function.

### Views
    
    
    import androidx.navigation.navGraphViewModels
    
    class MyFragment : Fragment() {
    
        // ViewModel API available in navigation.navigation-fragment
        // The ViewModel is scoped to the `nav_graph` Navigation graph
        val viewModel: SharedViewModel by navGraphViewModels(R.id.nav_graph)
    
        // Equivalent navGraphViewModels code using the viewModels API
        val viewModel: SharedViewModel by viewModels(
            { findNavController().getBackStackEntry(R.id.nav_graph) }
        )
    }

### Views
    
    
    import androidx.lifecycle.ViewModelProvider;
    
    public class MyFragment extends Fragment {
    
        SharedViewModel viewModel;
    
        @Override
        public void onViewCreated(View view, Bundle savedInstanceState) {
            NavController navController = NavHostFragment.findNavController(this);
            NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.my_graph);
    
            // The ViewModel is scoped to the `nav_graph` Navigation graph
            viewModel = new ViewModelProvider(backStackEntry).get(SharedViewModel.class);
        }
    }

If you're using Hilt in addition to Jetpack Navigation, you can use the [`hiltNavGraphViewModels(graphId)`](https://developer.android.com/reference/kotlin/androidx/hilt/navigation/fragment/package-summary#hiltnavgraphviewmodels) API as follows.

### Views
    
    
    import androidx.hilt.navigation.fragment.hiltNavGraphViewModels
    
    class MyFragment : Fragment() {
    
        // ViewModel API available in hilt.hilt-navigation-fragment
        // The ViewModel is scoped to the `nav_graph` Navigation graph
        // and is provided using the Hilt-generated ViewModel factory
        val viewModel: SharedViewModel by hiltNavGraphViewModels(R.id.nav_graph)
    }

### Views
    
    
    import androidx.hilt.navigation.HiltViewModelFactory;
    import androidx.lifecycle.ViewModelProvider;
    
    public class MyFragment extends Fragment {
    
        SharedViewModel viewModel;
    
        @Override
        public void onViewCreated(View view, Bundle savedInstanceState) {
            NavController navController = NavHostFragment.findNavController(this);
            NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.my_graph);
    
            // The ViewModel is scoped to the `nav_graph` Navigation graph
            // and is provided using the Hilt-generated ViewModel factory
            viewModel = new ViewModelProvider(
                backStackEntry,
                HiltViewModelFactory.create(getContext(), backStackEntry)
            ).get(SharedViewModel.class);
        }
    }

## Recommended for you

  * Note: link text is displayed when JavaScript is off
  * [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)
  * [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 

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


