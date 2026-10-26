---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings/
title: Comandos y atajos de teclado - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:50.696058+00:00
---

# Comandos y atajos de teclado - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings/

## En esta página

Volver arriba

  * Uso básico
  * Configuración de comandos
  * Configuración de las combinaciones de teclas
    * Teclas especiales
  * Ejemplos de comandos
  * Ejemplos de atajos de teclado
  * Notas y limitaciones



JavaScript (UI)

# Comandos y atajos de teclado

Copiar páginaCopiar página

Domina los comandos y atajos de teclado de Comfy para registrar acciones y atajos personalizados en tus extensiones.

Copiar páginaCopiar página

La API de Commands y Keybindings permite que las extensiones registren comandos personalizados y los asocien a atajos de teclado. Así, los usuarios pueden activar acciones rápidamente sin usar el mouse.

## 

​

Uso básico
    
    
    app.registerExtension({
      name: "MyExtension",
      // Register commands
      commands: [
        {
          id: "myCommand",
          label: "My Command",
          function: () => {
            console.log("Command executed!");
          }
        }
      ],
      // Associate keybindings with commands
      keybindings: [
        {
          combo: { key: "k", ctrl: true },
          commandId: "myCommand"
        }
      ]
    });
    

## 

​

Configuración de comandos

Cada comando requiere un `id`, un `label` y una `function`:
    
    
    {
      id: string,              // Unique identifier for the command
      label: string,           // Display name for the command
      function: () => void     // Function to execute when command is triggered
    }
    

## 

​

Configuración de las combinaciones de teclas

Cada combinación de teclas requiere un `combo` y un `commandId`:
    
    
    {
      combo: {                 // Combinación de teclas
        key: string,           // La tecla principal (un solo carácter o una tecla especial)
        ctrl?: boolean,        // Requiere la tecla Ctrl (opcional)
        shift?: boolean,       // Requiere la tecla Shift (opcional)
        alt?: boolean,         // Requiere la tecla Alt (opcional)
        meta?: boolean         // Requiere la tecla Meta/Command (opcional)
      },
      commandId: string        // ID del comando que se va a activar
    }
    

### 

​

Teclas especiales

Para las teclas que no son caracteres, usa uno de estos valores:

  * Flechas: `"ArrowUp"`, `"ArrowDown"`, `"ArrowLeft"`, `"ArrowRight"`
  * Teclas de función: `"F1"` hasta `"F12"`
  * Otras teclas especiales: `"Escape"`, `"Tab"`, `"Enter"`, `"Backspace"`, `"Delete"`, `"Home"`, `"End"`, `"PageUp"`, `"PageDown"`



## 

​

Ejemplos de comandos
    
    
    app.registerExtension({
      name: "CommandExamples",
      commands: [
        {
          id: "runWorkflow",
          label: "Run Workflow",
          function: () => {
            app.queuePrompt();
          }
        },
        {
          id: "clearWorkflow",
          label: "Clear Workflow",
          function: () => {
            if (confirm("Clear the workflow?")) {
              app.graph.clear();
            }
          }
        },
        {
          id: "saveWorkflow",
          label: "Save Workflow",
          function: () => {
            app.graphToPrompt().then(workflow => {
              const blob = new Blob([JSON.stringify(workflow)], {type: "application/json"});
              const url = URL.createObjectURL(blob);
              const a = document.createElement("a");
              a.href = url;
              a.download = "workflow.json";
              a.click();
              URL.revokeObjectURL(url);
            });
          }
        }
      ]
    });
    

## 

​

Ejemplos de atajos de teclado
    
    
    app.registerExtension({
      name: "KeybindingExamples",
      commands: [
        /* Commands defined above */
      ],
      keybindings: [
        // Ctrl+R to run workflow
        {
          combo: { key: "r", ctrl: true },
          commandId: "runWorkflow"
        },
        // Ctrl+Shift+C to clear workflow
        {
          combo: { key: "c", ctrl: true, shift: true },
          commandId: "clearWorkflow"
        },
        // Ctrl+S to save workflow
        {
          combo: { key: "s", ctrl: true },
          commandId: "saveWorkflow"
        },
        // F5 to run workflow (alternative)
        {
          combo: { key: "F5" },
          commandId: "runWorkflow"
        }
      ]
    });
    

## 

​

Notas y limitaciones

  * Las extensiones no pueden sobrescribir los atajos de teclado definidos en el núcleo de ComfyUI. Revisa los atajos de teclado del núcleo en estos archivos fuente:
    * [Comandos del núcleo](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/composables/useCoreCommands.ts)
    * [Comandos del menú del núcleo](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/coreMenuCommands.ts)
    * [Atajos de teclado del núcleo](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/coreKeybindings.ts)
    * [Combinaciones de teclas reservadas](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/reservedKeyCombos.ts)
  * Algunas combinaciones de teclas están reservadas por el navegador (como Ctrl+F para buscar) y no se pueden sobrescribir
  * Si varias extensiones registran la misma combinación de teclas, el comportamiento no está definido



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_commands_keybindings.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_commands_keybindings)

[Selection Toolbox](https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox)[API del menú de la barra superior](https://docs.comfy.org/es/custom-nodes/js/javascript_topbar_menu)
