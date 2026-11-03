---
url: https://docs.comfy.org/es/custom-nodes/js/context-menu-migration/
title: Gu\u00eda de migraci\u00f3n del men\u00fa contextual - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:25.051420+00:00
---

# Guía de migración del menú contextual - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/context-menu-migration/

## En esta página

Volver arriba

  * Migrar los menús del lienzo
    * Enfoque anterior (obsoleto)
    * Enfoque nuevo (recomendado)
    * Diferencias clave
  * Migrar los menús de nodos
    * Enfoque anterior (obsoleto)
    * Enfoque nuevo (recomendado)
    * Diferencias clave
  * Patrones comunes
    * Elementos de menú condicionales
    * Agregar separadores
    * Crear submenús
    * Acceder al estado
  * Solución de problemas
    * Cómo identificar el uso de la API antigua
    * Entender las advertencias de obsolescencia
    * Verificar el éxito de la migración
    * Ejemplo completo de migración
  * Recursos adicionales



Migration Guides

# Guía de migración del menú contextual

Copiar páginaCopiar página

Migra extensiones de ComfyUI del monkey-patching obsoleto a la API del menú contextual: menús del lienzo y nodos, elementos condicionales, submenús y depuración.

Copiar páginaCopiar página

Esta guía te ayuda a migrar del enfoque obsoleto de monkey-patching a la nueva API de extensión del menú contextual. El enfoque anterior de monkey-patching de `LGraphCanvas.prototype.getCanvasMenuOptions` y `nodeType.prototype.getExtraMenuOptions` está obsoleto:

Si ves advertencias de obsolescencia en la consola de tu navegador, tu extensión está usando la API antigua y deberías migrarla.

## 

​

Migrar los menús del lienzo

### 

​

Enfoque anterior (obsoleto)

El enfoque anterior modificaba el prototipo durante la configuración de la extensión:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      async setup() {
        // ❌ ANTIGUO: modificar el prototipo (monkey-patching)
        const original = LGraphCanvas.prototype.getCanvasMenuOptions
        LGraphCanvas.prototype.getCanvasMenuOptions = function() {
          const options = original.apply(this, arguments)
    
          options.push(null) // separador
          options.push({
            content: "My Custom Action",
            callback: () => {
              console.log("Action triggered")
            }
          })
    
          return options
        }
      }
    })
    

### 

​

Enfoque nuevo (recomendado)

El enfoque nuevo usa un hook dedicado de la extensión:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      // ✅ NUEVO: usa el hook getCanvasMenuItems
      getCanvasMenuItems(canvas) {
        return [
          null, // separador
          {
            content: "My Custom Action",
            callback: () => {
              console.log("Action triggered")
            }
          }
        ]
      }
    })
    

### 

​

Diferencias clave

Enfoque anterior| Enfoque nuevo  
---|---  
Modificado en `setup()`| Usa el hook `getCanvasMenuItems()`  
Envuelve la función existente| Devuelve los elementos del menú directamente  
Modifica el arreglo `options`| Devuelve un arreglo nuevo  
Acceso al lienzo mediante `this`| El lienzo se pasa como parámetro  
  
## 

​

Migrar los menús de nodos

### 

​

Enfoque anterior (obsoleto)

El enfoque anterior modificaba el prototipo del tipo de nodo:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeType.comfyClass === "KSampler") {
          // ❌ ANTERIOR: parchear el prototipo del nodo
          const original = nodeType.prototype.getExtraMenuOptions
          nodeType.prototype.getExtraMenuOptions = function(canvas, options) {
            original?.apply(this, arguments)
    
            options.push({
              content: "Randomize Seed",
              callback: () => {
                const seedWidget = this.widgets.find(w => w.name === "seed")
                if (seedWidget) {
                  seedWidget.value = Math.floor(Math.random() * 1000000)
                }
              }
            })
          }
        }
      }
    })
    

### 

​

Enfoque nuevo (recomendado)

El enfoque nuevo usa un hook de extensión dedicado:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      // ✅ NUEVO: usa el hook getNodeMenuItems
      getNodeMenuItems(node) {
        const items = []
    
        // Añade elementos solo para tipos de nodo específicos
        if (node.comfyClass === "KSampler") {
          items.push({
            content: "Randomize Seed",
            callback: () => {
              const seedWidget = node.widgets.find(w => w.name === "seed")
              if (seedWidget) {
                seedWidget.value = Math.floor(Math.random() * 1000000)
              }
            }
          })
        }
    
        return items
      }
    })
    

### 

​

Diferencias clave

Enfoque anterior| Enfoque nuevo  
---|---  
Se modificaba en `beforeRegisterNodeDef()`| Usa el hook `getNodeMenuItems()`  
Específico por tipo mediante una comprobación `if`| Específico por tipo mediante una comprobación `if` en el hook  
Modifica el array `options`| Devuelve un array nuevo  
Acceso al nodo mediante `this`| El nodo se pasa como parámetro  
  
## 

​

Patrones comunes

### 

​

