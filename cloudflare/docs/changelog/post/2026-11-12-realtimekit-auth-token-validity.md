---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-realtimekit-auth-token-validity/
title: Set custom validity windows for RealtimeKit auth tokens \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.961788+00:00
---

# Set custom validity windows for RealtimeKit auth tokens · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-realtimekit-auth-token-validity/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Set custom validity windows for RealtimeKit auth tokens

[Realtime](https://developers.cloudflare.com/realtime/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) auth tokens now support custom validity windows, and you can revoke a single token. When your backend adds a [participant](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/) to a meeting, it gets back an auth token that the participant's app uses to join.

Previously, every token was valid for 100 days from the moment it was issued. Now you can choose when a token starts and stops working, for example only during a scheduled class or interview, so a shared link stops working once the session is over. Pass `not_before` and `expires_on` in the `token` object when you [add a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/):

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Realtime Admin`
  * `Realtime`

Add a participantbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings/$MEETING_ID/participants" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Mary Sue",
    		"preset_name": "<preset_name>",
    		"custom_participant_id": "<uuid_of_the_user_in_your_system>",
    		"token": {
    				"not_before": "2026-12-01T15:00:00Z",
    				"expires_on": "2026-12-01T17:00:00Z"
    		}
    	}'

Both fields are optional, so existing integrations keep getting 100-day tokens.

You can also [revoke a single token](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/#revoke-tokens) without setting the whole meeting to `INACTIVE`. If the participant is in the meeting, RealtimeKit removes them. A revoked token can take up to 60 seconds to stop working everywhere, so delete the participant instead if you need to block them immediately.

RealtimeKit rejects expired, not yet valid, and revoked tokens before the participant enters the meeting, so you are not billed for them.

#### Learn more

  * [Token validity and refresh](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/#token-validity-and-refresh)
  * [Revoke tokens](https://developers.cloudflare.com/realtime/realtimekit/concepts/participant/#revoke-tokens)
  * [Add participant API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/)
  * [Refresh participant token API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/refresh_participant_token/)


