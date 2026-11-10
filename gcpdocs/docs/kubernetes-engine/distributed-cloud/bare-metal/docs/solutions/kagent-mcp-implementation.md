---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-implementation/
title: Bring your own MCP server to kagent reference implementation \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:50:19.657996+00:00
---

# Bring your own MCP server to kagent reference implementation  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Bring your own MCP server to kagent reference implementation Stay organized with collections  Save and categorize content based on your preferences. 

## Introduction

Bring your own (BYO) Model Context Protocol (MCP) servers let AI agents query and process data from external repositories in real time by using standardized connections across your existing infrastructure.

This solution reference implementation (SRI) document shows you how to deploy the [Nextcloud](https://nextcloud.com/) open source application and its MCP server alongside a Nextcloud agent on [Solo Enterprise for kagent](https://www.solo.io/products/kagent-enterprise). This architecture connects Nextcloud, kagent, and the Gemma 4 model within a Google Kubernetes Engine (GKE) cluster deployed in Google Distributed Cloud software only (GDC). In this configuration, kagent uses Nextcloud as a data repository, letting the Gemma 4 model access and process files in Nextcloud through standardized MCP interfaces. For architectural context, see the companion [reference architecture](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-architecture).

### Overview of Nextcloud

Nextcloud is an open source, self-hosted collaboration and cloud storage platform that supports on-premises deployment. Deploying Nextcloud on-premises helps maintain sovereignty, security, and privacy over your data.

Nextcloud provides the following features:

  * **File sync and share:** Store files, sync them across your desktop and mobile devices through dedicated apps, and share them with others by using links.
  * **Productivity tools:** Manage schedules and communication with built-in calendar, contacts, task management, and email clients.
  * **Collaboration:** Integrate office suites (such as Collabora Online or ONLYOFFICE) directly into Nextcloud to co-edit documents, spreadsheets, and presentations in real time.
  * **Extensibility:** Install plugins from the app store to add features such as password managers, Kanban boards, or music players.



### Solution architecture

This solution requires a GDC environment with [Solo Enterprise for kagent](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-deployment-implementation) and [vLLM with the Gemma 4 model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only-implementation) deployed, and a workstation with `kubectl` and `helm` installed.

The following diagram illustrates the solution architecture connecting GDC, kagent, Nextcloud, and vLLM with Gemma 4:

![Solution architecture: GDC, kagent, Nextcloud, and vLLM with Gemma 4.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/byo-mcp-server-kagent-diagram.png)

### Deployment approach

To deploy Nextcloud and integrate its MCP server with kagent, complete the following high-level steps:

  1. **Create a dedicated namespace for Nextcloud:** Isolate the deployment by creating the `nextcloud` namespace using `kubectl`.
  2. **Add and update the Helm repository:** Configure your workstation with the official Nextcloud Helm repository and update your local chart metadata.
  3. **Configure custom deployment values:** Create a custom `values.yaml` file to configure Nextcloud for your target environment. This configuration disables the default local SQLite database, configures MariaDB persistent storage, defines administrator credentials, and sets internal routing using a `ClusterIP` service.
  4. **Run the Helm installation:** Deploy the chart into the target namespace using your custom configuration file. Verify that all components, including the Nextcloud application and MariaDB storage Pods, reach the `Running` status.
  5. **Deploy the Nextcloud MCP server:** Create a deployment manifest (`nextcloud-mcp.yaml`) containing an opaque Secret for credentials, a Deployment using the `nextcloud-mcp-server:latest` image, and a `ClusterIP` Service exposing port `8000`. Apply this manifest to allow internal Kubernetes DNS communication with the Nextcloud application.
  6. **Register the tool server on kagent:** Connect the server in the kagent UI by using the internal service URL `http://nextcloud-mcp-service.nextcloud.svc.cluster.local:8000/mcp` and the `STREAMABLE_HTTP` protocol.



### Deploy Nextcloud and the MCP server

  1. Create a namespace for Nextcloud:
         
         kubectl create namespace nextcloud
         

The output is similar to the following:
         
         namespace/nextcloud created
         

  2. Add the Nextcloud Helm repository to your workstation and update your local chart metadata:
         
         helm repo add nextcloud https://nextcloud.github.io/helm/
         helm repo update
         

The output is similar to the following:
         
         "nextcloud" has been added to your repositories
         Hang tight while we grab the latest from your chart repositories...
         ...Successfully got an update from the "nextcloud" chart repository
         Update Complete. ⎈Happy Helming!⎈
         

  3. Create a custom `values.yaml` file on your workstation to override the default configuration parameters of the Nextcloud Helm chart:
         
         # 0. Nextcloud administrator configuration
         nextcloud:
           # Use the internal CoreDNS record
           host: "nextcloud.nextcloud.svc.cluster.local"  # Application access through CoreDNS rather than external DNS
           username: "admin"  # Application Login Credentials
           password: "SuperSecretPassword123"
         
         # You can use a standard ClusterIP service since
         # you are relying on internal routing, not an External LB.
         service:
           type: ClusterIP
         
         # 1. Configure RWO Storage for Nextcloud
         persistence:
           enabled: true
           storageClass: "local-shared"
           accessMode: ReadWriteOnce
           size: 50Gi # Adjust based on your file storage needs
         
         # 2. Explicitly disable the default local SQLite database
         internalDatabase:
           enabled: false
         
         # 3. Configure RWO Storage for the Database
         mariadb:
           enabled: true
           auth:
             database: "nextcloud"
             username: "nextcloud"
             password: "NextcloudDBPassword123"
             rootPassword: "RootDBPassword123"
           primary:
             persistence:
               enabled: true
               storageClass: "local-shared"
               accessModes:
                 - ReadWriteOnce
               size: 10Gi
         
         # 4. Force Nextcloud to connect through the TCP Network
         externalDatabase:
           enabled: true
           type: mysql
           host: "nextcloud-mariadb" # The internal Kubernetes service name for the DB
           database: "nextcloud"
           user: "nextcloud"
           password: "NextcloudDBPassword123" # MUST match mariadb.auth.password above
         
         # Optional: Enable Ingress to route external traffic to Nextcloud
         ingress:
           enabled: false # Set to true if you are using an Ingress Controller (like NGINX)
           className: "nginx"
           annotations:
             nginx.ingress.kubernetes.io/proxy-body-size: 4G # Required to allow large file uploads
         

  4. Deploy Nextcloud by using Helm:
         
         helm install nextcloud nextcloud/nextcloud \
             --namespace nextcloud \
             --values values.yaml
         

The output is similar to the following:
         
         NAME: nextcloud
         LAST DEPLOYED: Thu Jul  9 17:14:03 2026
         NAMESPACE: nextcloud
         STATUS: deployed
         REVISION: 1
         TEST SUITE: None
         NOTES:
         1. Get the nextcloud URL by running:
         
           export POD_NAME=$(kubectl get pods --namespace nextcloud -l "app.kubernetes.io/name=nextcloud" -o jsonpath="{.items[0].metadata.name}")
           echo http://127.0.0.1:8080/
           kubectl port-forward --namespace nextcloud $POD_NAME 8080:80
         
         2. Get your nextcloud login credentials by running:
         
           echo User:     admin
           echo Password: $(kubectl get secret --namespace nextcloud nextcloud -o jsonpath="{.data.nextcloud-password}" | base64 --decode)
         

Verify that the Nextcloud Pods are in the `Running` status and that the Services exist in the `nextcloud` namespace:
         
         kubectl get pod -n nextcloud
         kubectl get svc -n nextcloud
         

The output is similar to the following:
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         nextcloud-558cbccb4c-q6zqq              1/1     Running   0          25m
         nextcloud-mariadb-0                     1/1     Running   0          25m
         
         NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         nextcloud                    ClusterIP   10.255.224.187   <none>        8080/TCP   25m
         nextcloud-mariadb            ClusterIP   10.255.226.235   <none>        3306/TCP   25m
         nextcloud-mariadb-headless   ClusterIP   None             <none>        3306/TCP   25m
         

  5. To deploy the Nextcloud MCP server in the `nextcloud` namespace, create a file named `nextcloud-mcp.yaml` on your workstation:
         
         # Secret Creation
         apiVersion: v1
         kind: Secret
         metadata:
           name: nextcloud-mcp-secret
           namespace: nextcloud
         type: Opaque
         stringData:
           # Use your dedicated App Password here, NEVER your primary administrator password
           NEXTCLOUD_USERNAME: "admin"
           NEXTCLOUD_PASSWORD: "SuperSecretPassword123"
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nextcloud-mcp-server
           namespace: nextcloud
           labels:
             app: nextcloud-mcp
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: nextcloud-mcp
           template:
             metadata:
               labels:
                 app: nextcloud-mcp
             spec:
               containers:
                 - name: mcp-server
                   # The official Docker image provided by the project
                   image: ghcr.io/cbcoutinho/nextcloud-mcp-server:latest
                   imagePullPolicy: Always
                   ports:
                     - containerPort: 8000
                       name: http-mcp
                   env:
                     - name: NEXTCLOUD_HOST
                       # Since the MCP server is in the same namespace, it can securely
                       # talk to Nextcloud through the internal Kubernetes DNS, completely bypassing the internet.
                       value: "http://nextcloud.nextcloud.svc.cluster.local:8080"
                     - name: NEXTCLOUD_USERNAME
                       valueFrom:
                         secretKeyRef:
                           name: nextcloud-mcp-secret
                           key: NEXTCLOUD_USERNAME
                     - name: NEXTCLOUD_PASSWORD
                       valueFrom:
                         secretKeyRef:
                           name: nextcloud-mcp-secret
                           key: NEXTCLOUD_PASSWORD
                   resources:
                     requests:
                       cpu: "100m"
                       memory: "128Mi"
                     limits:
                       cpu: "500m"
                       memory: "512Mi"
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: nextcloud-mcp-service
           namespace: nextcloud
         spec:
           type: ClusterIP
           ports:
             - port: 8000
               targetPort: 8000
               protocol: TCP
               name: http-mcp
           selector:
             app: nextcloud-mcp
         

Apply the `nextcloud-mcp.yaml` manifest:
         
         kubectl apply -f nextcloud-mcp.yaml
         

The output is similar to the following:
         
         secret/nextcloud-mcp-secret created
         deployment.apps/nextcloud-mcp-server created
         service/nextcloud-mcp-service created
         

Verify that the Pods and Services are running in the `nextcloud` namespace:
         
         kubectl get svc -n nextcloud
         kubectl get pod -n nextcloud
         

The output is similar to the following:
         
         NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         nextcloud                    ClusterIP   10.255.224.187   <none>        8080/TCP   26m
         nextcloud-mariadb            ClusterIP   10.255.226.235   <none>        3306/TCP   26m
         nextcloud-mariadb-headless   ClusterIP   None             <none>        3306/TCP   26m
         nextcloud-mcp-service        ClusterIP   10.255.226.105   <none>        8000/TCP   55s
         
         NAME                                    READY   STATUS    RESTARTS   AGE
         nextcloud-558cbccb4c-q6zqq              1/1     Running   0          29m
         nextcloud-mariadb-0                     1/1     Running   0          29m
         nextcloud-mcp-server-58484d5799-mfvct   1/1     Running   0          4m11s
         

  6. To integrate the Nextcloud MCP tools by URL, go to the kagent UI and register a tool server with the following values:

     * **URL** : `http://nextcloud-mcp-service.nextcloud.svc.cluster.local:8000/mcp`
     * **Protocol** : `STREAMABLE_HTTP`
     * **Namespace** : `kagent`
     * **Cluster** : your cluster name (for example, `mgmt-cluster`)

Verify that the `RemoteMCPServer` resource is accepted in the `kagent` namespace:
    
    kubectl get remotemcpserver -n kagent
    

The output is similar to the following:
    
    NAME                 PROTOCOL          URL                                                                 ACCEPTED
    kagent-grafana-mcp   STREAMABLE_HTTP   http://kagent-grafana-mcp.kagent:8000/mcp                           True
    kagent-tool-server   STREAMABLE_HTTP   http://kagent-tools.kagent:8084/mcp                                 True
    nextcloud            STREAMABLE_HTTP   http://nextcloud-mcp-service.nextcloud.svc.cluster.local:8000/mcp   True
    

  7. To access Nextcloud from your workstation, forward local port `8080` to the `nextcloud` service (skip this step if you configured an external URL):
         
         kubectl port-forward -n nextcloud svc/nextcloud 8080:8080 &
         

The output is similar to the following:
         
         Forwarding from 127.0.0.1:8080 -> 80
         Forwarding from [::1]:8080 -> 80
         




### Verify the deployment and configure the Nextcloud agent

From your workstation browser, open `http://localhost:8080` to view the Nextcloud dashboard:

![Nextcloud application dashboard page.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-nextcloud-dashboard.png)

The **Files** view displays the directories and files stored in Nextcloud:

![Directory and Files interface within the Nextcloud application.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-nextcloud-directory-files.png)

In the kagent UI, the **Dashboard** page displays connected clusters and deployed agents:

![kagent application dashboard.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-dashboard.png)

The **Tool Servers** page lists the tools discovered through MCP for the Nextcloud application:

![kagent Tool Servers page showing tools discovered for the Nextcloud application.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-tool-server.png)

The **Tools** page displays the collection of Nextcloud tools available to agents:

![kagent Tools collection available in Nextcloud.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-tools.png)

To create the `nextcloud` agent in the kagent UI, enter the agent name, cluster, namespace, and description under **Basic Information** :

![kagent agent creation for Nextcloud.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-agent-creation.png)

Under **Behavior & Model Settings**, select the Gemma 4 model and enter the system instructions for the agent:

![kagent agent configuration for skill and model alignment.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-skill-model-alignment.png)

Under **Tools and Agents** , select the Nextcloud MCP tools for the agent, and then click **Create Agent** :

![kagent agent configuration for Nextcloud tool selection.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-tool-selection.png)

The **Agents** page displays the `nextcloud` agent with a `Ready` status:

![Agents added to the kagent application.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-kagent-agents-list.png)

You can prompt the Nextcloud agent to list directories and files in the Nextcloud application:

![Nextcloud agent listing directories and files.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-nextcloud-agent-list-files.png)

You can also prompt the Nextcloud agent to translate and transliterate file contents from English to French:

![Nextcloud agent translating file contents from English to French.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-gdc-so-nextcloud-agent-translate.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
