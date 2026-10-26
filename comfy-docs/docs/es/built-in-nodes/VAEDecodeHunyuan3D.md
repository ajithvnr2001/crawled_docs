---
url: https://docs.comfy.org/es/built-in-nodes/VAEDecodeHunyuan3D/
title: Decodificaci\u00f3n VAE de Hunyuan 3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.273933+00:00
---

# Decodificación VAE de Hunyuan 3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEDecodeHunyuan3D/

Hunyuan 3d

# Decodificación VAE de Hunyuan 3D - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D mediante un decodificador VAE.

Copiar páginaCopiar página

El nodo VAEDecodeHunyuan3D convierte representaciones latentes en datos de vóxeles 3D mediante un decodificador VAE. Procesa las muestras latentes a través del modelo VAE con configuraciones ajustables de fragmentación y resolución para generar datos volumétricos adecuados para aplicaciones 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`muestras`| La representación latente que se decodificará en datos de vóxeles 3D| LATENT| Sí| -  
`vae`| El modelo VAE utilizado para decodificar las muestras latentes| VAE| Sí| -  
`num_chunks`| El número de fragmentos en los que se divide el procesamiento para la gestión de memoria. Parámetro avanzado (valor predeterminado: 8000)| INT| Sí| 1000-500000  
`resolución_octree`| La resolución de la estructura de octree utilizada para la generación de vóxeles 3D. Parámetro avanzado (valor predeterminado: 256)| INT| Sí| 16-512  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`voxels`| Los datos de vóxeles 3D generados a partir de la representación latente decodificada| VOXEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/es.md)

* * *

**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEDecodeHunyuan3D.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEDecodeHunyuan3D)

[Latente Hunyuan 3D v2 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyLatentHunyuan3Dv2)[Imagen latente Hunyuan vacía](https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanImageLatent)
