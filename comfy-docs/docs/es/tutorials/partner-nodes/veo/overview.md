---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview/
title: Generaci\u00f3n de video con Google Veo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:56.609965+00:00
---

# Generación de video con Google Veo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview/

## En esta página

Volver arriba

  * Capacidades clave
  * Modelos



Veo

# Generación de video con Google Veo

Copiar páginaCopiar página

Genera videos cinematográficos de alta resolución con los modelos Veo de Google DeepMind, Veo 3.1 y Veo 2.0, directamente en ComfyUI.

Copiar páginaCopiar página

**Veo 3.1** y **Veo 2.0** de Google DeepMind traen la generación de video con IA más avanzada a ComfyUI. Veo 3.1 ofrece video 4K de calidad cinematográfica con audio nativo, mientras que Veo 2.0 ofrece imagen a video rápido para prototipado veloz, todo integrado de forma fluida en tu pipeline de ComfyUI.

## 

​

Capacidades clave

  * **Video 4K de calidad cinematográfica** : Veo 3.1 genera video en resolución 4K con detalle nítido, iluminación natural y física realista, apto para uso profesional en cine y publicidad.
  * **Sincronización de audio nativo** : la salida de video incluye audio sincronizado, lo que elimina la necesidad de generar audio por separado y de alinearlo manualmente en postproducción.
  * **Texto a video (Veo 3.1)** : genera video de alta calidad directamente a partir de prompts de texto, con soporte para dirección detallada de escena, movimiento de cámara y control del estilo visual.
  * **Nivel de velocidad optimizado** : una variante de inferencia más rápida de Veo 3.1 que sacrifica un poco de calidad a cambio de un tiempo de generación mucho menor, ideal para iterar y producir borradores.
  * **Imagen a video (Veo 2.0)** : anima imágenes estáticas y las convierte en clips de video cortos, conservando la composición original y añadiendo movimiento natural.
  * **Pipeline fluido en ComfyUI** : la integración completa te permite encadenar la salida de Veo con los nodos de ampliación, audio y composición existentes de ComfyUI sin pasos de exportación de archivos.



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

Google Veo ofrece dos generaciones de modelos en ComfyUI, cada una optimizada para casos de uso diferentes. Veo 3.1 es el modelo insignia de texto a video con dos niveles de velocidad, mientras que Veo 2.0 ofrece una opción ligera de imagen a video.

## Veo 3.1

Texto a video 4K de calidad cinematográfica con audio nativo. Niveles Estándar y Fast disponibles.

## Veo 2.0

Imagen a video ligero para animar imágenes estáticas.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veo/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veo/overview)

[Nodos de video](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video)[Veo 3.1](https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-3-1)
