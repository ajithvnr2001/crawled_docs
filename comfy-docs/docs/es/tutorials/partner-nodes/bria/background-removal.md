---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bria/background-removal/
title: Eliminaci\u00f3n de fondo de Bria en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.381803+00:00
---

# Eliminación de fondo de Bria en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bria/background-removal/

## En esta página

Volver arriba

  * En qué destaca Bria Background Removal
  * Salidas de ejemplo
    * Bria: Remove Image Background
    * Bria: Guided Remove Background
  * Procesamiento de fondos de video
    * Bria: Eliminar fondo de video
    * Bria: Eliminar fondo de video (transparente)
    * Bria: Pantalla verde de video
    * Bria: Reemplazar el fondo de un video



Bria

# Eliminación de fondo de Bria en ComfyUI

Copiar páginaCopiar página

Aprende a usar los Nodos asociados de Bria en ComfyUI para eliminar el fondo de imágenes y videos, usar pantalla verde y reemplazar fondos.

Copiar páginaCopiar página

Los modelos de procesamiento de fondo con IA de Bria ya están disponibles en ComfyUI mediante los Nodos asociados. Esta página cubre la **eliminación de fondo de imagen** , la **eliminación de fondo de imagen guiada** , la **eliminación de fondo de video** , el **fondo transparente de video** , la **pantalla verde de video** y el **reemplazo de fondo de video**.

## 

​

En qué destaca Bria Background Removal

  * **Eliminación de fondo de imágenes** : Elimina automáticamente el fondo de una imagen y devuelve el resultado con un fondo transparente.
  * **Eliminación de fondo de imágenes guiada** : Conserva el sujeto que describe un prompt y elimina el resto, de modo que puedes recortar un solo sujeto de una escena recargada en lugar de conservar todo lo que no sea fondo.
  * **Eliminación de fondo de video** : Reemplaza el fondo de un video con un color sólido de tu elección u obtiene el video con transparencia.
  * **Pantalla verde para video** : Aplica un efecto profesional de pantalla verde o azul tipo chroma key, con presets como broadcast_green, chroma_green y blue_screen.
  * **Reemplazo de fondo de video** : Reemplaza el fondo de un video con una imagen personalizada u otro video.
  * **Soporte para videos cortos** : El procesamiento de fondo de video acepta videos de entrada de hasta 60 segundos.



## 

​

Salidas de ejemplo

Eliminación de fondo de imagen, devolviendo el sujeto sobre un fondo transparente: ![Bria: Remove Image Background, salida de ejemplo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_bria_remove_image_background.png)

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

Bria: Remove Image Background

Sube una imagen para eliminar su fondo automáticamente usando la API de Bria. El resultado se devuelve como una imagen con fondo transparente. ![Vista previa del flujo de trabajo Bria: Remove Image Background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_remove_image_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Remove Image Background” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## denim_girl.png

nodo `LoadImage` 26 · `denim_girl.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/denim_girl.png)![Bria: Remove Image Background, salida de ejemplo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/utility_bria_remove_image_background.png)

### 

​

Bria: Guided Remove Background

Elimina el fondo de una imagen y conserva lo que describe un prompt. En lugar de conservar todo lo que no es fondo, el nodo reduce el recorte al sujeto que indiques, y así una persona u objeto sale intacto de una escena con mucho contenido. Los píxeles originales vuelven a resolución completa con un nuevo canal alfa. ![Vista previa del flujo de trabajo Bria: Guided Remove Background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_guided_remove_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Guided Background Removal” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## bria_guided_person.png

Cárgalo en el nodo `LoadImage`

El `prompt` nombra lo que se conserva, por ejemplo `the man in the blue shirt` o `only the shoes`. Un prompt que no coincide con nada devuelve una imagen totalmente transparente. Con `moderation` activado aparecen controles separados de entrada y salida visual; desactivado, se omiten. Para un recorte simple sin orientación, usa **Bria: Remove Image Background** arriba.

## 

​

Procesamiento de fondos de video

Los nodos de procesamiento de fondos de video de Bria te permiten eliminar, reemplazar o aplicar efectos de chroma key a los fondos de video. El video de entrada debe durar 60 segundos o menos.

### 

​

Bria: Eliminar fondo de video

Reemplaza el fondo de un video con un color sólido de tu elección. ![Vista previa del flujo de trabajo Bria: Eliminar fondo de video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Remove Video Background” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo` correspondiente:

## spear_warrior.mp4

nodo `LoadVideo` 4 · `spear_warrior.mp4`

### 

​

Bria: Eliminar fondo de video (transparente)

Elimina el fondo de un video y obtén una salida con transparencia. ![Vista previa del flujo de trabajo Bria: Eliminar fondo de video \(transparente\)](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_remove_video_background_transparent-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Remove Video Background (Transparent)” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo` correspondiente:

## ad_video_demo.mp4

nodo `LoadVideo` 5 · `ad_video_demo.mp4`

### 

​

Bria: Pantalla verde de video

Aplica a tu video un efecto profesional de pantalla verde o azul para chroma key, con varias opciones predefinidas como broadcast_green, chroma_green y blue_screen. ![Vista previa del flujo de trabajo Bria: Pantalla verde de video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_green_screen-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Video Green Screen” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadVideo` correspondiente:

## investigator.mp4

nodo `LoadVideo` 5 · `investigator.mp4`

### 

​

Bria: Reemplazar el fondo de un video

Reemplaza el fondo de un video con una imagen personalizada o con otro video. ![Vista previa del flujo de trabajo Bria: Reemplazar el fondo de un video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_video_replace_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bria: Video Replace Background” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadVideo` y `LoadImage` correspondientes:

## stained_window_vintage_woman.mp4

nodo `LoadVideo` 4 · `stained_window_vintage_woman.mp4`

## gothic_hall_light_rays.png

nodo `LoadImage` 8 · `gothic_hall_light_rays.png`

![gothic_hall_light_rays.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/gothic_hall_light_rays.png)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bria/background-removal.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bria/background-removal)

[Edición de imágenes](https://docs.comfy.org/es/tutorials/partner-nodes/bria/image-editing)[FIBO 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo)
