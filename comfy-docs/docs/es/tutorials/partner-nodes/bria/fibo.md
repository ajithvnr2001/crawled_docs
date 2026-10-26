---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo/
title: Bria FIBO 2.0 en ComfyUI: texto a imagen y edici\u00f3n de imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.828777+00:00
---

# Bria FIBO 2.0 en ComfyUI: texto a imagen y edición de imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo/

## En esta página

Volver arriba

  * Para qué sirve Bria FIBO 2.0
  * Salidas de ejemplo
    * Bria: FIBO 2.0 Text to Image
    * Bria: FIBO 2.0 Image Edit
    * Bria: outpainting de imagen



Bria

# Bria FIBO 2.0 en ComfyUI: texto a imagen y edición de imagen

Copiar páginaCopiar página

Genera y edita imágenes en ComfyUI con los Nodos asociados de FIBO 2.0: prompts JSON estructurados, edición por instrucción con máscara opcional y outpainting.

Copiar páginaCopiar página

FIBO 2.0 es el modelo de imágenes de 8B de Bria que genera y edita imágenes con un solo conjunto de pesos, y se ejecuta en ComfyUI como Nodos asociados. Mantiene el entrenamiento con subtítulos estructurados sobre el que se construyó la línea FIBO: los prompts se expanden a un subtítulo en Visual GenAI Language (VGL) que nombra la iluminación, la composición, el color, la cámara y la profundidad de campo como campos separados, y ambos nodos devuelven ese subtítulo como una cadena JSON `structured_prompt`. Ese JSON es lo que hace que FIBO sea predecible. Vuelve a pasarlo con la misma semilla para reconstruir una imagen, cambia un solo campo para refinarla o constrúyelo mediante programación. FIBO 2.0 añade la edición por instrucciones sobre el mismo modelo: describe el cambio en lenguaje natural, o entrega el prompt estructurado, y todo lo que no pediste cambiar se queda como está. Ambos nodos son Nodos API en la nube. Necesitan una cuenta de Comfy con créditos, no descargan ningún modelo y se facturan por ejecución; consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas. Esta página también cubre la plantilla de outpainting de Bria, que se ejecuta en el nodo Bria Expand Image.

## 

​

Para qué sirve Bria FIBO 2.0

  * **Un solo modelo para ambas direcciones** : los mismos pesos de FIBO 2.0 generan una imagen nueva o editan una existente
  * **Control estructurado** : la iluminación, la composición, la cámara y el estilo son campos JSON explícitos en lugar de conjeturas en el prompt
  * **Ediciones que se mantienen** : la identidad, la disposición, la iluminación y el detalle fino permanecen intactos fuera del área que pediste cambiar
  * **Tipografía y textura** : texto legible dentro de la imagen, superficies de materiales convincentes y una anatomía más confiable que en las versiones anteriores de FIBO
  * **Datos con licencia** : entrenado con datos con licencia, con la procedencia que el trabajo comercial necesita

FIBO 2.0 resuelve las ediciones que los equipos piden con más frecuencia:

  * **Hora del día y relighting** : cambia la hora o la fuente de luz sin reconstruir la escena
  * **Cambios de material y textura** : tela, metal, acabado y ropa
  * **Edición de áreas con máscara** : limita un cambio a una región pintada y mantén el resto idéntico píxel a píxel
  * **Ajuste de texto** : reescribe o cambia el estilo de las palabras dentro de una imagen
  * **Restilización** : vuelve a renderizar una foto con otra dirección artística
  * **Pósteres y portadas** : diseños guiados por texto donde el titular debe renderizarse literalmente



## 

​

Salidas de ejemplo

