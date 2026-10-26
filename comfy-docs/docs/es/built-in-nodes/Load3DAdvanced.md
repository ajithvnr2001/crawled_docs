---
url: https://docs.comfy.org/es/built-in-nodes/Load3DAdvanced/
title: Cargar 3D (Avanzado) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.761299+00:00
---

# Cargar 3D (Avanzado) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Load3DAdvanced/

3D

# Cargar 3D (Avanzado) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Load 3D (Advanced) carga un archivo de modelo 3D desde el directorio input/3d de ComfyUI y proporciona los datos del modelo junto con la información

Copiar páginaCopiar página

El nodo Load 3D (Advanced) carga un archivo de modelo 3D desde el directorio `input/3d` de ComfyUI y proporciona los datos del modelo junto con la información de colocación del modelo y de cámara capturada en el estado del viewport del visor 3D. Admite formatos de archivo 3D comunes y permite establecer el ancho y alto de renderizado del viewport en píxeles. Este nodo es experimental.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model_file`| El archivo de modelo 3D que se va a cargar. Selecciona “none” para omitir la carga de un archivo de modelo. Los archivos también se pueden subir mediante el widget.| COMBO| Sí| `"none"`  
Archivos de modelo 3D disponibles en el directorio `input/3d`  
`viewport_state`| El estado actual del viewport que contiene la información de cámara y del modelo desde el visor 3D.| LOAD3D| Sí| -  
`width`| Ancho de renderizado del viewport en píxeles (predeterminado: 1024).| INT| Sí| Mín.: 1  
Máx.: 4096  
Predeterminado: 1024  
Paso: 1  
`height`| Alto de renderizado del viewport en píxeles (predeterminado: 1024).| INT| Sí| Mín.: 1  
Máx.: 4096  
Predeterminado: 1024  
Paso: 1  
  
**Notas sobre los parámetros:**

  * El parámetro `model_file` solo lista archivos con las siguientes extensiones: .gltf, .glb, .obj, .fbx, .stl
  * Los archivos deben colocarse en el directorio `input/3d` de tu instalación de ComfyUI; también se buscan subcarpetas y las rutas de archivo se muestran relativas al directorio de entrada
  * Si `model_file` es “none”, no se cargan datos de modelo y la salida `model_3d` estará vacía
  * Si `model_file` se establece en un archivo que no existe, el nodo devuelve un error de validación: “Invalid 3D model file: {model_file}”
  * Si `viewport_state` no es un objeto de estado de viewport válido, se trata como vacío, por lo que `model_3d_info` se convierte en una lista vacía y `camera_info` se devuelve vacío



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_3d`| Archivo de modelo 3D cargado (glb/obj/stl/etc.). Vacío si no se seleccionó ningún archivo de modelo.| FILE3DANY  
`model_3d_info`| Colocación de cada modelo en la escena: posición, rotación y escala (espacio de mundo con Y hacia arriba).| LOAD3DMODELINFO  
`camera_info`| Información de la cámara del viewport: posición, objetivo de mirada, zoom y tipo.| LOAD3DCAMERA  
`width`| Ancho de renderizado del viewport en píxeles.| INT  
`height`| Alto de renderizado del viewport en píxeles.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/es.md)

* * *

**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Load3DAdvanced.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Load3DAdvanced)

[Cargar 3D y animación](https://docs.comfy.org/es/built-in-nodes/Load3D)[Crear archivo 3D (desde malla)](https://docs.comfy.org/es/built-in-nodes/MeshToFile3D)
