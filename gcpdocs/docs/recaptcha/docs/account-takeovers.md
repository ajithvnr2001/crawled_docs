---
url: https://docs.cloud.google.com/recaptcha/docs/account-takeovers/
title: Detect and prevent account takeovers \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T09:52:38.417711+00:00
---

# Detect and prevent account takeovers  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/account-takeovers/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Detect and prevent account takeovers Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Fraud Defense lets you detect and prevent account takeovers (ATOs) across your websites and mobile applications. To help protect accounts against credential stuffing and automated takeovers, you can combine account-level behavioral analysis in Account defense with compromised-credential checks in Password defense and step-up multi-factor authentication (MFA).

ATO attacks, such as credential stuffing, typically occur when an attacker sends requests to sign in by using credentials exposed in data breaches and [password dumps](https://security.googleblog.com/2014/09/cleaning-up-after-password-dumps.html). Because users frequently reuse passwords across unrelated sites, automated stuffing attacks can succeed even against properly configured authentication endpoints unless you evaluate behavioral risk and leaked credentials.

## Before you begin

[Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

## Detect and prevent ATOs

With Fraud Defense, you can detect and prevent ATOs by using the following capabilities:

  * Account defense and the ATO risk score
  * Password defense for password leak detection
  * Score-based keys and step-up MFA



### Use Account defense and the ATO risk score

[Account defense](https://docs.cloud.google.com/recaptcha/docs/account-defender) is the primary capability for detecting and preventing ATOs across [websites](https://docs.cloud.google.com/recaptcha/docs/account-defender) and [mobile apps](https://docs.cloud.google.com/recaptcha/docs/account-defender-mobile).

Account defense provides a dedicated [ATO risk score](https://docs.cloud.google.com/recaptcha/docs/account-defender#account-takeover-risk-score) (`accountDefenderAssessment.accountTakeoverVerdict.risk`, ranging from `0.0` to `1.0`) and explainability signals (`riskReasons` and `trustReasons`). These signals evaluate account-level behavioral history alongside session signals, providing approximately four times higher ATO detection precision than bot scores alone.

To integrate Account defense, pass a stable account identifier in the `user_info.account_id` field (`event.userInfo.accountId` when you call [`CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create). If the account identifier is available only after authentication, pass `account_id` when you call [`AnnotateAssessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate).

### Detect leaked passwords

Because ATOs frequently rely on credential stuffing with credentials exposed in password dumps, use [Password defense](https://docs.cloud.google.com/recaptcha/docs/check-passwords) on sign-in, password-change, and password-reset flows to detect compromised credentials.

When you check credentials during an assessment, Password defense evaluates the canonicalized username and password hash prefix against known data breaches without exposing plaintext credentials to Google. When you call [`CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create), pass the username (`credentials.username`) hash prefix (`lookupHashPrefix`) and encrypted credentials hash (`encryptedUserCredentialsHash`) in `privatePasswordLeakVerification`. If the verdict (`leakedPasswordVerdict`) indicates compromised credentials, require a password reset or trigger a step-up MFA challenge.

### Use score-based keys and step-up MFA

When the ATO risk score (`accountDefenderAssessment.accountTakeoverVerdict.risk`) or bot score (`riskAnalysis.score`) indicates elevated risk, use score-based keys to trigger step-up authentication or multi-factor authentication (MFA) in your application as your enforcement mechanism. For example, prompt the user for an additional factor, require re-authentication, or trigger one-time password (OTP) verification.

To implement score-based keys and step-up MFA, complete the following steps:

  * Install score-based keys to collect session signals and detect automation in large-scale ATOs:

    * **Web:** Call `grecaptcha.enterprise.execute()` on your web pages. For more information, see [Install score-based keys on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).

    * **Mobile:** Call `execute()` in the mobile SDKs. For more information, see [Integrate Fraud Defense with Android apps](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps) or [Integrate Fraud Defense with iOS apps](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps).

  * When `accountTakeoverVerdict.risk` exceeds your risk threshold or `riskAnalysis.score` falls below your bot threshold, trigger step-up authentication or an MFA challenge in your identity provider to verify account ownership on sign-in or for sensitive actions. Triggering step-up challenges selectively on elevated-risk requests reduces friction for legitimate users.




The following example shows how to integrate score-based keys in a sign-in workflow:
    
    
    function submitForm() {
      grecaptcha.enterprise.ready(function() {
        grecaptcha.enterprise.execute(
          'reCAPTCHA_site_key', {action: 'account_login'}).then(function(token) {
           document.getElementById("token").value = token;
           document.getElementByID("loginForm").submit();
        });
      });
    }
    
    
    <form id="loginForm" action="?" method="POST">
      Username: <input type="text" name="username"/><br/>
      Password: <input type="password" name="password"/><br/>
      <input type="hidden" id="token" name="recaptcha_token"/>
      <button onclick="submitForm()">Login</button>
    </form>
    
    
    <script src="https://www.google.com/recaptcha/enterprise.js" async defer></script>

You can experiment with this code in JSFiddle by clicking the `<>` icon in the top-right corner of the code window.
    
    
    <html>
      <head>
        <title>Account Login - Score</title>
        <script src="https://www.google.com/recaptcha/enterprise.js"></script>
        <script>
        function submitForm() {
          grecaptcha.enterprise.ready(function() {
            grecaptcha.enterprise.execute(
              'reCAPTCHA_site_key', {action: 'account_login'}).then(function(token) {
               document.getElementById("token").value = token;
               document.getElementByID("loginForm").submit();
            });
          });
        }
        </script>
      </head>
      <body>
        <form id="loginForm" action="?" method="POST">
          Username: <input type="text" name="username"/><br/>
          Password: <input type="password" name="password"/><br/>
          <input type="hidden" id="token" name="recaptcha_token"/>
          <button onclick="submitForm()">Login</button>
        </form>
      </body>
    </html>

**Note:** Visual [checkbox challenges](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox) are a legacy, web-only baseline for low-risk sites. Checkbox challenges don't evaluate account-level takeover signals or compromised credentials, and aren't supported on mobile apps.

## What's next

  * To learn about other account protection features, see [User accounts protection features](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
