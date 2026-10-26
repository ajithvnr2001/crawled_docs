---
url: https://docs.comfy.org/es/interface/bottom-panel/
title: Panel inferior - Atajos, registros y terminal - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.780160+00:00
---

# Panel inferior - Atajos, registros y terminal - ComfyUI

> Source: https://docs.comfy.org/es/interface/bottom-panel/

## En esta página

Volver arriba

  * Abrir el panel
  * Pestañas de atajos
  * Registros (autoalojado y Desktop)
  * Terminal (solo Desktop)
  * Páginas relacionadas



Panel inferior y ayuda

# Panel inferior - Atajos, registros y terminal

Copiar páginaCopiar página

El panel inferior de ComfyUI reúne Atajos, registros de ejecución en compilaciones que no son Cloud y una terminal solo en Desktop.

Copiar páginaCopiar página

El panel inferior es una franja de espacio de trabajo acoplada bajo el lienzo. Aloja pestañas de referencia de atajos de teclado en todas las compilaciones, un flujo de **Registros** en las compilaciones autoalojadas y de Desktop, y una **Terminal** solo en la aplicación Desktop. Comfy Cloud no registra pestañas de terminal; los atajos siguen funcionando. ![El panel inferior abierto en la pestaña Atajos, mostrando la lista Esenciales](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_shortcuts.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=9f77fbce04f73687e6be12b1b82a12d9) ![La pestaña Registros transmitiendo la salida de ejecución del proceso de ComfyUI en una instalación autoalojada](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_logs.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=18ba948694f1bb8e6a75f43bfe657206)

## 

​

Abrir el panel

Puedes abrir el panel inferior de varias formas:

  * **Atajos** : haz clic en el icono de teclado cerca de la parte inferior de la barra lateral izquierda (`Workspace.ToggleBottomPanel.Shortcuts`, predeterminado `Ctrl` \+ `Shift` \+ `K`). Eso alterna específicamente el panel de atajos.
  * **Panel de consola / terminal** (no Cloud): haz clic en el icono de terminal cerca de la parte inferior de la barra lateral izquierda. Eso ejecuta **Alternar panel inferior** , que prefiere el panel de terminal cuando las pestañas Registros/Terminal están cargadas y, de lo contrario, recurre a Atajos.
  * Menú **Ver** : **Panel inferior** (`Workspace.ToggleBottomPanel`).
  * **Atajo de registros** (no Cloud): el predeterminado `Ctrl` \+ ``` alterna la pestaña Registros (`Workspace.ToggleBottomPanelTab.logs-terminal`).

El panel está oculto mientras el [Modo de enfoque](https://docs.comfy.org/es/interface/canvas-controls) está activado.

## 

​

Pestañas de atajos

Atajos registra dos pestañas en el panel de **atajos** :

  * **Esenciales** : atajos comunes de edición y de cola.
  * **Controles de vista** : atajos de navegación y relacionados con la vista.

Estos paneles reflejan los mismos datos de comandos y combinaciones de teclas que puedes personalizar en Configuraciones → Combinación de teclas. Para ver la lista completa editable, consulta [Atajos](https://docs.comfy.org/es/interface/shortcuts).

## 

​

Registros (autoalojado y Desktop)

En las compilaciones que no son Cloud, una pestaña **Registros** transmite la salida de registros de ejecución del proceso de ComfyUI. Úsala para depurar nodos personalizados, errores del servidor o mensajes del backend sin cambiar a una terminal externa. Atajo predeterminado: `Ctrl` \+ ```.

## 

​

Terminal (solo Desktop)

En la aplicación **Desktop** , se registra una pestaña **Terminal** (terminal de comandos) junto a Registros. Proporciona un shell dentro de la aplicación para los usuarios de Desktop. No se registra en sesiones autoalojadas de solo navegador ni en Comfy Cloud. ![La pestaña Terminal en Desktop, mostrando un shell dentro de la aplicación junto a Registros](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/bottom-panel/bottom_panel_terminal.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=90f43833f6f52001db479d6cac56f88e) Las compilaciones de Cloud omiten por completo el registro tanto de Registros como de Terminal; solo queda Atajos.

## 

​

Páginas relacionadas

  * [Atajos](https://docs.comfy.org/es/interface/shortcuts)
  * [Controles del lienzo](https://docs.comfy.org/es/interface/canvas-controls) (el modo de enfoque oculta este panel)
  * [Centro de ayuda](https://docs.comfy.org/es/interface/help-center)
  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/bottom-panel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/bottom-panel)

[Nodes 2.0](https://docs.comfy.org/es/interface/nodes-2)[Centro de ayuda](https://docs.comfy.org/es/interface/help-center)
