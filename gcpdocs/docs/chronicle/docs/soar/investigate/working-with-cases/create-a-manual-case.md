---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case/
title: Create a case manually \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T19:10:28.279864+00:00
---

# Create a case manually  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a case manually

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can manually create a case to enter specific data. This is useful when you need to ingest information on an alert; for example, information that was reported from sources that aren't integrated with your detection pipeline (for example, alerts reported from non-cyber channels). 

  1. On the **Cases** page, click  add  **Add a Case > Create Manual Case**.
  2. In the **Case** step, configure the following case details: 
     * **Case Title** : Enter a title for the new case. 
     * **Creation reason** : Optional. Enter the reason for creating the case. 
     * **Environment** : Select the specific environment being monitored. If your organization has only one environment, it is selected automatically. 
     * **Assign to** : Assign the case to a specific role or user. Select **(Assign to me)** to assign the case to yourself. 
     * **Priority** : Set the priority level for the case. 
     * **Mark as important** : Click the **Mark as important** toggle on if the case should be flagged as important. 
  3. Optional: Under **Tags** , select any existing tags, create new tags, or leave blank. 
  4. Optional: Under **Playbooks** , configure case-level automation: 
     * **Attach playbooks automatically** : Enable the toggle to allow matching system triggers to attach playbooks automatically. 
     * **Attach case playbooks manually** : Select up to 3 case-scoped playbooks from the menu to run across the case container. This field is enabled once an environment is selected. 
  5. To create the case without an alert, click **Create case**. Otherwise, click **Next** (or click the **Alert** step header) to add alert information. 
  6. Optional: In the **Alert** step, configure alert details: 
     * **Alert Name** : Enter a name for the security alert. Leaving this blank creates the case without an alert. 
     * **Occurrence Time** : Select the date and time the alert occurred. If left empty, the current time is used. 
     * **SLA** : Specify a date and time by which the SOC team should resolve the case. 
     * **Entities** : Add existing entities or create new ones. **Note:** Adding entities requires both an Alert Name and an Environment. 
     * **Attach alert playbooks manually** : Select up to 3 alert-scoped playbooks to execute on the alert. **Note:** Attaching alert playbooks requires both an Alert Name and an Environment. 
  7. Click **Create case**. 

A confirmation notification appears with a link to open the new case. 


**Note:** Service Level Agreements (SLAs) are calculated only for cases that contain an alert. If you create a case without an alert, no SLA is calculated. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
