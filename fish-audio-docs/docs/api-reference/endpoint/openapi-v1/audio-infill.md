---
url: https://docs.fish.audio/api-reference/endpoint/openapi-v1/audio-infill/
title: Audio Infill - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-18T16:38:20.166220+00:00
---

# Audio Infill - Fish Audio

> Source: https://docs.fish.audio/api-reference/endpoint/openapi-v1/audio-infill/

cURL

Edit a Take
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/audio/infill \
      --header 'Authorization: Bearer <token>' \
      --header 'model: drama-3' \
      --form 'audio=@take.wav' \
      --form-string 'transcript=Next, load the wafer into chamber B and run the standard CVD recipe.' \
      --form 'prefix_frames=45' \
      --form 'suffix_frames=62' \
      --form 'format=mp3' \
      --output edited.mp3

400

401

402

503
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

TTS (v1)

# Audio Infill

Copy pageCopy page

Regenerate part of a recording with drama-3 and get the whole take back: request shapes, positions, length of the new span, response, and streaming

Copy pageCopy page

POST

/

v1

/

audio

/

infill

Try it

cURL

Edit a Take
    
    
    curl --request POST \
      --url https://api.fish.audio/v1/audio/infill \
      --header 'Authorization: Bearer <token>' \
      --header 'model: drama-3' \
      --form 'audio=@take.wav' \
      --form-string 'transcript=Next, load the wafer into chamber B and run the standard CVD recipe.' \
      --form 'prefix_frames=45' \
      --form 'suffix_frames=62' \
      --form 'format=mp3' \
      --output edited.mp3

400

401

402

503
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }
    
    
    {
      "status": 123,
      "message": "<string>",
      "reason": "<string>"
    }

Send the request as `multipart/form-data` (file uploads) or `application/msgpack`. You must include the `model: drama-3` header: only `drama-3` serves this endpoint.

