---
url: https://docs.comfy.org/es/tutorials/utility/sam3d-body/
title: SAM 3D Body: extraer una malla 3D humana desde un video en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.434164+00:00
---

# SAM 3D Body: extraer una malla 3D humana desde un video en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/sam3d-body/

## En esta página

Volver arriba

  * SAM 3D Body: extracción de malla humana 3D desde video
  * Cómo funciona
  * Pasos para ejecutar
  * Descargas de modelos
    * Ubicación de almacenamiento de los modelos



Pose & Detection

# SAM 3D Body: extraer una malla 3D humana desde un video en ComfyUI

Copiar páginaCopiar página

Extrae una malla 3D del cuerpo humano desde un video con SAM 3D Body: pose y forma, expresiones faciales y video con la malla superpuesta.

Copiar páginaCopiar página

**SAM 3D Body** es un modelo de código abierto que recupera una malla humana 3D de cuerpo completo a partir de un solo video. Combina seguimiento de video, detección de personas y predicción de malla para reconstruir el cuerpo humano con pose, forma y expresiones faciales, y luego renderiza el rig recuperado de vuelta sobre el video. El flujo de trabajo es útil para prototipos de captura de movimiento, análisis biomecánico y previsualización de animación de personajes.

### 

​

SAM 3D Body: extracción de malla humana 3D desde video

Carga un video de una persona. Extrae una malla humana 3D de cuerpo completo con pose, forma y expresiones faciales, renderizada como un video con superposición. ![Vista previa del flujo de trabajo SAM 3D Body](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sam3d_body-1.webp)

  * Usuarios locales

  * Usuarios de Cloud




Asegúrate de que tu ComfyUI esté actualizado.

  * [Descargar ComfyUI](https://www.comfy.org/download)
  * [Guía de actualización](https://docs.comfy.org/es/installation/update_comfyui)

Los flujos de trabajo de esta guía se encuentran en las [Plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template). Si no los encuentras en las plantillas, es posible que tu ComfyUI esté desactualizado.Si faltan nodos al cargar un flujo de trabajo, estas son las posibles razones:

  1. No estás usando la última versión de ComfyUI (versión nocturna)
  2. Algunos nodos fallaron al importarse durante el inicio



  * [Cloud](https://cloud.comfy.org) se actualizará después del lanzamiento estable de ComfyUI.

Por lo tanto, si notas que falta algún nodo central en este documento, puede deberse a que los nuevos nodos centrales aún no se han publicado en la última versión estable. Espera al próximo lanzamiento estable.

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo al instante en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “SAM 3D Body: 3D Human Mesh Extraction From Video” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo`:

## woman_holding_water_glass.mp4

nodo `LoadVideo` 85 · `woman_holding_water_glass.mp4`

## 

​

Cómo funciona

  1. **Seguimiento de video** : SAM3 rastrea a la persona a lo largo de los fotogramas del video. El seguimiento es prácticamente obligatorio cuando aparecen varias personas en el clip, y en general mejora la precisión de la detección
  2. **Detección de personas** : RT-DETR detecta las cajas delimitadoras de la persona, guiado por el prompt de texto (`person`)
  3. **Predicción de la malla** : SAM 3D Body predice la malla 3D de cuerpo completo a partir de los fotogramas rastreados, con un FOV de cámara MoGe opcional para una alineación más precisa con el video fuente
  4. **Expresiones faciales** : un paso basado en MediaPipe añade las expresiones faciales, que el modelo base no detecta
  5. **Suavizado** : la secuencia de mallas se suaviza a lo largo del tiempo
  6. **Renderizado** : se construye un archivo de pose (GLB), la malla se renderiza de vuelta sobre el video y luego se guarda como video de salida



## 

​

Pasos para ejecutar

  1. **Carga un video** : usa el nodo `LoadVideo` para cargar un video de una persona
  2. **Pon en cola el flujo de trabajo** : presiona Ctrl (Cmd en macOS) + Enter
  3. **Espera el pipeline** : el seguimiento, la detección, la predicción de malla y el renderizado se ejecutan en secuencia
  4. **Consulta el resultado** : revisa la malla en el nodo `Preview3D`. El video superpuesto se guarda en `ComfyUI/output/video/SAM3D_body/`



## 

​

Descargas de modelos

Descarga el modelo SAM 3D Body y los archivos necesarios. Colócalos en los subdirectorios correspondientes de `models/`.

## Checkpoint multiplex de SAM3

sam3.1_multiplex_fp16.safetensors: checkpoint multiplex de SAM3 para el seguimiento en video

## Detección de SAM 3D Body

sam_3d_body_dinov3_bf16.safetensors: modelo de detección de SAM 3D Body (con backbone DINOv3)

## Geometría MoGe

moge_2_vitl_normal_fp16.safetensors: estimación opcional del campo de visión de la cámara para la alineación

## Detector de personas RT-DETR

rt_detr_v4-x-hgnet_fp32.safetensors: modelo de detección de personas RT-DETR

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │      └── sam3.1_multiplex_fp16.safetensors
    │   ├── 📂 detection/
    │   │      └── sam_3d_body_dinov3_bf16.safetensors
    │   ├── 📂 geometry_estimation/
    │   │      └── moge_2_vitl_normal_fp16.safetensors
    │   └── 📂 diffusion_models/
    │          └── rt_detr_v4-x-hgnet_fp32.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/sam3d-body.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/sam3d-body)

[Eliminación de fondo con BiRefNet](https://docs.comfy.org/es/tutorials/utility/remove-background-birefnet)[Detección de rostros con MediaPipe](https://docs.comfy.org/es/tutorials/utility/face-detection/mediapipe)
