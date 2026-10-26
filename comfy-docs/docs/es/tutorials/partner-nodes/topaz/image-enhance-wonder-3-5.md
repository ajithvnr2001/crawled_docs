---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5/
title: Topaz Image Enhance Wonder 3.5 - Mejora de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.745343+00:00
---

# Topaz Image Enhance Wonder 3.5 - Mejora de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5/

## En esta página

Volver arriba

  * En qué destaca Topaz Image Enhance Wonder 3.5
  * Salidas de ejemplo
  * Topaz Image Enhance Wonder 3.5
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Empezar



Topaz

# Topaz Image Enhance Wonder 3.5 - Mejora de imágenes con IA

Copiar páginaCopiar página

Aumenta la escala y mejora imágenes con Topaz Image Enhance Wonder 3.5 en ComfyUI: restauración de detalles, reducción de ruido y nitidez de texto

Copiar páginaCopiar página

Topaz Image Enhance Wonder 3.5 es un modelo de mejora generativa disponible en ComfyUI a través de los Nodos asociados de Topaz. Añade detalles finos, reduce el ruido y agudiza el texto y los gráficos estructurados, con intensidades de mejora baja, media y alta. Conserva la relación de aspecto de la Entrada y admite factores de upscale de 1x a 6x.

## 

​

En qué destaca Topaz Image Enhance Wonder 3.5

  * **Restauración generativa de detalles** : Añade detalles finos a la imagen fuente
  * **Reducción de ruido** : Elimina el ruido mientras mejora la imagen
  * **Nitidez de texto y gráficos** : Aumenta la nitidez de texto y gráficos estructurados
  * **Intensidad ajustable** : Elige una intensidad de mejora baja, media o alta
  * **Salida flexible** : Conserva la relación de aspecto de la entrada y admite factores de upscale de 1x a 6x



## 

​

Salidas de ejemplo

Mejora de imagen con detalle fino añadido y ruido reducido: ![Salida de Topaz Image Enhance Wonder 3.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_topaz_image_enhance_wonder3_5.png)

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

Topaz Image Enhance Wonder 3.5

Aumenta la escala y mejora una sola imagen con el modelo generativo de Wonder 3.5, que añade detalles finos, reduce el ruido y mejora la nitidez de texto y gráficos estructurados. El flujo de trabajo toma 1 imagen de entrada y produce 1 salida mejorada junto con una comparación lado a lado. ![Vista previa del flujo de trabajo Topaz Image Enhance Wonder 3.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder3_5-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Topaz Image Enhance Wonder 3.5” en la Biblioteca de plantillas

![Salida de Topaz Image Enhance Wonder 3.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_topaz_image_enhance_wonder3_5.png)

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa cuatro nodos:

  * **LoadImage** : proporciona la imagen de origen
  * **TopazImageEnhanceV2** : el nodo principal, configurado con el modelo de mejora `Wonder 3.5`
  * **SaveImageAdvanced** : guarda la salida mejorada como PNG
  * **ImageCompare** : muestra el resultado mejorado junto al original para compararlos



### 

​

Pasos para ejecutar

  1. **Carga una imagen** : sube o selecciona tu imagen de entrada en el nodo **LoadImage**
  2. **Selecciona el modelo** : mantén `Wonder 3.5` en el nodo **TopazImageEnhanceV2**
  3. **Elige la intensidad de mejora** : `low`, `medium` o `high`
  4. **Configura el factor de escala** : de 1x a 6x
  5. **Haz clic en Queue** : pulsa `Ctrl+Enter` para generar



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Topaz Image Enhance Wonder 3.5`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)

[Topaz Labs](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/overview)[Image Enhance Bloom 2](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2)
