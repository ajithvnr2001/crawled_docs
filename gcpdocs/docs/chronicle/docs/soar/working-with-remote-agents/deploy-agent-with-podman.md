---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman/
title: Create an agent using Podman \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T23:33:33.626339+00:00
---

# Create an agent using Podman  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-podman/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an agent using Podman 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the procedure to deploy a Remote Agent using Podman. Before you begin, verify that your host meets the operating system and outbound firewall prerequisites, including access to container registries and Google Security Operations endpoints, in [Review deployment requirements](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites).

  1. Navigate to **Settings > Administration > SOAR Remote Agents**. 
  2. Click  add  **Add Agent** to start the installation process. 
  3. Select the **Podman** option.
  4. In the first step, name the agent and choose the environment where it will be installed.
  5. Follow the remaining steps in the platform wizard, including running the generated Podman command on your local machine. 
  6. After the deployment finishes, click **Next** to run a connectivity check with your new agent. A success notification will confirm the connection. If the check fails, a failure notification will display with helpful troubleshooting links. 
  7. Click **Done**. The remote agent is now added to the platform.  


**Note:** Remote agent containers do not restart by default after a host reboot. To automatically start the remote agent container after a reboot, consider configuring the container to run as a `systemd` service using [Quadlets or `podman generate systemd`](https://docs.podman.io/en/latest/markdown/podman-generate-systemd.1.html).  **Note:** You can't make any changes to the Podman image. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 
