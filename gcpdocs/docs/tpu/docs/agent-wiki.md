---
url: https://docs.cloud.google.com/tpu/docs/agent-wiki/
title: Troubleshoot with the ML Workload Debugging Wiki \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:36:55.328957+00:00
---

# Troubleshoot with the ML Workload Debugging Wiki  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/agent-wiki/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot with the ML Workload Debugging Wiki

The [ML Workload Debugging Wiki](https://github.com/google/ml-workload-debugging-wiki) is a GitHub repository that AI coding agents use to troubleshoot TPU workloads running on Google Kubernetes Engine (GKE) with [JAX](https://docs.jax.dev/en/latest/), [XLA](https://openxla.org/xla), or [Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro). The wiki enables AI agents to gather workload logs, match error signatures against known failure modes, run diagnostic workflows, and report root causes based on logs. This provides agents with the information necessary to diagnose workload crashes, hangs, restarts, or preemptions.

The wiki contains two forms of reference material:

  * **Knowledge pages** : Markdown pages that describe concepts, failure symptoms and their log signatures, troubleshooting playbooks, and diagnostic tools.
  * **Executable procedures** : JSON actions and workflows. An action is a single diagnostic step, such as a log query or a `kubectl` command. A workflow runs a sequence of actions to diagnose a specific failure mode.



When you run the `/troubleshoot` command, a team of specialized subagents triages the workload logs, selects and runs the workflow that matches the failure, and checks each conclusion against the primary logs. The agent then reports the root cause, the culprit hosts as quoted from the logs, and a failure table that summarizes each disruption.

## Key files

The following table lists the key files and directories within the Debug ML Workloads Wiki:

Path | Description  
---|---  
[`_wiki/TUTORIAL.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_wiki/TUTORIAL.md) |  A walkthrough of what happens during a diagnosis and how to evaluate the results, including a worked example.   
[`_wiki/INDEX.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_wiki/INDEX.md) |  A catalog of every page, action, and workflow in the wiki, with a one-line summary of each.   
[`_wiki/concepts/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/concepts) |  System architecture and component lifecycle concepts, such as the libtpu program lifecycle, goodput, and workload progress monitoring.   
[`_wiki/entities/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/entities) |  Hardware, software, and platform entities, such as TPU, GPU, JAX, XLA, and Pathways.   
[`_wiki/symptoms/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/symptoms) | Failure modes, their log signatures, and how to verify each one.  
[`_wiki/playbooks/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/playbooks) |  Troubleshooting strategies, decision-tree flowcharts, and common pitfalls.   
[`_wiki/tools/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/tools) | Diagnostic tools, scripts, and command-line reference guides.  
[`_wiki/workflows/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/workflows) |  Diagnostic procedures in JSON. Each workflow runs a sequence of actions to diagnose a specific failure mode.   
[`_wiki/actions/`](https://github.com/google/ml-workload-debugging-wiki/tree/main/_wiki/actions) |  Individual diagnostic steps in JSON, such as log queries and `kubectl` commands.   
[`_wiki/SCHEMA.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_wiki/SCHEMA.md) |  The page types, frontmatter requirements, and taxonomy tags that wiki pages must follow.   
[`_agents/QUICKSTART.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_agents/QUICKSTART.md) | Setup and dispatch details for Antigravity users.  
[`CLAUDE.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/CLAUDE.md) |  The workspace layout, command-line tools, and subagent roles, for Claude Code users.   
  
## Key commands

The following table lists the commands that you can run with the wiki:

Command | Usage | Description  
---|---|---  
`/troubleshoot` |  `/troubleshoot WORKLOAD_ID`, where `WORKLOAD_ID` is the name of the workload or JobSet.  |  Diagnoses a workload by using Cloud Logging, GKE cluster events, kubelet logs, and node logs. The router, practitioner, reviewer, and advisor subagents run the diagnosis and report the root cause, the culprit hosts as quoted from the logs, and a failure table.   
`/dashboard` |  `/dashboard [TARGET]`, where `TARGET` is an optional project ID, cluster name, or workload ID. If you omit `TARGET`, the dashboard shows all GKE clusters in the project that's set in your Google Cloud CLI configuration.  |  Starts the GKE Capacity & Triage Dashboard, a local web app at `http://localhost:8080`. The command scans the clusters for the target, and then returns a link to a dashboard view that's filtered to the target.   
`/handoff` |  `/handoff WORKLOAD_ID [CASE_ID] [--bucket=BUCKET] [--findings=PATH] [--no-watch]` All arguments except `WORKLOAD_ID` are optional: 

  * `CASE_ID`: your support case number.
  * `--bucket=BUCKET`: the name of the bucket. If you omit this flag, the agent asks for a bucket. 
  * `--findings=PATH`: the path to an existing findings file. If you set this flag, the command doesn't run `/troubleshoot`. 
  * `--no-watch`: turns off bucket monitoring.

|  Packages `/troubleshoot` findings into a Cloud Storage bucket to share with Cloud Customer Care, and then monitors the bucket for updates. To check for updates later, run `/handoff --watch STORAGE_KEY`, where `STORAGE_KEY` is the name of the handoff folder in the bucket.   
  
## Prerequisites

Before you set up the wiki, identify the workload that you want to diagnose, and note the following details:

  * The name of the workload or JobSet.
  * The ID of the Google Cloud project that runs the workload.
  * The approximate time range of the run to diagnose.



### Installations

The wiki requires the following installations:

  1. Install [Python 3](https://www.python.org/downloads/), including the `venv` module. The wiki requires Python 3.9 or newer. On Debian and Ubuntu, the `venv` module is in the `python3-venv` package.
  2. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
  3. Install [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl) and the `gke-gcloud-auth-plugin`.
  4. Install one of the following AI coding agents. The wiki includes configuration files for both: 
     * [Claude Code](https://code.claude.com/docs/en/overview)
     * [Google Antigravity](https://antigravity.google)



### Required roles

The agents run diagnostic commands with your Google Cloud credentials. To diagnose a workload, grant the following IAM roles to the project that runs the workload:

  * Logs Viewer (`roles/logging.viewer`): lets the agents read the workload container, node, and audit logs.
  * Kubernetes Engine Viewer (`roles/container.viewer`): lets the agents inspect the cluster, nodes, and pods that ran the workload.
  * Compute Viewer (`roles/compute.viewer`): lets the agents inspect the Compute Engine VMs that back the cluster nodes, including VM maintenance and termination events.
  * Monitoring Viewer (`roles/monitoring.viewer`): lets the agents read Cloud Monitoring metrics for workflows that inspect workload and node metrics.



To run the `/handoff` command, you also need the Storage Object Admin (`roles/storage.objectAdmin`) role on the Cloud Storage bucket that you share with Cloud Customer Care. This role lets the agents upload findings to the bucket and monitor it for updates.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set up the wiki

  1. Clone the repository and navigate to its root directory:
         
         git clone https://github.com/google/ml-workload-debugging-wiki.git
         cd ./ml-workload-debugging-wiki
         

The wiki uses paths that are relative to the repository root, so run the commands and start your agent from this directory.

  2. Create and activate a Python virtual environment and install the wiki's dependencies:
         
         python3 -m venv _wiki/.venv
         source _wiki/.venv/bin/activate
         pip install -r _wiki/requirements.txt
         

  3. Create local [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) for your user account. The wiki's Python tools use ADC to query Cloud Logging:
         
         gcloud auth application-default login
         

  4. Verify your setup by running the wiki linter:
         
         python3 _wiki/wiki_linter.py
         

The linter checks the wiki's structure, schemas, and links, and then prints a JSON report. If the report contains `"status": "PASS"`, the check succeeded. Warnings in the report don't affect the status.




## Troubleshoot a workload

Use the following steps to troubleshoot a workload with the ML Workload Debugging Wiki:

  1. Start your agent from the root of the ML Workload Debugging Wiki repository:

     * **Claude Code** : In the shell where you activated the virtual environment, run `claude`. Claude Code loads the wiki's instructions from `CLAUDE.md` and its command and subagent definitions from the `.claude/` directory.
     * **Antigravity** : Open the root of the repository as your workspace. The wiki's Antigravity skill and subagent definitions are in the `_agents/` directory. For setup details, see [`_agents/QUICKSTART.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_agents/QUICKSTART.md).
  2. Run the `/troubleshoot` command, specifying the name of the workload or JobSet that you want to diagnose:
         
         /troubleshoot WORKLOAD_ID
         

  3. Provide the agent the project ID and time range of the run. You can provide a precise time range in UTC timestamp format (`YYYY-MM-DDTHH:MM:SSZ`), or relative time ranges in natural language, such as "a hour ago" or "past 24 hours". The agents use the time range to scope their log queries, so make sure that it covers the entire run.




Diagnostic workflows run read-only checks by default. Before the agent runs an action that modifies cluster state, such as power cycling or tainting a node, it requests your explicit confirmation. Each command must be reviewed and approved. These actions are marked with `requires_approval: true` in their definitions in `_wiki/actions/`. The agent reports its findings after the diagnosis is complete.

To learn how to evaluate the findings, including how to recognize an inconclusive result, see [`_wiki/TUTORIAL.md`](https://github.com/google/ml-workload-debugging-wiki/blob/main/_wiki/TUTORIAL.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
