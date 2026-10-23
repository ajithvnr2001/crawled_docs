---
url: https://developer.android.com/training/cars/media/create-media-browser/browsable-search/
title: Display browsable search results \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:58.758405+00:00
---

# Display browsable search results  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/media/create-media-browser/browsable-search/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Display browsable search results Stay organized with collections  Save and categorize content based on your preferences. 

All apps must support voice searches. This page describes how to further enhance the search experience by supporting the initiation of searches without voice and by showing a list of search results so that users can pick another result. For example, if the suggested result isn't the most relevant.

Your media app can provide contextual search results in Android Auto and Android Automotive OS (AAOS). These results appear when a user initiates a search query or views the results of the most recent search.

To enable and provide these search results:

  * Declare search support in your service's `onGetRoot` method.

  * Override the `onSearch` method in your media browser service to handle user search terms.

  * Organize Search results using title items for improved browsability.




Your app can provide contextual search results that appear when a search query is started. Android Auto and AAOS show these results through search query interfaces or through affordances that pivot on queries made earlier. To learn more, see the [Support voice actions](https://developer.android.com/training/cars/media/voice-actions#support_voice).

![Playback view with a **Search results** option to view media items
related to the user's voice search](https://developer.android.com/static/images/training/cars/search_results.png)

**Figure 1.** Playback view with a **Search results** option to view media items related to the user's voice search.

To indicate that your app supports the display of search results, include the constant key [`BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED`](https://github.com/androidx/media/blob/release/libraries/session/src/main/java/androidx/media3/session/legacy/MediaConstants.java) in the extras bundle returned by your service's [`onGetRoot`](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy#onGetRoot) method, mapping to the Boolean `true`.

### Kotlin
    
    
    import androidx.media.utils.MediaConstants
    
    @Nullable
    override fun onGetRoot(
        @NonNull clientPackageName: String,
        clientUid: Int,
        @Nullable rootHints: Bundle
    ): BrowserRoot {
        val extras = Bundle()
        extras.putBoolean(
            MediaConstants.BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED, true)
        return BrowserRoot(ROOT_ID, extras)
    }
    

### Java
    
    
    import androidx.media.utils.MediaConstants;
    
    @Nullable
    @Override
    public BrowserRoot onGetRoot(
        @NonNull String clientPackageName,
        int clientUid,
        @Nullable Bundle rootHints) {
        Bundle extras = new Bundle();
        extras.putBoolean(
            MediaConstants.BROWSER_SERVICE_EXTRAS_KEY_SEARCH_SUPPORTED, true);
        return new BrowserRoot(ROOT_ID, extras);
    }
    

To provide search results, override the [`onSearch`](https://developer.android.com/reference/android/support/v4-media/MediaBrowserServiceCompat#onSearch\(java.lang.String,%20android.os.Bundle,%20android.support.v4.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E\)) method in your media browser service. Android Auto and AAOS forward the user's search terms to this method when a user invokes a search query interface or **Search results** affordance.

To make search results more browsable, you can use [title items](https://developer.android.com/training/cars/media/create-media-browser/content-styles#group-items). For example, if your app plays music, you can organize search results by album, artist, and song. This code snippet shows an implementation of the `onSearch` method:

### Kotlin
    
    
    fun onSearch(query: String, extras: Bundle) {
      // Detach from results to unblock the caller (if a search is expensive).
      result.detach()
      object:AsyncTask() {
        internal var searchResponse:ArrayList
        internal var succeeded = false
        protected fun doInBackground(vararg params:Void):Void {
          searchResponse = ArrayList()
          if (doSearch(query, extras, searchResponse))
          {
            succeeded = true
          }
          return null
        }
        protected fun onPostExecute(param:Void) {
          if (succeeded)
          {
            // Sending an empty List informs the caller that there were no results.
            result.sendResult(searchResponse)
          }
          else
          {
            // This invokes onError() on the search callback.
            result.sendResult(null)
          }
          return null
        }
      }.execute()
    }
    // Populates resultsToFill with search results. Returns true on success or false on error.
    private fun doSearch(
        query: String,
        extras: Bundle,
        resultsToFill: ArrayList
    ): Boolean {
      // Implement this method.
    }
    

### Java
    
    
    @Override
    public void onSearch(final String query, final Bundle extras,
                            Result&lt;List&lt;MediaItem>> result) {
    
      // Detach from results to unblock the caller (if a search is expensive).
      result.detach();
    
      new AsyncTask<Void, Void, Void>() {
        List>MediaItem> searchResponse;
        boolean succeeded = false;
        @Override
        protected Void doInBackground(Void... params) {
          searchResponse = new ArrayList&lt;MediaItem>();
          if (doSearch(query, extras, searchResponse)) {
            succeeded = true;
          }
          return null;
        }
    
        @Override
        protected void onPostExecute(Void param) {
          if (succeeded) {
           // Sending an empty List informs the caller that there were no results.
           result.sendResult(searchResponse);
          } else {
            // This invokes onError() on the search callback.
            result.sendResult(null);
          }
        }
      }.execute()
    }
    
    /** Populates resultsToFill with search results. Returns true on success or false on error. */
    private boolean doSearch(String query, Bundle extras, ArrayList&lt;MediaItem> resultsToFill) {
        // Implement this method.
    }
    

[ Previous arrow_back  Display media artwork  ](https://developer.android.com/training/cars/media/create-media-browser/media-artwork)

[ Next Implement custom browse actions  arrow_forward  ](https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
