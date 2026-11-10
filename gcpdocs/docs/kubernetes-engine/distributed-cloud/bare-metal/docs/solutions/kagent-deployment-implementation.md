---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-deployment-implementation/
title: Deploy Solo Enterprise for kagent on Google Distributed Cloud software only reference implementation \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T05:50:23.964611+00:00
---

# Deploy Solo Enterprise for kagent on Google Distributed Cloud software only reference implementation  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-deployment-implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Deploy Solo Enterprise for kagent on Google Distributed Cloud software only reference implementation Stay organized with collections  Save and categorize content based on your preferences. 

Solo Enterprise for kagent lets platform administrators deploy and manage AI agents on Google Distributed Cloud (GDC) software only (GDC-SO). In this reference implementation, you mirror container images and Helm charts to a private Harbor registry, deploy the kagent control plane, UI, and Solo Enterprise for agentgateway, and review cluster sizing guidelines. For more information about the architecture, see [Bring your own MCP server to kagent reference architecture](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/kagent-mcp-architecture).

## Prerequisites

Before you begin, make sure that you have access to a Linux workstation with Chrome, Docker, `crane`, `kubectl`, Helm, `envsubst`, and the `gdcloud` CLI. Make sure that the following components are configured for your GDC-SO environment:

Component | Detail or requirement | Example value  
---|---|---  
Google Cloud project for GDC-SO | Project associated with the GDC-SO cluster | `kagent-enterprise`  
Cluster | Target GDC-SO cluster | `user-project-8a210897`  
Kubernetes credentials (Connect Gateway) | Connection to the cluster | `gcloud container fleet memberships get-credentials user-project-8a210897`  
Private registry | Harbor registry URL | `solo-kagent-enterprise.org-1.zone1.google.gdch.test`  
Project repository | Project repository path | `solo-kagent-enterprise.org-1.zone1.google.gdch.test/kagent-enterprise`  
Pull secret | Docker pull secret name | `solo-harbor-pull-secret`  
  
The following instructions apply to Solo Enterprise for kagent version 0.4.0 and later.

This deployment was validated on GDC-SO version `1.31.5-gke.300`.

## Deploy on a GDC-SO cluster

Create a `.env` file based on your cluster and registry configuration:
    
    
    export PUBLIC_REGISTRY="us-docker.pkg.dev/solo-public/kagent-enterprise-helm/charts"
    export PUBLIC_MANAGEMENT_REGISTRY="us-docker.pkg.dev/solo-public/solo-enterprise-helm/charts"
    export PUBLIC_AGENTGATEWAY_REGISTRY="us-docker.pkg.dev/solo-public/enterprise-agentgateway/charts"
    
    # Set these based on your desired installation version
    export KAGENT_ENT_VERSION=0.4.1
    export KAGENT_VERSION=0.9.1
    export AGENTGATEWAY_VERSION=v2.4.0-beta.0
    export SOLO_LICENSE_KEY="SOLO_LICENSE_KEY"
    
    # Set the following values based on your GDC setup
    export PROJECT_ID="kagent-enterprise"
    export CLUSTER_NAME="user-project-8a210897"
    export NAMESPACE="solo-kagent"
    export USER_CONTEXT="user-vm-1-zone1-gdch_console-org-1-zone1-google-gdch-test_user-vm-1"
    export MGMT_CONTEXT="user-project-8a210897-zone1-gdch_console-org-1-zone1-google-gdch-test_user-project-8a210897"
    export PULL_SECRET_NAME="solo-harbor-pull-secret"
    
    # Set the following values based on your Harbor registry setup
    export ORG="ORG"
    export ZONE="ZONE"
    export PRIVATE_REGISTRY="solo-kagent-enterprise.${ORG}.${ZONE}.google.gdch.test"
    export PRIVATE_REPO="${PRIVATE_REGISTRY}/${PROJECT_ID}"
    export PRIVATE_CHART_REGISTRY="${PRIVATE_REPO}/charts"
    

Replace the following:

  * `SOLO_LICENSE_KEY`: your Solo Enterprise license key
  * `ORG`: your GDC organization name
  * `ZONE`: your GDC zone name



### Create the Helm values files

