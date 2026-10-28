---
url: https://docs.cloud.google.com/multi-party-compute/user-guide-v1alpha/
title: Multi-party Compute User Guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T00:17:56.554992+00:00
---

# Multi-party Compute User Guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/user-guide-v1alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)



#  Multi-party Compute User Guide Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide covers the experimental `v1alpha1` API, which is no longer under active development. For the `v1beta` API -- the stable, GA-intended API that will graduate to v1, see the [`v1beta` user guide](https://docs.cloud.google.com/multi-party-compute/user-guide).

This guide describes how to use the Multi-party Compute API to manage distributed keys, participants, and policies. It is intended for preview customers learning the key user journeys.

## Overview

The MPC API consists of two main components:

  1. **Core MPC** manages the lifecycle of distributed keys, proposals, and signing ceremonies.
  2. **Policy Engine** enforces governance, authorizing operations before they are executed.



For a detailed breakdown of how API access and cryptographic signing interact, see [Security and Authorization](https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha).

> **Note:** **Solo Simulation vs. Multi-user Simulation** : In a realistic environment, this system relies on strict **Separation of Duties** across multiple personas (Administrators, Policy Authors, and Signers), each with distinct cryptographic keys and IAM permissions. However, to simplify testing and learning, this guide is structured so a single developer can act as all roles from a single workstation. See [Security and Authorization](https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha) for details on how these roles interact in real scenarios.

## Prerequisites

Before starting, ensure you have:

  1. A Google Cloud Project. See [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) to make one.
  2. If not using Cloud Shell, the `gcloud` CLI installed and authenticated.
  3. Required APIs enabled, if not already done so. You need two, the new MPC API used in this guide, and Cloud Key Management Service if using it for assent key generation/signing.
         
         gcloud services enable mpc.googleapis.com cloudkms.googleapis.com
         

To view enabled APIs:
         
         gcloud services list --enabled
         

  4. Python 3.9+ and tutorial helper libraries installed:
         
         pip install embit eth-account eth-utils requests
         

  5. (Optional) If your organization authenticates using an external Identity Provider (such as Okta or Microsoft Entra ID) without Google Accounts, see [Configure Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid) to configure Application Default Credentials (ADC) with your federated identity.


**Tip:** We recommend using [**Cloud Shell**](https://console.cloud.google.com/?cloudshell=true) to run the commands in this guide. Cloud Shell comes pre-configured with the Google Cloud SDK (`gcloud`), `openssl`, `jq`, and other tools, and handles authentication automatically. To open Cloud Shell, click the terminal icon in the top navigation bar of the Google Cloud console.**Note:** While the MPC API supports dynamic **K-of-N keyshares** (allowing arbitrary thresholds), this guide demonstrates a **2-of-3** setup. Additionally, all policies require at least two authors (a **2-of-2** quorum) to be active.

## Setup

Update the following variables to populate the commands throughout this guide.

**Important:** If you leave or refresh this page, these input fields may reset to defaults.

### Required Setup

You **must** customize these parameters. The guide won't function with the placeholder values.

Parameter | Value | Description  
---|---|---  
**Project ID** | `my-project` | The consumer project ID you've provided to us for onboarding onto the preview.  
**Domain ID** | `67317436-0f29-ba9e-9146-d11c0bd8df9b` | The unique domain ID we've assigned to your instance.  
**Instance Path ID** | `mpc-unit-bob-123` | The path instance ID we've assigned to your instance.  
**Location** | `us-central1` | Deployment location. **Must** be `us-central1` (other regions are not supported in preview).  
  
### Tutorial Resource Labels

These are names for resources created during this tutorial. The default values are valid and can be kept to minimize setup friction.

Parameter | Value | Description  
---|---|---  
**Cloud KMS KeyRing ID** | `mpc-assent-keys` | Cloud Key Management Service KeyRing for external assent keys stored in Cloud KMS.  
**Signer 1 ID** | `signer-alice` | MPC Signer 1.  
**Signer 2 ID** | `signer-bob` | MPC Signer 2.  
**Signer 3 ID** | `signer-charlie` | MPC Signer 3.  
**Policy Author 1 ID** | `author-dave` | Policy Author 1.  
**Policy Author 2 ID** | `author-eve` | Policy Author 2.  
**Policy ID** | `ethereum-transfer-policy` | Policy ID (for example, `ethereum-transfer-policy` or `bitcoin-psbt-policy`).  
**KeyRing ID** | `my-key-ring` | KeyRing ID.  
**Key ID** | `my-key` | Key ID.  
**Proposal ID** | `my-proposal` | Proposal ID.  
  
## Step 1: Generate Assent Keys

To use the MPC API, you must generate keypairs for the following distinct roles. Note, these are **external cryptographic assent keys** , and are distinct from the distributed MPC threshold key shards generated internally during setup.

  * **Policy Authors** : Authorize governance policies.
  * **Signers** : Provide assent (voting/approval) on proposals.

**Note:** For simplicity, this guide simulates multiple **personas** (with assent keys) using a single **IAM identity**. Ensure your active account has administrative permissions (`roles/mpc.admin`). In production, Administrators provision **Policy Authors** and **Signers** (granting them `roles/mpc.editor`), and these users manage their own assent keys independently. See [Security and Authorization](https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha) for more details.

### A. Participant Keys (secp256k1)

Generate the necessary cryptographic keys for your participants. These commands are idempotent.

### Cloud KMS

We recommend managing assent keys in Cloud Key Management Service. Ensure your identity has permissions to create key rings, create keys, sign, and view public key verifiers (such as `roles/cloudkms.admin` and `roles/cloudkms.signerVerifier`). Ensure you have a `KeyRing` created, then generate a `secp256k1` key for all your signers.
    
    
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
    
    # Generate Keys
    for ID in signer-alice signer-bob signer-charlie; do
      echo "Generating KMS key for $ID..."
      provision_kms_key "$ID"
    done
    

### OpenSSL

You can use standard OpenSSL to generate `secp256k1` keys for each participant.
    
    
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
    
    for ID in signer-alice signer-bob signer-charlie; do
      echo "Generating OpenSSL key for $ID..."
      provision_openssl_key "$ID"
    done
    

### B. Policy Author Keys (secp256k1)

### Cloud KMS

Similarly, we recommend managing these assent keys in Cloud Key Management Service. Ensure your identity has permissions to create key rings, create keys, sign, and view public key verifiers (such as `roles/cloudkms.admin` and `roles/cloudkms.signerVerifier`). Ensure you have a `KeyRing` created, then generate a `secp256k1` key for all your Policy Authors.
    
    
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
    
    provision_keyring
    
    for ID in author-dave author-eve; do
      echo "Generating KMS key for $ID..."
      provision_kms_key "$ID"
    done
    

### OpenSSL

Policy Authors use the `secp256k1` curve for signing governance policies and administrative actions. You can generate these keys using standard OpenSSL.
    
    
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
    
    for ID in author-dave author-eve; do
      echo "Generating OpenSSL key for $ID..."
      provision_openssl_key "$ID"
    done
    

* * *

## Step 2: Register Participants

Before any entity can participate in the MPC flow (as a Signer) or the Policy flow (as a Policy Author), they must be registered as a Participant.

Registration requires an out-of-band coordination between the **Administrator** and the **Participant** :

  1. **The Entity** (Signer or Author) generates their key pair locally and transfers their **Public Key** to the Administrator securely.
  2. **The Administrator** (holding standard Google Cloud IAM permissions) calls the API to register the Public Key.

**Note:** Future versions will include an in-band **Invite Flow** to automate this key exchange directly through the API).

