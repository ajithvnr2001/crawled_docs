---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage-certificates-kubernetes-operator/
title: Manage certificates \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:47:32.697780+00:00
---

# Manage certificates  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage-certificates-kubernetes-operator/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  Manage certificates Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage-certificates-kubernetes-operator)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/manage-certificates-kubernetes-operator)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage-certificates-kubernetes-operator)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage-certificates-kubernetes-operator)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/manage-certificates-kubernetes-operator)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/manage-certificates-kubernetes-operator)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/manage-certificates-kubernetes-operator)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/manage-certificates-kubernetes-operator)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage-certificates-kubernetes-operator)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/manage-certificates-kubernetes-operator)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/manage-certificates-kubernetes-operator)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/manage-certificates-kubernetes-operator)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage-certificates-kubernetes-operator)



Custom certificate issuers let you manage Transport Layer Security (TLS) certificates on your Kubernetes-based AlloyDB Omni database cluster.

By default, the AlloyDB Omni Kubernetes operator uses cert-manager to provision a set of TLS certificates for each database cluster. Besides the database server certificate, the operator also creates certificates for control plane components to ensure internal connections are also secure. By default, each certificate is signed by an issuer managed by the operator.

If you prefer all certificates, including those for control plane components, to be chained back to your own trusted root certificate authority (CA), you can configure the operator to use an issuer of your choice. This lets you chain all certificates to your own public key infrastructure (PKI), including certificates used for control plane functionality, without exposing the implementation details of each internal entity.

## Default certificate lifetimes

By default, the AlloyDB Omni operator uses cert-manager to issue and automatically renew TLS certificates for the operator, control plane, and database instances.

The following table lists the default validity durations for certificates managed by the AlloyDB Omni operator:

Certificate type | Certificate description | Secret name | Namespace | Default duration  
---|---|---|---|---  
Operator mTLS client certificate | Used by the `local-controller-manager` Deployment for high availability (HA) health checks and connections between the operator and control plane agents. | `dbs-al-cert-l2-operator` | Operator namespace | `1440h0m0s` (60 days)  
Operator webhook server certificates | Used by the operator admission webhook servers to validate and mutate custom resources. | `fleet-webhook-server-cert`  
  
`local-webhook-server-cert` | Operator namespace | `1440h0m0s` (60 days)  
Per-instance control plane agent certificates | Used by the per-instance database agent, node manager, and backup daemon for control plane connections. | `dbs-al-cert-dbd-INSTANCE_ID-DB_CLUSTER_NAME`  
  
`dbs-al-cert-al-INSTANCE_ID-DB_CLUSTER_NAME-nm`  
  
`dbs-al-cert-backup-daemon-BACKUP_REPO_NAME` | Database cluster namespace | `1440h0m0s` (60 days)  
Backup certificates | Used by backup services for backup and restore connections. | `dbs-al-cert-backup-client`  
  
`dbs-al-cert-backup-client-DATA_PLANE_ISSUER_NAME`  
  
`dbs-al-cert-backup-server-INSTANCE_ID-DB_CLUSTER_NAME`  
  
`dbs-al-cert-standby-backup-server-INSTANCE_ID-DB_CLUSTER_NAME` | Database cluster namespace | `1440h0m0s` (60 days)  
Database server certificate | Secures data plane client connections to the database instance. | `dbs-al-cert-DB_CLUSTER_NAME` | Database cluster namespace | `87600h0m0s` (10 years)  
PgBouncer auth query certificate | Database client certificate used by the PgBouncer Deployment to connect to the database and perform connection pooling. Created only when you create a `PgBouncer` resource. | `dbs-al-pgb-cert-PGBOUNCER_NAME` | Database cluster namespace | `87600h0m0s` (10 years)  
Operator-managed self-signed CA certificates | Root CA certificates used by the operator's default self-signed issuers to sign operator, control plane agent, backup, and database server certificates. | `dbs-al-ca-l2-operator`  
  
`dbs-al-ca-DB_CLUSTER_NAME`  
  
