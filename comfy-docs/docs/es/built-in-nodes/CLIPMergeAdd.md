---
url: https://docs.comfy.org/es/built-in-nodes/CLIPMergeAdd/
title: Fusionar CLIP (sumar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.003692+00:00
---

# Fusionar CLIP (sumar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPMergeAdd/

Fusión

# Fusionar CLIP (sumar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIPMergeAdd combina dos modelos CLIP agregando parches del segundo modelo al primero.

Copiar páginaCopiar página

El nodo CLIPMergeAdd combina dos modelos CLIP agregando parches del segundo modelo al primero. Crea una copia del primer modelo CLIP e incorpora selectivamente parches clave del segundo modelo, excluyendo los parámetros position IDs y logit scale. Esto permite fusionar componentes de modelos CLIP mientras se preserva la estructura del modelo base.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip1`| El modelo CLIP base que se clonará y se usará como base para la fusión| CLIP| Sí| -  
`clip2`| El modelo CLIP secundario que proporciona parches clave para agregarlos al modelo base| CLIP| Sí| -  
  
Las claves que terminan en `.position_ids` o `.logit_scale` de `clip2` se omiten, por lo que esos parámetros conservan los valores de `clip1`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CLIP`| Un modelo CLIP fusionado que contiene la estructura del modelo base con parches agregados del modelo secundario| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/es.md)

* * *

**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPMergeAdd.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPMergeAdd)

[Guardar punto de control](https://docs.comfy.org/es/built-in-nodes/CheckpointSave)[Fusionar CLIP (simple)](https://docs.comfy.org/es/built-in-nodes/CLIPMergeSimple)