### curl
    
    
    provision_participant() {
      local id=$1
      local name=$2
      local pubkey_b64
    
      # Read the public key from the file generated in Step 1
      echo "Reading public key from ${id}_pub.pem..."
      # Public key must be represented as Base64 encoded bytes of the PEM/DER format.
      pubkey_b64=$(openssl base64 -A -in "${id}_pub.pem")
    
      # Check existence
      if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/$id"; then
        echo "Participant '$id' already exists. Skipping registration."
      else
        echo "Participant '$id' not found. Registering..."
        curl -X POST \
          -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
          -H "X-Goog-User-Project: my-project" \
          -H "Content-Type: application/json" \
          -d "{
            \"displayName\": \"$name\",
            \"activePublicAssentKey\": {
              \"publicKey\": \"$pubkey_b64\",
              \"algorithm\": \"PUBLIC_KEY_SIGNATURE_ALGORITHM_ECDSA_SECP256K1\"
            }
          }" \
          "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers?participant_id=$id" | jq
      fi
    }
    
    echo "Registering Signers..."
    for ID in signer-alice signer-bob signer-charlie; do
      provision_participant "$ID" "Signer $ID"
    done
    
    echo "Registering Policy Authors..."
    for ID in author-dave author-eve; do
      provision_participant "$ID" "Author $ID"
    done
    

* * *

## Step 3: Configure Policy Engine

Configure the Policy Engine by setting up the trust bundle and creating policies.

### A. Initialize the Policy Author Trust Bundle

Define who the authorized Policy Authors are. This is a singleton resource for the instance.

### curl
    
    
    # Get current sequence from the API. If null (initial state), fallback to 0.
    NEXT_BUNDLE_SEQUENCE=$(curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policyAuthorTrustBundle" \
      | jq -r '.sequenceNumber // 0')
    
    # Calculate higher sequence number.
    NEXT_BUNDLE_SEQUENCE=$((NEXT_BUNDLE_SEQUENCE + 1))
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "sequenceNumber": '"$NEXT_BUNDLE_SEQUENCE"',
        "authors": [
          {"authorId": "'"author-dave"'"},
          {"authorId": "'"author-eve"'"}
        ]
      }' \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policyAuthorTrustBundle | jq
    

### B. Create a Policy (PENDING_ACTIVE)

Define a Policy ID (`ethereum-transfer-policy` or `bitcoin-psbt-policy`) and create a rule describing what actions are permitted. While you can configure many policies to govern different scenarios, this guide demonstrates setting up a policy for either Ethereum or Bitcoin transactions. By default, the Policy Engine is **Fail-Fast (Block by Default)** ; if no policy explicitly permits a transaction, it is denied.

