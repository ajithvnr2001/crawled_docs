---
url: https://docs.comfy.org/es/tutorials/flux/flux1-krea-dev/
title: Tutorial del flujo de trabajo FLUX.1 Krea Dev en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:42.903636+00:00
---

# Tutorial del flujo de trabajo FLUX.1 Krea Dev en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux1-krea-dev/

## En esta página

Volver arriba

  * Flujo de trabajo de FLUX.1 Krea Dev en ComfyUI
    * FLUX.1 Krea Dev
    * 1\. Archivos del flujo de trabajo
    * 2\. Instalación manual de los modelos
    * 3\. Verificación paso a paso para asegurar que el flujo de trabajo funcione correctamente



FLUX

# Tutorial del flujo de trabajo FLUX.1 Krea Dev en ComfyUI

Copiar páginaCopiar página

Genera imágenes con el modelo de código abierto FLUX.1 Krea Dev en ComfyUI, de Black Forest Labs y Krea, con detalles naturales y una estética distintiva.

Copiar páginaCopiar página

![Póster de FLUX.1 Krea Dev](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_poster.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=79640b1911971da78cf2bedb7b3b75ca) [FLUX.1 Krea Dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev) es un modelo avanzado de generación de texto a imagen desarrollado en colaboración entre Black Forest Labs (BFL) y Krea. Actualmente es el mejor modelo FLUX de código abierto, diseñado específicamente para la generación de texto a imagen. **Características del modelo**

  * **Estilo estético único** : se enfoca en generar imágenes con una estética única, evitando la apariencia común de “IA”
  * **Detalles naturales** : no produce luces quemadas y mantiene una representación natural del detalle
  * **Realismo excepcional** : ofrece un realismo y una calidad de imagen sobresalientes
  * **Arquitectura totalmente compatible** : diseño de arquitectura totalmente compatible con FLUX.1 [dev]

**Licencia del modelo** Este modelo se distribuye bajo la [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/LICENSE.md)

## 

​

Flujo de trabajo de FLUX.1 Krea Dev en ComfyUI

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

FLUX.1 Krea Dev

Un modelo FLUX con ajuste fino que lleva el fotorrealismo al máximo. ![Vista previa del flujo de trabajo de FLUX.1 Krea Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_krea_dev-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX.1 Krea Dev” en la Biblioteca de plantillas

**Resultado de ejemplo** ![Resultado de ejemplo de FLUX.1 Krea Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux1_krea_dev.png)

#### 

​

1\. Archivos del flujo de trabajo

#### 

​

2\. Instalación manual de los modelos

Descarga los siguientes archivos de modelo: **Modelo de difusión**

  * [flux1-krea-dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors)

Si buscas una mayor calidad y tienes suficiente VRAM, puedes probar los pesos originales del modelo

  * [flux1-krea-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/blob/main/flux1-krea-dev.safetensors)



El archivo `flux1-dev.safetensors` requiere aceptar el acuerdo de [black-forest-labs/FLUX.1-Krea-dev](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev/) antes de descargarlo a través del navegador.

Si ya has usado flujos de trabajo relacionados con FLUX, los siguientes modelos son los mismos y no necesitas descargarlos de nuevo. **Codificadores de texto**

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors?download=true) Recomendado cuando tu VRAM es mayor de 32 GB.
  * [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors) Para VRAM baja

**VAE**

  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)

Ubicación de guardado de los archivos:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── flux1-krea-dev_fp8_scaled.safetensors or flux1-krea-dev.safetensors
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    
    

#### 

​

3\. Verificación paso a paso para asegurar que el flujo de trabajo funcione correctamente

Si tienes poca VRAM, es posible que este modelo no funcione con fluidez en tu equipo; puedes esperar a que la comunidad publique una versión FP8 o GGUF.

Consulta la imagen de abajo para asegurarte de que todos los archivos de modelo se hayan cargado correctamente ![Flujo de trabajo de FLUX Krea Dev en ComfyUI](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_krea_dev_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=8475817d518de939bb6c5aabf8c1770e)

  1. Asegúrate de que `flux1-krea-dev_fp8_scaled.safetensors` o `flux1-krea-dev.safetensors` esté cargado en el nodo `Load Diffusion Model`
     * `flux1-krea-dev_fp8_scaled.safetensors` es la opción recomendada para usuarios con poca VRAM
     * `flux1-krea-dev.safetensors` son los pesos originales; si tienes suficiente VRAM, como 24 GB, puedes usarlo para obtener mejor calidad
  2. Asegúrate de que los siguientes modelos estén cargados en el nodo `DualCLIPLoader`: 
     * clip_name1: t5xxl_fp16.safetensors o t5xxl_fp8_e4m3fn.safetensors
     * clip_name2: clip_l.safetensors
  3. Asegúrate de que `ae.safetensors` esté cargado en el nodo `Load VAE`
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux1-krea-dev.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux1-krea-dev)

[FLUX.2 Klein](https://docs.comfy.org/es/tutorials/flux/flux-2-klein)[FLUX.1 Kontext Dev](https://docs.comfy.org/es/tutorials/flux/flux-1-kontext-dev)
