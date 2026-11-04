---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox/
title: Cuadro de herramientas de selecci\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:51.712511+00:00
---

# Cuadro de herramientas de selección - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_selection_toolbox/

## En esta página

Volver arriba

  * Uso básico
  * Definición de comandos
  * Opciones de iconos
  * Visibilidad dinámica de comandos
  * Trabajar con elementos seleccionados
  * Ejemplo completo
  * Notas



JavaScript (UI)

# Cuadro de herramientas de selección

Copiar páginaCopiar página

Añade comandos de acción personalizados a Selection Toolbox de ComfyUI para nodos, grupos y elementos del lienzo seleccionados con getSelectionToolboxCommands.

Copiar páginaCopiar página

La API de Selection Toolbox permite a las extensiones agregar botones de acción personalizados que aparecen al seleccionar nodos en el lienzo. Esto brinda acceso rápido a comandos contextuales para los elementos seleccionados (nodos, grupos, etc.).

## 

​

Uso básico

Para agregar comandos al cuadro de herramientas de selección, tu extensión necesita:

  1. Definir los comandos con la [interfaz de comandos](https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings) estándar
  2. Implementar el método `getSelectionToolboxCommands` para especificar qué comandos aparecen en el cuadro de herramientas

Nota: el método `getSelectionToolboxCommands` se llama para cada elemento del conjunto de selección cada vez que haces una nueva selección.
    
    
    app.registerExtension({
      name: "MyExtension",
      commands: [
        {
          id: "my-extension.duplicate-special",
          label: "Duplicate Special",
          icon: "icon-[lucide--copy]",
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

Definición de comandos

Los comandos del cuadro de herramientas de selección usan la interfaz de comandos estándar de ComfyUI:
    
    
    {
      id: string,          // Identificador único para el comando
      label: string,       // Texto a mostrar en la información sobre herramientas del botón
      icon?: string,       // Clase de icono para el botón (opcional)
      function: (selectedItem) => void  // Función que se ejecuta al hacer clic
    }
    

La `function` recibe el elemento o los elementos seleccionados como parámetro, lo que te permite realizar acciones sobre la selección actual.

## 

​

Opciones de iconos

Los botones del cuadro de herramientas de selección usan clases de iconos de [Lucide](https://lucide.dev/icons/) con el formato `icon-[lucide--<icon-name>]` (por ejemplo, `icon-[lucide--star]`). El frontend genera estas clases al compilarse, así que solo están disponibles los iconos de Lucide que usa el propio frontend. Si un icono no se muestra, elige otro o define tu propia clase de icono en una hoja de estilos que cargue tu extensión. Las clases de PrimeIcons (`pi pi-*`) y de Material Design Icons (`mdi mdi-*`) todavía se muestran por ahora, pero se están retirando gradualmente. No las uses en código nuevo. Consulta la [migración por la eliminación de PrimeVue](https://docs.comfy.org/es/custom-nodes/js/primevue-removal-migration).

## 

​

Visibilidad dinámica de comandos

Cada vez que cambia la selección se llama al método `getSelectionToolboxCommands`, lo que te permite mostrar comandos diferentes según lo que esté seleccionado:
    
    
    app.registerExtension({
      name: "ContextualCommands",
      commands: [
        {
          id: "my-ext.align-nodes",
          label: "Align Nodes",
          icon: "icon-[lucide--align-start-vertical]",
          function: () => {
            // Align multiple nodes
          }
        },
        {
          id: "my-ext.configure-single",
          label: "Configure",
          icon: "icon-[lucide--settings]",
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

Trabajar con elementos seleccionados

Accede a la información sobre los elementos seleccionados a través del objeto canvas de la aplicación. La propiedad `selectedItems` es un Set que incluye nodos, grupos y otros elementos del lienzo:
    
    
    app.registerExtension({
      name: "SelectionInfo",
      commands: [
        {
          id: "my-ext.show-info",
          label: "Show Selection Info",
          icon: "icon-[lucide--info]",
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

Aquí tienes un ejemplo sencillo que muestra varias funciones del cuadro de herramientas de selección:
    
    
    app.registerExtension({
      name: "SelectionTools",
      commands: [
        {
          id: "selection-tools.count",
          label: "Count Selection",
          icon: "icon-[lucide--tag]",
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
          icon: "icon-[lucide--copy]",
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
          icon: "icon-[lucide--info]",
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

  * El cuadro de herramientas de selección debe estar habilitado en las configuraciones: `Comfy.Canvas.SelectionToolbox`
  * Los comandos deben definirse en el arreglo `commands` antes de referenciarlos en `getSelectionToolboxCommands`
  * El cuadro de herramientas se actualiza automáticamente cuando cambia la selección
  * El método `getSelectionToolboxCommands` se llama para cada elemento del conjunto de selección cada vez que se realiza una nueva selección
  * Usa `app.canvas.selectedItems` (un Set) para acceder a todos los elementos seleccionados, incluidos nodos, grupos y otros elementos del lienzo
  * Por compatibilidad con versiones anteriores, `app.canvas.selected_nodes` todavía existe, pero solo contiene nodos



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_selection_toolbox.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_selection_toolbox)

[Pestañas de la barra lateral](https://docs.comfy.org/es/custom-nodes/js/javascript_sidebar_tabs)[Comandos y atajos de teclado](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings)
