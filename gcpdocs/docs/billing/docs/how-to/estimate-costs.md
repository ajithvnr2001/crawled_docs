---
url: https://docs.cloud.google.com/billing/docs/how-to/estimate-costs/
title: Estimate your monthly costs \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:34:11.783160+00:00
---

# Estimate your monthly costs  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/estimate-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Estimate your monthly costs Stay organized with collections  Save and categorize content based on your preferences. 

Use cost estimator tools to estimate the monthly costs of your AI agents and hypothetical workloads. These estimates help you set spend caps, create Cloud Billing budgets and alerts, allocate project quotas, and get financial sign-off for a launch.

  * To generate high-level estimates based on reference architectures for agents built with Gemini Enterprise Agent Platform, use the cost estimator agent (preview) that is available in the Billing section of the Google Cloud console.
  * To get cost estimates for your planned Google Cloud workloads and other cloud infrastructure, use the Google Cloud pricing calculator. With the pricing calculator, you can estimate costs for a wide range of Google Cloud services and products.

**Important** : **All estimates** provided by the cost estimator agent or the Google Cloud pricing calculator serve solely as **non-binding planning projections** , rather than binding price quotes, fixed fees, or spending limits. Your actual metered usage strictly determines the final charges on your Cloud Billing invoice. 

## Estimate costs for AI agents using the cost estimator agent (preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the **cost estimator agent** , you can generate high-level estimates based on reference architectures for agents built with _Gemini Enterprise Agent Platform_.

During the preview, you can use the cost estimator agent to estimate the costs for the following services:

  * Agents built on the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform), which includes the built-in Vertex AI Search (now called Agent Search) and Google Cloud Observability components.



To get cost estimates for your planned usage of other Google Cloud services (such as BigQuery, Cloud SQL, Google Kubernetes Engine, or Cloud Storage), use the Google Cloud pricing calculator.

### How the cost estimator agent works

Estimating the monthly cost of an AI agent works differently than sizing traditional cloud infrastructure. Instead of picking fixed VM shapes or storage tiers, cost estimates for AI agents need to account for three areas of usage:

  * **Token usage** : Estimating how many input and output tokens a typical user interaction uses, and how context caching can reduce repeated input token costs.
  * **Behavior of different agent deployments** : Understanding how your chosen agent pattern operates in practice, such as how often an orchestrator coordinates sub-agents, calls tools, or invokes APIs during a session.
  * **Supporting infrastructure** : Including the platform services that run alongside the model, such as search grounding, managed runtime compute, session storage, safety scanning (Model Armor), evaluations, and observability (traces, logs, metrics).



#### Use plain language to describe the business need and adjust assumptions

The **cost estimator agent** lets you use plain language to model expected monthly spend so you have a concrete baseline for your budgets and spend caps.

  * **Start from a business need, not a SKU list**. Describe your use case, user volume, or preferred Gemini model. To get you started, the agent matches your use case to one of four reference architectures and prefills sample starting values for tokens, sessions, and runtime that you can customize.
  * **Adjust assumptions in chat or in the form**. Change traffic drivers (users, sessions, turns, tool calls) or component details (models, token counts, caching percentage, search tier) and then calculate the cost estimate.



#### Prices: Cost estimates use your actual billing account rates

The Google Cloud pricing engine calculates all estimates deterministically using your Cloud Billing account's price sheet, applying your contracted SKU prices and discounts to your estimated usage. Any SKUs not covered by a contract price use the public list prices. The AI agent never guesses SKU prices or calculates totals on its own. You can export the estimate with the full SKU breakdown to a CSV file.

#### Cost estimates are provided for informational purposes only

Treat outputs as planning estimates. Actual costs depend on real consumption. The tool models projected spend based on the traffic and token assumptions you enter. After you deploy your agent, Cloud Billing bills you strictly for metered consumption, including the exact tokens, grounding calls, runtime hours, and logs your agent consumes.

#### Sample agent architectures

The cost estimator agent supports the following AI agent reference architectures:

Sample architecture | Typical use case  
---|---  
**Conversational Chatbot** | Multi-turn customer or internal helpdesk assistants using Gemini models, prompt caching, search grounding, agent runtime execution, and observability tracing.  
**Workflow Operator** | Task automation agents that execute multi-step tool calls, API integrations, deterministic workflows, and enterprise systems integration with back-office workflows.  
**Autonomous Researcher** | Deep research and synthesis agents that coordinate a main orchestrator with specialized sub-agents and enterprise search.  
**Multi-agent Orchestrator** | Complex system that coordinates a central reasoning orchestrator with multiple specialized sub-agents, high-volume tool and API execution, enterprise search grounding, and end-to-end observability.  
  
