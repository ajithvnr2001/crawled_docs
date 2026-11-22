---
url: https://docs.comfy.org/es/tutorials/utility/wevisone-vl/
title: WeVisOne-VL en ComfyUI: segmentaci\u00f3n y detecci\u00f3n con indicaciones de texto - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:52.303745+00:00
---

# WeVisOne-VL en ComfyUI: segmentación y detección con indicaciones de texto - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/wevisone-vl/

## En esta página

Volver arriba

  * Segmentación de imágenes: WeVisOne-VL
  * Tareas
  * Modelos
  * Más control sobre el nodo



Segmentation & Background

# WeVisOne-VL en ComfyUI: segmentación y detección con indicaciones de texto

Copiar páginaCopiar página

Segmenta, detecta, cuenta y hace OCR a imágenes en ComfyUI con WeVisOne-VL: una consulta de texto devuelve máscaras alfa, cajas, puntos o la respuesta en bruto.

Copiar páginaCopiar página

WeVisOne-VL es un modelo compacto de visión-lenguaje que responde con formas en lugar de texto. Dale una imagen y una consulta de texto breve, y devuelve cajas, puntos o una máscara alfa por instancia en una sola pasada: sin anotación y sin indicaciones por objeto. En ComfyUI funciona como el nodo **WeVisOne-VL Detect**. La plantilla a continuación lo envuelve en un subgrafo y previsualiza la máscara alfa, las cajas dibujadas sobre la imagen fuente y los recortes de primer plano y de fondo, de modo que la máscara alfa entra directamente en una cadena de eliminación de fondo, enmascaramiento o composición. Los pesos son las versiones de Tencent con licencia Apache-2.0, reempaquetados para ComfyUI en [Comfy-Org/WeVisOne-VL](https://huggingface.co/Comfy-Org/WeVisOne-VL). El soporte llegó en [ComfyUI #17632](https://github.com/Comfy-Org/ComfyUI/pull/17632) y la plantilla requiere ComfyUI 0.45.0 o posterior.

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

## Segmentación de imágenes: WeVisOne-VL

Escribe en `query` lo que quieres recortar y ejecuta. Con la tarea `segmentation` predeterminada y la consulta `human`, el gráfico devuelve una sola máscara combinada con las personas que encuentra, además de sus cajas. Activa `individual_masks` en el nodo para obtener una máscara por persona. ![Vista previa del flujo de trabajo de segmentación WeVisOne-VL con matte, cajas y recortes](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_wevisone_vl-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Segmentación de imagen: WeVisOne-VL” en la Biblioteca de plantillas

**Material de entrada**

## utility_image_segment_wevisone_vl_input.png

Cárgala en el nodo `LoadImage`

## Tareas

El widget `task` reescribe tu consulta como la instrucción con la que se entrenó el checkpoint. Cada tarea recibe su consulta en una forma ligeramente distinta:

`task`| Forma de la consulta| Devuelve  
---|---|---  
`segmentation`| Una frase nominal corta, como `human`| Máscara alfa y cajas (una máscara combinada salvo que `individual_masks` esté activado)  
`detection`| Una etiqueta por línea| Solo cajas  
`referring`| Una frase descriptiva, como `the cup on the left`| Cajas  
`point`| Una etiqueta por línea| Puntos centrales como JSON  
`count_box`| El sujeto a contar| Un conteo, con una caja en cada instancia  
`count_point`| El sujeto a contar| Un conteo, con un punto en cada instancia  
`ocr`| Nada| Una caja en cada palabra de la imagen  
`ocr_grounding`| La cadena exacta que quieres encontrar| Una caja alrededor de esa cadena  
`visual_prompt`| Nada, usa la entrada `bboxes`| Cajas para objetos similares a las cajas de referencia  
`freeform`| Cualquier cosa| La respuesta sin procesar, con la consulta como prompt completo  
  
Mantén la consulta corta. Una oración completa hace que `segmentation` divague, y una frase que nombre la cosa funciona mejor que una descripción de ella.

## Modelos

El flujo de trabajo carga el codificador de texto 2B INT8. Los otros tres archivos son reemplazos directos de `clip_name` en el nodo `CLIPLoader` (tipo `stable_diffusion`): el par 4B es más pesado y lento, y los archivos BF16 intercambian tamaño por precisión.

## 2B INT8 (este flujo de trabajo)

wevisone_vl_2b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## 2B BF16

wevisone_vl_2b_bf16.safetensors → ComfyUI/models/text_encoders/

## 4B INT8

wevisone_vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## 4B BF16

wevisone_vl_4b_bf16.safetensors → ComfyUI/models/text_encoders/

## Más control sobre el nodo

  * **`individual_masks`** : activado, una máscara por caja; desactivado, una máscara de unión por fotograma
  * **`max_length`** : límite de longitud de la respuesta, 4096 tokens por defecto y hasta 32768
  * **Salidas** : `masks`, `bboxes`, `points` (JSON con x, y, label y frame) y `text` (la respuesta sin procesar)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/wevisone-vl.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/wevisone-vl)

[Segmentación con SAM 3.1](https://docs.comfy.org/es/tutorials/utility/video-segment-sam3)[BiRefNet](https://docs.comfy.org/es/tutorials/utility/remove-background-birefnet)
