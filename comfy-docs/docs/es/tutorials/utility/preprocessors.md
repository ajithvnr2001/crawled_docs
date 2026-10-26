---
url: https://docs.comfy.org/es/tutorials/utility/preprocessors/
title: Flujos de trabajo de preprocesadores en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.174611+00:00
---

# Flujos de trabajo de preprocesadores en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/preprocessors/

## En esta página

Volver arriba

  * ¿Qué son los preprocesadores?
  * Estimación de profundidad
    * Video a mapa de profundidad
  * Conversión de arte lineal
    * Conversión de video a arte lineal / Canny
  * Detección de pose
    * Video a mapa de pose - OpenPose
  * Extracción de normales
    * Convertir un video en un mapa de normales



Utility

# Flujos de trabajo de preprocesadores en ComfyUI

Copiar páginaCopiar página

Aprende a usar los preprocesadores de estimación de profundidad, conversión a arte lineal, detección de pose y extracción de normales en ComfyUI

Copiar páginaCopiar página

## 

​

¿Qué son los preprocesadores?

Estos flujos de trabajo contienen nodos personalizados. Debes instalarlos con [ComfyUI Manager](https://docs.comfy.org/es/manager/overview) antes de ejecutar los flujos de trabajo.

Los preprocesadores son herramientas fundamentales que extraen información estructural de las imágenes. Convierten las imágenes en señales de acondicionamiento como mapas de profundidad, arte lineal, esqueletos de pose y normales de superficie. Estas salidas permiten un mejor control y una mayor consistencia en flujos de trabajo con ControlNet, de imagen a imagen y de video. Usar los preprocesadores como flujos de trabajo separados permite:

  * Iterar más rápido sin volver a ejecutar el gráfico completo
  * Separar claramente el preprocesamiento de la generación
  * Depurar y ajustar con mayor facilidad
  * Obtener resultados de imagen y video más predecibles



## 

​

Estimación de profundidad

La estimación de profundidad convierte una imagen plana en un mapa de profundidad que representa la distancia relativa dentro de una escena. Esta señal estructural es fundamental para la generación controlada, las ediciones con conciencia espacial y los flujos de trabajo de relighting. Este flujo de trabajo hace hincapié en:

  * Extracción de profundidad limpia y estable
  * Normalización consistente para su uso posterior
  * Integración sencilla con ControlNet y pipelines de edición de imágenes

Las salidas de profundidad se pueden reutilizar en varias pasadas, lo que facilita la iteración sin volver a ejecutar pasos previos costosos.

### 

​

Video a mapa de profundidad

Convierte un video en un mapa de profundidad temporalmente estable. ![Vista previa del flujo de trabajo Video a mapa de profundidad](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-depthAnything-v2-relative-video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Video to Depth Map” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `VHS_LoadVideo` correspondiente:

## roller_coaster.mp4

Nodo `VHS_LoadVideo` 6 · `roller_coaster.mp4`

## 

​

Conversión de arte lineal

Los preprocesadores de arte lineal reducen una imagen a sus bordes y contornos esenciales, eliminando la textura y el color, pero conservando la estructura. Este flujo de trabajo está diseñado para:

  * Producir arte lineal limpio y de alto contraste
  * Minimizar los bordes rotos o ruidosos
  * Proporcionar una orientación estructural confiable para flujos de trabajo de estilización y redibujado

El arte lineal combina especialmente bien con la profundidad y la pose, ya que ofrece restricciones estructurales sólidas sin limitar en exceso el estilo.

### 

​

Conversión de video a arte lineal / Canny

Convierte un video en arte lineal o bordes Canny para los procesadores de control. ![Vista previa del flujo de trabajo de conversión de video a arte lineal](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-lineart-video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Video to Lineart / Canny” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `VHS_LoadVideo` correspondiente:

## utility-lineart-video-input.mp4

Nodo 2 `VHS_LoadVideo` · `utility-lineart-video-input.mp4`

## 

​

Detección de pose

La detección de pose extrae puntos clave del cuerpo y la estructura esquelética de las imágenes, lo que permite un control preciso de la postura y el movimiento humanos. Este flujo de trabajo se centra en:

  * Salidas de pose claras y legibles
  * Detección de puntos clave estable, apta para reutilizarse entre fotogramas
  * Compatibilidad con ControlNet basado en pose y con los pipelines de animación

Al aislar la extracción de pose en un flujo de trabajo dedicado, los datos de pose resultan más fáciles de inspeccionar, refinar y reutilizar.

### 

​

Video a mapa de pose - OpenPose

Convierte un video en un mapa de control de pose temporalmente estable. ![Vista previa del flujo de trabajo Video to Pose Map](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-openpose-video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Video to Pose Map - OpenPose” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `VHS_LoadVideo` correspondiente:

## pose_input.mp4

Nodo 2 de `VHS_LoadVideo` · `pose_input.mp4`

## 

​

Extracción de normales

La estimación de normales convierte una imagen plana en un mapa de normales de superficie: un campo de dirección por píxel que describe cómo está orientada cada parte de una superficie (normalmente codificado como RGB). Esta señal es útil para cambiar la iluminación, la estilización consciente de materiales y las ediciones muy estructuradas. Este flujo de trabajo hace hincapié en:

  * Extracción de normales limpia y estable con un moteado mínimo
  * Orientación y normalización consistentes para un uso posterior fiable
  * Salidas listas para ControlNet para cambios de iluminación, refinamiento y ediciones que preservan la estructura
  * Reutilización entre pasadas para iterar sin volver a ejecutar pasos anteriores

Puedes usar las salidas de normales para:

  * Impulsar cambios de iluminación y sombreado preservando la geometría
  * Añadir una estructura tipo 3D más marcada a los flujos de estilización y redibujado
  * Mejorar la consistencia entre fotogramas cuando se combina con pose/profundidad para trabajo de animación



### 

​

Convertir un video en un mapa de normales

Convierte un video en un mapa de normales estable en el tiempo. ![Vista previa del flujo de trabajo Convertir un video en un mapa de normales](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-normal_crafter-video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Video to Normal Map” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `VHS_LoadVideo` correspondiente:

## normals_input.mp4

Nodo `VHS_LoadVideo` 3 · `normals_input.mp4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/preprocessors.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/preprocessors)

[ACE-Step 1.5](https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1-5)[Ampliación de imágenes](https://docs.comfy.org/es/tutorials/utility/image-upscale)
