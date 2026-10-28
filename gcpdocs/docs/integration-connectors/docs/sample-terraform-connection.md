---
url: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/
title: Sample terraform template for connection creation \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:54:14.157849+00:00
---

# Sample terraform template for connection creation  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/

[ Skip to main content ](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/)
  * [Deutsch](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=de)
  * [Español](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=es-419)
  * [Français](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=id)
  * [Italiano](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=it)
  * [Português](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=ja)
  * [한국어](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-connection/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fintegration-connectors%2Fdocs%2Fsample-terraform-connection%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/devops-color.svg) ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)


Was this helpful?
Send feedback 
# Sample terraform template for connection creation Stay organized with collections  Save and categorize content based on your preferences.
The following is a sample terraform template for connection creation.
[](https://shell.cloud.google.com/cloudshell/editor?show=ide&cloudshell_git_repo=https://github.com/terraform-google-modules/terraform-docs-samples&cloudshell_open_in_editor=integrationconnectors/advanced/main.tf)[](https://github.com/terraform-google-modules/terraform-docs-samples/blob/HEAD/integrationconnectors/advanced/main.tf)

```
resource "google_integration_connectors_connection" "testconnection" {
  name              = "test-connection"
  description       = "tf updated description"
  location          = "us-central1"
  service_account   = "${data.google_project.default.number}-compute@developer.gserviceaccount.com"
  connector_version = "projects/${data.google_project.default.project_id}/locations/global/providers/zendesk/connectors/zendesk/versions/1"
  // These show all the different types of config variables, not necessary that each resource will use everything.
  config_variable {
    key           = "proxy_enabled"
    boolean_value = false
  }
  config_variable {
    key           = "sample_integer_value"
    integer_value = 1
  }

  config_variable {
    key = "sample_encryption_key_value"
    encryption_key_value {
      type         = "GOOGLE_MANAGED"
      kms_key_name = "sampleKMSKkey"
    }
  }

  config_variable {
    key = "sample_secret_value"
    secret_value {
      secret_version = google_secret_manager_secret_version.default.name
    }
  }

  suspended = false
  auth_config {
    // These show all the different types of additional variables, not necessary that each resource will use everything.
    additional_variable {
      key          = "sample_string"
      string_value = "sampleString"
    }
    additional_variable {
      key           = "sample_boolean"
      boolean_value = false
    }
    additional_variable {
      key           = "sample_integer"
      integer_value = 1
    }
    additional_variable {
      key = "sample_secret_value"
      secret_value {
        secret_version = google_secret_manager_secret_version.default.name
      }
    }
    additional_variable {
      key = "sample_encryption_key_value"
      encryption_key_value {
        type         = "GOOGLE_MANAGED"
        kms_key_name = "sampleKMSKkey"
      }
    }
    auth_type = "USER_PASSWORD"
    auth_key  = "sampleAuthKey"
    user_password {
      username = "user@xyz.com"
      password {
        secret_version = google_secret_manager_secret_version.default.name
      }
    }
  }

  destination_config {
    key = "url"
    destination {
      host = "https://test.zendesk.com"
      port = 80
    }
  }
  lock_config {
    locked = false
    reason = "Its not locked"
  }
  log_config {
    enabled = true
  }
  node_config {
    min_node_count = 2
    max_node_count = 50
  }
  labels = {
    foo = "bar"
  }
  ssl_config {
    // These show all the different types of additional variables, not necessary that each resource will use everything.
    additional_variable {
      key          = "sample_string"
      string_value = "sampleString"
    }
    additional_variable {
      key           = "sample_boolean"
      boolean_value = false
    }
    additional_variable {
      key           = "sample_integer"
      integer_value = 1
    }
    additional_variable {
      key = "sample_secret_value"
      secret_value {
        secret_version = google_secret_manager_secret_version.default.name
      }
    }
    additional_variable {
      key = "sample_encryption_key_value"
      encryption_key_value {
        type         = "GOOGLE_MANAGED"
        kms_key_name = "sampleKMSKkey"
      }
    }
    client_cert_type = "PEM"
    client_certificate {
      secret_version = google_secret_manager_secret_version.default.name
    }
    client_private_key {
      secret_version = google_secret_manager_secret_version.default.name
    }
    client_private_key_pass {
      secret_version = google_secret_manager_secret_version.default.name
    }
    private_server_certificate {
      secret_version = google_secret_manager_secret_version.default.name
    }
    server_cert_type = "PEM"
    trust_model      = "PRIVATE"
    type             = "TLS"
    use_ssl          = true
  }

  eventing_enablement_type = "EVENTING_AND_CONNECTION"
  eventing_config {
    // These show all the different types of additional variables, not necessary that each resource will use everything.
    additional_variable {
      key          = "sample_string"
      string_value = "sampleString"
    }
    additional_variable {
      key           = "sample_boolean"
      boolean_value = false
    }
    additional_variable {
      key           = "sample_integer"
      integer_value = 1
    }
    additional_variable {
      key = "sample_secret_value"
      secret_value {
        secret_version = google_secret_manager_secret_version.default.name
      }
    }
    additional_variable {
      key = "sample_encryption_key_value"
      encryption_key_value {
        type         = "GOOGLE_MANAGED"
        kms_key_name = "sampleKMSKkey"
      }
    }
    registration_destination_config {
      key = "registration_destination_config"
      destination {
        host = "https://test.zendesk.com"
        port = 80
      }
    }
    auth_config {
      auth_type = "USER_PASSWORD"
      auth_key  = "sampleAuthKey"
      user_password {
        username = "user@xyz.com"
        password {
          secret_version = google_secret_manager_secret_version.default.name
        }
      }
      // These show all the different types of additional variables, not necessary that each resource will use everything.
      additional_variable {
        key          = "sample_string"
        string_value = "sampleString"
      }
      additional_variable {
        key           = "sample_boolean"
        boolean_value = false
      }
      additional_variable {
        key           = "sample_integer"
        integer_value = 1
      }
      additional_variable {
        key = "sample_secret_value"
        secret_value {
          secret_version = google_secret_manager_secret_version.default.name
        }
      }
      additional_variable {
        key = "sample_encryption_key_value"
        encryption_key_value {
          type         = "GOOGLE_MANAGED"
          kms_key_name = "sampleKMSKkey"
        }
      }
    }
    enrichment_enabled = true
  }
  depends_on = [google_secret_manager_secret_iam_member.default]
}
```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 
