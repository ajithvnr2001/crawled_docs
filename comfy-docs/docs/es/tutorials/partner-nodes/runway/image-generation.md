---
url: https://docs.comfy.org/es/tutorials/partner-nodes/runway/image-generation/
title: Generaci\u00f3n de im\u00e1genes con Runway en ComfyUI: texto a imagen e im\u00e1genes de referencia - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:54.951109+00:00
---

# Generación de imágenes con Runway en ComfyUI: texto a imagen e imágenes de referencia - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/runway/image-generation/

## En esta página

Volver arriba

  * En qué destaca Runway Image Generation
  * Flujo de trabajo Runway texto a imagen
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar la ejecución del flujo de trabajo paso a paso
  * Flujo de trabajo de referencia a imagen de Runway
    * 1\. Descarga del flujo de trabajo y de la imagen de entrada
    * 2\. Completa la ejecución del flujo de trabajo paso a paso



Runway

# Generación de imágenes con Runway en ComfyUI: texto a imagen e imágenes de referencia

Copiar páginaCopiar página

Ejecuta los nodos asociados de imágenes de Runway en ComfyUI para generar imágenes desde un prompt o una imagen de referencia, con relaciones de aspecto ajustables.

Copiar páginaCopiar página

Runway es una empresa enfocada en la IA generativa que ofrece potentes capacidades de generación de imágenes. Sus modelos admiten funciones como la transferencia de estilo, la extensión de imágenes y el control del detalle. Actualmente, ComfyUI ha integrado la API de Runway, lo que te permite usar directamente los nodos relacionados en ComfyUI para generar imágenes.

## 

​

En qué destaca Runway Image Generation

  * **Generación de texto a imagen** : genera imágenes a partir de un prompt de texto con el nodo `Runway Text to Image`, con relaciones de aspecto de salida ajustables
  * **Generación de referencia a imagen** : genera imágenes guiadas por una imagen de referencia de entrada más un prompt de texto
  * **Transferencia de estilo, extensión de imagen y control de detalles** : los modelos de Runway admiten estas funciones para la generación de imágenes



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

Flujo de trabajo Runway texto a imagen

### 

​

1\. Descargar el archivo del flujo de trabajo

La imagen a continuación contiene la información del flujo de trabajo en sus `metadata`. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![ComfyUI Runway texto a imagen](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/text_to_image.png)

### 

​

2\. Completar la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de ComfyUI Runway texto a imagen](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_text_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66f4bf5de975a5f0302d930e352605ff) Puedes guiarte por los números de la imagen para completar la ejecución del flujo de trabajo básico de texto a imagen:

  1. En el nodo `Runway Text to Image`, ingresa tu prompt en el campo `prompt`
  2. (Opcional) Ajusta el parámetro `ratio` para definir diferentes relaciones de aspecto de salida
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de imágenes.
  4. Después de esperar a que la API devuelva los resultados, puedes ver la imagen generada en el nodo `Save Image` (haz clic derecho para guardarla). La imagen correspondiente también se guardará en el directorio `ComfyUI/output/`.



## 

​

Flujo de trabajo de referencia a imagen de Runway

### 

​

1\. Descarga del flujo de trabajo y de la imagen de entrada

La imagen a continuación contiene la información del flujo de trabajo en sus `metadata`. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![Imagen de referencia a imagen de ComfyUI Runway](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/runway_reference_to_image.png) Descarga la imagen a continuación para usarla como entrada. ![Imagen de entrada de referencia a imagen de ComfyUI Runway](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/image/reference_to_image/input.png)

### 

​

2\. Completa la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de referencia a imagen de ComfyUI Runway](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_reference_to_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f0ce702cc2a6a03d887072416d78c241) Puedes consultar los números de la imagen para completar la ejecución básica del flujo de trabajo de referencia a imagen:

  1. En el nodo `Load Image`, carga la imagen de entrada proporcionada.
  2. En el nodo `Runway Text to Image`, introduce tu prompt en el campo `prompt` y ajusta las dimensiones.
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de imagen.
  4. Después de esperar a que la API devuelva los resultados, puedes ver la imagen generada en el nodo `Save Image` (haz clic derecho para guardarla). La imagen correspondiente también se guardará en el directorio `ComfyUI/output/`.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/runway/image-generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/runway/image-generation)

[Reve Image](https://docs.comfy.org/es/tutorials/partner-nodes/reve/reve-image)[HY Image 3.5](https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-image-3-5)
