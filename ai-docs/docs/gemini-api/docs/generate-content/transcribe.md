---
url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe/
title: Audio transcription
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:43:54.719290+00:00
---

# Audio transcription

> Source: https://ai.google.dev/gemini-api/docs/generate-content/transcribe/

The Gemini API converts speech in audio files into text using the Gemini 3.5 Transcribe model (`gemini-3.5-transcribe`). Based on Gemini's audio understanding capabilities, it delivers accurate transcription with automatic language identification, speaker diarization, word-level timestamps, and custom vocabulary hints. It also provides a smart transcription mode featuring disfluency removal and smart formatting.

To transcribe an audio file, upload the audio and pass it to `gemini-3.5-transcribe`:

### Python
    
    
    from google import genai
    
    client = genai.Client()
    
    audio_file = client.files.upload(file="path/to/sample.mp3")
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
    )
    
    print(response.text)
    

### JavaScript
    
    
    import { GoogleGenAI } from "@google/genai";
    
    const ai = new GoogleGenAI({});
    
    const audioFile = await ai.files.upload({
      file: "path/to/sample.mp3",
      mimeType: "audio/mp3",
    });
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
    });
    
    console.log(response.text);
    

### REST
    
    
    # First upload the file via the Files API, then pass its URI:
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ]
      }'
    

## Overview

Gemini 3.5 Transcribe is optimized for speech-to-text tasks. It handles diverse accents, background noise, and multi-language conversations.

Key capabilities include:

  * **Automatic speech recognition (ASR):** Automatically detects languages across 85+ locales. Handles intra-sentence and inter-sentential code-switching without manual configuration.
  * **Custom vocabulary:** Biases recognition toward domain-specific terms, acronyms, and proper names by passing up to 1,000 phrases.
  * **Speaker diarization:** Distinguishes between multiple speakers and attributes spoken segments to distinct labels.
  * **Word-level timestamps:** Generates precise start and end time offsets for each recognized word.
  * **Smart transcription:** Cleans up disfluencies, filler words, repetitions, and applies structured formatting.
  * **Formatting and normalization:** Applies capitalization, punctuation, and inverse text normalization, such as converting "twenty six million dollars" to "$26M".



For general audio reasoning or question answering over audio content, use [Audio understanding](https://ai.google.dev/gemini-api/docs/generate-content/audio). For text-to-speech audio synthesis, use [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation).

## Language detection and hints

By default, the model detects the spoken language automatically. It switches between languages dynamically when speakers code-switch.

To use automatic detection, omit `language_codes` or provide an empty list:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
        config=types.GenerateContentConfig(
            audio_transcription_config=types.AudioTranscriptionConfig(
                language_codes=[],
            )
        ),
    )
    

### JavaScript
    
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
      config: {
        audioTranscriptionConfig: {
          languageCodes: [],
        },
      },
    });
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ],
        "generationConfig": {
          "audioTranscriptionConfig": {
            "languageCodes": []
          }
        }
      }'
    

If you know the language in advance, specify BCP-47 language codes in `language_codes` to improve transcription accuracy (see Supported languages):

### Python
    
    
    config = types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=["es-ES"],
        )
    )
    

### JavaScript
    
    
    const config = {
      audioTranscriptionConfig: {
        languageCodes: ["es-ES"],
      },
    };
    

### REST
    
    
    {
      "generationConfig": {
        "audioTranscriptionConfig": {
          "languageCodes": ["es-ES"]
        }
      }
    }
    

## Custom vocabulary

You can steer the speech model toward uncommon words, technical jargon, brand names, or proper nouns. Supply up to 1,000 terms in the `custom_vocabulary` array (best results are typically achieved with up to 100 terms):

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
        config=types.GenerateContentConfig(
            audio_transcription_config=types.AudioTranscriptionConfig(
                custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
            )
        ),
    )
    

### JavaScript
    
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
      config: {
        audioTranscriptionConfig: {
          customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
        },
      },
    });
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ],
        "generationConfig": {
          "audioTranscriptionConfig": {
            "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
          }
        }
      }'
    

## Speaker diarization

Speaker diarization identifies different voices in the recording and tags each segment with a speaker identifier like `spk_1` or `spk_2`. Up to 8 speakers are supported (attribution for 3 or more speakers is experimental).

Enable diarization by setting `diarization` to `True`:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
        config=types.GenerateContentConfig(
            audio_transcription_config=types.AudioTranscriptionConfig(
                diarization=True,
            )
        ),
    )
    