Create the Helm values files for the three charts. You don't need to modify any values unless you want to customize the installation. You can configure additional models and agents later in the kagent UI.

Create the `enterprise-agentgateway-values.yaml` file:
    
    
    image:
      registry: ${PRIVATE_REPO}/enterprise-agentgateway
      tag: ${AGENTGATEWAY_VERSION}
    licensing:
      licenseKey: ${SOLO_LICENSE_KEY}
    imagePullSecrets:
    - name: ${PULL_SECRET_NAME}
    inferenceExtension:
      enabled: true
    

Create the `kagent-enterprise-values.yaml` file:
    
    
    registry: ${PRIVATE_REPO}
    cluster: ${CLUSTER_NAME}
    imagePullSecrets:
    - name: ${PULL_SECRET_NAME}
    global:
      imagePullSecrets:
      - name: ${PULL_SECRET_NAME}
    oidc:
      skipOBO: true
    otel:
      tracing:
        enabled: true
        exporter:
          otlp:
            endpoint: http://solo-enterprise-telemetry-collector.${NAMESPACE}.svc.cluster.local.:4317
            insecure: true
    kubernetes:
      jwksUrl: "https://kubernetes.default.svc.cluster.local/openid/v1/jwks"
    providers:
      default: OpenAI # Choose the model API type
      OpenAI:
        provider: OpenAI
        model: "/model/gemma-4-12B" # Choose the model
        apiKeySecretRef: "kagent-openai"
        apiKeySecretKey: "none" # Name of the key in the Secret, or "none" if no API key is required
    controller:
      agentDeployment:
        podLabels:
          egress.networking.gke.io/enabled: "true"
      imagePullSecrets:
      - name: ${PULL_SECRET_NAME}
      image:
        registry: ${PRIVATE_REPO}
      agentImage:
        registry: ${PRIVATE_REPO}
        repository: "kagent-dev/kagent/app"
        pullSecret: "${PULL_SECRET_NAME}"
    licensing:
      createSecret: true
      secretName: "enterprise-kagent-license"
    kmcp:
      imagePullSecrets:
      - name: ${PULL_SECRET_NAME}
      image:
        registry: ${PRIVATE_REPO}
      enabled: true
    kagent-tools:
      enabled: true
      imagePullSecrets:
      - name: ${PULL_SECRET_NAME}
      tools:
        image:
          registry: ${PRIVATE_REPO}
    agents:
      k8s-agent:
        enabled: true
    grafana-mcp:
      enabled: false # Pull secret is not supported
    tools:
      grafana-mcp:
        enabled: false # Pull secret is not supported
    database:
      postgres:
        bundled:
          storageClassName: local-shared
          image:
            registry: ${PRIVATE_REPO}
          enabled: true
    

Create the `management-values.yaml` file:
    
    
    cluster: ${CLUSTER_NAME}
    context: "${USER_CONTEXT}"
    
    management-crds:
      enabled: false
    
    global:
      imagePullPolicy: IfNotPresent
      imagePullSecrets:
      - name: ${PULL_SECRET_NAME}
    
    products:
      kagent:
        enabled: true
      agentgateway:
        enabled: true
      mesh:
        enabled: false
      agentregistry:
        enabled: false
    
    oidc:
      issuer: ""
    
    traces:
      verbose: false
    
    tunnelserver:
      registry: ${PRIVATE_REPO}
      repository: solo-enterprise
      name: solo-enterprise-tunnel-server
    
    ui:
      backend:
        registry: ${PRIVATE_REPO}
        repository: solo-enterprise
        name: solo-enterprise-ui-backend
        clickhouse:
          migrations:
            registry: ${PRIVATE_REPO}
      frontend:
        registry: ${PRIVATE_REPO}
        repository: solo-enterprise
      telemetryGateway:
        repository: ${PRIVATE_REPO}/otel/opentelemetry-collector-contrib
    
    idp:
      registry: ${PRIVATE_REPO}
      repository: solo-enterprise
    
    telemetry:
      image:
        registry: ${PRIVATE_REPO}
        repository: otel
        name: opentelemetry-collector-contrib
      k8sobjects:
        enabled: true
      metrics:
        enabled: false
      selfMonitoring:
        enabled: false
        verbose: false
      traces:
        enabled: true
    
    clickhouse:
      enabled: true
      image:
        repository: ${PRIVATE_REPO}/clickhouse/clickhouse-server
    

