---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1
title: Package google.cloud.foodorderingaiagent.v1 \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:11.827817+00:00
---

# Package google.cloud.foodorderingaiagent.v1  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Package google.cloud.foodorderingaiagent.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[EvaluationRunService](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService)` (interface)
  * `[FoodOrderingService](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService)` (interface)
  * `[MenuService](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService)` (interface)
  * `[AgentAudio](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentAudio)` (message)
  * `[AgentEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentEvent)` (message)
  * `[AgentText](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentText)` (message)
  * `[AnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AnalyticsMetrics)` (message)
  * `[AppendIngestionPhaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AppendIngestionPhaseRequest)` (message)
  * `[AudioInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AudioInput)` (message)
  * `[AuditLogEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AuditLogEntry)` (message)
  * `[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability)` (message)
  * `[Availability.ChannelTypeAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.ChannelTypeAvailability)` (message)
  * `[Availability.DaypartAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.DaypartAvailability)` (message)
  * `[Availability.FulfillmentMethodAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.FulfillmentMethodAvailability)` (message)
  * `[Availability.MenuScheduleAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.MenuScheduleAvailability)` (message)
  * `[Availability.Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.Status)` (enum)
  * `[BatchCreateEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchCreateEvaluationCasesRequest)` (message)
  * `[BatchCreateEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchCreateEvaluationCasesResponse)` (message)
  * `[BatchDeleteStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchDeleteStoresRequest)` (message)
  * `[BatchGetMenuEntitiesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetMenuEntitiesRequest)` (message)
  * `[BatchGetMenuEntitiesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetMenuEntitiesResponse)` (message)
  * `[BatchGetStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetStoresRequest)` (message)
  * `[BatchGetStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetStoresResponse)` (message)
  * `[BatchUpdateEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateEvaluationCasesRequest)` (message)
  * `[BatchUpdateEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateEvaluationCasesResponse)` (message)
  * `[BatchUpdateStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateStoresRequest)` (message)
  * `[BatchUpdateStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateStoresResponse)` (message)
  * `[BidiProcessOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderRequest)` (message)
  * `[BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderResponse)` (message)
  * `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Blob)` (message)
  * `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` (message)
  * `[Brand.McpConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand.McpConfig)` (message)
  * `[BrandRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BrandRevision)` (message)
  * `[CelUpsell](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CelUpsell)` (message)
  * `[CelUpsell.SuggestedModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CelUpsell.SuggestedModifierGroup)` (message)
  * `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` (message)
  * `[ChannelConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.State)` (enum)
  * `[ChannelConfig.SupplementalInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.SupplementalInstructions)` (message)
  * `[ChannelConfig.TTSConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.TTSConfig)` (message)
  * `[ChannelConfig.TTSConfig.VoiceConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.TTSConfig.VoiceConfig)` (message)
  * `[ChannelConfig.Tone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.Tone)` (enum)
  * `[ChannelConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.Type)` (enum)
  * `[ChannelConfigRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfigRevision)` (message)
  * `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` (enum)
  * `[ChildSynonym](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChildSynonym)` (message)
  * `[ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientAppInfo)` (message)
  * `[ClientExecutionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientExecutionRequest)` (message)
  * `[ClientExecutionResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientExecutionResult)` (message)
  * `[ClosingOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClosingOffer)` (message)
  * `[ClosingOffer.ClosingMessage](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClosingOffer.ClosingMessage)` (message)
  * `[ClusteredEntityIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClusteredEntityIssue)` (message)
  * `[ComputeAnalyticsMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest)` (message)
  * `[ComputeAnalyticsMetricsRequest.AnalyticsType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest.AnalyticsType)` (enum)
  * `[ComputeAnalyticsMetricsRequest.FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest.FeatureGate)` (message)
  * `[ComputeAnalyticsMetricsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsResponse)` (message)
  * `[Config](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config)` (message)
  * `[Config.SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config.SessionMode)` (enum)
  * `[Config.TrafficType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config.TrafficType)` (enum)
  * `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` (message)
  * `[ConfigApplicationRuleRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRuleRevision)` (message)
  * `[ConfigRuleBinding](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigRuleBinding)` (message)
  * `[CreateBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateBrandRequest)` (message)
  * `[CreateChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateChannelConfigRequest)` (message)
  * `[CreateConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateConfigApplicationRuleRequest)` (message)
  * `[CreateDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateDiscountRequest)` (message)
  * `[CreateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationCaseRequest)` (message)
  * `[CreateEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationContextRequest)` (message)
  * `[CreateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationDatasetRequest)` (message)
  * `[CreateEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationMatcherRequest)` (message)
  * `[CreateIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateIngestionLogRequest)` (message)
  * `[CreateInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateInventoryRequest)` (message)
  * `[CreateMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateMenuRequest)` (message)
  * `[CreateRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateRemediationRequest)` (message)
  * `[CreateStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateStoreRequest)` (message)
  * `[CreateWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateWebhookSubscriptionRequest)` (message)
  * `[DateRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DateRange)` (message)
  * `[DeleteBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteBrandRequest)` (message)
  * `[DeleteBrandRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteBrandRevisionRequest)` (message)
  * `[DeleteChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteChannelConfigRequest)` (message)
  * `[DeleteChannelConfigRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteChannelConfigRevisionRequest)` (message)
  * `[DeleteConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteConfigApplicationRuleRequest)` (message)
  * `[DeleteConfigApplicationRuleRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteConfigApplicationRuleRevisionRequest)` (message)
  * `[DeleteDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteDiscountRequest)` (message)
  * `[DeleteEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationCaseRequest)` (message)
  * `[DeleteEvaluationCaseResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationCaseResultRequest)` (message)
  * `[DeleteEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationContextRequest)` (message)
  * `[DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationDatasetRequest)` (message)
  * `[DeleteEvaluationDatasetResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationDatasetResultRequest)` (message)
  * `[DeleteEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationMatcherRequest)` (message)
  * `[DeleteIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteIngestionLogRequest)` (message)
  * `[DeleteInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteInventoryRequest)` (message)
  * `[DeleteMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteMenuRequest)` (message)
  * `[DeleteRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteRemediationRequest)` (message)
  * `[DeleteSessionRecordRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteSessionRecordRequest)` (message)
  * `[DeleteStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteStoreRequest)` (message)
  * `[DeleteStoreRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteStoreRevisionRequest)` (message)
  * `[DeleteWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteWebhookSubscriptionRequest)` (message)
  * `[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress)` (message)
  * `[DeliveryAddress.ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress.ValidationStatus)` (enum)
  * `[DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiagnosticInfo)` (message)
  * `[DisambiguationMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationMapping)` (message)
  * `[DisambiguationMapping.Type](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationMapping.Type)` (enum)
  * `[DisambiguationStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationStrategy)` (message)
  * `[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)` (message)
  * `[Discount.Constraint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount.Constraint)` (message)
  * `[Discount.Scope](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount.Scope)` (enum)
  * `[DiscountIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiscountIntegrationAttributes)` (message)
  * `[DiscountType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiscountType)` (enum)
  * `[DtmfInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DtmfInput)` (message)
  * `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EndSession)` (message)
  * `[EndSession.EndType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EndSession.EndType)` (enum)
  * `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` (message)
  * `[EvaluationCase.DynamicTextTurnCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.DynamicTextTurnCase)` (message)
  * `[EvaluationCase.StaticTextTurnCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.StaticTextTurnCase)` (message)
  * `[EvaluationCase.StaticTextTurnCase.TextTurn](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.StaticTextTurnCase.TextTurn)` (message)
  * `[EvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult)` (message)
  * `[EvaluationCaseResult.Hyperlink](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.Hyperlink)` (message)
  * `[EvaluationCaseResult.MatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult)` (message)
  * `[EvaluationCaseResult.MatcherResult.AgentUtteranceStringMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.AgentUtteranceStringMatcherResult)` (message)
  * `[EvaluationCaseResult.MatcherResult.LLMJudgementMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.LLMJudgementMatcherResult)` (message)
  * `[EvaluationCaseResult.MatcherResult.OrderResultMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.OrderResultMatcherResult)` (message)
  * `[EvaluationCaseResult.Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.Status)` (enum)
  * `[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)` (message)
  * `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)` (message)
  * `[EvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDatasetResult)` (message)
  * `[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)` (message)
  * `[EvaluationMatcher.AgentUtteranceStringMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.AgentUtteranceStringMatcher)` (message)
  * `[EvaluationMatcher.LLMJudgementMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.LLMJudgementMatcher)` (message)
  * `[EvaluationMatcher.OrderResultMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.OrderResultMatcher)` (message)
  * `[EventInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput)` (message)
  * `[EventInput.CallerHangupEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.CallerHangupEvent)` (message)
  * `[EventInput.ClientEscalationEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.ClientEscalationEvent)` (message)
  * `[EventInput.CrewInterjectionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.CrewInterjectionEvent)` (message)
  * `[EventInput.DriveOffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.DriveOffEvent)` (message)
  * `[EventInput.EndSessionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.EndSessionEvent)` (message)
  * `[EventInput.EndSessionEvent.Reason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.EndSessionEvent.Reason)` (enum)
  * `[EventInput.OrderStateUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.OrderStateUpdateEvent)` (message)
  * `[EventInput.PosErrorEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.PosErrorEvent)` (message)
  * `[EventInput.StoreChangeEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.StoreChangeEvent)` (message)
  * `[ExperimentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ExperimentMetadata)` (message)
  * `[ExperimentMetadata.ExperimentStudy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ExperimentMetadata.ExperimentStudy)` (message)
  * `[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeatureGate)` (message)
  * `[FeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig)` (message)
  * `[FeaturesConfig.NameCollection](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.NameCollection)` (message)
  * `[FeaturesConfig.OrderDineIn](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.OrderDineIn)` (message)
  * `[FeaturesConfig.OrderPickup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.OrderPickup)` (message)
  * `[FetchServiceHealthRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthRequest)` (message)
  * `[FetchServiceHealthRequest.Granularity](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthRequest.Granularity)` (enum)
  * `[FetchServiceHealthResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse)` (message)
  * `[FetchServiceHealthResponse.MetricHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse.MetricHealth)` (message)
  * `[FetchServiceHealthResponse.MetricHealth.HistoryPoint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse.MetricHealth.HistoryPoint)` (message)
  * `[FinalizeOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FinalizeOrderRequest)` (message)
  * `[FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FinalizeOrderResponse)` (message)
  * `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` (enum)
  * `[GetBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetBrandRequest)` (message)
  * `[GetBrandRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetBrandRevisionRequest)` (message)
  * `[GetChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetChannelConfigRequest)` (message)
  * `[GetChannelConfigRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetChannelConfigRevisionRequest)` (message)
  * `[GetConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetConfigApplicationRuleRequest)` (message)
  * `[GetConfigApplicationRuleRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetConfigApplicationRuleRevisionRequest)` (message)
  * `[GetDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetDiscountRequest)` (message)
  * `[GetEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationCaseRequest)` (message)
  * `[GetEvaluationCaseResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationCaseResultRequest)` (message)
  * `[GetEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationContextRequest)` (message)
  * `[GetEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationDatasetRequest)` (message)
  * `[GetEvaluationDatasetResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationDatasetResultRequest)` (message)
  * `[GetEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationMatcherRequest)` (message)
  * `[GetIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetIngestionLogRequest)` (message)
  * `[GetInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetInventoryRequest)` (message)
  * `[GetMenuIssueClusterRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuIssueClusterRequest)` (message)
  * `[GetMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuIssueRequest)` (message)
  * `[GetMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuRequest)` (message)
  * `[GetRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetRemediationRequest)` (message)
  * `[GetSessionRecordRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetSessionRecordRequest)` (message)
  * `[GetStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetStoreRequest)` (message)
  * `[GetStoreRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetStoreRevisionRequest)` (message)
  * `[GetWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetWebhookSubscriptionRequest)` (message)
  * `[GreetingOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GreetingOffer)` (message)
  * `[Greetings](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Greetings)` (message)
  * `[HistoryEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.HistoryEntry)` (message)
  * `[IgnoreMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IgnoreMenuIssueRequest)` (message)
  * `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` (message)
  * `[Image.ImageSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image.ImageSource)` (message)
  * `[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)` (message)
  * `[IngestionLog.IngestionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog.IngestionType)` (enum)
  * `[IngestionLog.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog.State)` (enum)
  * `[IngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase)` (message)
  * `[IngestionPhase.Phase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase.Phase)` (enum)
  * `[IngestionPhase.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase.State)` (enum)
  * `[Interaction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction)` (message)
  * `[Interaction.AgentUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.AgentUtterance)` (message)
  * `[Interaction.ClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecution)` (message)
  * `[Interaction.ClientExecutionInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecutionInput)` (message)
  * `[Interaction.ClientExecutionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecutionOutput)` (message)
  * `[Interaction.ClientOrderUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientOrderUpdate)` (message)
  * `[Interaction.MatchIntent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntent)` (message)
  * `[Interaction.MatchIntentInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntentInput)` (message)
  * `[Interaction.MatchIntentOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntentOutput)` (message)
  * `[Interaction.ResolveOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrder)` (message)
  * `[Interaction.ResolveOrderInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrderInput)` (message)
  * `[Interaction.ResolveOrderOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrderOutput)` (message)
  * `[Interaction.SubmitOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.SubmitOrder)` (message)
  * `[Interaction.UserUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.UserUtterance)` (message)
  * `[InteractionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.InteractionMode)` (enum)
  * `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.InterruptionSignal)` (message)
  * `[IntervalMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics)` (message)
  * `[IntervalMetrics.ChannelMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.ChannelMetrics)` (message)
  * `[IntervalMetrics.OutcomeGroupCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.OutcomeGroupCount)` (message)
  * `[IntervalMetrics.PredictedFailureCategoryCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.PredictedFailureCategoryCount)` (message)
  * `[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)` (message)
  * `[Inventory.Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory.Status)` (enum)
  * `[Item](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Item)` (message)
  * `[ItemGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup)` (message)
  * `[ItemGroup.AllOf](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.AllOf)` (message)
  * `[ItemGroup.AnyOf](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.AnyOf)` (message)
  * `[ItemGroup.SelectItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.SelectItems)` (message)
  * `[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes)` (message)
  * `[ItemIntegrationAttributes.StreamIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.StreamIntegrationAttributes)` (message) **(deprecated)**
  * `[ItemIntegrationAttributes.StreamIntegrationAttributes.Tax](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.StreamIntegrationAttributes.Tax)` (message)
  * `[ItemIntegrationAttributes.ToastIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.ToastIntegrationAttributes)` (message)
  * `[ItemMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemMatcher)` (message)
  * `[ItemMatcher.ModifierMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemMatcher.ModifierMatcher)` (message)
  * `[ListBrandHistoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandHistoryRequest)` (message)
  * `[ListBrandHistoryResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandHistoryResponse)` (message)
  * `[ListBrandRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandRevisionsRequest)` (message)
  * `[ListBrandRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandRevisionsResponse)` (message)
  * `[ListBrandsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandsRequest)` (message)
  * `[ListBrandsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandsResponse)` (message)
  * `[ListChannelConfigRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigRevisionsRequest)` (message)
  * `[ListChannelConfigRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigRevisionsResponse)` (message)
  * `[ListChannelConfigsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigsRequest)` (message)
  * `[ListChannelConfigsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigsResponse)` (message)
  * `[ListConfigApplicationRuleRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRuleRevisionsRequest)` (message)
  * `[ListConfigApplicationRuleRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRuleRevisionsResponse)` (message)
  * `[ListConfigApplicationRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRulesRequest)` (message)
  * `[ListConfigApplicationRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRulesResponse)` (message)
  * `[ListDiscountsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListDiscountsRequest)` (message)
  * `[ListDiscountsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListDiscountsResponse)` (message)
  * `[ListEvaluationCaseResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCaseResultsRequest)` (message)
  * `[ListEvaluationCaseResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCaseResultsResponse)` (message)
  * `[ListEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCasesRequest)` (message)
  * `[ListEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCasesResponse)` (message)
  * `[ListEvaluationContextsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationContextsRequest)` (message)
  * `[ListEvaluationContextsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationContextsResponse)` (message)
  * `[ListEvaluationDatasetResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetResultsRequest)` (message)
  * `[ListEvaluationDatasetResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetResultsResponse)` (message)
  * `[ListEvaluationDatasetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetsRequest)` (message)
  * `[ListEvaluationDatasetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetsResponse)` (message)
  * `[ListEvaluationMatchersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationMatchersRequest)` (message)
  * `[ListEvaluationMatchersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationMatchersResponse)` (message)
  * `[ListIngestionLogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListIngestionLogsRequest)` (message)
  * `[ListIngestionLogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListIngestionLogsResponse)` (message)
  * `[ListInventoriesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListInventoriesRequest)` (message)
  * `[ListInventoriesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListInventoriesResponse)` (message)
  * `[ListMenuIssueClustersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssueClustersRequest)` (message)
  * `[ListMenuIssueClustersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssueClustersResponse)` (message)
  * `[ListMenuIssuesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssuesRequest)` (message)
  * `[ListMenuIssuesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssuesResponse)` (message)
  * `[ListMenusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenusRequest)` (message)
  * `[ListMenusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenusResponse)` (message)
  * `[ListRemediationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListRemediationsRequest)` (message)
  * `[ListRemediationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListRemediationsResponse)` (message)
  * `[ListSessionRecordsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListSessionRecordsRequest)` (message)
  * `[ListSessionRecordsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListSessionRecordsResponse)` (message)
  * `[ListStoreRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoreRevisionsRequest)` (message)
  * `[ListStoreRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoreRevisionsResponse)` (message)
  * `[ListStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoresRequest)` (message)
  * `[ListStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoresResponse)` (message)
  * `[ListWebhookSubscriptionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListWebhookSubscriptionsRequest)` (message)
  * `[ListWebhookSubscriptionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListWebhookSubscriptionsResponse)` (message)
  * `[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.LoyaltyAmount)` (message)
  * `[LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.LoyaltyInfo)` (message)
  * `[Menu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Menu)` (message)
  * `[MenuCategory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuCategory)` (message)
  * `[MenuIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig)` (message)
  * `[MenuIngestionConfig.AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.AvailabilityConfig)` (message)
  * `[MenuIngestionConfig.IngestionStoreMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.IngestionStoreMatcher)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.AutoBundleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.AutoBundleConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.CategoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.CategoryConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ItemIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemIntegrationAttributeConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig.ItemNumberMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig.ItemNumberMapping)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupIntegrationAttributeConfig)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule.NamingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule.NamingStrategy)` (enum)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule.SortStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule.SortStrategy)` (enum)
  * `[MenuIngestionConfig.ItemBuildingConfig.ModifierGroupReplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupReplicationRule)` (message)
  * `[MenuIngestionConfig.ItemBuildingConfig.SearchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.SearchConfig)` (message)
  * `[MenuIngestionConfig.LocalizedConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.LocalizedConfig)` (message)
  * `[MenuIngestionConfig.NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig)` (message)
  * `[MenuIngestionConfig.NameNormalizationConfig.ProductNameOverride](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig.ProductNameOverride)` (message)
  * `[MenuIngestionConfig.NameNormalizationConfig.RegexReplacement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig.RegexReplacement)` (message)
  * `[MenuIngestionConfig.ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` (message)
  * `[MenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue)` (message)
  * `[MenuIssue.ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.ConfidenceLevel)` (enum)
  * `[MenuIssue.EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.EntityType)` (enum)
  * `[MenuIssue.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.State)` (enum)
  * `[MenuIssueCluster](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueCluster)` (message)
  * `[MenuIssueClusterView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueClusterView)` (enum)
  * `[MenuLabel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuLabel)` (message)
  * `[MenuSchedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuSchedule)` (message)
  * `[MenuView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuView)` (enum)
  * `[MessageConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MessageConfig)` (message)
  * `[MetricMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MetricMetadata)` (message)
  * `[MetricValue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MetricValue)` (message)
  * `[MockClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MockClientExecution)` (message)
  * `[Modifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Modifier)` (message)
  * `[ModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierAction)` (message)
  * `[ModifierConstraints](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierConstraints)` (message)
  * `[ModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroup)` (message)
  * `[ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupIntegrationAttributes)` (message)
  * `[ModifierGroupIntegrationAttributes.ToastModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupIntegrationAttributes.ToastModifierGroupIntegrationAttributes)` (message)
  * `[ModifierGroupReference](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupReference)` (message)
  * `[ModifierGroupReference.DefaultModifierSelection](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupReference.DefaultModifierSelection)` (message)
  * `[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes)` (message)
  * `[ModifierIntegrationAttributes.ToastModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes.ToastModifierIntegrationAttributes)` (message)
  * `[NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.NutritionalInfo)` (message)
  * `[OfferMessage](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OfferMessage)` (message)
  * `[OperationsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OperationsConfig)` (message)
  * `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` (message)
  * `[OrderFulfillment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderFulfillment)` (message)
  * `[OrderItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderItem)` (message)
  * `[OrderLimits](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderLimits)` (message)
  * `[OrderMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderMetadata)` (message)
  * `[OrderModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifier)` (message)
  * `[OrderModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifierAction)` (message)
  * `[OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifierGroup)` (message)
  * `[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPriceInfo)` (message)
  * `[OrderPricesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPricesRequest)` (message)
  * `[OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPricesResponse)` (message)
  * `[OrderStatusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderStatusRequest)` (message)
  * `[OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderStatusResponse)` (message)
  * `[OwnershipType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OwnershipType)` (enum)
  * `[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PaymentInfo)` (message)
  * `[PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PaymentMethod)` (enum)
  * `[ProcessOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderRequest)` (message)
  * `[ProcessOrderRequest.TurnType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderRequest.TurnType)` (enum)
  * `[ProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderResponse)` (message)
  * `[PromoteChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PromoteChannelConfigRequest)` (message)
  * `[PromoteChannelConfigResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PromoteChannelConfigResponse)` (message)
  * `[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)` (message)
  * `[Remediation.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation.State)` (enum)
  * `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` (message)
  * `[RemediationAction.ActionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction.ActionType)` (enum)
  * `[RenamePayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RenamePayload)` (message)
  * `[ResolveMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ResolveMenuIssueRequest)` (message)
  * `[RestartOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RestartOrder)` (message)
  * `[ResumeRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ResumeRemediationRequest)` (message)
  * `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` (enum)
  * `[RunEvaluationCaseMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationCaseMetadata)` (message)
  * `[RunEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationCaseRequest)` (message)
  * `[RunEvaluationCaseResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationCaseResponse)` (message)
  * `[RunEvaluationDatasetMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetMetadata)` (message)
  * `[RunEvaluationDatasetMetadata.CompletedCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetMetadata.CompletedCase)` (message)
  * `[RunEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetRequest)` (message)
  * `[RunEvaluationDatasetResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetResponse)` (message)
  * `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` (message)
  * `[SentimentMeasurement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SentimentMeasurement)` (message)
  * `[SessionRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SessionRecord)` (message)
  * `[SpeechRecognition](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SpeechRecognition)` (message)
  * `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` (message)
  * `[StoreHours](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreHours)` (message)
  * `[StoreIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreIngestionConfig)` (message)
  * `[StoreIngestionConfig.StoreTimeZoneConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreIngestionConfig.StoreTimeZoneConfig)` (message)
  * `[StoreMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata)` (message)
  * `[StoreMetadata.Address](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Address)` (message)
  * `[StoreMetadata.Daypart](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Daypart)` (message)
  * `[StoreRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreRevision)` (message)
  * `[StoreStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreStatus)` (message)
  * `[StoreStatus.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreStatus.State)` (enum)
  * `[StoreView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreView)` (enum)
  * `[SubmitOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SubmitOrderRequest)` (message)
  * `[SuggestedAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedAction)` (message)
  * `[SuggestedActions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedActions)` (message)
  * `[SuggestedItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedItem)` (message)
  * `[SuggestedItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedItems)` (message)
  * `[SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModGroup)` (message)
  * `[SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifier)` (message)
  * `[SuggestedModifierGroups](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifierGroups)` (message)
  * `[SuggestedModifiers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifiers)` (message)
  * `[SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedOptions)` (message)
  * `[SuggestedStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedStore)` (message)
  * `[SuggestedStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedStores)` (message)
  * `[SuspendRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuspendRemediationRequest)` (message)
  * `[TargetItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TargetItem)` (message)
  * `[TargetModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TargetModifier)` (message)
  * `[TextInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TextInput)` (message)
  * `[TextInputAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TextInputAction)` (message)
  * `[TimeOfDayRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TimeOfDayRange)` (message)
  * `[TurnCompleted](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TurnCompleted)` (message)
  * `[UpdateBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateBrandRequest)` (message)
  * `[UpdateCategoryPayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateCategoryPayload)` (message)
  * `[UpdateChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateChannelConfigRequest)` (message)
  * `[UpdateConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateConfigApplicationRuleRequest)` (message)
  * `[UpdateDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateDiscountRequest)` (message)
  * `[UpdateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationCaseRequest)` (message)
  * `[UpdateEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationContextRequest)` (message)
  * `[UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationDatasetRequest)` (message)
  * `[UpdateEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationMatcherRequest)` (message)
  * `[UpdateInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateInventoryRequest)` (message)
  * `[UpdateStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateStoreRequest)` (message)
  * `[UpdateWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateWebhookSubscriptionRequest)` (message)
  * `[UpdatedOrderState](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdatedOrderState)` (message)
  * `[UpdatedOrderState.OrderStateUpdateStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdatedOrderState.OrderStateUpdateStatus)` (enum)
  * `[UpsellAttemptRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellAttemptRecord)` (message)
  * `[UpsellConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellConfig)` (message)
  * `[UpsellMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellMetrics)` (message)
  * `[UpsellMetrics.UpsellTypeMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellMetrics.UpsellTypeMetrics)` (message)
  * `[UpsellStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellStrategy)` (message)
  * `[ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidDeliveryStore)` (message)
  * `[ValidateDeliveryAddressRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidateDeliveryAddressRequest)` (message)
  * `[ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidateDeliveryAddressResponse)` (message)
  * `[WebhookAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig)` (message)
  * `[WebhookAuthConfig.ApiKeyAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.ApiKeyAuth)` (message)
  * `[WebhookAuthConfig.BasicAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.BasicAuth)` (message)
  * `[WebhookAuthConfig.BearerTokenAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.BearerTokenAuth)` (message)
  * `[WebhookAuthConfig.SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.SecretSource)` (message)
  * `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)` (message)
  * `[WebhookSubscription.State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription.State)` (enum)



## EvaluationRunService

EvaluationRunService provides an API to run evaluation cases.

RunEvaluationCase  
---  
` rpc RunEvaluationCase(`[RunEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationCaseRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Runs an evaluation case.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
RunEvaluationDataset  
---  
` rpc RunEvaluationDataset(`[RunEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Runs an evaluation dataset.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## FoodOrderingService

FoodOrderingService provides an API for food ordering agents.

BidiProcessOrder  
---  
` rpc BidiProcessOrder(`[BidiProcessOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderRequest)`) returns (`[BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderResponse)`) ` A bidirectional streaming API that processes continuous client inputs across multiple modalities (e.g., text, audio) and generates real-time multimodal output streams.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ProcessOrder  
---  
` rpc ProcessOrder(`[ProcessOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderRequest)`) returns (`[ProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderResponse)`) ` Performs a single turn logic to process user input and return the result.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
StreamProcessOrder  
---  
` rpc StreamProcessOrder(`[ProcessOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderRequest)`) returns (`[BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderResponse)`) ` Performs a single turn interaction, but uses server-side streaming to deliver incremental results and partial responses as they are generated.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## MenuService

MenuService provides APIs to manage brand, store and menu related resources.

AppendIngestionPhase  
---  
` rpc AppendIngestionPhase(`[AppendIngestionPhaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AppendIngestionPhaseRequest)`) returns (`[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)`) ` Appends an ingestion phase to an ingestion log.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchCreateEvaluationCases  
---  
` rpc BatchCreateEvaluationCases(`[BatchCreateEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchCreateEvaluationCasesRequest)`) returns (`[BatchCreateEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchCreateEvaluationCasesResponse)`) ` Batch creates EvaluationCases.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchDeleteStores  
---  
` rpc BatchDeleteStores(`[BatchDeleteStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchDeleteStoresRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Batch deletes stores.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchGetMenuEntities  
---  
` rpc BatchGetMenuEntities(`[BatchGetMenuEntitiesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetMenuEntitiesRequest)`) returns (`[BatchGetMenuEntitiesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetMenuEntitiesResponse)`) ` Batch gets entities for a menu.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchGetStores  
---  
` rpc BatchGetStores(`[BatchGetStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetStoresRequest)`) returns (`[BatchGetStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchGetStoresResponse)`) ` Batch gets stores.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchUpdateEvaluationCases  
---  
` rpc BatchUpdateEvaluationCases(`[BatchUpdateEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateEvaluationCasesRequest)`) returns (`[BatchUpdateEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateEvaluationCasesResponse)`) ` Batch updates EvaluationCases.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
BatchUpdateStores  
---  
` rpc BatchUpdateStores(`[BatchUpdateStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateStoresRequest)`) returns (`[BatchUpdateStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BatchUpdateStoresResponse)`) ` Batch updates stores.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ComputeAnalyticsMetrics  
---  
` rpc ComputeAnalyticsMetrics(`[ComputeAnalyticsMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest)`) returns (`[ComputeAnalyticsMetricsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsResponse)`) ` Computes analytics metrics for a given brand for specified time period with optional store filter.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateBrand  
---  
` rpc CreateBrand(`[CreateBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateBrandRequest)`) returns (`[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)`) ` Creates a brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateChannelConfig  
---  
` rpc CreateChannelConfig(`[CreateChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateChannelConfigRequest)`) returns (`[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)`) ` Creates a ChannelConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateConfigApplicationRule  
---  
` rpc CreateConfigApplicationRule(`[CreateConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateConfigApplicationRuleRequest)`) returns (`[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)`) ` Creates a ConfigApplicationRule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDiscount  
---  
` rpc CreateDiscount(`[CreateDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateDiscountRequest)`) returns (`[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)`) ` Creates a discount.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateEvaluationCase  
---  
` rpc CreateEvaluationCase(`[CreateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationCaseRequest)`) returns (`[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)`) ` Creates an EvaluationCase.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateEvaluationContext  
---  
` rpc CreateEvaluationContext(`[CreateEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationContextRequest)`) returns (`[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)`) ` Creates an EvaluationContext.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateEvaluationDataset  
---  
` rpc CreateEvaluationDataset(`[CreateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)`) ` Creates an EvaluationDataset.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateEvaluationMatcher  
---  
` rpc CreateEvaluationMatcher(`[CreateEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationMatcherRequest)`) returns (`[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)`) ` Creates an EvaluationMatcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateIngestionLog  
---  
` rpc CreateIngestionLog(`[CreateIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateIngestionLogRequest)`) returns (`[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)`) ` Creates an ingestion log.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateInventory  
---  
` rpc CreateInventory(`[CreateInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateInventoryRequest)`) returns (`[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)`) ` Creates an inventory.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateMenu  
---  
` rpc CreateMenu(`[CreateMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateMenuRequest)`) returns (`[Menu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Menu)`) ` Creates a menu.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateRemediation  
---  
` rpc CreateRemediation(`[CreateRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateRemediationRequest)`) returns (`[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)`) ` Creates a remediation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateStore  
---  
` rpc CreateStore(`[CreateStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateStoreRequest)`) returns (`[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)`) ` Creates a store.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateWebhookSubscription  
---  
` rpc CreateWebhookSubscription(`[CreateWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateWebhookSubscriptionRequest)`) returns (`[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)`) ` Creates a webhook subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteBrand  
---  
` rpc DeleteBrand(`[DeleteBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteBrandRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteBrandRevision  
---  
` rpc DeleteBrandRevision(`[DeleteBrandRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteBrandRevisionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified BrandRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteChannelConfig  
---  
` rpc DeleteChannelConfig(`[DeleteChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteChannelConfigRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified ChannelConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteChannelConfigRevision  
---  
` rpc DeleteChannelConfigRevision(`[DeleteChannelConfigRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteChannelConfigRevisionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified ChannelConfigRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteConfigApplicationRule  
---  
` rpc DeleteConfigApplicationRule(`[DeleteConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteConfigApplicationRuleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified ConfigApplicationRule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteConfigApplicationRuleRevision  
---  
` rpc DeleteConfigApplicationRuleRevision(`[DeleteConfigApplicationRuleRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteConfigApplicationRuleRevisionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified ConfigApplicationRuleRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDiscount  
---  
` rpc DeleteDiscount(`[DeleteDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteDiscountRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified discount.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationCase  
---  
` rpc DeleteEvaluationCase(`[DeleteEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationCaseRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationCase.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationCaseResult  
---  
` rpc DeleteEvaluationCaseResult(`[DeleteEvaluationCaseResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationCaseResultRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationCaseResult.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationContext  
---  
` rpc DeleteEvaluationContext(`[DeleteEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationContextRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationContext.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationDataset  
---  
` rpc DeleteEvaluationDataset(`[DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationDatasetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationDataset.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationDatasetResult  
---  
` rpc DeleteEvaluationDatasetResult(`[DeleteEvaluationDatasetResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationDatasetResultRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationDatasetResult.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluationMatcher  
---  
` rpc DeleteEvaluationMatcher(`[DeleteEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteEvaluationMatcherRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified EvaluationMatcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteIngestionLog  
---  
` rpc DeleteIngestionLog(`[DeleteIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteIngestionLogRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified ingestion log.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteInventory  
---  
` rpc DeleteInventory(`[DeleteInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteInventoryRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified inventory.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteMenu  
---  
` rpc DeleteMenu(`[DeleteMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteMenuRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified menu.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteRemediation  
---  
` rpc DeleteRemediation(`[DeleteRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteRemediationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a remediation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteSessionRecord  
---  
` rpc DeleteSessionRecord(`[DeleteSessionRecordRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteSessionRecordRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an SessionRecord. Note: This operation will remove the session details from the Spanner database. Associated data like audio recordings in GCS may also be removed depending on the implementation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteStore  
---  
` rpc DeleteStore(`[DeleteStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteStoreRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified store.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteStoreRevision  
---  
` rpc DeleteStoreRevision(`[DeleteStoreRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteStoreRevisionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified StoreRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteWebhookSubscription  
---  
` rpc DeleteWebhookSubscription(`[DeleteWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeleteWebhookSubscriptionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified webhook subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
FetchServiceHealth  
---  
` rpc FetchServiceHealth(`[FetchServiceHealthRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthRequest)`) returns (`[FetchServiceHealthResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse)`) ` Fetches operational service health telemetry for a specific region.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetBrand  
---  
` rpc GetBrand(`[GetBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetBrandRequest)`) returns (`[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)`) ` Gets a brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetBrandRevision  
---  
` rpc GetBrandRevision(`[GetBrandRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetBrandRevisionRequest)`) returns (`[BrandRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BrandRevision)`) ` Gets a BrandRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetChannelConfig  
---  
` rpc GetChannelConfig(`[GetChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetChannelConfigRequest)`) returns (`[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)`) ` Gets a ChannelConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetChannelConfigRevision  
---  
` rpc GetChannelConfigRevision(`[GetChannelConfigRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetChannelConfigRevisionRequest)`) returns (`[ChannelConfigRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfigRevision)`) ` Gets a ChannelConfigRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetConfigApplicationRule  
---  
` rpc GetConfigApplicationRule(`[GetConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetConfigApplicationRuleRequest)`) returns (`[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)`) ` Gets a ConfigApplicationRule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetConfigApplicationRuleRevision  
---  
` rpc GetConfigApplicationRuleRevision(`[GetConfigApplicationRuleRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetConfigApplicationRuleRevisionRequest)`) returns (`[ConfigApplicationRuleRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRuleRevision)`) ` Gets a ConfigApplicationRuleRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDiscount  
---  
` rpc GetDiscount(`[GetDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetDiscountRequest)`) returns (`[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)`) ` Gets a discount.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationCase  
---  
` rpc GetEvaluationCase(`[GetEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationCaseRequest)`) returns (`[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)`) ` Gets an EvaluationCase.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationCaseResult  
---  
` rpc GetEvaluationCaseResult(`[GetEvaluationCaseResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationCaseResultRequest)`) returns (`[EvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult)`) ` Gets an EvaluationCaseResult.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationContext  
---  
` rpc GetEvaluationContext(`[GetEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationContextRequest)`) returns (`[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)`) ` Gets an EvaluationContext.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationDataset  
---  
` rpc GetEvaluationDataset(`[GetEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)`) ` Gets an EvaluationDataset.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationDatasetResult  
---  
` rpc GetEvaluationDatasetResult(`[GetEvaluationDatasetResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationDatasetResultRequest)`) returns (`[EvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDatasetResult)`) ` Gets an EvaluationDatasetResult.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetEvaluationMatcher  
---  
` rpc GetEvaluationMatcher(`[GetEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetEvaluationMatcherRequest)`) returns (`[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)`) ` Gets an EvaluationMatcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetIngestionLog  
---  
` rpc GetIngestionLog(`[GetIngestionLogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetIngestionLogRequest)`) returns (`[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)`) ` Gets an ingestion log.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetInventory  
---  
` rpc GetInventory(`[GetInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetInventoryRequest)`) returns (`[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)`) ` Gets an inventory.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMenu  
---  
` rpc GetMenu(`[GetMenuRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuRequest)`) returns (`[Menu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Menu)`) ` Gets a menu.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMenuIssue  
---  
` rpc GetMenuIssue(`[GetMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuIssueRequest)`) returns (`[MenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue)`) ` Gets a menu issue.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetMenuIssueCluster  
---  
` rpc GetMenuIssueCluster(`[GetMenuIssueClusterRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetMenuIssueClusterRequest)`) returns (`[MenuIssueCluster](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueCluster)`) ` Gets a menu issue cluster.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetRemediation  
---  
` rpc GetRemediation(`[GetRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetRemediationRequest)`) returns (`[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)`) ` Gets a remediation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetSessionRecord  
---  
` rpc GetSessionRecord(`[GetSessionRecordRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetSessionRecordRequest)`) returns (`[SessionRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SessionRecord)`) ` Gets a specific SessionRecord. This method returns SessionRecord with audio_recording bytes if available.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetStore  
---  
` rpc GetStore(`[GetStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetStoreRequest)`) returns (`[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)`) ` Gets a store.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetStoreRevision  
---  
` rpc GetStoreRevision(`[GetStoreRevisionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetStoreRevisionRequest)`) returns (`[StoreRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreRevision)`) ` Gets a StoreRevision.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetWebhookSubscription  
---  
` rpc GetWebhookSubscription(`[GetWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GetWebhookSubscriptionRequest)`) returns (`[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)`) ` Gets a webhook subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
IgnoreMenuIssue  
---  
` rpc IgnoreMenuIssue(`[IgnoreMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IgnoreMenuIssueRequest)`) returns (`[MenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue)`) ` Ignores a menu issue, marking it as CLOSED_WONT_FIX.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBrandHistory  
---  
` rpc ListBrandHistory(`[ListBrandHistoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandHistoryRequest)`) returns (`[ListBrandHistoryResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandHistoryResponse)`) ` Lists history entries for a brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBrandRevisions  
---  
` rpc ListBrandRevisions(`[ListBrandRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandRevisionsRequest)`) returns (`[ListBrandRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandRevisionsResponse)`) ` Lists BrandRevisions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBrands  
---  
` rpc ListBrands(`[ListBrandsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandsRequest)`) returns (`[ListBrandsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListBrandsResponse)`) ` Lists brands.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListChannelConfigRevisions  
---  
` rpc ListChannelConfigRevisions(`[ListChannelConfigRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigRevisionsRequest)`) returns (`[ListChannelConfigRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigRevisionsResponse)`) ` Lists ChannelConfigRevisions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListChannelConfigs  
---  
` rpc ListChannelConfigs(`[ListChannelConfigsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigsRequest)`) returns (`[ListChannelConfigsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListChannelConfigsResponse)`) ` Lists ChannelConfigs.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListConfigApplicationRuleRevisions  
---  
` rpc ListConfigApplicationRuleRevisions(`[ListConfigApplicationRuleRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRuleRevisionsRequest)`) returns (`[ListConfigApplicationRuleRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRuleRevisionsResponse)`) ` Lists ConfigApplicationRuleRevisions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListConfigApplicationRules  
---  
` rpc ListConfigApplicationRules(`[ListConfigApplicationRulesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRulesRequest)`) returns (`[ListConfigApplicationRulesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListConfigApplicationRulesResponse)`) ` Lists ConfigApplicationRules.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDiscounts  
---  
` rpc ListDiscounts(`[ListDiscountsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListDiscountsRequest)`) returns (`[ListDiscountsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListDiscountsResponse)`) ` Lists discounts.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationCaseResults  
---  
` rpc ListEvaluationCaseResults(`[ListEvaluationCaseResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCaseResultsRequest)`) returns (`[ListEvaluationCaseResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCaseResultsResponse)`) ` Lists EvaluationCaseResults.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationCases  
---  
` rpc ListEvaluationCases(`[ListEvaluationCasesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCasesRequest)`) returns (`[ListEvaluationCasesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationCasesResponse)`) ` Lists EvaluationCases.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationContexts  
---  
` rpc ListEvaluationContexts(`[ListEvaluationContextsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationContextsRequest)`) returns (`[ListEvaluationContextsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationContextsResponse)`) ` Lists EvaluationContexts.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationDatasetResults  
---  
` rpc ListEvaluationDatasetResults(`[ListEvaluationDatasetResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetResultsRequest)`) returns (`[ListEvaluationDatasetResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetResultsResponse)`) ` Lists EvaluationDatasetResults.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationDatasets  
---  
` rpc ListEvaluationDatasets(`[ListEvaluationDatasetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetsRequest)`) returns (`[ListEvaluationDatasetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationDatasetsResponse)`) ` Lists EvaluationDatasets.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListEvaluationMatchers  
---  
` rpc ListEvaluationMatchers(`[ListEvaluationMatchersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationMatchersRequest)`) returns (`[ListEvaluationMatchersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListEvaluationMatchersResponse)`) ` Lists EvaluationMatchers.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListIngestionLogs  
---  
` rpc ListIngestionLogs(`[ListIngestionLogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListIngestionLogsRequest)`) returns (`[ListIngestionLogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListIngestionLogsResponse)`) ` Lists ingestion logs.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListInventories  
---  
` rpc ListInventories(`[ListInventoriesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListInventoriesRequest)`) returns (`[ListInventoriesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListInventoriesResponse)`) ` Lists inventories.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMenuIssueClusters  
---  
` rpc ListMenuIssueClusters(`[ListMenuIssueClustersRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssueClustersRequest)`) returns (`[ListMenuIssueClustersResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssueClustersResponse)`) ` Lists menu issue clusters for a brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMenuIssues  
---  
` rpc ListMenuIssues(`[ListMenuIssuesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssuesRequest)`) returns (`[ListMenuIssuesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenuIssuesResponse)`) ` Lists menu issues.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMenus  
---  
` rpc ListMenus(`[ListMenusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenusRequest)`) returns (`[ListMenusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListMenusResponse)`) ` Lists menus.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListRemediations  
---  
` rpc ListRemediations(`[ListRemediationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListRemediationsRequest)`) returns (`[ListRemediationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListRemediationsResponse)`) ` Lists remediations.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListSessionRecords  
---  
` rpc ListSessionRecords(`[ListSessionRecordsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListSessionRecordsRequest)`) returns (`[ListSessionRecordsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListSessionRecordsResponse)`) ` Lists SessionRecords for a given brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListStoreRevisions  
---  
` rpc ListStoreRevisions(`[ListStoreRevisionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoreRevisionsRequest)`) returns (`[ListStoreRevisionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoreRevisionsResponse)`) ` Lists StoreRevisions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListStores  
---  
` rpc ListStores(`[ListStoresRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoresRequest)`) returns (`[ListStoresResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListStoresResponse)`) ` Lists stores.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListWebhookSubscriptions  
---  
` rpc ListWebhookSubscriptions(`[ListWebhookSubscriptionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListWebhookSubscriptionsRequest)`) returns (`[ListWebhookSubscriptionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ListWebhookSubscriptionsResponse)`) ` Lists webhook subscriptions for a brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
PromoteChannelConfig  
---  
` rpc PromoteChannelConfig(`[PromoteChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PromoteChannelConfigRequest)`) returns (`[PromoteChannelConfigResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PromoteChannelConfigResponse)`) ` Promotes the specified channel config.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ResolveMenuIssue  
---  
` rpc ResolveMenuIssue(`[ResolveMenuIssueRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ResolveMenuIssueRequest)`) returns (`[MenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue)`) ` Resolves a menu issue and records the remediation action taken.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ResumeRemediation  
---  
` rpc ResumeRemediation(`[ResumeRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ResumeRemediationRequest)`) returns (`[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)`) ` Resumes a suspended remediation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SuspendRemediation  
---  
` rpc SuspendRemediation(`[SuspendRemediationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuspendRemediationRequest)`) returns (`[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)`) ` Suspends a remediation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateBrand  
---  
` rpc UpdateBrand(`[UpdateBrandRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateBrandRequest)`) returns (`[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)`) ` Updates the specified brand.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateChannelConfig  
---  
` rpc UpdateChannelConfig(`[UpdateChannelConfigRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateChannelConfigRequest)`) returns (`[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)`) ` Updates the specified ChannelConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateConfigApplicationRule  
---  
` rpc UpdateConfigApplicationRule(`[UpdateConfigApplicationRuleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateConfigApplicationRuleRequest)`) returns (`[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)`) ` Updates the specified ConfigApplicationRule.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDiscount  
---  
` rpc UpdateDiscount(`[UpdateDiscountRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateDiscountRequest)`) returns (`[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)`) ` Updates the specified discount.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateEvaluationCase  
---  
` rpc UpdateEvaluationCase(`[UpdateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationCaseRequest)`) returns (`[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)`) ` Updates the specified EvaluationCase.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateEvaluationContext  
---  
` rpc UpdateEvaluationContext(`[UpdateEvaluationContextRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationContextRequest)`) returns (`[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)`) ` Updates the specified EvaluationContext.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateEvaluationDataset  
---  
` rpc UpdateEvaluationDataset(`[UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)`) ` Updates the specified EvaluationDataset.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateEvaluationMatcher  
---  
` rpc UpdateEvaluationMatcher(`[UpdateEvaluationMatcherRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationMatcherRequest)`) returns (`[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)`) ` Updates the specified EvaluationMatcher.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateInventory  
---  
` rpc UpdateInventory(`[UpdateInventoryRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateInventoryRequest)`) returns (`[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)`) ` Updates the specified inventory.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateStore  
---  
` rpc UpdateStore(`[UpdateStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateStoreRequest)`) returns (`[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)`) ` Update the specified store.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateWebhookSubscription  
---  
` rpc UpdateWebhookSubscription(`[UpdateWebhookSubscriptionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateWebhookSubscriptionRequest)`) returns (`[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)`) ` Updates the specified webhook subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AgentAudio

The audio response from the agent.

Fields  
---  
`agent_audio` |  `bytes` The audio data from the agent.  
  
## AgentEvent

Special event from the agent that needs client to take action.

Fields  
---  
Union field `event`. The event from the agent. `event` can be only one of the following:  
`restart_order` |  `[RestartOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RestartOrder)` Customer requests to restart the order.  
  
## AgentText

The text response from the agent.

Fields  
---  
`text` |  `string` The text response from the agent.  
  
## AnalyticsMetrics

Represents analytics metrics for a given period, with a comparison to a previous period.

Fields  
---  
`interval_metrics[]` |  `[IntervalMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics)` Metrics for the intervals.  
`metrics_metadata[]` |  `[MetricMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MetricMetadata)` Static display metadata for all returned metrics.  
  
## AppendIngestionPhaseRequest

Request message for `[MenuService.AppendIngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.AppendIngestionPhase)`.

Fields  
---  
`name` |  `string` Required. The name of the ingestion log to append the phase to. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestion_log}  
`ingestion_phase` |  `[IngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase)` Required. The ingestion phase to append.  
`menu` |  `string` Optional. The resource name of the menu created or updated by this ingestion. Format: projects/{project}/locations/{location}/menus/{menu}  
  
## AudioInput

The audio input from the client. The input audio may have multiple channels for the customer, crew, etc. These should all be synchronized and in the format specified by the configuration . Audio headers should not be included. By default, the audio should be using 16-bit linear PCM audio encoding and 16000 Hz sample rate. Total bytes from all channels should be less than 25600 bytes.

Fields  
---  
`customer_audio` |  `bytes` Required. Customer audio data.  
`crew_audio` |  `bytes` Optional. Crew audio data. This is an optional audio channel for the crew member in the same lane as the customer, and served as the reference audio for echo cancellation.  
  
## AuditLogEntry

Represents a single historical action taken on an issue.

Fields  
---  
`user` |  `string` Output only. The email address of the user or principal who performed the action.  
`record_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the action was recorded.  
`applied_remediation_action` |  `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` Output only. The remediation action that was applied, if any.  
`resulting_state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.State)` Output only. The state of the issue after the action was applied.  
  
## Availability

Defines the availability of an item or modifier.

Fields  
---  
`daypart_availability` |  `[DaypartAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.DaypartAvailability)` Optional. Daypart-level availability information for this item. If omitted, daypart-based availability is ignored.  
`menu_schedule_availability` |  `[MenuScheduleAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.MenuScheduleAvailability)` Optional. Menu schedule-level availability information for this item. If omitted, menu schedule-based availability is ignored.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.Status)` Optional. Indicates a status leading to unavailability, or that the item is available. If omitted, the item is available by default.  
`fulfillment_availability` |  `[FulfillmentMethodAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.FulfillmentMethodAvailability)` Optional. The fulfillment methods this item is available for. If omitted, the item is available for all fulfillment methods.  
`channel_type_availability` |  `[ChannelTypeAvailability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability.ChannelTypeAvailability)` Optional. The channel types this item is available for. If omitted, the item is available for all channel types.  
  
## ChannelTypeAvailability

Constrains availability of this entity to specified channel types.

Fields  
---  
`channel_types[]` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Required. Channel types for which this item is available.  
  
## DaypartAvailability

Constrains availability of this entity to specified dayparts.

Fields  
---  
`daypart_ids[]` |  `string` Required. Dayparts during which this item is available.  
  
## FulfillmentMethodAvailability

Constrains availability of this entity to specified fulfillment methods.

Fields  
---  
`fulfillment_methods[]` |  `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` Required. Fulfillment methods for which this item is available.  
  
## MenuScheduleAvailability

Constrains availability of this entity to specified menu schedule.

Fields  
---  
`menu_schedule_ids[]` |  `string` Required. Menu schedules during which this item is available.  
  
## Status

Status of availability.

Enums  
---  
`STATUS_UNSPECIFIED` | Invalid status. CreateMenu will fail if any item or modifier has this status.  
`STATUS_AVAILABLE` | Indicates that the item is available for purchase.  
`STATUS_UNAVAILABLE` | Indicates that the item is unavailable for ambiguous reasons.  
`STATUS_OUT_OF_STOCK` | Indicates that the item is currently out of stock, but may become available in the near future.  
`STATUS_DISCONTINUED` | Indicates that the item is discontinued, and will remain unavailable for the foreseeable future.  
  
## BatchCreateEvaluationCasesRequest

Request message for `[MenuService.BatchCreateEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchCreateEvaluationCases)`.

Fields  
---  
`parent` |  `string` Required. The parent resource shared by all evaluation cases being created. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the evaluation cases specified in `requests` must match this field.  
`requests[]` |  `[CreateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CreateEvaluationCaseRequest)` Required. The request message specifying the resources to create. A maximum of 1000 evaluation cases can be created in a batch.  
  
## BatchCreateEvaluationCasesResponse

Response message for `[MenuService.BatchCreateEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchCreateEvaluationCases)`.

Fields  
---  
`evaluation_cases[]` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` EvaluationCases created.  
  
## BatchDeleteStoresRequest

Request message for `[MenuService.BatchDeleteStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchDeleteStores)`.

Fields  
---  
`parent` |  `string` Required. The parent resource shared by all stores being deleted. Format: projects/{project}/locations/{location}/brands/{brand}  
`names[]` |  `string` Required. The names of the stores to delete. A maximum of 1000 stores can be deleted in a batch. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
## BatchGetMenuEntitiesRequest

Request message for `[MenuService.BatchGetMenuEntities](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetMenuEntities)`.

Fields  
---  
`parent` |  `string` Required. The name of the menu to retrieve entities from. Format: projects/{project}/locations/{location}/menus/{menu}  
`item_ids[]` |  `string` Optional. The IDs of the items to retrieve.  
`modifier_ids[]` |  `string` Optional. The IDs of the modifier to retrieve.  
`modifier_group_ids[]` |  `string` Optional. The IDs of the modifier groups to retrieve.  
`category_ids[]` |  `string` Optional. The IDs of the categories to retrieve.  
  
## BatchGetMenuEntitiesResponse

Response message for `[MenuService.BatchGetMenuEntities](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetMenuEntities)`.

Fields  
---  
`items[]` |  `[Item](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Item)` The items requested.  
`modifiers[]` |  `[Modifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Modifier)` The modifiers requested.  
`modifier_groups[]` |  `[ModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroup)` The modifier groups requested.  
`categories[]` |  `[MenuCategory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuCategory)` The categories requested.  
  
## BatchGetStoresRequest

Request message for `[MenuService.BatchGetStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetStores)`.

Fields  
---  
`parent` |  `string` Required. The parent resource shared by all stores being retrieved. Format: projects/{project}/locations/{location}/brands/{brand}  
`names[]` |  `string` Required. The names of the stores to retrieve. A maximum of 1000 stores can be retrieved in a batch. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
## BatchGetStoresResponse

Response message for `[MenuService.BatchGetStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchGetStores)`.

Fields  
---  
`stores[]` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` The requested stores.  
  
## BatchUpdateEvaluationCasesRequest

Request message for `[MenuService.BatchUpdateEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateEvaluationCases)`.

Fields  
---  
`parent` |  `string` Required. The parent resource shared by all evaluation cases being updated. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the evaluation cases specified in `requests` must match this field.  
`requests[]` |  `[UpdateEvaluationCaseRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateEvaluationCaseRequest)` Required. The request message specifying the resources to update. A maximum of 1000 evaluation cases can be modified in a batch.  
  
## BatchUpdateEvaluationCasesResponse

Response message for `[MenuService.BatchUpdateEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateEvaluationCases)`.

Fields  
---  
`evaluation_cases[]` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` EvaluationCases updated.  
  
## BatchUpdateStoresRequest

Request message for `[MenuService.BatchUpdateStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateStores)`.

Fields  
---  
`parent` |  `string` Required. The parent resource shared by all stores being updated. Format: projects/{project}/locations/{location}/brands/{brand} If this is set, the parent of all of the stores specified in `requests` must match this field.  
`requests[]` |  `[UpdateStoreRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateStoreRequest)` Required. The request message specifying the resources to update. A maximum of 1000 stores can be modified in a batch.  
  
## BatchUpdateStoresResponse

Response message for `[MenuService.BatchUpdateStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.BatchUpdateStores)`.

Fields  
---  
`stores[]` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` Stores updated.  
  
## BidiProcessOrderRequest

The top-level message sent by the client for the `[FoodOrderingService.BidiProcessOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.BidiProcessOrder)` method.

Fields  
---  
Union field `message`. The message from the client. The client must send a config message first, before sending any other messages. `message` can be only one of the following:  
`config` |  `[Config](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config)` The configuration for the session and food ordering properties.  
`text_input` |  `[TextInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TextInput)` The text input from the client.  
`audio_input` |  `[AudioInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AudioInput)` The audio input from the client. The client must use either text or audio input, not both.  
`event_input` |  `[EventInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput)` The event input from the client.  
`client_execution_result` |  `[ClientExecutionResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientExecutionResult)` The result of a client execution request.  
`dtmf_input` |  `[DtmfInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DtmfInput)` The DTMF input from the client.  
  
## BidiProcessOrderResponse

The top-level message returned from `[FoodOrderingService.BidiProcessOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.BidiProcessOrder)` method.

Fields  
---  
`diagnostic_info` |  `[DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiagnosticInfo)` Diagnostic information containing execution timing, VAD speech boundaries, and latency metrics for the completed turn. Populated upon turn completion.  
Union field `response`. The response from the agent. `response` can be only one of the following:  
`agent_audio` |  `[AgentAudio](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentAudio)` The audio response from the agent.  
`speech_recognition` |  `[SpeechRecognition](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SpeechRecognition)` The speech recognition result from the agent.  
`legacy_order_state_response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The legacy order state response for a session.  
`interruption_signal` |  `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.InterruptionSignal)` Interruption signal detected from the audio input.  
`agent_event` |  `[AgentEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentEvent)` Event from the agent.  
`client_execution_request` |  `[ClientExecutionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientExecutionRequest)` The request forward to the client to execute. This is used for client side execution, such as adding a code to the order.  
`updated_order_state` |  `[UpdatedOrderState](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdatedOrderState)` Indicates an update to the order state. Includes the complete state of the order.  
`agent_text` |  `[AgentText](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AgentText)` The text response from the agent.  
`suggested_options` |  `[SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedOptions)` Options to suggest to the customer.  
`sentiment_measurement` |  `[SentimentMeasurement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SentimentMeasurement)` The realtime sentiment score measured for this turn.  
`turn_completed` |  `[TurnCompleted](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TurnCompleted)` Turn Completed message.  
`end_session` |  `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EndSession)` Indicates that the session is ending, and that this will be the last turn.The agent will finish sending any pending responses for the current turn, and then send a final turn_completed message. The agent will not start any new turns. For example, a 2 turn session will look like:

  * Turn 1
  * customer input 1
  * ... agent response and order state messages
  * turn_completed
  * Turn 2
  * customer input 2
  * ... agent response and order state messages
  * end_session
  * ... pending agent response and order state messages
  * turn_completed

  
  
## Blob

Represents a blob input or output in the conversation.

Fields  
---  
`mime_type` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `bytes` Required. Raw bytes of the blob.  
  
## Brand

A brand, which can be a restaurant chain or an individual restaurant.

Fields  
---  
`name` |  `string` Identifier. The brand name. Format: projects/{project}/locations/{location}/brands/{brand}  
`display_name` |  `string` Optional. Optional, human-readable display name for this brand for user interfaces.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this brand was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this brand was last updated.  
`default_channel_config` |  `string` Optional. Name of the ChannelConfig to use as the brand default for agent customization. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
`config_rule_bindings[]` |  `[ConfigRuleBinding](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigRuleBinding)` Optional. Conditional agent config overrides for the brand. These allow for overriding agent behavior based on certain conditions.  
`default_upsell_strategy_channel_config` |  `string` Optional. Name of the ChannelConfig to use as the brand default for upsell strategy. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
`kms_key` |  `string` Optional. Immutable. The Cloud KMS key to encrypt conversational session data at rest. Format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}`This field can only be set when creating a Brand and cannot be updated or disabled later.  
`mcp_config` |  `[McpConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand.McpConfig)` Optional. Configuration for Model Context Protocol (MCP) service.  
`time_zone` |  `[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeZone)` Optional. The time zone of the brand. This is used for brand-level analytics and reporting rollups.  
`menu_ingestion_config` |  `[MenuIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig)` Optional. Configuration for menu ingestion.  
`geo_api_consent_granted` |  `bool` Optional. Whether customer has granted legal consent to use the Geocoding API.  
`store_ingestion_config` |  `[StoreIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreIngestionConfig)` Optional. Configuration for store ingestion.  
`default_channel_type` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Optional. The default channel type for this brand if not specified in the session config.  
  
## McpConfig

Configuration for Model Context Protocol (MCP) service.

Fields  
---  
`enabled` |  `bool` Optional. Whether the MCP service is enabled for the brand.  
  
## BrandRevision

A revision of a brand.

Fields  
---  
`name` |  `string` Identifier. The resource name of the brand revision. Format: projects/{project}/locations/{location}/brands/{brand}/revisions/{revision}  
`snapshot` |  `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` Output only. The state of the brand resource at this revision.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. When the revision was created.  
`created_by` |  `string` Output only. The email of the user who recently created the resource.  
`alternate_ids[]` |  `string` Output only. Alternate IDs for this revision.  
`action` |  `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` Output only. The action that created this revision.  
  
## CelUpsell

Represents a pre-computed rule that defines under what contextual conditions a set of items should be proactively upsold to the user.

Fields  
---  
`condition_expression` |  `string` Required. A CEL (Common Expression Language) string evaluated against the current session state (`Order` and `ClientSessionMetadata`). If it evaluates to True, the rule triggers. Example: `"context.weather_condition == 'HOT' && order.items.size() > 0"`  
`suggested_menu_items[]` |  `string` Required. The semantic names of the items to suggest if this rule triggers.  
`trigger_reason` |  `string` Optional. A natural language instruction provided to the conversational LLM explaining _why_ this upsell is being made, so it can formulate a natural upsell. Example: `"Suggest a cold drink because it is a hot day."`  
`priority` |  `int32` Optional. The `priority` of this rule. Higher numbers mean higher priority. If multiple rules trigger, the highest priority rule's suggestions are favored. If omitted, the `priority` defaults to `0`.  
`suggested_modifiers[]` |  `string` Optional. The semantic names of the modifiers to suggest if this rule triggers.  
`suggested_modifier_groups[]` |  `[SuggestedModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CelUpsell.SuggestedModifierGroup)` Optional. The modifier groups to suggest if this rule triggers.  
`max_modifier_per_group` |  `int32` Optional. Max number of modifiers to suggest per group.  
`suggestion_only` |  `bool` Optional. Not real upsell, but just to show the suggested options to user.  
  
## SuggestedModifierGroup

A suggested modifier group.

Fields  
---  
`name` |  `string` Optional. The semantic name of the modifier group.  
`suggested_modifiers[]` |  `string` Optional. The semantic names of the modifiers to suggest within this group.  
  
## ChannelConfig

A channel configuration represents an operational strategy configuration. Channel configuration lifecycle: * **DRAFT** : A configuration is in a draft state when it has no associated config application rules and is not set as the default configuration for the brand. * **ACTIVE** : A configuration is in an active state when it is either associated with any config application rule or set as the brand's default. * When active, the runtime applies the channel configuration to matching stores. To ensure flexibility, the relationship between channel configuration and config application rule is one-to-many on each resource level: * On the brand level, there is a one-to-many relationship between channel configurations and config application rules. * On the store level, there is another one-to-many relationship between channel configurations and config application rules. When multiple channel configurations are applicable, the runtime determines the configuration to apply based on the following precedence order (latter overwrites former in case of conflict): 1. Brand-level default 2. Brand-level binding 3. Store-level default 4. Store-level binding

Fields  
---  
`name` |  `string` Identifier. The channel configuration name. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
`display_name` |  `string` Optional. Optional display name for this channel configuration for user interfaces. Value is limited to 63 characters.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this channel configuration was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this channel configuration was last updated.  
`operations_config` |  `[OperationsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OperationsConfig)` Optional. The operational strategy for the channel configuration.  
`tts_config` |  `[TTSConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.TTSConfig)` Optional. Configuration for text-to-speech. Note: This configuration does not apply to audio-to-audio agents.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.State)` Output only. The status of the channel configuration.  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.Type)` Required. The type of the channel configuration.  
`supplemental_instructions` |  `[SupplementalInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.SupplementalInstructions)` Optional. Supplemental instructions for the channel configuration.  
`tone` |  `[Tone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.Tone)` Optional. The tone of the agent.  
`config_application_rules[]` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` Output only. The config application rules associated with this channel configuration.  
`enabled_stores[]` |  `string` Output only. The names of the stores that have this channel configuration enabled. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
## State

Status of the channel configuration.

Enums  
---  
`STATE_UNSPECIFIED` | Status is unspecified.  
`DRAFT` | The channel configuration is a draft and not yet ready for use.  
`ACTIVE` | The channel configuration is active and can be used.  
`PROMOTED` | The channel configuration is promoted.  
  
## SupplementalInstructions

Configurations for supplemental instructions.

Fields  
---  
`freeform_instructions` |  `string` Optional. Free-form instructions included in the prompt.  
`store_selection_brand_instructions` |  `string` Optional. Supplemental brand instructions to include in prompt during store selection & explore mode.  
  
## TTSConfig

Configurations for text-to-speech behavior.

Fields  
---  
`voice_configs[]` |  `[VoiceConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig.TTSConfig.VoiceConfig)` Optional. The per-language voice configs for the channel configuration.  
  
## VoiceConfig

Configuration for a specific language's voice.

Fields  
---  
`language_code` |  `string` Optional. The language code of the voice configuration. BCP-47 language code, such as "en-US" or "fr-CA".  
`voice_id` |  `string` Optional. The ID of the voice to use.  
`speaking_rate` |  `double` Optional. The speaking rate of the voice. Value is limited to the range [0.5, 2.0].  
  
## Tone

The tone of the agent.

Enums  
---  
`TONE_UNSPECIFIED` | Tone is unspecified.  
`CONCISE_AND_DIRECT` | The agent's tone is concise and direct.  
`PROFESSIONAL_AND_FORMAL` | The agent's tone is professional and formal.  
`FRIENDLY` | The agent's tone is friendly.  
  
## Type

The type of the channel configuration.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`UPSELL_STRATEGY` | The channel configuration is for upsell strategy.  
`AGENT_CUSTOMIZATION` | The channel configuration is for agent customization.  
  
## ChannelConfigRevision

A revision of a channel configuration.

Fields  
---  
`name` |  `string` Identifier. The resource name of the channel config revision. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}/revisions/{revision}  
`snapshot` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` Output only. The state of the channel config resource at this revision.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. When the revision was created.  
`created_by` |  `string` Output only. The email of the user who recently created the resource.  
`alternate_ids[]` |  `string` Output only. Alternate IDs for this revision.  
`action` |  `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` Output only. The action that created this revision.  
  
## ChannelType

The type of channel used for agent communication. A channel type captures both the surface (e.g. mobile app, web app) and, for surfaces that support multiple conversation modes, the conversation mode. For mobile and web surfaces, the bare value (e.g. CHANNEL_TYPE_MOBILE_APP) denotes the voice conversation mode, and the "_TEXT" variant denotes the text (or multimodal, e.g. tap-to-speak) conversation mode. This enum is not frozen, and new values may be added in the future.

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` | Unspecified channel type.  
`CHANNEL_TYPE_DRIVE_THROUGH` | Drive through channel (voice).  
`CHANNEL_TYPE_MOBILE_APP` | Mobile app channel using the voice conversation mode.  
`CHANNEL_TYPE_PHONE_CALL` | Phone call channel (voice).  
`CHANNEL_TYPE_WEB_APP` | Web app channel using the voice conversation mode.  
`CHANNEL_TYPE_MOBILE_APP_TEXT` | Mobile app channel using the text (or multimodal, e.g. tap-to-speak) conversation mode.  
`CHANNEL_TYPE_WEB_APP_TEXT` | Web app channel using the text (or multimodal, e.g. tap-to-speak) conversation mode.  
  
## ChildSynonym

Child synonym for a menu entity. This is to support cases like "Sausage Egg Cheese Biscuit" to "Sausage Egg Biscuit" with modifier "Cheese".

Fields  
---  
`synonym` |  `string` Optional. The synonym for the menu entity.  
`children[]` |  `string` Optional. Additional child that needs to match for that synonym.  
  
## ClientAppInfo

Information about the client application and device environment. This is primarily used for logging, analytics, and debugging.

Fields  
---  
`device_model` |  `string` Optional. The device model of the client (e.g., "iPhone 13", "Pixel 7", "Kiosk v2").  
`os_version` |  `string` Optional. The operating system version of the client (e.g., "iOS 16.1", "Android 13").  
`sdk_version` |  `string` Optional. The version of the client SDK or application software.  
  
## ClientExecutionRequest

A request to the for client side to execute a command.

Fields  
---  
`execution_id` |  `string` Required. A unique ID for this execution request.  
Union field `request`. The specific request to be executed. `request` can be only one of the following:  
`finalize_order_request` |  `[FinalizeOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FinalizeOrderRequest)` A request to finalize the order.  
`submit_order_request` |  `[SubmitOrderRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SubmitOrderRequest)` A request to submit the order.  
`order_prices_request` |  `[OrderPricesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPricesRequest)` A request to get the order prices.  
`validate_delivery_address_request` |  `[ValidateDeliveryAddressRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidateDeliveryAddressRequest)` A request to validate the delivery address.  
`order_status_request` |  `[OrderStatusRequest](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderStatusRequest)` A request to get the order status.  
  
## ClientExecutionResult

The result of a client execution request.

Fields  
---  
`execution_id` |  `string` Required. The ID of the execution request this is a result for.  
Union field `response`. The specific result of the execution. `response` can be only one of the following:  
`finalize_order_response` |  `[FinalizeOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FinalizeOrderResponse)` The result of finalizing the order.  
`order_prices_response` |  `[OrderPricesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPricesResponse)` The result of getting the order prices.  
`validate_delivery_address_response` |  `[ValidateDeliveryAddressResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidateDeliveryAddressResponse)` The result of validating the delivery address.  
`order_status_response` |  `[OrderStatusResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderStatusResponse)` The result of getting the order status.  
  
## ClosingOffer

Upsell specific items after a customer has completed their order.

Fields  
---  
`closing_messages[]` |  `[ClosingMessage](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClosingOffer.ClosingMessage)` Required. Closing offer upsells to apply.  
  
## ClosingMessage

Closing upsell message configuration.

Fields  
---  
`offer_message` |  `[OfferMessage](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OfferMessage)` Required. Offer message configuration.  
`skip_terms[]` |  `string` Optional. This upsell will be skipped if any of these terms are present in the name of an item already in the customer's order.  
  
## ClusteredEntityIssue

Represents a deduplicated menu entity issue within a brand-level MenuIssueCluster, aggregated across all stores where the entity exhibits the issue.

Fields  
---  
`entity_id` |  `string` Output only. The ID of the affected menu entity.  
`entity_display_name` |  `string` Output only. Human-readable display name of the affected entity.  
`entity_type` |  `[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.EntityType)` Output only. The type of the affected entity.  
`issue_category` |  `string` Output only. The category of the issue flagged on this entity.  
`explanation` |  `string` Output only. A representative explanation of why the issue was flagged on this entity.  
`confidence_level` |  `[ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.ConfidenceLevel)` Output only. The highest confidence level observed for this entity issue across stores.  
`suggested_remediation_actions[]` |  `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` Output only. Entity-specific remediation actions recommended to fix this issue (including entity-specific rename or category payloads).  
`affected_store_count` |  `int32` Output only. The number of stores where this entity issue was detected.  
  
## ComputeAnalyticsMetricsRequest

Request message for `[MenuService.ComputeAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ComputeAnalyticsMetrics)`.

Fields  
---  
`brand` |  `string` Required. The brand to get analytics metrics for. Format: projects/{project}/locations/{location}/brands/{brand}  
`timestamps[]` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The timestamps that mark the start of each interval for which analytics metrics are calculated.  
`store_ids[]` |  `string` Optional. The list of store IDs to get analytics metrics for. If not specified, analytics metrics for all stores will be returned. Needed to query by city or state.  
`analytics_types[]` |  `[AnalyticsType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest.AnalyticsType)` Optional. The types of analytics to compute. If empty or unspecified, all available analytics types will be computed.  
`feature_gate` |  `[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ComputeAnalyticsMetricsRequest.FeatureGate)` Optional. Feature gates.  
`channel_type` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Optional. The channel type to filter analytics metrics by.  
  
## AnalyticsType

The type of analytics to compute.

Enums  
---  
`ANALYTICS_TYPE_UNSPECIFIED` | Unspecified analytics type.  
`GENERIC` | Compute generic/overall metrics (e.g., order count, escalation count, upsell count).  
`DAILY` | Compute daily metrics (e.g., daily order and escalation counts).  
`PREDICTED_FAILURE_CATEGORIES` | Compute predicted failure category metrics (e.g., predicted failure category count).  
  
## FeatureGate

Feature gates to control analytics computation behavior.

Fields  
---  
`enable_aggregation_data` |  `bool` Optional. For limited brands only. If set, compute analytics metrics using aggregation data.  
`enable_metrics_config` |  `bool` Optional. If set, use the dynamic configuration-driven metrics engine.  
  
## ComputeAnalyticsMetricsResponse

Response message for `[MenuService.ComputeAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ComputeAnalyticsMetrics)`.

Fields  
---  
`analytics_metrics` |  `[AnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AnalyticsMetrics)` Output only. The analytics metrics for the brand.  
  
## Config

The configuration for a session and food ordering properties. At the start of each connection, the client must first send a config message. This must happen before any other requests to initiate the session. If the client disconnects, they should repeat the same config message when they reconnect.

Fields  
---  
`session` |  `string` Required. The session for the order. Format: `projects/{project}/locations/{location}/sessions/{session}`  
`store` |  `string` Required. The store the order is being placed for. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
`lane_id` |  `string` Optional. The id of a specifc drive through lane.  
`enable_echo_cancellation` |  `bool` Optional. Whether to enable echo cancellation for the session. If enabled, the client should provide the customer_audio and crew_audio in the AudioInput.  
`daypart_id` |  `string` Optional. Daypart of the food menu, including breakfast, lunch, dinner, etc. This is used to determine the menu to use for the order.  
`feature_gate` |  `[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeatureGate)` Optional. The feature gates for the session. This is used to enable or disable features for the session.  
`client_app_info` |  `[ClientAppInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientAppInfo)` Optional. The information about the client application and device environment.  
`mode` |  `[SessionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config.SessionMode)` Optional. The mode of the session.  
`channel_type` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Optional. The type of channel used for agent communication.  
`enable_listen_only_dual_channel` |  `bool` Optional. Whether to enable listen-only dual channel for the session. If enabled, the client should provide the customer_audio and crew_audio in the AudioInput.  
`test_session_start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The start time of the session, used for testing or evaluation purposes.  
`fulfillment_method` |  `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` Optional. The fulfillment method for the session.  
`client_env` |  `string` Optional. The environment on the client side (e.g., "qa", "uat", "preprod").  
  
## SessionMode

The mode of the session.

Enums  
---  
`SESSION_MODE_UNSPECIFIED` | The session mode is not specified.  
`HYBRID` | The session supports both audio and text. This is the default.  
`TEXT` | The session is text-only.  
  
## TrafficType

The traffic type for the session. This is used to label the monitoring, logging, and observability metrics.

Enums  
---  
`TRAFFIC_TYPE_UNSPECIFIED` | The traffic type is not specified.  
`EXTERNAL` | The traffic is from an external client.  
`INTEGRATION_TEST` | The traffic is from an integration test.  
`EVAL` | The traffic is from the eval tool.  
`PROBER` | The traffic is from the prober.  
`MANUAL_TEST` | The traffic is from manual testing.  
`INTERNAL_TOOL` | The traffic is from an internal tool.  
`CONSOLE` | The traffic is from the food AI console.  
`QA` | Traffic from QA testing.  
  
## ConfigApplicationRule

A rule representing conditions for when to apply agent configurations.

Fields  
---  
`name` |  `string` Identifier. The config application rule name. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
`display_name` |  `string` Optional. Optional display name for this config application rule for user interfaces. Value is limited to 63 characters.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this config application rule was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this config application rule was last updated.  
  
## ConfigApplicationRuleRevision

A revision of a config application rule.

Fields  
---  
`name` |  `string` Identifier. The resource name of the config application rule revision. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}/revisions/{revision}  
`snapshot` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` Output only. The state of the config application rule resource at this revision.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. When the revision was created.  
`created_by` |  `string` Output only. The email of the user who recently created the resource.  
`alternate_ids[]` |  `string` Output only. Alternate IDs for this revision.  
`action` |  `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` Output only. The action that created this revision.  
  
## ConfigRuleBinding

Defines a conditional override of agent behavior.

Fields  
---  
`config_application_rule` |  `string` Required. The condition to check for whether to apply the override. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
`channel_config` |  `string` Required. The configuration to apply if the override condition is met. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
  
## CreateBrandRequest

Request message for `[MenuService.CreateBrand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateBrand)`.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of brands. Format: projects/{project}/locations/{location}  
`brand` |  `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` Required. The brand to create.  
`brand_id` |  `string` Optional. The ID to use for the brand, which will become the final component of the brand's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
## CreateChannelConfigRequest

Request message for `[MenuService.CreateChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateChannelConfig)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of channel configs. Format: projects/{project}/locations/{location}/brands/{brand}  
`channel_config` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` Required. The channel config to create.  
`channel_config_id` |  `string` Optional. The ID to use for the channel config, which will become the final component of the channel config's resource name.This value should only contain lower-case letters, numbers, and hyphens, with a 63 character maximum. The first character must be a letter, and the last character must be a letter or number.  
  
## CreateConfigApplicationRuleRequest

Request message for `[MenuService.CreateConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateConfigApplicationRule)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of config application rules. Format: projects/{project}/locations/{location}/brands/{brand}  
`config_application_rule` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` Required. The config application rule to create.  
`config_application_rule_id` |  `string` Optional. The ID to use for the config application rule, which will become the final component of the config application rule's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
## CreateDiscountRequest

Request message for `[MenuService.CreateDiscount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateDiscount)`.

Fields  
---  
`parent` |  `string` Required. The parent store, which owns this collection of discounts. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`discount_id` |  `string` Optional. The Discount ID to use for the discount, which will become the final component of the discount's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
`discount` |  `[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)` Required. The discount to create.  
  
## CreateEvaluationCaseRequest

Request message for `[MenuService.CreateEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationCase)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation cases. Format: projects/{project}/locations/{location}/brands/{brand}  
`evaluation_case` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` Required. The evaluation case to create.  
`evaluation_case_id` |  `string` Optional. The ID to use for the evaluation case, which will become the final component of the evaluation case's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
## CreateEvaluationContextRequest

Request message for `[MenuService.CreateEvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationContext)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation contexts. Format: projects/{project}/locations/{location}/brands/{brand}  
`evaluation_context` |  `[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)` Required. The evaluation context to create.  
`evaluation_context_id` |  `string` Optional. The ID to use for the evaluation context, which will become the final component of the evaluation context's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
## CreateEvaluationDatasetRequest

Request message for `[MenuService.CreateEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationDataset)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation datasets. Format: projects/{project}/locations/{location}/brands/{brand}  
`evaluation_dataset` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)` Required. The evaluation dataset to create.  
`evaluation_dataset_id` |  `string` Optional. The ID to use for the evaluation dataset, which will become the final component of the evaluation dataset's resource name.  
  
## CreateEvaluationMatcherRequest

Request message for `[MenuService.CreateEvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateEvaluationMatcher)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation matchers. Format: projects/{project}/locations/{location}/brands/{brand}  
`evaluation_matcher` |  `[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)` Required. The evaluation matcher to create.  
`evaluation_matcher_id` |  `string` Optional. The ID to use for the evaluation matcher, which will become the final component of the evaluation matcher's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
  
## CreateIngestionLogRequest

Request message for `[MenuService.CreateIngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateIngestionLog)`.

Fields  
---  
`parent` |  `string` Required. The parent resource where this ingestion log will be created. Format: projects/{project}/locations/{location}/brands/{brand}  
`ingestion_log` |  `[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)` Required. The ingestion log to create.  
`ingestion_log_id` |  `string` Required. The ID to use for the ingestion log, which will become the final component of the ingestion log's resource name.  
  
## CreateInventoryRequest

Request message for `[MenuService.CreateInventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateInventory)`.

Fields  
---  
`parent` |  `string` Required. The parent store, which owns this collection of inventories. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`inventory_id` |  `string` Optional. The Inventory ID to use for the inventory, which will become the final component of the inventory's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
`inventory` |  `[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)` Required. The inventory to create.  
  
## CreateMenuRequest

Request message for `[MenuService.CreateMenu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateMenu)`.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of menus. Format: projects/{project}/locations/{location}  
`menu_id` |  `string` Optional. The ID to use for the menu, which will become the final component of the menu's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
`menu` |  `[Menu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Menu)` Required. The menu to create.  
  
## CreateRemediationRequest

Request message for `[MenuService.CreateRemediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateRemediation)`.

Fields  
---  
`parent` |  `string` Required. The parent resource where this remediation will be created. Format: projects/{project}/locations/{location}/brands/{brand}  
`remediation_id` |  `string` Optional. The ID to use for the remediation, which will become the final component of the resource's name.  
`remediation` |  `[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)` Required. The remediation resource to create.  
  
## CreateStoreRequest

Request message for `[MenuService.CreateStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateStore)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of stores. Format: projects/{project}/locations/{location}/brands/{brand}  
`store_id` |  `string` Optional. The Store Id to use for the store, which will become the final component of the store's resource name.This value should only contain lower-case letters, numbers, and hyphen, with the first and last character a letter or a number, and a 63 character maximum.  
`store` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` Required. The store to create.  
  
## CreateWebhookSubscriptionRequest

Request message for `[MenuService.CreateWebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.CreateWebhookSubscription)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of webhook subscriptions. Format: projects/{project}/locations/{location}/brands/{brand}  
`webhook_subscription` |  `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)` Required. The webhook subscription to create.  
`webhook_subscription_id` |  `string` Optional. The ID to use for the webhook subscription, which will become the final component of the webhook subscription's resource name.This value should be 4-63 characters, and valid characters are [a-z0-9-], with the first character a letter and the last a letter or a number (RFC-1034).  
  
## DateRange

Represents a date range, inclusive of both ends.

Fields  
---  
`start_date` |  `[Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Date)` Required. The start date of the range, inclusive.  
`end_date` |  `[Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Date)` Required. The end date of the range, inclusive.  
  
## DeleteBrandRequest

Request message for `[MenuService.DeleteBrand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteBrand)`.

Fields  
---  
`name` |  `string` Required. The name of the brand to delete. Format: projects/{project}/locations/{location}/brands/{brand}  
  
## DeleteBrandRevisionRequest

Request message for `[MenuService.DeleteBrandRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteBrandRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the brand revision to delete. Format: projects/{project}/locations/{location}/brands/{brand}/revisions/{revision}  
  
## DeleteChannelConfigRequest

Request message for `[MenuService.DeleteChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteChannelConfig)`.

Fields  
---  
`name` |  `string` Required. The name of the channel config to delete. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
  
## DeleteChannelConfigRevisionRequest

Request message for `[MenuService.DeleteChannelConfigRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteChannelConfigRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the channel config revision to delete. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}/revisions/{revision}  
  
## DeleteConfigApplicationRuleRequest

Request message for `[MenuService.DeleteConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteConfigApplicationRule)`.

Fields  
---  
`name` |  `string` Required. The name of the config application rule to delete. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
  
## DeleteConfigApplicationRuleRevisionRequest

Request message for `[MenuService.DeleteConfigApplicationRuleRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteConfigApplicationRuleRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the config application rule revision to delete. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}/revisions/{revision}  
  
## DeleteDiscountRequest

Request message for `[MenuService.DeleteDiscount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteDiscount)`.

Fields  
---  
`name` |  `string` Required. The name of the discount to delete. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/discounts/{discount}  
  
## DeleteEvaluationCaseRequest

Request message for `[MenuService.DeleteEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationCase)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation case to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
  
## DeleteEvaluationCaseResultRequest

Request message for `[MenuService.DeleteEvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationCaseResult)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation case result to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluation_case_result}  
  
## DeleteEvaluationContextRequest

Request message for `[MenuService.DeleteEvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationContext)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation context to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
  
## DeleteEvaluationDatasetRequest

Request message for `[MenuService.DeleteEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationDataset)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation dataset to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
  
## DeleteEvaluationDatasetResultRequest

Request message for `[MenuService.DeleteEvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationDatasetResult)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation dataset result to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasetResults/{evaluation_dataset_result}  
  
## DeleteEvaluationMatcherRequest

Request message for `[MenuService.DeleteEvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteEvaluationMatcher)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation matcher to delete. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationMatchers/{evaluation_matcher}  
  
## DeleteIngestionLogRequest

Request message for `[MenuService.DeleteIngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteIngestionLog)`.

Fields  
---  
`name` |  `string` Required. The name of the ingestion log to delete. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestion_log}  
  
## DeleteInventoryRequest

Request message for `[MenuService.DeleteInventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteInventory)`.

Fields  
---  
`name` |  `string` Required. The name of the inventory to delete. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
  
## DeleteMenuRequest

Request message for `[MenuService.DeleteMenu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteMenu)`.

Fields  
---  
`name` |  `string` Required. The name of the menu to delete. Format: projects/{project}/locations/{location}/menus/{menu}  
  
## DeleteRemediationRequest

Request message for `[MenuService.DeleteRemediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteRemediation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the remediation to delete. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
  
## DeleteSessionRecordRequest

Request message for [SessionRecordService.DeleteSessionRecord][].

Fields  
---  
`name` |  `string` Required. The name of the session record to delete. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{session_record}  
  
## DeleteStoreRequest

Request message for `[MenuService.DeleteStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteStore)`.

Fields  
---  
`name` |  `string` Required. The name of the store to delete. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
## DeleteStoreRevisionRequest

Request message for `[MenuService.DeleteStoreRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteStoreRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the store revision to delete. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/revisions/{revision}  
  
## DeleteWebhookSubscriptionRequest

Request message for `[MenuService.DeleteWebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.DeleteWebhookSubscription)`.

Fields  
---  
`name` |  `string` Required. The name of the webhook subscription to delete. Format: projects/{project}/locations/{location}/brands/{brand}/webhookSubscriptions/{webhook_subscription}  
  
## DeliveryAddress

The delivery address of an order. It could be an existing saved or collected address.

Fields  
---  
`address` |  `[PostalAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.PostalAddress)` Optional. The delivery address.  
`validation_status` |  `[ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress.ValidationStatus)` Optional. The validation status of the address.  
`coordinates` |  `[LatLng](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.LatLng)` Optional. The geographic coordinates of the address. Used to validate if the address is within the delivery range of the store.  
  
## ValidationStatus

The validation status of the delivery address. It is determined by client-specific validation logic.

Enums  
---  
`VALIDATION_STATUS_UNSPECIFIED` | The address has not yet been validated.  
`VALIDATION_STATUS_VALID` | The address is valid.  
`VALIDATION_STATUS_INVALID` | The address is invalid (does not exist, cannot be parsed, etc.)  
`VALIDATION_STATUS_OUT_OF_RANGE` | The address exists and is resolved, but out of range for the store.  
`VALIDATION_STATUS_INCOMPLETE_ADDRESS` | The address is missing required fields (missing street number/name, city, state, zip, etc)  
  
## DiagnosticInfo

DiagnosticInfo provides strongly typed execution timing and latency metrics for a conversational turn.

Fields  
---  
`speech_start_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration relative to the start of the audio stream when user speech began.  
`speech_end_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration relative to the start of the audio stream when user speech ended.  
`perceived_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Perceived latency for the completed turn, measured from acoustic end of speech to the first synthesized audio packet dispatched to the client. Includes the 200ms VAD silence confirmation window.  
  
## DisambiguationMapping

A mapping rule to correct invalid terms or clarify ambiguous items.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationMapping.Type)` Required. The operational type of the disambiguation rule.  
`customer_terms[]` |  `string` Required. Customer utterances or shortcut strings. Each customer term is limited to 100 characters.  
`targets[]` |  `[TargetItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TargetItem)` Required. Fully structured target menu items to suggest or clarify, including nested modifiers.  
`custom_instruction` |  `string` Optional. Optional custom conditional macro instructions or phrasing hints.  
  
## Type

The operational type of the disambiguation rule.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified rule type.  
`SINGLE_TARGET` | Used for single-target mappings (shortcuts, custom combo configurations, or valid synonyms).  
`INVALID_ITEM` | Used for invalid items, out-of-stock items, or competitor products.  
`DISAMBIGUATION` | Used for ambiguous inputs requiring clarification among multiple valid target options.  
  
## DisambiguationStrategy

Strategy configuration for Disambiguation Control.

Fields  
---  
`mappings[]` |  `[DisambiguationMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationMapping)` Optional. The configured disambiguation mappings.  
  
## Discount

A discount that can be applied to orders at a store. Next ID: 16

Fields  
---  
`name` |  `string` Identifier. The discount name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/discounts/{discount}  
`display_name` |  `string` Required. The user-facing name of the discount (e.g., "20% Off Your Order").  
`type` |  `[DiscountType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiscountType)` Required. The type of discount being applied.  
`scope` |  `[Scope](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount.Scope)` Required. The scope at which the discount is applied.  
`schedule` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. The schedule when the discount is active.  
`fixed_amount` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The fixed monetary value of the discount or the fixed total price, depending on the 'type'.  
`percent` |  `float` Optional. The percentage value of the discount (0.0 to 100.0). Set when 'type' is PERCENT_OFF.  
`max_discount_value` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. If the discount type is PERCENT_OFF, we can set a max discount value user can get.  
`applied_items` |  `[ItemGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup)` Optional. The group of items the discount is applied to. Required if 'scope' is ITEM. E.g. Bundles, mix-and-match, and the GET part of BOGO are defined here.  
`required_items` |  `[ItemGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup)` Optional. The group of items that must be present in the cart to activate the discount only need to be set when discount type is BOGO. E.g. The BUY part of BOGO discount is defined here.  
`auto_apply` |  `bool` Optional. If true, the discount is automatically applied when the criteria are met.  
`promo_code` |  `string` Optional. The code required to apply the discount.  
`additional_constraint` |  `[Constraint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount.Constraint)` Optional. Additional constraint to apply this discount.  
`integration_attributes` |  `[DiscountIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DiscountIntegrationAttributes)` Optional. Metadata associated with this entity used for downstream integrations.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Optional. Image to display for this discount in the UI.  
  
## Constraint

Additional constraint to apply this discount.

Fields  
---  
`min_spend` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. Min spend in order to apply this discount.  
`max_uses_per_order` |  `int32` Optional. How many times can this discount being used per order.  
`allowed_channels[]` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Optional. Channels this discount can be applied. If not set, the discount can be applied to all channels.  
`requires_customer_signin` |  `bool` Optional. For mobile orders, if we need customer to signin to get this discount.  
`is_stackable` |  `bool` Optional. If this discount can be used with other discount.  
`allowed_fulfillment_methods[]` |  `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` Optional. Fulfillment methods this discount can be applied to. If not set, the discount can be applied to all fulfillment methods.  
  
## Scope

Defines the level at which the discount is applied.

Enums  
---  
`SCOPE_UNSPECIFIED` | Unspecified scope.  
`ORDER` | Applied to the entire order.  
`ITEM` | Applied to specific items.  
  
## DiscountIntegrationAttributes

Metadata associated with a discount used for downstream integrations.

Fields  
---  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
  
## DiscountType

The type of a discount.

Enums  
---  
`DISCOUNT_TYPE_UNSPECIFIED` | Unspecified discount type.  
`BOGO` | Buy X, Get Y Free/Z Percent Off/For Z amount.  
`FIXED_OFF` | A fixed monetary amount discount (e.g., $5.00 off an item or order).  
`PERCENT_OFF` | A percentage discount (e.g., 20% off an item or order).  
`FIXED_TOTAL` | Sets the final price of the discounted items to a fixed total (e.g., 2 items for $10.00).  
`FREE_DELIVERY` | Waives the delivery fee for the order.  
  
## DtmfInput

The DTMF (Dual-Tone Multi-Frequency) input from the client.

Represents touch-tone keypad input from telephony or client applications.

  1. Collection & Buffering: Clients may stream single digits in real time as the user presses them, or send multiple digits at once. Food AI Agent buffers incoming digits and resets caller inactivity timers.
  2. Endpointing & Termination: The sequence is finalized when an agent-configured finish digit (default is '#') is encountered, or when an endpointing silence timeout (default is 3 seconds) elapses without new digits. If a finish digit terminates a sequence, it is stripped from the digits passed to the agent unless it was the sole digit entered.
  3. Agent Response: Once finalized, Food AI Agent processes the digits and responds with standard conversational turn output (such as synthesized agent audio, POS tool calls, or text).
  4. Dynamic Control: The agent can dynamically enable or disable DTMF listening, configure the finish digit, or adjust the endpointing timeout per turn based on conversational context (for example, when prompting for a zip code or card number).

Fields  
---  
`digits` |  `string` Required. The DTMF digits entered by the user.Supported DTMF characters: '0'-'9', '*', '#', and 'A'-'D'.  
`finish_digit` |  `string` Optional. The finish digit (e.g., '#') that was used to complete the DTMF input, if any. When streaming digits in real time, clients can either send the finish digit as the last character in `digits` or specify it explicitly here.  
  
## EndSession

Indicates the agent has terminated the session, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

Fields  
---  
`type` |  `[EndType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EndSession.EndType)` The type of end session event.  
`reason` |  `string` The reason for ending the session.  
`pos_response` |  `string` Optional. The POS response from checking in the order (optional). This is an opaque string payload representing the POS transaction status.  
`agent_response` |  `string` Optional. The final agent response message to be spoken/displayed to the user (optional).  
`store_schedule` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. The store schedule. This is only set when the end type is STORE_CLOSED.  
  
## EndType

Type of end session event.

Enums  
---  
`END_TYPE_UNSPECIFIED` | The end type is not specified.  
`DRIVE_OFF` | The customer drove off.  
`AGENT_ESCALATION` | The agent escalated the session to a human agent.  
`CREW_INTERJECTION` | A crew member interjected in the session.  
`ORDER_COMPLETED` | Order was successfully completed and no further action is needed.  
`PAYMENT_FLOW_SUCCESS` | The payment flow was successful and no further action is needed.  
`PAYMENT_FLOW_FAILURE` | The payment flow failed.  
`CLIENT_ESCALATION` | The client escalated the session to a human agent.  
`CALLER_HANGUP` | The customer hung up the call prematurely.  
`REQUESTED_CHECKOUT` | The customer requested to check out.  
`REQUESTED_ORDER_STATUS` | The customer asked about their order status.  
`STORE_CLOSED` | The store is closed.  
  
## EvaluationCase

An individual evaluation case.

Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation case. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
`display_name` |  `string` Required. The human-readable name of the evaluation case.  
`description` |  `string` Optional. The description of the evaluation case.  
`evaluation_context` |  `string` Required. The resource name of the evaluation context this case is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
`evaluation_matchers[]` |  `string` Optional. The list of evaluation matchers to use for the evaluation case. The evaluation is performed once at the end of the BidiProcessOrder session. Each matcher produces a boolean result indicating whether the evaluation matcher passed or failed.  
Union field `test_case`. The test case to use for the evaluation case. `test_case` can be only one of the following:  
`static_text_turn_case` |  `[StaticTextTurnCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.StaticTextTurnCase)` Optional. A test case where the user and agent text turns are static.  
`dynamic_text_turn_case` |  `[DynamicTextTurnCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.DynamicTextTurnCase)` Optional. A test case where the user text inputs are dynamically generated using LLM with an ordering instruction.  
  
## DynamicTextTurnCase

An evaluation case where the user inputs are dynamically generated using LLM with an ordering instruction.

Fields  
---  
`ordering_instruction` |  `string` Required. The ordering instruction for the user to interact with the Food Ordering Agent. LLM dynamically generates the user text inputs based on the ordering instruction. This may include the targeted items to order, the user's preferences and constraints, and specific actions to that the user should inform the ordering agent.  
  
## StaticTextTurnCase

An evaluation case where the user inputs are static text inputs.

Fields  
---  
`text_turns[]` |  `[TextTurn](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase.StaticTextTurnCase.TextTurn)` Required. The list of text turns in the evaluation case.  
  
## TextTurn

A single text turn in the evaluation case, consisting of user input and agent response.

Fields  
---  
`user_text_input` |  `string` Required. The user text input for this turn.  
`example_agent_response` |  `string` Optional. The example agent response for this turn. Note that this is not the actual agent response. The actual agent response may differ from this example response. The example response is NOT used for evaluation, but only for display purposes to make the evaluation case easier to understand.  
  
## EvaluationCaseResult

An evaluation case result.

Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation case result. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluation_case_result}  
`evaluation_case` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` Output only. The evaluation case this result is associated with.  
`evaluation_context` |  `[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)` Output only. The evaluation context this result is associated with.  
`evaluation_dataset` |  `string` Output only. The evaluation dataset reference this result is associated with. If not set, it means the test case is run as a standalone test, not as part of an evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
`session_record` |  `string` Output only. The resource name of the session record this result is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{session_record}  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.Status)` Output only. The status of the evaluation case.  
`matcher_results[]` |  `[MatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult)` Output only. The list of evaluation matcher results for the evaluation case. The results of the evaluation matchers.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The create time of the evaluation case result.  
`labels[]` |  `string` Output only. The labels associated with the evaluation case result.  
`links[]` |  `[Hyperlink](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.Hyperlink)` Output only. The list of hyperlinks for the evaluation case result.  
  
## Hyperlink

A hyperlink to a resource.

Fields  
---  
`text` |  `string` Output only. The text to display for the hyperlink.  
`url` |  `string` Output only. The URL of the hyperlink.  
`internal_only` |  `bool` Output only. Whether the hyperlink is internal only.  
  
## MatcherResult

A result of an evaluation matcher.

Fields  
---  
`evaluation_matcher` |  `[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)` Output only. The evaluation matcher this result is associated with.  
Union field `result`. The result of the evaluation matcher. `result` can be only one of the following:  
`order_result_matcher_result` |  `[OrderResultMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.OrderResultMatcherResult)` Output only. The result of an order result matcher.  
`agent_utterance_string_matcher_result` |  `[AgentUtteranceStringMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.AgentUtteranceStringMatcherResult)` Output only. The result of an agent utterance string matcher.  
`llm_judgement_matcher_result` |  `[LLMJudgementMatcherResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult.MatcherResult.LLMJudgementMatcherResult)` Output only. The result of an agent utterance LLM judgement matcher.  
  
## AgentUtteranceStringMatcherResult

A result of an agent utterance string matcher.

Fields  
---  
`match` |  `bool` Output only. Whether the agent utterance string matcher passed or not.  
  
## LLMJudgementMatcherResult

A result of an agent utterance LLM judgement matcher.

Fields  
---  
`match` |  `bool` Output only. Whether the agent utterance LLM judgement matcher passed or not.  
`reasoning` |  `string` Output only. Describes the reasoning on why the LLM judgement matched or failed.  
  
## OrderResultMatcherResult

A result of an order result matcher.

Fields  
---  
`match` |  `bool` Output only. Whether the order result matcher passed or not.  
`difference` |  `string` Output only. The pretty printed difference between the expected order and the actual order in the order result matcher in the (-want +got) format.  
  
## Status

The status of the evaluation case.

Enums  
---  
`STATUS_UNSPECIFIED` | Invalid status.  
`PASS` | All the evaluation matchers are satisfied.  
`FAIL` | At least one of the evaluation matchers is not satisfied.  
`ERROR` | There was an error that the BidiProcessOrder session terminated unexpectedly and the evaluation could not be completed.  
  
## EvaluationContext

An evaluation context for an evaluation suite or case.

Fields  
---  
`name` |  `string` Identifier. The full resource name of the evaluation context. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
`display_name` |  `string` Required. The human-readable name of the evaluation context.  
`description` |  `string` Optional. The description of the evaluation context.  
`store` |  `string` Required. The full resource name of the store to use for the evaluation case. Format: projects/{project_id}/locations/{location}/brands/{brand_id}/stores/{store_id}  
`menu` |  `string` Optional. Optional menu to use for the evaluation context. If not provided, it will use the default menu for the store. Format: projects/{project_id}/locations/{location}/brands/{brand_id}/menus/{menu_id}  
`test_session_start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Optional injected start time of the Food Ordering session. If set, the evaluation session will assume the test session started at this time. This is for simulating ordering behavior at a specific time of day. If not set, the evaluation session will use the current time as the start time.  
`mock_client_executions[]` |  `[MockClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MockClientExecution)` Optional. Optional mocked client execution responses for client execution requests sent by the food ordering service during the evaluation session.  
`daypart_id` |  `string` Optional. Optional daypart ID to use for the evaluation context. If provided, the agent will use this daypart ID when establishing the process order configuration.  
  
## EvaluationDataset

A dataset of evaluation cases.

Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
`display_name` |  `string` Required. The human-readable name of the evaluation dataset.  
`description` |  `string` Optional. The description of the evaluation dataset.  
`evaluation_cases[]` |  `string` Optional. The list of evaluation cases references for this dataset. Each case with the following format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
`evaluation_context` |  `string` Optional. Optional evaluation context to use for the evaluation dataset. If set, this overrides the evaluation context set in the individual evaluation cases. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
  
## EvaluationDatasetResult

An evaluation dataset result.

Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation dataset result. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasetResults/{evaluation_dataset_result}  
`evaluation_dataset` |  `string` Output only. The evaluation dataset reference this result is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
`evaluation_case_results[]` |  `string` Output only. The list of evaluation case results for the evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluation_case_result}  
`evaluation_suite_report_link` |  `string` Output only. Optional URL link to the evaluation suite report.  
  
## EvaluationMatcher

An evaluation matcher.

Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation matcher.  
`display_name` |  `string` Required. The human-readable name of the evaluation matcher.  
`description` |  `string` Optional. The description of the evaluation matcher.  
Union field `matcher`. The matcher to use for the evaluation matcher. The matcher must produce a boolean result indicating whether the evaluation matcher passed or not. `matcher` can be only one of the following:  
`order_result_matcher` |  `[OrderResultMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.OrderResultMatcher)` Optional. An evaluation matcher for an order result.  
`agent_utterance_string_matcher` |  `[AgentUtteranceStringMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.AgentUtteranceStringMatcher)` Optional. An evaluation matcher for an agent utterance string.  
`llm_judgement_matcher` |  `[LLMJudgementMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher.LLMJudgementMatcher)` Optional. An evaluation matcher using LLM judgement.  
  
## AgentUtteranceStringMatcher

An evaluation matcher for an agent utterance string.

Fields  
---  
`invert` |  `bool` Optional. If true, the match condition is inverted (e.g., "does not contain" or "does not match").  
Union field `match_pattern`.`match_pattern` can be only one of the following:  
`contains` |  `string` Optional. The agent utterance should contain this substring.  
`regex` |  `string` Optional. The agent utterance should match this regex.  
  
## LLMJudgementMatcher

An evaluation matcher using LLM judgement with the following prompt: "You are a helpful assistant that helps users place food orders at a restaurant. You will be given user inputs and agent responses. Your task is to determine if the agent response satisfies the following criteria: {criteria}"

Fields  
---  
`criteria` |  `string` Required. The criteria for the LLM to consider if an agent response passes the check.  
`invert` |  `bool` Optional. If true, the match condition is inverted (e.g., "does not contain").  
  
## OrderResultMatcher

An evaluation matcher for an order result.

Fields  
---  
`expected_order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` Required. The expected order to match against. The actual order must match this expected order after normalization. The evaluation passes if all fields and quantities match. Default quantities of 1 are ignored during comparison to handle field omission consistently.  
`expected_legacy_order` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The expected legacy order state to match against. Used when the evaluation context has use_legacy_order_state set to true.  
  
## EventInput

The event input from the client. This is used to trigger specific events within the agent.

Fields  
---  
Union field `event`. Next ID: 12 The event to trigger. `event` can be only one of the following:  
`drive_off_event` |  `[DriveOffEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.DriveOffEvent)` The drive off event.  
`crew_interjection_event` |  `[CrewInterjectionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.CrewInterjectionEvent)` The crew interjection event.  
`update_order_state_event` |  `[OrderStateUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.OrderStateUpdateEvent)` A client-side update to the order state.  
`client_escalation_event` |  `[ClientEscalationEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.ClientEscalationEvent)` A client-side escalation event.  
`caller_hangup_event` |  `[CallerHangupEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.CallerHangupEvent)` Optional. A caller hangup event.  
`pos_error_input` |  `[PosErrorEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.PosErrorEvent)` Optional. A POS error event.  
`end_session_event` |  `[EndSessionEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.EndSessionEvent)` Optional. A client-initiated end session event.  
`store_change_event` |  `[StoreChangeEvent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.StoreChangeEvent)` Optional. The store change event.  
  
## CallerHangupEvent

This type has no fields.

Indicates the customer hung up the call prematurely (e.g., AI aversion).

## ClientEscalationEvent

Indicates the client is escalating the session to a human agent.

Fields  
---  
`reason` |  `string` Optional. The reason for client escalation e.g. "payment-declined", "pos-error", "integration-error" etc.  
  
## CrewInterjectionEvent

The crew interjection event. This indicates a crew member interjected in the session. Session will be closed after this event.

Fields  
---  
`mode` |  `string` Optional. The mode in which the crew member interjected, e.g. "headset", "pos".  
  
## DriveOffEvent

The drive off event. This indicates the customer drove off. Session will be closed after this event.

Fields  
---  
`reason` |  `string` Optional. The reason for drive off e.g. "order completed", "unexpected driveoff".  
  
## EndSessionEvent

Indicates the client is explicitly requesting to end the session (for example, the customer tapped a "Checkout" or "Done" button on a touch interface, rather than the agent detecting the end of the conversation). The session will be closed after this event.

Fields  
---  
`reason` |  `[Reason](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput.EndSessionEvent.Reason)` Optional. The reason the client is ending the session.  
  
## Reason

The reason the client is ending the session.

Enums  
---  
`REASON_UNSPECIFIED` | The reason is unspecified. The session is ended as a generic client-initiated request.  
`CHECKOUT` | The customer proceeded to checkout / payment.  
`CHECKOUT_COMPLETED` | The checkout is completed.  
  
## OrderStateUpdateEvent

The update order state request. This event should be sent when the order is updated on the client side, e.g. when an item is added or removed via a traditional touch interface.

Fields  
---  
`order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` Required. The updated state of the Order associated with this session.  
  
## PosErrorEvent

Point-of-Sale (POS) specific failures.

Fields  
---  
`error_messages[]` |  `string` Optional. A list of human-readable descriptions of the errors. Multiple error messages can be provided if multiple issues occur simultaneously (e.g., multiple items are out of stock) or to provide a more detailed breakdown of a single complex failure. These messages may be used by the agent to inform the customer or for logging purposes.  
`affected_item_uids[]` |  `string` Optional. Unique item UIDs generated by the Food Ordering AI Agent that caused the error. Corresponds to `UpdatedOrderState.OrderItem.uid`.  
`affected_external_ids[]` |  `string` Optional. List of external IDs (from the Menu) that caused the error. Should be equal to the actual representatives in the POS, which are usually under integration attributes in menu.proto (e.g., in `ItemIntegrationAttributes` or `ModifierIntegrationAttributes`).  
`metadata` |  `map<string, string>` Optional. Free-form metadata for debugging or brand-specific signaling. Can be used to pass brand-specific error codes or categories (e.g., {"BRAND_ERROR_CODE": "OUT_OF_STOCK"}).  
  
## StoreChangeEvent

This type has no fields.

The store change event. This indicates the client selected or switched to a different store.

## ExperimentMetadata

The metadata associated with the experiment.

Fields  
---  
`public_studies[]` |  `[ExperimentStudy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ExperimentMetadata.ExperimentStudy)` Output only. The public studies active during the session.  
  
## ExperimentStudy

The metadata associated with the study.

Fields  
---  
`study_name` |  `string` Optional. The name of the study.  
`arm_name` |  `string` Optional. The name of the experiment arm.  
  
## FeatureGate

The feature gates for the session. This is used to enable or disable features for the session.

Fields  
---  
`menu_response_enabled` |  `bool` Optional. Returns the menu data to the client in BidiProcessOrderResponse if set.  
`updated_order_state_enabled` |  `bool` Optional. If set, updated_order_state is returned instead of legacy_order_state_response.  
`enable_order_status_retrieval` |  `bool` Optional. If set, the agent will support order status retrieval.  
`enable_client_escalation_audio` |  `bool` Optional. If set, client escalation audio is synthesized and streamed on ClientEscalationEvent.  
  
## FeaturesConfig

Configurations for agent features. Feature flag list that is used to generate agent's custom instructions and tools.

Fields  
---  
`order_pickup` |  `[OrderPickup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.OrderPickup)` Optional. Order pickup feature configuration.  
`order_dine_in` |  `[OrderDineIn](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.OrderDineIn)` Optional. Order Dine-in feature configuration.  
`name_collection` |  `[NameCollection](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig.NameCollection)` Optional. Name collection feature configuration.  
  
## NameCollection

This type has no fields.

Enables agent to collect customer name during session.

## OrderDineIn

This type has no fields.

Allows customer to order food via agent for dine in

## OrderPickup

This type has no fields.

Allows customer to order food via agent for pickup.

## FetchServiceHealthRequest

Request message for `[MenuService.FetchServiceHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.FetchServiceHealth)`.

Fields  
---  
`parent` |  `string` Required. Format: locations/{location}  
`history_granularity` |  `[Granularity](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthRequest.Granularity)` Optional. Granularity of historical points. Defaults to ONE_DAY if unset.  
`lookback_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Lookback window (e.g. 7 days, 30 days). Defaults to 7 days (168h) if unset.  
`metric_names[]` |  `string` Optional. Filter by specific metric names (e.g. "foodai-service-uprate"). If empty, returns all configured health metrics for the location.  
  
## Granularity

Granularity of history points to return.

Enums  
---  
`GRANULARITY_UNSPECIFIED` | Unspecified granularity. Defaults to ONE_DAY.  
`ONE_HOUR` | 1-hour interval points.  
`ONE_DAY` | 1-day interval points.  
  
## FetchServiceHealthResponse

Response message for `[MenuService.FetchServiceHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.FetchServiceHealth)`.

Fields  
---  
`location` |  `string` The location requested, e.g. "locations/us".  
`is_stale` |  `bool` True if any metric's latest completed sample is older than 3 hours.  
`latest_interval_start` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Timestamp of the latest completed interval included in the calculation.  
`metrics[]` |  `[MetricHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse.MetricHealth)` Health metrics evaluated for this location.  
  
## MetricHealth

Health summary for a specific metric and indicator.

Fields  
---  
`metric_name` |  `string` The metric identifier, e.g. "foodai-service-uprate".  
`indicator_name` |  `string` The indicator name, e.g. "Availability".  
`compliance_percentage` |  `double` Aggregate compliance percentage over the lookback window: (total_good_count / total_count) * 100.0. Range: [0.0, 100.0].  
`total_good_count` |  `double` Total good events across complete intervals in the lookback window.  
`total_count` |  `double` Total events across complete intervals in the lookback window.  
`history_points[]` |  `[HistoryPoint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FetchServiceHealthResponse.MetricHealth.HistoryPoint)` Chronological history points over the requested lookback duration.  
  
## HistoryPoint

Unified history point (either daily or hourly based on requested granularity).

Fields  
---  
`interval_start` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Start time of the interval.  
`compliance_percentage` |  `double` Compliance percentage for this interval: (good_count / total_count) * 100.0. Range: [0.0, 100.0].  
`good_count` |  `double` Number of good events in this interval.  
`total_count` |  `double` Total number of events in this interval.  
  
## FinalizeOrderRequest

This type has no fields.

A request to finalize the order. This is typically sent by the agent when the customer indicates they are done ordering and want to pay.

## FinalizeOrderResponse

The result of finalizing the order.

Fields  
---  
`payment_flow_enabled` |  `bool` Optional. Whether to enable the payment handling flow in the agent.  
`payment_info` |  `[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PaymentInfo)` Optional. The payment information of the customer. No-op if payment_flow_enabled is false. Only `credit_card_last_four_digits` and `payment_method` should be populated here; raw cardholder or sensitive authentication data must never be included.  
`total_amount_due` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The total amount due for the order.  
`order_price_info` |  `[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPriceInfo)` Optional. The detailed price information of the order.  
  
## FulfillmentMethod

The fulfillment method of an order.

Enums  
---  
`FULFILLMENT_METHOD_UNSPECIFIED` | Unspecified fulfillment method.  
`FULFILLMENT_METHOD_DINE_IN` | An order that will be consumed by the customer in the store.  
`FULFILLMENT_METHOD_PICKUP` | An order that will be picked up by the customer at the store.  
`FULFILLMENT_METHOD_DRIVE_THRU` | An order placed in a drive thru.  
`FULFILLMENT_METHOD_DELIVERY` | An order that will be delivered to the customer.  
`FULFILLMENT_METHOD_CURBSIDE` | A curbside pickup order. The customer will park their car in a designated spot outside of the store, and the order will be brought out to them.  
  
## GetBrandRequest

Request message for `[MenuService.GetBrand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetBrand)`.

Fields  
---  
`name` |  `string` Required. The name of the brand to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}  
  
## GetBrandRevisionRequest

Request message for `[MenuService.GetBrandRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetBrandRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the brand revision to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/revisions/{revision}  
  
## GetChannelConfigRequest

Request message for `[MenuService.GetChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetChannelConfig)`.

Fields  
---  
`name` |  `string` Required. The name of the channel config to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
  
## GetChannelConfigRevisionRequest

Request message for `[MenuService.GetChannelConfigRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetChannelConfigRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the channel config revision to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}/revisions/{revision}  
  
## GetConfigApplicationRuleRequest

Request message for `[MenuService.GetConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetConfigApplicationRule)`.

Fields  
---  
`name` |  `string` Required. The name of the config application rule to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
  
## GetConfigApplicationRuleRevisionRequest

Request message for `[MenuService.GetConfigApplicationRuleRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetConfigApplicationRuleRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the config application rule revision to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}/revisions/{revision}  
  
## GetDiscountRequest

Request message for `[MenuService.GetDiscount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetDiscount)`.

Fields  
---  
`name` |  `string` Required. The name of the discount to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/discounts/{discount}  
  
## GetEvaluationCaseRequest

Request message for `[MenuService.GetEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationCase)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation case to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
  
## GetEvaluationCaseResultRequest

Request message for `[MenuService.GetEvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationCaseResult)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation case result to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluation_case_result}  
  
## GetEvaluationContextRequest

Request message for `[MenuService.GetEvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationContext)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation context to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
  
## GetEvaluationDatasetRequest

Request message for `[MenuService.GetEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationDataset)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation dataset to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
  
## GetEvaluationDatasetResultRequest

Request message for `[MenuService.GetEvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationDatasetResult)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation dataset result to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasetResults/{evaluation_dataset_result}  
  
## GetEvaluationMatcherRequest

Request message for `[MenuService.GetEvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetEvaluationMatcher)`.

Fields  
---  
`name` |  `string` Required. The name of the evaluation matcher to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationMatchers/{evaluation_matcher}  
  
## GetIngestionLogRequest

Request message for `[MenuService.GetIngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetIngestionLog)`.

Fields  
---  
`name` |  `string` Required. The name of the ingestion log to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestion_log}  
  
## GetInventoryRequest

Request message for `[MenuService.GetInventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetInventory)`.

Fields  
---  
`name` |  `string` Required. The name of the inventory to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
  
## GetMenuIssueClusterRequest

Request message for `[MenuService.GetMenuIssueCluster](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetMenuIssueCluster)`.

Fields  
---  
`name` |  `string` Required. The resource name of the menu issue cluster to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/menuIssueClusters/{menu_issue_cluster}  
`view` |  `[MenuIssueClusterView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueClusterView)` Optional. The view to return. Defaults to MENU_ISSUE_CLUSTER_VIEW_FULL.  
  
## GetMenuIssueRequest

Request message for `[MenuService.GetMenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetMenuIssue)`.

Fields  
---  
`name` |  `string` Required. The resource name of the menu issue to retrieve. Format: projects/{project}/locations/{location}/menus/{menu}/issues/{issue}  
  
## GetMenuRequest

Request message for `[MenuService.GetMenu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetMenu)`.

Fields  
---  
`name` |  `string` Required. The name of the menu to retrieve. Format: projects/{project}/locations/{location}/menus/{menu}  
  
## GetRemediationRequest

Request message for `[MenuService.GetRemediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetRemediation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the remediation to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
  
## GetSessionRecordRequest

Request message for [SessionRecordService.GetSessionRecord][].

Fields  
---  
`name` |  `string` Required. The name of the session record to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{session_record}  
  
## GetStoreRequest

Request message for `[MenuService.GetStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetStore)`.

Fields  
---  
`name` |  `string` Required. The name of the store to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
  
## GetStoreRevisionRequest

Request message for `[MenuService.GetStoreRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetStoreRevision)`.

Fields  
---  
`name` |  `string` Required. The name of the store revision to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/revisions/{revision}  
  
## GetWebhookSubscriptionRequest

Request message for `[MenuService.GetWebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.GetWebhookSubscription)`.

Fields  
---  
`name` |  `string` Required. The name of the webhook subscription to retrieve. Format: projects/{project}/locations/{location}/brands/{brand}/webhookSubscriptions/{webhook_subscription}  
  
## GreetingOffer

Upsell specific items as part of the agent welcome message.

Fields  
---  
`messages[]` |  `[OfferMessage](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OfferMessage)` Required. Greeting upsell messages to be used.  
  
## Greetings

Represents greeting messages for a specific language.

Fields  
---  
`language_code` |  `string` Optional. The language code of the greeting phrases. BCP-47 language code, such as "en-US" or "fr-CA".  
`greeting_phrases[]` |  `string` Optional. A list of greeting phrases in the specified language.  
  
## HistoryEntry

History entry for a resource revision.

Fields  
---  
`commit_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the revision was created.  
`created_by` |  `string` The user or service that created the revision.  
`revision_name` |  `string` The full resource name of the revision.  
`resource_type` |  `string` The type of the base resource (e.g., "Brand", "Store", "ChannelConfig").  
`action` |  `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` The action that created this revision.  
Union field `resource_revision`. The resource revision. `resource_revision` can be only one of the following:  
`brand` |  `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` The brand at the time of the commit.  
`store` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` The store at the time of the commit.  
`channel_config` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` The channel config at the time of the commit.  
`config_application_rule` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` The config application rule at the time of the commit.  
  
## IgnoreMenuIssueRequest

Request message for `[MenuService.IgnoreMenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.IgnoreMenuIssue)`.

Fields  
---  
`name` |  `string` Required. The resource name of the menu issue to ignore. Format: projects/{project}/locations/{location}/menus/{menu}/issues/{issue}  
  
## Image

Image to display for a menu entity.

Fields  
---  
`source_uri` |  `string` Required. The source URI of the image.  
`sources[]` |  `[ImageSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image.ImageSource)` Optional. The sources of the image with different resolutions.  
  
## ImageSource

Image uri with resolution.

Fields  
---  
`uri` |  `string` Optional. The URI of the image.  
`width` |  `int32` Optional. The width of the image.  
`height` |  `int32` Optional. The height of the image.  
  
## IngestionLog

A record of a menu ingestion run.

Fields  
---  
`name` |  `string` Identifier. The resource name of the ingestion log. Format: projects/{project}/locations/{location}/brands/{brand}/ingestionLogs/{ingestion_log}  
`store` |  `string` Optional. The resource name of the store for the ingestion. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog.State)` Output only. Data about the current state of the ingestion.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when ingestion job started.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when ingestion job finished.  
`phases[]` |  `[IngestionPhase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase)` Output only. List of phase runtimes.  
`ingestion_type` |  `[IngestionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog.IngestionType)` Optional. Immutable. The type of the ingestion run.  
  
## IngestionType

The type of the ingestion run.

Enums  
---  
`INGESTION_TYPE_UNSPECIFIED` | The ingestion type is unspecified.  
`MENU_UPDATE` | A regular menu update.  
`PRODUCT_OUTAGE_UPDATE` | A product outage update (e.g., product out of stock).  
  
## State

The status of the ingestion run.

Enums  
---  
`STATE_UNSPECIFIED` | The status is unspecified.  
`SUCCEEDED` | The ingestion was successful.  
`FAILED` | The ingestion failed.  
`PROCESSING` | The ingestion is being processed.  
  
## IngestionPhase

A phase of the ingestion run.

Fields  
---  
`phase` |  `[Phase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase.Phase)` Required. Name of the phase.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Start time of the phase.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. End time of the phase.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionPhase.State)` Optional. State of the phase. Set by the caller on append, so it's an input, not a resource state.  
`details` |  `string` Optional. Details about the phase.  
  
## Phase

Enum for the name of the phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase is unspecified.  
`READ_SOURCE_MENU` | Reading the source menu.  
`PARSE_SOURCE_MENU` | Parsing the source menu.  
`BRAND_SPECIFIC_VALIDATION` | Validating the brand specific configuration.  
`BRAND_AGNOSTIC_VALIDATION` | Validating the brand agnostic configuration.  
`CREATE_MENU` | Creating the menu.  
  
## State

The execution state of the phase.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unspecified.  
`SUCCEEDED` | The phase completed successfully.  
`FAILED` | The phase failed.  
  
## Interaction

Represents a single interaction in a turn in the conversation.

Fields  
---  
`turn_position` |  `int64` Output only. Turn position in the conversation.  
Union field `interaction`. The type of interaction. `interaction` can be only one of the following:  
`user_utterance` |  `[UserUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.UserUtterance)` User utterance.  
`agent_utterance` |  `[AgentUtterance](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.AgentUtterance)` Agent utterance.  
`resolve_order` |  `[ResolveOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrder)` ResolveOrder call performed by the agent  
`submit_order` |  `[SubmitOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.SubmitOrder)` SubmitOrder call performed by the agent  
`match_intent` |  `[MatchIntent](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntent)` MatchIntent call performed by the agent  
`client_execution` |  `[ClientExecution](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecution)` ClientExecution call performed by the agent  
`client_order_update` |  `[ClientOrderUpdate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientOrderUpdate)` Client-initiated order state update  
`suggested_options` |  `[SuggestedOptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedOptions)` Suggested options surfaced to the customer during the turn.  
  
## AgentUtterance

The agent utterance.

Fields  
---  
`text` |  `string` The text of the agent utterance.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the agent utterance occurred.  
  
## ClientExecution

The client execution interaction.

Fields  
---  
`tool_name` |  `string` The tool name for the client execution interaction.  
`input` |  `[ClientExecutionInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecutionInput)` The input for the client execution interaction.  
`output` |  `[ClientExecutionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ClientExecutionOutput)` The output for the client execution interaction.  
  
## ClientExecutionInput

The input for the client execution interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the client execution interaction input.  
  
## ClientExecutionOutput

The output for the client execution interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the client execution interaction output.  
  
## ClientOrderUpdate

Client-initiated order state update.

Fields  
---  
`order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` An order state update sent by the client.  
  
## MatchIntent

The match intent interaction.

Fields  
---  
`input` |  `[MatchIntentInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntentInput)` The input for the match intent interaction.  
`output` |  `[MatchIntentOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.MatchIntentOutput)` The output for the match intent interaction.  
  
## MatchIntentInput

The input for the match intent interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the match intent interaction input.  
  
## MatchIntentOutput

The output for the match intent interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the match intent interaction output.  
  
## ResolveOrder

The resolve order interaction.

Fields  
---  
`input` |  `[ResolveOrderInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrderInput)` The input for the resolve order action.  
`output` |  `[ResolveOrderOutput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction.ResolveOrderOutput)` The output for the resolve order action.  
  
## ResolveOrderInput

The input for the resolve order interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the resolve order interaction.  
  
## ResolveOrderOutput

The output for the resolve order interaction.

Fields  
---  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The payload for the resolve order interaction output.  
  
## SubmitOrder

This type has no fields.

The submit order interaction.

## UserUtterance

The user utterance.

Fields  
---  
`text` |  `string` The text of the user utterance.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the user utterance occurred.  
  
## InteractionMode

The interaction mode of the agent.

Enums  
---  
`INTERACTION_MODE_UNSPECIFIED` | Interaction mode is unspecified.  
`ORDER_TAKING` | The agent participates in a two-way conversation to take orders.  
`LISTEN_ONLY` | The agent only listens and does not speak.  
  
## InterruptionSignal

This type has no fields.

Indicates the agent's audio response has been interrupted (e.g. by end user barge-in). Client should stop playback immediately.

## IntervalMetrics

Represents analytics metrics for a specific time interval.

Fields  
---  
`interval` |  `[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Interval)` The start / end time reflected by these metrics.  
`total_order_count` |  `int64` Output only. The total number of orders.  
`success_order_count` |  `int64` Output only. The number of successful orders.  
`avg_order_duration_ms` |  `int64` Output only. The average order duration in ms.  
`upsell_success_rate  
**(deprecated)**` |  `double` This item is deprecated!Output only. Deprecated: Use `upsell_metrics.upsell_success_rate` instead. The upsell success rate.  
`upsell_revenue  
**(deprecated)**` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` This item is deprecated!Output only. Deprecated: Use `upsell_metrics.upsell_revenue` instead. The upsell revenue.  
`escalation_count` |  `int64` Output only. The escalation outcome group count.  
`predicted_failure_category_counts[]` |  `[PredictedFailureCategoryCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.PredictedFailureCategoryCount)` Output only. The predicted failure category counts.  
`invalid_order_count` |  `int64` Output only. The total number of invalid orders.  
`crew_escalation_count` |  `int64` Output only. The number of crew escalation orders.  
`metrics[]` |  `[MetricValue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MetricValue)` Output only. The dynamic metric values.  
`outcome_group_counts[]` |  `[OutcomeGroupCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.OutcomeGroupCount)` Output only. The outcome group counts.  
`total_session_count` |  `int64` Output only. The total number of sessions.  
`avg_turn_count` |  `double` Output only. The average number of conversation turns per session.  
`avg_agent_latency_ms` |  `double` Output only. The average agent perceived latency in milliseconds across all turns.  
`average_order_value` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The average order value across completed orders.  
`channel_metrics[]` |  `[ChannelMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IntervalMetrics.ChannelMetrics)` Output only. Metrics broken down by channel.  
`total_order_value` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The total order value across completed orders.  
`upsell_rate  
**(deprecated)**` |  `double` This item is deprecated!Output only. Deprecated: Use `upsell_metrics.upsell_rate` instead. The percentage of total orders containing at least one upsell item.  
`avg_order_value` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The average order value across completed orders.  
`upsell_metrics` |  `[UpsellMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellMetrics)` Output only. Consolidated upsell performance metrics for this interval.  
  
## ChannelMetrics

Metrics broken down by channel.

Fields  
---  
`channel` |  `string` Output only. The ordering channel (e.g. "Phone, Mobile, Drive-thru").  
`total_session_count` |  `int64` Output only. The total number of sessions for this channel.  
  
## OutcomeGroupCount

Outcome group count.

Fields  
---  
`outcome_group` |  `string` Output only. The outcome group label.  
`count` |  `int64` Output only. The count of sessions in this outcome group.  
  
## PredictedFailureCategoryCount

Predicted failure category count.

Fields  
---  
`category` |  `string` Output only. The predicted failure category.  
`count` |  `int64` Output only. The count of sessions in this category.  
  
## Inventory

An inventory resource for a store.

Fields  
---  
`name` |  `string` Identifier. The resource name of the inventory. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
`item_id` |  `string` Required. The item ID that this inventory belongs to.  
`modifier_id` |  `string` Optional. The modifier ID that this inventory belongs to.  
`pos_id` |  `string` Optional. The point of sale (POS) ID associated with this inventory.  
`quantity` |  `int32` Optional. The quantity of the item/modifier in stock.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory.Status)` Optional. The status of the inventory.  
  
## Status

Availability status of the inventory.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified status.  
`IN_STOCK` | The item/modifier is in stock.  
`OUT_OF_STOCK` | The item/modifier is out of stock.  
  
## Item

Item represents a menu entity which is valid only as a top-level item within an order. Item may represent a single food item, drink, service, promotion, or combination meal which can be modified with various choices.

Fields  
---  
`id` |  `string` Required. Identifier for this item, unique within the menu.  
`semantic_name` |  `string` Optional. Concise, human-readable name which clearly & distinctly identifies this item. Should be unique among Items in the menu.  
`display_name` |  `string` Required. Human-readable name for this item to be used on user interfaces.  
`category_ids[]` |  `string` Optional. Category of the item.  
`description` |  `string` Optional. Human-readable description.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Optional. Image to display for this item in the UI.  
`availability` |  `[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability)` Optional. Availability of the item.  
`base_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The base price of the item. This may be affected by the selected modifiers.  
`integration_attributes` |  `[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes)` Optional. Metadata associated with this entity used for downstream integrations.  
`modifier_groups[]` |  `[ModifierGroupReference](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupReference)` Optional. References to modifier groups which apply to this item.  
`modifier_constraints` |  `[ModifierConstraints](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierConstraints)` Optional. Constrains what modifiers can / must be applied to this item across referenced ModifierGroups.  
  
## ItemGroup

A collection of items from the menu, defined by selection criteria, used to specify required or applied items for a discount. Next ID: 7

Fields  
---  
`name` |  `string` Optional. Name of the item group.  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
Union field `type`. The type of item group. `type` can be only one of the following:  
`select_items` |  `[SelectItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.SelectItems)` A list of matchers. An item is considered a match if it satisfies ANY of these ItemMatcher criteria (OR logic).  
`all_of` |  `[AllOf](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.AllOf)` Represents a logical AND of sub-groups.  
`any_of` |  `[AnyOf](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup.AnyOf)` Represents a logical OR of sub-groups.  
  
## AllOf

Represents a logical AND of sub-groups.

Fields  
---  
`groups[]` |  `[ItemGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup)` Required. Sub-groups components.  
  
## AnyOf

Represents a logical OR of sub-groups.

Fields  
---  
`groups[]` |  `[ItemGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemGroup)` Required. Sub-groups components.  
  
## SelectItems

Defines a requirement to select a specific quantity of items where each item matches ANY of the provided ItemCriteria.

Fields  
---  
`matches[]` |  `[ItemMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemMatcher)` Required. Matchers for the items.  
`min_quantity` |  `int32` Optional. Minimum quantity required for a match.  
`max_quantity` |  `int32` Optional. Maximum quantity allowed for a match.  
  
## ItemIntegrationAttributes

Metadata associated with an item used for downstream integrations.

Fields  
---  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`stream_attributes  
**(deprecated)**` |  `[StreamIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.StreamIntegrationAttributes)` This item is deprecated!Optional. Represents metadata associated with this item used for Stream integration. Deprecated: StreamOrders integration is discontinued; this field is ignored.  
`toast_attributes` |  `[ToastIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.ToastIntegrationAttributes)` Optional. Represents metadata associated with this item used for Toast integration. If Toast integration isn't enabled for the store, this field is ignored.  
`external_item_id` |  `string` Optional. The external item ID.  
  
## StreamIntegrationAttributes

This item is deprecated!

Represents attributes for an Item from a Stream menu. Deprecated: StreamOrders integration is discontinued; this message is ignored.

Fields  
---  
`taxes[]` |  `[Tax](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes.StreamIntegrationAttributes.Tax)` Optional. Represents tax rates which apply to this item.  
`item_family_id` |  `string` Optional. Represents the item family that contains this item variant in Stream's menu.  
  
## Tax

Tax rate information associated with this item.

Fields  
---  
`stream_id` |  `string` Required. The ID of the tax in the Stream menu.  
`is_inclusive` |  `bool` Optional. Determines if the tax amount is already included in the item price  
`rate` |  `float` Required. The rate of the tax as a percentage.  
`display_name` |  `string` Optional. The name of the tax.  
`is_default` |  `bool` Optional. Whether the tax is the default tax.  
  
## ToastIntegrationAttributes

Represents attributes for an Item from a Toast menu.

Fields  
---  
`menu_group_guid` |  `string` Optional. Represents the menu group guid of the item in Toast's menu.  
  
## ItemMatcher

Defines the criteria for matching a single item. All specified fields are combined using AND. Next ID: 5

Fields  
---  
`item_id` |  `string` Optional. Item ID to match.  
`modifier_id` |  `string` Optional. Modifier ID to match.  
`category_id` |  `string` Optional. Category ID to match.  
`modifier_matcher` |  `[ModifierMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemMatcher.ModifierMatcher)` Optional. Defines the criteria for modifiers in order to match the Item.  
  
## ModifierMatcher

Defines the criteria for matching modifiers.

Fields  
---  
`allowed_modifier_ids[]` |  `string` Optional. Modifier id that are required in order to apply the discount.  
`min_modifiers` |  `int32` Optional. The minimum number of modifiers required for a match. If required_modifier_ids is set, will only count modifiers in the list.  
`max_modifiers` |  `int32` Optional. The maximum number of modifiers allowed for a match. If required_modifier_ids is set, will only count modifiers in the list.  
  
## ListBrandHistoryRequest

Request message for `[MenuService.ListBrandHistory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandHistory)`.

Fields  
---  
`parent` |  `string` Required. The brand to list history for. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of history entries to return.  
`page_token` |  `string` Optional. A page token, received from a previous `ListBrandHistory` call.  
`filter` |  `string` Optional. A filter expression to filter the results. Supported filters: - `user`: Filter by creator user. - `timestamp`: Filter by commit time. - `resource_type`: Filter by resource type.  
  
## ListBrandHistoryResponse

Response message for `[MenuService.ListBrandHistory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandHistory)`.

Fields  
---  
`brand_history[]` |  `[HistoryEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.HistoryEntry)` The history entries.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page.  
  
## ListBrandRevisionsRequest

Request message for `[MenuService.ListBrandRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandRevisions)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of revisions. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of revisions to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListBrandRevisions` call. Provide this to retrieve the subsequent page.  
  
## ListBrandRevisionsResponse

Response message for `[MenuService.ListBrandRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrandRevisions)`.

Fields  
---  
`brand_revisions[]` |  `[BrandRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BrandRevision)` The brand revisions from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListBrandsRequest

Request message for `[MenuService.ListBrands](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrands)`.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of brands. Format: projects/{project}/locations/{location}  
`page_size` |  `int32` Optional. The maximum number of brands to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListBrands` call. Provide this to retrieve the subsequent page.  
  
## ListBrandsResponse

Response message for `[MenuService.ListBrands](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListBrands)`.

Fields  
---  
`brands[]` |  `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` The brands from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListChannelConfigRevisionsRequest

Request message for `[MenuService.ListChannelConfigRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigRevisions)`.

Fields  
---  
`parent` |  `string` Required. The parent channel config, which owns this collection of revisions. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
`page_size` |  `int32` Optional. The maximum number of revisions to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListChannelConfigRevisions` call. Provide this to retrieve the subsequent page.  
  
## ListChannelConfigRevisionsResponse

Response message for `[MenuService.ListChannelConfigRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigRevisions)`.

Fields  
---  
`channel_config_revisions[]` |  `[ChannelConfigRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfigRevision)` The channel config revisions from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListChannelConfigsRequest

Request message for `[MenuService.ListChannelConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigs)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of channel configs. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of channel configs to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListChannelConfigs` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter expression that filters the results. The expression syntax is documented in <https://google.aip.dev/160>.The following fields are supported: - `type`Examples: - `type="AGENT_CUSTOMIZATION"`  
  
## ListChannelConfigsResponse

Response message for `[MenuService.ListChannelConfigs](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListChannelConfigs)`.

Fields  
---  
`channel_configs[]` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` The channel configs from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListConfigApplicationRuleRevisionsRequest

Request message for `[MenuService.ListConfigApplicationRuleRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRuleRevisions)`.

Fields  
---  
`parent` |  `string` Required. The parent config application rule, which owns this collection of revisions. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
`page_size` |  `int32` Optional. The maximum number of revisions to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListConfigApplicationRuleRevisions` call. Provide this to retrieve the subsequent page.  
  
## ListConfigApplicationRuleRevisionsResponse

Response message for `[MenuService.ListConfigApplicationRuleRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRuleRevisions)`.

Fields  
---  
`config_application_rule_revisions[]` |  `[ConfigApplicationRuleRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRuleRevision)` The config application rule revisions from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListConfigApplicationRulesRequest

Request message for `[MenuService.ListConfigApplicationRules](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRules)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of config application rules. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of config application rules to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListConfigApplicationRules` call. Provide this to retrieve the subsequent page.  
  
## ListConfigApplicationRulesResponse

Response message for `[MenuService.ListConfigApplicationRules](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListConfigApplicationRules)`.

Fields  
---  
`config_application_rules[]` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` The config application rules from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListDiscountsRequest

Request message for `[MenuService.ListDiscounts](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListDiscounts)`.

Fields  
---  
`parent` |  `string` Required. The parent store, which owns this collection of discounts. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`page_size` |  `int32` Optional. The maximum number of discounts to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListDiscounts` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160.  
  
## ListDiscountsResponse

Response message for `[MenuService.ListDiscounts](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListDiscounts)`.

Fields  
---  
`discounts[]` |  `[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)` The discounts from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationCaseResultsRequest

Request message for `[MenuService.ListEvaluationCaseResults](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCaseResults)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation case results. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation case results to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationCaseResults` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Only retrieve evaluation case results matching the filter. Currently only supports filtering by `evaluation_case`, e.g. `evaluation_case="projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{case_id}"`.  
  
## ListEvaluationCaseResultsResponse

Response message for `[MenuService.ListEvaluationCaseResults](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCaseResults)`.

Fields  
---  
`evaluation_case_results[]` |  `[EvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult)` The evaluation case results from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationCasesRequest

Request message for `[MenuService.ListEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCases)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation cases. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation cases to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationCases` call. Provide this to retrieve the subsequent page.  
  
## ListEvaluationCasesResponse

Response message for `[MenuService.ListEvaluationCases](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationCases)`.

Fields  
---  
`evaluation_cases[]` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` The evaluation cases from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationContextsRequest

Request message for `[MenuService.ListEvaluationContexts](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationContexts)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation contexts. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation contexts to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationContexts` call. Provide this to retrieve the subsequent page.  
  
## ListEvaluationContextsResponse

Response message for `[MenuService.ListEvaluationContexts](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationContexts)`.

Fields  
---  
`evaluation_contexts[]` |  `[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)` The evaluation contexts from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationDatasetResultsRequest

Request message for `[MenuService.ListEvaluationDatasetResults](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasetResults)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation dataset results. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation dataset results to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationDatasetResults` call. Provide this to retrieve the subsequent page.  
  
## ListEvaluationDatasetResultsResponse

Response message for `[MenuService.ListEvaluationDatasetResults](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasetResults)`.

Fields  
---  
`evaluation_dataset_results[]` |  `[EvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDatasetResult)` The evaluation dataset results from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationDatasetsRequest

Request message for `[MenuService.ListEvaluationDatasets](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasets)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation datasets. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation datasets to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationDatasets` call. Provide this to retrieve the subsequent page.  
  
## ListEvaluationDatasetsResponse

Response message for `[MenuService.ListEvaluationDatasets](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationDatasets)`.

Fields  
---  
`evaluation_datasets[]` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)` The evaluation datasets from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationMatchersRequest

Request message for `[MenuService.ListEvaluationMatchers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationMatchers)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of evaluation matchers. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of evaluation matchers to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListEvaluationMatchers` call. Provide this to retrieve the subsequent page.  
  
## ListEvaluationMatchersResponse

Response message for `[MenuService.ListEvaluationMatchers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListEvaluationMatchers)`.

Fields  
---  
`evaluation_matchers[]` |  `[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)` The evaluation matchers from the specified collection. [(google.api.field_policy).auditing = "AUDIT_SIZE"];  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListIngestionLogsRequest

Request message for `[MenuService.ListIngestionLogs](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListIngestionLogs)`.

Fields  
---  
`parent` |  `string` Required. The parent resource, which owns this collection of ingestion logs. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of ingestion logs to return. The service may return fewer than this value. If unspecified, at most 50 ingestion logs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListIngestionLogs` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListIngestionLogs` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter expression to restrict ingestion logs returned.  
  
## ListIngestionLogsResponse

Response message for `[MenuService.ListIngestionLogs](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListIngestionLogs)`.

Fields  
---  
`ingestion_logs[]` |  `[IngestionLog](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.IngestionLog)` The ingestion logs from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListInventoriesRequest

Request message for `[MenuService.ListInventories](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListInventories)`.

Fields  
---  
`parent` |  `string` Required. The parent store, which owns this collection of inventories. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`page_size` |  `int32` Optional. The maximum number of inventories to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListInventories` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160.  
  
## ListInventoriesResponse

Response message for `[MenuService.ListInventories](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListInventories)`.

Fields  
---  
`inventories[]` |  `[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)` The inventories from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListMenuIssueClustersRequest

Request message for `[MenuService.ListMenuIssueClusters](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenuIssueClusters)`.

Fields  
---  
`parent` |  `string` Required. The parent brand containing the menu issue clusters to list. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of menu issue clusters to return. The service may return fewer than this value. If unspecified, at most 50 menu issue clusters will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous `ListMenuIssueClusters` call to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression to restrict the returned menu issue clusters (e.g., by `issue_categories` or `entity_types`).  
`view` |  `[MenuIssueClusterView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueClusterView)` Optional. The view to return. Defaults to MENU_ISSUE_CLUSTER_VIEW_BASIC.  
  
## ListMenuIssueClustersResponse

Response message for `[MenuService.ListMenuIssueClusters](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenuIssueClusters)`.

Fields  
---  
`menu_issue_clusters[]` |  `[MenuIssueCluster](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssueCluster)` The list of retrieved menu issue clusters.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListMenuIssuesRequest

Request message for `[MenuService.ListMenuIssues](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenuIssues)`.

Fields  
---  
`parent` |  `string` Required. The parent menu containing the issues to list. Format: projects/{project}/locations/{location}/menus/{menu}  
`page_size` |  `int32` Optional. The maximum number of menu issues to return. The service may return fewer than this value. If unspecified, at most 50 menu issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous `ListMenuIssues` call to retrieve the subsequent page.  
`filter` |  `string` Optional. Useful for the UI to filter by State (e.g., state="OPEN") or EntityType.  
  
## ListMenuIssuesResponse

Response message for `[MenuService.ListMenuIssues](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenuIssues)`.

Fields  
---  
`menu_issues[]` |  `[MenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue)` The list of retrieved menu issues.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListMenusRequest

Request message for `[MenuService.ListMenus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenus)`.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of menus. Format: projects/{project}/locations/{location}  
`page_size` |  `int32` Optional. The maximum number of menus to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListMenus` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter expression that filters the results. The expression syntax is documented in <https://google.aip.dev/160>.The following fields are supported: - `store` \- `brand``store=projects/my-project/locations/us-central1/brands/my-brand/stores/my-store` \- `brand=projects/my-project/locations/us-central1/brands/my-brand`  
`view` |  `[MenuView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuView)` Optional. The view to return for the menus.  
  
## ListMenusResponse

Response message for `[MenuService.ListMenus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListMenus)`.

Fields  
---  
`menus[]` |  `[Menu](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Menu)` The menus from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListRemediationsRequest

Request message for `[MenuService.ListRemediations](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListRemediations)`.

Fields  
---  
`parent` |  `string` Required. The parent brand containing the remediations. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of remediations to return. The service may return fewer than this value. If unspecified, at most 50 remediations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token received from a previous `ListRemediations` call.  
`filter` |  `string` Optional. Useful for the UI to filter by State (e.g., state="ACTIVE").  
  
## ListRemediationsResponse

Response message for `[MenuService.ListRemediations](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListRemediations)`.

Fields  
---  
`remediations[]` |  `[Remediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation)` The list of retrieved remediations.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page.  
  
## ListSessionRecordsRequest

Request message for [SessionRecordService.ListSessionRecords][].

Fields  
---  
`parent` |  `string` Required. The brand to list order sessions for. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of session records to return. The service may return fewer than this value. If unspecified, at most 50 sessions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListSessionRecords` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160. This field allows filtering session records based on various attributes.Supported Filter Fields:

  * session_id (String): The ID of the session. Operators: = Example: `session_id = "session-123"`
  * store_id (String): The ID of the store. Operators: =, != Example: `store_id = "store-123"`
  * store_ids (String): A comma-separated list of store IDs. Operators: =, !=, : Example: `store_ids = "store-123,store-456"`
  * lane_id (String): The ID of the lane. Operators: =, != Example: `lane_id = "lane-1"`
  * session_start_time (Timestamp): The start time of the session. Timestamps expect an RFC-3339 formatted string (e.g. 2012-04-21T11:30:00-04:00). UTC offsets are supported Operators: =, !=,

> , >=, <, <= Example: `session_start_time >= "2025-10-01T00:00:00Z"`

  * start_time_of_day (String): The start time of day for the session in HH:MM format (24-hour). Operators: >=, <= Example: `start_time_of_day >= "09:00"`
  * end_time_of_day (String): The end time of day for the session in HH:MM format (24-hour). Operators: >=, <= Example: `end_time_of_day <= "17:00"`
  * time_zone (String): The IANA timezone name (or UTC offset) used when evaluating start_time_of_day and end_time_of_day. Defaults to UTC if unspecified. Operators: = Example: `time_zone = "America/New_York"`
  * outcome_label (String): The final outcome label of the session. Operators: =, != Example: `outcome_label = "SUCCESS"`
  * outcome_group_label (String): The group label for the session outcome. Operators: =, != Example: `outcome_group_label = "SUCCESS"`
  * predicted_failure_category (String): The predicted failure category for the session from the intervention analysis. Operators: =, != Example: `predicted_failure_category = "Menu"`
  * channel_type (String): The type of channel used for the session. Operators: =, != Example: `channel_type = "CHANNEL_TYPE_MOBILE_APP"`
  * environment (String): The execution environment of the session. Operators: =, != Example: `environment = "preprod"`
  * traffic_type (String): The traffic source type of the session. Operators: =, != Example: `traffic_type = "CONSOLE"`
  * experiment_study_name (String): The name of the experiment study. Operators: = Example: `experiment_study_name = "menu_study"`
  * experiment_arm_name (String): The name of the experiment arm. Operators: = Example: `experiment_arm_name = "treatment"`
  * agent_utterances (String): Text spoken by the agent. Operator: : (HAS token/Full Text Search) Example: `agent_utterances:"anything else"`
  * user_utterances (String): Text spoken by the user. Operator: : (HAS token/Full Text Search) Example: `user_utterances:"burger"`

Logical Operators:Conditions can be combined using `AND`, `OR`, and `NOT`. Parentheses `()` can be used to group expressions to control the order of evaluation. Example: `(user_utterances:"help" OR agent_utterances:"issue") AND store_id != "test-store"` Example: `user_utterances:"order" AND session_start_time >= "2025-10-03T00:00:00Z"`  
  
## ListSessionRecordsResponse

Response message for [SessionRecordService.ListSessionRecords][].

Fields  
---  
`session_records[]` |  `[SessionRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SessionRecord)` The list of session records.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListStoreRevisionsRequest

Request message for `[MenuService.ListStoreRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStoreRevisions)`.

Fields  
---  
`parent` |  `string` Required. The parent store, which owns this collection of revisions. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`page_size` |  `int32` Optional. The maximum number of revisions to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListStoreRevisions` call. Provide this to retrieve the subsequent page.  
  
## ListStoreRevisionsResponse

Response message for `[MenuService.ListStoreRevisions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStoreRevisions)`.

Fields  
---  
`store_revisions[]` |  `[StoreRevision](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreRevision)` The store revisions from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListStoresRequest

Request message for `[MenuService.ListStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStores)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of stores. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of menus to return. The service may return fewer than this value.  
`page_token` |  `string` Optional. A page token, received from a previous `ListMenus` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. Filter expression based on AIP-160. Allows filtering stores based on various attributes. Supported Filter Fields:

  * status (String): The status of the store. Operators: =, != Example: `status = "ACTIVE"` (enum value)
  * update_time (Timestamp): The last updated time of the store. Timestamps expect an RFC-3339 formatted string (e.g. 2012-04-21T11:30:00-04:00). UTC offsets are supported Operators: =, !=, >, >=, <, <= Example: `update_time >= "2025-10-01T00:00:00Z"`
  * tags (String): Tags associated with the store. Operator: : (HAS) Example: `tags:"store-tag"`
  * city (String): The city of the store. Operators: =, != Example: `city = "Mountain View"`
  * state (String): The state of the store address. Operators: =, != Example: `state = "CA"`

Logical Operators:Conditions can be combined using `AND`, `OR`, and `NOT`. Parentheses `()` can be used to group expressions to control the order of evaluation. Example: `status = "ACTIVE" AND state = "CA"`  
`view` |  `[StoreView](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreView)` Optional. The view to return for the stores.  
  
## ListStoresResponse

Response message for `[MenuService.ListStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListStores)`.

Fields  
---  
`stores[]` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` The stores from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListWebhookSubscriptionsRequest

Request message for `[MenuService.ListWebhookSubscriptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListWebhookSubscriptions)`.

Fields  
---  
`parent` |  `string` Required. The parent brand, which owns this collection of webhook subscriptions. Format: projects/{project}/locations/{location}/brands/{brand}  
`page_size` |  `int32` Optional. The maximum number of webhook subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 webhook subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListWebhookSubscriptions` call. Provide this to retrieve the subsequent page.  
  
## ListWebhookSubscriptionsResponse

Response message for `[MenuService.ListWebhookSubscriptions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ListWebhookSubscriptions)`.

Fields  
---  
`webhook_subscriptions[]` |  `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)` The webhook subscriptions from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## LoyaltyAmount

Represents a customer's loyalty amount.

Fields  
---  
`units` |  `int64` Required. The loyalty points.  
  
## LoyaltyInfo

Represents a customer's loyalty information.

Fields  
---  
`loyalty_amount` |  `[LoyaltyAmount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.LoyaltyAmount)` Required. The loyalty amount. This can be a loyalty balance or loyalty consumed.  
  
## Menu

Defines a menu of what can be ordered from a restaurant.

Fields  
---  
`name` |  `string` Identifier. The menu name. Format: projects/{project}/locations/{location}/menus/{menu}  
`store` |  `string` Optional. The resource name of the Store this Menu is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`display_name` |  `string` Optional. Optional, human-readable display name for this menu for user interfaces.  
`items[]` |  `[Item](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Item)` Optional. Items in this menu.  
`modifiers[]` |  `[Modifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Modifier)` Optional. Item modifiers in this menu.  
`modifier_groups[]` |  `[ModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroup)` Optional. Modifier groups in this menu.  
`categories[]` |  `[MenuCategory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuCategory)` Optional. Menu categories in this menu.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this menu was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this menu was last updated.  
`labels[]` |  `[MenuLabel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuLabel)` Optional. Labels for this menu.  
`menu_schedules[]` |  `[MenuSchedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuSchedule)` Optional. Menu schedules in this menu.  
`applied_remediations[]` |  `string` Output only. A list of Remediation resource names that were actively applied to this menu snapshot during ingestion.  
  
## MenuCategory

Defines a category containing items or modifiers. Categories are used to organize items in user interfaces and for semantic grouping for the agent's understanding.

Fields  
---  
`id` |  `string` Required. Identifier for this menu category, unique within the menu.  
`display_name` |  `string` Optional. Human-readable name for this menu category to be used on user interfaces.  
`description` |  `string` Optional. Human-readable description.  
`parent_id` |  `string` Optional. The parent menu category ID. If empty, this is a top-level category.  
  
## MenuIngestionConfig

Configuration for menu ingestion.

Fields  
---  
`availability_config` |  `[AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.AvailabilityConfig)` Optional. Configuration for menu item availability.  
`name_normalization_config` |  `[NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig)` Optional. Configuration for name normalization during menu ingestion.  
`item_building_config` |  `[ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig)` Optional. Configuration for building items during menu ingestion.  
`custom_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom configurations for brand-specific menu ingestion.  
`localized_configs[]` |  `[LocalizedConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.LocalizedConfig)` Optional. Language-specific menu ingestion configurations. Name-based configurations (e.g., name matchers, name normalization, search synonyms, category configs) for specific languages are grouped here under their respective BCP-47 language code. Duplicate language codes are not allowed.  
  
## AvailabilityConfig

Configuration for menu item availability.

Fields  
---  
`conditional_exclusions[]` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. Items that are conditionally excluded based on matching criteria.  
`modifier_only_product_ids[]` |  `string` Optional. Products that are only available in meals or combos and not directly orderable.  
  
## IngestionStoreMatcher

Matcher used to match one or multiple stores during menu ingestion time.

Fields  
---  
`store_ids[]` |  `string` Optional. Specific store IDs where the configuration applies. If not specified, applies across all stores as the default.  
  
## ItemBuildingConfig

Optional. Configuration for building items during menu ingestion.

Fields  
---  
`item_number_configs[]` |  `[ItemNumberConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig)` Optional. Rules for assigning item numbers to items.  
`modifier_group_ordering_rules[]` |  `[ModifierGroupOrderingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule)` Optional. Rules for ordering/sorting modifier groups.  
`modifier_group_replication_rules[]` |  `[ModifierGroupReplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupReplicationRule)` Optional. Rules for replicating multi-quantity modifier groups into individual slots.  
`modifier_group_naming_rules[]` |  `[ModifierGroupNamingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule)` Optional. Rules for naming modifier groups.  
`auto_bundle_config` |  `[AutoBundleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.AutoBundleConfig)` Optional. Configuration for auto-bundling combos.  
`category_configs[]` |  `[CategoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.CategoryConfig)` Optional. Configuration for the categories assigned to items.  
`search_configs[]` |  `[SearchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.SearchConfig)` Optional. Configuration for the search attributes assigned to items.  
`modifier_group_integration_attribute_configs[]` |  `[ModifierGroupIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupIntegrationAttributeConfig)` Optional. Configuration for the integration attributes assigned to modifier groups.  
`item_integration_attribute_configs[]` |  `[ItemIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemIntegrationAttributeConfig)` Optional. Configuration for the integration attributes assigned to items.  
  
## AutoBundleConfig

Configuration for auto-bundling items into combos.

Fields  
---  
`default_allow_auto_bundle` |  `bool` Optional. Whether auto-bundling is allowed by default for all combos.  
`allow_auto_bundle_item_matchers[]` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. Item matchers of combos that allow auto-bundling (overriding the default when default_allow_auto_bundle is false).  
`disallow_auto_bundle_item_matchers[]` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. Item matchers of combos that disallow auto-bundling (overriding the default when default_allow_auto_bundle is true).  
  
## CategoryConfig

Configuration for the categories assigned to items.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this category config applies.  
`category_ids[]` |  `string` Optional. The IDs of the categories to assign to the items.  
`hierarchical_categories[]` |  `string` Optional. The hierarchical categories to assign to the items.  
  
## ItemIntegrationAttributeConfig

Configuration for integration attributes assigned to items.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this item integration attribute config applies.  
`integration_attribute` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom integration attributes to assign to the matched items.  
  
## ItemNumberConfig

Configuration for assigning item/menu numbers to items.

Fields  
---  
`store_matcher` |  `[IngestionStoreMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.IngestionStoreMatcher)` Optional. Matcher for stores where these item number mappings apply. If not specified or empty, applies across all stores as the default.  
`item_number_mappings[]` |  `[ItemNumberMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ItemNumberConfig.ItemNumberMapping)` Optional. List of item matcher to item number mappings.  
  
## ItemNumberMapping

Mapping from an item matcher to its item numbers.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s).  
`item_numbers[]` |  `string` Optional. The item numbers to assign (e.g., ["1"], ["2", "2a"]).  
  
## ModifierGroupIntegrationAttributeConfig

Configuration for integration attributes assigned to modifier groups.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this modifier group integration attribute config applies.  
`modifier_group_names[]` |  `string` Optional. The names or types of the modifier groups to which this integration attribute config applies.  
`integration_attribute` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom integration attributes to assign to the matched modifier groups.  
  
## ModifierGroupNamingRule

Configuration for naming modifier groups.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this naming rule applies.  
`naming_strategy` |  `[NamingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupNamingRule.NamingStrategy)` Optional. The naming strategy to apply to modifier groups of the matched items.  
  
## NamingStrategy

Strategy for naming modifier groups.

Enums  
---  
`NAMING_STRATEGY_UNSPECIFIED` | Unspecified naming strategy.  
`CATEGORY_NAME` | Name modifier groups using the category or modifier group type (e.g., Entree, Side, Drink).  
`CHOICE_GROUP_NAME` | Name modifier groups using the choice group name from the source POS/catalog.  
  
## ModifierGroupOrderingRule

Configuration for ordering/sorting modifier groups.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this ordering rule applies.  
`sort_strategy` |  `[SortStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig.ModifierGroupOrderingRule.SortStrategy)` Optional. The sorting strategy to apply to modifier groups.  
`priority_list[]` |  `string` Optional. Ordered list of terms (e.g. keywords, modifier group names, or types) used when sort_strategy is PRIORITY_LIST. Modifier groups matching earlier terms in the list are sorted first.  
  
## SortStrategy

Strategy for sorting modifier groups.

Enums  
---  
`SORT_STRATEGY_UNSPECIFIED` | Unspecified sorting strategy.  
`ALPHABETICAL` | Sort modifier groups alphabetically by display name.  
`PRIORITY_LIST` | Sort modifier groups by priority list.  
  
## ModifierGroupReplicationRule

Configuration for replicating/expanding multi-quantity modifier groups into individual single-quantity slots (e.g., expanding a 2-drink choice into Drink 1 and Drink 2).

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this replication rule applies.  
`modifier_group_types[]` |  `string` Optional. Modifier group types or names to replicate (e.g., "Side", "Drink", "Entree"). If not specified, applies to all modifier groups of the matched items.  
`enabled` |  `bool` Optional. Whether replication is enabled for the matched items and modifier groups. Defaults to true.  
  
## SearchConfig

Configuration for the search attributes assigned to items.

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s) to which this search config applies.  
`synonyms[]` |  `string` Optional. The synonyms to assign to the items.  
`child_synonyms[]` |  `[ChildSynonym](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChildSynonym)` Optional. The child synonyms to assign to the items.  
  
## LocalizedConfig

High-level localized configuration for menu ingestion. Groups name-based configurations (e.g. name normalization rules, search synonyms, category configs, name matchers) that belong to a specific language.

Fields  
---  
`language_code` |  `string` Required. The BCP-47 language code for this configuration (e.g., `en`, `es`, `ja`, `en-US`, `es-MX`).  
`name_normalization_config` |  `[NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig)` Optional. Configuration for name normalization for this language.  
`item_building_config` |  `[ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ItemBuildingConfig)` Optional. Configuration for building items specific to this language (e.g., language-specific search synonyms, category configs, modifier group ordering rules).  
`availability_config` |  `[AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.AvailabilityConfig)` Optional. Language-specific availability rules (e.g. conditional exclusions matching localized product names).  
`custom_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Language-specific custom configurations.  
  
## NameNormalizationConfig

Configuration for name normalization during menu ingestion.

Fields  
---  
`product_name_overrides[]` |  `[ProductNameOverride](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig.ProductNameOverride)` Optional. Overrides product names for matched item(s).  
`regex_replacements[]` |  `[RegexReplacement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.NameNormalizationConfig.RegexReplacement)` Optional. Ordered list of regular expression replacements applied to normalize item names.  
`casing_exceptions[]` |  `string` Optional. Words or tokens whose casing should be preserved during title casing.  
  
## ProductNameOverride

A rule for overriding a product name for matched item(s).

Fields  
---  
`product_matcher` |  `[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIngestionConfig.ProductMatcher)` Optional. The product matcher to identify the item(s).  
`target_name` |  `string` Required. Target product name to use when matched.  
  
## RegexReplacement

A regular expression replacement rule.

Fields  
---  
`pattern` |  `string` Required. The regular expression pattern to match.  
`replacement` |  `string` Optional. The string to replace matches with. If omitted, matches are replaced with an empty string.  
  
## ProductMatcher

Matcher used to match one or multiple menu entities like items/modifierGroup/modifiers during menu ingestion time.

Fields  
---  
`product_ids[]` |  `string` Optional. The product IDs to match.  
`product_exact_names[]` |  `string` Optional. The exact product names to match.  
`product_regex_name` |  `string` Optional. A regular expression to match product names.  
`product_type` |  `string` Optional. The product type to match.  
`parent_product_type` |  `string` Optional. The parent product type under which the product is matched.  
`daypart_id` |  `string` Optional. The daypart during which the match applies.  
`existing_product_id` |  `string` Optional. The product ID that must exist for the match to trigger.  
`parent_product_id` |  `string` Optional. The parent product ID under which the product is matched (e.g. only match a modifier when it is offered on a specific item).  
  
## MenuIssue

Represents a detected problem in a menu during an audit.

Fields  
---  
`name` |  `string` Identifier. The resource name of the MenuIssue. Format: projects/{project}/locations/{location}/menus/{menu}/issues/{issue}  
`entity_id` |  `string` Output only. The ID of the affected entity.  
`entity_display_name` |  `string` Output only. Human-readable name of the affected entity to simplify UI rendering.  
`entity_type` |  `[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.EntityType)` Output only. The type of the affected entity.  
`issue_category` |  `string` Output only. The category of the issue (e.g. STRANGE_ITEM etc).  
`explanation` |  `string` Output only. A detailed explanation of why the issue was flagged.  
`confidence_level` |  `[ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.ConfidenceLevel)` Output only. The confidence level of the detected issue.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.State)` Output only. The current resolution state of the issue.  
`suggested_remediation_actions[]` |  `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` Output only. Actions recommended to fix the issue.  
`first_detect_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the issue was first detected.  
`last_detect_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the issue was most recently detected.  
`resolve_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the issue was resolved.  
`regression_count` |  `int32` Output only. The number of times this issue has regressed after resolution.  
`audit_log_entries[]` |  `[AuditLogEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AuditLogEntry)` Output only. The audit trail of actions taken on this issue.  
  
## ConfidenceLevel

Indicates certainty to help reviewers prioritize which issues to audit first.

Enums  
---  
`CONFIDENCE_LEVEL_UNSPECIFIED` | Unspecified confidence level.  
`LOW` | Low confidence in the flagged issue.  
`MEDIUM` | Medium confidence in the flagged issue.  
`HIGH` | High confidence in the flagged issue.  
  
## EntityType

Defines the category of the menu entity to help route issues to the correct UI component.

Enums  
---  
`ENTITY_TYPE_UNSPECIFIED` | Unspecified entity type.  
`ITEM` | Indicates the issue affects a standard menu item.  
`MODIFIER` | Indicates the issue affects a modifier.  
`MENU` | Indicates the issue affects the overall menu structure.  
  
## State

The current resolution state of the issue.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified issue state.  
`OPEN` | The issue is active and requires triage.  
`AUTO_RESOLVED` | The issue was resolved automatically by the system due to high confidence.  
`MANUALLY_RESOLVED` | The issue was manually reviewed and resolved by a human operator.  
`CLOSED_WONT_FIX` | The issue was intentionally ignored and should not trigger alerts.  
`REGRESSED` | The issue reappeared in the menu data after being previously resolved.  
  
## MenuIssueCluster

Represents a brand-level root-cause cluster of menu issues aggregated across one or more stores.

Fields  
---  
`name` |  `string` Identifier. The resource name of the menu issue cluster. Format: projects/{project}/locations/{location}/brands/{brand}/menuIssueClusters/{menu_issue_cluster}  
`title` |  `string` Output only. A concise, human-readable title summarizing the shared root cause of the cluster.  
`description` |  `string` Output only. A detailed explanation of the shared root cause across all issues in the cluster.  
`action_plan` |  `string` Output only. A free-text summary of the recommended operator action plan to resolve the shared root cause. Entity-specific remediation actions are available on `entity_issues`.  
`issue_categories[]` |  `string` Output only. Issue categories present in this cluster (e.g. MISSING_CATEGORY, MODIFIER_AS_PRIMARY_ITEM).  
`entity_types[]` |  `[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.EntityType)` Output only. Entity types present in this cluster.  
`affected_store_count` |  `int32` Output only. The number of stores in the brand affected by this cluster.  
`affected_entity_count` |  `int32` Output only. The number of unique menu entities affected in this cluster.  
`total_issue_count` |  `int32` Output only. The total number of store-level menu issues grouped into this cluster.  
`entity_issues[]` |  `[ClusteredEntityIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClusteredEntityIssue)` Output only. The entity issues in this cluster, each with its own remediation actions. Only returned in MENU_ISSUE_CLUSTER_VIEW_FULL.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this cluster was created.  
  
## MenuIssueClusterView

Specifies which fields of a MenuIssueCluster are returned.

Enums  
---  
`MENU_ISSUE_CLUSTER_VIEW_UNSPECIFIED` | The default view, which depends on the method: FULL for `GetMenuIssueCluster` and BASIC for `ListMenuIssueClusters`.  
`MENU_ISSUE_CLUSTER_VIEW_BASIC` | Returns all fields except `entity_issues`.  
`MENU_ISSUE_CLUSTER_VIEW_FULL` | Returns all fields, including `entity_issues`.  
  
## MenuLabel

String labels for describing a menu in UIs.

Fields  
---  
`name` |  `string` Required. Name for the label.  
  
## MenuSchedule

Defines the menu schedule for items and modifiers.

Fields  
---  
`id` |  `string` Optional. The schedule id, for instance "BREAKFAST", "LUNCH", etc.  
`schedules[]` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. Schedule active hours.  
`display_name` |  `string` Optional. Specifies an optional display name for this schedule.  
  
## MenuView

Specifies the level of detail to return for menus.

Enums  
---  
`MENU_VIEW_UNSPECIFIED` | The default / unset value. The API will default to the FULL view.  
`MENU_VIEW_BASIC` | Include basic metadata about the menu.  
`MENU_VIEW_NAME_ONLY` | Only include the name of the menu  
`MENU_VIEW_FULL` | Include everything. This is the default value.  
  
## MessageConfig

Language-specific message to use for an upsell.

Fields  
---  
`language_code` |  `string` Required. Code of the language to use for this message. BCP-47 language code, such as "en-US" or "fr-CA".  
`message_text` |  `string` Required. Language-specific message text.  
  
## MetricMetadata

Represents analytics metrics for a specific time interval. Represents the display metadata for a metric.

Fields  
---  
`metric_id` |  `string` e.g. "automation_rate", must be unique across metrics  
`display_name` |  `string` User-friendly display name.  
`description` |  `string` Description of what the metric calculates.  
`unit` |  `string` Display unit (e.g. "%", "$", "s", "count").  
`display_group` |  `string` Group name for categorization in UI.  
`display_order` |  `int32` Display order order in dashboards.  
`target_threshold` |  `double` The target performance threshold.  
  
## MetricValue

Represents a single dynamic metric value.

Fields  
---  
`metric_id` |  `string` Unique system identifier (e.g. "automation_rate").  
`value` |  `double` Calculated value for the metric.  
`previous_value` |  `double` Value of this metric in the previous comparison period.  
  
## MockClientExecution

Represents a mocked client execution request and response pair. If the requests sent by the food ordering service in an eval run matches the mock request, the mock response will be returned to the service. Note the request.execution_id will be ignored during matching since it's session specific.

Fields  
---  
`raw_json_request` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The request for the mock client execution.  
`raw_json_response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The response for the mock client execution.  
  
## Modifier

Defines modifying options made within for items or other modifiers, via relationships defined by ModifierGroup.

Fields  
---  
`id` |  `string` Required. Identifier for this modifier, unique within the menu.  
`display_name` |  `string` Required. Human-readable name for this item to be used on user interfaces.  
`description` |  `string` Optional. Human-readable description.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Optional. Image to display for this item in the UI.  
`semantic_name` |  `string` Optional. Concise, human-readable name which clearly & distinctly identifies this modifier. Should be unique among Modifiers in ModifierGroups where this Modifier exists.  
`category_ids[]` |  `string` Optional. Category of the modifier.  
`availability` |  `[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Availability)` Optional. Availability for this modifier.  
`price_adjustment` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. An additive adjustment applied to the top-level item's price when this modifier is selected. Leave empty if the modifier does not affect the price.  
`integration_attributes` |  `[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes)` Optional. Metadata associated with this entity used for downstream integrations.  
`modifier_groups[]` |  `[ModifierGroupReference](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupReference)` Optional. References to modifier groups which apply to this modifier.  
`modifier_constraints` |  `[ModifierConstraints](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierConstraints)` Optional. Constrains what modifiers can / must be applied to this modifier across referenced ModifierGroups.  
  
## ModifierAction

Defines an action that can be taken on modifiers.

Fields  
---  
`name` |  `string` Required. The modifier action name -- e.g. "NO", "SIDE", "ADD", "EXTRA".  
  
## ModifierConstraints

Constrains what modifiers can or must be applied to an entity across referenced ModifierGroups.

Fields  
---  
`min_quantity` |  `int32` Optional. The minimum number of modifiers that must be applied across directly referenced ModifierGroups. If not specified, no minimum is enforced.  
`max_quantity` |  `int32` Optional. The maximum number of modifiers that may be applied across directly referenced ModifierGroups. If not specified, no maximum is enforced.  
  
## ModifierGroup

Defines a group of modifiers from which selections can be made.

Fields  
---  
`id` |  `string` Required. Identifier for this modifier group, unique within its menu.  
`display_name` |  `string` Required. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Medium Combo".  
`semantic_name` |  `string` Optional. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Combo".  
`modifier_ids[]` |  `string` Required. The modifier IDs that are part of this group.  
`modifier_actions[]` |  `[ModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierAction)` Optional. The actions that can be taken on the modifiers in this group.  
`min_selection_count` |  `int32` Optional. The minimum count of modifiers from the referenced group that must be selected in order for the Item to be valid. If not set, there is no minimum. For a group where exactly one selection is required, this should be 1.  
`max_selection_count` |  `int32` Optional. The maximum count of total modifiers from the referenced group that may be selected. If not set, there is no maximum. For a group where exactly one selection is required, this should be 1.  
`max_selection_count_per_modifier` |  `int32` Optional. Limits the number of times each modifier can be applied within this group. If not set, the default is 1.  
`max_unique_selection_count` |  `int32` Optional. The maximum count of distinct modifiers from this group that may be selected with a positive quantity. If not set, there is no maximum.  
`free_selection_count` |  `int32` Optional. The number of modifier unit selections from this group that are included at no additional charge before per-modifier price adjustments apply. If not set, no units are free.  
`integration_attributes` |  `[ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupIntegrationAttributes)` Optional. Metadata associated with this entity used for downstream integrations.  
  
## ModifierGroupIntegrationAttributes

Metadata associated with a modifier group used for downstream integrations.

Fields  
---  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`toast_attributes` |  `[ToastModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupIntegrationAttributes.ToastModifierGroupIntegrationAttributes)` Optional. Represents metadata associated with this modifier group used for Toast integration. If Toast integration isn't enabled for the store, this field is ignored.  
`external_modifier_group_id` |  `string` Optional. The external modifier group ID.  
  
## ToastModifierGroupIntegrationAttributes

Represents attributes for a ModifierGroup from a Toast menu.

Fields  
---  
`guid` |  `string` Optional. Represents the menu group guid of the item in Toast's menu.  
`is_pre_modifier_group` |  `bool` Optional. If true, this modifier group represents a Toast PreModifierGroup.  
  
## ModifierGroupReference

A reference to a modifier group.

Fields  
---  
`id` |  `string` Required. The modifier group ID.  
`default_modifiers[]` |  `[DefaultModifierSelection](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupReference.DefaultModifierSelection)` Optional. The set of modifiers that are applied by default.  
`min_selection_count` |  `int32` Optional. The minimum count of modifiers from the referenced ModifierGroup which must be selected. If this value is set on both the ModifierGroupReference and the ModifierGroup, both constraints are enforced. If not set, there is no minimum.  
`max_selection_count` |  `int32` Optional. The maximum count of total modifiers from the referenced group that may be selected. If this value is set on both the ModifierGroupReference and the ModifierGroup, both constraints are enforced. If not set, there is no maximum.  
`max_unique_selection_count` |  `int32` Optional. The maximum count of distinct modifiers from the referenced group that may be selected with a positive quantity. Overrides ModifierGroup.max_unique_selection_count when set to a value greater than 0. If not set, falls back to ModifierGroup.max_unique_selection_count.  
`free_selection_count` |  `int32` Optional. The number of modifier unit selections from the referenced group that are included at no additional charge before per-modifier price adjustments apply. Overrides ModifierGroup.free_selection_count when set to a value greater than 0. If not set, falls back to ModifierGroup.free_selection_count.  
  
## DefaultModifierSelection

Specifies the default selection of a modifier within a ModifierGroup.

Fields  
---  
`id` |  `string` Required. The modifier ID.  
`quantity` |  `int32` Optional. The quantity of this modifier to apply. If omitted, reference is treated as having a quantity of 1.  
  
## ModifierIntegrationAttributes

Metadata associated with a modifier used for downstream integrations.

Fields  
---  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`toast_attributes` |  `[ToastModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes.ToastModifierIntegrationAttributes)` Optional. Represents metadata associated with this modifier used for Toast integration. If Toast integration isn't enabled for the store, this field is ignored.  
`external_modifier_id` |  `string` Optional. The external modifier ID.  
  
## ToastModifierIntegrationAttributes

Represents attributes for a Modifier from a Toast menu.

Fields  
---  
`guid` |  `string` Optional. Represents the modifier option guid of the item in Toast's menu.  
`is_pre_modifier` |  `bool` Optional. If true, this modifier represents a Toast PreModifier.  
  
## NutritionalInfo

Nutritional information for an item or modifier.

Fields  
---  
`calories` |  `string` Calorie count or calorie range string (e.g. "290", "250-300 Cal").  
  
## OfferMessage

Common configuration for greeting and closing offer messages.

Fields  
---  
`display_name` |  `string` Optional. Name to use for display and analytics.  
`message_frequency` |  `float` Optional. Fraction of the time to use this message. Ex: a message_frequency of 0.2 means this message will be used for 20% of sessions. If all message_frequency values are unset (0.0), each message will be used for 1/n proportion of sessions, where n is the number of OfferMessages configured for the offer type. If only some message_frequency values are set, OfferMessages with unset message_frequency values will not be used.  
`upsold_items[]` |  `string` Optional. Names of the items being upsold in this message. Set this OR upsold_item_ids, but not both.  
`message_configs[]` |  `[MessageConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MessageConfig)` Required. Per-language upsell messages.  
`upsold_item_ids[]` |  `string` Optional. IDs of the items being upsold in this message. Set this OR upsold_items, but not both.  
  
## OperationsConfig

Configurations for defining an operational strategy.

Fields  
---  
`display_name` |  `string` Optional. The name of this operational strategy.  
`description` |  `string` Optional. A description of this operational strategy.  
`upsell_strategy` |  `[UpsellStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellStrategy)` Optional. Configuration for upsell behavior.  
`greetings[]` |  `[Greetings](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Greetings)` Optional. Customized greeting messages to use (per language).  
`default_language_code` |  `string` Optional. Default language to use for serving customers.  
`features_config` |  `[FeaturesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FeaturesConfig)` Optional. Agent features configuration.  
`interaction_mode` |  `[InteractionMode](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.InteractionMode)` Optional. The interaction mode of the agent.  
`disambiguation_strategy` |  `[DisambiguationStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DisambiguationStrategy)` Optional. Strategy configuration for Disambiguation Control.  
`order_limits` |  `[OrderLimits](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderLimits)` Optional. Limits applied to orders for this channel configuration, e.g. max items and max order total.  
  
## Order

Order represents the content of a user's in-progress or completed order.

Fields  
---  
`items[]` |  `[OrderItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderItem)` Optional. The items in the order.  
`metadata` |  `[OrderMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderMetadata)` Optional. Other metadata collected or inferred during the order.  
`fulfillment` |  `[OrderFulfillment](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderFulfillment)` Optional. The fulfillment information for the order.  
`price_info` |  `[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPriceInfo)` Optional. Price information for the order.  
`external_order_id` |  `string` Output only. The external identifier for this order. Populated only if a point-of-sale integration is enabled.  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. Arbitrary metadata associated with the order, used for downstream custom integrations. For example, it can be converted into the payload expected by a point-of-sale (POS) system or a web/mobile client to sync the cart or submit the order. Populated by brand-specific hooks.  
  
## OrderFulfillment

OrderFulfillment contains information about order fulfillment.

Fields  
---  
`fulfillment_method` |  `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` Optional. The fulfillment method of the order.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the order was created at.  
`target_fulfillment_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The time the order is scheduled for fulfillment, used for 'order ahead'. If not provided, the order is assumed to be for 'as soon as possible'.  
  
## OrderItem

OrderItem specifies the state of an Item which is part of an Order.

Fields  
---  
`uid` |  `string` Optional. A system-assigned unique identifier for this item.  
`item_id` |  `string` Required. Identifier for an Item in the Menu, unique within its Menu.  
`display_name` |  `string` Output only. Human-readable name for this line item to be shown on user interfaces.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Output only. Image to display for this item in the UI.  
`base_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The base price of the item. This may be affected by the selected modifiers. This is the price per unit of the item.  
`integration_attributes` |  `[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifier_groups[]` |  `[OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifierGroup)` Optional. ModifierGroups applied to this item.  
`quantity` |  `int32` Optional. The quantity of this item in the order.  
`total_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The total price for this line item, inclusive of selected modifiers and reflecting the item quantity, before tax. Used for per-item bag display.  
`category_ids[]` |  `string` Output only. Category IDs the underlying menu item belongs to. Mirrors the menu's Item.category_ids so clients can group ordered items by menu category.  
`is_pending` |  `bool` Output only. Indicates if the item is in a pending state.  
  
## OrderLimits

Limits applied to orders, e.g. max items and max order total.

Fields  
---  
`order_item_limit` |  `int32` Optional. Max number of items allowed in an order.  
`order_value_limit` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. Max order total allowed. Currency is hardcoded to USD for now.  
  
## OrderMetadata

OrderMetadata contains other metadata collected or inferred during the order.

Fields  
---  
`collected_customer_name` |  `string` Optional. Name of the customer, collected while taking the order. Only populated when the agent is configured to collect the customer's name. This may be collected verbally and could contain spelling mistakes or mistranscriptions, so care should be taken when displaying it to users, and it shouldn't be trusted as e.g. payment information.  
`caller_phone_number` |  `string` Optional. The phone number of the customer placing the order.  
`delivery_address` |  `[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress)` Optional. The delivery address, if the order is a delivery order.  
  
## OrderModifier

OrderModifier specifies the state of a Modifier which is part of an OrderModifierGroup.

Fields  
---  
`uid` |  `string` Optional. A system-assigned unique identifier for this modifier.  
`modifier_id` |  `string` Required. Identifier for this modifier, unique within the menu.  
`display_name` |  `string` Output only. The modifier display name to be shown on user interfaces.  
`price_adjustment` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The price adjustment associated with this modifier, if any. This is the price per unit of the modifier.  
`quantity` |  `int32` Optional. The quantity of this modifier action applied.  
`modifier_action` |  `[OrderModifierAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifierAction)` Optional. The modifier action applied to this modifier.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Output only. Image to display for this modifier in the UI.  
`integration_attributes` |  `[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifier_groups[]` |  `[OrderModifierGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifierGroup)` Optional. Nested modifier groups applied to this modifier.  
`is_default` |  `bool` Output only. Whether this modifier is a default selection for its modifier group. Needed so clients can compute an accurate selections diff.  
  
## OrderModifierAction

OrderModifierAction specifies the ModifierAction associated with an applied OrderModifier.

Fields  
---  
`name` |  `string` Optional. The modifier action name -- e.g. "NO", "SIDE", "ADD", "EXTRA".  
  
## OrderModifierGroup

OrderModifierGroup specifies the state of a ModifierGroup which is part of an OrderItem.

Fields  
---  
`modifier_group_id` |  `string` Required. Identifier for this modifier group, unique within its menu.  
`display_name` |  `string` Output only. The modifier group name -- e.g. "Toppings (Sandwich)" or "Side for Medium Combo".  
`integration_attributes` |  `[ModifierGroupIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierGroupIntegrationAttributes)` Output only. Metadata associated with this entity used for downstream integrations.  
`modifiers[]` |  `[OrderModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderModifier)` Optional. The modifiers applied to this modifier group.  
  
## OrderPriceInfo

OrderPriceInfo encapsulates the various price components of an order.

Fields  
---  
`total_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The final total price after all taxes, fees, and discounts are applied.  
`subtotal_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The subtotal price of all items and modifiers, before taxes, discounts.  
`tax_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The amount of tax applied to the order.  
`discount` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. Total discount applied to the order  
`saving` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. Deal savings applied to the order  
`fees` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. Total fees applied to the order  
`tip` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The resolved tip amount applied to the order.  
  
## OrderPricesRequest

A request to get the order prices.

Fields  
---  
`order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` Optional. The order to get the prices for. If not specified, we can assume the request is for the existing order/cart in the session.  
  
## OrderPricesResponse

The result of getting the order prices.

Fields  
---  
`success` |  `bool` Required. Whether the order prices were successfully retrieved.  
`order_price_info` |  `[OrderPriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderPriceInfo)` Optional. Total order price after all discounts, fees, taxes, etc  
  
## OrderStatusRequest

This type has no fields.

A request to get the order status.

## OrderStatusResponse

The result of getting the order status.

Fields  
---  
`success` |  `bool` Required. Whether the order status was successfully retrieved.  
  
## OwnershipType

The ownership type of the store.

Enums  
---  
`OWNERSHIP_TYPE_UNSPECIFIED` | Unspecified ownership type.  
`CORPORATE` | A company-owned corporate store.  
`FRANCHISE` | A franchisee-owned store.  
  
## PaymentInfo

Payment information of the user.

Direction of flow and PCI scope:

  * `credit_card_last_four_digits` and `payment_method` may flow in both directions (e.g., returned in `FinalizeOrderResponse.payment_info` or passed in `Config.user_info.payment_info` to indicate a saved card on file).
  * `credit_card_cvv`, `credit_card_number`, `credit_card_expiration_month`, `credit_card_expiration_year`, and `credit_card_postal_code` are outbound-only from the Food Ordering Service to the client POS integration in `SubmitOrderRequest.payment_info` (populated deterministically from DTMF keypad callbacks without routing through the LLM). Clients must never populate these fields in `FinalizeOrderResponse.payment_info`, `Config.user_info.payment_info`, or `OrderPayment.payment_info`.

Fields  
---  
`credit_card_last_four_digits` |  `string` Optional. The last four digits of the credit card. This is used to verify the credit card number at the payment stage.  
`credit_card_cvv` |  `string` Optional. CVV of the credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`payment_method` |  `[PaymentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PaymentMethod)` Optional. The type of payment method used.  
`credit_card_number` |  `string` Optional. The credit card number (digits only, no spaces or separators; 12 to 19 digits per ISO/IEC 7812) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`credit_card_expiration_month` |  `int32` Optional. The expiration month of the credit card (1 through 12) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`credit_card_expiration_year` |  `int32` Optional. The four-digit expiration year of the credit card (e.g. 2028) when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
`credit_card_postal_code` |  `string` Optional. The billing postal/ZIP code of the credit card (e.g. "40299" or "M5V 3L9") when paying with a new credit card. Outbound-only in `SubmitOrderRequest.payment_info`; must never be populated in `FinalizeOrderResponse`, `UserInfo`, or `OrderPayment`.  
  
## PaymentMethod

The type of payment method.

Enums  
---  
`PAYMENT_METHOD_UNSPECIFIED` | Unspecified payment method.  
`PAYMENT_METHOD_CREDIT_CARD` | Credit card.  
`PAYMENT_METHOD_CASH` | Cash.  
  
## ProcessOrderRequest

Request message for `[FoodOrderingService.ProcessOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.ProcessOrder)`.

Fields  
---  
`config` |  `[Config](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config)` Required. The configuration for the session and food ordering properties.  
`turn_type` |  `[TurnType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ProcessOrderRequest.TurnType)` Optional. Explicit indicator of the request's position in the session lifecycle. Allows clients to deterministically control when initial session setup variables are injected.  
Union field `input`. The input from the client. `input` can be only one of the following:  
`text_input` |  `[TextInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TextInput)` The text input from the client.  
`audio_input` |  `[AudioInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.AudioInput)` The audio input from the client.  
`event_input` |  `[EventInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EventInput)` The event input from the client.  
`client_execution_result` |  `[ClientExecutionResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClientExecutionResult)` The result of a client execution request.  
`blob_input` |  `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Blob)` Generic binary data input.  
`dtmf_input` |  `[DtmfInput](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DtmfInput)` The DTMF input from the client.  
  
## TurnType

Represents the lifecycle position of a unary request within a session.

Enums  
---  
`TURN_TYPE_UNSPECIFIED` | Unspecified turn type.  
`INITIALIZE` | Explicitly indicates this request initializes the session in unary mode. When set, initial session variables (e.g., store metadata and menus) are injected into the session.  
`SUBSEQUENT` | Explicitly indicates a subsequent conversational turn or mid-session update. When set, initial session variables are omitted to prevent input token explosion.  
  
## ProcessOrderResponse

Response message for `[FoodOrderingService.ProcessOrder](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FoodOrderingService.ProcessOrder)`. Functionally contains fields from BidiProcessOrderResponse minus streaming-specific ones.

Fields  
---  
`responses[]` |  `[BidiProcessOrderResponse](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.BidiProcessOrderResponse)` Output only. List of agent responses to the request, returned in-order.  
  
## PromoteChannelConfigRequest

Request message for `[MenuService.PromoteChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.PromoteChannelConfig)`.

Fields  
---  
`name` |  `string` Required. The name of the channel config to promote. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
`destination_brand` |  `string` Optional. The destination brand to promote the channel config to. Format: projects/{project}/locations/{location}/brands/{brand}If `destination_brand` is provided and is different from the brand in `name`, a copy of the channel config will be created in `destination_brand`. Otherwise, no copy will be made.  
  
## PromoteChannelConfigResponse

Response message for `[MenuService.PromoteChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.PromoteChannelConfig)`.

Fields  
---  
`channel_config` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` The promoted channel config.  
  
## Remediation

Represents a persistent remediation applied to a brand.

Fields  
---  
`name` |  `string` Identifier. The resource name. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
`target_entity_id` |  `string` Required. The ID of the menu entity this remediation targets.  
`target_entity_type` |  `[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuIssue.EntityType)` Required. The type of the menu entity this remediation targets.  
`remediation_action` |  `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` Required. The underlying remediation action to be executed during ingestion.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Remediation.State)` Output only. The current state of this remediation.  
`target_stores[]` |  `string` Optional. If empty, this remediation applies to all stores within the brand. If populated, it only applies to the specific stores listed here.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this remediation was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this remediation was last updated.  
  
## State

The lifecycle state of the remediation.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The remediation is actively being applied during ingestion.  
`SUSPENDED` | The remediation is temporarily suspended.  
  
## RemediationAction

A structured action for remediation.

Fields  
---  
`action_type` |  `[ActionType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction.ActionType)` Required. The specific operation to execute.  
Union field `action_payload`. Payload containing the specific data required to execute the chosen action. `action_payload` can be only one of the following:  
`rename_payload` |  `[RenamePayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RenamePayload)` The replacement display name to use when the action type is RENAME_ENTITY.  
`update_category_payload` |  `[UpdateCategoryPayload](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdateCategoryPayload)` The target hierarchical category to use when the action type is UPDATE_CATEGORY.  
  
## ActionType

Defines the specific operation to execute against the menu ingestion pipeline.

Enums  
---  
`ACTION_TYPE_UNSPECIFIED` | Unspecified action type.  
`DISABLE_ITEM` | Disables the item entirely so customers cannot order it.  
`SET_NON_A_LA_CARTE` | Restricts the item from being sold individually while preserving modifier behavior.  
`RENAME_ENTITY` | Renames the entity to resolve ambiguous naming.  
`UPDATE_CATEGORY` | Moves the item into a new, correct category.  
  
## RenamePayload

Payload containing parameters for renaming a menu entity.

Fields  
---  
`display_name` |  `string` Optional. The replacement display name to use for the target entity.  
  
## ResolveMenuIssueRequest

Request message for `[MenuService.ResolveMenuIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ResolveMenuIssue)`.

Fields  
---  
`name` |  `string` Required. The resource name of the menu issue to resolve. Format: projects/{project}/locations/{location}/menus/{menu}/issues/{issue}  
`applied_remediation_action` |  `[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RemediationAction)` Optional. The remediation action that was taken by the client to resolve the issue.  
  
## RestartOrder

Customer requests to start over the order.

Fields  
---  
`confirmation_step` |  `bool` The agent is asking the customer to confirm the restarting request.  
  
## ResumeRemediationRequest

Request message for `[MenuService.ResumeRemediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.ResumeRemediation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the remediation to resume. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
  
## RevisionAction

The action that created a revision.

Enums  
---  
`REVISION_ACTION_UNSPECIFIED` | Unspecified action.  
`CREATE` | The revision was created because the resource was created.  
`UPDATE` | The revision was created because the resource was updated.  
  
## RunEvaluationCaseMetadata

Metadata message for `[EvaluationRunService.RunEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationCase)`.

Fields  
---  
`evaluation_case` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` Output only. The evaluation case being run.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The start time of the operation.  
`tags[]` |  `string` Output only. Tags associated with the operation for filtering and classification.  
  
## RunEvaluationCaseRequest

Request message for `[EvaluationRunService.RunEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationCase)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation case to run. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
  
## RunEvaluationCaseResponse

Response message for `[EvaluationRunService.RunEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationCase)`.

Fields  
---  
`result` |  `[EvaluationCaseResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCaseResult)` Output only. The result of the evaluation case run.  
  
## RunEvaluationDatasetMetadata

Metadata message for `[EvaluationRunService.RunEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationDataset)`.

Fields  
---  
`evaluation_dataset` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)` Output only. The evaluation dataset being run.  
`completed_cases_count` |  `int32` Output only. Number of evaluation cases that have completed execution.  
`passed_cases_count` |  `int32` Output only. Number of evaluation cases that have passed so far.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The create time of the operation.  
`completed_case_details[]` |  `[CompletedCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RunEvaluationDatasetMetadata.CompletedCase)` Output only. The cases that have completed execution.  
`tags[]` |  `string` Output only. Tags associated with the operation for filtering and classification.  
  
## CompletedCase

A case that has completed execution.

Fields  
---  
`evaluation_case` |  `string` Output only. The resource name of the evaluation case. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
`evaluation_case_result` |  `string` Output only. The resource name of the evaluation case result. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluation_case_result}  
  
## RunEvaluationDatasetRequest

Request message for `[EvaluationRunService.RunEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationDataset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation dataset to run. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
  
## RunEvaluationDatasetResponse

Response message for `[EvaluationRunService.RunEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationRunService.RunEvaluationDataset)`.

Fields  
---  
`result` |  `[EvaluationDatasetResult](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDatasetResult)` Output only. The result of the evaluation dataset run.  
  
## Schedule

A configurable schedule for one day of the week or specific date.

Fields  
---  
`days[]` |  `[DayOfWeek](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.DayOfWeek)` Optional. The days of the week to apply the schedule to.  
`date_ranges[]` |  `[DateRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DateRange)` Optional. The date ranges to apply the schedule to. If set, the schedule is only active on these specific date ranges. If both days and date_ranges are set, the schedule is active when both condition is met. For example, if days is [MONDAY] and date_ranges is [2026-01-01, 2026-01-31], the schedule is active on all Monday in January.  
`time_ranges[]` |  `[TimeOfDayRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TimeOfDayRange)` Optional. The time of day ranges to apply the schedule to. If set, the schedule is only active during these time ranges. If unset, the schedule is not limited by time of day, except in `StoreHours.schedules`, where a schedule without `time_ranges` lists days on which the store does not open.  
  
## SentimentMeasurement

The realtime sentiment score measured for this turn.

Fields  
---  
`score` |  `float` Optional. Sentiment score between -1.0 (negative sentiment) and 1.0 (positive sentiment).  
`magnitude` |  `float` Optional. Magnitude of sentiment, regardless of score.  
  
## SessionRecord

Represents a single session record.

Fields  
---  
`name` |  `string` Identifier. The resource name of the SessionRecord. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{session_record}  
`session_start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the session started.  
`store_id` |  `string` Immutable. The ID of the store where the order was placed.  
`lane_id` |  `string` Immutable. The lane ID of the order session.  
`interactions[]` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Interaction)` Output only. The conversation turns.  
`outcome_label` |  `string` Output only. The final outcome label of the order.  
`outcome_group_label` |  `string` Output only. The group label for the outcome.  
`audio_recording_path  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated: Use storage_path instead. Path to the full audio recording.  
`order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` Output only. The order associated with the session record.  
`session_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. Total duration of the session.  
`upsell_attempt_records[]` |  `[UpsellAttemptRecord](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellAttemptRecord)` Output only. Upsells performed during the session.  
`audio_recording` |  `bytes` Output only. Audio recording for the session. This field is only populated when calling GetSessionRecord.  
`traffic_type` |  `[TrafficType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Config.TrafficType)` Output only. The traffic type for the session.  
`channel_type` |  `[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelType)` Output only. The type of channel used for the session (e.g. drive-through, mobile app, phone call).  
`environment` |  `string` Output only. The execution environment of the session (e.g. prod, preprod, preprod-au).  
`experiment_metadata` |  `[ExperimentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ExperimentMetadata)` Output only. The metadata associated with the experiment.  
`menu` |  `string` Output only. The resource name of the menu active during the session. Format: `projects/{project}/locations/{location}/menus/{menu}`  
  
## SpeechRecognition

The speech recognition result from the agent.

Fields  
---  
`transcript` |  `string` Transcribed text from the audio input in the detected language.  
`language_code` |  `string` The language code of the transcript. The language code should be in BCP-47 format, such as "en-US".  
`is_final` |  `bool` Indicates whether this is the final transcript for the turn.  
  
## Store

An individual store for a brand.

Fields  
---  
`name` |  `string` Identifier. The store name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this store was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this store was last updated.  
`status` |  `[StoreStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreStatus)` Required. The status of the store.  
`time_zone` |  `[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeZone)` Required. The time zone of the store. This is used to determine which menu daypart to use for the store at a given time and for any time-based overrides.  
`store_metadata` |  `[StoreMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata)` Optional. Metadata for the store.  
`tags[]` |  `string` Optional. Tags associated with the store.  
`integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Free-form key-value pairs for brand-specific integration attributes.  
`ownership_type` |  `[OwnershipType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OwnershipType)` Optional. The ownership type of the store.  
  
## StoreHours

The operating hours of the store.

Fields  
---  
`fulfillment_method` |  `[FulfillmentMethod](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.FulfillmentMethod)` Optional. The fulfillment method of the store hours, for instance "PICKUP", "DELIVERY", etc. If unspecified, the store hours are assumed to be applicable to all fulfillment methods.  
`schedules[]` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. The operating hours for the store for the specified fulfillment_method. The store is open when any schedule with `time_ranges` is active. A schedule without `time_ranges` lists days on which the store does not open; it never makes the store open and does not override other schedules.  
  
## StoreIngestionConfig

Configuration for store ingestion.

Fields  
---  
`staging_store_ids[]` |  `string` Optional. Store IDs routed to the staging environment during ingestion.  
`test_store_ids[]` |  `string` Optional. Store IDs designated for testing during ingestion.  
`store_time_zone_configs[]` |  `[StoreTimeZoneConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreIngestionConfig.StoreTimeZoneConfig)` Optional. Time zone mappings for specific stores.  
`default_order_limits` |  `[OrderLimits](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.OrderLimits)` Optional. Default order limits applied to stores when not provided by the store data source.  
`default_schedule` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. Default operating schedule applied to stores when not provided by the store data source.  
`default_dayparts[]` |  `[Daypart](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Daypart)` Optional. Default dayparts applied to stores when not provided by the store data source.  
`custom_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom configurations for brand-specific store ingestion.  
  
## StoreTimeZoneConfig

Mapping of a time zone to specific stores.

Fields  
---  
`time_zone` |  `[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeZone)` Optional. The time zone to apply to the matched stores.  
`store_ids[]` |  `string` Optional. The store IDs that use this time zone.  
  
## StoreMetadata

Metadata for the store.

Fields  
---  
`display_name` |  `string` Optional. The display name of the store to be used in UI and customer-facing elements.  
`contact_email` |  `string` Optional. The email address of the store to be provided to customers.  
`address` |  `[Address](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Address)` Optional. The address information for the store.  
`store_hours[]` |  `[StoreHours](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreHours)` Optional. The open hours of the store.  
`dayparts[]` |  `[Daypart](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Daypart)` Optional. Dayparts defined for the store.  
`phone_number` |  `string` Optional. The main phone number of the store to take orders, ask for catering, make general inquiries, and make reservations.  
  
## Address

The address information for the store.

Fields  
---  
`street_address` |  `string` Optional. The street address of the store.  
`city` |  `string` Optional. The city of the store.  
`state` |  `string` Optional. The state of the store.  
`country` |  `string` Optional. The country of the store.  
`postal_code` |  `string` Optional. The postal code of the store.  
`latitude` |  `double` Optional. The latitude of the store.  
`longitude` |  `double` Optional. The longitude of the store.  
`google_maps_url` |  `string` Optional. The Google Maps URL for the store.  
  
## Daypart

A daypart for the store.

Fields  
---  
`id` |  `string` Optional. The day part id, for instance "BREAKFAST", "LUNCH", etc.  
`schedules[]` |  `[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Schedule)` Optional. Daypart active hours.  
`display_name` |  `string` Optional. Specifies an optional display name for this daypart.  
  
## StoreRevision

A revision of a store.

Fields  
---  
`name` |  `string` Identifier. The resource name of the store revision. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/revisions/{revision}  
`snapshot` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` Output only. The state of the store resource at this revision.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. When the revision was created.  
`created_by` |  `string` Output only. The email of the user who recently created the resource.  
`alternate_ids[]` |  `string` Output only. Alternate IDs for this revision.  
`action` |  `[RevisionAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.RevisionAction)` Output only. The action that created this revision.  
  
## StoreStatus

The status of the store.

Fields  
---  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreStatus.State)` Optional. The state of the store.  
  
## State

The status of the store.

Enums  
---  
`STATE_UNSPECIFIED` | The store is in an unspecified state.  
`ACTIVE` | The store is active.  
`DISABLED` | The store is disabled.  
  
## StoreView

Specifies the level of detail to return for stores.

Enums  
---  
`STORE_VIEW_UNSPECIFIED` | The default / unset value. The API will default to the FULL view.  
`STORE_VIEW_GEO_ONLY` | Only return the store name, latitude, and longitude. This view allows a larger page size (up to 10k).  
`STORE_VIEW_FULL` | Include everything. This is the default value.  
  
## SubmitOrderRequest

A request to submit the order, with all the required payment information collected from the customer.

Fields  
---  
`payment_info` |  `[PaymentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.PaymentInfo)` Required. The payment information for the order.  
`loyalty_info` |  `[LoyaltyInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.LoyaltyInfo)` Optional. The loyalty consumed for the order.  
`tip_amount` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Optional. The tip amount for the order.  
  
## SuggestedAction

A single action pill / chip.

Fields  
---  
`display_name` |  `string` The user-facing label rendered on the pill (e.g. "Edit Pizza", "Sign in").  
Union field `action`. The typed action triggered when the pill is tapped. `action` can be only one of the following:  
`text_input` |  `[TextInputAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TextInputAction)` Sends back the text input through the text_input event.  
  
## SuggestedActions

A collection of action pills.

Fields  
---  
`actions[]` |  `[SuggestedAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedAction)` The list of suggested actions to display as pills.  
  
## SuggestedItem

An item to suggest to the customer.

Fields  
---  
`item_id` |  `string` ID of the item in the menu.  
`display_name` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Image to display for this item in the UI.  
`base_price` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` The base price of the item. This may be affected by the selected modifiers. This is the price per unit of the item.  
`integration_attributes` |  `[ItemIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ItemIntegrationAttributes)` Metadata associated with this entity used for downstream integrations.  
`nutritional_info` |  `[NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.NutritionalInfo)` Nutritional information for this item.  
`description` |  `string` Description for this item.  
  
## SuggestedItems

A list of items to suggest to the customer.

Fields  
---  
`items[]` |  `[SuggestedItem](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedItem)` The items to suggest to the customer.  
  
## SuggestedModGroup

A modifier group to suggest to the customer.

Fields  
---  
`modifier_group_id` |  `string` ID of the modifier group in the menu.  
`display_name` |  `string` The display name of the modifier group.  
`modifiers[]` |  `[SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifier)` The modifiers in this group.  
`max_selection_count` |  `int32` The maximum number of modifiers that can be selected from this group.  
`min_selection_count` |  `int32` The minimum number of modifiers that must be selected from this group.  
`max_selection_count_per_modifier` |  `int32` Limits the number of times each modifier can be applied within this group.  
`min_selection_not_matched` |  `bool` Whether the minimum selection count is not matched.  
  
## SuggestedModifier

A modifier to suggest to the customer.

Fields  
---  
`modifier_id` |  `string` ID of the modifier in the menu.  
`modifier_group_id` |  `string` ID of the modifier group that this modifier should be added to if the suggestion is accepted.  
`modifier_group_display_name` |  `string` Display name of the modifier group that this modifier belongs to.  
`display_name` |  `string` Human-readable name for this tem to be shown on user interfaces.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Image)` Image to display for this item in the UI.  
`price_adjustment` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` The price adjustment associated with this modifier, if any. This is the price per unit of the modifier.  
`integration_attributes` |  `[ModifierIntegrationAttributes](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ModifierIntegrationAttributes)` Metadata associated with this entity used for downstream integrations.  
`already_included` |  `bool` Whether this modifier is already included in the order.  
`suggested_modifier_groups[]` |  `[SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModGroup)` The nested modifier groups suggested for this modifier.  
`nutritional_info` |  `[NutritionalInfo](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.NutritionalInfo)` Nutritional information for this modifier.  
  
## SuggestedModifierGroups

A list of modifier groups to suggest to the customer.

Fields  
---  
`modifier_groups[]` |  `[SuggestedModGroup](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModGroup)` The modifier groups to suggest to the customer.  
  
## SuggestedModifiers

A list of modifiers to suggest to the customer.

Fields  
---  
`modifiers[]` |  `[SuggestedModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifier)` The modifiers to suggest to the customer.  
`parent_uid` |  `string` The unique identifier of the parent item/modifier to apply the modifiers to.  
  
## SuggestedOptions

Options to suggest to the customer.

Fields  
---  
`suggested_modifier_groups` |  `[SuggestedModifierGroups](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifierGroups)` A group of suggested modifiers.  
`custom_integration_attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Arbitrary metadata to be associated with an entity, used to build downstream integrations, i.e. identifiers or schema information for constructing an order for submission to a third-party point of sale API.  
`suggested_actions` |  `[SuggestedActions](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedActions)` Optional. Generic contextual action pills.  
Union field `suggested_options`. The suggested options. `suggested_options` can be only one of the following:  
`suggested_items` |  `[SuggestedItems](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedItems)` A list of items to suggest to the customer.  
`suggested_modifiers` |  `[SuggestedModifiers](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedModifiers)` A list of modifiers to suggest to the customer.  
`suggested_stores` |  `[SuggestedStores](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedStores)` A list of stores to suggest to the customer.  
  
## SuggestedStore

A store to suggest to the customer.

Fields  
---  
`store  
**(deprecated)**` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` This item is deprecated!The suggested store.  
`distance` |  `double` The distance from the customer to the store in miles.  
`address` |  `[Address](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreMetadata.Address)` The address of the store.  
`store_hours[]` |  `[StoreHours](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.StoreHours)` The store hours.  
`phone_number` |  `string` The phone number of the store.  
`store_name` |  `string` The store resource name. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`open` |  `bool` Whether the store is currently open.  
`time_zone` |  `[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeZone)` The timezone of the store.  
  
## SuggestedStores

A list of stores to suggest to the customer.

Fields  
---  
`stores[]` |  `[SuggestedStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.SuggestedStore)` The stores to suggest to the customer.  
  
## SuspendRemediationRequest

Request message for `[MenuService.SuspendRemediation](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.SuspendRemediation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the remediation to suspend. Format: projects/{project}/locations/{location}/brands/{brand}/remediations/{remediation}  
  
## TargetItem

A structured item alternative target.

Fields  
---  
`item_name` |  `string` Required. The item name in the menu catalog.  
`modifiers[]` |  `[TargetModifier](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.TargetModifier)` Optional. Structured modifiers to attach to this target.  
`item_id` |  `string` Optional. The unique ID of the item in the menu catalog (linking directly to menu.proto).  
  
## TargetModifier

A structured modifier to apply to the target item.

Fields  
---  
`modifier_name` |  `string` Required. The modifier name matching the catalog entry directly.  
`modifier_group_name` |  `string` Optional. Optional modifier group name to bind the modifier.  
`modifier_id` |  `string` Optional. The unique ID of the modifier in the menu catalog (linking directly to menu.proto).  
`modifier_group_id` |  `string` Optional. The unique ID of the modifier group in the menu catalog.  
  
## TextInput

The text input from the client. Instead of audio, the client can alternatively send text input to the agent. A client must use either text or audio input, not both.

Fields  
---  
`text` |  `string` Required. The text utterance from the client.  
  
## TextInputAction

Action that sends a text query back to FoodAI via TextInput event.

Fields  
---  
`text` |  `string` For sending back the text input through text_input event.  
  
## TimeOfDayRange

Represents a period between two times of day on an unspecified date. For example, business hours like 09:00 to 17:00.

Fields  
---  
`start_time` |  `[TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeOfDay)` Required. The start of the time range, inclusive.  
`end_time` |  `[TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.TimeOfDay)` Required. The end of the time range, exclusive. If end_time is earlier than start_time, it means the endtime is on the next day.  
  
## TurnCompleted

This type has no fields.

Indicates that the Food AI agent has detected the end of the current conversation turn and will provide no further output for this turn.

## UpdateBrandRequest

Request message for `[MenuService.UpdateBrand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateBrand)`.

Fields  
---  
`brand` |  `[Brand](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Brand)` Required. The brand to update.The brand's `name` field is used to identify the brand to update. Format: projects/{project}/locations/{location}/brands/{brand}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateCategoryPayload

Payload containing parameters for updating the hierarchical category of a menu entity.

Fields  
---  
`hierarchical_category` |  `string` Optional. The new hierarchical category path to assign to the target entity.  
  
## UpdateChannelConfigRequest

Request message for `[MenuService.UpdateChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateChannelConfig)`.

Fields  
---  
`channel_config` |  `[ChannelConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ChannelConfig)` Required. The channel config to update.The channel config's `name` field is used to identify the channel config to update. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channel_config}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateConfigApplicationRuleRequest

Request message for `[MenuService.UpdateConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateConfigApplicationRule)`.

Fields  
---  
`config_application_rule` |  `[ConfigApplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ConfigApplicationRule)` Required. The config application rule to update.The config application rule's `name` field is used to identify the config application rule to update. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{config_application_rule}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateDiscountRequest

Request message for `[MenuService.UpdateDiscount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateDiscount)`.

Fields  
---  
`discount` |  `[Discount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Discount)` Required. The discount to update.The discount's `name` field is used to identify the discount to update. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/discounts/{discount}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
`allow_missing` |  `bool` Optional. If set to true, and the discount is not found, a new discount will be created. In this situation, `update_mask` is ignored.  
  
## UpdateEvaluationCaseRequest

Request message for `[MenuService.UpdateEvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationCase)`.

Fields  
---  
`evaluation_case` |  `[EvaluationCase](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationCase)` Required. The evaluation case to update.The evaluation case's `name` field is used to identify the evaluation case to update. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluation_case}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
`allow_missing` |  `bool` Optional. If set to true, and the evaluation case is not found, a new evaluation case will be created. In this situation, `update_mask` is ignored.  
  
## UpdateEvaluationContextRequest

Request message for `[MenuService.UpdateEvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationContext)`.

Fields  
---  
`evaluation_context` |  `[EvaluationContext](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationContext)` Required. The evaluation context to update.The evaluation context's `name` field is used to identify the evaluation context to update. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluation_context}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateEvaluationDatasetRequest

Request message for `[MenuService.UpdateEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationDataset)`.

Fields  
---  
`evaluation_dataset` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationDataset)` Required. The evaluation dataset to update.The evaluation dataset's `name` field is used to identify the evaluation dataset to update. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluation_dataset}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateEvaluationMatcherRequest

Request message for `[MenuService.UpdateEvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateEvaluationMatcher)`.

Fields  
---  
`evaluation_matcher` |  `[EvaluationMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.EvaluationMatcher)` Required. The evaluation matcher to update.The evaluation matcher's `name` field is used to identify the evaluation matcher to update. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationMatchers/{evaluation_matcher}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
  
## UpdateInventoryRequest

Request message for `[MenuService.UpdateInventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateInventory)`.

Fields  
---  
`inventory` |  `[Inventory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Inventory)` Required. The inventory to update.The inventory's `name` field is used to identify the inventory to update. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
`allow_missing` |  `bool` Optional. If set to true, and the inventory is not found, a new inventory will be created. In this situation, `update_mask` is ignored.  
  
## UpdateStoreRequest

Request message for `[MenuService.UpdateStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateStore)`.

Fields  
---  
`store` |  `[Store](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Store)` Required. The store to update.The store's `name` field is used to identify the store to update. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update  
`allow_missing` |  `bool` Optional. If set to true, and the store is not found, a new store will be created. In this situation, `update_mask` is ignored.  
  
## UpdateWebhookSubscriptionRequest

Request message for `[MenuService.UpdateWebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.MenuService.UpdateWebhookSubscription)`.

Fields  
---  
`webhook_subscription` |  `[WebhookSubscription](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription)` Required. The webhook subscription to update.The webhook subscription's `name` field is used to identify the webhook subscription to update. Format: projects/{project}/locations/{location}/brands/{brand}/webhookSubscriptions/{webhook_subscription}  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update.  
  
## UpdatedOrderState

Event returned by the agent representing an update to the order state.

Fields  
---  
`order` |  `[Order](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.Order)` The updated state of the Order associated with this session.  
`changed` |  `bool` Output only. Whether the order state has updates.  
`status` |  `[OrderStateUpdateStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpdatedOrderState.OrderStateUpdateStatus)` Output only. Status of the order state update.  
`detailed_message` |  `string` Output only. Detailed message if the update failed.  
  
## OrderStateUpdateStatus

Status of the order state update.

Enums  
---  
`ORDER_STATE_UPDATE_STATUS_UNSPECIFIED` | Unspecified status.  
`SUCCEEDED` | The update succeeded.  
`FAILED` | The update failed.  
  
## UpsellAttemptRecord

Represents an upsell attempt during an ordering session. This data is used to display upsell information in the console order history, namely upsell type, turn id, item names, price increase, and acceptance status.

Fields  
---  
`turn_id` |  `int32` Output only. ID of the turn in which the upsell opportunity occurred. Example: 2.  
`upsell_type` |  `string` Output only. The type or configured display name of the upsell event. Example: "COMBO", "UP_SIZE", or "Add fries".  
`accepted` |  `bool` Output only. Whether the upsell was accepted by the customer.  
`original_item_display_name` |  `string` Output only. The display name of the original item in the order that triggered the upsell. Example: "Cheeseburger".  
`target_item_display_name` |  `string` Output only. The display name of the target item offered or accepted in the upsell. Example: "French Fries" or "Cheeseburger Combo Meal".  
`price_increase` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. The additional monetary price increase for the upsold item. Example: {currency_code: "USD", units: 1, nanos: 500000000} ($1.50).  
  
## UpsellConfig

Defines the configuration for an upsell instance.

Fields  
---  
`display_name` |  `string` Optional. Name for the upsell. Is used for UI display, as well as metrics aggregation and analytics.  
`priority` |  `int32` Required. Number representing the priority ordering of the upsell configuration relative to all other UpsellConfigs within a given UpsellStrategy. Higher priority UpsellConfigs will have their upsell attempted before lower priority ones.

  * Values can be on the range [1, inf).
  * Lower values have higher priority. For example, an UpsellConfig with priority 1 in an UpsellStrategy will always be attempted first.
  * Within an UpsellStrategy, each UpsellConfig must have a uniquely-valued priority (ex: only one UpsellConfig can have a priority of 3).
  * Priority values don't necessarily have to be contiguous within an UpsellStrategy (ex: there can be UpsellConfigs with priority values: {1, 2, 5, 6, 9}). The precedence of upsell configurations is determined on a relative basis (from the previous example: 1 < 2 < 5 < 6 < 9).

  
`skip_on_multi_quantity_upsold_from_item` |  `bool` Optional. Whether to skip this upsell if the item to upsell from has a quantity > 1\. This configuration only applies to the relevant upsell types: - Item to combo - Combo up size - Modifier addition - Combo drink - Item up size - Combo variant - Item triggered  
`skip_on_previous_turn_upsell` |  `bool` Optional. Whether to skip this upsell if the prior conversational turn was an upsell.  
`disabled` |  `bool` Optional. Indicates whether the upsell type is disabled. If true, the upsell will not be attempted. This configuration is useful for disabling an upsell type as part of a config application rule override.  
Union field `upsell_type_config`. The type-specific configuration of the upsell. `upsell_type_config` can be only one of the following:  
`greeting_offer` |  `[GreetingOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.GreetingOffer)` Upsell specific items as part of the agent welcome message.  
`closing_offer` |  `[ClosingOffer](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ClosingOffer)` Upsell specific items after a customer has completed their order.  
`cel_upsell` |  `[CelUpsell](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.CelUpsell)` Dynamically evaluated upsell rule based on Common Expression Language (CEL).  
  
## UpsellMetrics

Represents upsell performance metrics for an interval.

Fields  
---  
`upsell_rate` |  `double` Output only. Percentage of total orders containing at least one upsell item.  
`upsell_success_rate` |  `double` Output only. Upsell conversion rate (percentage of upsell suggestions accepted).  
`upsell_revenue` |  `[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.type#google.type.Money)` Output only. Incremental revenue lift generated from accepted upsells.  
`total_attempt_count` |  `int64` Output only. Total upsell attempts across all types.  
`total_accepted_count` |  `int64` Output only. Total accepted upsells across all types.  
`type_metrics[]` |  `[UpsellTypeMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellMetrics.UpsellTypeMetrics)` Output only. The upsell metrics broken down by upsell type.  
  
## UpsellTypeMetrics

Upsell metrics broken down by type.

Fields  
---  
`upsell_type` |  `string` Output only. The upsell type (e.g. "SUGGESTIVE_UPSELL", "COMBO_UP_SIZE").  
`attempt_count` |  `int64` Output only. The number of times this upsell type was attempted.  
`accepted_count` |  `int64` Output only. The number of times this upsell type was accepted.  
`upsell_success_rate` |  `double` Output only. Conversion rate for this specific type (accepted_count / attempt_count * 100).  
  
## UpsellStrategy

Defines the strategy for upselling.

Fields  
---  
`max_upsell_offers` |  `int32` Optional. The maximum number of upsell offers to present per session.  
`max_upsell_declines` |  `int32` Optional. The maximum number of times a customer can decline an upsell before further upsells are skipped for the current session.  
`max_items_in_cart` |  `int32` Optional. The maximum number of items allowed in the cart before further upsells are skipped for the current session.  
`upsells[]` |  `[UpsellConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.UpsellConfig)` Optional. The configured upsells.  
`catering_guidelines` |  `string` Optional. Represents a set of text representing the offline-generated serving calculations and group ordering rules for this menu. Read by the conversational LLM.  
  
## ValidDeliveryStore

A store that can deliver to the specified delivery address.

Fields  
---  
`store` |  `string` Required. The store that can deliver to the address. Format: `projects/{project}/locations/{location}/brands/{brand}/stores/{store}`  
  
## ValidateDeliveryAddressRequest

A request to validate a delivery address collected during the session.

Fields  
---  
`delivery_address` |  `[DeliveryAddress](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress)` Required. The delivery address to validate.  
  
## ValidateDeliveryAddressResponse

The result of validating a delivery address.

Fields  
---  
`success` |  `bool` Required. Whether or not the validation completed without error.  
`validation_status` |  `[ValidationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.DeliveryAddress.ValidationStatus)` Required. The validation status of the delivery address.  
`valid_delivery_stores[]` |  `[ValidDeliveryStore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.ValidDeliveryStore)` Optional. The list of valid stores that can deliver to the original delivery address. This should only be populated when the validation status is VALIDATION_STATUS_OUT_OF_RANGE. And will be ignored otherwise.  
  
## WebhookAuthConfig

Authentication configuration for outbound webhook deliveries.

Fields  
---  
Union field `auth_method`. The authentication method to use when dispatching webhook requests. `auth_method` can be only one of the following:  
`basic_auth` |  `[BasicAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.BasicAuth)` Optional. Configuration for HTTP Basic authentication.  
`api_key_auth` |  `[ApiKeyAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.ApiKeyAuth)` Optional. Configuration for API key / custom header authentication.  
`bearer_token_auth` |  `[BearerTokenAuth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.BearerTokenAuth)` Optional. Configuration for Bearer token authentication.  
  
## ApiKeyAuth

API Key / Custom Header Authentication (`<header>: <secret_value>`).

Fields  
---  
`header` |  `string` Required. The HTTP header to populate (e.g., "X-API-Key").  
`api_key` |  `[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.SecretSource)` Required. Secret containing the API key or header value.  
  
## BasicAuth

HTTP Basic Authentication (`Authorization: Basic <base64(user:pass)>`).

Fields  
---  
`credential` |  `[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.SecretSource)` Required. Secret containing the colon-separated basic auth credential in `<username>:<password>` format.  
  
## BearerTokenAuth

Bearer Token Authentication (`Authorization: Bearer <token>`).

Fields  
---  
`token` |  `[SecretSource](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig.SecretSource)` Required. Secret containing the bearer token.  
  
## SecretSource

Reference to a secret value used for webhook authentication.

Fields  
---  
Union field `source`. The backing store for the secret value. `source` can be only one of the following:  
`secret_version` |  `string` Optional. The name of the Secret Manager secret version resource storing the secret value. Format: `projects/{project}/secrets/{secret}/versions/{secret_version}`Note: You must grant the `roles/secretmanager.secretAccessor` role to the Food Ordering AI Agent service agent `service-<PROJECT-NUMBER>@gcp-sa-foodorderingaiagent.iam.gserviceaccount.com`.  
  
## WebhookSubscription

A webhook subscription configured for a brand to receive real-time event notifications.

Fields  
---  
`name` |  `string` Identifier. The resource name of the webhook subscription. Format: `projects/{project}/locations/{location}/brands/{brand}/webhookSubscriptions/{webhook_subscription}`  
`display_name` |  `string` Optional. Human-readable display name for this webhook subscription.  
`state` |  `[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookSubscription.State)` Optional. The current state of the webhook subscription. Users may transition a subscription between `ACTIVE` and `PAUSED`.  
`event_types[]` |  `string` Required. Event types that trigger this webhook subscription (e.g., `sessions/started`, `sessions/updated`, `sessions/closed`, `orders/updated`).  
`destination_url` |  `string` Required. The HTTPS endpoint URL where webhook events are delivered via HTTP POST.  
`filter` |  `string` Optional. Common Expression Language (CEL) filter expression evaluated against event attributes (e.g., `channel == 'CHANNEL_TYPE_DRIVE_THROUGH' && store.endsWith('/stores/store-123')`). If empty, all events matching `event_types` for the brand are delivered.  
`auth_config` |  `[WebhookAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rpc/google.cloud.foodorderingaiagent.v1#google.cloud.foodorderingaiagent.v1.WebhookAuthConfig)` Optional. Authentication configuration for outbound webhook deliveries.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this webhook subscription was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time this webhook subscription was last updated.  
  
## State

Lifecycle state of the webhook subscription.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The subscription is active and receiving webhook event deliveries.  
`PAUSED` | The subscription has been paused by the user and will not receive events until re-activated.  
`SUSPENDED` | The subscription has been automatically suspended by the platform circuit breaker due to repeated delivery failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
