---
url: https://docs.comfy.org/es/tutorials/partner-nodes/pika/pika-h3-flex/
title: Pika H3 Flex en ComfyUI: texto, imagen y video de referencia - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:41.669182+00:00
---

# Pika H3 Flex en ComfyUI: texto, imagen y video de referencia - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/pika/pika-h3-flex/

## En esta página

Volver arriba

  * Empezar
  * Pika H3 Flex: texto a video (API)
  * Imagen a video y primer y último fotograma
  * Referencia a video
  * Nodos de audio de Pika
  * Formato del prompt
  * Costo



Pika

# Pika H3 Flex en ComfyUI: texto, imagen y video de referencia

Copiar páginaCopiar página

Ejecuta Pika H3 Flex con el API de socios en ComfyUI: video de texto, imagen, primer y último fotograma y referencia con audio generado, de 480p a 4K.

Copiar páginaCopiar página

Pika H3 Flex es la versión post-entrenada de Pika de [MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3), servida a través de la API de socios de Pika. El nodo **Pika H3 Flex Video** genera un clip con audio sincronizado a partir de un prompt de texto, un primer fotograma o un último fotograma, y el nodo **Pika H3 Flex Reference to Video** añade imágenes, videos y clips de audio de referencia. Ninguno descarga pesos. Esta página cubre la versión de API. Para la versión de pesos abiertos que ejecuta dos adaptadores LoRA sobre la base H3 de forma local, consulta [Pika H3 Flex](https://docs.comfy.org/es/tutorials/video/pika/pika-h3-flex).

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

Empezar

  1. Actualiza ComfyUI a 0.44.1 o posterior
  2. Ve a Template Library y busca `Pika H3 Flex`
  3. Escribe el prompt y luego ejecuta el flujo de trabajo



## 

​

Pika H3 Flex: texto a video (API)

Genera un clip con audio generado a partir de un prompt de texto, de hasta 15 segundos. ![Vista previa del flujo de trabajo de texto a video de Pika H3 Flex](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_h3_flex_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pika H3 Flex” en la biblioteca de plantillas

  * **Resolución** : `480p`, `768p`, `1080p`, `2k` o `4k`, por defecto `768p`. `1080p` y superiores se renderizan a 768p y se escalan una vez
  * **Duración** : de 5 a 15 segundos. La salida sigue una cuadrícula de fotogramas, donde 5 segundos dan 124 fotogramas, unos 5.17 segundos
  * **Relación de aspecto** : `auto` sigue el primer fotograma conectado; de lo contrario, sigue el prompt
  * **Reescribir prompt** : desactivado por defecto, lo que mantiene reproducibles el prompt y la semilla



## 

​

Imagen a video y primer y último fotograma

El mismo nodo se encarga de ambos casos. Conecta `first_frame` por sí solo para animar una imagen inicial, o conecta `first_frame` y `last_frame` juntos para generar el movimiento entre dos fotogramas fijos.

## 

​

Referencia a video

El nodo **Pika H3 Flex Reference to Video** genera o edita un clip guiado por material de referencia: hasta 9 imágenes, 3 videos y 3 clips de audio, con 12 referencias en total. Los videos y los clips de audio deben durar de 2 a 15 segundos cada uno, con un límite de 15 segundos por separado para videos y para audio. Menciona las referencias en el prompt como `@Image1`, `@Video1` o `@Audio1`, en el orden en que están conectadas. Desactiva `reference_video_audio` cuando quieras un ambiente nuevo o música nueva en lugar del sonido de los videos conectados.

## 

​

Nodos de audio de Pika

Tres nodos de audio se ejecutan en la misma API de Pika y se facturan por segundo de audio generado:

  * **Pika Soundtrack** : reemplaza el audio de un video de hasta 10 minutos con una banda sonora sincronizada. La instrucción describe los efectos de sonido, el ambiente o la música; déjala vacía para derivar el audio a partir de la imagen.
  * **Pika SFX** : genera un efecto de sonido a partir de una descripción de texto, de 1 a 20 segundos de duración.
  * **Pika Music** : genera una canción a partir de un prompt de texto y letras opcionales, de 10 a 360 segundos, o versiona una canción original con su propia duración, limitada a 5 a 360 segundos.



## 

​

Formato del prompt

Los prompts de Pika H3 Flex siguen la estructura del modo de texto de MiniMax H3, donde una sola descripción reúne la imagen y el sonido:
    
    
    integrated_multimodal_description: [Shot 1] Live-action, cinematic, ... The camera tracks low alongside the board ...
    
    overall_soundscape: Wind rushes past the microphone, the board slaps across shallow water ...
    
    non_diegetic_music: A bright electronic pulse at a fast tempo ...
    

Mantén cada evento descrito dentro de la duración que definas. Para ver la estructura completa del prompt, incluidas las etiquetas de diálogo y las listas de tomas, consulta la [guía de escritura de prompts de MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md).

## 

​

Costo

Los nodos de video se cobran por segundo de salida, y la tarifa aumenta con la resolución. Consulta [Precios de los nodos de socio](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer los créditos actuales.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/pika/pika-h3-flex.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/pika/pika-h3-flex)

[Moonvalley Marey](https://docs.comfy.org/es/tutorials/partner-nodes/moonvalley/moonvalley-video-generation)[PixVerse AI](https://docs.comfy.org/es/tutorials/partner-nodes/pixverse/overview)
