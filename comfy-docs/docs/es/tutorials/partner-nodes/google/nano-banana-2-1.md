---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-1/
title: Nano Banana 2.1: generaci\u00f3n y edici\u00f3n de im\u00e1genes con IA en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.777938+00:00
---

# Nano Banana 2.1: generación y edición de imágenes con IA en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-1/

## En esta página

Volver arriba

  * En qué destaca Nano Banana 2.1
  * Salidas de ejemplo
  * Usarlo
  * Flujos de trabajo
    * Texto a imagen
    * Edición de imagen
  * Configuraciones que importan
  * ¿Qué modelo deberías elegir?
  * Empezar



Google

# Nano Banana 2.1: generación y edición de imágenes con IA en ComfyUI

Copiar páginaCopiar página

Genera y edita imágenes con Nano Banana 2.1 en ComfyUI: salida de 1K a 4K, tres niveles de razonamiento y hasta 14 imágenes de referencia

Copiar páginaCopiar página

Nano Banana 2.1 (`gemini-nano-banana-2.1`) está disponible en ComfyUI a través de los Nodos asociados. Un solo nodo cubre tanto la generación de texto a imagen como la edición de imágenes: comienza con un prompt o conecta imágenes de referencia y describe el cambio que quieres hacer.

## 

​

En qué destaca Nano Banana 2.1

  * **Generación y edición en un solo nodo** : un mismo nodo se encarga de texto a imagen y de la edición de imágenes, así puedes iterar sobre un resultado sin reconstruir el flujo de trabajo
  * **Salida en 1K, 2K y 4K** : elige la resolución que se ajuste a la tarea, desde borradores rápidos hasta imágenes grandes y detalladas
  * **Nivel de razonamiento ajustable** : `MINIMAL`, `MEDIUM` y `HIGH` controlan cuánto razona el modelo antes de dibujar. Nano Banana 2.1 empieza en `MEDIUM`, mientras que los otros dos modelos empiezan en `MINIMAL`
  * **Hasta 14 imágenes de referencia** : conecta varias imágenes en una sola llamada para guiar el sujeto, el estilo o la composición
  * **Cambio de modelo sin recablear** : el menú desplegable de modelo también ejecuta Nano Banana 2 y Nano Banana 2 Lite en el mismo nodo



## 

​

Salidas de ejemplo

Texto a imagen, usando el prompt predeterminado del flujo de trabajo: ![Póster con la tipografía NANO BANANA 2.1 en blanco de gran tamaño sobre un plátano amarillo envuelto en anillos de vidrio translúcido sobre un fondo negro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_1_t2i.png) Edición de imagen, a partir de una imagen de entrada más la instrucción “Cambia el fondo a oscuro y vuelve a iluminar este retrato con una luz azul dramática desde el frente y una cálida luz de contorno ámbar desde atrás”:

![Retrato de perfil de un hombre con barba que lleva gafas de sol envolventes plateadas y una cadena plateada, sobre un cielo gris pálido](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/silver_frame_profile.png)![El mismo retrato sobre un fondo oscuro, iluminado por una cálida luz de contorno ámbar desde atrás y una luz azul fría desde el frente](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_1_image_edit.png)

## 

​

Usarlo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Se ejecuta con la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI, más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujos de trabajo

### 

​

Texto a imagen

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana 2.1” en la Biblioteca de plantillas

Escribe la descripción de la imagen que quieres y ejecuta el flujo de trabajo. No necesitas archivos de entrada: el prompt es la única entrada, `aspect_ratio` decide la forma (consulta más abajo) y el resultado se guarda como un PNG.

### 

​

Edición de imagen

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana 2.1” en la Biblioteca de plantillas

## Descargar imagen de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo

Carga una imagen en el nodo `Load Image` y describe la edición en el prompt. El flujo de trabajo conecta la imagen a la entrada de referencia del modelo y añade un nodo `Image Compare`, para que puedas comparar el original con el resultado en el mismo lienzo.

## 

​

Configuraciones que importan

Configuración| Qué hace  
---|---  
`aspect_ratio`| `auto` coincide con la relación de aspecto de la primera imagen de referencia y, si no hay imagen de referencia, normalmente devuelve una imagen de 16:9. Los demás valores son relaciones fijas: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `8:1`, `1:8`  
`resolution`| Salida en `1K`, `2K` o `4K`. Las resoluciones más altas cuestan más por imagen  
`thinking_level`| `MINIMAL` es la más rápida y no añade costo de razonamiento; `MEDIUM` y `HIGH` dedican más tiempo y créditos al razonamiento del modelo antes de dibujar. Nano Banana 2.1 comienza en `MEDIUM`  
`response_modalities`| `IMAGE` devuelve la imagen. `IMAGE+TEXT` también devuelve el texto del modelo, que aparece en las salidas `text` y `thought_image`  
`seed`| Fija un valor para que las ejecuciones repetidas sean lo más parecidas posible dentro de lo que permite el modelo  
  
El nodo expone `temperature` y `top_p`, pero Nano Banana 2.1 no las envía. Se aplican cuando cambias el menú desplegable del modelo a Nano Banana 2 o Nano Banana 2 Lite.

## 

​

¿Qué modelo deberías elegir?

Modelo| Resoluciones de salida| Niveles de razonamiento| Ideal para  
---|---|---|---  
**Nano Banana 2.1**|  1K, 2K, 4K| MINIMAL, MEDIUM, HIGH| Edición y generación donde importan la composición y el detalle  
**[Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2)**|  1K, 2K, 4K| MINIMAL, HIGH| Calidad y velocidad equilibradas en tamaños mayores  
**[Nano Banana 2 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite)**|  1K| MINIMAL, HIGH| La opción más rápida y económica para borradores y ejecuciones de gran volumen  
  
## 

​

Empezar

  1. Actualiza ComfyUI a la versión 0.39.1 o posterior: los flujos de trabajo usan el nodo `Nano Banana 2.1`
  2. Haz doble clic en el lienzo y busca “Nano Banana 2.1”, o abre la Biblioteca de plantillas y elige Texto a imagen o Edición de imagen
  3. Ingresa un prompt. Para editar, primero carga una imagen en el nodo `Load Image`
  4. Elige la resolución y el nivel de razonamiento, y luego ejecuta el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/nano-banana-2-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/nano-banana-2-1)

[Crystal Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-upscale)[Nano Banana Pro](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-pro)
