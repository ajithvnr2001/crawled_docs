---
url: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-4/
title: Topaz Image Enhance Wonder 4: ampliaci\u00f3n de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:31.860933+00:00
---

# Topaz Image Enhance Wonder 4: ampliación de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-4/

## En esta página

Volver arriba

  * En qué destaca Topaz Image Enhance Wonder 4
  * Topaz Image Enhance Wonder 4
    * Controles
    * Pasos para ejecutar
  * Cuándo usarlo
  * Empezar



Topaz

# Topaz Image Enhance Wonder 4: ampliación de imágenes con IA

Copiar páginaCopiar página

Amplía imágenes suaves y comprimidas con Topaz Image Enhance Wonder 4 en ComfyUI: una sola pasada al tamaño objetivo que reconstruye detalle plausible en lugar de estirar píxeles

Copiar páginaCopiar página

Topaz Image Enhance Wonder 4 es un modelo de ampliación de imágenes disponible en ComfyUI a través de los nodos partner de Topaz. Reconstruye detalle plausible en lugar de estirar píxeles, así que una imagen pequeña y suave vuelve limpia hasta seis veces su tamaño. Conserva la relación de aspecto de la entrada y admite factores de upscale de 1x a 6x.

## 

​

En qué destaca Topaz Image Enhance Wonder 4

  * **Reconstrucción de detalle** : Reconstruye detalle plausible en imágenes suaves o comprimidas en lugar de interpolar píxeles
  * **Una sola pasada** : Una pasada al tamaño objetivo, sin ajustes de intensidad ni de grano
  * **Recuperación de fuentes pequeñas** : Útil para escaneos antiguos, capturas de pantalla, miniaturas de IA y recortes de móvil
  * **Salida flexible** : Conserva la relación de aspecto de la entrada y admite factores de upscale de 1x a 6x



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

Topaz Image Enhance Wonder 4

Amplía una sola imagen con Wonder 4, que reconstruye el detalle al tamaño objetivo en una sola pasada. El flujo de trabajo toma 1 imagen de entrada y produce 1 salida ampliada junto a una comparación lado a lado. ![Vista previa del flujo de trabajo de Topaz Image Enhance Wonder 4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder4-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Image Upscale: Topaz Wonder 4” en la Biblioteca de plantillas

### 

​

Controles

Control| Qué hace  
---|---  
`model`| Se ajusta a `Wonder 4`. `Wonder 3.5` y `Bloom 2` añaden sus propios ajustes, como la intensidad de mejora o un prompt  
`scale_by`| En el nodo **ImageScaleBy** : el factor de upscale. Wonder 4 admite de 1x a 6x; Bloom 2 llega hasta 12x  
`output_width` / `output_height`| En el nodo **TopazImageEnhanceV2** : el tamaño objetivo en píxeles, rellenado aquí desde **GetImageSize**. Deja ambos en 0 para que el tamaño de salida sea automático  
`filename_prefix`| En el nodo **SaveImageAdvanced** : el prefijo del nombre del archivo de salida  
  
Wonder 4 conserva la relación de aspecto de la fuente: cuando el ancho y el alto solicitados no coinciden, gana la escala mayor y la salida es más grande de lo pedido. La salida está limitada a 179 megapíxeles y 32.000 píxeles por lado, y el nodo reduce la entrada a unos 16 megapíxeles antes de enviarla.

### 

​

Pasos para ejecutar

  1. **Carga una imagen** : sube o selecciona tu imagen de entrada en el nodo **LoadImage**
  2. **Selecciona el modelo** : mantén `Wonder 4` en el nodo **TopazImageEnhanceV2**
  3. **Ajusta el tamaño objetivo** : cambia `scale_by` en el nodo **ImageScaleBy** , de 1x a 6x
  4. **Anulación opcional** : introduce un tamaño en píxeles en `output_width` o `output_height` del nodo (deja ambos en 0 para mantener el tamaño automático)
  5. **Haz clic en Queue** : pulsa `Ctrl+Enter` para generar



## 

​

Cuándo usarlo

Recurre a Wonder 4 con imágenes pequeñas, medianas, suaves, con ruido o comprimidas: escaneos antiguos, capturas de pantalla, miniaturas de IA y recortes de móvil. Una imagen con gráficos y textura es una buena prueba, porque los bordes rasgados, las costuras y las zonas de color plano muestran de inmediato si el modelo inventa detalle o conserva el original. Para una foto ya nítida y de alta resolución, un upscaler de precisión conserva más del original.

## 

​

Empezar

  1. Actualiza ComfyUI a 0.44.0 o posterior
  2. Ve a la Biblioteca de plantillas y busca `Image Upscale: Topaz Wonder 4`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/topaz/image-enhance-wonder-4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/topaz/image-enhance-wonder-4)

[Image Enhance Wonder 3 5](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)[Image Enhance Bloom 2](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/image-enhance-bloom-2)
