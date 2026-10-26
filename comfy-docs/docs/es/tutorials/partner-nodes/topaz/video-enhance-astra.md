---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-astra/
title: Topaz Astra Video Creative Upscale - Ampliaci\u00f3n de video con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.592670+00:00
---

# Topaz Astra Video Creative Upscale - Ampliación de video con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-astra/

## En esta página

Volver arriba

  * Para qué sirve Topaz Astra Video Creative Upscale
  * Topaz Astra: Video Creative Upscale
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Empezar



Topaz

# Topaz Astra Video Creative Upscale - Ampliación de video con IA

Copiar páginaCopiar página

Amplía y mejora videos con Topaz Astra en ComfyUI: ampliación Starlight (Astra) Fast con interpolación de cuadros apo-8 opcional

Copiar páginaCopiar página

Topaz Astra Video Creative Upscale está disponible en ComfyUI a través de los nodos asociados de Topaz. Amplía y mejora videos con el modelo Starlight (Astra) Fast, combinado opcionalmente con la interpolación de cuadros apo-8 para aumentar la frecuencia de cuadros. El flujo de trabajo acepta entrada MP4 y produce salida MP4 mejorada.

## 

​

Para qué sirve Topaz Astra Video Creative Upscale

  * **Ampliación creativa de video** : amplía y mejora videos con el modelo Starlight (Astra) Fast
  * **Interpolación de cuadros opcional** : cambia al modelo de interpolación apo-8 para aumentar la frecuencia de cuadros y suavizar el movimiento
  * **Resoluciones de destino** : salida en FullHD (1080p) o 4K (2160p)
  * **Entrada y salida simples** : acepta entrada MP4 y produce salida MP4 mejorada



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

Topaz Astra: Video Creative Upscale

Amplía y mejora un video con el modelo Starlight (Astra) Fast, con interpolación de cuadros apo-8 opcional para suavizar el movimiento. ![Vista previa del flujo de trabajo Topaz Astra Video Creative Upscale](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_video_enhance-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Topaz Astra” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadVideo** : proporciona el video de origen
  * **TopazVideoEnhanceV2** : el nodo central, configurado con el modelo de ampliación `Starlight (Astra) Fast`
  * **SaveVideo** : guarda el video mejorado



### 

​

Pasos para ejecutar

  1. **Carga un video** : conecta tu video MP4 al nodo **LoadVideo**
  2. **Selecciona el ampliador** : mantén `Starlight (Astra) Fast` en el nodo **TopazVideoEnhanceV2**
  3. **Define la resolución** : `FullHD (1080p)` o `4K (2160p)`
  4. **Interpolación de cuadros opcional** : cambia el modelo de interpolación a `apo-8` para aumentar la frecuencia de cuadros
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Topaz Astra`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/video-enhance-astra.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/video-enhance-astra)

[Video Enhance Starlight Precise 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5)[Astra 2](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/astra-2)
