---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2/
title: Topaz Image Enhance Bloom 2: ampliaci\u00f3n creativa de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.517147+00:00
---

# Topaz Image Enhance Bloom 2: ampliación creativa de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2/

## En esta página

Volver arriba

  * Para qué es bueno Topaz Image Enhance Bloom 2
  * Salidas de ejemplo
  * Topaz Image Enhance Bloom 2
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Empezar



Topaz

# Topaz Image Enhance Bloom 2: ampliación creativa de imágenes con IA

Copiar páginaCopiar página

Amplía y mejora imágenes con Topaz Image Enhance Bloom 2 en ComfyUI: ampliación creativa que añade detalle, textura y elementos visuales

Copiar páginaCopiar página

Topaz Image Enhance Bloom 2 es un modelo de ampliación creativa disponible en ComfyUI a través de los nodos asociados de Topaz. Añade nuevo detalle, textura y elementos visuales a tus imágenes, con un control de creatividad de 1 a 9 para un refinamiento sutil o una reinterpretación audaz. Conserva la relación de aspecto de la entrada y admite factores de ampliación de 1x a 6x.

## 

​

Para qué es bueno Topaz Image Enhance Bloom 2

  * **Ampliación creativa** : Agrega nuevos detalles, texturas y elementos visuales a tus imágenes
  * **Creatividad ajustable** : Un control de 1 para una mejora contenida hasta 9 para una reinterpretación pronunciada
  * **Prompt automático** : Si el prompt está vacío, el modelo crea uno automáticamente
  * **Salida flexible** : Conserva la relación de aspecto de la entrada y admite factores de ampliación de 1x a 6x



## 

​

Salidas de ejemplo

Ampliación creativa de una imagen generada por IA, con nuevos detalles y texturas añadidos: ![Salida de Topaz Image Enhance Bloom 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Upscaled_topaz_bloom2.png)

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

Topaz Image Enhance Bloom 2

Mejora imágenes generadas por IA con el modelo de ampliación creativa de Bloom 2, que añade nuevo detalle, textura y elementos visuales. El control de Creatividad va de 1, para una mejora contenida, a 9, para una reinterpretación marcada. Si el prompt está vacío, el modelo crea uno automáticamente. ![Vista previa del flujo de trabajo Topaz Image Enhance Bloom 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_bloom2-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Topaz Image Enhance Bloom 2” en la Biblioteca de plantillas

![Salida de Topaz Image Enhance Bloom 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Upscaled_topaz_bloom2.png)

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa cuatro nodos:

  * **LoadImage** : proporciona la imagen de origen
  * **TopazImageEnhanceV2** : el nodo principal, configurado con el modelo de ampliación `Bloom 2`
  * **SaveImageAdvanced** : guarda la salida mejorada como PNG
  * **ImageCompare** : muestra el resultado mejorado junto al original para compararlos



### 

​

Pasos para ejecutar

  1. **Carga una imagen** : sube o selecciona tu imagen de entrada en el nodo **LoadImage**
  2. **Selecciona el modelo** : mantén `Bloom 2` en el nodo **TopazImageEnhanceV2**
  3. **Establece la creatividad** : de 1 para una mejora contenida a 9 para una reinterpretación marcada
  4. **Prompt opcional** : déjalo vacío para que el modelo cree uno automáticamente
  5. **Haz clic en Queue** : pulsa `Ctrl+Enter` para generar



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Topaz Image Enhance Bloom 2`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2)

[Image Enhance Wonder 3 5](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/video/overview)
