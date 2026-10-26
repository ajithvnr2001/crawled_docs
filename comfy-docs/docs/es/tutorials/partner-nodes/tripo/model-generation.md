---
url: https://docs.comfy.org/es/tutorials/partner-nodes/tripo/model-generation/
title: Generaci\u00f3n de modelos con los nodos asociados de Tripo: ejemplo oficial de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.819902+00:00
---

# Generación de modelos con los nodos asociados de Tripo: ejemplo oficial de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/tripo/model-generation/

## En esta página

Volver arriba

  * Para qué sirve Tripo Model Generation
  * Flujo de trabajo de texto a modelo
    * 2\. Completa la ejecución del flujo de trabajo paso a paso
  * Flujo de trabajo de imagen a modelo
    * 2\. Completa la ejecución del flujo de trabajo paso a paso
  * Flujo de trabajo de generación de modelos multivista
    * 2\. Completar la ejecución del flujo de trabajo paso a paso
  * Procesamiento de tareas posteriores para la misma tarea



Tripo

# Generación de modelos con los nodos asociados de Tripo: ejemplo oficial de ComfyUI

Copiar páginaCopiar página

Aprende a usar la API de los nodos de Tripo en ComfyUI para generar modelos 3D.

Copiar páginaCopiar página

Tripo AI es una empresa enfocada en el modelado 3D con IA generativa. Ofrece plataformas fáciles de usar y servicios de API que convierten rápidamente prompts de texto o imágenes 2D (una o varias) en modelos 3D de alta calidad. ComfyUI ahora integra de forma nativa la API correspondiente de Tripo, así que puedes usar cómodamente los nodos relacionados en ComfyUI para generar modelos.

## 

​

Para qué sirve Tripo Model Generation

Actualmente, los nodos asociados de ComfyUI admiten las siguientes capacidades de generación de modelos de Tripo:

  * Texto a modelo
  * Imagen a modelo
  * Generación de modelos multivista
  * Modelo con rig
  * Retarget de modelo con rig



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

Flujo de trabajo de texto a modelo

Genera un modelo 3D a partir de un prompt de texto con las capacidades de texto a modelo de Tripo. ![Vista previa del flujo de trabajo de texto a modelo de Tripo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_text_to_model-1.webp)

## Ejecutar texto a modelo en Cloud

Prueba el flujo de trabajo de texto a modelo al instante en Comfy Cloud.

## Descargar el flujo de trabajo de texto a modelo

Descarga el JSON para ejecutarlo localmente en ComfyUI.

### 

​

2\. Completa la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de texto a modelo de Tripo en ComfyUI](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_text_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b25199fbdd5c00f3fd8a1b587586bbed) Puedes guiarte por los números de la imagen para completar la ejecución del flujo de trabajo básico de texto a modelo:

  1. En el nodo `Tripo: Text to Model`, ingresa tu prompt en el campo `prompt`
     * model: Puedes seleccionar distintos modelos
     * style: Puedes establecer distintos estilos
     * texture_quality: Puedes establecer distintas calidades de textura
  2. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del modelo. Cuando el flujo de trabajo termine, el modelo correspondiente se guardará automáticamente en el directorio `ComfyUI/output/`
  3. En el nodo `Preview 3D`, haz clic para expandir el menú
  4. Selecciona `Export` para exportar directamente el modelo correspondiente



## 

​

Flujo de trabajo de imagen a modelo

Genera un modelo 3D a partir de una sola imagen de entrada. ![Vista previa del flujo de trabajo Tripo de imagen a modelo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_image_to_model-1.webp)

## Ejecutar imagen a modelo en Cloud

Prueba el flujo de trabajo de imagen a modelo al instante en Comfy Cloud.

## Descargar el flujo de trabajo de imagen a modelo

Descarga el JSON para ejecutarlo localmente en ComfyUI.

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/image_to_model/panda.jpg)

### 

​

2\. Completa la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de Tripo de texto a modelo en ComfyUI](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=302a46095bbb73ea478f441fa489b763) Puedes guiarte por los números de la imagen para completar la ejecución básica del flujo de trabajo de imagen a modelo:

  1. En el nodo `Load Image`, carga la imagen de entrada proporcionada
  2. En el nodo `Tripo: Image to Model`, modifica los ajustes de parámetros correspondientes 
     * model: Puedes seleccionar diferentes modelos
     * style: Puedes establecer diferentes estilos
     * texture_quality: Puedes establecer diferentes calidades de textura
  3. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del modelo. Cuando el flujo de trabajo termine, el modelo correspondiente se guardará automáticamente en el directorio `ComfyUI/output/`
  4. Para descargar el modelo, consulta las instrucciones de la sección de texto a modelo



## 

​

Flujo de trabajo de generación de modelos multivista

Genera un modelo 3D a partir de imágenes de múltiples vistas para obtener mayor precisión. ![Vista previa del flujo de trabajo de generación de modelos multivista de Tripo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model-1.webp)

## Ejecutar Multiview-to-Model en la nube

Prueba el flujo de trabajo Multiview-to-Model al instante en Comfy Cloud.

## Descargar el flujo de trabajo Multiview-to-Model

Descarga el JSON para ejecutarlo localmente en ComfyUI.

![Vista frontal](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/front.jpg) ![Vista trasera](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/tripo/multiview_to_image/back.jpg)

### 

​

2\. Completar la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de ComfyUI Tripo Text to Model](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/api_nodes/tripo/tripo_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5c4abf93f36e2ea96202c7cdb92d9917) Puedes consultar los números de la imagen para completar la ejecución básica del flujo de trabajo de múltiples vistas a modelo:

  1. En los nodos `Load Image`, carga las imágenes de entrada proporcionadas respectivamente
  2. En el nodo `Tripo: Image to Model`, modifica las configuraciones de parámetros correspondientes 
     * model: puedes seleccionar diferentes modelos
     * style: puedes establecer diferentes estilos
     * texture_quality: puedes establecer diferentes calidades de textura
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del modelo. Cuando el flujo de trabajo termine, el modelo correspondiente se guardará automáticamente en el directorio `ComfyUI/output/`
  4. Para las entradas de otras vistas, puedes consultar el diagrama de pasos y configurar el modo del nodo correspondiente en `Always` para habilitarlo
  5. Para descargar el modelo, consulta las instrucciones de la sección Text to Model



## 

​

Procesamiento de tareas posteriores para la misma tarea

Los nodos correspondientes de Tripo permiten el procesamiento posterior de la misma tarea. Solo tienes que introducir el `model_task_id` correspondiente en los nodos relevantes. Además, hemos incluido los nodos correspondientes en las plantillas relevantes, y también puedes modificar el modo del nodo correspondiente según sea necesario para habilitarlo. ![Procesamiento de tareas de Tripo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/tripo/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ad7966d458e1d327c98d2b21eccdd7a4)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/tripo/model-generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/tripo/model-generation)

[Tripo 3 1](https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-3-1)[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/audio/overview)
