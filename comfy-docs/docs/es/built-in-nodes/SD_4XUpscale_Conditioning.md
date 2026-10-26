---
url: https://docs.comfy.org/es/built-in-nodes/SD_4XUpscale_Conditioning/
title: Acondicionamiento SD ampliar 4X - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:26.557216+00:00
---

# Acondicionamiento SD ampliar 4X - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SD_4XUpscale_Conditioning/

Stable Diffusion Upscaler

# Acondicionamiento SD ampliar 4X - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SD4XUpscaleConditioning prepara datos de condicionamiento para aumentar la escala de imágenes con modelos de difusión.

Copiar páginaCopiar página

El nodo SD_4XUpscale_Conditioning prepara datos de condicionamiento para aumentar la escala de imágenes con modelos de difusión. Escala las imágenes de entrada según una proporción elegida, añade un aumento de ruido opcional y devuelve el condicionamiento positivo y negativo modificados junto con un latente vacío para el tamaño escalado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imágenes`| Imágenes de entrada que se van a escalar.| IMAGE| Sí| -  
`positivo`| Datos de condicionamiento positivo que guían la generación hacia el contenido deseado.| CONDITIONING| Sí| -  
`negativo`| Datos de condicionamiento negativo que alejan la generación del contenido no deseado.| CONDITIONING| Sí| -  
`relación_escala`| Multiplicador aplicado a las dimensiones de la imagen de entrada al preparar el condicionamiento y el latente escalados (predeterminado: 4.0).| FLOAT| Sí| 0.0 - 10.0 (paso 0.01)  
`aumento_ruido`| Cantidad de ruido que se añadirá durante el proceso de escalado (predeterminado: 0.0).| FLOAT| Sí| 0.0 - 1.0 (paso 0.001)  
  
Nota: `noise_augmentation` es un parámetro avanzado, que se muestra en la interfaz del nodo bajo el conmutador “Advanced”.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Condicionamiento positivo modificado con los datos de imagen escalados y la configuración de aumento de ruido aplicados.| CONDITIONING  
`negative`| Condicionamiento negativo modificado con los datos de imagen escalados y la configuración de aumento de ruido aplicados.| CONDITIONING  
`latent`| Representación latente vacía que coincide con las dimensiones escaladas.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SD_4XUpscale_Conditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SD_4XUpscale_Conditioning)

[Codificar texto CLIP para SDXL Refiner](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeSDXLRefiner)[Acondicionamiento SV3D](https://docs.comfy.org/es/built-in-nodes/SV3D_Conditioning)
