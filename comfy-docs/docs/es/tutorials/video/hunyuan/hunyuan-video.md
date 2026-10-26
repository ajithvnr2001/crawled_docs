---
url: https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video/
title: Ejemplos de Hunyuan Video en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:59.063102+00:00
---

# Ejemplos de Hunyuan Video en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video/

## En esta página

Volver arriba

  * Modelos comunes para todos los flujos de trabajo
  * Flujo de trabajo de texto a video con Hunyuan
    * 1\. Flujo de trabajo
    * 2\. Instalación manual de los modelos
    * 3\. Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de imagen a video de Hunyuan
    * Modelo compartido para las versiones v1 y v2
    * Flujo de trabajo imagen a video V1 “concat”
    * 1\. Flujo de trabajo y recursos
    * 2\. Instalación manual de los modelos relacionados
    * 3\. Pasos para ejecutar el flujo de trabajo
    * Flujo de trabajo de imagen a video v2 “replace”
    * 1\. Flujo de trabajo y recursos
    * 2\. Instalación manual de modelos relacionados
    * 3\. Pasos para ejecutar el flujo de trabajo
  * Pruébalo tú mismo



Hunyuan

# Ejemplos de Hunyuan Video en ComfyUI

Copiar páginaCopiar página

Guía para usar los flujos de trabajo texto a video e imagen a video de Hunyuan en ComfyUI

Copiar páginaCopiar página

