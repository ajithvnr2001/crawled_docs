---
url: https://docs.comfy.org/es/tutorials/image/nvidia/pid-latent-upscale/
title: Ejemplo de flujo de trabajo de PiD Latent Upscale en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.265264+00:00
---

# Ejemplo de flujo de trabajo de PiD Latent Upscale en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/nvidia/pid-latent-upscale/

## En esta página

Volver arriba

  * Cómo funciona PiD
    * Checkpoints de PiD disponibles
    * Configuraciones del subgrafo
    * Pasos para ejecutar
  * Descargas de modelos
    * Ubicación de almacenamiento de los modelos
    * Salida de ejemplo



PixelDiT

# Ejemplo de flujo de trabajo de PiD Latent Upscale en ComfyUI

Copiar páginaCopiar página

PiD (Pixel Diffusion Decoder) convierte un latente de difusión en una imagen 4x en 4 pasos destilados en espacio de píxeles. No requiere decodificación VAE aparte.

Copiar páginaCopiar página

**PiD (Pixel Diffusion Decoder)** convierte un **latente** de difusión en una **imagen con superresolución 4x** en 4 pasos destilados en el espacio de píxeles. No se necesita una decodificación VAE aparte. Este flujo de trabajo muestra cómo usar PiD para hacer upscale de un latente de Z-Image-Turbo de **1024px a 4096px**. **Enlaces relacionados** :

  * [Comfy-Org/PixelDiT en Hugging Face](https://huggingface.co/Comfy-Org/PixelDiT)
  * [nvidia/PixelDiT-1300M-1024px (lanzamiento oficial)](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)

![Vista previa del flujo de trabajo PiD Latent Upscale](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-1.webp)

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

Descarga el JSON o busca “Image Upscale: PiD Latent Decode” en la Biblioteca de plantillas

## 

​

Cómo funciona PiD

PiD hace coincidir los checkpoints según el **espacio latente / VAE** del modelo anterior (el lado del codificador), no solo por el nombre del modelo de difusión. Debes seleccionar el checkpoint de PiD que corresponda al espacio latente del modelo usado para la generación inicial. Este flujo de trabajo usa **Z-Image-Turbo** (latente de 1024px a salida de 4096px), que comparte el VAE de 16 canales de Flux.1.

## Conoce el Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y ampliar el flujo de trabajo.

### 

​

Checkpoints de PiD disponibles

Todos los checkpoints se descargan desde [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT) en `models/diffusion_models/`.

Checkpoint| Entrada a salida| Latente compatible (VAE base)  
---|---|---  
[`pid_flux1_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_512_to_2048_4step_bf16.safetensors)| 512 a 2048| VAE de 16 canales de Flux1-dev (Flux.1, Z-Image)  
[`pid_flux1_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_1024_to_4096_4step_bf16.safetensors)| 1024 a 4096| VAE de 16 canales de Flux1-dev (Flux.1, Z-Image) **(este flujo de trabajo)**  
[`pid_flux2_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_512_to_2048_4step_bf16.safetensors)| 512 a 2048| VAE de 128 canales de Flux2-dev (Flux.2)  
[`pid_flux2_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_1024_to_4096_4step_bf16.safetensors)| 1024 a 4096| VAE de 128 canales de Flux2-dev (Flux.2)  
[`pid_sd3_512_to_2048_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_512_to_2048_4step_bf16.safetensors)| 512 a 2048| VAE de 16 canales de SD3 medium  
[`pid_sd3_1024_to_4096_4step_bf16`](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_1024_to_4096_4step_bf16.safetensors)| 1024 a 4096| VAE de 16 canales de SD3 medium  
  
### 

​

Configuraciones del subgrafo

Configura estos valores en el subgrafo **Latent Upscale Decode (PiD)** :

Configuración| Valor| Descripción  
---|---|---  
`latent_format`| `flux`| `flux` para Flux.1/Flux.2/Z-Image, `sd3` para SD3 (Flux.2 se detecta automáticamente por sus 128 canales)  
`degrade_sigma`| `0.0`| Qué tan “finalizado” está el latente de entrada. `0.0` para totalmente denoised (predeterminado), `0.1–0.8` para parcialmente denoised, `1.0` para ruido puro  
  
### 

​

Pasos para ejecutar

  1. **Genera un latente**. Usa un flujo de trabajo T2I (por ejemplo, Z-Image-Turbo) para producir una imagen latente.
  2. **Conecta con PiD**. Introduce el latente en el nodo de subgrafo **Latent Upscale Decode (PiD)**.
  3. **Selecciona el checkpoint**. Elige el checkpoint de PiD que coincida con el espacio latente del VAE de tu modelo anterior.
  4. **Define el tamaño de salida**. Ajusta el tamaño de salida de PiD a **4x** la resolución del latente de entrada.
  5. **Ejecuta**. El subgrafo decodifica y aplica upscale en una sola pasada de 4 pasos.



## 

​

Descargas de modelos

PiD forma parte de la familia de modelos PixelDiT. Este flujo de trabajo también requiere el modelo Z-Image-Turbo para la generación inicial.

## PiD Flux.1 1024 to 4096

pid_flux1_1024_to_4096_4step_bf16.safetensors: checkpoint de PiD para el espacio latente de Flux.1 / Z-Image

## Modelo de difusión Z-Image-Turbo

z_image_turbo_bf16.safetensors: se usa para la generación inicial antes del upscale con PiD

## Codificador de texto (Z-Image)

qwen_3_4b.safetensors: codificador de texto para Z-Image-Turbo

## VAE (Z-Image)

ae.safetensors: VAE para Z-Image-Turbo

## Codificador de texto (PiD)

gemma_2_2b_it_elm_fp8_scaled.safetensors: codificador de texto para el CLIPLoader del subgrafo de PiD (type: pixeldit)

> PiD usa un VAE **pixel_space** integrado. No hace falta ningún archivo VAE aparte para PiD.

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_3_4b.safetensors
    │   │      └── gemma_2_2b_it_elm_fp8_scaled.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── pid_flux1_1024_to_4096_4step_bf16.safetensors
    │   │      └── z_image_turbo_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

### 

​

Salida de ejemplo

![Salida de ejemplo de PiD](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-2.webp)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/nvidia/pid-latent-upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/nvidia/pid-latent-upscale)

[PixelDiT](https://docs.comfy.org/es/tutorials/image/pixeldit/pixeldit)[Krea 2](https://docs.comfy.org/es/tutorials/image/krea/krea-2)