Before creating or approving a policy, authors must sign a payload representing the intent. You can use the following helper functions to handle binary serialization and signing.

**Important:** **Quorum Signature Structure** : The signature must be generated over a SHA-256 digest of: `UTF8("action:ACTIVE\n") + UTF8(policy.name) + UTF8("sequence:") + LE_INT64(sequence_number) + serializeRuleCanonical(policy.rule)` For initial creation, use sequence `0`. Subsequent authors approve using the sequence returned by the server. `serializeRuleCanonical` for Cedar is: `UTF8("cedar_document:") + UTF8(rule.cedar_document)`. The Cedar policy string in the `sign_policy` call MUST match the `cedarDocument` in the API payload exactly, otherwise the API will fail with a signature validation error.

### Ethereum

This rule permits smaller Ethereum transfers (<= 2 ETH, represented as 2,000,000,000 Gwei) to a specific address for **Alice**.

**1\. Generate Quorum Signature**

**Using Cloud KMS:**
    
    
    sign_policy() {
      local author_id=$1
      local sequence=$2
      local cedar_doc=$3
      local policy_id=$4
      export _HELPER_POLICY_ID="$policy_id"
      export _HELPER_SEQUENCE="$sequence"
      export _HELPER_CEDAR_DOC="$cedar_doc"
      python3 -c "import os; p='my-project'; l='us-central1'; i='mpc-unit-bob-123'; pol=os.environ.get('_HELPER_POLICY_ID'); s=int(os.environ.get('_HELPER_SEQUENCE')); d=os.environ.get('_HELPER_CEDAR_DOC'); n=f'projects/{p}/locations/{l}/instances/{i}/policyEngine/policies/{pol}'; payload=b'action:ACTIVE\n'+n.encode('utf-8')+b'sequence:'+s.to_bytes(8,'little')+b'cedar_document:'+d.encode('utf-8'); open('payload.bin', 'wb').write(payload)"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${author_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=payload.bin \
        --signature-file=policy_sig.bin > /dev/null
      openssl base64 -A -in policy_sig.bin
    }
    
    # Sign as Author 1 (Sequence 0)
    QUORUM_SIGNATURE=$(sign_policy "author-dave" 0 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.to_address == "0x1111111111111111111111111111111111111111" && context.transaction.value_gwei <= 2000000000 };' "ethereum-transfer-policy")
    

**Using OpenSSL:**
    
    
    sign_policy() {
      local author_id=$1
      local sequence=$2
      local cedar_doc=$3
      local policy_id=$4
      export _HELPER_POLICY_ID="$policy_id"
      export _HELPER_SEQUENCE="$sequence"
      export _HELPER_CEDAR_DOC="$cedar_doc"
      python3 -c "import os; p='my-project'; l='us-central1'; i='mpc-unit-bob-123'; pol=os.environ.get('_HELPER_POLICY_ID'); s=int(os.environ.get('_HELPER_SEQUENCE')); d=os.environ.get('_HELPER_CEDAR_DOC'); n=f'projects/{p}/locations/{l}/instances/{i}/policyEngine/policies/{pol}'; payload=b'action:ACTIVE\n'+n.encode('utf-8')+b'sequence:'+s.to_bytes(8,'little')+b'cedar_document:'+d.encode('utf-8'); open('payload.bin', 'wb').write(payload)"
      openssl dgst -sha256 -sign "${author_id}_priv.pem" -out policy_sig.bin payload.bin
      openssl base64 -A -in policy_sig.bin
    }
    
    # Sign as Author 1 (Sequence 0)
    QUORUM_SIGNATURE=$(sign_policy "author-dave" 0 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.to_address == "0x1111111111111111111111111111111111111111" && context.transaction.value_gwei <= 2000000000 };' "ethereum-transfer-policy")
    

**2\. Call CreatePolicy API**
    
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/ethereum-transfer-policy"; then
      echo "Policy 'ethereum-transfer-policy' already exists. Skipping creation."
    else
      echo "Policy 'ethereum-transfer-policy' not found. Creating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "displayName": "Ethereum Transfer Permit Policy",
          "rule": {
            "cedarDocument": "permit(principal == User::\"alice\", action == Action::\"Transfer\", resource == Resource::\"mpc_operation\") when { context.transaction.to_address == \"0x1111111111111111111111111111111111111111\" && context.transaction.value_gwei <= 2000000000 };"
          },
          "createAuthorSignature": {
            "authorId": "'"author-dave"'",
            "signature": "'"$QUORUM_SIGNATURE"'",
            "approvalTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"
          }
        }' \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies?policy_id=ethereum-transfer-policy" | jq
    fi
    

### Bitcoin