La serie Hunyuan Video está desarrollada y publicada como código abierto por [Tencent](https://huggingface.co/tencent). Presenta una arquitectura híbrida que admite tanto la generación de [texto a video](https://github.com/Tencent/HunyuanVideo) como de [imagen a video](https://github.com/Tencent/HunyuanVideo-I2V), con una escala de parámetros de 13B. Características técnicas:

  * **Arquitectura principal:** utiliza una arquitectura DiT (Diffusion Transformer) similar a Sora, que fusiona de forma eficaz la información de texto, imagen y movimiento para mejorar la coherencia, la calidad y la alineación entre los fotogramas del video generado. Un mecanismo de atención completa unificado permite transiciones de cámara con múltiples vistas y, al mismo tiempo, garantiza la coherencia del sujeto.
  * **VAE 3D:** el VAE 3D personalizado comprime los videos en un espacio latent compacto, lo que hace más eficiente la generación de imagen a video.
  * **Alineación superior entre imagen, video y texto:** emplea codificadores de texto MLLM que destacan tanto en la generación de imágenes como de videos, siguen mejor las instrucciones de texto, capturan detalles y realizan razonamientos complejos.

Puedes aprender más en los repositorios oficiales: [Hunyuan Video](https://github.com/Tencent/HunyuanVideo) y [Hunyuan Video-I2V](https://github.com/Tencent/HunyuanVideo-I2V). Esta guía te mostrará cómo configurar los flujos de trabajo de **texto a video** y de **imagen a video** en ComfyUI.

Las imágenes de los flujos de trabajo de este tutorial contienen metadatos con la información de descarga de los modelos.Solo tienes que arrastrarlas a ComfyUI o usar el menú `Workflows` -> `Open (ctrl+o)` para cargar el flujo de trabajo correspondiente, que te pedirá descargar los modelos requeridos.Como alternativa, esta guía ofrece enlaces directos a los modelos por si fallan las descargas automáticas o si no usas la versión Desktop. Todos los modelos están disponibles [aquí](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files) para descargar.

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

Modelos comunes para todos los flujos de trabajo

Los siguientes modelos se usan tanto en los flujos de trabajo de texto a video como en los de imagen a video. Descárgalos y guárdalos en los directorios indicados:

## Text Encoder: clip_l.safetensors

Guárdalo en ComfyUI/models/text_encoders

## Text Encoder: llava_llama3_fp8_scaled.safetensors

Guárdalo en ComfyUI/models/text_encoders

## VAE: hunyuan_video_vae_bf16.safetensors

Guárdalo en ComfyUI/models/vae

Ubicación de almacenamiento:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── llava_llama3_fp8_scaled.safetensors
    │   └── vae/
    │       └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Flujo de trabajo de texto a video con Hunyuan

Hunyuan Text-to-Video se publicó como código abierto en diciembre de 2024 y permite generar videos cortos de 5 segundos mediante descripciones en lenguaje natural, tanto en chino como en inglés.

### 

​

1\. Flujo de trabajo

Descarga la imagen del flujo de trabajo que aparece a continuación y arrástrala a ComfyUI para cargarlo: ![ComfyUI Workflow - Hunyuan Text-to-Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hunyuan_video_text_to_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Hunyuan Video” en la Biblioteca de plantillas

### 

​

2\. Instalación manual de los modelos

## Modelo de difusión: hunyuan_video_t2v_720p_bf16.safetensors

Guarda el archivo en ComfyUI/models/diffusion_models

Asegúrate de tener todos estos archivos de modelo en las ubicaciones correctas:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                       // Modelo compartido
    │   │   └── llava_llama3_fp8_scaled.safetensors      // Modelo compartido
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors       // Modelo compartido
    │   └── diffusion_models/
    │       └── hunyuan_video_t2v_720p_bf16.safetensors  // Modelo T2V
    

### 

​

3\. Pasos para ejecutar el flujo de trabajo

![ComfyUI Hunyuan Video T2V Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_t2v.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=8cf9db23e82c1c31702966878d7d6326)

  1. Comprueba que el nodo `DualCLIPLoader` tenga cargados estos modelos: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Comprueba que el nodo `Load Diffusion Model` tenga cargado `hunyuan_video_t2v_720p_bf16.safetensors`
  3. Comprueba que el nodo `Load VAE` tenga cargado `hunyuan_video_vae_bf16.safetensors`
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



Cuando el parámetro `length` del nodo `EmptyHunyuanLatentVideo` se establece en 1, el modelo puede generar una imagen estática.

## 

​

Flujo de trabajo de imagen a video de Hunyuan

El modelo Hunyuan Image-to-Video se publicó como código abierto el 6 de marzo de 2025, basado en el framework HunyuanVideo. Transforma imágenes estáticas en videos suaves y de alta calidad, y también ofrece código de entrenamiento de LoRA para personalizar efectos de video especiales como el crecimiento del cabello, la transformación de objetos y más. Actualmente, el modelo Hunyuan Image-to-Video tiene dos versiones:

  * v1 “concat”: mejor fluidez de movimiento, pero menor adherencia a la orientación de la imagen
  * v2 “replace”: actualizada al día siguiente de la v1, con mejor orientación de la imagen, pero al parecer menos dinámica en comparación con la v1



v1 “concat”

![HunyuanVideo v1](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video.webp)

v2 “replace”

![HunyuanVideo v2](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/hunyuan_video_image_to_video_v2.webp)

### 

​

Modelo compartido para las versiones v1 y v2

## CLIP Vision: llava_llama3_vision.safetensors

Guardar en ComfyUI/models/clip_vision

### 

​

Flujo de trabajo imagen a video V1 “concat”

#### 

​

1\. Flujo de trabajo y recursos

Descarga la imagen del flujo de trabajo que aparece a continuación y arrástrala a ComfyUI para cargar el flujo de trabajo: ![Flujo de trabajo de ComfyUI - Hunyuan imagen a video v1](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v1_robot.webp)

## Descargar flujo de trabajo

Descarga la imagen del flujo de trabajo y arrástrala a ComfyUI

Descarga la imagen a continuación y úsala como fotograma inicial para la generación de imagen a video:

## Fotograma inicial: robot-ballet.png

Guárdala y úsala como imagen de entrada para la generación I2V

#### 

​

2\. Instalación manual de los modelos relacionados

## Modelo de difusión: hunyuan_video_image_to_video_720p_bf16.safetensors

Guarda en ComfyUI/models/diffusion_models

Asegúrate de tener todos estos archivos de modelo en las ubicaciones correctas:
    
    
    ComfyUI/
    ├── models/
    │   ├── clip_vision/
    │   │   └── llava_llama3_vision.safetensors                     // Modelo compartido de I2V
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                                  // Modelo compartido
    │   │   └── llava_llama3_fp8_scaled.safetensors                 // Modelo compartido
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors                  // Modelo compartido
    │   └── diffusion_models/
    │       └── hunyuan_video_image_to_video_720p_bf16.safetensors  // Modelo de la versión I2V v1 "concat"
    

#### 

​

3\. Pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de ComfyUI Hunyuan Video I2V v1](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v1.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=66d1fd271cc2a45a4fbcd92850074912)

  1. Asegúrate de que `DualCLIPLoader` haya cargado estos modelos: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Asegúrate de que `Load CLIP Vision` haya cargado `llava_llama3_vision.safetensors`
  3. Asegúrate de que `Load Image Model` haya cargado `hunyuan_video_image_to_video_720p_bf16.safetensors`
  4. Asegúrate de que `Load VAE` haya cargado `vae_name: hunyuan_video_vae_bf16.safetensors`
  5. Asegúrate de que `Load Diffusion Model` haya cargado `hunyuan_video_image_to_video_720p_bf16.safetensors`
  6. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



### 

​

Flujo de trabajo de imagen a video v2 “replace”

El flujo de trabajo v2 es esencialmente el mismo que el del v1. Solo necesitas descargar el modelo **replace** y usarlo en el nodo `Load Diffusion Model`.

#### 

​

1\. Flujo de trabajo y recursos

Descarga la imagen del flujo de trabajo de abajo y arrástrala a ComfyUI para cargarlo: ![Flujo de trabajo de ComfyUI - Hunyuan imagen a video v2](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/hunyuan-video/i2v/v2_fennec_gril.webp)

## Descargar flujo de trabajo

Descarga la imagen del flujo de trabajo y arrástrala a ComfyUI

Descarga la imagen de abajo y úsala como fotograma inicial para la generación de imagen a video:

## Fotograma inicial: flux_dev_example.png

Guarda y usa como imagen de entrada para la generación I2V

#### 

​

2\. Instalación manual de modelos relacionados

## Modelo de difusión: hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors

Guárdalo en ComfyUI/models/diffusion_models

Asegúrate de tener todos estos archivos de modelo en las ubicaciones correctas:
    
    
    ComfyUI/
    ├── models/
    │   ├── clip_vision/
    │   │   └── llava_llama3_vision.safetensors                                // Modelo compartido de I2V
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors                                             // Modelo compartido
    │   │   └── llava_llama3_fp8_scaled.safetensors                            // Modelo compartido
    │   ├── vae/
    │   │   └── hunyuan_video_vae_bf16.safetensors                             // Modelo compartido
    │   └── diffusion_models/
    │       └── hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors  // Modelo de la versión v2 "replace"
    

#### 

​

3\. Pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de ComfyUI Hunyuan Video I2V v2](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/flow_diagram_i2v_v2.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f26ddd8edc837fbf9d2bb4f6459a82ee)

  1. Asegúrate de que el nodo `DualCLIPLoader` haya cargado estos modelos: 
     * clip_name1: clip_l.safetensors
     * clip_name2: llava_llama3_fp8_scaled.safetensors
  2. Asegúrate de que el nodo `Load CLIP Vision` haya cargado `llava_llama3_vision.safetensors`
  3. Asegúrate de que el nodo `Load Image Model` haya cargado `hunyuan_video_image_to_video_720p_bf16.safetensors`
  4. Asegúrate de que el nodo `Load VAE` haya cargado `hunyuan_video_vae_bf16.safetensors`
  5. Asegúrate de que el nodo `Load Diffusion Model` haya cargado `hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors`
  6. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Pruébalo tú mismo

Aquí tienes algunas imágenes y prompts que proporcionamos. Úsalos tal cual o ajústalos para crear tu propio video. ![example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/humanoid_android_dressed_in_a_flowing.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=16d6b0ea15e14c74e8d2e5bfacfe4bf8)
    
    
    Futuristic robot dancing ballet, dynamic motion, fast motion, fast shot, moving scene
    

* * *

![example](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/advanced/hunyuanvideo/samurai.png?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f8a76a691a7a9ebda088941350538375)
    
    
    Samurai waving sword and hitting the camera. camera angle movement, zoom in, fast scene, super fast, dynamic
    

* * *

![example](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/a_flying_car.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=aa2ce4f30c4d367170a8a696e62a7c7e)
    
    
    flying car fastly moving and flying through the city
    

* * *

![example](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/tutorial/advanced/hunyuanvideo/cyber_car_race.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=875b086bd33ac131bda4fe6c718b9bc7)
    
    
    cyberpunk car race in night city, dynamic, super fast, fast shot
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/hunyuan/hunyuan-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/hunyuan/hunyuan-video)

[Bernini-R](https://docs.comfy.org/es/tutorials/video/bytedance/bernini-r)[HunyuanVideo 1.5](https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video-1-5)
