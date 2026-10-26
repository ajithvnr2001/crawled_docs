---
url: https://docs.comfy.org/es/tutorials/image/hidream/hidream-o1/
title: Ejemplo de flujo de trabajo con HiDream-O1-Image nativo de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:43.948992+00:00
---

# Ejemplo de flujo de trabajo con HiDream-O1-Image nativo de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/hidream/hidream-o1/

## En esta página

Volver arriba

  * Versiones del modelo
  * Flujo de trabajo completo de HiDream-O1-Image
    * HiDream O1 Full: Generación de imágenes
    * 1\. Descargar el flujo de trabajo
    * 2\. Descargar los modelos
    * 3\. Usar el flujo de trabajo
  * Flujo de trabajo de HiDream-O1-Image Dev
    * HiDream O1 Dev
    * 1\. Descargar el flujo de trabajo
    * 2\. Descargar los modelos
    * 3\. Usar el flujo de trabajo
  * Notas adicionales



HiDream

# Ejemplo de flujo de trabajo con HiDream-O1-Image nativo de ComfyUI

Copiar páginaCopiar página

Guía de los flujos de trabajo de texto a imagen y edición de imágenes con HiDream-O1-Image nativo de ComfyUI

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

![Demostración de HiDream-O1-Image](https://raw.githubusercontent.com/HiDream-ai/HiDream-O1-Image/main/assets/general.webp) HiDream-O1-Image es un modelo fundacional generativo de imágenes unificado, publicado como código abierto por HiDream-ai el 8 de mayo de 2026. Construido sobre un Pixel-level Unified Transformer (UiT), funciona sin VAE externos ni codificadores de texto separados, y admite **texto a imagen** , **edición de imágenes por instrucciones** , **personalización basada en sujeto** y **generación de storyboards** en resoluciones de hasta 2.048 × 2.048. HiDream-O1-Image se distribuye bajo la [Licencia MIT](https://github.com/HiDream-ai/HiDream-O1-Image?tab=MIT-1-ov-file) y es compatible de forma nativa con ComfyUI (PR [#13817](https://github.com/Comfy-Org/ComfyUI/pull/13817)). [HiDream-O1-Image - GitHub](https://github.com/HiDream-ai/HiDream-O1-Image)

### 

​

Versiones del modelo

Modelo| Pasos de inferencia| Repositorio  
---|---|---  
HiDream-O1-Image (Full)| 50| [🤗 HiDream-O1-Image](https://huggingface.co/HiDream-ai/HiDream-O1-Image)  
HiDream-O1-Image-Dev| 28| [🤗 HiDream-O1-Image-Dev](https://huggingface.co/HiDream-ai/HiDream-O1-Image-Dev)  
  
## 

​

Flujo de trabajo completo de HiDream-O1-Image

### 

​

HiDream O1 Full: Generación de imágenes

Ingresa un prompt de texto y, de forma opcional, sube imágenes de referencia. Genera una imagen de alta resolución de hasta 2048x2048 con texto a imagen, edición o personalización basada en un sujeto. ![Vista previa del flujo de trabajo HiDream O1 Full](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HiDream O1 Full” en la Biblioteca de plantillas

**Salida de ejemplo** ![Salida de ejemplo de HiDream O1 Full](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_hidream_o1.png)

### 

​

1\. Descargar el flujo de trabajo

### 

​

2\. Descargar los modelos

**Checkpoint** : reempaquetado y cuantizado. Todos usan bf16 para los valores atípicos más extremos y tienen eliminadas las capas deepstack sin usar:

  * [hidream_o1_image_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_fp8_scaled.safetensors): FP8, usa matmuls fp8/mxfp8 en capas MLP seguras para acelerar en hardware compatible
  * [hidream_o1_image_mxfp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_mxfp8.safetensors): variante cuantizada MXFP8
  * [hidream_o1_image_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_bf16.safetensors): precisión bf16 completa (la más grande)

**Codificador de texto** (mejora del prompt): compartido en todas las versiones:

  * [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/blob/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors)

**LoRA (opcional)** : la destilación Dev también se puede aplicar al modelo Full como un LoRA, lo que te permite ajustar la intensidad de la destilación (por [Kijai](https://huggingface.co/Kijai/hidream-O1-image_comfy)):

  * [hidream_o1_dev_lora_rank_64_bf16.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_dev_lora_rank_64_bf16.safetensors): rango completo
  * [hidream_o1_dev_lora_rank_64_bf16_pruned_v1.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_dev_lora_rank_64_bf16_pruned_v1.safetensors): variante podada
  * [hidream_o1_image_dev_2604_lora_avg_rankg_224_bf16.safetensors](https://huggingface.co/Kijai/hidream-O1-image_comfy/blob/main/loras/hidream_o1_image_dev_2604_lora_avg_rankg_224_bf16.safetensors): destilación alternativa basada en checkpoint


    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   ├── hidream_o1_image_fp8_scaled.safetensors
    │   │   ├── hidream_o1_image_mxfp8.safetensors
    │   │   └── hidream_o1_image_bf16.safetensors
    │   ├── 📂 loras/
    │   │   └── hidream_o1_dev_lora_rank_64_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

### 

​

3\. Usar el flujo de trabajo

  * Asegúrate de que `CheckpointLoaderSimple` cargue el checkpoint que elijas
  * Ingresa tu prompt en el nodo `CLIPTextEncode`
  * **Modo texto a imagen:** ajusta el interruptor **“Switch to Image Edit”** a **off** (valor predeterminado). El sampler usará tu prompt de texto directamente.
  * **Modo edición de imagen:** ajusta **“Switch to Image Edit”** a **on** , luego sube una imagen de referencia en el nodo `Load Image` y conéctala a `HiDreamO1ReferenceImages`.



> **Nota:** El sampler O1 genera muestras latentes que deben decodificarse con un nodo `VAEDecode` usando el VAE que carga `CheckpointLoaderSimple`.

## 

​

Flujo de trabajo de HiDream-O1-Image Dev

### 

​

HiDream O1 Dev

Introduce un prompt de texto e imágenes de referencia opcionales. Genera una imagen de alta resolución (hasta 2048x2048) con soporte para texto a imagen, edición de imágenes y personalización basada en el sujeto. ![Vista previa del flujo de trabajo HiDream O1 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1_dev-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HiDream O1 Dev” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## noir_portrait.png

Nodo `LoadImage` 213 · `noir_portrait.png`

![noir_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/noir_portrait.png)

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/noir_portrait.png)![Salida de ejemplo de HiDream O1 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_hidream_o1_dev.png)

### 

​

1\. Descargar el flujo de trabajo

### 

​

2\. Descargar los modelos

**Checkpoint (Dev)** : reempaquetado y cuantizado. Todos usan bf16 para los valores atípicos más extremos y se eliminaron las capas deepstack sin usar:

  * [hidream_o1_image_dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_fp8_scaled.safetensors): FP8, usa matmuls fp8/mxfp8 en capas MLP seguras para acelerar en hardware compatible
  * [hidream_o1_image_dev_mxfp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_mxfp8.safetensors): variante cuantizada MXFP8
  * [hidream_o1_image_dev_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/blob/main/checkpoints/hidream_o1_image_dev_bf16.safetensors): precisión bf16 completa (la más grande)

**Codificador de texto** (mejora del prompt): compartido en todas las versiones:

  * [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/blob/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors)


    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   ├── hidream_o1_image_dev_fp8_scaled.safetensors
    │   │   ├── hidream_o1_image_dev_mxfp8.safetensors
    │   │   └── hidream_o1_image_dev_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

### 

​

3\. Usar el flujo de trabajo

  * Asegúrate de que `CheckpointLoaderSimple` cargue `hidream_o1_image_dev_fp8_scaled.safetensors`
  * La versión Dev usa 28 pasos con CFG=1.0, no se necesita un prompt negativo
  * **Modo texto a imagen:** pon el interruptor **“Switch to Image Edit”** en **off** (predeterminado)
  * **Modo de edición de imagen:** pon **“Switch to Image Edit”** en **on** , sube una imagen de referencia en `Load Image` y conéctala a `HiDreamO1ReferenceImages`



## 

​

Notas adicionales

  * **Representación de texto largo:** HiDream-O1-Image destaca en la representación de texto dentro de las imágenes. Especifica el contenido del texto, el estilo de fuente, el color y la posición en tu prompt para obtener los mejores resultados. ![Representación de texto largo y control del diseño](https://raw.githubusercontent.com/HiDream-ai/HiDream-O1-Image/main/assets/text-layout.webp)
  * **Escalado de imagen:** Si tu imagen de referencia de entrada es demasiado grande, habilita el nodo `ImageScaleToTotalPixels` (Ctrl+B) para escalarla a 4MP.
  * **Suavizado de costuras de parches (experimental):** El nodo `HiDreamO1PatchSeamSmoothing` reduce los artefactos de costura visibles durante el muestreo. Habilitado de forma predeterminada en el flujo de trabajo Full.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/hidream/hidream-o1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/hidream/hidream-o1)

[HiDream-e1](https://docs.comfy.org/es/tutorials/image/hidream/hidream-e1)[NewBie-image-Exp0.1](https://docs.comfy.org/es/tutorials/image/newbie-image/newbie-image-exp-0-1)
