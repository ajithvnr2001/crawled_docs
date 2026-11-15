---
url: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-quality/
title: Grok Imagine Image Quality en ComfyUI: modelo de imagen retirado - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:55.570824+00:00
---

# Grok Imagine Image Quality en ComfyUI: modelo de imagen retirado - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-quality/

## En esta página

Volver arriba

  * En qué destaca Grok Imagine Image Quality
  * Salidas de ejemplo
  * Grok Imagine Image Quality: generación
    * Resumen del flujo de trabajo
    * Pasos para ejecutar



Grok

# Grok Imagine Image Quality en ComfyUI: modelo de imagen retirado

Copiar páginaCopiar página

Cómo se ejecuta ahora el modelo retirado Grok Imagine Image Quality en ComfyUI y qué modelo usar en su lugar.

Copiar páginaCopiar página

**Retirado** : xAI retiró `grok-imagine-image-quality`. La opción sigue en la lista de modelos del nodo y las ejecuciones se sirven ahora con `grok-imagine-image-2.0` en calidad baja. Para trabajo nuevo usa [Grok Imagine Image 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-2-0): allí el control de calidad está disponible directamente.

Grok Imagine Image Quality era el modelo de imagen de mayor fidelidad de xAI, disponible en ComfyUI a través de los nodos asociados de Grok. Aportaba más detalle, mejor renderizado de texto y un mayor control creativo en comparación con el modelo de imagen estándar de Grok.

## En qué destaca Grok Imagine Image Quality

  * **Más detalle** : una salida de mayor fidelidad que el modelo de imagen estándar de Grok
  * **Mejor renderizado de texto** : maneja prompts que incluyen texto que quieres que aparezca renderizado en la imagen
  * **Mayor control creativo** : más control sobre el resultado generado en comparación con el modelo estándar
  * **Opciones de resolución** : salidas en 1K o 2K



## Salidas de ejemplo

Ejemplo de salida de la plantilla: ![Salida de generación de Grok Imagine Image Quality](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

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

## Grok Imagine Image Quality: generación

Esta plantilla sigue seleccionando `grok-imagine-image-quality`. Las ejecuciones se sirven con `grok-imagine-image-2.0` en calidad baja. ![Vista previa del flujo de trabajo de generación de Grok Imagine Image Quality](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_quality_image_generation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Image Quality” en la Biblioteca de plantillas

![Salida de generación de Grok Imagine Image Quality](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

### Resumen del flujo de trabajo

Este flujo de trabajo usa dos nodos:

  * **GrokImageNode** : el nodo principal, configurado con el modelo `grok-imagine-image-quality`
  * **SaveImage** : guarda la imagen generada



### Pasos para ejecutar

  1. **Ingresa tu prompt** : describe la escena y cualquier texto que quieras que aparezca renderizado en **GrokImageNode**
  2. **Elige la relación de aspecto** : selecciona una de las relaciones disponibles
  3. **Establece la resolución** : `1K` o `2K`
  4. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/grok/grok-image-quality.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/grok/grok-image-quality)

[Grok Image 2 0](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-2-0)[HitPaw](https://docs.comfy.org/es/tutorials/partner-nodes/hitpaw/overview)
