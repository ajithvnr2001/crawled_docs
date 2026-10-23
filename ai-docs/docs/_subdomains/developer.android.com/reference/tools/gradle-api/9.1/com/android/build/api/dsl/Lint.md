---
url: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint/
title: Lint \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:04:13.676666+00:00
---

# Lint  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# Lint

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/Lint.kt+class:com.android.build.api.dsl.Lint)

Added in 7.0.0
    
    
    interface [Lint](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint)

* * *

DSL object for configuring lint options. Example:
    
    
    android {  
       lint {  
             // set to true to turn off analysis progress reporting by lint  
             quiet = true  
             // if true, stop the gradle build if errors are found  
             abortOnError = false  
             // set to true to have all release builds run lint on issues with severity=fatal  
             // and abort the build (controlled by abortOnError above) if fatal issues are found  
             checkReleaseBuilds = true  
             // if true, only report errors  
             ignoreWarnings = true  
             // if true, emit full/absolute paths to files with errors (true by default)  
             absolutePaths = true  
             // if true, check all issues, including those that are off by default  
             checkAllWarnings = true  
             // if true, treat all warnings as errors  
             warningsAsErrors = true  
             // turn off checking the given issue id's  
             disable += ['TypographyFractions', 'TypographyQuotes']  
             // turn on the given issue id's  
             enable += ['RtlHardcoded','RtlCompat', 'RtlEnabled']  
             // check *only* the given issue id's  
             checkOnly += ['NewApi', 'InlinedApi']  
             // if true, don't include source code lines in the error output  
             noLines = true  
             // if true, show all locations for an error, do not truncate lists, etc.  
             showAll = true  
             // whether lint should include full issue explanations in the text error output  
             explainIssues = false  
             // Fallback lint configuration (default severities, etc.)  
             lintConfig = file("default-lint.xml")  
             // if true, generate a text report of issues (false by default)  
             textReport = true  
             // file to write report to (if not specified, defaults to standard output)  
             textOutput file("$buildDir/reports/lint-results.txt")  
             // if true, generate an XML report for use by for example Jenkins  
             xmlReport true  
             // file to write report to (if not specified, defaults to lint-results.xml)  
             xmlOutput file("$buildDir/reports/lint-report.xml")  
             // if true, generate an HTML report (with issue explanations, sourcecode, etc)  
             htmlReport true  
             // optional path to HTML report (default will be lint-results.html in the builddir)  
             htmlOutput file("$buildDir/reports/lint-report.html")  
             // if true, generate a SARIF report (OASIS Static Analysis Results Interchange Format)  
             sarifReport true  
             // optional path to SARIF report (default will be lint-results.sarif in the builddir)  
             sarifOutput file("$buildDir/reports/lint-report.html")  
             // Set the severity of the given issues to fatal (which means they will be  
             // checked during release builds (even if the lint target is not included)  
             fatal 'NewApi', 'InlinedApi'  
             // Set the severity of the given issues to error  
             error 'Wakelock', 'TextViewEdits'  
             // Set the severity of the given issues to warning  
             warning 'ResourceAsColor'  
             // Set the severity of the given issues to ignore (same as disabling the check)  
             ignore 'TypographyQuotes'  
             // Set the severity of the given issues to informational  
             informational 'StopShip'  
             // Use (or create) a baseline file for issues that should not be reported  
             baseline file("lint-baseline.xml")  
             // Normally most lint checks are not run on test sources (except the checks  
             // dedicated to looking for mistakes in unit or instrumentation tests, unless  
             // ignoreTestSources is true). You can turn on normal lint checking in all  
             // sources with the following flag, false by default:  
             checkTestSources true  
             // Like checkTestSources, but always skips analyzing tests -- meaning that it  
             // also ignores checks that have explicitly asked to look at test sources, such  
             // as the unused resource check.  
             ignoreTestSources true  
             // Normally lint will skip generated sources, but you can turn it on with this flag  
             checkGeneratedSources true  
             // Whether lint should check all dependencies too as part of its analysis.  
             // Default is false.  
             checkDependencies true  
             // targetSdk version used when generating a lint report for a library.  
             // Must be equal or higher than main target SDK. Must be set for libraries only.  
             targetSdk 33  
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html))` Configures all aspects regarding target sdk used when generating a lint report for a library.  
  
### Public properties  
  
---  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[abortOnError](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#abortOnError\(\))` Whether lint should set the exit code of the process if errors are found  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[absolutePaths](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#absolutePaths\(\))` Whether lint should display full paths in the error output.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[baseline](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#baseline\(\))` The baseline file to use, if any.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[checkAllWarnings](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkAllWarnings\(\))` Whether lint should check all warnings, including those off by default  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[checkDependencies](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkDependencies\(\))` Whether lint should check all dependencies too as part of its analysis.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[checkGeneratedSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkGeneratedSources\(\))` Returns whether lint should run checks on generated sources.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[checkOnly](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkOnly\(\))` The exact set of issues to check set by `[checkOnly](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkOnly\(\))`.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[checkReleaseBuilds](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkReleaseBuilds\(\))` Whether lint should check for fatal errors during release builds.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[checkTestSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkTestSources\(\))` Whether lint should run all checks on test sources, instead of just the lint checks that have been specifically written to include tests (e.g. checks looking for specific test errors, or checks that need to consider testing code such as the unused resource detector)  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[disable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#disable\(\))` The set of issue IDs to suppress.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#enable\(\))` The set of issue IDs to enable.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[error](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#error\(\))` Issues that have severity overridden to 'error'  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[explainIssues](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#explainIssues\(\))` Whether lint should include explanations for issue errors.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[fatal](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#fatal\(\))` Issues that have severity overridden to 'fatal'  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[htmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlOutput\(\))` The optional path to where an HTML report should be written.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[htmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlReport\(\))` Whether we should write an HTML report.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[ignore](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignore\(\))` **This property is deprecated.** Ignore and disable are synonyms  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreTestFixturesSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreTestFixturesSources\(\))` Whether lint should ignore all testFixtures sources.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreTestSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreTestSources\(\))` Whether lint should ignore all test sources.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[ignoreWarnings](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreWarnings\(\))` Returns whether lint will only check for errors (ignoring warnings)  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[informational](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#informational\(\))` Issues that have severity overridden to 'informational'  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[lintConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#lintConfig\(\))` The default config file to use as a fallback.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[noLines](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#noLines\(\))` Whether lint should include the source lines in the output where errors occurred (true by default)  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[quiet](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#quiet\(\))` Whether lint should be quiet (for example, not write informational messages such as paths to report files written)  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[sarifOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifOutput\(\))` The optional path to where a SARIF report (OASIS Static Analysis Results Interchange Format) should be written.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[sarifReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifReport\(\))` Whether we should write a SARIF (OASIS Static Analysis Results Interchange Format) report.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[showAll](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#showAll\(\))` Whether lint should include all output (e.g. include all alternate locations, not truncating long messages, etc.)  
`[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?` |  `[targetSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdk\(\))` The target sdk version used when generating a lint report for a library.  
`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?` |  `[targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdkPreview\(\))` The target sdk preview version used when generating a lint report for a library.  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[textOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textOutput\(\))` The optional path to where a text report should be written.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[textReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textReport\(\))` Whether lint should write a text report.  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[warning](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#warning\(\))` Issues that have severity overridden to 'warning'  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[warningsAsErrors](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#warningsAsErrors\(\))` Whether lint should treat all warnings as errors  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[xmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlOutput\(\))` The optional path to where an XML report should be written.  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[xmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlReport\(\))` Whether we should write an XML report.  
  
## Public functions

### targetSdk

Added in 9.1.1
    
    
    fun [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdk\(kotlin.Function1\))(action: [TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/TargetSdkSpec).() -> [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

Configures all aspects regarding target sdk used when generating a lint report for a library. Must be equal or higher than main target SDK. Must be set for libraries only. See `[TargetSdkSpec](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/TargetSdkSpec)` for available options.

## Public properties

### abortOnError

Added in 7.1.0
    
    
    var [abortOnError](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#abortOnError\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should set the exit code of the process if errors are found

### absolutePaths

Added in 7.1.0
    
    
    var [absolutePaths](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#absolutePaths\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should display full paths in the error output. By default the paths are relative to the path lint was invoked from.

### baseline

Added in 7.1.0
    
    
    var [baseline](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#baseline\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The baseline file to use, if any. The baseline file is an XML report previously created by lint, and any warnings and errors listed in that report will be ignored from analysis.

If you have a project with a large number of existing warnings, this lets you set a baseline and only see newly introduced warnings until you get a chance to go back and address the "technical debt" of the earlier warnings.

### checkAllWarnings

Added in 7.1.0
    
    
    var [checkAllWarnings](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkAllWarnings\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should check all warnings, including those off by default

### checkDependencies

Added in 7.1.0
    
    
    var [checkDependencies](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should check all dependencies too as part of its analysis. Default is false.

### checkGeneratedSources

Added in 7.1.0
    
    
    var [checkGeneratedSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkGeneratedSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns whether lint should run checks on generated sources.

### checkOnly

Added in 7.0.0
    
    
    val [checkOnly](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkOnly\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The exact set of issues to check set by `[checkOnly](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkOnly\(\))`.

If empty, lint will detect the issues that are enabled by default plus any issues enabled via `[enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#enable\(\))` and without issues disabled via `[disable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#disable\(\))`.

### checkReleaseBuilds

Added in 7.1.0
    
    
    var [checkReleaseBuilds](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkReleaseBuilds\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should check for fatal errors during release builds. Default is true. If issues with severity "fatal" are found, the release build is aborted.

### checkTestSources

Added in 7.1.0
    
    
    var [checkTestSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkTestSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should run all checks on test sources, instead of just the lint checks that have been specifically written to include tests (e.g. checks looking for specific test errors, or checks that need to consider testing code such as the unused resource detector)

### disable

Added in 7.0.0
    
    
    val [disable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#disable\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of issue IDs to suppress. Callers are allowed to modify this collection.

### enable

Added in 7.0.0
    
    
    val [enable](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#enable\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

The set of issue IDs to enable. Callers are allowed to modify this collection.

### error

Added in 7.1.0
    
    
    val [error](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#error\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Issues that have severity overridden to 'error'

### explainIssues

Added in 7.1.0
    
    
    var [explainIssues](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#explainIssues\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should include explanations for issue errors. (Note that HTML and XML reports intentionally do this unconditionally, ignoring this setting.)

### fatal

Added in 7.1.0
    
    
    val [fatal](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#fatal\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Issues that have severity overridden to 'fatal'

### htmlOutput

Added in 7.0.0
    
    
    var [htmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The optional path to where an HTML report should be written. Setting this property will also turn on `[htmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlReport\(\))`.

### htmlReport

Added in 7.0.0
    
    
    var [htmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether we should write an HTML report. Default is true. The location can be controlled by `[htmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#htmlOutput\(\))`.

### ignore

Added in 7.1.0

Deprecated in 7.1.0
    
    
    val [ignore](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignore\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Ignore and disable are synonyms

Issues that have severity overridden to 'ignore'

### ignoreTestFixturesSources

Added in 7.2.0
    
    
    var [ignoreTestFixturesSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreTestFixturesSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should ignore all testFixtures sources.

### ignoreTestSources

Added in 7.1.0
    
    
    var [ignoreTestSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreTestSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should ignore all test sources. This is like `[checkTestSources](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#checkTestSources\(\))`, but always skips analyzing tests -- meaning that it also ignores checks that have explicitly asked to look at test sources, such as the unused resource check.

### ignoreWarnings

Added in 7.1.0
    
    
    var [ignoreWarnings](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#ignoreWarnings\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Returns whether lint will only check for errors (ignoring warnings)

### informational

Added in 7.1.0
    
    
    val [informational](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#informational\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Issues that have severity overridden to 'informational'

### lintConfig

Added in 7.0.0
    
    
    var [lintConfig](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#lintConfig\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The default config file to use as a fallback. This corresponds to a `lint.xml` file with severities etc to use when a project does not have more specific information.

### noLines

Added in 7.1.0
    
    
    var [noLines](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#noLines\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should include the source lines in the output where errors occurred (true by default)

### quiet

Added in 7.1.0
    
    
    var [quiet](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#quiet\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should be quiet (for example, not write informational messages such as paths to report files written)

### sarifOutput

Added in 7.0.0
    
    
    var [sarifOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The optional path to where a SARIF report (OASIS Static Analysis Results Interchange Format) should be written. Setting this property will also turn on `[sarifReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifReport\(\))`.

### sarifReport

Added in 7.0.0
    
    
    var [sarifReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether we should write a SARIF (OASIS Static Analysis Results Interchange Format) report. Default is false. The location can be controlled by `[sarifOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#sarifOutput\(\))`.

### showAll

Added in 7.1.0
    
    
    var [showAll](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#showAll\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should include all output (e.g. include all alternate locations, not truncating long messages, etc.)

### targetSdk

Added in 8.2.0
    
    
    var [targetSdk](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdk\(\)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)?

The target sdk version used when generating a lint report for a library. Must be equal or higher than main target SDK. Must be set for libraries only.

### targetSdkPreview

Added in 8.2.0
    
    
    var [targetSdkPreview](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#targetSdkPreview\(\)): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)?

The target sdk preview version used when generating a lint report for a library. Must be set for libraries only.

### textOutput

Added in 7.0.0
    
    
    var [textOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The optional path to where a text report should be written.

To output the lint report to `stdout` set `[textReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textReport\(\))``=true`, and leave `[textOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textOutput\(\))` unset.

### textReport

Added in 7.0.0
    
    
    var [textReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should write a text report.

With the default setting (`[textReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textReport\(\))``=false`), the lint task will print a summary to `stdout` if there are any lint warnings or errors including a link to the full text report.

When `[textReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textReport\(\))``=true` and `[textOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textOutput\(\))` is unset, the full report will be printed by the lint task, rather than just a summary. When `[textOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#textOutput\(\))` is set, the full text report will be copied to the specified location.

### warning

Added in 7.1.0
    
    
    val [warning](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#warning\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

Issues that have severity overridden to 'warning'

### warningsAsErrors

Added in 7.1.0
    
    
    var [warningsAsErrors](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#warningsAsErrors\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether lint should treat all warnings as errors

### xmlOutput

Added in 7.0.0
    
    
    var [xmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

The optional path to where an XML report should be written. Setting this property will also turn on `[xmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlReport\(\))`.

### xmlReport

Added in 7.0.0
    
    
    var [xmlReport](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

Whether we should write an XML report. Default is true. The location can be controlled by `[xmlOutput](https://developer.android.com/reference/tools/gradle-api/9.1/com/android/build/api/dsl/Lint#xmlOutput\(\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
