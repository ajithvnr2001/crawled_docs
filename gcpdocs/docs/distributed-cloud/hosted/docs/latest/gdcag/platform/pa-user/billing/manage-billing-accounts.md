---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts/
title: Create and link billing accounts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T05:49:03.073721+00:00
---

# Create and link billing accounts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/manage-billing-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create and link billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to create a Google Distributed Cloud (GDC) air-gapped billing account to track resource usage.

Distributed Cloud environments require a billing account to track usage costs for projects and organizations. All billing accounts within an organization use a single price sheet to charge service usage to the customer. If you don't link a billing account to an organization or project, you'll lose cost data associated with the resource, resulting in cost discrepancies.

This document is for developers in platform administrator or application operator groups that create and administer billing accounts in GDC. For more information, see [Audiences for GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences) documentation.

## Before you begin

### Request IAM roles

Contact your Organization Identity and Access Management (IAM) Admin to request the following roles:

  * Global Organization Billing Account Admin (`organization-billing-account-admin`): create, manage, and bind the `BillingAccount` resource in the `platform` namespace.

  * Global Organization Billing Account User (`organization-billing-account-user`): read, list, and bind the `BillingAccount` resource in the `platform` namespace.

  * Global Organization Billing Account Manager (`organization-billing-manager`): read, list, create, and update the `BillingAccountBinding` resource across namespaces (such as the `platform` namespace for organization-level billing or a project namespace for project-level billing).


**Note:** The same IAM role manages billing for all projects. To separate billing administration for different projects, you must use one dedicated role for each project. Contact your Organization IAM Admin to [create additional roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/custom-roles) for individual project administration requirements.

### Get the kubeconfig file

To run verification commands against the global API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#global-resources-kubeconfig) the kubeconfig file for the global API server if you don't have one.

  2. Use the path to the kubeconfig file of the global API server to replace `GLOBAL_API_SERVER_KUBECONFIG` in these instructions.


**Note:** When managing `BillingAccount` and `BillingAccountBinding` custom resources (CRs) using YAML manifests, note that they are global resources and must be applied to the global API server. Don't apply or modify these YAML files directly using `kubectl apply` or `kubectl edit`. Instead, follow the Git-based Infrastructure as Code (IaC) workflow in the `IAC-R0004: Create and merge a merge request` runbook to commit them to the `infrastructure/global/orgs/ORG_NAME/oc/bil/` directory of the `iac` repository and go through the multi-party approval (MPA) process.

## Create a new billing account

###  CLI 

To create a billing account, use the `gdcloud billing accounts create` command.

For more information, see [gdcloud billing accounts create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-billing-accounts-create).

###  IaC 

To create a billing account on the global API server using Infrastructure as Code (IaC), do the following:

  1. Create a `billingaccount-BIL_ACCOUNT_NAME.yaml` file in the `infrastructure/global/orgs/ORG_NAME/oc/bil/` directory of your local `iac` repository (`IAC_REPO_PATH/infrastructure/global/orgs/ORG_NAME/oc/bil/billingaccount-BIL_ACCOUNT_NAME.yaml`), and add the `BillingAccount` custom resource with the following contents:
         
         apiVersion: billing.global.gdc.goog/v1
         kind: BillingAccount
         metadata:
           namespace: platform
           name: BIL_ACCOUNT_NAME
         spec:
           displayName: BIL_DISPLAY_NAME
           paymentSystemConfig:
             cloudBillingConfig:
               accountID: CLOUD_BILLING_ACCOUNT_ID
         

Replace the following variables:

     * `IAC_REPO_PATH`: the path to the root of your local `iac` repository.
     * `ORG_NAME`: the name of the organization.
     * `BIL_ACCOUNT_NAME`: the name of the billing account, for example, `test-billing-account`.
     * `BIL_DISPLAY_NAME`: the billing account display name, for example, `"Test Billing Account"`.
     * `CLOUD_BILLING_ACCOUNT_ID`: your Google Cloud billing account ID, for example, `"012345-6789AB-CDEF01"`.
  2. Verify your payment configuration type. Distributed Cloud billing accounts must have one of the following payment configurations:

     * `cloudBillingConfig`: the default payment configuration. This configuration stores a Cloud Billing account ID.

     * `customConfig`: a custom configuration for partners to store their payment configuration to bill the organization. `customConfig` supports a dictionary of key-value strings, with a mandatory key `payment-config-type`.

