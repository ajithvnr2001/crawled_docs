---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-hotword-rule/
title: Inspect data with a hotword rule \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-01T05:37:49.713504+00:00
---

# Inspect data with a hotword rule  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-hotword-rule/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect data with a hotword rule Stay organized with collections  Save and categorize content based on your preferences. 

This sample uses a custom regex with a hotword rule to increase the likelihood of match.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Customizing match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectDataWithHotwordRule
    {
        public static InspectContentResponse InspectDataHotwordRule(
            string projectId,
            string text,
            string customRegex,
            string hotwordRegex,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) infoType = null)
        {
            // Instantiate dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
                {
                    Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                    Data = Google.Protobuf.ByteString.CopyFromUtf8(text)
                }
            };
    
            // Construct the info type if null.
            var infotype = infoType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "C_MRN" };
    
            // Construct the custom regex detector.
            var customInfoT[ype](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html) = new CustomInfoType
            {
                InfoType = infotype,
                Regex = new Regex { Pattern = customRegex },
                Lik[elihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) = L[ikelihoo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible)d.Possible
            };
    
            // Construct hotword rule.
            var hotwordRule = new DetectionRule.Types.HotwordRule
            {
                HotwordRegex = new Regex { Pattern = hotwordRegex },
                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment
                {
                    FixedLik[elihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) = L[ikelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryLikely).VeryLikely
                },
                Proximity = new DetectionRule.Types.Proximity
                {
                    WindowBefore = 10
                }
            };
    
            // Construct the rule set for the inspect config.
            var inspectionRule[Set](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html) = new InspectionRuleSet
            {
                InfoTypes = { infotype },
                Rules =
                {
              [      ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html)new InspectionRule
                    {
                        HotwordRule = hotwordRule
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectCon[fig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html) = new InspectConfig
            {
                CustomInfoTypes = { customInfoType },
                IncludeQuote = true,
                RuleSet = { inspectionRuleSet },
            };
    
            // Construct the request.
            var requ[est](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html) = new InspectContentRequest
            {
                ParentAsLocationN[ame](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) = new LocationName(projectId, "global"),
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            // Call the API.
            var response = dlp.InspectContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
            {
                Console.WriteLine("Quote: " + f.Quote);
            [    ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)Console.WriteLine("Info type: " + f.InfoType.Name);[
             ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html)   Console.WriteLine("Likelihood: " + f.Likelihood);
            }
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectWithHotWordRules inspects data with hot word rule, it uses custom
    // regex with a hot word rule to increase the likelihood match
    func inspectWithHotWordRules(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Patient's MRN 444-5-22222 and just a number 333-2-33333"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed[,](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)
    	// call the Close method to cleanup its resources.
    	client, err := dlp.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	/[/ Clo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)sing the client safely cleans up background resources.
    	defer client.C&lose()
    
    	// Specify the type an&d content to be inspected.
    	contentItem :&= dlppb.ContentItem{
    		DataItem: dlppb.[ContentItem_ByteItem{
    			](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL)ByteItem: dlppb.ByteContentItem{
    				Type: dlppb.ByteContentItem_TEXT_UTF8,
    				Data: []byte(textToInspect),
    	&		},
    		},
    	}
    
    	// Construct the cu&stom regex detectors
    	customInfoType := dlppb.C&ustomInfoType{
    		InfoType: dlppb.InfoTy&pe{
    			Name: "C_MRN",
    		},
    		Type: dlppb.CustomInfoType_Regex_{
    			Regex: dlppb.CustomInfoTy[pe_Regex](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY){
    				Pattern: "[1-9]{3}-[1-9]{1}-[1-9]{5}",
    			},
    &		},
    		Likelihood: dlppb.Likelihood_POSSIBLE,
    	}
    
    	// Construct &hotword rule.
    	hotWordRule := dlppb.CustomInfoType_DetectionRule_HotwordRule{
    		Hotw&ordRegex: dlppb.CustomInfoType_Regex{
    			Pattern: "(?i)(mrn|medical)(?-i)",
    		},
    		Proximity:& dlppb.CustomInfoType_DetectionRule_Proximity{
    			WindowBefore: int32(10&),
    		},
    		LikelihoodAdjustment: dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    			Adjustme[nt](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY): dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_F&ixedLikelihood{
    				FixedLikelihood: dlppb.Likelihood_VERY_LIKELY,
    			},
    	&	},
    	}
    
    	inspectionRuleSet := dlppb.InspectionRuleSet{
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: dlppb.InspectionRule_HotwordRule{
    					HotwordRule: hotWordRule,
    				},
    			},
    		},
    		InfoTypes: []*dlppb.InfoType{
    	&		customInfoType.InfoType,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := dlppb.InspectContentRequest{
    		&Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				customInfoType,
    			},
    			RuleSet: []*dlppb.InspectionRuleSet{
    				inspectionRuleSet,
    			},
    			IncludeQuote: true,
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Parse the response and process results
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "InfoType Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).[BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class InspectWithHotwordRules {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Patient's MRN 444-5-22222 and just a number 333-2-33333";
        String customRegexPattern = "[1-9]{3}-[1-9]{1}-[1-9]{5}";
        String hotwordRegexPattern = "(?i)(mrn|medical)(?-i)";
        inspectWithHotwordRules(projectId, textToInspect, customRegexPattern, hotwordRegexPattern);
      }
    
      // Inspects a BigQuery Table
      public static void inspectWithHotwordRules(
          String projectId, String textToInspect, String customRegexPattern, String hotwordRegexPattern)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely [clean up any rem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html)aining [background resou](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html)rces.
        try (DlpServiceClient dlp = DlpServiceClient.create()) {
          /[/ Specify the t](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html)ype and content to be [inspected.](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html)
          ByteContentItem byteItem =
            [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html)ByteContentItem.newBuilder()
         [       ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_) [ ](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).setType(B[ytesType](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_).TEXT_UTF8)
                  .setData(ByteString.copyF[romUtf8](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html)(textToInspe[ct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html)))
                  .build();
          ContentItem item = ContentItem.newBuilder().setByteItem(byteItem).build();
    
          // Specify [the r](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html)egex patt[ern t](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html)he inspection [will look ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)for.
          Regex regex = Regex.newBuilder().setPattern(customRegexPattern).build();[
    
          ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html)// Construct[ the cus](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html)tom regex detector.
          InfoType infoType = [InfoType.newBu](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html)ilder().setName("C_MRN&[quot;](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html)).build();
          CustomInfoType customInfoType =
              CustomInfoType.newBuilder().setInfoType(infoType).setRegex(regex).[build();
    
          // S](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html)pecify hotword likelihood adjustme[nt.
          Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html)Adjustment lik[elihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_) =[
             ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) LikelihoodAdjustment.newBuilder().setFixedLikelihood(Likelihood.VERY_LIKELY).build();
    
          // Spe[cify a wi](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html)ndow around a[ finding ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html)to apply a det[ection rule.](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)
          Proximity proximity = Proximity.newBuilder().setWi[ndowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html)(10).build();
    
          // Co[nstruct hot](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html)word rule.
          HotwordRule hotwordRule =
      [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html)   HotwordRule[.newBuilde](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)r()
                  .setHotwordRegex(Regex.newBuilder().setPattern(hotwordRegexPattern).build())
                  .setLikelihoodAdjustment(likelihoodAdjustment)
                  .setProximity(proximity)
                  .buil[d](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html)();
    
          // Construct rule set for the inspec[t config.](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html)
          InspectionRuleSet inspectionRuleSet =
              InspectionRuleSet.newBuilder([)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html)
                  .addInfoTypes(infoType)
                  .addRules(InspectionRule.newBuilder().setHotwordRule(hotwordRule))
                  .build();
    
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html)// Construct the configuration [for the Inspe](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html)ct request.
          InspectConf[ig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_) config =
              InspectConfig.newBuilder()
     [             ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_).addCustomInfoTypes(customInfoType)
         [         ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).setIncludeQuote(true)
        [          ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_).setMinLikelihood(Likelihood.POSSIBLE)
                  .addRuleSet(inspectionRuleSet)
                  .build();
    
          /[/ Construct the Inspe](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html)ct request to be sent[ by the client.](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html)
          InspectContentRequest request =
          [    ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html)InspectContentRequest.newBuilder()
                  .setParent(LocationName.of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
          [        ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html).build();
    
          // Use the client to send the API request.
          InspectContentResponse response = dlp.inspectContent(request);
    
          // Parse the resp[onse and ](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)process results
          System.out.pr[intln](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html)(&quot;Findings:[ "](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__) + response.getResult().getFindingsCount());
          for (Finding f : response.getResult().getFindingsList()) {
            System.out.println("\tQuote: " + f.getQuote());
            System.out.println("\tInfo type: " + f.getInfoType().getName());
            System.out.println("\tLikelihood: " + f.getLikelihood());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require(&[#39;@google-cloud](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)/dlp');
    
    // Instantiates a client
    const dlp = [new DLP.DlpServi](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)ceClient();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Patients MRN 444-5-22222';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = DLP.protos.google.privacy.dlp.v2.Likelihood.POSSIBLE;
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // See https://cloud.google.com/dlp/docs/concepts-infotypes for more information
    // about supported infoTypes.
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // Whether to include the matching string
    // const includeQuote = true;
    
    // Custom hotword regex patten
    // const hotwordRegexPattern = '(?i)(mrn|medical)(?-i)';
    
    async function inspectWithHotwordRule() {
      // Construct item t[o inspect](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html)
      cons[t](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html) item = {
        byte[Item](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html): {
          type: DLP.protos.google.privacy.dlp.v2.ByteContentItem.BytesType
            .TEXT_UTF8,
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Construct a hot word rule
      const hotwordRule = {
        hotwordRegex: {
          pattern: hotwordRegexPattern,
        },
        proximity: {
          windowBefore: 10,
       [ ](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html)},
        lik[elihoodAdju](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html)stment: {
          fixedLikelihood:
            DLP.protos.google.privacy.dlp.v2.Likelihood.VERY_LIKELY,
        },
      };
    
      // Construct a hotword inspection rule
     > const inpectionRuleSet = [
        {
          infoTypes: customInfoTypes.map(
            customInfoType = customInfoType.infoType
          ),
          rules: [{hotwordRule: hotwordRule}],
        },
      ];>
    
      // Assigns likelihood to each match
      customInfoTypes = customInfoType[s](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).map(custo[mInfoTyp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html)e = {
        customInfoType.likelihood =
          DLP.protos.google.privacy.dlp.v2.Likelihood.POSSIBLE;
        return customInfoType;
      });
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: {
          infoTypes: infoTypes,
          customInfoTypes: customInfoTypes,
          minLikelihood: minLikelihood,
          includeQuote: includeQuote,
          limits: {
            maxFindingsPerRequest: maxFindings,
          },
          ruleSet: inpectionRuleSet,
        },
        item: item,
      };
    
      // Run request
      const [response] = await >dlp.inspectContent(request);
      const findings = response.result.fi>ndings;
      if (findings.length  0) {
        console.log('Findings:');
        findings.forEach(finding = {
          if (includeQuote) {
            console.log(`\tQuote: ${finding.quote}`);
          }
          console.log(`\tInfo type: ${finding.infoType.name}`);
          console.log(`\tLikelihood: ${finding.likelihood}`);
        });
      } else {
        console.log('No findings.');
      }
    }
    inspectWithHotwordRule();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\HotwordRule;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\LikelihoodAdjustment;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\Proximity;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * Inspect data with a hotword rule
     * This sample uses a custom regex with a hotword rule to increase the likelihood of match.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_hotword_rule(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = "Patient's MRN 444-5-22222 and just a number 333-2-33333"
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new >ContentItem())
            -setValue($textToInspect);
    
        // Specify the regex pattern the inspection will look for.
        $customRegexPattern = '[1-9]{3}-[1-9]{1}-[1-9]{5}';
        $hotwordRegexPattern = '(?i)(mrn|medical)(?-i)';
    
        // Construct the custom regex detector.
        $c>MrnDetector = (new InfoType())
            -setName('C_MRN');
        $c>ustomInfoType = (new CustomInfoType(>))
            -setInfoType($cMrnDetector)
          >  -setLikelihood(Likelihood::POSSIBL>E)
            -setRegex((new Regex())
                -setPattern($customRegexPattern));
    
        // Specify hotword likelihood adjustment.
        $likelihoodAdj>ustment = (new LikelihoodAdjustment())
            -setFixedLikelihood(Likelihood::VERY_LIKELY);
    
        // Specify a window around a finding to apply a detection ru>le.
        $proximity = (new Proximity())
            -setWindowBefore(10);
    
    >    $hotwordRule = (new HotwordRule())
        >    -setHotwordRegex((new Regex())
            >    -setPattern($hotwordRegexPattern))
            -setLikel>ihoodAdjustment($likelihoodAdjustment)
            -setProximity($proximity);
    
        // Construct rule set for the inspect config.
        $inspect>ionRuleSet = (new InspectionRuleSet())<>/span>
            -setInfoTypes([$cMrnDetector])
            -setRules([
        >        (new InspectionRule())
                    -setHotwordRule($hotwordRule)
            ]);
    
        // Construct the configuration for the Inspect request.
        >$inspectConfig = (new InspectConfig())
            >-setCustomInfoTypes([$customInf>oType])
            -setIncludeQuote(true)
            -setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentR>equest = (new InspectContent>Request())
            -setParent($parent)
       >     -setInspectConfig($inspectConfig>)
            -setItem($item);
        $response = $dlp-inspectContent($inspectContentRequest);
    
       > // Print th>e results
        $findings = $response-getResult()-getFindings();
        if (count($findings) == 0) {
            printf('No findings.' . PHP_EOL);
        } else {
            printf('Findings:' . PHP_EOL);
            foreach ($findings as $>finding) {
                printf('  Quote: %s' . PHP_EOL, $findin>g-getQuote());>
                printf('  Info type: %s' . PHP_EOL, $finding-getInfoType()-getName>());
                printf('  Likelihood: %s' . PHP_EOL, Likelihood::name($finding-getLikelihood()));
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def inspect_data_w_custom_hotwords(
        project: str,
        content_string: str,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze string with medical record
           number custom regex detector, with custom hotwords rules to boost finding
           certainty under some circumstances.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a c[lient.](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
    [    dlp = google](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html).cloud.dlp_v2.DlpServiceClient()
    
        # Construct a custom regex detector info type called "C_MRN",
        # with ###-#-##### pattern, where each # represents a digit from 1 to 9.
        # The detector has a detection likelihood of POSSIBLE.
        custom_info_types = [
            {
                "info_type": {"name": "C_MRN"},
                "regex": {&[quot;p](https://docs.cloud.google.com/python/docs/reference/dlp/latest)a[ttern"](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html);: "[1-9]{3}-[1-9]{1}-[1-9]{5}"},
                "likelihood": google.cloud.dlp_v2.Likelihood.POSSIBLE,
            }
        ]
    
        # Construct a rule set with hotwords "mrn" and "medical", with a likelohood
        # boost to VERY_LIKELY when hotwords are present within the 10 character-
        # window preceding the PII finding.
        hotword_rule = {
            "[hotwor](https://docs.cloud.google.com/python/docs/reference/dlp/latest)d[_regex&quo](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html)t;: {"pattern": "(?i)(mrn|medical)(?-i)"},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.dlp_v2.Likelihood.VERY_LIKELY
            },
            "proximity": {"window_before": 10},
        }
    
        rule_set = [
            {"info_types": [{"name": "C_MRN"}], "rules": [{"hotword_rule": hotword_rule}]}
        ]
    
        # Construct the configuration dictionary with the custom regex info type.
        inspect_config = {
            "custom_info_types": custom_info_types,
       [     "rule](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.inspect_content(
            request={"parent": parent, "inspect_config": inspect_config, "item&quot;: item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
