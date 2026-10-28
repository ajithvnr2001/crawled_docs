---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/
title: Configure email notifications \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:10.589073+00:00
---

# Configure email notifications  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Fpipelines%2Femail-notifications%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#before_you_begin)
  * [Send a notification from a pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#sending-notification-from-pipeline)
  * [Example of a notification email](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#example_of_a_notification_email)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)


Was this helpful?
Send feedback 
#  Configure email notifications Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#before_you_begin)
  * [Send a notification from a pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#sending-notification-from-pipeline)
  * [Example of a notification email](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#example_of_a_notification_email)


Gemini Enterprise Agent Platform Pipelines can notify you of the success or failure of a pipeline run. When the pipeline exits, Google Cloud sends a final status notification email to the email addresses that you specify.
This guide shows how to configure email notifications from a pipeline by using the [Email notification component](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notification-component) in the Google Cloud SDK.
## Before you begin
Before you build a pipeline that sends notifications, use the following instructions to set up your Google Cloud project and development environment.
  1. To get your Google Cloud project ready to run ML pipelines, follow the instructions in the guide to [configuring your Google Cloud project](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project).
  2. Install v2 or later of the Kubeflow Pipelines SDK.

```
pip install --upgrade "kfp>=2,<3"

```



  1. To use Gemini Enterprise Agent Platform Python client in your pipelines, [install the Gemini Enterprise Agent Platform client libraries v1.7 or later](https://github.com/googleapis/python-aiplatform).
  2. To use Gemini Enterprise Agent Platform services in your pipelines, [install the Google Cloud Pipeline Components](https://github.com/kubeflow/pipelines/tree/master/components/google-cloud#installation).


## Send a notification from a pipeline
The following example shows how to configure email notifications by defining an email notification task (`notify_email_task`) and adding it to the pipeline's exit handler (`dsl.ExitHandler`). This notification task invokes the `VertexNotificationEmailOp` operator in the email notification component when the pipeline exits.

```
from kfp import dsl
from kfp import compiler
from google_cloud_pipeline_components.v1.vertex_notification_email import VertexNotificationEmailOp

@dsl.pipeline(
    name='PIPELINE_NAME',
    pipeline_root=PIPELINE_ROOT_PATH,
)
def TASK_NAME():
    notify_email_task = VertexNotificationEmailOp(recipients=RECIPIENTS_LIST)

    with dsl.ExitHandler(notify_email_task):
        # Add your pipeline tasks here.

compiler.Compiler().compile(pipeline_func=notification_email_pipeline,
        package_path='notification_email_pipeline.yaml')

```

Replace the following:
  * PIPELINE_NAME: The name of the pipeline.
  * PIPELINE_ROOT_PATH: Specify a Cloud Storage URI that your [pipelines service account can access](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-project#service-account). The artifacts of your pipeline runs are stored within the pipeline root.
The pipeline root can be set as an argument of the `@kfp.dsl.pipeline` annotation on the pipeline function, or it can be set when you call `create_run_from_job_spec` to create a pipeline run.
  * TASK_NAME: The name of the pipeline task for which you're configuring email notifications.
  * RECIPIENTS_LIST: A comma-separated list of up to three email addresses to send the notification email to.


Add your pipeline tasks in the body of the `dsl.ExitHandler` exit handler function. By wrapping the tasks in the exit handler function in this way, you specify that the notification email component should report the status of these tasks when the pipeline exits. For example, if a task within the exit handler's contents fails, then the notification reports the status as failed.
## Example of a notification email
If you configure email notifications for a pipeline using the code sample in [Send a notification from a pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/email-notifications/#sending-notification-from-pipeline), Gemini Enterprise Agent Platform sends an email notification similar to the following when the pipeline exits:
> Subject: Vertex Pipelines job "PIPELINE_NAME" task "TASK_NAME"  
>  From: Google Notifications <notify-noreply@google.com>  
>    
>  Hello Agent Platform Customer,  
>    
>  Gemini Enterprise Agent Platform Pipelines job "PIPELINE_NAME" task "TASK_NAME" ended with the following state: {status}.  
>    
>  Additional details:  
>  - Project: {project}  
>  - Pipeline name: PIPELINE_NAME  
>  - Pipeline job ID: {pipeline_job_id}  
>  - Start time: {start_time}  
>    
>  To view this pipeline job in Cloud Console, use the following link: {console_link}  
>    
>  Sincerely,  
>  The Google Cloud AI Team  
> 
In this example:
  * `{status}` represents the final state of the task, which can be `SUCCEEDED`, `FAILED`, or `CANCELLED`.
  * `{project}` is the project name.
  * `{pipeline_job_id}` is the unique pipeline job ID.
  * `{start_time}` represents the start time for the pipeline.
  * `{console_link}` is a hyperlink to the pipeline job in the Google Cloud console.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