### Set up the environment

In the same directory as your `.env` and Helm values files, load the environment variables and render the Helm values templates. Run the remaining commands in this guide in the same shell session so that these variables remain set:

**Note:** The `COMMON_FLAGS` variable includes `--insecure-skip-tls-verify` for environments that use self-signed certificates. In production environments, configure your workstation to trust the cluster certificate authority (CA) and remove `--insecure-skip-tls-verify`.
    
    
    SCRIPT_DIR="${PWD}"
    
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
    
    COMMON_FLAGS=(--kube-context "$MGMT_CONTEXT" -n "$NAMESPACE" --create-namespace --insecure-skip-tls-verify)
    
    # Values files live alongside the script. Render them with envsubst into
    # *.generated.yaml siblings that are then fed to helm upgrade.
    
    MANAGEMENT_VALUES_GENERATED="$SCRIPT_DIR/management-values.generated.yaml"
    KAGENT_ENTERPRISE_VALUES_GENERATED="$SCRIPT_DIR/kagent-enterprise-values.generated.yaml"
    ENTERPRISE_AGENTGATEWAY_VALUES_GENERATED="$SCRIPT_DIR/enterprise-agentgateway-values.generated.yaml"
    
    envsubst < "$SCRIPT_DIR/management-values.yaml"            > "$MANAGEMENT_VALUES_GENERATED"
    envsubst < "$SCRIPT_DIR/kagent-enterprise-values.yaml"     > "$KAGENT_ENTERPRISE_VALUES_GENERATED"
    envsubst < "$SCRIPT_DIR/enterprise-agentgateway-values.yaml" > "$ENTERPRISE_AGENTGATEWAY_VALUES_GENERATED"
    

### Mirror images and charts from the public registry

