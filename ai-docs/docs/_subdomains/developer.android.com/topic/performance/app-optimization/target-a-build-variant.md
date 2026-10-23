---
url: https://developer.android.com/topic/performance/app-optimization/target-a-build-variant/
title: Target a build variant \u00a0|\u00a0 App quality \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:42:58.983757+00:00
---

# Target a build variant  |  App quality  |  Android Developers

> Source: https://developer.android.com/topic/performance/app-optimization/target-a-build-variant/

  * [ Android Developers ](https://developer.android.com/)
  * [ Design & Plan ](https://developer.android.com/design)
  * [ App quality ](https://developer.android.com/quality)
  * [ Technical quality ](https://developer.android.com/quality/technical)



#  Target a build variant Stay organized with collections  Save and categorize content based on your preferences. 

If you have different versions of your app based on different build variants, create custom [keep rules](https://developer.android.com/topic/performance/app-optimization/add-keep-rules) for each variant. For example, if you have a free tier and a paid tier of your app with different features and dependencies, each tier should have its own keep rules.

## Create keep rules

**For AGP 9.3+:**

To maintain specific keep rules for different flavors of your app, place the keep rules for each flavor in the relevant keep rules source set . For example, for `flavor1`, write keep rules in `app/src/flavor1/keepRules/flavor1-rules.keep`.

### AGP 9.3+ (Kotlin)
    
    
    android {
        buildTypes {
            release {
                optimization {
                    enable = true // Enables code and resource optimizations.
                }
            }
        }
        flavorDimensions.add("version")
            productFlavors {
                create("flavor1") {
                    ...
                    // Place your keep rules in app/src/flavor1/keepRules/ with the file suffix .keep
                }
                create("flavor2") {
                    ...
                    // Place your keep rules in app/src/flavor2/keepRules/ with the file suffix .keep
                }
            }
    }
    

### AGP 9.3+ (Groovy)
    
    
    android {
        buildTypes {
            release {
                optimization {
                    enable = true // Enables code and resource optimizations.
                }
            }
        }
        flavorDimensions "version"
        productFlavors {
            flavor1 {
                ...
            }
            flavor2 {
                ...
                // Place your keep rules in app/src/flavor2/keepRules/ with the file suffix .keep
            }
        }
    }
    

**For AGP versions earlier than 9.3:**

To create keep rules that are specific to a build variant, add the `proguardFiles` property in the corresponding _flavor_ block under `productFlavors`.

Consider the following build script that adds the rules file `flavor2‑rules.pro` to the `flavor2` product flavor:

### Legacy DSL (Kotlin)
    
    
    android {
        ...
        buildTypes {
            getByName("release") {
                isMinifyEnabled = true
                isShrinkResources = true
                proguardFiles(
                    getDefaultProguardFile("proguard-android-optimize.txt"),
                    "proguard-rules.pro"
                )
            }
        }
        flavorDimensions.add("version")
            productFlavors {
                create("flavor1") {
                    ...
                }
                create("flavor2") {
                    proguardFile("flavor2-rules.pro")
                }
            }
    }
    

### Legacy DSL (Groovy)
    
    
    android {
        ...
        buildTypes {
            release {
                minifyEnabled = true
                shrinkResources = true
                proguardFiles(
                    getDefaultProguardFile('proguard-android-optimize.txt'),
                    'proguard-rules.pro'
                )
            }
        }
        flavorDimensions "version"
        productFlavors {
            flavor1 {
                ...
            }
            flavor2 {
                proguardFile 'flavor2-rules.pro'
            }
        }
    }
    

**Note:** The `flavor2` product flavor uses rules from three rules files—`flavor2‑rules.pro`, `proguard‑rules.pro`, and `proguard‑android‑optimize.txt`—because the script applies the rules from the release block.

## Additional resources

  * [Customize which resources to keep](https://developer.android.com/topic/performance/app-optimization/customize-which-resources-to-keep) — Learn how to add keep rules for resources.



Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
