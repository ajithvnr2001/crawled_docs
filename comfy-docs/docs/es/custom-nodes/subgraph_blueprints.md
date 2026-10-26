---
url: https://docs.comfy.org/es/custom-nodes/subgraph_blueprints/
title: Planos de subgrafos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:51.785236+00:00
---

# Planos de subgrafos - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/subgraph_blueprints/

## En esta página

Volver arriba

  * Ejemplo
  * Crear un archivo JSON de subgrafo
  * Ver también



Package & Publish

# Planos de subgrafos

Copiar páginaCopiar página

Publica grupos de nodos reutilizables como planos de subgrafos en tus nodos personalizados de ComfyUI, accesibles desde el menú de subgrafos.

Copiar páginaCopiar página

Si tienes componentes de subgrafo reutilizables asociados a tus nodos personalizados, ComfyUI puede ponerlos a disposición de los usuarios como planos de subgrafos globales. Los planos de subgrafos permiten a los usuarios añadir rápidamente grupos de nodos ya creados desde el menú de subgrafos. Como desarrollador de nodos, todo lo que tienes que hacer es crear una carpeta `subgraphs` en el directorio de tu nodo personalizado y colocar allí los archivos `.json`. Internamente, ComfyUI busca archivos de subgrafos en todos los directorios de nodos personalizados y los sirve a través del endpoint de API `/global_subgraphs`.

## 

​

Ejemplo

Dentro del directorio `ComfyUI-MyCustomNodeModule/subgraphs/`:

  * `My_upscale_subgraph.json`
  * `My_effects_subgraph.json`

En este ejemplo, el navegador de subgrafos de ComfyUI muestra los planos de `ComfyUI-MyCustomNodeModule` que los usuarios pueden añadir a sus flujos de trabajo.

## 

​

Crear un archivo JSON de subgrafo

Los archivos JSON de subgrafos usan el mismo formato que los archivos JSON de flujos de trabajo. La forma más sencilla de crear uno:

  1. Crea tu subgrafo en ComfyUI
  2. Selecciona los nodos que quieres incluir
  3. Conviértelos en un subgrafo
  4. Exporta el subgrafo como JSON
  5. Coloca el archivo JSON en tu carpeta `subgraphs/`



## 

​

Ver también

  * [Subgrafos (guía del usuario)](https://docs.comfy.org/es/interface/features/subgraph): cómo interactúan los usuarios con los subgrafos
  * [Guía para desarrolladores de subgrafos](https://docs.comfy.org/es/custom-nodes/js/subgraphs): desarrollo de extensiones de frontend para subgrafos
  * [Plantillas de flujos de trabajo](https://docs.comfy.org/es/custom-nodes/workflow_templates): cómo añadir flujos de trabajo de ejemplo a tus nodos personalizados



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/subgraph_blueprints.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/subgraph_blueprints)

[Plantillas de flujos de trabajo](https://docs.comfy.org/es/custom-nodes/workflow_templates)[Descripción general del Registry](https://docs.comfy.org/es/registry/overview)
