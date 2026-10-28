---
url: https://docs.cloud.google.com/multi-party-compute/user-guide/
title: Multi-party Compute User Guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T00:17:52.373366+00:00
---

# Multi-party Compute User Guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/user-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Multi-party Compute User Guide Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide walks through the user journeys of the Multi-party Compute API to manage distributed keys, users, teams, and policies. It is intended for preview customers learning the key user journeys.

## Overview

The MPC API manages the lifecycle of instances, teams, users, key rings, distributed keys, and threshold signing ceremonies, with built-in cryptographic governance enforced across three policy layers:

  * **Administration Policies (Role Quorums)** : _Admins_ onboard _Users_ and _Teams_ , and a quorum of Admins (`EnableUserRole` and `ApproveRoleChange`) is required to grant or revoke the _Admin_ and _Policy Author_ roles. Granting the _Signer_ role takes effect immediately from a single Admin because _Signer_ alone grants no access to existing keys; a _Signer_ only receives key shares when included in a _KeyRing_ 's _KeyPolicy_ during key generation.
  * **Key Policies (`KeyRing.keyPolicy`)**: _Admins_ define a _KeyRing_ 's _KeyPolicy_ when creating the _KeyRing_ , specifying which _Signers_ (_Signer_ , grouped into _Teams_) hold key shares and the K-of-N signer approvals (`CreateTransaction` and `RecordSignerDecision`) required to authorize a signature.
  * **Transaction Policies (`TransactionPolicy` and `KeyList`)**: A quorum of **Policy Authors** (`POLICY_AUTHOR`) proposes, approves, or disables [Cedar](https://docs.cedarpolicy.com/) `permit` and `forbid` rules (`TransactionPolicy`) and `KeyList` address allowlists. Every `CreateTransaction` request is evaluated against active transaction policies (`PERMIT` or `DENY`) before signing.



## Prerequisites

Before starting, ensure you have:

  1. A Google Cloud Project. See [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to make one.
  2. If not using Cloud Shell, the `gcloud` CLI installed and authenticated.
  3. Required APIs enabled, if not already done so. You need two: the MPC API used in this guide, and Cloud Key Management Service if using it for authorization key generation and signing.
         
         gcloud services enable mpc.googleapis.com cloudkms.googleapis.com
         

To view enabled APIs:
         
         gcloud services list --enabled
         

  4. Python 3.9+ and tutorial helper libraries installed:
         
         pip install embit eth-account eth-utils requests
         

  5. (Optional) If your organization authenticates using an external Identity Provider (such as Okta or Microsoft Entra ID) without Google Accounts, see [Configure Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid) to configure Application Default Credentials (ADC) with your federated identity.


**Tip:** We recommend using [**Cloud Shell**](https://console.cloud.google.com/?cloudshell=true) to run the commands in this guide. Cloud Shell comes pre-configured with the Google Cloud SDK (`gcloud`), `openssl`, `jq`, and other tools, and handles authentication automatically. To open Cloud Shell, click the terminal icon in the top navigation bar of the Google Cloud console.**Note:** While the MPC API supports dynamic **K-of-N keyshares** (allowing arbitrary thresholds across teams and users), this guide demonstrates a **2-of-3** signer setup within a single team. Additionally, policies require at least two Policy Authors (a **2-of-2** quorum) to become active, and role changes (`ADMIN` and `POLICY_AUTHOR`) require a **2-of-2** Admin quorum.

## Setup

Update the following variables to populate the commands throughout this guide.

**Important:** If you leave or refresh this page, these input fields may reset to defaults.

### Required Setup

You **must** customize these parameters. The guide won't function with the placeholder values.

> **Note:** **Solo Simulation vs. Multi-user Simulation** : In a realistic environment, this system relies on strict **Separation of Duties** across multiple personas (Administrators, Policy Authors, and Signers), each with a distinct principal, cryptographic authorization key, and IAM permissions. Because the API enforces that each `User` is bound to a unique principal and cannot self-approve role or quorum actions, following this guide end-to-end requires **multiple user accounts**. We plan to add support to simplify single-user testing in a future release. Each `User` principal can be either a Google Cloud email address or a [Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid) principal; this guide uses Google Cloud email examples (such as `alice@example.com`).

Parameter | Value | Description  
---|---|---  
**Project ID** | `my-project` | The consumer project ID for your MPC instance.  
**Instance ID** | `my-mpc-instance` | The ID for your MPC instance (`[a-z]([a-z0-9-]{0,61}[a-z0-9])?`).  
**Location** | `us-central1` | Deployment location (for example, `us-central1`).  
**Admin 1 Principal** | `admin-1@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of the first `ADMIN` user in the instance.  
**Admin 2 Principal** | `admin-2@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of the second `ADMIN` user in the instance.  
**Signer 1 Principal** | `alice@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of Signer 1 (Alice).  
**Signer 2 Principal** | `bob@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of Signer 2 (Bob).  
**Signer 3 Principal** | `charlie@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of Signer 3 (Charlie).  
**Policy Author 1 Principal** | `dave@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of Policy Author 1 (Dave).  
**Policy Author 2 Principal** | `eve@example.com` | Google Cloud email or [BYOID](https://docs.cloud.google.com/multi-party-compute/byoid) principal of Policy Author 2 (Eve).  
  
Authenticate each account once in your terminal session so `gcloud auth print-access-token "<principal>"` can retrieve tokens for any persona without switching accounts mid-tutorial (`ADMIN_1_PRINCIPAL` is authenticated last so it remains the active `gcloud` CLI account for IAM and Cloud KMS commands):
    
    
    for PRINCIPAL in \
      "admin-2@example.com" \
      "alice@example.com" \
      "bob@example.com" \
      "charlie@example.com" \
      "dave@example.com" \
      "eve@example.com" \
      "admin-1@example.com"; do
      gcloud auth login "$PRINCIPAL"
    done
    

### Tutorial Resource Labels

These are local identifiers for the authorization keys created using Cloud KMS during this tutorial. The default values are valid and can be kept to minimize setup friction. Note that resource IDs for `Team`, `User`, `TransactionPolicy`, `KeyRing`, `Key`, `KeyList`, and `Transaction` resources are server-generated and captured into shell variables (`TEAM_NAME`, `SIGNER_1_NAME`, `POLICY_NAME`, `KEY_RING_NAME`, `KEY_NAME`, `KEY_LIST_NAME`, `TRANSACTION_NAME`) when each resource is created.

Parameter | Value | Description  
---|---|---  
**Cloud KMS KeyRing ID** | `mpc-assent-keys` | Cloud Key Management Service KeyRing for external authorization keys stored in Cloud KMS.  
**Cloud KMS Admin 1 ID** | `admin-1` | MPC Admin 1 authorization key label.  
**Cloud KMS Admin 2 ID** | `admin-2` | MPC Admin 2 authorization key label.  
**Cloud KMS Signer 1 ID** | `signer-alice` | MPC Signer 1 authorization key label.  
**Cloud KMS Signer 2 ID** | `signer-bob` | MPC Signer 2 authorization key label.  
**Cloud KMS Signer 3 ID** | `signer-charlie` | MPC Signer 3 authorization key label.  
**Cloud KMS Policy Author 1 ID** | `author-dave` | Policy Author 1 authorization key label.  
**Cloud KMS Policy Author 2 ID** | `author-eve` | Policy Author 2 authorization key label.  
  
* * *

## Step 1: Create an MPC Instance

An MPC `Instance` represents your dedicated, isolated MPC environment. Creating and administering an instance requires the **Multi-party Compute Admin (`roles/mpc.admin`)** IAM role on your project. You create and inspect the `Instance` as an Admin using `MPCInstanceService` on the control plane endpoint (`https://mpc.googleapis.com`), and send all subsequent resource requests to the instance's dedicated data plane URL (`INSTANCE_URL`).

### A. Create the Instance

First, ensure your Admin principals (`admin-1@example.com` and `admin-2@example.com`) have `roles/mpc.admin` on the project, and call `instances.create` (`CreateInstance`) as Admin 1 to provision your MPC instance:

### curl
    
    
    grant_iam_role() {
      local principal=$1
      local iam_role=$2
      local member="user:${principal}"
    
      # BYOID principals already start with "principal://"
      if [[ "$principal" == principal://* ]]; then
        member="${principal}"
      fi
    
      echo "Granting ${iam_role} to ${member}..."
      gcloud projects add-iam-policy-binding "my-project" \
        --member="${member}" \
        --role="${iam_role}" \
        --condition=None > /dev/null
    }
    
    for ADMIN_PRINCIPAL in "admin-1@example.com" "admin-2@example.com"; do
      grant_iam_role "$ADMIN_PRINCIPAL" "roles/mpc.admin"
    done
    
    export INSTANCE_NAME="projects/my-project/locations/us-central1/instances/my-mpc-instance"
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "https://mpc.googleapis.com/v1beta/${INSTANCE_NAME}"; then
      echo "Instance 'my-mpc-instance' already exists. Skipping creation."
    else
      echo "Instance 'my-mpc-instance' not found. Creating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "displayName": "Tutorial MPC Instance"
        }' \
        "https://mpc.googleapis.com/v1beta/projects/my-project/locations/us-central1/instances?instanceId=my-mpc-instance" | jq
    fi
    

This returns a long-running operation (LRO). You must wait for the Instance `state` to become `ACTIVE` before calling its data plane URL.

#### 🕵️‍♂️ Check Instance State (Polling)

Poll the instance status until `state` becomes `ACTIVE`, and save its `url` field to `INSTANCE_URL`:

### curl
    
    
    INSTANCE_INFO=$(curl -s -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "https://mpc.googleapis.com/v1beta/${INSTANCE_NAME}")
    
    echo "$INSTANCE_INFO" | jq
    export INSTANCE_URL=$(echo "$INSTANCE_INFO" | jq -r '.url')
    echo "Instance Data Plane URL: $INSTANCE_URL"
    

* * *

## Step 2: Generate Authorization Keys

To use the MPC API, you must generate keypairs for the following distinct roles. Note that these are **external cryptographic authorization keys** (`User.authorizationKey`), meaning you generate and custody them outside the MPC instance, and therefore they are distinct from the MPC key shares generated during key creation:

  * **Admins** : Authorize changes to `ADMIN` and `POLICY_AUTHOR` user roles, and create `Key`s.
  * **Policy Authors** : Authorize governance policies (`TransactionPolicy`).
  * **Signers** : Provide authorization (`AUTHORIZE` or `DENY`) on transactions.



Generate the `secp256k1` cryptographic authorization keys for your Signers, Policy Authors, and Admins. These commands are idempotent.

### Cloud KMS

We recommend managing authorization keys in Cloud Key Management Service. Ensure your identity has permissions to create key rings, create keys, sign, and view public key verifiers (such as `roles/cloudkms.admin` and `roles/cloudkms.signerVerifier`). Ensure you have a `KeyRing` created, then generate a `secp256k1` key for each Signer, Policy Author, and Admin.
    
    
    provision_keyring() {
      if gcloud kms keyrings describe "mpc-assent-keys" --location="us-central1" > /dev/null 2>&1; then
        echo "KeyRing 'mpc-assent-keys' already exists."
      else
        echo "KeyRing 'mpc-assent-keys' not found. Creating it..."
        gcloud kms keyrings create "mpc-assent-keys" --location="us-central1"
      fi
    }
    
    provision_kms_key() {
      local id=$1
      if gcloud kms keys describe "${id}-key" --keyring="mpc-assent-keys" --location="us-central1" > /dev/null 2>&1; then
        echo "KMS key '${id}-key' already exists."
      else
        echo "KMS key '${id}-key' not found. Creating it..."
        gcloud kms keys create "${id}-key" \
          --keyring="mpc-assent-keys" \
          --location="us-central1" \
          --purpose=asymmetric-signing \
          --default-algorithm=ec-sign-secp256k1-sha256 \
          --protection-level=hsm
      fi
    
      gcloud kms keys versions get-public-key 1 \
        --key="${id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --output-file="${id}_pub.pem"
    
      echo "Retrieved public key from KMS and saved to ${id}_pub.pem:"
      cat "${id}_pub.pem"
    }
    
    # Run Setup
    provision_keyring
    
    # Generate Keys for Signers, Policy Authors, and Admins
    for ID in \
      signer-alice \
      signer-bob \
      signer-charlie \
      author-dave \
      author-eve \
      admin-1 \
      admin-2; do
      echo "Generating KMS key for $ID..."
      provision_kms_key "$ID"
    done
    

### OpenSSL

You can use standard OpenSSL to generate `secp256k1` keys for each Signer, Policy Author, and Admin.
    
    
    provision_openssl_key() {
      local id=$1
      if [[ ! -f "${id}_priv.pem" ]]; then
        openssl ecparam -name secp256k1 -genkey -noout -out "${id}_priv.pem"
        openssl ec -in "${id}_priv.pem" -pubout -out "${id}_pub.pem"
        echo "Wrote private key to ${id}_priv.pem and public key to ${id}_pub.pem:"
        cat "${id}_pub.pem"
      else
        echo "Private key file '${id}_priv.pem' already exists. Skipping OpenSSL generation."
        echo "Using existing public key from '${id}_pub.pem':"
        cat "${id}_pub.pem"
      fi
    }
    
    for ID in \
      signer-alice \
      signer-bob \
      signer-charlie \
      author-dave \
      author-eve \
      admin-1 \
      admin-2; do
      echo "Generating OpenSSL key for $ID..."
      provision_openssl_key "$ID"
    done
    

* * *

## Step 3: Register Teams and Users

Before any entity can participate in transaction signing (as a `SIGNER`) or policy authoring (as a `POLICY_AUTHOR`), they must be granted IAM permissions on the project and registered as an application-level `User` in the instance (see [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization) for how IAM roles and `User` roles work together).

Registration requires out-of-band coordination between the **Administrator** and the **User** :

  1. **The Entity** (Signer or Policy Author) generates their key pair locally and transfers their **Public Key** to the Administrator securely.
  2. **The Administrator** grants the User's principal the appropriate IAM role on the project (`roles/mpc.editor` for Signers and Policy Authors; `roles/mpc.admin` for Admins) and calls the MPC API to register the User's `principal` and `authorizationKey`.

**Note:** A future preview release will replace this out-of-band key handoff with an in-band **Invite Flow** , where Administrators invite Users by principal and each User logs in to register their own `authorizationKey` directly to complete onboarding.

### A. Create a Signer Team

Every `User` with the `SIGNER` role must belong to a `Team`, and all other `User`s with other roles cannot belong to a `Team`. As Admin 1 (`admin-1@example.com`), create a "Treasury Signers" `Team` (`CreateTeam`) to hold your three signers and capture its server-generated resource `name`:

### curl
    
    
    TEAM_RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "displayName": "Treasury Signers",
      }' \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/teams?requestId=11111111-1111-4111-8111-111111111101")
    
    echo "$TEAM_RESPONSE" | jq
    export TEAM_NAME=$(echo "$TEAM_RESPONSE" | jq -r '.name')
    echo "Created Team: $TEAM_NAME"
    

### B. Grant IAM Roles and Register Signers and Policy Authors

Each user requires both a project-level IAM role (`roles/mpc.editor` for Signers and Policy Authors, and `roles/mpc.admin` for Admins) to call the MPC API and an application-level `User` resource inside the instance. When calling [`users.create`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/create) (`CreateUser`), the `roles` field can only be empty or `["SIGNER"]`:

  * **Signers** : Granted `roles/mpc.editor` in IAM and created with `roles: ["SIGNER"]` and `team: "$TEAM_NAME"`. The `SIGNER` role becomes `ACTIVE` immediately without requiring Admin quorum approval, because having the `SIGNER` role alone does not grant access to any existing keys; a Signer only receives key shares when included in a `KeyRing`'s `KeyPolicy` during key generation.
  * **Policy Authors** : Granted `roles/mpc.editor` in IAM and created with no initial roles and no `team`, then granted the `POLICY_AUTHOR` role in Step 3.C using Admin quorum approval (since `POLICY_AUTHOR` and `ADMIN` have instance-wide governance authority).




### curl
    
    
    provision_user() {
      local id=$1
      local display_name=$2
      local principal=$3
      local request_id=$4
      local team=$5
      local pubkey_b64
      local signer_fields=""
    
      # 1. Grant project-level IAM permission (roles/mpc.editor) to the User's principal
      grant_iam_role "$principal" "roles/mpc.editor" >&2
    
      # 2. Read the public key from the file generated in Step 2 (Base64-encoded PEM/DER bytes)
      pubkey_b64=$(openssl base64 -A -in "${id}_pub.pem")
    
      if [[ -n "$team" ]]; then
        signer_fields=", \"roles\": [\"SIGNER\"], \"team\": \"${team}\""
      fi
    
      # 3. Register the application-level User in the MPC instance as Admin 1
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"displayName\": \"${display_name}\",
          \"principal\": \"${principal}\",
          \"authorizationKey\": {
            \"publicKey\": \"${pubkey_b64}\",
            \"algorithm\": \"PUBLIC_KEY_SIGNATURE_ALGORITHM_ECDSA_SECP256K1\"
          }${signer_fields}
        }" \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/users?requestId=${request_id}"
    }
    
    echo "Registering Signers..."
    export SIGNER_1_NAME=$(provision_user "signer-alice" "Signer Alice" "alice@example.com" "11111111-1111-4111-8111-111111111001" "${TEAM_NAME}" | tee /dev/stderr | jq -r '.name')
    export SIGNER_2_NAME=$(provision_user "signer-bob" "Signer Bob" "bob@example.com" "11111111-1111-4111-8111-111111111002" "${TEAM_NAME}" | tee /dev/stderr | jq -r '.name')
    export SIGNER_3_NAME=$(provision_user "signer-charlie" "Signer Charlie" "charlie@example.com" "11111111-1111-4111-8111-111111111003" "${TEAM_NAME}" | tee /dev/stderr | jq -r '.name')
    
    echo "Registering Policy Authors..."
    export POLICY_AUTHOR_1_NAME=$(provision_user "author-dave" "Author Dave" "dave@example.com" "11111111-1111-4111-8111-111111111004" | tee /dev/stderr | jq -r '.name')
    export POLICY_AUTHOR_2_NAME=$(provision_user "author-eve" "Author Eve" "eve@example.com" "11111111-1111-4111-8111-111111111005" | tee /dev/stderr | jq -r '.name')
    

### C. Grant the Policy Author Role (Admin Quorum Approval)

Enabling or disabling the `POLICY_AUTHOR` or `ADMIN` role on a `User` requires a quorum of Admins:

  1. **Admin 1** calls [`users.enableRole`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/enableRole) (`EnableUserRole`), which moves the role to `PENDING_ACTIVE` and records Admin 1's signature as the first approval.
  2. **Admin 2** calls [`users.approveRoleChange`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/approveRoleChange) (`ApproveRoleChange`) with their signature, transitioning the role to `ACTIVE`.

**Important:** **User Role Signature Structure (`UserSigningPayload`)**: Each Admin signs a serialized `google.cloud.mpc.v1beta.UserSigningPayload` protobuf message (`instance = 1`, `principal = 2`, `authorization_key = 3`, `role_changes = 4` with `role = 1`, `action = 2`, `version = 3`) and passes both `"signature"` and `"signedPayload"` in `authorizationInfo`. A `User` cannot request or approve their own role change (`PERMISSION_DENIED`).

### Cloud KMS

**1\. Request`POLICY_AUTHOR` as Admin 1 (`EnableUserRole`)**
    
    
    sign_role_change() {
      local admin_id=$1
      local target_id=$2
      local principal=$3
      python3 -c 'import sys; inst, prin, pub = sys.argv[1], sys.argv[2], open(sys.argv[3], "rb").read(); v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("role_payload.bin", "wb").write(f(1, inst.encode()) + f(2, prin.encode()) + f(3, f(1, pub) + b"\x10\x01") + f(4, b"\x08\x02\x10\x01\x18\x01"))' "${INSTANCE_NAME}" "${principal}" "${target_id}_pub.pem"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${admin_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=role_payload.bin \
        --signature-file=role_sig.bin > /dev/null
      openssl base64 -A -in role_sig.bin
    }
    
    enable_policy_author() {
      local target_user=$1
      local target_id=$2
      local target_principal=$3
    
      echo "Admin 1 requesting POLICY_AUTHOR for ${target_user}..."
      local admin_1_sig=$(sign_role_change "admin-1" "${target_id}" "${target_principal}")
      local signed_payload_b64=$(openssl base64 -A -in role_payload.bin)
    
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"role\": \"POLICY_AUTHOR\",
          \"authorizationInfo\": {
            \"signature\": \"${admin_1_sig}\",
            \"signedPayload\": \"${signed_payload_b64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${target_user}:enableRole" | jq
    }
    
    enable_policy_author "${POLICY_AUTHOR_1_NAME}" "author-dave" "dave@example.com"
    enable_policy_author "${POLICY_AUTHOR_2_NAME}" "author-eve" "eve@example.com"
    

**2\. Approve`POLICY_AUTHOR` as Admin 2 (`ApproveRoleChange`)**
    
    
    approve_policy_author() {
      local target_user=$1
      local target_id=$2
      local target_principal=$3
    
      echo "Admin 2 approving POLICY_AUTHOR for ${target_user}..."
      local admin_2_sig=$(sign_role_change "admin-2" "${target_id}" "${target_principal}")
      local signed_payload_b64=$(openssl base64 -A -in role_payload.bin)
    
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-2@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"authorizationInfo\": {
            \"signature\": \"${admin_2_sig}\",
            \"signedPayload\": \"${signed_payload_b64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${target_user}:approveRoleChange" | jq
    }
    
    approve_policy_author "${POLICY_AUTHOR_1_NAME}" "author-dave" "dave@example.com"
    approve_policy_author "${POLICY_AUTHOR_2_NAME}" "author-eve" "eve@example.com"
    

### OpenSSL

**1\. Request`POLICY_AUTHOR` as Admin 1 (`EnableUserRole`)**
    
    
    sign_role_change() {
      local admin_id=$1
      local target_id=$2
      local principal=$3
      python3 -c 'import sys; inst, prin, pub = sys.argv[1], sys.argv[2], open(sys.argv[3], "rb").read(); v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("role_payload.bin", "wb").write(f(1, inst.encode()) + f(2, prin.encode()) + f(3, f(1, pub) + b"\x10\x01") + f(4, b"\x08\x02\x10\x01\x18\x01"))' "${INSTANCE_NAME}" "${principal}" "${target_id}_pub.pem"
      openssl dgst -sha256 -sign "${admin_id}_priv.pem" -out role_sig.bin role_payload.bin
      openssl base64 -A -in role_sig.bin
    }
    
    enable_policy_author() {
      local target_user=$1
      local target_id=$2
      local target_principal=$3
    
      echo "Admin 1 requesting POLICY_AUTHOR for ${target_user}..."
      local admin_1_sig=$(sign_role_change "admin-1" "${target_id}" "${target_principal}")
      local signed_payload_b64=$(openssl base64 -A -in role_payload.bin)
    
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"role\": \"POLICY_AUTHOR\",
          \"authorizationInfo\": {
            \"signature\": \"${admin_1_sig}\",
            \"signedPayload\": \"${signed_payload_b64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${target_user}:enableRole" | jq
    }
    
    enable_policy_author "${POLICY_AUTHOR_1_NAME}" "author-dave" "dave@example.com"
    enable_policy_author "${POLICY_AUTHOR_2_NAME}" "author-eve" "eve@example.com"
    

**2\. Approve`POLICY_AUTHOR` as Admin 2 (`ApproveRoleChange`)**
    
    
    approve_policy_author() {
      local target_user=$1
      local target_id=$2
      local target_principal=$3
    
      echo "Admin 2 approving POLICY_AUTHOR for ${target_user}..."
      local admin_2_sig=$(sign_role_change "admin-2" "${target_id}" "${target_principal}")
      local signed_payload_b64=$(openssl base64 -A -in role_payload.bin)
    
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-2@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"authorizationInfo\": {
            \"signature\": \"${admin_2_sig}\",
            \"signedPayload\": \"${signed_payload_b64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${target_user}:approveRoleChange" | jq
    }
    
    approve_policy_author "${POLICY_AUTHOR_1_NAME}" "author-dave" "dave@example.com"
    approve_policy_author "${POLICY_AUTHOR_2_NAME}" "author-eve" "eve@example.com"
    

* * *

## Step 4: Configure Transaction Policies

Configure transaction policies by creating and approving a `TransactionPolicy` (and optionally a `KeyList`).

### A. Create a Policy (PENDING_ACTIVE)

Create a Cedar policy rule describing what transactions are permitted. While you can configure many policies to govern different scenarios, this guide demonstrates setting up a policy for either Ethereum or Bitcoin transactions. By default, transaction policy evaluation is **Fail-Fast (Block by Default)** ; if no active `permit` policy matches a transaction, the policy evaluation decision is `DENY`. For full details on Cedar attributes, see [Write transaction policy rules](https://docs.cloud.google.com/multi-party-compute/writing-rules).

**Important:** **Quorum Signature Structure (`TransactionPolicySigningPayload`)**: Before creating, approving, or disabling a policy, a `User` with an active `POLICY_AUTHOR` role signs a serialized `google.cloud.mpc.v1beta.TransactionPolicySigningPayload` protobuf message: `instance = 1` (for `CreateTransactionPolicy`) or `transaction_policy = 2` (for `ApproveTransactionPolicy` and `DisableTransactionPolicy`), `action = 3` (`ACTIVATE = 1` or `DISABLE = 2`), and `rule = 4` (`cedar_document = 1`). The `cedar_document` string in the signed payload MUST match `transactionPolicy.rule.cedarDocument` in the API request byte-for-byte, otherwise signature verification fails.

### Ethereum, KMS

This rule permits smaller Ethereum transfers (`<= 2 ETH`, represented as `2,000,000,000` in units of 10-9 ETH / Gwei) to a specific recipient address (`0x1111111111111111111111111111111111111111`).
    
    
    permit (principal, action, resource)
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context.secondary_key == "0x1111111111111111111111111111111111111111" &&
      context has amount_token_scaled &&
      context.amount_token_scaled <= 2000000000
    };
    
    
    
    sign_policy() {
      local author_id=$1
      local resource_type=$2
      local resource_name=$3
      local action=$4
      local cedar_doc=$5
      python3 -c 'import sys; rt, rn, act, doc = sys.argv[1:]; v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("policy_payload.bin", "wb").write(f(1 if rt == "instance" else 2, rn.encode()) + bytes([24, 1 if act == "ACTIVATE" else 2]) + f(4, f(1, doc.encode())))' "${resource_type}" "${resource_name}" "${action}" "${cedar_doc}"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${author_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=policy_payload.bin \
        --signature-file=policy_sig.bin > /dev/null
      openssl base64 -A -in policy_sig.bin
    }
    
    export CEDAR_RULE='permit (principal, action, resource) when { context.schema == "ETHEREUM_TX_V2" && context.secondary_key == "0x1111111111111111111111111111111111111111" && context has amount_token_scaled && context.amount_token_scaled <= 2000000000 };'
    
    # Sign as Policy Author 1
    QUORUM_SIGNATURE=$(sign_policy "author-dave" "instance" "${INSTANCE_NAME}" "ACTIVATE" "${CEDAR_RULE}")
    POLICY_PAYLOAD_B64=$(openssl base64 -A -in policy_payload.bin)
    
    POLICY_RESPONSE=$(jq -n \
      --arg rule "$CEDAR_RULE" \
      --arg sig "$QUORUM_SIGNATURE" \
      --arg payload "$POLICY_PAYLOAD_B64" \
      '{
        transactionPolicy: {
          displayName: "Ethereum Transfer Permit Policy",
          rule: {cedarDocument: $rule}
        },
        authorizationInfo: {
          signature: $sig,
          signedPayload: $payload
        },
        requestId: "11111111-1111-4111-8111-111111111201"
      }' \
    | curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "dave@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d @- \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/transactionPolicies")
    
    echo "$POLICY_RESPONSE" | jq
    export POLICY_NAME=$(echo "$POLICY_RESPONSE" | jq -r '.name')
    

### Ethereum, OpenSSL

This rule permits smaller Ethereum transfers (`<= 2 ETH`, represented as `2,000,000,000` in units of 10-9 ETH / Gwei) to a specific recipient address (`0x1111111111111111111111111111111111111111`).
    
    
    permit (principal, action, resource)
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context.secondary_key == "0x1111111111111111111111111111111111111111" &&
      context has amount_token_scaled &&
      context.amount_token_scaled <= 2000000000
    };
    
    
    
    sign_policy() {
      local author_id=$1
      local resource_type=$2
      local resource_name=$3
      local action=$4
      local cedar_doc=$5
      python3 -c 'import sys; rt, rn, act, doc = sys.argv[1:]; v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("policy_payload.bin", "wb").write(f(1 if rt == "instance" else 2, rn.encode()) + bytes([24, 1 if act == "ACTIVATE" else 2]) + f(4, f(1, doc.encode())))' "${resource_type}" "${resource_name}" "${action}" "${cedar_doc}"
      openssl dgst -sha256 -sign "${author_id}_priv.pem" -out policy_sig.bin policy_payload.bin
      openssl base64 -A -in policy_sig.bin
    }
    
    export CEDAR_RULE='permit (principal, action, resource) when { context.schema == "ETHEREUM_TX_V2" && context.secondary_key == "0x1111111111111111111111111111111111111111" && context has amount_token_scaled && context.amount_token_scaled <= 2000000000 };'
    
    # Sign as Policy Author 1
    QUORUM_SIGNATURE=$(sign_policy "author-dave" "instance" "${INSTANCE_NAME}" "ACTIVATE" "${CEDAR_RULE}")
    POLICY_PAYLOAD_B64=$(openssl base64 -A -in policy_payload.bin)
    
    POLICY_RESPONSE=$(jq -n \
      --arg rule "$CEDAR_RULE" \
      --arg sig "$QUORUM_SIGNATURE" \
      --arg payload "$POLICY_PAYLOAD_B64" \
      '{
        transactionPolicy: {
          displayName: "Ethereum Transfer Permit Policy",
          rule: {cedarDocument: $rule}
        },
        authorizationInfo: {
          signature: $sig,
          signedPayload: $payload
        },
        requestId: "11111111-1111-4111-8111-111111111201"
      }' \
    | curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "dave@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d @- \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/transactionPolicies")
    
    echo "$POLICY_RESPONSE" | jq
    export POLICY_NAME=$(echo "$POLICY_RESPONSE" | jq -r '.name')
    

### Bitcoin, KMS

This rule permits Bitcoin transfers using the `BITCOIN_TX_V2` schema (BIP 174 PSBT v0) where the net outbound transfer amount does not exceed 250,000 satoshis (`context.amount_token_scaled <= 2500000`, or 0.0025 BTC normalized to 10-9 fixed decimal units) and the miner fee does not exceed 10,000 satoshis (`context.max_fee_atomic <= 100000`).
    
    
    permit (principal, action, resource)
    when {
      context.schema == "BITCOIN_TX_V2" &&
      context has amount_token_scaled &&
      context.amount_token_scaled <= 2500000 &&
      context.max_fee_atomic <= 100000
    };
    
    
    
    sign_policy() {
      local author_id=$1
      local resource_type=$2
      local resource_name=$3
      local action=$4
      local cedar_doc=$5
      python3 -c 'import sys; rt, rn, act, doc = sys.argv[1:]; v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("policy_payload.bin", "wb").write(f(1 if rt == "instance" else 2, rn.encode()) + bytes([24, 1 if act == "ACTIVATE" else 2]) + f(4, f(1, doc.encode())))' "${resource_type}" "${resource_name}" "${action}" "${cedar_doc}"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${author_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=policy_payload.bin \
        --signature-file=policy_sig.bin > /dev/null
      openssl base64 -A -in policy_sig.bin
    }
    
    export CEDAR_RULE='permit (principal, action, resource) when { context.schema == "BITCOIN_TX_V2" && context has amount_token_scaled && context.amount_token_scaled <= 2500000 && context.max_fee_atomic <= 100000 };'
    
    # Sign as Policy Author 1
    QUORUM_SIGNATURE=$(sign_policy "author-dave" "instance" "${INSTANCE_NAME}" "ACTIVATE" "${CEDAR_RULE}")
    POLICY_PAYLOAD_B64=$(openssl base64 -A -in policy_payload.bin)
    
    POLICY_RESPONSE=$(jq -n \
      --arg rule "$CEDAR_RULE" \
      --arg sig "$QUORUM_SIGNATURE" \
      --arg payload "$POLICY_PAYLOAD_B64" \
      '{
        transactionPolicy: {
          displayName: "Bitcoin PSBT Permit Policy",
          rule: {cedarDocument: $rule}
        },
        authorizationInfo: {
          signature: $sig,
          signedPayload: $payload
        },
        requestId: "11111111-1111-4111-8111-111111111202"
      }' \
    | curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "dave@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d @- \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/transactionPolicies")
    
    echo "$POLICY_RESPONSE" | jq
    export POLICY_NAME=$(echo "$POLICY_RESPONSE" | jq -r '.name')
    

### Bitcoin, OpenSSL

This rule permits Bitcoin transfers using the `BITCOIN_TX_V2` schema (BIP 174 PSBT v0) where the net outbound transfer amount does not exceed 250,000 satoshis (`context.amount_token_scaled <= 2500000`, or 0.0025 BTC normalized to 10-9 fixed decimal units) and the miner fee does not exceed 10,000 satoshis (`context.max_fee_atomic <= 100000`).
    
    
    permit (principal, action, resource)
    when {
      context.schema == "BITCOIN_TX_V2" &&
      context has amount_token_scaled &&
      context.amount_token_scaled <= 2500000 &&
      context.max_fee_atomic <= 100000
    };
    
    
    
    sign_policy() {
      local author_id=$1
      local resource_type=$2
      local resource_name=$3
      local action=$4
      local cedar_doc=$5
      python3 -c 'import sys; rt, rn, act, doc = sys.argv[1:]; v = lambda n: bytes([n & 127 | 128]) + v(n >> 7) if n > 127 else bytes([n]); f = lambda k, b: bytes([k << 3 | 2]) + v(len(b)) + b; open("policy_payload.bin", "wb").write(f(1 if rt == "instance" else 2, rn.encode()) + bytes([24, 1 if act == "ACTIVATE" else 2]) + f(4, f(1, doc.encode())))' "${resource_type}" "${resource_name}" "${action}" "${cedar_doc}"
      openssl dgst -sha256 -sign "${author_id}_priv.pem" -out policy_sig.bin policy_payload.bin
      openssl base64 -A -in policy_sig.bin
    }
    
    export CEDAR_RULE='permit (principal, action, resource) when { context.schema == "BITCOIN_TX_V2" && context has amount_token_scaled && context.amount_token_scaled <= 2500000 && context.max_fee_atomic <= 100000 };'
    
    # Sign as Policy Author 1
    QUORUM_SIGNATURE=$(sign_policy "author-dave" "instance" "${INSTANCE_NAME}" "ACTIVATE" "${CEDAR_RULE}")
    POLICY_PAYLOAD_B64=$(openssl base64 -A -in policy_payload.bin)
    
    POLICY_RESPONSE=$(jq -n \
      --arg rule "$CEDAR_RULE" \
      --arg sig "$QUORUM_SIGNATURE" \
      --arg payload "$POLICY_PAYLOAD_B64" \
      '{
        transactionPolicy: {
          displayName: "Bitcoin PSBT Permit Policy",
          rule: {cedarDocument: $rule}
        },
        authorizationInfo: {
          signature: $sig,
          signedPayload: $payload
        },
        requestId: "11111111-1111-4111-8111-111111111202"
      }' \
    | curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "dave@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d @- \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/transactionPolicies")
    
    echo "$POLICY_RESPONSE" | jq
    export POLICY_NAME=$(echo "$POLICY_RESPONSE" | jq -r '.name')
    

### B. Approve Policy (Transition to ACTIVE)

Policy changes require 2-of-2 signatures, and therefore a second Policy Author must call [`transactionPolicies.approve`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/approve) (`ApproveTransactionPolicy`) with a signed `TransactionPolicySigningPayload`.

### Ethereum
    
    
    # 1. Check the policy state
    POLICY_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth print-access-token "eve@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${POLICY_NAME}")
    
    POLICY_STATE=$(echo "$POLICY_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$POLICY_STATE" == "PENDING_ACTIVE" ]; then
      # 2. Sign as Policy Author 2 naming transaction_policy ($POLICY_NAME)
      QUORUM_SIGNATURE_2=$(sign_policy "author-eve" "transaction_policy" "${POLICY_NAME}" "ACTIVATE" "${CEDAR_RULE}")
      POLICY_PAYLOAD_2_B64=$(openssl base64 -A -in policy_payload.bin)
    
      # 3. Call ApproveTransactionPolicy as Policy Author 2
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "eve@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"authorizationInfo\": {
            \"signature\": \"${QUORUM_SIGNATURE_2}\",
            \"signedPayload\": \"${POLICY_PAYLOAD_2_B64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${POLICY_NAME}:approve" | jq
    elif [ "$POLICY_STATE" == "ACTIVE" ]; then
      echo "Policy '${POLICY_NAME}' is already ACTIVE. Skipping approval."
    else
      echo "Policy '${POLICY_NAME}' is in an unexpected state: $POLICY_STATE"
    fi
    

### Bitcoin
    
    
    # 1. Check the policy state
    POLICY_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth print-access-token "eve@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${POLICY_NAME}")
    
    POLICY_STATE=$(echo "$POLICY_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$POLICY_STATE" == "PENDING_ACTIVE" ]; then
      # 2. Sign as Policy Author 2 naming transaction_policy ($POLICY_NAME)
      QUORUM_SIGNATURE_2=$(sign_policy "author-eve" "transaction_policy" "${POLICY_NAME}" "ACTIVATE" "${CEDAR_RULE}")
      POLICY_PAYLOAD_2_B64=$(openssl base64 -A -in policy_payload.bin)
    
      # 3. Call ApproveTransactionPolicy as Policy Author 2
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "eve@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"authorizationInfo\": {
            \"signature\": \"${QUORUM_SIGNATURE_2}\",
            \"signedPayload\": \"${POLICY_PAYLOAD_2_B64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${POLICY_NAME}:approve" | jq
    elif [ "$POLICY_STATE" == "ACTIVE" ]; then
      echo "Policy '${POLICY_NAME}' is already ACTIVE. Skipping approval."
    else
      echo "Policy '${POLICY_NAME}' is in an unexpected state: $POLICY_STATE"
    fi
    

### C. Create and Manage a KeyList (Optional)

A `KeyList` (`KeyListService`) is a named list of blockchain addresses (`manualEntry`, MPC `key`, or `keyRing`) that policies can reference as trusted destinations. Admins (`ADMIN`) can create a `KeyList` with [`keyLists.create`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/create) and update its entries at any time with [`keyLists.addEntries`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/addEntries) and [`keyLists.removeEntries`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/removeEntries):

### curl
    
    
    KEY_LIST_RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "displayName": "Approved Destinations",
        "description": "Trusted recipient addresses",
        "entries": [
          {
            "manualEntry": {
              "address": "0x1111111111111111111111111111111111111111",
              "source": "Treasury onboarding",
              "reason": "Approved recipient address"
            }
          }
        ]
      }' \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/keyLists?requestId=11111111-1111-4111-8111-111111111301")
    
    echo "$KEY_LIST_RESPONSE" | jq
    export KEY_LIST_NAME=$(echo "$KEY_LIST_RESPONSE" | jq -r '.name')
    

* * *

## Step 5: Create a Key

As Admin 1 (`admin-1@example.com`), create a `KeyRing` with an inline `KeyPolicy` and generate a distributed MPC key.

### A. Create KeyRing with an inline KeyPolicy

A `KeyRing` is a logical grouping for your MPC keys and defines an immutable inline `KeyPolicy` (`keyRing.keyPolicy`) that every key created in the `KeyRing` follows. A `KeyPolicy` is a tree of threshold rules (`PolicyNode`) whose child `subKeyShares` can be `teamNode` (`threshold` of `totalMembers` in a `Team`), `userNode` (a specific `SIGNER` `User`), or a nested `policyNode`.

Here we configure a **2-of-3** threshold rule over the three signers in `${TEAM_NAME}` (`threshold: 2`, `totalMembers: 3`, stored in `GCP_TEE`):

### curl
    
    
    KEY_RING_RESPONSE=$(jq -n \
      --arg team "${TEAM_NAME}" \
      '{
        displayName: "Treasury KeyRing",
        keyPolicy: {
          policy: {
            policyNodeId: "treasury-2-of-3",
            threshold: 1,
            subKeyShares: [
              {
                teamNode: {
                  team: $team,
                  threshold: 2,
                  totalMembers: 3,
                  storageInfo: {storageType: "GCP_TEE"}
                }
              }
            ]
          }
        }
      }' \
    | curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d @- \
        "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/keyRings?requestId=11111111-1111-4111-8111-111111111401")
    
    echo "$KEY_RING_RESPONSE" | jq
    export KEY_RING_NAME=$(echo "$KEY_RING_RESPONSE" | jq -r '.name')
    echo "Created KeyRing: $KEY_RING_NAME"
    

### B. Generate Distributed Key (DKG)

Call [`keys.create`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/create) (`CreateKey`) as Admin 1 to run Distributed Key Generation (DKG) across the participants selected by your `KeyRing`'s `KeyPolicy`.

`CreateKey` is synchronous and returns the `ACTIVE` `Key` resource, including `publicKeyInfo.publicKey` and server-derived `publicKeyInfo.blockchainAddresses` (`EC_SIGN_SECP256K1` for Ethereum and Bitcoin, or `EC_SIGN_ED25519` for Solana once it is supported):

### curl
    
    
    KEY_RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "algorithm": "EC_SIGN_SECP256K1"
      }' \
      "${INSTANCE_URL}/v1beta/${KEY_RING_NAME}/keys?requestId=11111111-1111-4111-8111-111111111501")
    
    echo "$KEY_RESPONSE" | jq
    export KEY_NAME=$(echo "$KEY_RESPONSE" | jq -r '.name')
    export PUBLIC_KEY_B64=$(echo "$KEY_RESPONSE" | jq -r '.publicKeyInfo.publicKey')
    

