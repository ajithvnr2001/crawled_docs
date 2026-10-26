---
url: https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-image-3-5/
title: Tencent Hunyuan Image 3.5 Preview en ComfyUI: flujos de trabajo de texto a imagen y edici\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.430818+00:00
---

# Tencent Hunyuan Image 3.5 Preview en ComfyUI: flujos de trabajo de texto a imagen y edición - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-image-3-5/

## En esta página

Volver arriba

  * En qué destaca HY Image 3.5 Preview
  * Flujo de trabajo de texto a imagen de Tencent HY Image 3.5 Preview
    * Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de edición de imagen con Tencent HY Image 3.5 Preview
    * Pasos para ejecutar el flujo de trabajo
    * Consejos para el prompt
  * Empezar



Tencent

# Tencent Hunyuan Image 3.5 Preview en ComfyUI: flujos de trabajo de texto a imagen y edición

Copiar páginaCopiar página

Genera y edita imágenes con Tencent Hunyuan Image 3.5 Preview en ComfyUI: texto multilingüe, 5 imágenes de referencia y salida 4K desde 2K.

Copiar páginaCopiar página

Tencent Hunyuan Image 3.5 Preview es el modelo de imagen en vista previa de Tencent, disponible en ComfyUI a través de los Nodos asociados. Genera imágenes a partir de texto y edita imágenes existentes a partir de una instrucción, con especial atención al renderizado de texto multilingüe, el fotorrealismo y la coherencia entre una imagen de referencia y el resultado editado. En comparación con los modelos de imagen Hunyuan anteriores, HY Image 3.5 Preview refuerza tres áreas: el renderizado y la composición tipográfica de texto multilingüe para publicidad, infografías y diseño de UI; el fotorrealismo y el alcance estilístico en fotografía cinematográfica, cómic, fotografía comercial e ilustración; y la coherencia de edición, que conserva los rasgos clave de personas y productos al cambiar el fondo, el atuendo y el estilo. Hay dos flujos de trabajo disponibles. `Tencent HY Image: Text to Image` genera una imagen a partir de un prompt, y `Tencent HY Image: Edit` edita o combina hasta cinco imágenes de referencia. Ambos se ejecutan en los servidores de Tencent a través de Comfy API, por lo que no se requieren descargas de modelos ni una GPU local.

## 

​

En qué destaca HY Image 3.5 Preview

  * **Texto y composición multilingües** : genera texto legible para pósteres, infografías y maquetas de UI en lugar de imágenes de escenas simples
  * **Alcance fotorrealista** : abarca fotogramas cinematográficos, arte de cómic, fotografía comercial e ilustración a partir de prompts breves
  * **Consistencia en la edición** : mantiene estables los rasgos distintivos de personas y productos cuando cambias el fondo, la ropa o el estilo
  * **Hasta 5 imágenes de referencia** : combina varias imágenes en una sola edición y haz referencia a cada una en el prompt
  * **Salida de hasta 4K** : genera hasta 2K de forma nativa y aplica upscale a la salida de 4K a partir de un render de 2K



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

Flujo de trabajo de texto a imagen de Tencent HY Image 3.5 Preview

Genera una imagen a partir de un prompt de texto. El modelo reescribe y expande el prompt antes de renderizar, así que los prompts cortos funcionan.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY Image 3.5” en la biblioteca de plantillas

![Póster con el texto HY Image 3.5 Preview en mayúsculas blancas sobre una forma brillante de metal líquido con reflejos iridiscentes sobre un fondo oscuro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_tencent_hy_image_3_5_preview_t2i.png)

### 

​

Pasos para ejecutar el flujo de trabajo

  1. Edita el `prompt` en el nodo `Tencent HY Image: Text to Image`
  2. (Opcional) Configura `aspect_ratio` para controlar la forma de la salida. Con `auto` el modelo elige la relación de aspecto a partir del prompt, y `auto` no está disponible en 4K
  3. (Opcional) Cambia `resolution` respecto al valor predeterminado `2K`. `1K` equivale a unos 1024x1024 y `2K` a unos 2048x2048 píxeles. La salida `4K` se renderiza a 2K y luego el modelo aplica upscale
  4. (Opcional) Cambia `resolution` a `custom` para establecer un `width` y un `height` exactos. Ambos deben ser múltiplos de 16 y el área total puede llegar hasta 4096x4096. Por encima de una relación de aproximadamente 6:1 el modelo empieza a repetir el sujeto
  5. Haz clic en `Run` o presiona `Ctrl(cmd) + Enter` para generar la imagen
  6. Consulta el resultado en el nodo `Save Image`



## 

​

Flujo de trabajo de edición de imagen con Tencent HY Image 3.5 Preview

Edita o combina hasta cinco imágenes de referencia a partir de una instrucción de texto. Úsalo para cambiar un fondo, cambiar la ropa, cambiar el estilo de una foto de producto o fusionar varias referencias en una sola imagen sin perder los rasgos que definen al sujeto. ![Ejemplo de salida de edición de imagen con Tencent HY Image 3.5 Preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy_image_3_5_preview_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HY Image 3.5” en la Biblioteca de plantillas

![Motocicleta conceptual angular de color negro mate sobre un soporte de boxes naranja con un fondo rojo intenso](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/futuristic_brutalist_motorcycle.png)

### 

​

Pasos para ejecutar el flujo de trabajo

  1. Sube la imagen de ejemplo al nodo `Load Image` que ya está conectado al nodo `Tencent HY Image: Edit`. El flujo de trabajo descargado hace referencia al archivo por su nombre (`futuristic_brutalist_motorcycle.png`), así que ese nodo permanece vacío hasta que la subas. Si prefieres editar tus propias imágenes, conecta de 1 a 5 imágenes a la entrada `images` del nodo `Tencent HY Image: Edit`
  2. Escribe la instrucción de edición en `prompt`. Haz referencia a las entradas en orden como `@Image1`, `@Image2`, etcétera. Una entrada por lotes cuenta una vez por cada imagen
  3. (Opcional) Configura `aspect_ratio` y `resolution`. Con `auto`, la salida sigue la relación de aspecto de la primera imagen de referencia. La salida `4K` se renderiza a 2K y después el modelo aplica upscale
  4. (Opcional) Configura `reference_detail` en `high` para que el modelo vea las referencias a hasta 2048x2048 píxeles en lugar de 1024x1024. Esto conserva mejor el texto pequeño y los detalles finos, pero tarda más
  5. Haz clic en `Run` o pulsa `Ctrl(cmd) + Enter` para generar la imagen
  6. Consulta el resultado en el nodo `Save Image`



### 

​

Consejos para el prompt

  * Describe por separado la edición y las partes que deben permanecer sin cambios, por ejemplo `@Image1 change the background to a night market, keep the subject and jacket unchanged`
  * Numera las referencias en el orden en que están conectadas. La numeración del prompt debe coincidir con el orden de las entradas
  * `watermark` está en las opciones avanzadas del nodo y viene desactivado de forma predeterminada. Actívalo para añadir al resultado una marca de agua generada por IA



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión, o usa [Comfy Cloud](https://cloud.comfy.org/?utm_source=docs&utm_medium=referral&utm_campaign=hy-image-3-5)
  2. Ve a la Biblioteca de plantillas y busca `HY Image 3.5`
  3. Abre el flujo de trabajo de Texto a imagen o de edición de imagen y ejecútalo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/tencent/hy-image-3-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/tencent/hy-image-3-5)

[Generación de imágenes](https://docs.comfy.org/es/tutorials/partner-nodes/runway/image-generation)[Topaz Labs](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/overview)
