---
url: https://docs.comfy.org/es/tutorials/partner-nodes/rodin/model-generation/
title: Hyper3D Rodin en ComfyUI: generaci\u00f3n 3D de una y varias vistas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.022168+00:00
---

# Hyper3D Rodin en ComfyUI: generación 3D de una y varias vistas - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/rodin/model-generation/

## En esta página

Volver arriba

  * Para qué sirve Rodin Model Generation
  * Flujo de trabajo de generación de modelo con una sola vista
    * 2\. Completa la ejecución del flujo de trabajo paso a paso
  * Flujo de trabajo de generación de modelos multi-vista
    * 1\. Descargar el archivo de flujo de trabajo
    * 2\. Completar la ejecución del flujo de trabajo paso a paso
  * Otros nodos relacionados



Rodin

# Hyper3D Rodin en ComfyUI: generación 3D de una y varias vistas

Copiar páginaCopiar página

Genera modelos 3D listos para producción en ComfyUI con el nodo asociado Hyper3D Rodin a partir de una imagen o de hasta cinco vistas.

Copiar páginaCopiar página

Hyper3D Rodin (hyper3d.ai) es una plataforma enfocada en generar rápidamente modelos 3D y materiales de alta calidad, listos para producción, mediante inteligencia artificial. ComfyUI ahora ha integrado de forma nativa la API de generación de modelos de Rodin correspondiente, lo que te permite usar cómodamente los nodos relacionados en ComfyUI para generar modelos.

## 

​

Para qué sirve Rodin Model Generation

  * **Generación de modelos de una sola vista** : Genera un modelo 3D a partir de una sola imagen de entrada
  * **Generación de modelos multivista** : Genera un modelo 3D a partir de hasta 5 imágenes de entrada, como vistas frontal, trasera e izquierda
  * **Distintos niveles de detalle** : Admite la generación de modelos con detalle ajustable, incluidos distintos recuentos de polígonos para obtener modelos más suaves y detallados
  * **Exportación directa** : Los modelos generados se guardan en el directorio `ComfyUI/output/Rodin` y puedes exportarlos desde el nodo `Preview 3D`



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

Flujo de trabajo de generación de modelo con una sola vista

Genera un modelo 3D a partir de una sola imagen de entrada con Rodin. ![Vista previa del flujo de trabajo de generación de modelo con una sola vista de Rodin](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_image_to_model-1.webp)

## Descargar archivo del flujo de trabajo

Generación de modelo con una sola vista (formato Json)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/doll.jpg)

### 

​

2\. Completa la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de Rodin Image to Model en ComfyUI](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ed79f1fb8546ed41a3d157cece818ee9) Puedes guiarte por los números de la imagen para completar la ejecución del flujo de trabajo básico de texto a imagen:

  1. En el nodo `Load Image`, carga la imagen de entrada proporcionada
  2. (Opcional) En `Rodin 3D Generate - Regular Generate`, ajusta los parámetros correspondientes 
     * polygon_count: puedes establecer distintos recuentos de polígonos; cuanto mayor sea el valor, más suave y detallado será el modelo
  3. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter`, para ejecutar la generación del modelo. Cuando el flujo de trabajo termine, el modelo correspondiente se guardará automáticamente en el directorio `ComfyUI/output/Rodin`
  4. En el nodo `Preview 3D`, haz clic para expandir el menú
  5. Selecciona `Export` para exportar directamente el modelo correspondiente



## 

​

Flujo de trabajo de generación de modelos multi-vista

El nodo correspondiente, `Rodin 3D Generate - Regular Generate`, permite hasta 5 imágenes de entrada

### 

​

1\. Descargar el archivo de flujo de trabajo

Puedes modificar el flujo de trabajo de una sola vista a uno de varias vistas, o descargar directamente el archivo de flujo de trabajo que aparece a continuación ![Vista previa del flujo de trabajo de generación de modelos multi-vista de Rodin](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_multiview_to_model-1.webp)

## Descargar archivo de flujo de trabajo

Generación de modelos multi-vista (formato JSON)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/front.jpg) ![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/back.jpg) ![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/rodin/multiview_to_model/left.jpg)

### 

​

2\. Completar la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de ComfyUI Rodin de imagen a modelo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/rodin_multiview_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=6241527775e83bd480811631ef4d88ed) Puedes guiarte por los números de la imagen para completar la ejecución básica del flujo de trabajo de texto a imagen:

  1. En el nodo `Load Image`, carga las imágenes de entrada proporcionadas
  2. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del modelo. Cuando el flujo de trabajo termine, el modelo correspondiente se guardará automáticamente en el directorio `ComfyUI/output/Rodin`
  3. En el nodo `Preview 3D`, haz clic para expandir el menú
  4. Selecciona `Export` para exportar directamente el modelo correspondiente



## 

​

Otros nodos relacionados

Actualmente, Rodin ofrece distintos tipos de nodos de generación de modelos en ComfyUI. Dado que las condiciones de entrada correspondientes son las mismas que las del flujo de trabajo presentado en este artículo, puedes habilitarlos según tus necesidades. Además, hemos incluido los nodos correspondientes en las plantillas respectivas, así que también puedes modificar el modo del nodo correspondiente según tus necesidades para habilitarlo. ![Otros nodos relacionados de Rodin](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/rodin/other_nodes.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7caf60a6b994156e71476564c856fc15)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/rodin/model-generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/rodin/model-generation)

[Meshy 6](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-6)[Tripo P2](https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-p2)
