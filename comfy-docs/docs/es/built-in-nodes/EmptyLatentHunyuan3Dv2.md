---
url: https://docs.comfy.org/es/built-in-nodes/EmptyLatentHunyuan3Dv2/
title: Latente Hunyuan 3D v2 vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.943159+00:00
---

# Latente Hunyuan 3D v2 vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyLatentHunyuan3Dv2/

Hunyuan 3d

# Latente Hunyuan 3D v2 vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea un lote de muestras latentes vacías (de todos ceros) formateadas para modelos de generación 3D Hunyuan3Dv2.

Copiar páginaCopiar página

Este nodo crea un lote de muestras latentes vacías (de todos ceros) formateadas para modelos de generación 3D Hunyuan3Dv2. Produce el tensor latente con la forma correcta que sirve como punto de partida para flujos de trabajo de generación 3D, con el latente etiquetado con el tipo “hunyuan3dv2”.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`resolución`| La dimensión de resolución del espacio latente a crear (predeterminado: 3072)| INT| Sí| 1 - 8192  
`tamaño_del_lote`| El número de imágenes latentes en el lote (predeterminado: 1)| INT| Sí| 1 - 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Un tensor latente vacío de forma [batch_size, 64, resolution] que contiene muestras rellenas de ceros, etiquetado con el tipo “hunyuan3dv2”| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/es.md)

* * *

**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyLatentHunyuan3Dv2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyLatentHunyuan3Dv2)

[Imagen Latente Vacía HiDream-O1](https://docs.comfy.org/es/built-in-nodes/EmptyHiDreamO1LatentImage)[Decodificación VAE de Hunyuan 3D](https://docs.comfy.org/es/built-in-nodes/VAEDecodeHunyuan3D)