`dbs-al-ca-dbd-INSTANCE_ID-DB_CLUSTER_NAME`  
  
`dbs-al-ca-backup-server`  
  
`dbs-al-ca-backup-daemon-BACKUP_REPO_NAME` | Operator namespace and database cluster namespace | `87600h0m0s` (10 years)  
  
In this table, the Secret names use the following placeholders:

  * `INSTANCE_ID`: the 4-character identifier generated for the database instance.
  * `DB_CLUSTER_NAME`: the name of your `DBCluster` resource.
  * `DATA_PLANE_ISSUER_NAME`: the name of the custom cert-manager issuer configured in `spec.primarySpec.tls.dataPlaneCertIssuer.name`, if specified.
  * `BACKUP_REPO_NAME`: the name of your `BackupRepository` resource, if configured.
  * `PGBOUNCER_NAME`: the name of your `PgBouncer` resource.

**Warning:** In AlloyDB Omni operator versions earlier than 1.8.2, the operator doesn't reload the renewed `dbs-al-cert-l2-operator` client certificate into existing HA health-check connections. Approximately 60 days after the certificate is issued, health checks might fail with a `tls: expired certificate` error and trigger an unplanned failover. To avoid this issue, upgrade to operator version 1.8.2 or later, or follow the steps in Mitigate operator client certificate expiration in operator versions earlier than 1.8.2.

## Configure custom issuers

You can configure custom certificate issuers for the database cluster, the AlloyDB Omni operator, and PgBouncer.

