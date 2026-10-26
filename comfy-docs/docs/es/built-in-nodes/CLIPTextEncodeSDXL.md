---
url: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeSDXL/
title: Codificar texto CLIP para SDXL - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.462636+00:00
---

# Codificar texto CLIP para SDXL - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeSDXL/

Stable Diffusion

# Codificar texto CLIP para SDXL - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para codificar texto de entrada utilizando un modelo CLIP específicamente personalizado para la arquitectura SDXL.

Copiar páginaCopiar página

Este nodo está diseñado para codificar texto de entrada utilizando un modelo CLIP específicamente personalizado para la arquitectura SDXL. Emplea un sistema de codificación dual (CLIP-L y CLIP-G) para procesar descripciones textuales, lo que resulta en una generación de imágenes más precisa.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`clip`| Instancia del modelo CLIP utilizada para la codificación de texto.| CLIP  
`width`| Especifica el ancho de la imagen en píxeles, valor predeterminado 1024.| INT  
`height`| Especifica la altura de la imagen en píxeles, valor predeterminado 1024.| INT  
`crop_w`| Ancho del área de recorte en píxeles, valor predeterminado 0.| INT  
`crop_h`| Altura del área de recorte en píxeles, valor predeterminado 0.| INT  
`target_width`| Ancho objetivo para la imagen de salida, valor predeterminado 1024.| INT  
`target_height`| Altura objetivo para la imagen de salida, valor predeterminado 1024.| INT  
`text_g`| Descripción textual global para la descripción general de la escena.| STRING  
`text_l`| Descripción textual local para la descripción de detalles.| STRING  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Contiene el texto codificado y la información condicional necesaria para la generación de imágenes.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPTextEncodeSDXL.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPTextEncodeSDXL)

[Codificar texto CLIP para SD3](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeSD3)[Codificar texto CLIP para SDXL Refiner](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeSDXLRefiner)
