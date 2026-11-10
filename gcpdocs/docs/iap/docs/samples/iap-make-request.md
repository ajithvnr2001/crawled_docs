---
url: https://docs.cloud.google.com/iap/docs/samples/iap-make-request/
title: Authenticate from a service account \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T06:09:43.925666+00:00
---

# Authenticate from a service account  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/samples/iap-make-request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Samples ](https://docs.cloud.google.com/iap/docs/samples)



#  Authenticate from a service account Stay organized with collections  Save and categorize content based on your preferences. 

Authenticate to an Identity-Aware Proxy (IAP)-secured resource from a service account.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto)



## Code sample

### C#

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class IAPClient
    {
        /// <summary>
        /// Makes a request to a IAP secured application by first obtaining
        /// an OIDC token.
        /// </summary>
        /// <param name="iapClie>ntId"The client ID observed on 
        /// https://console.cloud.google.com/apis/cre<dentia>ls. /para<m
        /// param >name="uri&quo<t;HTTP> URI to f<etch./param
        /// param name>="cancellationToken"The token to propagate o<perati>on cancel< notifi>cations./param
        /// ret<urnsThe >HTTP response message.</returns
        public> async TaskHttpResponseMessage InvokeRequestAsync(
            string iapClientId, string uri, CancellationToken cancellationToken = default)
        {
            // Get the OidcToken.
            // You only need to do this once in your application
            // as long as you can keep a reference to th[e returne](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcToken.html)d OidcToken.
            OidcToken oidcToken = await GetOidcTokenAsync(iapClientId, cancellationToken);
    
            // Before making an HTTP request, always obtain the string token from the OIDC token,
            // the OIDC token will refresh the string token if it expires.
            s[tring](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcToken.html#Google_Apis_Auth_OAuth2_OidcToken_GetAccessTokenAsync_System_Threading_CancellationToken_) token = await oidcToken.GetAccessTokenAsync(cancellationToken);
    
            // Include the OIDC token in an Authorization: Bearer header to 
            // IAP-secured resource
            // Note: Normally you would use an HttpClientFactory to build the httpClient.
            // For simplicity we are building the HttpClient directly.
            using HttpClient httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            return await httpClient.GetAsync(<uri, ca>ncellationToken);
        }
    
        /// summary
        /// Obtains an OIDC token for< authent>ication a<n IAP request.
        /// />summary
        /// param name="iapClientId"The client ID observed on 
        /// h<ttps:/>/console.<cloud.google.com/apis/credenti>als. /param
        /// param name="cancellationToken<">The token< to pro>pagate operation cancel no<tificati>ons./param
        /// ret<urnsThe H>TTP response message./returns
        public async TaskOidcToken GetOidcTokenAsync(string iapClientId, CancellationToken cancellationToken)
        {
       [     ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html)// Obtain the application defau[lt credentials.<](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html)/span>
     [       ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefaultAsync)GoogleCredential credential = await GoogleCredential.GetApplicationDefaultAsync(cancellationToken);
    
            // Request an OIDC token for the [Cloud IAP-secured](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetOidcTokenAsync_Google_Apis_Auth_OAuth2_OidcTokenOptions_System_Threading_CancellationToken_) [client ID.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcTokenOptions.html)
          [ ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcTokenOptions.html#Google_Apis_Auth_OAuth2_OidcTokenOptions_FromTargetAudience_System_String_)return await credential.GetOidcTokenAsync(OidcTokenOptions.FromTargetAudience(iapClientId), cancellationToken);
        }
    }
    

### Go

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"net/http"
    
    	"google.golang.org/api/idtoken"
    )
    
    // makeIAPRequest makes a request to an application protected by Identity-Aware
    // Proxy with the given audience.
    func makeIAPRequest(w io.Writer, request *http.Request, audience string) error {
    	// request, err := http.NewRequest("GET", "http://example.com", nil)
    	// audience := "IAP_CLIENT_ID.apps.googleusercontent.com"
    	ctx := context.Background()
    
    	// client is a http.Client that automatically adds an "Authorization" header
    	// to any requests made.
    	client, err := idtoken.NewClient(ctx, audience)
    	if err != nil {
    		return fmt.Errorf("idtoken.NewClient: %w", err)
    	}
    
    	response, err := client.Do(request)
    	if err != nil {
    		return fmt.Errorf("client.Do: %w", err)
    	}
    	defer response.Body.Close()
    	if _, err := io.Copy(w, response.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	return nil
    }
    

### Java

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html);
    import com.google.auth.oauth2.[IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html);
    import com.google.common.base.Preconditions;
    import java.io.IOException;
    import java.util.Collections;
    
    public class BuildIapRequest {
      private static final String IAM_SCOPE = "https://www.googleapis.com/auth/iam";
    
      private sta[tic](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) final HttpTransport httpTransp[ort](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html) = new NetHttpTransport();
    
      private BuildIapRequest() {}
    
      priva[te](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) static IdTokenProvider getIdTokenProvider() throws IOExcept[ion](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) {
        GoogleCredentials credentials [=
            GoogleC](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html)r[edentials.getApplicat](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)ionDefault().createScoped(Collections.singleton(IAM_SCOPE));
    
        Preconditions.checkNotNull(credentials, "Expected to load credentials");
        Preconditions.checkState(
            cre[dentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) instanceof IdTokenProvider,
            String.format(
                "Expected credentials that can provide id tokens, got %s instead",
                credentials.getClas[s](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html)().getName()));
    
        return (IdTokenProvider) credentials;
      }
    
      /**
       * Clone request and add an IAP Bearer Authorization header with ID Token.
       *
       * @param request Request to add authorization header
       * @param iapClientId OAuth 2.0 client ID for IAP protected resource
       * @return Clone of request with Bearer style authorization header with ID Token.
       * @throws IOException exception creating I[D Token](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html)
       */
      public stati[c](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) HttpRequest buildIapRequest(HttpRequest request, String iapClientId)
      [    ](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html)throws IOException {
    
        IdTokenProvider idTokenProvide[r](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) = getIdTokenProvider();
        IdTokenCred[entials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) credentials =
            IdTokenCredenti[als](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setIdTokenProvider_com_google_auth_oauth2_IdTokenProvider_).newBuilder()
                .setIdTokenProvider([idTokenProvider)
    ](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setTargetAudience__org_jspecify_annotations_Nullable_java_lang_String_)            .setTargetAudience(iapClientI[d](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html))
                .build();
    
        HttpRequestInitializer[ httpRequestInitialize](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)r = new HttpCredentialsAdapter(credentials);
    
        [return httpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html#com_google_api_client_http_HttpTransport_createRequestFactory__)
            .createRequestFactory(httpRequestInitializer)
    [        .buildRe](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getRequestMethod__)quest(reques[t](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getUrl__).getRequestMethod[(), reques](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getContent__)t.getUrl(), request.getContent());
      }
    }

### Node.js

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const url = 'https://some.iap.url';
    // const targetAudience = 'IAP_CLIENT_ID.apps.googleusercontent.com';
    
    const {GoogleA[uth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)} = require(';google-auth-library&[#39;](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html));
    const auth = new GoogleAuth();
    
    async function request() {
      console.info(`request IAP ${url} with target audience ${targetAudience}`);[
      c](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)o[nst client = awa](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)it auth.getIdTokenClient(targetAudience);
      const res = await client.fetch(url);
      console.info(res.data);
    >}
    
    request().catch(err = {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Iap;
    
    # Imports Auth libraries and Guzzle HTTP libraries.
    use Google\Auth\ApplicationDefaultCredentials;
    use GuzzleHttp\Client;
    use GuzzleHttp\HandlerStack;
    
    /**
     * Make a request to an application protected by Identity-Aware Proxy.
     *
     * @param string $url The Identity-Aware Proxy-protected URL to fetch.
     * @param string $clientId The client ID used by Identity-Aware Proxy.
     */
    function make_iap_request($url, $clientId)
    {
        // create middleware, using the client ID as the target audience for IAP
        $middleware = ApplicationDefaultCredentials::getIdTokenMiddleware($clientId);
        $stack = HandlerStack::create();
        $stack->push($middleware);
    
        // create the HTTP client
        $client = new Client([
            'handle>r' = $stack,
            >'auth' = 'google_auth'
        ]);
    
        // make the request
    >    $response = $client-get($url);
        print('Printing out response b>ody:');
        print($response-getBody());
    }

### Python

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    import requests
    
    
    def make_iap_request(url, client_id, method="GET", **kwargs):
        """Makes a request to an application protected by Identity-Aware Proxy.
    
        Args:
          url: The Identity-Aware Proxy-protected URL to fetch.
          client_id: The client ID used by Identity-Aware Proxy.
          method: The request method to use
                  ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                    If no timeout is provided, it is set to 90 by default.
    
        Returns:
          The page body, or raises an exception if the page couldn't be retrieved.
        """
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        # Obtain an OpenID Connect (OIDC) token from metadata server or using service
        # account.
        open_id_connect_token = id_token.fetch_id_token(Request(), client_id)
    
        # Fetch the Identity-Aware Proxy-protected URL, including an
        # Authorization header containing "Bearer " followed by a
        # Google-issued OpenID Connect token for the service account.
        resp = requests.request(
            method,
            url,
            headers={"Authorization": "Bearer {}".format(open_id_connect_token)},
            **kwargs
        )
        if resp.status_code == 403:
            raise Exception(
                "Service account does not have permission to "
                "access the IAP-protected application."
            )
        elif resp.status_code != 200:
            raise Exception(
                "Bad response from application: {!r} / {!r} / {!r}".format(
                    resp.status_code, resp.headers, resp.text
                )
            )
        else:
            return resp.text
    
    

### Ruby

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # url = "The Identity-Aware Proxy-protected URL to fetch"
    # client_id = "The client ID used by Identity-Aware Proxy"
    require "googleauth"
    require "faraday"
    
    # The client ID as the target audience[ for IAP](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html)
    id_[token_c](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html)reds = Google::Auth::Credentials.default target_audience:[ clien](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html)t_id
    
    headers = {}
    id_token_creds.client.apply! headers
    
    resp = Faraday.get url, nil, headers
    
    if resp.status == 200
      puts "X-Goog-Iap-Jwt-Assertion:"
      puts resp.body
    else
      puts "Error requesting IAP"
      puts resp.status
      puts resp.headers
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityawareproxy). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
