---
url: https://docs.comfy.org/es/tutorials/utility/moge/
title: MoGe en ComfyUI: profundidad, mapas de puntos y flujos de trabajo con mallas 3D - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:57.897744+00:00
---

# MoGe en ComfyUI: profundidad, mapas de puntos y flujos de trabajo con mallas 3D - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/moge/

## En esta página

Volver arriba

  * Introducción a MoGe en ComfyUI
  * Instalar los modelos
  * Flujos de trabajo de ejemplo
    * MoGe: Estimación de profundidad
    * 1.1 Pasos para ejecutar
    * MoGe: estimación de geometría en perspectiva
    * 2.1 Pasos para ejecutar
    * Moge: Panorama a malla
    * 3.1 Pasos para ejecutar
    * MoGe 3: estimación de geometría
    * 4.1 Pasos para ejecutar
  * Recursos de la comunidad



Depth & 3D

# MoGe en ComfyUI: profundidad, mapas de puntos y flujos de trabajo con mallas 3D

Copiar páginaCopiar página

Usa MoGe en ComfyUI para estimación de geometría monocular: profundidad métrica, mapas de puntos, mapas de normales y mallas desde una sola imagen.

Copiar páginaCopiar página

# 

​

Introducción a MoGe en ComfyUI

[MoGe](https://github.com/microsoft/MoGe) (CVPR 2025, de Microsoft Research) es un modelo potente para recuperar geometría 3D a partir de imágenes monoculares de dominio abierto. Estima mapas de puntos métricos, mapas de profundidad métricos, mapas de normales y el campo de visión de la cámara: todo en una sola pasada hacia adelante. Capacidades principales:

  * **Estimación de geometría 3D precisa** : mapas de puntos, mapas de profundidad y mapas de normales a partir de una sola imagen: un modelo, una pasada hacia adelante
  * **Escala métrica** (MoGe-2, MoGe-3): mapas de puntos y mapas de profundidad a escala real
  * **Soporte flexible de resoluciones** : funciona con varias resoluciones y relaciones de aspecto (2:1 a 1:2)
  * **Inferencia rápida** : ~60ms por imagen en A100 / RTX 3090 (FP16, ViT-L)
  * **Generación de mallas** tanto a partir de imágenes en perspectiva como panorámicas

ComfyUI incluye checkpoints para tres versiones de MoGe:

Archivo| Versión| Escala métrica| Mapas de normales| Parámetros  
---|---|---|---|---  
`moge_1_vitl_fp16`| **MoGe-1**|  -| -| 314M  
`moge_2_vitl_normal_fp16`| **MoGe-2**|  ✅| ✅| 331M  
`moge_3_vitl_fp16`| **MoGe-3**|  ✅| ✅| 370M  
`moge_3_vitg_fp16`| **MoGe-3**|  ✅| ✅| 1.25B  
  
> MoGe-2 añade escala métrica y estimación de mapas de normales de alta calidad, con un detalle visual más nítido y una latencia de inferencia menor. **MoGe-2 con normales (`moge_2_vitl_normal_fp16`) es el checkpoint RECOMENDADO.** MoGe-3 mantiene la arquitectura de MoGe-2 y añade una etapa de refinamiento volumétrico disperso autoguiada que mejora significativamente la geometría detallada de los mapas de puntos. Se distribuye como checkpoint ViT-L (`moge_3_vitl_fp16`) y como checkpoint ViT-g más grande (`moge_3_vitg_fp16`).

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

ComfyUI ahora tiene soporte nativo para los nodos de MoGe. Asegúrate de haber actualizado a la última versión de [ComfyUI](https://github.com/Comfy-Org/ComfyUI) antes de comenzar.Los modelos generados en formato `.glb` se enviarán a la carpeta `ComfyUI/output/mesh`.

## 

​

Instalar los modelos

Descarga los checkpoints de MoGe y guárdalos en la carpeta correspondiente de ComfyUI:

  * **MoGe-2 (recomendado)** : [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors)
  * **MoGe-1 (modelo base)** : [moge_1_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_1_vitl_fp16.safetensors)
  * **MoGe-3 (máximo detalle)** : [moge_3_vitg_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_3_vitg_fp16.safetensors) (1.25B) o [moge_3_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/blob/main/geometry_estimation/moge_3_vitl_fp16.safetensors) (370M)


    
    
    ComfyUI/
    ├── models/
    │   ├── geometry_estimation/
    │   │   ├── moge_2_vitl_normal_fp16.safetensors
    │   │   ├── moge_1_vitl_fp16.safetensors
    │   │   ├── moge_3_vitg_fp16.safetensors
    │   │   └── moge_3_vitl_fp16.safetensors
    

Solo para los checkpoints de MoGe-3: los nodos `Run MoGe Inference` y `Run MoGe Panorama Inference` exponen un control avanzado `refine_steps` (0 a 8, predeterminado 3) que ejecuta pasadas de refinamiento volumétrico disperso sobre la profundidad predicha. `0` desactiva el refinamiento, y más pasadas aumentan la nitidez del detalle fino y de los bordes con un costo aproximadamente lineal. Los checkpoints de MoGe-1 y MoGe-2 ignoran esta configuración.

## 

​

Flujos de trabajo de ejemplo

### 

​

MoGe: Estimación de profundidad

Sube una sola imagen RGB y genera una vista previa de profundidad en color y un mapa de profundidad sin procesar. ![Vista previa del flujo de trabajo de estimación de profundidad de MoGe](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge_depth_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “MoGe: Depth Estimation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## alien_world.png

nodo `LoadImage` 9 · `alien_world.png`

### 

​

1.1 Pasos para ejecutar

  1. Asegúrate de que el nodo `LoadMoGeModel` tenga cargado un checkpoint de MoGe
  2. Carga una imagen en el nodo `Load Image`
  3. Haz clic en `Queue` o usa `Ctrl(cmd) + Enter` para ejecutar
  4. El flujo de trabajo genera una vista previa de profundidad en color, una vista previa de profundidad sin procesar y una máscara



### 

​

MoGe: estimación de geometría en perspectiva

Sube una imagen para estimar su geometría en perspectiva. Genera un mapa de profundidad 3D y normales de superficie a partir de la entrada, y luego convierte el resultado en una malla GLB con textura. ![MoGe perspective to mesh workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_perspective_to_mesh-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “MoGe: Perspective Geometry Estimation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## modern_living_room.png

`LoadImage` nodo 9 · `modern_living_room.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/modern_living_room.png)

Esto es **estimación de geometría monocular** : las áreas ocluidas y las caras posteriores de los objetos faltarán o quedarán fragmentadas. Resulta útil para prototipar escenas rápidamente, como geometría de referencia o para visualizar profundidad y normales como una malla, pero no reemplaza una reconstrucción 3D multi-vista.

### 

​

2.1 Pasos para ejecutar

  1. Asegúrate de que el nodo `LoadMoGeModel` haya cargado un checkpoint de MoGe
  2. Carga una foto en perspectiva en el nodo `Load Image`
  3. (Opcional) Visualiza las vistas previas de normales de OpenGL y DirectX
  4. Haz clic en `Queue` o usa `Ctrl(cmd) + Enter` para ejecutar



### 

​

Moge: Panorama a malla

Sube una imagen panorámica equirectangular de 360° y genera una malla GLB con textura y colores por vértice. ![Vista previa del flujo de trabajo MoGe panorama a malla](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_panorama_to_mesh-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Moge: Panorama to Mesh” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## lego_street_panorama.png

Nodo `LoadImage` 28 · `lego_street_panorama.png`

![Panorama de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/lego_street_panorama.png)

El flujo de trabajo usa `MoGePanoramaInference` para dividir el panorama en 12 vistas en perspectiva, ejecutar la estimación de geometría monocular en cada vista de forma independiente y luego unirlas en una sola malla.

### 

​

3.1 Pasos para ejecutar

  1. Asegúrate de que el nodo `LoadMoGeModel` haya cargado uno de los checkpoints de MoGe
  2. Carga una imagen panorámica equirectangular en el nodo `Load Image`
  3. Haz clic en `Queue` o usa `Ctrl(cmd) + Enter` para ejecutar



### 

​

MoGe 3: estimación de geometría

Estima geometría de detalle fino a partir de una sola imagen con MoGe 3. Los checkpoints de MoGe-3 elevan el mapa de puntos aproximado a una envoltura de vóxeles dispersos y refinan la profundidad con convoluciones 3D dispersas y ligeras, lo que conserva las estructuras finas y las discontinuidades de profundidad que los decodificadores en el espacio de imagen difuminan. ![Vista previa del flujo de trabajo de estimación de geometría de MoGe 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge3_geometry_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Geometry Estimation: MoGe 3” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## cosmic_suitcase.png

nodo `LoadImage` 3 · `cosmic_suitcase.png`

### 

​

4.1 Pasos para ejecutar

  1. Asegúrate de que el subgrafo `Geometry Estimation (MoGe 3)` tenga un checkpoint de MoGe 3 seleccionado: la plantilla incluye `moge_3_vitg_fp16.safetensors`, y `moge_3_vitl_fp16.safetensors` está disponible en el mismo menú desplegable
  2. Carga una imagen en el nodo `Load Image`
  3. (Opcional) Cambia `output` en el nodo del subgrafo para renderizar un mapa distinto: `mask` es el valor predeterminado, y `depth`, `depth_colored`, `normal_opengl` y `normal_directx` son las otras opciones
  4. Haz clic en `Queue` o usa `Ctrl(cmd) + Enter` para ejecutar



* * *

## 

​

Recursos de la comunidad

  * [MoGe en GitHub (microsoft/MoGe)](https://github.com/microsoft/MoGe): artículo de investigación y código
  * [Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe): pesos oficiales del modelo para ComfyUI



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/moge.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/moge)

[Depth Anything 3](https://docs.comfy.org/es/tutorials/utility/depth-anything-3)[Interpolación de fotogramas](https://docs.comfy.org/es/tutorials/utility/frame-interpolation)
