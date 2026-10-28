---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/
title: Perform a major upgrade of a Podman image \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:10:46.085217+00:00
---

# Perform a major upgrade of a Podman image  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/

[ Skip to main content ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/)
  * [Deutsch](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=de)
  * [Español](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=es-419)
  * [Français](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=id)
  * [Italiano](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=it)
  * [Português](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=ja)
  * [한국어](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fchronicle%2Fdocs%2Fsoar%2Fworking-with-remote-agents%2Fupgrade-agent-podman-image%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/secops-color.svg) ](https://docs.cloud.google.com/chronicle/docs)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)


Was this helpful?
Send feedback 
# Perform a major upgrade of a Podman image  Stay organized with collections  Save and categorize content based on your preferences.
Supported in:
Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)
This document explains how to perform a major upgrade for an existing remote agent using the Podman image. The procedure assumes you're viewing the **Major Upgrade** dialog in the Google Security Operations SOAR platform. 
  1. On the **Major Upgrade** dialog, copy the provided Podman run command: 
```
PODMAN_COMMAND
```

  2. List the current running Podman containers: 
```
podman ps
```

  3. Enter your agent's container ID: 
```
CONTAINER_ID
```

  4. Enter your agent's container name: 
```
AGENT_NAME
```
. 
  5. Pull the latest Podman image to your machine using the following command. You can replace the `:latest` tag with a specific version, such as `1.4.8.3`. 
```
podman pull us-docker.pkg.dev/siem-ar-public/images/agent:latest
```

  6. Copy the original environment variables (`.bash_profile`) to a local temporary file. 
```
podman exec CONTAINER_ID cat /home/siemplify_agent/.bash_profile > temp_bash_profile.txt
```

  7. Stop the agent's Podman container. 
```
podman stop CONTAINER_ID
```

  8. Rename the container for backup. 
```
podman rename AGENT_NAME AGENT_NAME_backup
```

  9. Run the new agent image. If you changed the `latest` tag, make sure the image tag matches the one pulled in. 
```
PODMAN
```

  10. List the running Podman containers. 
```
podman ps
```

  11. Enter your agent's new container ID: 
```
NEW_CONTAINER_ID
```

  12. Copy the environment variables `.bash_profile` from the temporary file to the new container. 
```
cat temp_bash_profile.txt | podman exec -i 
    NEW_CONTAINER_ID sh -c 'cat > /home/siemplify_agent/.bash_profile'
```

  13. Restart the agent service to apply the modified environment variables. 
```
podman exec NEW_CONTAINER_ID supervisorctl restart all
```



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
