---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy/
title: HTTPModifier policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-24T09:20:42.723291+00:00
---

# HTTPModifier policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  HTTPModifier policy Stay organized with collections  Save and categorize content based on your preferences. 

[Standard policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The HTTPModifier policy changes an existing request or response message. 

The policy lets you perform the following actions on those messages:

  * Add new form parameters, headers, or query parameters to a message
  * Remove headers, query parameters, and form parameters from a message
  * Set the value of existing properties in a message



With HTTPModifier, you can add, change, or remove properties of either the request or response. You can alternatively use HTTPModifier to create a custom request or response message and pass it to an alternative target, as described in Create custom request messages.

HTTPModifier provides a subset of the [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) functionality. See [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) for additional functionality including assigning variables, modifying payloads, and copying values from the message.

The HTTPModifier policy can create flow variables with the following child elements:

  * [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add)
  * [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)
  * [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove)
  * [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto)



The order in which you organize the [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add), [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set), and [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove) elements is important. The policy executes those actions in the order in which they appear in the policy configuration. If you need to remove all headers, then set a specific header, you should include the [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove) element before the [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) element. 

This policy is a _Standard policy_ and can be deployed to any environment type. For information on policy types and availability with each environment type, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Use cases

There are many situations in which you might want to modify a request or a response message during processing by Apigee. For example: 

  * Define a default value for a query string parameter or other type of input.
  * Strip HTTP headers from a request message before the message is forwarded to the backend service.
  * Add HTTP headers before a response is sent to the consumer app.
  * Generate customized request or response messages. For example, you might use an external callout to invoke a remote API from an API proxy. You can use the HTTPModifier policy to create a custom request message and assign it to a variable. Then, use an external callout to send that message to the remote API.
  * Add headers to requests and responses for debugging and troubleshooting.



## `<HTTPModifier>` element

Defines an HTTPModifier policy.

**Default Value** | See **Default Policy** tab, below  
---|---  
**Required?** | Required  
**Type** | Complex object  
**Parent Element** |  N/A   
**Child Elements** |  [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add)  
[`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto)  
`<DisplayName>`  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#ignoreunresolvedvariables)  
[`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove)  
[`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
  
  
The `<HTTPModifier>` element uses the following syntax:

### Syntax

The `<HTTPModifier>` element uses the following syntax:
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
        name="POLICY_NAME" >
      <!-- All HTTPModifier child elements are optional -->
      <Add>
        <FormParams>
          <FormParam name="FORMPARAM_NAME">FORMPARAM_VALUE</FormParam>
          ...
        </FormParams>
        <Headers>
          <Header name="HEADER_NAME">HEADER_VALUE</Header>
          ...
        </Headers>
        <QueryParams>
          <QueryParam name="QUERYPARAM_NAME">QUERYPARAM_VALUE</QueryParam>
          ...
        </QueryParams>
      </Add>
    
      <AssignTo createNew="[true|false]" transport="http"
        type="[request|response]">DESTINATION_VARIABLE_NAME</AssignTo>
    
      <DisplayName>POLICY_DISPLAY_NAME</DisplayName>
    
      <IgnoreUnresolvedVariables>[true|false]</IgnoreUnresolvedVariables>
    
      <!-- Can also be empty to remove everything from the message (<Remove/>) -->
      <Remove>
        <!-- Can also be an empty array to remove all FormParams (<FormParams/>) -->
        <FormParams>
          <FormParam name="FORMPARAM_NAME">FORMPARAM_VALUE</FormParam>
          ...
        </FormParams>
        <!-- Can also be an empty array to remove all Headers (<Headers/>) -->
        <Headers>
          <Header name="HEADER_NAME">HEADER_VALUE</Header>
          ...
        </Headers>
        <!-- Can also be an empty array to remove all QueryParams (<QueryParams/>) -->
        <QueryParams>
          <QueryParam name="QUERYPARAM_NAME">QUERYPARAM_VALUE</QueryParam>
          ...
        </QueryParams>
      </Remove>
    
      <Set>
        <FormParams>
          <FormParam name="FORMPARAM_NAME">FORMPARAM_VALUE</FormParam>
          ...
        </FormParams>
        <Headers>
          <Header name="HEADER_NAME">HEADER_VALUE</Header>
          ...
        </Headers>
        <Path>PATH</Path>
        <QueryParams>
          <QueryParam name="QUERYPARAM_NAME">QUERYPARAM_VALUE</QueryParam>
          ...
        </QueryParams>
        <StatusCode>HTTP_STATUS_CODE or {variable}</StatusCode>
        <Verb>[GET|POST|PUT|PATCH|DELETE|{variable}]</Verb>
        <Version>[1.0|1.1|{variable}]</Verb>
      </Set>
    
    </HTTPModifier>

### Default Policy

The following example shows the default settings when you add an HTTPModifier policy to your flow in the Apigee UI:
    
    
    <HTTPModifier continueOnError="false" enabled="true" name=&qu>ot;<http-modifi>er-default"<;
      DisplayN>ame<HTTP Modifi>er-<1/Disp>layNa<me
      Pr>opertie<s/
      Remove
        H>eader<s
          >Heade<r name=&quo>t;h1&qu<ot;/
        /Headers
       > Quer<yParams
        >  Que<ryParam na>me=&quo<t;q1"/
        /Que>ryPar<ams
        For>mPa<rams
      >   < Fo>rmPar<am name=>"<;f1"/
     >   /F<ormParams
     > /R<emov>e
     < Ad>d
       < Headers>/
       < QueryParams>/
       < FormParams>/
      /<Add
    <  Se>t
     <   He>ade>rs/
     <   Qu>ery<Para>ms/<
        FormParams/
        !-- >Verb<GET/Verb --
        Path/
      /S>et
    <  IgnoreUnresolvedVariablestrue/IgnoreUnresolvedVariables
     > <AssignTo crea>teNew="false" transport="http" type="request"/
    /HTTPModifier

When you insert a new HTTPModifier policy in the Apigee UI, the template contains stubs for all possible operations. Typically, you select which operations you want to perform with this policy and remove the rest of the child elements. For example, if you want to perform an add operation, use the `<Add>` element and remove `<Remove>` and other child elements from the policy to make it more readable.

This element has the following attributes that are common to all policies:

**Attribute** | **Default** | **Required?** | **Description**  
---|---|---|---  
`name` | N/A | **Required** |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name.  
`continueOnError` | false | Optional | Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also: 

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

  
`enabled` | true | Optional | Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow.  
`async` not_interested | false | Deprecated | This attribute is deprecated.  
  
The following table provides a high-level description of the child elements of [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier):

Child Element | Required? | Description  
---|---|---  
Common operations  
[`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) | Optional | Adds information _to_ the message object that is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element. `<Add>` adds headers or parameters to the message that don't exist in the original message. Note that [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) also provides this functionality. To overwrite existing headers or parameters, use the [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) element.  
[`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove) | Optional | Deletes the specified elements from the message variable specified in the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.  
[`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) | Optional | Replaces values of existing properties on the request or response, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element. `<Set>` overwrites headers or parameters that already exist in the original message or adds new if they don't.  
Other child elements  
[`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) | Optional | Specifies which message the HTTPModifier policy operates on. This can be the standard request or response, or it can be a new custom message.  
[`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#ignoreunresolvedvariables) | Optional | Determines whether processing stops when an unresolved variable is encountered.  
  
Each of these child elements is described in the sections that follow.

## Examples

The following examples show some of the ways in which you can use the HTTPModifier policy:

### 1: Add header

The following example adds a header to the request with the [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) element. The VerifyAPIKey variable in this example is generated by the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy):
    
    
    <HTTPModifier name="HM-add-heade>rs-<1&q>uot;
    <  Add
     >   Head<ers
          Header name=&q>uot;partner-id"{verifyapikey.VAK-1.devel<oper.ap>p.par<tner-id}>/He<ader>
      <  /Heade>rs
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### 2: Modify response

The following example modifies an existing response object by adding a header to it:
    
    
    <HTTPModifier name="HM-modify-resp>ons<e&q>uot;
    <  Set
     >   Head<ers
          Header name=&>quot;Cache-Hit"{lookupcache.Loo<kupCach>e-1.c<achehit}>/He<ader>
      <  /Headers
      /Set
      Ignor>eUnre<solvedVariablesfalse/Ignor>eUn<resolved>Variable<s
      Assig>n<Toresponse/As>signTo
    /HTTPModifier

This example does not create a new message. Instead, it modifies an existing response message by adding an HTTP header.

Because this example specifies `response` as the variable name in the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element, this policy modifies the response object that was originally set with data returned by the target server.

The HTTP header added to the response message by this policy is derived from a variable populated by the [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy). Therefore the response message modified by this HTTPModifier policy contains an HTTP header that indicates whether the results have been pulled from the cache or not. Setting headers in the response can be handy for debugging and troubleshooting.

**Tip:** This pattern of setting headers for debugging and troubleshooting is a common practice. You can see what header value was sent back by inspecting the response with the Debug tool or other means.

### 3: Remove query param

The following example removes the `apikey` query parameter from the request:
    
    
    <HTTPModifier name="HM-remove-query-p>ara<m">;
      R<emove
        Q>ueryPar<ams
          QueryParam name>=&quo<t;apikey&quo>t;/<
        /Q>uer<yParams
    >  /Remo<ve
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

It's a best practice to strip the `apikey` query parameter from the request message when you use the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) for user authentication. You do this to prevent sensitive key information from being passed to the backend target.

## Child element reference

This section describes the child elements of [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier).

### `<Add>`

Adds information to the request or response, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.

The `<Add>` element adds new properties on the message that don't exist in the original message. Note that [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) also provides this functionality. To change the values of _existing_ properties, use the [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)  
**Child Elements** |  [`<FormParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-formparams)  
[`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-headers)  
[`<QueryParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-queryparams)  
  
  
The `<Add>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>"<;POLICY_NA>ME"<; 
      Add
        FormParams
          F>ormParam name=&<quot;FORMP>ARAM_NAME"<FORMPARAM_V>ALUE/<FormPar>am
        <  ...
        /FormParams
       > Headers
       <   Head>er name="H<EADER_NA>ME&qu<ot;HEADER_V>ALUE/He<ader
          ...
        /Headers
        Q>ueryParams
         < QueryParam> name="QUE<RYPARAM_NAME>&qu<ot;Q>U<ERYPARAM_VALU>E/QueryParam
          ...
        /QueryParams
      /Add
    /HTTPModifier

### Example 1

The following example uses the [`<FormParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-formparams) element to get the values of three query string parameters from the initial request and set them as form parameters on the target endpoint request:
    
    
    <HTTPModifier name="HM-add-formpara>ms-<3&q>uot;
    <  Add
        >FormPar<ams
          FormParam name=>"username"{requ<est.queryp>aram.na<me}/FormParam
          FormP>aram name="zip_code&quo<t;{request>.queryp<aram.zipCode}/FormParam
          For>mParam name="default<_language&>quot;<{request.qu>ery<para>m.l<ang}/F>ormPa<ram
        /For>mPa<rams
      >/Ad<d
      Remo>ve
        <QueryPara>m<s/
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

### Example 2

The following example uses the [`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-headers) element to add a `partner-id` header to the request that will be sent to the target endpoint:
    
    
    <HTTPModifier name="HM-add-heade>rs-<1&q>uot;
    <  Add
     >   Head<ers
          Header name=&q>uot;partner-id"{verifyapikey.VAK-1.devel<oper.ap>p.par<tner-id}>/He<ader>
      <  /Heade>rs
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### Example 3

The following example uses the [`<QueryParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add-queryparams) element to add a single query parameter with a static value to the request:
    
    
    <HTTPModifier name="HM-add-querypara>ms-<1&q>uot;
    <  Add
        Q>ueryPar<ams
          QueryParam name>=&<quot;myPara>m&quo<t;42/QueryPa>ram<
       > /Q<ueryPara>ms
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

This example uses `<Add>` in the request preflow. If you look at the results in a tool such as the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview), the request to `https://example-target.com/get` becomes `https://example-target.com/get?myParam=42`.

The child elements of `<Add>` support dynamic string substitution, known as [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro).

#### `<FormParams>` (child of [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add))

Adds new form parameters to the request message. This element has no effect on a response message.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<FormParam>` elements  
**Parent Element** |  [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add)  
**Child Elements** |  `<FormParam>`  
  
  
The `<FormParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY_NA>ME"<;** 
      Add
        FormParams
          F>ormParam name=&<quot;FORMP>ARAM_NAME"<FORMPARAM_V>ALU<E/FormParam
          ...
        /FormParams
      AssignTo createNew="[true|false]&qu>ot; transport="http&<quot;
       > ty<pe=&>q<uot;[request|>response]"DESTINATION_VARIABLE_NAME/AssignTo
      /Add
    /HTTPModifier

### Example 1

The following example adds a single form parameter (`answer`) and a static value (`42`) to the request:
    
    
    <HTTPModifier name="HM-add-formpara>ms-<1&q>uot;
    <  Add
        >FormPar<ams
          FormParam nam>e=<"answ>er&qu<ot;42/FormP>ara<m
      >  /<FormPara>ms
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### Example 2

The following example gets the value of the `name` query parameter and adds it to the request as a form parameter, and then removes the query parameter:
    
    
    <HTTPModifier name="HM-Swap-QueryParam-to-FormPa>ram<s&q>uot;
    <  Add
        FormParam n>ame="name"{request<.que>ryp<aram.n>ame}
    <  /Add
      Remove
        Que>ryP<aram na>m<e="name&>quot;/
      /Remove
    /HTTPModifier

Note that this example does not specify a target with `<AssignTo>`. This policy adds the parameter to the request only.

### Example 3

The following example adds multiple form parameters to the request:
    
    
    <HTTPModifier name="HM-add-formpara>ms-<3&q>uot;
    <  Add
        >FormPar<ams
          FormParam name=>"username"{requ<est.queryp>aram.na<me}/FormParam
          FormP>aram name="zip_code&quo<t;{request>.queryp<aram.zipCode}/FormParam
          For>mParam name="default<_language&>quot;<{request.qu>ery<para>m.l<ang}/F>ormPa<ram
        /For>mPa<rams
      >/Ad<d
      Remo>ve
        <QueryPara>m<s/
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

This example gets the query string parameters from the originating request and adds them as form parameters with different names. Then it removes the original query parameters. Apigee will send the modified request to the target endpoint.

You can use the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) to look at the flow. You'll see that the body of the request contains the URL-encoded form data, which was originally passed in as query string parameters:
    
    
    username=nick&zip_code=90210&default_language=en

You can use `<FormParams>` only when the following criteria are met:

  * HTTP verbs: `GET`, `POST`
  * Message type: Request
  * One (or both) of the following: 
    * Form data: Set to some value, or `""` (the empty string). For example, with `curl`, add `-d ""` to your request.
    * `Content-Length` header: Set to 0 (if no data is in the original request; otherwise, the current length, in bytes). For example, with `curl` add `-H "Content-Length: 0"` to your request.



For example:
    
    
    curl -vL -X POST -d "" -H "Content-Type: application/x-www-form-urlencoded"
      https://ahamilton-eval-test.apigee.net/am-test

When you add `<FormParams>`, Apigee sets the request's `Content-Type` header to `application/x-www-form-urlencoded` before sending the message to the target service.

#### `<Headers>` (child of [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add))

Adds new headers to the specified request or response, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<Header>` elements  
**Parent Element** |  [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add)  
**Child Elements** |  `<Header>`  
  
  
The `<Headers>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY>_NAME&q<uot; 
      Add
        Headers
     >     Header <name=&q>uot;HEADER_NAME<"HE>**ADE<R_VA>L<UE/Header
       >   ...
        /Headers
      /Add
    /HTTPModifier

### Example 1

The following example adds a `partner-id` header to the request message, and assigns the value of the `verifyapikey.VAK-1.developer.app.partner-id` flow variable to that header.
    
    
    <HTTPModifier name="HM-add-heade>rs-<1&q>uot;
    <  Add
     >   Head<ers
          Header name=&q>uot;partner-id"{verifyapikey.VAK-1.devel<oper.ap>p.par<tner-id}>/He<ader>
      <  /Heade>rs
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

#### `<QueryParams>` (child of [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add))

Adds new query parameters to the request. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<QueryParam>` elements  
**Parent Element** |  [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add)  
**Child Elements** |  `<QueryParam>`  
  
  
The `<QueryParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY_NAM>E"< 
      Add
        QueryParams
          Que>ryParam name=&qu<ot;QUERYPAR>AM_NAME"QU<ERYPARAM_VAL>**UE/<Quer>y<Param
          .>..
        /QueryParams
      /Add
    /HTTPModifier

### Example 1

The following example adds the query parameter `myParam` to the request and assigns the value `42` to it:
    
    
    <HTTPModifier name="HM-add-querypara>ms-<1&q>uot;
    <  Add
        Q>ueryPar<ams
          QueryParam name>=&<quot;myPara>m&quo<t;42/QueryPa>ram<
       > /Q<ueryPara>ms
      /A<dd
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

You can use `<QueryParams>` only when the following criteria are met:

  * HTTP verbs: `GET`, `POST`
  * Message type: Request



In addition, you can only set query parameters when the `<AssignTo>` element's `type` attribute is a request message. Setting them on the response has no effect.

If you define an empty array of query parameters in your policy (`<Add><QueryParams/></Add>`), the policy does not add any query parameters. This is the same as omitting `<QueryParams>`.

### `<AssignTo>`

Determines which object the HTTPModifier policy operates on. The options are:

  * **Request message:** The [`request`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#request) received by the API proxy
  * **Response message:** The [`response`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#response) returned from the target server
  * **Custom message:** A custom request or response object



Note that in some cases, you cannot change the object on which the HTTPModifier policy acts. For example, you cannot use [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) or [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) to add or change query parameters (`<QueryParams>`) or form parameters (`<FormParams>`) on the response. You can only manipulate query parameters and form parameters on the request.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String  
**Parent Element** |  [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)  
**Child Elements** |  None   
  
If you do not specify `<AssignTo>`, or if you specify the `<AssignTo>` element but do not specify a text value for the element, the policy acts on the default request or response, which is based on where the policy executes. If the policy executes in the request flow, it affects the request message. If it executes in the response flow, the policy affects the response by default.

The `<AssignTo>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > **na <me="POLICY_NAME" 
      AssignTo createNew="[true|false]" transp>ort="http"
        <type=&quo>**t<;[request|res>ponse]"DESTINATION_VARIABLE_NAME/AssignTo
    /HTTPModifier

### Example 1

The following example specifies no message in the text of the `<AssignTo>`. That implies that the policy will act on either the `request` or `response` message, depending on where the policy executes.
    
    
    <HTTPModifier name="assign>to-<1"
      AssignTo createNew="false" transport=&q>uot;http" type=&<quot;request&>quot;/<!-- no-op -->
      ...
    /HTTPModifier

If you specify `createNew="false"`, and do not explicitly provide a message name, the other attributes of `<AssignTo>` are irrelevant. In this case, you may wish to omit the `<AssignTo>` element completely.

### Example 2

The following example creates a new request object, over-writing the existing object:
    
    
    <HTTPModifier name="assign>to-<2"
      AssignTo createNew="true" transport=&q>uot;htt<p" type=>"request"/
      ...
    /HTTPModifier

When you create a new request or response object, the other elements of the HTTPModifier policy (such as [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) and [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) act on that new request object.

You can access the new request object in other policies later in the flow, or send the new request object to an external service with a [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).

### Example 3

The following example creates a new request object named `MyRequestObject`:
    
    
    <HTTPModifier name="assign>to-<3"
      AssignTo createNew="true" transport=&>quot;http"< type=&qu>ot;requ<est"MyRe>questObject/AssignTo
      ...
    /HTTPModifier

When you create a new request or response object, the other elements of the HTTPModifier policy (such as [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) and [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) act on that new request object.

You can access the new request object by name in other policies later in the flow, or send the new request object to an external service with a [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).

The following table describes the attributes of `<AssignTo>`:

Attribute | Description | Required? | Type  
---|---|---|---  
`createNew` |  Determines whether this policy creates a new message when assigning values. If `true`, then the policy creates a new variable of the type specified by `type` (either `request` or `response`). If you do not specify the name of the new variable, then the policy creates a new request or response object, based on the value of `type`. **Caution** : When creating a new request or response object, the existing request or response object is deleted and replaced by the new one, meaning all information in the object is lost.If `false`, then the policy responds in one of two ways:

  * If `<AssignTo>` can resolve the variable name to a request or response, then it continues processing. For example, if the policy is in a request flow, the variable is the request object. If the policy is in a response, the variable is the response object.
  * If `<AssignTo>` cannot be resolved, or resolves to a non-message type, then the policy throws an error.

If `createNew` is not specified, the policy responds in one of two ways: 

  * If `<AssignTo>` resolves to a message, then processing advances to the next step.
  * If `<AssignTo>` cannot be resolved, or resolves to a non-message type, a new variable of type specified in `type` is created.

| Optional | Boolean  
`transport` |  Specifies the transport type for the request or response message type. The default value is `http` (the only supported value). | Optional | String  
`type` | Specifies the type of the new message, when `createNew` is `true`. Valid values are `request` or `response`. The default value is `request`. If you omit this attribute, then Apigee creates either a request or a response, depending on where in the flow this policy executes. | Optional | String  
  
### `<DisplayName>`

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, more natural-sounding name.

The `<DisplayName>` element is common to all policies.

**Default Value** | N/A  
---|---  
**Required?** | Optional. If you omit `<DisplayName>`, the value of the policy's `name` attribute is used.  
**Type** | String  
**Parent Element** |  <PolicyElement>  
**Child Elements** |  None   
  
The `<DisplayName>` element uses the following syntax:

### Syntax
    
    
    <_PolicyElement_ >
      **< DisplayName>POLICY_DISPLAY_NAME</DisplayName>**
      ...
    </_PolicyElement_ >

### Example
    
    
    <_PolicyElement_ >
      **< DisplayName>My Validation Policy</DisplayName>**
    </_PolicyElement_ >

The `<DisplayName>` element has no attributes or child elements.

### `<IgnoreUnresolvedVariables>`

Determines whether processing stops when an unresolved variable is encountered.

**Default Value** | False  
---|---  
**Required?** | Optional  
**Type** | Boolean  
**Parent Element** |  [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)  
**Child Elements** |  None   
  
Set to `true` to ignore unresolved variables and continue processing; otherwise `false`. The default value is `false`.

Setting `<IgnoreUnresolvedVariables>` to `true` is different from setting the [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)'s `continueOnError` to `true` in that it is specific to setting and getting values of variables. If you set `continueOnError` to `true`, then Apigee ignores all errors, not just errors encountered when using variables.

The `<IgnoreUnresolvedVariables>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > **na <me="POLICY_NAME">; 
      IgnoreU<nresolvedVariables[true|fa>**l<se]/IgnoreUnr>esolvedVariables
    /HTTPModifier

### Example 1

The following example sets `<IgnoreUnresolvedVariables>` to `true`:
    
    
    <HTTPModifier name="HM-Set-Hea>der<s&q>uot;
    <  Set
     >   Head<ers
          Header name=&#>39;new-header'{possibly<-defin>ed-va<riable}H>ead<er
     >   **< /Headers
      /Set
      IgnoreU>nres<olvedVariablestrue/IgnoreU>**n<resolvedVaria>bles
    /HTTPModifier

Because `<IgnoreUnresolvedVariables>` is set to `true`, if the `possibly-defined-variable` variable is not defined, this policy will not throw a fault. 

### `<Remove>`

Removes headers, query parameters, or form parameters from a message. An empty tag removes all corresponding parameters including headers, formparams, and queryparams.

The affected message can be a request or a response. You specify which message `<Remove>` acts on by using the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)  
**Child Elements** |  [`<FormParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove-formparams)  
[`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove-headers)  
[`<QueryParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove-queryparams)  
  
  
A common use case for `<Remove>` is to delete a query parameter or header that contains sensitive information from the incoming request object, to avoid passing it to the backend server.

The `<Remove>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > **na <me="POLICY_NAME" 
      !-- Can also be empty to remove< everyt>hing fro<m the >messa<ge (Remove/) -->
      Remove
        !-- Can also be an empty< array to r>emove all <FormParams> (FormP<arams/) -->
        FormParams
     >     FormParam <name=">;FORMPARAM_NAME<"FORMP>ARAM_<VALUE/FormParam
          ...
        /FormParams
        !-- Can <also be >an empty a<rray to> remove< all Headers (Headers/) ->->
        He<aders
     >     Header nam<e=">HEADE<R_NAME"HEADER_VALUE/Header
          ...
        /Headers
       < !-- Can als>o be an em<pty array t>o remov<e all QueryParams (QueryParams/) >-->
        Query<Params
        >  QueryParam na<me="QUE>RYP<ARAM_NA>**M<E"QUERYP>ARAM_VALUE/QueryParam
          ...
        /QueryParams
      /Remove
    /HTTPModifier

### Example 1

The following example removes all form parameters and a query parameter from the `request` object:
    
    
    <HTTPModifier name="HM-remo>ve-<2">;
      R<emove
        !<-- Empty (F>ormParams/) removes all form par>amete<rs --
        F>ormPa<rams/
        Q>ueryPar<ams
          QueryParam n>ame=&<quot;qp1&quo>t;/<
        /Q>uer<yParams
    >  /Remo<ve
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### Example 2

The following example removes everything from a message object:
    
    
    <HTTPModifier name="HM-remo>ve-<3">
      <Remove/
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

Typically you would do this only if you were going to use the [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set) element to set some replacement values into the message.

#### `<FormParams>` (child of [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove))

Removes the specified form parameters from the request. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<FormParam>` elements or an empty array  
**Parent Element** |  [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove)  
**Child Elements** |  `<FormParam>`  
  
  
The `<FormParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me="POLICY_NAME" 
      !-- Can also be empty to remove< everyt>hing fro<m the >m**essa <ge** (Remove/) -->
      Remove
        !-- Can also be an empty< array to r>emove all <FormParams> (FormP<arams/) -->
        FormParams
     >     FormParam <name=">;FORMPARAM_NAME<"FORMP>ARA<M_VALUE>/<FormParam
       >   ...
        /FormParams
      /Remove
    /HTTPModifier

### Example 1

The following example removes three form parameters from the request:
    
    
    <HTTPModifier name="HM-remove-formpara>ms-<1">;
      R<emove
        >FormPar<ams
          FormParam name=">;form_p<aram_1"/
          FormParam >name=&q<uot;form_param_2"/
          >FormP<aram name=&>quo<t;form_>par<am_3&quo>t;/
       < /FormPar>a<ms
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

### Example 2

The following example removes all form parameters from the request:
    
    
    <HTTPModifier name="HM-remove-formpara>ms-<2">;
      R<emove
        F>orm<Params/>
      </Remove
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

### Example 3

If there are multiple form params with the same name, use the following syntax:
    
    
    <HTTPModifier name="HM-remove-formpara>ms-<3">;
      R<emove
        >FormPar<ams
          FormParam >name=&q<uot;f1"/
          >FormPar<am name="f2">/
       <   FormPara>m n<ame=&qu>ot;<f3.2&quo>t;/
       < /FormPar>a<ms
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

This example removes `f1`, `f2`, and the second value of `f3`. If `f3` has only one value, then it is not removed.

You can use `<FormParams>` only when the following criteria are met:

  * Message type: Request
  * `Content-Type`: `application/x-www-form-urlencoded`



#### `<Headers>` (child of [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove))

Removes the specified HTTP headers from the request or response, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<Header>` elements or an empty array  
**Parent Element** |  [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove)  
**Child Elements** |  `<Header>`  
  
  
The `<Headers>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me="POLICY_NAME" 
      !-- Can also be empty to remove< everyt>hing fro<m the >m**essa <ge** (Remove/) -->
      Remove
        !-- Can also be an em<pty arra>y to remov<e all H>eaders <(Headers/) -->
        Hea>ders
          H<eader n>ame="HEADE<R_NAME&q>uot<;HEADER>_<VALUE/Header
    >      ...
        /Headers
      /Remove
    /HTTPModifier

### Example 1

The following example removes the `user-agent` header from the request:
    
    
    <HTTPModifier name="HM-remove-one-he>ade<r">;
      R<emove
     >   Head<ers
          Header name=&qu>ot;us<er-agent>&qu<ot;/
      >  /<Headers
    >  /Remo<ve
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### Example 2

The following example removes all headers from the request:
    
    
    <HTTPModifier name="HM-remove-all-hea>der<s">;
      R<emove
      >  H<eaders/>
      </Remove
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

### Example 3

If there are multiple headers with the same name, use the following syntax:
    
    
    <HTTPModifier name="HM-remove-heade>rs-<3">;
      R<emove
     >   Head<ers
          Header >name=&q<uot;h1"/
       >   Head<er name="h2&qu>ot;/
    <      He>ade<r name=>&qu<ot;h3.2&>quot;/
    <    /Head>e<rs
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

This example removes `h1`, `h2`, and the second value of `h3` from the request. If `h3` has only one value, then it is not removed.

#### `<QueryParams>` (child of [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove))

Removes the specified query parameters from the request. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<QueryParam>` elements or an empty array  
**Parent Element** |  [`<Remove>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#remove)  
**Child Elements** |  `<QueryParam>`  
  
  
The `<QueryParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me="POLICY_NAME" 
      !-- Can also be empty to remove< everyt>hing fro<m the >m**essa <ge** (Remove/) -->
      Remove
        !-- Can also be an empty <array to rem>ove all Qu<eryParams (>QueryPa<rams/) -->
        QueryParams
       >   QueryParam na<me="QU>ERYPARAM_NAME&q<uot;QUERYPAR>AM_<VALUE/Q>u<eryParam
        >  ...
        /QueryParams
      /Remove
    /HTTPModifier

### Example 1

The following example removes a single query parameter from the request:
    
    
    <HTTPModifier name="HM-remove-querypara>ms-<1">;
      Rem<ove
          Q>ueryParam<s
            QueryParam n>ame=&qu<ot;qp1">/
     <     /Q>uer<yParams
    >  /Remo<ve
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

### Example 2

The following example removes all query parameters from the request:
    
    
    <HTTPModifier name="HM-remove-querypara>ms-&tl;2">;
      Rem<ove
          Qu>ery<Params/>
      </Remove
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

### Example 3

If there are multiple query params with the same name, use the following syntax:
    
    
    <HTTPModifier name="HM-remove-querypara>ms-<3">;
      Rem<ove
          Q>ueryParam<s
            QueryParam n>ame="<;qp1"/
            Qu>eryParam <name="qp2"/
      >      Q<ueryParam na>me=<"q>p3.<2"/>
          </QueryPar>a<ms
      /Remove
    >  AssignTorequest/AssignTo
    /HTTPModifier

This example removes `qp1`, `qp2`, and the second value of `qp3` from the request. If `qp3` has only one value, then it is not removed.

### Example 4

The following example removes the `apikey` query parameter from the request:
    
    
    <HTTPModifier name="HM-remove-query-p>ara<m">;
      R<emove
        Q>ueryPar<ams
          QueryParam name>=&quo<t;apikey&quo>t;/<
        /Q>uer<yParams
    >  /Remo<ve
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

You can use `<QueryParams>` only when the following criteria are met:

  * HTTP verbs: `GET`, `POST`
  * Message type: Request



### `<Set>`

Sets information in the request or response message, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element. `<Set>` overwrites headers or query or form parameters that already exist in the original message or adds new if they don't.

Headers and query and form parameters in an HTTP message may hold multiple values. To add additional values for a header or parameter, use the [`<Add>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#add) element instead.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Complex type  
**Parent Element** |  [`<HTTPModifier>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#httpmodifier)  
**Child Elements** |  [`<FormParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-formparams)  
[`<Headers>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-headers)  
[`<Path>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-path)  
[`<QueryParams>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-queryparams)  
[`<StatusCode>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-statuscode)  
[`<Verb>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-verb)  
[`<Version>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-version)  
  
**Note** : The sub-elements of `<Set>` support the dynamic string substitution feature called [message templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro). 

The `<Set>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > **na <me=>"<;POLICY_NA>ME"<; 
      Set
        FormParams
          F>ormParam name=&<quot;FORMP>ARAM_NAME"<FORMPARAM_V>ALUE/<FormPar>am
        <  ...
        /FormParams
       > Headers
       <   Head>er name="H<EADER_NA>ME&qu<ot;H>EADE<R_VAL>UE/He<ader
          >...
       < /Headers
        PathPATH/Path
        Q>ueryParams
         < QueryParam> name="QUE<RYPARAM_NAME>"<;QUERYPARA>M_VALUE/QueryParam
          ...
     <   /QueryPa>rams
    <    >StatusCodeHTTP_STATUS_CODE or {variabl<e}/St>atusC<ode
       > Verb[GET|POST|PUT|P<ATCH|>DEL<ETE|>**{<variable}]/Ve>rb
        Version[1.0|1.1|{variable}]/Verb
      /Set
    /HTTPModifier

### Example

The following example sets a specific header. When this policy is attached in the Request flow, it will allow the upstream system to receive an additional header that was not included in the original inbound request.
    
    
    <HTTPModifier name="HM-Set-He>ade<r&q>uot;
    <  Set
     >   Header<s
            Header name="authentic>ated-developer"{verifyapikey<.VAK-1.>devel<oper.id}>/He<ader>
      <  /Heade>rs
      /S<et
      Assi>g<nTorequest/As>signTo
    /HTTPModifier

#### `<FormParams>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Overwrites existing form parameters on a request and replaces them with the new values that you specify with this element. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<FormParam>` elements  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  `<FormParam>`  
  
  
The `<FormParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY_NA>ME"<; 
      Set
        FormParams
          F>ormParam name=&<quot;FORMP>ARAM_NAME"<FORMPARAM_V>**ALU<E/Fo>r<mParam
          >...
        /FormParams
      /Set
    /HTTPModifier

### Example 1

The following example sets a form parameter called `myparam` to the value of the `request.header.myparam` variable in a new, custom request:
    
    
    <HTTPModifier name="HM-set-formpara>ms-<1&q>uot;
    <  Set
        >FormPar<ams
          FormParam name>="myparam"{req<uest.heade>r.myp<aram}/FormP>ara<m
      >  /<FormParams
      /Set
      AssignTo createNew="true" >>transport="<;http&quo>t<; type=">requestMyCustomRequest/AssignTo
    /HTTPModifier

You can use `<FormParams>` only when the following criteria are met:

  * HTTP verb: `POST`
  * Message type: Request



If you define empty form parameters in your policy (`<Add><FormParams/></Add>`), the policy does not add any form parameters. This is the same as omitting the `<FormParams>`.

`<Set>` changes the `Content-Type` of the message to `application/x-www-form-urlencoded` before sending it to the target endpoint.

#### `<Headers>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Overwrites existing HTTP headers in the request or response, which is specified by the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<Header>` elements  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  `<Header>`  
  
  
The `<Headers>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY>_NAME&q<uot; 
      Set
        Headers
     >     Header <name=&q>uot;HEADER_NAME<"HE>**ADE<R_VA>L<UE/Header
       >   ...
        /Headers
      /Set
    /HTTPModifier

### Example 1

The following example sets the `x-ratelimit-remaining` header to the value of the `ratelimit.Quota-1.available.count` variable:
    
    
    <HTTPModifier name="HM-Set-RateLimit-He>ade<r&q>uot;
    <  Set
     >   Head<ers
          Header name="X-RateL>imit-Remaining"{ratelimit.Quot<a-1.ava>ilabl<e.count}>/He<ader>
      <  /Heade>rs
      /Se<t
      Assig>n<Toresponse/As>signTo
    /HTTPModifier

If you define empty headers in your policy (`<Set><Headers/></Set>`), the policy does not set any headers. This will have the same effect as omitting `<Headers>`.

#### `<Path>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

**Note** : 

This element isn't currently working as designed to override/rewrite a proxy's target URL.

Sometimes you may need to send a message to a URL other than the URL defined in an API proxy's `TargetEndpoint`. (You can't override `target.url` in the `ProxyEndpoint`, because Apigee sets the variable in the `TargetEndpoint`).

#### `<QueryParams>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Overwrites existing query parameters in the request with new values. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | Array of `<QueryParam>` elements  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  `<QueryParam>`  
  
  
The `<QueryParams>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY_NAM>E"< 
      Set
        QueryParams
          Que>ryParam name=&qu<ot;QUERYPAR>AM_NAME"QU<ERYPARAM_VAL>**UE/<Quer>y<Param
          .>..
        /QueryParams
      /Set
    /HTTPModifier

### Example 1

The following example sets the `address` query parameter to the value of the `request.header.address` variable:
    
    
    <HTTPModifier name="HM-set-querypara>ms-<1&q>uot;
    <  Set
        Q>ueryPar<ams
          QueryParam name>="address"{req<uest.header>.addr<ess}/QueryPa>ram<
       > </QueryParams
    >  /Set
    /HTTPModifier

You can use `<QueryParams>` only when the following criteria are met:

  * HTTP verbs: `GET`, `POST`
  * Message type: Request



If you define empty query parameters in your policy (`<Set><QueryParams/></Set>`), the policy does not set any query parameters. This is the same as omitting `<QueryParams>`.

#### `<StatusCode>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Sets the status code on the response. This element has no effect on a request.

**Default Value** | '200' (when [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto)'s `createNew` attribute is set to 'true')  
---|---  
**Required?** | Optional  
**Type** | String or VARIABLE  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  None   
  
The `<StatusCode>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY_NA>ME"** 
      Set
        StatusCode<HTTP_STATUS>_CO<DE o>r< {variable}/S>tatusCode
      /Set
    /HTTPModifier

### Example 1

The following example sets a simple status code:
    
    
    <HTTPModifier name="HM-set-statuscode>-40<4&q>uot;
    <  Set
        >Stat<usCode404&>lt;<Stat>usC<ode
      /S>et
      Ass<ignToresp>o<nse/AssignTo
    >/HTTPModifier

### Example 2

The content of `<StatusCode>` is treated as a message template. This means a variable name wrapped in curly braces will be replaced at runtime with the value of the referenced variable, as the following example shows:
    
    
    <HTTPModifier name="set-statusco>de-<2&q>uot;
    <  Set
        >StatusCode{calloutresponse.st<atus.code}/>Sta<tusC>ode<
      /Set
    >  Assign<Torespons>e</AssignTo
    /HT>TPModifier

You can use `<StatusCode>` only when the following criteria are met:

  * Message type: Response



#### `<Verb>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Sets the HTTP verb on the request. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String or VARIABLE  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  None   
  
The `<Verb>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POL>ICY_NAME"** 
      Set
        Verb[GET|POS<T|PUT>|PA<TCH|>D<ELETE|{variab>le}]/Verb
      /Set
    /HTTPModifier

### Example 1

The following example sets a simple verb on the request:
    
    
    <HTTPModifier name="HM-set-ve>rb-<1&q>uot;
    <  Se>t
      <  Ver>bPO<ST/V>erb<
      /Set
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

### Example 2

The content of `<Verb>` is treated as a message template. This means a variable name wrapped in curly braces will be replaced at runtime with the value of the referenced variable.

The following example uses a variable to populate a verb:
    
    
    <HTTPModifier name="HM-set-verb-to-dynamic-v>alu<e&q>uot;
    <  Se>t
        Verb{my<_vari>abl<e}/V>erb<
      /Set
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

You can use `<Verb>` only when the following criteria are met:

  * Message type: Request



#### `<Version>` (child of [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set))

Sets the HTTP version on a request. This element has no effect on a response.

**Default Value** | N/A  
---|---  
**Required?** | Optional  
**Type** | String or VARIABLE  
**Parent Element** |  [`<Set>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set)  
**Child Elements** |  None   
  
The `<Version>` element uses the following syntax:

### Syntax
    
    
    <HTTPModifier
        continueOnError="[false|true]"
        enabled="[true|false]"
       > na<me=>&**quot <;POLICY>_NAME"** 
      Set
     <   Ve>rsi<on[1>.<0|1.1|{variab>le}]/Verb
      /Set
    /HTTPModifier

### Example 1

The following example sets the version number to `1.1`:
    
    
    <HTTPModifier name="HM-set-versi>on-<1&q>uot;
    <  Set
     >   <Version1>.1/<Vers>i<on
      /Set
    /HT>TPModifier

### Example 2

The following uses a variable in curly braces to set the version number:
    
    
    <HTTPModifier name="HM-set-versi>on-<2&q>uot;
    <  Set
     >   Version{m<y_versio>n}/<Vers>ion<
      /Set
    >  Assig<nToreques>t</AssignTo
    /HT>TPModifier

The content of `<Version>` is treated as a message template. This means a variable name wrapped in curly braces will be replaced at runtime with the value of the referenced variable.

You can use `<Version>` only when the following criteria are met:

  * Message type: Request



## Create custom request messages

You can use HTTPModifier to create a custom request message. After you create a custom request, you can use it in the following ways:

  * Access its variables in other policies
  * Pass it to an external service

**Note** : You cannot pass a custom request message to the target endpoint in the flow. Apigee only passes the _original request_ (with any modifications you might have made) to the target endpoint.

To create a custom request message, use the [`<AssignTo>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#assignto) element in your HTTPModifier policy. Set `createNew` to `true` and specify the name of the new message in the body of the element, as the following example shows:
    
    
    <HTTPModifier name="assign>to-3&<quot;
        AssignTo createNew="true" transport=&>quot;http"< type=&qu>ot;request&<quot;MyReques>tObject/AssignTo
        ...
      /HTTPModifier

By default, Apigee does nothing with the custom request message. After creating it, Apigee will continue through the flow with the original request. To use the custom request, add a policy such that uses the request message and explicitly reference the newly created request message in the configuration for that policy. This would allow you to pass the custom request to an external service endpoint.

The following examples create custom request messages:

### Example 1

The following example creates a custom request object with HTTPModifier:
    
    
    <HTTPModifier name="HTTPModifi>er-<3"
      AssignTo createNew="true&>quot; type=&quo<t;request>&qu<ot;>MyCus<tomRequest/>AssignT<o
      Set
        QueryParams
     >     QueryParam name=&quo<t;address&q>uot;{<request.quer>ypara<m.ad>dy}</Quer>yPa<ram<>/span>
       < /QueryParams
        VerbGET>/Verb<
      /Set
      IgnoreUnresolved>V<ariablesfalse>/IgnoreUnresolvedVariables
    /HTTPModifier

This example:

  * Creates a new request message object called `MyCustomRequest`.
  * On MyCustomRequest, this policy: 
    * Sets the `address` query parameter on the custom message to the value of the incoming request's `addy` query parameter.
    * Sets the HTTP verb to `GET`.
  * Sets [`<IgnoreUnresolvedVariables>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#ignoreunresolvedvariables) to `false`. When `<IgnoreUnresolvedVariables>` is `false`, if one of the variables referenced in the policy configuration does not exist, Apigee will enter [fault state](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#howerrorsoccur) in the API flow.



### Example 2

Here's another example demonstrating how to create a custom request object with HTTPModifier:
    
    
    <HTTPModifier name="HTTPModifi>er-<2"
      AssignTo createNew="true&>quot; type=&quo<t;request>&qu<ot;>partn<er.r>eque<st/As>sig<nTo<>/span>
     < Set
        Verb>POST/Verb
      /Set
    /HTTPModifier

This example creates a new custom request called `partner.request`. It then sets the [`<Verb>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy#set-verb) on the new request.

You can access the various properties of a custom message in another HTTPModifier policy that occurs later in the flow. The following example gets the value of a header from a named custom response, and places it into a new header in the request message:
    
    
    <HTTPModifier name="HM-Set-He>ade<r"
    >  Assig<nToreques>t/A<ssi>gnTo
    <  Set
     >   Head<ers
          Header name="inject>ed-approval-id"{MyCalloutResponse<.header>.appr<oval-id}>/He<ader>
    <    /Headers
    >  /Set
    /HTTPModifier

## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the **Fix** column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`entities.UnresolvedVariable` | `500` | Message Template Variable in Undefined or out of scope.  
`steps.httpmodifier.InvalidStatusCode` | `500` | The resolved value of the status code is not valid. See the fault string for more information. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/http-modifier-runtime-errors#unresolvedvariable)  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ next to the error's cause description to visit the troubleshooting page. Error name | Cause | Fix  
---|---|---  
`InvalidIndex` | If the index specified in the `<Remove>` elements of the `HTTPModifier` policy is `0` or a negative number, then deployment of the API Proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/http-modifier-deployment-errors#invalidindex)  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`httpmodifier.POLICY_NAME.failed` | POLICY_NAME is the user-specified name of the policy that threw the fault. | `httpmodifier.HM-SetResponse.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
       "fault":{
          "detail":{
             "errorcode":"steps.httpmodifier.InvalidStatusCode"
          },
          "faultstring":"HTTPModifier[HM-SetResponse]: Invalid status code bad_request"
       }
    }

### Example fault rule
    
    
    <FaultRule name="HTTPModifier Faults">
        <Step>
            <Name>HM-CustomNonMessageTypeErrorResponse</Name>
            <Condition>(fault.name Matches "InvalidStatusCode")</Condition>
        </Step>
        <Condition>(httpmodifier.failed = true)</Condition>
    </FaultRule>

## Schemas

Each policy type is defined by an XML schema (`.xsd`). For reference, [policy schemas](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) are available on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-24 UTC."],[],[]] 
