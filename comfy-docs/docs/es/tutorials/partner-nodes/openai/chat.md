---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openai/chat/
title: OpenAI Chat en ComfyUI: conversaciones y comprensi\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.137987+00:00
---

# OpenAI Chat en ComfyUI: conversaciones y comprensión de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openai/chat/

## En esta página

Volver arriba

  * Para qué sirve OpenAI Chat
  * OpenAI: ChatGPT
  * Completar la ejecución del flujo de trabajo paso a paso
  * Notas adicionales



OpenAI

# OpenAI Chat en ComfyUI: conversaciones y comprensión de imágenes

Copiar páginaCopiar página

Usa el nodo asociado OpenAI Chat en ComfyUI para conversaciones, interpretación de imágenes y generación de prompts desde imágenes con modelos seleccionables.

Copiar páginaCopiar página

OpenAI es una empresa enfocada en la IA generativa que ofrece potentes capacidades conversacionales. Actualmente, ComfyUI ha integrado la API de OpenAI, lo que te permite usar directamente los nodos relacionados en ComfyUI para completar funciones conversacionales.

## 

​

Para qué sirve OpenAI Chat

  * **Conversaciones inteligentes** : interactúa con los modelos de lenguaje avanzados de OpenAI directamente dentro de ComfyUI
  * **Comprensión de imágenes** : carga una imagen para que la IA la interprete y responda
  * **Control de tareas** : ajusta `OpenAI Chat Advanced Options` para que la IA ejecute tareas específicas, como analizar una imagen y generar un prompt
  * **Elección de modelo** : selecciona distintos modelos de OpenAI desde el nodo `OpenAI Chat`
  * **Entrada de varias imágenes** : agrupa varias imágenes en un lote cuando necesites que la IA interprete más de una



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

OpenAI: ChatGPT

Interactúa con los modelos de lenguaje avanzados de OpenAI para mantener conversaciones inteligentes. ![Vista previa del flujo de trabajo OpenAI: ChatGPT](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_chat-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “OpenAI: ChatGPT” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## example.png

Nodo `LoadImage` 5 · `example.png`

![example.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/example.png)

## 

​

Completar la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de OpenAI Chat](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a101638c18cc6656457c72f47bf0307c)

En la plantilla correspondiente, hemos creado una configuración de rol para analizar la generación de prompts.

Puedes guiarte por los números de la imagen para completar la ejecución básica del flujo de trabajo de texto a imagen:

  1. En el nodo `Load Image`, carga la imagen que necesitas que la IA interprete
  2. (Opcional) Si es necesario, puedes modificar las configuraciones en `OpenAI Chat Advanced Options` para que la IA ejecute tareas específicas
  3. En el nodo `OpenAI Chat`, puedes modificar `Prompt` para establecer el prompt de la conversación, o modificar `model` para seleccionar modelos diferentes
  4. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la conversación.
  5. Después de esperar a que la API devuelva los resultados, puedes ver el contenido correspondiente devuelto por la IA en el nodo `Preview Any`.



## 

​

Notas adicionales

  * Actualmente, el nodo de entrada de archivos `OpenAI Chat Input Files` requiere que primero cargues los archivos en el directorio `ComfyUI/input/`. Este nodo está en proceso de mejora y modificaremos la plantilla después de las actualizaciones
  * El flujo de trabajo incluye un ejemplo que usa `Batch Images` como entrada. Si tienes varias imágenes que necesitan interpretación de la IA, puedes consultar el diagrama de pasos y usar el clic derecho para establecer el modo del nodo correspondiente en `Always` y así activarlo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openai/chat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openai/chat)

[Gemini](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini)[GPT-6 Astra](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-6-astra)
