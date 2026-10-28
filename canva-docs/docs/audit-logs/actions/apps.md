---
url: https://www.canva.dev/docs/audit-logs/actions/apps/
title: Apps - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-28T16:20:12.591344+00:00
---

# Apps - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/apps/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Apps

Copy page

## Install an app

An `actor` triggers this event when they use a third-party app for the first time (or following app uninstall). For example, when a user selects "open" on a new app in the editor, or selects **Use in a new design** or **Use in existing design** from the apps [marketplace⁠(opens in a new tab or window)](https://www.canva.com/your-apps/). The installation is for a user in a team.

`type``string`

**Default value:** `INSTALL_APP`

**Available values:** The only valid value is `INSTALL_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



`settings``string[]`

Optional

A set of settings.

**Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..

`canva_ai_permissions``AppCanvaAiPermissions`

Optional

The permissions for how Canva AI uses an app.

Properties of **canva_ai_permissions**

`enabled``boolean`

`has_server_address``boolean`

  * The `actor` set a server address. The actual value is sensitive and is not included.



`tool_permissions``AppCanvaAiToolPermission[]`

Optional

The tool permissions the `actor` set for using an app with Canva AI.

Properties of **tool_permissions**

`name``string`

The name of the tool.

`permission``string`

How a tool may be used by Canva AI.

**Available values:**

  * `ALWAYS_ALLOW`: Canva AI is always allowed to use the tool.
  * `ASK_EVERY_TIME`: Canva AI will always ask before using the tool.
  * `BLOCKED`: Canva AI is never allowed to use the tool.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "INSTALL_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ],
    
        "settings": [
    
          "ENABLED_FOR_CANVA_AI"
    
        ],
    
        "canva_ai_permissions": {
    
          "enabled": true,
    
          "has_server_address": true,
    
          "tool_permissions": [
    
            {
    
              "name": "spell-checker-tool",
    
              "permission": "ALWAYS_ALLOW"
    
            }
    
          ]
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Uninstall an app

An `actor` triggers this event when they remove a third-party app from their list of apps.

`type``string`

**Default value:** `UNINSTALL_APP`

**Available values:** The only valid value is `UNINSTALL_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNINSTALL_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an app's permissions

An `actor` triggers this event when they accept updated permissions for an installed third-party app. The app's developer may have updated the permissions required by the app.

`type``string`

**Default value:** `UPDATE_APP_PERMISSIONS`

**Available values:** The only valid value is `UPDATE_APP_PERMISSIONS`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`old_permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



`new_permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_APP_PERMISSIONS",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "old_permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ],
    
        "new_permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a setting for an app

An `actor` triggers this event when they update a setting for an app.

`type``string`

**Default value:** `UPDATE_APP_SETTING`

**Available values:** The only valid value is `UPDATE_APP_SETTING`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`setting``string`

The setting for an app.

**Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..

`old_value``boolean`

`new_value``boolean`

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_APP_SETTING",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "setting": "ENABLED_FOR_CANVA_AI",
    
        "old_value": true,
    
        "new_value": true
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an app's Canva AI permissions

An `actor` triggers this event when they update the Canva AI permissions for an app.

`type``string`

**Default value:** `UPDATE_APP_CANVA_AI_PERMISSIONS`

**Available values:** The only valid value is `UPDATE_APP_CANVA_AI_PERMISSIONS`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`changed_fields``string[]`

Optional

The fields that were changed in this update.

**Available values:**

  * `ENABLED`: The `enabled` field was changed.
  * `TOOL_PERMISSIONS`: One or more tool permissions were changed.
  * `SERVER_ADDRESS`: The server address was changed. The actual value is sensitive and is not included.



`old_enabled``boolean`

Optional

Whether Canva AI permissions were enabled before this update.

`new_enabled``boolean`

Optional

Whether Canva AI permissions were enabled after this update.

`tool_permission_changes``UpdateAppCanvaAiToolPermissionChange[]`

Optional

The tool permissions the `actor` requested changes for in this update.

ADD_APP_CANVA_AI_TOOL_PERMISSIONADD_APP_CANVA_AI_TOOL_PERMISSION

REMOVE_APP_CANVA_AI_TOOL_PERMISSIONREMOVE_APP_CANVA_AI_TOOL_PERMISSION

UPDATE_APP_CANVA_AI_TOOL_PERMISSIONUPDATE_APP_CANVA_AI_TOOL_PERMISSION