### C. Derive Blockchain Address & Locate UTXOs

When `CreateKey` completes, `publicKeyInfo.blockchainAddresses` in the response automatically includes derived addresses (`secp256k1Addresses.ethereumAddress` and `secp256k1Addresses.bitcoinMainnetAddresses` for `EC_SIGN_SECP256K1`, or `ed25519Addresses.solanaAddress` for `EC_SIGN_ED25519`). You can also independently verify or derive Testnet addresses and locking scripts from the 65-byte uncompressed public key (`0x04 || X || Y`) using the following scripts, and locate any unspent funds needed for transactions.

### Ethereum

Ethereum addresses are returned in `.publicKeyInfo.blockchainAddresses.secp256k1Addresses.ethereumAddress` and can also be derived from the Keccak-256 hash of the 64-byte uncompressed public key point (`pub_bytes[1:]`), taking the last 20 bytes.

#### Address Derivation Script (`derive_address.py`)

Execute the following block to create and run `derive_address.py`:
    
    
    cat <<'EOF' > derive_address.py
    import base64
    from eth_utils import keccak, to_checksum_address
    
    # Insert your base64 publicKey from Step 5.B
    PUBLIC_KEY_B64 = "your-public-key"
    
    pub_bytes = base64.b64decode(PUBLIC_KEY_B64)
    if len(pub_bytes) == 65 and pub_bytes[0] == 4:
        raw_addr = "0x" + keccak(pub_bytes[1:])[-20:].hex()
        checksummed_addr = to_checksum_address(raw_addr)
        print("Ethereum Address:", checksummed_addr)
    else:
        print(f"Error: Expected 65-byte uncompressed key, got {len(pub_bytes)} bytes.")
    EOF
    python3 derive_address.py
    

