---
url: https://docs.comfy.org/es/tutorials/flux/flux-2-klein/
title: Gu\u00eda de ComfyUI FLUX.2 Klein 4B - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:43.004117+00:00
---

# Guía de ComfyUI FLUX.2 Klein 4B - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-2-klein/

## En esta página

Volver arriba

  * Acerca de FLUX.2 [klein]
  * Flujos de trabajo de FLUX.2 Klein 4B
    * FLUX.2 [Klein] 4B: Texto a imagen
    * FLUX.2 [Klein] 4B: Edición de imagen
    * FLUX.2 [Klein] 4B destilado: Edición de imagen
  * Descargas de modelos de FLUX.2 Klein 4B
  * Flujos de trabajo de FLUX.2 Klein 9B
    * FLUX.2 [Klein] 9B: Texto a imagen
    * FLUX.2 [Klein] 9B: Edición de imagen
    * FLUX.2 [Klein] 9B destilado: Edición de imagen
  * Descargas de modelos de FLUX.2 Klein 9B



FLUX

# Guía de ComfyUI FLUX.2 Klein 4B

Copiar páginaCopiar página

Introducción rápida a FLUX.2 [klein] 4B y cómo ejecutar flujos de trabajo de texto a imagen y edición de imágenes en ComfyUI.

Copiar páginaCopiar página

## 

​

Acerca de FLUX.2 [klein]

FLUX.2 [Klein] es el modelo más rápido de la familia FLUX: unifica texto a imagen y edición de imágenes en una sola arquitectura compacta. Está diseñado para flujos de trabajo interactivos, vistas previas inmediatas y aplicaciones donde la latencia es crítica, con variantes destiladas que ofrecen una inferencia de extremo a extremo en torno a un segundo y mantienen una gran calidad en la edición con una o varias referencias. **Aspectos destacados del modelo:**

  * Dos tipos de 4B: Base (sin destilar) para máxima flexibilidad y ajuste fino; Distilled (4 pasos) para despliegues que priorizan la velocidad
  * Rendimiento: destilado ~1.2s (5090) · 8.4GB VRAM; base ~17s (5090) · 9.2GB VRAM
  * Soporte de edición: transformaciones de estilo, ediciones semánticas, reemplazo y eliminación de objetos, composición con varias referencias, ediciones iterativas



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

Flujos de trabajo de FLUX.2 Klein 4B

### 

​

FLUX.2 [Klein] 4B: Texto a imagen

![Vista previa del flujo de trabajo de texto a imagen de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_text_to_image-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Flujo de trabajo de texto a imagen 4B

Descarga el flujo de trabajo de texto a imagen para FLUX.2 Klein 4B.

**Salida de ejemplo** ![Ejemplo de texto a imagen de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_text_to_image.png)

### 

​

FLUX.2 [Klein] 4B: Edición de imagen

![Vista previa del flujo de trabajo de edición de imagen base de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_base-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Edición de imagen 4B base

Descarga el flujo de trabajo de edición de imagen con el modelo base 4B.

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## robed_women.png

Nodo `LoadImage` 76 · `robed_women.png`

## pink_tone_chair.png

Nodo `LoadImage` 81 · `pink_tone_chair.png`

![robed_women.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/robed_women.png)![pink_tone_chair.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/pink_tone_chair.png)

**Salida de ejemplo** ![Ejemplo de edición de imagen base de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/image_flux2_klein_image_edit_4b_base.png)

### 

​

FLUX.2 [Klein] 4B destilado: Edición de imagen

![Vista previa del flujo de trabajo de edición de imagen destilado de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_distilled-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Edición de imagen 4B destilada

Descarga el flujo de trabajo rápido de edición de imagen 4B destilado.

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## handbag_white.png

Nodo `LoadImage` 76 · `handbag_white.png`

## comfy_logo_blue.png

Nodo `LoadImage` 81 · `comfy_logo_blue.png`

![handbag_white.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/handbag_white.png)![comfy_logo_blue.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/comfy_logo_blue.png)

**Salida de ejemplo** ![Ejemplo de edición de imagen destilado de FLUX.2 Klein 4B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_image_edit_4b_distilled.png)

## 

​

Descargas de modelos de FLUX.2 Klein 4B

## qwen_3_4b.safetensors

Codificador de texto para modelos 4B.

## flux-2-klein-base-4b-fp8.safetensors

Modelo de difusión (4B base).

## flux-2-klein-4b-fp8.safetensors

Modelo de difusión (4B destilado).

## flux2-vae.safetensors

VAE para modelos 4B.

**Ubicación de almacenamiento de los modelos 4B**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── flux-2-klein-base-4b-fp8.safetensors
    │   │      └── flux-2-klein-4b-fp8.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

## 

​

Flujos de trabajo de FLUX.2 Klein 9B

### 

​

FLUX.2 [Klein] 9B: Texto a imagen

![Vista previa del flujo de trabajo texto a imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image_9b-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Flujo de trabajo texto a imagen 9B

Descarga el flujo de trabajo texto a imagen de FLUX.2 Klein 9B.

**Salida de ejemplo** ![Ejemplo de texto a imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_text_to_image_9b.png)

### 

​

FLUX.2 [Klein] 9B: Edición de imagen

![Vista previa del flujo de trabajo base de edición de imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Base de edición de imagen 9B

Descarga el flujo de trabajo de edición de imagen con el modelo base 9B.

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## car_interior_white.jpeg

Nodo `LoadImage` 76 · `car_interior_white.jpeg`

## comfy_logo_blue.png

Nodo `LoadImage` 81 · `comfy_logo_blue.png`

![car_interior_white.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/car_interior_white.jpeg)![comfy_logo_blue.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/comfy_logo_blue.png)

**Salida de ejemplo** ![Ejemplo base de edición de imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/thumbnail/image_flux2_klein_image_edit_9b_base.png)

### 

​

FLUX.2 [Klein] 9B destilado: Edición de imagen

![Vista previa del flujo de trabajo destilado de edición de imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_distilled-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Edición de imagen 9B destilado

Descarga el flujo de trabajo rápido destilado de edición de imagen 9B.

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## bold_outfit_woman.jpeg

Nodo `LoadImage` 76 · `bold_outfit_woman.jpeg`

## handbag_white.png

Nodo `LoadImage` 121 · `handbag_white.png`

![bold_outfit_woman.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/bold_outfit_woman.jpeg)![handbag_white.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/handbag_white.png)

**Salida de ejemplo** ![Ejemplo destilado de edición de imagen de FLUX.2 Klein 9B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_klein_image_edit_9b_distilled.png)

## 

​

Descargas de modelos de FLUX.2 Klein 9B

Para los modelos de difusión, visita el repositorio de BFL, acepta el acuerdo y luego descarga los modelos.

## flux-2-klein-base-9b-fp8.safetensors

Modelo de difusión (9B base).

## flux-2-klein-9b-fp8.safetensors

Modelo de difusión (9B destilado).

## qwen_3_8b_fp8mixed.safetensors

Codificador de texto para modelos 9B.

## flux2-vae.safetensors

VAE para modelos 9B.

**Ubicación de almacenamiento de los modelos 9B**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── flux-2-klein-9b-fp8.safetensors
    │   │      └── flux-2-klein-base-9b-fp8.safetensors
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_8b_fp8mixed.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-2-klein.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-2-klein)

[FLUX.2 Dev](https://docs.comfy.org/es/tutorials/flux/flux-2-dev)[FLUX.1 Krea Dev](https://docs.comfy.org/es/tutorials/flux/flux1-krea-dev)
