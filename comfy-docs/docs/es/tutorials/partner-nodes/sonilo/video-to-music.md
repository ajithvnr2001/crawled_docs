---
url: https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music/
title: Sonilo en ComfyUI: generaci\u00f3n de video a m\u00fasica y de texto a audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.357505+00:00
---

# Sonilo en ComfyUI: generación de video a música y de texto a audio - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music/

## En esta página

Volver arriba

  * Para qué sirve Sonilo Video to Music
  * Casos de uso
  * Empezar
    * Sonilo: Generación de bandas sonoras para video
    * Sonilo: Generación de música a partir de texto



Sonilo

# Sonilo en ComfyUI: generación de video a música y de texto a audio

Copiar páginaCopiar página

Genera bandas sonoras sincronizadas con tu video en ComfyUI con los Nodos asociados de Sonilo: flujos de trabajo de video a música y de texto a audio.

Copiar páginaCopiar página

Sonilo es un servicio de video a música impulsado por IA que genera bandas sonoras sincronizadas con tu metraje. Analiza las imágenes, el ritmo y las señales emocionales para producir música anclada a tu línea de tiempo, fotograma a fotograma. Puedes controlar la generación de música directamente desde tus grafos de nodos de ComfyUI, junto con tus flujos de trabajo existentes.

## 

​

Para qué sirve Sonilo Video to Music

  * **Alineación de duración, ritmo y emoción** \- La música se genera para coincidir con la duración, el ritmo y el arco emocional exactos de tu video, entregando bandas sonoras que se sienten compuestas intencionalmente para el contenido.
  * **Generación instantánea** \- Genera música completa y de alta calidad en segundos, lo que permite iterar más rápido y disfrutar de un flujo de trabajo creativo sin interrupciones.
  * **Uso comercial listo** \- Toda la música generada incluye derechos de uso comercial, por lo que está lista para usarse en entornos profesionales, de marca y de producción sin complejidades adicionales de licencias.



## 

​

Casos de uso

  * **Estudios de publicidad y creativos** \- Genera música que se ajuste al ritmo de videos de producto, anuncios de marca y anuncios para redes sociales.
  * **Productoras y estudios de postproducción** \- Automatiza la generación de bandas sonoras en grandes volúmenes de material de video.
  * **Artistas de VFX y gráficos en movimiento** \- Genera música que evolucione con tus imágenes, fotograma a fotograma.
  * **Creadores de contenido y agencias** \- Produce videos listos para cada plataforma con música sincronizada en múltiples formatos.
  * **Desarrolladores e ingenieros de pipelines** \- Integra la generación de música directamente en flujos de trabajo automatizados mediante ComfyUI.



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

1

Actualizar ComfyUI

Actualiza ComfyUI a la última versión o usa [Comfy Cloud](https://www.comfy.org/cloud).

2

Buscar un flujo de trabajo de Sonilo

Abre la **Workflow Library** , explora **Templates** y busca “Sonilo” para encontrar un flujo de trabajo listo para usar.

3

Ejecutar el flujo de trabajo

Conecta tu fuente de video, actualiza el prompt y haz clic en el botón **Run** o usa `Ctrl(Cmd) + Enter` para generar.

### 

​

Sonilo: Generación de bandas sonoras para video

Genera bandas sonoras sincronizadas a partir de material de video. Introduce un video para producir música que coincida con su ritmo y sus matices emocionales. ![Sonilo: Video Soundtrack Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_v2m-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Sonilo: Video Soundtrack Generation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo` correspondiente:

## leopard_rider.mp4

nodo `LoadVideo` 705 · `leopard_rider.mp4`

  1. Carga tu video en el nodo de entrada.
  2. (Opcional) Añade un prompt de texto para guiar el estilo o el ambiente de la música generada.
  3. Haz clic en el botón **Run** o usa el atajo `Ctrl(Cmd) + Enter` para iniciar la generación de música.
  4. El audio generado se guardará en el directorio `ComfyUI/output/audio`.



### 

​

Sonilo: Generación de música a partir de texto

Genera música de alta calidad, lista para producción, a partir de prompts de texto. ![Sonilo: Text to Music Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_t2m-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Sonilo: Text to Music Generation” en la Biblioteca de plantillas

**Prompts de ejemplo:**

  * `Dreamy ambient electronic music, gentle rhythm, suitable for short videos`
  * `Futuristic electronic instrumental, sci-fi sense, ethereal and deep`
  * `Lazy jazz instrumental, saxophone, relaxing cafe atmosphere`


  1. Introduce tu prompt de texto describiendo la música que quieres generar.
  2. Haz clic en el botón **Run** o usa el atajo `Ctrl(Cmd) + Enter` para iniciar la generación de audio.
  3. El audio generado se guardará en el directorio `ComfyUI/output/audio`.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/sonilo/video-to-music.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/sonilo/video-to-music)

[Seed Audio 1 0](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seed-audio-1-0)[HeyGen Voice 1.0](https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-voice-1)