#### Fund the Ethereum Address

Before broadcasting in Step 7, ensure your derived Ethereum address has enough Sepolia testnet ETH to cover the transaction value and gas costs. You can request free testnet ETH by entering your newly derived address into the [Faucet for Ethereum Sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia).

### Bitcoin

Bitcoin Mainnet addresses (`p2wpkhAddress`, `p2shP2wpkhAddress`, and `p2pkhAddress`) are returned in `.publicKeyInfo.blockchainAddresses.secp256k1Addresses.bitcoinMainnetAddresses`. From the uncompressed 65-byte `secp256k1` EC public key (`0x04 || X || Y`), you can also derive the 33-byte compressed public key, locking scripts, and Testnet4 addresses across all three formats:

  1. **Native SegWit (P2WPKH / BIP 173)** : Bech32 address (`bc1q...` on Mainnet, `tb1q...` on Testnet4) with a 22-byte witness `scriptPubKey` (`0014<hash160>`). This is the recommended modern format with lowest transaction fees.
  2. **Nested SegWit (P2SH-P2WPKH / BIP 49)** : Wrapped SegWit address (`3...` on Mainnet, `2...` on Testnet4) with a 23-byte `scriptPubKey` (`a914<hash160>87`) and a 22-byte redeemScript (`0014<hash160>`), compatible with legacy systems.
  3. **Legacy (P2PKH / BIP 44)** : Original Pay-to-PubKey-Hash Base58 address (`1...` on Mainnet, `m/n...` on Testnet4) with a 25-byte `scriptPubKey` (`76a914<hash160>88ac`).



