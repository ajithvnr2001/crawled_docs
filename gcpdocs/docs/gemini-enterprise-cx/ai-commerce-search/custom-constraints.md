---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/custom-constraints/
title: Use custom organization policies \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:32:20.340618+00:00
---

# Use custom organization policies  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Use custom organization policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `retail.googleapis.com/AttributesConfig`
  * `retail.googleapis.com/Catalog`
  * `retail.googleapis.com/Control`
  * `retail.googleapis.com/Product`
  * `retail.googleapis.com/ServingConfig`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

### Benefits

You can use custom organization policies to enforce governance rules on your AI Commerce Search resources. For example, you can enforce that products cannot be created with forbidden types, ensure specific catalog configurations, or restrict modifications to search and serving controls. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## AI Commerce Search supported resources

The following table lists the AI Commerce Search resources that you can reference in custom constraints. 

Resource | Field  
---|---  
retail.googleapis.com/AttributesConfig |  `resource.catalogAttributes[*].dynamicFacetableOption`  
`resource.catalogAttributes[*].exactSearchableOption`  
`resource.catalogAttributes[*].facetConfig.facetIntervals.exclusiveMaximum`  
`resource.catalogAttributes[*].facetConfig.facetIntervals.exclusiveMinimum`  
`resource.catalogAttributes[*].facetConfig.facetIntervals.maximum`  
`resource.catalogAttributes[*].facetConfig.facetIntervals.minimum`  
`resource.catalogAttributes[*].facetConfig.ignoredFacetValues.endTime`  
`resource.catalogAttributes[*].facetConfig.ignoredFacetValues.startTime`  
`resource.catalogAttributes[*].facetConfig.ignoredFacetValues.values`  
`resource.catalogAttributes[*].facetConfig.mergedFacet.mergedFacetKey`  
`resource.catalogAttributes[*].facetConfig.mergedFacetValues.mergedValue`  
`resource.catalogAttributes[*].facetConfig.mergedFacetValues.values`  
`resource.catalogAttributes[*].facetConfig.rerankConfig.facetValues`  
`resource.catalogAttributes[*].facetConfig.rerankConfig.rerankFacet`  
`resource.catalogAttributes[*].indexableOption`  
`resource.catalogAttributes[*].key`  
`resource.catalogAttributes[*].recommendationsFilteringOption`  
`resource.catalogAttributes[*].retrievableOption`  
`resource.catalogAttributes[*].searchableOption`  
`resource.catalogAttributes[*].typeaheadConfig.caseSentive`  
`resource.catalogAttributes[*].typeaheadConfig.tokenizable`  
`resource.catalogAttributes[*].typeaheadOption`  
`resource.name`  
retail.googleapis.com/Catalog |  `resource.catalogConfig.attributeConfigs.attribute`  
`resource.catalogConfig.attributeConfigs.dynamicFacetable`  
`resource.catalogConfig.attributeConfigs.indexable`  
`resource.catalogConfig.attributeConfigs.searchable`  
`resource.catalogConfig.attributeConfigs.typeaheadable`  
`resource.displayName`  
`resource.merchantCenterLinkingConfig.links.branchId`  
`resource.merchantCenterLinkingConfig.links.destinations`  
`resource.merchantCenterLinkingConfig.links.feeds.dataSourceId`  
`resource.merchantCenterLinkingConfig.links.feeds.primaryFeedId`  
`resource.merchantCenterLinkingConfig.links.feeds.primaryFeedName`  
`resource.merchantCenterLinkingConfig.links.languageCode`  
`resource.merchantCenterLinkingConfig.links.merchantCenterAccountId`  
`resource.merchantCenterLinkingConfig.links.regionCode`  
`resource.name`  
`resource.productLevelConfig.ingestionProductType`  
`resource.productLevelConfig.merchantCenterProductIdField`  
retail.googleapis.com/Control |  `resource.displayName`  
`resource.name`  
`resource.rule.boostAction.boost`  
`resource.rule.boostAction.productsFilter`  
`resource.rule.condition.activeTimeRange.endTime`  
`resource.rule.condition.activeTimeRange.startTime`  
`resource.rule.condition.contextItemFilters`  
`resource.rule.condition.pageCategories`  
`resource.rule.condition.queryTerms.fullMatch`  
`resource.rule.condition.queryTerms.value`  
`resource.rule.doNotAssociateAction.doNotAssociateTerms`  
`resource.rule.doNotAssociateAction.queryTerms`  
`resource.rule.doNotAssociateAction.terms`  
`resource.rule.filterAction.filter`  
`resource.rule.forceReturnFacetAction.facetPositionAdjustments.attributeName`  
`resource.rule.forceReturnFacetAction.facetPositionAdjustments.position`  
`resource.rule.ignoreAction.ignoreTerms`  
`resource.rule.onewaySynonymsAction.onewayTerms`  
`resource.rule.onewaySynonymsAction.queryTerms`  
`resource.rule.onewaySynonymsAction.synonyms`  
`resource.rule.pinAction.pinMap`  
`resource.rule.pinAction.variantOverrides`  
`resource.rule.redirectAction.redirectUri`  
`resource.rule.removeFacetAction.attributeNames`  
`resource.rule.replacementAction.queryTerms`  
`resource.rule.replacementAction.replacementTerm`  
`resource.rule.replacementAction.term`  
`resource.rule.twowaySynonymsAction.synonyms`  
`resource.searchSolutionUseCase`  
`resource.solutionTypes`  
retail.googleapis.com/Product |  `resource.attributes[*].indexable`  
`resource.attributes[*].numbers`  
`resource.attributes[*].searchable`  
`resource.attributes[*].text`  
`resource.audience.ageGroups`  
`resource.audience.genders`  
`resource.availability`  
`resource.availableQuantity`  
`resource.availableTime`  
`resource.brands`  
`resource.categories`  
`resource.collectionMemberIds`  
`resource.colorInfo.colorFamilies`  
`resource.colorInfo.colors`  
`resource.conditions`  
`resource.description`  
`resource.expireTime`  
`resource.fulfillmentInfo.placeIds`  
`resource.fulfillmentInfo.type`  
`resource.gtin`  
`resource.images.height`  
`resource.images.uri`  
`resource.images.width`  
`resource.languageCode`  
`resource.materials`  
`resource.name`  
`resource.patterns`  
`resource.priceInfo.cost`  
`resource.priceInfo.currencyCode`  
`resource.priceInfo.originalPrice`  
`resource.priceInfo.price`  
`resource.priceInfo.priceEffectiveTime`  
`resource.priceInfo.priceExpireTime`  
`resource.primaryProductId`  
`resource.promotions.description`  
`resource.promotions.displayName`  
`resource.promotions.endTime`  
`resource.promotions.minimumQuantity`  
`resource.promotions.originalCreateTime`  
`resource.promotions.percentOff`  
`resource.promotions.placeFilter`  
`resource.promotions.productFilter`  
`resource.promotions.promotionId`  
`resource.promotions.startTime`  
`resource.publishTime`  
`resource.rating.averageRating`  
`resource.rating.ratingCount`  
`resource.rating.ratingHistogram`  
`resource.sizes`  
`resource.title`  
`resource.ttl`  
`resource.type`  
`resource.uri`  
retail.googleapis.com/ServingConfig |  `resource.boostControlIds`  
`resource.displayName`  
`resource.diversityLevel`  
`resource.diversityType`  
`resource.doNotAssociateControlIds`  
`resource.dynamicFacetSpec.mode`  
`resource.enableCategoryFilterLevel`  
`resource.facetControlIds`  
`resource.filterControlIds`  
`resource.forceReturnFacetControlIds`  
`resource.ignoreControlIds`  
`resource.ignoreRecsDenylist`  
`resource.modelId`  
`resource.name`  
`resource.onewaySynonymsControlIds`  
`resource.personalizationSpec.mode`  
`resource.pinControlIds`  
`resource.priceRerankingLevel`  
`resource.redirectControlIds`  
`resource.removeFacetControlIds`  
`resource.replacementControlIds`  
`resource.solutionTypes`  
`resource.synonymsControlIds`  
`resource.twowaySynonymsControlIds`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.restrictProductType`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/Cluster`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.restrictProductType`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `retail.googleapis.com/Product`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.type == 'FORBIDDEN'"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.restrictProductType`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that denies the creation of products with a forbidden type.