Una edición por instrucción en el flujo de trabajo FIBO 2.0 Image Edit, conservando la escena de la azotea y cambiando solo la luz: ![Bria: FIBO 2.0 Image Edit, salida de ejemplo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

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

### 

​

Bria: FIBO 2.0 Text to Image

Describe la imagen, elige una forma y ejecuta. FIBO 2.0 expande el prompt en un subtítulo estructurado, genera a 1 MP o 4 MP y devuelve el subtítulo junto a la imagen para que puedas reconstruirla o refinarla más tarde. ![Vista previa del flujo de trabajo Bria: FIBO 2.0 Text to Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_fibo2_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: FIBO 2.0 Text to Image” en la Biblioteca de plantillas

**Cómo usarlo**

  1. **Escribe el prompt** : describe la imagen en `prompt`. FIBO 2.0 sigue de cerca briefs largos y específicos, incluido el texto exacto que debe aparecer dentro de la imagen.
  2. **Elige la forma** : `aspect_ratio` usa `1:1` de forma predeterminada, y los preajustes cubren `16:9`, `9:16`, `4:3`, `3:2` y los formatos más anchos `2:1`, `21:9`, `3:1`, `5:1`.
  3. **Elige la resolución** : `resolution` es `1MP` o `4MP`.
  4. **Referencia opcional** : conecta una foto a `image` para orientar el estilo o el contenido. El resultado es una composición nueva con la relación seleccionada, no una edición de esa foto, y no se puede combinar con `structured_prompt`.
  5. **Ejecuta e itera** : `seed` reproduce un resultado. La salida `structured_prompt` contiene el subtítulo JSON, así que puedes pasarla a otro nodo FIBO 2.0 para refinar un solo campo o reconstruir la misma imagen más tarde.



Los preajustes extendidos de FIBO 2.0 (`16:10`, `10:16`, `2:1`, `1:2`, `21:9`, `9:21`, `3:1`, `1:3`, `4:1`, `1:4`, `5:1`, `1:5`) están limitados a `1MP` y aceptan exactamente uno de `prompt` o `structured_prompt`. Usa las variantes horizontales para banners y encabezados de redes sociales; las relaciones estándar aceptan ambos campos juntos.

### 

​

Bria: FIBO 2.0 Image Edit

Edita una imagen describiendo el cambio, con una máscara opcional para limitarlo a una región. FIBO 2.0 mantiene la identidad, la disposición y el detalle fuera del área editada, y devuelve el prompt estructurado de la edición para poder reconstruirla o refinarla desde JSON. ![Vista previa del flujo de trabajo Bria: FIBO 2.0 Image Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: FIBO 2.0 Image Edit” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## sunlit_rooftop_capture.png

nodo `LoadImage` 5 · `sunlit_rooftop_capture.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sunlit_rooftop_capture.png)![Salida de ejemplo de Bria: FIBO 2.0 Image Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

**Cómo usarlo**

  1. **Carga la imagen** : súbela en `LoadImage` y conéctala a `BriaImageEditNode`.
  2. **Describe la edición** : escribe el cambio en `prompt`, por ejemplo `Modern architectural photography at night, blue hour`. Usa `negative_prompt` para mantener fuera los elementos no deseados.
  3. **O usa JSON** : pega un `structured_prompt` de un resultado anterior de FIBO 2.0 para un control preciso y repetible. El nodo acepta `prompt` o `structured_prompt`, no ambos.
  4. **Máscara opcional** : pinta la región que quieres regenerar y conéctala a `mask`. Sin máscara, la edición se aplica a toda la imagen, y se rechaza una máscara que no coincida con el tamaño de la imagen.
  5. **Ajusta y ejecuta** : `guidance_scale` va de 3 a 5 (un valor más alto sigue el prompt con más fidelidad) y `steps` de 20 a 50. `seed` reproduce un resultado.



### 

​

Bria: outpainting de imagen

Una plantilla de outpainting profesional impulsada por Bria, diseñada para extender imágenes sin costuras y ampliar la escena respetando los bordes. ![Vista previa del flujo de trabajo Bria: outpainting de imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Image Outpainting” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## baby_otter.png

nodo `LoadImage` 11 · `baby_otter.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/baby_otter.png)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bria/fibo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bria/fibo)

[Eliminación de fondo](https://docs.comfy.org/es/tutorials/partner-nodes/bria/background-removal)[Seedream 5 Pro](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-pro)
