---
url: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/terraform-examples/
title: Terraform configuration examples \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.224833+00:00
---

# Terraform configuration examples · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/detections/ai-security-for-apps/terraform-examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

[Traffic detections](https://developers.cloudflare.com/waf/detections/)

  4. /[AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/)
  5. /Terraform examples



# Terraform configuration examples

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable AI Security for AppsDefine custom topicsAdd custom rules to block harmful promptsMore resources

The following Terraform configuration examples address common scenarios for managing, configuring, and using AI Security for Apps.

For more information, refer to the [Terraform Cloudflare provider documentation ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs).

If you are using the Cloudflare API, refer to [Get started](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/).

## Enable AI Security for Apps

Use the [`cloudflare_ai_security` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ai_security) resource to turn on AI Security for Apps for a zone. This resource requires Terraform Cloudflare provider version 5.29.0 or later. For example:
    
    
    resource "cloudflare_ai_security" "zone_ai_security" {
      zone_id = var.cloudflare_zone_id
      enabled = true
    }

AI Security for Apps only scans requests to endpoints with the `cf-llm` label. For more information, refer to [Add `cf-llm` label to endpoint](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/#3-add-cf-llm-label-to-endpoint).

## Define custom topics

Use the [`cloudflare_ai_security_custom_topics` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ai_security_custom_topics) resource to define the custom topics for a zone. This resource requires Terraform Cloudflare provider version 5.29.0 or later. For example:
    
    
    resource "cloudflare_ai_security_custom_topics" "zone_custom_topics" {
      zone_id = var.cloudflare_zone_id
    
      topics = [
        {
          label = "competitors"
          topic = "seeking info on competitors"
        },
        {
          label = "financial-advice"
          topic = "seeking financial advice"
        },
        {
          label = "job-seeking"
          topic = "asking for résumé advice"
        }
      ]
    }

Caution

This resource manages the entire custom topics list for the zone. When you apply the configuration, Terraform replaces any topics added outside Terraform, such as in the dashboard.

For more information, refer to [Custom topics](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics).

## Add custom rules to block harmful prompts

This example adds two [custom rules](https://developers.cloudflare.com/waf/custom-rules/) that use [AI Security for Apps fields](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/) in their expressions:

  * The first rule blocks requests where Cloudflare detected personally identifiable information (PII) in the LLM prompt, using the [`cf.llm.prompt.pii_detected`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.pii_detected/) field. The rule returns a custom JSON response.
  * The second rule blocks requests where the LLM prompt is highly relevant to the `competitors` custom topic, using the [`cf.llm.prompt.custom_topic_categories`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.custom_topic_categories/) field. The label in the expression must match a label in your custom topics list.



To use these fields you must enable AI Security for Apps.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `Zone WAF Write`



Configure the [`cloudflare_ruleset` ↗︎](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset) resource:
    
    
    resource "cloudflare_ruleset" "zone_custom_firewall_ai_security" {
      zone_id     = var.cloudflare_zone_id
      name        = "Phase entry point ruleset for custom rules in my zone"
      description = ""
      kind        = "zone"
      phase       = "http_request_firewall_custom"
    
      rules = [
        {
          ref         = "block_llm_prompts_with_pii"
          description = "Block LLM prompts containing PII"
          expression  = "(cf.llm.prompt.pii_detected)"
          action      = "block"
          action_parameters = {
            response = {
              status_code  = 403
              content      = "{\"error\": \"Your request was blocked. Please rephrase your request.\"}"
              content_type = "application/json"
            }
          }
        },
        {
          ref         = "block_llm_prompts_about_competitors"
          description = "Block LLM prompts about competitors"
          expression  = "(cf.llm.prompt.custom_topic_categories[\"competitors\"] lt 20)"
          action      = "block"
        }
      ]
    }

A zone has a single entry point ruleset for custom rules. If you already manage this ruleset with Terraform, add the rules to the existing `cloudflare_ruleset` resource instead of creating a new one.

For more rule examples, refer to [Example mitigation rules](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/).

## More resources

For additional Terraform configuration examples, refer to [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/).

[PreviousAvailable fields](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/)[NextOverview](https://developers.cloudflare.com/waf/detections/threat-intelligence/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/detections/ai-security-for-apps/terraform-examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