#### Google Cloud products and levers included in the calculator

Across the sample agent architectures, the calculator prices the following Google Cloud product areas:

Product area | Included components | Key levers that you can adjust  
---|---|---  
**Agent Platform** | Orchestrator, sub-agents, Agent Runtime, Agent sessions, Agent Gateway, Model Armor, Agent evals | **Models and tokens** : You can select a Gemini model (for example, Gemini 3.1, 3.5, 4.0, and later Flash and Pro releases), input tokens, percentage of input tokens cached, and output tokens. **Grounding** : percentage of requests grounded with Google Search, Enterprise Web, and Google Maps. **Runtime and sessions** : Agent Runtime vCPU hours and RAM hours, session read/write vCPU hours and GiB storage, and Agent Gateway requests. **Safety and evals** : Model Armor percentage of tokens scanned, monthly evaluation runs and token volume.  
**Agent Search** (formerly Vertex AI Search) | Agent Search | Monthly search request volume.  
**Google Cloud's operations suite** | Google Cloud Observability - traces, logging, monitoring | Cloud Trace spans, Cloud Logging storage (GiB), and Cloud Monitoring metrics volume (MiB).  
  
### Limitations, consumption variability, and exclusions

The cost estimator agent is subject to the following limitations:

  * **Currency** : The calculator uses your Cloud Billing account's default currency for all prices when it's calculating the estimated costs. However, the agent reports the _results of the estimate_ in **USD**.
  * **Language** : The cost estimator agent only supports interactions in the **English** language.
  * **Estimates are only as accurate as the usage assumptions entered**. The calculator multiplies your unit SKU rates by the session, turn, token, caching, and runtime numbers in the form. In production, real token intensity and sub-agent fan-out vary by user prompt and agent code. Always monitor your actual metered spend after you deploy and set Cloud Billing budgets and spend caps as needed.
  * **Supports Gemini Enterprise Agent Platform only**. During this preview, the cost estimator agent only prices the Gemini Enterprise Agent Platform stack. You can't add other Google Cloud services (such as BigQuery, Cloud SQL, Google Kubernetes Engine, Cloud Storage, or Pub/Sub) to your estimate. To get cost estimates for any additional Google Cloud services alongside your agent, go to the Google Cloud pricing calculator.
  * **Doesn't query historical billed spend or change account settings**. This agent is strictly for forward-looking estimates. It can't look up past invoices, explain historical cost spikes, or create budgets and committed use discounts (CUDs). For historical AI spend analysis, use the [AI cost summary agent](https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary) (**Your AI spend** card) on the Cloud Billing **Overview** page, and review [cost reports for Gemini Enterprise](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).
  * **Prefilled values are starting placeholders, not recommendations**. To help you get started, the form provides prefilled sample values along with any numbers you provide in your prompt. Because every agent workload is different, review and adjust these inputs to match your expected usage.
  * **Manual percentage discounts aren't supported**. You can't ask the agent to apply an arbitrary flat discount (for example, _"take 20% off the total"_). Every rate must come from the public price list catalog or your billing account's official price sheet.
  * **Exclusions and official disclaimer** :

    * **Cost estimates are provided for informational purposes only.** Your actual billed amounts vary based on your actual usage and configuration.
    * **Exclusions** : Costs associated with human labor, licenses, business process mapping, solution re-architecting, grounding data stores, or interacting third-party tools are not covered by this tool or its estimates.



### Permissions required to access and run the cost estimator agent

The cost estimator agent is located in the Billing section of the Google Cloud console. To access the estimator and generate cost estimates for agents built on Gemini Enterprise Agent Platform, you need permissions on the Cloud Billing account. Your administrator must grant you a role on the Cloud Billing account that lets you access the billing account, view all costs in the billing account, and generate cost estimates based on contract prices or list prices.

Custom role | Predefined roles  
---|---  
If you're using a custom role to access contract prices, you need a role granted on your Cloud Billing account that includes the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing): 

  * billing.accounts.get
  * billing.accounts.getIamPolicy
  * billing.accounts.getSpendingInformation
  * billing.billingAccountPrice.get
  * billing.billingAccountPrices.list
  * billing.billingAccountServices.get
  * billing.billingAccountServices.list
  * billing.billingAccountSkuGroupSkus.get
  * billing.billingAccountSkuGroupSkus.list
  * billing.billingAccountSkuGroups.get
  * billing.billingAccountSkuGroups.list
  * billing.billingAccountSkus.get
  * billing.billingAccountSkus.list

