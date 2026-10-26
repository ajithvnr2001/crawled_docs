---
url: https://docs.comfy.org/es/built-in-nodes/LatentOperationTonemapReinhard/
title: Operaci\u00f3n latente tonemap Reinhard - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.018097+00:00
---

# Operación latente tonemap Reinhard - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentOperationTonemapReinhard/

Operaciones

# Operación latente tonemap Reinhard - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea una operación latente que aplica mapeo tonal Reinhard a vectores latentes.

Copiar páginaCopiar página

Este nodo crea una operación latente que aplica mapeo tonal Reinhard a vectores latentes. Normaliza cada vector latente, mide la distribución de magnitud general (media y desviación estándar) y luego comprime las magnitudes extremas usando la curva de Reinhard, con la intensidad general controlada por un multiplicador. El nodo está marcado como experimental (también se puede buscar como “hdr latent”).

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`multiplicador`| Controla la intensidad del efecto de mapeo tonal (predeterminado: 1.0)| FLOAT| Sí| 0.0 a 100.0 (paso 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`operation`| Devuelve una operación de mapeo tonal que se puede aplicar a vectores latentes| LATENT_OPERATION  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/es.md)

* * *

**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentOperationTonemapReinhard.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentOperationTonemapReinhard)

[Operación de enfoque de latente](https://docs.comfy.org/es/built-in-nodes/LatentOperationSharpen)[Sumar latentes](https://docs.comfy.org/es/built-in-nodes/LatentAdd)
