---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-6/
title: OpenAI GPT Image 2.6: flujos de trabajo Flare y Sunburst - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-07T13:48:28.253954+00:00
---

# OpenAI GPT Image 2.6: flujos de trabajo Flare y Sunburst - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-6/

## En esta página

Volver arriba

  * Primeros pasos
  * Configuraciones del nodo
  * GPT Image 2.6 Flare: Texto a imagen
  * GPT Image 2.6 Flare: edición de imagen
  * GPT Image 2.6 Sunburst: Texto a imagen
  * GPT Image 2.6 Sunburst: edición de imagen



OpenAI

# OpenAI GPT Image 2.6: flujos de trabajo Flare y Sunburst

Copiar páginaCopiar página

Genera y edita imágenes con los nodos asociados OpenAI GPT Image 2.6 Flare y Sunburst: borradores rápidos y cuatro plantillas de flujo de trabajo.

Copiar páginaCopiar página

GPT Image 2.6 es la familia de modelos de imagen de OpenAI, disponible en ComfyUI en el nodo socio **OpenAI GPT Image 2.6**. Viene en dos variantes:

  * **Flare** (`gpt-image-2.6-flare`): devuelve un borrador en segundos y mantiene la composición sobre carteles densos y fotos de producto. Úsala para primeras pasadas de concepto, mood boards y borradores con mucha tipografía
  * **Sunburst** (`gpt-image-2.6-sunburst`): invierte su presupuesto de render en textura fina, tipografía pequeña y materiales, y mantiene sujetos e iluminación consistentes entre pasadas. Úsala para visuales finalizados y composiciones densas donde el detalle tiene que resistir

Ambas variantes hacen texto a imagen y edición de imagen, con hasta 16 imágenes de referencia, una máscara opcional para relleno inteligente, niveles de calidad de `low` a `max` y un control de `complexity` que define cuánto planifica la imagen el modelo antes de renderizar. El nodo también sigue ofreciendo GPT Image 2.5, GPT Image 2 y GPT Image 1.5.

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

Primeros pasos

  1. Actualiza ComfyUI a 0.44.1 o una versión posterior
  2. En la Biblioteca de nodos, busca **OpenAI GPT Image 2.6** y agrega el nodo
  3. Establece `model` en `gpt-image-2.6-flare` o `gpt-image-2.6-sunburst`
  4. Conecta la salida de imagen del nodo a un nodo Guardar Imagen, o abre una de las cuatro plantillas que aparecen a continuación



## 

​

Configuraciones del nodo

  * **modelo** : `gpt-image-2.6-flare` para iterar rápido, `gpt-image-2.6-sunburst` para renders que priorizan el detalle
  * **prompt** : qué generar, o la instrucción de edición cuando hay imágenes de referencia conectadas
  * **tamaño** : `auto`, un preset como `1024x1024` o `3840x2160`, o `Custom`
  * **custom_width / custom_height** : se usan solo cuando `size` es `Custom`, de 480 a 3840 en pasos de 16
  * **fondo** : `auto`, `opaque` o `transparent`
  * **calidad** : `low`, `medium`, `high`, `xhigh` o `max`. Afecta el costo y el tiempo de generación
  * **complejidad** : `low`, `medium` o `high` (predeterminado). Cuánto planifica el modelo la imagen antes de renderizarla
  * **imágenes** : imágenes de referencia opcionales para edición, hasta 16
  * **máscara** : máscara opcional para relleno inteligente, las áreas blancas se reemplazan. Requiere exactamente una imagen de referencia
  * **n** : cuántas imágenes generar, de 1 a 8
  * **semilla** : se conserva por compatibilidad con la API, el backend todavía no la usa

Flare es la forma más económica de encontrar un prompt que funcione. Ejecútalo con calidad `low` o `medium` hasta que la composición quede bien y, después, vuelve a ejecutar el prompt ganador en Sunburst para obtener la imagen final.

## 

​

GPT Image 2.6 Flare: Texto a imagen

Genera un póster a partir de un prompt de texto. La plantilla pide texto renderizado y una composición densa, y ahí es donde importa la velocidad de Flare: puedes iterar sobre el texto sin pagar por la calidad final en cada intento.

## Descargar flujo de trabajo

Descarga el JSON o busca “GPT Image 2.6 Flare” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo GPT Image 2.6 Flare Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_t2i-1.webp)

## 

​

GPT Image 2.6 Flare: edición de imagen

Cambia un solo detalle de una foto y deja el resto intacto: conserva el rostro, la pose, el encuadre y la iluminación, y luego cambia la ropa, el cabello o un solo objeto.

## Descargar flujo de trabajo

Descarga el JSON o busca “GPT Image 2.6 Flare” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo de edición de imagen con GPT Image 2.6 Flare](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_image_edit-1.webp) Sube este archivo al nodo `Load Image`:

## Imagen de entrada: young_man_windblown.png

La imagen de entrada de ejemplo, o usa la tuya

## 

​

GPT Image 2.6 Sunburst: Texto a imagen

Genera un póster terminado con tipografía renderizada y textura fina. El prompt de la plantilla describe una capa a la vez: escena, sujeto, tipografía, pequeños elementos gráficos y, por último, la paleta y el estilo de renderizado.

## Descargar flujo de trabajo

Descarga el JSON o busca “GPT Image 2.6 Sunburst” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo GPT Image 2.6 Sunburst Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_t2i-1.webp)

## 

​

GPT Image 2.6 Sunburst: edición de imagen

Edita una foto manteniendo idénticos el ángulo de cámara, el encuadre, la posición del sujeto y la luz. Sunburst renderiza texturas finas y letras pequeñas, así que los pósteres y las escenas densas se mantienen bien en la segunda o tercera pasada.

## Descargar flujo de trabajo

Descarga el JSON o busca “GPT Image 2.6 Sunburst” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo GPT Image 2.6 Sunburst: edición de imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_image_edit-1.webp) Sube este archivo al nodo `Load Image`:

## Imagen de entrada: api_openai_gpt_image_26_sunburst_image_edit_input.png

La imagen de entrada del ejemplo, o usa la tuya

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openai/gpt-image-2-6.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openai/gpt-image-2-6)

[Muse Image](https://docs.comfy.org/es/tutorials/partner-nodes/meta/muse-image)[GPT Image 2.5](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-5)