#### Address Derivation Script (`derive_btc_address.py`)

Execute the following block to create and run `derive_btc_address.py`:
    
    
    cat <<'EOF' > derive_btc_address.py
    """Derives Bitcoin addresses (Native SegWit, Nested SegWit, Legacy) from an MPC public key using embit."""
    
    import base64
    from embit import ec, script
    from embit.networks import NETWORKS
    
    # Insert the Base64-encoded public key from Step 5.B (publicKeyInfo.publicKey, decodes to 65 raw bytes)
    PUBLIC_KEY_B64 = "your-public-key"
    
    raw_bytes = base64.b64decode(PUBLIC_KEY_B64)
    if len(raw_bytes) != 65 or raw_bytes[0] != 4:
      raise ValueError(f"Expected 65-byte uncompressed public key (0x04...), got {len(raw_bytes)} bytes")
    
    # 1. Parse and compress public key to 33 bytes
    pub = ec.PublicKey.parse(raw_bytes)
    pub.compressed = True
    compressed_pubkey_hex = pub.sec().hex()
    
    print("================================================================")
    print(f"Compressed Public Key (33 bytes): {compressed_pubkey_hex}")
    print("================================================================")
    
    # 2. Native SegWit (P2WPKH - BIP 173)
    p2wpkh = script.p2wpkh(pub)
    print("\n[1. Native SegWit (P2WPKH / Bech32 - BIP 173)]")
    print(f"  ScriptPubKey:           {p2wpkh.data.hex()}")
    print(f"  Testnet4 Address (tb):  {p2wpkh.address(NETWORKS['test'])}")
    print(f"  Mainnet Address (bc):   {p2wpkh.address(NETWORKS['main'])}")
    
    # 3. Nested SegWit (P2SH-P2WPKH - BIP 49)
    p2sh_p2wpkh = script.p2sh(p2wpkh)
    print("\n[2. Nested SegWit (P2SH-P2WPKH / Base58 - BIP 49)]")
    print(f"  RedeemScript:           {p2wpkh.data.hex()}")
    print(f"  ScriptPubKey:           {p2sh_p2wpkh.data.hex()}")
    print(f"  Testnet4 Address (2):   {p2sh_p2wpkh.address(NETWORKS['test'])}")
    print(f"  Mainnet Address (3):    {p2sh_p2wpkh.address(NETWORKS['main'])}")
    
    # 4. Legacy (P2PKH - BIP 44)
    p2pkh = script.p2pkh(pub)
    print("\n[3. Legacy (P2PKH / Base58 - BIP 44)]")
    print(f"  ScriptPubKey:           {p2pkh.data.hex()}")
    print(f"  Testnet4 Address (m/n): {p2pkh.address(NETWORKS['test'])}")
    print(f"  Mainnet Address (1):    {p2pkh.address(NETWORKS['main'])}")
    EOF
    
    python3 derive_btc_address.py
    