### JavaScript
    
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
      config: {
        audioTranscriptionConfig: {
          diarization: true,
        },
      },
    });
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ],
        "generationConfig": {
          "audioTranscriptionConfig": {
            "diarization": true
          }
        }
      }'
    

## Word-level timestamps

Word-level timestamps provide exact start and end offsets for every recognized word in the audio stream.

Enable timestamps by setting `word_timestamp` to `True`:

### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
        config=types.GenerateContentConfig(
            audio_transcription_config=types.AudioTranscriptionConfig(
                word_timestamp=True,
            )
        ),
    )
    

### JavaScript
    
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
      config: {
        audioTranscriptionConfig: {
          wordTimestamp: true,
        },
      },
    });
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ],
        "generationConfig": {
          "audioTranscriptionConfig": {
            "wordTimestamp": true
          }
        }
      }'
    

You can combine `diarization` and `word_timestamp` in a single request to receive both speaker labels and word timestamps:

### Python
    
    
    config = types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
            word_timestamp=True,
        )
    )
    

### JavaScript
    
    
    const config = {
      audioTranscriptionConfig: {
        diarization: true,
        wordTimestamp: true,
      },
    };
    

### REST
    
    
    {
      "generationConfig": {
        "audioTranscriptionConfig": {
          "diarization": true,
          "wordTimestamp": true
        }
      }
    }
    

## Transcription modes

Gemini 3.5 Transcribe supports two transcription modes via the `mode` parameter:

  * **`VERBATIM` (default)**: Returns an exact word-for-word transcript of everything spoken, preserving raw filler words ("um", "uh", "like", "you know"), repetitions, pauses, and false starts. Required when using timestamps or speaker diarization.
  * **`SMART` (Smart transcription)**: Optimizes the transcript for reading by applying intelligent post-processing: 
    * **Disfluency removal** : Strips conversational filler words, stuttering, and false starts.
    * **Inline self-corrections** : Resolves spoken corrections directly (for example, _"Let's meet on Tuesday, actually no, Wednesday at two"_ becomes _"Let's meet on Wednesday at 2:00 PM"_).
    * **Automatic structured formatting** : Automatically structures spoken thoughts into paragraphs, numbered lists, bullet points, formatted dates, currencies, and numbers.
    * **Grammatical cleanup** : Applies natural punctuation, sentence casing, and flow.

Spoken audio | `VERBATIM` output | `SMART` (Smart transcription) output  
---|---|---  
"Um, so for the meeting, I think we should, uh, invite Alice and, wait no, Bob and Carol." | "Um so for the meeting I think we should uh invite Alice and wait no Bob and Carol." | "For the meeting, I think we should invite Bob and Carol."  
"First item review budget second item finalize timeline third item send recap" | "first item review budget second item finalize timeline third item send recap" | "1. Review budget  
2\. Finalize timeline  
3\. Send recap"  
  
### Python
    
    
    from google import genai
    from google.genai import types
    
    client = genai.Client()
    
    response = client.models.generate_content(
        model="gemini-3.5-transcribe",
        contents=[audio_file],
        config=types.GenerateContentConfig(
            audio_transcription_config=types.AudioTranscriptionConfig(
                mode="SMART",
            )
        ),
    )
    print(response.text)
    

### JavaScript
    
    
    const response = await ai.models.generateContent({
      model: "gemini-3.5-transcribe",
      contents: [audioFile],
      config: {
        audioTranscriptionConfig: {
          mode: "SMART",
        },
      },
    });
    console.log(response.text);
    

### REST
    
    
    curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
      -H "x-goog-api-key: $GEMINI_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "parts": [
              {
                "fileData": {
                  "fileUri": "YOUR_FILE_URI",
                  "mimeType": "audio/mp3"
                }
              }
            ]
          }
        ],
        "generationConfig": {
          "audioTranscriptionConfig": {
            "mode": "SMART"
          }
        }
      }'
    

## Parsing transcription output

The complete transcript text is returned in `response.text`.

When `word_timestamp` or `diarization` is enabled, the API also returns detailed word-level annotations and speaker labels attached to the candidate parts.

Here is how to extract and iterate over word timestamps and speaker turns:

