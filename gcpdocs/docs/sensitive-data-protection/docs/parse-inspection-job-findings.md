---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/parse-inspection-job-findings/
title: Parse findings stored as Protobuf text \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-26T05:40:09.969393+00:00
---

# Parse findings stored as Protobuf text  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/parse-inspection-job-findings/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Parse findings stored as Protobuf text Stay organized with collections  Save and categorize content based on your preferences. 

This code sample shows how to extract details from inspection findings that are saved in Protobuf text format. Do this task if you [saved your inspection findings to Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions#save-findings-cloud-storage). This example converts the exported [`SaveToGcsFindingsOutput`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SaveToGcsFindingsOutput) object into a human-readable format. You can then use the output to analyze individual inspection findings.

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.privacy.dlp.v2.Finding;
    import com.google.privacy.dlp.v2.SaveToGcsFindingsOutput;
    import com.google.protobuf.ByteString;
    import com.google.protobuf.TextFormat;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.io.Reader;
    import java.nio.charset.StandardCharsets;
    
    public class ProcessInspectFindingsSavedToGcs {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String inputPath = "src/test/resources/save_to_gcs_findings.txt";
        processFindingsGcsFile(inputPath);
      }
    
      // Processes a file containing findings from a DLP inspect job.
      public static void processFindingsGcsFile(String inputPath)
          throws IOException {
        SaveToGcsFindingsOutput.Builder builder = SaveToGcsFindingsOutput.newBuilder();
        try (Reader reader =
            new InputStreamReader(new FileInputStream(inputPath), StandardCharsets.UTF_8)) {
          TextFormat.merge(reader, builder);
        }
        SaveToGcsFindingsOutput output = builder.build();
    
        // Parse the converted proto and process results
        System.out.println("Findings: " + output.getFindingsCount());
        for (Finding f : output.getFindingsList()) {
          System.out.println("\tInfo type: " + f.getInfoType().getName());
          System.out.println("\tLikelihood: " + f.getLikelihood());
        }
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
