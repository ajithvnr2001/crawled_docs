---
url: https://docs.comfy.org/es/custom-nodes/js/subgraphs/
title: Subgrafos de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.667424+00:00
---

# Subgrafos de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/subgraphs/

## En esta página

Volver arriba

  * Descripción general
  * Identificadores de nodo
  * Recorrer los nodos
    * Solo la capa actual
    * Todos los nodos de forma recursiva
  * Grafo raíz vs grafo activo
  * Eventos
    * Eventos de nivel de subgrafo
    * Eventos de nivel de lienzo
    * Patrón de escucha
  * Promoción de widgets
  * Limpieza
  * Véase también



JavaScript (UI)

# Subgrafos de ComfyUI

Copiar páginaCopiar página

Trabaja con subgrafos en extensiones de ComfyUI: IDs de nodo, recorrido del gráfico, eventos, promoción de widgets y limpieza.

Copiar páginaCopiar página

## 

​

Descripción general

Los subgrafos permiten agrupar nodos en componentes reutilizables y anidables. Cada subgrafo es su propio `LGraph` con un UUID. Para la guía de usuario, consulta [Subgrafos](https://docs.comfy.org/es/interface/features/subgraph).

## 

​

Identificadores de nodo

ComfyUI usa tres tipos distintos de identificador de nodo. Usar el equivocado provoca fallos silenciosos.

Tipo| Formato| Se usa para  
---|---|---  
`node.id`| `42` (número)| Local a su nivel inmediato del grafo. `graph.getNodeById(id)`  
ID de ejecución| `"1:2:3"` (cadena separada por dos puntos)| Mensajes de progreso del backend, `UNIQUE_ID`  
ID de localizador| `"<uuid>:<localId>"` o `"<localId>"`| Estado de la UI: insignias, errores, imágenes  
  
Para construir el ID de localizador de un nodo desde dentro de una extensión:
    
    
    function getLocatorId(node) {
      const graphId = node.graph?.id
      return graphId ? `${graphId}:${node.id}` : String(node.id)
    }
    

## 

​

Recorrer los nodos

### 

​

Solo la capa actual
    
    
    for (const node of app.graph.nodes) {
      console.log(node.id, node.type)
    }
    

### 

​

Todos los nodos de forma recursiva

Para entrar en subgrafos anidados, usa un helper recursivo que llame a un callback en cada nodo:
    
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    

Ejemplo completo:
    
    
    import { app } from "../../scripts/app.js"
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    
    app.registerExtension({
      name: "MyExtension.SubgraphWalker",
      async afterConfigureGraph() {
        walkGraph(app.graph, (node, graph) => {
          console.log(`[${graph.id ?? "root"}] node ${node.id}: ${node.type}`)
        })
      }
    })
    

## 

​

Grafo raíz vs grafo activo

Quieres…| Usa  
---|---  
Operar sobre todos los nodos del flujo de trabajo| `app.graph` (raíz)  
Operar solo sobre la capa visible| `app.canvas?.graph`  
Acceder a un subgrafo específico| `someNode.subgraph`  
      
    
    // All nodes (including nested subgraphs)
    walkGraph(app.graph, (node) => { /* ... */ })
    
    // Only nodes the user currently sees
    for (const node of app.canvas?.graph?.nodes ?? []) { /* ... */ }
    

## 

​

Eventos

### 

​

Eventos de nivel de subgrafo

Se emiten en `subgraph.events`:

Evento| Carga útil| Cuándo  
---|---|---  
`widget-promoted`| `{ widget, subgraphNode }`| Widget promovido al nodo padre  
`widget-demoted`| `{ widget, subgraphNode }`| Widget eliminado del nodo padre  
`input-added`| `{ input }`| Ranura de entrada añadida  
`removing-input`| `{ input, index }`| Ranura de entrada en proceso de eliminación  
`output-added`| `{ output }`| Ranura de salida añadida  
`removing-output`| `{ output, index }`| Ranura de salida en proceso de eliminación  
`renaming-input`| `{ input, index, oldName, newName }`| Ranura de entrada renombrada  
`renaming-output`| `{ output, index, oldName, newName }`| Ranura de salida renombrada  
  
### 

​

Eventos de nivel de lienzo

Se emiten en `app.canvas.canvas` (el elemento canvas de HTML):

Evento| Carga útil| Cuándo  
---|---|---  
`subgraph-opened`| `{ subgrafo, closingGraph, fromNode }`| El usuario navega dentro de un subgrafo  
`subgraph-converted`| `{ subgraphNode }`| Una selección se convierte en un subgrafo  
  
### 

​

Patrón de escucha
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension.SubgraphEvents",
      async setup() {
        app.canvas.canvas.addEventListener("subgraph-opened", (e) => {
          const { subgraph, fromNode } = e.detail
          console.log(`Opened subgraph from node ${fromNode.id}`)
        })
      }
    })
    

## 

​

Promoción de widgets

Cuando un `SubgraphInput` se conecta a un widget dentro de un subgrafo, aparece una copia de ese widget en el nodo de subgrafo padre. Esto dispara `widget-promoted`. Eliminar la conexión dispara `widget-demoted`.

El comportamiento de la promoción de widgets todavía está en evolución y puede cambiar en versiones futuras.
    
    
    import { app } from "../../scripts/app.js"
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    
    app.registerExtension({
      name: "MyExtension.WidgetPromotion",
      async afterConfigureGraph() {
        walkGraph(app.graph, (node) => {
          if (!node.subgraph) return
          if (node._promCleanup) node._promCleanup.abort()
          const controller = new AbortController()
          node._promCleanup = controller
          const { signal } = controller
    
          node.subgraph.events.addEventListener("widget-promoted", (e) => {
            console.log(`Widget "${e.detail.widget.name}" promoted`)
          }, { signal })
    
          node.subgraph.events.addEventListener("widget-demoted", (e) => {
            console.log(`Widget "${e.detail.widget.name}" demoted`)
          }, { signal })
    
          const origRemoved = node.onRemoved
          node.onRemoved = function () {
            controller.abort()
            origRemoved?.apply(this, arguments)
          }
        })
      }
    })
    

## 

​

Limpieza

Usa un `AbortController` para limpiar todos los listeners de eventos cuando se elimina un nodo.
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension.Cleanup",
      async nodeCreated(node) {
        if (!node.subgraph) return
    
        const controller = new AbortController()
        const { signal } = controller
    
        node.subgraph.events.addEventListener("input-added", (e) => {
          console.log(`Input added: ${e.detail.input.name}`)
        }, { signal })
    
        node.subgraph.events.addEventListener("removing-input", (e) => {
          console.log(`Input removing: ${e.detail.input.name}`)
        }, { signal })
    
        const origRemoved = node.onRemoved
        node.onRemoved = function () {
          controller.abort()
          origRemoved?.apply(this, arguments)
        }
      }
    })
    

`onRemoved` también puede dispararse durante la conversión de un subgrafo, no solo al eliminar. Protege la lógica de desmontaje si necesitas conservar el estado durante la reestructuración.

## 

​

Véase también

  * [Subgrafos (guía del usuario)](https://docs.comfy.org/es/interface/features/subgraph)
  * [Ganchos de extensión](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/subgraphs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/subgraphs)

[API del menú de la barra superior](https://docs.comfy.org/es/custom-nodes/js/javascript_topbar_menu)[Ejemplos anotados](https://docs.comfy.org/es/custom-nodes/js/javascript_examples)
