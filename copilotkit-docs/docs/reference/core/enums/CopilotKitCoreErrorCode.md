---
url: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode/
title: CopilotKitCoreErrorCode
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:15.324107+00:00
---

# CopilotKitCoreErrorCode

> Source: https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreErrorCode/

TypeScript/Enums

# CopilotKitCoreErrorCode

Stable error codes surfaced through the onError subscriber callback.

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotKitCoreErrorCode` enumerates the stable, machine-readable codes that [`CopilotKitCore`](https://docs.copilotkit.ai/reference/core/classes/CopilotKitCore) attaches to errors. You encounter it in the [`onError`](https://docs.copilotkit.ai/reference/core/types/CopilotKitCoreSubscriber) callback of a subscriber, where you can branch on `code` to handle specific failures.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotKitCoreErrorCode } from "@copilotkit/core";

## DefinitionCopy Anchor Link

Copy Text
    
    
    enum CopilotKitCoreErrorCode {
      RUNTIME_INFO_FETCH_FAILED = "runtime_info_fetch_failed",
      AGENT_CONNECT_FAILED = "agent_connect_failed",
      AGENT_RUN_FAILED = "agent_run_failed",
      AGENT_RUN_FAILED_EVENT = "agent_run_failed_event",
      AGENT_RUN_ERROR_EVENT = "agent_run_error_event",
      TOOL_ARGUMENT_PARSE_FAILED = "tool_argument_parse_failed",
      TOOL_HANDLER_FAILED = "tool_handler_failed",
      TOOL_NOT_FOUND = "tool_not_found",
      AGENT_NOT_FOUND = "agent_not_found",
      AGENT_THREAD_LOCKED = "agent_thread_locked",
      TRANSCRIPTION_FAILED = "transcription_failed",
      TRANSCRIPTION_SERVICE_NOT_CONFIGURED = "transcription_service_not_configured",
      TRANSCRIPTION_INVALID_AUDIO = "transcription_invalid_audio",
      TRANSCRIPTION_RATE_LIMITED = "transcription_rate_limited",
      TRANSCRIPTION_AUTH_FAILED = "transcription_auth_failed",
      TRANSCRIPTION_NETWORK_ERROR = "transcription_network_error",
      SUBSCRIBER_CALLBACK_FAILED = "subscriber_callback_failed",
      HEADER_RESOLUTION_FAILED = "header_resolution_failed",
    }

## MembersCopy Anchor Link

Prop

Type

`RUNTIME_INFO_FETCH_FAILED?`runtime_info_fetch_failed

`AGENT_CONNECT_FAILED?`agent_connect_failed

`AGENT_RUN_FAILED?`agent_run_failed

`AGENT_RUN_FAILED_EVENT?`agent_run_failed_event

`AGENT_RUN_ERROR_EVENT?`agent_run_error_event

`TOOL_ARGUMENT_PARSE_FAILED?`tool_argument_parse_failed

`TOOL_HANDLER_FAILED?`tool_handler_failed

`TOOL_NOT_FOUND?`tool_not_found

`AGENT_NOT_FOUND?`agent_not_found

`AGENT_THREAD_LOCKED?`agent_thread_locked

CopilotKitCore does not emit the six `TRANSCRIPTION_*` codes below. Transcription errors arrive as `TranscriptionErrorCode` values from `@copilotkit/shared`.

Prop

Type

`TRANSCRIPTION_FAILED?`transcription_failed

`TRANSCRIPTION_SERVICE_NOT_CONFIGURED?`transcription_service_not_configured

`TRANSCRIPTION_INVALID_AUDIO?`transcription_invalid_audio

`TRANSCRIPTION_RATE_LIMITED?`transcription_rate_limited

`TRANSCRIPTION_AUTH_FAILED?`transcription_auth_failed

`TRANSCRIPTION_NETWORK_ERROR?`transcription_network_error

`SUBSCRIBER_CALLBACK_FAILED?`subscriber_callback_failed

`HEADER_RESOLUTION_FAILED?`header_resolution_failed

## UsageCopy Anchor Link

Copy Text
    
    
    copilotkit.subscribe({
      onError: ({ code, error, context }) => {
        if (code === CopilotKitCoreErrorCode.AGENT_THREAD_LOCKED) {
          // Show "Agent is busy, retry?" UI
          return;
        }
        console.error(code, error, context);
      },
    });

How is this guide?

GoodBad

[Previous PageProxiedCopilotRuntimeAgent](https://docs.copilotkit.ai/reference/core/classes/ProxiedCopilotRuntimeAgent)[Next PageCopilotKitCoreRuntimeConnectionStatus](https://docs.copilotkit.ai/reference/core/enums/CopilotKitCoreRuntimeConnectionStatus)