Authenticate Docker and Helm to your private Harbor registry, and then mirror the Helm charts and container images from the public registry:
    
    
    # Authenticate to the private Harbor registry before mirroring charts and images.
    helm registry login "$PRIVATE_REGISTRY"
    docker login "$PRIVATE_REGISTRY"
    
    function mirror() {
      if command -v crane &> /dev/null; then
        crane cp "$1" "$2"
      else
        docker pull "$1"
        docker tag "$1" "$2"
        docker push "$2"
      fi
    }
    
    MANAGEMENT_CHARTS=(management-crds management)
    KAGENT_CHARTS=(kagent-enterprise-crds kagent-enterprise)
    AGENTGATEWAY_CHARTS=(enterprise-agentgateway-crds enterprise-agentgateway)
    
    # Mirror Helm chart OCI artifacts to the private registry using the same mirror() helper.
    
    for CHART in "${MANAGEMENT_CHARTS[@]}"; do
      mirror \
        "${PUBLIC_MANAGEMENT_REGISTRY}/${CHART}:${KAGENT_ENT_VERSION}" \
        "${PRIVATE_CHART_REGISTRY}/${CHART}:${KAGENT_ENT_VERSION}"
    done
    
    for CHART in "${KAGENT_CHARTS[@]}"; do
      mirror \
        "${PUBLIC_REGISTRY}/${CHART}:${KAGENT_ENT_VERSION}" \
        "${PRIVATE_CHART_REGISTRY}/${CHART}:${KAGENT_ENT_VERSION}"
    done
    
    for CHART in "${AGENTGATEWAY_CHARTS[@]}"; do
      mirror \
        "${PUBLIC_AGENTGATEWAY_REGISTRY}/${CHART}:${AGENTGATEWAY_VERSION}" \
        "${PRIVATE_CHART_REGISTRY}/${CHART}:${AGENTGATEWAY_VERSION}"
    done
    
    # Discover images by templating the charts directly from their public OCI source.
    
    IMAGES=$( (
      helm template management "oci://${PUBLIC_MANAGEMENT_REGISTRY}/management" \
        --version "$KAGENT_ENT_VERSION" \
        --set products.kagent.enabled=true \
        --set products.agentgateway.enabled=true \
        --set products.agentregistry.enabled=true \
        --set licensing.licenseKey=placeholder
      helm template kagent-enterprise "oci://${PUBLIC_REGISTRY}/kagent-enterprise" \
        --version "$KAGENT_ENT_VERSION" \
        --set licensing.licenseKey=placeholder \
        --set kmcp.licensing.licenseKey=placeholder \
        --set ui.enabled=true \
        --set kagent-tools.enabled=true \
        --set agents.k8s-agent.enabled=true
      helm template enterprise-agentgateway "oci://${PUBLIC_AGENTGATEWAY_REGISTRY}/enterprise-agentgateway" \
        --version "$AGENTGATEWAY_VERSION" \
        --set licensing.licenseKey=placeholder
    ) | grep "image:" | grep -v '{' | sed 's/.*image: //' | tr -d '" ' | grep -E '^[a-zA-Z0-9].*[:/]' | sort -u)
    
    IMAGES_EXTRA="cr.kagent.dev/kagent-dev/kagent/golang-adk:$KAGENT_VERSION cr.kagent.dev/kagent-dev/kagent/app:$KAGENT_VERSION ghcr.io/kagent-dev/kagent/skills-init:$KAGENT_VERSION"
    
    TARGET_PREFIX="${PRIVATE_REPO//\//\\/}"
    
    for IMG in $IMAGES $IMAGES_EXTRA; do
      echo "From: $IMG"
      NEW_IMG=$(echo "$IMG" | sed s/'us-docker\.pkg\.dev\/solo-public'/"$TARGET_PREFIX"/ | sed s/'^clickhouse\/'/"$TARGET_PREFIX\/clickhouse\/"/ | sed s/'^argoproj\/'/"$TARGET_PREFIX\/argoproj\/"/ | sed s/'^docker.io\/otel\/'/"$TARGET_PREFIX\/otel\/"/ | sed s/'^docker.io\/library\/postgres'/"$TARGET_PREFIX\/library\/postgres"/ | sed s/'^cr.kagent.dev\/kagent-dev\/'/"$TARGET_PREFIX\/kagent-dev\/"/ | sed s/'^docker.io\/mcp\/'/"$TARGET_PREFIX\/mcp\/"/ | sed s/'^ghcr.io\/kagent-dev\/'/"$TARGET_PREFIX\/kagent-dev\/"/)
      echo "To  : $NEW_IMG"
      mirror "$IMG" "$NEW_IMG"
    done
    

### Create a namespace in the GDC-SO cluster

Create the target namespace in your cluster:
    
    
    kubectl create namespace "$NAMESPACE" --context "$MGMT_CONTEXT" \
        --dry-run=client -o yaml | kubectl apply --context "$MGMT_CONTEXT" -f -
    

### Create and apply a Docker pull secret to the cluster

Create the Docker registry pull secret in your cluster:
    
    
    kubectl create secret docker-registry "$PULL_SECRET_NAME" \
        --context "$MGMT_CONTEXT" \
        --namespace "$NAMESPACE" \
        --docker-server="$PRIVATE_REGISTRY" \
        --docker-username="REGISTRY_USERNAME" \
        --docker-password="REGISTRY_PASSWORD"
    

Replace the following:

  * `REGISTRY_USERNAME`: your Harbor registry username
  * `REGISTRY_PASSWORD`: your Harbor registry password



### Install kagent

