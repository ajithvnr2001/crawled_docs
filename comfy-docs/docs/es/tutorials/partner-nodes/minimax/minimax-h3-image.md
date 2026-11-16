---
url: https://docs.comfy.org/es/tutorials/partner-nodes/minimax/minimax-h3-image/
title: MiniMax H3 Image API: Texto a imagen y edici\u00f3n de im\u00e1genes en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:58.323550+00:00
---

# MiniMax H3 Image API: Texto a imagen y edición de imágenes en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/minimax/minimax-h3-image/

## En esta página

Volver arriba

  * En qué destaca MiniMax H3 Image
  * Texto a imagen
  * Editar imagen
  * Opciones
  * Empezar



MiniMax

# MiniMax H3 Image API: Texto a imagen y edición de imágenes en ComfyUI

Copiar páginaCopiar página

Genera imágenes 2K o 4K desde un prompt o edita hasta 16 imágenes de referencia con MiniMax H3 Image mediante la API de socios de ComfyUI.

Copiar páginaCopiar página

MiniMax H3 Image es el modelo de imagen de MiniMax, disponible en ComfyUI a través del nodo de socio **MiniMax H3 Image**. Texto a imagen y la edición de imágenes usan el mismo nodo: sin imágenes de referencia conectadas, genera a partir de tu prompt, y con referencias conectadas, las edita o las combina. Los flujos de trabajo se ejecutan en los servidores de MiniMax a través de tu cuenta de Comfy API, así que no hay descargas de modelos ni una GPU local que administrar.

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

## En qué destaca MiniMax H3 Image

  * **Salida en 2K y 4K** : elige un nivel de tamaño y una relación de aspecto, o define un ancho y un alto exactos
  * **Edición de imágenes** : edita o combina hasta 16 imágenes de referencia, a las que haces referencia en el prompt como `@Image1` a `@Image16`
  * **Reescritura de prompts** : de forma predeterminada, MiniMax amplía un prompt corto hasta convertirlo en una descripción detallada de la escena y devuelve el prompt reescrito junto con la imagen
  * **Detalle de nivel de cartel** : adecuado para carteles, embalajes e imágenes editoriales que necesitan texto legible y detalle denso



## Texto a imagen

Genera una imagen a partir de un prompt en 2K o 4K. ![Vista previa del flujo de trabajo de texto a imagen de MiniMax H3 Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax-H3-Image: Text to Image (API)” en la Biblioteca de plantillas

## Editar imagen

Conecta una imagen de origen, describe el cambio y solo se reescribe lo que pide el prompt. La plantilla agrega una mujer a un render finalizado y conserva el resto del encuadre. ![Vista previa del flujo de trabajo de edición de imágenes de MiniMax H3 Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_minimax_h3_image_image_edit-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax-H3-Image: Image Edit (API)” en la Biblioteca de plantillas

**Materiales de entrada**

## surreal_rendering_modern.png

`LoadImage` · `surreal_rendering_modern.png`

## Opciones

Entrada| Valores| Notas  
---|---|---  
`model`| `MiniMax-H3-Image`, `MiniMax-H3-Image-Highspeed`| En la plantilla, cambia el menú desplegable `model` para cambiar de modelo  
`size`| `2K`, `4K`, `custom`| 2K y 4K derivan el ancho y el alto de la relación de aspecto. `custom` toma un ancho y un alto de 512 a 7680 px cada uno, con 655,360 a 20,000,000 px en total y una relación de aspecto de 3:1 como máximo  
`aspect_ratio`| `auto` más 15 relaciones fijas| `auto` sigue el prompt, o la imagen de referencia cuando hay una conectada  
`enhance_prompt`| activado de forma predeterminada| MiniMax reescribe primero el prompt como una descripción detallada de la escena. Las ediciones siempre se mejoran, así que desactivarlo solo afecta a Texto a imagen, que entonces necesita una relación fija o un tamaño personalizado  
`images`| hasta 16| Imágenes de referencia para editar y combinar. Menciónalas en el prompt como `@Image1`, `@Image2`, etc., en el orden de conexión  
  
Los prompts pueden tener hasta 8,000 caracteres cuando hay imágenes de referencia conectadas. El nodo también devuelve el `revised_prompt` reescrito junto a la imagen.

## Empezar

  1. Actualiza ComfyUI a 0.45.1 o posterior
  2. En la biblioteca de plantillas, busca `MiniMax-H3-Image`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/minimax/minimax-h3-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/minimax/minimax-h3-image)

[Muse Image](https://docs.comfy.org/es/tutorials/partner-nodes/meta/muse-image)[GPT Image 2.6](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-image-2-6)