This rule permits Bitcoin transfers using the `bitcoin.transaction.v2` schema (BIP 174 PSBT) where the net outbound transfer amount does not exceed 250,000 satoshis (`context.transaction.spend_amount_scaled <= 2500000`, or 0.0025 BTC normalized to 10-9 fixed decimal units) and the miner fee does not exceed 10,000 satoshis (`context.transaction.max_fee_atomic <= 100000`).
    
    
    permit(
      principal == User::"alice",
      action == Action::"Transfer",
      resource == Resource::"mpc_operation"
    )
    when {
      context.transaction.schema == "bitcoin.transaction.v2" &&
      context.transaction.spend_amount_scaled <= 2500000 &&
      context.transaction.max_fee_atomic <= 100000
    };
    

**1\. Generate Quorum Signature**

**Using Cloud KMS:**
    
    
    sign_policy() {
      local author_id=$1
      local sequence=$2
      local cedar_doc=$3
      local policy_id=$4
      export _HELPER_POLICY_ID="$policy_id"
      export _HELPER_SEQUENCE="$sequence"
      export _HELPER_CEDAR_DOC="$cedar_doc"
      python3 -c "import os; p='my-project'; l='us-central1'; i='mpc-unit-bob-123'; pol=os.environ.get('_HELPER_POLICY_ID'); s=int(os.environ.get('_HELPER_SEQUENCE')); d=os.environ.get('_HELPER_CEDAR_DOC'); n=f'projects/{p}/locations/{l}/instances/{i}/policyEngine/policies/{pol}'; payload=b'action:ACTIVE\n'+n.encode('utf-8')+b'sequence:'+s.to_bytes(8,'little')+b'cedar_document:'+d.encode('utf-8'); open('payload.bin', 'wb').write(payload)"
      gcloud kms asymmetric-sign \
        --version=1 \
        --key="${author_id}-key" \
        --keyring="mpc-assent-keys" \
        --location="us-central1" \
        --digest-algorithm=sha256 \
        --input-file=payload.bin \
        --signature-file=policy_sig.bin > /dev/null
      openssl base64 -A -in policy_sig.bin
    }
    
    # Sign as Author 1 (Sequence 0)
    QUORUM_SIGNATURE=$(sign_policy "author-dave" 0 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.schema == "bitcoin.transaction.v2" && context.transaction.spend_amount_scaled <= 2500000 && context.transaction.max_fee_atomic <= 100000 };' "bitcoin-psbt-policy")
    

**Using OpenSSL:**
    
    
    sign_policy() {
      local author_id=$1
      local sequence=$2
      local cedar_doc=$3
      local policy_id=$4
      export _HELPER_POLICY_ID="$policy_id"
      export _HELPER_SEQUENCE="$sequence"
      export _HELPER_CEDAR_DOC="$cedar_doc"
      python3 -c "import os; p='my-project'; l='us-central1'; i='mpc-unit-bob-123'; pol=os.environ.get('_HELPER_POLICY_ID'); s=int(os.environ.get('_HELPER_SEQUENCE')); d=os.environ.get('_HELPER_CEDAR_DOC'); n=f'projects/{p}/locations/{l}/instances/{i}/policyEngine/policies/{pol}'; payload=b'action:ACTIVE\n'+n.encode('utf-8')+b'sequence:'+s.to_bytes(8,'little')+b'cedar_document:'+d.encode('utf-8'); open('payload.bin', 'wb').write(payload)"
      openssl dgst -sha256 -sign "${author_id}_priv.pem" -out policy_sig.bin payload.bin
      openssl base64 -A -in policy_sig.bin
    }
    
    # Sign as Author 1 (Sequence 0)
    QUORUM_SIGNATURE=$(sign_policy "author-dave" 0 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.schema == "bitcoin.transaction.v2" && context.transaction.spend_amount_scaled <= 2500000 && context.transaction.max_fee_atomic <= 100000 };' "bitcoin-psbt-policy")
    

**2\. Call CreatePolicy API**
    
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/bitcoin-psbt-policy"; then
      echo "Policy 'bitcoin-psbt-policy' already exists. Skipping creation."
    else
      echo "Policy 'bitcoin-psbt-policy' not found. Creating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "displayName": "Bitcoin PSBT Permit Policy",
          "rule": {
            "cedarDocument": "permit(principal == User::\"alice\", action == Action::\"Transfer\", resource == Resource::\"mpc_operation\") when { context.transaction.schema == \"bitcoin.transaction.v2\" && context.transaction.spend_amount_scaled <= 2500000 && context.transaction.max_fee_atomic <= 100000 };"
          },
          "createAuthorSignature": {
            "authorId": "'"author-dave"'",
            "signature": "'"$QUORUM_SIGNATURE"'",
            "approvalTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"
          }
        }' \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies?policy_id=bitcoin-psbt-policy" | jq
    fi
    

### C. Approve Policy (Transition to ACTIVE)

If your policy setup requires M-of-N signatures, subsequent authors call `AddQuorumSignature`. 

To generate the signature, you must first retrieve the current sequence of the policy.

