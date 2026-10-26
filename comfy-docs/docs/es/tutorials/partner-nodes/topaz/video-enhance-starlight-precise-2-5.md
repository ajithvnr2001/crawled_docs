---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5/
title: Topaz Starlight Precise 2.5 - Ampliaci\u00f3n de video con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.970625+00:00
---

# Topaz Starlight Precise 2.5 - Ampliación de video con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5/

## En esta página

Volver arriba

  * Para qué sirve Topaz Starlight Precise 2.5
  * Salidas de ejemplo
  * Topaz Starlight Precise 2.5
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Empezar



Topaz

# Topaz Starlight Precise 2.5 - Ampliación de video con IA

Copiar páginaCopiar página

Amplía videos hasta 4K con Topaz Starlight Precise 2.5 en ComfyUI: resultados más nítidos y menos artefactos en video de acción real

Copiar páginaCopiar página

Topaz Starlight Precise 2.5 es un modelo de ampliación de video disponible en ComfyUI a través de los nodos asociados de Topaz. Amplía videos MP4 hasta resolución 4K con resultados más nítidos y menos artefactos.

## 

​

Para qué sirve Topaz Starlight Precise 2.5

  * **Ampliación a 4K** : amplía videos MP4 hasta resolución 4K
  * **Mayor nitidez** : una salida más nítida con menos artefactos
  * **Metraje de acción real** : los pocos artefactos lo hacen ideal para video de acción real
  * **Opciones de resolución** : salida en FullHD (1080p) o 4K (2160p)



## 

​

Salidas de ejemplo

Ampliación de video con el modelo Starlight Precise 2.5, donde se aprecia el resultado mejorado y más nítido:

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

Topaz Starlight Precise 2.5

Amplía un video para obtener una salida más nítida y de mayor resolución con el modelo Starlight Precise 2.5. Este flujo de trabajo amplía videos MP4 hasta 4K con resultados más nítidos y menos artefactos.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Topaz Starlight Precise 2.5” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadVideo** : proporciona el video de origen
  * **TopazVideoEnhanceV2** : el nodo principal, configurado con el modelo de ampliación `Starlight Precise 2.5`
  * **SaveVideo** : guarda el video mejorado



### 

​

Pasos para ejecutar

  1. **Carga un video** : conecta tu video MP4 al nodo **LoadVideo**
  2. **Selecciona el ampliador** : mantén `Starlight Precise 2.5` en el nodo **TopazVideoEnhanceV2**
  3. **Define la resolución** : `FullHD (1080p)` o `4K (2160p)`
  4. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Topaz Starlight Precise 2.5`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/video-enhance-starlight-precise-2-5)

[Topaz Labs](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/overview)[Video Enhance Astra](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-astra)
