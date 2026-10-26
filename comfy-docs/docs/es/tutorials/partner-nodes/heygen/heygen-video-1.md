---
url: https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-video-1/
title: HeyGen Video 1.0 en ComfyUI: texto, imagen y referencia a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.558762+00:00
---

# HeyGen Video 1.0 en ComfyUI: texto, imagen y referencia a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-video-1/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Texto a video
    * Imagen a video
    * Referencia a video
  * Controles del nodo
  * Consejos para escribir el prompt
  * Empezar



HeyGen

# HeyGen Video 1.0 en ComfyUI: texto, imagen y referencia a video

Copiar páginaCopiar página

Genera clips de 5 a 15 segundos con diálogo sincronizado desde un prompt, un primer fotograma o hasta 12 imágenes, videos y audios de referencia en ComfyUI

Copiar páginaCopiar página

**HeyGen Video 1.0** es un modelo de video de propósito general de HeyGen que genera la imagen, la línea hablada y el ambiente en una sola pasada. Describes la toma y el diálogo en el prompt, y el clip vuelve con voz sincronizada, así que un video de presentador o de producto no necesita rodaje, ni presentador, ni un paso aparte de locución. En ComfyUI el modelo se ejecuta mediante dos nodos asociados. **HeyGen Video 1.0 Reference to Video** se encarga de texto a video por sí solo y de referencia a video una vez que conectas imágenes, videos o audio; **HeyGen Video 1.0 Image to Video** parte de un primer fotograma. Ambos son nodos API en la nube: requieren una cuenta de Comfy con créditos y no descargan ningún modelo local. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por segundo. Cada ejecución devuelve un clip de 5 a 15 segundos en 480p, 768p o 2K, con el diálogo, el tono ambiente y cualquier música ya incluidos en el video.

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

Flujos de trabajo disponibles

### 

​

Texto a video

Genera un clip solo a partir de un prompt. El prompt incluye la acción, la línea hablada y el sonido, así que una sola ejecución del nodo devuelve un clip hablado finalizado.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HeyGen Video 1.0: Text to Video” en la Biblioteca de plantillas

La plantilla de texto a video ejecuta el nodo Reference to Video sin nada conectado, que es el modo texto a video de ese nodo.

### 

​

Imagen a video

Anima una imagen. La imagen es el primer fotograma del clip y la salida conserva su relación de aspecto, así que recorta la imagen cuando necesites una forma distinta. El prompt determina lo que ocurre y lo que se dice.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HeyGen Video 1.0: Image to Video” en la Biblioteca de plantillas

**Material de entrada**

## model_red_curls_ring.png

Cárgala en el nodo `LoadImage` que alimenta el nodo HeyGen Video 1.0 Image to Video

### 

​

Referencia a video

Mantén la coherencia de personas, productos y lugares a lo largo de la toma conectándolos como referencias: hasta 9 imágenes, 3 videos y 3 clips de audio, 12 en total. Después, el prompt se refiere a ellos como `@Image1`, `@Video1` y `@Audio1`, numerados por tipo en el orden de entrada.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HeyGen Video 1.0: Reference to Video” en la Biblioteca de plantillas

**Materiales de entrada**

## model_black_blazer_red_earrings.png

Cárgala en el primer espacio de imagen de referencia · `@Image1`

## cognac_leather_handbag.png

Cárgala en el segundo espacio de imagen de referencia · `@Image2`

## 

​

Controles del nodo

Control| Valores| Se aplica a| Efecto  
---|---|---|---  
`prompt`| texto, hasta 32000 caracteres| ambos nodos| El plano, la línea hablada y el sonido. Los medios de referencia se direccionan como `@Image1`, `@Video1`, `@Audio1`  
`duration`| 5 a 15 segundos| ambos nodos| Control deslizante, valor predeterminado 5  
`resolution`| `480p`, `768p`, `2K`| ambos nodos| Resolución de salida. En Reference to Video, `2K` requiere una `aspect_ratio` de `16:9` o `9:16`, y `auto` funciona a `2K` solo cuando no hay medios de referencia conectados  
`aspect_ratio`| `auto`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`| Reference to Video| `auto` es 16:9 cuando no hay nada conectado. Con referencias, sigue la primera imagen de referencia, o el primer video de referencia cuando no hay imágenes conectadas  
`seed`| entero| ambos nodos| Los resultados aún pueden variar entre ejecuciones con la misma semilla  
`reference_images`| hasta 9| Reference to Video| Una imagen por ranura. Se rechaza una entrada por lotes en una sola ranura  
`reference_videos`| hasta 3| Reference to Video| Un video por ranura  
`reference_audios`| hasta 3| Reference to Video| Necesita al menos una imagen o un video de referencia conectado. Una referencia de voz requiere unos segundos de habla limpia  
  
El nodo Image to Video toma la imagen, el prompt, la duración, la resolución y la semilla. No tiene control de relación de aspecto, porque el primer fotograma define la forma del clip.

## 

​

Consejos para escribir el prompt

  * **Escribe la línea hablada dentro del prompt**. Pon el diálogo entre comillas como parte de la descripción de la toma, para que el modelo lo diga y sincronice el movimiento de los labios. Ambas plantillas incluyen prompts de ejemplo extensos que muestran la estructura: primero la toma y el sujeto, luego la línea entre comillas, y después el sonido y el lenguaje de cámara.
  * **Describe el sonido junto con la imagen**. El tono ambiente de la sala, una pieza musical o el ruido que produce una acción se escriben en el prompt en lugar de configurarse con un control. Los prompts de ejemplo terminan con el ambiente, por ejemplo un tono de sala silencioso con un leve silbido de tetera, o un suave tintineo de vidrio al apoyar un objeto.
  * **Mantén la consistencia de un producto o un presentador**. Conecta el producto o a la persona como imagen de referencia y nómbralo en el prompt, luego describe cómo debe mantenerse igual, por ejemplo conservando el color, las proporciones y los herrajes exactos de un bolso de `@Image2`.
  * **Define la toma con referencias**. Con `aspect_ratio` en `auto`, el encuadre sigue a la primera imagen de referencia, así que la referencia que conectes primero decide la forma del video.
  * **Espera variaciones entre ejecuciones**. La semilla no fija el resultado; las mismas configuraciones pueden producir una toma distinta.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `HeyGen Video 1.0`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/heygen/heygen-video-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/heygen/heygen-video-1)

[Happyhorse1 0](https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-0)[Higgsfield Genjutsu](https://docs.comfy.org/es/tutorials/partner-nodes/higgsfield/genjutsu-motion-transfer)
