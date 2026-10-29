---
url: https://www.canva.dev/blog/developers/canva-mcp-ga/
title: How to use Canva MCP in your AI application - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T16:27:55.478931+00:00
---

# How to use Canva MCP in your AI application - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/canva-mcp-ga/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

MCP

# How to use Canva MCP in your AI application

Learn how to connect your AI assistant or platform to Canva's design capabilities with the Canva MCP server.

![](https://www.canva.dev/_next/static/media/thumbnail.0b616771.jpg)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 27, 2026

* * *

You can now add Canva MCP to your AI assistant, platform, or connector yourself, with no waiting on approval. Create an app in the Developer Portal, turn on Canva MCP, and connect to Canva’s remote MCP server using your app’s OAuth client.

With Canva MCP, your users can work with their Canva designs through the AI tools they already use. They can generate designs from a brief, find existing designs, make edits, manage assets, and export their work through natural-language workflows.

## What you can do with Canva MCP

The Canva MCP server exposes tools for common design workflows, including:

  * Creating designs and images from a prompt.
  * Searching designs, folders, and pages to find existing work.
  * Editing designs, adding comments, and managing assets.
  * Exporting designs in formats such as PDF, PNG, JPG, PPTX, and MP4.



The tools let your AI experience connect a user's intent to Canva's design capabilities, while users continue to work with their designs and assets in Canva.

## Get started

To connect your AI application to Canva MCP:

  1. Create an app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).

  2. Navigate to **Outside Canva** , and select **Start integrating**.

![The Developer Portal app outside Canva start page, with the Start integrating button highlighted](https://www.canva.dev/_next/static/media/start-integrating.333d8308.png)

  3. Under **Integration methods** , turn on **Canva MCP**.

![The Integration methods section, with Canva MCP enabled and Canva REST APIs turned off](https://www.canva.dev/_next/static/media/select-mcp.b4a4e025.png)

  4. Under **Credentials** , copy the client ID. Click Generate secret, then store the client secret somewhere secure. It isn't shown again.

![The Developer Portal credentials section, with the client ID and masked client secret](https://www.canva.dev/_next/static/media/clientid.ff63e117.png)

  5. Add the redirect URL your OAuth client uses under **Redirect URLs**.

![The Developer Portal Redirect URLs page](https://www.canva.dev/_next/static/media/redirect.54f883d0.png)

  6. Configure your MCP client to connect to the Canva MCP server at `https://api.canva.com/connect/v1/mcp` using Streamable HTTP.




Each user must authenticate with their own Canva account. The tools respect that user's Canva permissions; Canva MCP doesn't support organization-level or service-account authentication.

If your client uses a Client ID Metadata Document (CIMD) instead of a client secret, apply through the [Canva MCP waitlist⁠(opens in a new tab or window)](https://docs.google.com/forms/d/1jgC4vAA2-5LqaNzVhnP8ygSknF4Vysc1UzAWJukzcp0/viewform) to register its redirect URI.

## Tips for a reliable experience

As you build, keep these details in mind:

  * **Discover tools when you connect.** List tools from the server rather than assuming a fixed set, and check the tool documentation for request and response shapes.
  * **Handle long-running operations.** Design generation can take time. Keep the job ID and poll according to the returned polling policy. Once the job is successful, provide the user the edit URL and show the design in the chat.
  * **Keep users informed.** Show progress and report success only after the tool confirms the operation completed.
  * **Make it easy to continue in Canva.** After a design workflow, surface the returned edit link so users can open their design in Canva.
  * **Respect user access and plan limits.** Tools work with each user's permissions, and some features require a paid Canva plan.



For example requests and detailed implementation guidance, see [Canva MCP best practices](https://www.canva.dev/docs/apps/mcp/best-practices/), the [tool reference](https://www.canva.dev/docs/apps/mcp/tools/), and [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/).

## Choose the right Canva connection

Use Canva MCP when you're adding Canva to your own AI experience. If you want to connect a popular AI assistant to Canva, most already have a Canva connection. Follow the [Canva AI Connector setup guide⁠(opens in a new tab or window)](https://www.canva.com/help/mcp-agent-setup/).

To learn more about Canva for AI assistants, start with the [Canva MCP overview](https://www.canva.dev/docs/apps/mcp/) and [access and permissions guide](https://www.canva.dev/docs/apps/mcp/access/).

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.eab8445b.png)](https://www.canva.dev/blog/developers/spotlight-on-the-background/)

[BackgroundSpotlight on the background](https://www.canva.dev/blog/developers/spotlight-on-the-background/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jan 22, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.1b60cf41.jpg)](https://www.canva.dev/blog/developers/applying-canva-brand-templates/)

[Connect APIApply Canva Brand templates with the Autofill APIHow to identify and consistently apply Canva Brand Templates using the Brand template API and Autofill API.](https://www.canva.dev/blog/developers/applying-canva-brand-templates/)

Timo Bingaman, Joe RobinsonOct 9, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.832cdac2.png)](https://www.canva.dev/blog/developers/passing-user-input-from-canva-ui-to-your-lambda-function/)

[LambdaPassing User Input from Canva UI to your Lambda FunctionLearn how to pass Canva user inputs with Lambda Functions.](https://www.canva.dev/blog/developers/passing-user-input-from-canva-ui-to-your-lambda-function/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 20, 2023