|  To gain the required permissions using a [ predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles), ask your administrator to grant you one of the following [ Cloud Billing IAM roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on your Cloud Billing account:

  * Billing Account Viewer
  * Billing Account Administrator

For more information about Cloud Billing permissions, see the following:

  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)

  
  
### Generate a cost estimate for an agent

Gemini can help you generate cost estimates for your AI workloads. Get started by describing your business needs or viewing a list of typical agent types.

**Caution:** **The cost estimator agent produces cost estimates for planning purposes only. Actual costs are 100% based on metered consumption.** Generating an estimate does not lock in a fixed monthly price or cap your spend. AI agents are consumption-based workloads. Your production agent might exceed the assumptions in the form. Your actual billed costs scale to match your usage. Costs increase if your agent processes longer prompts, runs more reasoning loops or tool retries, has a lower cache hit rate, or serves more traffic than estimated.

To get estimates for agents built with Gemini Enterprise Agent Platform, complete the following steps:

  1. **Access the cost estimator agent** :

     1. In the Google Cloud console, go to the Billing **Overview** page.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

     2. At the prompt, choose the Cloud Billing account you want to view.

The **Overview** page opens for the Cloud Billing account.

     3. In the Billing navigation menu, in the **Cost optimization** section, select **Cost estimation**.

  2. **Describe the agent you want to build**. Start with a prompt using one of the following options:

     * **Custom prompt** : Enter a prompt describing your workload. For example, _"Help me estimate the cost of an HR department helpdesk agent that can support 5,000 internal users."_
     * **Starter prompt** : Pick one of the starter prompts on the page.
  3. **Confirm a sample architecture**. The agent recommends the closest matching sample agent architecture for your use case, explains what components are included, and asks you to confirm before loading parameters.

  4. **Review and edit workload assumptions**.

     1. **Review** : After you confirm the reference architecture, the agent loads a core configuration form and prefills the parameters with sample starting workload usage amounts and any numbers from your prompt. These values are just placeholders to help you get started.
     2. **Edit** : Adjust the traffic inputs and component details to match your expected usage. You can edit the form directly or use a prompt to provide more details.
  5. **Generate the estimate and download the CSV**.

     1. Click **Generate estimate**. The cost estimator agent returns your total estimated monthly cost, a breakdown by agent component, and prepares the cost estimate details for download to a CSV file.

     2. Click **Download CSV** to downloads a `cost_estimate.csv` file that contains the architecture estimate total and SKU-level details for all parameters included in the estimate. The SKU-level details include the following:

        * Component / Item
        * Product
        * Display Name
        * SKU ID
        * Region
        * Usage Unit
        * Base Cost
        * List Cost
        * Estimated Cost
        * Currency



* * *

## Estimate costs for Google Cloud workloads using the pricing calculator

The [Google Cloud pricing calculator](https://cloud.google.com/products/calculator) helps you estimate the monthly costs of hypothetical workloads and other cloud infrastructure for an application.

With the pricing calculator, you can estimate costs for a wide range of Google Cloud services and products.

### Optional: Link your Cloud Billing account to the pricing calculator

If your Cloud Billing account is associated with a custom pricing contract, you can link the billing account to the pricing calculator to get cost estimates that factor in your contract prices.

#### Permissions required to link a billing account

To link the billing account to the pricing calculator, you must be assigned a role on the Cloud Billing account that gives you the permissions needed to view the custom contract prices associated with the billing account.

Custom role | Predefined roles  
---|---  
If you're using a custom role to access contract prices, you need a role granted on your Cloud Billing account that includes the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing): 

  * billing.accounts.get
  * billing.accounts.list
  * billing.billingAccountPrice.get
  * billing.billingAccountPrices.list
  * billing.billingAccountServices.get
  * billing.billingAccountServices.list
  * billing.billingAccountSkuGroupSkus.get
  * billing.billingAccountSkuGroupSkus.list
  * billing.billingAccountSkuGroups.get
  * billing.billingAccountSkuGroups.list
  * billing.billingAccountSkus.get
  * billing.billingAccountSkus.list

|  To gain the required permissions using a [ predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles), ask your administrator to grant you one of the following [ Cloud Billing IAM roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on your Cloud Billing account:

  * Billing Account Viewer
  * Billing Account Administrator

For more information about Cloud Billing permissions, see the following:

  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)

  
  
### Access the pricing calculator

With the pricing calculator, you can estimate costs for a wide range of Google Cloud services and products.

[Go to the pricing calculator](https://cloud.google.com/products/calculator)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
