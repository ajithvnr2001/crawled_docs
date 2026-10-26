---
url: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-2512/
title: Ejemplo de flujo de trabajo nativo de ComfyUI con Qwen-Image-2512 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.098349+00:00
---

# Ejemplo de flujo de trabajo nativo de ComfyUI con Qwen-Image-2512 - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-2512/

## En esta página

Volver arriba

  * Relaciones de aspecto compatibles
  * Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-2512
    * Qwen Image 2512
    * 1\. Archivo del flujo de trabajo
    * 2\. Descarga del modelo



Qwen

# Ejemplo de flujo de trabajo nativo de ComfyUI con Qwen-Image-2512

Copiar páginaCopiar página

Genera imágenes con Qwen-Image-2512 en ComfyUI, la actualización de diciembre de Qwen-Image con más realismo humano, detalles naturales más finos y mejor texto.

Copiar páginaCopiar página

**Qwen-Image-2512** es la actualización de diciembre del modelo fundacional de texto a imagen de Qwen-Image. En comparación con el modelo base Qwen-Image lanzado en agosto, Qwen-Image-2512 presenta mejoras significativas en la calidad de imagen y el realismo. **Mejoras clave en Qwen-Image-2512** :

  * **Realismo humano mejorado** : reduce de forma significativa el aspecto de “generado por IA” y aumenta sustancialmente el realismo general de la imagen, especialmente en sujetos humanos
  * **Detalle natural más fino** : ofrece un renderizado notablemente más detallado de paisajes, pelaje de animales y otros elementos naturales
  * **Renderizado de texto mejorado** : mejora la precisión y la calidad de los elementos textuales, logrando una mejor disposición y una composición multimodal (texto + imagen) más fiel

**Enlaces oficiales** :

  * [Repositorio de GitHub](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2512)
  * [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-2512)
  * [Informe técnico](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
  * [Blog](https://qwen.ai/blog?id=qwen-image-2512)



## 

​

Relaciones de aspecto compatibles

Relación de aspecto| Resolución  
---|---  
1:1| 1328x1328  
16:9| 1664x928  
9:16| 928x1664  
4:3| 1472x1104  
3:4| 1104x1472  
3:2| 1584x1056  
2:3| 1056x1584  
  
## 

​

Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-2512

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

Qwen Image 2512

Modelo de texto a imagen con mayor realismo humano, detalles naturales más finos y mejor renderizado de texto. ![Vista previa del flujo de trabajo de Qwen-Image-2512](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen-Image-2512” en la Biblioteca de plantillas

**Ejemplo de salida** ![Ejemplo de salida de Qwen-Image-2512](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_Image_2512.png)

### 

​

1\. Archivo del flujo de trabajo

Después de actualizar ComfyUI, puedes encontrar el archivo del flujo de trabajo en las plantillas, o arrastrar la vista previa del flujo de trabajo de arriba a ComfyUI para cargarlo. El flujo de trabajo incluye dos subgrafos:

  * **Text to Image (Qwen-Image 2512)** : generación estándar de 50 pasos
  * **Text to Image (Qwen-Image 2512 4steps)** : generación acelerada de 4 pasos usando el LoRA Lightning



### 

​

2\. Descarga del modelo

**Codificadores de texto**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA (opcional, para la aceleración Lightning de 4 pasos)**

  * [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

**Modelos de difusión**

  * [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (Recomendado para la mayoría de usuarios)
  * [qwen_image_2512_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_2512_bf16.safetensors) (Si tienes suficiente VRAM y quieres mejor calidad)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   ├── 📂 loras/
    │   │      └── Qwen-Image-Lightning-4steps-V1.0.safetensors
    │   ├── 📂 diffusion_models/
    │   │      ├── qwen_image_2512_bf16.safetensors
    │   │      └── qwen_image_2512_fp8_e4m3fn.safetensors
    │   └── 📂 vae/
    │          └── qwen_image_vae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/qwen/qwen-image-2512.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/qwen/qwen-image-2512)

[Qwen-Image](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image)[Qwen-Image-Edit](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit)
