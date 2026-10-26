---
url: https://docs.comfy.org/es/tutorials/utility/remove-background-birefnet/
title: BiRefNet: eliminar el fondo de una imagen en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.252568+00:00
---

# BiRefNet: eliminar el fondo de una imagen en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/remove-background-birefnet/

## En esta página

Volver arriba

  * Principales ventajas
  * Flujo de trabajo de eliminación de fondo con BiRefNet
    * 1\. Descargar el flujo de trabajo
    * BiRefNet: Remove Background
    * 2\. Descargar los modelos
    * 3\. Usar el flujo de trabajo
  * Notas adicionales



Segmentation & Background

# BiRefNet: eliminar el fondo de una imagen en ComfyUI

Copiar páginaCopiar página

Aprende a eliminar el fondo de una imagen con el modelo BiRefNet, compatible de forma nativa con ComfyUI

Copiar páginaCopiar página

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

BiRefNet (Bilateral Reference Network) es un modelo de eliminación de fondo de imágenes de alta calidad. Produce máscaras limpias y detalladas para una amplia variedad de sujetos, incluidas personas, productos, animales y objetos complejos con detalles finos como cabello o pelaje. BiRefNet es compatible de forma nativa con ComfyUI (PR [#12747](https://github.com/Comfy-Org/ComfyUI/pull/12747)). Los pesos del modelo están disponibles bajo la [Licencia MIT](https://github.com/ZhengPeng7/BiRefNet/blob/main/LICENSE). [BiRefNet en Hugging Face](https://huggingface.co/ZhengPeng7/BiRefNet) | [Repositorio de modelos de Comfy-Org](https://huggingface.co/Comfy-Org/BiRefNet) | [Artículo (arXiv)](https://arxiv.org/abs/2401.00807)

### 

​

Principales ventajas

  * **Máscaras de alta calidad** : detección precisa de bordes para cabello, pelaje y detalles finos
  * **Detección versátil de sujetos** : funciona bien con personas, productos, animales y escenas complejas
  * **Flujo de trabajo sencillo de un solo clic** : solo carga una imagen y el modelo se encarga del resto
  * **Salida RGBA** : produce una imagen con fondo transparente lista para composición



> **Limitaciones:** Los fondos extremadamente desordenados o los sujetos que se confunden con el fondo pueden producir máscaras menos precisas. El modelo procesa una sola imagen a la vez.

## 

​

Flujo de trabajo de eliminación de fondo con BiRefNet

### 

​

1\. Descargar el flujo de trabajo

Actualiza tu ComfyUI a la última versión y luego ve a `Workflow` -> `Browse Templates` y busca “BiRefNet: Remove Background” en la categoría Utility.

### 

​

BiRefNet: Remove Background

Sube una imagen con cualquier fondo. Genera una versión con el fondo eliminado y una máscara de segmentación de precisión. ![Vista previa del flujo de trabajo de eliminación de fondo con BiRefNet](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_birefnet_remove_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “BiRefNet: Remove Background” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## the_lily_veil.png

nodo `LoadImage` 17 · `the_lily_veil.png`

### 

​

2\. Descargar los modelos

El modelo BiRefNet está alojado en el [repositorio de modelos BiRefNet de Comfy-Org](https://huggingface.co/Comfy-Org/BiRefNet).

  * [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/blob/main/background_removal/birefnet.safetensors)

Colócalo en la siguiente estructura de carpetas:
    
    
    📂 ComfyUI/
    └── 📂 models/
        └── 📂 background_removal/
            └── birefnet.safetensors
    

### 

​

3\. Usar el flujo de trabajo

  * **Image** : carga una imagen con el nodo `Load Image` (colócala en la carpeta `input/` de ComfyUI)
  * El subgrafo `Remove Background (BiRefNet)` procesa la imagen y produce: 
    * **IMAGE** : el resultado con fondo transparente (RGBA)
    * **mask** : la máscara del primer plano extraída

Puedes previsualizar las salidas y usarlas como entradas de otros nodos para composición, edición adicional o guardado.

## Acerca de los subgrafos

Este flujo de trabajo usa nodos de subgrafo para un procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

## 

​

Notas adicionales

  * **Directorio del modelo** : el modelo debe colocarse en `ComfyUI/models/background_removal/`, no en la carpeta `checkpoints`
  * **Actualización requerida** : el soporte para BiRefNet está disponible en versiones recientes de ComfyUI. Asegúrate de que tu ComfyUI esté actualizado.
  * **Salida RGBA** : el resultado con fondo transparente se puede componer directamente sobre nuevos fondos o usarse en flujos de trabajo posteriores.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/remove-background-birefnet.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/remove-background-birefnet)

[Segmentación con SAM 3.1](https://docs.comfy.org/es/tutorials/utility/video-segment-sam3)[SAM 3D Body](https://docs.comfy.org/es/tutorials/utility/sam3d-body)
