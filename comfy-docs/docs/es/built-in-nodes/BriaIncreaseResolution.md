---
url: https://docs.comfy.org/es/built-in-nodes/BriaIncreaseResolution/
title: Aumentar resoluci\u00f3n con Bria - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:32.993458+00:00
---

# Aumentar resolución con Bria - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaIncreaseResolution/

Bria

# Aumentar resolución con Bria - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Bria Increase Resolution aumenta la resolución de una imagen de entrada 2x o 4x usando el servicio de escalado de imágenes de Bria

Copiar páginaCopiar página

Bria Increase Resolution aumenta la resolución de una imagen de entrada 2x o 4x usando el servicio de escalado de imágenes de Bria, preservando el contenido original. El nodo sube la imagen, la envía para su procesamiento en el servicio de Bria, espera el resultado y devuelve la imagen escalada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se va a escalar.| IMAGE| Sí| Imagen única  
`desired_increase`| Multiplicador de resolución. La salida debe caber dentro de 8192 píxeles en cada lado.| COMBO| Sí| ”2"  
"4”  
`auto_downscale`| Reduce automáticamente el multiplicador y escala hacia abajo la imagen de entrada si eso aún no es suficiente, cuando la salida superaría el límite. (predeterminado: False)| BOOLEAN| Sí| True  
False  
`moderación`| Configuración de moderación. Cuando se establece en “true”, habilita las subopciones `visual_input_moderation` y `visual_output_moderation`, ambas con valor predeterminado False.| DYNAMIC_COMBO| Sí| ”false"  
"true”  
  
Notas:

  * Cuando `moderation` se establece en “true”, las subopciones `visual_input_moderation` y `visual_output_moderation` están disponibles, ambas con valor predeterminado False. Controlan la moderación de la imagen de entrada y del contenido de la imagen de salida.
  * El nodo impone un lado máximo de salida de 8192 píxeles. Si el multiplicador seleccionado excediera este límite y `auto_downscale` está deshabilitado, se genera un error. Habilitar `auto_downscale` permite que el nodo use automáticamente un multiplicador menor o reduzca la escala de la imagen de entrada en su lugar.
  * Bria primero amplía el lado corto de la imagen de entrada a al menos 224 píxeles antes de escalarla. Las imágenes demasiado alargadas pueden provocar un error que solicita recortarlas a una forma más cuadrada.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen escalada devuelta por el servicio de Bria.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/es.md)

* * *

**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaIncreaseResolution.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaIncreaseResolution)

[Bria FIBO 2.0 Image Edit](https://docs.comfy.org/es/built-in-nodes/BriaImageEditNode)[Bria Reiluminar](https://docs.comfy.org/es/built-in-nodes/BriaRelight)
