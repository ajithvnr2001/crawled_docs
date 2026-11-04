---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-flash/
title: ByteDance Seedream 5.0 Flash: generaci\u00f3n r\u00e1pida de im\u00e1genes en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.729392+00:00
---

# ByteDance Seedream 5.0 Flash: generación rápida de imágenes en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-flash/

## En esta página

Volver arriba

  * En qué destaca Seedream 5.0 Flash
  * Salidas de ejemplo
  * Flujo de trabajo de texto a imagen con Seedream 5.0 Flash
  * Flujo de trabajo de edición de imagen con Seedream 5.0 Flash
  * Empezar



ByteDance

# ByteDance Seedream 5.0 Flash: generación rápida de imágenes en ComfyUI

Copiar páginaCopiar página

Genera y edita imágenes de hasta 2K con Seedream 5.0 Flash en ComfyUI, el nivel de tarifa plana de la familia de imágenes Seedream 5.0 de ByteDance

Copiar páginaCopiar página

Seedream 5.0 Flash es el nivel rápido de la familia de imágenes Seedream 5.0 de ByteDance, junto con Seedream 5.0 Pro y Seedream 5.0 Lite. Genera una imagen a partir de un prompt de texto y edita una imagen existente a partir de una sola instrucción en el mismo nodo, y cobra una tarifa plana por imagen generada en todas las resoluciones que admite. Cada ejecución devuelve una imagen de entre 1K y 2K, con ocho relaciones de aspecto disponibles en cada uno de los niveles 1K, 1.5K y 2K. Puedes adjuntar hasta 10 imágenes de referencia para composiciones con varias referencias, como una foto de producto colocada en un nuevo diseño. El mismo modelo también se puede seleccionar en el nodo de separación de capas, que divide una imagen plana en capas transparentes editables.

## 

​

En qué destaca Seedream 5.0 Flash

  * **Tarifa plana en todas las resoluciones** : un solo precio por imagen generada en 1K, 1.5K y 2K, así que la resolución que elijas no cambia el costo
  * **Generación y edición en un solo nodo** : genera a partir de un prompt o adjunta una imagen de referencia y describe el cambio en una frase
  * **Entrada con múltiples referencias** : acepta hasta 10 imágenes de referencia, suficiente para combinar varios sujetos, productos o estilos en una sola composición
  * **Renderizado de texto** : maneja leyendas, etiquetas y texto de composición dentro de la imagen generada
  * **Una imagen por ejecución** : cada ejecución devuelve una imagen. Las opciones de generación por lote y secuencial disponibles en otros modelos Seedream no están expuestas para este modelo
  * **Separación de capas** : se puede seleccionar como el modelo en el nodo de separación de capas para convertir una imagen plana en una pila de capas editable



## 

​

Salidas de ejemplo

Generación de texto a imagen, produciendo una imagen con el tamaño predefinido seleccionado: ![Ejemplo de texto a imagen con Seedream 5.0 Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bytedance_seedream_5_0_flash_t2i.png) Edición de imagen a partir de una sola imagen de referencia y una instrucción de texto: ![Ejemplo de edición de imagen con Seedream 5.0 Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bytedance_seedream_5_0_flash_image_edit.png)

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

Flujo de trabajo de texto a imagen con Seedream 5.0 Flash

Genera una imagen a partir de un prompt de texto. El flujo de trabajo devuelve una sola imagen con el tamaño preestablecido seleccionado en el nodo. ![Vista previa del flujo de trabajo de texto a imagen con Seedream 5.0 Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_flash_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.0 Flash” en la Biblioteca de plantillas

## 

​

Flujo de trabajo de edición de imagen con Seedream 5.0 Flash

Edita una imagen existente con una instrucción de texto. Conecta la imagen de origen a la entrada `image_1` del nodo y describe el cambio que deseas, desde cambiar el fondo hasta reconstruir un set de producto alrededor del sujeto de la referencia. ![Vista previa del flujo de trabajo de edición de imagen con Seedream 5.0 Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_flash_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.0 Flash” en la Biblioteca de plantillas

## 

​

Empezar

  1. Actualiza ComfyUI a la versión 0.37.3 o posterior
  2. Ve a Template Library y busca `Seedream 5.0 Flash`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedream-5-flash.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedream-5-flash)

[FIBO 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo)[Seedream 5 Pro](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-pro)