Install the CRD charts and the Solo Enterprise for kagent Helm charts:
    
    
    # Standard clusters allow cluster-scoped resources, so install CRD charts first.
    
    helm upgrade -i management-crds \
      "oci://${PRIVATE_CHART_REGISTRY}/management-crds" \
      "${COMMON_FLAGS[@]}" \
      --version "$KAGENT_ENT_VERSION"
    
    helm upgrade -i kagent-enterprise-crds \
      "oci://${PRIVATE_CHART_REGISTRY}/kagent-enterprise-crds" \
      "${COMMON_FLAGS[@]}" \
      --version "$KAGENT_ENT_VERSION"
    
    helm upgrade -i enterprise-agentgateway-crds \
      "oci://${PRIVATE_CHART_REGISTRY}/enterprise-agentgateway-crds" \
      "${COMMON_FLAGS[@]}" \
      --version "$AGENTGATEWAY_VERSION"
    
    helm upgrade -i management \
      "oci://${PRIVATE_CHART_REGISTRY}/management" \
      "${COMMON_FLAGS[@]}" \
      --version "$KAGENT_ENT_VERSION" \
      --values "$MANAGEMENT_VALUES_GENERATED" \
      --set "licensing.licenseKey=$SOLO_LICENSE_KEY"
    
    helm upgrade -i kagent-enterprise \
      "oci://${PRIVATE_CHART_REGISTRY}/kagent-enterprise" \
      "${COMMON_FLAGS[@]}" \
      --version "$KAGENT_ENT_VERSION" \
      --values "$KAGENT_ENTERPRISE_VALUES_GENERATED" \
      --set "licensing.licenseKey=$SOLO_LICENSE_KEY" \
      --set "kmcp.licensing.licenseKey=$SOLO_LICENSE_KEY" \
      --set "controller.agentImage.tag=$KAGENT_VERSION" \
      --set "controller.skillsInitImage.tag=$KAGENT_VERSION"
    
    
    helm upgrade -i enterprise-agentgateway \
      "oci://${PRIVATE_CHART_REGISTRY}/enterprise-agentgateway" \
      "${COMMON_FLAGS[@]}" \
      --version "$AGENTGATEWAY_VERSION" \
      --values "$ENTERPRISE_AGENTGATEWAY_VALUES_GENERATED" \
      --set "licensing.licenseKey=$SOLO_LICENSE_KEY"
    

### Validate the deployment

Verify that the pods are running in your namespace:
    
    
    kubectl get pods -n "$NAMESPACE" --context "$MGMT_CONTEXT"
    

The output is similar to the following:
    
    
    NAME                                                  READY   STATUS    RESTARTS   AGE
    enterprise-agentgateway-5b57c9496b-hfnqq              1/1     Running   0          36m
    k8s-agent-796b6674f5-fd8cq                            1/1     Running   0          4m8s
    kagent-controller-5f7b44f647-9nd95                    1/1     Running   0          5m31s
    kagent-postgresql-688d8c679d-4g9n9                    1/1     Running   0          36m
    kagent-tools-6b9f8d58c6-t5zsm                         1/1     Running   0          23m
    kmcp-enterprise-controller-manager-7886cdfb57-kgnmw   1/1     Running   0          23m
    management-clickhouse-shard0-0                        1/1     Running   0          14m
    solo-enterprise-telemetry-collector-0                 1/1     Running   0          23m
    solo-enterprise-ui-7c7c889d6-frkvn                    5/5     Running   0          9m34s
    

Forward a local port to the `solo-enterprise-ui` service:
    
    
    kubectl port-forward -n "$NAMESPACE" --context "$MGMT_CONTEXT" \
        svc/solo-enterprise-ui 9090:80
    

In your browser, go to `http://localhost:9090` to open the Solo Enterprise for kagent UI and configure your models and agents:

![Solo Enterprise for kagent UI dashboard.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/kagent-so-impl-ui-dashboard.png)

## Performance considerations and deployment sizing

The following sections describe how component resource consumption scales and provide baseline storage and resource sizing for a single-cluster deployment.

### Scaling characteristics

Resource consumption changes qualitatively as the number of agents and the per-agent request load increase in a single-cluster installation (the `management` and `kagent-enterprise` charts without a relay). Use these characteristics to identify which components are sensitive to specific scaling dimensions before you adjust resource allocations or plan capacity.

#### Key architectural facts that govern scaling

  * **Agent-to-LLM traffic is direct.** Agents call large language model (LLM) endpoints (such as an in-cluster model service) directly. This traffic doesn't pass through the controller or any other management-plane component. Adding agents or increasing request rates doesn't increase LLM-related load on any shared component.
  * **MCP servers are in the hot path of agent tool execution.** When an agent invokes a tool backed by a Model Context Protocol (MCP) server, the call is synchronous and blocking. MCP server latency and throughput directly affect agent request latency. Each deployed `MCPServer` resource is a separate Deployment with its own resource envelope.
  * **Telemetry is the primary scaling surface.** Metrics, traces, and Kubernetes object snapshots all flow through the telemetry pipeline into ClickHouse. This pipeline grows with both agent count and request volume and is the most resource-sensitive part of the system.
  * **The tunnel server is present but carries no meaningful traffic in a single-cluster installation.** The `tunnel-server` container runs in the UI pod, but it has no clients to serve and doesn't contribute to scaling pressure.



