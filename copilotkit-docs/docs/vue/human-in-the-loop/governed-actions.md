---
url: https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions/
title: Governed Action Approval UI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:24.282790+00:00
---

# Governed Action Approval UI

> Source: https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/vue/human-in-the-loop)[Pausing the Agent for Input](https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/vue/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Governed Action Approval UI

Gate side-effecting agent actions with an approval UI before they execute.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Some agent actions are safe to run immediately, while others should be blocked or paused for user approval before they create side effects. A governed action approval UI gives the user a clear checkpoint:

  * **What** the agent wants to do
  * **Why** it wants to do it
  * **Which reference or policy decision** produced the verdict
  * **What happens next** if the user approves or rejects it



Use this pattern when the agent proposes an action such as sending an email, updating a record, creating a ticket, applying a discount, or calling any write API.

## Action envelope#

Keep the approval payload small, serializable, and vendor-neutral. The agent or backend can attach any policy engine result to the action as long as the UI receives the same basic envelope:
    
    
    type GovernedAction = {
      id: string;
      summary: string;
      tool: string;
      reference: string;
      verdict: "allow" | "deny" | "require_approval";
      arguments: Record<string, unknown>;
    };

The frontend should handle each verdict deterministically:

Verdict| UI behavior  
---|---  
`allow`| Execute the action without asking again, optionally showing an audit note.  
`deny`| Do not execute the action. Show the reason or reference and ask the agent to choose a safer path.  
`require_approval`| Render a user approval card. Execute only if the user approves.  
  
## Inline approval with `useInterrupt`#

If your runtime can pause an agent run, model the approval as an interrupt. The agent proposes the action, the UI renders the checkpoint, and the run resumes with the user's decision. Vue exposes the primary `resolve` and `cancel` methods on `slotProps`:

src/components/GovernedActionApproval.vue
    
    
    <script setup lang="ts">
    import { computed, watchEffect } from "vue";
    import { useInterrupt } from "@copilotkit/vue/v2";
    
    type GovernedAction = {
      id: string;
      summary: string;
      tool: string;
      reference: string;
      verdict: "allow" | "deny" | "require_approval";
      arguments: Record<string, unknown>;
    };
    
    const { slotProps } = useInterrupt({ renderInChat: false });
    const action = computed(
      () => slotProps.value?.interrupt?.metadata?.action as
        | GovernedAction
        | undefined,
    );
    
    async function approve(approved: boolean) {
      const current = action.value;
      if (!current || !slotProps.value) return;
    
      await slotProps.value.resolve({
        approved,
        actionId: current.id,
        reference: current.reference,
      });
    }
    
    watchEffect(() => {
      if (action.value?.verdict === "allow") void approve(true);
      if (action.value?.verdict === "deny") void slotProps.value?.cancel();
    });
    </script>
    
    <template>
      <section v-if="action" class="rounded-lg border p-4 shadow-sm">
        <p>
          {{
            action.verdict === "allow"
              ? "Allowed by policy"
              : action.verdict === "deny"
                ? "Blocked by policy"
                : "User approval required"
          }}
        </p>
        <h3>{{ action.summary }}</h3>
        <p>Tool: {{ action.tool }}</p>
        <p>Reference: {{ action.reference }}</p>
        <pre>{{ JSON.stringify(action.arguments, null, 2) }}</pre>
        <div v-if="action.verdict === 'require_approval'">
          <button @click="approve(true)">Approve and run</button>
          <button @click="approve(false)">Reject</button>
        </div>
      </section>
    </template>

On resume, the agent should execute only when it receives an approved response for the same action id and reference:
    
    
    type ApprovalResponse = {
      approved: boolean;
      actionId: string;
      reference: string;
    };
    
    async function handleApproval(
      action: GovernedAction,
      response: ApprovalResponse,
    ) {
      if (
        response.approved &&
        response.actionId === action.id &&
        response.reference === action.reference
      ) {
        return executeSideEffect(action.tool, action.arguments);
      }
    
      return {
        skipped: true,
        reason: "The user did not approve this action.",
      };
    }

## Tool-call approval with `useHumanInTheLoop`#

For LLM-initiated pauses, register the approval checkpoint as a human-in-the-loop tool. The model asks to call `approve_governed_action`, your Vue component renders the card, and the tool result tells the agent whether it may continue:

src/components/GovernedActionTool.vue
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    import GovernedActionCard from "./GovernedActionCard.vue";
    
    const governedActionSchema = z.object({
      id: z.string(),
      summary: z.string(),
      tool: z.string(),
      reference: z.string(),
      verdict: z.enum(["allow", "deny", "require_approval"]),
      arguments: z.record(z.unknown()),
    });
    
    useHumanInTheLoop({
      name: "approve_governed_action",
      description:
        "Ask the user to approve a governed side-effect action before it runs.",
      parameters: governedActionSchema,
      render: GovernedActionCard,
    });
    </script>
    
    <template><p>Governed action tool registered.</p></template>

The render component receives partial `args` while the tool call streams and a `respond` callback only while the call is executing. It should call `respond` with the same `{ approved, actionId, reference }` envelope used by the interrupt path:

src/components/GovernedActionCard.vue
    
    
    <script setup lang="ts">
    import { computed, ref, watchEffect } from "vue";
    
    const props = defineProps<{
      args: {
        id?: string;
        summary?: string;
        reference?: string;
        verdict?: "allow" | "deny" | "require_approval";
      };
      respond?: (result: unknown) => Promise<void>;
    }>();
    
    const submitted = ref(false);
    const ready = computed(() =>
      Boolean(props.respond && props.args.id && props.args.reference && props.args.verdict),
    );
    
    function submitDecision(approved: boolean) {
      if (!ready.value || submitted.value || !props.respond) return;
      if (approved && props.args.verdict === "deny") return;
      submitted.value = true;
      void props.respond({
        approved,
        actionId: props.args.id,
        reference: props.args.reference,
      });
    }
    
    watchEffect(() => {
      if (props.args.verdict === "allow") submitDecision(true);
      if (props.args.verdict === "deny") submitDecision(false);
    });
    </script>
    
    <template>
      <section>
        <p v-if="props.args.verdict === 'allow'">Allowed by policy</p>
        <p v-else-if="props.args.verdict === 'deny'">Blocked by policy</p>
        <p>{{ props.args.summary ?? "Preparing approval…" }}</p>
        <div v-if="ready && !submitted && props.args.verdict === 'require_approval'">
          <button @click="submitDecision(true)">Approve and run</button>
          <button @click="submitDecision(false)">Reject</button>
        </div>
      </section>
    </template>

## Provider setup#

Both composables must run in components beneath `CopilotKitProvider`:

src/App.vue
    
    
    <script setup lang="ts">
    import { CopilotChat, CopilotKitProvider } from "@copilotkit/vue/v2";
    import GovernedActionApproval from "./components/GovernedActionApproval.vue";
    import GovernedActionTool from "./components/GovernedActionTool.vue";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <GovernedActionApproval />
        <GovernedActionTool />
        <CopilotChat />
      </CopilotKitProvider>
    </template>

## Recommended guardrails#

  * Check policy on the server before presenting the approval, not only in the browser.
  * Include a stable `action.id` and `reference` so the approval cannot be replayed for a different action.
  * Show the exact action arguments before the user approves.
  * Treat `deny` as terminal for that proposed action; do not execute a denied side effect from a later UI callback.
  * Log the proposal, verdict, user decision, and execution result so the action is auditable.



## Going further#

  * [Pausing the Agent for Input](https://docs.copilotkit.ai/useInterrupt) — use graph-enforced interrupts when the backend must stop before a side effect.
  * [HITL Overview](https://docs.copilotkit.ai/human-in-the-loop) — compare tool-based and interrupt-based human-in-the-loop patterns.
  * [Frontend Tools](https://docs.copilotkit.ai/frontend-tools) — register browser-side tools that can display approval UI or update application state.


