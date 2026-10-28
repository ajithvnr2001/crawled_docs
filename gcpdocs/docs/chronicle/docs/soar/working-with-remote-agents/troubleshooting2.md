---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/
title: Troubleshoot remote agents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:10:15.509682+00:00
---

# Troubleshoot remote agents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/

[ Skip to main content ](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/)
  * [Deutsch](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=es-419)
  * [Français](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=id)
  * [Italiano](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=ja)
  * [한국어](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/secops-color.svg) ](https://docs.cloud.google.com/chronicle/docs)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Key mismatch issue](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#key-mismatch-issue)
  * [Remote connector failure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#remote-connector-failure)
  * [Docker agent deployment failure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#docker-agent-deployment-failure)
  * [Agent stuck in 'Waiting for agent' status](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#agent-stuck-in-waiting-for-agent-status)
  * [Docker image fails to load (IP4 forwarding is disabled)](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#docker-image-fails-to-load-ip4-forwarding-is-disabled)
  * [Error after shutdown or reboot of Agent](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#error-after-shutdown-or-reboot-of-agent)
  * [Unsuccessful remote agent upgrade](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#unsuccessful-remote-agent-upgrade)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)


Was this helpful?
Send feedback 
  * On this page
  * [Key mismatch issue](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#key-mismatch-issue)
  * [Remote connector failure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#remote-connector-failure)
  * [Docker agent deployment failure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#docker-agent-deployment-failure)
  * [Agent stuck in 'Waiting for agent' status](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#agent-stuck-in-waiting-for-agent-status)
  * [Docker image fails to load (IP4 forwarding is disabled)](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#docker-image-fails-to-load-ip4-forwarding-is-disabled)
  * [Error after shutdown or reboot of Agent](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#error-after-shutdown-or-reboot-of-agent)
  * [Unsuccessful remote agent upgrade](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2/#unsuccessful-remote-agent-upgrade)


# Troubleshoot remote agents Stay organized with collections  Save and categorize content based on your preferences.
Supported in:
Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)
This document provides a collection of tips and procedures to help you diagnose and resolve common issues encountered during the deployment and operation of the Google Security Operations Remote Agent.
## Key mismatch issue
This issue occurs when the private keys in Google Security Operations and the Remote Agent don't match. To solve this, make sure the key in the agent resources matches the key in the Siemplify `agent_db`.
## Remote connector failure
If a remote connector fails, follow these steps:
  1. Verify that an integrations instance is successfully installed on the agent.
  2. Check the agent logs at the error level to find any failures in the connection process.
  3. Test the same connector configuration locally and see if there are errors.


## Docker agent deployment failure
If the Docker deployment fails, follow these steps:
  1. Remove the Docker container: 
    1. Run the following command to list the running containers:
`docker ps `
    2. Run the following command to remove the failed containers:
`docker rm  -f container_id_or_name`
  2. Remove images: 
    1. Run the following command to list the images:
`docker images `
    2. Run the following command to remove the image:
`docker rmi image_id_or_name`
  3. Remove volumes: 
    1. Run the following command to list the volumes:
`docker volume ls`
    2. Run the following command to remove the volumes:
`docker volume rm volume_name`
  4. Redeploy the agent. For more information, see [Create an agent using Docker](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker).


## Agent stuck in 'Waiting for agent' status
If the agent was successfully deployed but the status remains "waiting for agent", follow these steps to troubleshoot the issue:
  1. **Check host connectivity** : Test the Agent host machine's internet connectivity (for example, `curl www.google.com` or `ping 8.8.8.8`). If this fails, the issue is with the host's internet connection.
  2. **Check container connectivity** : If the host test passes, enter the container shell using `docker exec -it container_ID bash` and recheck connectivity. If the container lacks connectivity, restart the Docker service on the host machine (service docker restart).
    1. Run the following command:
`docker exec -it  bash`
    2. Check the connectivity again as you did previously. 
    3. If there is no connectivity, run the following command to restart the Docker service from the host machine (not the container): 
`service docker restart`
    4. Run the following command to start container again:
`docker start`
  3. Review container logs for errors
If the previous step did not help, and the agent status is still 'waiting for agent' after refreshing the **Remote agent** page in Google SecOps, log back in the container and pull the logs.
    1. Find the logs in the `/var/log/SiemplifyAgent/` directory.
    2. Look for any errors in the log files to identify the root cause.


## Docker image fails to load (IP4 forwarding is disabled)
If you see an error in the CLI when you try to load a Google SecOps Docker image (system) or agent, IP4 forwarding might be disabled. Follow these steps to enable it and restart your agent:
  1. Add the following line to the `/etc/sysctl.conf` file:
`net.ipv4.ip_forward=1` Note that you will need to use a file editor (like nano for example use: `yum install nano -y`  

  2. Run the following command to restart network service:
`systemctl restart network`
  3. Run the following command to restart the Docker service:
`sudo systemctl restart docker`
  4. Run the following command to check if the container is running:
`docker ps`
  5. If the container is not running, run the following command to list all containers (including stopped ones):
`docker ps -a`
  6. If the container is listed but stopped, run the following command to start it:
`docker start container_id_or_name`
  7. If the agent or system is still not running after restarting Docker and the container: 
    1. Run the following command to stop the container:
`docker stop container_id_or_name`
    2. Run the following command to delete the container:
`docker rm container_id_or_name`
    3. Run the following command to delete the image:
`docker rmi image_name`
    4. Load the image again.


## Error after shutdown or reboot of Agent
Run the following command to force start of Installer agent:   
`systemctl start supervisord`
Run the following command to force start of the Docker agent:  
`docker start `
## Unsuccessful remote agent upgrade
If a prior upgrade was initiated but did not complete successfully and the Remote Agent version did not change, wait 15 minutes and refresh the **Remote agent** page in Google Security Operations. You can then re-initiate the upgrade.
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
