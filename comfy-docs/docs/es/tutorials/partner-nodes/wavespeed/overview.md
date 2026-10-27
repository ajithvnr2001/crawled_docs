---
url: https://docs.comfy.org/es/tutorials/partner-nodes/wavespeed/overview/
title: WaveSpeed en ComfyUI: ampliaci\u00f3n de imagen y video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:12.807982+00:00
---

# WaveSpeed en ComfyUI: ampliación de imagen y video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/wavespeed/overview/

## En esta página

Volver arriba

  * Funciones principales
  * Modelos



WaveSpeed

# WaveSpeed en ComfyUI: ampliación de imagen y video

Copiar páginaCopiar página

Amplía video y restaura imágenes en ComfyUI con WaveSpeed: ampliación temporal de video FLSH-VSR, restauración de fotos SeedVR2 y ampliación general.

Copiar páginaCopiar página

WaveSpeed es una plataforma de mejora de contenido multimedia con IA de alto rendimiento, ahora disponible como nodos nativos de flujo de trabajo en ComfyUI. Ofrece **ampliación de imágenes** y **SeedVR2 AI image fix** para fotos, además de **ampliación de video con FLSH-VSR** , todo impulsado por ComfyCloud y sin necesidad de una GPU local.

## 

​

Funciones principales

  * **Ampliación de video con FLSH-VSR** : superresolución de video con IA y coherencia temporal que mantiene un detalle uniforme entre fotogramas, ideal para archivo, mejora de video con IA y conversión de SD a HD.
  * **Ampliación general de imágenes** : aumento de tamaño y mejora de calidad para múltiples propósitos, que abarca fotografías, arte digital, renders y capturas de pantalla.
  * **SeedVR2 AI image fix** : modelo de restauración basado en diffusion para recuperar imágenes dañadas, degradadas o de baja calidad, incluida la reparación de fotos antiguas, la eliminación de ruido y artefactos, y la reconstrucción de detalles perdidos.
  * **Sin necesidad de GPU local** : todo el procesamiento se ejecuta en la infraestructura de ComfyCloud, lo que mantiene tu hardware local libre para la generación y la composición.
  * **Integración sencilla en el pipeline** : nodos simples que puedes insertar directamente y que funcionan como paso final de mejora o como etapa intermedia de preprocesamiento en cualquier flujo de trabajo de ComfyUI.
  * **Amplia compatibilidad de contenido** : los modelos manejan diversos tipos de entrada, incluidas fotografías, arte con IA, fotogramas de video e imágenes web comprimidas.



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

Modelos

WaveSpeed ofrece dos grupos de modelos en ComfyUI. El grupo **Upscale** cubre la ampliación general de imágenes y la restauración con SeedVR2, mientras que **FlashVSR** proporciona superresolución de video con coherencia temporal.

## WaveSpeed Upscale

Ampliación general de imágenes y restauración de imágenes con SeedVR2 AI.

## WaveSpeed FlashVSR

Ampliación de video con IA y coherencia temporal.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/wavespeed/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/wavespeed/overview)

[Wan2 7](https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan2-7)[WaveSpeed Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/wavespeed/wavespeed-upscale)
