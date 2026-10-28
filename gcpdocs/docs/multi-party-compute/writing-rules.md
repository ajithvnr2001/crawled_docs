---
url: https://docs.cloud.google.com/multi-party-compute/writing-rules/
title: Write transaction policy rules \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:40.196974+00:00
---

# Write transaction policy rules  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/writing-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Write transaction policy rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the attributes that a transaction policy can check, and shows example rules for Ethereum (`ETHEREUM_TX_V2` and `EIP712_TYPED_DATA_V1`), Bitcoin (`BITCOIN_TX_V2`), and Solana (`SOLANA_TX_V1`) transactions.

To learn how policies are combined, which policies are enforced, and why a transaction is denied, see [Transaction policy evaluation](https://docs.cloud.google.com/multi-party-compute/policy-evaluation).

## Rule structure

A transaction policy is a single [Cedar](https://docs.cedarpolicy.com/) `permit` or `forbid` statement over the principal, action, resource, and context:
    
    
    permit (
      principal,
      action == Action::"buy_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context.principal_keyring == "institutional-treasury" &&
      context.schema == "ETHEREUM_TX_V2" &&
      context has amount_token_scaled && context.amount_token_scaled <= 1000000000
    };
    

Keep the following in mind:

  * **Attributes are at the top level of the context.** Write `context.amount_token_scaled`, not `context.transaction.spend_amount_scaled` as in `v1alpha1`.
  * **Some attributes are optional.** An optional attribute that isn't in the context makes the policy fail to evaluate, and a policy that fails to evaluate doesn't match. Check for an optional attribute with `has` before you read it, or with `unless { context has ... }` in a `forbid` rule. For more information, see [Scenario 6](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#scenario-6) and [Scenario 8](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#scenario-8).
  * **Cedar strings are case-sensitive.** Compare addresses in the format that the table for each chain describes.



For the principal, see [The Cedar request](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#cedar-request). For the actions that `CreateTransaction` accepts (`buy_transaction`, `sell_transaction`, and `internal_transfer_transaction`), see [Action and resource](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#action-and-resource).

## Context attributes

Each transaction's context has the attributes decoded from its payload, the IDs of the signing key and its KeyRing, and the [metadata attributes](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#context) (`fiat_amount`, `validity`, `principal_value1`, and `principal_value2`) that the initiator sets.

The payload attributes are the same for every blockchain. The following table describes all context attributes, and the tables for Ethereum, Bitcoin, and Solana describe how Multi-party Compute populates each attribute for that blockchain:

Attribute | Cedar type | Always present? | Value  
---|---|---|---  
`schema` | `String` | Yes | The payload format: `"ETHEREUM_TX_V2"`, `"BITCOIN_TX_V2"`, `"SOLANA_TX_V1"`, or `"EIP712_TYPED_DATA_V1"`. For more information, see Schema names.  
`blockchain` | `String` | Yes | `"ETH"`, `"BTC"`, or `"SOL"`.  
`principal_keyring` | `String` | Yes | The ID of the KeyRing that holds the signing key, for example `"treasury"`.  
`principal_key` | `String` | Yes | The ID of the signing key, for example `"hot-wallet-1"`.  
`secondary_key` | `String` | Yes | The destination address, token or NFT recipient, approved spender or operator, or EIP-712 counterparty decoded from the payload.  
`amount_token_scaled` | `Long` | No | The fungible amount transferred or approved, in units of 10-9 of the asset. Omitted when no fungible amount is transferred, for example an ERC-721 operation or a contract call that sends no ETH. For more information, see Amounts.  
`token_symbol` | `String` | No | The symbol of the asset, for example `"ETH"`, `"BTC"`, `"SOL"`, or `"USDC"`. Omitted when the asset isn't one that Multi-party Compute recognizes, and for ERC-721 operations.  
`contract_address` | `String` | No | The ERC-20 or ERC-721 token contract or called contract (Ethereum), the verifying contract (EIP-712), or the mint (Solana). Omitted for native transfers.  
`token_standard` | `String` | No | `"ERC721"` for ERC-721 transfers and approvals (`ETHEREUM_TX_V2`). Omitted for native transfers and fungible token operations.  
`token_id` | `String` | No | The 256-bit ERC-721 `tokenId` as a base-10 string (`ETHEREUM_TX_V2`). Omitted for `setApprovalForAll` and for transactions that aren't ERC-721.  
`from_address` | `String` | No | The current owner (`from`) in ERC-721 `transferFrom` and `safeTransferFrom` calls, in mixed-case EIP-55 checksum format.  
`approve_all` | `Bool` | No | The `approved` flag in ERC-721 `setApprovalForAll(operator, approved)` calls: `true` when granting operator approval, `false` when revoking it.  
`deadline` | `Long` | No | The expiration time of an `EIP712_TYPED_DATA_V1` message, in seconds since the Unix epoch, from its `deadline`, `sigDeadline`, or `validBefore` field.  
`eip712` | `Record` | No | The structured EIP-712 payload: `primary_type`, `domain`, and `message`, with 256-bit integers as base-10 strings. `EIP712_TYPED_DATA_V1` only.  
`chain_id` | `Long` | No | The EVM chain ID, for example `1` for Ethereum Mainnet or `11155111` for Sepolia. Ethereum and EIP-712 only.  
`max_fee_atomic` | `Long` | Yes | The most that the transaction can pay in network fees, in units of 10-9 of the blockchain's native coin. `0` for `EIP712_TYPED_DATA_V1`.  
`payload` | `String` | Yes | The hex-encoded digest of the payload, in lowercase.  
`time_stamp` | `Long` | Yes | The transaction's `createTime`, in seconds since the Unix epoch.  
`key_lists` | `Record` of `Set<String>` | Yes | A record mapping each KeyList ID in the instance to the `Set<String>` of blockchain addresses in that KeyList, resolved at `createTime`. An empty record when the instance has no KeyLists. Read a KeyList with bracket syntax, for example `context.key_lists["trusted-destinations"]`. For more information, see [KeyLists in the Cedar context](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#keylist-syntax).  
  
`principal_keyring` and `principal_key` are IDs, not full resource names. A key ID is unique only within its KeyRing. Check `principal_keyring` to apply a rule to every key in a KeyRing, or both attributes to name one key:
    
    
    context.principal_keyring == "treasury" && context.principal_key == "hot-wallet-1"
    

If the payload can't be decoded by the parser for `Transaction.schema`, or can't be projected into a context, no policy is evaluated and the transaction is denied with `UNRECOGNIZED_PAYLOAD`. For more information, see [Deny reasons](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#deny-reasons).

### Schema names

The `schema` attribute is the name of the `PayloadSchema` value in the `v1beta` API: `"ETHEREUM_TX_V2"`, `"BITCOIN_TX_V2"`, `"SOLANA_TX_V1"`, or `"EIP712_TYPED_DATA_V1"`. The lowercase names that `v1alpha1` rules use, such as `"ethereum.transaction.v2"`, never match in `v1beta`.

A rule without a `schema` or `blockchain` check applies to every blockchain. To limit a rule to one blockchain, check `schema`.

### Amounts

`amount_token_scaled` and `max_fee_atomic` use the same scale for every asset: 1 unit is 10-9 of the asset, so 1.0 of any asset is `1000000000`. To get the value for a rule, multiply the amount by 1,000,000,000 (109). The following table shows some examples:

Amount | `amount_token_scaled`  
---|---  
0.1 ETH | `100000000`  
1.0 ETH, 1.0 BTC, 1.0 SOL, or 1.0 USDC | `1000000000`  
0.0025 BTC (250,000 satoshis) | `2500000`  
1.5 SOL (1,500,000,000 lamports) | `1500000000`  
5,000 USDC | `5000000000000`  
  
For assets with more than 9 decimal places, such as ETH, the part of the amount smaller than 10-9 is dropped. A rule can't check it.

### Ethereum

The following table describes the context attributes for `ETHEREUM_TX_V2` payloads (RLP-encoded legacy and EIP-2718 transactions, including EIP-1559):

Attribute | Value  
---|---  
`secondary_key` | For ETH transfers and contract calls, the transaction's `to` address. For ERC-20 `transfer` and `transferFrom`, and ERC-721 `transferFrom` and `safeTransferFrom`, the token or NFT recipient. For ERC-20 and ERC-721 `approve`, the approved spender. For ERC-721 `setApprovalForAll`, the operator. In mixed-case EIP-55 checksum format.  
`amount_token_scaled` | For ETH transfers and ERC-20 transfers and approvals, the amount. For contract calls, the ETH sent with the call; omitted if no ETH is sent. Always omitted for ERC-721 transfers and approvals, so that fungible spending limits don't match NFT token IDs.  
`token_symbol` | `"ETH"` for ETH transfers, and for contract calls that send ETH. For recognized ERC-20 tokens on Ethereum Mainnet, `"USDC"`, `"USDT"`, `"DAI"`, or `"WBTC"`; omitted for other tokens and for ERC-721 operations.  
`contract_address` | For ERC-20 and ERC-721 transfers and approvals, the token or NFT contract. For contract calls, the contract called. In mixed-case EIP-55 checksum format. Omitted for ETH transfers.  
`token_standard` | `"ERC721"` for ERC-721 transfers and approvals. Omitted for ETH transfers, ERC-20 operations, and other contract calls.  
`token_id` | For ERC-721 `transferFrom`, `safeTransferFrom`, and `approve`, the 256-bit `tokenId` as a base-10 `String`, so that NFT IDs never overflow Cedar's 64-bit `Long`. Because it's a `String`, compare it for equality with `==` or `in [...]`; `<` and `>` compare strings, not numbers. Omitted for `setApprovalForAll` and for transactions that aren't ERC-721.  
`from_address` | For ERC-721 `transferFrom` and `safeTransferFrom`, the current owner (`from`), in mixed-case EIP-55 checksum format.  
`approve_all` | For ERC-721 `setApprovalForAll(operator, approved)`, the `approved` flag as a `Bool`: `true` when granting the operator approval over every NFT in the collection, `false` when revoking it.  
`chain_id` | The chain ID from the transaction. Can be omitted on legacy transactions, so check it with `has`.  
`max_fee_atomic` | Gas limit × maximum fee per gas (or gas price for legacy transactions), in gwei.  
  
For ERC-20 `transfer(address, uint256)` (`0xa9059cbb`), whose selector is unique to ERC-20, a token that Multi-party Compute doesn't recognize has its amount scaled as if the token had 18 decimal places. Match recognized tokens by `contract_address`, and don't set amount limits on unrecognized tokens whose decimals aren't 18. ERC-20 `transferFrom` and `approve` share their selectors with ERC-721, so they need a recognized contract; a call to an unrecognized contract with one of these selectors is denied with `UNRECOGNIZED_PAYLOAD`. For more information, see ERC-721 non-fungible tokens.

The context doesn't say which kind of Ethereum transaction it is, so keep the following in mind:

  * **Contract calls that send ETH look like ETH transfers.** Both have `token_symbol` `"ETH"` and an `amount_token_scaled`. Only a contract call has `contract_address`. To allow only ETH transfers, add `!(context has contract_address)`.
  * **ERC-20 approvals look like ERC-20 transfers.** An `approve` has the same `contract_address`, `amount_token_scaled`, and `secondary_key` (the spender) as a transfer of the same amount to the same address. A policy that permits the transfer also permits the approval.



Contract creation transactions (with an empty `to` address) can't be decoded and are denied with `UNRECOGNIZED_PAYLOAD`.

#### ERC-721 non-fungible tokens

Under `ETHEREUM_TX_V2`, Multi-party Compute decodes the following ERC-721 methods:

  * `safeTransferFrom(address from, address to, uint256 tokenId)` (`0x42842e0e`)
  * `safeTransferFrom(address from, address to, uint256 tokenId, bytes data)` (`0xb88d4fde`)
  * `transferFrom(address from, address to, uint256 tokenId)` (`0x23b872dd`)
  * `approve(address to, uint256 tokenId)` (`0x095ea7b3`)
  * `setApprovalForAll(address operator, bool approved)` (`0xa22cb465`)



ERC-20 and ERC-721 share the same 4-byte selectors for `transferFrom` (`0x23b872dd`) and `approve` (`0x095ea7b3`). To decide whether the `uint256` argument is a fungible amount or a token ID, Multi-party Compute looks up the `to` contract address in its registry of recognized token contracts. For ERC-721 calls, `amount_token_scaled` is omitted, `token_standard` is `"ERC721"`, and `token_id` is a base-10 `String`. A call to an unrecognized contract with one of these shared selectors is denied with `UNRECOGNIZED_PAYLOAD`.

#### EIP-712 typed data

For `EIP712_TYPED_DATA_V1` payloads (UTF-8 JSON-encoded EIP-712 typed data with `types`, `primaryType`, `domain`, and `message`), Multi-party Compute validates the JSON structure and computes the 32-byte EIP-712 signing digest, `keccak256(0x1901 ++ domainSeparator ++ hashStruct(message))`, where `++` is byte concatenation. Validation rejects nesting deeper than 15 levels, cyclic types, `null` array elements, and `domain` fields that don't match `types.EIP712Domain`, and preserves 256-bit integers without floating-point precision loss.

An `EIP712_TYPED_DATA_V1` payload projects the following attributes:

Attribute | Value  
---|---  
`blockchain` | Always `"ETH"`.  
`schema` | Always `"EIP712_TYPED_DATA_V1"`.  
`contract_address` | `domain.verifyingContract`, in mixed-case EIP-55 checksum format. Omitted when the domain doesn't set `verifyingContract`.  
`chain_id` | `domain.chainId` as a `Long`. Omitted when the domain doesn't set `chainId`.  
`max_fee_atomic` | Always `0`, because signing typed data doesn't pay a network fee.  
`secondary_key` | For recognized message types, the counterparty: `spender` for ERC-2612 `Permit` and Uniswap `Permit2`, or `to` for ERC-3009 `TransferWithAuthorization` and Safe `SafeTx`. For other message types, `domain.verifyingContract`.  
`amount_token_scaled` | For recognized message types (`Permit`, `Permit2`, `TransferWithAuthorization`, and `SafeTx`), the authorized token or ETH value (`value` or `details.amount`), in units of 10-9. Omitted for other message types.  
`token_symbol` | `"USDC"`, `"USDT"`, `"DAI"`, or `"WBTC"` when the verifying contract or the Permit2 token (`details.token`) is a recognized token on Ethereum Mainnet. Omitted otherwise.  
`deadline` | The expiration time of the message, in seconds since the Unix epoch, when the message has a `deadline`, `sigDeadline`, or `validBefore` field. Omitted otherwise.  
`eip712` | A `Record` with the typed data. For more information, see the following table.  
  
The `eip712` record has the following fields:

Field | Cedar type | Value  
---|---|---  
`context.eip712.primary_type` | `String` | The `primaryType` name, for example `"Permit"`, `"PermitSingle"`, `"TransferWithAuthorization"`, or `"SafeTx"`.  
`context.eip712.domain` | `Record` | The `EIP712Domain` fields that the payload sets: `name`, `version`, `chainId`, `verifyingContract`, and `salt`.  
`context.eip712.message` | `Record` | The `message` fields. 256-bit integer values (`uint256` and `int256`) are base-10 `String`s, so rules can match exact values without 64-bit overflow.  
  
### Bitcoin

The following table describes the context attributes for `BITCOIN_TX_V2` payloads (BIP 174 PSBT v0):

Attribute | Value  
---|---  
`secondary_key` | The address of the one output that isn't change. For a consolidation, where every output is change, the first output's address.  
`amount_token_scaled` | The amount sent to `secondary_key`, not counting change (1 satoshi = `10`). `0` for a consolidation.  
`token_symbol` | Always `"BTC"`.  
`contract_address` | Never present.  
`chain_id` | Never present, because a PSBT doesn't say which network it's for. Addresses are always formatted as Mainnet addresses, so a Testnet address also starts with `bc1`, `1`, or `3`. The address prefix shows the address type, not the network.  
`max_fee_atomic` | The miner fee: total inputs minus total outputs (1 satoshi = `10`).  
  
To keep Bitcoin networks apart, use different keys for each network, for example in a KeyRing for Mainnet and another for Testnet, and scope rules to them with `principal_keyring` or `principal_key`. The same key can sign on both networks, so this only works if you never use a Mainnet key on Testnet.

A transaction that sends to more than one address that isn't change can't be decoded. A transaction with no address to send to, such as one whose only output that isn't change is an `OP_RETURN` output, can't be evaluated.

### Solana

The following table describes the context attributes for `SOLANA_TX_V1` payloads (unsigned legacy or v0 Solana messages):

Attribute | Value  
---|---  
`secondary_key` | For SOL transfers, the destination wallet. For token transfers, the destination token account, not the wallet that owns it. In base58.  
`amount_token_scaled` | The amount. For SOL, the number of lamports (1 lamport = `1`). For tokens, the raw amount scaled with the decimals that the `TransferChecked` instruction carries.  
`token_symbol` | `"SOL"` for SOL transfers. For tokens, `"USDC"`, `"USDT"`, or `"PYUSD"`; omitted for other mints.  
`contract_address` | For token transfers, the mint address, in base58. Omitted for SOL transfers.  
`chain_id` | Never present. Solana messages don't name a cluster.  
`max_fee_atomic` | The most that the whole transaction can pay in lamports: 5,000 for each required signature, plus the priority fee, ⌈compute unit limit × compute unit price in micro-lamports ÷ 106⌉, if the transaction sets a compute unit price.  
  
A Solana transaction can contain several instructions:

  * **Transfer instructions:** System Program `Transfer` (SOL), and SPL Token or Token-2022 `TransferChecked`. The unchecked `Transfer` instruction, and tokens with more than 9 decimal places, can't be decoded.
  * **Other instructions:** ComputeBudget `SetComputeUnitLimit` and `SetComputeUnitPrice`, Memo (v1 and v2), Associated Token Account `Create` and `CreateIdempotent`, and System Program `AdvanceNonceAccount`. These instructions don't produce a context of their own.



Each transfer instruction is evaluated separately with its own context. The transaction is permitted only if every transfer is permitted; if any transfer is denied, the whole transaction is denied. `max_fee_atomic` is the fee for the whole transaction and is the same in every context, so don't add it up across transfers.

If the transaction sets a compute unit price without a compute unit limit, the fee uses the Solana default limit of 200,000 compute units for each instruction other than ComputeBudget instructions, up to 1,400,000.

The transaction's signers must match the accounts that each instruction needs to sign, and the source and destination accounts must be writable. v0 messages that use address lookup tables can't be decoded. Pass the unsigned message bytes, not a signed transaction envelope, in `Transaction.payload` and `Transaction.rawMessage`.

The recognized mints are the Solana Mainnet mints. On Devnet or Testnet, a token transfer has no `token_symbol`, so check `contract_address` instead.

An Associated Token Account `Create` instruction funds the new account's rent-exempt reserve in SOL. That amount isn't in `amount_token_scaled`.

## Example rules

The following examples are `permit` and `forbid` policies that you can adapt. Each example checks every optional attribute with `has` before it reads it.

### Buy limit for a KeyRing using payload and metadata

Permit `buy_transaction` transfers of up to 500,000 USDC on Ethereum Mainnet from any key in the `institutional-treasury` KeyRing, when the initiator labels the transaction with `"equities-desk"`, sets a validity of at most 300 seconds, and states a value of at most $500,000:
    
    
    permit (
      principal,
      action == Action::"buy_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context.principal_keyring == "institutional-treasury" &&
      context.schema == "ETHEREUM_TX_V2" &&
      context has chain_id && context.chain_id == 1 &&
      context has contract_address &&
      context.contract_address == "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" &&
      context has amount_token_scaled && context.amount_token_scaled <= 500000000000000 &&
      context has fiat_amount && context.fiat_amount <= 500000 &&
      context has validity && context.validity <= 300 &&
      context has principal_value1 && context.principal_value1 == "equities-desk"
    };
    

Multi-party Compute doesn't check `fiat_amount` against the payload. For more information, see [Context attributes](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#context).

### Spending limit for one key

Permit ETH transfers of up to 1 ETH from one key on Ethereum Mainnet. `!(context has contract_address)` excludes contract calls that send ETH:
    
    
    permit (principal, action, resource)
    when {
      context.principal_keyring == "treasury" &&
      context.principal_key == "hot-wallet-1" &&
      context.schema == "ETHEREUM_TX_V2" &&
      context has chain_id && context.chain_id == 1 &&
      context has token_symbol && context.token_symbol == "ETH" &&
      !(context has contract_address) &&
      context has amount_token_scaled && context.amount_token_scaled <= 1000000000
    };
    

### Stablecoin allowlist on Ethereum

Permit transfers of up to 5,000 USDC to one address, and approvals (allowances) of up to 5,000 USDC for that address. The policy checks `contract_address` rather than `token_symbol`, so a token from another contract that uses the same symbol doesn't match:
    
    
    permit (principal, action, resource)
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context has contract_address &&
      context.contract_address == "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" &&
      context.secondary_key == "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B" &&
      context has amount_token_scaled && context.amount_token_scaled <= 5000000000000
    };
    

`token_symbol` is `"USDC"` for this transaction.

### ERC-721 transfer and operator approval guard

Permit transferring one tokenized treasury note (`token_id == "1042"`) from an approved ERC-721 contract to a settlement address, and forbid granting collection-wide operator approvals (`setApprovalForAll` with `approve_all == true`).

Policy A permits the one NFT transfer:
    
    
    permit (
      principal,
      action == Action::"internal_transfer_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context has chain_id && context.chain_id == 1 &&
      context has token_standard && context.token_standard == "ERC721" &&
      context has contract_address &&
      context.contract_address == "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D" &&
      context has token_id && context.token_id == "1042" &&
      context.secondary_key == "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
    };
    

Policy B forbids collection-wide operator approvals:
    
    
    forbid (principal, action, resource)
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context has approve_all && context.approve_all == true
    };
    

### EIP-712 gasless USDC permit limit

Permit signing an off-chain ERC-2612 `Permit` for up to 25,000 USDC on Ethereum Mainnet for an approved settlement router, when the permit expires before a given time:
    
    
    permit (
      principal,
      action == Action::"buy_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context.schema == "EIP712_TYPED_DATA_V1" &&
      context has chain_id && context.chain_id == 1 &&
      context has contract_address &&
      context.contract_address == "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" &&
      context has eip712 && context.eip712.primary_type == "Permit" &&
      context.secondary_key == "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45" &&
      context has amount_token_scaled && context.amount_token_scaled <= 25000000000000 &&
      context has deadline && context.deadline <= 1793491200
    };
    

### Bitcoin spending limit and fee cap

Permit transfers of up to 0.0025 BTC with a miner fee of up to 10,000 satoshis, from keys in a KeyRing that you use only on Bitcoin Mainnet:
    
    
    permit (principal, action, resource)
    when {
      context.schema == "BITCOIN_TX_V2" &&
      context.principal_keyring == "btc-mainnet" &&
      context has amount_token_scaled && context.amount_token_scaled <= 2500000 &&
      context.max_fee_atomic <= 100000
    };
    

### SOL transfer and priority fee limit

Permit SOL transfers of up to 1.5 SOL when the total fee, including any priority fee, is at most 50,000 lamports (0.00005 SOL):
    
    
    permit (principal, action, resource)
    when {
      context.schema == "SOLANA_TX_V1" &&
      context has token_symbol && context.token_symbol == "SOL" &&
      !(context has contract_address) &&
      context has amount_token_scaled && context.amount_token_scaled <= 1500000000 &&
      context.max_fee_atomic <= 50000
    };
    

### SPL token or Token-2022 transfer on Solana

Permit transfers of up to 250 USDC to one token account. The same rule matches the SPL Token and Token-2022 programs, because the context doesn't say which program the transfer uses:
    
    
    permit (principal, action, resource)
    when {
      context.schema == "SOLANA_TX_V1" &&
      context has contract_address &&
      context.contract_address == "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" &&
      context.secondary_key == "9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin" &&
      context has amount_token_scaled && context.amount_token_scaled <= 250000000000
    };
    

`secondary_key` is the recipient's token account for this mint. To allow a recipient wallet, list its token account for each mint that you allow. In a transaction with several transfers, this rule must match every transfer.

### Unrecognized asset block

Deny any transfer whose asset Multi-party Compute doesn't recognize. This `forbid` policy only uses `has`, so it can't fail to evaluate:
    
    
    forbid (principal, action, resource)
    when { context has amount_token_scaled }
    unless { context has token_symbol };
    

### Fee cap for a blockchain

`max_fee_atomic` is always present, so this `forbid` policy can't fail to evaluate. Because the scale is 10-9 of each native coin, the same number is a different value on each blockchain. Scope the policy to one blockchain:
    
    
    forbid (principal, action, resource)
    when { context.blockchain == "ETH" && context.max_fee_atomic > 10000000 };
    

This denies Ethereum transactions that can pay more than 0.01 ETH in fees.

## KeyRings

A [KeyRing](https://docs.cloud.google.com/multi-party-compute/overview#key-policies) is a static container that groups MPC keys, for example `"institutional-treasury"` or `"btc-cold-storage"`. Each key is created inside a single KeyRing and stays in that KeyRing permanently.

KeyRings participate in policies in three ways:

  * **KeyRing`KeyPolicy` (signing quorum).** When you create a KeyRing, you set its immutable [KeyPolicy](https://docs.cloud.google.com/multi-party-compute/overview#key-policies), which defines the threshold tree of teams and users that hold key shares and must approve before any key in the KeyRing can sign. Transaction policies work alongside the `KeyPolicy`: the transaction policy evaluates the business rules for the payload (`PERMIT` or `DENY`), while the KeyRing's `KeyPolicy` governs whose key shares must authorize the signing ceremony.
  * **Scoping transaction policies by signing KeyRing (`context.principal_keyring`).** Every transaction's context includes `context.principal_keyring`, set to the ID of the KeyRing that holds the signing key, and `context.principal_key`, set to the ID of the signing key. A rule with `context.principal_keyring == "institutional-treasury"` applies to every key in the KeyRing, including keys created in that KeyRing later, without creating or approving a new policy:
        
        permit (
          principal,
          action == Action::"internal_transfer_transaction",
          resource == Resource::"transaction_management"
        )
        when {
          context.principal_keyring == "institutional-treasury" &&
          context has fiat_amount && context.fiat_amount <= 100000
        };
        

  * **Destination KeyRing allowlist (in a KeyList).** You can also add a KeyRing as an entry in a [KeyList](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#keylists), so that transfers to the blockchain address of any active key in that KeyRing, such as internal sweeps between hot and cold KeyRings, are permitted automatically as new keys are created. For an example, see KeyList allowlist and blocklist.




### KeyList allowlist and blocklist

Permit transfers of up to 1 ETH only to addresses in the `trusted-destinations` KeyList. `context.key_lists["trusted-destinations"]` is the set of addresses that the KeyList expands to at the transaction's `createTime`, so adding or removing an entry changes what this rule permits without a new policy:
    
    
    // Assuming you created a KeyList with ID "trusted-destinations":
    permit (principal, action, resource)
    when {
      context.schema == "ETHEREUM_TX_V2" &&
      context has token_symbol && context.token_symbol == "ETH" &&
      !(context has contract_address) &&
      context.key_lists["trusted-destinations"].contains(context.secondary_key) &&
      context has amount_token_scaled && context.amount_token_scaled <= 1000000000
    };
    

Deny any transaction to an address in the `blocked-addresses` KeyList, on every blockchain. `key_lists` and `secondary_key` are always present, and `CreateTransactionPolicy` verifies that the KeyList exists, so this `forbid` policy can't fail to evaluate:
    
    
    // Assuming you created a KeyList with ID "blocked-addresses":
    forbid (principal, action, resource)
    when { context.key_lists["blocked-addresses"].contains(context.secondary_key) };
    

Write the KeyList ID in bracket syntax, `context.key_lists["..."]`, rather than dot syntax. Dot syntax fails to parse for IDs that contain a hyphen or start with a digit. Entries are compared as strings, so add manual entries in the address format that the table for each blockchain describes. For more information, see [KeyLists in the Cedar context](https://docs.cloud.google.com/multi-party-compute/policy-evaluation#keylist-syntax).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
