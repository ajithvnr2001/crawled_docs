---
url: https://docs.comfy.org/es/built-in-nodes/GetMeshInfo/
title: Obtener informaci\u00f3n de malla - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:51.550424+00:00
---

# Obtener información de malla - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GetMeshInfo/

Mallas

# Obtener información de malla - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Get Mesh Info informa el número de vértices y caras de una malla, junto con los atributos que contiene (como UVs, colores de vértices, normales y texturas).

Copiar páginaCopiar página

Get Mesh Info informa el número de vértices y caras de una malla, junto con los atributos que contiene (como UVs, colores de vértices, normales y texturas). El informe se muestra en el nodo y se devuelve como una salida de texto, mientras que la malla en sí pasa sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`malla`| La malla que se va a inspeccionar. El nodo cuenta sus vértices y caras, detecta qué atributos están presentes y pasa la malla sin cambios.| MESH| Sí| —  
  
Nota: Cuando la entrada contiene varias mallas (un lote), el informe muestra los recuentos totales de vértices y caras para todo el lote, además de un desglose por malla. Para lotes con relleno de ceros, se utilizan los recuentos por elemento almacenados en los datos de la malla.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`mesh`| La malla original, pasada sin ninguna modificación.| MESH  
`info`| Un informe de texto de varias líneas con el recuento de vértices, el recuento de caras y los atributos detectados (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Los atributos similares a texturas se muestran con sus dimensiones de altura × anchura. Los recuentos grandes se formatean con comas, por ejemplo “1,234,567 (1.23M)” o “12,345 (12.3K)”. El mismo texto se muestra en el nodo.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/es.md)

* * *

**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GetMeshInfo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GetMeshInfo)

[Rellenar agujeros](https://docs.comfy.org/es/built-in-nodes/FillHoles)[Combinar mallas](https://docs.comfy.org/es/built-in-nodes/MergeMeshes)
