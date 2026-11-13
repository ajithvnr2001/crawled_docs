---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-4-hydrogen/
title: Gemini 4 Hydrogen: imagen a prompt en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:12.455366+00:00
---

# Gemini 4 Hydrogen: imagen a prompt en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-4-hydrogen/

## En esta página

Volver arriba

  * Para qué sirve Gemini 4 Hydrogen
  * Convertir una imagen en prompt con Gemini 4 Hydrogen
  * Configuraciones del nodo que cambian la salida
  * Familia de modelos Gemini 4
  * Notas



Google

# Gemini 4 Hydrogen: imagen a prompt en ComfyUI

Copiar páginaCopiar página

Analiza una imagen de referencia con Gemini 4 Hydrogen en ComfyUI y genera prompts, descripciones detalladas o desgloses visuales con el nodo socio de Gemini.

Copiar páginaCopiar página

Gemini 4 Hydrogen es uno de los modelos de texto Gemini 4 disponibles en el nodo socio `Google Gemini`. Adjuntas una imagen de referencia y una instrucción de texto, y el modelo escribe el texto que le pediste: un prompt con dirección de arte, una descripción detallada o un desglose estructurado de lo que contiene la imagen. Devuelve texto plano, así que el resultado puede alimentar otro nodo en el mismo flujo de trabajo en lugar de terminar en una ventana de chat.

## Para qué sirve Gemini 4 Hydrogen

  * **Ingeniería inversa de prompts** : convierte una imagen en un prompt positivo reutilizable que abarca sujeto, composición, cámara, iluminación, paleta, textura y estilo
  * **Descripciones detalladas** : escribe texto descriptivo extenso para un fotograma fijo, con la profundidad de razonamiento necesaria para mantener la descripción coherente entre párrafos
  * **Análisis visual estructurado** : pide un desglose elemento por elemento de un diseño, gráfico o escena en lugar de un solo párrafo
  * **Contexto multimodal** : además de la imagen, el nodo acepta un clip de audio, un clip de video y archivos mediante `Gemini Input Files`, hasta 16 imágenes en total
  * **Anotación por lotes** : ejecuta una carpeta de imágenes a través del flujo de trabajo con un nodo `Save Text` para que cada resultado quede guardado como archivo



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

## Convertir una imagen en prompt con Gemini 4 Hydrogen

La plantilla oficial carga una imagen, la envía a `Gemini 4 Hydrogen` junto con un prompt que solicita un prompt positivo estándar de arte con IA y, después, muestra la respuesta en `Preview Any` y la escribe en un archivo de texto. ![Flujo de trabajo de Gemini 4 Hydrogen que lee una imagen y escribe un prompt](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_4_hydrogen-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini 4 Hydrogen” en la Biblioteca de plantillas

**Materiales de entrada**

## blue_poppies_field.png

Nodo `LoadImage` · `blue_poppies_field.png`

  1. Carga tu imagen en el nodo `LoadImage` y conéctala a la entrada `images` del nodo `Google Gemini`.
  2. Edita el texto del nodo `Text (User Prompt)` si quieres otro tipo de respuesta. El prompt de la plantilla solicita sujeto, composición, cámara, iluminación, color, textura y estilo, y pide únicamente el prompt positivo.
  3. Ejecuta el flujo de trabajo. La respuesta aparece en `Preview Any` y `Save Text` escribe un archivo `.txt` en `ComfyUI/output/Gemini/` cuyo nombre empieza por `Gemini4_Hydrogen`. Dentro del archivo, a `USER PROMPT:` le sigue tu prompt y a `OUTPUT:` la respuesta del modelo.



## Configuraciones del nodo que cambian la salida

Configuración| Qué hace  
---|---  
`model`| Elige **Gemini 4 Hydrogen**. El mismo menú desplegable también incluye Gemini 4 Argon, Gemini 4 Carbon, Gemini 3.8 Flash y modelos de texto Gemini más antiguos  
`thinking_level`| Cuánto razona el modelo antes de responder. Hydrogen acepta `LOW`, `MEDIUM`, `HIGH` y `XHIGH`, y usa `HIGH` de forma predeterminada. Los niveles más altos cuestan más tokens de razonamiento y tardan más  
`max_output_tokens`| Límite de tokens generados, incluido el razonamiento. El valor predeterminado es 65536. Si las respuestas llegan vacías o cortadas con un nivel de razonamiento alto, auméntalo  
`images`, `audio`, `video`| Contexto multimodal opcional. Hasta 16 imágenes, un clip de audio y un clip de video por solicitud  
`video_processing`| `static` muestrea fotogramas a una tasa fija; `agentic` permite que el modelo navegue por la línea de tiempo y cargue solo los fotogramas, el audio o la transcripción que necesita, lo que usa muchos menos tokens de entrada en videos largos  
`system_prompt`| Instrucciones permanentes para el modelo; útiles cuando reutilizas un mismo prompt en muchas imágenes  
`files`| Contexto de archivos opcional desde el nodo `Gemini Input Files`. Primero sube los archivos a `ComfyUI/input/`  
  
Hydrogen no tiene widget de `temperature` ni de `top_p`. La variación de la salida proviene del prompt, del nivel de razonamiento y de la semilla, y no se garantiza una salida determinista.

## Familia de modelos Gemini 4

El nodo `Google Gemini` expone tres modelos de texto Gemini 4. Comparten un mismo conjunto de entradas y se diferencian en cuánto razonan y en la longitud de respuesta que pueden devolver:

Modelo| Niveles de razonamiento| Predeterminado| Tokens de salida máximos  
---|---|---|---  
Gemini 4 Hydrogen| `LOW`, `MEDIUM`, `HIGH`, `XHIGH`| `HIGH`| 65536  
Gemini 4 Argon| `LOW`, `MEDIUM`, `HIGH`| `MEDIUM`| 32768  
Gemini 4 Carbon| `LOW`, `MEDIUM`, `HIGH`| `MEDIUM`| 32768  
  
Por ahora, solo Hydrogen incluye una plantilla. Para probar Argon o Carbon, duplica el flujo de trabajo de Hydrogen y cambia el menú desplegable `model`; el resto del gráfico permanece igual.

## Notas

La plantilla Gemini 4 Hydrogen requiere ComfyUI 0.46.0 o una versión posterior. Las compilaciones anteriores no muestran los modelos Gemini 4 en el nodo `Google Gemini`. Todavía no existe una versión de Comfy Cloud de esta plantilla.

  * Este flujo de trabajo se ejecuta en tu cuenta de Comfy y se factura con los mismos créditos que los demás Nodos asociados. Consulta [Créditos de Nodos de Socio](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.
  * El flujo de trabajo original de chat de Gemini, incluido el ejemplo de `Batch Images`, permanece en la página de [Google Gemini](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini).



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/gemini-4-hydrogen.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/gemini-4-hydrogen)

[Crystal Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-upscale)[Nano Banana 2.1](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-1)
