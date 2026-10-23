---
url: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions/
title: LintOptions \u00a0|\u00a0 API reference \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:33:58.012888+00:00
---

# LintOptions  |  API reference  |  Android Developers

> Source: https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ API reference ](https://developer.android.com/reference)



Stay organized with collections  Save and categorize content based on your preferences. 

# LintOptions

[View Source](https://cs.android.com/search?q=file:com/android/build/api/dsl/LintOptions.kt+class:com.android.build.api.dsl.LintOptions)

Added in 4.2.0

Deprecated in 7.0.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    interface [LintOptions](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions)

* * *

**This interface is deprecated.**  
Renamed to Lint

DSL object for configuring lint options.

This block is replaced by the new `[Lint](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/Lint)` block. Unlike most other renamed blocks the new type is unrelated, to allow for some extra changes, such as removing the 'is' prefix from boolean properties.

Example:
    
    
    android {  
       lintOptions {  
             // set to true to turn off analysis progress reporting by lint  
             quiet true  
             // if true, stop the gradle build if errors are found  
             abortOnError false  
             // set to true to have all release builds run lint on issues with severity=fatal  
             // and abort the build (controlled by abortOnError above) if fatal issues are found  
             checkReleaseBuilds true  
             // if true, only report errors  
             ignoreWarnings true  
             // if true, emit full/absolute paths to files with errors (true by default)  
             absolutePaths true  
             // if true, check all issues, including those that are off by default  
             checkAllWarnings true  
             // if true, treat all warnings as errors  
             warningsAsErrors true  
             // turn off checking the given issue id's  
             disable 'TypographyFractions','TypographyQuotes'  
             // turn on the given issue id's  
             enable 'RtlHardcoded','RtlCompat', 'RtlEnabled'  
             // check *only* the given issue id's  
             check 'NewApi', 'InlinedApi'  
             // if true, don't include source code lines in the error output  
             noLines true  
             // if true, show all locations for an error, do not truncate lists, etc.  
             showAll true  
             // whether lint should include full issue explanations in the text error output  
             explainIssues false  
             // Fallback lint configuration (default severities, etc.)  
             lintConfig file("default-lint.xml")  
             // if true, generate a text report of issues (false by default)  
             textReport true  
             // location to write the output; can be a file or 'stdout' or 'stderr'  
             //textOutput 'stdout'  
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
        }  
    }

## Summary

### Public functions  
  
---  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[baseline](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baseline\(java.io.File\))~~(baselineFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html))` **This function is deprecated.** Replaced by lint.baseline  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[baseline](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baseline\(kotlin.String\))~~(baseline: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.baseline  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[check](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#check\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Use checkOnly instead; check will turn off all other checks so the method has been renamed to be more explicit about this  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[check](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#check\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Use checkOnly instead; check will turn off all other checks so the method has been renamed to be more explicit about this  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.checkOnly += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.checkOnly += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.disable += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.disable += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.enable += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.enable += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[error](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#error\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.error += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[error](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#error\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.error += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[fatal](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#fatal\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.fatal += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[fatal](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#fatal\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.fatal += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[ignore](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#ignore\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.ignore += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[ignore](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#ignore\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.ignore += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[informational](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#informational\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.informational += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[informational](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#informational\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.informational += ids  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(java.io.File\))~~(textOutput: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html))` **This function is deprecated.** Replaced by lint.textOutput  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(kotlin.String\))~~(textOutput: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.textOutput  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[warning](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#warning\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.warning += id  
`[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` |  `@[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
~~[warning](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#warning\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html))` **This function is deprecated.** Replaced by lint.warning += ids  
  
### Public properties  
  
---  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[baselineFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baselineFile\(\))` **This property is deprecated.** Moved to lint.baseline  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(\))` **This property is deprecated.** Moved to lint.checkOnly  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(\))` **This property is deprecated.** Moved to lint.disable  
`[MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>` |  `[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(\))` **This property is deprecated.** Moved to lint.enable  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[htmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlOutput\(\))` **This property is deprecated.** Moved to lint.htmlOutput  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[htmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlReport\(\))` **This property is deprecated.** Moved to lint.htmlReport  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isAbortOnError](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isAbortOnError\(\))` **This property is deprecated.** Moved to lint.abortOnError  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isAbsolutePaths](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isAbsolutePaths\(\))` **This property is deprecated.** Moved to lint.absolutePaths  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCheckAllWarnings](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckAllWarnings\(\))` **This property is deprecated.** Moved to lint.checkAllWarnings  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCheckDependencies](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckDependencies\(\))` **This property is deprecated.** Moved to lint.checkDependencies  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCheckGeneratedSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckGeneratedSources\(\))` **This property is deprecated.** Moved to lint.checkGeneratedSources  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCheckReleaseBuilds](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckReleaseBuilds\(\))` **This property is deprecated.** Moved to lint.checkReleaseBuilds  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isCheckTestSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckTestSources\(\))` **This property is deprecated.** Moved to lint.checkTestSources  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isExplainIssues](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isExplainIssues\(\))` **This property is deprecated.** Moved to lint.explainIssues  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIgnoreTestSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isIgnoreTestSources\(\))` **This property is deprecated.** Moved to lint.ignoreTestSources  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isIgnoreWarnings](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isIgnoreWarnings\(\))` **This property is deprecated.** Moved to lint.ignoreWarnings  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isNoLines](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isNoLines\(\))` **This property is deprecated.** Moved to lint.noLines  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isQuiet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isQuiet\(\))` **This property is deprecated.** Moved to lint.quiet  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isShowAll](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isShowAll\(\))` **This property is deprecated.** Moved to lint.showAll  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[isWarningsAsErrors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isWarningsAsErrors\(\))` **This property is deprecated.** Moved to lint.warningsAsErrors  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[lintConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#lintConfig\(\))` **This property is deprecated.** Moved to lint.lintConfig  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[sarifOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifOutput\(\))` **This property is deprecated.** Moved to lint.sarifOutput  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[sarifReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifReport\(\))` **This property is deprecated.** Moved to lint.sarifReport  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(\))` **This property is deprecated.** Moved to lint.textOutput  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[textReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textReport\(\))` **This property is deprecated.** Moved to lint.textReport  
`[File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?` |  `[xmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlOutput\(\))` **This property is deprecated.** Moved to lint.xmlOutput  
`[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |  `[xmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlReport\(\))` **This property is deprecated.** Moved to lint.xmlReport  
  
## Public functions

### baseline

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[baseline](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baseline\(java.io.File\))~~(baselineFile: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.baseline

Sets the baseline file to use, if any. The baseline file is an XML report previously created by lint, and any warnings and errors listed in that report will be ignored from analysis.

If you have a project with a large number of existing warnings, this lets you set a baseline and only see newly introduced warnings until you get a chance to go back and address the "technical debt" of the earlier warnings.

### baseline

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[baseline](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baseline\(kotlin.String\))~~(baseline: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.baseline

Sets the baseline file to use, if any. The baseline file is an XML report previously created by lint, and any warnings and errors listed in that report will be ignored from analysis.

If you have a project with a large number of existing warnings, this lets you set a baseline and only see newly introduced warnings until you get a chance to go back and address the "technical debt" of the earlier warnings.

### check

Added in 4.2.0

Deprecated in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[check](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#check\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use checkOnly instead; check will turn off all other checks so the method has been renamed to be more explicit about this

Adds the id to the set of unique issues to check.

### check

Added in 4.2.0

Deprecated in 4.2.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[check](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#check\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Use checkOnly instead; check will turn off all other checks so the method has been renamed to be more explicit about this

Adds the ids to the set of unique issues to check.

### checkOnly

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.checkOnly += id

Adds the id to the set of issues to check. Note that when using this, all other checks are turned off.

### checkOnly

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.checkOnly += ids

Adds the id to the set of issues to check. Note that when using this, all other checks are turned off.

### disable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.disable += ids

Adds the id to the set of issues to suppress.

### disable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.disable += ids

Adds the ids to the set of issues to suppress.

### enable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.enable += id

Adds the id to the set of issues to enable.

### enable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.enable += ids

Adds the ids to the set of issues to enable.

### error

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[error](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#error\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.error += id

Adds a severity override for the given issue.

### error

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[error](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#error\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.error += ids

Adds a severity override for the given issues.

### fatal

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[fatal](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#fatal\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.fatal += id

Adds a severity override for the given issue.

### fatal

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[fatal](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#fatal\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.fatal += ids

Adds a severity override for the given issues.

### ignore

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[ignore](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#ignore\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.ignore += id

Adds a severity override for the given issue.

### ignore

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[ignore](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#ignore\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.ignore += ids

Adds a severity override for the given issues.

### informational

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[informational](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#informational\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.informational += id

Adds a severity override for the given issue.

### informational

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[informational](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#informational\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.informational += ids

Adds a severity override for the given issues.

### textOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(java.io.File\))~~(textOutput: [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.textOutput

Sets the optional path to where a text report should be written

### textOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(kotlin.String\))~~(textOutput: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.textOutput

Sets the optional path to where a text report should be written

### warning

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[warning](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#warning\(kotlin.String\))~~(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.warning += id

Adds a severity override for the given issue.

### warning

Added in 4.2.0

Deprecated in 7.1.0
    
    
    @[Incubating](https://docs.gradle.org/current/javadoc/org/gradle/api/Incubating.html)  
    fun ~~[warning](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#warning\(kotlin.Array\))~~(vararg ids: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)): [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)

**This function is deprecated.**  
Replaced by lint.warning += ids

Adds a severity override for the given issues.

## Public properties

### baselineFile

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [baselineFile](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#baselineFile\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.baseline

The baseline file to use, if any. The baseline file is an XML report previously created by lint, and any warnings and errors listed in that report will be ignored from analysis.

If you have a project with a large number of existing warnings, this lets you set a baseline and only see newly introduced warnings until you get a chance to go back and address the "technical debt" of the earlier warnings.

### checkOnly

Added in 4.2.0

Deprecated in 7.1.0
    
    
    val [checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Moved to lint.checkOnly

The exact set of issues to check set by `[checkOnly](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#checkOnly\(kotlin.String\))`. s If empty, lint will detect the issues that are enabled by default plus any issues enabled via `[enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(kotlin.String\))` and without issues disabled via `[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.String\))`.

### disable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    val [disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Moved to lint.disable

The set of issue IDs to suppress.

Issues passed to `[disable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#disable\(kotlin.String\))` to this list, call Callers are allowed to modify this collection.

### enable

Added in 4.2.0

Deprecated in 7.1.0
    
    
    val [enable](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#enable\(\)): [MutableSet](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)>

**This property is deprecated.**  
Moved to lint.enable

The set of issue IDs to enable. Callers are allowed to modify this collection.

### htmlOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [htmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.htmlOutput

The optional path to where an HTML report should be written. Setting this property will also turn on `[htmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlReport\(\))`.

### htmlReport

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [htmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.htmlReport

Whether we should write an HTML report. Default is true. The location can be controlled by `[htmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#htmlOutput\(\))`.

### isAbortOnError

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isAbortOnError](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isAbortOnError\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.abortOnError

Whether lint should set the exit code of the process if errors are found

### isAbsolutePaths

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isAbsolutePaths](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isAbsolutePaths\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.absolutePaths

Whether lint should display full paths in the error output. By default the paths are relative to the path lint was invoked from.

### isCheckAllWarnings

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isCheckAllWarnings](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckAllWarnings\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.checkAllWarnings

Whether lint should check all warnings, including those off by default

### isCheckDependencies

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isCheckDependencies](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckDependencies\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.checkDependencies

Whether lint should check all dependencies too as part of its analysis. Default is false.

### isCheckGeneratedSources

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isCheckGeneratedSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckGeneratedSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.checkGeneratedSources

Returns whether lint should run checks on generated sources.

### isCheckReleaseBuilds

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isCheckReleaseBuilds](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckReleaseBuilds\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.checkReleaseBuilds

Whether lint should check for fatal errors during release builds. Default is true. If issues with severity "fatal" are found, the release build is aborted.

### isCheckTestSources

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isCheckTestSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckTestSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.checkTestSources

Whether lint should run all checks on test sources, instead of just the lint checks that have been specifically written to include tests (e.g. checks looking for specific test errors, or checks that need to consider testing code such as the unused resource detector)

### isExplainIssues

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isExplainIssues](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isExplainIssues\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.explainIssues

Whether lint should include explanations for issue errors. (Note that HTML and XML reports intentionally do this unconditionally, ignoring this setting.)

### isIgnoreTestSources

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isIgnoreTestSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isIgnoreTestSources\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.ignoreTestSources

Whether lint should ignore all test sources. This is like `[isCheckTestSources](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isCheckTestSources\(\))`, but always skips analyzing tests -- meaning that it also ignores checks that have explicitly asked to look at test sources, such as the unused resource check.

### isIgnoreWarnings

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isIgnoreWarnings](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isIgnoreWarnings\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.ignoreWarnings

Returns whether lint will only check for errors (ignoring warnings)

### isNoLines

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isNoLines](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isNoLines\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.noLines

Whether lint should include the source lines in the output where errors occurred (true by default)

### isQuiet

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isQuiet](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isQuiet\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.quiet

Whether lint should be quiet (for example, not write informational messages such as paths to report files written)

### isShowAll

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isShowAll](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isShowAll\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.showAll

Whether lint should include all output (e.g. include all alternate locations, not truncating long messages, etc.)

### isWarningsAsErrors

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [isWarningsAsErrors](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#isWarningsAsErrors\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.warningsAsErrors

Whether lint should treat all warnings as errors

### lintConfig

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [lintConfig](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#lintConfig\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.lintConfig

The default config file to use as a fallback. This corresponds to a `lint.xml` file with severities etc to use when a project does not have more specific information.

### sarifOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [sarifOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.sarifOutput

The optional path to where a SARIF report (OASIS Static Analysis Results Interchange Format) should be written. Setting this property will also turn on `[sarifReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifReport\(\))`.

### sarifReport

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [sarifReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.sarifReport

Whether we should write a SARIF (OASIS Static Analysis Results Interchange Format) report. Default is false. The location can be controlled by `[sarifOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#sarifOutput\(\))`.

### textOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.textOutput

The optional path to where a text report should be written. The special value "stdout" can be used to point to standard output. Setting this property will also turn on `[textReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textReport\(\))`.

### textReport

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [textReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.textReport

Whether we should write a text report. Default is false. The location can be controlled by `[textOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#textOutput\(kotlin.String\))`.

### xmlOutput

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [xmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlOutput\(\)): [File](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/io/File.html)?

**This property is deprecated.**  
Moved to lint.xmlOutput

The optional path to where an XML report should be written. Setting this property will also turn on `[xmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlReport\(\))`.

### xmlReport

Added in 4.2.0

Deprecated in 7.1.0
    
    
    var [xmlReport](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlReport\(\)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)

**This property is deprecated.**  
Moved to lint.xmlReport

Whether we should write an XML report. Default is true. The location can be controlled by `[xmlOutput](https://developer.android.com/reference/tools/gradle-api/8.13/com/android/build/api/dsl/LintOptions#xmlOutput\(\))`.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-07-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-21 UTC."],[],[]] 
