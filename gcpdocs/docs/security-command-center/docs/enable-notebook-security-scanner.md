---
url: https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner/
title: Enable and use Notebook Security Scanner \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T06:04:05.240403+00:00
---

# Enable and use Notebook Security Scanner  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable and use Notebook Security Scanner Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Notebook Security Scanner helps you detect and resolve vulnerabilities in Python packages within Colab Enterprise notebooks (`.ipynb` files). After you enable the scanner through Security Command Center in the Google Cloud console, it scans notebooks every 24 hours and publishes findings to the Security Command Center **Findings** page.

Notebook Security Scanner supports Colab Enterprise notebooks in the `us-central1`, `us-east4`, `us-west1`, and `europe-west4` regions. You manage this feature through the Google Cloud console; the Notebook Security Scanner API (`notebooksecurityscanner.googleapis.com`) isn't intended for direct use.

## Enable Notebook Security Scanner

You can enable Notebook Security Scanner at the organization level or project level.

The way you enable Notebook Security Scanner depends on whether Security Command Center needs to be activated for your organization or project, or on the Security Command Center tier that is activated for your organization or project. Depending on your use case, follow the instructions in the appropriate section:

### New activation Premium tier

If your organization doesn't have Security Command Center, then activate Security Command Center Premium tier for your organization or project, and enable Notebook Security Scanner.

  1. In the Google Cloud console, go to the Security Command Center page.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/config/services)

  2. In the resource selector, select your organization or project.
  3. Click **Get Security Command Center**.
  4. Select the **Premium** tier, and click **Next**.
  5. For **Notebook Security Scanner** , select **Enable** from the list, and click **Next**.
  6. Select **Grant roles automatically** , and then click **Grant roles**.
  7. After the service account is provisioned, click **Next**.
  8. To complete the activation process, click **Finish**.



### New activation Enterprise tier

If your organization doesn't have Security Command Center, then [activate Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#activate-the-security-command-center-enterprise-tier) for your organization, and enable Notebook Security Scanner.

### Existing Premium or Enterprise tier

If the Security Command Center Premium or Enterprise tier is activated for your organization or project, then enable Notebook Security Scanner.

  1. In the Google Cloud console, go to the Security Command Center page.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/config/services)

  2. Click **settings Settings**.
  3. In the **Notebook Security Scanner** card, click **Manage settings**.
  4. For your project, select **Enable** from the **Notebook Security Scanner** column.



## Review and resolve package vulnerability findings

After you enable Notebook Security Scanner, Notebook Security Scanner scans the Colab Enterprise notebooks (files with the `ipynb` filename extension) in your project or organization every 24 hours to detect vulnerabilities in Python packages and publishes these findings to the Security Command Center **Findings** page. For a newly created Colab Enterprise notebook, the package vulnerability findings might take a maximum of four hours to appear in the Security Command Center **Findings** page.

To review package vulnerability findings in Security Command Center, follow these steps:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. In the resource selector, select your organization or project.

  3. In the **Quick filters** section, go to the **Source display name** subsection, and then select **Notebook Security Scanner**.

The **Findings query results** panel shows only the package vulnerability findings of Notebook Security Scanner.

  4. To view details of a specific finding, click the finding name in the **Category** column. The finding details panel expands to display a summary of the finding details.

**Note:** There might be some vulnerabilities published with packages and versions which might not be present in the notebook. This is because, for the Python packages that are being installed without versions in unexecuted code cells, Notebook Security Scanner assumes the latest package version according to the [Python Package Index (PyPI)](https://pypi.org/) and publishes any vulnerabilities.
  5. To resolve a package vulnerability finding, follow the steps mentioned in the **Next steps** section of the finding.

In some cases, a fix for a package vulnerability might not be available. In such cases, we recommend that you use alternative Python packages.




## What's next

  * [View package vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/view-python-package-vulnerabilities). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
