---
url: https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-2-5/
title: Generaci\u00f3n de video con la API de LTX-2.5 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.546064+00:00
---

# Generación de video con la API de LTX-2.5 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-2-5/

## En esta página

Volver arriba

  * En qué destaca LTX-2.5
  * Salidas de ejemplo
  * Flujos de trabajo con la API de LTX-2.5
    * LTX-2.5 Text to Video
    * Consejos para el prompt
    * LTX-2.5 Image to Video
    * Consejos para el prompt
    * LTX-2.5 FLF2V
    * Consejos para el prompt



Lightricks

# Generación de video con la API de LTX-2.5 en ComfyUI

Copiar páginaCopiar página

Usa los nodos API de LTX-2.5 en ComfyUI para flujos de trabajo en la nube de texto a video, imagen a video y primer y último fotograma, con niveles Fast y Pro.

Copiar páginaCopiar página

[LTX-2.5](https://ltx.io/model/ltx-2-5) es el modelo de video y de mundo de pesos abiertos de Lightricks, disponible en ComfyUI a través de los nodos API de LTX-2.5. Los flujos de trabajo de la API ejecutan la generación en los servidores de Lightricks, así que no necesitas descargar modelos ni contar con una GPU local, y cada segundo de video generado se factura a tu cuenta de Comfy API. La API de LTX-2.5 ofrece dos niveles de modelo: **LTX-2.5 (Pro)** para la máxima calidad y **LTX-2.5 (Fast)** para una generación más rápida con el modelo destilado. Ambos niveles admiten la generación de audio y video sincronizados con escenas multicámara nativas, y el nivel Fast entrega una resolución de hasta 4K.

## 

​

En qué destaca LTX-2.5

  * **Audio y video sincronizados** : Ambos niveles generan audio y video juntos, con escenas de múltiples tomas nativas
  * **Dos niveles de modelo** : LTX-2.5 (Pro) para máxima calidad y LTX-2.5 (Fast) para generar más rápido con el modelo destilado
  * **Salidas de hasta 4K** : El nivel Fast produce hasta resolución 4K
  * **No requiere GPU local** : La generación se ejecuta en los servidores de Lightricks, sin descargas de modelos
  * **Varios modos de generación** : texto a video, imagen a video y video a partir del primer y último fotograma



## 

​

Salidas de ejemplo

Generación de texto a video con audio sincronizado: Generación de imagen a video a partir de una sola imagen inicial: Generación de primer y último fotograma a video, combinando dos fotogramas en una sola secuencia animada:

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

Flujos de trabajo con la API de LTX-2.5

La biblioteca de plantillas incluye tres flujos de trabajo de ejemplo de la API:

  * **Text to Video** : Genera videos a partir de prompts de texto
  * **Image to Video** : Genera videos a partir de una sola imagen inicial
  * **FLF2V** : Genera un video entre una imagen de primer y último fotograma



### 

​

LTX-2.5 Text to Video

Genera videos a partir de prompts de texto con la API de LTX-2.5, con audio sincronizado.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 T2V” en la Biblioteca de plantillas

#### 

​

Consejos para el prompt

  1. **Modelo** : Elige `LTX-2.5 (Pro)` para la máxima calidad, o `LTX-2.5 (Fast)` para una generación más rápida
  2. **Duración** : Pro admite de 2 a 10 segundos; Fast admite de 2 a 20 segundos. Las duraciones superiores a 10 segundos requieren una resolución de 720p o 1080p y 24/25 FPS
  3. **Resolución y relación** : Elige un preajuste de resolución como `1280x720` (horizontal) o `720x1280` (vertical); Fast añade las opciones `2560x1440` y `3840x2160`
  4. **FPS** : Elige entre 24, 25, 48 o 50 FPS en Fast, y 24, 25 o 50 FPS en Pro
  5. **Audio** : La generación de audio está activada de forma predeterminada; desactívala en las configuraciones avanzadas del nodo si solo necesitas un video sin sonido
  6. **Prompt** : Describe toda la escena en un solo párrafo fluido, incluyendo el plano, la acción, los personajes, el movimiento de cámara y el audio que deseas



### 

​

LTX-2.5 Image to Video

Genera un video a partir de una sola imagen inicial con la API de LTX-2.5, con audio sincronizado.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 I2V” en la Biblioteca de plantillas

## Imagen de entrada: space_battle.png

Fotograma inicial del flujo de trabajo, o usa tu propia imagen.

#### 

​

Consejos para el prompt

  1. **Modelo** : Este flujo de trabajo viene con `LTX-2.5 (Fast)` seleccionado para iterar más rápido; cambia a `LTX-2.5 (Pro)` para la máxima calidad
  2. **Solo una imagen** : La entrada de imagen acepta exactamente una imagen inicial
  3. **Prompt** : Describe lo que sucede a continuación: el movimiento, el movimiento de cámara y los sonidos que siguen a la imagen inicial. Frases como “Use the provided start image as the first frame” ayudan a anclar la generación
  4. **Duración y resolución** : El nivel Fast admite hasta 20 segundos y resoluciones de hasta 4K; las duraciones superiores a 10 segundos requieren 720p/1080p a 24/25 FPS



### 

​

LTX-2.5 FLF2V

Genera un video entre una imagen de primer y último fotograma con la API de LTX-2.5, combinando ambos fotogramas en una sola secuencia animada.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 FLF2V” en la Biblioteca de plantillas

## Primer fotograma: porsche_car_01.png

Primer fotograma del video.

## Último fotograma: porsche_car_02.png

Último fotograma del video, conectado a la entrada `last_frame` del nodo.

#### 

​

Consejos para el prompt

  1. **Fotogramas** : El flujo de trabajo conecta la primera imagen a la entrada `image` y la segunda imagen a la entrada `last_frame`; el modelo genera el movimiento entre ambas
  2. **Mantén los fotogramas alineados** : Usa imágenes con la misma relación de aspecto para una interpolación suave
  3. **Modelo** : Este flujo de trabajo viene con `LTX-2.5 (Pro)` seleccionado; cambia a `LTX-2.5 (Fast)` para una generación más rápida
  4. **Prompt** : Describe la transición entre los fotogramas y el audio (diálogos, efectos de sonido, música) que deseas



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/lightricks/ltx-2-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/lightricks/ltx-2-5)

[Kling Motion Control](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-motion-control)[Luma Text to Video (heredado)](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-video)
