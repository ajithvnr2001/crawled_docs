---
url: https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/
title: Quickstart: Create a Firestore database by using a web or mobile client library \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:51:09.023212+00:00
---

# Quickstart: Create a Firestore database by using a web or mobile client library  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/

[ Skip to main content ](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/)
  * [Deutsch](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=de)
  * [Español](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=es-419)
  * [Français](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=id)
  * [Italiano](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=it)
  * [Português](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=ja)
  * [한국어](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/databases-color.svg) ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Set up your development environment](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#set_up_your_development_environment)
  * [Initialize Firestore in Native Mode](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#initialize)
  * [Add data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#add_data)
  * [Read data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#read_data)
  * [Secure your data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#secure_your_data)
  * [Watch a video tutorial](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#watch_a_video_tutorial)
  * [Next steps](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#next_steps)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)


Was this helpful?
Send feedback 
  * On this page
  * [Set up your development environment](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#set_up_your_development_environment)
  * [Initialize Firestore in Native Mode](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#initialize)
  * [Add data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#add_data)
  * [Read data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#read_data)
  * [Secure your data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#secure_your_data)
  * [Watch a video tutorial](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#watch_a_video_tutorial)
  * [Next steps](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#next_steps)


# Create a Firestore database by using a web or mobile client library Stay organized with collections  Save and categorize content based on your preferences.
This quickstart shows you how to set up Firestore, add data, and read data by using the Android, Apple platforms, Web, Unity, or C++ client library.
  1. If you haven't already, create a Firebase project: In the [Firebase console](https://console.firebase.google.com/), click **Add project** , then follow the on-screen instructions to create a Firebase project or to add Firebase services to an existing Google Cloud project.
  2. In the left panel, go to **Databases & Storage** > [**Firestore**](https://console.firebase.google.com/project/_/firestore/).
  3. Click **Create database**.
  4. Select a [location](https://docs.cloud.google.com/firestore/docs/locations#types) for your database.
If you aren't able to select a location, then your project's ["location for default Google Cloud resources"](https://docs.cloud.google.com/firestore/docs/locations#default-cloud-location) has already been set. Some of your project's resources (like the default Firestore instance) share a common location dependency, and their location can be set either during project creation or when setting up another service that shares this location dependency.
  5. Select a starting mode for your Firestore Security Rules: 

Test mode
    
Good for getting started with the mobile and web client libraries, but allows anyone to read and overwrite your data. After testing, **make sure to review the[Secure your data](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#secure_your_data) section.**     
To get started with the web, Apple platforms, or Android SDK, select test mode. 

Locked mode
    
Denies all reads and writes from mobile and web clients. Your authenticated application servers (C#, Go, Java, Node.js, PHP, Python, or Ruby) can still access your database.     
To get started with the C#, Go, Java, Node.js, PHP, Python, or Ruby server client library, select locked mode.
Your initial set of Firestore Security Rules will apply to your default Firestore database. If you create multiple databases for your project, you can deploy Firestore Security Rules for each database.
  6. Click **Create**.


When you enable Firestore, it also enables the API in the [Cloud API Manager](https://console.cloud.google.com/projectselector/apis/api/firestore.googleapis.com/overview).
## Set up your development environment
Add the required dependencies and client libraries to your app.
[Web version 9](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-9-modular)[Web version 8](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-8-namespaced)[Apple platforms](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#apple-platforms)[Android](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#android)[Dart](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#dart-flutter) More
[C++](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#c++)[Unity](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#unity)
  1. Follow the instructions to [add Firebase to your Web app](https://firebase.google.com/docs/web/setup). 
  2. Import both Firebase and Firestore: 
```
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
```



  1. Follow the instructions to [add Firebase to your Web app](https://firebase.google.com/docs/web/setup). 
  2. Add the Firebase and Firestore libraries to your app: 
```
<script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.1/firebase-firestore.js"></script>
```
The Firestore SDK is also available as an npm package. 
```
npm install firebase@8.10.1 --save
```
You'll need to manually require both Firebase and Firestore. 
```
const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");
```



Follow the instructions to [add Firebase to your Apple app](https://firebase.google.com/docs/ios/setup). 
Use Swift Package Manager to install and manage Firebase dependencies.
  1. In Xcode, with your app project open, navigate to **File > Swift Packages > Add Package Dependency**.
  2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk
  
```

  3. Choose the Firestore library.
  4. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background. 


  1. Follow the instructions to [add Firebase to your Android app](https://firebase.google.com/docs/android/setup).
  2. Declare the dependency for the Firestore library for Android in your module (app-level) Gradle file (usually `app/build.gradle.kts` or `app/build.gradle`): 
```
implementation("com.google.firebase:firebase-firestore:27.1.0")
```

If your app uses multiple Firebase libraries, consider using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom), which ensures that your app's Firebase library versions are always compatible. 
**Looking for a Kotlin-specific library module?** Starting with the [October 2023 release](https://firebase.google.com/support/release-notes/android#2023-10-10), both Kotlin and Java developers can depend on the main library module (for details, see the [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration)). 


  1. If you haven't already, [configure and initialize Firebase](https://firebase.google.com/docs/flutter/setup) in your Flutter app.
  2. From the root of your Flutter project, run the following command to install the plugin: 
```
flutter pub add cloud_firestore
```

  3. Once complete, rebuild your Flutter application: 
```
flutter run
```



  1. Follow the instructions to [add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup).
  2. **C++ interface for Android.**
     * **Gradle dependencies.** Add the following to your module (app-level) Gradle file (usually `app/build.gradle`): 
```
        android.defaultConfig.externalNativeBuild.cmake {
          arguments "-DFIREBASE_CPP_SDK_DIR=$gradle.firebase_cpp_sdk_dir"
        }

        apply from: "$gradle.firebase_cpp_sdk_dir/Android/firebase_dependencies.gradle"
        firebaseCpp.dependencies {
          // earlier entries
          auth
          firestore
        }
        
```

     * **Binary dependencies.** Similarly, the recommended way to get the binary dependencies is to add the following to your `CMakeLists.txt` file: 
```
        add_subdirectory(${FIREBASE_CPP_SDK_DIR} bin/ EXCLUDE_FROM_ALL)
        set(firebase_libs firebase_auth firebase_firestore firebase_app)
        # Replace the target name below with the actual name of your target,
        # for example, "native-lib".
        target_link_libraries(${YOUR_TARGET_NAME_HERE} "${firebase_libs}")
        
```

  3. To set up **desktop integration** , see [Add Firebase to your C++ project](https://firebase.google.com/docs/cpp/setup#desktop-workflow).


  1. Follow the instructions to [add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup).
  2. Use the Unity interface to configure your project to minify Android builds.
You must minify the build to avoid the message `Error while merging dex archives`. 
     * The option can be found in **Player Settings > Android > Publishing Settings > Minify**. 
     * The options may differ in different versions of Unity so refer to the official [Unity documentation](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#minify) and the [Firebase Unity Build Debug Guide](https://firebase.google.com/docs/unity/build-debug-guide#single_dex_issues_and_minification_mandatory_if_using_cloud_firestore). 
     * If, after enabling minification, the number of referenced methods still exceeds the limit, another option is to enable `multidex` in: 
       * `mainTemplate.gradle` if **Custom Gradle Template** under **Player Settings** is enabled 
       * or, the module-level `build.gradle` file, if you use Android Studio to build the exported project. 


## Initialize Firestore in Native Mode
Initialize an instance of Firestore:
[Web version 9](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-9-modular)[Web version 8](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-8-namespaced)[Swift](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#swift)[Objective-C](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#objective-c)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#java-android) More
[Dart](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#dart-flutter)[C++](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#c++)[Unity](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#unity)

```
// Initialize Firestore through Firebase
import { initializeApp } from "firebase/app"
import { getFirestore } from "firebase/firestore"
const firebaseApp = initializeApp({
  apiKey: '### FIREBASE API KEY ###',
  authDomain: '### FIREBASE AUTH DOMAIN ###',
  projectId: '### CLOUD FIRESTORE PROJECT ID ###'
});

const db = getFirestore();
```
The values for `initializeApp` can be found in your web app's [`firebaseConfig`](https://support.google.com/firebase/answer/7015592). To persist data when the device loses its connection, see the [Enable Offline Data](https://docs.cloud.google.com/firestore/native/docs/manage-data/enable-offline) documentation.  
```
// Initialize Firestore through Firebase
firebase.initializeApp({
  apiKey: '### FIREBASE API KEY ###',
  authDomain: '### FIREBASE AUTH DOMAIN ###',
  projectId: '### CLOUD FIRESTORE PROJECT ID ###'
});

var db = firebase.firestore();
```
The values for `initializeApp` can be found in your web app's [`firebaseConfig`](https://support.google.com/firebase/answer/7015592). To persist data when the device loses its connection, see the [Enable Offline Data](https://docs.cloud.google.com/firestore/native/docs/manage-data/enable-offline) documentation. 
**Note:** This product is not available on watchOS and App Clip targets. 

```
import FirebaseCore
import FirebaseFirestore

FirebaseApp.configure()

let db = Firestore.firestore()
[AppDelegate.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/AppDelegate.swift#L31-L33)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
@import FirebaseCore;
@import FirebaseFirestore;

// Use Firebase library to configure APIs
[FIRApp configure];

FIRFirestore *defaultFirestore = [FIRFirestore firestore];
[AppDelegate.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/AppDelegate.m#L32-L32)

  
```

```
  // Access a Firestore instance from your Activity
  val db = Firebase.firestore
DocSnippets[.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L109-L109)

```

```
// Access a Firestore instance from your Activity
  FirebaseFirestore db = FirebaseFirestore.getInstance();
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L131-L131)

```

```
db = FirebaseFirestore.instance;
```

```
// Make sure the call to `Create()` happens some time before you call Firestore::GetInstance().
App::Create();
Firestore* db = Firestore::GetInstance();
[AppDelegate.mm](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/ios/firestore-snippets-cpp/AppDelegate.mm#L34-L36)

```

```
using Firebase.Firestore;
using Firebase.Extensions;
```

```
FirebaseFirestore db = FirebaseFirestore.DefaultInstance;
```

## Add data
Firestore stores data in Documents, which are stored in Collections. Firestore creates collections and documents implicitly the first time you add data to the document. You do not need to explicitly create collections or documents.
Create a new collection and a document using the following example code.
[Web version 9](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-9-modular)[Web version 8](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-8-namespaced)[Swift](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#swift)[Objective-C](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#objective-c)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#java-android) More
[Dart](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#dart-flutter)[C++](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#c++)[Unity](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#unity)

```
import { collection, addDoc } from "firebase/firestore"; 

try {
  const docRef = await addDoc(collection(db, "users"), {
    first: "Ada",
    last: "Lovelace",
    born: 1815
  });
  console.log("Document written with ID: ", docRef.id);
} catch (e) {
  console.error("Error adding document: ", e);
}
[add_ada_lovelace.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/add_ada_lovelace.js#L8-L19)

```

```
db.collection("users").add({
    first: "Ada",
    last: "Lovelace",
    born: 1815
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});
[test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L125-L135)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
// Add a new document with a generated ID
do {
  let ref = try await db.collection("users").addDocument(data: [
    "first": "Ada",
    "last": "Lovelace",
    "born": 1815
  ])
  print("Document added with ID: \(ref.documentID)")
} catch {
  print("Error adding document: \(error)")
}
[ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L172-L182)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
// Add a new document with a generated ID
__block FIRDocumentReference *ref =
    [[self.db collectionWithPath:@"users"] addDocumentWithData:@{
      @"first": @"Ada",
      @"last": @"Lovelace",
      @"born": @1815
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error adding document: %@", error);
      } else {
        NSLog(@"Document added with ID: %@", ref.documentID);
      }
    }];
[ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L92-L104)

```

```
// Create a new user with a first and last name
val user = hashMapOf(
    "first" to "Ada",
    "last" to "Lovelace",
    "born" to 1815,
)

// Add a new document with a generated ID
db.collection("users")
    .add(user)
    .addOnSuccessListener { documentReference ->
        Log.d(TAG, "DocumentSnapshot added with ID: ${documentReference.id}")
    }
    .addOnFailureListener { e ->
        Log.w(TAG, "Error adding document", e)
    }
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L137-L152)

```

```
// Create a new user with a first and last name
Map<String, Object> user = new HashMap<>();
user.put("first", "Ada");
user.put("last", "Lovelace");
user.put("born", 1815);

// Add a new document with a generated ID
db.collection("users")
        .add(user)
        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
            @Override
            public void onSuccess(DocumentReference documentReference) {
                Log.d(TAG, "DocumentSnapshot added with ID: " + documentReference.getId());
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error adding document", e);
            }
        });
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L163-L183)

```

```
// Create a new user with a first and last name
final user = <String, dynamic>{
  "first": "Ada",
  "last": "Lovelace",
  "born": 1815
};

// Add a new document with a generated ID
db.collection("users").add(user).then((DocumentReference doc) =>
    print('DocumentSnapshot added with ID: ${doc.id}'));
[firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L44-L53)

```

```
// Add a new document with a generated ID
Future<DocumentReference> user_ref =
    db->Collection("users").Add({{"first", FieldValue::String("Ada")},
                                 {"last", FieldValue::String("Lovelace")},
                                 {"born", FieldValue::Integer(1815)}});

user_ref.OnCompletion([](const Future<DocumentReference>& future) {
  if (future.error() == Error::kErrorOk) {
    std::cout << "DocumentSnapshot added with ID: " << future.result()->id()
              << std::endl;
  } else {
    std::cout << "Error adding document: " << future.error_message() << std::endl;
  }
});
[snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L79-L92)

```

```
DocumentReference docRef = db.Collection("users").Document("alovelace");
Dictionary<string, object> user = new Dictionary<string, object>
{
	{ "First", "Ada" },
	{ "Last", "Lovelace" },
	{ "Born", 1815 },
};
docRef.SetAsync(user).ContinueWithOnMainThread(task => {
	Debug.Log("Added data to the alovelace document in the users collection.");
});
```

Now add another document to the `users` collection. Notice that this document includes a key-value pair (middle name) that does not appear in the first document. Documents in a collection can contain different sets of information.
[Web version 9](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-9-modular)[Web version 8](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-8-namespaced)[Swift](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#swift)[Objective-C](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#objective-c)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#java-android) More
[Dart](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#dart-flutter)[C++](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#c++)[Unity](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#unity)

```
// Add a second document with a generated ID.
import { addDoc, collection } from "firebase/firestore"; 

try {
  const docRef = await addDoc(collection(db, "users"), {
    first: "Alan",
    middle: "Mathison",
    last: "Turing",
    born: 1912
  });

  console.log("Document written with ID: ", docRef.id);
} catch (e) {
  console.error("Error adding document: ", e);
}
[add_alan_turing.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/add_alan_turing.js#L8-L22)

```

```
// Add a second document with a generated ID.
db.collection("users").add({
    first: "Alan",
    middle: "Mathison",
    last: "Turing",
    born: 1912
})
.then((docRef) => {
    console.log("Document written with ID: ", docRef.id);
})
.catch((error) => {
    console.error("Error adding document: ", error);
});
[test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L155-L167)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
// Add a second document with a generated ID.
do {
  let ref = try await db.collection("users").addDocument(data: [
    "first": "Alan",
    "middle": "Mathison",
    "last": "Turing",
    "born": 1912
  ])
  print("Document added with ID: \(ref.documentID)")
} catch {
  print("Error adding document: \(error)")
}
[ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L188-L199)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
// Add a second document with a generated ID.
__block FIRDocumentReference *ref =
    [[self.db collectionWithPath:@"users"] addDocumentWithData:@{
      @"first": @"Alan",
      @"middle": @"Mathison",
      @"last": @"Turing",
      @"born": @1912
    } completion:^(NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error adding document: %@", error);
      } else {
        NSLog(@"Document added with ID: %@", ref.documentID);
      }
    }];
[ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L110-L123)

```

```
// Create a new user with a first, middle, and last name
val user = hashMapOf(
    "first" to "Alan",
    "middle" to "Mathison",
    "last" to "Turing",
    "born" to 1912,
)

// Add a new document with a generated ID
db.collection("users")
    .add(user)
    .addOnSuccessListener { documentReference ->
        Log.d(TAG, "DocumentSnapshot added with ID: ${documentReference.id}")
    }
    .addOnFailureListener { e ->
        Log.w(TAG, "Error adding document", e)
    }
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L158-L174)

```

```
// Create a new user with a first, middle, and last name
Map<String, Object> user = new HashMap<>();
user.put("first", "Alan");
user.put("middle", "Mathison");
user.put("last", "Turing");
user.put("born", 1912);

// Add a new document with a generated ID
db.collection("users")
        .add(user)
        .addOnSuccessListener(new OnSuccessListener<DocumentReference>() {
            @Override
            public void onSuccess(DocumentReference documentReference) {
                Log.d(TAG, "DocumentSnapshot added with ID: " + documentReference.getId());
            }
        })
        .addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Log.w(TAG, "Error adding document", e);
            }
        });
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L190-L211)

```

```
// Create a new user with a first and last name
final user = <String, dynamic>{
  "first": "Alan",
  "middle": "Mathison",
  "last": "Turing",
  "born": 1912
};

// Add a new document with a generated ID
db.collection("users").add(user).then((DocumentReference doc) =>
    print('DocumentSnapshot added with ID: ${doc.id}'));
[firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L59-L69)

```

```
db->Collection("users")
    .Add({{"first", FieldValue::String("Alan")},
          {"middle", FieldValue::String("Mathison")},
          {"last", FieldValue::String("Turing")},
          {"born", FieldValue::Integer(1912)}})
    .OnCompletion([](const Future<DocumentReference>& future) {
      if (future.error() == Error::kErrorOk) {
        std::cout << "DocumentSnapshot added with ID: "
                  << future.result()->id() << std::endl;
      } else {
        std::cout << "Error adding document: " << future.error_message()
                  << std::endl;
      }
    });
[snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L101-L114)

```

```
DocumentReference docRef = db.Collection("users").Document("aturing");
Dictionary<string, object> user = new Dictionary<string, object>
{
	{ "First", "Alan" },
	{ "Middle", "Mathison" },
	{ "Last", "Turing" },
	{ "Born", 1912 }
};
docRef.SetAsync(user).ContinueWithOnMainThread(task => {
	Debug.Log("Added data to the aturing document in the users collection.");
});
```

## Read data
Use the data viewer in the [Firebase console](https://console.firebase.google.com/project/_/firestore/data) to quickly verify that you've added data to Firestore.
You can also use the `get` method to retrieve the entire collection.
[Web version 9](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-9-modular)[Web version 8](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web-version-8-namespaced)[Swift](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#swift)[Objective-C](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#objective-c)[Kotlin](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#kotlin-android)[Java](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#java-android) More
[Dart](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#dart-flutter)[C++](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#c++)[Unity](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#unity)

```
import { collection, getDocs } from "firebase/firestore"; 

const querySnapshot = await getDocs(collection(db, "users"));
querySnapshot.forEach((doc) => {
  console.log(doc.id, "=>", doc.data());
});
[get_all_users.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/get_all_users.js#L8-L13)

```

```
db.collection("users").get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        console.log(doc.id, "=>", doc.data());
    });
});
[test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L143-L147)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
do {
  let snapshot = try await db.collection("users").getDocuments()
  for document in snapshot.documents {
    print("\(document.documentID) => \(document.data())")
  }
} catch {
  print("Error getting documents: \(error)")
}
[ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L205-L212)

```

**Note:** This product is not available on watchOS and App Clip targets. 

```
[[self.db collectionWithPath:@"users"]
    getDocumentsWithCompletion:^(FIRQuerySnapshot * _Nullable snapshot,
                                 NSError * _Nullable error) {
      if (error != nil) {
        NSLog(@"Error getting documents: %@", error);
      } else {
        for (FIRDocumentSnapshot *document in snapshot.documents) {
          NSLog(@"%@ => %@", document.documentID, document.data);
        }
      }
    }];
[ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L129-L139)

```

```
db.collection("users")
    .get()
    .addOnSuccessListener { result ->
        for (document in result) {
            Log.d(TAG, "${document.id} => ${document.data}")
        }
    }
    .addOnFailureListener { exception ->
        Log.w(TAG, "Error getting documents.", exception)
    }
[DocSnippets.kt](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L180-L189)

```

```
db.collection("users")
        .get()
        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                if (task.isSuccessful()) {
                    for (QueryDocumentSnapshot document : task.getResult()) {
                        Log.d(TAG, document.getId() + " => " + document.getData());
                    }
                } else {
                    Log.w(TAG, "Error getting documents.", task.getException());
                }
            }
        });
[DocSnippets.java](https://github.com/firebase/snippets-android/blob/4d625814cc35f931646387cd6211a213382b9740/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L217-L230)

```

```
await db.collection("users").get().then((event) {
  for (var doc in event.docs) {
    print("${doc.id} => ${doc.data()}");
  }
});
[firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L75-L79)

```

```
Future<QuerySnapshot> users = db->Collection("users").Get();
users.OnCompletion([](const Future<QuerySnapshot>& future) {
  if (future.error() == Error::kErrorOk) {
    for (const DocumentSnapshot& document : future.result()->documents()) {
      std::cout << document << std::endl;
    }
  } else {
    std::cout << "Error getting documents: " << future.error_message()
              << std::endl;
  }
});
[snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L131-L141)

```

```
CollectionReference usersRef = db.Collection("users");
usersRef.GetSnapshotAsync().ContinueWithOnMainThread(task =>
{
  QuerySnapshot snapshot = task.Result;
  foreach (DocumentSnapshot document in snapshot.Documents)
  {
    Debug.Log(String.Format("User: {0}", document.Id));
    Dictionary<string, object> documentDictionary = document.ToDictionary();
    Debug.Log(String.Format("First: {0}", documentDictionary["First"]));
    if (documentDictionary.ContainsKey("Middle"))
    {
      Debug.Log(String.Format("Middle: {0}", documentDictionary["Middle"]));
    }

    Debug.Log(String.Format("Last: {0}", documentDictionary["Last"]));
    Debug.Log(String.Format("Born: {0}", documentDictionary["Born"]));
  }

  Debug.Log("Read all data from the users collection.");
});
```

## Secure your data
Use [Firebase Authentication](https://firebase.google.com/docs/auth/) and [Firestore Security Rules](https://docs.cloud.google.com/firestore/native/docs/security/get-started) to secure your data in Firestore in Native Mode.
Here are some basic rule sets you can use to get started. You can modify your security rules from the Firebase console in the **Databases & Storage** > **Firestore** > [**Rules** tab](https://console.firebase.google.com/project/_/firestore/rules).
[Auth required](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#auth-required)[Locked mode](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#locked-mode)[Test mode](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#test-mode) More

```
// Allow read/write access on all documents to any user signed in to the application
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if request.auth != null;
    }
  }
}

```

```
// Deny read/write access to all users under any conditions
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}

```

```
// Allow read/write access to all users under any conditions
// Warning: **NEVER** use this rule set in production; it allows
// anyone to overwrite your entire database.
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}

```

Before you deploy your Web, Android, or iOS app to production, also take steps to ensure that only your app clients can access your Firestore in Native Mode data. See the [App Check](https://firebase.google.com/docs/app-check) documentation.
## Watch a video tutorial
For detailed guidance on getting started with the Firestore mobile and web client libraries, watch one of the following video tutorials:
[Web](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#web)[iOS](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#ios)[Android](https://docs.cloud.google.com/firestore/native/docs/create-database-web-mobile-client-library/#android) More
You can find more videos in the Firebase [YouTube channel](https://www.youtube.com/firebase).
## Next steps
Deepen your knowledge with the following topics:
  * **Codelabs** — Learn to use Firestore in Native Mode in a real app by following the codelab for [Android](https://codelabs.developers.google.com/codelabs/firestore-android), [iOS](https://codelabs.developers.google.com/codelabs/firestore-ios), or [Web](https://codelabs.developers.google.com/codelabs/firestore-web).
  * **[Data model](https://docs.cloud.google.com/firestore/native/docs/data-model)** — Learn more about how data is structured in Firestore, including hierarchical data and subcollections.
  * **[Add data](https://docs.cloud.google.com/firestore/native/docs/manage-data/add-data)** — Learn more about creating and updating data in Firestore.
  * **[Get data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data)** — Learn more about how to retrieve data.
  * **[Perform simple and compound queries](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)** — Learn how to run simple and compound queries.
  * **[Order and limit queries](https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data)** — Learn how to order and limit the data returned by your queries.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
