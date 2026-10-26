---
url: https://docs.comfy.org/es/tutorials/flux/flux-1-fill-dev/
title: Ejemplo de ComfyUI Flux.1 fill dev - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:42.549387+00:00
---

# Ejemplo de ComfyUI Flux.1 fill dev - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-1-fill-dev/

## En esta página

Volver arriba

  * Introducción al modelo Flux.1 fill dev
  * Instalación de Flux.1 Fill dev y de los modelos relacionados
  * Flujo de trabajo de relleno inteligente con Flux.1 Fill dev
    * Flux.1 Inpaint
    * 1\. Flujo de trabajo de relleno inteligente y recursos
    * 2\. Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de outpainting con Flux.1 Fill dev
    * Flux.1 Outpaint
    * 1\. Flujo de trabajo y recurso de outpainting
    * 2\. Pasos para ejecutar el flujo de trabajo



FLUX

# Ejemplo de ComfyUI Flux.1 fill dev

Copiar páginaCopiar página

Aprende a usar Flux.1 fill dev para crear flujos de trabajo de relleno inteligente y extensión de imagen.

Copiar páginaCopiar página

![Flux.1 fill dev](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux-fill-dev-demo.jpeg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=e9b567aff5fbd43dce197d819f5f028e)

## 

​

Introducción al modelo Flux.1 fill dev

Flux.1 fill dev es una de las herramientas principales de la [suite FLUX.1 Tools](https://blackforestlabs.ai/flux-1-tools/) lanzada por [Black Forest Labs](https://blackforestlabs.ai/), diseñada específicamente para inpainting y outpainting de imágenes. Características principales de Flux.1 fill dev:

  * Potentes capacidades de inpainting y outpainting de imágenes, con resultados solo superados por la versión comercial FLUX.1 Fill [pro].
  * Excelente capacidad para comprender y seguir el prompt, capturando con precisión la intención del usuario y manteniendo una alta consistencia con la imagen original.
  * Tecnología avanzada de entrenamiento con destilación guiada, que hace el modelo más eficiente sin dejar de producir salidas de alta calidad.
  * Términos de licencia flexibles: las salidas generadas se pueden usar para uso personal, científico y comercial. Consulta la [licencia no comercial de FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) para más detalles.

Repositorio de código abierto: [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev) Esta guía mostrará flujos de trabajo de inpainting y outpainting basados en el modelo Flux.1 fill dev. Si no estás familiarizado con los flujos de trabajo de inpainting y outpainting, puedes consultar el [ejemplo de inpainting de ComfyUI Layout](https://docs.comfy.org/es/tutorials/basic/inpaint) y el [ejemplo de extensión de imagen de ComfyUI](https://docs.comfy.org/es/tutorials/basic/outpaint) para ver explicaciones relacionadas.

## 

​

Instalación de Flux.1 Fill dev y de los modelos relacionados

Antes de empezar, completemos la instalación de los archivos del modelo Flux.1 Fill dev. Los flujos de trabajo de inpainting y outpainting que vienen a continuación usan exactamente los mismos archivos de modelo. Si ya has usado antes la versión completa del [flujo de trabajo de texto a imagen de Flux.1](https://docs.comfy.org/es/tutorials/flux/flux-1-text-to-image), en esta sección solo necesitas descargar el archivo de modelo **flux1-fill-dev.safetensors**. Sin embargo, como la descarga del modelo correspondiente exige aceptar antes el acuerdo de uso, visita la página [black-forest-labs/FLUX.1-Fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev) y asegúrate de haber aceptado el acuerdo correspondiente, como se muestra en la imagen de abajo. ![Acuerdo de Flux](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux1_fill_dev_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=388a26b32b5841dbf6ef32f31537e43d) Lista completa de modelos: |- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) |- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors) |- [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors) |- [flux1-fill-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev/blob/main/flux1-fill-dev.safetensors) Ubicación de almacenamiento de los archivos:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │    ├── clip_l.safetensors
    │   │    └── t5xxl_fp16.safetensors
    │   ├── vae/
    │   │    └── ae.safetensors
    │   └── diffusion_models/
    │        └── flux1-fill-dev.safetensors
    

## 

​

Flujo de trabajo de relleno inteligente con Flux.1 Fill dev

### 

​

Flux.1 Inpaint

Rellena las partes faltantes de las imágenes con Flux.1 Fill Inpainting. ![Vista previa del flujo de trabajo Flux.1 Inpaint](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_inpaint_example-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Inpaint” en la biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## flux_fill_inpaint_example_input_image.png

`LoadImage`, nodo 17 · `flux_fill_inpaint_example_input_image.png`

![flux_fill_inpaint_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_inpaint_example_input_image.png)

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_inpaint_example_input_image.png)![Salida de ejemplo de Flux.1 Inpaint](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_fill_inpaint_example.png)

### 

​

1\. Flujo de trabajo de relleno inteligente y recursos

La imagen correspondiente ya contiene un canal alpha, así que no necesitas dibujar una máscara por separado. Si quieres dibujar tu propia máscara, [haz clic aquí](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/flux/inpaint/flux_fill_inpaint_input_original.png) para obtener la imagen sin máscara y consulta la sección de uso de MaskEditor en el [Ejemplo de relleno inteligente de diseño de ComfyUI](https://docs.comfy.org/es/tutorials/basic/inpaint#usar-el-editor-de-m%C3%A1scara) para aprender a dibujar una máscara en el nodo `Load Image`.

### 

​

2\. Pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de relleno inteligente con Flux.1 Fill dev de ComfyUI](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_inpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8d4238c0487b7ddf527ec044aa02d578)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `flux1-fill-dev.safetensors`.
  2. Asegúrate de que el nodo `DualCLIPLoader` tenga cargados los siguientes modelos: 
     * clip_name1: `t5xxl_fp16.safetensors`
     * clip_name2: `clip_l.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `ae.safetensors`.
  4. Sube la imagen de entrada proporcionada en el documento al nodo `Load Image`; si usas la versión sin máscara, recuerda completar el dibujo de la máscara con el editor de máscara
  5. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Flujo de trabajo de outpainting con Flux.1 Fill dev

### 

​

Flux.1 Outpaint

Amplía las imágenes más allá de sus límites con outpainting de Flux.1. ![Vista previa del flujo de trabajo de outpainting de Flux.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_outpaint_example-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Outpaint” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## flux_fill_outpaint_example_input_image.png

Nodo `LoadImage` 17 · `flux_fill_outpaint_example_input_image.png`

![flux_fill_outpaint_example_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_fill_outpaint_example_input_image.png)

### 

​

1\. Flujo de trabajo y recurso de outpainting

### 

​

2\. Pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de outpainting con Flux.1 Fill dev de ComfyUI](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_outpaint.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=5f152f459be5f120b3895636685cb3d3)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `flux1-fill-dev.safetensors`.
  2. Asegúrate de que el nodo `DualCLIPLoader` tenga cargados los siguientes modelos: 
     * clip_name1: `t5xxl_fp16.safetensors`
     * clip_name2: `clip_l.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `ae.safetensors`.
  4. Sube la imagen de entrada incluida en el documento al nodo `Load Image`.
  5. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-1-fill-dev.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-1-fill-dev)

[ByteDance USO](https://docs.comfy.org/es/tutorials/flux/flux-1-uso)[Flux.1 ControlNet](https://docs.comfy.org/es/tutorials/flux/flux-1-controlnet)
