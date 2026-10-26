---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash/
title: Gemini Omni Flash: generaci\u00f3n de video conversacional - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.856109+00:00
---

# Gemini Omni Flash: generación de video conversacional - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash/

## En esta página

Volver arriba

  * En qué destaca Gemini Omni Flash 1.1
  * Flujos de trabajo disponibles
    * Text to Video (Omni Flash)
    * Text to Video (Omni Flash 1.1)
    * Imagen a video (Omni Flash 1.1)
    * Referencia a video (Omni Flash 1.1)
    * Editar video (Omni Flash 1.1)
    * Extender video (Omni Flash 1.1)
  * Empezar



Google

# Gemini Omni Flash: generación de video conversacional

Copiar páginaCopiar página

Genera y edita videos con lenguaje natural usando Gemini Omni Flash 1.1, el modelo de video multimodal de Google, disponible en ComfyUI con Nodos asociados

Copiar páginaCopiar página

Gemini Omni Flash es el modelo de generación y edición de video conversacional de Google DeepMind, parte de la familia Gemini Omni presentada por primera vez en Google I/O 2026. Combina el razonamiento multimodal de Gemini con la creación nativa de video: describes lo que quieres en lenguaje natural, adjuntas imágenes o videos de referencia y el modelo genera un clip con audio sincronizado. La versión actual, Gemini Omni Flash 1.1, alcanzó la disponibilidad general el 27 de agosto de 2026 y añade interpolación de fotogramas clave, opciones de salida en 360p/4K y extensión de escena.

## 

​

En qué destaca Gemini Omni Flash 1.1

  * **Edición de video conversacional** : Refina y edita videos con lenguaje natural: cambia personajes, reilumina escenas, altera ángulos, agrega o elimina objetos manteniendo las pistas de audio y video originales
  * **Entrada multimodal** : Combina texto, imágenes (hasta 14) y videos (hasta 3, de 10 segundos cada uno) para guiar la generación. Cada resultado incluye una pista de audio nativa
  * **Interpolación de fotogramas clave** : Con la tarea `image_to_video`, adjunta un fotograma inicial y un fotograma final opcional, y el modelo genera el metraje intermedio
  * **Referencia a video** : Vincula imágenes de referencia a roles con etiquetas como `<IMAGE_REF_0>` para que los personajes, productos y objetos de tus imágenes aparezcan en una nueva escena sin que la imagen se use como fotograma
  * **Extensión de escena** : La tarea `extend` agrega hasta 10 segundos de metraje nuevo a un clip, leyendo los últimos 10 segundos de contexto para mantener la consistencia del personaje y del movimiento, hasta unos 40 segundos acumulados
  * **Control de resolución** : Genera borradores en 360p (cerca de un tercio del costo de 720p) y luego vuelve a renderizar en 720p, 1080p o 4K. Se admiten las relaciones de aspecto 16:9 y 9:16
  * **Conocimiento del mundo y simulación** : Combina la comprensión de la física con el conocimiento de Gemini sobre historia, ciencia y contexto cultural, lo que permite narrativas significativas más allá del fotorrealismo
  * **Sincronización de texto y acción** : Renderiza texto y gráficos legibles directamente en el video, sincronizando la tipografía cinética con los movimientos en pantalla



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

Los flujos de trabajo de Gemini Omni Flash 1.1 requieren ComfyUI 0.34.2 o posterior. En el nodo, selecciona **Omni Flash 1.1** en el menú desplegable de modelo para usar el modelo GA; la opción **Omni Flash** ejecuta el modelo de vista previa, que está programado para retirarse el 30 de septiembre de 2026.

## 

​

Flujos de trabajo disponibles

### 

​

Text to Video (Omni Flash)