### Ethereum
    
    
    # 1. Get the policy state and sequence
    POLICY_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/ethereum-transfer-policy")
    
    POLICY_STATE=$(echo "$POLICY_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$POLICY_STATE" == "PENDING_ACTIVE" ]; then
      POLICY_SEQUENCE=$(echo "$POLICY_INFO" | jq -r '.globalSequence // 0')
      echo "Policy Sequence: $POLICY_SEQUENCE"
    
      # 2. Sign as Author 2
      QUORUM_SIGNATURE_SEQ=$(sign_policy "author-eve" $POLICY_SEQUENCE 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.to_address == "0x1111111111111111111111111111111111111111" && context.transaction.value_gwei <= 2000000000 };' "ethereum-transfer-policy")
    
      # 3. Call AddQuorumSignature
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/ethereum-transfer-policy",
          "signature": {
            "authorId": "'"author-eve"'",
            "signature": "'"$QUORUM_SIGNATURE_SEQ"'",
            "approvalTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"
          }
        }' \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/ethereum-transfer-policy:addQuorumSignature" | jq
    elif [ "$POLICY_STATE" == "ACTIVE" ]; then
      echo "Policy 'ethereum-transfer-policy' is already ACTIVE. Skipping signature."
    else
      echo "Policy 'ethereum-transfer-policy' is in an unknown or unexpected state: $POLICY_STATE"
    fi
    

### Bitcoin
    
    
    # 1. Get the policy state and sequence
    POLICY_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/bitcoin-psbt-policy")
    
    POLICY_STATE=$(echo "$POLICY_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$POLICY_STATE" == "PENDING_ACTIVE" ]; then
      POLICY_SEQUENCE=$(echo "$POLICY_INFO" | jq -r '.globalSequence // 0')
      echo "Policy Sequence: $POLICY_SEQUENCE"
    
      # 2. Sign as Author 2
      QUORUM_SIGNATURE_SEQ=$(sign_policy "author-eve" $POLICY_SEQUENCE 'permit(principal == User::"alice", action == Action::"Transfer", resource == Resource::"mpc_operation") when { context.transaction.schema == "bitcoin.transaction.v2" && context.transaction.spend_amount_scaled <= 2500000 && context.transaction.max_fee_atomic <= 100000 };' "bitcoin-psbt-policy")
    
      # 3. Call AddQuorumSignature
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/bitcoin-psbt-policy",
          "signature": {
            "authorId": "'"author-eve"'",
            "signature": "'"$QUORUM_SIGNATURE_SEQ"'",
            "approvalTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"
          }
        }' \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/bitcoin-psbt-policy:addQuorumSignature" | jq
    elif [ "$POLICY_STATE" == "ACTIVE" ]; then
      echo "Policy 'bitcoin-psbt-policy' is already ACTIVE. Skipping signature."
    else
      echo "Policy 'bitcoin-psbt-policy' is in an unknown or unexpected state: $POLICY_STATE"
    fi
    

* * *

## Step 4: Create a Key

We now create a key ring and generate a distributed key.

### A. Create KeyRing

Logical grouping for your MPC keys.

### curl
    
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring"; then
      echo "KeyRing 'my-key-ring' already exists. Skipping creation."
    else
      echo "KeyRing 'my-key-ring' not found. Creating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{}' \
      https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings?key_ring_id=my-key-ring | jq
    fi
    

### B. Generate Distributed Key (DKG)

Initiate an asynchronous ceremony to generate a distributed key across participants.

