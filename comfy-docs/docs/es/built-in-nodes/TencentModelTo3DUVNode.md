---
url: https://docs.comfy.org/es/built-in-nodes/TencentModelTo3DUVNode/
title: Hunyuan3D: Modelo a UV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.544030+00:00
---

# Hunyuan3D: Modelo a UV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TencentModelTo3DUVNode/

Tencent

# Hunyuan3D: Modelo a UV - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo utiliza la API de Tencent Hunyuan3D para realizar el desplegado UV en un modelo 3D.

Copiar páginaCopiar página

Este nodo utiliza la API de Tencent Hunyuan3D para realizar el desplegado UV en un modelo 3D. Toma un archivo de modelo 3D como entrada, lo envía a la API para su procesamiento y devuelve el modelo procesado en formatos OBJ y FBX junto con una imagen de textura UV generada. El modelo de entrada debe tener menos de 30,000 caras.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo_3d`| Modelo 3D de entrada (GLB, OBJ o FBX). El modelo debe tener menos de 30000 caras.| FILE3D| Sí| GLB  
OBJ  
FBX  
`semilla`| Un valor de semilla (predeterminado: 1). Esto controla si el nodo debe volver a ejecutarse, pero los resultados no son deterministas independientemente del valor de la semilla.| INT| No| 0 a 2147483647  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`OBJ`| El archivo de modelo 3D procesado en formato OBJ.| FILE3D  
`FBX`| El archivo de modelo 3D procesado en formato FBX.| FILE3D  
`imagen UV`| La imagen de textura UV generada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/es.md)

* * *

**Source fingerprint (SHA-256):** `16bf094cfc3146e9d302d73862d2080b94c5aa2d575221d3c8316a3cf69fc5e1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TencentModelTo3DUVNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TencentModelTo3DUVNode)

[Hunyuan3D: Imagen(es) a modelo (Pro)](https://docs.comfy.org/es/built-in-nodes/TencentImageToModelNode)[Hunyuan3D: Topología inteligente](https://docs.comfy.org/es/built-in-nodes/TencentSmartTopologyNode)