Elementos de menú condicionales

Ambos enfoques admiten elementos condicionales, pero la nueva API es más limpia:
    
    
    // ✅ NEW: Clean conditional logic
    getCanvasMenuItems(canvas) {
      const items = []
    
      if (canvas.selectedItems.size > 0) {
        items.push({
          content: `Process ${canvas.selectedItems.size} Selected Nodes`,
          callback: () => {
            // Process nodes
          }
        })
      }
    
      return items
    }
    

### 

​

Agregar separadores

Los separadores se agregan de la misma forma en ambos enfoques:
    
    
    getCanvasMenuItems(canvas) {
      return [
        null, // Separator (horizontal line)
        {
          content: "My Action",
          callback: () => {}
        }
      ]
    }
    

### 

​

Crear submenús

La forma recomendada de crear submenús es usar la propiedad declarativa `submenu`:
    
    
    getNodeMenuItems(node) {
      return [
        {
          content: "Advanced Options",
          submenu: {
            options: [
              { content: "Option 1", callback: () => {} },
              { content: "Option 2", callback: () => {} }
            ]
          }
        }
      ]
    }
    

Este enfoque declarativo es más limpio y coincide con los patrones usados en todo el código base de ComfyUI.

Aunque también se admite un enfoque basado en callbacks con `has_submenu: true` y `new LiteGraph.ContextMenu()`, se prefiere la propiedad declarativa `submenu` por su mejor mantenibilidad.

### 

​

Acceder al estado
    
    
    // ✅ NEW: State access is clearer
    getCanvasMenuItems(canvas) {
      // Access canvas properties
      const selectedCount = canvas.selectedItems.size
      const graphMousePos = canvas.graph_mouse
    
      return [/* menu items */]
    }
    
    getNodeMenuItems(node) {
      // Access node properties
      const nodeType = node.comfyClass
      const isDisabled = node.mode === 2
      const widgets = node.widgets
    
      return [/* menu items */]
    }
    

## 

​

Solución de problemas

### 

​

Cómo identificar el uso de la API antigua

Busca estos patrones en tu código:
    
    
    // ❌ Signs of old API:
    LGraphCanvas.prototype.getCanvasMenuOptions = function() { /* ... */ }
    nodeType.prototype.getExtraMenuOptions = function() { /* ... */ }
    

### 

​

Entender las advertencias de obsolescencia

Si ves esta advertencia en la consola:
    
    
    [DEPRECATED] Monkey-patching getCanvasMenuOptions is deprecated. (Extension: "MyExtension")
    Please use the new context menu API instead.
    See: https://docs.comfy.org/custom-nodes/js/context-menu-migration
    

Tu extensión está usando el enfoque anterior y debes migrarla.

### 

​

Verificar el éxito de la migración

Después de la migración:

  1. Elimina todas las modificaciones de prototipo de `setup()` y `beforeRegisterNodeDef()`
  2. Agrega los ganchos `getCanvasMenuItems()` y/o `getNodeMenuItems()`
  3. Verifica que tus elementos del menú sigan apareciendo correctamente
  4. Verifica que no aparezcan advertencias de obsolescencia en la consola



### 

​

Ejemplo completo de migración

**ANTES:**
    
    
    app.registerExtension({
      name: "MyExtension",
      async setup() {
        const original = LGraphCanvas.prototype.getCanvasMenuOptions
        LGraphCanvas.prototype.getCanvasMenuOptions = function() {
          const options = original.apply(this, arguments)
          options.push({ content: "Action", callback: () => {} })
          return options
        }
      },
      async beforeRegisterNodeDef(nodeType) {
        if (nodeType.comfyClass === "KSampler") {
          const original = nodeType.prototype.getExtraMenuOptions
          nodeType.prototype.getExtraMenuOptions = function(_, options) {
            original?.apply(this, arguments)
            options.push({ content: "Node Action", callback: () => {} })
          }
        }
      }
    })
    

**DESPUÉS:**
    
    
    app.registerExtension({
      name: "MyExtension",
      getCanvasMenuItems(canvas) {
        return [
          { content: "Action", callback: () => {} }
        ]
      },
      getNodeMenuItems(node) {
        if (node.comfyClass === "KSampler") {
          return [
            { content: "Node Action", callback: () => {} }
          ]
        }
        return []
      }
    })
    

## 

​

Recursos adicionales

  * [Ejemplos anotados](https://docs.comfy.org/es/custom-nodes/js/javascript_examples): Más ejemplos con la nueva API
  * [Ganchos de extensión](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks): Lista completa de los ganchos de extensión disponibles
  * [Comandos y atajos de teclado](https://docs.comfy.org/es/custom-nodes/js/javascript_commands_keybindings): Agrega atajos de teclado a las acciones de tu menú



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/context-menu-migration.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/context-menu-migration)

[Migración a V3](https://docs.comfy.org/es/custom-nodes/v3_migration)[Reemplazo de nodos](https://docs.comfy.org/es/custom-nodes/backend/node-replacement)
