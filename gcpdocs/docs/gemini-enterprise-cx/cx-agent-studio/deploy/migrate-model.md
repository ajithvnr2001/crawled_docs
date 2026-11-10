---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/migrate-model/
title: Migrate to a new model \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T17:31:13.956643+00:00
---

# Migrate to a new model  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/migrate-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Migrate to a new model Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to migrate an existing CX Agent Studio agent application to a different foundation [model](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#model-support), validate agent quality, and deploy the updated configuration in stages without disrupting live production traffic.

## Migration workflow overview

A complete model migration follows four stages:

  1. **Isolate your changes** : Create an immutable [version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version) of your production agent application, or [export and import](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export) the application into a separate test environment.
  2. **Update model settings** : Change the global model, review sub-agent and tool model overrides, and verify retry and fallback settings using the console, exported configuration files, or the REST API.
  3. **Evaluate and refine performance** : Test conversations in the [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator), run [evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation) with **Find issues with AI** , and use [AI Co-Builder: Arc](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc) to tune instructions until your quality metrics meet target thresholds.
  4. **Deploy in stages** : Save the validated configuration as a version and use [traffic splitting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split) on your deployment channel to shift live traffic gradually while monitoring results.



## Step 1: Isolate your changes

Before changing model settings, isolate your work so that updates and testing don't affect live customer conversations. You can isolate changes either by using versions within the same agent application or by exporting the application to a separate sandbox environment.

### Use versions in the same agent application

When your deployment channels point to a specific immutable [version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version), edits that you make to the draft agent application don't affect live traffic until you create a version and assign it to a deployment channel.

To save a baseline snapshot of your current configuration:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com) and select your agent application.
  2. Open the **Versions** pane in the agent builder.
  3. Click **\+ Create version**.
  4. Enter a descriptive name, such as `pre-model-migration-baseline`, and an optional description, and then click **Create**.
  5. Open the **Deploy** tab and verify that your active deployment channels point to an immutable version (indicated by a **Live** badge in the **Versions** pane) rather than the mutable draft.



### Export and import to a sandbox environment

