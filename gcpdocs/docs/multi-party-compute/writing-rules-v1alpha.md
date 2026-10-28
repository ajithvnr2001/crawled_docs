---
url: https://docs.cloud.google.com/multi-party-compute/writing-rules-v1alpha/
title: Writing Cedar rules \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:37:14.259995+00:00
---

# Writing Cedar rules  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/writing-rules-v1alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)



#  Writing Cedar rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This page covers the deprecated `v1alpha1` API and will be removed in December 2026. For the `v1beta` API, see [Write transaction policy rules](https://docs.cloud.google.com/multi-party-compute/writing-rules).

This page describes how to author Cedar policy rules to validate transactions in the Multi-Party Compute (MPC) Policy Engine.

The Policy Engine decodes incoming transaction payloads inside a secure Trusted Execution Environment (TEE) and projects the transacting intent attributes onto the Cedar evaluation context.

## Cedar rule structure

When writing Cedar rules for the Policy Engine, you specify a rule using a nested set of conditions:

  * **Principal** : The logical identity of the transaction requester (the initiator of the transaction) within the Multi-Party Compute workspace (for example, `User::"alice"`), rather than the Google Cloud IAM identity (user or service account) calling the API.
  * **Action** : The requested cryptographic action (for example, `Action::"sign_transaction"`).
  * **Resource** : The target asset or operation class being operated upon (for example, `Resource::"mpc_operation"`).
  * **Context** : The parsed transaction metadata and parameters (accessible under `context.transaction`).



* * *

## Ethereum transaction schema reference

The protocol-agnostic framework allows rules to omit the schema check to remain reusable across different blockchain networks. However, to explicitly restrict a rule to Ethereum transaction payloads, check: `context.transaction.schema == "ethereum.transaction.v2"`.

The following attributes are supported inside the `context.transaction` record:

Attribute | Type | Description  
---|---|---  
`schema` | String | The format schema. For Ethereum transactions, this is always `"ethereum.transaction.v2"`.  
`operation` | String |  The transacting operation type. Supported values: 

  * `"NATIVE_TRANSFER"`: A direct transfer of the main chain currency (such as ETH).
  * `"TOKEN_TRANSFER"`: An ERC-20 token transfer (such as USDC, USDT, DAI).
  * `"TOKEN_APPROVE"`: An ERC-20 token approval to let a contract spend tokens.
  * `"CONTRACT_CALL"`: A generic smart contract interaction (like staking or swapping).

  
`chain_id` | String | The target blockchain network ID (for example, `"1"` for Ethereum Mainnet or `"11155111"` for Sepolia Testnet).  
`asset_symbol` | String | The ticker symbol of the token being transferred (for example, `"ETH"`, `"USDC"`, `"DAI"`, or `"WBTC"`). Unlisted tokens return `"UNKNOWN"`.  
`asset_contract_address` | String | The smart contract address of the ERC-20 token (in mixed-case EIP-55 checksum format). This resolves to an empty string (`""`) for standard ETH transfers.  
`recipient` | String | The destination recipient address (in mixed-case EIP-55 checksum format). For token approvals, this represents the spender address.  
`spend_amount_scaled` | Long |  The token transfer amount normalized to a fixed 9-decimal precision (nanocoin format), removing the need to track varying token decimals (such as 6, 8, or 18) when writing rules.   
  
**How to calculate:** Multiply the human-readable asset amount (e.g., 1.5 ETH or 5,000 USDC) by 1,000,000,000 (109) to get the value for your rule: 

  * `0.1` ETH → `100000000` (0.1 × 109)
  * `1.0` of any asset → `1000000000` (1.0 × 109)
  * `5,000` USDC → `5000000000000` (5,000 × 109)

  
`spend_amount_dust` | Long | The leftover remainder of the transaction amount that falls below the 9-decimal precision threshold. For assets with more than 9 decimals (such as ETH, which has 18), this contains the unscaled sub-Gwei value (the remaining Wei). This is always `0` for assets with 9 or fewer decimals (such as USDC or WBTC).  
`max_fee_atomic` | Long | The maximum total transaction fee cap (scaled by 109, representing Gwei).  
`gas_limit` | Long | The maximum amount of gas allocated for transaction execution.  
`destination_type` | String | The classification of the recipient address. Supported values: `"EOA"` (standard user wallet), `"CONTRACT"` (smart contract), or `"INTERNAL_TREASURY"` (an internal vault).  
`temporal_validity` | Long | The transaction account nonce (used to prevent transaction replay attacks).  
  