#### Component scaling behavior

The following sections describe how individual components scale with agent count and request load.

##### kagent-controller

  * Grows sublinearly with agent count—each agent holds an agent-to-agent (A2A) stream connection.
  * Isn't sensitive to request volume because LLM calls and tool executions bypass the controller.
  * Supports horizontal scaling to distribute connection and policy evaluation load.



##### KMCP enterprise controller

The KMCP enterprise controller is event-driven on `MCPServer` resource changes only and isn't sensitive to agent count or request volume.

##### MCP servers

  * Deploys one Deployment per `MCPServer` custom resource (CR); fleet size grows with the number of `MCPServer` resources deployed.
  * Runs in the synchronous hot path of agent tool execution—latency and throughput directly affect agents.
  * Scales with the total tool call rate across all consumers when shared servers are called by many agents concurrently.
  * Runs built-in servers (`grafana-mcp`, `querydoc`) as a single replica by default; increase replicas or limits for heavily shared use.
  * Uses user-defined images, resource requests, and resource limits for user-deployed MCP servers.



##### Telemetry collector

  * Scales linearly with request volume—each request emits metrics and, optionally, traces.
  * Is the component most likely to become resource-constrained under high agent load.
  * Serves as the OpenTelemetry Protocol (OTLP) gateway (receivers on ports 4316-4318) for remote clusters in a multi-cluster installation; no separate gateway pod exists.
  * Uses the `k8sobjects` sidecar, which scales with Kubernetes inventory size rather than request rate.



##### ClickHouse

ClickHouse is the primary resource bottleneck under sustained load. Storage, memory, and CPU all grow with the following factors:

  * **Agent count:** Each additional agent type increases metric cardinality (unique label combinations).
  * **Request volume:** Each request produces metric data points and trace spans that are written and indexed.
  * **Kubernetes inventory size:** `k8sobjects` snapshots are stored periodically regardless of request load.



Write throughput is the initial pressure point; query performance (used by the UI backend) degrades as data volume grows without schema or retention tuning. The default configuration targets a moderate single-node deployment; heavier loads might require increasing `replicasPerShard` or `shards`, or adjusting retention TTLs.

##### UI backend

  * Is stateless and query-bound; scales with data volume in ClickHouse rather than real-time request throughput.
  * Increases the cost of fleet graph and trace queries as agent count and historical data grow.



##### Agents

  * **Python-based agents:**
    * Each agent is an independent Deployment—adding agents is purely additive with no shared-state penalty.
    * Per-agent resource consumption scales with request concurrency and tool chain depth.
  * **Go-based agents:**
    * Uses approximately 36 times less idle memory (7 MB versus 253 MB per agent at rest).
    * Uses an approximately 11 times smaller container image (29.7 MB versus 335.4 MB).
    * Starts approximately 6.7 times faster (2.7 seconds versus 18.2 seconds).



#### Scaling characteristic summary

The following table summarizes how each component scales with agent count and request load:

Component | Sensitive to agent count | Sensitive to request load | Notes  
---|---|---|---  
Controller | Moderate | Low | Maintains A2A streams per agent; not affected by LLM call rate  
Scaler | None | None | Event-driven, effectively static  
KMCP enterprise controller | None | None | Reacts to `MCPServer` resource changes only  
MCP servers | High | High | One Deployment per `MCPServer` CR; in the hot path of tool execution  
Telemetry collector | High | High | Primary scaling surface; linear with request volume  
ClickHouse | High | High | Primary bottleneck; driven by cardinality and write rate  
UI backend | Low | Low | Query-bound; affected by historical data volume  
Agents (Python and Go) | Not applicable | High | Independent Deployments; scale with concurrency  
  
