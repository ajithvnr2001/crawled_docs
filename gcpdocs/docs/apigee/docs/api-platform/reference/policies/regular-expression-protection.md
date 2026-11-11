---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection/
title: RegularExpressionProtection policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:11:39.174158+00:00
---

# RegularExpressionProtection policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  RegularExpressionProtection policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The RegularExpressionProtection policy extracts information from a message (for example, URI path, query parameter, header, form parameter, variable, XML payload, or JSON payload) and compares the value to regular expressions designed to identify threats. If any regular expression comparison evaluates to true, the policy throws a fault.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

**Note:** Instructions on this page assume a proficiency with regular expressions. You can find regular expression examples and other guidance for using regular expressions in Apigee in [Pattern matching with conditionals](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#patternmatching). 

### Samples

### GitHub

The [regex-protection sample on GitHub](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/regex-protection) illustrates how to trap potential SQL injection attacks issued through a query parameter that might contain malicious code in a `<script>` tag. The sample also illustrates a good practice of setting a generic 400 error status to prevent hackers from gaining any useful information from the response.

### JavaScript include attack protection
    
    
    <RegularExpressionProtection name="JsonPathRegExProtec>tion&<quot;<>/span>
        Sou<rcerequ>est/S<ource
        JSONPayload escapeSlashCharac>ter=&quo<t;true&q>uot;
          < JSONPath
    > <         Ex>pression$/E<xpressi><on
          <    Pattern![>CD>AT<A[< \s*script\b[^]*[>^]+><\s*\/\s*>script\s<* ]]/Patt>ern
     <      /JSONP>at<h
        /JSONPayload
     /Regular>ExpressionProtection

The sample above illustrates how to use the RegularExpressionProtection policy to evaluate JSON payloads for JavaScript include attacks. Specifically, the content extracted by `<JSONPath>`/`<Expression>` is evaluated against the regular expression in `<JSONPath>`/`<Pattern>`.

If the regular expression in your `<JSONPath>`/`<Pattern>` includes XML-reserved characters (", &, ', <, or >), you must wrap it in a CDATA (character data) section, as shown in the sample above, or XML-encode the reserved characters: for example, by replacing `<` with `&lt;` and `>` with `&gt;`. 

Additionally, if your regular expression includes forward slashes (/), you must escape them by setting the `<JSONPayload>` `escapeSlashCharacter` attribute to `true`.

### Case insensitive matching

It's a common use case to do case-insensitive matching. Here's an example of how you can accomplish that in a regular expression using the construct `(?i)`. In this example, for instance, `DELETE`, `delete`, and `Delete` will evaluate to true. 
    
    
    <Pattern>[\s]*(?i)((delete)|(exec)|(drop\s*table)|(insert)|(shutdown)|(update)|(\bor\b))</Pattern>

### Form parameter checks
    
    
    <RegularExpressionProtection name="REP-Formp>ara<m">;
      Sou<rcerequ>est</Source
      IgnoreUnresolve>dVari<ablesfalse/IgnoreUnresolve>dVa<riables
      FormParam name=&>quot;<firstna><me"
        P&att><ern![CDA>TA[<[-+=$%]]]/>Pat<tern
      /FormParam
      FormP>aram <name=&q><uot;lastname&q&uot><;
        Pa>tte<rn![CDATA[>[<-+=$%]]]/Pattern
      /FormPara>m
    /RegularExpressionProtection

This RegularExpressionProtection policy configuration will evaluate form parameters for the occurrence of special chatacters, within the set `[-+=$%&]`. This policy will have an effect only when the content-type header in the request is `application/x-www-form-urlencoded`. The policy configuration uses a CDATA (character data) section to wrap the regular expressions, because of the presence of the & character, which is special in XML. 

* * *

## About the Regular Expression Protection policy

Apigee enables you to configure _regular expressions_ that can be evaluated against API traffic at runtime to identify common content-level threats that follow certain patterns.

A _regular expression_ , or _regex_ for short, is a set of strings that specify a pattern in a string. Regular expressions enable content to be programmatically evaluated for patterns. Regular expressions can be used, for example, to evaluate an email address to ensure that it is properly structured. For more information, see [Regular Expressions](https://docs.oracle.com/javase/tutorial/essential/regex/intro.html) in the Java Tutorials.

The most common usage of RegularExpressionProtection is the evaluation of JSON and XML payloads for malicious content.

No regular expression can eliminate all content-based attacks, and multiple mechanisms should be combined to enable defense-in-depth. This section describes some recommended patterns for excluding content.

### Example exclusion patterns

Regular expressions must be XML-encoded in the policy's XML configuration file. See also [Antipattern: Use greedy quantifiers in the RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/greedy-quantifiers). 

Name | Regular Expression  
---|---  
SQL Injection | 
    
    
    [\s]*((delete)|(exec)|(drop\s*table)|(insert)|(shutdown)|(update)|(\bor\b))  
  
Server-Side Include Injection | 
    
    
    <!--#(include|exec|echo|config|printenv)\s+.*

XML encoded:
    
    
    &lt;!--#(include|exec|echo|config|printenv)\s+.*  
  
XPath Abbreviated Syntax Injection | 
    
    
    (/(@?[\w_?\w:\*]+(\[[^]]+\])*)?)+  
  
XPath Expanded Syntax Injection | 
    
    
    /?(ancestor(-or-self)?|descendant(-or-self)?|following(-sibling))  
  
JavaScript Injection | 
    
    
    <\s*script\b[^>]*>[^<]+<\s*/\s*script\s*>

XML encoded:
    
    
    &lt;\s*script\b[^&gt;]*&gt;[^&lt;]+&lt;\s*/\s*script\s*&gt;  
  
###  Set the Content-Type header in a request with an XML or JSON payload

The payload of the Regular Expression Protection policy can include the following elements:

  * `<XMLPayload>` element: Specifies that information needs to be extracted from an XML payload and evaluated against the regular expression provided. 

If you use `<XMLPayload>` in the policy, the `Content-Type` header of the request must be an XML content-type such as `application/xml` or `text/xml`.

  * `<JSONPayload>` element: Specifies that information needs to be extracted from a JSON payload and evaluated against the regular expression provided. 

If you use `<JSONPayload>` in the policy, the `Content-Type` header of the request must be a JSON content-type such as `application/json`.




Typically you design an API to accept either XML or JSON. However, there could be a scenario where the API accepted both. You could then define a Regular Expression Protection policy that uses both the `<XMLPayload>` and `<JSONPayload>` elements. Only one element would apply for a specific request based on the value of the `Content-Type` header.

## Element reference

The element reference describes the elements and attributes of the RegularExpressionProtection policy.

**NOTE:** In this topic "`REGEX PATTERN`" stands in for a valid Regular Expression pattern used to perform the desired matching. Apigee follows the same Regex rules as the classes in the [java.util.regex package](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) in the Java language.
    
    
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name=&qu>ot;R<egular-Expr>ession-Protection-1"
       Di<splayNameReg>ular< Expre>ssion Pr<otectio>n 1/<DisplayName
       Sourceresp>onse/<Source
       IgnoreUnresolved>Vari<ablesfa>lse/Ig<noreUnr>esolvedVariab<les
       U>RIPath<
         P>atternREGEX P<ATTERN/P>atte<rn
         >Patt<ernREGEX PATTERN/Pattern
       /UR>IPath
    <   Quer>yParam name=&<quot;a-q>uery-p<aram&qu>ot;
         Patt<ernREGEX> PAT<TERN/Patter>n
      <   PatternREGEX PATTER>N/Patt<ern
       >/QueryParam
     <  Header> name=<"a>-header"<
         Pa>tter<nREGEX >PATT<ERN/Pattern
         PatternREGEX> PATTE<RN/Patt>ern
       /Heade<r
       For>mParam< name=&>quot;a-form-p<aram&quo>t;
     <    Patter>nREG<EX PATTERN/Pattern
         Pattern>REGEX <PATTERN>/Pattern
       /<FormPara>m
       V<ariable> name="r<equest.c>onte<nt"<>/span>
        < PatternRE>GEX PA<TTERN/Patt>ern
        < PatternREGEX PATTERN/Pat>tern
       /Variable
       <XMLPayload>
         <Namespaces
    >      < Name>space pr<efix=">;apigee"http://www.apig<ee.com/Name>space
      <   />Namesp<aces<>/span>
         XPa<th
        >   Expression</apigee:>Greeting</apigee>:User/Express<ion
        >   Typ<estrin>g/Ty<pe
           P>atte<rnREGEX PAT>TERN/P<attern
     >      Pa<tternREGEX> PATTERN/Pattern
         </XPath
       />XMLPaylo<ad
       J>SONPayload
      <   JSONP>ath
        <   Expr>ession$.store<.book[*]>.autho<r/Express>ion
     <      Patter>n<REGEX PATTERN/Pattern
          > PatternREGEX PATTERN/Pattern
         /JSONPath
        /JSONPayload
    /RegularExpressionProtection

## <RegularExpressionProtection> attributes
    
    
    <RegularExpressionProtection async="false" continueOnError="false" enabled="true" name=&qu>ot;Regular-Expression-Protection-1"

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <Source> element

Indicates the message from which information needs to be extracted.

If the `<Source>` element is omitted, the value defaults to `message`. For example, `<Source>message</Source>`. When set to `message`, the policy uses the request message as source when attached to a request flow. Likewise, the policy uses the response message when attached to a response flow.

If the source message cannot be resolved or if it resolves to a non-message type, the policy returns an error.
    
    
    <Source>response</Source>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
## <IgnoreUnresolvedVariables> element

Determines whether the policy returns an error when it encounters a variable that is unresolvable.

If set to `false` (the default), the policy returns an error when an unresolvable variable is encountered. If set to `true`, the unresolved variable is treated as empty string (Null).
    
    
    <IgnoreUnresolvedVariables>false</IgnoreUnresolvedVariables>

**Default:** | false  
---|---  
**Presence:** | Optional  
**Type:** | Boolean  
  
## <URIPath> element

Specifies that information needs to be extracted from the request URI path and evaluated against the regular expressions provided. You must provide at least one `<Pattern>` element specifying a regular expression pattern to match.
    
    
    <URIPath>
      <Pattern>REGEX PATTERN</Pattern>
      <Pattern>REGEX PATTERN</Pattern>
    </URIPath>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
## <QueryParam> element

Specifies that information needs to be extracted from the request query parameter and evaluated against the regular expressions provided. You must provide at least one `<Pattern>` element specifying a regular expression pattern to match.
    
    
    <QueryParam name="a-query-p>ara<m">
      PatternREG<EX PATTE>RN/<Pattern>
      PatternREG<EX PATTE>R<N/Pattern
    />QueryParam

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name | Name of the request query parameter from which information needs to be extracted for evaluation against the regular expressions provided.  | N/A | Required  
  
## <Header> element

Specifies that information needs to be extracted from the request and response headers and evaluated against the regular expressions provided. You must provide at least one `<Pattern>` element specifying a regular expression pattern to match.
    
    
    <Header name="a-he>ade<r">
      PatternREG<EX PATTE>RN/<Pattern>
      PatternREG<EX PATTE>R<N/Patte>rn
    /Header

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name |  Name of the request and response header from which information needs to be extracted for evaluation against the regular expressions provided. | N/A | Required  
  
## <FormParam> element

Specifies that information needs to be extracted from the request form parameter and evaluated against the regular expressions provided. You must provide at least one `<Pattern>` element specifying a regular expression pattern to match.
    
    
    <FormParam name="a-form-p>aram<"
    >   PatternREG<EX PATTE>RN/P<attern
    >   PatternREG<EX PATTE>R<N/Pattern
    >/FormParam

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name |  Name of the request form parameter from which information needs to be extracted for evaluation against the regular expressions provided. | N/A | Required  
  
## <Variable> element

Specifies that information needs to be extracted from the given variable and evaluated against the regular expressions provided.
    
    
    <Variable name="request.con>tent<"
    >   PatternREG<EX PATTE>RN/P<attern
    >   PatternREG<EX PATTE>R<N/Pattern>
    /Variable

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
name |  Name of the variable from which information needs to be extracted for evaluation against the regular expressions provided. | N/A | Required  
  
## <XMLPayload> element

Specifies that information needs to be extracted from an XML payload and evaluated against the regular expressions provided.
    
    
    <XMLPayload>
       <Namespaces>
          <Namespace prefix="ap>igee"http://www.<apigee.com>/Nam<espace
       />Name<space>s
       XP<ath
          >Expression/apigee:Greeting/a<pigee:User/>Express<ion<>/span>
          <Types>tring/T<ype
       >   PatternREG<EX PATTE>RN/Patt<ern
       >   PatternREG<EX PATTE>RN/P<attern>
    <   /XPath
    />XMLPayload

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
## <XMLPayload>/<Namespaces> element

Specifies the namespaces to be used in the XPath evaluation.
    
    
    <XMLPayload>
       <Namespaces>
          <Namespace prefix="ap>igee"http://www.<apigee.com>/Nam<espace
       />Name<space>s
       XP<ath
          >Expression/apigee:Greeting/a<pigee:User/>Express<ion<>/span>
          <Types>tring/T<ype
       >   PatternREG<EX PATTE>RN/Patt<ern
       >   PatternREG<EX PATTE>RN/P<attern>
    <   /XPath
    />XMLPayload

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
##  <XMLPayload>/<Namespaces>/<Namespace> element

Specifies each namespace to be used in the XPath evaluation.  

    
    
    <Namespaces>
       <Namespace prefix="ap>igee"http://www.<apigee.com>/<Namespace
    />Namespaces

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
prefix |  Provides a prefix to help qualify a given namespace. | N/A | Required  
  
## <XMLPayload>/<XPath> element

Specifies the XPath to be evaluated.  

    
    
    <XPath>
       <Expression>/apigee:Greeting/apigee:User</Expression>
       <Type>string</Type>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </XPath>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
## <XMLPayload>/<XPath>/<Expression> element

Specifies the XPath expression defined for the variable. Only XPath 1.0 expressions are supported. For example, `<Expression>/company/employee[@age>=$request.header.age]</Expression>` extracts details for employees whose age is greater than or equal to the value specified in `request.header.age`.  

    
    
    <XPath>
       <Expression>/apigee:Greeting/apigee:User</Expression>
       <Type>string</Type>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </XPath>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
## <XMLPayload>/<XPath>/<Type> element

Specifies the desired output data type.

Usually you will use "string" or "nodeset". Use "string" if you are certain that your xpath query will result in at most one value, or if you want to check at most one value. If your xpath query may return multiple values, specify "nodeset" to check all the values. 

For example, consider the XPath expression `//*/@*`. It matches all attributes on all elements. If you specify "string" as the `Type`, Apigee will coerce the result of this query to a single string; it will be the value of one of the attributes on one of the elements in the XML document, but which attribute and which element is not defined. Apigee will then perform pattern matching against the value of just that single attribute. This is probably not what you want.

Conversely, if you specify "nodeset" as the `Type` for that XPath expression, Apigee will perform pattern matching against each of the attribute values on each element in the XML document.
    
    
    <XPath>
       <Expression>/apigee:Greeting/apigee:User</Expression>
       <Type>string</Type>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </XPath>

**Default:** | string  
---|---  
**Presence:** | Optional  
**Type:** | String  
**Valid values:** |  One of these keywords: `string`, `boolean`, `int`, `long`, `float`, `double`, and `nodeset`.  
  
## <XMLPayload>/<XPath>/<Pattern> element

Defines the regular expression pattern. If a regular expression in your`<Pattern>` element includes XML-reserved characters (", &, ', <, or .), you must XML-encode it before you include it.
    
    
    <XPath>
       <Expression>/apigee:Greeting/apigee:User</Expression>
       <Type>string</Type>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </XPath>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | String  
  
## <JSONPayload> element

Specifies that information needs to be extracted from a JSON payload and evaluated against the regular expressions provided.
    
    
    <JSONPayload>
       <JSONPath>
          <Expression>$.store.book[*].author</Expression>
          <Pattern>REGEX PATTERN</Pattern>
          <Pattern>REGEX PATTERN</Pattern>
       </JSONPath>
    </JSONPayload>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | N/A  
  
### Attributes

Attribute | Description | Default | Presence  
---|---|---|---  
escapeSlashCharacter |  Set to `true` to escape any forward slash (/) characters in the regular expressions in `<JSONPath>`/`<Pattern>`. | true | Optional  
  
##  <JSONPayload>/<JSONPath>/<Expression> element

Specifies the JSONPath expression defined for the variable.
    
    
    <JSONPath>
       <Expression>$.store.book[*].author</Expression>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </JSONPath>

**Default:** | N/A  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
## <JSONPayload>/<JSONPath>/<Pattern> element

Defines the regular expression pattern. If a regular expression in your `<Pattern>` element includes XML-reserved characters (", &, ', <, or .), you must XML-encode it before you include it.
    
    
    <JSONPath>
       <Expression>$.store.book[*].author</Expression>
       <Pattern>REGEX PATTERN</Pattern>
       <Pattern>REGEX PATTERN</Pattern>
    </JSONPath>

**Default:** | N/A  
---|---  
**Presence:** | Required  
**Type:** | String  
  
## Error reference

This section describes the error codes and messages returned and fault variables set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. If you want to capture an error and raise your own custom error, set the `continueOnError="true"` attribute on the policy root element. To learn more, see [ What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Error Code | Message  
---|---  
`ExecutionFailed` | `Failed to execute the RegularExpressionProtection StepDefinition {0}. Reason: {1}`  
`InstantiationFailed` | `Failed to instantiate the RegularExpressionProtection StepDefinition {0}`  
`NonMessageVariable` | `Variable {0} does not resolve to a Message`  
`SourceMessageNotAvailable` | `{0} message is not available for RegularExpressionProtection StepDefinition {1}`  
`ThreatDetected` | `Regular Expression Threat Detected in {0}: regex: {1} input: {2}`  
`VariableResolutionFailed` | `Failed to resolve variable {0}`  
  
### Deployment errors

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Error Code | Message | Fix  
---|---|---  
`CannotBeConvertedToNodeset` | `RegularExpressionProtection {0}: Result of xpath {1} cannot be converted to nodeset. Context {2}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#cannotbeconvertedtonodeset)  
`DuplicatePrefix` | `RegularExpressionProtection {0}: Duplicate prefix {1}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#duplicateprefix)  
`EmptyJSONPathExpression` | `RegularExpressionProtection {0}: Empty JSONPath expression` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#emptyjsonpathexpression)  
`EmptyXPathExpression` | `RegularExpressionProtection {0}: Empty XPath expression` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#emptyxpathexpression)  
`InvalidRegularExpression` | `RegularExpressionProtection {0}: Invalid Regular Expression {1}, Context {2}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#invalidregularexpression)  
`JSONPathCompilationFailed` | `RegularExpressionProtection {0}: Failed to compile jsonpath {1}. Context {2}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#jsonpathcompilationfailed)  
`NONEmptyPrefixMappedToEmptyURI` | `RegularExpressionProtection {0}: Non-empty prefix {1} cannot be mapped to empty uri` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#nonemptyprefixmappedtoemptyuri)  
`NoPatternsToEnforce` | `RegularExpressionProtection {0}: No patterns to enforce in {1}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#nopatternstoenforce)  
`NothingToEnforce` | `RegularExpressionProtection {0}: at least one of URIPath, QueryParam, Header, FormParam, XMLPayload, JSONPayload is mandatory` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#nothingtoenforce)  
`XPathCompilationFailed` | `RegularExpressionProtection {0}: Failed to compile xpath {1}. Context {2}` | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/regular-expression-protection-deployment-errors#xpathcompilationfailed)  
  
### Fault variables

These variables are set when this policy triggers an error. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the table above.  | `fault.name Matches "ThreatDetected"`  
`regularexpressionprotection.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `regularexpressionprotection.Regular-Expressions-Protection-1.failed = true`  
  
## Schemas

**Sample:** See our [GitHub repository](https://github.com/apigee/api-platform-samples/tree/master/schemas/policy) samples for the most recent schemas.

## Related topics

[JSON Threat Protection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy)

[XML Threat Protection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 