* * *

## Bitcoin transaction schema reference

To explicitly restrict a rule to Bitcoin BIP 174 PSBT transaction payloads, check: `context.transaction.schema == "bitcoin.transaction.v2"`.

The following attributes are supported inside the `context.transaction` record:

Attribute | Type | Description  
---|---|---  
`schema` | String | The format schema. For Bitcoin transactions, this is always `"bitcoin.transaction.v2"`.  
`operation` | String |  The transacting operation type. Supported values: 

  * `"NATIVE_TRANSFER"`: A direct transfer of Bitcoin (BTC).
  * `"OP_RETURN"`: An unspendable data anchoring / null data output.

  
`chain_id` | String | The target network Bech32 Human-Readable Part (HRP): `"bc"` (Bitcoin Mainnet), `"tb"` (Testnet / Testnet4), or `"bcrt"` (Regtest).  
`asset_symbol` | String | The asset ticker symbol: `"BTC"`.  
`recipient` | String | The primary destination address. For `OP_RETURN` transactions, this is `"unaddressable"`. For internal consolidation sweeps (100% change), this resolves to the first change address.  
`spend_amount_scaled` | Long |  The net outbound transfer amount normalized to fixed 9-decimal precision (10-9 units). Because 1 satoshi equals 10 nanocoin units (1 sat = 10 units, 1 BTC = 109 units), internal change amounts are excluded. For internal sweeps / 100% change transactions, this evaluates to `0`.   
`max_fee_atomic` | Long | The calculated miner fee cap normalized to 9-decimal precision: (∑ Inputs − ∑ Outputs) × 10.  
`destination_type` | String | The classification of the recipient script. Supported values: `"P2WPKH"` (Native SegWit), `"P2TR"` (Taproot), `"P2PKH"` (Legacy), `"P2SH"` (Nested SegWit / Script Hash), `"TREASURY_CHANGE"` (internal change sweep), or `""`.  
`temporal_validity` | Long | The transaction `nLockTime` field.  
`outputs` | Set<Record> | The normalized set of all transaction outputs: `[{ address: String, amount_scaled: Long, is_change: Bool }]`.  
  
### Core Bitcoin policy concepts

  1. **Universal 9-Decimal Scaling Math** : Amounts in Bitcoin policies use normalized 9-decimal nanocoin precision (1 sat = 10 units, 1 BTC = 109 units):

**Amount scaled = Satoshis × 10 = BTC × 109**

     * `0.0005` BTC (50,000 satoshis) → `500000` (50,000 × 10)
     * `0.0025` BTC (250,000 satoshis) → `2500000` (250,000 × 10)
     * `1.0` BTC (100,000,000 satoshis) → `1000000000` (100,000,000 × 10)
  2. **Change Output Separation** : The parser inspects BIP-32 derivation paths (`m/.../1/*`) and correlates input scripts to automatically identify internal change outputs. Change amounts are excluded from `spend_amount_scaled`, ensuring that spending limit policies evaluate strictly against net outbound value transferred to third parties.

  3. **Single Non-Change Recipient Rule** : To prevent ambiguous multi-recipient routing attacks, transactions containing multiple distinct external third-party recipients fail closed (`ErrUnsupportedTx`).




* * *

## Cedar rule examples

The following examples demonstrate how to configure allowlists, limit rules, and replay bounds using Cedar for Ethereum and Bitcoin transactions.

### Ethereum examples

The following rules illustrate common policy patterns for Ethereum and ERC-20 transactions.

#### 1\. Direct ETH transfer limit

This rule permits Alice to transfer base chain ETH, checking that the scaled transfer amount does not exceed 1.0 ETH (1,000,000,000 scaled Gwei units).
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.operation == "NATIVE_TRANSFER" &&
        context.transaction.asset_symbol == "ETH" &&
        context.transaction.spend_amount_scaled <= 1000000000
    };
    

#### 2\. ERC-20 token allowlist rule

This rule permits USDC token transfers up to 5,000 USDC. It restricts transfers to a recipient address on an allowlist. Note that because Cedar strings are case-sensitive, the recipient address must match the mixed-case EIP-55 format.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.operation == "TOKEN_TRANSFER" &&
        context.transaction.asset_symbol == "USDC" &&
        context.transaction.recipient == "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B" &&
        context.transaction.spend_amount_scaled <= 5000000000000
    };
    

#### 3\. Smart contract and DeFi call fallbacks

