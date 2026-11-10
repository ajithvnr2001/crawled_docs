---
url: https://developers.cloudflare.com/realtime/realtimekit/humans/core/noise-cancellation/
title: Noise Cancellation \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.903091+00:00
---

# Noise Cancellation · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/humans/core/noise-cancellation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)Build for humans

  4. /[Build using Core SDK](https://developers.cloudflare.com/realtime/realtimekit/humans/core/)
  5. /Noise Cancellation



# Noise Cancellation

Last updated Nov 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationInitialisationInitialisation optionsStatesControl methodsManual handling

Use [`@cloudflare/realtimekit-noise-cancellation` ↗︎](https://www.npmjs.com/package/@cloudflare/realtimekit-noise-cancellation) to filter background noise from a participant's microphone. Audio processing runs on their device before sending audio to the meeting.

Noise cancellation supports web applications built with React, Angular, or JavaScript. Mobile SDKs are not supported.

Prerequisite

Initialize a RealtimeKit meeting instance before adding noise cancellation. Refer to [Initialize Core SDK](https://developers.cloudflare.com/realtime/realtimekit/humans/core/).

This page is not available for the **Mobile** platform.

WebMobile

ReactWeb ComponentsAngular

## Installation

Install the package:

npmyarnpnpmbun
    
    
    npm i @cloudflare/realtimekit-noise-cancellation
    
    
    yarn add @cloudflare/realtimekit-noise-cancellation
    
    
    pnpm add @cloudflare/realtimekit-noise-cancellation
    
    
    bun add @cloudflare/realtimekit-noise-cancellation

Import `RealtimeKitNoiseCancellation` in your application:
    
    
    // Skip this import if you use the CDN example.
    import { RealtimeKitNoiseCancellation } from "@cloudflare/realtimekit-noise-cancellation";

Alternatively, use the CDN. The Core SDK script exposes `RealtimeKitClient` globally. Load noise cancellation as an ES module after initializing the meeting:
    
    
    <script src="https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit@latest/dist/browser.js"></script>
    
    <script type="module">
    	RealtimeKitClient.init({
    		authToken: "<participant_auth_token>",
    	})
    		.then((meeting) => {
    			// Continue with your meeting.join() or UI Kit setup.
    
    			// Load and start noise cancellation without delaying join.
    			void import("https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit-noise-cancellation@0.1.0/dist/index.js")
    				.then(({ RealtimeKitNoiseCancellation }) =>
    					RealtimeKitNoiseCancellation.init({ meeting }),
    				)
    				.catch(console.warn);
    		})
    		.catch(console.error);
    </script>

Use the [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/) to fetch the `authToken`.

## Initialisation

Pass your initialized meeting to `init()`. Initialize one noise canceller per meeting instance:
    
    
    const noiseCanceller = await RealtimeKitNoiseCancellation.init({ meeting });

In React, add this setup after `initMeeting()` resolves.

In Angular, add this setup after `RealtimeKitClient.init()` resolves, for example in `ngAfterViewInit()`.

In JavaScript or HTML, add this setup after `RealtimeKitClient.init()` resolves. If you use UI Kit, attach the meeting to the meeting element first.

Keep noise cancellation setup separate from your meeting join or UI flow so participants can join while processing loads.

By default, `autoManage` is `true`. The package starts processing when the microphone is available and maintains processing through mute/unmute and reconnections. If the microphone is muted during initialization, processing starts when you unmute it. The package does not unmute the microphone.

## Initialisation options

Option | Required | Description  
---|---|---  
`meeting` | Yes | The RealtimeKit meeting instance.  
`autoManage` | No | Defaults to `true`. Automatically starts processing when the microphone is available and disposes the instance when the participant leaves. Set to `false` to manage activation and cleanup yourself.  
`onError` | No | Receives runtime and automatic lifecycle errors as an `Error`.  
`signal` | No | An `AbortSignal` that cancels initialization and disposes the instance when aborted.  
  
The package exports the `NoiseCancellationOptions` TypeScript type for these options.

## States

Read `enabled` to check whether noise cancellation is turned on:
    
    
    const isEnabled = noiseCanceller.enabled;

Value | Meaning  
---|---  
`true` | Noise cancellation is turned on.  
`false` | Processing has not started, has been turned off, or the instance has been disposed.  
  
Call `getStatus()` only while processing is active. It returns a `NoiseCancellationStatus` object with processing and capture metadata, including sample rates and model packaging:
    
    
    if (noiseCanceller.enabled) {
    	const status = noiseCanceller.getStatus();
    	console.log(status);
    }

## Control methods

Method | Description  
---|---  
`enable()` | Starts noise cancellation. The microphone must be active and unmuted.  
`disable()` | Stops noise cancellation and restores the microphone's previous processing settings. You can call `enable()` to start processing again.  
`dispose()` | Releases the instance and its resources. Initialize a new instance if you need noise cancellation again.  
  
Each method returns a `Promise<void>`. Handle rejections from `init()` and explicit method calls in your application. The `onError` callback handles runtime and automatic lifecycle errors and does not replace this error handling.

With `autoManage: true`, the package calls `dispose()` when the participant leaves. Temporary disconnections do not dispose the instance. Switching to a connected meeting disposes the old instance; initialize a new one for the new meeting object.

Disposing an instance does not stop the microphone track or close RealtimeKit's `AudioContext`.

## Manual handling

Set `autoManage: false` when your application needs to control when processing starts and when resources are released. Initialization creates the instance without starting noise cancellation or registering automatic cleanup on meeting leave.

  1. Initialize the noise canceller with automatic management turned off:
         
         const noiseCanceller = await RealtimeKitNoiseCancellation.init({
         	meeting,
         	autoManage: false,
         });

  2. After the microphone becomes active and unmuted, start processing:
         
         await noiseCanceller.enable();

  3. (Optional) To temporarily stop filtering, call `disable()`. Call `enable()` again when the microphone is active and unmuted:
         
         await noiseCanceller.disable();

  4. When the participant leaves, your application switches meetings, or the component unmounts, release the instance:
         
         await noiseCanceller.dispose();




You can also pass an `AbortController`'s `signal` to `init()` and abort it during application or component teardown. This disposes the instance even when `autoManage` is `false`.

[PreviousPolls](https://developers.cloudflare.com/realtime/realtimekit/humans/core/polls/)[NextVideo Effects](https://developers.cloudflare.com/realtime/realtimekit/humans/core/video-effects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/humans/core/noise-cancellation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
