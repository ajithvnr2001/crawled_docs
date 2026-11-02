---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview/
title: Generaci\u00f3n de video con Google Veo en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:39.730902+00:00
---

# Generación de video con Google Veo en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview/

## En esta página

Volver arriba

  * Capacidades clave
  * Modelos



Veo

# Generación de video con Google Veo en ComfyUI

Copiar páginaCopiar página

Genera video con Veo 3.1 de Google DeepMind en ComfyUI: salida 4K con audio nativo, en niveles Estándar, Fast y Lite.

Copiar páginaCopiar página

**Veo 3.1** de Google DeepMind genera video con audio nativo sincronizado a través de los nodos asociados de ComfyUI, así que el render se ejecuta en los servidores de Google y la salida se encadena directamente con los nodos de ampliación, audio y composición de ComfyUI.

## 

​

Capacidades clave

  * **Video 4K de calidad cinematográfica** : Veo 3.1 genera hasta resolución 4K con iluminación natural y movimiento realista.
  * **Sincronización de audio nativo** : el video de salida incluye audio sincronizado, así que no hay que alinear una pasada de audio por separado.
  * **Tres niveles de velocidad** : Estándar, Fast y Lite intercambian calidad y latencia por costo, lo que sirve tanto para renders finales como para iterar rápido.
  * **Orientación por imagen** : el nodo de texto a video acepta una imagen de referencia opcional, y un nodo dedicado anima entre un primer y un último fotograma.
  * **Pipeline fluido en ComfyUI** : encadena la salida de Veo con nodos de ampliación, audio y composición sin exportar archivos.



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

Veo 3.1 es el modelo actual en ComfyUI. Veo 2.0 se retiró: su nodo se eliminó en ComfyUI #15883 y su flujo de trabajo está archivado, así que esa página se conserva solo como referencia.

## Veo 3.1

Texto a video con audio nativo. Niveles Estándar, Fast y Lite.

## Veo 2.0

Modelo de imagen a video retirado, conservado como referencia.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veo/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veo/overview)

[Nodos de video](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video)[Veo 3.1](https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-3-1)
