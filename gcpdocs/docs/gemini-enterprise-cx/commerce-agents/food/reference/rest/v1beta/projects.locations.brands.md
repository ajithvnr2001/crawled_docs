---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands
title: REST Resource: projects.locations.brands \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:15.604820+00:00
---

# REST Resource: projects.locations.brands  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Brand
    * JSON representation
    * ConfigRuleBinding
      * JSON representation
    * McpConfig
      * JSON representation
    * MenuIngestionConfig
      * JSON representation
    * AvailabilityConfig
      * JSON representation
    * ProductMatcher
      * JSON representation
    * NameNormalizationConfig
      * JSON representation
    * ProductNameOverride
      * JSON representation
    * RegexReplacement
      * JSON representation
    * ItemBuildingConfig
      * JSON representation
    * ItemNumberConfig
      * JSON representation
    * IngestionStoreMatcher
      * JSON representation
    * ItemNumberMapping
      * JSON representation
    * ModifierGroupOrderingRule
      * JSON representation
    * SortStrategy
    * ModifierGroupReplicationRule
      * JSON representation
    * ModifierGroupNamingRule
      * JSON representation
    * NamingStrategy
    * AutoBundleConfig
      * JSON representation
    * CategoryConfig
      * JSON representation
    * SearchConfig
      * JSON representation
    * ChildSynonym
      * JSON representation
    * ModifierGroupIntegrationAttributeConfig
      * JSON representation
    * ItemIntegrationAttributeConfig
      * JSON representation
    * LocalizedConfig
      * JSON representation
    * StoreIngestionConfig
      * JSON representation
    * StoreTimeZoneConfig
      * JSON representation
  * Methods



## Resource: Brand

A brand, which can be a restaurant chain or an individual restaurant.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "defaultChannelConfig": string,
      "configRuleBindings": [
        {
          object ([ConfigRuleBinding](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ConfigRuleBinding))
        }
      ],
      "defaultUpsellStrategyChannelConfig": string,
      "kmsKey": string,
      "mcpConfig": {
        object ([McpConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.McpConfig))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone))
      },
      "menuIngestionConfig": {
        object ([MenuIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.MenuIngestionConfig))
      },
      "geoApiConsentGranted": boolean,
      "storeIngestionConfig": {
        object ([StoreIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.StoreIngestionConfig))
      },
      "defaultChannelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The brand name. Format: projects/{project}/locations/{location}/brands/{brand}  
`displayName` |  `string` Optional. Optional, human-readable display name for this brand for user interfaces.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this brand was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this brand was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`defaultChannelConfig` |  `string` Optional. Name of the ChannelConfig to use as the brand default for agent customization. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
`configRuleBindings[]` |  `object (`[ConfigRuleBinding](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ConfigRuleBinding)`)` Optional. Conditional agent config overrides for the brand. These allow for overriding agent behavior based on certain conditions.  
`defaultUpsellStrategyChannelConfig` |  `string` Optional. Name of the ChannelConfig to use as the brand default for upsell strategy. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
`kmsKey` |  `string` Optional. Immutable. The Cloud KMS key to encrypt conversational session data at rest. Format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}`This field can only be set when creating a Brand and cannot be updated or disabled later.  
`mcpConfig` |  `object (`[McpConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.McpConfig)`)` Optional. Configuration for Model Context Protocol (MCP) service.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone)`)` Optional. The time zone of the brand. This is used for brand-level analytics and reporting rollups.  
`menuIngestionConfig` |  `object (`[MenuIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.MenuIngestionConfig)`)` Optional. Configuration for menu ingestion.  
`geoApiConsentGranted` |  `boolean` Optional. Whether customer has granted legal consent to use the Geocoding API.  
`storeIngestionConfig` |  `object (`[StoreIngestionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.StoreIngestionConfig)`)` Optional. Configuration for store ingestion.  
`defaultChannelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ChannelType)`)` Optional. The default channel type for this brand if not specified in the session config.  
  
### ConfigRuleBinding

Defines a conditional override of agent behavior.

JSON representation  
---  
      
    
    {
      "configApplicationRule": string,
      "channelConfig": string
    }  
  
Fields  
---  
`configApplicationRule` |  `string` Required. The condition to check for whether to apply the override. Format: projects/{project}/locations/{location}/brands/{brand}/configApplicationRules/{configApplicationRule}  
`channelConfig` |  `string` Required. The configuration to apply if the override condition is met. Format: projects/{project}/locations/{location}/brands/{brand}/channelConfigs/{channelConfig}  
  
