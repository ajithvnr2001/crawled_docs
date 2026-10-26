---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_topbar_menu/
title: API del men\u00fa de la barra superior de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.525856+00:00
---

# API del menú de la barra superior de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_topbar_menu/

## En esta página

Volver arriba

  * Uso básico
  * Configuración de comandos
  * Configuración del menú
  * Ejemplos de menú
    * Agregar a menús existentes
    * Crear una estructura de submenú
    * Varias ubicaciones de menú



JavaScript (UI)

# API del menú de la barra superior de ComfyUI

Copiar páginaCopiar página

Agrega comandos personalizados al menú de la barra superior de ComfyUI: añádelos a menús existentes, crea submenús o coloca un comando en varias ubicaciones.

Copiar páginaCopiar página

La API Topbar Menu permite a las extensiones agregar elementos de menú personalizados a la barra de menú superior de ComfyUI. Resulta útil para dar acceso a funciones avanzadas o a comandos que se usan con menos frecuencia.

## 

​

Uso básico
    
    
    app.registerExtension({
      name: "MyExtension",
      // Define los comandos
      commands: [
        { 
          id: "myCommand", 
          label: "My Command", 
          function: () => { alert("Command executed!"); } 
        }
      ],
      // Agrega comandos al menú
      menuCommands: [
        { 
          path: ["Extensions", "My Extension"], 
          commands: ["myCommand"] 
        }
      ]
    });
    

Las definiciones de comandos siguen el mismo patrón que en la [API de comandos y atajos de teclado](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings). Consulta esa página para obtener información más detallada sobre cómo definir comandos.

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

Configuración del menú

El arreglo `menuCommands` define dónde colocar los comandos dentro de la estructura del menú:
    
    
    {
      path: string[],          // Arreglo que representa la jerarquía del menú
      commands: string[]       // Arreglo de IDs de comandos para agregar en esta ubicación
    }
    

El arreglo `path` especifica la jerarquía del menú. Por ejemplo, `["File", "Export"]` agregaría comandos al submenú “Export” dentro del menú “File”.

## 

​

Ejemplos de menú

### 

​

Agregar a menús existentes
    
    
    app.registerExtension({
      name: "MenuExamples",
      commands: [
        { 
          id: "saveAsImage", 
          label: "Save as Image", 
          function: () => { 
            // Código para guardar el lienzo como imagen
          } 
        },
        { 
          id: "exportWorkflow", 
          label: "Export Workflow", 
          function: () => { 
            // Código para exportar el flujo de trabajo
          } 
        }
      ],
      menuCommands: [
        // Agregar al menú File
        { 
          path: ["File"], 
          commands: ["saveAsImage", "exportWorkflow"] 
        }
      ]
    });
    

### 

​

Crear una estructura de submenú
    
    
    app.registerExtension({
      name: "SubmenuExample",
      commands: [
        { 
          id: "option1", 
          label: "Option 1", 
          function: () => { console.log("Option 1"); } 
        },
        { 
          id: "option2", 
          label: "Option 2", 
          function: () => { console.log("Option 2"); } 
        },
        { 
          id: "suboption1", 
          label: "Sub-option 1", 
          function: () => { console.log("Sub-option 1"); } 
        }
      ],
      menuCommands: [
        // Crear una estructura de menú anidada
        { 
          path: ["Extensions", "My Tools"], 
          commands: ["option1", "option2"] 
        },
        { 
          path: ["Extensions", "My Tools", "Advanced"], 
          commands: ["suboption1"] 
        }
      ]
    });
    

### 

​

Varias ubicaciones de menú

Puedes agregar el mismo comando en varias ubicaciones de menú:
    
    
    app.registerExtension({
      name: "MultiLocationExample",
      commands: [
        { 
          id: "helpCommand", 
          label: "Get Help", 
          function: () => { window.open("https://docs.example.com", "_blank"); } 
        }
      ],
      menuCommands: [
        // Agregar al menú Help
        { 
          path: ["Help"], 
          commands: ["helpCommand"] 
        },
        // También agregar al menú Extensions
        { 
          path: ["Extensions"], 
          commands: ["helpCommand"] 
        }
      ]
    });
    

Los comandos pueden funcionar con otras API de ComfyUI, como las configuraciones. Para obtener más información sobre la API de configuraciones, consulta la documentación de la [API de configuraciones](https://docs.comfy.org/es/custom-nodes/js/javascript_settings).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_topbar_menu.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_topbar_menu)

[Comandos y atajos de teclado](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings)[Subgrafos](https://docs.comfy.org/es/custom-nodes/js/subgraphs)
