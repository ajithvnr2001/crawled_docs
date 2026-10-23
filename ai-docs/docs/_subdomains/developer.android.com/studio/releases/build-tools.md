---
url: https://developer.android.com/studio/releases/build-tools/
title: SDK Build Tools release notes \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:45:45.867865+00:00
---

# SDK Build Tools release notes  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/releases/build-tools/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ SDK tools guides ](https://developer.android.com/tools)



#  SDK Build Tools release notes Stay organized with collections  Save and categorize content based on your preferences. 

Android SDK Build-Tools is a component of the Android SDK required for building Android apps. It's installed in the `<sdk>/build-tools/` directory.

You should always keep your Build Tools component updated by downloading the latest version using the [Android SDK Manager](https://developer.android.com/studio/intro/update). If you're using [Android plugin for Gradle 3.0.0](https://developer.android.com/studio/releases/gradle-plugin#3-0-0) or higher, your project automatically uses a default version of the build tools that the plugin specifies. To use a different version of the build tools, specify it using [`buildToolsVersion`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.AppExtension.html#com.android.build.gradle.AppExtension:buildToolsVersion) in your module's `build.gradle`, as follows:

### Groovy
    
    
    android {
        buildToolsVersion "36.0.0"
        ...
    }

### Kotlin
    
    
    android {
        buildToolsVersion = "36.0.0"
        ...
    }

## Revisions

The sections below provide notes about releases of the Build Tools. To determine which revisions of the Build Tools are available in your SDK, refer to the _Installed Packages_ listing in the Android SDK Manager.

Build Tools, Revision 34.0.0 RC3 _(April 2023)_

General bug fixes and improvements.

Build Tools, Revision 34.0.0 _(February 2023)_

This update includes support for building with Android 14 preview APIs.

Build Tools, Revision 33.0.2 _(February 2023)_

This update fixes the following issue:

  * `core-lambda-stubs.jar` version 33.0.0 differs on macOS versus Linux/Windows. (See [issue #237299698](https://issuetracker.google.com/issues/237299698).) 



Build Tools, Revision 33.0.1 _(November 2022)_

This update fixes the following issue:

  * AIDL fails with build-tools 33.0.0. (See [issue #236167971](https://issuetracker.google.com/issues/236167971)) 



Build Tools, Revision 30.0.0 rc4 _(May 2020)_

This update includes support for building with Android 11 Preview APIs.

Build Tools, Revision 29.0.3 _(January 2020)_

This update fixes the following issue:

  * Build issue with Renderscript on macOS Catalina. (See [issue #142590626](https://issuetracker.google.com/issues/142590626)) 



Build Tools, Revision 29.0.2 _(August 2019)_

This update fixes the following issue:

  * [librsjni_androidx.so SIGSEGV](https://issuetracker.google.com/issues/133169129)



Build Tools, Revision 29.0.0 _(June 2019)_

This update includes support for building with API level 29.

Build Tools, Revision 28.0.3 _(September 2018)_

This update includes support for [Android Gradle plugin 3.2.0](https://developer.android.com/studio/releases/gradle-plugin#3-2-0) and fixes the following issues:

  * Fixed a JNI library bug that caused apps to crash when calling `androidx.renderscript.RenderScript.create()`. 
  * Fixed a bug that caused `Program type already present` build errors with `androidx.annotation` resources. 



Build Tools, Revision 28.0.2 _(August 2018)_

Includes the latest version of [D8](https://developer.android.com/studio/command-line/d8).

Build Tools, Revision 27.0.3 _(December 2017)_

Improves support for compiling lambdas when you enable [Java 8 language features](https://developer.android.com/studio/write/java8-support).

Build Tools, Revision 27.0.2 _(December 2017)_

Improves support for [Java 8 language features](https://developer.android.com/studio/write/java8-support).

Build Tools, Revision 27.0.1 _(November 2017)_

Adds support for legacy multidex for test APKs. ([Issue #37324038](https://issuetracker.google.com/37324038)) 

Build Tools, Revision 26.0.2 _(October 2017)_

In addition to general bug fixes, this release includes the following updates:

  * Updates `apksigner` to version 0.8: 
    * Compatibility with Java 9. ([Issue #37137869](https://issuetracker.google.com/issues/37137869)) 
    * New `--pass-encoding` parameter to handle keystores and keys that are encrypted using non-ASCII passwords. If you switch to Java 9 and `apksigner` fails to decrypt your keystore or key, use this parameter to specify the character encoding you used to create the keystore or key. For more information, see the [`apksigner` documentation](https://developer.android.com/studio/command-line/apksigner#options-sign-key-cert) or run `apksigner sign --help` from the commandline. 
    * Better error message when `apksigner` can't verify a JAR signature due to an unsupported digest or signature algorithm. ([Issue #63525618](https://issuetracker.google.com/issues/63525618)) 
  * Support for AAPT2 daemon mode when using [Android plugin for Gradle `3.0.0-beta7`](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration) or higher. 



Build Tools, Revision 26.0.1 _(July 2017)_

In addition to general bug fixes, this release restores `apksigner` to the build tools package (it was omitted by mistake in version 26.0.0) and includes the following updates to the tool:

  * Adds PKCS #11 support to allow signing with keys held in secure hardware. ([Issue #37140484](https://issuetracker.google.com/issues/37140484)) 
  * Adds support for loading additional [JCA Providers](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#Provider) before signing. 
  * Honors `[android:targetSandboxVersion](https://developer.android.com/reference/android/R.attr#targetSandboxVersion)` when verifying APKs. 
  * When signing, rejects APKs with files that include 'CR' (carriage return), 'LF' (line feed), or 'NUL' (null) special characters in the file name. 
  * Fixes `apksigner.bat` to correctly handle parameters containing spaces. ([Issue #38132450](https://issuetracker.google.com/issues/38132450))
  * Fixes a bug in JAR signature verification when multiple digests are present for the same entry in `MANIFEST.MF`. ([Issue #38497270](https://issuetracker.google.com/issues/38497270)) 



Build Tools, Revision 26.0.0 _(June 2017)_

Adds support for building with API level 26 and contains general bug fixes.

Build Tools, Revision 25.0.3 _(April 2017)_

Updates to `apksigner`:

  * Added `--in` parameter for symmetry with existing `--out` parameter.
  * If you do not specify the key password using `--key-pass`, `apksigner` uses the keystore password as key password. However, if the key requires a different password, you are now prompted to enter the key password from the command line. ([Issue #37134986](https://issuetracker.google.com/issues/37134986))
  * Added compatibility with `jarsigner` for non-ASCII passwords. ([Issue #37135737](https://issuetracker.google.com/issues/37135737))



Build Tools, Revision 25.0.2 _(December 2016)_

Bug fixes.

Build Tools, Revision 25.0.1 _(November 2016)_

This release includes bug fixes and the following improvements to `apksigner`:

  * Support for APKs with obfuscated JAR entry names.
  * `--print-certs` switch now also dumps MD5 fingerprints.



Build Tools, Revision 25.0.0 _(October 2016)_

Bug fixes for the Jack toolchain: 

  * Fixed issue with Jack supporting non-ASCII source files. ([Issue #218892](https://code.google.com/p/android/issues/detail?id=218892)) 
  * Fixed issue that causes an `AssertionError` during some compilations. ([Issue #208414](https://code.google.com/p/android/issues/detail?id=208414)) 



Build Tools, Revision 24.0.3 _(September 2016)_

  * Added [ `apksigner`](https://developer.android.com/studio/command-line/apksigner), an APK signing tool to replace `jarsigner`. By default, `apksigner` signs APKs using the conventional JAR signing scheme (used by `jarsigner`) and the [APK Signature Scheme v2](https://developer.android.com/about/versions/nougat/android-7.0#apk_signature_v2) introduced in Android 7.0 (API level 24). Any modification to an APK signed with APK Signature Scheme v2 invalidates its signature. Thus, APK post-processing, such as `zipalign`, must be performed before `apksigner` is invoked, not after. Invoking `zipalign` before `apksigner` works fine because `apksigner` preserves APK alignment and compression (unlike `jarsigner`).



Build Tools, Revision 23.0.3 _(March 2016)_

  * Fix issues in the [RenderScript](https://developer.android.com/guide/topics/renderscript/compute) Support Library on arm64 devices.
  * Fix issues in the [RenderScript](https://developer.android.com/guide/topics/renderscript/compute) Support Library on certain Jelly Bean devices.
  * Support `renderscriptTargetAPI 21+` when using Android Plugin for Gradle, Revision 2.1.0 and above .



Build Tools, Revision 23.0.2 _(November 2015)_

  * Improved the merging performance of the `dx` tool.
  * Fixed issues in the [RenderScript](https://developer.android.com/guide/topics/renderscript/compute) compiler for Windows.



Build Tools, Revision 23.0.1 _(October 2015)_

Fixed issues in the RenderScript tools.

Build Tools, Revision 23.0.0 _(August 2015)_

Added support for the Android 6.0 (API level 23) release.

Build Tools, Revision 22.0.1 _(March 2015)_

Fixed compatibility issues with [RenderScript](https://developer.android.com/guide/topics/renderscript/compute) kernels on Android 4.4 (API level 19) to Android 4.1 (API level 16) devices.

Build Tools, Revision 22.0.0 _(March 2015)_

Added support for Android 5.1 (API level 22).

Build Tools, Revision 21.1.2 _(February 2015)_

Fixed problem with building data layouts in 32-bit mode.

Build Tools, Revision 21.1.1 _(November 2014)_

Fixed multidex script issues.

Build Tools, Revision 21.1 _(October 2014)_

Added multidex file support for APKs and Jack support to address the 64K method reference limit.

Build Tools, Revision 21.0.2 _(October 2014)_

Complete updates for Eclipse ADT to solve instability issues on Windows platforms.

Build Tools, Revision 21.0.1 _(October 2014)_

Initial updates for Eclipse ADT on Windows. Please use Revision 21.0.2.

Build Tools, Revision 21.0.0 _(October 2014)_

General Notes:
    

  * Added support for Android 5.0 (API level 21).
  * RenderScript now supports seamless 32/64-bit operation for API level 21 and higher.
  * Fixed issue with the Gradle build system when using the JaCoCo plugin. ([Issue 69174](http://b.android.com/69174))
  * Added an _input-list_ option for use with long command lines on Windows.



Build Tools, Revision 20.0.0 _(June 2014)_

General Notes:
    

  * Added support for Android Wear.



Build Tools, Revision 19.1.0 _(May 2014)_

General Notes:
    

  * Added `zipalign` to the Build Tools.
  * Modified `aapt` to ignore XML files that fail to compile.



Build Tools, Revision 19.0.3 _(March 2014)_

Fixed an issue with RenderScript support.

Build Tools, Revision 19.0.2 _(February 2014)_

Fixed RenderScript build issues:
    

  * Fixed a problem with RenderScript bitcode encoding. ([Issue 64775](http://b.android.com/64775)) 
  * Fixed a problem with RenderScript missing math symbols ([Issue 64110](http://b.android.com/64110)) 



Build Tools, Revision 19.0.1 _(December 2013)_

Fixed miscellaneous build issues:
    

  * Fixed support for compiling RenderScript in NDK mode with Gradle.
  * Fixed `BufferOverflowException` problem in the dx build. ([Issue 61710](http://b.android.com/61710)) 



Build Tools, Revision 19 _(October 2013)_

Added support for Android 4.4 (API level 19) build targets.

Build Tools, Revision 18.1.1 _(September 2013)_

Fixed several minor build issues.

Build Tools, Revision 18.1.0 _(September 2013)_

Fixed issue with RenderScript support mode.

Build Tools, Revision 18.0.1 _(July 2013)_

Added support for Android 4.3 (API level 18) build targets.

Build Tools, Revision 17 _(May 2013)_

Initial release.

General Notes:
    

  * Included support for Android 4.2 (API level 17) build targets.
  * Decoupled the build-specific components of the Android SDK from the platform-tools component, so that the build tools can be updated independently of the integrated development environment (IDE) components.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