### Python
    
    
    def extract_word_transcriptions(response):
        words = []
        for candidate in getattr(response, "candidates", []) or []:
            content = getattr(candidate, "content", None)
            for part in getattr(content, "parts", []) or []:
                transcription = getattr(part, "audio_transcription", None)
                if transcription:
                    speaker = getattr(transcription, "speaker_label", "")
                    for word_info in getattr(transcription, "words", []) or []:
                        word = getattr(word_info, "word", "")
                        start = getattr(word_info, "start_offset", "")
                        end = getattr(word_info, "end_offset", "")
                        words.append({
                            "word": word,
                            "speaker": speaker,
                            "start_offset": start,
                            "end_offset": end,
                        })
        return words
    
    words = extract_word_transcriptions(response)
    
    for w in words:
        speaker = f"[{w['speaker']}] " if w["speaker"] else ""
        timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
        print(f"{speaker}{timing}{w['word']}")
    

### JavaScript
    
    
    function extractWordTranscriptions(response) {
      const words = [];
      for (const candidate of response.candidates ?? []) {
        for (const part of candidate.content?.parts ?? []) {
          const transcription = part.audioTranscription;
          if (transcription) {
            const speaker = transcription.speakerLabel ?? "";
            for (const wordInfo of transcription.words ?? []) {
              words.push({
                word: wordInfo.word ?? "",
                speaker: speaker,
                startOffset: wordInfo.startOffset ?? "",
                endOffset: wordInfo.endOffset ?? "",
              });
            }
          }
        }
      }
      return words;
    }
    
    const words = extractWordTranscriptions(response);
    
    for (const w of words) {
      const speaker = w.speaker ? `[${w.speaker}] ` : "";
      const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
      console.log(`${speaker}${timing}${w.word}`);
    }
    

### REST
    
    
    {
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "audioTranscription": {
                  "speakerLabel": "spk_1",
                  "words": [
                    {
                      "word": "Hello",
                      "startOffset": "0.100s",
                      "endOffset": "0.400s"
                    },
                    {
                      "word": "world",
                      "startOffset": "0.500s",
                      "endOffset": "0.800s"
                    }
                  ]
                }
              }
            ],
            "role": "model"
          },
          "finishReason": "STOP"
        }
      ]
    }
    

## Supported languages

The following languages and BCP-47 language codes are supported for Gemini 3.5 Transcribe:

