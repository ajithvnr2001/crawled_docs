---
url: https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:07.996215+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop/

React/Hooks

# useHumanInTheLoop

React hook for interactive tools that pause agent execution and wait for user input

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useHumanInTheLoop` registers an interactive tool that pauses agent execution until the user responds through your custom UI. Unlike [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool), there is no `handler` function. Instead, the hook provides an internal status machine (`InProgress` -> `Executing` -> `Complete`) and supplies a `respond` callback to the render component while the tool is in the `Executing` state. The agent remains paused until `respond` is called with the user's input.

This hook is built on top of `useFrontendTool` with an internally managed handler that resolves the tool call promise when `respond` is called. Use it for confirmation dialogs, approval workflows, form collection, or any scenario where a human must provide input before the agent can continue.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core/v2";
    
    function useHumanInTheLoop<T extends Record<string, unknown>>(
      tool: ReactHumanInTheLoop<T>,
      deps?: ReadonlyArray<unknown>,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`tool`ReactHumanInTheLoop<T>

`deps?`ReadonlyArray<unknown>

## ToolCallStatusCopy Anchor Link

The `ToolCallStatus` enum is exported from `@copilotkit/react-core/v2` and defines the three phases of tool execution:

Value| Description  
---|---  
`ToolCallStatus.InProgress`| Arguments are being streamed from the agent. The tool has not started executing yet.  
`ToolCallStatus.Executing`| Arguments are fully resolved. For `useHumanInTheLoop`, the `respond` callback is available.  
`ToolCallStatus.Complete`| Execution is finished. The `result` string is available.  
  
## UsageCopy Anchor Link

### Confirmation DialogCopy Anchor Link

A common pattern where the agent asks the user to confirm a destructive action.

Copy Text
    
    
    import { useHumanInTheLoop, ToolCallStatus } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function DeleteConfirmation() {
      useHumanInTheLoop(
        {
          name: "confirmDeletion",
          description: "Ask the user to confirm before deleting items",
          parameters: z.object({
            itemName: z.string().describe("Name of the item to delete"),
            itemCount: z.number().describe("Number of items to delete"),
          }),
          render: ({ args, status, respond, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <div className="p-4 text-gray-500">Preparing confirmation...</div>
              );
            }
    
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <div className="p-4 border rounded">
                  <p>
                    Are you sure you want to delete {args.itemCount} {args.itemName}
                    (s)?
                  </p>
                  <div className="flex gap-2 mt-4">
                    <button
                      onClick={() => respond({ confirmed: true })}
                      className="bg-red-500 text-white px-4 py-2 rounded"
                    >
                      Delete
                    </button>
                    <button
                      onClick={() => respond({ confirmed: false })}
                      className="bg-gray-300 px-4 py-2 rounded"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <div className="p-2 text-sm text-gray-600">
                  {parsed.confirmed ? "Items deleted." : "Deletion cancelled."}
                </div>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Form Input CollectionCopy Anchor Link

Collect structured input from the user before the agent proceeds.

Copy Text
    
    
    function ShippingAddressForm() {
      useHumanInTheLoop(
        {
          name: "collectShippingAddress",
          description:
            "Collect shipping address from the user before placing an order",
          parameters: z.object({
            orderSummary: z
              .string()
              .describe("A summary of the order being placed"),
          }),
          render: ({ args, status, respond }) => {
            const [address, setAddress] = useState({
              street: "",
              city: "",
              zip: "",
            });
    
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <div className="p-4 border rounded space-y-3">
                  <p className="font-medium">Order: {args.orderSummary}</p>
                  <p>Please enter your shipping address:</p>
                  <input
                    placeholder="Street address"
                    value={address.street}
                    onChange={(e) =>
                      setAddress({ ...address, street: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <input
                    placeholder="City"
                    value={address.city}
                    onChange={(e) =>
                      setAddress({ ...address, city: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <input
                    placeholder="ZIP code"
                    value={address.zip}
                    onChange={(e) =>
                      setAddress({ ...address, zip: e.target.value })
                    }
                    className="w-full border p-2 rounded"
                  />
                  <button
                    onClick={() => respond(address)}
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                  >
                    Submit Address
                  </button>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete) {
              return (
                <div className="p-2 text-green-600">
                  Shipping address submitted.
                </div>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Approval Workflow with ContextCopy Anchor Link

Copy Text
    
    
    function ExpenseApproval() {
      useHumanInTheLoop(
        {
          name: "approveExpense",
          description: "Request manager approval for an expense report",
          parameters: z.object({
            employeeName: z.string().describe("Name of the employee"),
            amount: z.number().describe("Expense amount in dollars"),
            category: z.string().describe("Expense category"),
            description: z.string().describe("Description of the expense"),
          }),
          render: ({ args, status, respond, result }) => {
            if (status === ToolCallStatus.Executing && respond) {
              return (
                <div className="p-4 border rounded">
                  <h3 className="font-bold">Expense Approval Required</h3>
                  <div className="mt-2 space-y-1 text-sm">
                    <p>Employee: {args.employeeName}</p>
                    <p>Amount: ${args.amount.toFixed(2)}</p>
                    <p>Category: {args.category}</p>
                    <p>Description: {args.description}</p>
                  </div>
                  <div className="flex gap-2 mt-4">
                    <button
                      onClick={() => respond({ approved: true })}
                      className="bg-green-500 text-white px-4 py-2 rounded"
                    >
                      Approve
                    </button>
                    <button
                      onClick={() =>
                        respond({ approved: false, reason: "Needs more detail" })
                      }
                      className="bg-red-500 text-white px-4 py-2 rounded"
                    >
                      Reject
                    </button>
                  </div>
                </div>
              );
            }
    
            if (status === ToolCallStatus.Complete && result) {
              const parsed = JSON.parse(result);
              return (
                <div
                  className={`p-2 text-sm ${parsed.approved ? "text-green-600" : "text-red-600"}`}
                >
                  {parsed.approved
                    ? "Expense approved."
                    : `Expense rejected: ${parsed.reason}`}
                </div>
              );
            }
    
            return null;
          },
        },
        [],
      );
    
      return null;
    }

## BehaviorCopy Anchor Link

  * **Blocks agent execution** : The agent pauses when this tool is called and waits until your UI calls `respond`.
  * **Internal status machine** : The hook manages three states -- `InProgress` (arguments streaming in), `Executing` (waiting for user response), and `Complete` (user has responded). Your render component receives the appropriate props for each state.
  * **Single response** : Call the `respond` callback only once per tool call. Calling it resolves the tool call promise with the provided value.
  * **Stopped runs** : If the run stops before the user answers, the tool call fails with `Human-in-the-loop interaction aborted`, and `respond` has no effect.
  * **Built on`useFrontendTool`**: Internally, this hook wraps `useFrontendTool` with an internally generated handler, so all the same lifecycle behavior (mount/unmount registration, duplicate warnings) applies.
  * **Mount/Unmount lifecycle** : The tool and its render component are registered on mount and removed on unmount.
  * **Calls after unmount** : If the agent calls the tool after it was removed (for example, the component unmounted while the run was in flight), CopilotKit answers the call with a `Tool not found` error result and reports a `TOOL_NOT_FOUND` error, so the conversation can continue. This applies only to tools that were sent to the agent for that run, and only when the run finishes normally; an interrupted, stopped or failed run leaves the call open. A call to a name that was not sent to the agent for that run stays unanswered; register a wildcard tool (`name: "*"`) to handle those.
  * **No return value** : The hook returns `void`.



How is this guide?

GoodBad

[Previous PageuseFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[Next PageuseInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)
