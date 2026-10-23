---
url: https://developer.android.com/studio/run/emulator-networking-dns/
title: Configure emulator DNS settings \u00a0|\u00a0 Android Studio \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:50.357995+00:00
---

# Configure emulator DNS settings  |  Android Studio  |  Android Developers

> Source: https://developer.android.com/studio/run/emulator-networking-dns/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Android Studio ](https://developer.android.com/studio)
  * [ IDE guides ](https://developer.android.com/studio/intro)



#  Configure emulator DNS settings Stay organized with collections  Save and categorize content based on your preferences. 

At startup, the emulator reads the list of DNS servers that your system is using. It then stores the IP addresses of up to four servers on this list and sets up aliases to them on the emulated addresses `10.0.2.3`, `10.0.2.4`, `10.0.2.5`, and `10.0.2.6`, as needed.

On Linux and macOS, the emulator obtains the DNS server addresses by parsing the file `/etc/resolv.conf`. On Windows, the emulator obtains the addresses by calling the `GetNetworkParams()` API. This usually means that the emulator ignores the content of your `hosts` file (`/etc/hosts` on Linux and macOS, `%WINDOWS%/system32/HOSTS` on Windows).

## Manually specify DNS servers

When starting the emulator from the command line, you can use the `-dns-server <serverList>` option to manually specify the addresses of DNS servers to use.

  * `<serverList>` is a comma-separated list of server names or IP addresses.
  * This option is useful if you encounter DNS resolution problems in the emulated network, such as an "Unknown Host error" message when using the web browser.


    
    
    emulator @MyAvd -dns-server 8.8.8.8,8.8.4.4,2001:4860:4860::8888,2001:4860:4860::8844
    

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-03-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-12 UTC."],[],[]] 
