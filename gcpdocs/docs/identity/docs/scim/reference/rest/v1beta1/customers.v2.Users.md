---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users
title: REST Resource: customers.v2.Users \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-29T06:14:06.313922+00:00
---

# REST Resource: customers.v2.Users  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.Users Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: User

SCIM representation of a user.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "emails": [
        {
          object ([Email](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Email))
        }
      ],
      "addresses": [
        {
          object ([Address](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Address))
        }
      ],
      "phoneNumbers": [
        {
          object ([Phone](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Phone))
        }
      ],
      "groups": [
        {
          object ([GroupReference](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#GroupReference))
        }
      ],
      "id": string,
      "externalId": string,
      "meta": {
        object ([Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta))
      },
      "userName": string,
      "name": {
        object ([Name](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Name))
      },
      "displayName": string,
      "active": boolean,
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        object ([EnterpriseUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#EnterpriseUserExtension))
      },
      "urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityUser": {
        object ([CloudIdentityUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#CloudIdentityUserExtension))
      }
    }  
  
Fields  
---  
`schemas[]` |  `string` Required. A list of URIs which indicate the namespaces of the SCIM schemas that define the attributes present in the current JSON structure. Must only contain values defined as `schema` and `schemaExtensions` for the User ResourceType.  
`emails[]` |  `object (`[Email](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Email)`)` Optional. The list of the user's email addresses. The maximum allowed data size is 10KB. The email corresponding to `userName` will automatically be added to this list with its `primary` sub-attribute set to `true`. This primary email entry is read-only and cannot be modified through this attribute.  
`addresses[]` |  `object (`[Address](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Address)`)` Optional. The list of the user's physical addresses. The maximum allowed data size is 10KB.  
`phoneNumbers[]` |  `object (`[Phone](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Phone)`)` Optional. A list of the user's phone numbers. The maximum allowed data size is 1KB.  
`groups[]` |  `object (`[GroupReference](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#GroupReference)`)` Output only. The list of groups the user has direct membership in, truncated to a maximum of 1000 groups.This attribute is not returned by default and must be requested using the `attributes` query parameter. Reading this attribute requires customer allowlisting. Please contact support to explain your use case and request access.  
`id` |  `string` Identifier. The unique ID for the user. The attribute characteristics are `caseExact` as `true`, a mutability of `readOnly`, and a `returned` characteristic of `always`.  
`externalId` |  `string` Optional. A client-defined identifier for the SCIM user. This field is case-sensitive and mutable. The client is responsible for ensuring uniqueness, as the server does not enforce it.  
`meta` |  `object (`[Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta)`)` Output only. A complex attribute containing resource metadata. All `meta` sub-attributes are assigned by the service provider (have a `mutability` of `readOnly`), and all of these sub-attributes have a `returned` characteristic of `default`. This attribute is ignored when provided by clients.  
`userName` |  `string` Required. The user's primary email address. Used as the unique identifier for the user.  
`name` |  `object (`[Name](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Name)`)` Required. The user's name.  
`displayName` |  `string` Optional. The user's display name. Limit: 256 characters.  
`active` |  `boolean` Optional. The user's account status (`false` means the account is suspended). Default: `true`.  
`urn:ietf:params:scim:schemas:extension:enterprise:2.0:User` |  `object (`[EnterpriseUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#EnterpriseUserExtension)`)` Optional. SCIM Enterprise User extension attributes.  
`urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityUser` |  `object (`[CloudIdentityUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#CloudIdentityUserExtension)`)` Optional. SCIM Cloud Identity User extension attributes.  
  
## Name

SCIM representation of a User's name.

JSON representation  
---  
      
    
    {
      "familyName": string,
      "givenName": string
    }  
  
Fields  
---  
`familyName` |  `string` Required. The user's family name.  
`givenName` |  `string` Required. The user's given name.  
  
## Email

SCIM representation of a user's email.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`value` |  `string` Required. The user's email address.  
`type` |  `string` The type of the email account. Valid values are `home`, `work`, and `other`.  
`primary` |  `boolean` Output only. Indicates if this is the user's primary email. This value is set to `true` only for the email which corresponds to `userName`.  
  
## Address

SCIM representation of a user's address.

JSON representation  
---  
      
    
    {
      "formatted": string,
      "streetAddress": string,
      "locality": string,
      "region": string,
      "postalCode": string,
      "country": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`formatted` |  `string` Full address, formatted for display.  
`streetAddress` |  `string` The street address.  
`locality` |  `string` The city or locality.  
`region` |  `string` The region or state.  
`postalCode` |  `string` The postal code or zip code.  
`country` |  `string` The country.  
`type` |  `string` The type of the address. Valid values are `home`, `work`, and `other`.  
`primary` |  `boolean` Indicates if this is the user's primary address.  
  
## Phone

SCIM representation of a user's phone number.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`value` |  `string` Required. The phone number.  
`type` |  `string` The type of the phone number. Valid values are `home`, `work`, `mobile`, `fax`, `pager`, and `other`.  
`primary` |  `boolean` Indicates if this is the user's primary phone number.  
  
## EnterpriseUserExtension

Defines the attributes for the SCIM Enterprise User extension. The schema URN for this extension is: `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`. See [RFC 7643 Section 4.3](https://datatracker.ietf.org/doc/html/rfc7643#section-4.3) for more details.

JSON representation  
---  
      
    
    {
      "employeeNumber": string,
      "costCenter": string,
      "organization": string,
      "department": string,
      "manager": {
        object ([Manager](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Manager))
      }
    }  
  
Fields  
---  
`employeeNumber` |  `string` Optional. Identifier, typically assigned by the organization, used to identify the user inside the organization.  
`costCenter` |  `string` Optional. Identifier for the cost center to which the user's expenditures are attributed.  
`organization` |  `string` Optional. The name of an organization a user belongs to.  
`department` |  `string` Optional. The name of a department user belongs to in the text format.  
`manager` |  `object (`[Manager](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Manager)`)` Optional. The user's manager. A complex attribute that optionally allows service providers to represent organizational hierarchy by referencing the `id` attribute of another user.  
  
## Manager

SCIM representation of a user's manager. Fields are based on [RFC 7643 Section 4.3](https://datatracker.ietf.org/doc/html/rfc7643#section-4.3).

JSON representation  
---  
      
    
    {
      "value": string,
      "$ref": string
    }  
  
Fields  
---  
`value` |  `string` Optional. The `id` of the SCIM resource representing the user's manager.  
`$ref` |  `string` Output only. The URI of the SCIM resource representing the user's manager.  
  
## GroupReference

SCIM representation of a user's group membership.

JSON representation  
---  
      
    
    {
      "value": string,
      "$ref": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` Output only. The `id` of the SCIM resource representing the group.  
`$ref` |  `string` Output only. The URI of the SCIM resource representing the group.  
`type` |  `string` Output only. The type of group membership. Valid values are `direct` and `indirect`.  
  
## CloudIdentityUserExtension

Defines the attributes for the Google Cloud Identity User extension. The schema URN for this extension is: `urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityUser`.

JSON representation  
---  
      
    
    {
      "websites": [
        {
          object ([Website](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Website))
        }
      ],
      "additionalExternalIds": [
        {
          object ([ExternalId](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#ExternalId))
        }
      ],
      "additionalIms": [
        {
          object ([AdditionalIm](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#AdditionalIm))
        }
      ],
      "additionalOrganizations": [
        {
          object ([AdditionalOrganization](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#AdditionalOrganization))
        }
      ],
      "addressListVisible": boolean,
      "gender": string,
      "organizationalUnit": {
        object ([OrganizationalUnit](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#OrganizationalUnit))
      },
      "primaryOrganization": {
        object ([PrimaryOrganization](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#PrimaryOrganization))
      }
    }  
  
Fields  
---  
`websites[]` |  `object (`[Website](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Website)`)` Optional. The websites associated with the user, excluding websites of type `profile` (which correspond to the SCIM core schema attribute `profileUrl`).  
`additionalExternalIds[]` |  `object (`[ExternalId](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#ExternalId)`)` Optional. A collection of external identifiers for the user. This list serves as a supplemental set to those already represented by the SCIM core schema attribute `externalId` and the SCIM Enterprise User extension attribute `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber`.  
`additionalIms[]` |  `object (`[AdditionalIm](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#AdditionalIm)`)` Optional. Non-primary instant messaging addresses for the user. Excludes primary IM addresses, which correspond to the SCIM core schema attribute `ims`.  
`additionalOrganizations[]` |  `object (`[AdditionalOrganization](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#AdditionalOrganization)`)` Optional. Non-primary organizations of the user.  
`addressListVisible` |  `boolean` Optional. Indicates whether the user should be shown in the global address list. If unassigned or cleared by the client, this attribute defaults to `true`.  
`gender` |  `string` Optional. The gender of the user. Supported values are `female`, `male`, `other`, and `unknown`. Custom values are also supported; any other string value is treated as a custom gender.  
`organizationalUnit` |  `object (`[OrganizationalUnit](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#OrganizationalUnit)`)` Optional. The organizational unit of the user.  
`primaryOrganization` |  `object (`[PrimaryOrganization](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#PrimaryOrganization)`)` Optional. Additional attributes of the primary organization of the user. Excludes `name`, `department`, and `costCenter` (which are represented by `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`), as well as `title` (which corresponds to the SCIM core schema attribute `title`).  
  
## OrganizationalUnit

SCIM representation of a user's organizational unit.

JSON representation  
---  
      
    
    {
      "path": string
    }  
  
Fields  
---  
`path` |  `string` Optional. The full path of the organizational unit the user belongs to (for example, `/corp/engineering`), or `/` for the top-level organizational unit. The organizational unit must already exist. If unassigned or cleared by the client, this attribute defaults to `/`.  
  
## Website

SCIM representation of a user's website. Excludes websites of type `profile`, which correspond to the SCIM core schema attribute `profileUrl`.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` Required. The website URL.  
`type` |  `string` Optional. The type of the website. Supported values are `home`, `work`, and `other`. Any input value other than `home` or `work` is treated as `other`.  
  
## ExternalId

SCIM representation of a user's additional external identifier. Excludes external identifiers already represented by the SCIM core schema attribute `externalId` and the SCIM Enterprise User extension attribute `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber`.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` Required. The value of the external ID.  
`type` |  `string` Optional. The type of the external ID. Supported values include `account`, `customer`, `loginId`, and `network`. Custom values are also supported; any other string value is treated as a custom type. The values `organization` and `cloudidentityscim.googleapis.com` are reserved and cannot be used.  
  
## AdditionalIm

SCIM representation of a user's non-primary instant messaging (IM) address. Excludes primary IM addresses, which correspond to the SCIM core schema attribute `ims`.

JSON representation  
---  
      
    
    {
      "value": string,
      "usage": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` Required. The IM address.  
`usage` |  `string` Optional. The usage of the IM. Supported values include `home`, `work`, and `other`. Custom values are also supported; any other string value is treated as a custom usage.  
`type` |  `string` Optional. The type of the IM service. Supported values include `aim`, `gtalk`, `icq`, `jabber`, `msn`, `netmeeting`, `qq`, `skype`, and `yahoo`. Custom values are also supported; any other string value is treated as a custom type.  
  
## PrimaryOrganization

SCIM representation of a user's primary organization. The fields in this complex attribute apply to the same primary organization as the SCIM Enterprise User extension (`urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`). It excludes `name`, `department`, and `costCenter` (which are represented by the `organization`, `department`, and `costCenter` attributes in `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`), as well as `title` (which corresponds to the SCIM core schema attribute `title`).

JSON representation  
---  
      
    
    {
      "type": string,
      "domain": string,
      "fullTimeEquivalent": integer,
      "location": string,
      "symbol": string
    }  
  
Fields  
---  
`type` |  `string` Optional. The type of the organization. Valid values are `school` and `work`.  
`domain` |  `string` Optional. The domain name associated with the organization. For example, `example.com`.  
`fullTimeEquivalent` |  `integer` Optional. The full-time equivalent millipercent within the organization (100000 = 100%).  
`location` |  `string` Optional. The physical location of the organization.  
`symbol` |  `string` Optional. The symbol of the organization.  
  
## AdditionalOrganization

SCIM representation of a user's non-primary organization. Excludes the user's primary organization, which is represented across the `primaryOrganization` attribute, the SCIM Enterprise User extension (`urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`), and the SCIM core schema attribute `title`.

JSON representation  
---  
      
    
    {
      "type": string,
      "costCenter": string,
      "department": string,
      "domain": string,
      "fullTimeEquivalent": integer,
      "location": string,
      "name": string,
      "symbol": string,
      "title": string
    }  
  
Fields  
---  
`type` |  `string` Optional. The type of the organization. Valid values are `school` and `work`.  
`costCenter` |  `string` Optional. The cost center of the organization.  
`department` |  `string` Optional. The department of the organization.  
`domain` |  `string` Optional. The domain name associated with the organization. For example, `example.com`.  
`fullTimeEquivalent` |  `integer` Optional. The full-time equivalent millipercent within the organization (100000 = 100%).  
`location` |  `string` Optional. The physical location of the organization.  
`name` |  `string` Optional. The name of the organization.  
`symbol` |  `string` Optional. The symbol of the organization.  
`title` |  `string` Optional. The user's title within the organization.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/create)`

|  Creates a User.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/delete)`

|  Deletes a User.  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/get)`

|  Retrieves a User.  
  
### `[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/list)`

|  Retrieves a list of Users.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/patch)`

|  Updates a User using SCIM patch semantics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-28 UTC."],[],[]] 
