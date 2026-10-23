---
url: https://docs.comfy.org/interface/shortcuts/
title: Keyboard and Mouse Shortcuts - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:43.861752+00:00
---

# Keyboard and Mouse Shortcuts - ComfyUI

> Source: https://docs.comfy.org/interface/shortcuts/

## On this page

  * Find and edit a shortcut
  * Keybinding presets



ComfyUI Settings

# Keyboard and Mouse Shortcuts

Copy pageCopy page

ComfyUI keyboard and mouse shortcuts: the full default list, plus how to rebind commands and save your own keybinding presets in Settings.

Copy pageCopy page

The settings described on this page are located in the **ComfyUI in-app settings menu**. You can open it by navigating to **Settings** (gear icon) or using the `Ctrl + ,` keyboard shortcut, then select the corresponding category to view and configure these options.

ComfyUI ships with a default set of keyboard shortcuts, and every command can be rebound. Open **Settings (gear icon)** > **Keybinding** to see and change them. ![ComfyUI Shortcut Settings](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/keybinding.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3b36de580ec995fdd0ec7cc64e3b670c)

## 

​

Find and edit a shortcut

The panel lists every command with its current keybinding. The search box at the top narrows the list, and clicking the **Command** header sorts it alphabetically. The **Source** column names the extension or custom node pack that provides a command; commands that come from ComfyUI itself leave it empty. Select the edit icon on a row to record a new key combination. A row menu can reset that command to its default or remove its keybindings. When a command has more than one keybinding, the row expands and each binding gets its own edit and delete buttons. **Reset All** at the bottom of the panel clears every customization after a confirmation prompt.

## 

​

Keybinding presets

Your edits belong to a named preset, and the preset selector at the top of the panel switches between them. The **Default Preset** holds the built-in shortcuts. Selecting it restores those shortcuts and drops the unsaved edits in your current session. Presets you saved earlier stay on disk.

  * A preset name shows a `*` while it has unsaved changes. For a saved preset, select **Save Changes** to store them. The Default Preset has no Save Changes button, so its edits are saved through **Save as new preset**.
  * The … (more) button next to the preset selector holds **Save as new preset** (hidden while the Default Preset has no edits), **Reset to default** , **Delete preset** (disabled for the Default Preset), **Import preset** , and **Export preset**.
  * **Import preset** reads a preset file exported from ComfyUI, so a shortcut set can move between installs or be handed to another user. **Export preset** writes the current preset to a JSON file.
  * Switching presets while there are unsaved changes prompts to save them first, or to discard them and continue.

Presets are stored as JSON files in the ComfyUI user directory under `keybindings/`. Below is the current default list of shortcuts.

  * Windows/Linux

  * MacOS




Shortcut| Command  
---|---  
Ctrl + Enter| Queue prompt  
Ctrl + Shift + Enter| Queue prompt (Front)  
Ctrl + Alt + Enter| Interrupt  
Ctrl + Z / Ctrl + Y| Undo/Redo  
Ctrl + S| Save workflow  
Ctrl + O| Load workflow  
Ctrl + A| Select all nodes  
Alt + C| Collapse/uncollapse selected nodes  
Ctrl + M| Mute/unmute selected nodes  
Ctrl + B| Bypass/unbypass selected nodes  
Delete  
Backspace| Delete selected nodes  
Backspace| Clear workflow  
Space| Move canvas when holding and moving cursor  
Ctrl + Click  
Shift + Click| Add clicked node to selection  
Ctrl + C/Ctrl + V| Copy and paste selected nodes (without maintaining connections to outputs of unselected nodes)  
Ctrl + C/Ctrl + Shift + V| Copy and paste selected nodes (maintaining connections from outputs of unselected nodes to inputs of pasted nodes)  
Shift + Drag| Move multiple selected nodes at the same time  
Ctrl + G| Add frame to selected nodes  
Ctrl + ,| Show settings dialog  
Alt + =| Zoom in (canvas)  
Alt + -| Zoom out (canvas)  
.| Fit view to selected nodes  
P| Pin/unpin selected items  
Q| Toggle queue sidebar  
W| Toggle workflow sidebar  
N| Toggle node library sidebar  
M| Toggle model library sidebar  
Ctrl + `| Toggle log bottom panel  
F| Toggle focus mode (full screen)  
R| Refresh node definitions  
Double-Click LMB| Quick search for nodes to add  
  
Shortcut| Command  
---|---  
Cmd ⌘ + Enter| Queue prompt  
Cmd ⌘ + Shift + Enter| Queue prompt (Front)  
Cmd ⌘ + Alt + Enter| Interrupt  
Cmd ⌘ + Z/Cmd ⌘ + Y| Undo/Redo  
Cmd ⌘ + S| Save workflow  
Cmd ⌘ + O| Load workflow  
Cmd ⌘ + A| Select all nodes  
Opt ⌥ + C| Collapse/uncollapse selected nodes  
Cmd ⌘ + M| Mute/unmute selected nodes  
Cmd ⌘ + B| Bypass/unbypass selected nodes  
Delete  
Backspace| Delete selected nodes  
Backspace| Clear workflow  
Space| Move canvas when holding and moving cursor  
Cmd ⌘ + Click  
Shift + Click| Add clicked node to selection  
Cmd ⌘ + C / Cmd ⌘ + V| Copy and paste selected nodes (without maintaining connections to outputs of unselected nodes)  
Cmd ⌘ + C / Cmd ⌘ + Shift + V| Copy and paste selected nodes (maintaining connections from outputs of unselected nodes to inputs of pasted nodes)  
Shift + Drag| Move multiple selected nodes at the same time  
Cmd ⌘ + G| Add frame to selected nodes  
Cmd ⌘ + ,| Show settings dialog  
Opt ⌥ + =| Zoom in (canvas)  
Opt ⌥ + -| Zoom out (canvas)  
.| Fit view to selected nodes  
P| Pin/unpin selected items  
Q| Toggle queue sidebar  
W| Toggle workflow sidebar  
N| Toggle node library sidebar  
M| Toggle model library sidebar  
Cmd ⌘ + `| Toggle log bottom panel  
F| Toggle focus mode (full screen)  
R| Refresh node definitions  
Double-Click LMB| Quick search for nodes to add  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/shortcuts.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/shortcuts)

[Mask Editor](https://docs.comfy.org/interface/settings/mask-editor)[Extension](https://docs.comfy.org/interface/settings/extension)
