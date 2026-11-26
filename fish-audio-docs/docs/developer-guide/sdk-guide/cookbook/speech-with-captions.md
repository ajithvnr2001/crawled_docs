---
url: https://docs.fish.audio/developer-guide/sdk-guide/cookbook/speech-with-captions/
title: Generate speech with SRT/VTT captions - Fish Audio
method: scrapling+scrapegraph
fetched_at: 2026-11-26T17:49:32.910045+00:00
---

# Generate speech with SRT/VTT captions - Fish Audio

> Source: https://docs.fish.audio/developer-guide/sdk-guide/cookbook/speech-with-captions/

## On this page

Back to top

  * Prerequisites
  * Recipe
  * Related



Text to Speech

# Generate speech with SRT/VTT captions

Copy pageCopy page

Generate narration with word-level timestamps from the Python SDK, group the words into caption cues, and write the audio with matching SRT and WebVTT files

Copy pageCopy page

## Prerequisites

Create a Fish Audio account

Sign up for a free Fish Audio account to get started with our API.

  1. [Sign up on fish.audio](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=sign-up)
  2. Fill in your details to create an account, complete steps to verify your account.
  3. Log in to your account and open [Get Started](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=developer-dashboard)



Get your API key

Once you have an account, you’ll need an API key to authenticate your requests.

  1. Log in and open [Get Started](https://fish.audio/app/developers/get-started/?utm_source=docs&utm_medium=prerequisites&utm_content=get-api-key)
  2. Click “Get your API key”: the key is created in one click and shown only once
  3. Copy your key and store it securely



Keep your API key secret! Never commit it to version control or share it publicly.

This recipe needs `fish-audio-sdk` 1.6.0 or later: `pip install -U fish-audio-sdk`.

## Recipe

[`tts.convert_with_timestamps()`](https://docs.fish.audio/features/text-to-speech#word-timestamps) returns the audio together with timed segments, so the captions match the generated speech exactly. Segments are word-level (one character in Chinese and Japanese) and carry no punctuation, so the recipe groups consecutive segments into caption-sized cues before it writes them. Segment `start` / `end` are in **seconds** ; SRT wants `HH:MM:SS,mmm` (comma), WebVTT wants `HH:MM:SS.mmm` (dot). The recipe starts a new cue after a pause longer than 0.6 seconds, or when the cue would grow past 42 characters or 6 seconds. It joins words with a space, except between Chinese or Japanese characters. A segment can have `start` equal to `end`, so a cue with no duration gets a short one that ends no later than the next cue starts. If the next cue starts at the same millisecond, that cue is moved 1 ms later, so every cue ends after it starts and cues never overlap.

Python
    
    
    import re
    
    from fishaudio import FishAudio
    from fishaudio.utils import save
    
    client = FishAudio()
    
    MAX_CHARS = 42  # longest cue text, in characters
    MAX_MS = 6000  # longest cue, in milliseconds
    MAX_GAP_MS = 600  # a longer pause between words starts a new cue
    MIN_MS = 500  # display time for a cue whose words have no duration
    
    # Chinese and Japanese are written without spaces between words.
    NO_SPACE = re.compile(r"[぀-ヿ㐀-䶿一-鿿]")
    
    TEXT = (
        "Welcome to the museum. The east wing opens at nine and closes at six. "
        "Guided tours leave every hour from the main hall, and the café on the "
        "second floor serves lunch until three."
    )
    
    
    def join_words(left: str, right: str) -> str:
        if NO_SPACE.match(left[-1]) and NO_SPACE.match(right[0]):
            return left + right
        return f"{left} {right}"
    
    
    def group_cues(segments) -> list[dict]:
        """Group word-level segments into cues, with start and end in milliseconds."""
        cues = []
        for segment in segments:
            word = segment.text.strip()
            if not word:
                continue
            start, end = round(segment.start * 1000), round(segment.end * 1000)
            if cues:
                cue = cues[-1]
                text = join_words(cue["text"], word)
                if (
                    start - cue["end"] <= MAX_GAP_MS
                    and len(text) <= MAX_CHARS
                    and end - cue["start"] <= MAX_MS
                ):
                    cue["text"], cue["end"] = text, max(cue["end"], end)
                    continue
            cues.append({"start": start, "end": end, "text": word})
    
        # A segment can have start == end. Give a cue with no duration a short one,
        # ending no later than the next cue starts, so every cue ends after it starts.
        for i, cue in enumerate(cues):
            if cue["end"] <= cue["start"]:
                end = cue["start"] + MIN_MS
                if i + 1 < len(cues):
                    end = min(end, cues[i + 1]["start"])
                cue["end"] = max(end, cue["start"] + 1)
                # If the next cue starts at the same millisecond, move it 1 ms later
                # so the two cues don't overlap.
                if i + 1 < len(cues) and cues[i + 1]["start"] < cue["end"]:
                    cues[i + 1]["start"] = cue["end"]
        return cues
    
    
    def format_timestamp(ms: int, separator: str) -> str:
        """HH:MM:SS,mmm for SRT (separator ","), HH:MM:SS.mmm for WebVTT (".")."""
        hours, ms = divmod(ms, 3_600_000)
        minutes, ms = divmod(ms, 60_000)
        seconds, ms = divmod(ms, 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}{separator}{ms:03d}"
    
    
    result = client.tts.convert_with_timestamps(text=TEXT, format="mp3")
    save(result.audio, "narration.mp3")
    
    # Text without words (only punctuation or a sound tag such as "[sigh]") still
    # produces audio, but no timings. Parts of a long text can also lack timings.
    if not result.segments:
        raise SystemExit("No word timings for this text; captions not written.")
    
    cues = group_cues(result.segments)
    
    # SRT: 1-based index, comma decimal separator, blank line between cues.
    with open("narration.srt", "w", encoding="utf-8") as srt:
        for i, cue in enumerate(cues, start=1):
            start = format_timestamp(cue["start"], ",")
            end = format_timestamp(cue["end"], ",")
            srt.write(f"{i}\n{start} --> {end}\n{cue['text']}\n\n")
    
    # WebVTT: same cues, "WEBVTT" header, dot decimal separator.
    with open("narration.vtt", "w", encoding="utf-8") as vtt:
        vtt.write("WEBVTT\n\n")
        for cue in cues:
            start = format_timestamp(cue["start"], ".")
            end = format_timestamp(cue["end"], ".")
            vtt.write(f"{start} --> {end}\n{cue['text']}\n\n")
    
    # duration is None when the end of the audio has no timings.
    length = f"{result.duration:.2f}s" if result.duration is not None else "length not reported"
    print(f"Wrote narration.mp3 ({length}) with {len(cues)} cues")
    

Play `narration.mp3` with `narration.vtt` as its text track, or load `narration.srt` next to it in a video editor. Tune `MAX_CHARS`, `MAX_MS`, and `MAX_GAP_MS` for your player and audience. Captions show the words as they were spoken after [text normalization](https://docs.fish.audio/features/text-to-speech#language), without punctuation: `$42.50` becomes the two words `42` and `50`, not the text you sent. To show your original wording, keep your own sentences and use the segment times only to decide when each sentence starts and ends.

Long text is generated in several chunks. The SDK already places every segment on the timeline of the complete audio, so you don’t need to add `chunk_audio_offset_sec` yourself as the [API reference](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech-stream-with-timestamps) describes for raw requests.

## Related

  * [Text to Speech: word timestamps](https://docs.fish.audio/features/text-to-speech#word-timestamps)
  * [Transcribe audio to SRT/VTT captions](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/transcribe-to-captions), the same cues from a recording instead of generated speech
  * [Text to Speech Stream with Timestamps API](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech-stream-with-timestamps)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/fishaudio/docs/edit/main/developer-guide/sdk-guide/cookbook/speech-with-captions.mdx)[Raise issue](https://github.com/fishaudio/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/developer-guide/sdk-guide/cookbook/speech-with-captions)

[Telephony-grade audio (8 kHz) for IVR and phone](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/telephony-8khz-audio)[Transcribe audio to SRT/VTT captions](https://docs.fish.audio/developer-guide/sdk-guide/cookbook/transcribe-to-captions)
