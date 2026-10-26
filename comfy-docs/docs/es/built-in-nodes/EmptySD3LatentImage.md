---
url: https://docs.comfy.org/es/built-in-nodes/EmptySD3LatentImage/
title: Imagen latente SD3 vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.326958+00:00
---

# Imagen latente SD3 vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptySD3LatentImage/

Stable Diffusion

# Imagen latente SD3 vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

EmptySD3LatentImage crea una imagen latente en blanco (todo ceros) con la disposición que esperan los modelos Stable Diffusion 3.

Copiar páginaCopiar página

EmptySD3LatentImage crea una imagen latente en blanco (todo ceros) con la disposición que esperan los modelos Stable Diffusion 3. Como el latente está vacío, normalmente se usa como el punto de partida que un flujo de trabajo de generación rellena con una imagen. El ancho y el alto que elijas determinan el tamaño de la imagen final.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho de la imagen latente en píxeles (predeterminado: 1024). Los valores se incrementan en pasos de 16.| INT| Sí| 16 a MAX_RESOLUTION (paso: 16)  
`altura`| El alto de la imagen latente en píxeles (predeterminado: 1024). Los valores se incrementan en pasos de 16.| INT| Sí| 16 a MAX_RESOLUTION (paso: 16)  
`tamaño_del_lote`| La cantidad de imágenes latentes a generar en el lote (predeterminado: 1).| INT| Sí| 1 a 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`LATENT`| Un tensor latente que contiene muestras en blanco (todo ceros) en el formato compatible con SD3. El tensor tiene 16 canales, se reduce por un factor de 8 en relación con `width` y `height`, y tiene una relación de reducción espacial de 8.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/es.md)

* * *

**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptySD3LatentImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptySD3LatentImage)

[Codificación VAE de la etapa C de Stable Cascade](https://docs.comfy.org/es/built-in-nodes/StableCascade_StageC_VAEEncode)[Recortar latente](https://docs.comfy.org/es/built-in-nodes/LatentCrop)