The following examples show `BillingAccount` YAML file snippets for different payment configurations:

`cloudBillingConfig` example:
    
    spec:
      paymentSystemConfig:
        cloudBillingConfig:
          accountID: CLOUD_BILLING_ACCOUNT_ID
    

Replace `CLOUD_BILLING_ACCOUNT_ID` with your Google Cloud billing account ID.

`customConfig` example:
    
    spec:
     paymentSystemConfig:
       customConfig:
          "payment-config-type": PAYMENT_CONFIG_TYPE
    

Replace `PAYMENT_CONFIG_TYPE` with your chosen payment configuration type for your custom billing configuration.

If you don't have the information for your organization's `customConfig` configuration, enter the following details:
    
    spec:
     paymentSystemConfig:
       customConfig:
          "payment-config-type": "N/A"
    

The following example YAML file shows a complete `BillingAccount` resource with the `cloudBillingConfig` configuration:
    
    apiVersion: billing.global.gdc.goog/v1
    kind: BillingAccount
    metadata:
      namespace: platform
      name: test-billing-account
    spec:
      displayName: "Test Billing Account"
      paymentSystemConfig:
        cloudBillingConfig:
          accountID: "012345-6789AB-CDEF01"
    

  3. Wire the resource in the `kustomization.yaml` hierarchy of your local `iac` repository (which targets the global API server) and submit a merge request:

     1. Ensure all three `kustomization.yaml` levels under `infrastructure/global/orgs/ORG_NAME/` reference the billing resource and its parent directories:

        * In `infrastructure/global/orgs/ORG_NAME/oc/bil/kustomization.yaml`, include `billingaccount-BIL_ACCOUNT_NAME.yaml` in the `resources` list (keeping any existing billing account or binding files):
              
              apiVersion: kustomize.config.k8s.io/v1beta1
              kind: Kustomization
              resources:
              # Keep existing resources in this list
              - billingaccount-BIL_ACCOUNT_NAME.yaml
              

        * In `infrastructure/global/orgs/ORG_NAME/oc/kustomization.yaml`, ensure `bil` is listed in `resources`:
              
              apiVersion: kustomize.config.k8s.io/v1beta1
              kind: Kustomization
              resources:
              # Keep existing resources in this list
              - bil
              

        * In `infrastructure/global/orgs/ORG_NAME/kustomization.yaml`, ensure `oc` is listed in `resources`:
              
              apiVersion: kustomize.config.k8s.io/v1beta1
              kind: Kustomization
              resources:
              # Keep existing resources in this list
              - oc
              

     2. Commit and push the changes to a new branch in GitLab to create a merge request and trigger the multi-party approval (MPA) workflow by following the `IAC-R0004: Create and merge a merge request` runbook:
            
            cd IAC_REPO_PATH
            git checkout -b USER_BRANCH
            git add infrastructure/global/orgs/ORG_NAME/oc/bil/billingaccount-BIL_ACCOUNT_NAME.yaml \
                    infrastructure/global/orgs/ORG_NAME/oc/bil/kustomization.yaml \
                    infrastructure/global/orgs/ORG_NAME/oc/kustomization.yaml \
                    infrastructure/global/orgs/ORG_NAME/kustomization.yaml
            git commit -m "Create billing account"
            git -c http.sslVerify=false push -o merge_request.create origin USER_BRANCH
            

Replace `USER_BRANCH` with your chosen Git branch name.




## Link an organization or project to a billing account

You must link a billing account to the organization before creating any projects. This ensures that all projects created within the organization inherit a valid billing account by default.

You can also explicitly link a project to a specific billing account if you want it to differ from the organization's billing account.

