---
url: https://docs.comfy.org/es/built-in-nodes/MarigoldV2PostProcess/
title: Posprocesado de Marigold V2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.122213+00:00
---

# Posprocesado de Marigold V2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MarigoldV2PostProcess/

Estimación de geometría

# Posprocesado de Marigold V2 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo convierte una predicción decodificada de Marigold V2 en una imagen visualizable.

Copiar páginaCopiar página

Este nodo convierte una predicción decodificada de Marigold V2 en una imagen visualizable. Toma el tensor de predicción sin procesar y le da formato según el tipo de predicción del que se trate: profundidad normalizada (los objetos cercanos aparecen brillantes), normales de superficie de longitud unitaria o albedo sRGB.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| La predicción decodificada de Marigold V2 que se convertirá en una imagen visualizable.| IMAGE| Sí| -  
`prediction`| El tipo de predicción contenida en la entrada, que determina cómo se convierten los datos. `"depth"` normaliza los valores de profundidad para que las superficies cercanas sean brillantes y las lejanas oscuras, y luego copia el resultado en los tres canales de color. `"normals"` reescala los valores al rango -1..1, los normaliza a normales de superficie de longitud unitaria y los asigna de nuevo a 0..1. `"albedo"` aplica una conversión lineal a sRGB a los valores.| COMBO| Sí| `"depth"`  
`"normals"`  
`"albedo"`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen procesada en la representación seleccionada: profundidad normalizada (escala de grises repetida en los tres canales), normales de superficie de longitud unitaria o albedo sRGB.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/es.md)

* * *

**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MarigoldV2PostProcess.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MarigoldV2PostProcess)

[Renderizar Depth Anything 3](https://docs.comfy.org/es/built-in-nodes/DA3Render)[Obtener FoV de la geometría MoGe](https://docs.comfy.org/es/built-in-nodes/MoGeGeometryToFOV)