### McpConfig

Configuration for Model Context Protocol (MCP) service.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Whether the MCP service is enabled for the brand.  
  
### MenuIngestionConfig

Configuration for menu ingestion.

JSON representation  
---  
      
    
    {
      "availabilityConfig": {
        object ([AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AvailabilityConfig))
      },
      "nameNormalizationConfig": {
        object ([NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NameNormalizationConfig))
      },
      "itemBuildingConfig": {
        object ([ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemBuildingConfig))
      },
      "customConfig": {
        object
      },
      "localizedConfigs": [
        {
          object ([LocalizedConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.LocalizedConfig))
        }
      ]
    }  
  
Fields  
---  
`availabilityConfig` |  `object (`[AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AvailabilityConfig)`)` Optional. Configuration for menu item availability.  
`nameNormalizationConfig` |  `object (`[NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NameNormalizationConfig)`)` Optional. Configuration for name normalization during menu ingestion.  
`itemBuildingConfig` |  `object (`[ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemBuildingConfig)`)` Optional. Configuration for building items during menu ingestion.  
`customConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom configurations for brand-specific menu ingestion.  
`localizedConfigs[]` |  `object (`[LocalizedConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.LocalizedConfig)`)` Optional. Language-specific menu ingestion configurations. Name-based configurations (e.g., name matchers, name normalization, search synonyms, category configs) for specific languages are grouped here under their respective BCP-47 language code. Duplicate language codes are not allowed.  
  
### AvailabilityConfig

Configuration for menu item availability.

JSON representation  
---  
      
    
    {
      "conditionalExclusions": [
        {
          object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
        }
      ],
      "modifierOnlyProductIds": [
        string
      ]
    }  
  
Fields  
---  
`conditionalExclusions[]` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. Items that are conditionally excluded based on matching criteria.  
`modifierOnlyProductIds[]` |  `string` Optional. Products that are only available in meals or combos and not directly orderable.  
  
### ProductMatcher

Matcher used to match one or multiple menu entities like items/modifierGroup/modifiers during menu ingestion time.

JSON representation  
---  
      
    
    {
      "productIds": [
        string
      ],
      "productExactNames": [
        string
      ],
      "productRegexName": string,
      "productType": string,
      "parentProductType": string,
      "daypartId": string,
      "existingProductId": string,
      "parentProductId": string
    }  
  
Fields  
---  
`productIds[]` |  `string` Optional. The product IDs to match.  
`productExactNames[]` |  `string` Optional. The exact product names to match.  
`productRegexName` |  `string` Optional. A regular expression to match product names.  
`productType` |  `string` Optional. The product type to match.  
`parentProductType` |  `string` Optional. The parent product type under which the product is matched.  
`daypartId` |  `string` Optional. The daypart during which the match applies.  
`existingProductId` |  `string` Optional. The product ID that must exist for the match to trigger.  
`parentProductId` |  `string` Optional. The parent product ID under which the product is matched (e.g. only match a modifier when it is offered on a specific item).  
  
### NameNormalizationConfig

Configuration for name normalization during menu ingestion.

JSON representation  
---  
      
    
    {
      "productNameOverrides": [
        {
          object ([ProductNameOverride](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductNameOverride))
        }
      ],
      "regexReplacements": [
        {
          object ([RegexReplacement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.RegexReplacement))
        }
      ],
      "casingExceptions": [
        string
      ]
    }  
  
Fields  
---  
`productNameOverrides[]` |  `object (`[ProductNameOverride](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductNameOverride)`)` Optional. Overrides product names for matched item(s).  
`regexReplacements[]` |  `object (`[RegexReplacement](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.RegexReplacement)`)` Optional. Ordered list of regular expression replacements applied to normalize item names.  
`casingExceptions[]` |  `string` Optional. Words or tokens whose casing should be preserved during title casing.  
  
### ProductNameOverride

A rule for overriding a product name for matched item(s).

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "targetName": string
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s).  
`targetName` |  `string` Required. Target product name to use when matched.  
  
### RegexReplacement

A regular expression replacement rule.

JSON representation  
---  
      
    
    {
      "pattern": string,
      "replacement": string
    }  
  
Fields  
---  
`pattern` |  `string` Required. The regular expression pattern to match.  
`replacement` |  `string` Optional. The string to replace matches with. If omitted, matches are replaced with an empty string.  
  
### ItemBuildingConfig

Optional. Configuration for building items during menu ingestion.

JSON representation  
---  
      
    
    {
      "itemNumberConfigs": [
        {
          object ([ItemNumberConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemNumberConfig))
        }
      ],
      "modifierGroupOrderingRules": [
        {
          object ([ModifierGroupOrderingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupOrderingRule))
        }
      ],
      "modifierGroupReplicationRules": [
        {
          object ([ModifierGroupReplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupReplicationRule))
        }
      ],
      "modifierGroupNamingRules": [
        {
          object ([ModifierGroupNamingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupNamingRule))
        }
      ],
      "autoBundleConfig": {
        object ([AutoBundleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AutoBundleConfig))
      },
      "categoryConfigs": [
        {
          object ([CategoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.CategoryConfig))
        }
      ],
      "searchConfigs": [
        {
          object ([SearchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.SearchConfig))
        }
      ],
      "modifierGroupIntegrationAttributeConfigs": [
        {
          object ([ModifierGroupIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupIntegrationAttributeConfig))
        }
      ],
      "itemIntegrationAttributeConfigs": [
        {
          object ([ItemIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemIntegrationAttributeConfig))
        }
      ]
    }  
  
Fields  
---  
`itemNumberConfigs[]` |  `object (`[ItemNumberConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemNumberConfig)`)` Optional. Rules for assigning item numbers to items.  
`modifierGroupOrderingRules[]` |  `object (`[ModifierGroupOrderingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupOrderingRule)`)` Optional. Rules for ordering/sorting modifier groups.  
`modifierGroupReplicationRules[]` |  `object (`[ModifierGroupReplicationRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupReplicationRule)`)` Optional. Rules for replicating multi-quantity modifier groups into individual slots.  
`modifierGroupNamingRules[]` |  `object (`[ModifierGroupNamingRule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupNamingRule)`)` Optional. Rules for naming modifier groups.  
`autoBundleConfig` |  `object (`[AutoBundleConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AutoBundleConfig)`)` Optional. Configuration for auto-bundling combos.  
`categoryConfigs[]` |  `object (`[CategoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.CategoryConfig)`)` Optional. Configuration for the categories assigned to items.  
`searchConfigs[]` |  `object (`[SearchConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.SearchConfig)`)` Optional. Configuration for the search attributes assigned to items.  
`modifierGroupIntegrationAttributeConfigs[]` |  `object (`[ModifierGroupIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ModifierGroupIntegrationAttributeConfig)`)` Optional. Configuration for the integration attributes assigned to modifier groups.  
`itemIntegrationAttributeConfigs[]` |  `object (`[ItemIntegrationAttributeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemIntegrationAttributeConfig)`)` Optional. Configuration for the integration attributes assigned to items.  
  
### ItemNumberConfig

Configuration for assigning item/menu numbers to items.

JSON representation  
---  
      
    
    {
      "storeMatcher": {
        object ([IngestionStoreMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.IngestionStoreMatcher))
      },
      "itemNumberMappings": [
        {
          object ([ItemNumberMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemNumberMapping))
        }
      ]
    }  
  
Fields  
---  
`storeMatcher` |  `object (`[IngestionStoreMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.IngestionStoreMatcher)`)` Optional. Matcher for stores where these item number mappings apply. If not specified or empty, applies across all stores as the default.  
`itemNumberMappings[]` |  `object (`[ItemNumberMapping](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemNumberMapping)`)` Optional. List of item matcher to item number mappings.  
  
### IngestionStoreMatcher

Matcher used to match one or multiple stores during menu ingestion time.

JSON representation  
---  
      
    
    {
      "storeIds": [
        string
      ]
    }  
  
Fields  
---  
`storeIds[]` |  `string` Optional. Specific store IDs where the configuration applies. If not specified, applies across all stores as the default.  
  
### ItemNumberMapping

Mapping from an item matcher to its item numbers.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "itemNumbers": [
        string
      ]
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s).  
`itemNumbers[]` |  `string` Optional. The item numbers to assign (e.g., ["1"], ["2", "2a"]).  
  
### ModifierGroupOrderingRule

Configuration for ordering/sorting modifier groups.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "sortStrategy": enum ([SortStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.SortStrategy)),
      "priorityList": [
        string
      ]
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this ordering rule applies.  
`sortStrategy` |  `enum (`[SortStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.SortStrategy)`)` Optional. The sorting strategy to apply to modifier groups.  
`priorityList[]` |  `string` Optional. Ordered list of terms (e.g. keywords, modifier group names, or types) used when sortStrategy is PRIORITY_LIST. Modifier groups matching earlier terms in the list are sorted first.  
  
### SortStrategy

Strategy for sorting modifier groups.

Enums  
---  
`SORT_STRATEGY_UNSPECIFIED` | Unspecified sorting strategy.  
`ALPHABETICAL` | Sort modifier groups alphabetically by display name.  
`PRIORITY_LIST` | Sort modifier groups by priority list.  
  
### ModifierGroupReplicationRule

Configuration for replicating/expanding multi-quantity modifier groups into individual single-quantity slots (e.g., expanding a 2-drink choice into Drink 1 and Drink 2).

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "modifierGroupTypes": [
        string
      ],
      "enabled": boolean
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this replication rule applies.  
`modifierGroupTypes[]` |  `string` Optional. Modifier group types or names to replicate (e.g., "Side", "Drink", "Entree"). If not specified, applies to all modifier groups of the matched items.  
`enabled` |  `boolean` Optional. Whether replication is enabled for the matched items and modifier groups. Defaults to true.  
  
### ModifierGroupNamingRule

Configuration for naming modifier groups.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "namingStrategy": enum ([NamingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NamingStrategy))
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this naming rule applies.  
`namingStrategy` |  `enum (`[NamingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NamingStrategy)`)` Optional. The naming strategy to apply to modifier groups of the matched items.  
  
### NamingStrategy

Strategy for naming modifier groups.

Enums  
---  
`NAMING_STRATEGY_UNSPECIFIED` | Unspecified naming strategy.  
`CATEGORY_NAME` | Name modifier groups using the category or modifier group type (e.g., Entree, Side, Drink).  
`CHOICE_GROUP_NAME` | Name modifier groups using the choice group name from the source POS/catalog.  
  
### AutoBundleConfig

Configuration for auto-bundling items into combos.

JSON representation  
---  
      
    
    {
      "defaultAllowAutoBundle": boolean,
      "allowAutoBundleItemMatchers": [
        {
          object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
        }
      ],
      "disallowAutoBundleItemMatchers": [
        {
          object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
        }
      ]
    }  
  
Fields  
---  
`defaultAllowAutoBundle` |  `boolean` Optional. Whether auto-bundling is allowed by default for all combos.  
`allowAutoBundleItemMatchers[]` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. Item matchers of combos that allow auto-bundling (overriding the default when defaultAllowAutoBundle is false).  
`disallowAutoBundleItemMatchers[]` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. Item matchers of combos that disallow auto-bundling (overriding the default when defaultAllowAutoBundle is true).  
  
### CategoryConfig

Configuration for the categories assigned to items.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "categoryIds": [
        string
      ],
      "hierarchicalCategories": [
        string
      ]
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this category config applies.  
`categoryIds[]` |  `string` Optional. The IDs of the categories to assign to the items.  
`hierarchicalCategories[]` |  `string` Optional. The hierarchical categories to assign to the items.  
  
### SearchConfig

Configuration for the search attributes assigned to items.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "synonyms": [
        string
      ],
      "childSynonyms": [
        {
          object ([ChildSynonym](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ChildSynonym))
        }
      ]
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this search config applies.  
`synonyms[]` |  `string` Optional. The synonyms to assign to the items.  
`childSynonyms[]` |  `object (`[ChildSynonym](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ChildSynonym)`)` Optional. The child synonyms to assign to the items.  
  
### ChildSynonym

Child synonym for a menu entity. This is to support cases like "Sausage Egg Cheese Biscuit" to "Sausage Egg Biscuit" with modifier "Cheese".

JSON representation  
---  
      
    
    {
      "synonym": string,
      "children": [
        string
      ]
    }  
  
Fields  
---  
`synonym` |  `string` Optional. The synonym for the menu entity.  
`children[]` |  `string` Optional. Additional child that needs to match for that synonym.  
  
### ModifierGroupIntegrationAttributeConfig

Configuration for integration attributes assigned to modifier groups.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "modifierGroupNames": [
        string
      ],
      "integrationAttribute": {
        object
      }
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this modifier group integration attribute config applies.  
`modifierGroupNames[]` |  `string` Optional. The names or types of the modifier groups to which this integration attribute config applies.  
`integrationAttribute` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom integration attributes to assign to the matched modifier groups.  
  
### ItemIntegrationAttributeConfig

Configuration for integration attributes assigned to items.

JSON representation  
---  
      
    
    {
      "productMatcher": {
        object ([ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher))
      },
      "integrationAttribute": {
        object
      }
    }  
  
Fields  
---  
`productMatcher` |  `object (`[ProductMatcher](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ProductMatcher)`)` Optional. The product matcher to identify the item(s) to which this item integration attribute config applies.  
`integrationAttribute` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom integration attributes to assign to the matched items.  
  
### LocalizedConfig

High-level localized configuration for menu ingestion. Groups name-based configurations (e.g. name normalization rules, search synonyms, category configs, name matchers) that belong to a specific language.

JSON representation  
---  
      
    
    {
      "languageCode": string,
      "nameNormalizationConfig": {
        object ([NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NameNormalizationConfig))
      },
      "itemBuildingConfig": {
        object ([ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemBuildingConfig))
      },
      "availabilityConfig": {
        object ([AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AvailabilityConfig))
      },
      "customConfig": {
        object
      }
    }  
  
Fields  
---  
`languageCode` |  `string` Required. The BCP-47 language code for this configuration (e.g., `en`, `es`, `ja`, `en-US`, `es-MX`).  
`nameNormalizationConfig` |  `object (`[NameNormalizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.NameNormalizationConfig)`)` Optional. Configuration for name normalization for this language.  
`itemBuildingConfig` |  `object (`[ItemBuildingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.ItemBuildingConfig)`)` Optional. Configuration for building items specific to this language (e.g., language-specific search synonyms, category configs, modifier group ordering rules).  
`availabilityConfig` |  `object (`[AvailabilityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.AvailabilityConfig)`)` Optional. Language-specific availability rules (e.g. conditional exclusions matching localized product names).  
`customConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Language-specific custom configurations.  
  