Language | BCP-47 Code | Language | BCP-47 Code  
---|---|---|---  
Afrikaans | `af-ZA` | Japanese | `ja-JP`  
Amharic | `am-ET` | Javanese | `jv-ID`  
Arabic (Egypt) | `ar-EG` | Kabuverdianu | `kea-CV`  
Armenian | `hy-AM` | Kannada | `kn-IN`  
Assamese | `as-IN` | Kazakh | `kk-KZ`  
Azerbaijani | `az-AZ` | Korean | `ko-KR`  
Belarusian | `be-BY` | Kyrgyz | `ky-KG`  
Bengali (Bangladesh) | `bn-BD` | Latvian | `lv-LV`  
Bengali (India) | `bn-IN` | Lingala | `ln-CD`  
Bosnian | `bs-BA` | Lithuanian | `lt-LT`  
Bulgarian | `bg-BG` | Macedonian | `mk-MK`  
Bulgarian (Aromanian) | `rup-BG` | Malay | `ms-MY`  
Burmese | `my-MM` | Malayalam | `ml-IN`  
Cantonese (Traditional) | `yue-Hant-HK` | Maltese | `mt-MT`  
Catalan | `ca-ES` | Mandarin Chinese (Simplified) | `cmn-Hans-CN`  
Cebuano | `ceb` | Marathi | `mr-IN`  
Central Khmer | `km-KH` | Mongolian | `mn-MN`  
Croatian | `hr-HR` | Nepali | `ne-NP`  
Czech | `cs-CZ` | Norwegian | `nb-NO`  
Danish | `da-DK` | Oriya | `or-IN`  
Dutch | `nl-NL` | Polish | `pl-PL`  
English (Great Britain) | `en-GB` | Portuguese (Brazil) | `pt-BR`  
English (India) | `en-IN` | Portuguese (Portugal) | `pt-PT`  
English (United States) | `en-US` | Punjabi | `pa-IN`  
Estonian | `et-EE` | Punjabi (Gurmukhi script) | `pa-Guru-IN`  
Farsi | `fa-IR` | Romanian | `ro-RO`  
Filipino | `fil-PH` | Russian | `ru-RU`  
Finnish | `fi-FI` | Serbian | `sr-RS`  
French | `fr-FR` | Sindhi (Arabic script) | `sd-Arab-IN`  
Galician | `gl-ES` | Slovak | `sk-SK`  
Georgian | `ka-GE` | Slovenian | `sl-SI`  
German | `de-DE` | Spanish (Latin America) | `es-419`  
Greek | `el-GR` | Spanish (United States) | `es-US`  
Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE`  
Hausa | `ha-NG` | Swedish | `sv-SE`  
Hebrew | `he-IL` | Tajik | `tg-TJ`  
Hindi | `hi-IN` | Telugu | `te-IN`  
Hungarian | `hu-HU` | Thai | `th-TH`  
Icelandic | `is-IS` | Turkish | `tr-TR`  
Indian English | `en-IN` | Ukrainian | `uk-UA`  
Indonesian | `id-ID` | Uzbek | `uz-UZ`  
Italian | `it-IT` | Vietnamese | `vi-VN`  
  
## Supported audio formats

Gemini 3.5 Transcribe supports the following audio format MIME types:

  * WAV - `audio/wav`
  * MP3 - `audio/mp3`
  * AIFF - `audio/aiff`
  * AAC - `audio/aac`
  * OGG - `audio/ogg`
  * FLAC - `audio/flac`
  * MPEG - `audio/mpeg`
  * M4A - `audio/m4a`
  * L16 - `audio/l16`
  * Opus - `audio/opus`
  * ALAW - `audio/alaw`
  * MULAW - `audio/mulaw`
  * WebM - `audio/webm`



For the complete list of supported MIME types and parameter schemas, see the [Interactions API reference](https://ai.google.dev/api/interactions-api#Resource:Content).

## Parameter reference

Configure transcription by setting fields within the `audio_transcription_config` object in `GenerateContentConfig`:

Field | Type | Description  
---|---|---  
`language_codes` | Array of strings | BCP-47 language codes (e.g., `["en-US"]`). If omitted or empty (`[]`), the model automatically detects the language and handles code-switching.  
`custom_vocabulary` | Array of strings | Up to 1,000 custom terms, acronyms, or proper names to bias speech recognition. Incompatible with speaker diarization and word-level timestamps.  
`word_timestamp` | Boolean | Set to `True` to include word start and end offsets. If omitted or `False`, no word timestamps are returned. Incompatible with custom vocabulary.  
`diarization` | Boolean | Set to `True` to identify and label distinct speakers. Incompatible with custom vocabulary.  
`mode` | String | Transcription mode. Supported values: `"VERBATIM"` (default) and `"SMART"`. Incompatible with timestamps and diarization.  
  
## Best practices

  * **Provide clean audio:** Ensure audio recordings have clear voice separation and avoid severe clipping.
  * **Provide language hints when known:** If you know the audio language in advance, specify `language_codes` to maximize accuracy.
  * **Target custom vocabulary:** Include only distinct domain terms, brand names, or proper nouns in `custom_vocabulary` rather than common everyday words.
  * **Use the Files API for large recordings:** For files longer than a few seconds, upload the file using `client.files.upload` and pass the returned file to the model contents.



## Limitations

  * **Audio duration:** Standard unary requests support audio files up to 1 hour. Audio processing is limited to 30 minutes when features like speaker diarization or word-level timestamps are enabled.
  * **Word-level timestamps:** Enabling word-level timestamps may degrade overall transcription accuracy.
  * **Speaker diarization:** Speaker diarization supports up to 8 speakers. Speaker attribution for 3 or more speakers is experimental.
  * **Custom vocabulary:** You can provide up to 1,000 terms in `custom_vocabulary`, but best results are typically achieved with up to 100 terms. You cannot combine `custom_vocabulary` with speaker diarization or word-level timestamps; the API rejects requests that specify `custom_vocabulary` alongside either feature.
  * **Mode compatibility:** Smart transcription (`mode: "SMART"`) cannot be combined with `word_timestamp` or `diarization`.



## What's next

  * Stream real-time audio with the [Live transcription guide](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe) using the Live API.
  * Explore [Audio understanding](https://ai.google.dev/gemini-api/docs/generate-content/audio) to analyze, summarize, or query audio content.
  * Learn how to synthesize audio from text using [Text-to-speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation).
  * Check the [Pricing page](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.5-transcribe) for model pricing and token limits.
  * Check the [Files API](https://ai.google.dev/gemini-api/docs/files) guide for details on uploading and managing media files.


