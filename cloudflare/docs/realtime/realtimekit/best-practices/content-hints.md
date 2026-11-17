---
url: https://developers.cloudflare.com/realtime/realtimekit/best-practices/content-hints/
title: Content hints \u00b7 Cloudflare Realtime docs
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.483066+00:00
---

# Content hints · Cloudflare Realtime docs

> Source: https://developers.cloudflare.com/realtime/realtimekit/best-practices/content-hints/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Realtime](https://developers.cloudflare.com/realtime/)
  3. /…

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/)

  4. /Best practices
  5. /Content hints



# Content hints

Last updated Nov 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a hintApply hints to local tracks

Use `MediaStreamTrack.contentHint` to describe the content of local media tracks. The browser can use this hint to guide media processing and encoding.

This guide applies to the RealtimeKit Web SDKs, including applications that use Web UI Kit.

This page is not available for the **Mobile** platform.

WebMobile

ReactWeb ComponentsAngular

## Choose a hint

Choose a hint based on the content, not only the capture source.

Track kind | Hint | Use case  
---|---|---  
Audio | `"speech"` | Microphone conversations and spoken presentations.  
Audio | `"music"` | Music performances or shared audio that contains music.  
Audio | `"speech-recognition"` | Audio intended for machine speech recognition.  
Video | `"motion"` | Camera video, movies, or games where smooth motion matters.  
Video | `"detail"` | Presentations, diagrams, or artwork where detail matters.  
Video | `"text"` | Documents, code editors, or web pages with text.  
Either | `""` | Clear the explicit hint and let the browser choose.  
  
For example, use `"text"` for a shared code editor, but `"motion"` for a shared video. Use `"music"` for shared music and `"speech"` for spoken content.

## Apply hints to local tracks

Set hints on the outgoing tracks exposed by [`meeting.self`](https://developers.cloudflare.com/realtime/realtimekit/humans/core/local-participant/#media-properties). Listen to `audioUpdate`, `videoUpdate`, and `screenShareUpdate` to apply hints when tracks become available or change.

  1. [Initialize the Core SDK](https://developers.cloudflare.com/realtime/realtimekit/humans/core/#initialize-core-sdk) and obtain the `meeting` instance.

  2. Register update listeners and apply hints to existing tracks.

This example assumes spoken microphone audio, camera video, and presentation screen sharing. It uses `"music"` for optional shared audio. Change these hints to match your content.
         
         function applyContentHints(meeting) {
         	const { self } = meeting;
         
         	function setHint(track, hint) {
         		if (track && "contentHint" in track) {
         			track.contentHint = hint;
         		}
         	}
         
         	function handleAudioUpdate({ audioTrack }) {
         		setHint(audioTrack, "speech");
         	}
         
         	function handleVideoUpdate({ videoTrack }) {
         		setHint(videoTrack, "motion");
         	}
         
         	function handleScreenShareUpdate({ screenShareTracks }) {
         		setHint(screenShareTracks?.video, "detail");
         		setHint(screenShareTracks?.audio, "music");
         	}
         
         	self.on("audioUpdate", handleAudioUpdate);
         	self.on("videoUpdate", handleVideoUpdate);
         	self.on("screenShareUpdate", handleScreenShareUpdate);
         
         	// Initialization may have already created local tracks.
         	handleAudioUpdate(self);
         	handleVideoUpdate(self);
         	handleScreenShareUpdate(self);
         
         	return () => {
         		self.off("audioUpdate", handleAudioUpdate);
         		self.off("videoUpdate", handleVideoUpdate);
         		self.off("screenShareUpdate", handleScreenShareUpdate);
         	};
         }
         
         const removeContentHintListeners = applyContentHints(meeting);

  3. When your component unmounts or before you replace the meeting instance, remove the listeners you registered.
         
         removeContentHintListeners();




A content hint belongs to an individual track. The example automatically reapplies hints when update events provide replacement tracks. This covers device changes and switches to a different shared screen.

For browser compatibility and property details, refer to [`MediaStreamTrack.contentHint` on MDN ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack/contentHint/) and [Can I use: content hints ↗︎](https://caniuse.com/?search=contentHint).

[PreviousVideo resolution and simulcast](https://developers.cloudflare.com/realtime/realtimekit/best-practices/video-and-simulcast/)[NextFAQ](https://developers.cloudflare.com/realtime/realtimekit/faq/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/realtime/realtimekit/best-practices/content-hints.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
