---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-load-balancer-k8s/
title: Configure a load balancer for AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-08T08:59:21.300941+00:00
---

# Configure a load balancer for AlloyDB Omni on Kubernetes  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-load-balancer-k8s/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Configure a load balancer for AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-load-balancer-k8s)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-load-balancer-k8s)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/configure-load-balancer-k8s)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-load-balancer-k8s)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/configure-load-balancer-k8s)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-load-balancer-k8s)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-load-balancer-k8s)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-load-balancer-k8s)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/configure-load-balancer-k8s)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/configure-load-balancer-k8s)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/configure-load-balancer-k8s)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-load-balancer-k8s)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-load-balancer-k8s)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/configure-load-balancer-k8s)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/configure-load-balancer-k8s)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/configure-load-balancer-k8s)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/configure-load-balancer-k8s)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-load-balancer-k8s)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/configure-load-balancer-k8s)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-load-balancer-k8s)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/configure-load-balancer-k8s)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-load-balancer-k8s)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/configure-load-balancer-k8s)

To expose your AlloyDB Omni database cluster to clients outside your Kubernetes cluster, you can configure a `LoadBalancer` Service in the `DBCluster` manifest. This document is for database administrators and Kubernetes operators who manage AlloyDB Omni deployments on Kubernetes and need to customize load balancer behavior. 

When you enable external incoming traffic in your `DBCluster` manifest, the AlloyDB Omni Kubernetes operator creates a Kubernetes `Service` object of type `LoadBalancer`. Different Kubernetes platforms use custom annotations to control load balancer properties, such as internal or external IP address assignment. AlloyDB Omni lets you specify these annotations in the `spec.primarySpec.dbLoadBalancerOptions.annotations` field of your `DBCluster` manifest. When you create or update the database cluster with `spec.allowExternalIncomingTraffic` set to `true`, the AlloyDB Omni operator applies those annotations to the `metadata.annotations` field of the `LoadBalancer` `Service` object.

## Configure a load balancer using the database spec

You can configure custom load balancer annotations by setting the `dbLoadBalancerOptions` field in the `spec.primarySpec` section of your `DBCluster` manifest.

###  Kubernetes 

Annotations define the type and properties of the load balancer `Service` object in your Kubernetes environment. Check the documentation for your Kubernetes platform or load balancer implementation to identify the supported annotation keys and values.

To create a database cluster with custom load balancer annotations and allow incoming traffic from outside the Kubernetes cluster, apply the following manifest:
    
    
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-DB_CLUSTER_NAME
      namespace: NAMESPACE
    type: Opaque
    data:
      DB_CLUSTER_NAME: "ENCODED_PASSWORD"
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
      namespace: NAMESPACE
    spec:
      databaseVersion: "17.9.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-DB_CLUSTER_NAME
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        dbLoadBalancerOptions:
          annotations:
            **ANNOTATION_KEY : "ANNOTATION_VALUE"**
      **allowExternalIncomingTraffic: true**
    EOF

Replace the following:

  * `DB_CLUSTER_NAME`: a name for your database cluster—for example, `my-db-cluster`.
  * `NAMESPACE`: the Kubernetes namespace for your database cluster.
  * `ENCODED_PASSWORD`: the password for the `postgres` administrator user, encoded as a base64 string.
  * `ANNOTATION_KEY` and `ANNOTATION_VALUE`: a load balancer annotation key and string value supported by your Kubernetes environment. Enclose the value in double quotes, even for boolean or numeric values such as `"true"`. You can specify one or more key-value pairs under `annotations`.



In this manifest:

  * `ANNOTATION_KEY: "ANNOTATION_VALUE"`: specifies a custom annotation that the AlloyDB Omni operator adds to the load balancer `Service` object for your database cluster.
  * `allowExternalIncomingTraffic: true`: sets the `allowExternalIncomingTraffic` field to `true` to allow incoming traffic from outside the Kubernetes cluster.

