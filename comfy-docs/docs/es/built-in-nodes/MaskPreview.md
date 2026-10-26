---
url: https://docs.comfy.org/es/built-in-nodes/MaskPreview/
title: Previsualizar m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.240889+00:00
---

# Previsualizar máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MaskPreview/

Máscara

# Previsualizar máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo MaskPreview muestra una vista previa visual de los datos de la máscara directamente en la interfaz de ComfyUI, sin guardarla en el directorio de salida.

Copiar páginaCopiar página

El nodo MaskPreview muestra una vista previa visual de los datos de la máscara directamente en la interfaz de ComfyUI, sin guardarla en el directorio de salida. Esto te permite inspeccionar la máscara en cualquier punto de tu flujo de trabajo, mientras que la máscara también pasa a través del nodo sin cambios para que pueda seguir usándose en etapas posteriores.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`mask`| Los datos de máscara que se van a previsualizar| MASK| Sí| -  
`filename_prefix`| Prefijo de nombre de archivo usado para la vista previa (predeterminado: “ComfyUI”)| STRING| No| -  
`prompt`| Información de prompt para metadatos (proporcionada automáticamente)| PROMPT| No| -  
`extra_pnginfo`| Información PNG adicional para metadatos (proporcionada automáticamente)| EXTRA_PNGINFO| No| -  
  
Solo `mask` es una entrada visible que debe conectarse. Los parámetros `filename_prefix`, `prompt` y `extra_pnginfo` son proporcionados por el sistema: `filename_prefix` usa su valor predeterminado, mientras que `prompt` y `extra_pnginfo` están ocultos y son proporcionados automáticamente por el entorno de ejecución de ComfyUI.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`mask`| Los mismos datos de máscara que se previsualizaron, devueltos sin cambios para que puedan usarse en otra parte del flujo de trabajo| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/es.md)

* * *

**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MaskPreview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MaskPreview)

[Componer máscara](https://docs.comfy.org/es/built-in-nodes/MaskComposite)[Convertir máscara a imagen](https://docs.comfy.org/es/built-in-nodes/MaskToImage)
