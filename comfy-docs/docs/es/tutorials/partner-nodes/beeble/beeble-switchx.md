---
url: https://docs.comfy.org/es/tutorials/partner-nodes/beeble/beeble-switchx/
title: Beeble SwitchX en ComfyUI: cambio de iluminaci\u00f3n y edici\u00f3n de entorno - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.619728+00:00
---

# Beeble SwitchX en ComfyUI: cambio de iluminación y edición de entorno - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/beeble/beeble-switchx/

## En esta página

Volver arriba

  * En qué destaca Beeble SwitchX
  * Beeble SwitchX: edición de imagen
    * Cómo funciona
    * Pasos para ejecutar
    * Parámetros del nodo
  * Beeble SwitchX: Edición de video
    * Cómo funciona
    * Pasos para ejecutar
    * Salidas



Beeble

# Beeble SwitchX en ComfyUI: cambio de iluminación y edición de entorno

Copiar páginaCopiar página

Cambia la iluminación de imágenes y videos con Beeble SwitchX en ComfyUI: reemplaza fondos, integra un sujeto en otra escena y exporta recortes o mattes alfa.

Copiar páginaCopiar página

Los [Nodos asociados de Beeble SwitchX](https://docs.comfy.org/es/built-in-nodes/BeebleSwitchXImageEdit) te permiten transformar el entorno, la iluminación y el estilo de imágenes y videos existentes mientras conservas el sujeto original. Sube una imagen de un personaje o sujeto junto con un entorno de referencia, y SwitchX compone tu sujeto en la nueva escena con iluminación y sombras realistas.

## 

​

En qué destaca Beeble SwitchX

  * **Reemplazo de entorno** : reemplaza el entorno de fondo de una imagen o un video con una escena de referencia mientras conserva el sujeto original
  * **Reiluminación realista** : integra el sujeto en el nuevo entorno con iluminación, sombras y perspectiva adecuadas
  * **Edición de video conservando el movimiento** : aplica reiluminación a las regiones enmascaradas del sujeto en un video, mientras que las áreas no enmascaradas conservan los píxeles y el movimiento originales
  * **Salidas listas para composición** : el flujo de trabajo de imagen guarda un recorte enmascarado y el flujo de trabajo de video genera una máscara alfa independiente para facilitar la composición



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

Beeble SwitchX: edición de imagen

Sustituye el entorno del fondo y vuelve a iluminar a tu sujeto con una imagen de referencia. ![Beeble SwitchX Image Edit Workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Beeble SwitchX: Image Edit” en la biblioteca de plantillas

### 

​

Cómo funciona

Este flujo de trabajo recibe dos imágenes de entrada:

  * **Imagen del sujeto** : tu personaje o sujeto principal (con fondo)
  * **Entorno de referencia** : la nueva escena, iluminación o estilo que quieres aplicar

El nodo genera un resultado en el que el sujeto se integra de forma natural en el nuevo entorno con la iluminación, las sombras y la perspectiva adecuadas.

### 

​

Pasos para ejecutar

  1. **Sube la imagen del sujeto** : usa el primer nodo **LoadImage** para cargar la imagen de tu sujeto (por ejemplo, una persona con auriculares)
  2. **Sube la imagen de referencia** : usa el segundo nodo **LoadImage** para cargar el entorno o estilo objetivo
  3. **Introduce tu prompt** : describe la escena en el nodo **BeebleSwitchXImageEdit**
  4. **Establece la resolución** : elige la resolución de salida
  5. **Ajusta la semilla** : modifica la semilla para obtener resultados distintos
  6. **Haz clic en Queue** : pulsa `Ctrl+Enter` para generar
  7. **Consulta los resultados** : la imagen editada aparece en **SaveImage** , y el recorte con máscara se guarda por separado



### 

​

Parámetros del nodo

Parámetro| Descripción  
---|---  
`prompt`| Descripción de la escena y el entorno  
`resolution`| Resolución de salida (p. ej., 720p)  
`seed`| Semilla aleatoria para obtener resultados reproducibles  
  
## 

​

Beeble SwitchX: Edición de video

Aplica una nueva iluminación de entorno a un video mientras conservas el movimiento original y las regiones sin máscara. ![Flujo de trabajo de Beeble SwitchX Edición de video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_beeble_switchx_video_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Beeble SwitchX: Video Edit” en la Biblioteca de plantillas

### 

​

Cómo funciona

Este flujo de trabajo toma un video de origen y una imagen de referencia, y luego aplica la iluminación y el entorno de referencia a las regiones del sujeto enmascaradas en el video. Las áreas sin máscara conservan los píxeles y el movimiento originales. El flujo de trabajo también genera una máscara alfa para facilitar la composición.

### 

​

Pasos para ejecutar

  1. **Sube el video de origen** : usa el nodo **LoadVideo** para cargar tu video de entrada
  2. **Sube la imagen de referencia** : usa el nodo **LoadImage** para cargar el entorno o estilo objetivo
  3. **Establece el alcance del video** : el nodo **Video Slice** controla qué fotogramas se procesan (inicio, fin, inclusivo)
  4. **Introduce tu prompt** : describe el entorno y la iluminación deseados en el nodo **BeebleSwitchXVideoEdit**
  5. **Establece la resolución** : elige la resolución de salida
  6. **Ajusta la semilla** : modifica la semilla para obtener resultados diferentes
  7. **Haz clic en Queue** : presiona `Ctrl+Enter`
  8. **Consulta los resultados** : el video editado se guarda y se genera un video de máscara alfa aparte para la composición



### 

​

Salidas

Salida| Descripción  
---|---  
**Video editado** (`SaveVideo`)| El video final con el nuevo entorno e iluminación aplicados a las regiones enmascaradas  
**Máscara alfa** (`SaveVideo`)| Un video alfa aparte para componer las regiones editadas  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/beeble/beeble-switchx.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/beeble/beeble-switchx)

[FLUX 1 Kontext](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)[Product Holding y Try-On](https://docs.comfy.org/es/tutorials/partner-nodes/bria/product-compositing)
