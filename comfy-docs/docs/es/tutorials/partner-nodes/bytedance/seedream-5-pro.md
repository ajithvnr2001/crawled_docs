---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-pro/
title: ByteDance Seedream 5.0 Pro - Generaci\u00f3n profesional de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.596134+00:00
---

# ByteDance Seedream 5.0 Pro - Generación profesional de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-pro/

## En esta página

Volver arriba

  * En qué destaca Seedream 5.0 Pro
  * Salidas de ejemplo
  * Flujo de trabajo texto a imagen de Seedream 5.0 Pro
  * Flujo de trabajo de edición de imágenes con Seedream 5.0 Pro
  * Flujo de trabajo de separación de capas de Seedream 5.0 Pro
  * Empezar



ByteDance

# ByteDance Seedream 5.0 Pro - Generación profesional de imágenes con IA

Copiar páginaCopiar página

Genera imágenes de alta calidad con mejor seguimiento de instrucciones, edición precisa y resultados profesionales con Seedream 5.0 Pro en ComfyUI

Copiar páginaCopiar página

Seedream 5.0 Pro es el modelo de generación de imágenes de nivel profesional de ByteDance, concebido como el hermano más capaz de Seedream 5.0 Lite. Ofrece mayor fidelidad, un seguimiento de instrucciones más preciso y una consistencia de salida más sólida para flujos de trabajo creativos y de producción exigentes.

## 

​

En qué destaca Seedream 5.0 Pro

  * **Salida de mayor fidelidad** : calidad de imagen superior con detalles más nítidos, texturas más ricas y una reproducción del color más precisa en resoluciones de hasta 4K
  * **Seguimiento preciso de instrucciones** : maneja prompts complejos de varios pasos con mayor exactitud, incluidos razonamiento espacial preciso, tipografía y renderizado de texto denso
  * **Edición con varias imágenes mejorada** : edita hasta 14 imágenes de referencia y conserva la identidad del sujeto, el estilo y la composición de forma más fiable que nunca
  * **Consistencia de nivel profesional** : los rasgos de los personajes, el diseño del producto, la iluminación y la paleta de colores se mantienen estables en un lote de imágenes generadas
  * **Conocimiento del mundo más profundo** : una base de conocimiento ampliada que respalda la ilustración técnica, la visualización científica y los briefs creativos con mucha carga de conocimiento



## 

​

Salidas de ejemplo

Generación de texto a imagen, con el modelo a cargo de la composición, la iluminación y el detalle: ![Ejemplo de texto a imagen con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Seedream5.0_Pro_T2I.png) Edición de imágenes con instrucciones de texto, manteniendo intacta la estructura original: ![Ejemplo de edición de imagen con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Seedream5.0_Pro_image_edit.png) Separación de capas, que divide una imagen plana en una pila editable de hasta 16 capas transparentes más un fondo con inpainting: ![Ejemplo de separación de capas con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/api_bytedance_seedream_5_0_layer_separation.png)

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

Flujo de trabajo texto a imagen de Seedream 5.0 Pro

Genera una imagen de alta calidad a partir de un prompt de texto, con Seedream 5.0 Pro encargándose de la composición, la iluminación y el detalle. ![Vista previa del flujo de trabajo texto a imagen de Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_pro_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.0 Pro” en la Biblioteca de plantillas

![Vista previa texto a imagen de Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Seedream5.0_Pro_T2I.png)

## 

​

Flujo de trabajo de edición de imágenes con Seedream 5.0 Pro

Edita imágenes existentes con instrucciones de texto. Cambia objetos, intercambia estilos, ajusta colores o recompón escenas manteniendo intacta la estructura original. ![Vista previa del flujo de trabajo de edición de imágenes con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_pro_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.0 Pro” en la Biblioteca de plantillas

![Entrada de la edición de imágenes con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/interior_college.png) ![Salida de la edición de imágenes con Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/Seedream5.0_Pro_image_edit.png)

## 

​

Flujo de trabajo de separación de capas de Seedream 5.0 Pro

La separación de capas es el pilar de descomposición por capas de la edición interactiva de precisión de Seedream 5.0 Pro. Divide una sola imagen plana en una pila editable: una imagen base (placa de fondo) más hasta 16 capas transparentes independientes, cada una con su orden de apilamiento, coordenadas de caja delimitadora, nombre y descripción semántica. El modelo rellena mediante inpainting las regiones ocultas detrás de los sujetos extraídos, de modo que cada capa y la base que queda debajo es un recurso de diseño completo e independiente, listo para arrastrar, escalar y recomponer. Sin ningún prompt, el modelo identifica automáticamente todos los elementos principales: bloques de texto, sujetos, decoraciones y fondo. Un solo póster puede generar más de 10 capas, con una separación de texto de calidad de diseño que admite titulares multilingües y fuentes CJK. También puedes describir los elementos en lenguaje natural para controlar la separación, o apuntar a regiones exactas con etiquetas de caja delimitadora. Este flujo de trabajo es ideal para diseño de marca, creación de recursos de comercio electrónico, iteración de pósters y cualquier tarea en la que un mapa de bits plano deba convertirse en un documento por capas editable. La plantilla incluye el modelo **Seedream 5.0 Flash** seleccionado. Cambia el modelo en el nodo a `seedream 5.0 pro` para ejecutar la separación con Seedream 5.0 Pro. ![Vista previa del flujo de trabajo de separación de capas de Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_layer_separation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.0 Pro” en la Biblioteca de plantillas

![Vista previa de la separación de capas de Seedream 5.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/api_bytedance_seedream_5_0_layer_separation.png)

Cuando uses este flujo de trabajo en el editor de ComfyUI, cambia al modo Nodes2.0 y haz clic en `Open Compositor` para ver y organizar las capas separadas.

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión (0.15.0+)
  2. Ve a la Biblioteca de plantillas y busca `Seedream 5.0 Pro`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedream-5-pro.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedream-5-pro)

[FIBO 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo)[Seedream 5 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-lite)
