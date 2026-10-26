---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2/
title: OpenAI GPT-Image-2 en ComfyUI: generaci\u00f3n de im\u00e1genes con razonamiento - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.888897+00:00
---

# OpenAI GPT-Image-2 en ComfyUI: generación de imágenes con razonamiento - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2/

## En esta página

Volver arriba

  * Para qué es bueno GPT-Image-2
    * Generación guiada por razonamiento
    * Edición de imágenes que conserva lo importante
    * Hasta ocho imágenes coherentes por prompt
  * Flujos de trabajo híbridos
  * Salidas de ejemplo
  * Primeros pasos
  * Flujos de trabajo disponibles
    * Texto a imagen (T2I)
    * Edición de imagen



OpenAI

# OpenAI GPT-Image-2 en ComfyUI: generación de imágenes con razonamiento

Copiar páginaCopiar página

Usa OpenAI GPT-Image-2 en ComfyUI para generar imágenes con razonamiento: texto denso, renderizado de UI, edición en 2K y hasta ocho imágenes consistentes.

Copiar páginaCopiar página

OpenAI GPT-Image-2 (`gpt-image-2`) es el modelo de imagen más reciente de OpenAI, disponible en ComfyUI a través de los Nodos asociados. Es el primer modelo de imagen de OpenAI que _razona_ antes de generar: en lugar de un muestreo de una sola pasada, el modelo planifica la composición, verifica su trabajo e itera. Este nodo admite:

  * Generación de texto a imagen con un manejo sólido de texto denso, elementos de UI, iconografía, infografías, mapas, diapositivas y paneles de manga
  * Edición de imágenes con alta fidelidad estructural a una resolución de hasta 2K
  * Hasta 8 imágenes consistentes a partir de un solo prompt, conservando la continuidad de personajes y objetos

GPT-Image-2 se selecciona como una opción de `model` en el nodo **OpenAI GPT Image 2.5** de la Biblioteca de nodos. El nodo llama a la API de generación de imágenes de OpenAI de forma síncrona y devuelve imágenes que coinciden con la descripción.

## 

​

Para qué es bueno GPT-Image-2

### 

​

Generación guiada por razonamiento

GPT-Image-2 planifica la composición antes de renderizar. Eso lo hace muy adecuado para prompts que históricamente rompían a los modelos de imagen: por ejemplo, un póster con una lista de siete elementos con viñetas en Helvetica de 11pt, centrado: y produce resultados limpios con texto denso, elementos de UI pequeños, iconografía, infografías, mapas y diapositivas.

### 

​

Edición de imágenes que conserva lo importante

GPT-Image-2 realiza ediciones puntuales con fidelidad estructural: mantiene todo lo que queda fuera de la zona editada estable píxel a píxel mientras aplica el cambio solicitado de forma limpia a una resolución de hasta 2K. Úsalo para tareas como colorear fotos en blanco y negro o pasar una escena del mediodía al atardecer sin deformar rostros, geometría ni detalles finos.

### 

​

Hasta ocho imágenes coherentes por prompt

El modelo puede devolver hasta **ocho imágenes distintas a partir de un solo prompt** manteniendo la continuidad de personajes y objetos a lo largo de la serie. Esto resulta útil para storyboards, hojas de referencia, vistas de personaje y variantes de producto sin fijar la semilla ni hacer malabares con el prompt. Envía el lote directamente a un nodo `Save Image` o encadénalo a un flujo de trabajo de video más adelante. ![Ejemplo de imágenes coherentes con GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/consistent_example.jpg)

## 

​

Flujos de trabajo híbridos

GPT-Image-2 encaja de forma natural en flujos de trabajo híbridos: úsalo para el fotograma principal con mucho texto y luego pasa a tus modelos locales para ampliación, estilización o generación de video: el mejor modelo para cada paso, en un solo gráfico.

## 

​

Salidas de ejemplo

Generación de texto a imagen con composición guiada por razonamiento: ![Ejemplo de texto a imagen con GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_t2i_1.jpg) Edición de imagen sobre una imagen de entrada, preservando la estructura fuera de la zona de edición: ![Ejemplo de imagen a imagen con GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_i2i_1.jpg) ![Ejemplo 1 de edición de imagen con GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_1.jpg)

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

  1. Actualiza ComfyUI a la última versión (v0.19.4 o posterior) o usa [Comfy Cloud](https://links.comfy.org/4u4o7Pv).
  2. En la Biblioteca de nodos, busca **OpenAI GPT Image 2.5** y agrega el nodo.
  3. Establece el campo `model` en `gpt-image-2`.



## 

​

Flujos de trabajo disponibles

### 

​

Texto a imagen (T2I)

Genera una imagen a partir de un prompt de texto con la composición basada en razonamiento de GPT-Image-2.

## Ejecutar Text-to-Image en Cloud

Prueba el flujo de trabajo Text-to-Image al instante en Comfy Cloud.

## Descargar el flujo de trabajo Text-to-Image

Descarga el JSON del flujo de trabajo.

![Vista previa del flujo de trabajo Text-to-Image de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_t2i-1.webp) ![Ejemplo de texto a imagen de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_t2i_1.jpg)

### 

​

Edición de imagen

Edita una imagen de entrada con alta fidelidad estructural a una resolución de hasta 2K.

## Ejecutar Image Edit en Cloud

Prueba el flujo de trabajo Image Edit al instante en Comfy Cloud.

## Descargar el flujo de trabajo Image Edit

Descarga el JSON del flujo de trabajo.

![Vista previa del flujo de trabajo Image Edit de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_image_edit-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo

![Ejemplo de imagen a imagen de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_i2i_1.jpg) ![Ejemplo 1 de edición de imagen de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_1.jpg) ![Ejemplo 2 de edición de imagen de GPT-Image-2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai/gpt_image_2/gpt_image_2_image_edit_2.jpg)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openai/gpt-image-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openai/gpt-image-2)

[GPT Image 2.5](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-5)[Gpt Image 1](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-1)
