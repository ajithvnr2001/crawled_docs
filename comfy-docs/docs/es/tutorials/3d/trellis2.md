---
url: https://docs.comfy.org/es/tutorials/3d/trellis2/
title: Ejemplo de flujo de trabajo de ComfyUI para convertir una imagen en un modelo 3D con TRELLIS.2 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:40.738723+00:00
---

# Ejemplo de flujo de trabajo de ComfyUI para convertir una imagen en un modelo 3D con TRELLIS.2 - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/3d/trellis2/

## En esta página

Volver arriba

  * TRELLIS.2: modelo 3D a partir de una imagen
  * Cómo funciona
  * Pasos para ejecutar
  * Descarga de modelos
    * Ubicación de almacenamiento de los modelos



3D

# Ejemplo de flujo de trabajo de ComfyUI para convertir una imagen en un modelo 3D con TRELLIS.2

Copiar páginaCopiar página

Genera modelos 3D de alta fidelidad con texturas PBR completas desde una sola imagen con TRELLIS.2, el modelo abierto de Microsoft de 4B parámetros para imagen a 3D.

Copiar páginaCopiar página

**TRELLIS.2** es un modelo de imagen a 3D de código abierto de Microsoft Research y el sucesor de TRELLIS. Es un modelo de 4B parámetros construido sobre VAE 3D nativos con compresión espacial de 16× y una representación de vóxeles dispersos llamada O-Voxel, que produce recursos 3D detallados con materiales PBR completos a partir de una sola imagen. TRELLIS.2 comparte su arquitectura base con Pixal3D: ambos usan el mismo codificador de imágenes DINOv3, los mismos VAE de forma y textura, y las mismas etapas de generación de estructura, forma y textura. Solo cambian el modelo de difusión principal y el formato de acondicionamiento. Si ya has ejecutado el [flujo de trabajo de Pixal3D](https://docs.comfy.org/es/tutorials/3d/pixal3d), la configuración del modelo es casi idéntica.

### 

​

TRELLIS.2: modelo 3D a partir de una imagen

Sube una sola imagen. Genera un modelo 3D de alta fidelidad con texturas PBR completas usando TRELLIS.2. Este flujo de trabajo también incluye el pipeline de Pixal3D. Para ejecutar TRELLIS.2, establece el nodo `Boolean (Switch to Trellis2)` en `true`. El flujo de trabajo cambia automáticamente al modelo TRELLIS.2 y a su acondicionamiento. ![Vista previa del flujo de trabajo de TRELLIS.2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_trellis2_image_to_model-1.webp)

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

nodo `LoadImage` 122 · `viking_wolf_rune_axe.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/viking_wolf_rune_axe.png)

## 

​

Cómo funciona

TRELLIS.2 genera un recurso 3D en tres etapas de difusión y luego ejecuta un pipeline completo de posprocesamiento de la malla:

  1. **Eliminación de fondo** : BiRefNet elimina el fondo de la imagen de entrada y el flujo de trabajo recorta el sujeto a un lienzo centrado. Un interruptor te permite saltar la eliminación de fondo
  2. **Generación de estructura** : se muestrea un latente de estructura dispersa y se decodifica en vóxeles, que luego se convierten en una malla aproximada
  3. **Refinamiento de forma** : la etapa de forma y la etapa de sobremuestreo refinan la malla hasta la resolución objetivo (1536)
  4. **Generación de textura** : una etapa de difusión de textura produce vóxeles de material PBR (color base, metalicidad, rugosidad)
  5. **Posprocesamiento** : DC remesh, QEM decimation, UV unwrapping y baking de mapas de color base, normal y oclusión ambiental en la malla texturizada final



## 

​

Pasos para ejecutar

  1. **Carga una imagen** : usa el nodo `LoadImage` para cargar una sola imagen del objeto
  2. **Cambia al pipeline de TRELLIS.2** : establece `Boolean (Switch to Trellis2)` en `true`. El flujo de trabajo carga el checkpoint de TRELLIS.2 automáticamente
  3. **Envía el flujo de trabajo a la cola** : presiona Ctrl (Cmd en macOS) + Enter
  4. **Espera al pipeline** : las etapas de estructura, forma y textura se ejecutan en secuencia, seguidas del posprocesamiento
  5. **Visualiza el resultado** : revisa la malla en el nodo `Preview3DAdvanced`. El modelo 3D se guarda en `ComfyUI/output/3d/ComfyUI/`



## 

​

Descarga de modelos

Descarga los modelos que usa este flujo de trabajo. Los dos checkpoints de difusión son obligatorios: el interruptor elige cuál se ejecuta. Colócalos en los subdirectorios correspondientes de `models/`.

## TRELLIS.2 UNet

trellis_2_int8_convrot.safetensors: modelo de difusión de TRELLIS.2, cargado cuando el interruptor está en `true`

## Pixal3D UNet

pixal3d_int8_convrot.safetensors: modelo de difusión de Pixal3D, cargado de forma predeterminada

## VAE de forma

trellis_2_shape_vae_bf16.safetensors: VAE para la decodificación de estructura y forma

## VAE de textura

trellis_2_texture_vae_bf16.safetensors: VAE para la decodificación de texturas

## DINOv3 CLIP vision

dino_v3_L_naf_fp32.safetensors: codificador de visión CLIP para el conditioning de imágenes. El dino_v3_vit_l.safetensors equivalente del repositorio TRELLIS.2 también funciona

## BiRefNet eliminación de fondo

birefnet.safetensors: modelo de eliminación de fondo para el preprocesamiento

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── trellis_2_int8_convrot.safetensors
    │   │      └── pixal3d_int8_convrot.safetensors
    │   ├── 📂 vae/
    │   │      ├── trellis_2_shape_vae_bf16.safetensors
    │   │      └── trellis_2_texture_vae_bf16.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── dino_v3_L_naf_fp32.safetensors
    │   └── 📂 background_removal/
    │          └── birefnet.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/3d/trellis2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/3d/trellis2)

[Pixal3D](https://docs.comfy.org/es/tutorials/3d/pixal3d)[TripoSplat](https://docs.comfy.org/es/tutorials/3d/triposplat)