Genera video a partir de un solo prompt de texto con el modelo Gemini Omni Flash de nivel preview. Describe la escena, la duración y la relación de aspecto en un solo prompt, y el modelo renderiza el clip con una pista de audio nativa. ![Vista previa del flujo de trabajo Text to Video de Gemini Omni Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni” en la Biblioteca de plantillas

El modelo Omni Flash en su versión preview tiene programado su retiro para el 30 de septiembre de 2026. Usa los flujos de trabajo de Omni Flash 1.1 que aparecen a continuación para el modelo GA.

### 

​

Text to Video (Omni Flash 1.1)

Genera video cinematográfico a partir de prompts en lenguaje natural con Gemini Omni Flash 1.1. Describe la duración deseada (de 3 a 10 segundos) directamente en el prompt y elige la relación de aspecto y la resolución de salida en el nodo: 16:9 o 9:16, 360p para borradores económicos y hasta 4K para los renders finales. Cada clip incluye una pista de audio generada. ![Vista previa del flujo de trabajo Text to Video de Gemini Omni Flash 1.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.1” en la Biblioteca de plantillas

### 

​

Imagen a video (Omni Flash 1.1)

Anima una imagen con Gemini Omni Flash 1.1. Con la tarea `image_to_video`, la primera imagen adjunta pasa a ser el fotograma inicial y una segunda imagen opcional pasa a ser el fotograma final: el modelo genera el metraje intermedio, lo que hace predecibles las órbitas de cámara, las transiciones de zoom y los clips en bucle. ![Vista previa del flujo de trabajo Imagen a video de Gemini Omni Flash 1.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.1” en la Biblioteca de plantillas

### 

​

Referencia a video (Omni Flash 1.1)

Genera video que incorpore sujetos específicos a partir de hasta 14 imágenes de referencia. En el modo de referencia, vincula cada imagen a un rol con etiquetas como `<IMAGE_REF_0>` y haz referencia a las etiquetas en tu prompt: los personajes, productos y objetos de tus imágenes aparecen en la escena, mientras que la imagen en sí nunca se usa como fotograma. Combina referencias de personajes con referencias de estilo para obtener contenido coherente con tu marca. ![Vista previa del flujo de trabajo Gemini Omni Flash 1.1 Reference to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_r2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.1” en la Biblioteca de plantillas

### 

​

Editar video (Omni Flash 1.1)

Edita videos con lenguaje natural usando Gemini Omni Flash 1.1. Con la tarea `edit`, el nodo toma exactamente un video de entrada (10 segundos o menos) y lo reescribe según tus instrucciones: cambia fondos, rediseña escenas, agrega o elimina elementos. Las tareas `edit` y `extend` mantienen la relación de aspecto del video de entrada. Los prompts simples funcionan mejor; agregar «mantén todo lo demás igual» maximiza la consistencia. ![Vista previa del flujo de trabajo Editar video con Gemini Omni Flash 1.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.1” en la Biblioteca de plantillas

### 

​

Extender video (Omni Flash 1.1)

Extiende un video existente hasta 10 segundos por paso con la tarea `extend`, creando historias de hasta unos 40 segundos en total. El modelo analiza los últimos 10 segundos de contexto y mantiene la coherencia de personajes, movimiento y audio mientras la escena continúa desde donde se quedó. De manera opcional, adjunta imágenes de referencia para introducir personajes nuevos a mitad de la historia. La extensión añade contenido nuevo solo al final del clip, pero el modelo puede revisar los fotogramas finales del material de origen para que la transición sea fluida. ![Vista previa del flujo de trabajo para extender video con Gemini Omni Flash 1.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_extend-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.1” en la biblioteca de plantillas

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión (0.34.2 o posterior para los flujos de trabajo de Omni Flash 1.1)
  2. Haz doble clic en el lienzo y busca los nodos “Gemini Omni Flash”
  3. O ve a la Biblioteca de plantillas para usar los flujos de trabajo listos para usar
  4. Elige el flujo de trabajo que coincida con tu tipo de entrada (texto, imagen o video)
  5. Escribe tu prompt y genera



Para obtener los mejores resultados, combina Gemini Omni Flash con Nano Banana 2 Lite: genera imágenes a alta velocidad y luego usa Gemini Omni Flash para animarlas y convertirlas en video.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/gemini-omni-flash.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/gemini-omni-flash)

[Crystal Video Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-video-upscale)[Video Grok](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-video)