To configure a certificate issuer, you must first create a [cert-manager issuer](https://cert-manager.io/docs/configuration/) of type `ClusterIssuer` or `Issuer` that is associated with the CA you want to sign your certificates. The AlloyDB Omni operator references this issuer when creating [certificates](https://cert-manager.io/docs/usage/certificate/).

### Database cluster certificates

There are two database cluster spec fields to configure certificate issuers:

  * `spec.primarySpec.tls.dataPlaneCertIssuer`: a reference to the cert-manager issuer that provisions data plane certificates. The issuer CA is the one that the database client can trust in order to verify the database during a TLS connection.

  * `spec.primarySpec.tls.controlPlaneAgentsCertIssuer`: a reference to the cert-manager issuer that provisions control plane certificates. These certificates are used for internal connections.



    
    
    spec:
      primarySpec:
        tls:
          dataPlaneCertIssuer:
            name: DATA_PLANE_ISSUER_NAME
            kind: DATA_PLANE_ISSUER_KIND
          controlPlaneAgentsCertIssuer:
            name: CONTROL_PLANE_ISSUER_NAME
            kind: CONTROL_PLANE_ISSUER_KIND
    

Replace the following:

  * `DATA_PLANE_ISSUER_NAME`: the name of the cert-manager issuer that provisions data plane certificates, such as for the database server.

  * `DATA_PLANE_ISSUER_KIND`: the API kind of the cert-manager issuer, which must be either `Issuer` or `ClusterIssuer`. Defaults to `Issuer`.

  * `CONTROL_PLANE_ISSUER_NAME`: the name of the cert-manager issuer that provisions control plane certificates for internal components.

  * `CONTROL_PLANE_ISSUER_KIND`: the API kind of the cert-manager issuer, which must be either `Issuer` or `ClusterIssuer`. Defaults to `Issuer`.




### Operator certificates

The steps for configuring a cert-manager issuer for operator certificates depend on the method used to install the AlloyDB Omni operator.

#### Configure using Helm

If you are installing the AlloyDB Omni operator for the first time, use `helm install` and set the appropriate values. This assumes that you follow the instructions to [deploy the operator using Helm](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes).
    
    
    helm install alloydbomni-operator alloydbomni-operator-OPERATOR_VERSION.tgz \
    --create-namespace \
    --namespace alloydb-omni-system \
    --set operatorCertIssuer.certManagerIssuerName="OPERATOR_CERT_ISSUER_NAME" \
    --set operatorCertIssuer.certManagerIssuerKind="OPERATOR_CERT_ISSUER_KIND" \
    --atomic \
    --timeout 5m
    

If you already have the operator installed and need to set the certificate issuer, use `helm upgrade` to set the appropriate values:
    
    
    helm upgrade alloydbomni-operator alloydbomni-operator-OPERATOR_VERSION.tgz \
    --create-namespace \
    --namespace alloydb-omni-system \
    --set operatorCertIssuer.certManagerIssuerName="OPERATOR_CERT_ISSUER_NAME" \
    --set operatorCertIssuer.certManagerIssuerKind="OPERATOR_CERT_ISSUER_KIND" \
    --atomic \
    --timeout 5m
    

Replace the following:

  * `OPERATOR_VERSION`: the version of the AlloyDB Omni operator to install.

  * `OPERATOR_CERT_ISSUER_NAME`: the name of the cert-manager issuer that provisions the operator certificate, which is used for internal connections.

  * `OPERATOR_CERT_ISSUER_KIND`: the API kind of the cert-manager issuer, which must be either `Issuer` or `ClusterIssuer`. Defaults to `Issuer`.




#### Configure using Operator Lifecycle Manager

If you used Operator Lifecycle Manager (OLM) to install the AlloyDB Omni operator, you can modify the `Subscription` resource `spec.config.env` field to set the `CERT_MANAGER_ISSUER_NAME` and `CERT_MANAGER_ISSUER_KIND` environment variables of the operator `Deployment`.
    
    
    spec:
      config:
        env:
        - name: CERT_MANAGER_ISSUER_NAME
          value: OPERATOR_CERT_ISSUER_NAME
        - name: CERT_MANAGER_ISSUER_KIND
          value: OPERATOR_CERT_ISSUER_KIND
    

Replace the following:

  * `OPERATOR_CERT_ISSUER_NAME`: the name of the cert-manager issuer that provisions the operator certificate, which is used for internal connections.

  * `OPERATOR_CERT_ISSUER_KIND`: the API kind of the cert-manager issuer, which must be either `Issuer` or `ClusterIssuer`. Defaults to `Issuer`.




### PgBouncer certificates

To support custom issuers, the PgBouncer controller checks the `DBCluster` `spec.primarySpec.tls.dataPlaneCertIssuer` field and uses that to provision the PgBouncer certificate. The PgBouncer controller also uses the attributes configured in `spec.primarySpec.tls.dataPlaneCertRequest` to provision the PgBouncer certificate. This helps ensure that PgBouncer uses a certificate from the same CA that has the same attributes as the database.

## Configure custom certificate attributes

You can customize the attributes of the TLS certificates generated by the operator, such as the certificate duration, renewal window, subject alternative names (SANs), common name, and private key configuration.

You configure custom certificate attributes in your `DBCluster` manifest:

  * `spec.primarySpec.tls.dataPlaneCertRequest`: specifies attributes for data plane certificates, including the pgBackRest server, PgBouncer auth query, and database server certificates.
  * `spec.primarySpec.tls.controlPlaneAgentsCertRequest`: specifies attributes for provisioning control plane certificates. These certificates are used for internal connections.



### Configure certificate requests

Specify the request properties in the following format:
    
    
    spec:
      primarySpec:
        tls:
          dataPlaneCertRequest:
            commonName: DATABASE_COMMON_NAME
            dnsNames:
            - DATABASE_DNS_NAME_1
            - DATABASE_DNS_NAME_2
            duration: DATA_PLANE_DURATION
            renewBefore: DATA_PLANE_RENEW_BEFORE
            privateKey:
              algorithm: DATA_PLANE_ALGORITHM
              size: DATA_PLANE_KEY_SIZE
              rotationPolicy: DATA_PLANE_ROTATION_POLICY
          controlPlaneAgentsCertRequest:
            duration: CONTROL_PLANE_DURATION
            renewBefore: CONTROL_PLANE_RENEW_BEFORE
            privateKey:
              algorithm: CONTROL_PLANE_ALGORITHM
              size: CONTROL_PLANE_KEY_SIZE
              rotationPolicy: CONTROL_PLANE_ROTATION_POLICY
    

Replace the following:

  * `DATABASE_COMMON_NAME`: (Optional, data plane only) the common name of the database certificate.
  * `DATABASE_DNS_NAME_1`, `DATABASE_DNS_NAME_2`: (Optional, data plane only) a list of subject alternative names (SANs) for the database certificate.
  * `DATA_PLANE_DURATION` and `CONTROL_PLANE_DURATION`: the requested validity duration of the certificate as a string duration—for example, `720h0m0s` for a custom 30-day duration. In each certificate request block, you must either specify both `duration` and `renewBefore` (with `renewBefore` less than `duration`) or omit both fields. When both fields are omitted, the default duration is `1440h0m0s`, or 60 days, for control plane and backup certificates, and `87600h0m0s`, or 10 years, for the database server and PgBouncer auth query certificates.
  * `DATA_PLANE_RENEW_BEFORE` and `CONTROL_PLANE_RENEW_BEFORE`: the duration before expiration that cert-manager must start a renewal attempt—for example, `120h0m0s` for five days before expiration. In each certificate request block, you must either specify both `duration` and `renewBefore` (with `renewBefore` less than `duration`) or omit both fields. When both fields are omitted, the default renewal window is `120h0m0s`, or five days, for control plane and backup certificates, and `1440h0m0s`, or 60 days, for the database server and PgBouncer auth query certificates.
  * `DATA_PLANE_ALGORITHM` and `CONTROL_PLANE_ALGORITHM`: the private key algorithm. Valid values are `RSA`, `ECDSA`, or `Ed25519`.
  * `DATA_PLANE_KEY_SIZE` and `CONTROL_PLANE_KEY_SIZE`: the private key size in bits. If the algorithm is `RSA`, valid values are `4096` or `8192` (default is `4096`). If the algorithm is `ECDSA`, valid values are `384` or `521` (default is `384`). If the algorithm is `Ed25519`, size is ignored.
  * `DATA_PLANE_ROTATION_POLICY` and `CONTROL_PLANE_ROTATION_POLICY`: the policy that controls private key regeneration. Valid values are `Always` or `Never`.



### Operator and backup client certificates

To customize certificate attributes for the operator and the backup client (which are shared across all instances in a namespace and aren't managed by a database cluster specification), modify the `Certificate` custom resources. The operator retains these manual modifications.

## Clean up certificate secrets

When you delete a `DBCluster` resource, the AlloyDB Omni operator deletes the associated `Certificate` resources, but cert-manager does not clean up the certificate `Secret` resources by default. To configure the cert-manager controller to clean up secrets when certificates are deleted, see [Cleaning up secrets when certificates are deleted](https://cert-manager.io/docs/usage/certificate/#cleaning-up-secrets-when-certificates-are-deleted) in cert-manager documentation.

If you have already deleted a `DBCluster` resource without configuring the automated cleanup, delete the dangling certificate secrets manually:
    
    
    kubectl delete secret CERTIFICATE_SECRET_NAME -n NAMESPACE
    

Replace the following:

  * `CERTIFICATE_SECRET_NAME`: the name of the certificate secret to delete.
  * `NAMESPACE`: the namespace of the database cluster.



## Verify

To verify that the operator `Deployment` is healthy and that the environment variables `CERT_MANAGER_ISSUER_NAME` and `CERT_MANAGER_ISSUER_KIND` are set, run the following command:
    
    
    kubectl get deployments local-controller-manager -n alloydb-omni-system -o yaml
    

To verify that the correct issuer is used, inspect the `Certificate` objects as follows:
    
    
    kubectl get certificate -n NAMESPACE
    

Replace `NAMESPACE` with the namespace of your database cluster or `alloydb-omni-system` for the operator certificate.

Check the `issuerRef` field in the output for each certificate to confirm that it matches your custom issuer.

## Mitigate operator client certificate expiration in operator versions earlier than 1.8.2

In AlloyDB Omni operator versions earlier than 1.8.2, the `local-controller-manager` Deployment caches the 60-day `dbs-al-cert-l2-operator` mTLS client certificate in memory for HA health-check connections to control plane agents. Although cert-manager automatically renews the `dbs-al-cert-l2-operator` Secret five days before expiration, the `local-controller-manager` Deployment doesn't reload the renewed certificate until the operator Pod restarts. When the cached certificate expires on day 60, subsequent health-check reconnections fail with a `tls: expired certificate` error and might trigger unplanned HA failovers.

To permanently resolve this issue, [upgrade the AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-operator-version) to version 1.8.2 or later.

If you can't upgrade to operator version 1.8.2 or later right away, rotate the `dbs-al-cert-l2-operator` Secret and restart the `local-controller-manager` Deployment at least 10 days before the certificate expires. This procedure doesn't restart database Pods or disrupt database traffic.

**Caution:** Don't run this procedure while a failover, switchover, or backup operation is in progress. Delete only the leaf certificate Secret (`dbs-al-cert-l2-operator`) in the `alloydb-omni-system` namespace. Don't delete the 10-year root CA Secret (`dbs-al-ca-l2-operator`) or the `dbs-al-cert-request-l2-operator` `Certificate` resource.

### Before you begin

Before you run the `rotate_cert.sh` script, confirm that your environment meets the following requirements:

  * Install `bash`, `kubectl`, `openssl`, and `base64` in your `PATH`.
  * [Configure access to your Kubernetes cluster](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) and set your active `kubectl` context to the target cluster. To confirm the active context, run `kubectl config current-context`. Repeat this procedure for each cluster that runs an operator version earlier than 1.8.2.
  * Confirm that your account has [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) permissions in the operator namespace, which defaults to `alloydb-omni-system`: 
    * `get` on `Certificate` resources and `Pod` logs
    * `get` and `list` on `Pod` resources
    * `get` and `delete` on the `dbs-al-cert-l2-operator` Secret (plus `create` and `patch` to restore a backed-up Secret)
    * `get` and `patch` on the `local-controller-manager` Deployment
    * `delete` on `CertificateRequest` resources (to restore a backed-up Secret)



### Rotate the operator client certificate

The `rotate_cert.sh` script supports two modes and an optional namespace argument, which defaults to `alloydb-omni-system`:

  * `./rotate_cert.sh check`: performs a read-only check and prints the following information: 
    * Current certificate serial number and validity dates
    * Recommended rotation deadline, set 10 days before expiration
    * `local-controller-manager` container start time
    * In-memory certificate status of either `[OK]` or `[WARNING]`
    * A `kubectl` backup command
  * `./rotate_cert.sh rotate`: performs the following actions: 
    * Deletes the `dbs-al-cert-l2-operator` Secret
    * Waits for cert-manager to issue a new certificate serial number and update the `dbs-al-cert-request-l2-operator` `Certificate` resource
    * Restarts the `local-controller-manager` Deployment
    * Checks the new Pod's logs and prints the new expiration date



To check and rotate the operator client certificate, follow these steps:

  1. Save the following script to a file named `rotate_cert.sh`, and then make the file executable:
         
         cat << 'EOF' > rotate_cert.sh
         #!/usr/bin/env bash
         set -euo pipefail
         MODE="${1:-}"
         NS="${2:-alloydb-omni-system}"
         SECRET="dbs-al-cert-l2-operator"
         CERT="dbs-al-cert-request-l2-operator"
         DEPLOY="local-controller-manager"
         get_cert_info() {
           kubectl get secret "$SECRET" -n "$NS" -o jsonpath='{.data.tls\.crt}' 2>/dev/null \
             | base64 -d 2>/dev/null | openssl x509 -noout -serial -enddate 2>/dev/null || true
         }
         calc_rotate_by() {
           date -u -d "$1 - 10 days" +"%Y-%m-%d" 2>/dev/null \
             || date -u -j -v-10d -f "%Y-%m-%dT%H:%M:%SZ" "$1" +"%Y-%m-%d" 2>/dev/null || echo "unknown"
         }
         get_container_name() {
           local names
           names="$(kubectl get pods -n "$NS" -l local-control-plane=controller-manager \
             --field-selector=status.phase=Running --sort-by=.metadata.creationTimestamp \
             -o jsonpath='{.items[-1].spec.containers[*].name}' 2>/dev/null || true)"
           if [[ " $names " == *" local-manager "* ]]; then
             echo "local-manager"
           else
             echo "manager"
           fi
         }
         case "$MODE" in
           check)
             INFO="$(get_cert_info)"
             SERIAL="$(echo "$INFO" | sed -n 's/^serial=//p')"
             ENDDATE="$(echo "$INFO" | sed -n 's/^notAfter=//p')"
             NOT_BEFORE="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.notBefore}')"
             NOT_AFTER="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.notAfter}')"
             CONTAINER="$(get_container_name)"
             STARTED_AT="$(kubectl get pods -n "$NS" -l local-control-plane=controller-manager \
               --field-selector=status.phase=Running --sort-by=.metadata.creationTimestamp \
               -o jsonpath="{.items[-1].status.containerStatuses[?(@.name==\"$CONTAINER\")].state.running.startedAt}")"
             echo "Certificate Serial      : $SERIAL"
             echo "Certificate Start Date  : $NOT_BEFORE"
             echo "Certificate End Date    : $ENDDATE ($NOT_AFTER)"
             echo "Recommended Rotate By   : $(calc_rotate_by "$NOT_AFTER") (10 days before expiry)"
             echo "Operator Started At     : $STARTED_AT"
             if [[ "$STARTED_AT" < "$NOT_BEFORE" ]]; then
               echo "[WARNING] Operator started ($STARTED_AT) BEFORE current cert was issued ($NOT_BEFORE). It is still caching the old cert in memory! Run './rotate_cert.sh rotate $NS' now."
             else
               echo "[OK] Operator is running with the current certificate in memory."
             fi
             echo "Optional Backup Command : kubectl get secret $SECRET -n $NS -o yaml > $SECRET-backup.yaml"
             ;;
           rotate)
             OLD_SERIAL="$(get_cert_info | sed -n 's/^serial=//p')"
             OLD_REV="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.revision}' 2>/dev/null || true)"
             echo "Current Certificate Serial: ${OLD_SERIAL:-none}"
             kubectl delete secret "$SECRET" -n "$NS" --ignore-not-found
             NEW_SERIAL=""
             NOT_AFTER=""
             for _ in {1..30}; do
               sleep 2
               NEW_SERIAL="$(get_cert_info | sed -n 's/^serial=//p')"
               NEW_REV="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.revision}' 2>/dev/null || true)"
               READY_COND="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' 2>/dev/null || true)"
               NOT_AFTER="$(kubectl get certificate "$CERT" -n "$NS" -o jsonpath='{.status.notAfter}' 2>/dev/null || true)"
               [[ -n "$NEW_SERIAL" && "$NEW_SERIAL" != "$OLD_SERIAL" && "$NEW_REV" != "$OLD_REV" && "$READY_COND" == "True" && -n "$NOT_AFTER" ]] && break
             done
             [[ -n "$NEW_SERIAL" && "$NEW_SERIAL" != "$OLD_SERIAL" && "$READY_COND" == "True" ]] || { echo "[ERROR] Timed out waiting for new cert."; exit 1; }
             kubectl rollout restart "deployment/$DEPLOY" -n "$NS"
             kubectl rollout status "deployment/$DEPLOY" -n "$NS" --timeout=180s
             NEW_POD="$(kubectl get pods -n "$NS" -l local-control-plane=controller-manager \
               --field-selector=status.phase=Running --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1].metadata.name}')"
             CONTAINER="$(get_container_name)"
             READY=false
             for _ in {1..40}; do
               LOGS="$(kubectl logs "pod/$NEW_POD" -n "$NS" -c "$CONTAINER" 2>/dev/null || true)"
               grep -q "tls: expired certificate" <<<"$LOGS" && { echo "[ERROR] Found 'tls: expired certificate' in operator logs!"; exit 1; }
               grep -q "L2 controller cert generation completed successfully" <<<"$LOGS" && { READY=true; break; }
               sleep 3
             done
             [[ "$READY" == "true" ]] || { echo "[ERROR] Timed out waiting for L2 controller cert generation log."; exit 1; }
             echo "[SUCCESS] New Serial: $NEW_SERIAL | End Date: $NOT_AFTER | Next Rotate By: $(calc_rotate_by "$NOT_AFTER") (10 days before expiry)"
             ;;
           *)
             echo "Usage: $0 <check|rotate> [namespace]"
             echo "  check       : Validate current certificate status and operator start time."
             echo "  rotate      : Trigger immediate certificate rotation and restart the operator."
             echo "  [namespace] : Namespace of the operator (defaults to 'alloydb-omni-system')."
             exit 1 ;;
         esac
         EOF
         chmod +x rotate_cert.sh
         

  2. Run the `rotate_cert.sh` script in `check` mode to inspect the current certificate expiration date, recommended rotation date, and operator in-memory status:
         
         ./rotate_cert.sh check
         

  3. Optional: Back up the `dbs-al-cert-l2-operator` Secret before you rotate the certificate:
         
         kubectl get secret dbs-al-cert-l2-operator -n alloydb-omni-system \
           -o yaml > dbs-al-cert-l2-operator-backup.yaml
         

  4. If the `check` output displays `[WARNING]`, or if the current date is on or before the `Recommended Rotate By` date, run the `rotate_cert.sh` script in `rotate` mode:
         
         ./rotate_cert.sh rotate
         

Confirm that the output ends with `[SUCCESS]` and displays the new certificate serial number, expiration date, and next recommended rotation date. If the output displays `[ERROR]` or the script exits with a non-zero status, rerun `./rotate_cert.sh check` and inspect the operator logs by running `kubectl logs deployment/local-controller-manager -n alloydb-omni-system -c local-manager` (or `-c manager` in operator versions earlier than 1.6.0).

  5. Optional: If you created a backup file in step 3, delete the local backup file after confirming that rotation succeeded because the file contains the old private key:
         
         rm -f dbs-al-cert-l2-operator-backup.yaml
         




### Restore a backed-up certificate

If cert-manager fails to issue a new certificate during rotation and you need to roll back to an unexpired `dbs-al-cert-l2-operator-backup.yaml` file, follow these steps:

  1. Delete the pending or failed `CertificateRequest` resource for the `dbs-al-cert-request-l2-operator` certificate so that cert-manager doesn't reject the restored private key with a `SecretMismatch` reason and overwrite the restored Secret:
         
         REV="$(kubectl get certificate dbs-al-cert-request-l2-operator -n alloydb-omni-system -o jsonpath='{.status.revision}')"
         kubectl delete certificaterequest \
           "dbs-al-cert-request-l2-operator-$((REV + 1))" \
           -n alloydb-omni-system --ignore-not-found
         

  2. Remove the top-level `metadata.resourceVersion` and `metadata.uid` fields from the `dbs-al-cert-l2-operator-backup.yaml` file and apply the Secret by using server-side apply:
         
         grep -vE '^  (resourceVersion|uid):' dbs-al-cert-l2-operator-backup.yaml \
           | kubectl apply --server-side --force-conflicts -f -
         

  3. Restart the `local-controller-manager` Deployment to load the restored certificate into memory:
         
         kubectl rollout restart deployment/local-controller-manager -n alloydb-omni-system
         kubectl rollout status deployment/local-controller-manager -n alloydb-omni-system --timeout=180s
         

  4. Run the `rotate_cert.sh` script in `check` mode to confirm that the `Certificate Serial` value matches the backed-up certificate serial number and that the script reports `[OK]`:
         
         ./rotate_cert.sh check
         

The restored certificate retains its original expiration date, so you must still rotate the certificate on or before the `Recommended Rotate By` date.

  5. Delete the local backup file after you confirm the restore:
         
         rm -f dbs-al-cert-l2-operator-backup.yaml
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 
