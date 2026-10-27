---
url: https://docs.comfy.org/es/tutorials/3d/pixal3d/
title: Pixal3D en ComfyUI: modelos 3D PBR desde una sola imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:11.847959+00:00
---

# Pixal3D en ComfyUI: modelos 3D PBR desde una sola imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/3d/pixal3d/

## En esta página

Volver arriba

  * Pixal3D: de imagen a modelo 3D
  * Pixal3D: de varias vistas a 3D
  * Cómo funciona
  * Pasos para ejecutar
  * Descargas de modelos
    * Ubicación de almacenamiento de los modelos



3D

# Pixal3D en ComfyUI: modelos 3D PBR desde una sola imagen

Copiar páginaCopiar página

Convierte una imagen en un modelo 3D con textura en ComfyUI con Pixal3D, el modelo de imagen a 3D de Tencent ARC con materiales PBR completos.

Copiar páginaCopiar página

**Pixal3D** es un modelo abierto de imagen a 3D de Tencent ARC, presentado en SIGGRAPH 2026. Convierte una sola imagen en un recurso 3D de alta fidelidad con materiales PBR completos. La mayoría de los generadores nativos 3D sintetizan formas en un espacio canónico e inyectan señales de la imagen mediante atención, lo que deja ambiguas las asociaciones entre píxeles y 3D. Pixal3D, en cambio, usa generación alineada a píxeles: establece una correspondencia directa entre píxeles y 3D mediante retroproyección, de modo que el frente del modelo generado coincide 1:1 con tu imagen de entrada, sin texturas deformadas ni desalineadas.

### 

​

Pixal3D: de imagen a modelo 3D

Sube una sola imagen. Genera un modelo 3D de alta fidelidad con texturas PBR completas, alineado a tu vista de entrada. Este flujo de trabajo también incluye el pipeline de TRELLIS.2. El nodo `Boolean (Switch to Trellis2)` tiene `false` por defecto, lo que ejecuta el pipeline de Pixal3D y carga el modelo Pixal3D automáticamente. ![Vista previa del flujo de trabajo de Pixal3D](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_trellis2_image_to_model-1.webp)

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

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo al instante en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pixal3D & TRELLIS.2: Image to Model” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage`:

## viking_wolf_rune_axe.png

Nodo `LoadImage` 122 · `viking_wolf_rune_axe.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/viking_wolf_rune_axe.png)

### 

​

Pixal3D: de varias vistas a 3D

Genera un modelo 3D a partir de una hoja de rotación de personaje (vistas de frente, perfil y espalda en una sola imagen). El modelo multivista usa los puntos de vista adicionales para reconstruir geometría que el pipeline de una sola imagen no puede ver, lo que da perfiles laterales y traseros más precisos. Usa la plantilla `Character Turnaround Sheet Generator` de la biblioteca de plantillas para producir la hoja de rotación con Nano Banana 2, o prepara tu propia imagen multivista con el sujeto separado del fondo. ![Vista previa del flujo de trabajo de varias vistas de Pixal3D](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_multi_views-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo al instante en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pixal3D: Multi Views to 3D” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage`:

## character_turnaround_4view_sheet.png

Nodo `LoadImage` 364 · `character_turnaround_4view_sheet.png`

Este flujo de trabajo usa los modelos que se indican a continuación. Descárgalos y colócalos en los subdirectorios correspondientes de `models/`:

## Pixal3D Multiview UNet

pixal3d_multiview_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## VAE de forma

trellis_2_shape_vae_bf16.safetensors → ComfyUI/models/vae/

## VAE de textura

trellis_2_texture_vae_bf16.safetensors → ComfyUI/models/vae/

## DINOv3 CLIP vision

dino_v3_L_naf_fp32.safetensors → ComfyUI/models/clip_vision/

## BiRefNet: eliminación de fondo

birefnet.safetensors → ComfyUI/models/background_removal/

## 

​

Cómo funciona

Pixal3D combina una generación consciente de la cámara y alineada por píxeles con un pipeline completo de posprocesamiento de malla:

  1. **Eliminación de fondo** : BiRefNet elimina el fondo de la imagen de entrada y el flujo de trabajo recorta el sujeto a un lienzo centrado. Un interruptor te permite saltar la eliminación de fondo
  2. **Estimación de cámara** : MoGe estima la geometría y el campo de visión de la cámara a partir de la imagen. El campo de visión impulsa el acondicionamiento alineado por píxeles
  3. **Generación de estructura** : se muestrea un latente de estructura dispersa y se decodifica en vóxeles, que luego se convierten en una malla aproximada
  4. **Refinamiento de forma** : la etapa de forma y la etapa de upsampling refinan la malla hasta la resolución objetivo (1536)
  5. **Generación de texturas** : una etapa de difusión de texturas produce vóxeles de material PBR (color base, metalicidad, rugosidad)
  6. **Posprocesamiento** : remesh DC, decimación QEM, desplegado UV y horneado de mapas de color base, normales y oclusión ambiental en la malla texturizada final



## 

​

Pasos para ejecutar

  1. **Carga una imagen** : usa el nodo `LoadImage` para cargar una sola imagen del objeto.
  2. **Pon el flujo de trabajo en cola** : presiona Ctrl (Cmd en macOS) + Enter.
  3. **Espera a que se complete el pipeline** : las etapas de estructura, forma y textura se ejecutan en secuencia, seguidas del posprocesamiento.
  4. **Consulta el resultado** : revisa la malla en el nodo `Preview3DAdvanced`. El modelo 3D se guarda en `ComfyUI/output/3d/ComfyUI/`.



## 

​

Descargas de modelos

Descarga los modelos que usa este flujo de trabajo. Los dos checkpoints de difusión son obligatorios: el interruptor elige cuál se ejecuta. Colócalos en los subdirectorios correspondientes de `models/`.

## Pixal3D UNet

pixal3d_int8_convrot.safetensors: modelo de difusión de Pixal3D, cargado de forma predeterminada

## TRELLIS.2 UNet

trellis_2_int8_convrot.safetensors: modelo de difusión de TRELLIS.2, cargado cuando el interruptor está en `true`

## VAE de forma

trellis_2_shape_vae_bf16.safetensors: VAE para la decodificación de estructura y forma

## VAE de textura

trellis_2_texture_vae_bf16.safetensors: VAE para la decodificación de texturas

## DINOv3 CLIP vision

dino_v3_L_naf_fp32.safetensors: codificador de visión CLIP para el acondicionamiento de imágenes

## MoGe Geometry

moge_2_vitl_normal_fp16.safetensors: estimación de profundidad y de cámara para el acondicionamiento alineado por píxeles

## BiRefNet eliminación de fondo

birefnet.safetensors: modelo de eliminación de fondo para el preprocesamiento

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── pixal3d_int8_convrot.safetensors
    │   │      └── trellis_2_int8_convrot.safetensors
    │   ├── 📂 vae/
    │   │      ├── trellis_2_shape_vae_bf16.safetensors
    │   │      └── trellis_2_texture_vae_bf16.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── dino_v3_L_naf_fp32.safetensors
    │   ├── 📂 geometry_estimation/
    │   │      └── moge_2_vitl_normal_fp16.safetensors
    │   └── 📂 background_removal/
    │          └── birefnet.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/3d/pixal3d.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/3d/pixal3d)

[OmniGen2](https://docs.comfy.org/es/tutorials/image/omnigen/omnigen2)[TRELLIS.2](https://docs.comfy.org/es/tutorials/3d/trellis2)
