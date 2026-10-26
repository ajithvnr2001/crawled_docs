---
url: https://docs.comfy.org/es/built-in-nodes/StableCascade_EmptyLatentImage/
title: Imagen latente Stable Cascade vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:32.286902+00:00
---

# Imagen latente Stable Cascade vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StableCascade_EmptyLatentImage/

Stable Cascade

# Imagen latente Stable Cascade vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo StableCascadeEmptyLatentImage crea tensores latentes vacíos para modelos Stable Cascade.

Copiar páginaCopiar página

El nodo StableCascade_EmptyLatentImage crea tensores latentes vacíos para modelos Stable Cascade. Genera dos representaciones latentes separadas, una para la etapa C y otra para la etapa B, con dimensiones calculadas a partir de la resolución de entrada y la configuración de compresión. Este nodo proporciona un punto de partida para el pipeline de generación de Stable Cascade.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho de la imagen de salida en píxeles (predeterminado: 1024, paso: 8)| INT| Sí| 256 a MAX_RESOLUTION  
`altura`| La altura de la imagen de salida en píxeles (predeterminado: 1024, paso: 8)| INT| Sí| 256 a MAX_RESOLUTION  
`compresión`| El factor de compresión que determina las dimensiones latentes para la etapa C (predeterminado: 42, paso: 1). Este es un parámetro avanzado.| INT| Sí| 4 a 128  
`tamaño_del_lote`| El número de muestras latentes que se generarán en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
  
Nota: El valor de `compression` controla el tamaño latente de la etapa C: su altura y ancho son la `height` y la `width` de entrada divididas por `compression`. El latente de la etapa B siempre usa una compresión fija de 4.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`stage_c`| El tensor latente de la etapa C con dimensiones [batch_size, 16, height//compression, width//compression]| LATENT  
`stage_b`| El tensor latente de la etapa B con dimensiones [batch_size, 4, height//4, width//4]| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/es.md)

* * *

**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StableCascade_EmptyLatentImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StableCascade_EmptyLatentImage)

[Unir latentes de SeedVR2](https://docs.comfy.org/es/built-in-nodes/SeedVR2TemporalMerge)[Codificación VAE de la etapa C de Stable Cascade](https://docs.comfy.org/es/built-in-nodes/StableCascade_StageC_VAEEncode)
