---
url: https://docs.cloud.google.com/vision/docs/samples/vision-safe-search-detection-gcs/
title: Detect safe search on a Cloud Storage file. \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:43:13.928514+00:00
---

# Detect safe search on a Cloud Storage file.  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-safe-search-detection-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect safe search on a Cloud Storage file. Stay organized with collections  Save and categorize content based on your preferences. 

Perform safe search detection on a file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect explicit content (SafeSearch)](https://docs.cloud.google.com/vision/docs/detecting-safe-search)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectSafeSearch gets image properties from the Vision API for an image at the given file path.
    func detectSafeSearchURI(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	image := vision.NewImageFromURI(file)
    	props, err := client.DetectSafeSearch(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, "Safe Search properties:")
    	fmt.Fprintln(w, "Adult:", props.Adult)
    	fmt.Fprintln(w, "Medical:", props.Medical)
    	fmt.Fprintln(w, "Racy:", props.Racy)
    	fmt.Fprintln(w, "Spoofed:", props.Spoof)
    	fmt.Fprintln(w, "Violence:", props.Violence)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type;
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import com.google.cloud.vision.v1.[SafeSearchAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectSafeSearchGcs {
    
      public static void detectSafeSearchGcs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "gs://your-gcs-bucket/path/to/image/file.jpg";
        detectSafeSearchGcs(filePath);
      }
    
      // Detects whether the specified image on Google Cloud Storage has features you would want to
      // moderate.
      public static void detectSafeSearchGcs(String gcsPath) throws IOException <{
        ListAnnotateIm>ageRequest requests = new<> ArrayLis[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html)();
    
        ImageSource im[gSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html) = ImageSource.new[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.Builder.html#com_google_cloud_vision_v1_ImageSource_Builder_setGcsImageUri_java_lang_String_)().setGcsImageUri(gcsPath).bui[ld](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html)();
        Im[age](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = Image.new[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.Builder.html#com_google_cloud_vision_v1_Image_Builder_setSource_com_google_cloud_vision_v1_ImageSource_)().setSource(imgSource).bui[ld](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html)();
        Featu[re](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = Feature.newBuilder().setType(Type.SAFE_SEARCH_DETECTION).bui[ld](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html)();
        AnnotateImageRequest request [=
            AnnotateIm](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html)ageRequest.newBuilder().addFeatures(feat).setImage(img).build();
        requests.add(request);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background [resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html)
        try (ImageAnnot[atorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) client = ImageAnnotatorClien[t](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html).create()) {
          BatchAnnotateImagesResponse response = client.batchAnnotateImages(r<equests);
          ListA>nnotateImageResponse r[esponses](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__) = response.getResponses[List](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html)();
    
          for (AnnotateImageResponse res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            // For full list of available annotations, see http://g[.co/cloud/vision/doc](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html)s
            SafeSearchAnnotation annotation = res.getSafeSearchAnnotation();
            System.out.format(
                "adult: %s%nmedical: %s%nspoofed: %s%nviolence: %s%nr[acy: %s%](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html#com_google_cloud_vision_v1_SafeSearchAnnotation_getAdult__)n",
                annota[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html#com_google_cloud_vision_v1_SafeSearchAnnotation_getMedical__).getAdult(),
                annotati[on](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html#com_google_cloud_vision_v1_SafeSearchAnnotation_getSpoof__).getMedical(),
                annota[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html#com_google_cloud_vision_v1_SafeSearchAnnotation_getViolence__).getSpoof(),
                annotatio[n](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.SafeSearchAnnotation.html#com_google_cloud_vision_v1_SafeSearchAnnotation_getRacy__).getViolence(),
                annotation.getRacy());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require(&[#39;@google-cloud/vi](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)sion');
    
    // Creates a client
    const client = new[ vision.ImageAnnotat](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)orClient();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const bucketName = 'Bucket where the file resides, e.g. my-bucket';
    // const fileName = 'Path to file within bucket, e.g. path/to/image.png';
    
    // Performs safe search property detection on the remote file
    const [result] = await client.safeSearchDetection(
      `gs://${bucketName}/${fileName}`
    );
    const detections = result.safeSearchAnnotation;
    console.log(`Adult: ${detections.adult}`);
    console.log(`Spoof: ${detections.spoof}`);
    console.log(`Medical: ${detections.medical}`);
    console.log(`Violence: ${detections.violence}`);

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    /**
     * @param string $path GCS path to the image, e.g. "gs://path/to/your/image.jpg"
     */
    function detect_safe_search_gcs(string $path)
    {
        $imageAnnotator = new ImageAnnotatorClient();
    
        # annotate the image
        $response = $image>Annotator-safeSearchDetection($path);
        $safe = >$response-getSafeSearchAnnotation();
    
        if ($safe) {
            $adul>t = $safe-getAdult();
            $medica>l = $safe-getMedical();
            $spoo>f = $safe-getSpoof();
            $violenc>e = $safe-getViolence();
            $rac>y = $safe-getRacy();
    
            # names of likelihood from google.cloud.vision.enums
            $likelihoodName = ['UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY',
            'POSSIBLE', 'LIKELY', 'VERY_LIKELY'];
    
            printf('Adult: %s' . PHP_EOL, $likelihoodName[$adult]);
            printf('Medical: %s' . PHP_EOL, $likelihoodName[$medical]);
            printf('Spoof: %s' . PHP_EOL, $likelihoodName[$spoof]);
            printf('Violence: %s' . PHP_EOL, $likelihoodName[$violence]);
            printf('Racy: %s' . PHP_EOL, $likeli>hoodName[$racy]);
        } else {
            print('No Results.' . PHP_EOL);
        }
    
        $imageAnnotator-close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_safe_search_uri(uri):
        """Detects unsafe features in the file located in Google Cloud Storage or
        on the Web."""
        from google.cloud impor[t](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html) vision
    
        client = vision.ImageAnnotat[orCli](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)ent()
        image = vision.Image()
        image.source.image_uri = uri
    
        response = client.safe_search_detection(image=image)
        safe = response.safe_search_annotation
    
        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = (
            "UNKNOWN",
            "VERY_UNLIKELY",
            "UNLIKELY",
            "POSSIBLE",
            "LIKELY",
            "VERY_LIKELY",
        )
        print("Safe search:")
    
        print(f"adult: {likelihood_name[safe.adult]}")
        print(f"medical: {likelihood_name[safe.medical]}")
        print(f"spoofed: {likelihood_name[safe.spoof]}")
        print(f"violence: {likelihood_name[safe.violence]}")
        print(f"racy: {likelihood_name[safe.racy]}")
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