**Note:** To configure custom load balancer annotations on an existing database cluster, add `allowExternalIncomingTraffic: true` and `primarySpec.dbLoadBalancerOptions.annotations` to your existing `DBCluster` manifest and apply it, rather than re-applying the sample `Secret` and `resources` block.

## Get the database cluster and connectivity details

###  Kubernetes 

To verify that the database cluster resource is in the `Ready` status, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog -n NAMESPACE -w

Replace `NAMESPACE` with the Kubernetes namespace for your database cluster.

The output is similar to the following:
    
    
    NAME               PRIMARYENDPOINT   PRIMARYPHASE   DBCLUSTERPHASE
    DB_CLUSTER_NAME    10.95.0.84        Ready          DBClusterReady
    

To verify that your custom annotation and the assigned external endpoint exist on the load balancer `Service` object, run the following command:
    
    
    kubectl get svc LOAD_BALANCER_SERVICE_NAME -n NAMESPACE -o yaml

Replace the following:

  * `LOAD_BALANCER_SERVICE_NAME`: the name of the operator-managed `LoadBalancer` `Service` object. For the primary read-write endpoint, the AlloyDB Omni operator names this `Service` `al-DB_CLUSTER_NAME-rw-elb` (you can also list `Service` objects by running `kubectl get svc -n NAMESPACE`).
  * `NAMESPACE`: the name of the Kubernetes namespace for your load balancer `Service` object.



The output is similar to the following:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        **ANNOTATION_KEY : "ANNOTATION_VALUE"**
      creationTimestamp: "2024-02-22T15:26:18Z"
      finalizers:
      - service.kubernetes.io/load-balancer-cleanup
      labels:
        alloydbomni.internal.dbadmin.goog/dbcluster: DB_CLUSTER_NAME
        alloydbomni.internal.dbadmin.goog/dbcluster-ns: NAMESPACE
      name: LOAD_BALANCER_SERVICE_NAME
      namespace: NAMESPACE
      ownerReferences:
      - apiVersion: alloydbomni.dbadmin.goog/v1
        blockOwnerDeletion: true
        controller: true
        kind: DBCluster
        name: DB_CLUSTER_NAME
        uid: 2dd76c9f-7698-4210-be41-6d2259840a85
      resourceVersion: "33628320"
      uid: 1f45362b-6d6f-484d-ad35-11c14e91933e
    spec:
      allocateLoadBalancerNodePorts: true
      clusterIP: 10.60.4.76
      clusterIPs:
      - 10.60.4.76
      externalTrafficPolicy: Cluster
      internalTrafficPolicy: Cluster
      ipFamilies:
      - IPv4
      ipFamilyPolicy: SingleStack
      ports:
      - name: db
        nodePort: 31453
        port: 5432
        protocol: TCP
        targetPort: 5432
      selector:
        alloydbomni.internal.dbadmin.goog/dbcluster: DB_CLUSTER_NAME
        alloydbomni.internal.dbadmin.goog/dbcluster-ns: NAMESPACE
        alloydbomni.internal.dbadmin.goog/task-type: database
        dbs.internal.dbadmin.goog/ha-role: Primary
      sessionAffinity: None
      type: LoadBalancer
    status:
      loadBalancer:
        ingress:
        - **ip: 10.95.0.84**

The output includes the following fields:

  * `metadata.annotations`: contains the `ANNOTATION_KEY: "ANNOTATION_VALUE"` annotation that you configured in your `DBCluster` manifest.
  * `status.loadBalancer.ingress`: displays the external endpoint assigned to the load balancer `Service` object. Depending on your Kubernetes environment, the load balancer controller populates either `ip` (which matches the `PRIMARYENDPOINT` value of your database cluster) or `hostname` (for DNS-based load balancers such as on AWS EKS, where `status.primary.endpoints` on the `DBCluster` records the hostname and port).



## What's next

  * [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage)
  * [Use the PgBouncer connection pooler](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/use-connection-pooler-kubernetes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 
