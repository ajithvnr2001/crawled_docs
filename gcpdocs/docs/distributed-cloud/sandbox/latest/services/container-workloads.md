---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/
title: Deploy container workloads \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T11:14:32.340897+00:00
---

# Deploy container workloads  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Preparation](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#preparation)
  * [Upload image to Harbor](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#upload-image)
  * [Deploy container app](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#deploy-container)
    * [Create a network policy](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#create_a_network_policy)
    * [Connect to the application](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#connect_to_the_application)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)


Send feedback 
#  Deploy container workloads Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Preparation](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#preparation)
  * [Upload image to Harbor](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#upload-image)
  * [Deploy container app](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#deploy-container)
    * [Create a network policy](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#create_a_network_policy)
    * [Connect to the application](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads/#connect_to_the_application)


This page describes the process of uploading a container image to Harbor, and deploying that image in your GDC Sandbox instance.
## Preparation
  1. Follow the instructions in [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect) to connect to your instance with Linux command line access. You can connect to your gateway over Remote Desktop, or run `sshuttle` on your Linux machine.
  2. Ask your Organization IAM Admin to grant you the following roles at the project level:
     * Secret Admin (`secret-admin`): required to create Kubernetes secrets and operate in the GDC console.
     * Namespace Admin (`namespace-admin`): required to deploy container workloads in your project.
     * Namespace Viewer (`namespace-viewer`): required to view project and namespace resources.
     * Project Viewer (`project-viewer`): required to access the GDC console and the Distributed Cloud CLI.
     * Harbor Instance Viewer (`harbor-instance-viewer`): required to view and select a Harbor instance.
     * Harbor Project Creator (`harbor-project-creator`): required to access and manage a Harbor project.
     * Project NetworkPolicy Admin (`project-networkpolicy-admin`): required to create and manage project network policies.
  3. Set environment variables that will be used in the following instructions:

```
export TENANT_PROJECT=TENANT_PROJECT # Intended deployment project for the container workflow.
export HARBOR_INSTANCE_NAME=HARBOR_INSTANCE_NAME # Harbor Container Registry instance name.
export HARBOR_PROJECT=HARBOR_PROJECT # Container registry project name for your images.
export AO_USER=AO_USER # Your user name in the instance, e.g.: fop-my-user@example.com.
export INSTANCE_URL=${HARBOR_INSTANCE_NAME}-${TENANT_PROJECT}.org-1.zone1.google.gdch.test.
export DOCKER_CONFIG_PATH=DOCKER_CONFIG_PATH # Path to docker config file e.g.: /root/.docker/config.json.

```

  4. To create a Harbor registry instance, follow [Create a Harbor registry instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/pa-ao-operations/create-harbor-instances#create-a-harbor-registry-instance), or you can use the pre-created Sandbox Harbor instance: the default `user-project` in GDC Sandbox comes with an already deployed Harbor Instance, `user-haas-instance`, which can be used for development.

```
export HARBOR_INSTANCE_NAME=user-haas-instance
export TENANT_PROJECT=user-project
export INSTANCE_URL=${HARBOR_INSTANCE_NAME}-${TENANT_PROJECT}.org-1.zone1.google.gdch.test

```



## Upload image to Harbor
  1. Create a Harbor project by following [Create a Harbor Project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/pa-ao-operations/create-harbor-projects#create-a-harbor-project).
Example:

```
gdcloud harbor harbor-projects create HARBOR_PROJECT  \
--project=TENANT_PROJECT \
--instance=HARBOR_INSTANCE_NAME

```

  2. Sign-in to Docker. Begin at [Sign in to Docker or Helm with CLI secrets](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/pa-ao-operations/configure-docker-authentication#sign-in-cli-secrets).
  3. Download or build your container image, and follow the Google Distributed Cloud air-gapped instructions to [Push an image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/pa-ao-operations/push-image) to push it to Harbor.
For example, here is is a workflow for pulling from Gitlab and pushing to Harbor:
    1. Sign in and pull from your Gitlab container registry.

```
export GITLAB_ID=GITLAB_ID
export GITLAB_PROJECT_NAME=GITLAB_PROJECT_NAME
export GITLAB_IMAGE_PATH=registry.gitlab.com/GITLAB_ID/GITLAB_PROJECT_NAME
docker login registry.gitlab.com
docker pull ${GITLAB_IMAGE_PATH}

```

    2. Push the Gitlab image to Harbor:

```
export TAG=demo-image
docker tag ${TAG} ${GITLAB_IMAGE_PATH}
docker push ${INSTANCE_URL}/${HARBOR_PROJECT}/${TAG}

```



## Deploy container app
Continue at [Create Kubernetes image pull secret](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform-application/deploy-container-workloads#create-image-pull-secret) to create a secret and deploy your app.
### Create a network policy
  1. Create a network policy to allow all network traffic to the tenant project:

```
kubectl --kubeconfig GLOBAL_API_KUBECONFIG -n TENANT_PROJECT \
create -f - <<EOF
apiVersion: networking.gdc.goog/v1
kind: ProjectNetworkPolicy
metadata:
  annotations:
  name: allow-all
spec:
  ingress:
  - from:
    - ipBlock:
        cidr: 0.0.0.0/0
  podSelector: {}
  policyTypes:
  - Ingress
EOF

```



### Connect to the application
  1. Export the IP address for the service:

```
export IP=`kubectl --kubeconfig=${KUBECONFIG} get service ${SERVICE_NAME} \
      -n TENANT_PROJECT -o jsonpath='{.status.loadBalancer.ingress[*].ip}'`

```

  2. To connect from your local machine using `sshuttle`, run the following command to create an SSH tunnel. If you have an existing `sshuttle` session that you created when you connected to your instance, you must terminate that session before running the following command:

```
  sshuttle -r zone1-org-1-data@GDC_SANDBOX_INSTANCE_NAME --no-latency-control \
  --ssh-cmd 'gcloud compute ssh --project PROJECT_NAME --zone ZONE --tunnel-through-iap' \
  10.200.0.0/16 --dns

```

  3. Test the service by sending a HTTP request http://${IP}`:

```
  curl http://${IP}

```



Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
