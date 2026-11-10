---
url: https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats/
title: Detect and investigate threats in SAP logs \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T12:41:50.719377+00:00
---

# Detect and investigate threats in SAP logs  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Detect and investigate threats in SAP logs Stay organized with collections  Save and categorize content based on your preferences. 

After you [ingest your SAP logs](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources) into [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) (Google SecOps), you can search normalized SAP events and deploy SAP-specific YARA-L detection rules to identify and investigate threats across your SAP landscape.

Google hosts SAP YARA-L threat detection rules in official Google SecOps GitHub repositories. You can also configure the [SAP response integration](https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration) and use [prebuilt SAP mitigation actions](https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration#prebuilt-sap-mitigation-actions) to automate incident containment.

To detect and investigate SAP threats, follow this workflow:

  1. Search and filter SAP logs.
  2. Import detection rules from GitHub.
  3. Manage and customize detection rules.
  4. Investigate SAP-related cases.



## Search and filter SAP logs

After Google SecOps ingests and normalizes your SAP logs, you can verify log delivery and hunt for threats across your SAP landscape by using the following search features:

  * **UDM search** : Run queries across parsed and normalized SAP events in [UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search). In the Google SecOps menu, go to **Investigation** > **Search** and filter events by log type, for example, `metadata.log_type = "SAP_SECURITY_AUDIT"`.
  * **Raw log search** : Search unparsed raw logs by using strings or regular expressions. For information about how to run raw log searches, see [Use raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs).
  * **Aggregations** : Group and analyze event fields to identify anomalies across large SAP datasets. For information about aggregations, see [Aggregations](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search).



## Import detection rules from GitHub

Google hosts the SAP threat detection rules on GitHub. To use the SAP threat detection content, download and import these rules into your environment. The repository contains SAP YARA-L rules that detect threats such as unauthorized configuration changes, privilege escalation, and RFC abuse.

To import the SAP detection rules into your environment, do the following:

  1. Go to the [Google SecOps Detection Rules](https://github.com/chronicle/detection-rules) repository on GitHub.
  2. Navigate to the `rules/community/sap` directory and download the SAP YARA-L rule files (`.yaral`).
  3. In the Google SecOps menu, go to **Detection** > **Rules and Detections** > **Rules Editor**.
  4. Click the add (**+**) icon to create a new rule, paste the YARA-L content from the downloaded file, and click **Save as new**.



For more information about managing rules, see [Manage rules using the Rules Editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules).

## Manage and customize detection rules

After you import the SAP YARA-L detection rules, configure their operational states and tune them by using data tables or custom rule conditions to match your SAP environment.

### Configure rule operational states

Google SecOps disables imported YARA-L rules by default. To start evaluating SAP logs against the imported rules, configure the operational state for each rule. For information about how to enable rules and manage rule actions, see [Run a rule on live data](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data) and [View all rules in the Rules dashboard](https://docs.cloud.google.com/chronicle/docs/detection/view-all-rules#rule-actions).

You can configure the following operational states for each rule:

  * **Detecting** : Evaluates incoming logs against the rule and generates detections. Enable this state for all imported SAP rules that apply to your landscape.
  * **Alerting** : Promotes rule detections to formal alerts. The SOAR engine uses alerts to create and group investigation cases.
  * **Risk scoring** : Assigns a risk score to entities involved in a detection so you can prioritize high-risk users or SAP systems. For information about risk scores, see [Specify entity risk score in rules](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax#risk_score_outcome_variable).



### Customize rules with data tables

SAP detection rules reference specific Google SecOps data tables to identify production systems, monitor sensitive programs, and exclude authorized maintenance activity by SAP Basis administrators. For some of these rules to function as expected, you need to populate their associated data tables. For more information about required tables, see the documentation or comments within the rule file in GitHub.

To populate the SAP data tables, do the following:

  1. In the Google SecOps menu, go to **Investigation** > **Data Tables**.
  2. Create or open the data tables referenced by your SAP detection rules and populate them with values specific to your landscape. Common SAP-specific data tables include the following: 
     * `SAP_ADMIN_USERS`: SAP usernames of authorized Basis administrators who perform routine system maintenance.
     * `production_systems`: SAP System IDs (SIDs), such as `PRD` or `DS4`, that identify your production SAP environments.
     * `sensitive_abap_programs`: Custom or standard ABAP programs and reports that require heightened execution monitoring.
     * `sensitive_roles` and `sensitive_tables`: Critical SAP components that trigger alerts when accessed.



For information about how to manage and query supplementary data, see [Use data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables).

### Customize rules by using the Rules Editor

Use the **Rules Editor** to customize rule logic, such as adding specific SAP transaction codes or excluding authorized users from detection findings. Common edits include:

  * **Filter events by transaction codes** : Add or remove specific SAP transaction codes (TCODEs) to narrow the rule's scope.
  * **Exclude authorized activity** : Add logic to ignore events that specific service accounts, administrative users, or maintenance windows generate.
  * **Adjust correlation windows** : Modify the `match` or `duration` values in multi-event rules to change the timeframe for related security events.



For example, to exclude activity that a specific maintenance account performs, add the following condition to the `events` section of the rule:
    
    
    $event.principal.user.userid != "MAINTENANCE_USER"
    

Replace `MAINTENANCE_USER` with the SAP username of the maintenance account.

To exclude all authorized administrators from the `SAP_ADMIN_USERS` data table, add the following condition:
    
    
    not $event.principal.user.userid in %SAP_ADMIN_USERS
    

For more information about managing rules, see [Manage rules using the Rules Editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules).

## Investigate SAP-related cases

In Google SecOps, an [alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert) indicates that a YARA-L rule matched activity in your SAP logs. A [case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview) groups one or more related alerts together for your investigation.

### Access cases

To inspect SAP security cases, do the following:

  1. In the Google SecOps menu, go to **Response** > **Cases**.
  2. Select a case from the list to open its details. You can filter the queue by **Priority** , **Status** , or **Search** for SAP-specific alerts (for example, by entering `SAP`).



### Navigate the analyst interface

When you open a case, use the following views to investigate the underlying SAP activity:

  * [**Case overview**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview): Displays the Gemini case summary, case metadata, and all associated alerts.
  * [**Case wall**](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview#case-wall-tab): Provides a chronological timeline of case events where you can add analyst notes, attach artifacts, and review executed [SOAR playbook actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen).
  * [**Alert view**](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-alert): Shows the specific Unified Data Model (UDM) events and rule name that triggered the alert. You can customize column layouts in this view to highlight SAP-specific UDM fields.



### Use automated analysis with Gemini

When Google SecOps creates a case, Gemini generates a case summary that includes:

  * A description of the detected threat.
  * Recommended investigation steps.
  * Suggested remediation actions.



This summary provides context to help you investigate SAP-specific log events. For information about the case summary widget, see [Summarize cases with Gemini](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/using-the-gemini-case-summary-widget).

## What's next

  * [SAP to UDM field mapping reference](https://docs.cloud.google.com/sap/docs/secops/udm-mapping-overview): Review how SAP log fields map to the Unified Data Model.
  * [Configure the SAP response integration](https://docs.cloud.google.com/sap/docs/secops/configure-sap-response-integration): Learn how to deploy the SAP RFC Gateway and use prebuilt mitigation actions to contain threats, such as locking compromised SAP users.
  * [Troubleshoot SAP log ingestion and response](https://docs.cloud.google.com/sap/docs/secops/troubleshooting): Resolve common configuration and connectivity issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
