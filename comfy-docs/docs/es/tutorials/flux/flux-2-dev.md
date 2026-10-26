---
url: https://docs.comfy.org/es/tutorials/flux/flux-2-dev/
title: FLUX.2 Dev en ComfyUI: texto a imagen y mockups de producto - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:43.078378+00:00
---

# FLUX.2 Dev en ComfyUI: texto a imagen y mockups de producto - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-2-dev/

## En esta página

Volver arriba

  * Acerca de FLUX.2
  * FLUX.2 Dev
  * FLUX.2 Dev texto a imagen
  * Maqueta de producto
  * Enlaces de modelos



FLUX

# FLUX.2 Dev en ComfyUI: texto a imagen y mockups de producto

Copiar páginaCopiar página

Ejecuta FLUX.2 Dev en ComfyUI para imágenes fotorrealistas de hasta 4MP con consistencia multi-referencia, texto legible y mockups de producto.

Copiar páginaCopiar página

## 

​

Acerca de FLUX.2

[FLUX.2](https://bfl.ai/blog/flux-2) es un modelo de imágenes de nueva generación de [Black Forest Labs](https://blackforestlabs.ai/), que ofrece resultados fotorrealistas de hasta 4MP con una mejora considerable en iluminación, piel, telas y detalle de las manos. Añade una consistencia fiable con múltiples referencias (hasta 10 imágenes), una precisión de edición mejorada, una mejor comprensión visual y un renderizado de texto de nivel profesional. **Características principales:**

  * **Consistencia con múltiples referencias:** Mantiene de forma fiable la identidad, la geometría del producto, las texturas, los materiales, el vestuario y la intención de composición en múltiples salidas
  * **Fotorrealismo de alta resolución:** Genera imágenes de hasta 4MP con un comportamiento realista de la iluminación, razonamiento espacial y detalles que tienen en cuenta la física
  * **Control de nivel profesional:** Control exacto de la pose, colores de marca precisos según el código hex, cualquier relación de aspecto y prompts estructurados para flujos de trabajo programáticos
  * **Renderizado de texto utilizable:** Produce texto limpio y legible en pantallas de interfaz, infografías y contenido en varios idiomas

**Modelos disponibles:**

  * **FLUX.2 Dev:** Modelo de código abierto (utilizado en este tutorial)
  * **FLUX.2 Pro:** Versión API de Black Forest Labs



En este flujo de trabajo usamos pesos cuantizados. El repositorio original de FLUX.2 está disponible [aquí](https://huggingface.co/black-forest-labs/FLUX.2-dev/).

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

FLUX.2 Dev

Genera imágenes fotorrealistas con consistencia entre múltiples referencias y renderizado de texto profesional. ![Vista previa del flujo de trabajo FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2-1.webp)

## Ejecutar en Comfy Cloud

Abre este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo de forma local

**Materiales de entrada** Sube este archivo al nodo `LoadImage` **46** :

## Imagen de entrada para FLUX.2 Dev

Nodo `LoadImage` 46 · `image_flux2_input_image.png`

![Imagen de entrada para FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_image.png)![Salida de ejemplo de FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2.png)

## 

​

FLUX.2 Dev texto a imagen

Texto a imagen con iluminación, materiales y detalles realistas mejorados. No necesitas imágenes de entrada. ![Vista previa del flujo de trabajo de texto a imagen de FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image-1.webp)

## Ejecutar en Comfy Cloud

Abre este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo localmente

**Salida de ejemplo** ![Ejemplo de texto a imagen de FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_text_to_image.png)

## 

​

Maqueta de producto

Crea maquetas de producto aplicando patrones de diseño a envases, tazas y otros productos mediante la consistencia de múltiples referencias. ![Vista previa del flujo de trabajo de maqueta de producto de FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_fp8-1.webp)

## Ejecutar en Comfy Cloud

Abre este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo en local

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## Imagen de referencia de entrada para FLUX.2 Dev

Nodo `LoadImage` 42 · `image_flux2_input_ref_image.png`

## Ilustración de entrada para FLUX.2 Dev

Nodo `LoadImage` 46 · `image_flux2_input_Illustration.png`

![Imagen de referencia de entrada para FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_ref_image.png)![Ilustración de entrada para FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_flux2_input_Illustration.png)

**Ejemplo de salida** ![Salida de maqueta de producto de FLUX.2 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux2_fp8.png)

## 

​

Enlaces de modelos

**text_encoders**

  * [mistral_3_small_flux2_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors)

**diffusion_models**

  * [flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors)

**vae**

  * [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/vae/flux2-vae.safetensors)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── mistral_3_small_flux2_bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── flux2_dev_fp8mixed.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-2-dev.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-2-dev)

[FLUX 3 Klein](https://docs.comfy.org/es/tutorials/flux/flux-3-klein)[FLUX.2 Klein](https://docs.comfy.org/es/tutorials/flux/flux-2-klein)
