---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_examples/
title: Ejemplos anotados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:50.775474+00:00
---

# Ejemplos anotados - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_examples/

## En esta página

Volver arriba

  * Menús de clic derecho
    * Menú del fondo
    * Menú del nodo
    * Submenús
  * Capturar eventos de la UI
  * Detectar cuándo empieza un flujo de trabajo
  * Detectar un flujo de trabajo interrumpido
  * Capturar clics en tu nodo



JavaScript (UI)

# Ejemplos anotados

Copiar páginaCopiar página

Explora ejemplos de JavaScript de Comfy para crear Nodos personalizados y Extensiones de UI. Fragmentos de código prácticos para interfaces web robustas.

Copiar páginaCopiar página

Una colección cada vez mayor de fragmentos de código de ejemplo…

## 

​

Menús de clic derecho

### 

​

Menú del fondo

El menú principal del fondo (clic derecho sobre el lienzo) se genera con una llamada a `LGraphCanvas.getCanvasMenuOptions`. La forma estándar de editarlo es implementar el método `getCanvasMenuItems` en tu extensión:
    
    
    app.registerExtension({
      name: "MyExtension",
      getCanvasMenuItems(canvas) {
        const items = []
        items.push(null) // inserts a divider
        items.push({
          content: "The text for the menu",
          callback: async () => {
            // do whatever
          }
        })
        return items
      }
    });
    

### 

​

Menú del nodo

Cuando haces clic derecho sobre un nodo, el menú se genera de forma similar mediante `node.getExtraMenuOptions`. La forma estándar es implementar el método `getNodeMenuItems` en tu extensión:
    
    
    app.registerExtension({
      name: "MyExtension",
      getNodeMenuItems(node) {
        const items = []
    
        // You can filter by node type if needed
        if (node.comfyClass === "MyNodeClass") {
          items.push({
            content: "Do something fun",
            callback: async () => {
              // fun thing
            }
          })
        }
    
        return items
      }
    });
    

### 

​

Submenús

Si quieres un submenú, usa la propiedad `submenu` con un arreglo `options`:
    
    
    app.registerExtension({
      name: "MyExtension",
      getCanvasMenuItems(canvas) {
        const items = []
        items.push({
          content: "Menu with options",
          submenu: {
            options: [
              {
                content: "option 1",
                callback: (v) => {
                  // do something with v
                }
              },
              {
                content: "option 2",
                callback: (v) => {
                  // do something with v
                }
              },
              {
                content: "option 3",
                callback: (v) => {
                  // do something with v
                }
              }
            ]
          }
        })
        return items
      }
    });
    

## 

​

Capturar eventos de la UI

Esto funciona tal como esperas: busca el elemento de la UI en el DOM y añade un eventListener. `setup()` es un buen lugar para hacerlo, ya que la página se ha cargado por completo. Por ejemplo, para detectar un clic en el botón ‘Queue’:
    
    
    function queue_button_pressed() { console.log("Queue button was pressed!") }
    document.getElementById("queue-button").addEventListener("click", queue_button_pressed);
    

## 

​

Detectar cuándo empieza un flujo de trabajo

Este es uno de los muchos eventos de `api`:
    
    
    import { api } from "../../scripts/api.js";
    /* in setup() */
        function on_execution_start() { 
            /* do whatever */
        }
        api.addEventListener("execution_start", on_execution_start);
    

## 

​

Detectar un flujo de trabajo interrumpido

**Obsoleto:** El patrón de interceptación de la API que se muestra abajo está obsoleto y puede cambiar en cualquier momento en un futuro próximo. Usa los [ganchos de extensión](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks) oficiales y los escuchadores de eventos de la API cuando estén disponibles.

Un ejemplo sencillo de interceptación de la api:
    
    
    import { api } from "../../scripts/api.js";
    /* in setup() */
        const original_api_interrupt = api.interrupt;
        api.interrupt = function () {
            /* Do something before the original method is called */
            original_api_interrupt.apply(this, arguments);
            /* Or after */
        }
    

## 

​

Capturar clics en tu nodo

**Obsoleto:** El patrón de interceptación de métodos de nodo que se muestra abajo está obsoleto y puede cambiar en cualquier momento en un futuro próximo. Usa los [ganchos de extensión](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks) oficiales cuando estén disponibles.

`node` tiene un método mouseDown que puedes interceptar. Esta vez tenemos cuidado de propagar cualquier valor de retorno.
    
    
    async nodeCreated(node) {
        if (node?.comfyClass === "My Node Name") {
            const original_onMouseDown = node.onMouseDown;
            node.onMouseDown = function( e, pos, canvas ) {
                alert("ouch!");
                return original_onMouseDown?.apply(this, arguments);
            }        
        }
    }
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_examples.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_examples)

[Subgrafos](https://docs.comfy.org/es/custom-nodes/js/subgraphs)[Soporte i18n](https://docs.comfy.org/es/custom-nodes/i18n)