This rule permits general contract interactions (such as staking or swapping) without amount restrictions, provided they are not asset-spending transfer operations.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.operation == "CONTRACT_CALL"
    };
    

#### 4\. Strict replay protection (Chain ID boundary)

To prevent transaction replay attacks where a payload signed for a testnet chain is re-submitted on production mainnets, you can scope your rule to a specific Chain ID (e.g. `11155111` for Sepolia).
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.chain_id == "11155111"
    };
    

### Bitcoin examples

The following rules illustrate common policy patterns for Bitcoin PSBT transactions.

#### 1\. Spending limit and miner fee cap

This rule permits direct Bitcoin (BTC) transfers where the net outbound transfer amount does not exceed 0.0025 BTC (250,000 satoshis → 2,500,000 scaled units) and the miner fee does not exceed 10,000 satoshis (100,000 atomic units).
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.operation == "NATIVE_TRANSFER" &&
        context.transaction.asset_symbol == "BTC" &&
        context.transaction.spend_amount_scaled <= 2500000 &&
        context.transaction.max_fee_atomic <= 100000
    };
    

#### 2\. SegWit (`P2WPKH`) and Taproot (`P2TR`) address allowlist

This rule restricts Bitcoin transfers to an approved SegWit or Taproot destination address.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.schema == "bitcoin.transaction.v2" &&
        (context.transaction.destination_type == "P2WPKH" || context.transaction.destination_type == "P2TR") &&
        context.transaction.recipient == "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
    };
    

#### 3\. UTXO consolidation and treasury sweep

This rule permits internal UTXO consolidation sweeps where all outputs return to internal change addresses (`destination_type == "TREASURY_CHANGE"` and `spend_amount_scaled == 0`), while bounding the consolidation fee.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.schema == "bitcoin.transaction.v2" &&
        context.transaction.destination_type == "TREASURY_CHANGE" &&
        context.transaction.spend_amount_scaled == 0 &&
        context.transaction.max_fee_atomic <= 50000
    };
    

#### 4\. Output set inspection

This rule validates that the transaction output set contains a specific destination output and amount.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.outputs.contains({
            address: "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
            amount_scaled: 500000,
            is_change: false
        })
    };
    

#### 5\. Network scoping (Mainnet versus Testnet)

This rule scopes authorization to Bitcoin Testnet (`tb`) transactions, preventing execution on Bitcoin Mainnet (`bc`).
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.schema == "bitcoin.transaction.v2" &&
        context.transaction.chain_id == "tb"
    };
    

#### 6\. `OP_RETURN` data anchoring

This rule permits unspendable `OP_RETURN` data anchoring transactions (`spend_amount_scaled == 0` and `recipient == "unaddressable"`), enforcing a strict fee cap.
    
    
    permit (
        principal == User::"alice",
        action == Action::"sign_transaction",
        resource == Resource::"mpc_operation"
    )
    when {
        context.transaction.operation == "OP_RETURN" &&
        context.transaction.recipient == "unaddressable" &&
        context.transaction.spend_amount_scaled == 0 &&
        context.transaction.max_fee_atomic <= 10000
    };
    

* * *

## Parser safety defenses

To safeguard transacting operations in production environments, the Policy Engine parses payloads strictly and rejects invalid structures at the gateway layer before evaluating any Cedar rules:

  * **Zero-value base currency enforcement:** The parser explicitly rejects Ethereum token transfer operations (`TOKEN_TRANSFER`) that also attempt to bundle non-zero base transfer assets. This prevents malicious payloads from transferring standard base asset values while presenting the transaction as a standard token transfer.
  * **UTXO and Witness Verification:** For Bitcoin PSBT transactions, the parser validates that all inputs supply valid `witness_utxo` data, preventing fee calculation spoofing or unverified signing.
  * **Change Output Script Verification:** Internal change outputs must match an input script pubkey or known BIP-32 change path (`m/.../1/*`). Payloads attempting to spoof change outputs to third-party addresses fail closed.
  * **Single External Recipient Enforcement:** Bitcoin payloads containing multiple external non-change destination addresses fail closed (`ErrUnsupportedTx`) to prevent ambiguous multi-recipient policy authorization.
  * **Integer Overflow and Underflow Protection:** Nonces, locktimes, gas or fee caps, and amounts that exceed safety bounds (`MaxInt64`) or produce underflows (such as total output value exceeding total input value) are immediately rejected.
  * **Missing Fee Verification:** Transactions that fail to define proper miner fees or gas parameters fail closed automatically.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
