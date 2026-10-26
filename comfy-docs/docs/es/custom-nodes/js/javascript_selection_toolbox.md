---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox/
title: Selection Toolbox - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.434134+00:00
---

# Selection Toolbox - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox/

## En esta página

Volver arriba

  * Uso básico
  * Definición de comando
  * Opciones de iconos
  * Visibilidad dinámica de comandos
  * Trabajar con los elementos seleccionados
  * Ejemplo completo
  * Notas



JavaScript (UI)

# Selection Toolbox

Copiar páginaCopiar página

Añade comandos de acción personalizados a Selection Toolbox de ComfyUI para nodos, grupos y elementos del lienzo seleccionados con getSelectionToolboxCommands.

Copiar páginaCopiar página

La API Selection Toolbox permite a las extensiones agregar botones de acción personalizados que aparecen al seleccionar nodos en el lienzo. Esto brinda acceso rápido a comandos contextuales para los elementos seleccionados (nodos, grupos, etc.).

## 

​

Uso básico

Para añadir comandos al cuadro de herramientas de selección, tu extensión debe:

  1. Definir los comandos con la [interfaz de comandos](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings) estándar
  2. Implementar el método `getSelectionToolboxCommands` para especificar qué comandos aparecen en el cuadro de herramientas

Nota: el método `getSelectionToolboxCommands` se llama para cada elemento del conjunto de selección cada vez que se realiza una nueva selección.
    
    
    app.registerExtension({
      name: "MyExtension",
      commands: [
        {
          id: "my-extension.duplicate-special",
          label: "Duplicate Special",
          icon: "pi pi-copy",
          function: (selectedItem) => {
            // Your command logic here
            console.log("Duplicating selected nodes with special behavior");
          }
        }
      ],
      getSelectionToolboxCommands: (selectedItem) => {
        // Return array of command IDs to show in the toolbox
        return ["my-extension.duplicate-special"];
      }
    });
    

## 

​

Definición de comando

Los comandos del cuadro de herramientas de selección usan la interfaz de comandos estándar de ComfyUI:
    
    
    {
      id: string,          // Unique identifier for the command
      label: string,       // Display text for the button tooltip
      icon?: string,       // Icon class for the button (optional)
      function: (selectedItem) => void  // Function executed when clicked
    }
    

La `function` recibe el elemento o los elementos seleccionados como parámetro, lo que te permite realizar acciones sobre la selección actual.

## 

​

Opciones de iconos

Los botones del cuadro de herramientas de selección admiten las mismas bibliotecas de iconos que otros elementos de la interfaz:

  * Iconos de PrimeVue: `pi pi-[icon-name]` (por ejemplo, `pi pi-star`)
  * Iconos de Material Design: `mdi mdi-[icon-name]` (por ejemplo, `mdi mdi-content-copy`)



## 

​

Visibilidad dinámica de comandos

El método `getSelectionToolboxCommands` se llama cada vez que cambia la selección, lo que te permite mostrar comandos distintos según lo que esté seleccionado:
    
    
    app.registerExtension({
      name: "ContextualCommands",
      commands: [
        {
          id: "my-ext.align-nodes",
          label: "Align Nodes",
          icon: "pi pi-align-left",
          function: () => {
            // Align multiple nodes
          }
        },
        {
          id: "my-ext.configure-single",
          label: "Configure",
          icon: "pi pi-cog",
          function: () => {
            // Configure single node
          }
        }
      ],
      getSelectionToolboxCommands: (selectedItem) => {
        const selectedItems = app.canvas.selectedItems;
        const itemCount = selectedItems ? selectedItems.size : 0;
        
        if (itemCount > 1) {
          // Show alignment command for multiple items
          return ["my-ext.align-nodes"];
        } else if (itemCount === 1) {
          // Show configuration for single item
          return ["my-ext.configure-single"];
        }
        
        return [];
      }
    });
    

## 

​

Trabajar con los elementos seleccionados