#### Locating Unspent Outputs (UTXOs)

Unlike account-based blockchains, Bitcoin transactions spend specific unspent transaction outputs (UTXOs). Before constructing a transaction in Step 6:

  1. Fund your derived Native SegWit address (for example, using a testnet faucet).
  2. Query your address's unspent UTXOs using your Bitcoin node (`bitcoin-cli listunspent 1 9999999 "[\"tb1q...\"]"`) or a block explorer API.
  3. Note the following 4 parameters for Step 6: 
     * **`txid`** : The 32-byte transaction hash of the unspent output.
     * **`vout`** : The zero-indexed output index (for example, `0` or `1`).
     * **`value`** : The unspent amount in satoshis (for example, `200000` satoshis = 0.002 BTC).
     * **`scriptPubKey`** : The locking script hex (for example, `0014...`).



* * *

## Step 6: Execute an MPC Operation

Policy evaluation and signing initiation happen together when a `SIGNER` calls [`transactions.create`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/create) (`CreateTransaction`). The instance decodes `payload` according to `schema`, evaluates all active transaction policies, records the result in `policyEvaluationRecord`, and records the initiating signer's `AUTHORIZE` decision.

### A. Create Transaction (Evaluate Policy & Initiate Signing)

**Important:** **Transaction Decision Signature Structure (`TransactionSigningPayload`)**: Rather than signing the raw 32-byte digest directly, the initiating signer and each co-signer sign a serialized `google.cloud.mpc.v1beta.TransactionSigningPayload` protobuf message (`key = 1` for `CreateTransaction` or `transaction = 2` for `RecordSignerDecision`, `decision = 3` where `AUTHORIZE = 1` and `DENY = 2`, `digest = 4` for `EC_SIGN_SECP256K1` or `raw_message = 5` for `EC_SIGN_ED25519`, and `metadata = 6` if set). Ensure the `digest` bytes match the hash of `payload`.

Submit the transaction as Signer 1 (`alice@example.com`) for policy evaluation and signing:

### Ethereum, KMS

#### 🛑 Case A: Rejection (Too High Value)

Attempt to create a transaction of **3 ETH** (exceeds our 2 ETH policy limit):
    
    
    sign_tx_decision() {
      local signer_id=$1
      local resource_type=$2
      local resource_name=$3
      local decision=$4
      local digest_hex=$5
      python3 -c 'import sys; rt, rn, dec, dg = sys.argv[1:]; f = lambda k, b: bytes([k << 3 | 2, len(b)]) + b; open("tx_decision_payload.bin", "wb").write(f(1 if rt == "key" else 2, rn.encode()) + bytes([24, 1 if dec == "AUTHORIZE" else 2]) + f(4, bytes.fromhex(dg)))' "${resource_type}" "${resource_name}" "${decision}" "${digest_hex}"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${signer_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=tx_decision_payload.bin \
        --signature-file=tx_decision_sig.bin > /dev/null
      openssl base64 -A -in tx_decision_sig.bin
    }
    
    # Payload for 3 ETH (amount_token_scaled = 3,000,000,000 > 2,000,000,000)
    RAW_TX_BYTES_HEX="ef808504a817c8008252089411111111111111111111111111111111111111118829a2241af62c00008083aa36a78080"
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$RAW_TX_BYTES_HEX')).decode('utf-8'))")
    DIGEST_HEX=$(python3 -c "from eth_utils import keccak; print(keccak(bytes.fromhex('$RAW_TX_BYTES_HEX')).hex())")
    DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"ETHEREUM_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111601\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions" | jq
    

Expected Policy Evaluation Result: `decision: DENY` (`denyReason: NO_PERMIT_RULE_MATCHED`).

#### ✅ Case B: Approval (Permitted Value)

Create a transaction of **1 Gwei** (within our 2 ETH limit):
    
    
    # Payload for 1 Gwei
    RAW_TX_BYTES_HEX="eb808504a817c800825208941111111111111111111111111111111111111111843b9aca008083aa36a78080"
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$RAW_TX_BYTES_HEX')).decode('utf-8'))")
    export DIGEST_HEX=$(python3 -c "from eth_utils import keccak; print(keccak(bytes.fromhex('$RAW_TX_BYTES_HEX')).hex())")
    export DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"ETHEREUM_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111602\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions")
    
    echo "$RESPONSE" | jq
    export TRANSACTION_NAME=$(echo "$RESPONSE" | jq -r '.name')
    

Expected Response: `state: PENDING_AUTHORIZATION` and `policyEvaluationRecord.decision: PERMIT`.

### Ethereum, OpenSSL

#### 🛑 Case A: Rejection (Too High Value)

Attempt to create a transaction of **3 ETH** (exceeds our 2 ETH policy limit):
    
    
    sign_tx_decision() {
      local signer_id=$1
      local resource_type=$2
      local resource_name=$3
      local decision=$4
      local digest_hex=$5
      python3 -c 'import sys; rt, rn, dec, dg = sys.argv[1:]; f = lambda k, b: bytes([k << 3 | 2, len(b)]) + b; open("tx_decision_payload.bin", "wb").write(f(1 if rt == "key" else 2, rn.encode()) + bytes([24, 1 if dec == "AUTHORIZE" else 2]) + f(4, bytes.fromhex(dg)))' "${resource_type}" "${resource_name}" "${decision}" "${digest_hex}"
      openssl dgst -sha256 -sign "${signer_id}_priv.pem" -out tx_decision_sig.bin tx_decision_payload.bin
      openssl base64 -A -in tx_decision_sig.bin
    }
    
    # Payload for 3 ETH (amount_token_scaled = 3,000,000,000 > 2,000,000,000)
    RAW_TX_BYTES_HEX="ef808504a817c8008252089411111111111111111111111111111111111111118829a2241af62c00008083aa36a78080"
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$RAW_TX_BYTES_HEX')).decode('utf-8'))")
    DIGEST_HEX=$(python3 -c "from eth_utils import keccak; print(keccak(bytes.fromhex('$RAW_TX_BYTES_HEX')).hex())")
    DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"ETHEREUM_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111601\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions" | jq
    

