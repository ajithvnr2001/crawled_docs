---
url: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit/
title: Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.810302+00:00
---

# Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-Edit - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit/

## En esta página

Volver arriba

  * Transmisión en vivo de ComfyOrg Qwen-Image-Edit
  * Ejemplo de flujo de trabajo nativo de ComfyUI con Qwen-Image-Edit
    * Qwen Image Edit
    * 1\. Archivo del flujo de trabajo
    * 2\. Descarga de modelos
    * 3\. Seguir los pasos para completar el flujo de trabajo
  * Qwen Image Edit 2509
    * Descarga de modelos



Qwen

# Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-Edit

Copiar páginaCopiar página

Qwen-Image-Edit es la versión de edición de Qwen-Image, entrenada sobre el modelo de 20B, con edición precisa de texto y edición semántica y de apariencia.

Copiar páginaCopiar página

**Qwen-Image-Edit** es la versión de edición de imágenes de Qwen-Image. Está entrenado adicionalmente a partir del modelo Qwen-Image de 20B, y logra extender las capacidades únicas de renderizado de texto de Qwen-Image a las tareas de edición, lo que permite una edición precisa del texto. Además, Qwen-Image-Edit introduce la imagen de entrada tanto en Qwen2.5-VL (para el control semántico visual) como en el VAE Encoder (para el control de apariencia visual), y así consigue capacidades de edición tanto semántica como de apariencia. **Características del modelo** Las características incluyen:

  * Edición precisa de texto: Qwen-Image-Edit admite la edición de texto bilingüe (chino e inglés), lo que permite añadir, eliminar y modificar texto directamente en las imágenes conservando el tamaño, la fuente y el estilo originales.
  * Edición dual semántica y de apariencia: Qwen-Image-Edit admite no solo la edición visual de bajo nivel (como la transferencia de estilo, la adición, la eliminación o la modificación de elementos), sino también la edición semántica visual de alto nivel (como la creación de IP, la rotación de objetos, etc.).
  * Rendimiento sólido en múltiples benchmarks: las evaluaciones en varios benchmarks públicos muestran que Qwen-Image-Edit alcanza el estado del arte (SOTA) en tareas de edición, lo que lo convierte en un modelo base potente para la generación de imágenes.

**Enlaces oficiales** :

  * [Repositorio de GitHub](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit)
  * [ModelScope](https://modelscope.cn/models/qwen/Qwen-Image-Edit)



## 

​

Transmisión en vivo de ComfyOrg Qwen-Image-Edit

## 

​

Ejemplo de flujo de trabajo nativo de ComfyUI con Qwen-Image-Edit

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

Qwen Image Edit

Edita imágenes con edición de texto bilingüe precisa y capacidades de edición semántica y de apariencia duales usando el modelo MMDiT de 20B de Qwen-Image-Edit. ![Vista previa del flujo de trabajo Qwen-Image-Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en GPU en la nube sin configuración

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen Image Edit” en la biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## image_qwen_image_edit_input_image.png

Nodo `LoadImage` 78 · `image_qwen_image_edit_input_image.png`

![image_qwen_image_edit_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_qwen_image_edit_input_image.png)

**Resultado de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_qwen_image_edit_input_image.png)![Resultado de ejemplo de Qwen-Image-Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_image_edit.jpg)

### 

​

1\. Archivo del flujo de trabajo

### 

​

2\. Descarga de modelos

Todos los modelos están disponibles en [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) o [Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI) **Modelo de difusión**

  * [qwen_image_edit_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_fp8_e4m3fn.safetensors)

**LoRA**

  * [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors)

**Codificador de texto**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── qwen_image_edit_fp8_e4m3fn.safetensors
    │   ├── 📂 loras/
    │   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    

### 

​

3\. Seguir los pasos para completar el flujo de trabajo

![Diagrama de pasos](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/qwen/qwen_image_edit.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=98a706bfa8f1578a4dfd7f2a0a415926)

  1. Carga de modelos 
     * Asegúrate de que el nodo `Load Diffusion Model` cargue `qwen_image_edit_fp8_e4m3fn.safetensors`
     * Asegúrate de que el nodo `Load CLIP` cargue `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * Asegúrate de que el nodo `Load VAE` cargue `qwen_image_vae.safetensors`
  2. Carga de imagen 
     * Asegúrate de que el nodo `Load Image` tenga subida la imagen que quieres editar
  3. Configuración del prompt 
     * Define el prompt en el nodo `CLIP Text Encoder`
  4. El nodo `Scale Image to Total Pixels` escalará tu imagen de entrada a un total de un millón de píxeles, 
     * Principalmente para evitar la pérdida de calidad en las imágenes de salida causada por imágenes de entrada demasiado grandes, como 2048x2048
     * Si conoces bien el tamaño de tu imagen de entrada, puedes omitir este nodo con `Ctrl+B`
  5. Si quieres usar la LoRA Lightning de 4 pasos para acelerar la generación de imágenes, puedes seleccionar el nodo `LoraLoaderModelOnly` y presionar `Ctrl+B` para activarla
  6. Para las configuraciones `steps` y `cfg` del nodo KSampler, agregamos una nota debajo del nodo donde puedes probar las configuraciones de parámetros óptimas
  7. Haz clic en el botón `Queue`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Qwen Image Edit 2509

Qwen-Image-Edit-2509 es la siguiente iteración de Qwen-Image-Edit. Mantiene la edición precisa de texto bilingüe del modelo original y agrega entrada de varias imágenes, ediciones más consistentes a lo largo de una serie de imágenes y compatibilidad con ControlNet, así que puedes editar una imagen tomando otras como referencia. ![Vista previa del flujo de trabajo de Qwen Image Edit 2509](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen Image Edit 2509” en la biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` que corresponda:

## image_qwen_image_edit_2509_input_image.png

Nodo `LoadImage` 78 · `image_qwen_image_edit_2509_input_image.png`

### 

​

Descarga de modelos

**Modelo de difusión**

  * [qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors)

**LoRA (opcional, para la aceleración Lightning de 4 pasos)**

  * [Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors)

**Codificador de texto**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── qwen_image_edit_2509_fp8_e4m3fn.safetensors
    │   ├── 📂 loras/
    │   │   └── Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/qwen/qwen-image-edit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/qwen/qwen-image-edit)

[Qwen-Image-2512](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-2512)[Qwen-Image-Layered](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-layered)