Use this endpoint to apply a script change to an existing recording without re-recording it. Send the take, the full revised `transcript`, and the span to replace. Drama 3 regenerates that span in the speaker’s voice, taken from the audio around it, and returns the whole take with the new span in place. There is no `reference_id`. For a walkthrough with examples, see the [Audio Infill guide](https://docs.fish.audio/features/text-to-speech/audio-infill).

## Request shapes

A request takes one of two shapes. Both require `transcript`. Mixing them, for example `audio` together with `prefix_audio`, returns 400.

Shape| Send| Use it to  
---|---|---  
Edit a take| `audio`, the start of the span (`prefix_frames` or `prefix_seconds`), and its end (`suffix_frames` or `suffix_seconds`)| Replace or insert speech inside one recording.  
Join two clips| `prefix_audio` and, optionally, `suffix_audio`| Generate the speech between two clips, or continue a clip.  
  
## Request fields

Field| Required| Default| Description  
---|---|---|---  
`transcript`| Yes| —| The full text of the result: the kept audio before the change, the new span, and the kept audio after it, with the edit already applied. Sent to the model as written, without text normalization. A missing, empty, or whitespace-only value returns 400.  
`audio`| Edit a take| —| The whole recording to edit, as an audio file.  
`prefix_frames`| Edit a take: this or `prefix_seconds`| —| The frame where the regenerated span starts. Everything before it is kept. A whole number of 0 or more; `0` keeps nothing before the span.  
`prefix_seconds`| Edit a take: this or `prefix_frames`| —| The start of the span in seconds from the start of the take, 0 or more, rounded to the nearest frame.  
`suffix_frames`| Edit a take: this or `suffix_seconds`| —| The frame where the regenerated span ends and the kept audio resumes. A whole number of 0 or more. Equal to the start inserts new speech at that point; the take’s length keeps nothing after the span.  
`suffix_seconds`| Edit a take: this or `suffix_frames`| —| The end of the span in seconds from the start of the take, 0 or more, rounded to the nearest frame.  
`prefix_audio`| Join two clips| —| The clip before the generated speech. Sent alone, the model continues it.  
`suffix_audio`| No| —| The clip after the generated speech. Requires `prefix_audio`.  
`format`| No| `mp3`| Output audio format: `wav`, `pcm`, `mp3`, or `opus`.  
`sample_rate`| No| Unset| Output sample rate in Hz. When unset, the format’s default is used: 44100 Hz for most formats, 48000 Hz for `opus`.  
`mp3_bitrate`| No| `128`| MP3 bitrate in kbps: `64`, `128`, or `192`. Only applies when `format` is `mp3`.  
`opus_bitrate`| No| `-1000`| Opus bitrate in bps: `-1000` (automatic), `24000`, `32000`, `48000`, or `64000`. Only applies when `format` is `opus`.  
  
`format`, `sample_rate`, `mp3_bitrate`, and `opus_bitrate` have the same meaning as on [`/v1/tts`](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech).

  * **Multipart:** send each audio file as a file part and every other field as a text part. Write numbers as decimal text, such as `prefix_seconds=2.1`. Let your HTTP client set the multipart `Content-Type` and boundary.
  * **MessagePack:** set `Content-Type: application/msgpack`, use the same field names, and send each audio file as binary bytes.
  * Number fields accept a number or numeric text in both bodies. Frame positions must be whole numbers: `1.5` for `prefix_frames` returns 400.
  * With curl, send `transcript` with `--form-string` instead of `--form` (`-F`): curl reads a `--form` value that starts with `<` or `@` as a file.



## Positions

When you edit a take, frames `[start, end)` are regenerated and the audio before and after them is kept.

  * Give each side in frames (`prefix_frames`, `suffix_frames`) or in seconds (`prefix_seconds`, `suffix_seconds`). Each side takes one of the two: both for the same side returns 400, and so does a side left out.
  * Positions are absolute, counted from the start of the take, at 44100 / 2048 (about 21.53) frames per second. Seconds are rounded to the nearest frame: `frames = round(seconds × 44100 / 2048)`.
  * A start equal to the end inserts new speech at that point.
  * Some original audio has to stay. A start of 0 together with an end at the end of the take returns 400: with no original audio left, there is no voice to continue, and the model would read the line in a voice it picks itself, different on every request. Keeping only one side, to change the first or the last words of a take, is allowed.
  * For the best results, keep at least 0.75 s of the original on each side and replace at least 0.2 s.
  * The endpoint does not search the audio or the transcript for the words to change. You supply the positions.



## Join two clips

Send `prefix_audio` and, optionally, `suffix_audio`. Drama 3 generates the speech between them. With `prefix_audio` alone, it continues the clip. No positions are needed, and `transcript` covers both clips and the new speech. `suffix_audio` without `prefix_audio` returns 400.

## Length of the new span

The model decides how long the regenerated span is, up to 1024 frames (about 47 s). There is no way to request an exact length yet, so the span can come out shorter or longer than the speech it replaces, and the returned take shorter or longer than the original. If the audio has to stay in sync with picture, such as video or lip-sync, check the length of the result.

## Response

A successful response (HTTP 200) is the whole take as one audio file in `format`, with nothing else in the body. For a join, it is both clips with the new speech between them. The kept parts are re-synthesized together with the new span rather than copied byte for byte. On a human recording, the kept parts also pass through the model’s audio codec.

### Stream events

Send `Accept: text/event-stream` to receive server-sent events instead. Each event is a `data:` line with a JSON object, told apart by its `type`, and the stream ends with `data: [DONE]`.

`type`| Fields| Description  
---|---|---  
`start`| `format`, `sample_rate`, `middle_start_seconds`| Sent first. `middle_start_seconds` is where the new span starts in the result.  
`audio.delta`| `audio`| A base64-encoded piece of the result. Concatenate the decoded `audio` of every `audio.delta` in arrival order to get the same file.  
`done`| `output_frames`, `middle_end_seconds`, `total_seconds`| Sent last. `output_frames` is the number of frames generated for the new span, `middle_end_seconds` is where the new span ends in the result, and `total_seconds` is the length of the result.  
  
Because the length of the new span is not fixed, use `middle_start_seconds` and `middle_end_seconds` to find the new span in the result.

## Errors

Status| When  
---|---  
`400`| `transcript` is missing or empty; the two shapes are mixed; neither `audio` nor `prefix_audio` is sent; a side of the span is left out or given twice; the span covers the whole take; `suffix_audio` is sent without `prefix_audio`; a frame position is not a whole number; or an audio file can’t be decoded. Read the `message`.  
`401`| Invalid or missing API key.  
`402`| No API credit for `drama-3`.  
`502`| The model returned no audio for the new span.  
  
See [Errors](https://docs.fish.audio/api-reference/errors) for the error body and retry guidance.

#### Authorizations

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Headers

model

string

required

The model that regenerates the span. Only `drama-3` serves this endpoint.

Allowed value: `"drama-3"`

#### Body

multipart/form-dataapplication/msgpackmultipart/form-dataapplication/msgpack

transcript

string

required

The full text of the result: the kept audio before the change, the new span and the kept audio after it, with the edit already applied. Sent to the model as written, without text normalization.

audio

file | null

Edit a take: the whole recording to edit. Requires the start of the span (`prefix_frames` or `prefix_seconds`) and its end (`suffix_frames` or `suffix_seconds`). Do not combine with `prefix_audio` / `suffix_audio`.

prefix_frames

integer | null

Edit a take: the frame where the regenerated span starts. Everything before it is kept. A whole number of frames at 44100 / 2048 (about 21.53) frames per second; 0 keeps nothing before the span. Give this or `prefix_seconds`, not both.

Required range: `x >= 0`

prefix_seconds

number | null

Edit a take: `prefix_frames` given in seconds from the start of the take, rounded to the nearest frame. Give this or `prefix_frames`, not both.

Required range: `x >= 0`

suffix_frames

integer | null

Edit a take: the frame where the regenerated span ends and the kept audio resumes. Equal to `prefix_frames` inserts new speech at that point; the take's length keeps nothing after the span. Give this or `suffix_seconds`, not both.

Required range: `x >= 0`

suffix_seconds

number | null

Edit a take: `suffix_frames` given in seconds from the start of the take, rounded to the nearest frame. Give this or `suffix_frames`, not both.

Required range: `x >= 0`

prefix_audio

file | null

Join two clips: the clip before the generated speech. Alone, the model continues it.

suffix_audio

file | null

Join two clips: the clip after the generated speech. Requires `prefix_audio`.

format

enum<string>

default:mp3

Output audio format.

Available options: 

`wav`, 

`pcm`, 

`mp3`, 

`opus`

sample_rate

integer | null

Audio sample rate in Hz. When null, uses the format's default (44100 Hz for most formats, 48000 Hz for opus).

mp3_bitrate

enum<integer>

default:128

MP3 bitrate in kbps. Only applies when format is mp3.

Available options: 

`64`, 

`128`, 

`192`

opus_bitrate

enum<integer>

default:-1000

Opus bitrate in bps. -1000 for automatic. Only applies when format is opus.

Available options: 

`-1000`, 

`24000`, 

`32000`, 

`48000`, 

`64000`

#### Response

200

Request fulfilled, document follows

Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/api-reference/endpoint/openapi-v1/audio-infill.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/api-reference/endpoint/openapi-v1/audio-infill)

[WebSocket TTS with Timestamps](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech-live-with-timestamps)[Speech to Text](https://docs.fish.audio/api-reference/endpoint/openapi-v1/speech-to-text)
