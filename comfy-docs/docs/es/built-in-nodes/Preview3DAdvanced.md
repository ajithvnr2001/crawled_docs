---
url: https://docs.comfy.org/es/built-in-nodes/Preview3DAdvanced/
title: Vista previa 3D (Avanzado) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.858905+00:00
---

# Vista previa 3D (Avanzado) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Preview3DAdvanced/

3D

# Vista previa 3D (Avanzado) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo muestra una vista previa del modelo 3D en la interfaz de usuario sin guardar el archivo en el directorio de salida de ComfyUI.

Copiar páginaCopiar página

Este nodo muestra una vista previa del modelo 3D en la interfaz de usuario sin guardar el archivo en el directorio de salida de ComfyUI. Guarda el modelo en un archivo temporal y transmite los datos del modelo, la información del modelo, la información de la cámara y las dimensiones de la vista previa para su posterior procesamiento en el flujo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model_3d`| Archivo de modelo 3D procedente de un nodo 3D anterior.| FILE3D| Sí| GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D compatible  
`info_modelo_3d`| Ubicación de cada modelo en la escena: posición, rotación y escala (espacio mundial con eje Y hacia arriba). Opcional. Opción avanzada.| LOAD3DMODELINFO| No| -  
`viewport_state`| Estado actual del viewport que contiene la información de la cámara y del modelo.| LOAD3D| Sí| -  
`info_cámara`| Información de la cámara del viewport: posición, punto de mira, zoom y tipo. Opcional. Opción avanzada.| LOAD3DCAMERA| No| -  
`ancho`| Ancho de renderizado del viewport en píxeles. Valor predeterminado: 1024.| INT| Sí| 1 a 4096  
`alto`| Altura de renderizado del viewport en píxeles. Valor predeterminado: 1024.| INT| Sí| 1 a 4096  
  
Nota: cuando `camera_info` o `model_3d_info` no están conectados, sus valores se toman de `viewport_state` cuando estén disponibles. Si `viewport_state` no contiene información de cámara, `camera_info` es None. Si `viewport_state` no tiene información de modelo, `model_3d_info` se define como una lista vacía por defecto. Si `viewport_state` no es un diccionario, se trata como vacío.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`archivo_modelo`| Archivo de modelo 3D (glb/obj/stl/etc.) procedente de un nodo 3D anterior, transmitido sin cambios.| FILE3D  
`info_cámara`| Ubicación de cada modelo en la escena: posición, rotación y escala (espacio mundial con eje Y hacia arriba). Utiliza el valor de entrada o recurre al valor almacenado en `viewport_state`.| LOAD3DMODELINFO  
`info_modelo_3d`| Información de la cámara del viewport: posición, punto de mira, zoom y tipo. Utiliza el valor de entrada o recurre al valor almacenado en `viewport_state`.| LOAD3DCAMERA  
`ancho`| Ancho de renderizado del viewport en píxeles.| INT  
`alto`| Altura de renderizado del viewport en píxeles.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/es.md)

* * *

**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Preview3DAdvanced.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Preview3DAdvanced)

[Vista previa 3D y animación (OBSOLETO)](https://docs.comfy.org/es/built-in-nodes/Preview3D)[Vista previa de Splat](https://docs.comfy.org/es/built-in-nodes/PreviewGaussianSplat)