### curl
    
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key"; then
      echo "Key 'my-key' already exists. Skipping generation."
    else
      echo "Key 'my-key' not found. Generating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "threshold": 2,
          "algorithm": "ECDSA_SECP256K1",
          "participantShares": [
            {"participantId": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/signer-alice"},
            {"participantId": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/signer-bob"},
            {"participantId": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/signer-charlie"}
          ]
        }' \
      https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys?key_id=my-key | jq
    fi
    

This returns a long-running operation (LRO). You must wait for the Key `state` to become `ACTIVE` (which means DKG ceremony has succeeded).

#### 🕵️‍♂️ Check Key State (Polling)

Poll the key status by running the following command periodically until the `state` field in the response becomes `ACTIVE` (indicating the DKG ceremony has succeeded).

### curl
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key | jq
    

### C. Derive Blockchain Address & Locate UTXOs

After your distributed key becomes `ACTIVE`, the MPC key is ready to use. In this step, you derive the blockchain-specific address from the 65-byte uncompressed public key returned by the MPC key generation (`0x04 || X || Y`), and locate any unspent funds needed for transactions.

### Ethereum

Ethereum addresses are derived from the Keccak-256 hash of the 64-byte uncompressed public key point (`pub_bytes[1:]`), taking the last 20 bytes.

#### Address Derivation Script (`derive_address.py`)

Execute the following block to create and run `derive_address.py`:
    
    
    cat <<'EOF' > derive_address.py
    import base64
    from eth_utils import keccak, to_checksum_address
    
    # Insert your base64 public_key from Step 4.B
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

Before broadcasting in Step 6, ensure your derived Ethereum address has enough Sepolia testnet ETH to cover the transaction value and gas costs. You can request free testnet ETH by entering your newly derived address into the [Faucet for Ethereum Sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia).

### Bitcoin

Bitcoin addresses are derived from the uncompressed 65-byte `secp256k1` EC public key (`0x04 || X || Y`). Multiple address formats are supported from the same public key:

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
    
    # Insert the Base64-encoded public key from Step 4.B (publicKey field, decodes to 65 raw bytes)
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

Unlike account-based blockchains, Bitcoin transactions spend specific unspent transaction outputs (UTXOs). Before constructing a transaction in Step 5:

  1. Fund your derived Native SegWit address (for example, using a testnet faucet).
  2. Query your address's unspent UTXOs using your Bitcoin node (`bitcoin-cli listunspent 1 9999999 "[\"tb1q...\"]"`) or a block explorer API.
  3. Note the following 4 parameters for Step 5: 
     * **`txid`** : The 32-byte transaction hash of the unspent output.
     * **`vout`** : The zero-indexed output index (for example, `0` or `1`).
     * **`value`** : The unspent amount in satoshis (for example, `200000` satoshis = 0.002 BTC).
     * **`scriptPubKey`** : The locking script hex (for example, `0014...`).



* * *

## Step 5: Execute an MPC Operation

Execute an MPC operation by evaluating a transaction and creating a proposal.

### A. Evaluate Transaction (Get Authorization Token)

Before signing an MPC operation, authorize the payload against your policies to receive a JWS token and the 32-byte signing digest.

### Ethereum

#### 🛑 Case A: Rejection (Too High Value)

Attempt to authorize a transaction of **3 ETH** (exceeds our 2 ETH limit).
    
    
    # Payload for 3 ETH (Hex equivalent contains value_gwei > 2B)
    RAW_TX_BYTES_HEX="ef808504a817c8008252089411111111111111111111111111111111111111118829a2241af62c00008083aa36a78080"
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "principal": "User::\"alice\"",
        "action": "Action::\"Transfer\"",
        "resource": "Resource::\"mpc_operation\"",
        "schema": "ETHEREUM_TX_V1",
        "payload": "'"$RAW_TX_BYTES_HEX"'"
      }' \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine:authorizePayload | jq
    

Expected Response: `decision: DENY`

#### ✅ Case B: Approval (Permitted Value)

Attempt to authorize a transaction of **1 Gwei** (within our 2 ETH limit).
    
    
    # Payload for 1 Gwei
    RAW_TX_BYTES_HEX="eb808504a817c800825208941111111111111111111111111111111111111111843b9aca008083aa36a78080"
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "principal": "User::\"alice\"",
        "action": "Action::\"Transfer\"",
        "resource": "Resource::\"mpc_operation\"",
        "schema": "ETHEREUM_TX_V1",
        "payload": "'"$RAW_TX_BYTES_HEX"'"
      }' \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine:authorizePayload)
    
    echo "$RESPONSE" | jq
    
    # Automatically capture variables for next steps
    DIGEST_HEX=$(echo "$RESPONSE" | jq -r .digest)
    POLICY_ENGINE_TOKEN=$(echo "$RESPONSE" | jq -r .token)
    
    # Convert to Base64 (which curl expects for bytes fields)
    DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    POLICY_ENGINE_TOKEN_B64=$(python3 -c "import base64; print(base64.b64encode('$POLICY_ENGINE_TOKEN'.encode('utf-8')).decode('utf-8'))")
    

Expected Response: `decision: PERMIT` along with a `token`.

### Bitcoin

In the Bitcoin UTXO model, transactions spend specific unspent outputs. In SegWit (BIP 143), calculating the signature hash requires knowing the satoshi amount and locking script of the input being spent. 

The Policy Engine requires BIP 174 PSBT v0 format (`BITCOIN_TX_V2`) with `PSBT_IN_WITNESS_UTXO` populated for each input.

**Important:** **Change Output and Satoshi Accounting** : In Bitcoin, any unallocated difference (`InputSatoshis - RecipientSatoshis - MinerFeeSatoshis`) is claimed by miners. To prevent losing funds, transactions must explicitly allocate a **Change Output** returning the unspent balance back to the sender's own derived Native SegWit address.

#### PSBT Construction Script (`build_psbt.py`)

Execute the following block to assemble a valid BIP 174 PSBT v0 payload:
    
    
    cat <<'EOF' > build_psbt.py
    """Constructs a BIP 174 PSBT v0 payload using embit for Bitcoin policy evaluation."""
    
    from embit import script, transaction
    from embit.psbt import PSBT
    
    # 1. Inputs (From Step 4.C)
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

Attempt to authorize a transaction where the miner fee exceeds the 10,000 satoshi policy limit. In this example, setting `MINER_FEE_SATS = 15000` (and `CHANGE_SATS = 135000`) in `build_psbt.py` scales to `max_fee_atomic = 150000` (exceeding the policy cap of `100000`), producing the following payload that triggers a `DENY` decision from the Policy Engine.
    
    
    # Construct a PSBT payload with miner_fee_sats = 15000 -> max_fee_atomic = 150000 (exceeds 100000 limit)
    REJECTED_PSBT_HEX="70736274ff0100710200000001d81639a6635e3921442629bc7f51f22ca9e4ca3d27c280c9f1936915334f598f0100000000ffffffff0250c3000000000000160014751e76e8199196d454941c45d1b3a323f1433bd6580f020000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000000001011f400d030000000000160014eced05cd51d964102a20c856b09080ad620e9da2000000"
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "principal": "User::\"alice\"",
        "action": "Action::\"Transfer\"",
        "resource": "Resource::\"mpc_operation\"",
        "schema": "BITCOIN_TX_V2",
        "payload": "'"$REJECTED_PSBT_HEX"'"
      }' \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine:authorizePayload | jq
    

