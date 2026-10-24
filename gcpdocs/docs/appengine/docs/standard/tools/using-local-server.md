---
url: https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server/
title: Using the local development server \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T09:47:46.797483+00:00
---

# Using the local development server  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using the local development server Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

**Note:** You can't use the latest version of `dev_appserver.py` to locally run your applications for runtimes that reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule).

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) includes a local development server (`dev_appserver.py`). You can use the local development server to simulate running your App Engine application in production as well as use it to access App Engine legacy bundled services. The simulated environment enforces some sandbox restrictions, such as restricted system functions and runtime language module imports, but not others, like request timeouts or quotas.

The local development server also simulates the services provided by the libraries in the SDK for App Engine, including Datastore, Memcache, and Task Queues, by performing their tasks locally. When your application is running in the development server, you can still make remote API calls to the production infrastructure by using the Google API HTTP endpoints.

## Set up the local development server

**Note:** The `dev_appserver` tool does not support development of Python 3 apps on Windows.

To run the local development server tool, you must set up the following:

  1. Verify that you have installed a Python 3 interpreter that is [compatible with the Python version required by the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup).
  2. Verify that you have installed the Google Cloud CLI component that includes the App Engine extension for Python 3 (`app-engine-python`):
         
         gcloud components list
         

If the `app-engine-python` component is not installed, run the following command:
         
         gcloud components install app-engine-python
         

  3. Locate the installation path of Google Cloud SDK by running the following command:
         
         gcloud info
         

The command returns the root directory where you installed Google Cloud SDK, for example:

`Installation Root: [/Users/myname/google-cloud-sdk]`

  4. Locate the `dev_appserver.py` tool under the `/bin/` folder where you installed Google Cloud CLI, for example:
         
         CLOUD_SDK_ROOT/bin/dev_appserver.py
         

  5. Note the path to the `dev_appserver.py` for later.




## Run the local development server

After setting up the local development server and creating the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) configuration file for your app, you can use the `dev_appserver.py` command to run your app locally.

To start the local development server:

  1. In the directory that contains your `app.yaml` configuration file, run the `dev_appserver.py` command. 

Specify the directory path to your app, for example:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py [PATH_TO_YOUR_APP]
         

Alternatively, you can specify the configuration file of a specific service, for example:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py app.yaml
         

To change the port, you include the `--port` option:
         
         python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --port=9999 [PATH_TO_YOUR_APP]
         

  2. The local development server is now running and listening for requests. You can visit <http://localhost:8080/> in your web browser to see the app in action. 

If you specified a custom port with the `--port` option, remember to open your browser to that port.




To stop the local server from the command line, press the following:

  * macOS or Linux: `Control+C`
  * Windows: `Control+Break`



## Specify application IDs

To access your App ID in the local server, for example to spoof an email address, use the [`get_application_id()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/get_application_id) function.

To get the hostname of the running app, use the [`get_default_version_hostname()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/app_identity/get_default_version_hostname) function.

## Detect application runtime environment

To determine whether your code is running in production or in the local development server, you can check the value of the `GAE_ENV` environment variable:
    
    
    if os.getenv('GAE_ENV', '').startswith('standard'):
      # Production in the standard environment
    else:
      # Local development server
    

## Use the Mail service

The local development server can send email for calls to the App Engine mail service using either an SMTP server or a local installation of [Sendmail](http://www.sendmail.org/).

### Using SMTP

To enable mail support with an SMTP server, invoke `dev_appserver.py` as follows::
    
    
    python3 [CLOUD_SDK_ROOT]/bin/dev_appserver.py --smtp_host=smtp.example.com --smtp_port=25 \
        --smtp_user=ajohnson --smtp_password=k1tt3ns [PATH_TO_YOUR_APP]
    

where you set the `--smtp_host`, `--smtp_port`, `--smtp_user` and `--smtp_password` options with your own values.

### Using Sendmail

To enable mail support with Sendmail, invoke `dev_appserver.py` as follows:
    
    
    python3 [CLOUD_SDK_ROOT]/bin/dev_appserver.py --enable_sendmail=yes [PATH_TO_YOUR_APP]
    

The local server uses the `sendmail` command to send email messages with your installation's default configuration.

**Note:** If you don't invoke `dev_appserver.py` with either SMTP or Sendmail as described, then attempts to send email from your application will do nothing, but the attempt will appear successful in your application.

## Use the URL Fetch service

When your application uses the URL fetch API to make an HTTP request, the local development server makes the request directly from your computer. The URL Fetch behavior on the local server may differ from production App Engine if you use a proxy server for accessing websites.

## Use the Users service

App Engine provides a [Users service](https://docs.cloud.google.com/appengine/docs/standard/users) to simplify authentication and authorization for your application. The local development server [simulates the behavior of Google Accounts](https://docs.cloud.google.com/appengine/docs/standard/users#Google_accounts_and_the_development_server) with its own sign-in and sign-out pages.

While running under the local development server, the functions return URLs for `/_ah/login` and `/_ah/logout` on the local server.

## Command-line arguments

For the local development server command options, see [Local development server options](https://docs.cloud.google.com/appengine/docs/standard/tools/local-devserver-command).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
