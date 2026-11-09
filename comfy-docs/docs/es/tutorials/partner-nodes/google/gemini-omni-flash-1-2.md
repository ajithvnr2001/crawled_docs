---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash-1-2/
title: Gemini Omni Flash 1.2: generaci\u00f3n de video conversacional - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.351842+00:00
---

# Gemini Omni Flash 1.2: generación de video conversacional - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash-1-2/

## En esta página

Volver arriba

  * Para qué sirve Gemini Omni Flash 1.2
  * Flujos de trabajo disponibles
    * Text to Video (Omni Flash 1.2)
    * Imagen a video (Omni Flash 1.2)
    * Referencia a video (Omni Flash 1.2)
    * Editar video (Omni Flash 1.2)
    * Extender video (Omni Flash 1.2)
  * Empezar



Google

# Gemini Omni Flash 1.2: generación de video conversacional

Copiar páginaCopiar página

Genera y edita video con Gemini Omni Flash 1.2 en ComfyUI: flujos de texto, imagen, referencia, edición y extensión, con audio nativo en cada clip

Copiar páginaCopiar página

Gemini Omni Flash 1.2 es el modelo de video conversacional de Google, disponible en ComfyUI a través del nodo socio **Google Gemini Omni (Video)**. Describe la toma en lenguaje natural, adjunta imágenes o un clip de referencia y el nodo devuelve video con audio sincronizado. La versión 1.2 genera clips de 3 a 15 segundos en 360p, 720p, 1080p o 4K, en 16:9 o 9:16. Acepta hasta 14 imágenes de referencia y 3 videos de referencia, y extiende un clip hasta 30 segundos. Omni Flash 1.1 y el modelo de vista previa anterior siguen disponibles para seleccionar en el nodo.

## 

​

Para qué sirve Gemini Omni Flash 1.2

  * **Edición conversacional** : cambia un personaje, vuelve a iluminar una escena, modifica el ángulo de cámara o agrega y elimina objetos mientras el resto del plano mantiene su encuadre y su audio
  * **Entrada multimodal** : combina texto, hasta 14 imágenes y hasta 3 videos de referencia de 15 segundos cada uno
  * **Interpolación de fotogramas clave** : con la tarea `image_to_video`, adjunta un fotograma inicial y un fotograma final opcional, y el modelo genera el metraje entre ambos
  * **Referencia a video** : etiqueta cada imagen de referencia como `<IMAGE_REF_0>` y nómbrala en el prompt, para que un personaje o producto aparezca en una escena nueva en lugar de usarse como fotograma
  * **Extensión de escena** : la tarea `extend` continúa un clip desde sus últimos fotogramas, hasta un resultado de 30 segundos, sin una costura visible
  * **Control de resolución** : haz un borrador a 360p y luego renderiza el clip final hasta 4K



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

Los flujos de trabajo de Gemini Omni Flash 1.2 requieren ComfyUI 0.44.1 o posterior. Selecciona **Omni Flash 1.2** en el menú desplegable de modelos del nodo.

## 

​

Flujos de trabajo disponibles

### 

​

Text to Video (Omni Flash 1.2)

Escribe la escena, la duración (de 3 a 15 segundos) y el movimiento en un solo prompt. El nodo devuelve el clip con una pista de audio generada. ![Vista previa del flujo de trabajo Text to Video de Gemini Omni Flash 1.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.2” en la Biblioteca de plantillas

### 

​

Imagen a video (Omni Flash 1.2)

Anima una imagen fija con la tarea `image_to_video`. La primera imagen es el fotograma inicial, una segunda imagen opcional es el fotograma final, y el prompt aporta el movimiento y el sonido. ![Vista previa del flujo de trabajo Imagen a video de Gemini Omni Flash 1.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.2” en la Biblioteca de plantillas

### 

​

Referencia a video (Omni Flash 1.2)

Mantén un sujeto consistente a lo largo de una nueva escena. Etiqueta cada imagen de referencia como `<IMAGE_REF_0>` y nombra la etiqueta en el prompt: el personaje o producto aparece en el clip, mientras que la imagen en sí nunca se usa como fotograma. ![Vista previa del flujo de trabajo Referencia a video de Gemini Omni Flash 1.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_r2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.2” en la Biblioteca de plantillas

### 

​

Editar video (Omni Flash 1.2)

Cambia una sola cosa en un clip finalizado con la tarea `edit`: cambia un fondo, modifica el estilo de una escena, agrega o elimina un elemento, mientras el corte, el tiempo y el audio se mantienen. Adjunta exactamente un video de hasta 15 segundos, limita el prompt al cambio que quieres y agrega “keep everything else the same” para lograr la máxima consistencia. ![Vista previa del flujo de trabajo Editar video de Gemini Omni Flash 1.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.2” en la Biblioteca de plantillas

### 

​

Extender video (Omni Flash 1.2)

Continúa un clip finalizado en lugar de volver a grabarlo. La tarea `extend` lee los últimos fotogramas y mantiene el sujeto, el encuadre y el audio durante el siguiente tramo: una entrada de 5 segundos se convierte en una salida de 10 segundos. Los videos de entrada pueden durar hasta 25 segundos y el resultado puede llegar a 30 segundos. ![Vista previa del flujo de trabajo Extender video de Gemini Omni Flash 1.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_extend-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemini Omni 1.2” en la Biblioteca de plantillas

## 

​

Empezar

  1. Actualiza ComfyUI a 0.44.1 o posterior
  2. Haz doble clic en el lienzo y busca “Google Gemini Omni (Video)”, o abre un flujo de trabajo desde la Biblioteca de plantillas
  3. Selecciona **Omni Flash 1.2** en el menú desplegable de modelo
  4. Elige la tarea que coincida con tu entrada, escribe el prompt y ejecuta



Para obtener los mejores resultados, combina Gemini Omni Flash con Nano Banana 2 Lite: genera imágenes a alta velocidad y luego anímalas para convertirlas en video.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/gemini-omni-flash-1-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/gemini-omni-flash-1-2)

[Crystal Video Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-video-upscale)[Gemini Omni Flash](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash)
