---
url: https://docs.cloud.google.com/universal-ledger/reference/gculpy-language/
title: The GCULpy language \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-05T00:20:24.200430+00:00
---

# The GCULpy language  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/gculpy-language/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  The GCULpy language Stay organized with collections  Save and categorize content based on your preferences. 

GCULpy is a strict statically typed subset of Python, designed to be safe, readable, and auditable. Its design intentionally limits certain dynamic features of Python to prevent common smart contract vulnerabilities and ensure that the behavior of a contract is always predictable.

This page provides a reference for the GCULpy language specification, covering the core concepts and the lifecycle of a contract on a Universal Ledger network.

## Core concepts

The following contract defines a sample **ERC20 token** in GCULpy:
    
    
    import gcul
    
    class ERC20Token(gcul.Contract):
        """Sample ERC20 implementation for the Universal Ledger."""
    
        symbol: str
        total_supply: int
        balance: gcul.AccountField[int]
    
        def __init__(self, symbol: str):
            self.symbol = symbol
            self.total_supply = 0
    
        def mint(self, beneficiary: gcul.Account, value: int) -> int:
            """Mints tokens to the given beneficiary."""
            assert self.is_owner(gcul.sender), "Only the owner can mint"
            assert value >= 0, "Mint amount must be non-negative"
            self.total_supply += value
            self.balance[beneficiary] += value
            return value
    
        def transfer(self, beneficiary: gcul.Account, value: int) -> int:
            """Transfers tokens from the sender to the given beneficiary."""
            assert value >= 0, "Transfer amount must be non-negative"
            assert (
                value <= self.balance[gcul.sender]
            ), "Sender does not have enough balance"
            self.balance[gcul.sender] -= value
            self.balance[beneficiary] += value
            return value
    

A GCULpy contract is a class that inherits from `gcul.Contract`. It contains **fields** (storing state) and **methods** (processing logic that operate on fields).

### Fields

State in a GCULpy contract is stored in fields. All fields must be declared with a static type at the class level. There are two kinds of fields:

  * **Contract fields** hold a single value stored with the contract itself. In the `ERC20Token` example, `symbol: str` and `total_supply: int` are contract fields.

  * **Account fields** hold a separate value for each account interacting with the contract. They are declared with `gcul.AccountField[T]`, where `T` is the type of the per-account value. In the `ERC20Token` example, `balance: gcul.AccountField[int]` is an account field. Before a contract can write to storage space reserved for that account, the storage permission must explicitly be granted to the contract. Once the data is stored, only the contract instance can modify it—the account cannot.




Restriction Fields have the following storage limits. A transaction that would exceed either limit fails.

  * All contract fields of a contract share a single storage entry, which can hold about 5 MiB of serialized data in total.
  * All account fields that a contract stores for each individual account can hold at most 1 MiB of serialized data in total.



### Methods

