---
url: https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-t2-5/
title: Meshy T2.5 en ComfyUI: 3D listo para juegos dentro de un presupuesto de tri\u00e1ngulos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:52.487731+00:00
---

# Meshy T2.5 en ComfyUI: 3D listo para juegos dentro de un presupuesto de triángulos - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-t2-5/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Text to Model (Smart Topology)
    * Image to Model (Smart Topology)
  * Controles del nodo
  * Consejos para los prompts
  * Empezar



Meshy

# Meshy T2.5 en ComfyUI: 3D listo para juegos dentro de un presupuesto de triángulos

Copiar páginaCopiar página

Genera mallas 3D listas para juegos con Meshy T2.5 en ComfyUI: texto e imagen a modelo con el presupuesto de triángulos que definas y texturas PBR opcionales.

Copiar páginaCopiar página

**Meshy T2.5** construye una malla 3D directamente con la cantidad de triángulos que pides. Los pipelines anteriores generan una malla densa y la retopologizan después, lo que pierde detalle y exige limpieza antes de que el recurso pueda entregarse. T2.5 apunta al presupuesto desde el inicio, así que un objeto de 15000 triángulos vuelve con aproximadamente 15000 triángulos y entra directamente en un motor. ComfyUI lo expone mediante dos nodos asociados: **Meshy: Text to Model (Smart Topology)** y **Meshy: Image to Model (Smart Topology)**. Ambos son nodos API en la nube que requieren una cuenta de Comfy con créditos y no descargan archivos de modelo de forma local. Cada uno devuelve un archivo GLB y un archivo FBX, y las plantillas escriben el GLB con un nodo Save GLB. T2.5 es el modo para objetos, decoración de entornos y recursos de juego low-poly donde importa una cantidad de triángulos predecible. Para rigging, animación y el pipeline completo de recursos, usa [Meshy 7](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-7) en su lugar.

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

Flujos de trabajo disponibles

### 

​

Text to Model (Smart Topology)

Describe el objeto y la malla se construye con el presupuesto que definas. No se necesitan archivos de entrada. ![Vista previa del flujo de trabajo Meshy T2.5: Text to Model](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_t2m-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Meshy T2.5: Text to Model (Smart Topology)” en la Biblioteca de plantillas

**Prompts de ejemplo**

  * `A weathered wooden treasure chest with iron banding, a rounded lid and a rusted lock plate, standing open with a few gold coins inside, standalone game prop, clean silhouette`
  * `Low-poly stone lantern covered in moss, chipped edges, wide base, neutral studio lighting`
  * `Sci-fi crate with recessed panel lines and a lit status strip, boxy silhouette, no text`



### 

​

Image to Model (Smart Topology)

Convierte una sola imagen en una malla lista para el motor. El texturizado es opcional y puede ejecutarse con mapas PBR en 2k, 4k u 8k. ![Vista previa del flujo de trabajo Meshy T2.5: Image to Model](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_i2m-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Meshy T2.5: Image to Model (Smart Topology)” en la Biblioteca de plantillas

**Material de entrada**

## abstract_3d_toy_van_game_asset.png

Cárgalo en el nodo `LoadImage`

`texture_prompt` y `texture_image` no se pueden usar juntos: guía el texturizado con uno u otro, o deja ambos vacíos y deja que la imagen de origen lo dirija.

## 

​

Controles del nodo

Control| Valores| Se aplica a| Efecto  
---|---|---|---  
`model`| `meshy-t2.5`| ambos nodos| La versión del modelo Smart Topology  
`prompt`| texto, hasta 800 caracteres| Text to Model| Descripción del objeto que se va a construir  
`image`| una imagen| Image to Model| La imagen fuente de la que se construye la malla  
`target_polycount`| 100 a 30000, predeterminado 15000| ambos nodos| Cantidad aproximada de triángulos del resultado  
`pose_mode`| vacío, `A-pose`, `T-pose`| ambos nodos| Fija la postura de un personaje. Déjalo vacío para objetos  
`should_texture`| `true`, `false`| Image to Model| Indica si se debe texturizar la malla después de generarla  
`enable_pbr`| desactivado de forma predeterminada| Image to Model, texturizado activado| Añade mapas de metalicidad, rugosidad y normales al color base  
`texture_prompt`| texto, hasta 800 caracteres| Image to Model, texturizado activado| Orientación mediante texto para la textura. No se puede combinar con `texture_image`  
`texture_image`| una imagen| Image to Model, texturizado activado| Orientación mediante imagen para la textura. No se puede combinar con `texture_prompt`  
`texture_resolution`| `2k`, `4k`, `8k`| Image to Model, texturizado activado| Resolución de las texturas generadas  
`seed`| entero| ambos nodos| Controla si el nodo se vuelve a ejecutar. La salida de Meshy no es determinista, independientemente de la semilla  
  
Las salidas del nodo son `meshy_task_id`, `GLB` y `FBX`. Save GLB escribe el archivo desde la salida `GLB`, no desde el id de tarea ni desde la salida FBX.

## 

​

Consejos para los prompts

  * **Nombra el objeto y la silueta.** `Standalone game prop, clean silhouette, no text` evita que el modelo añada una escena, una base o un texto que luego tengas que eliminar.
  * **Define el presupuesto antes de generar.** Cambiar `target_polycount` después implica una nueva generación, así que decide primero si el recurso es una pieza protagonista o un elemento de fondo.
  * **Describe el material, no los esquemas de iluminación.** Palabras de superficie como `weathered wood, iron banding, rusted lock plate` se conservan en la malla y la textura. Las palabras de iluminación de estudio solo afectan a cómo se ve la vista previa.
  * **Usa`pose_mode` solo para personajes.** La pose A o la pose T ofrecen una postura apta para el rig. Para los objetos, es mejor dejarlo vacío.
  * **Texturiza cuando la forma sea correcta.** Ejecuta una vez sin texturizado, revisa la silueta y luego activa `should_texture` para la pasada final.
  * **No esperes obtener la misma malla dos veces.** La semilla solo decide si el nodo se vuelve a ejecutar, así que una nueva ejecución da un resultado nuevo.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Meshy T2.5`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/meshy/meshy-t2-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/meshy/meshy-t2-5)

[Hunyuan3D 3 0](https://docs.comfy.org/es/tutorials/partner-nodes/hunyuan3d/hunyuan3d-3-0)[Meshy 7](https://docs.comfy.org/es/tutorials/partner-nodes/meshy/meshy-7)