### StoreIngestionConfig

Configuration for store ingestion.

JSON representation  
---  
      
    
    {
      "stagingStoreIds": [
        string
      ],
      "testStoreIds": [
        string
      ],
      "storeTimeZoneConfigs": [
        {
          object ([StoreTimeZoneConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.StoreTimeZoneConfig))
        }
      ],
      "defaultOrderLimits": {
        object ([OrderLimits](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/OrderLimits))
      },
      "defaultSchedule": {
        object ([Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Schedule))
      },
      "defaultDayparts": [
        {
          object ([Daypart](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Daypart))
        }
      ],
      "customConfig": {
        object
      }
    }  
  
Fields  
---  
`stagingStoreIds[]` |  `string` Optional. Store IDs routed to the staging environment during ingestion.  
`testStoreIds[]` |  `string` Optional. Store IDs designated for testing during ingestion.  
`storeTimeZoneConfigs[]` |  `object (`[StoreTimeZoneConfig](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands#Brand.StoreTimeZoneConfig)`)` Optional. Time zone mappings for specific stores.  
`defaultOrderLimits` |  `object (`[OrderLimits](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/OrderLimits)`)` Optional. Default order limits applied to stores when not provided by the store data source.  
`defaultSchedule` |  `object (`[Schedule](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Schedule)`)` Optional. Default operating schedule applied to stores when not provided by the store data source.  
`defaultDayparts[]` |  `object (`[Daypart](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/Daypart)`)` Optional. Default dayparts applied to stores when not provided by the store data source.  
`customConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom configurations for brand-specific store ingestion.  
  
### StoreTimeZoneConfig

Mapping of a time zone to specific stores.

JSON representation  
---  
      
    
    {
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone))
      },
      "storeIds": [
        string
      ]
    }  
  
Fields  
---  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeZone)`)` Optional. The time zone to apply to the matched stores.  
`storeIds[]` |  `string` Optional. The store IDs that use this time zone.  
  
## Methods  
  
---  
  
### `[computeAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics)`

|  Computes analytics metrics for a given brand for specified time period with optional store filter.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/create)`

|  Creates a brand.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/delete)`

|  Deletes the specified brand.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/get)`

|  Gets a brand.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/list)`

|  Lists brands.  
  
### `[listHistory](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/listHistory)`

|  Lists history entries for a brand.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.brands/patch)`

|  Updates the specified brand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 