Before you begin, you need to know the following:

  * Your organization ID
  * A project ID



### Create the constraint

  1. Save the following file as `constraint-restrict-product-type.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictProductType
         resourceTypes:
         - retail.googleapis.com/Product
         methodTypes:
         - CREATE
         - UPDATE
         condition: "resource.type == 'FORBIDDEN'"
         actionType: DENY
         displayName: Restrict forbidden product type
         description: Products with forbidden type are not permitted.
         

This defines a constraint where any product created or updated with `type == 'FORBIDDEN'` is denied.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-restrict-product-type.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT           ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                      DISPLAY_NAME
         custom.restrictProductType  DENY         CREATE,UPDATE  retail.googleapis.com/Product       Restrict forbidden product type
         




### Create the policy

  1. Save the following file as `policy-restrict-product-type.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.restrictProductType
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-restrict-product-type.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT                  LIST_POLICY    BOOLEAN_POLICY    ETAG
         custom.restrictProductType  -              SET               COCs...
         




After you apply the policy, wait about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try creating a product with type `FORBIDDEN`:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/branches/default_branch/products?productId=test-product \
      -d '{"title": "Test Product", "type": "FORBIDDEN"}'
    

The output is similar to the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.restrictProductType": "Products with forbidden type are not permitted."].
    

## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Restrict product type | 
    
    
      name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictProductType
      resourceTypes:
      - retail.googleapis.com/Product
      methodTypes:
      - CREATE
      - UPDATE
      condition: "resource.type == 'FORBIDDEN'"
      actionType: DENY
      displayName: Restrict forbidden product type
      description: Products with forbidden type are not permitted.  
  
Restrict serving control solutions | 
    
    
      name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictControlSolutionType
      resourceTypes:
      - retail.googleapis.com/Control
      methodTypes:
      - CREATE
      - UPDATE
      condition: "resource.solutionTypes.exists(t, t == 'SOLUTION_TYPE_SEARCH')"
      actionType: DENY
      displayName: Restrict search solution controls
      description: Creation or modification of search solution controls is restricted.  
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
