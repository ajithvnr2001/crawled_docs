---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/astra-2/
title: Astra 2 - Ampliaci\u00f3n creativa de video con diffusion - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.676811+00:00
---

# Astra 2 - Ampliación creativa de video con diffusion - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/astra-2/

## En esta página

Volver arriba

  * ¿Qué es Astra 2?
  * Descripción general del modelo
  * En qué destaca Astra 2
  * Relacionado
  * En ComfyUI
  * Flujo de trabajo de ejemplo



Topaz

# Astra 2 - Ampliación creativa de video con diffusion

Copiar páginaCopiar página

Qué hace Astra 2 con tus videos en ComfyUI y cómo ampliar con control de detalle y estilo.

Copiar páginaCopiar página

Ampliación creativa mejorada para video de IA generativa, con control avanzado del detalle y el estilo.

## 

​

¿Qué es Astra 2?

**Si eres nuevo aquí:** Astra 2 está pensado para **video generado por IA y estilizado**. La ampliación simple casi solo agranda y enfoca los píxeles existentes; Astra 2 puede **añadir detalle y textura nuevos y plausibles** donde la fuente es suave, para que el clip se sienta más rico, no solo más grande.

## 

​

Descripción general del modelo

Se basa en Astra 1 con un control más claro sobre cómo se generan el detalle y la estilización (creatividad, nitidez, prompts **descriptivos** opcionales, no listas de pasos). Encaja bien en: metraje estilizado o de IA generativa, planos generales y escenas con poco detalle, y metraje que se ve demasiado suave hasta que se restaura la textura.

## 

​

En qué destaca Astra 2

  * **Añade textura y detalle** : no solo nitidez.
  * **Aspecto controlable** : creatividad, nitidez, orientación por prompt opcional.
  * **Estilizado y planos generales** : donde el detalle inferido importa.



## 

​

Relacionado

  * [Ampliación de video en ComfyUI](https://docs.comfy.org/es/tutorials/utility/video-upscale): orientación para elegir un enfoque de ampliación.



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

En ComfyUI

Usa **Topaz Video Enhance**. **Topaz Video Enhance (Legacy)** no ofrece **Astra 2**. Configura el ampliador en **Astra 2** y la resolución en **FullHD** o **4K** ; la entrada debe ser **MP4**. **Prompt** opcional: máximo **450** fotogramas (~15 s a 30 fps). Prompt vacío: hasta **9000** fotogramas. Expande los controles avanzados para **Sharp** y **Realism** cuando lo necesites.

## 

​

Flujo de trabajo de ejemplo

**Load Video** → **Topaz Video Enhance** → **Save Video**. Después de abrir la plantilla, elige **Astra 2** en el ampliador si hay otro preajuste seleccionado. ![Vista previa del flujo de trabajo de Astra 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_astra2-1.webp)

## Ejecutar en Comfy Cloud

Abre el flujo de trabajo al instante en Comfy Cloud.

## Descargar flujo de trabajo

Descarga el JSON del flujo de trabajo para ComfyUI local.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/astra-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/astra-2)

[Video Enhance Astra](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/video-enhance-astra)[Nodos de video](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video)
