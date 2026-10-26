---
url: https://docs.comfy.org/es/tutorials/utility/depth-anything-3/
title: Ejemplos de Depth Anything 3 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:57.684592+00:00
---

# Ejemplos de Depth Anything 3 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/depth-anything-3/

## En esta página

Volver arriba

  * Introducción a ComfyUI Depth Anything 3
  * Instalación del modelo
  * Flujos de trabajo de ejemplo
    * Depth Anything 3: estimación de profundidad de imagen
    * Pasos para ejecutar
    * Depth Anything 3: estimación de profundidad de video
    * Pasos para ejecutar
  * Variantes del modelo
  * Recursos de la comunidad



Depth & 3D

# Ejemplos de Depth Anything 3 en ComfyUI

Copiar páginaCopiar página

Ejecuta Depth Anything 3 en ComfyUI para estimar profundidad monocular y multivista, recuperar la pose de cámara y reconstruir 3D desde imágenes y video.

Copiar páginaCopiar página

# 

​

Introducción a ComfyUI Depth Anything 3

[Depth Anything 3 (DA3)](https://github.com/ByteDance-Seed/Depth-Anything-3), de ByteDance Seed, es un vision transformer que recupera geometría espacialmente consistente a partir de entradas visuales arbitrarias, con o sin poses de cámara conocidas. Un único encoder DINO simple y una representación unificada de rayos de profundidad permiten que una sola familia de modelos cubra profundidad monocular, profundidad multivista, estimación de pose de cámara y reconstrucción 3D. Capacidades clave:

  * **Profundidad monocular y multivista unificada** : estima la profundidad a partir de una sola imagen o de varias vistas
  * **Estimación de pose de cámara** : recupera las posiciones de cámara a partir de conjuntos de imágenes sin orden
  * **Reconstrucción 3D** a partir de entradas multivista
  * **Estimación de profundidad en video** : secuencias de profundidad por fotograma para entradas de video
  * **Múltiples variantes de modelo** : Small, Base, Mono/Metric Large



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

ComfyUI ya es compatible de forma nativa con los nodos de Depth Anything 3. Asegúrate de haber actualizado a la última versión de [ComfyUI](https://github.com/Comfy-Org/ComfyUI) antes de empezar.

## 

​

Instalación del modelo

Descarga los checkpoints de Depth Anything 3 y guárdalos en la carpeta correspondiente de ComfyUI:

  * **Small** ([depth_anything_3_small.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_small.safetensors)): Ligero, inferencia rápida
  * **Base** ([depth_anything_3_base.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_base.safetensors)): Rendimiento equilibrado
  * **Mono-Large** ([depth_anything_3_mono_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_mono_large.safetensors)): La mejor opción para profundidad monocular, incluye detección de cielo
  * **Metric-Large** ([depth_anything_3_metric_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/blob/main/geometry_estimation/depth_anything_3_metric_large.safetensors)): Profundidad a escala métrica en metros, incluye detección de cielo


    
    
    ComfyUI/
    ├── models/
    │   ├── geometry_estimation/
    │   │   ├── depth_anything_3_small.safetensors
    │   │   ├── depth_anything_3_base.safetensors
    │   │   ├── depth_anything_3_mono_large.safetensors
    │   │   └── depth_anything_3_metric_large.safetensors
    

## 

​

Flujos de trabajo de ejemplo

### 

​

Depth Anything 3: estimación de profundidad de imagen

Sube una imagen y genera un mapa de profundidad con Depth Anything 3. Consulta una comparación lado a lado de la imagen original y la salida de profundidad. ![Vista previa del flujo de trabajo de estimación de profundidad de imagen con Depth Anything 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_image_depth_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “Depth Anything 3: Image Depth Estimation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## retro_futuristic_home.png

nodo `LoadImage` 85 · `retro_futuristic_home.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/retro_futuristic_home.png)

### 

​

Pasos para ejecutar

  1. **LoadImage** : carga tu imagen de entrada
  2. **LoadDA3Model** : selecciona una variante de Depth Anything 3
  3. **Run** : haz clic en Queue o usa `Cmd+Enter`
  4. El flujo de trabajo genera un mapa de profundidad y una comparación lado a lado



## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

### 

​

Depth Anything 3: estimación de profundidad de video

Sube un video para generar una secuencia de profundidad por fotograma. Dentro del subgrafo, **GetVideoComponents** divide el video de entrada en fotogramas, **LoadDA3Model** carga el modelo y **SetVideoComponents** vuelve a ensamblar los fotogramas de profundidad en un video de salida. ![Vista previa del flujo de trabajo de estimación de profundidad de video con Depth Anything 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_video_depth_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “Depth Anything 3: Video Depth Estimation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo` correspondiente:

## empty_room_assembly.mp4

nodo `LoadVideo` 87 · `empty_room_assembly.mp4`

### 

​

Pasos para ejecutar

  1. **LoadVideo** : carga tu video de entrada
  2. **Seleccionar modelo** : elige entre **Small** , **Base** , **Mono-Large** o **Metric-Large**
  3. **Run** : haz clic en Queue o usa `Cmd+Enter`
  4. El flujo de trabajo genera un video con mapas de profundidad por fotograma



## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

## 

​

Variantes del modelo

Variante| head_type| has_sky| has_confidence| camera_decoder| Ideal para  
---|---|---|---|---|---  
**Small**|  dualdpt| ❌| ✅| ✅| Inferencia rápida, móvil/edge  
**Base**|  dualdpt| ❌| ✅| ✅| Rendimiento equilibrado  
**Mono-Large**|  dpt| ✅| ❌| ❌| Profundidad monocular con detección de cielo  
**Metric-Large**|  dpt| ✅| ❌| ❌| Profundidad métrica física en metros  
  
  * **Small** y **Base** usan el tipo de head `dualdpt` con estimación de confianza y soporte del decodificador de cámara para aplicaciones multivista.
  * **Mono-Large** y **Metric-Large** usan el tipo de head `dpt` con detección de cielo. Metric-Large genera profundidad sin procesar en metros.



## 

​

Recursos de la comunidad

  * [Depth Anything 3 GitHub (ByteDance-Seed)](https://github.com/ByteDance-Seed/Depth-Anything-3): artículo de investigación y código
  * [Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3): pesos oficiales del modelo para ComfyUI



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/depth-anything-3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/depth-anything-3)

[Marigold V2](https://docs.comfy.org/es/tutorials/utility/marigold-v2)[MoGe](https://docs.comfy.org/es/tutorials/utility/moge)
