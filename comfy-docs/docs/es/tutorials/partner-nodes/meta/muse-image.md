---
url: https://docs.comfy.org/es/tutorials/partner-nodes/meta/muse-image/
title: Meta Muse Image en ComfyUI: texto a imagen y edici\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.500967+00:00
---

# Meta Muse Image en ComfyUI: texto a imagen y edición de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/meta/muse-image/

## En esta página

Volver arriba

  * En qué destaca Meta Muse Image
  * Salidas de ejemplo
  * Flujo de trabajo de texto a imagen de Meta Muse Image
  * Flujo de trabajo de edición de imágenes de Meta Muse Image
    * Archivos de entrada
  * Empezar
    * Consejos para prompts
  * Precios



Meta

# Meta Muse Image en ComfyUI: texto a imagen y edición de imágenes

Copiar páginaCopiar página

Usa Muse Image 1.0 de Meta en ComfyUI: texto a imagen con búsqueda web integrada y edición por instrucciones con hasta 10 imágenes de referencia.

Copiar páginaCopiar página

Meta Muse Image 1.0 es el primer modelo de generación de imágenes de Meta Superintelligence Labs, anunciado el 7 de julio de 2026. Genera imágenes de aproximadamente 2.5 megapíxeles y destaca por su enfoque agéntico: antes de renderizar, el modelo puede buscar datos en la web, buscar imágenes de referencia e incluso ejecutar código para lograr cantidades, diseños, gráficos y diagramas precisos. ComfyUI expone Muse Image mediante dos Nodos asociados: Meta Muse Image Text to Image para la generación y Meta Muse Image Edit para la edición basada en instrucciones y la combinación.

## 

​

En qué destaca Meta Muse Image

  * **Renderizado agéntico** : El modelo planifica antes de dibujar, con búsqueda web, búsqueda de imágenes y ejecución de código integradas (las tres opciones están activadas por defecto en las opciones avanzadas del nodo)
  * **Cantidades y disposiciones precisas** : Los pósters con mucho texto, las gráficas, los diagramas y las disposiciones se benefician de la ruta de ejecución de código; si la desactivas, se recurre a una aproximación
  * **Edición con múltiples referencias** : El nodo Edit acepta de 1 a 10 imágenes de referencia. Haz referencia a ellas en el prompt como `@Image1`, `@Image2`, etc., numeradas en el orden de entrada
  * **Encuadre flexible** : 14 relaciones de aspecto desde 1:1 hasta 21:9 y 9:21, además de `auto`, que permite que el modelo elija a partir del prompt (generación) o mantiene la relación de la entrada (edición)
  * **Control de razonamiento** : Elige la intensidad de razonamiento `high` o `low` según cuánta planificación necesite la imagen



## 

​

Salidas de ejemplo

Generación de texto a imagen a partir de un solo prompt: ![Salida de Muse Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/muse_image_1.0.png)

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

Flujo de trabajo de texto a imagen de Meta Muse Image

Genera una imagen a partir de una descripción de texto con el modelo Muse Image 1.0 de Meta. Acepta un prompt de texto y produce una imagen. ![Vista previa del flujo de trabajo Texto a imagen de Meta Muse Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Muse Image” en la Biblioteca de plantillas

![Salida de texto a imagen de Muse Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/muse_image_1.0.png)

## 

​

Flujo de trabajo de edición de imágenes de Meta Muse Image

Edita o combina hasta 10 imágenes de referencia guiadas por un prompt de texto. Las imágenes de referencia se conectan a las entradas `image_1` a `image_10`, y el prompt se refiere a cada una como `@Image1`, `@Image2`, etc., numeradas en el orden de las entradas. Una entrada por lotes cuenta una sola vez por imagen. ![Vista previa del flujo de trabajo de edición de imágenes Meta Muse](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meta_muse_image_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Muse Image” en la Biblioteca de plantillas

### 

​

Archivos de entrada

## Figura de ballena

deep_blue_whale_swim_scene.png

## Casa moderna

desert_red_modern_house.png

El flujo de trabajo de ejemplo combina las dos entradas con el prompt: “Usa la figura de ballena de @image1 y haz que recorra el cielo sobre la imagen de @image2”. ![Resultado de la edición de imágenes Meta Muse Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_meta_muse_image_image_edit.png)

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a Biblioteca de plantillas y busca `Muse Image`



### 

​

Consejos para prompts

  * Sé explícito sobre qué debe mantenerse preciso: Muse Image sigue las instrucciones al pie de la letra, así que indica directamente en el prompt los recuentos, las posiciones y las etiquetas
  * Para pósters y diagramas, mantén activado el interruptor de ejecución de código (opciones avanzadas) para calcular las cantidades y la alineación en lugar de aproximarlas
  * En el flujo de trabajo Edit, nombra cada referencia que conectes. Una etiqueta `@Image` sin una entrada conectada hace que la ejecución falle
  * Usa la relación de aspecto `auto` cuando quieras que el modelo decida el encuadre a partir del prompt; usa una relación fija para obtener resultados consistentes en una serie



## 

​

Precios

Nodo| Créditos  
---|---  
Meta Muse Image Text to Image| 3.017 / imagen  
Meta Muse Image Edit| 3.017 / imagen  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/meta/muse-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/meta/muse-image)

[Magnific Creative Tools](https://docs.comfy.org/es/tutorials/partner-nodes/magnific/magnific-creative-tools)[GPT Image 2.5](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-5)
