---
url: https://docs.comfy.org/es/built-in-nodes/CheckpointLoader/
title: Cargar punto de control con configuraci\u00f3n (OBSOLETO) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.678427+00:00
---

# Cargar punto de control con configuración (OBSOLETO) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CheckpointLoader/

Cargadores

# Cargar punto de control con configuración (OBSOLETO) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CheckpointLoader carga un checkpoint de modelo preentrenado junto con su archivo de configuración.

Copiar páginaCopiar página

El nodo CheckpointLoader carga un checkpoint de modelo preentrenado junto con su archivo de configuración. Toma un archivo de configuración y un archivo de checkpoint como entradas y devuelve los componentes del modelo cargado — el modelo principal, el modelo CLIP y el modelo VAE — para su uso en el flujo de trabajo. Este nodo está obsoleto.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`nombre_configuración`| El archivo de configuración que define la arquitectura y los ajustes del modelo| COMBO| Sí| Archivos de configuración disponibles  
`nombre_ckpt`| El archivo de checkpoint que contiene los pesos y parámetros del modelo entrenado| COMBO| Sí| Archivos de checkpoint disponibles  
  
**Nota:** Este nodo requiere que se seleccionen tanto un archivo de configuración como un archivo de checkpoint. El archivo de configuración debe coincidir con la arquitectura del archivo de checkpoint que se está cargando.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El componente principal del modelo cargado, listo para inferencia| MODEL  
`CLIP`| El componente del modelo CLIP cargado para codificación de texto| CLIP  
`VAE`| El componente del modelo VAE cargado para codificación y decodificación de imágenes| VAE  
  
**Nota importante:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras. Considere utilizar nodos de carga alternativos para nuevos flujos de trabajo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CheckpointLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CheckpointLoader)

[Cargar codificador de audio](https://docs.comfy.org/es/built-in-nodes/AudioEncoderLoader)[Cargar punto de control](https://docs.comfy.org/es/built-in-nodes/CheckpointLoaderSimple)
