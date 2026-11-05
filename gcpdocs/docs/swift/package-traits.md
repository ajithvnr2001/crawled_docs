---
url: https://docs.cloud.google.com/swift/package-traits/
title: Package traits \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:40:58.948452+00:00
---

# Package traits  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/package-traits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Package traits Stay organized with collections  Save and categorize content based on your preferences. 

Swift Package Manager (SPM) supports package traits (SE-0450) starting in Swift 6.2. Package traits let packages conditionally compile parts of a library, enabling only the features and dependencies needed by your application.

## Why client libraries use traits

Several Google Cloud APIs define large numbers of independent services. For example, Compute Engine v1 defines over 120 services, and Vertex AI defines over 30 services. Generating and compiling every client and its associated request, response, and model types results in long compile times and larger binary sizes, even when an application only interacts with one or two services.

To optimize build performance, the Google Cloud client libraries for Swift use package traits to partition large libraries. Enabling a trait conditionally compiles the specific service client and all the types required to use that client. The client libraries enable package traits for large APIs to manage build overhead, though the exact threshold is subject to change.

## Default traits

Packages that use traits define a set of default traits for commonly used services. For example, Compute Engine enables only `Instances` (and transitively `ZoneOperations`) by default.

When you add a dependency without specifying any traits, SPM enables the default traits automatically:
    
    
    .package(
        url: "https://github.com/googleapis/swift-google-cloud-compute-v1.git",
        from: "0.4.0"
    )
    

If the default traits provide all the services that your application needs, no further configuration is required.

## Enable additional traits

To enable services beyond the defaults, specify the required traits in your `Package.swift` file.

### Combine default traits with additional traits

To keep the default services and enable additional services, include the `".defaults"` trait alongside the traits that you want to enable:
    
    
    // swift-tools-version: 6.2
    import PackageDescription
    
    let package = Package(
        name: "MyApplication",
        dependencies: [
            .package(
                url: "https://github.com/googleapis/swift-google-cloud-compute-v1.git",
                from: "0.4.0",
                traits: [".defaults", "Disks"]
            ),
        ],
        targets: [
            .target(
                name: "MyApplication",
                dependencies: [
                    .product(
                        name: "GoogleCloudComputeV1",
                        package: "swift-google-cloud-compute-v1"
                    ),
                ]
            ),
        ]
    )
    

### Disable defaults and select specific traits

To disable the default traits and compile only specific services, list the selected traits without `".defaults"`:
    
    
    .package(
        url: "https://github.com/googleapis/swift-google-cloud-compute-v1.git",
        from: "0.4.0",
        traits: ["Disks"]
    )
    

## Compiler diagnostics for disabled traits

If your code attempts to use a client whose trait isn't enabled in `Package.swift`, the Swift compiler produces an actionable diagnostic:
    
    
    error: 'DisksClient' is unavailable: Enable the 'Disks' trait in Package.swift to use this client.
    

This diagnostic indicates which trait to add to your `Package.swift` dependencies.

## Command-line workflows

When developing, testing, or building from the command line, you can enable traits using the `--traits` option with `swift build` or `swift test`:
    
    
    swift build --traits defaults,Disks
    

To build with only specific traits and bypass the defaults, omit `defaults`:
    
    
    swift build --traits Disks
    

## Discover available traits

Each generated client library documents its available traits, default traits, and the corresponding client classes in two places:

  * The `README.md` file in each package under the **Package Traits** section.
  * The DocC documentation for each package in the **Package Traits** article.



## What's next

  * Follow the [Quickstart: Get started with Swift](https://docs.cloud.google.com/swift/quickstart) to set up and run your first Swift application with the Google Cloud client libraries.
  * Browse the [Swift Cloud Client Libraries](https://docs.cloud.google.com/swift/reference) reference documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