Expected Response: `decision: DENY`

#### ✅ Case B: Approval (Permitted Bitcoin PSBT)

Attempt to authorize the previously constructed valid PSBT (`RECIPIENT_SATS = 50000` maps to `spend_amount_scaled = 500000 <= 2500000` and `MINER_FEE_SATS = 250` maps to `max_fee_atomic = 2500 <= 100000`).
    
    
    RESPONSE=$(curl -s -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      -H "Content-Type: application/json" \
      -d '{
        "principal": "User::\"alice\"",
        "action": "Action::\"Transfer\"",
        "resource": "Resource::\"mpc_operation\"",
        "schema": "BITCOIN_TX_V2",
        "payload": "'"$BTC_PSBT_HEX"'"
      }' \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine:authorizePayload)
    
    echo "$RESPONSE" | jq
    
    # Automatically capture variables for next steps
    DIGEST_HEX=$(echo "$RESPONSE" | jq -r .digest)
    POLICY_ENGINE_TOKEN=$(echo "$RESPONSE" | jq -r .token)
    
    # Convert to Base64 (which curl expects for bytes fields)
    DIGEST_B64=$(python3 -c "import base64; print(base64.b64encode(bytes.fromhex('$DIGEST_HEX')).decode('utf-8'))")
    POLICY_ENGINE_TOKEN_B64=$(python3 -c "import base64; print(base64.b64encode('$POLICY_ENGINE_TOKEN'.encode('utf-8')).decode('utf-8'))")
    

Expected Response: `decision: PERMIT` along with a JWS `token` and 32-byte BIP 143 sighash `digest`.

This returns:

  * `decision`: `PERMIT` or `DENY`
  * `token`: The JWS policy token (Proof of compliance).
  * `digest`: The hex-encoded 32-byte signing digest.
  * `evaluatedPolicyIds`: Policies that were evaluated that affected the decision.



### B. Create Proposal (Initiate Signing)

Offer the digest payload for signing, attaching the Policy Engine token received in Step 5A.

**Note:** Steps 5B, 5C, and 5D operate identically across blockchain architectures (Ethereum, Bitcoin, etc.) because the MPC threshold keys sign the normalized 32-byte digest directly.

### curl
    
    
    # Check existence
    if curl -s -f -o /dev/null -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal"; then
      echo "Proposal 'my-proposal' already exists. Skipping creation."
    else
      echo "Proposal 'my-proposal' not found. Creating..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "digest": "'"$DIGEST_B64"'",
          "keyVersion": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/versions/1",
          "initiator": "projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/signer-alice",
          "policyApproverSignature": "'"$POLICY_ENGINE_TOKEN_B64"'"
        }' \
      https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals?proposal_id=my-proposal | jq
    fi
    

**Important:** Ensure the digest bytes pass to the API match the content evaluated in Policy Engine, otherwise the token signature will fail validation.

This returns a long-running operation (LRO). The expected Proposal `state` will be `PENDING_ASSENT` (indicating it is ready for participants to sign).

#### 🕵️‍♂️ Check Proposal State (Polling)

Poll the proposal status by running the following command periodically.

### curl
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal | jq
    

### C. Record Participant Decisions (Assent)

Participants must sign off on the proposal hash with their local private keys (Key Shares) and forward the assent.

#### 1\. Sign Proposal Digest