Expected Policy Evaluation Result: `decision: DENY` (`denyReason: NO_PERMIT_RULE_MATCHED`).

#### ✅ Case B: Approval (Permitted Value)

Create a transaction of **1 Gwei** (within our 2 ETH limit):
    
    
    # Payload for 1 Gwei
    RAW_TX_BYTES_HEX="eb808504a817c800825208941111111111111111111111111111111111111111843b9aca008083aa36a78080"
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$RAW_TX_BYTES_HEX')).decode('utf-8'))")
    export DIGEST_HEX=$(python3 -c "from eth_utils import keccak; print(keccak(bytes.fromhex('$RAW_TX_BYTES_HEX')).hex())")
    export DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"ETHEREUM_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111602\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions")
    
    echo "$RESPONSE" | jq
    export TRANSACTION_NAME=$(echo "$RESPONSE" | jq -r '.name')
    

Expected Response: `state: PENDING_AUTHORIZATION` and `policyEvaluationRecord.decision: PERMIT`.

### Bitcoin, KMS

In the Bitcoin UTXO model, transactions spend specific unspent outputs. In SegWit (BIP 143), calculating the signature hash requires knowing the satoshi amount and locking script of the input being spent.

Bitcoin policy evaluation requires BIP 174 PSBT v0 format (`BITCOIN_TX_V2`) with `PSBT_IN_WITNESS_UTXO` populated for each input.

**Important:** **Change Output and Satoshi Accounting** : In Bitcoin, any unallocated difference (`InputSatoshis - RecipientSatoshis - MinerFeeSatoshis`) is claimed by miners. To prevent losing funds, transactions must explicitly allocate a **Change Output** returning the unspent balance back to the sender's own derived Native SegWit address.

#### PSBT Construction Script (`build_psbt.py`)

Execute the following block to assemble a valid BIP 174 PSBT v0 payload:
    
    
    cat <<'EOF' > build_psbt.py
    """Constructs a BIP 174 PSBT v0 payload using embit for Bitcoin policy evaluation."""
    
    from embit import script, transaction
    from embit.psbt import PSBT
    
    # 1. Inputs (From Step 5.C)
    PREV_TXID_HEX = "8f594f33156993f1c980c2273dcae4a92cf2517fbc29264421395e63a63916d8"
    PREV_VOUT = int("1")
    INPUT_VALUE_SATS = int("200000")  # Total UTXO input value in satoshis
    SENDER_SCRIPTPUBKEY_HEX = "0014eced05cd51d964102a20c856b09080ad620e9da2"
    
    # 2. Output Allocations
    RECIPIENT_SATS = int("50000")  # Recipient payment in satoshis
    MINER_FEE_SATS = int("250")  # Miner fee in satoshis
    RECIPIENT_SCRIPTPUBKEY_HEX = "0014751e76e8199196d454941c45d1b3a323f1433bd6"
    
    # Change Output calculation: InputSats - RecipientSats - MinerFeeSats
    CHANGE_SATS = INPUT_VALUE_SATS - RECIPIENT_SATS - MINER_FEE_SATS
    if CHANGE_SATS <= 0:
      raise ValueError(f"Insufficient input satoshis ({INPUT_VALUE_SATS}) for payment and fee")
    
    # 3. Construct Unsigned Transaction (Version 2, 1 input, 2 outputs, locktime 0)
    tx = transaction.Transaction(
        version=2,
        vin=[transaction.TransactionInput(
            txid=bytes.fromhex(PREV_TXID_HEX),
            vout=PREV_VOUT,
            sequence=0xFFFFFFFF,
        )],
        vout=[
            transaction.TransactionOutput(
                value=RECIPIENT_SATS,
                script_pubkey=script.Script(bytes.fromhex(RECIPIENT_SCRIPTPUBKEY_HEX)),
            ),
            transaction.TransactionOutput(
                value=CHANGE_SATS,
                script_pubkey=script.Script(bytes.fromhex(SENDER_SCRIPTPUBKEY_HEX)),
            ),
        ],
        locktime=0,
    )
    
    # 4. Package into BIP 174 PSBT with Input Witness UTXO
    psbt = PSBT(tx)
    psbt.inputs[0].witness_utxo = transaction.TransactionOutput(
        value=INPUT_VALUE_SATS,
        script_pubkey=script.Script(bytes.fromhex(SENDER_SCRIPTPUBKEY_HEX)),
    )
    
    print(psbt.serialize().hex())
    EOF
    
    BTC_PSBT_HEX=$(python3 build_psbt.py)
    echo "Generated PSBT Hex (${#BTC_PSBT_HEX} chars):"
    echo "$BTC_PSBT_HEX"
    

#### 🛑 Case A: Rejection (Fee Limit Exceeded)

