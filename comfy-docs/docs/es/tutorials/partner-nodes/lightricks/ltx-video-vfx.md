---
url: https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-video-vfx/
title: LTX Video VFX en ComfyUI: recambia el encuadre, escala y convierte SDR a HDR - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:12.729885+00:00
---

# LTX Video VFX en ComfyUI: recambia el encuadre, escala y convierte SDR a HDR - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-video-vfx/

## En esta página

Volver arriba

  * Reencuadre
  * Ampliación
  * SDR to HDR
  * AlphaGen
  * Empezar



Lightricks

# LTX Video VFX en ComfyUI: recambia el encuadre, escala y convierte SDR a HDR

Copiar páginaCopiar página

Nodos de LTX Video VFX en ComfyUI: recambia el encuadre, escala a 1080p, 4K u 8K, convierte SDR a HDR u obtén un matte alfa.

Copiar páginaCopiar página

**LTX Video VFX** es un conjunto de nodos de video de Lightricks que trabajan sobre un clip finalizado en lugar de generar uno nuevo. Un nodo reencuadra la toma a otra relación de aspecto, otro la escala, otro la convierte de SDR a HDR y otro extrae una máscara alfa en escala de grises. Cada nodo recibe un video y devuelve un video. Son nodos API en la nube. Necesitan una cuenta de Comfy con créditos y no descargan ningún modelo local. Reencuadrar y escalar reconstruyen la imagen al nuevo tamaño en lugar de estirar la fuente, así que el detalle se conserva tras el cambio. Consulta [Precios de nodos Socio](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer la tarifa por segundo.

## Reencuadre

El reencuadre reconstruye la zona que queda fuera del video de origen para que coincida con él, así el sujeto permanece en plano en lugar de quedar recortado. Úsalo para convertir un clip vertical en un corte panorámico o para readaptar el metraje a otra plataforma.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “Reframe: LTX VFX” en la Biblioteca de plantillas

## man_black_horse_surreal.mp4

Cárgalo en el nodo `LoadVideo` que alimenta el nodo LTX Video Reframe

  * **Resolución** : preajustes de 720p o 1080p en 1:1, 4:5, 5:4, 9:16 y 16:9. El valor predeterminado es 1080x1920 (9:16)
  * **Posición** : `center` de forma predeterminada. `top`, `bottom`, `left` y `right` anclan la fuente a ese borde, y `custom` toma `x`, `y` y `width` como fracciones del fotograma de salida. La fuente debe permanecer dentro del fotograma y admite una ampliación máxima de 2x
  * **Límites** : hasta 60 segundos y 1800 fotogramas; cada lado, de 64 a 4096 píxeles



## Ampliación

La ampliación renderiza el clip a un tamaño mayor y conserva su relación de aspecto, frecuencia de cuadros y audio. La salida es tan grande como quepa en el objetivo elegido, rotada para clips verticales. ![Vista previa del flujo de trabajo LTX Video Upscale](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_upscale-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Upscale: LTX VFX” en Template Library

## desert_cave_caravan.mp4

Cárgalo en el nodo `LoadVideo` que alimenta el nodo LTX Video Upscale

  * **Resolución** : `1080p`, `4k` (predeterminado) u `8k`
  * **Límites** : lado corto de al menos 480 píxeles, hasta 7680x4320. Hasta 2401 cuadros en 1080p, 601 en 4k y 241 en 8k



## SDR to HDR

SDR to HDR convierte un clip de rango dinámico estándar en HDR de 10 bits (BT.2020, HLG) a la misma resolución. El nodo devuelve solo la imagen, así que la plantilla reconstruye el clip con el audio original del video de origen.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “SDR to HDR: LTX VFX” en la Biblioteca de plantillas

## sky_citadel_ring_collapse.mp4

Cárgalo en el nodo `LoadVideo` que alimenta el nodo LTX Video SDR to HDR

  * **Límites** : hasta 3840x2160 en cualquier orientación. Hasta 273 fotogramas en 1080p, 193 en 1440p y 65 en 4K



## AlphaGen

AlphaGen extrae una máscara en escala de grises que coincide con la entrada fotograma a fotograma, con blanco como primer plano. La salida es un video, así que envíala a través de **Obtener componentes de video** e **Image to Mask** para usarla como máscara. La pista de audio no se conserva. Todavía no existe una plantilla para este nodo: agrégalo desde la biblioteca de nodos y conecta tu propio `LoadVideo`.

  * **Límites** : hasta 10 segundos, como máximo 3840x2160 en cualquier orientación



## Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a Template Library y busca `LTX VFX`, luego arrastra una plantilla al lienzo
  3. Reemplaza el clip de ejemplo del nodo **Load Video** por uno propio, define la resolución objetivo en Reframe o Upscale y luego haz clic en **Queue**



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

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/lightricks/ltx-video-vfx.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/lightricks/ltx-video-vfx)

[Ltx 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-2-5)[Luma Text to Video](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-video)
