---
url: https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-upscale/
title: Pruna P-Video Upscale: escala video a 720p, 1080p, 2K o 4K - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:31.939130+00:00
---

# Pruna P-Video Upscale: escala video a 720p, 1080p, 2K o 4K - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-upscale/

## En esta página

Volver arriba

  * Agregar el nodo a un flujo de trabajo
  * Controles del nodo
  * Límites
  * Precios



Pruna

# Pruna P-Video Upscale: escala video a 720p, 1080p, 2K o 4K

Copiar páginaCopiar página

Escala video a 720p, 1080p, 2K o 4K en ComfyUI con Pruna P-Video Upscale: mantiene la relación de aspecto y el audio, e interpola hasta 60 fps.

Copiar páginaCopiar página

Pruna P-Video Upscale amplía un clip finalizado a 720p, 1080p, 2K o 4K. La salida mantiene la relación de aspecto y la pista de audio del video de origen. La frecuencia de cuadros se queda en la del origen, se interpola hasta 60 fps o baja descartando cuadros. El nodo es **Pruna P-Video Upscale** , en la categoría `partner/video/Pruna`. Recibe cualquier salida de video, desde un nodo **Load Video** o desde una generación en el mismo flujo de trabajo, y devuelve el clip escalado, así que puedes encadenarlo después de un nodo de texto a video o de imagen a video. Se ejecuta en los servidores de Pruna a través de la Comfy API. No hace falta descargar modelos ni tener una GPU local; necesitas una cuenta de Comfy API con créditos.

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

Agregar el nodo a un flujo de trabajo

  1. **Agrega el nodo** : haz clic derecho en el lienzo y busca **Pruna P-Video Upscale** , dentro de `partner/video/Pruna`
  2. **Conecta un video** : conecta una salida de video a la entrada `video`
  3. **Elige el objetivo** : `720p`, `1080p` (predeterminado), `2K` o `4K`
  4. **Define la frecuencia de cuadros** : `source` mantiene la frecuencia de la entrada hasta 60 fps; una frecuencia mayor se interpola y una menor descarta cuadros
  5. **Guarda el resultado** : conecta la salida a un nodo **Save Video**
  6. **Haz clic en Queue** : presiona `Ctrl+Enter` para ejecutarlo



## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`video`| video| El clip que se va a escalar. El límite de 512 MiB se aplica al MP4 que prepara el nodo, no al archivo que cargas  
`target`| `720p`, `1080p`, `2K`, `4K`| Área de píxeles de salida de aproximadamente 0.9, 2.1, 3.7 u 8.3 megapíxeles. Predeterminado `1080p`  
`fps`| `source`, `16`, `24`, `25`, `30`, `48`, `50`, `60`| Frecuencia de cuadros de salida. `source` mantiene la frecuencia de la entrada, con un límite de 60; una frecuencia menor descarta cuadros  
`turbo`| on / off| Escalado más rápido con detalle más suave, al mismo precio  
  
## 

​

Límites

  * Un origen más grande que el objetivo vuelve con su tamaño original, así que un clip de 1080p enviado a `720p` sigue siendo 1920×1080
  * La duración máxima por objetivo es de 2400, 1200, 600 o 300 cuadros para `720p`, `1080p`, `2K` o `4K`, contados a un máximo de 30 fps. Eso equivale a unos 100, 50, 25 o 12.5 segundos a 24 fps
  * Los clips de más de 10 megapíxeles deben apuntar a `2K` o `4K`
  * La entrada se recodifica a H.264 MP4 antes de subirla, y el límite de 512 MiB se aplica a ese archivo preparado, no al original. La pista de audio se conserva en el resultado
  * Las salidas de más de 30 fps cuestan el doble de la tarifa por segundo, también cuando `source` mantiene una frecuencia de origen superior a 30



## 

​

Precios

Pruna P-Video Upscale cobra por segundo de video de salida, y la tarifa depende del objetivo. Consulta [Precios de los nodos de socios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas actuales.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/pruna/p-video-upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/pruna/p-video-upscale)

[Pruna P-Video-2](https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-2)[Generación de video](https://docs.comfy.org/es/tutorials/partner-nodes/runway/video-generation)
