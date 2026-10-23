---
url: https://developer.android.com/codelabs/kmp-get-started/
title: Get Started With Kotlin Multiplatform \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:31.651371+00:00
---

# Get Started With Kotlin Multiplatform  |  Android Developers

> Source: https://developer.android.com/codelabs/kmp-get-started/

  * [ Android Developers ](https://developer.android.com/)



#  Get Started With Kotlin Multiplatform Stay organized with collections  Save and categorize content based on your preferences. 

##  1\. Before you begin 

## **Prerequisites**

  * Knowledge of how to build Jetpack Compose apps.
  * Experience with Kotlin.
  * Basic understanding of [Swift syntax](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html).



## **What you need**

  * The latest [stable version of Android Studio](https://developer.android.com/studio/) (Meerkat or higher).
  * A macOS system with [Xcode 16.1 and iPhone simulator](https://developer.apple.com/documentation/safari-developer-tools/installing-xcode-and-simulators) with iOS 16.0 or higher.



## **What you will learn**

  * Understand the basics of Kotlin Multiplatform.
  * How to share code across platforms.
  * How to connect the shared code on Android and iOS.



**Note:** If you don't have a Mac machine, you're not able to build the iOS part of this app. You're still able to follow the Android and shared part of the codebase.

##  2\. Get set up 

To get started, follow these steps:

  1. Clone the [GitHub repository](https://github.com/android/codelab-android-kmp):


    
    
    $ git clone https://github.com/android/codelab-android-kmp.git
    

Alternatively, you can download the repository as a zip file:

[file_downloadDownload the repository](https://github.com/android/codelab-android-kmp/archive/refs/heads/main.zip)

  2. In **Android Studio** , open the **`get-started`** project, which contains the following branches:


  * `main`: Contains the starter code for this project, where you make changes to complete the codelab.
  * `end`: Contains the solution code for this codelab.



**Note:** The git repository contains also other codelabs, use the **get-started** project.

This codelab begins with the `main` branch. You can follow the codelab step-by-step at your own pace.

  3. If you want to see the solution code, run this command:


    
    
    $ git clone -b end https://github.com/android/codelab-android-kmp.git
    

Alternatively, you can download the solution code:

[file_downloadDownload the solution code](https://github.com/android/codelab-android-kmp/archive/refs/heads/end.zip)

## **Install Xcode**

To build and run the iOS part of this codelab, you need Xcode and an iOS simulator:

  1. If you haven't done so, you might need to [create an Apple account](https://support.apple.com/108647).
  2. Install [Xcode](https://apps.apple.com/us/app/xcode/id497799835) from the Mac App Store (for this you need an Apple account).
  3. Once installed, launch Xcode.
  4. A dialog will be presented that indicates which components are built-in, and which you need to download. ![c4aba94d795dabee.png](https://developer.android.com/static/codelabs/kmp-get-started/img/c4aba94d795dabee.png)
  5. Check the iOS 18.4 (or newer).
  6. Click Download & Install.
  7. Wait until the components are installed.



**Note** : Downloading and installing Xcode may take a while as it's a large binary.

This codelab was tested with Xcode 16.3. If you use any other Xcode version, and if you're running into issues, then we recommend downloading the exact version as mentioned in this codelab.

## The sample app

This codebase contains both an Android app built with [Jetpack Compose](https://d.android.com/compose) and an iOS app built with [SwiftUI](https://developer.apple.com/xcode/swiftui/). The Android project is located in the `androidApp/` folder, whereas the iOS project is located in the `iosApp/` folder that also contains the `KMPGetStartedCodelab.xcodeproj` to run with [Xcode](https://developer.apple.com/xcode/).

##  3\. Introduction to Kotlin Multiplatform 

Kotlin Multiplatform (KMP) allows you to write code once and share it across multiple target platforms, such as Android, iOS, Web, and Desktop. By leveraging KMP, you can minimize code duplication, maintain consistency, and significantly reduce development time and effort.

KMP doesn't dictate how much or what parts of your codebase you need to share. It is up to you to decide which parts of the code are worth sharing.

## **Deciding on what to share**

This shared code enables you to maintain consistency and reduce duplication across platforms. Many mobile teams start by sharing a discrete set of business logic (e.g., database access, network access, etc.) and the associated tests, and then sharing additional code over time.

Many Android Jetpack libraries have support for KMP. Jetpack libraries that have been made multiplatform offer multiple tiers of support depending on the target platform. For the full list of libraries and their support levels, see the [documentation](https://developer.android.com/kotlin/multiplatform#supported-platforms).

For example, one of the [supported libraries](https://developer.android.com/kotlin/multiplatform#multiplatform-jetpack), the Room database library, supports both Android, iOS & Desktop. This allows you to port the database creation and related database logic to a common KMP shared module while preserving the other native code on both platforms.

A possible next step after migrating the database would be _to share other_[ _domain logic_](https://developer.android.com/topic/architecture/domain-layer). Then, you may also consider using the `ViewModel` multiplatform [library](https://developer.android.com/jetpack/androidx/releases/lifecycle) from Android Jetpack.

## **How to write platform-specific code**

Kotlin Multiplatform introduces new techniques for implementing platform-specific functionality.

### **Expect and actual declarations**

The [`expect`](https://kotlinlang.org/docs/multiplatform-expect-actual.html) [`actual`](https://kotlinlang.org/docs/multiplatform-expect-actual.html) Kotlin language feature is designed to support Kotlin multiplatform codebase with full IDE support.

This approach is ideal when the platform-specific behavior can be encapsulated in a single function or class. It's a flexible and powerful mechanism. For example, a common `expect` class can have platform-specific `actual` counterparts with more open visibility modifiers, additional super types, or different parameter types or modifiers. These kinds of variations wouldn't be possible with a strict interface API. Moreover, _`expect`_ _`actual`_ is statically resolved, meaning the platform-specific implementation is enforced at compile time.

**Note:** expect/actual classes are currently an experimental feature. You can also implement an interface of expect/actual functions. See the [documentation](https://kotlinlang.org/docs/multiplatform-expect-actual.html) for all options.

### **Interface and Implementations in Kotlin**

If both platforms need to follow similar APIs but with different implementations, you can define an interface in shared code as an alternative to expected and actual declarations.This approach enables you to use different testing implementations, or switch to a different implementation at runtime.

Additionally, interfaces require no Kotlin-specific knowledge, making this option approachable for developers familiar with interfaces in other languages.

### **Interface in common shared code, implementation in native code (Android or Swift).**

In some cases you need to write code that isn't available from KMP code. In this situation you can define an interface in shared code, implement it for Android in Kotlin, and provide an iOS counterpart in Swift. Typically, the native implementations are then injected into the shared code, either by dependency injection or directly. This strategy allows for a customized experience on each platform while maintaining a common interface for shared code.

##  4\. Open the Xcode project from Android Studio 

**Note:** You can also continue with the codelab and get back here once you're ready to integrate the iOS part.

Once Xcode is installed, you should make sure that you can run the iOS app.

You can open the iOS project directly from Android Studio.

  1. Switch the Project pane to use the **Project View**![4f1a2c2ad988334c.png](https://developer.android.com/static/codelabs/kmp-get-started/img/4f1a2c2ad988334c.png)
  2. Find the **KmpGetStartedCodelab.xcodeproj** file in **[root]/iosApp/** folder ![1357ffb58fe05180.png](https://developer.android.com/static/codelabs/kmp-get-started/img/1357ffb58fe05180.png)
  3. Right-click the file and select **Open In** and **Open in Associated Application**. This will open the iOS app in Xcode. ![f93dee415dfd40e9.png](https://developer.android.com/static/codelabs/kmp-get-started/img/f93dee415dfd40e9.png)
  4. Run the project in Xcode by clicking ⌘+R or navigating to Product menu and select Run



![fff7f322c13ccdc0.png](https://developer.android.com/static/codelabs/kmp-get-started/img/fff7f322c13ccdc0.png).

**Note:** You can also open the Xcode project by finding the **KmpGetStarted.xcodeproj** file in Finder and double-click it to launch as an app.

##  5\. Add a KMP module 

To add KMP support to your project, first create a `shared` module for the code that will be reused across platforms (Android, iOS).

Android Studio provides a way to add a Kotlin Multiplatform module using its KMP Shared module template.

To create the KMP module, in Android Studio:

  1. Navigate to **File > New > New Module > Kotlin Multiplatform Shared Module**
  2. Change the package to `com.example.kmp.shared`
  3. Click **Finish**![4ef605dcc1fe6301.png](https://developer.android.com/static/codelabs/kmp-get-started/img/4ef605dcc1fe6301.png)
  4. Once the module creation completes and Gradle finishes syncing, a new `shared` module will appear in the project. To see the view shown below, you may need to switch from Android View to Project View.



![eb58eea4e534dab2.png](https://developer.android.com/static/codelabs/kmp-get-started/img/eb58eea4e534dab2.png)

The shared module generated by the KMP Shared module template includes some basic placeholder functions and tests. These placeholders ensure that the module compiles and runs successfully from the start.

Important: Keep in mind the difference between the iosApp folder and the iosMain folder. The iosApp folder contains the standalone iOS app code whereas the iosMain is part of the KMP shared module that you just added. iosApp contains Swift code while iosMain contains iOS platform-specific KMP code.

## **Link the shared module to the Android app**

First, you need to link the new shared module as a dependency in the `:androidApp` Gradle module to enable the app to use the shared code:

  1. Open the `androidApp/build.gradle.kts` file
  2. Add the `shared` module dependency in the dependencies block as follows


    
    
    dependencies {
        ...
        implementation(projects.shared)
    }
    

**Note:** Because the project has Gradle's [Type-safe project accessors](https://docs.gradle.org/current/userguide/declaring_dependencies_basics.html#sec:type-safe-project-accessors) feature enabled, you can access the `shared` module with `projects.shared.`Without the type-safe accessors feature, you can access the module using `implementation(project(":shared"))`.

  3. Sync the project with its Gradle files ![c4a6ca72cf444e6e.png](https://developer.android.com/static/codelabs/kmp-get-started/img/c4a6ca72cf444e6e.png)



## Verify code access to the `shared` **module**

To verify that the Android app can access code from the `shared` module, we'll make a simple update to the app.

  1. In the KMPGetStartedCodelab project, open the `MainActivity` file at `androidApp/src/main/java/com/example/kmp/getstarted/android/MainActivity.kt`
  2. Modify the content `Text` composable to include the `platform()` information in the displayed string.


    
    
    Text(
      "Hello ${platform()}",
    )
    

  3. Click `⌥(option)+return` on your keyboard and select `Import function 'platform'`![da301d17884eaef9.png](https://developer.android.com/static/codelabs/kmp-get-started/img/da301d17884eaef9.png)
  4. Build and run the app on an Android device or emulator.



This update checks whether the app can call the `platform()` function from the `shared` module, which should return `"Android"` when running on the Android platform.

![9828afe63d7cd9da.png](https://developer.android.com/static/codelabs/kmp-get-started/img/9828afe63d7cd9da.png)

##  6\. Set up the shared module to the iOS app 

Swift can't use Kotlin modules directly like the Android apps do, and requires a [compiled binary framework](https://developer.apple.com/documentation/xcode/creating-a-multi-platform-binary-framework-bundle) (XCFramework bundle) to be produced. An XCFramework bundle is a binary package that includes the frameworks and libraries necessary to build for multiple Apple platforms.

## **How the shared library is distributed**

The new module template in Android Studio already configured the shared module to produce a framework for each of the iOS architectures. You can find the following code in the `shared` module's `build.gradle.kts` file.
    
    
    val xcfName = "sharedKit"
    
    iosX64 {
      binaries.framework {
        baseName = xcfName
      }
    }
    
    iosArm64 {
      binaries.framework {
        baseName = xcfName
      }
    }
    
    iosSimulatorArm64 {
      binaries.framework {
        baseName = xcfName
      }
    }
    

**Note:** The output framework is called `sharedKit` by default based on the name of the module mentioned in the KMP template (and above), and this name is controlled by the `xcfName` property in the shared module's `build.gradle.kts` file. In your own project, you may rename this to match the name of the Framework that may define the brand or identity associated with the framework.

## Link the shared library in the iOS project

This step involves setting up Xcode to run a script to generate the Kotlin framework, and calling the `platform()` function in the iOS app.

For consuming the shared library, you need to connect the Kotlin framework to the iOS project with the following steps:

  1. Open the iOS project (the _`iosApp`_ directory mentioned previously) in Xcode and open the project settings by double-clicking the project name in the project navigator ![94047b06db4a3b6f.png](https://developer.android.com/static/codelabs/kmp-get-started/img/94047b06db4a3b6f.png)
  2. On the **Build Phases** tab of the project settings, click + and select **New Run Script Phase**. This adds a new "Run script" phase after all other phases. ![d4907a9cb0a5ac6e.png](https://developer.android.com/static/codelabs/kmp-get-started/img/d4907a9cb0a5ac6e.png)
  3. Double-click the **Run Script** title to rename it. Change the default **Run Script** name to **Compile Kotlin Framework** so it's understandable what this phase does.
  4. Unfold the build phase, and in the text field below **Shell** , enter the script code:


    
    
    cd "$SRCROOT/.."
    ./gradlew :shared:embedAndSignAppleFrameworkForXcode
    

![7b6a393e44ddbe60.png](https://developer.android.com/static/codelabs/kmp-get-started/img/7b6a393e44ddbe60.png)

  5. Drag the **Compile Kotlin Framework** phase **before** the **Compile Sources** phase. ![27dbe2cf958c986f.png](https://developer.android.com/static/codelabs/kmp-get-started/img/27dbe2cf958c986f.png)
  6. Build the project in Xcode by clicking ⌘+B or navigating to **Product menu** and select **Build**. Note that the build progress is shown on top of Xcode. ![bb0f9cb0f96d1f89.png](https://developer.android.com/static/codelabs/kmp-get-started/img/bb0f9cb0f96d1f89.png)



**Note:** If the build fails due with error: You have sandboxing for user scripts enabled perform the following steps:

  * In your Xcode project, navigate to "Build Setting",
  * Under "Build Options" set "User script sandboxing" (`ENABLE_USER_SCRIPT_SANDBOXING`) to `NO`.
  * Run `./gradlew --stop` to stop the Gradle daemon in the terminal
  * Rebuild the Xcode project



If everything is set up correctly, the project will successfully build.

![bb9b12d5f6ad0bac.png](https://developer.android.com/static/codelabs/kmp-get-started/img/bb9b12d5f6ad0bac.png)

Setting the run script build phase this way allows you to compile your iOS project from Xcode without the need to switch to a different tool to compile the shared module.

**Note:** If you make changes to the `shared` code, you won't immediately see the changes in Xcode until you rebuild the project, which triggers the `embedAndSignAppleFrameworkForXcode` Gradle task.

## Verify code access to the `shared` **module**

To verify that the iOS app can successfully access code from the `shared` module, you'll make the same simple update to the app that you made for the Android app.

  1. In the iOS project, in Xcode, open the `ContentView.swift` file at: `Sources/View/ContentView.swift`
  2. Add `import sharedKit` at the top of the file.
  3. Modify the `Text` view to include the `Platform_iosKt.platform()` information in the displayed string with `\(Platform_iosKt.platform())`.



Here is the final result of the file:
    
    
    import SwiftUI
    import sharedKit 
    
    struct ContentView: View {
        var body: some View {
            VStack {
                Image(systemName: "globe")
                    .imageScale(.large)
                    .foregroundStyle(.tint)
                
                Text("Hello, \(Platform_iosKt.platform())!")
            }
            .padding()
        }
    }
    

  4. Run the app either by clicking ⌘+R, or navigate to the **Product** menu and click **Run.**



**Note:** You might see a warning shown after the build saying the Compile Kotlin script will be run during every build. You can ignore this warning.

_> Run script build phase ‘Compile Kotlin` will be run during every build because it does not specify any outputs. To address this issue, either add output dependencies to the script phase, or configure it to run in every build by unchecking "Based on dependency analysis" in the script phase._

This update checks whether the iOS app can call the `platform()` function from the shared module, which should return `"iOS"` when running on the iOS platform.

**Note:** The [string interpolation in Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/stringsandcharacters/#String-Interpolation) is using `\(code)` syntax.

![8024b5cc4bcd3f84.png](https://developer.android.com/static/codelabs/kmp-get-started/img/8024b5cc4bcd3f84.png)

##  7\. Add Swift/Kotlin Interface Enhancer (SKIE) 

By default the native interface Kotlin produces is an Objective-C header. Swift is directly compatible with Objective-C, but Objective-C doesn't include all the modern features of Swift or Kotlin.

This is also the reason why in the previous example, you couldn't use the `platform()` call directly in the Swift code – KMP can't generate a global function, because Objective-C doesn't support global functions, only static functions encapsulated in a class, which is why you need to add `Platform_iosKt`.

To make the interface more Swift-friendly, you can use the [Swift/Kotlin Interface Enhancer (SKIE)](https://skie.touchlab.co/) tool to improve the Swift interface of the `:shared` module.

The common features of SKIE are:

  * Better support for default arguments
  * Better support for sealed hierarchies (`sealed class`, `sealed interface`)
  * Better support for `enum class` with exhaustive handling in `switch` statements
  * Interoperability between `Flow` to `AsyncSequence`
  * Interoperability between `suspend fun` and `async func`



**Tip:** While this step is optional in your projects outside of this codelab, it is recommended to use SKIE as it removes many limitations the shared framework would have otherwise. For example, SKIE allows you to use Kotlin's `suspend` functions and `Flow` types in Swift directly, significantly improving the usability of the shared module for your iOS team.

  1. Add `co.touchlab.skie` Gradle plugin to the `libs.versions.toml` file:


    
    
    [versions]
    skie = "0.10.1"
    
    [plugins]
    skie = { id = "co.touchlab.skie", version.ref = "skie" }
    

  2. Add the plugin to the root `build.gradle.kts` file


    
    
    plugins {
       ...
       alias(libs.plugins.skie) apply false
    }
    

  3. Add the plugin to the `:shared` module `build.gradle.kts` file:


    
    
    plugins {
       ...
       alias(libs.plugins.skie)
    }
    

  4. Gradle sync the project



**Note:** The SKIE plugin collects anonymized analytics on the plugin usage. You can disable it by adding `skie.analytics { enabled = false }` to your `build.gradle.kts` file in the `:shared` module.

Read [https://skie.touchlab.co/Analytics](http://skie.touchlab.co/Analytics) for more information**.**

## **Remove the static function call**

Now when you rebuild the iOS app, you might not notice anything immediately, but you can remove the `Platform_iosKt` prefix and let the `platform()` function act as a global function.
    
    
    Text("Hello, KMP! \(platform())")
    

This works, because SKIE (among other features) leverages the Swift [**API Notes**](https://github.com/swiftlang/swift/tree/main/apinotes), which adds information about APIs to better consume it from Swift code.

##  8\. Congratulations 

Congratulations, you've added the first shared Kotlin Multiplatform code to Android and iOS projects. While this is only a minimal starting point, you're now able to start discovering more advanced features and use cases for sharing code with KMP.

## **What's next?**

Learn to use Jetpack Room to share a data layer between Android and iOS in the next [codelab](https://developer.android.com/codelabs/kmp-migrate-room).

## Learn more

  * Learn which Jetpack libraries [support KMP](https://developer.android.com/kotlin/multiplatform)
  * Check the official [Kotlin Multiplatform documentation](https://kotlinlang.org/docs/multiplatform-intro.html)



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
