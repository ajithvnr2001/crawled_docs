---
url: https://docs.comfy.org/es/built-in-nodes/TencentSmartTopologyNode/
title: Hunyuan3D: Topolog\u00eda inteligente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.621304+00:00
---

# Hunyuan3D: Topología inteligente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TencentSmartTopologyNode/

Tencent

# Hunyuan3D: Topología inteligente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo realiza una retopología inteligente en un modelo 3D, creando automáticamente una nueva malla más limpia con un recuento de polígonos optimizado.

Copiar páginaCopiar página

Este nodo realiza una retopología inteligente en un modelo 3D, creando automáticamente una nueva malla más limpia con un recuento de polígonos optimizado. Se conecta a una API de Tencent Hunyuan 3D para procesar el modelo, compatible con formatos de archivo GLB y OBJ de hasta 200 MB. El nodo devuelve el modelo procesado como un archivo OBJ.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo_3d`| Modelo 3D de entrada (GLB u OBJ). El archivo debe estar en formato GLB u OBJ y no puede superar los 200 MB.| FILE3D| Sí| -  
`tipo_de_polígono`| Tipo de composición de la superficie.| STRING| Sí| `"triangle"`  
`"quadrilateral"`  
`nivel_de_caras`| Nivel de reducción de polígonos.| STRING| Sí| `"medium"`  
`"high"`  
`"low"`  
`semilla`| La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (valor predeterminado: 0)| INT| No| 0 a 2147483647  
  
**Nota:** El parámetro `seed` se utiliza para activar una re-ejecución del nodo, pero no se garantiza que el resultado final sea el mismo para el mismo valor de semilla.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`OBJ`| El modelo 3D procesado con topología optimizada, devuelto en formato OBJ.| FILE3D  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/es.md)

* * *

**Source fingerprint (SHA-256):** `13c2dce5f5fbc46a505d0366d8da1c4e762d3a64d11fae1bcceebd510b273f62`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TencentSmartTopologyNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TencentSmartTopologyNode)

[Hunyuan3D: Modelo a UV](https://docs.comfy.org/es/built-in-nodes/TencentModelTo3DUVNode)[Hunyuan3D: Texto a modelo (Pro)](https://docs.comfy.org/es/built-in-nodes/TencentTextToModelNode)
