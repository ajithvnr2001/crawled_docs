---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-6-astra/
title: GPT-6 Astra en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.344979+00:00
---

# GPT-6 Astra en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-6-astra/

## En esta página

Volver arriba

  * Cuándo elegir GPT-6 Astra
  * Usar el modelo en el nodo OpenAI Chat
  * Esfuerzo de razonamiento
  * Plantilla de GPT-6 Astra



OpenAI

# GPT-6 Astra en ComfyUI

Copiar páginaCopiar página

Usa OpenAI GPT-6 Astra con el nodo OpenAI Chat para razonamiento complejo, análisis de imágenes y flujos de trabajo con LLM en ComfyUI

Copiar páginaCopiar página

**GPT-6 Astra** es el modelo más capaz de OpenAI, diseñado para el trabajo de extremo a extremo más exigente: razonamiento complejo, programación, uso de computadora, investigación y creación de documentos. Publicado el 3 de septiembre de 2026, admite una ventana de contexto de 1,050,000 tokens, entrada de texto e imagen, y niveles de esfuerzo de razonamiento desde `low` hasta `max`. En ComfyUI, GPT-6 Astra se ejecuta a través del nodo `OpenAI Chat`: selecciona `gpt-6-astra` en el menú desplegable `model` del nodo. Esta página se centra en cómo usar el modelo dentro de los flujos de trabajo de ComfyUI. Para conocer los aspectos básicos del nodo que comparten todos los modelos, consulta el [tutorial de OpenAI Chat](https://docs.comfy.org/es/tutorials/partner-nodes/openai/chat).

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

Cuándo elegir GPT-6 Astra

El nodo `OpenAI Chat` ofrece muchos modelos, desde `gpt-5-nano` hasta `gpt-6-astra`. GPT-6 Astra es la opción más potente, pero también la más costosa, así que encaja en tareas donde los modelos más económicos tienen dificultades:

  * **Análisis de imágenes con contexto largo** : introducir muchas imágenes (mediante `Batch Images`) o archivos de prompt grandes y solicitar un análisis estructurado en una sola pasada
  * **Ingeniería de prompts** : convertir una imagen de referencia o una idea aproximada en un prompt positivo detallado y separado por comas para modelos de imagen o video
  * **Flujos de trabajo agénticos** : tareas de varios pasos como analizar la descripción de un conjunto de datos, luego escribir un plan de generación y luego redactar los prompts en sí
  * **Seguimiento de instrucciones complejas** : formatos de salida precisos (JSON, YAML, orden fijo de secciones) que los modelos más pequeños suelen no respetar

Para generar descripciones simples o respuestas cortas, `gpt-5` o `gpt-5-mini` producen buenos resultados a una fracción del costo. Consulta la [tabla de precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo.

## 

​

Usar el modelo en el nodo OpenAI Chat

El nodo `OpenAI Chat` recibe:

  * `prompt`: la instrucción. Para tareas de generación de prompts, describe exactamente qué extraer de la imagen y el formato de salida que quieres
  * `images`: contexto de imagen opcional. Conecta un `LoadImage`, o `Batch Images` para varias imágenes; cada imagen conectada se envía al modelo
  * `files`: documentos opcionales del nodo `OpenAI Chat Input Files`
  * `advanced_options`: configuración opcional del nodo `OpenAI Chat Advanced Options`

La salida es un `String`. Formas típicas de usarla en pasos posteriores:

  * En un nodo `Preview Any` para leer la respuesta
  * En `Save Text` para escribir el prompt generado en un archivo `.txt`
  * En la entrada de prompt positivo de un nodo `CLIP Text Encode`, para crear flujos de trabajo de generación de imágenes o video totalmente automáticos en los que el LLM escribe el prompt
  * En las entradas de texto de los Nodos asociados, por ejemplo, para redactar una descripción de escena antes de la generación de video



## 

​

Esfuerzo de razonamiento

GPT-6 Astra es un modelo de razonamiento. Conecta un nodo `OpenAI Chat Advanced Options` y configura `reasoning_effort` para controlar el equilibrio entre la calidad de la respuesta y el costo:

Nivel| Comportamiento  
---|---  
`default`| El modelo elige automáticamente  
`low`| La opción más rápida y económica, útil para análisis sencillos  
`medium`| Opción equilibrada predeterminada para generar prompts  
`high`| Análisis exhaustivo de imágenes o instrucciones complejas  
`xhigh`| Razonamiento profundo de varios pasos  
`max`| Máximo razonamiento para las tareas más difíciles  
  
El mismo nodo también expone `max_output_tokens` (de 16 a 16384, incluidos los tokens de razonamiento) y un campo `instructions` que funciona como un system prompt persistente, útil para fijar un formato de salida a lo largo de muchas ejecuciones.

## 

​

Plantilla de GPT-6 Astra

Una plantilla aparte muestra a GPT-6 Astra analizando una imagen y generando un prompt estructurado de arte con IA a partir de ella. El flujo de trabajo carga una imagen, envía un prompt de análisis al nodo `OpenAI Chat` con `model` establecido en `gpt-6-astra`, y escribe el resultado en un archivo de texto mediante `Save Text`. ![Vista previa del flujo de trabajo de GPT-6 Astra](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt6_astra-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “GPT-6 Astra” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## blue_poppies_field.png

Nodo `LoadImage` · `blue_poppies_field.png`

Pasos:

  1. Carga tu imagen en el nodo `LoadImage`
  2. En el nodo `OpenAI Chat`, ajusta el prompt de análisis o cambia `model` según lo necesites. El prompt de la plantilla pide al modelo que extraiga el sujeto, la composición, la cámara, la iluminación, la paleta de colores, la textura y el estilo, y que luego entregue únicamente un prompt positivo separado por comas
  3. Haz clic en `Run`. El prompt generado aparece en la vista previa y el nodo `Save Text` lo guarda en un archivo `.txt`

Para ir más allá, copia el prompt guardado en un nodo `CLIP Text Encode` o en un nodo de modelo de imagen o video y genera directamente a partir de la salida del modelo. GPT-6 Astra cobra según el uso de tokens de la API, a una tarifa más alta que otros modelos de OpenAI Chat. Consulta la [tabla de precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para más detalles.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openai/gpt-6-astra.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openai/gpt-6-astra)

[Chat](https://docs.comfy.org/es/tutorials/partner-nodes/openai/chat)[LLM](https://docs.comfy.org/es/tutorials/partner-nodes/openrouter/llm)
