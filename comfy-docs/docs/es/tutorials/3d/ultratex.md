---
url: https://docs.comfy.org/es/tutorials/3d/ultratex/
title: UltraTex: texturiza un modelo 3D en ComfyUI desde una imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:28.904334+00:00
---

# UltraTex: texturiza un modelo 3D en ComfyUI desde una imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/3d/ultratex/

## En esta página

Volver arriba

  * Texturar un modelo 3D
  * Qué cambiar
  * Antes de ejecutar
  * Descargas de modelos



3D

# UltraTex: texturiza un modelo 3D en ComfyUI desde una imagen

Copiar páginaCopiar página

Texturiza una malla 3D sin textura con UltraTex sobre FLUX.2 Klein 9B en ComfyUI: seis vistas normales, albedo y metalicidad/rugosidad, y un GLB PBR.

Copiar páginaCopiar página

**UltraTex** texturiza una malla 3D a partir de una sola imagen de referencia. Es un framework de texturizado multivista 2K de SIGGRAPH Asia 2026 y, en ComfyUI, se ejecuta sobre la base FLUX.2 Klein base 9B: los LoRA de UltraTex reconvierten ese modelo en un generador de texturas y el VAE de UltraTex mantiene limpias las vistas renderizadas. Dale una malla sin texturizar y una imagen de cómo debería verse el objeto. El flujo de trabajo renderiza la malla desde seis vistas de normales en espacio de mundo, pinta el albedo en una pasada y el metallic/roughness en otra, hornea ambos sobre las UV de la malla y guarda un GLB PBR con los mapas PNG. Requiere ComfyUI **0.46.0+** y el paquete de plantillas **0.11.115+**.

## Texturar un modelo 3D

Carga tu malla en **Load 3D (Advanced)** y la imagen de referencia en **Load Image** , luego ejecuta el flujo de trabajo. La plantilla incluye una malla de estatuilla de rana y su versión pintada, así que funciona tal como se descarga. ![UltraTex texturizando una malla de estatuilla de rana a partir de una imagen de referencia](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_ultratex_texture_3d_model-1.webp)

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

## Descargar flujo de trabajo

Descarga el JSON o busca “UltraTex: Texture a 3D Model” en la Biblioteca de plantillas

**Materiales de entrada**

## sir_frog.obj

La malla a texturizar, abierta en Load 3D (Advanced)

## sir_frog.png

La referencia: cómo debería verse el objeto

## Qué cambiar

  * **Load 3D (Advanced)** : tu malla y la cámara desde la que se toma la vista frontal. El horneado reutiliza ese mismo rig de cámara.
  * **Load Image** : la referencia vista desde el lado de la cámara frontal, porque se proyecta en la vista frontal. Mantén un objeto en una única orientación.
  * **Rendered Mesh Resolution** (1024) determina el tamaño de los renders y del latente. **Texture Resolution** (4096) determina el tamaño de los mapas horneados.
  * **Albedo pass** ejecuta 4 pasos con semilla 1. **Metallic/roughness pass** ejecuta 8 pasos con semilla 4.
  * **Camera orbit** está fijada a cuatro vistas laterales, más arriba y abajo, seis vistas en total. UltraTex Conditioning solo acepta esas seis vistas o las cuatro laterales, así que una órbita reducida necesita un lote latente de 4.



## Antes de ejecutar

  * La malla ya debe tener coordenadas UV. El horneado y el paso de aplicación las reutilizan, y no hay un paso de desplegado UV.
  * Las semillas solo cambian el detalle de la superficie. La silueta siempre proviene de la malla.
  * `fill_unseen` propaga el color a téxeles que ninguna vista vio. Desactívalo para conservar la textura propia de la malla en esas zonas.



## Descargas de modelos

Siete archivos van en `ComfyUI/models`. El gráfico incluido necesita 13.16 GB; si cambias el checkpoint por la versión de precisión completa, sube a 21.87 GB.

## Modelo de difusión: flux-2-klein-base-9b_int8_convrot.safetensors

FLUX.2 Klein base 9B, INT8, 9.44 GB. Colócalo en `ComfyUI/models/diffusion_models/`

## LoRA de destilación: flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors

Se carga con intensidad 0.5, 1.96 GB. Colócalo en `ComfyUI/models/loras/`

## LoRA de albedo: ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors

Pase de albedo, 478 MB. Colócalo en `ComfyUI/models/loras/`

## LoRA de metalicidad/rugosidad: ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors

Pase de metalicidad/rugosidad, 478 MB. Colócalo en `ComfyUI/models/loras/`

## Embedding: flux-2-klein-9b_empty_prompt.safetensors

Prompt vacío previamente codificado, 25 MB. Colócalo en `ComfyUI/models/embeddings/`

## VAE: ultratex_flux2_vae_fp32.safetensors

UltraTex VAE, FP32, 336 MB. Colócalo en `ComfyUI/models/vae/`

## Eliminación de fondo: birefnet.safetensors

Enmascara la imagen de referencia, 444 MB. Colócalo en `ComfyUI/models/background_removal/`

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── flux-2-klein-base-9b_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   ├── flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors
    │   │   ├── ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors
    │   │   └── ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors
    │   ├── 📂 embeddings/
    │   │   └── flux-2-klein-9b_empty_prompt.safetensors
    │   ├── 📂 vae/
    │   │   └── ultratex_flux2_vae_fp32.safetensors
    │   └── 📂 background_removal/
    │       └── birefnet.safetensors
    

El gráfico no carga ningún codificador de texto: `Load Conditioning` lee en su lugar el prompt vacío previamente codificado. Los pesos del modelo se distribuyen bajo la [Licencia No Comercial de FLUX](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/blob/main/LICENSE.md). Artículo y código: [UltraTex en arXiv](https://arxiv.org/abs/2609.23169), [yiboz2001/UltraTex](https://github.com/yiboz2001/UltraTex).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/3d/ultratex.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/3d/ultratex)

[OmniGen2](https://docs.comfy.org/es/tutorials/image/omnigen/omnigen2)[Pixal3D](https://docs.comfy.org/es/tutorials/3d/pixal3d)
