---
url: https://developer.android.com/guide/topics/manifest/path-permission-element/
title: <path-permission> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:23.077622+00:00
---

# <path-permission>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/path-permission-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <path-permission> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <path-permission android:path="_string_ "
                     android:pathPrefix="_string_ "
                     android:pathPattern="_string_ "
                     android:permission="_string_ "
                     android:readPermission="_string_ "
                     android:writePermission="_string_ " />

contained in:
    `[<provider>](https://developer.android.com/guide/topics/manifest/provider-element)`
description:
    Defines the path and required permissions for a specific subset of data within a content provider. This element can be specified multiple times to supply multiple paths. 
attributes:
    

`android:path`
    A complete URI path for a subset of content provider data. Permission can be granted only to the particular data identified by this path. When used to provide search suggestion content, it is appended with `/search_suggest_query`. 
`android:pathPrefix`
    The initial part of a URI path for a subset of content provider data. Permission can be granted to all data subsets with paths that share this initial part. 
`android:pathPattern`
    A complete URI path for a subset of content provider data, but one that can use the following wildcards: 

  * An asterisk (`*`). This matches a sequence of zero to many occurrences of the immediately preceding character.
  * A period followed by an asterisk (`.*`). This matches any sequence of zero or more characters.



Because the backslash (`\`) is used as an escape character when the string is read from XML, before it is parsed as a pattern, you need to double-escape. For example, a literal `*` is written as "`\\*`" and a literal `\` is written as "`\\\`". This is the same as what you write if constructing the string in the Java programming language. 

For more information about these types of patterns, see the descriptions of [`PATTERN_LITERAL`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_LITERAL), [`PATTERN_PREFIX`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_PREFIX), and [`PATTERN_SIMPLE_GLOB`](https://developer.android.com/reference/android/os/PatternMatcher#PATTERN_SIMPLE_GLOB) in the [`PatternMatcher`](https://developer.android.com/reference/android/os/PatternMatcher) class. 

`android:permission`
    The name of a permission that clients need in order to read or write the content provider's data. This attribute is a convenient way of setting a single permission for both reading and writing. However, the `readPermission` and `writePermission` attributes take precedence over this one. 
`android:readPermission`
    A permission that clients need in order to query the content provider. 
`android:writePermission`
    A permission that clients need in order to make changes to the data controlled by the content provider. 
introduced in:
    API level 4
see also:
    `[SearchManager](https://developer.android.com/reference/android/app/SearchManager)`
    `[Manifest.permission](https://developer.android.com/reference/android/Manifest.permission)`
    [Security tips](https://developer.android.com/guide/topics/security/security)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2025-02-10 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-10 UTC."],[],[]] 