To link an organization or project to a `BillingAccount` on the global API server using Infrastructure as Code (IaC), do the following:

  1. Create a `BillingAccountBinding` YAML file for your target scope:

###  Link an organization 

Add the following content to `billingaccountbinding-platform.yaml`:
         
         apiVersion: billing.global.gdc.goog/v1
         kind: BillingAccountBinding
         metadata:
           name: billing
           namespace: platform
         spec:
           billingAccountRef:
             name: BIL_ACCOUNT_NAME
             namespace: platform
         

Replace `BIL_ACCOUNT_NAME` with the name of the billing account.

###  Link a project 

Add the following content to `billingaccountbinding-PROJECT_NAME.yaml`:
         
         apiVersion: billing.global.gdc.goog/v1
         kind: BillingAccountBinding
         metadata:
           name: billing
           namespace: PROJECT_NAME
         spec:
           billingAccountRef:
             name: BIL_ACCOUNT_NAME
             namespace: platform
         

Replace the following variables:

     * `PROJECT_NAME`: the name of the project bound to the billing account.
     * `BIL_ACCOUNT_NAME`: the name of the billing account.

  2. Add the `BillingAccountBinding` resource to your `iac` repository:

     1. Place the `BillingAccountBinding` YAML file (`billingaccountbinding-platform.yaml` or `billingaccountbinding-PROJECT_NAME.yaml`) in the `infrastructure/global/orgs/ORG_NAME/oc/bil/` directory within your local `iac` repository.
     2. Add the `BillingAccountBinding` YAML filename to the `resources` list in `infrastructure/global/orgs/ORG_NAME/oc/bil/kustomization.yaml`. Also ensure that `infrastructure/global/orgs/ORG_NAME/oc/kustomization.yaml` includes `bil` and `infrastructure/global/orgs/ORG_NAME/kustomization.yaml` includes `oc` in their `resources` lists if not already present, as shown in Create a new billing account.
     3. Commit and push the changes to GitLab to create a merge request and trigger the approval workflow by following the `IAC-R0004: Create and merge a merge request` runbook, as shown in Create a new billing account.
  3. (Optional) After the merge request is approved and synced, verify the status of the `BillingAccountBinding` resource on the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe billingaccountbinding billing -n NAMESPACE
         

Replace `NAMESPACE` with `platform` for the organization, or `PROJECT_NAME` for a project.


**Note:** After 15 minutes of project creation, a default account binding is created for the project with the billing account of the parent organization.

### List billing account bindings

View a list of all deployed `BillingAccountBinding` resources and their current status across all namespaces in the organization on the global API server:
    
    
      kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG get billingaccountbinding -A -o 'custom-columns=NAME:metadata.name,NAMESPACE:metadata.namespace,BillingAccountName:spec.billingAccountRef.name,STATUS:status.conditions[0].status'
    

This command outputs the `NAME`, `NAMESPACE`, `BillingAccountName`, and `STATUS` of each `BillingAccountBinding`. The `STATUS` field indicates whether the binding is active or if there are any errors.

### Billing account hierarchy and behavior

When linking billing accounts to organizations and projects, the following hierarchy and behaviors apply:

  * **Project-level association takes precedence:** If a specific project, such as `project-A`, is explicitly linked to a `BillingAccount`, for example, `billing-account-1`, then all costs for `project-A` bill exclusively to `billing-account-1`. This project-level association remains valid regardless of any organization-level billing account settings.

  * **Organization-level association for unlinked projects:** If your organization links to a `BillingAccount`, for example, `billing-account-0`, all projects _within that organization that don't have their own explicit`BillingAccountBinding`_ automatically associate with and charge to `billing-account-0`. This association typically takes effect approximately 15 minutes after a project is created.

  * **Changing organization billing accounts:** If the billing account linked to an organization changes, for example, `billing-account-0` changes to `billing-account-new`, `billing-account-0` projects _don't_ automatically switch to `billing-account-new`. These projects remain bound to `billing-account-0`, and you must manually update the billing account to have the projects use `billing-account-new`.




## Change the linked billing account