Accede a la información de los elementos seleccionados a través del objeto canvas de la app. La propiedad `selectedItems` es un Set que incluye nodos, grupos y otros elementos del lienzo:
    
    
    app.registerExtension({
      name: "SelectionInfo",
      commands: [
        {
          id: "my-ext.show-info",
          label: "Show Selection Info",
          icon: "pi pi-info-circle",
          function: () => {
            const selectedItems = app.canvas.selectedItems;
            
            if (selectedItems && selectedItems.size > 0) {
              console.log(`Selected ${selectedItems.size} items`);
              
              // Iterate through selected items
              selectedItems.forEach(item => {
                if (item.type) {
                  console.log(`Item: ${item.type} (ID: ${item.id})`);
                }
              });
            }
          }
        }
      ],
      getSelectionToolboxCommands: () => ["my-ext.show-info"]
    });
    

## 

​

Ejemplo completo

Aquí tienes un ejemplo sencillo que muestra varias características del cuadro de herramientas de selección:
    
    
    app.registerExtension({
      name: "SelectionTools",
      commands: [
        {
          id: "selection-tools.count",
          label: "Count Selection",
          icon: "pi pi-hashtag",
          function: () => {
            const count = app.canvas.selectedItems?.size || 0;
            app.extensionManager.toast.add({
              severity: "info",
              summary: "Selection Count",
              detail: `You have ${count} item${count !== 1 ? 's' : ''} selected`,
              life: 3000
            });
          }
        },
        {
          id: "selection-tools.copy-ids",
          label: "Copy IDs",
          icon: "pi pi-copy",
          function: () => {
            const items = Array.from(app.canvas.selectedItems || []);
            const ids = items.map(item => item.id).filter(id => id !== undefined);
            
            if (ids.length > 0) {
              navigator.clipboard.writeText(ids.join(', '));
              app.extensionManager.toast.add({
                severity: "success",
                summary: "Copied",
                detail: `Copied ${ids.length} IDs to clipboard`,
                life: 2000
              });
            }
          }
        },
        {
          id: "selection-tools.log-types",
          label: "Log Types",
          icon: "pi pi-info-circle",
          function: () => {
            const items = Array.from(app.canvas.selectedItems || []);
            const typeCount = {};
            
            items.forEach(item => {
              const type = item.type || 'unknown';
              typeCount[type] = (typeCount[type] || 0) + 1;
            });
            
            console.log("Selection types:", typeCount);
          }
        }
      ],
      
      getSelectionToolboxCommands: (selectedItem) => {
        const selectedItems = app.canvas.selectedItems;
        const itemCount = selectedItems ? selectedItems.size : 0;
        
        if (itemCount === 0) return [];
        
        const commands = ["selection-tools.count", "selection-tools.log-types"];
        
        // Only show copy command if items have IDs
        const hasIds = Array.from(selectedItems).some(item => item.id !== undefined);
        if (hasIds) {
          commands.push("selection-tools.copy-ids");
        }
        
        return commands;
      }
    });
    

## 

​

Notas

  * La cuadro de herramientas de selección debe estar habilitada en las configuraciones: `Comfy.Canvas.SelectionToolbox`
  * Los comandos deben definirse en el arreglo `commands` antes de referenciarlos en `getSelectionToolboxCommands`
  * La cuadro de herramientas se actualiza automáticamente cuando cambia la selección
  * El método `getSelectionToolboxCommands` se llama para cada elemento del conjunto de selección cada vez que se realiza una nueva selección
  * Usa `app.canvas.selectedItems` (un Set) para acceder a todos los elementos seleccionados, incluidos nodos, grupos y otros elementos del lienzo
  * Por compatibilidad con versiones anteriores, `app.canvas.selected_nodes` todavía existe, pero solo contiene nodos



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_selection_toolbox.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_selection_toolbox)

[Pestañas de la barra lateral](https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs)[Comandos y atajos de teclado](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings)
