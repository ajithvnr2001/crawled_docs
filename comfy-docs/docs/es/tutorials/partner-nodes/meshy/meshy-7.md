---
url: https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-7/
title: Meshy 7 en ComfyUI: flujos de trabajo de texto a 3D e imagen a 3D - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.963674+00:00
---

# Meshy 7 en ComfyUI: flujos de trabajo de texto a 3D e imagen a 3D - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-7/

## En esta página

Volver arriba

  * En qué destaca Meshy 7
  * Flujo de trabajo de texto a modelo con Meshy 7
  * Flujo de trabajo de imagen a modelo de Meshy 7



Meshy

# Meshy 7 en ComfyUI: flujos de trabajo de texto a 3D e imagen a 3D

Copiar páginaCopiar página

Genera modelos 3D listos para producción con Meshy 7 en ComfyUI: flujos de trabajo de texto a 3D e imagen a 3D con modo ultra, texturas PBR, rigging y animación

Copiar páginaCopiar página

Meshy 7 es el modelo fundacional de generación 3D de Meshy, construido en torno a la alineación de imagen a 3D. Lee las imágenes de entrada a varias escalas y acepta entradas de mayor resolución, de modo que la información de forma detallada se conserva en la generación en lugar de promediarse. El resultado es una geometría 3D, color, material y patrón que permanecen alineados con la imagen de origen. En ComfyUI, Meshy 7 está disponible a través de los Nodos asociados de Meshy. Puedes generar un modelo de borrador a partir de un prompt de texto o de una sola imagen, luego refinarlo hasta convertirlo en un recurso completamente texturizado con mapas PBR, aplicarle rigging y animarlo, todo dentro de un mismo flujo de trabajo. Cada nodo de Meshy expone Meshy 7.1, Meshy 7, Meshy 6 y `latest` en su opción **model**. La plantilla de texto a modelo empieza en Meshy 7 y la plantilla de imagen a modelo empieza en Meshy 7.1.

## 

​

En qué destaca Meshy 7

  * **Text-to-3D e image-to-3D** : Generar un modelo a partir de un prompt de texto o de una sola imagen de entrada
  * **Ultra Mode** : Una pasada de refinamiento adicional para una geometría de mayor fidelidad y con detalles de superficie más finos, disponible en Meshy 7.1, Meshy 7 y los modelos `latest`. Text to Model e Image to Model también seleccionan la resolución de la pasada con `ultra_resolution`: `2k` (2048³) de forma predeterminada, o `4k` (4096³) en Meshy 7.1 y `latest`
  * **Texturizado PBR** : Generar mapas de metalicidad, rugosidad y normales con texturas de color base de 2K a 8K
  * **Pipeline completo de assets** : Refinar, crear el rig y animar el modelo generado en el mismo flujo de trabajo



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

Flujo de trabajo de texto a modelo con Meshy 7

Genera un modelo 3D directamente a partir de una descripción de texto. El flujo de trabajo crea la malla preliminar con el nodo Meshy 7 Text to Model y después la texturiza, le aplica el rig y la anima de forma automática.

## Ejecutar en Comfy Cloud

Ejecuta el flujo de trabajo de texto a modelo al instante en Comfy Cloud.

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo de forma local.

![Vista previa del flujo de trabajo de texto a modelo de Meshy 7](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_text_to_model-1.webp)

## 

​

Flujo de trabajo de imagen a modelo de Meshy 7

Convierte una sola imagen 2D en un modelo 3D detallado. El codificador de imágenes multiescala de Meshy 7 conserva la información de forma detallada de la imagen de origen, y el flujo de trabajo aplica texturas, rigging y animación al resultado en una sola pasada.

## Ejecutar en Comfy Cloud

Ejecuta el flujo de trabajo de imagen a modelo al instante en Comfy Cloud.

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo de forma local.

![Vista previa del flujo de trabajo de imagen a modelo de Meshy 7](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy7_image_to_model-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/meshy/meshy-7.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/meshy/meshy-7)

[Topología inteligente T2.5](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-t2-5)[Meshy 6](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-6)
