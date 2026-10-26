---
url: https://docs.comfy.org/es/built-in-nodes/Tencent3DTextureEditNode/
title: Hunyuan3D: Edici\u00f3n de textura 3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.286717+00:00
---

# Hunyuan3D: Edición de textura 3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Tencent3DTextureEditNode/

Tencent

# Hunyuan3D: Edición de textura 3D - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo utiliza la API de Tencent Hunyuan3D para editar las texturas de un modelo 3D.

Copiar páginaCopiar página

Este nodo utiliza la API de Tencent Hunyuan3D para editar las texturas de un modelo 3D. Proporcionas un modelo 3D y una descripción de texto de los cambios deseados, y el nodo devuelve una nueva versión del modelo con sus texturas redibujadas según tu indicación.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`model_3d`| Modelo 3D en formato FBX. El modelo debe tener menos de 100000 caras.| FILE3D| Sí| FBX, Cualquiera  
`prompt`| Describe la edición de textura. Admite hasta 1024 caracteres UTF-8.| STRING| Sí|   
`seed`| La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0)| INT| No| 0 a 2147483647  
  
**Nota:** La entrada `model_3d` debe ser un archivo en formato FBX. Este nodo no admite otros formatos de archivo 3D.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`GLB`| El modelo 3D procesado en formato GLB.| FILE3D  
`OBJ`| El modelo 3D procesado en formato OBJ.| FILE3D  
`texture_image`| La imagen de textura recién generada para el modelo 3D.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/es.md)

* * *

**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Tencent3DTextureEditNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Tencent3DTextureEditNode)

[Hunyuan3D: Parte 3D](https://docs.comfy.org/es/built-in-nodes/Tencent3DPartNode)[Hunyuan3D: Imagen(es) a modelo (Pro)](https://docs.comfy.org/es/built-in-nodes/TencentImageToModelNode)
