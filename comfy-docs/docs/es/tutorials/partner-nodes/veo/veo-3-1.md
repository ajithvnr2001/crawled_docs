---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-3-1/
title: Veo 3.1 en ComfyUI: texto a video con audio nativo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:40.109459+00:00
---

# Veo 3.1 en ComfyUI: texto a video con audio nativo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-3-1/

## En esta página

Volver arriba

  * Nodos
  * Ejecutar Veo 3.1
  * Modelo retirado



Veo

# Veo 3.1 en ComfyUI: texto a video con audio nativo

Copiar páginaCopiar página

Ejecuta Veo 3.1 de Google en ComfyUI con el nodo asociado: video 4K con audio nativo, tres niveles de velocidad y cobro en créditos por segundo.

Copiar páginaCopiar página

Veo 3.1 es el modelo de texto a video de Google DeepMind. Genera video con audio sincronizado y, en ComfyUI, se ejecuta como nodo asociado: la generación ocurre en los servidores de Google, así que pagas con créditos de Comfy y no necesitas descargar modelos ni contar con una GPU local.

## 

​

Nodos

Veo 3.1 se distribuye como dos nodos asociados. Agrega cualquiera de ellos desde la biblioteca de nodos:

  * **Google Veo 3 Video Generation** : texto a video, con una entrada opcional de imagen de referencia.
  * **Google Veo 3 First-Last-Frame to Video** : anima desde un primer fotograma hasta un último fotograma.

Ambos nodos ofrecen las mismas tres opciones de modelo:

Nivel| Opción de `model`| Resolución  
---|---|---  
Standard| `veo-3.1-generate`| 720p, 1080p, 4K  
Fast| `veo-3.1-fast-generate`| 720p, 1080p, 4K  
Lite| `veo-3.1-lite`| 720p, 1080p  
  
Los clips duran de 4 a 8 segundos con una relación de aspecto de 16:9 o 9:16. `generate_audio` conserva el audio sincronizado en la salida, y el nodo de primer y último fotograma lo trae activado por defecto.

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

Ejecutar Veo 3.1

Todavía no se incluye ningún flujo de trabajo de ejemplo para Veo 3.1, así que arma el gráfico alrededor del nodo: carga tu prompt, define el nivel en el widget `model` y luego pon el prompt en cola. Los créditos se cobran por segundo de video generado y varían según el nivel, la resolución y si se genera audio. Consulta [precios de los nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas actuales.

## 

​

Modelo retirado

Veo 2.0 ya no está disponible. Su nodo se eliminó de ComfyUI y su plantilla de flujo de trabajo se archivó; la [página de Veo 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-2-0) se conserva solo como referencia.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veo/veo-3-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veo/veo-3-1)

[Veo](https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview)[Veo 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/veo/veo-2-0)