Methods define the executable logic of a contract. They behave like Python methods and can read or modify the contract's fields.

  * `__init__`: The constructor is called only once when the contract is first deployed. Every contract field must be assigned a value in the constructor. The constructor doesn't initialize account fields; each account's value is created when that account grants the storage permission.

  * **Private methods** : Methods starting with an underscore (for example, `_internal_logic`) are private and can only be called by other methods within the same contract. The Universal Ledger interpreter enforces this constraint.

  * **Public methods** : Any method not starting with an underscore (`_`) is public. Public methods can be called by any user with the `ROLE_CONTRACT_PARTICIPANT` by submitting an [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction.




Restriction Public methods and all `@gcul.readonly` methods cannot use mutable types in their signatures, for example `list` or `dict`. Instead, use read-only type declarations such as `Sequence` or `Mapping`.

Restriction During execution, methods are limited to a network-wide upper bound of computation usage. Exceeding this limit results in a transaction failure.

## Contract lifecycle

The following sections walk through the typical operations involved in the lifecycle of a GCULpy contract.

### Deploy a contract

First, you compile your GCULpy source code using the `gculpyc` compiler. Then, a user with the `ROLE_CONTRACT_CREATOR` may submit a [CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcontract) transaction to deploy the compiled bytecode to a Universal Ledger network. For detailed instructions see the [Deploy a programmable contract](https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract) tutorial.

Such a transaction would look like:
    
    
    client_transaction {
      sender_id: "OWNER_ACCOUNT_ID"
      create_contract_transaction {
        contract_bytes: "COMPILED_BYTECODE"
        init_arguments {
          key: "symbol"
          value: { string_value: "US02079K1079" }
        }
      }
    }
    

When the network processes this transaction:

  * The constructor, that is the `__init__` method, is executed with the provided arguments to create a new contract instance.
  * The sender of the transaction becomes the **contract's owner**.
  * The contract instance is permanently stored in the ledger and assigned a unique **contract ID** which is returned as part of the transaction output.



### Grant permissions

Before a contract can store data in an **account field** on behalf of an account, either an account for a user or another contract, the storage permission must be granted to the contract storing the data. This is a critical security step.

#### Granting permissions for a user account

A user with a `ROLE_CONTRACT_PARTICIPANT` may submit a [GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#grantcontractpermissions) transaction for a specific contract ID:
    
    
    client_transaction {
      sender_id: "PARTICIPANT_ACCOUNT_ID"
      grant_contract_permissions_transaction {
        contract_id: "CONTRACT_ID"
        permissions: CONTRACT_PERMISSION_STORAGE
      }
    }
    

When the network processes this transaction:

  * If the contract does not define any account fields, the transaction is rejected.
  * If the contract defines account fields, all of them are populated with default values (for example, `contract.balance[gcul.sender] = 0`). These values are then stored in the world state as part of the account's data.



#### Granting permissions for a delegate contract

A user with a `ROLE_CONTRACT_PARTICIPANT` may submit a [GrantContractPermissions](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#grantcontractpermissions) transaction to allow one contract to store data on behalf of another contract they own:
    
    
    client_transaction {
      sender_id: "OWNER_ACCOUNT_ID"
      grant_contract_permissions_transaction {
        contract_id: "TARGET_CONTRACT_ID"
        delegate_contract_id: "DELEGATE_CONTRACT_ID"
        permissions: CONTRACT_PERMISSION_STORAGE
      }
    }
    

When the network processes this transaction:

  * The transaction sender, that is `sender_id`, must be the **owner** of the contract identified by `delegate_contract_id`.
  * A contract cannot grant storage permissions to itself, so `delegate_contract_id` must differ from `contract_id`.
  * Storage permissions are granted exclusively to the contract specified in `delegate_contract_id`, rather than the transaction sender.
  * Account fields defined on the target contract, `contract_id`, are initialized for the delegate contract, `delegate_contract_id`, allowing methods on the target contract to safely access account fields keyed by `gcul.caller` or `gcul.sender` during cross-contract invocations.



### Invoke contract methods

Once a contract is deployed and any necessary permissions are granted, users can interact with it by calling its public methods. A user with a `ROLE_CONTRACT_PARTICIPANT` may submit an [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction specifying the contract ID, method name, and method argument values.
    
    
    client_transaction {
      sender_id: "PARTICIPANT_ACCOUNT_ID"
      invoke_contract_method_transaction {
        contract_id: "CONTRACT_ID"
        method_name: "mint"
        method_arguments {
          key: "beneficiary"
          value: { account_id: "BENEFICIARY_ID" }
        }
        method_arguments {
          key: "value"
          value: { int64_value: 10 }
        }
      }
    }
    

When the network processes this transaction:

  * The contract instance associated with the provided `CONTRACT_ID` is retrieved.
  * The method `mint(beneficiary=Account("BENEFICIARY_ID"), value=10)` is executed. The `Account` object for the beneficiary is built and validated by the runtime. The method's logic may safely assume that the provided ID is valid and refers to an existing account on the ledger.
  * If the method fails for any reason, the transaction will fail and _no updates_ will be made to the contract's state.
  * If the method succeeds, the updated state of the contract is recorded in the world state.



## Language specification

GCULpy is designed for safety and predictability and, as such, disallows several Python features; these will be called out with the Restriction label. These restrictions are intended to be permanent language features, introduced to make the contract logic easier to read, audit, and analyze statically, limiting surprising or unsafe behaviors.

Other features are called out with the Roadmap label, these are on the implementation roadmap but not yet supported by the `gculpyc` compiler.

### Types

GCULpy supports a range of common variable types with a strong emphasis on static typing.

Core value types:

  * `int`, `bool`, `str`, `None` are already supported.
  * Roadmap `Decimal`, `bytes`, `Enum` are on the roadmap.
  * Restriction `float` and `complex` are not allowed.
  * Restriction `int` values are signed 64-bit integers, from -263 to 263 \- 1. An integer literal outside this range will result in a compile-time error, and an operation whose result is outside this range will result in a runtime error.
  * Restriction `str` values can be at most 1,000,000 characters long. A longer string literal will result in a compile-time error. Passing a longer string as a method argument, or producing one as the result of an operation, will result in a runtime error.



Container types:

  * `list` and `dict`: 
    * `list[T]`: A mutable sequence. Supports indexing, for example `my_list[0]`, and the `append()` method.
    * `dict[K, V]`: A mutable mapping. Supports indexing, for example `my_dict[key]`, and the `pop()` method.
  * `collections.abc.Sequence` and `collections.abc.Mapping`: 
    * `collections.abc.Sequence[T]`: A read-only reference to a sequence. Supports reading elements by index, for example `my_seq[0]`, but elements can't be modified or deleted. `list[T]` is a subtype of `Sequence[T]`, so you can pass, return, or assign a `list[T]` value or list literal to a target typed as `Sequence[T]`, but you can't assign a `Sequence[T]` to a `list[T]`.
    * `collections.abc.Mapping[K, V]`: A read-only reference to a mapping. Supports reading entries by key, for example `my_map[key]`, but entries can't be modified or deleted. `dict[K, V]` is a subtype of `Mapping[K, V]`, so you can pass, return, or assign a `dict[K, V]` value or dictionary literal to a target typed as `Mapping[K, V]`, but you can't assign a `Mapping[K, V]` to a `dict[K, V]`.
  * Roadmap `tuple`, `set`, `dataclass` are on the roadmap.
  * Restriction Concrete types must be specified for values in a container, for example `dict[str, int]` is allowed, but a plain `dict` or `dict[str, Any]` are not.
  * Roadmap List slicing, for example `my_list[1:3]`.
  * Roadmap Other methods, such as `.get()`, `.keys()`, `.values()`, `.items()`, `.clear()`, or `.extend()`.



Restriction All variables—including contract and account fields, function parameters and return types—must be defined and typed statically. Their type cannot be changed at runtime and only concrete types are supported. Types cannot be used as values, for example they cannot be stored in variables or passed to functions as arguments. Trying to assign a value to an undeclared field will result in a compile-time error.

Restriction A local variable must be assigned before it's read. Local variables have no default value, so reading one before it's assigned results in a runtime error.

### Classes and inheritance

You can only define classes that are direct subclasses of either `gcul.Contract` or `gcul.ContractInterface`. This strict rule prevents the complexities of full Python inheritance, which can introduce hard-to-find bugs and make code difficult to reason about. For security, attempting to override a property or method from a parent class will raise an error, providing a clear safeguard against unexpected behavior.

Roadmap GCULpy will offer more flexibility while maintaining its core principles. The roadmap includes support for **single inheritance** on user-defined classes with method overriding explicitly managed with an `@override` decorator. Additionally, the `super()` built-in will be only supported in its argument-free form, to ensure direct, predictable operations.

### The gcul module

GCULpy provides a built-in `gcul` module with essential types, decorators, and variables for contract development.

#### class `gcul.Contract`

The base class for all contracts. You cannot create instances of it directly; contracts are only ever instantiated through [CreateContract](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#createcontract) transactions. Methods and properties from the base `gcul.Contract` class cannot be overridden in subclasses.

  * `Contract.is_owner(account: Account) -> bool`

Returns `True` if the provided account is the contract owner.

  * `Contract.call(target: ContractInterface, payment: Amount | None = None) -> ContractMethods`

Initiates a cross-contract interaction with `target`. Instead of calling methods on the target directly (e.g., `target.foo()`), you must use `self.call()` to explicitly route the invocation through the ledger runtime. This mechanism returns a secure proxy object used to invoke corresponding public methods on the target contract, ensuring that execution boundaries are strictly enforced and any `payment` is safely delivered. See ContractInterface for details.

A `payment` must be supplied when calling a method decorated with `@gcul.payable`; and must be omitted for non-payable methods.

`target` must be a different contract. Calling the current contract through `self.call()` raises a runtime error. To call another method on the same contract, call it directly, for example, `self.foo()`.

  * `Contract.native_transfer(beneficiary: Account, amount: Amount) -> None`

Transfers an on-ledger amount directly from the contract's balance to `beneficiary`.

  * `Contract.id: str`

Unique string ID of the contract.




#### class `gcul.Account`

A built-in type representing a user or contract account on the ledger. You cannot create `gcul.Account` objects directly; the runtime environment creates them for you and provides them as function or method arguments. To pass an account as a transaction argument, supply an [AccountValue](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#accountvalue) holding the account ID. The runtime validates the ID and converts it into a full account object. If the ID doesn't belong to a registered account, the transaction fails. This ensures you only ever work with valid accounts.

The definition of the class is roughly equivalent to:
    
    
    @dataclasses.dataclass(frozen=True)
    class Account:
      """A valid account on the ledger."""
    
      id: str  # The ID of the account as a string.
    

  * `Account.id: str`

Unique string ID of the account.




#### class `gcul.Amount`

Represents a monetary value denominated in a specific ledger currency. Instantiate an amount using `gcul.Amount(value: int, currency: gcul.Currency)`. The definition of the class is roughly equivalent to:
    
    
    @dataclasses.dataclass(frozen=True)
    class Amount:
      """Represents an amount denominated in a ledger currency."""
    
      value: int
      currency: Currency
    

#### class `gcul.Currency`

Represents a fully qualified currency on the ledger. The definition of the class is roughly equivalent to:
    
    
    @dataclasses.dataclass(frozen=True)
    class Currency:
      """Represents a fully qualified currency on the ledger."""
    
      code: str
      operator_id: str
    

#### class `gcul.ContractInterface`

The base class for declaring the public interface of a contract. Methods and properties from the base `gcul.ContractInterface` class cannot be overridden in subclasses. Furthermore, the methods in the interface declaration cannot include any code, only `...` is allowed.

For a contract to call methods on another contract deployed on the ledger, declare an interface class inheriting from `gcul.ContractInterface`. Method stubs _must_ match their corresponding declaration in the target contract. This includes arguments, return type, and decorator annotations such as `@gcul.readonly` or `@gcul.payable`.

Inside your contract code, use `self.call(target, payment)` to invoke a method from another contract.

The following example illustrates how a `TokenVendor` contract interacts with another contract implementing the `ERC20Interface`. It uses `self.call()` to transfer tokens to a buyer in exchange for an on-ledger currency payment:
    
    
    class ERC20Interface(gcul.ContractInterface):
      """Interface for an external ERC20 token contract."""
    
      def transfer(self, beneficiary: gcul.Account, value: int) -> int:
        ...
    
    class TokenVendor(gcul.Contract):
      """A vendor contract that distributes ERC20 tokens."""
    
      price_per_token: int
    
      def __init__(self, price_per_token: int) -> None:
        self.price_per_token = price_per_token
    
      @gcul.payable
      def purchase_tokens(self, token: ERC20Interface, quantity: int) -> int:
        """Accepts on-ledger currency for a specific quantity of ERC20 tokens."""
    
        # Enforce positive quantity.
        assert quantity > 0, "Quantity must be positive"
    
        # Calculate the required payment.
        required_payment = quantity * self.price_per_token
        assert gcul.payment.value == required_payment, "Incorrect payment amount"
    
        # Invokes `transfer` on the external ERC20 token contract
        # to move tokens from the vendor's own balance to the caller.
        return self.call(token).transfer(gcul.caller, quantity)
    

Interface types can also be used as contract fields, not just as method parameters. Storing an interface in a field lets a contract hold a reference to another contract across transactions, and replace that reference later. The following example contract uses the `ERC20Interface` declared earlier:
    
    
    class Router(gcul.Contract):
      """Holds a replaceable reference to an ERC20 token contract."""
    
      target: ERC20Interface
    
      def __init__(self, target: ERC20Interface) -> None:
        self.target = target
    
      def set_target(self, new_target: ERC20Interface) -> None:
        assert self.is_owner(gcul.sender), "Only the owner can set the target"
        self.target = new_target
    

#### class `gcul.AccountField`

A built-in generic type for declaring account fields. `gcul.AccountField[T]` holds a separate value of type `T` for each account that has granted the contract the storage permission. It behaves as a mapping with `gcul.Account` keys, which you can use to read or write a value for each specific account. For example:
    
    
    class Token(gcul.Contract):
      balance: gcul.AccountField[int]
    
      def deposit(self, account: gcul.Account, value: int) -> None:
        self.balance[account] = value  # Writes the value for one account.
    
      def get_balance(self, account: gcul.Account) -> int:
        return self.balance[account]  # Reads the value for one account.
    

`T` must be a type that has a default value, so `gcul.Account`, `gcul.Amount`, `gcul.Currency`, and interface types cannot be used as account field values. When an account grants the storage permission to a contract, every account field is populated with the default value of its type for that account.

**Note:** A plain `dict[gcul.Account, T]` isn't an account field. It's an ordinary dictionary value, which you can use as a contract field, a method parameter, or a return type. As a contract field it holds one dictionary in the contract's own storage, so no storage permission is needed. The tradeoff is that every entry shares the contract's single storage budget of about 5 MiB, so a dictionary with many account keys can exhaust it. An account field instead gives each account its own storage.

Restriction Indexing with an account is the only operation an account field supports. The field itself can't be assigned to a variable, passed as an argument, returned from a function, or iterated over.

Restriction Account field entries can't be deleted. A stored value can be overwritten, but the entry itself is permanent.

Restriction Account fields for `gcul.sender`, `gcul.caller`, and any `gcul.Account` passed as a method argument (including inside lists or other containers) are loaded before method execution. For other accounts, a single transaction can lazily load account fields for at most 15 distinct `(contract, account)` pairs; accessing an account field for the same pair multiple times in a transaction counts only once. A transaction that exceeds this limit fails.

#### `@gcul.readonly`

Annotates a contract method as read-only. Method declarations with this decorator can't mutate contract state or make on-ledger currency transfers. They also cannot use mutable container types in their signatures, for example `list` or `dict`; they must use read-only type declarations such as `Sequence` or `Mapping` instead.

#### `@gcul.payable`

Annotates a contract method as requiring a payment to be executed. If a method expects to receive an on-ledger currency payment using `gcul.payment`, it must be marked with this decorator, otherwise the transaction will fail.

#### `gcul.sender: gcul.Account`

Holds a reference to the account that signed and submitted the current [InvokeContractMethod](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#invokecontractmethod) transaction. The value of `gcul.sender` does not change throughout transaction execution, even if it involves cross-contract calls, unlike `gcul.caller` which references the immediate caller.

#### `gcul.caller: gcul.Account`

Holds a reference to the immediate caller of the current method. For direct user transactions, `gcul.caller` matches `gcul.sender` pointing to whoever submitted the transaction. For cross-contract calls, `gcul.caller` corresponds to the calling contract's account ID. Internal calls within a contract don't change the value of `gcul.caller`.

#### `gcul.payment: gcul.Amount`

Holds the payment transferred to a method decorated with `@gcul.payable`. Accessing `gcul.payment` inside a non-payable method raises a compile-time error.

### Operators

Most operators available in Python are supported in GCULpy and work as expected.

  * Addition (`+`) and subtraction (`-`), including unary and binary forms.
  * Multiplication (`*`), floor division (`//`), and modulo (`%`).
  * Exponentiation (`**`) for positive exponents.
  * Comparisons (`<`, `<=`, `>`, `>=`, `==`, `!=`).
  * Bitwise and (`&`), or (`|`), xor (`^`), left shift (`<<`), right shift (`>>`), negation (`~`).
  * Boolean operations (`and`, `or`, `not`).
  * Roadmap Object identity (`is`).
  * Restriction Negative exponents are not allowed and raise a runtime error.
  * Restriction True division (`/`), as it has a `float` return type, is not allowed and results in a compile-time error.



### Control flow

Most control-flow statements from Python work in GCULpy with the same semantics:

  * `pass` statements.
  * internal function calls (same contract, non-recursive).
  * `assert` statements.
  * `if ... then .. else ...` statements.
  * `for VAR in CONTAINER` statements.
  * external function calls (to any other contract, non-recursive).
  * `break` and `continue` statements.
  * `raise` statements.
  * Roadmap `try ... except` statements.
  * Roadmap `match` statements.
  * Roadmap `generators` and `yield` statements.
  * Roadmap context managers and `with` statements.



Restriction GCULpy is intentionally **Turing-incomplete** to prevent infinite loops and facilitate static analysis. Here's how it enforces this:

  * **No infinite loops:** Iteration is only allowed using `for` loops over finite containers or bounded sequences with `range(...)`; `while` loops are not allowed. Some container updates, for example adding or removing elements to a list or keys to a dictionary, are not allowed while iterating over them.
  * **No recursion:** A function cannot call itself, either directly or indirectly. The runtime environment performs both static and runtime checks to detect and reject the use of recursion.
  * **No async control flow:** Use of `async` primitives is not allowed to maintain the core design principles of predictability, security, and deterministic execution. Asynchronous operations make it difficult to reason about the control flow of a program, often leading to vulnerabilities and race conditions.



### Built-in functions

GCULpy supports the following built-in functions:

  * `abs(x)`

Returns the absolute value of an integer `x`. Arguments must be of type `int`.

  * `len(s)`

Returns the length, that is the number of items, of a string or finite container.

  * `max(iterable)`   
`max(arg1, arg2, *args)`

Returns the largest item in an iterable or the largest of two or more arguments. Calling `max()` on an empty iterable raises a runtime error.

  * `min(iterable)`   
`min(arg1, arg2, *args)`

Returns the smallest item in an iterable or the smallest of two or more arguments. Calling `min()` on an empty iterable raises a runtime error.

  * `range(stop)`   
`range(start, stop[, step=1])`

Generates an arithmetic sequence of integers with a non-zero integer `step`.

Restriction Can only be used in-line with `for` loops, for example `for i in range(10): ...`. Range objects cannot be assigned to variables or stored in fields, passed as arguments to functions, or queried with `len()`.




Roadmap The following built-in functions are on the implementation roadmap:

|  |  |   
---|---|---|---  
_A_  
`all()`  
`any()` _B_  
`bin()`  
`bool()`  
`bytes()` _C_  
`chr()`  
_D_  
`dict()`  
`divmod()` |  _E_  
`enumerate()` _F_  
`format()`  
`frozenset()` _H_  
`hash()`  
`hex()` _I_  
`id()`  
`int()` _L_  
`list()` |  _O_  
`oct()`  
`ord()` _P_  
`pow()`  
`property()` _R_  
`repr()`  
`reversed()` |  _S_  
`set()`  
`sorted()`  
`staticmethod()`  
`str()`  
`sum()`  
`super()` _T_  
`tuple()` _Z_  
`zip()`  
  
## Release notes

  * **03 Nov, 2026.** Released the GA version of the `gculpyc` compiler (`v0.2.0`), including support for cross-contract calls, on-ledger currency transfers and payments, `@gcul.readonly` methods, `list`, additional control-flow statements, and built-in functions.

  * **28 Jan, 2026.** Early version of `gculpyc` compiler made available to participants in the Universal Ledger private preview. For a tutorial using the compiler, see [Deploy a programmable contract](https://docs.cloud.google.com/universal-ledger/tutorial/deploy-contract).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 
