---
url: https://docs.comfy.org/es/tutorials/partner-nodes/qwen/qwen-image-3-0-pro/
title: Qwen Image 3.0 Pro - Generaci\u00f3n avanzada de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:54.706568+00:00
---

# Qwen Image 3.0 Pro - Generación avanzada de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/qwen/qwen-image-3-0-pro/

## En esta página

Volver arriba

  * Para qué sirve Qwen Image 3.0 Pro
  * Salidas de ejemplo
  * Flujo de trabajo texto a imagen de Qwen Image 3.0 Pro
  * Flujo de trabajo de edición de imágenes de Qwen Image 3.0 Pro
  * Empezar



Qwen

# Qwen Image 3.0 Pro - Generación avanzada de imágenes con IA

Copiar páginaCopiar página

Genera imágenes densas en información, prompts ultra largos, texto pequeño preciso y edición de varias imágenes con Qwen Image 3.0 Pro en ComfyUI

Copiar páginaCopiar página

Qwen Image 3.0 Pro es el modelo de generación de imágenes de tercera generación de Alibaba, centrado en resultados útiles: infografías, documentos y edición basada en instrucciones en lugar de pura estética. Se posiciona como una herramienta para crear visuales densos y ricos en información en una sola pasada, con el lema “Contenido rico, detalles auténticos, conocimiento profundo.” El modelo acepta prompts de hasta 4,500 tokens, aproximadamente 4.5 veces la longitud de entrada de la generación anterior. Utiliza ese presupuesto para componer páginas de periódico, infografías de varios paneles, artículos académicos con notación matemática legible y otros diseños de alta densidad sin comprimir el encargo en unas pocas frases. También renderiza texto pequeño legible hasta aproximadamente 10 píxeles en 12 idiomas y más de 20 fuentes, e integra conocimiento del mundo para tareas como mapas meteorológicos y replicación de interfaces de transmisión en vivo.

## 

​

Para qué sirve Qwen Image 3.0 Pro

  * **Prompts ultralargos** : acepta hasta 4,500 tokens de instrucciones para composiciones detalladas y densas en información
  * **Diseños densos y prácticos** : genera páginas de periódico completas, infografías de varios paneles y documentos académicos con fórmulas en una sola pasada
  * **Renderizado de texto pequeño** : produce texto legible hasta unos 10px en 12 idiomas y más de 20 fuentes
  * **Integración de conocimiento del mundo** : genera contenido basado en información del mundo real, como mapas del clima de ciudades específicas
  * **Edición basada en instrucciones** : edita hasta 3 imágenes de referencia con cambios específicos en objetos, estilos o regiones
  * **Generación por lotes** : genera de 1 a 6 imágenes por ejecución



## 

​

Salidas de ejemplo

Generación de texto a imagen, con el modelo encargándose del diseño, la tipografía y la composición: ![Ejemplo de texto a imagen de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_qwen3_t2i.png) Edición de imagen basada en instrucciones, conservando la estructura original: ![Ejemplo de edición de imagen de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_qwen3_image_edit.png)

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

Flujo de trabajo texto a imagen de Qwen Image 3.0 Pro

Genera una imagen detallada a partir de un prompt de texto, con Qwen Image 3.0 Pro encargándose del diseño, la tipografía y la composición. ![Vista previa del flujo de trabajo texto a imagen de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen Image 3.0 Pro” en la Biblioteca de plantillas

![Vista previa de texto a imagen de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_qwen3_t2i.png)

## 

​

Flujo de trabajo de edición de imágenes de Qwen Image 3.0 Pro

Edita imágenes existentes con instrucciones de texto. Combina hasta 3 imágenes de referencia, cambia objetos, intercambia estilos o recompón escenas manteniendo la estructura original. ![Vista previa del flujo de trabajo de edición de imágenes de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen Image 3.0 Pro” en la Biblioteca de plantillas

![Entrada para la edición de imágenes de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/wasteland_merchant.png) ![Salida de la edición de imágenes de Qwen Image 3.0 Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_qwen3_image_edit.png)

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Qwen Image 3.0 Pro`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/qwen/qwen-image-3-0-pro.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/qwen/qwen-image-3-0-pro)

[Quiver SVG](https://docs.comfy.org/es/tutorials/partner-nodes/quiver/quiver-svg)[Recraft V4](https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-v4)