Attempt to create a transaction where the miner fee exceeds the 10,000 satoshi policy limit. In this example, setting `MINER_FEE_SATS = 15000` (and `CHANGE_SATS = 135000`) in `build_psbt.py` scales to `max_fee_atomic = 150000` (exceeding the policy cap of `100000`), producing the following payload that triggers a `DENY` policy evaluation decision.
    
    
    sign_tx_decision() {
      local signer_id=$1
      local resource_type=$2
      local resource_name=$3
      local decision=$4
      local digest_hex=$5
      python3 -c 'import sys; rt, rn, dec, dg = sys.argv[1:]; f = lambda k, b: bytes([k << 3 | 2, len(b)]) + b; open("tx_decision_payload.bin", "wb").write(f(1 if rt == "key" else 2, rn.encode()) + bytes([24, 1 if dec == "AUTHORIZE" else 2]) + f(4, bytes.fromhex(dg)))' "${resource_type}" "${resource_name}" "${decision}" "${digest_hex}"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${signer_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=tx_decision_payload.bin \
        --signature-file=tx_decision_sig.bin > /dev/null
      openssl base64 -A -in tx_decision_sig.bin
    }
    
    # Construct a PSBT payload with miner_fee_sats = 15000 -> max_fee_atomic = 150000 (exceeds 100000 limit)
    REJECTED_PSBT_HEX="70736274ff0100710200000001d81639a6635e3921442629bc7f51f22ca9e4ca3d27c280c9f1936915334f598f0100000000ffffffff0250c3000000000000160014751e76e8199196d454941c45d1b3a323f1433bd6580f020000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000000001011f400d030000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000"
    REJECTED_PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$REJECTED_PSBT_HEX')).decode('utf-8'))")
    REJECTED_DIGEST_HEX=$(python3 -c "from embit import script; from embit.psbt import PSBT; p=PSBT.parse(bytes.fromhex('$REJECTED_PSBT_HEX')); u=p.inputs[0].witness_utxo; sc=script.Script(b'\x76\xa9\x14'+u.script_pubkey.data[2:]+b'\x88\xac'); print(p.tx.sighash_segwit(0, sc, u.value).hex())")
    REJECTED_DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$REJECTED_DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${REJECTED_DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"BITCOIN_TX_V2\",
          \"payload\": \"${REJECTED_PAYLOAD_B64}\",
          \"digest\": \"${REJECTED_DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111603\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions" | jq
    

Expected Policy Evaluation Result: `decision: DENY` (`denyReason: NO_PERMIT_RULE_MATCHED`).

#### ✅ Case B: Approval (Permitted Bitcoin PSBT)

Create a transaction with the previously constructed valid PSBT (`RECIPIENT_SATS = 50000` maps to `amount_token_scaled = 500000 <= 2500000` and `MINER_FEE_SATS = 250` maps to `max_fee_atomic = 2500 <= 100000`):
    
    
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$BTC_PSBT_HEX')).decode('utf-8'))")
    export DIGEST_HEX=$(python3 -c "from embit import script; from embit.psbt import PSBT; p=PSBT.parse(bytes.fromhex('$BTC_PSBT_HEX')); u=p.inputs[0].witness_utxo; sc=script.Script(b'\x76\xa9\x14'+u.script_pubkey.data[2:]+b'\x88\xac'); print(p.tx.sighash_segwit(0, sc, u.value).hex())")
    export DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"BITCOIN_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111604\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions")
    
    echo "$RESPONSE" | jq
    export TRANSACTION_NAME=$(echo "$RESPONSE" | jq -r '.name')
    

Expected Response: `state: PENDING_AUTHORIZATION` and `policyEvaluationRecord.decision: PERMIT`.

### Bitcoin, OpenSSL

In the Bitcoin UTXO model, transactions spend specific unspent outputs. In SegWit (BIP 143), calculating the signature hash requires knowing the satoshi amount and locking script of the input being spent.

Bitcoin policy evaluation requires BIP 174 PSBT v0 format (`BITCOIN_TX_V2`) with `PSBT_IN_WITNESS_UTXO` populated for each input.

**Important:** **Change Output and Satoshi Accounting** : In Bitcoin, any unallocated difference (`InputSatoshis - RecipientSatoshis - MinerFeeSatoshis`) is claimed by miners. To prevent losing funds, transactions must explicitly allocate a **Change Output** returning the unspent balance back to the sender's own derived Native SegWit address.

#### PSBT Construction Script (`build_psbt.py`)

Execute the following block to assemble a valid BIP 174 PSBT v0 payload:
    
    
    cat <<'EOF' > build_psbt.py
    """Constructs a BIP 174 PSBT v0 payload using embit for Bitcoin policy evaluation."""
    
    from embit import script, transaction
    from embit.psbt import PSBT
    
    # 1. Inputs (From Step 5.C)
    PREV_TXID_HEX = "8f594f33156993f1c980c2273dcae4a92cf2517fbc29264421395e63a63916d8"
    PREV_VOUT = int("1")
    INPUT_VALUE_SATS = int("200000")  # Total UTXO input value in satoshis
    SENDER_SCRIPTPUBKEY_HEX = "0014eced05cd51d964102a20c856b09080ad620e9da2"
    
    # 2. Output Allocations
    RECIPIENT_SATS = int("50000")  # Recipient payment in satoshis
    MINER_FEE_SATS = int("250")  # Miner fee in satoshis
    RECIPIENT_SCRIPTPUBKEY_HEX = "0014751e76e8199196d454941c45d1b3a323f1433bd6"
    
    # Change Output calculation: InputSats - RecipientSats - MinerFeeSats
    CHANGE_SATS = INPUT_VALUE_SATS - RECIPIENT_SATS - MINER_FEE_SATS
    if CHANGE_SATS <= 0:
      raise ValueError(f"Insufficient input satoshis ({INPUT_VALUE_SATS}) for payment and fee")
    
    # 3. Construct Unsigned Transaction (Version 2, 1 input, 2 outputs, locktime 0)
    tx = transaction.Transaction(
        version=2,
        vin=[transaction.TransactionInput(
            txid=bytes.fromhex(PREV_TXID_HEX),
            vout=PREV_VOUT,
            sequence=0xFFFFFFFF,
        )],
        vout=[
            transaction.TransactionOutput(
                value=RECIPIENT_SATS,
                script_pubkey=script.Script(bytes.fromhex(RECIPIENT_SCRIPTPUBKEY_HEX)),
            ),
            transaction.TransactionOutput(
                value=CHANGE_SATS,
                script_pubkey=script.Script(bytes.fromhex(SENDER_SCRIPTPUBKEY_HEX)),
            ),
        ],
        locktime=0,
    )
    
    # 4. Package into BIP 174 PSBT with Input Witness UTXO
    psbt = PSBT(tx)
    psbt.inputs[0].witness_utxo = transaction.TransactionOutput(
        value=INPUT_VALUE_SATS,
        script_pubkey=script.Script(bytes.fromhex(SENDER_SCRIPTPUBKEY_HEX)),
    )
    
    print(psbt.serialize().hex())
    EOF
    
    BTC_PSBT_HEX=$(python3 build_psbt.py)
    echo "Generated PSBT Hex (${#BTC_PSBT_HEX} chars):"
    echo "$BTC_PSBT_HEX"
    

#### 🛑 Case A: Rejection (Fee Limit Exceeded)

Attempt to create a transaction where the miner fee exceeds the 10,000 satoshi policy limit. In this example, setting `MINER_FEE_SATS = 15000` (and `CHANGE_SATS = 135000`) in `build_psbt.py` scales to `max_fee_atomic = 150000` (exceeding the policy cap of `100000`), producing the following payload that triggers a `DENY` policy evaluation decision.
    
    
    sign_tx_decision() {
      local signer_id=$1
      local resource_type=$2
      local resource_name=$3
      local decision=$4
      local digest_hex=$5
      python3 -c 'import sys; rt, rn, dec, dg = sys.argv[1:]; f = lambda k, b: bytes([k << 3 | 2, len(b)]) + b; open("tx_decision_payload.bin", "wb").write(f(1 if rt == "key" else 2, rn.encode()) + bytes([24, 1 if dec == "AUTHORIZE" else 2]) + f(4, bytes.fromhex(dg)))' "${resource_type}" "${resource_name}" "${decision}" "${digest_hex}"
      openssl dgst -sha256 -sign "${signer_id}_priv.pem" -out tx_decision_sig.bin tx_decision_payload.bin
      openssl base64 -A -in tx_decision_sig.bin
    }
    
    # Construct a PSBT payload with miner_fee_sats = 15000 -> max_fee_atomic = 150000 (exceeds 100000 limit)
    REJECTED_PSBT_HEX="70736274ff0100710200000001d81639a6635e3921442629bc7f51f22ca9e4ca3d27c280c9f1936915334f598f0100000000ffffffff0250c3000000000000160014751e76e8199196d454941c45d1b3a323f1433bd6580f020000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000000001011f400d030000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000"
    REJECTED_PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$REJECTED_PSBT_HEX')).decode('utf-8'))")
    REJECTED_DIGEST_HEX=$(python3 -c "from embit import script; from embit.psbt import PSBT; p=PSBT.parse(bytes.fromhex('$REJECTED_PSBT_HEX')); u=p.inputs[0].witness_utxo; sc=script.Script(b'\x76\xa9\x14'+u.script_pubkey.data[2:]+b'\x88\xac'); print(p.tx.sighash_segwit(0, sc, u.value).hex())")
    REJECTED_DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$REJECTED_DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${REJECTED_DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"BITCOIN_TX_V2\",
          \"payload\": \"${REJECTED_PAYLOAD_B64}\",
          \"digest\": \"${REJECTED_DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111603\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions" | jq
    

Expected Policy Evaluation Result: `decision: DENY` (`denyReason: NO_PERMIT_RULE_MATCHED`).

#### ✅ Case B: Approval (Permitted Bitcoin PSBT)

Create a transaction with the previously constructed valid PSBT (`RECIPIENT_SATS = 50000` maps to `amount_token_scaled = 500000 <= 2500000` and `MINER_FEE_SATS = 250` maps to `max_fee_atomic = 2500 <= 100000`):
    
    
    PAYLOAD_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$BTC_PSBT_HEX')).decode('utf-8'))")
    export DIGEST_HEX=$(python3 -c "from embit import script; from embit.psbt import PSBT; p=PSBT.parse(bytes.fromhex('$BTC_PSBT_HEX')); u=p.inputs[0].witness_utxo; sc=script.Script(b'\x76\xa9\x14'+u.script_pubkey.data[2:]+b'\x88\xac'); print(p.tx.sighash_segwit(0, sc, u.value).hex())")
    export DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    
    SIGNER_1_SIG_B64=$(sign_tx_decision "signer-alice" "key" "${KEY_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
    SIGNED_DECISION_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d "{
        \"transaction\": {
          \"action\": \"Action::\\\"Transfer\\\"\",
          \"schema\": \"BITCOIN_TX_V2\",
          \"payload\": \"${PAYLOAD_B64}\",
          \"digest\": \"${DIGEST_B64}\"
        },
        \"authorizationInfo\": {
          \"signature\": \"${SIGNER_1_SIG_B64}\",
          \"signedPayload\": \"${SIGNED_DECISION_PAYLOAD_B64}\"
        },
        \"requestId\": \"11111111-1111-4111-8111-111111111604\"
      }" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions")
    
    echo "$RESPONSE" | jq
    export TRANSACTION_NAME=$(echo "$RESPONSE" | jq -r '.name')
    

Expected Response: `state: PENDING_AUTHORIZATION` and `policyEvaluationRecord.decision: PERMIT`.

#### 🕵️‍♂️ Check Transaction State (Polling)

Poll the transaction status by running the following command periodically:

### curl
    
    
    curl -s -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${TRANSACTION_NAME}" | jq
    

### B. Record Signer Decision (Authorize)

Because `CreateTransaction` in Step 6.A already recorded Signer 1's `AUTHORIZE` decision (1 of 2 required by the 2-of-3 `KeyPolicy` threshold), only one additional co-signer holding a key share needs to authorize the transaction using [`transactions.recordSignerDecision`](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/recordSignerDecision) (`RecordSignerDecision`).

**Note:** Steps 6.B and 6.C operate identically across Ethereum and Bitcoin because the MPC threshold keys sign the 32-byte `digest` verified against `payload`.

Sign the `TransactionSigningPayload` naming `transaction` (`${TRANSACTION_NAME}`) and call `recordSignerDecision` as Signer 2 (`bob@example.com`):

### curl
    
    
    # 1. Check state for Signer 2
    TX_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth print-access-token "bob@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${TRANSACTION_NAME}")
    
    TX_STATE=$(echo "$TX_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$TX_STATE" == "PENDING_AUTHORIZATION" ]; then
      # 2. Sign as Signer 2 naming transaction ($TRANSACTION_NAME)
      SIGNER_2_SIG_B64=$(sign_tx_decision "signer-bob" "transaction" "${TRANSACTION_NAME}" "AUTHORIZE" "${DIGEST_HEX}")
      SIGNER_2_PAYLOAD_B64=$(openssl base64 -A -in tx_decision_payload.bin)
    
      # 3. Call RecordSignerDecision as Signer 2
      echo "Recording AUTHORIZE decision for Signer 2..."
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token "bob@example.com")" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d "{
          \"decision\": \"AUTHORIZE\",
          \"authorizationInfo\": {
            \"signature\": \"${SIGNER_2_SIG_B64}\",
            \"signedPayload\": \"${SIGNER_2_PAYLOAD_B64}\"
          }
        }" \
        "${INSTANCE_URL}/v1beta/${TRANSACTION_NAME}:recordSignerDecision" | jq
    elif [ "$TX_STATE" == "SIGNING" ] || [ "$TX_STATE" == "SIGNING_SUCCEEDED" ]; then
      echo "Transaction is in state $TX_STATE. Skipping Signer 2."
    else
      echo "Transaction is in an unexpected state: $TX_STATE"
    fi
    

### C. Fetch Final Signature

Once the threshold of authorizations is reached, check the transaction state and fetch `finalSignature` (and `recoveryId` for `EC_SIGN_SECP256K1` keys):

### curl
    
    
    curl -s -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token "alice@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${TRANSACTION_NAME}" | jq
    

When `state` is `SIGNING_SUCCEEDED`, copy the `finalSignature` field from the returned JSON for Step 7.

* * *

## Step 7: Broadcast Transaction to Blockchain

Once your transaction reaches the `SIGNING_SUCCEEDED` state and you have fetched the `finalSignature`, the last step is to construct the signed wire transaction and broadcast it to the network.

### Ethereum

### Recovery Identifier Derivation & Broadcasting

The MPC API returns a raw 64-byte ECDSA signature in `finalSignature` (comprising the 32-byte `r` and `s` values in canonical low-S form per EIP-2), along with the recovery parity bit (`0` or `1`) in `recoveryId`.

The following Python script constructs the signed transaction using your `finalSignature`, verifies the recovered sender address against your MPC key's Ethereum address, and broadcasts it to the network.

**Broadcast Script:**