If you prefer to test model changes in a separate project or staging application, export your agent application and import it into your test environment:

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com) and select your project.
  2. In the agent applications list, open the menu for your application, and then select **Export**.
  3. If your sandbox environment uses different external dependencies, such as data stores or service endpoints, extract the downloaded archive, update the `environment.json` file, and compress the directory into a zip archive. For more information, see [Environment file](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export#environment_file).
  4. In your sandbox project or test application, open the application menu, select **Import** , and upload the archive.
  5. Optional: Export your [evaluation test cases](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#import_and_export) from the source application and import them into the sandbox application so you can run regression tests.



## Step 2: Update model settings

Review the list of [supported models](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#model-support) to choose a target Gemini model that matches your agent's modality (text or voice). You can update model settings using the console, exported configuration files, or the REST API.

### Update models using the console

When migrating an agent application in the console, check the global application model, individual agent overrides, data store tool models, and fallback settings:

  1. **Change the global model** : 
     1. In the agent builder, open **Settings** to view [agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings#application).
     2. Under **Basic** > **Interactions** , select your target model in the **Global model** field. This model serves as the default for all agents in the application that don't specify an override.
  2. **Check root and sub-agent model overrides** : 
     1. In the agent builder, open the menu in the title bar of the root agent, and then select **Edit config** to view [agent settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/settings#agent).
     2. Check the **Model** field. If the agent overrides the global model, select your target model or clear the override so the agent inherits the global model.
     3. Repeat this check for every sub-agent in your agent hierarchy.
  3. **Check data store tool models** : 
     1. If your application uses [data store tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/data-store), open the **Tools** panel and select each data store tool.
     2. Expand **Advanced** > **Modalities** and verify the **Rewriter model** and **Summarization model** selections for both **Text** and **Voice** configurations.
  4. **Review retry and fallback settings** : 
     1. Open **Settings** for the agent application and go to **Basic** > **Behavior** > **Fallback behavior**.
     2. Verify that **Retries** , **Agent response** , and **Fallback** are configured appropriately for error handling during model generation.

**Note:** If you're migrating a voice agent from `gemini-composite-v1` to `gemini-composite-v2`, also review your speaking style prompt and convert square-bracket inline tags to angle brackets. For more information, see [Migrate from Composite V1](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#migrate-composite-v1).

### Update models using exported configuration files

If you manage your agent application through version control or CI/CD pipelines, you can update the model settings in the [exported archive](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/export) and re-import the package:

  1. Extract your exported agent application zip archive.
  2. For each agent directory under `agents/<var>AGENT_NAME</var>/`, open the `agents/<var>AGENT_NAME</var>/<var>AGENT_NAME</var>.yaml` file and update the `modelSettings.model` field to the target model ID:
         
         displayName: "AGENT_NAME"
         modelSettings:
           model: "MODEL_ID"
         instruction: "agents/AGENT_NAME/instruction.txt"
         

Replace the following:

     * `<var>AGENT_NAME</var>`: the display name of the agent.
     * `<var>MODEL_ID</var>`: the identifier of the target model, such as `gemini-3.5-flash` or `gemini-composite-v2`.
  3. Compress the root directory into a zip archive and [import](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export) the updated archive into CX Agent Studio.




### Update models using the REST API

You can programmatically update [`ModelSettings`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ModelSettings) on your agent application and on individual agents using the CX Agent Studio REST API.

Before calling the API, gather the following values:

  * `<var>PROJECT_ID</var>`: your Google Cloud project ID.
  * `<var>LOCATION_ID</var>`: the region of your agent application, such as `us` or `eu`.
  * `<var>APP_ID</var>`: the resource ID of your agent application.
  * `<var>AGENT_ID</var>`: the resource ID of a specific root agent or sub-agent.
  * `<var>MODEL_ID</var>`: the target model identifier, such as `gemini-3.5-flash`.



To update the default global model for the agent application, send a `PATCH` request to the [`projects.locations.apps.patch`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/patch) method with `updateMask=modelSettings`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID?updateMask=modelSettings" \
      -d '{
        "modelSettings": {
          "model": "MODEL_ID"
        }
      }'
    

To update the model override on an individual root agent or sub-agent, send a `PATCH` request to the [`projects.locations.apps.agents.patch`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.agents/patch) method with `updateMask=modelSettings`:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ces.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID/agents/AGENT_ID?updateMask=modelSettings" \
      -d '{
        "modelSettings": {
          "model": "MODEL_ID"
        }
      }'
    

## Step 3: Evaluate and refine agent performance

Foundation models can differ in reasoning style, instruction adherence, verbosity, and tool-calling behavior. After switching models, test your agent and refine its instructions before routing live customer traffic to the updated configuration.

### Test interactively in the simulator

Run initial sanity checks in the _Preview agent_ [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator):

  1. Open the simulator in the agent builder and click **Start new conversation**.
  2. Test representative text or audio interactions and verify that the agent follows instructions, invokes tools with valid arguments, and transitions between sub-agents as expected.
  3. Expand the trace details for each turn to inspect step latency, tool inputs and outputs, and raw JSON responses.
  4. Optional: To add a conversation to your regression suite, open the simulator menu and select **Save as golden**.



### Run evaluations and diagnose issues with AI

Use [evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation) to measure performance across your golden, scenario, and simulation test cases and compare results against your baseline version:

  1. Click **Evaluate** at the top of the agent builder.
  2. Select the test cases that cover your critical user journeys and agent variants, and then click **Run selected**.
  3. In the run dialog, select **Find issues with AI** , set the run count to 3 or more for optimal AI analysis, and then start the run. For more information, see [Use AI to improve test cases](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#find-issues-with-ai).
  4. When the run finishes, review the evaluation metrics—including [tool correctness](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#tool_correctness), [semantic match](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#semantic_match), [user goal satisfaction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#user_goal_satisfaction), [goal completion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#goal_completion), [hallucinations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#hallucinations), and [task completion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#task_completion)—and inspect any failed turns or uncompleted goals.
  5. On the results page, click **Ask Gemini** to review the generated `loss_report`, summarize root causes across failed runs, and view suggested instruction or configuration fixes.



### Hill-climb instructions with AI Co-Builder: Arc

If your evaluation results show regressions or behavior changes under the target model, use [AI Co-Builder: Arc](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/arc) and the evaluation helper to iteratively refine your prompts:

  1. Click **Arc** at the top of the agent builder to open the AI Co-Builder.
  2. Click **Select context** and select the specific agents or instructions that need adjustment, or attach failed transcripts and loss reports.
  3. Prompt Arc to update your [instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) or tool descriptions to address the observed failures while preserving behavior across other test cases. You can also use the [restructure instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction#restructure) feature to organize instructions into a structured format.
  4. Re-run your evaluation suite after applying fixes and repeat until all test cases meet your pass criteria. For additional guidance, see [Evaluations and hillclimbing best practices](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#evaluations_and_hillclimbing_best_practices).



## Step 4: Deploy in stages with traffic splitting

Once your updated agent passes evaluations, roll it out gradually using versions and deployment traffic splitting.

### Create a version for the migrated agent

Save an immutable snapshot of your validated configuration:

  1. If you tested changes in a separate sandbox application, [export](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/export) the validated application package and import it into your production application.
  2. In your production application, open the **Versions** pane and click **\+ Create version**.
  3. Enter a name and description that identify the target model, such as `v2-gemini-3-5-flash`, and then click **Create**.



### Gradually shift live traffic

Use [traffic splitting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split) to route a small percentage of live conversations to the migrated version before promoting it to 100% of traffic:

  1. Click the **Deploy** tab at the top of the agent builder and select your deployment channel.
  2. Under **Agent version** , click **Add version** and include both your baseline production version and your migrated candidate version.
  3. Assign a small initial **Traffic percentage** to the candidate version (for example, `90`% for the baseline version and `10`% for the candidate version, totaling 100%), and then save the channel configuration. You can also configure `experimentConfig.versionRelease.trafficAllocations` programmatically using the [REST API](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split#using_the_rest_api).
  4. Monitor live performance across versions: 
     * Check session volume, latency, and escalation rates on the [monitoring dashboard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/monitor).
     * Inspect live transcripts in [conversation history](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/conversation-history).
     * Query exported interaction logs by `app_version_id` in BigQuery to compare tool execution and outcome rates across versions. For example SQL queries, see [Analyze version performance in BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/traffic-split#analyze_version_performance_in_bigquery).
  5. As you confirm stability and quality, increase the traffic percentage for the migrated version in stages until it serves 100% of live traffic. If you detect unexpected issues during the rollout, route 100% of traffic back to the baseline version or [restore the previous version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version#restore_a_version) in the **Versions** pane.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
