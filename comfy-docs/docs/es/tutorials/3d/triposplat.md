---
url: https://docs.comfy.org/es/tutorials/3d/triposplat/
title: Ejemplo de flujo de trabajo de TripoSplat de imagen a Gaussian splat en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:40.854305+00:00
---

# Ejemplo de flujo de trabajo de TripoSplat de imagen a Gaussian splat en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/3d/triposplat/

## En esta página

Volver arriba

  * TripoSplat: de imagen a Gaussian splat
  * Cómo funciona
  * Guía de nodos del flujo de trabajo
    * LoadImage
    * TripoSplat (subgrafo)
    * CreateCameraInfo
    * RenderSplat
    * SplatToMesh
    * SaveGLB
    * SaveVideo
    * SplatToFile3D
    * CreateVideo
  * Pasos para ejecutar
  * Opciones de salida
  * Descarga de modelos
    * Ubicación de almacenamiento de los modelos



3D

# Ejemplo de flujo de trabajo de TripoSplat de imagen a Gaussian splat en ComfyUI

Copiar páginaCopiar página

Genera representaciones 3D Gaussian splat de alta calidad desde una sola imagen 2D con TripoSplat, con densidad y presupuesto controlables para el renderizado.

Copiar páginaCopiar página

**TripoSplat** es un modelo de código abierto que genera representaciones de **Gaussian splat 3D** directamente a partir de una sola imagen 2D. Fue desarrollado por VAST-AI y publicado bajo una licencia de código abierto. A diferencia de los métodos tradicionales de reconstrucción 3D, que requieren múltiples vistas o generan mallas como resultado principal, TripoSplat crea representaciones de **Gaussian splat** : una técnica de renderizado en la que se colocan miles de gaussianas 3D con color en el espacio para representar una escena. Este enfoque permite un renderizado rápido y de alta calidad, con densidad y presupuesto controlables.

### 

​

TripoSplat: de imagen a Gaussian splat

Sube una sola imagen 2D. Genera una representación de Gaussian splat 3D de alta calidad con densidad y presupuesto controlables para el renderizado. ![Vista previa del flujo de trabajo de TripoSplat](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_triposplat_image_to_gaussian_splat-1.webp)

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

Descarga el JSON o busca “TripoSplat: Image to Gaussian Splat” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## white-hotel-on-rocky-island.png

Nodo `LoadImage` 99 · `white-hotel-on-rocky-island.png`

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/white-hotel-on-rocky-island.png)

## 

​

Cómo funciona

TripoSplat usa una **arquitectura feed-forward** que toma una sola imagen RGB y predice directamente un conjunto de primitivas Gaussianas 3D. El pipeline implica:

  1. **Codificación de imagen** : la imagen de entrada se procesa con un codificador visual (DINOv2).
  2. **Generación de triplanos** : las características se decodifican en una representación de triplanos.
  3. **Predicción de Gaussianas** : se muestrea el triplano para producir los parámetros de las Gaussianas (posición, escala, rotación, opacidad, color).
  4. **Renderizado** : las Gaussianas se renderizan desde puntos de vista arbitrarios mediante splatting diferenciable.



## Acerca de Subgraph

Este flujo de trabajo usa un nodo Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

## 

​

Guía de nodos del flujo de trabajo

### 

​

LoadImage

  * Carga tu imagen de entrada (PNG/JPG)
  * Imagen de muestra: `white-hotel-on-rocky-island.png` (disponible en la Biblioteca de plantillas)



### 

​

TripoSplat (subgrafo)

El nodo de subgrafo principal procesa la imagen y genera el splat gaussiano 3D. Parámetros expuestos:

Parámetro| Predeterminado| Descripción  
---|---|---  
`switch`| N/D| Habilita o deshabilita el subgrafo  
`num_gaussians`| N/D| Número de primitivas gaussianas a generar (controla calidad/rendimiento)  
`seed`| N/D| Semilla aleatoria para reproducibilidad  
`unet_name`| N/D| Checkpoint del modelo diffusion TripoSplat  
`clip_name`| N/D| Modelo codificador de visión CLIP  
`vae_name`| N/D| VAE para codificar/decodificar (2 entradas: una para el VAE principal y otra para el codificador)  
`bg_removal_name`| N/D| Modelo de eliminación de fondo  
  
### 

​

CreateCameraInfo

  * Define la órbita de la cámara para renderizar el resultado
  * Parámetros: tipo de órbita, ángulo, distancia, campo de visión, etc.
  * Predeterminado: órbita con elevación de 35°, distancia de 30 y zoom de 2.5



### 

​

RenderSplat

  * Renderiza el splat gaussiano en una imagen 2D desde el ángulo de cámara definido
  * Parámetros: resolución de salida (predeterminado 1024×1024), configuraciones de calidad de imagen



### 

​

SplatToMesh

  * Convierte el splat gaussiano en una malla (opcional)
  * Parámetros: densidad de la malla, suavizado y simplificación



### 

​

SaveGLB

  * Guarda el resultado como un archivo GLB 3D



### 

​

SaveVideo

  * Guarda un video de la escena 3D renderizada



### 

​

SplatToFile3D

  * Exporta el splat gaussiano en formato SPZ



### 

​

CreateVideo

  * Crea un video a partir de los fotogramas renderizados



## 

​

Pasos para ejecutar

  1. **Carga una imagen** : usa el nodo **LoadImage** para cargar una sola imagen 2D
  2. **Ejecuta el subgrafo TripoSplat** : el modelo generará una representación Gaussian splat
  3. **Elige el formato de salida** : exporta como GLB, SPZ, video o renderiza a malla
  4. **Consulta los resultados** : usa el archivo 3D creado o la vista previa renderizada



## 

​

Opciones de salida

Nodo| Formato| Caso de uso  
---|---|---  
**SaveGLB**| `.glb`| Formato de archivo 3D estándar, importable en software 3D  
**SplatToFile3D**| `.spz`| Formato comprimido de Gaussian splat para un almacenamiento eficiente  
**RenderSplat**|  Imagen 2D| Vista previa rápida del resultado desde cualquier ángulo  
**SplatToMesh**|  Malla| Convierte a una malla tradicional para seguir editando  
  
## 

​

Descarga de modelos

Descarga el modelo de TripoSplat y los archivos necesarios. Colócalos en los subdirectorios correspondientes de `models/`.

## TripoSplat diffusion

triposplat_fp16.safetensors: checkpoint del modelo de difusión de TripoSplat

## TripoSplat VAE decoder

triposplat_vae_decoder_fp16.safetensors: decodificador VAE

## Flux2 VAE

flux2-vae.safetensors: VAE de FLUX.2 para la codificación latente

## DINOv2 CLIP

dino_v3_vit_h.safetensors: codificador de visión CLIP (DINOv2)

## BiRefNet bg removal

birefnet.safetensors: modelo de eliminación de fondo para el preprocesamiento

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      └── triposplat_fp16.safetensors
    │   ├── 📂 vae/
    │   │      ├── triposplat_vae_decoder_fp16.safetensors
    │   │      └── flux2-vae.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── dino_v3_vit_h.safetensors
    │   └── 📂 background_removal/
    │          └── birefnet.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/3d/triposplat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/3d/triposplat)

[TRELLIS.2](https://docs.comfy.org/es/tutorials/3d/trellis2)[Hunyuan3D-2](https://docs.comfy.org/es/tutorials/3d/hunyuan3D-2)
