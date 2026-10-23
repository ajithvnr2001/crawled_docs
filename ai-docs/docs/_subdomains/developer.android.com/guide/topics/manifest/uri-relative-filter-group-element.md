---
url: https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element/
title: <uri-relative-filter-group> \u00a0|\u00a0 App architecture \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:40:27.438842+00:00
---

# <uri-relative-filter-group>  |  App architecture  |  Android Developers

> Source: https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App architecture ](https://developer.android.com/topic/architecture/intro)



#  <uri-relative-filter-group> Stay organized with collections  Save and categorize content based on your preferences. 

syntax:
    
    
    
    <uri-relative-filter-group android:allow=["true" | "false"]>
      <data ... />
      ...
    </uri-relative-filter-group>

contained in:
     ` [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element) `
can contain:
     `[<data>](https://developer.android.com/guide/topics/manifest/data-element)`
description:
     **Note:** The `<uri-relative-filter-group>` element and its features, including query and fragment matching and `android:allow` attribute, are only supported on Android 15 (API level 35) and higher. They are ignored and have no effect on lower Android versions.  Creates precise `Intent` matching rules that can include URI query parameters and URI fragments. The rules can be inclusion (_allow_) rules or exclusion (_blocking_) rules, depending on the `android:allow` attribute. The matching rules are specified by the `[path*](https://developer.android.com/guide/topics/manifest/data-element#path)`, `[fragment*](https://developer.android.com/guide/topics/manifest/data-element#fragment)`, and `[query*](https://developer.android.com/guide/topics/manifest/data-element#query)` attributes of the contained `[<data>](https://developer.android.com/guide/topics/manifest/data-element)` elements. **Note:** Only the contained `[path*](https://developer.android.com/guide/topics/manifest/data-element#path)`, `[fragment*](https://developer.android.com/guide/topics/manifest/data-element#fragment)`, and `[query*](https://developer.android.com/guide/topics/manifest/data-element#query)` attributes are used for intent matching. All other `<data>` attributes are ignored. 

**Matching**

To match a URI, each portion of the URI relative filter group must match a part of the URI. There can be portions of the URI that are not specified in the URI relative filter group. For example: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="true">
        <data android:query="param1=value1" />
        <data android:query="param2=value2" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

The filter matches `https://project.example.com/any/path/here?param1=value1&param2=value2&param3=value3` because everything specified by the URI relative filter group is present. The filter also matches `https://project.example.com/any/path/here?param2=value2&param1=value1` because the order of the query parameters doesn't matter. However, the filter doesn't match `https://project.example.com/any/path/here?param1=value1`, which is missing `param2=value2`. 

**OR and AND**

`[<data>](https://developer.android.com/guide/topics/manifest/data-element)` tags outside a `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` are ORed, while `<data>` tags inside of a `<uri-relative-filter-group>` are ANDed. 

Consider the following example: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <data android:pathPrefix="/prefix" />
      <data android:pathSuffix="suffix" />
      ...
    </intent-filter>

The filter matches paths that start with `/prefix` OR end with `suffix`. 

In contrast, the next example matches paths that start with `/prefix` AND end with `suffix`: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group>
        <data android:pathPrefix="/prefix" />
        <data android:pathSuffix="suffix" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

As a result, multiple `[path](https://developer.android.com/guide/topics/manifest/data-element#path)` attributes in the same `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` don't match anything: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group>
        <data android:path="/path1" />
        <data android:path="/path2" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

**Declaration order**

Consider the following example:
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group>
        <data android:fragment="fragment" />
      </uri-relative-filter-group>
      <uri-relative-filter-group android:allow="false">
        <data android:fragmentPrefix="fragment" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

The filter matches the fragment `#fragment` because a match is found before the exclusion rule is evaluated, but fragments like `#fragment123` don't match. 

**Sibling tags**

`[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` tags work together with their sibling `[<data>](https://developer.android.com/guide/topics/manifest/data-element)` tags (that is, `<data>` tags that are are outside the `<uri-relative-filter-group>` but inside the same `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`). `<uri-relative-filter-group>` tags must have sibling `<data>` tags to function properly because URI attributes are mutually dependent at the `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)` level: 

  * If a `[scheme](https://developer.android.com/guide/topics/manifest/data-element#scheme)` isn't specified for the intent filter, all the other URI attributes are ignored. 
  * If a `[host](https://developer.android.com/guide/topics/manifest/data-element#host)` isn't specified for the filter, the `[port](https://developer.android.com/guide/topics/manifest/data-element#port)` attribute and all the `[path*](https://developer.android.com/guide/topics/manifest/data-element#path)` attributes are ignored. 



The `[<data>](https://developer.android.com/guide/topics/manifest/data-element)` children of an `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)` are evaluated before any `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` tags. Then the `<uri-relative-filter-group>` tags are evaluated in order, for example: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="false">
        <data android:path="/path" />
        <data android:query="query" />
      </uri-relative-filter-group>
      <data android:path="/path" />
      ...
    </intent-filter>

The filter accepts `https://project.example.com/path?query` because it matches `<data android:path="/path" />`, which is outside the `<uri-relative-filter-group>` exclusion rule. 

**Note:** Because `[path*](https://developer.android.com/guide/topics/manifest/data-element#path)` attributes from `[<data>](https://developer.android.com/guide/topics/manifest/data-element)` tags are evaluated before the `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` tags (which are evaluated in declaration order), it is best practice to place the `path*` attributes before the `<uri-relative-filter-group>` tags. 

**Common use case**

Imagine you have the URI `https://project.example.com/path`, which you want to match to an `Intent` depending on the presence or value of a query parameter. To create an intent filter that matches `https://project.example.com/path` and blocks `https://project.example.com/path?query`, you might try something like: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="true">
        <data android:path="/path" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

This, in fact, doesn't work. The `https://project.example.com/path?query` URI matches the path `/path`, and the `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` tag allows _extra_ parts when it is matching. 

Revise the intent filter as follows: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="false">
        <data android:path="/path" />
        <data android:queryAdvancedPattern=".+" />
      </uri-relative-filter-group>
      <uri-relative-filter-group android:allow="true">
        <data android:path="/path" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

This filter works because the blocking rules that forbid nonempty query parameters are evaluated first. 

To simplify the code, flip the behavior to allow query parameters and block URIs without query parameters: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="true">
        <data android:path="/path" />
        <data android:queryAdvancedPattern=".+" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

**URI-encoded characters**

To match URIs that contain URI-encoded characters, write the raw, unencoded characters in the filter, for example: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="true">
        <data android:query="param=value!" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

The filter matches `?param=value!` _and_ `?param=value%21`. 

However, if you write encoded characters in the filter as follows: 
    
    
    <intent-filter...>
      <data android:scheme="https" android:host="project.example.com" />
      <uri-relative-filter-group android:allow="true">
        <data android:query="param=value%21" />
      </uri-relative-filter-group>
      ...
    </intent-filter>

The filter matches neither `?param=value!` nor `?param=value%21`. 

**Number of elements**

You can place any number of `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)` elements inside an `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`. 

**Additional resources**

For information on how intent filters work, including the rules for how intent objects are matched against filters, see [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters) and [Intent Filters](https://developer.android.com/guide/topics/manifest/manifest-intro#ifs). 

For information on `[<uri-relative-filter-group>](https://developer.android.com/guide/topics/manifest/uri-relative-filter-group-element)`, see `[UriRelativeFilterGroup](https://developer.android.com/reference/kotlin/android/content/UriRelativeFilterGroup)` and `[UriRelativeFilter](https://developer.android.com/reference/kotlin/android/content/UriRelativeFilter)`. 

attributes:
    

`android:allow`
     Whether this URI relative filter group is an inclusion (_allow_) rule rather than an exclusion (_blocking_) rule. The default value is `"true"`. Value | Description  
---|---  
`"true"` (default) | If the URI relative filter group matches, the intent filter matches  
`"false"` | If the URI relative filter group matches, the intent filter doesn't match  
introduced in:
    API level 35
see also:
     `[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)`   
`[<data>](https://developer.android.com/guide/topics/manifest/data-element)`

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
