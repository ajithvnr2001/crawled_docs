---
url: https://docs.comfy.org/es/built-in-nodes/MergeSplat/
title: Unir splats - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.865447+00:00
---

# Unir splats - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MergeSplat/

Splat

# Unir splats - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Fusionar Splats combina múltiples modelos de splat gaussiano en un solo splat mediante la concatenación de sus datos.

Copiar páginaCopiar página

El nodo Fusionar Splats combina múltiples modelos de splat gaussiano en un solo splat mediante la concatenación de sus datos. Esto es útil para fusionar varias decodificaciones del mismo latente generadas con diferentes semillas, lo que puede densificar la superficie y mejorar la calidad al crear mallas 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`splat0`| Primer splat gaussiano a fusionar| SPLAT| Sí| Al menos 1 splat requerido  
`splat1`| Segundo splat gaussiano a fusionar| SPLAT| Sí| Al menos 1 splat requerido  
`splat2`| Splat gaussiano adicional a fusionar (opcional)| SPLAT| No| Hasta 32 splats en total  
`splat3`| Splat gaussiano adicional a fusionar (opcional)| SPLAT| No| Hasta 32 splats en total  
…| Splats adicionales (hasta splat31)| SPLAT| No| Hasta 32 splats en total  
  
**Nota:** La lista de entradas agrega automáticamente nuevas ranuras a medida que conectas splats. Debes conectar al menos un splat. El nodo acepta un mínimo de 2 y un máximo de 32 splats.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`splat`| El splat gaussiano fusionado que contiene todos los splats de entrada concatenados| SPLAT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/es.md)

* * *

**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MergeSplat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MergeSplat)

[Obtener recuento de splats](https://docs.comfy.org/es/built-in-nodes/GetSplatCount)[Render Splat](https://docs.comfy.org/es/built-in-nodes/RenderSplat)
