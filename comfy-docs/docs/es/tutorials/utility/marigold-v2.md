---
url: https://docs.comfy.org/es/tutorials/utility/marigold-v2/
title: Gu\u00eda de estimaci\u00f3n de profundidad, normales y albedo con Marigold V2 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.103298+00:00
---

# Guía de estimación de profundidad, normales y albedo con Marigold V2 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/marigold-v2/

## En esta página

Volver arriba

  * Instalar el modelo
  * Estimación de profundidad
    * 1\. Pasos para ejecutar
    * 2\. Descargas de modelos
  * Estimación de normales de superficie
    * 1\. Pasos para ejecutar
    * 2\. Descargas de modelos
  * Estimación de albedo
    * 1\. Pasos para ejecutar
    * 2\. Descargas de modelos
  * Nodo de posprocesado de Marigold V2



Depth & 3D

# Guía de estimación de profundidad, normales y albedo con Marigold V2 en ComfyUI

Copiar páginaCopiar página

Estima profundidad, normales y albedo de una sola imagen en ComfyUI con Marigold V2: transformers de difusión Qwen-Image Edit con LoRAs dedicadas.

Copiar páginaCopiar página

Marigold V2 es una familia de modelos de estimación monocular de Huawei Bayer Lab que reutilizan un diffusion transformer (Qwen-Image Edit 2509) para la estimación de geometría e imágenes intrínsecas. A partir de una sola imagen RGB, los modelos predicen un mapa de profundidad, normales de superficie o albedo, dando continuidad al Marigold original (CVPR 2024), que reutilizó Stable Diffusion para esa misma tarea. Los modelos V2 se distribuyen como LoRA sobre un modelo de difusión base compartido, lo que mantiene pequeña cada descarga y hace que la estructura del flujo de trabajo sea idéntica en las tres tareas. En comparación con las redes de profundidad clásicas, el enfoque basado en difusión produce predicciones nítidas y conscientes de los bordes, y generaliza a imágenes de dominio abierto sin reentrenamiento. Entre los usos típicos están el control guiado por profundidad para la generación de imágenes y video, los pipelines de reconstrucción de escenas 3D, el relighting y la edición de materiales a partir del albedo estimado. Marigold V2 es compatible de forma nativa con ComfyUI. Actualiza a la última versión de [ComfyUI](https://github.com/comfyanonymous/ComfyUI) antes de empezar.

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

Instalar el modelo

Cada flujo de trabajo usa cuatro archivos: el modelo de difusión base compartido, más un LoRA, un VAE y un embedding de acondicionamiento específicos de cada tarea. Las tres tareas usan archivos distintos de LoRA, VAE y acondicionamiento, así que cada sección de flujo de trabajo a continuación enlaza los archivos exactos que necesita. El modelo de difusión base se comparte entre los tres flujos de trabajo:

## Modelo de difusión

qwen_image_edit_2509_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

Si planeas ejecutar las tres tareas, descarga los LoRA, VAE y embeddings de acondicionamiento de cada tarea desde las secciones de flujo de trabajo y guárdalos como se indica en cada sección.

## 

​

Estimación de profundidad

Predice un mapa de profundidad a partir de una sola imagen. La predicción decodificada se normaliza para que las superficies cercanas aparezcan claras. ![Vista previa del flujo de trabajo de estimación de profundidad de Marigold V2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_depth_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Depth Estimation: Marigold V2” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## ev_suv_gold_desert_pavilion.png

Nodo `LoadImage` · `ev_suv_gold_desert_pavilion.png`

### 

​

1\. Pasos para ejecutar

  1. Carga tu imagen de entrada en el nodo `LoadImage`
  2. Encola el flujo de trabajo: el modelo base se ejecuta con la LoRA de profundidad y el nodo Marigold V2 Post-Process normaliza la predicción decodificada
  3. Guarda o previsualiza el mapa de profundidad resultante



### 

​

2\. Descargas de modelos

## LoRA de profundidad

marigold_v2_depth_log_stage2.safetensors → ComfyUI/models/loras/

## VAE de profundidad

marigold_v2_depth_log_stage2_vae.safetensors → ComfyUI/models/vae/

## Embedding de condicionamiento de profundidad

marigold_v2_depth_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_depth_log_stage2.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_depth_log_stage2_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_depth_conditioning.safetensors
    

## 

​

Estimación de normales de superficie

Predice normales de superficie por píxel a partir de una sola imagen. La salida asigna a cada píxel la dirección hacia la que mira la superficie, algo útil para el relighting y el análisis de geometría. ![Vista previa del flujo de trabajo de estimación de normales de superficie de Marigold V2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_surface_normal_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Surface Normal Estimation: Marigold V2” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## greek_statue_orange_cloth.png

Nodo `LoadImage` · `greek_statue_orange_cloth.png`

### 

​

1\. Pasos para ejecutar

  1. Carga tu imagen de entrada en el nodo `LoadImage`
  2. Encola el flujo de trabajo con la LoRA de normales cargada
  3. Guarda o previsualiza el mapa de normales resultante



### 

​

2\. Descargas de modelos

## LoRA de normales

marigold_v2_normals.safetensors → ComfyUI/models/loras/

## VAE de normales

marigold_v2_normals_vae.safetensors → ComfyUI/models/vae/

## Embedding de condicionamiento de normales

marigold_v2_normals_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_normals.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_normals_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_normals_conditioning.safetensors
    

## 

​

Estimación de albedo

Predice el albedo (el color intrínseco) de una sola imagen, separando el color del material de la iluminación y el sombreado. El nodo Marigold V2 Post-Process convierte la salida a sRGB. ![Vista previa del flujo de trabajo de estimación de albedo de Marigold V2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_albedo_estimation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Albedo Estimation: Marigold V2” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## flower_with_texture.png

Nodo `LoadImage` · `flower_with_texture.png`

### 

​

1\. Pasos para ejecutar

  1. Carga tu imagen de entrada en el nodo `LoadImage`
  2. Encola el flujo de trabajo con la LoRA de albedo cargada
  3. Guarda o previsualiza la imagen de albedo resultante



### 

​

2\. Descargas de modelos

## LoRA de albedo

marigold_v2_albedo.safetensors → ComfyUI/models/loras/

## VAE de albedo

marigold_v2_albedo_vae.safetensors → ComfyUI/models/vae/

## Embedding de condicionamiento de albedo

marigold_v2_albedo_conditioning.safetensors → ComfyUI/models/embeddings/
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 loras/
    │   │   └── marigold_v2_albedo.safetensors
    │   ├── 📂 vae/
    │   │   └── marigold_v2_albedo_vae.safetensors
    │   └── 📂 embeddings/
    │       └── marigold_v2_albedo_conditioning.safetensors
    

## 

​

Nodo de posprocesado de Marigold V2

Todos los flujos de trabajo terminan en el nodo **Marigold V2 Post-Process** , que convierte la predicción decodificada sin procesar en una imagen que puedes ver. La opción **prediction** debe coincidir con la tarea:

  * **depth** : normaliza la predicción para que las superficies cercanas aparezcan claras
  * **normals** : asigna los valores sin procesar a normales de superficie unitarias
  * **albedo** : convierte la predicción a sRGB



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/marigold-v2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/marigold-v2)

[Detección de poses con SDPose](https://docs.comfy.org/es/tutorials/utility/pose-detection-sdpose)[Depth Anything 3](https://docs.comfy.org/es/tutorials/utility/depth-anything-3)