### Cloud KMS
    
    
    sign_digest() {
      local signer_id=$1
      local digest_hex=$2
    
      local digest_b64=$(python3 -c "import base64, sys; print(base64.b64encode(bytes.fromhex('$digest_hex')).decode('utf-8'))")
    
      # Direct API calls are used here because the input is already a pre-computed 32-byte digest from the MPC.
      # Tools like gcloud assume input is raw data and apply a redundant hashing layer, altering the payload.
      # Unlike Policy signings which hash raw administrative text, Proposal signatures must sign this exact 32-byte hash as-is.
      curl -s -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json" \
        -d "{\"digest\": {\"sha256\": \"$digest_b64\"}}" \
      https://cloudkms.googleapis.com/v1/projects/my-project/locations/us-central1/keyRings/mpc-assent-keys/cryptoKeys/${signer_id}-key/cryptoKeyVersions/1:asymmetricSign | jq -r .signature
    }
    
    SIGNER_2_SIG_B64=$(sign_digest "signer-bob" "$DIGEST_HEX")
    SIGNER_3_SIG_B64=$(sign_digest "signer-charlie" "$DIGEST_HEX")
    

### OpenSSL
    
    
    sign_digest() {
      local signer_id=$1
      local digest_hex=$2
    
      python3 -c "import sys; sys.stdout.buffer.write(bytes.fromhex('$digest_hex'))" > digest.bin
    
      openssl pkeyutl -sign -inkey "${signer_id}_priv.pem" -in digest.bin -out digest_sig.bin
    
      openssl base64 -A -in digest_sig.bin
    }
    
    SIGNER_2_SIG_B64=$(sign_digest "signer-bob" "$DIGEST_HEX")
    SIGNER_3_SIG_B64=$(sign_digest "signer-charlie" "$DIGEST_HEX")
    

#### 2\. Record Decision

### curl
    
    
    # 1. Check state for Signer 2
    PROPOSAL_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal")
    
    PROPOSAL_STATE=$(echo "$PROPOSAL_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$PROPOSAL_STATE" == "PENDING_ASSENT" ]; then
      echo "Recording assent for Signer 2..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "signature": "'"$SIGNER_2_SIG_B64"'",
          "decision": "ASSENT",
          "participant": "signer-bob"
        }' \
      https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal:recordParticipantDecision | jq
    elif [ "$PROPOSAL_STATE" == "READY" ] || [ "$PROPOSAL_STATE" == "SUCCEEDED" ]; then
      echo "Proposal is in state $PROPOSAL_STATE. Skipping Signer 2."
    else
      echo "Proposal is in an unknown or unexpected state: $PROPOSAL_STATE"
    fi
    
    # 2. Re-check state for Signer 3 (Signer 2 might have triggered a state change)
    PROPOSAL_INFO=$(curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
      "https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal")
    
    PROPOSAL_STATE=$(echo "$PROPOSAL_INFO" | jq -r '.state // "UNKNOWN"')
    
    if [ "$PROPOSAL_STATE" == "PENDING_ASSENT" ]; then
      echo "Recording assent for Signer 3..."
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "X-Goog-User-Project: my-project" \
        -H "Content-Type: application/json" \
        -d '{
          "signature": "'"$SIGNER_3_SIG_B64"'",
          "decision": "ASSENT",
          "participant": "signer-charlie"
        }' \
      https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal:recordParticipantDecision | jq
    elif [ "$PROPOSAL_STATE" == "READY" ] || [ "$PROPOSAL_STATE" == "SUCCEEDED" ]; then
      echo "Proposal is in state $PROPOSAL_STATE. Skipping Signer 3."
    else
      echo "Proposal is in an unknown or unexpected state: $PROPOSAL_STATE"
    fi
    

### D. Fetch Final Signature

Once the threshold of assents is reached, check the proposal state or fetch the signature.

### curl
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal | jq
    

If the proposal is in a `SUCCEEDED` state, look into the `finalSignature` field inside the returned JSON.

* * *

## Step 6: Broadcast Transaction to Blockchain

Once your proposal reaches the `SUCCEEDED` state and you have fetched the `finalSignature`, the last step is to construct the signed wire transaction and broadcast it to the network.

### Ethereum

### Recovery Identifier Derivation & Broadcasting

The MPC API returns a raw 64-byte ECDSA signature (comprising the `r` and `s` values). The server ensures that the signature is in canonical low-s form (EIP-2). However, Ethereum requires a Recovery Identifier (`v`) to derive the sender's address and verify the signature, which is not directly returned in standard 64-byte MPC signatures.

The following Python script handles this complexity. It dynamically determines the correct recovery bit by matching your expected sender address, constructs the valid transaction, and broadcasts it to the network.

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

  * **`invalid sender: recovery failed` or `invalid transaction v, r, s values`:** This occurs if the transaction parameters in your script don't _exactly_ match the payload that was signed. Ensure the `value`, `nonce`, and `to` fields match what was processed in Step 5.
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

Use these read-only commands to inspect the state of your resources at any time.

* * *

### 👥 1. Participants & Signers

Inspect participants and signers in your instance.

#### A. List all registered participants

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers | jq
    

#### B. Get details for a specific participant

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/signers/signer-alice | jq
    

* * *

### 📜 2. Policy Engine

Inspect policies and trust bundles.

#### A. Get the Policy Author Trust Bundle

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policyAuthorTrustBundle | jq
    

#### B. List all Policies

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies | jq
    

#### C. Get details for a specific Policy

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/policyEngine/policies/ethereum-transfer-policy | jq
    

* * *

### 🔑 3. Keys & KeyRings

Inspect key rings and keys.

#### A. List all KeyRings

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings | jq
    

#### B. List all Keys in a KeyRing

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys | jq
    

#### C. Get status of a specific Distributed Key (DKG Status)

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key | jq
    

* * *

### 📝 4. Proposals (Signing Operations)

Inspect proposals and signing status.

#### A. List all Proposals for a Key

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals | jq
    

#### B. Get details or status of a specific Proposal

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "X-Goog-User-Project: my-project" \
    https://67317436-0f29-ba9e-9146-d11c0bd8df9b.us-central1.mpc.goog/v1alpha1/projects/my-project/locations/us-central1/instances/mpc-unit-bob-123/mpc/keyRings/my-key-ring/keys/my-key/proposals/my-proposal | jq
    

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