### Storage sizing

The following table provides initial recommendations for starting storage volume sizes:

  * PostgreSQL storage (kagent state, including session, memory, and lifecycle management) scales linearly as the number of chat sessions increases.
  * ClickHouse storage (tracing) also scales linearly as the number of unique chat sessions increases.

Component | Recommended starting volume  
---|---  
PostgreSQL | 50 GiB  
ClickHouse | 50 GiB  
  
### Deployment sizing

The following sections list the default CPU, memory, and storage resource requests and limits for the Helm charts.

#### Management chart

The `management` chart deploys the `solo-enterprise-ui` pod, a standalone telemetry collector, and ClickHouse.

##### `solo-enterprise-ui` pod containers

The following table lists the default resource requests and limits for the `solo-enterprise-ui` pod containers:

Container | Enabled | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---|---  
`ui-backend` | Always | 250m | 500m | 512Mi | 1024Mi  
`ui-frontend` | Always | 250m | 500m | 512Mi | 1024Mi  
`k8sobjects-collector` | `telemetry.k8sobjects.enabled` | 100m | 300m | 384Mi | 768Mi  
`idp` | `autoAuth` enabled | 100m | 250m | 256Mi | 512Mi  
  
##### Telemetry collector (StatefulSet or Deployment)

The following table lists the default resource requests and limits for the telemetry collector:

Component | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---  
`telemetry-collector` | 200m | 1000m | 512Mi | 2Gi  
  
The telemetry gateway (OpenTelemetry collector) also defines its own resources separately:

Component | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---  
`telemetry-gateway` | 100m | 500m | 300Mi | 1024Mi  
  
##### ClickHouse subchart

The following table lists the default resource requests and limits for the ClickHouse subchart, based on the Bitnami `2xlarge` preset and configured by using the `replicasPerShard` and `shards` values:

Component | CPU request | CPU limit | Memory request | Memory limit | Ephemeral storage  
---|---|---|---|---|---  
`clickhouse` | 1000m (1 core) | 6000m (6 cores) | 3072Mi (3 GiB) | 12288Mi (12 GiB) | 50Mi  
  
#### kagent-enterprise chart

The `kagent-enterprise` chart deploys the core controller, the `kmcp-enterprise` subchart, built-in MCP tool servers, and optional agents.

##### Core components

The following table lists the default resource requests and limits for the core controller:

Component | Enabled | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---|---  
`controller` | Always | 100m | 2000m (2 cores) | 128Mi | 512Mi  
  
##### kmcp-enterprise subchart

The following table lists the default resource requests and limits for the `kmcp-enterprise` controller:

Component | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---  
`kmcp-enterprise-controller` | 100m | 500m | 128Mi | 512Mi  
  
##### Built-in tools

The following table lists the default resource requests and limits for the built-in tool servers:

Component | Enabled | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---|---  
`kagent-tools` | `kagent-tools.enabled` | 100m | 1000m | 256Mi | 1Gi  
`grafana-mcp` | `grafana-mcp.enabled` | 100m | 500m | 128Mi | 512Mi  
`querydoc` | `querydoc.enabled` | 100m | 500m | 128Mi | 512Mi  
  
##### Agents

All agents share the same default resource profile. Each agent is disabled by default and enabled individually:

Agent | CPU request | CPU limit | Memory request | Memory limit  
---|---|---|---|---  
`k8s-agent` | 100m | 1000m | 256Mi | 1Gi  
`kgateway-agent` | 100m | 1000m | 256Mi | 1Gi  
`istio-agent` | 100m | 1000m | 256Mi | 1Gi  
`promql-agent` | 100m | 1000m | 256Mi | 1Gi  
`observability-agent` | 100m | 1000m | 256Mi | 1Gi  
`argo-rollouts-agent` | 100m | 1000m | 256Mi | 1Gi  
`helm-agent` | 100m | 1000m | 256Mi | 1Gi  
`cilium-policy-agent` | 100m | 1000m | 256Mi | 1Gi  
`cilium-manager-agent` | 100m | 1000m | 256Mi | 1Gi  
`cilium-debug-agent` | 100m | 1000m | 256Mi | 1Gi  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 
