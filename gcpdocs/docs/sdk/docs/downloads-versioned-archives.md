---
url: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives/
title: Installing from versioned archives \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:50:58.852119+00:00
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
Linux 64-bit (x86_64) | [google-cloud-cli-linux-x86_64.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz) | 93.8 MB | b0dc27650a82e50321aa7c9d068cdc01443aa348f15489af9e5dec0a94623ae6  
Linux 64-bit (Arm) | [google-cloud-cli-linux-arm.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-arm.tar.gz) | 89.9 MB | c9e8618c9257b3289deb7cb5483479230d5d96230bd68a80fce17f592d0d3012  
Linux 32-bit (x86) | [google-cloud-cli-linux-x86.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86.tar.gz) | 54.2 MB | b9a98b7ce9bc744c7bc955d8e42e2e862747d75d43b58d3b6a0bb16ed39b2da9  
macOS 64-bit (x86_64) | [google-cloud-cli-darwin-x86_64.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86_64.tar.gz) | 54.3 MB | f6a222b32bac56fca8d787098a01c8e92cd0de52dd8c144ee74ca0c246c65b56  
macOS 64-bit (arm64) | [google-cloud-cli-darwin-arm.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-arm.tar.gz) | 54.2 MB | 71a0aab59d239e08f3a4ea69ef33b4eecbd21f79ed5567e3fd4745f81ec8e003  
macOS 32-bit (x86) | [google-cloud-cli-darwin-x86.tar.gz](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-darwin-x86.tar.gz) | 52.7 MB | e2a62c407607f789770071ac356a34576965571e3bf2451fe7876b56feae60b6  
Windows 64-bit (x86_64) | [google-cloud-cli-windows-x86_64.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-windows-x86_64.zip) | 78.8 MB | 1a2891fe481b8e2f9c54db8e5aacfcd6b6d589688ecef0ca5d988631fa0ebcf0  
Windows 64-bit (x86_64) with Python bundled | [google-cloud-sdk-590.0.1-windows-x86_64-bundled-python.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-590.0.1-windows-x86_64-bundled-python.zip) | 104.4 MB | 38dad2c60c8507a2042e419ac9293e66b9f96156226c6cda92dcb1c4e8c65cf2  
Windows 32-bit (x86) | [google-cloud-cli-windows-x86.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-windows-x86.zip) | 78.7 MB | 41a17a6a4d327230ea063f87929f936e254af37cca29916b33ef7e813363d396  
Windows 32-bit (x86) with Python bundled | [google-cloud-sdk-590.0.1-windows-x86-bundled-python.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-590.0.1-windows-x86-bundled-python.zip) | 101.7 MB | 2b2a012c832b412431ff4b124308cbb1d8d089970f034ce675d3cb949bcca24a  
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

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
