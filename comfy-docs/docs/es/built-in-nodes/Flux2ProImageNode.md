---
url: https://docs.comfy.org/es/built-in-nodes/Flux2ProImageNode/
title: Imagen Flux.2 [pro] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:47.500178+00:00
---

# Imagen Flux.2 [pro] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Flux2ProImageNode/

Imagen

# Imagen Flux.2 [pro] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera una imagen con Flux.2 [pro] mediante la API de BFL a partir de un prompt y dimensiones de salida explícitas

Copiar páginaCopiar página

Genera una imagen con Flux.2 [pro] mediante la API de BFL a partir de un prompt y dimensiones de salida explícitas, opcionalmente guiado por imágenes de referencia. **Nota:** Este nodo está marcado como obsoleto en el código fuente.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt para la generación o edición de la imagen.| STRING| Sí| -  
`ancho`| Ancho de la imagen generada en píxeles (predeterminado: 1024).| INT| Sí| 256 a 2048 (paso 32)  
`alto`| Alto de la imagen generada en píxeles (predeterminado: 768).| INT| Sí| 256 a 2048 (paso 32)  
`semilla`| La semilla aleatoria utilizada para crear el ruido (predeterminado: 0).| INT| Sí| 0 a 18446744073709551615  
`mejora_de_prompt`| Indica si se debe realizar un sobremuestreo (upsampling) en el prompt. Si está activo, el prompt se modifica automáticamente para una generación más creativa (predeterminado: `True`). Esta es una configuración avanzada.| BOOLEAN| Sí| True / False  
`imágenes`| Imágenes de referencia opcionales para la generación de imagen a imagen. Cada imagen se reduce a un máximo de 2048x2048 píxeles antes de la carga.| IMAGE| No| 0 a 9 imágenes  
  
**Restricciones:**

  * Conectar más de 9 imágenes de referencia genera un error.
  * El tamaño de salida se cobra por megapíxel, por lo que valores mayores de `width` y `height` cuestan más.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`IMAGE`| La imagen generada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ProImageNode/es.md)

* * *

**Source fingerprint (SHA-256):** `ffa3934abaa38e030eedf2624e7a91333e24a92d7ac89af8637e59d59341eb6d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Flux2ProImageNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Flux2ProImageNode)

[Imagen Flux.2 [max]](https://docs.comfy.org/es/built-in-nodes/Flux2MaxImageNode)[Imagen Flux.1 Kontext [máx]](https://docs.comfy.org/es/built-in-nodes/FluxKontextMaxImageNode)
