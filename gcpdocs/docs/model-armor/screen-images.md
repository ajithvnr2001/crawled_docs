---
url: https://docs.cloud.google.com/model-armor/screen-images/
title: Screen images \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T11:10:59.497032+00:00
---

# Screen images  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/screen-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Screen images Stay organized with collections  Save and categorize content based on your preferences. 

Model Armor screens standalone images and images embedded within supported rich text documents in prompts and responses to help protect your generative AI applications from risks embedded within images.

Model Armor screens images using the following methods:

  * **Visual scanning** : Screens visual content within images for sensitive objects and subject matter using the [advanced Sensitive Data Protection filter](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#advanced_sdp_configuration). For more information, see [object infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#objects-images) and [image context infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#image-context).
  * **Optical character recognition (OCR)** : Extracts text from images and screens that text against configured filters, including [responsible AI safety categories](https://docs.cloud.google.com/model-armor/overview#ma-responsible-ai-safety-categories), [prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection), [malicious URLs](https://docs.cloud.google.com/model-armor/overview#ma-malicious-url-detection), and [Sensitive Data Protection](https://docs.cloud.google.com/model-armor/overview#ma-sensitive-data-prot) infoTypes.



## Specifications and limitations

Consider the following specifications and limitations when you use Model Armor to screen images:

  * **Supported image formats** : Model Armor screens standalone images in JPEG, PNG, and BMP formats. It also extracts and screens embedded images from [supported rich text files](https://docs.cloud.google.com/model-armor/overview#ma-support-screening-pdfs).
  * **Size limits** : Each standalone image must be 4 MB or smaller. Rich text files must be 4 MB or smaller in total file size and contain at most 5 embedded images. Exceeding any of these limits causes Model Armor to skip scanning the entire file. For more information, see [File size system limit](https://docs.cloud.google.com/model-armor/quotas#input-size-limit) and Screen embedded images in documents.
  * **Standalone prompts** : When you call the `SanitizeUserPrompt` and `SanitizeModelResponse` methods with standalone images, Model Armor screens a single image per request. Screening multiple standalone images in a single request isn't supported. In addition, Model Armor doesn't support standalone prompts that combine text and images in a single request. However, you can screen rich text documents containing both text and images by enabling both text and image modalities.
  * **De-identification** : When you configure a Sensitive Data Protection de-identify template, Model Armor redacts either text or standalone images, not both. De-identification isn't supported for rich text documents when the image modality (`MODALITY_IMAGE`) is selected. For more information, see Redact sensitive data in standalone images and Screen embedded images in documents.
  * **Streaming** : Model Armor [streaming methods](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#sanitize-streaming) support only textual input and don't support images or files.
  * **Supported integrations** : You can screen images by calling the Model Armor REST API directly or through the [Gemini Enterprise integration](https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration). All other Model Armor integrations scan and sanitize only text. For more information, see [Supported modalities](https://docs.cloud.google.com/model-armor/integrations#modalities).
  * **Regional availability** : Image screening is supported only in specific multi-regions. If you send a prompt containing an image to an endpoint where Model Armor doesn't support image screening, the `invocationResult` field in the response indicates `FAILURE`. For a list of locations that support image screening, see [Supported features by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).



## Token calculation and pricing for images

Model Armor uses a unified [token-based pricing model](https://docs.cloud.google.com/model-armor/overview#pricing) where image tokens are billed at the same rate as text tokens.

You aren't billed when Model Armor rejects or skips an input before filter processing, such as empty inputs or files and images that exceed the [file size or embedded image limits](https://docs.cloud.google.com/model-armor/quotas#input-size-limit). However, if an input passes initial validation, you are billed for the calculated tokens even in the following cases:

  * **All detectors are skipped** : Some or all configured filters (detectors) are skipped and return `EXECUTION_SKIPPED` (for example, when an image payload within the 4 MB limit can't be parsed by detectors, or when a filter is skipped for a modality).
  * **Non-image files wrapped with the`IMAGE` byte data type**: A non-image file (such as a ZIP, CSV, or Microsoft Word document) is sent with `byteDataType` set to `IMAGE` (up to 4 MB). Model Armor bills the request using the standalone image token calculation even though filters return `EXECUTION_SKIPPED`.



Model Armor calculates tokens for images and documents based on the input type and configured modalities:

  * **Standalone images** : Model Armor converts each processed image (up to 4 MB) into tokens using a base count of 5,000 tokens per image, plus 1,000 tokens per megabyte (MB) of image size. When calculating size-based tokens, Model Armor rounds the image size up to the next whole MB:

Tokens per image = 5,000 + (1,000 × image size in MB, rounded up to the next whole MB)

Text extracted from an image through OCR is included in the image token calculation and doesn't incur separate text token charges.

  * **[Rich text documents](https://docs.cloud.google.com/model-armor/overview#ma-support-screening-pdfs)** : Token calculation depends on the [modalities configured in your template](https://docs.cloud.google.com/model-armor/manage-templates#select-modality):

    * **Text modality (`MODALITY_TEXT`)**: Model Armor calculates tokens from the text extracted from the document (about 4 characters per token). Embedded images aren't extracted or billed.
    * **Image modality (`MODALITY_IMAGE`)**: Model Armor calculates tokens individually for each processed embedded image using the image token formula. Document text isn't billed.
    * **Text and image modalities (`MODALITY_TEXT` and `MODALITY_IMAGE`)**: Model Armor calculates the total token count as the sum of the tokens from the extracted document text and the tokens for each processed embedded image.



The following table shows examples of how Model Armor calculates tokens for processed images:

Image size | Rounded size for calculation | Token calculation | Total tokens  
---|---|---|---  
500 KB | 1 MB | 5,000 + (1 × 1,000) | 6,000 tokens  
1.9 MB | 2 MB | 5,000 + (2 × 1,000) | 7,000 tokens  
4 MB | 4 MB | 5,000 + (4 × 1,000) | 9,000 tokens  
  
## Before you begin

Before you screen images, complete the following prerequisites:

### Create or update a template with the image modality enabled

When you [create or update a template](https://docs.cloud.google.com/model-armor/manage-templates#create-ma-template), [select the modality](https://docs.cloud.google.com/model-armor/manage-templates#select-modality) to include `MODALITY_IMAGE` (either **Image** or **All** in the Google Cloud console, or `"modalities": ["MODALITY_IMAGE", "MODALITY_TEXT"]` in `templateMetadata` when using the REST API). If you don't specify a modality, leave the `modalities` field empty, or specify only `MODALITY_TEXT`, Model Armor scans only text and returns `EXECUTION_SKIPPED` for filters that scan the skipped modality.

### Obtain the required permissions

Ensure that you have the required Identity and Access Management roles to sanitize prompts and responses (such as `roles/modelarmor.user`) and, if you use the advanced Sensitive Data Protection mode across projects, grant the required DLP roles to the Model Armor service agent. For instructions, see [Obtain the required permissions](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#required-permissions).

## Sanitize standalone images

To screen a standalone image in a user prompt or model response, set the `byteDataType` field to `IMAGE` and provide the base64-encoded image in a supported format (JPEG, PNG, or BMP) in the `byteData` field.

Use the following command to sanitize a prompt that contains an image:
    
    
    curl -X POST \
        -d "$(jq -n \
        --arg data "$(base64 -w 0 -i IMAGE)" \
        '{userPromptData: {byteItem: {byteDataType: "IMAGE", byteData: $data}}}')" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeUserPrompt"

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the template.
  * `LOCATION`: the location of the template.
  * `TEMPLATE_ID`: the ID of a template that is configured to scan for images (`MODALITY_IMAGE`).
  * `IMAGE`: the path to the image file in a supported format.



The response is similar to the following:
    
    
    {
      "sanitizationResult": {
        "filterMatchState": "MATCH_FOUND",
        "invocationResult": "SUCCESS",
        "filterResults": {
          "csam": {
            "csamFilterFilterResult": {
              "executionState": "EXECUTION_SUCCESS",
              "matchState": "NO_MATCH_FOUND"
            }
          },
          "pi_and_jailbreak": {
            "piAndJailbreakFilterResult": {
              "executionState": "EXECUTION_SUCCESS",
              "matchState": "MATCH_FOUND",
              "confidenceLevel": "HIGH"
            }
          },
          "sdp": {
            "sdpFilterResult": {
              "inspectResult": {
                "executionState": "EXECUTION_SUCCESS",
                "matchState": "MATCH_FOUND"
              }
            }
          }
        }
      }
    }

### Redact sensitive data in standalone images

When you use the Sensitive Data Protection advanced mode, Model Armor redacts sensitive findings in standalone images if you configure your Model Armor template with both a Sensitive Data Protection inspect template and a Sensitive Data Protection de-identify template. Make sure that you configure [image redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images) in the de-identify template. For more information about configuring Sensitive Data Protection in Model Armor, see [Set Sensitive Data Protection settings](https://docs.cloud.google.com/model-armor/manage-templates#set-sdp-settings). For information about de-identification limitations, see Specifications and limitations and Screen embedded images in documents.

**Note:** When you use Sensitive Data Protection advanced mode, the `BASIC_AUTH_HEADER` infoType might be reported in detection results even if it isn't explicitly included in the configured inspection template.

The following example shows the filter configuration with [Sensitive Data Protection redaction enabled](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images):
    
    
    {
      "filterConfig": {
        "sdpSettings": {
          "advancedConfig": {
            "inspectTemplate": "projects/PROJECT_ID/locations/LOCATION/inspectTemplates/INSPECT_TEMPLATE_ID",
            "deidentifyTemplate": "projects/PROJECT_ID/locations/LOCATION/deidentifyTemplates/DEIDENTIFY_TEMPLATE_ID"
          }
        }
      }
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the Sensitive Data Protection templates.
  * `LOCATION`: the location of the templates.
  * `INSPECT_TEMPLATE_ID`: the ID of the inspect template.
  * `DEIDENTIFY_TEMPLATE_ID`: the ID of the de-identify template.



When you sanitize a standalone image using a template with image redaction enabled, the response includes the redacted image and bounding box coordinates for each finding:
    
    
    {
      "sanitizationResult": {
        "filterMatchState": "MATCH_FOUND",
        "invocationResult": "SUCCESS",
        "filterResults": {
          "csam": {
            "csamFilterFilterResult": {
              "executionState": "EXECUTION_SUCCESS",
              "matchState": "NO_MATCH_FOUND"
            }
          },
          "sdp": {
            "sdpFilterResult": {
              "redactResult": {
                "executionState": "EXECUTION_SUCCESS",
                "matchState": "MATCH_FOUND",
                "redactedImage": "[REDACTED_IMAGE]",
                "findings": [
                  {
                    "infoType": "EMAIL_ADDRESS",
                    "likelihood": "LIKELY",
                    "location": {
                      "contentLocations": [
                        {
                          "imageFindingLocation": {
                            "boundingBoxes": {
                              "top": 16,
                              "left": 121,
                              "width": 620,
                              "height": 90
                            }
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            }
          }
        }
      }
    }

## Screen embedded images in documents

When you enable the image modality (`MODALITY_IMAGE`) in your template and sanitize a rich text document (`PDF`, `WORD_DOCUMENT`, `EXCEL_DOCUMENT`, or `POWERPOINT_DOCUMENT`), Model Armor automatically extracts and screens up to 5 embedded images in the document. If you enable both `MODALITY_TEXT` and `MODALITY_IMAGE`, Model Armor screens both the document text and the embedded images.

Whether you enable only `MODALITY_IMAGE` or both `MODALITY_IMAGE` and `MODALITY_TEXT`, Model Armor skips scanning the entire document, including both text and embedded images, without partial scanning. It returns `EXECUTION_SKIPPED` for all configured filters, including inspection, and an overall `filterMatchState` of `NO_MATCH_FOUND` in the following cases:

  * The document exceeds the [4 MB file size limit or the 5-image limit](https://docs.cloud.google.com/model-armor/quotas#input-size-limit).
  * A Sensitive Data Protection de-identify template is configured. To inspect rich text documents when the image modality is enabled, configure only an inspect template without a de-identify template.



For code samples showing how to send file-based prompts using REST and client libraries, see [File-based prompts](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#file-prompts).

### Partial file inspection

Model Armor returns a partial result (`invocationResult: PARTIAL`) only at the filter (detector) level across the entire file, rather than per image:

  * **Per-image failure (entire file skipped)** : If some embedded images in a file are scanned successfully but one or more other images in the file fail to be extracted or scanned, Model Armor skips the entire file. It returns `executionState: EXECUTION_SKIPPED` for all configured filters and an overall `filterMatchState` of `NO_MATCH_FOUND`.
  * **Detector-level failure (partial result)** : If some configured filters succeed across the file while one or more other filters are skipped for the entire file (for example, because of a detector timeout), Model Armor returns a partial result with the following fields: 
    * **Invocation result** : The `invocationResult` field is set to `PARTIAL` (instead of `SUCCESS`), indicating that one or more configured filters were skipped for the file while other filters completed inspection.
    * **Filter execution state** : Filters that were skipped for the file report `executionState: EXECUTION_SKIPPED`. Filters that completed inspection across the file report `executionState: EXECUTION_SUCCESS`.
    * **Match state** : The `filterMatchState` field reflects the findings from the filters that completed inspection. If any completed filter detects a violation, `filterMatchState` is set to `MATCH_FOUND`. If no violations are detected by the completed filters, `filterMatchState` is set to `NO_MATCH_FOUND`.



#### Security considerations with partial inspection

From a security standpoint, an `invocationResult` value of `PARTIAL` indicates that one or more configured filters couldn't evaluate the file. Potential security threats or policy violations targeted by the skipped filters might still be present in the file.

By default, if the filters that completed inspection detect no policy violations, `filterMatchState` is `NO_MATCH_FOUND`. If your application requires all configured filters to complete inspection before allowing prompts to reach an AI model, inspect the `invocationResult` field in the response. If the value is `PARTIAL`, configure your application logic to handle the request according to your organization's risk tolerance, such as rejecting the prompt or routing it for secondary review.

#### Example partial inspection response

The following example shows a response where the child sexual abuse material (CSAM) filter was skipped for the file while other configured filters completed inspection. Model Armor returns an `invocationResult` of `PARTIAL`, an `EXECUTION_SKIPPED` status for the CSAM filter, and `EXECUTION_SUCCESS` for the remaining filters:
    
    
    {
      "sanitizationResult": {
        "filterMatchState": "NO_MATCH_FOUND",
        "invocationResult": "PARTIAL",
        "filterResults": {
          "csam": {
            "csamFilterFilterResult": {
              "executionState": "EXECUTION_SKIPPED",
              "matchState": "NO_MATCH_FOUND"
            }
          },
          "pi_and_jailbreak": {
            "piAndJailbreakFilterResult": {
              "executionState": "EXECUTION_SUCCESS",
              "matchState": "NO_MATCH_FOUND"
            }
          },
          "sdp": {
            "sdpFilterResult": {
              "inspectResult": {
                "executionState": "EXECUTION_SUCCESS",
                "matchState": "NO_MATCH_FOUND"
              }
            }
          }
        }
      }
    }

## What's next

  * [Create and manage Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates).
  * [Sanitize prompts and responses](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses).
  * Check [feature availability by region](https://docs.cloud.google.com/model-armor/feature-availability-by-region#supported-by-region).
  * Review [quotas and system limits](https://docs.cloud.google.com/model-armor/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