In Distributed Cloud, you can't delete a billing account. If you need to change to your billing configuration, you must change the billing account that is linked to the organization or project by modifying the `BillingAccountBinding`. Some scenarios for this use case include the following examples:

  * Accounting rules within your company require you split charges associated with developer and production-level workloads into separate accounts.
  * You create a billing account to charge a customer contract for a one year period. When the contract expires, you must charge for the remaining period that exceeds a year.




###  For a project 

To change the billing account for a project using Infrastructure as Code (IaC), do the following:

  1. Create a new `BillingAccount` to link to the project. This account replaces the old account.

  2. (Optional) Check the `BillingAccountBinding` resource in the project namespace on the global API server to see if an explicit project-level billing account binding exists:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe billingaccountbinding billing -n PROJECT_NAME
         

Replace `PROJECT_NAME` with the name of the project. If the project is using the default billing account inherited from the organization (which is automatically created on the zonal management cluster rather than the global API server), this command returns a `NotFound` error on the global API server.

  3. Update or create the `BillingAccountBinding` definition in your local `iac` repository:

     1. In `infrastructure/global/orgs/ORG_NAME/oc/bil/`, locate `billingaccountbinding-PROJECT_NAME.yaml`. If the project was previously using the default inherited organization binding (which is automatically created on the zonal management cluster rather than the global API server, and is not yet in the `iac` repository), create `billingaccountbinding-PROJECT_NAME.yaml` as shown in Link an organization or project to a billing account and add the `BillingAccountBinding` YAML filename to the `resources` list in `infrastructure/global/orgs/ORG_NAME/oc/bil/kustomization.yaml` (along with the parent `oc/kustomization.yaml` and `orgs/ORG_NAME/kustomization.yaml` entries if not already present).
     2. Modify the `spec.billingAccountRef.name` field to use the new `BillingAccount` name created in step 1.
     3. Commit and push the changes to GitLab to create a merge request and trigger the approval workflow by following the `IAC-R0004: Create and merge a merge request` runbook, as described in Create a new billing account.
  4. (Optional) After the changes are approved and synced, verify that the `BillingAccountBinding` resource is updated on the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe billingaccountbinding billing -n PROJECT_NAME
         




The following example shows a `BillingAccountBinding` YAML file with the account `expired-billing-account` linked to the project `project-one`:
    
    
      apiVersion: billing.global.gdc.goog/v1
      kind: BillingAccountBinding
      metadata:
        # The name of a BillingAccountBinding will typically always be `billing`.
        name: billing
        # This is the project.
        namespace: project-one
      spec:
        billingAccountRef:
          # This is an example of a BillingAccount that has expired.
          name: expired-billing-account
          namespace: platform
    

The following example shows the `BillingAccountBinding` YAML file from the earlier example modified to link a new account called `new-billing-account`:
    
    
      apiVersion: billing.global.gdc.goog/v1
      kind: BillingAccountBinding
      metadata:
        name: billing
        # This is the project.
        namespace: project-one
      spec:
        billingAccountRef:
          # This is the example of the new BillingAccount.
          name: new-billing-account
          namespace: platform
    

###  For an organization 

To change the billing account for an organization using Infrastructure as Code (IaC), do the following:

  1. Create a new `BillingAccount` to link to the organization. This account replaces the old account.

  2. (Optional) Check the `BillingAccountBinding` resource in the `platform` namespace on the global API server to see which billing account is linked:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe billingaccountbinding billing -n platform
         

  3. Update the `BillingAccountBinding` definition in your local `iac` repository:

     1. Locate the `billingaccountbinding-platform.yaml` file for the organization in `infrastructure/global/orgs/ORG_NAME/oc/bil/`.
     2. Modify the `spec.billingAccountRef.name` field to use the new `BillingAccount` name created in step 1.
     3. Commit and push the changes to GitLab to create a merge request and trigger the approval workflow by following the `IAC-R0004: Create and merge a merge request` runbook, as described in Create a new billing account.
  4. (Optional) After the changes are approved and synced, verify that the `BillingAccountBinding` resource is updated on the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe billingaccountbinding billing -n platform
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