Execute the following copy-pastable block in your terminal to write and run `broadcast_eth.py`:
    
    
    cat <<'EOF' > broadcast_eth.py
    """Broadcasts an Ethereum transaction using a normalized MPC signature."""
    
    import base64
    import os
    import requests
    from eth_account import Account
    try:
        from eth_account._utils.transactions import encode_transaction, serializable_unsigned_transaction_from_dict
    except ImportError:
        from eth_account._utils.legacy_transactions import encode_transaction, serializable_unsigned_transaction_from_dict
    
    # ==========================================
    # 1. INPUTS
    # ==========================================
    FINAL_SIGNATURE_B64 = "your-final-signature"
    RPC_URL = "https://ethereum-sepolia-rpc.publicnode.com"
    EXPECTED_SENDER = "0xyour-mpc-key-address"
    
    if not FINAL_SIGNATURE_B64 or FINAL_SIGNATURE_B64 == "your-final-signature":
        raise ValueError("FINAL_SIGNATURE_B64 is not set. Please provide a valid signature.")
    
    # ==========================================
    # 2. TRANSACTION PARAMETERS
    # ==========================================
    CHAIN_ID = 11155111  # Sepolia Testnet
    tx_dict = {
        "nonce": int("0"),
        "gasPrice": int("20000000000"),  # 20 Gwei
        "gas": int("21000"),
        "to": "0x1111111111111111111111111111111111111111",
        "value": int("1000000000"),  # 1 Gwei
        "data": b"",
        "chainId": CHAIN_ID,
    }
    
    # ==========================================
    # 3. DECODE & SPLIT SIGNATURE
    # ==========================================
    missing_padding = len(FINAL_SIGNATURE_B64) % 4
    if missing_padding:
        FINAL_SIGNATURE_B64 += "=" * (4 - missing_padding)
    
    sig_bytes = base64.b64decode(FINAL_SIGNATURE_B64)
    r = int.from_bytes(sig_bytes[:32], byteorder="big")
    s = int.from_bytes(sig_bytes[32:], byteorder="big")
    
    # ==========================================
    # 4. RECOVERY IDENTIFIER (V) DERIVATION
    # ==========================================
    chain_v_base = (CHAIN_ID * 2) + 35
    
    # ==========================================
    # 5. GENERATE UNSIGNED TX & RECOVER SENDER ADDRESS
    # ==========================================
    unsigned_tx = serializable_unsigned_transaction_from_dict(tx_dict)
    
    derived_sender = None
    encoded_tx = None
    final_v = chain_v_base
    
    EXPECTED_SENDER_PLACEHOLDER = "0xyour-mpc-key-address"
    is_valid_expected = EXPECTED_SENDER and EXPECTED_SENDER != EXPECTED_SENDER_PLACEHOLDER
    
    for parity in [0, 1]:
        try_v = chain_v_base + parity
        try:
            tx_candidate = encode_transaction(unsigned_tx, vrs=(try_v, r, s))
            addr = Account.recover_transaction("0x" + tx_candidate.hex())
    
            if is_valid_expected and EXPECTED_SENDER.lower() == addr.lower():
                derived_sender = addr
                final_v = try_v
                encoded_tx = tx_candidate
                break
    
            if not is_valid_expected and derived_sender is None:
                derived_sender = addr
                final_v = try_v
                encoded_tx = tx_candidate
                print(f"Warning: EXPECTED_SENDER not provided or is placeholder. Assuming first recovered address: {addr}")
    
        except Exception:
            continue
    
    if encoded_tx is None:
        if is_valid_expected:
            raise ValueError(f"Could not recover address matching EXPECTED_SENDER: {EXPECTED_SENDER}")
        else:
            raise ValueError("Could not derive broadcastable transaction. Ensure signature matches payload.")
    
    if derived_sender:
        print(f"Derived Sender Address: {derived_sender}")
    else:
        print("Derived Sender Address: Could not recover (ensure signature matches current transaction payload)")
    
    valid_tx_hex = "0x" + encoded_tx.hex()
    print(f"Broadcastable Transaction Hex:\n{valid_tx_hex}\n")
    
    # ==========================================
    # 6. BROADCAST TO NETWORK
    # ==========================================
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_sendRawTransaction",
        "params": [valid_tx_hex],
        "id": 1,
    }
    
    print(f"Broadcasting to {RPC_URL}...")
    response = requests.post(RPC_URL, json=payload)
    resp_json = response.json()
    print("RPC Response:", resp_json)
    if "result" in resp_json:
        tx_hash = resp_json["result"]
        print(f"View transaction on Sepolia Etherscan: https://sepolia.etherscan.io/tx/{tx_hash}")
    EOF
    
    python3 broadcast_eth.py
    

#### Troubleshooting Common Errors

  * **`invalid sender: recovery failed` or `invalid transaction v, r, s values`:** This occurs if the transaction parameters in your script don't _exactly_ match the payload that was signed. Ensure the `value`, `nonce`, and `to` fields match what was processed in Step 6.
  * **`insufficient funds for gas * price + value`:** Your transaction is cryptographically valid and was accepted by the node, but your MPC Key's Ethereum address does not have enough testnet ETH to cover the operation. You will need to fund your address before broadcasting.



### Bitcoin

### SegWit Wire Transaction Assembly & Broadcasting

For Bitcoin Native SegWit transactions (BIP 141), the raw 64-byte `(r, s)` MPC signature must be formatted into canonical low-S ASN.1 DER, appended with `0x01` (`SIGHASH_ALL`), and assembled with the 33-byte compressed public key into the 2-element SegWit witness stack: `[DER signature || 0x01, compressed public key]`.

**Broadcast Script:**

Execute the following block to create and run `broadcast_btc.py`:
    
    
    cat <<'EOF' > broadcast_btc.py
    """Assembles a signed Bitcoin Native SegWit transaction from an MPC signature using embit and broadcasts it."""
    
    import base64
    import urllib.request
    from embit import ec, script, transaction
    
    # ==========================================
    # 1. INPUTS
    # ==========================================
    FINAL_SIGNATURE_B64 = "your-final-signature"
    COMPRESSED_PUBKEY_HEX = "03deb76948c14003446a8c1d79e88fb3607c9bbc1f5143b186aa7b61d6b1facc36"
    
    PREV_TXID_HEX = "8f594f33156993f1c980c2273dcae4a92cf2517fbc29264421395e63a63916d8"
    PREV_VOUT = int("1")
    
    RECIPIENT_SATS = int("50000")
    RECIPIENT_SCRIPTPUBKEY_HEX = "0014751e76e8199196d454941c45d1b3a323f1433bd6"
    
    CHANGE_SATS = int("149750")
    CHANGE_SCRIPTPUBKEY_HEX = "0014eced05cd51d964102a20c856b09080ad620e9da2"
    
    BROADCAST_API_URL = "https://mempool.space/testnet4/api/tx"
    
    # ==========================================
    # 2. CONVERT RAW (r, s) SIGNATURE TO CANONICAL LOW-S ASN.1 DER + SIGHASH_ALL
    # ==========================================
    sig_bytes = base64.b64decode(FINAL_SIGNATURE_B64)
    internal_sig = ec.secp256k1.ecdsa_signature_parse_compact(sig_bytes)
    ec.secp256k1.ecdsa_signature_normalize(internal_sig, internal_sig)
    der_sig = ec.secp256k1.ecdsa_signature_serialize_der(internal_sig) + b"\x01"  # 0x01 = SIGHASH_ALL
    
    # ==========================================
    # 3. BUILD TRANSACTION & ATTACH SEGWIT WITNESS STACK
    # ==========================================
    tx = transaction.Transaction(
        version=2,
        vin=[transaction.TransactionInput(
            txid=bytes.fromhex(PREV_TXID_HEX),
            vout=PREV_VOUT,
            sequence=0xFFFFFFFF,
        )],
        vout=[
            transaction.TransactionOutput(
                value=RECIPIENT_SATS,
                script_pubkey=script.Script(bytes.fromhex(RECIPIENT_SCRIPTPUBKEY_HEX)),
            ),
            transaction.TransactionOutput(
                value=CHANGE_SATS,
                script_pubkey=script.Script(bytes.fromhex(CHANGE_SCRIPTPUBKEY_HEX)),
            ),
        ],
        locktime=0,
    )
    
    pubkey_bytes = bytes.fromhex(COMPRESSED_PUBKEY_HEX)
    tx.vin[0].witness = transaction.Witness([der_sig, pubkey_bytes])
    
    signed_tx_hex = tx.serialize().hex()
    print("--- Signed Bitcoin SegWit Wire Transaction Hex ---")
    print(signed_tx_hex)
    
    # ==========================================
    # 4. BROADCAST TO NETWORK
    # ==========================================
    if BROADCAST_API_URL:
      print(f"\nBroadcasting to {BROADCAST_API_URL}...")
      try:
        req = urllib.request.Request(
            BROADCAST_API_URL,
            data=signed_tx_hex.encode("utf-8"),
            headers={"Content-Type": "text/plain"},
            method="POST",
        )
        with urllib.request.urlopen(req) as resp:
          txid_result = resp.read().decode("utf-8").strip()
          print(f"✅ Broadcast Successful! Transaction ID (txid): {txid_result}")
          print(f"Track in Mempool Explorer: https://mempool.space/testnet4/tx/{txid_result}")
      except Exception as e:
        print(f"Broadcast response: {e}")
    EOF
    
    python3 broadcast_btc.py
    

#### Troubleshooting Common Errors

  * **`mandatory-script-verify-flag-failed (Signature must be zero for failed CHECK(MULTI)SIG operation)` / `non-mandatory-script-verify-flag (Non-canonical DER signature)`:** Ensure the `s` component of the signature is in canonical low-s form (`s <= N/2`) and properly DER-encoded.
  * **`bad-txns-in-belowout` / `bad-txns-fee-negative`:** Total outputs exceed input value. Ensure your change calculation (`InputSatoshis - PaymentSatoshis - MinerFee`) is strictly positive.



## 📖 Appendix: Operational Cookbook (Querying & Inspecting)

Use these commands to inspect and manage the state of your resources at any time.

* * *

### 🏢 1. Instances

Inspect and manage MPC instances in your project and location.

#### A. List all Instances

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "https://mpc.googleapis.com/v1beta/projects/my-project/locations/us-central1/instances" | jq
    

#### B. Get details for a specific Instance

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "https://mpc.googleapis.com/v1beta/${INSTANCE_NAME}" | jq
    

* * *

### 👥 2. Teams & Users

Inspect teams and users in your instance.

#### A. List all Teams

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/teams" | jq
    

#### B. Get details for a specific Team

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${TEAM_NAME}" | jq
    

#### C. List all registered Users

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/users" | jq
    

#### D. Get details for a specific User

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${SIGNER_1_NAME}" | jq
    

* * *

### 📜 3. Transaction Policies & KeyLists

Inspect transaction policies and key lists.

#### A. List all Transaction Policies

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/transactionPolicies" | jq
    

#### B. Get details for a specific Transaction Policy

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${POLICY_NAME}" | jq
    

#### C. List and Get KeyLists

### curl
    
    
    # List all KeyLists
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/keyLists" | jq
    
    # Get a specific KeyList
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${KEY_LIST_NAME}" | jq
    

* * *

### 🔑 4. Keys & KeyRings

Inspect key rings and distributed keys.

#### A. List all KeyRings

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/keyRings" | jq
    

#### B. List all Keys in a KeyRing

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${KEY_RING_NAME}/keys" | jq
    

#### C. Get details of a specific Distributed Key

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}" | jq
    

* * *

### 📝 5. Transactions (Signing Operations)

Inspect transactions and signing status.

#### A. List all Transactions for a Key (or across all Keys)

### curl
    
    
    # List transactions for a specific Key
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${KEY_NAME}/transactions" | jq
    
    # List transactions across all KeyRings and Keys using the '-' wildcard
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${INSTANCE_NAME}/keyRings/-/keys/-/transactions" | jq
    

#### B. Get details or status of a specific Transaction

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token "admin-1@example.com")" \
      -H "X-Goog-User-Project: my-project" \
      "${INSTANCE_URL}/v1beta/${TRANSACTION_NAME}" | jq
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