The `actor` added a permission for how a tool may be used by Canva AI.

`type``string`

**Default value:** `ADD_APP_CANVA_AI_TOOL_PERMISSION`

**Available values:** The only valid value is `ADD_APP_CANVA_AI_TOOL_PERMISSION`.

`name``string`

The name of the tool.

`permission``string`

How a tool may be used by Canva AI.

**Available values:**

  * `ALWAYS_ALLOW`: Canva AI is always allowed to use the tool.
  * `ASK_EVERY_TIME`: Canva AI will always ask before using the tool.
  * `BLOCKED`: Canva AI is never allowed to use the tool.



The `actor` removed a permission for how a tool may be used by Canva AI.

`type``string`

**Default value:** `REMOVE_APP_CANVA_AI_TOOL_PERMISSION`

**Available values:** The only valid value is `REMOVE_APP_CANVA_AI_TOOL_PERMISSION`.

`name``string`

The name of the tool.

`permission``string`

How a tool may be used by Canva AI.

**Available values:**

  * `ALWAYS_ALLOW`: Canva AI is always allowed to use the tool.
  * `ASK_EVERY_TIME`: Canva AI will always ask before using the tool.
  * `BLOCKED`: Canva AI is never allowed to use the tool.



The `actor` updated a permission for how a tool may be used by Canva AI.

`type``string`

**Default value:** `UPDATE_APP_CANVA_AI_TOOL_PERMISSION`

**Available values:** The only valid value is `UPDATE_APP_CANVA_AI_TOOL_PERMISSION`.

`name``string`

The name of the tool.

`old_permission``string`

How a tool may be used by Canva AI.

**Available values:**

  * `ALWAYS_ALLOW`: Canva AI is always allowed to use the tool.
  * `ASK_EVERY_TIME`: Canva AI will always ask before using the tool.
  * `BLOCKED`: Canva AI is never allowed to use the tool.



`new_permission``string`

How a tool may be used by Canva AI.

**Available values:**

  * `ALWAYS_ALLOW`: Canva AI is always allowed to use the tool.
  * `ASK_EVERY_TIME`: Canva AI will always ask before using the tool.
  * `BLOCKED`: Canva AI is never allowed to use the tool.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_APP_CANVA_AI_PERMISSIONS",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "changed_fields": [
    
          "ENABLED",
    
          "TOOL_PERMISSIONS",
    
          "SERVER_ADDRESS"
    
        ],
    
        "old_enabled": true,
    
        "new_enabled": true,
    
        "tool_permission_changes": [
    
          {
    
            "type": "ADD_APP_CANVA_AI_TOOL_PERMISSION",
    
            "name": "spell-checker-tool",
    
            "permission": "ALWAYS_ALLOW"
    
          },
    
          {
    
            "type": "REMOVE_APP_CANVA_AI_TOOL_PERMISSION",
    
            "name": "spell-checker-tool",
    
            "permission": "ALWAYS_ALLOW"
    
          },
    
          {
    
            "type": "UPDATE_APP_CANVA_AI_TOOL_PERMISSION",
    
            "name": "spell-checker-tool",
    
            "old_permission": "ALWAYS_ALLOW",
    
            "new_permission": "ALWAYS_ALLOW"
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Disconnect from a third-party service through an app

An `actor` triggers this event when they disconnect from a third-party service from within a third-party [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps) installed in Canva. For example, a user disconnects from Google Drive in the [Google Drive App⁠(opens in a new tab or window)](https://www.canva.com/your-apps/googledrive/google-drive).

`type``string`

**Default value:** `DISCONNECT_FROM_THIRD_PARTY_APP`

**Available values:** The only valid value is `DISCONNECT_FROM_THIRD_PARTY_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DISCONNECT_FROM_THIRD_PARTY_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Connect to a third-party service through an app

An `actor` triggers this event when they connect to a third-party service using a third-party [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps) installed in Canva. For example, a user connects to Google Drive using the [Google Drive App⁠(opens in a new tab or window)](https://www.canva.com/your-apps/googledrive/google-drive).

`type``string`

**Default value:** `CONNECT_TO_THIRD_PARTY_APP`

**Available values:** The only valid value is `CONNECT_TO_THIRD_PARTY_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CONNECT_TO_THIRD_PARTY_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
