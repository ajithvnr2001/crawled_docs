---
url: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives/
title: Installing from versioned archives \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T15:29:30.923579+00:00
---

# Installing from versioned archives  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Installing from versioned archives Stay organized with collections  Save and categorize content based on your preferences. 

The gcloud CLI provides downloadable, versioned archives for each release. Each versioned archive contains a self-contained installation of the gcloud CLI in a directory named `google-cloud-sdk` that can be copied to any location on your file system.

## Best uses for installing from versioned archives

Versioned archives are designed for non-interactive installation of specific versions of the gcloud CLI and are useful when:

  * You require a specific version of the gcloud CLI. For example:

    * You're scripting with the gcloud CLI or another gcloud CLI component and want to make sure that your scripts don't break as the result of a gcloud CLI update.
    * You're using the gcloud CLI as part of a CI (continuous integration) process or production system where you want to control your dependencies in order to ensure compatibility between parts of the system.
    * You're performing automated deployments of the gcloud CLI to many machines that must be in sync.
    * You're behind a proxy or firewall that requires [additional configuration](https://docs.cloud.google.com/sdk/docs/proxy-settings) to be able to access the internet.
  * You don't want to perform an interactive installation.




## Installation instructions

To install the latest release of the gcloud CLI from a versioned archive:

  1. Check which version (64-bit or 32-bit) your OS is running on.

     * Linux / macOS: Run `getconf LONG_BIT` from your command line
     * Windows: **Control Panel** > **System** > **System Type**

Additionally, for macOS, to check your machine hardware name (x86_64, arm64, or x86), run `uname -m`.

  2. Download the appropriate archive compatible with your version:

Platform | Package | Size | SHA256 Checksum  
---|---|---|---  
Linux 64-bit (x86_64) | [google-cloud-cli-linux-x86_64.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz) | 94.7 MB | 181a74765ab1f2d3dd37bc1b7f9b53b6f5b348eef44ea2e194b9ed41310b44bb  
Linux 64-bit (Arm) | [google-cloud-cli-linux-arm.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-arm.tar.gz) | 90.7 MB | 13e40f07f44bb6380a8d17275e352964360543af8ea18a7ddfee0445481f9413  
Linux 32-bit (x86) | [google-cloud-cli-linux-x86.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86.tar.gz) | 54.8 MB | 476eef9d8f890795c246b6c567e7623e3c404c0c824d2e3be6f6be81d08bfe74  
macOS 64-bit (x86_64) | [google-cloud-cli-darwin-x86_64.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86_64.tar.gz) | 54.9 MB | 108c1a0bb5d273703b61c4dc9cafab9cc0e674797347ab18d5357d228a517131  
macOS 64-bit (arm64) | [google-cloud-cli-darwin-arm.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-arm.tar.gz) | 54.8 MB | 563b2102362a54506836b73ef3485b6abfe112c1e48559022bbb5dbf45f55e4e  
macOS 32-bit (x86) | [google-cloud-cli-darwin-x86.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86.tar.gz) | 53.2 MB | 35d83632d1b2fc48fe342c957a3105995d5f855c2d770b37de277178f0cfe2d8  
Windows 64-bit (x86_64) | [google-cloud-cli-windows-x86_64.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-windows-x86_64.zip) | 105.6 MB | 8fbdc9d644ffdd25a7f515c2643edc87100d3d48be9d3aa635454f6d7fb6a53c  
Windows 64-bit (x86_64) with Python bundled | [google-cloud-sdk-593.0.0-windows-x86_64-bundled-python.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-593.0.0-windows-x86_64-bundled-python.zip) | 105.6 MB | 8fbdc9d644ffdd25a7f515c2643edc87100d3d48be9d3aa635454f6d7fb6a53c  
Windows 32-bit (x86) | [google-cloud-cli-windows-x86.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-windows-x86.zip) | 102.8 MB | efb31b7f685035a637692beda552a1401115488e35c6bac2fa46e9ed668b433e  
Windows 32-bit (x86) with Python bundled | [google-cloud-sdk-593.0.0-windows-x86-bundled-python.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-593.0.0-windows-x86-bundled-python.zip) | 102.8 MB | efb31b7f685035a637692beda552a1401115488e35c6bac2fa46e9ed668b433e  
  3. Extract the contents of the file to any location on your file system. Preferably, this is your Home folder.

  4. To add the gcloud CLI tools to your path, run the install script from the root of the folder you extracted. Running this script also generates instructions to enable command completion in your `bash` shell (Linux and macOS only) and enable usage reporting.

     * On Linux or macOS:
           
           ./google-cloud-sdk/install.sh
           

To run the install script with screen reader mode turned on:
           
           ./google-cloud-sdk/install.sh --screen-reader=true
           

     * On Windows:
           
           .\google-cloud-sdk\install.bat
           

Run `install.sh --help` or `install.bat --help` for a list of flags you can pass to this script, including those that can run the installation non-interactively.

**Note:** If you answered `n` when the installer prompted asking to modify your profile to update your `PATH` and enable command completion, you can still set up your profile to do so (to ensure the gcloud CLI works correctly) by doing the following: 
     * Bash shell
       * Source `/path/to/gcloud/path.bash.inc` in your profile to add the gcloud CLI tools to your `PATH`.
       * Source `/path/to/gcloud/completion.bash.inc` in your profile to enable command completion for the gcloud CLI.
     * Zsh shell
       * Source `/path/to/gcloud/path.zsh.inc` in your profile to add the gcloud CLI command line tools to your `PATH`.
       * Source `/path/to/gcloud/completion.zsh.inc` in your profile to enable command completion for the gcloud CLI.
     * Fish shell
       * Source `/path/to/gcloud/path.fish.inc` in your profile to add the gcloud CLI command line tools to your `PATH`.
  5. To initialize the gcloud CLI, run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init):

     * For Linux or macOS:
           
           ./google-cloud-sdk/bin/gcloud init
           

     * For Windows:
           
           .\google-cloud-sdk\bin\gcloud init
           




## Previous versions

Previous versions of the gcloud CLI are available in the [download archive](https://console.cloud.google.com/storage/browser/cloud-sdk-release) in Cloud Storage. They are directly accessible through `https://storage.googleapis.com/cloud-sdk-release/<archive_name>`.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
