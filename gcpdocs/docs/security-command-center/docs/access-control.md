---
url: https://docs.cloud.google.com/security-command-center/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:26:41.124141+00:00
---

# Access control with IAM  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Identity and Access Management (IAM) roles let you control who can view and manage assets, findings, and security sources across your Security Command Center environment at different levels of your resource hierarchy. The specific roles that you need depend on whether you activate Security Command Center at the organization level or project level. For information about these activation scopes, see [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).

## Where to find access control information

For information about the IAM roles that you need to use Security Command Center, see one of the following pages depending on the level at which you activated Security Command Center:

  * [IAM for organization-level activations of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/access-control-org)

  * [IAM for project-level activations of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/access-control-project)




## Migrate custom roles to use `securitycentermanagement` permissions

Starting November 09, 2026, actions performed on the **Settings** page require one or more of the following `securitycentermanagement` permissions:

  * `securitycentermanagement.securityCenterServices.get`
  * `securitycentermanagement.securityCenterServices.list`
  * `securitycentermanagement.securityCenterServices.update`



If you used predefined IAM roles to grant access to the **Settings** page, no changes are required.

The following predefined IAM roles are updated to include the new permissions.

  * The `roles/securityposture.admin` and `roles/securityposture.postureDeployer` roles include the following permissions: 

    * `securitycentermanagement.securityCenterServices.get`
    * `securitycentermanagement.securityCenterServices.list`
    * `securitycentermanagement.securityCenterServices.update`
  * The Writer (`roles/writer`) and Editor (`roles/editor`) roles include the `securitycentermanagement.securityCenterServices.update` permission. 




If you use custom roles that include the permissions listed in the following table, update the custom role to include the replacement permission. Until the custom role is updated, users granted that role might see a `PERMISSION_DENIED` error when using the **Settings** page.

Replace this permission: | With this permission:  
---|---  
`securitycenter.  
containerthreatdetectionsettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
containerthreatdetectionsettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
eventthreatdetectionsettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
eventthreatdetectionsettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
eventthreatdetectionsettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
integratedvulnerabilityscannersettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
integratedvulnerabilityscannersettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
integratedvulnerabilityscannersettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
organizationsettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
rapidvulnerabilitydetectionsettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
rapidvulnerabilitydetectionsettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
rapidvulnerabilitydetectionsettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
securitycentersettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
securityhealthanalyticssettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
securityhealthanalyticssettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
securityhealthanalyticssettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
virtualmachinethreatdetectionsettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
virtualmachinethreatdetectionsettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
virtualmachinethreatdetectionsettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
`securitycenter.  
websecurityscannersettings.calculate` | This permission isn't required. Replaced by `securitycentermanagement.securityCenterServices.get`  
`securitycenter.  
websecurityscannersettings.get` | `securitycentermanagement.  
securityCenterServices.get`  
`securitycenter.  
websecurityscannersettings.update` | `securitycentermanagement.  
securityCenterServices.update`  
Any permission starting with `securitycenter.  
securityhealthanalyticscustommodules.*` | The corresponding permission starting with `securitycentermanagement.  
securityhealthanalyticscustommodules.*`  
Any permission starting with `securitycenter.  
effectivesecurityhealthanalyticscustommodules.*` | The corresponding permission starting with `securitycentermanagement.  
effectivesecurityhealthanalyticscustommodules.*`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
