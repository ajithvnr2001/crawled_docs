---
url: https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-2/
title: Pruna P-Video-2: texto e imagen a video en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:54.634684+00:00
---

# Pruna P-Video-2: texto e imagen a video en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-2/

## En esta página

Volver arriba

  * En qué destaca P-Video-2
  * P-Video-2: de texto a video
    * Pasos para ejecutar
    * Consejos
  * P-Video-2: Imagen a vídeo
    * Pasos para ejecutar
    * Activo de entrada
  * Referencia de opciones del nodo



Pruna

# Pruna P-Video-2: texto e imagen a video en ComfyUI

Copiar páginaCopiar página

Genera video desde texto o una imagen inicial con los nodos asociados de Pruna P-Video-2 en ComfyUI: clips de 1 a 20 segundos, 720p o 1080p, audio nativo y modo borrador.

Copiar páginaCopiar página

Pruna P-Video-2 es el modelo de generación de video de Pruna enfocado en la calidad, disponible en ComfyUI a través de dos nodos asociados: **Pruna P-Video-2 Text to Video** y **Pruna P-Video-2 Image to Video**. Produce clips de 1 a 20 segundos en 720p o 1080p, a 24 o 48 fps, en siete relaciones de aspecto (16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 1:1), con audio nativo: ambiente, efectos de sonido y diálogos con sincronización labial generados a partir del prompt. El nodo de imagen a video anima un primer fotograma con un último fotograma opcional, y ambos nodos aceptan una entrada de audio opcional que impulsa el movimiento y se convierte en la banda sonora. El modo borrador renderiza vistas previas más rápidas y con menos detalle, facturadas al 60% de la tarifa estándar, así que puedes iterar sobre la composición antes de comprometerte con un render de calidad completa. Los nodos se ejecutan por completo en los servidores de Pruna a través de la API de Comfy. No necesitas descargar modelos ni contar con una GPU local; solo necesitas una cuenta de la API de Comfy con créditos.

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

En qué destaca P-Video-2

  * **Audio nativo** : genera una banda sonora con ambiente, efectos de sonido y diálogos con sincronización labial, o sigue una pista de audio conectada
  * **Salida flexible** : 720p o 1080p a 24 o 48 fps, de 1 a 20 segundos (o duración `auto` elegida a partir del prompt), siete relaciones de aspecto
  * **Modo borrador** : vistas previas más rápidas y menos detalladas al 60% de la tarifa estándar
  * **Primer y último fotograma** : la función imagen a video anima entre dos imágenes con relaciones de aspecto muy similares

El precio depende de la resolución y del modo borrador, con facturación por segundo. Consulta [Precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver los detalles.

## 

​

P-Video-2: de texto a video

Genera un video a partir de un prompt de texto. ![Flujo de trabajo de Pruna P-Video-2 de texto a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga JSON o busca “Prune P-Video 2: Text to Video” en la biblioteca de plantillas

### 

​

Pasos para ejecutar

  1. **Ingresa tu prompt** : describe la escena, su movimiento y su sonido en el nodo **Pruna P-Video-2 Text to Video** (hasta 5000 caracteres)
  2. **Establece la duración y la resolución** : elige entre 1 y 20 segundos o `auto`, y luego 720p (aproximadamente 0.9 megapíxeles) o 1080p (aproximadamente 2 megapíxeles)
  3. **Elige la frecuencia de cuadros** : 24 o 48 fps. 48 fps no está disponible con draft a 1080p
  4. **Opcional: conecta audio** : una entrada de audio impulsa el movimiento y establece la duración del video en lugar de `duration` (de 1 a 20 segundos; el audio más largo se recorta)
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



### 

​

Consejos

  * `enhance_prompt` (activado de forma predeterminada) reescribe los prompts cortos con más detalle. Desactívalo para reproducir un resultado exactamente con la misma semilla
  * Puedes desactivar `generate_audio` para obtener un clip sin sonido



## 

​

P-Video-2: Imagen a vídeo

Anima una imagen y conviértela en un video, con un último cuadro opcional. ![Flujo de trabajo Pruna P-Video-2 Imagen a vídeo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Prune P-Video 2: Image to Video” en la Biblioteca de plantillas

### 

​

Pasos para ejecutar

  1. **Sube un primer cuadro** : conecta un nodo **LoadImage**. La salida conserva la relación de aspecto de esta imagen
  2. **Opcional: sube un último cuadro** : el video termina en esta imagen. Su relación de aspecto debe ser cercana a la del primer cuadro
  3. **Describe el movimiento y el sonido** : escribe cómo se mueve y cómo suena la escena en el prompt (hasta 5000 caracteres)
  4. **Configura la duración, la resolución y la frecuencia de cuadros** : las mismas opciones que en texto a video
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



### 

​

Activo de entrada

El flujo de trabajo de ejemplo usa esta imagen de muestra:

  * [alien_mothership_foggy_megacity.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/alien_mothership_foggy_megacity.png)



## 

​

Referencia de opciones del nodo

Opción| Valores| Predeterminado| Notas  
---|---|---|---  
`duration`| 1 a 20, o `auto`| 5| Se ignora cuando hay audio conectado; el video entonces sigue la duración del audio  
`resolution`| 720p / 1080p| 720p| 720p es aproximadamente 0.9 MP, 1080p aproximadamente 2 MP en 16:9  
`fps`| 24 / 48| 24| 48 fps no está disponible con draft en 1080p  
`draft`| on / off| off| Renderizado más rápido y con menos detalle al 60% de la tarifa estándar  
`generate_audio`| on / off| on| Se ignora cuando hay audio conectado  
`enhance_prompt`| on / off| on| Avanzado. Desactívalo para lograr una reproducibilidad exacta de la semilla  
`seed`| 0 a 2147483647| 42| La reproducibilidad exacta requiere `enhance_prompt` desactivado  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/pruna/p-video-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/pruna/p-video-2)

[V6 y V6 Max](https://docs.comfy.org/es/tutorials/partner-nodes/pixverse/pixverse-v6)[Generación de video](https://docs.comfy.org/es/tutorials/partner-nodes/runway/video-generation)
