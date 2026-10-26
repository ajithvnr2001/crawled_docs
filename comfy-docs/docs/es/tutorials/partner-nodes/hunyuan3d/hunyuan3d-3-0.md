---
url: https://docs.comfy.org/es/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0/
title: Hunyuan 3D 3.0 en ComfyUI: de texto, imagen y varias vistas a 3D - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:50.767290+00:00
---

# Hunyuan 3D 3.0 en ComfyUI: de texto, imagen y varias vistas a 3D - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0/

## En esta página

Volver arriba

  * En qué destaca Hunyuan 3D 3.0
  * Primeros pasos
    * 1\. Acceder a las plantillas de flujo de trabajo
    * 2\. Ejecutar el flujo de trabajo
    * HunYuan3D: Text to Model
    * HY 3D: Image to Model
  * Funciones avanzadas
    * HY 3D: 3D Parts Decomposition
    * HY 3D: UV Unwrapping
    * HY 3D: Smart Topology



Hunyuan 3D

# Hunyuan 3D 3.0 en ComfyUI: de texto, imagen y varias vistas a 3D

Copiar páginaCopiar página

Genera modelos 3D en ComfyUI con el nodo asociado Hunyuan 3D 3.0 desde texto, imágenes o varias vistas, además de descomposición en partes y UV unwrapping.

Copiar páginaCopiar página

Hunyuan 3D 3.0 es el modelo de generación 3D de última generación de Tencent que permite crear contenido 3D en cuestión de minutos. Puede generar recursos 3D listos para producción a partir de prompts de texto, imágenes o bocetos, con una barrera de entrada mucho menor que la de los flujos de trabajo tradicionales de modelado 3D. ComfyUI ahora integra de forma nativa la API correspondiente de Hunyuan 3D, lo que te permite usar cómodamente los nodos relacionados en ComfyUI para generar modelos. Actualmente, los Nodos asociados de ComfyUI admiten las siguientes capacidades de generación de modelos 3D de Hunyuan:

  * Generación de texto a 3D
  * Generación de imagen a 3D
  * Generación de múltiples vistas a 3D



## 

​

En qué destaca Hunyuan 3D 3.0

  * **Conceptualización para desarrollo de videojuegos** : Generación rápida de personajes, objetos y entornos con topología optimizada para rigging y renderizado en tiempo real
  * **Producto y comercio electrónico** : Convierte fotos de productos en modelos 3D interactivos para mostrarlos en línea
  * **Diseño industrial** : Creación de prototipos 3D a partir de bocetos y descomposición de piezas lista para imprimir en 3D
  * **VFX y animación** : Recursos de alta resolución con UV profesionales y materiales PBR



Para usar los Nodos asociados, debes asegurarte de haber iniciado sesión correctamente y de estar utilizando un entorno de red permitido. Consulta la sección [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de la documentación para conocer los requisitos específicos de uso de los Nodos asociados.

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

## 

​

Primeros pasos

### 

​

1\. Acceder a las plantillas de flujo de trabajo

  1. Abre la Biblioteca de plantillas en la barra lateral
  2. Ve a **3D** → **Hunyuan 3D**
  3. Selecciona una plantilla de flujo de trabajo para Hunyuan 3D



### 

​

2\. Ejecutar el flujo de trabajo

  1. Ingresa tu prompt de texto, imágenes o bocetos según el tipo de flujo de trabajo
  2. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del modelo
  3. Cuando el flujo de trabajo termine, previsualiza y exporta tu modelo 3D



### 

​

HunYuan3D: Text to Model

Ingresa un prompt de texto o sube una imagen de referencia para generar un modelo 3D detallado. **Prompt de ejemplo** : “Mechanical dolphin with gears, steampunk” ![Vista previa del flujo de trabajo HunYuan3D: Text to Model](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_text_to_model-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HunYuan3D: Text to Model” en la Biblioteca de plantillas

### 

​

HY 3D: Image to Model

Sube una imagen para generar un modelo 3D con geometría y texturas PBR. Sube 2–4 imágenes multivista desde distintos ángulos para mejorar la geometría y la fidelidad de los materiales. ![Vista previa del flujo de trabajo HY 3D: Image to Model](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_image_to_model-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY 3D: Image to Model” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## pink_robot_front.png

Nodo `LoadImage` 1 · `pink_robot_front.png`

## pink_robot_back.png

Nodo `LoadImage` 10 · `pink_robot_back.png`

![pink_robot_front.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_robot_front.png)![pink_robot_back.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_robot_back.png)

## 

​

Funciones avanzadas

Tras la [integración inicial de HY 3D 3.0](https://blog.comfy.org/p/hunyuan-3d-30-in-comfyui-state-of), las funciones de procesamiento avanzado de Hunyuan 3D ya están disponibles mediante Nodos asociados. Estos flujos de trabajo ayudan a cerrar la brecha entre la generación y la producción al incorporar pasos clave de posprocesamiento en ComfyUI.

### 

​

HY 3D: 3D Parts Decomposition

Sube un modelo 3D para segmentarlo automáticamente en las partes que lo componen y generar un recurso 3D totalmente descompuesto para reutilizarlo y editarlo. ![Vista previa del flujo de trabajo HY 3D: 3D Parts Decomposition](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_part-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY 3D: 3D Parts Decomposition” en la Biblioteca de plantillas

### 

​

HY 3D: UV Unwrapping

Sube un modelo 3D para realizar el desplegado UV. Genera un modelo procesado con una distribución UV optimizada para el texturizado. ![Vista previa del flujo de trabajo HY 3D: UV Unwrapping](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_model2uv-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY 3D: UV Unwrapping” en la Biblioteca de plantillas

### 

​

HY 3D: Smart Topology

Sube un archivo de modelo 3D de alta densidad de polígonos. Genera un modelo 3D con menos polígonos y topología optimizada, con el nivel de reducción que especifiques. ![Vista previa del flujo de trabajo HY 3D: Smart Topology](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_smart_topology-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY 3D: Smart Topology” en la Biblioteca de plantillas

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0)

[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/3d/overview)[Topología inteligente T2.5](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-t2-5)
