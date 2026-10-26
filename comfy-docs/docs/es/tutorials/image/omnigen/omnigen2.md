---
url: https://docs.comfy.org/es/tutorials/image/omnigen/omnigen2/
title: Ejemplos de flujos de trabajo nativos de OmniGen2 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.985779+00:00
---

# Ejemplos de flujos de trabajo nativos de OmniGen2 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/omnigen/omnigen2/

## En esta página

Volver arriba

  * Descarga de modelos de OmniGen2
  * Flujo de trabajo de texto a imagen con ComfyUI OmniGen2
    * OmniGen2: Texto a imagen
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
  * Flujo de trabajo de edición de imágenes con ComfyUI OmniGen2
    * Edición de imágenes con OmniGen2
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
    * 3\. Instrucciones adicionales del flujo de trabajo



Imagen

# Ejemplos de flujos de trabajo nativos de OmniGen2 en ComfyUI

Copiar páginaCopiar página

Ejecuta OmniGen2 de forma nativa en ComfyUI para generar imágenes a partir de texto, editar imágenes con instrucciones y combinar varias imágenes.

Copiar páginaCopiar página

OmniGen2 es un modelo de generación multimodal unificado de código abierto del equipo de investigación [VectorSpaceLab](https://github.com/VectorSpaceLab/OmniGen2). Un único conjunto de pesos maneja la generación de texto a imagen, la edición de imágenes guiada por instrucciones y la generación en contexto basada en un sujeto. ComfyUI es compatible con OmniGen2 de forma nativa, por lo que las tres tareas se ejecutan localmente mediante los flujos de trabajo de ejemplo oficiales. El modelo combina un modelo de visión e idioma congelado Qwen2.5-VL de 3B con un transformer de difusión independiente de 4B, alrededor de 7B de parámetros en total. El modelo de visión e idioma lee tus imágenes de referencia y las instrucciones escritas, y el transformer de difusión convierte esa comprensión en píxeles. Como ambas rutas mantienen sus propios parámetros y su propio tokenizer de imágenes, OmniGen2 conserva su capacidad de comprensión visual y mantiene alta la calidad de imagen. ComfyUI incluye dos flujos de trabajo oficiales para el modelo: texto a imagen y edición de imágenes a partir de instrucciones en lenguaje natural como “cambia el vestido a azul”. El flujo de trabajo de edición de imágenes también maneja la composición de varias imágenes, combinando personas, objetos de referencia y escenas de varias imágenes de entrada.

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

**Aspectos destacados del modelo** :

  * **Comprensión visual** : lee y analiza el contenido de las imágenes mediante el modelo base Qwen2.5-VL
  * **Generación de texto a imagen** : crea imágenes de alta fidelidad a partir de prompts de texto
  * **Edición de imágenes guiada por instrucciones** : aplica ediciones complejas a partir de instrucciones en lenguaje natural
  * **Generación en contexto** : combina personas, objetos de referencia y escenas de varias entradas en imágenes nuevas

**Características técnicas** :

  * **Arquitectura de doble ruta** : modelo de texto Qwen2.5-VL de 3B más un transformer de difusión independiente de 4B
  * **Codificación de posición Omni-RoPE** : posicionamiento espacial y distinción de identidad en varias imágenes
  * **Desacoplamiento de parámetros** : evita que la generación de texto autoregresiva degrade la calidad de imagen
  * **Texto dentro de la imagen** : genera contenido de texto legible dentro de la imagen generada



## 

​

Descarga de modelos de OmniGen2

Como este artículo incluye distintos flujos de trabajo, los archivos de modelo correspondientes y sus ubicaciones de instalación son los siguientes. La información de descarga de los archivos de modelo también está incluida en los flujos de trabajo correspondientes: **Modelos de difusión**

  * [omnigen2_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/blob/main/split_files/diffusion_models/omnigen2_fp16.safetensors)

**VAE**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**Codificadores de texto**

  * [qwen_2.5_vl_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors)

Ubicación de guardado de los archivos:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── omnigen2_fp16.safetensors
    │   ├── 📂 vae/
    │   │   └── ae.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen_2.5_vl_fp16.safetensors
    

## 

​

Flujo de trabajo de texto a imagen con ComfyUI OmniGen2

### 

​

OmniGen2: Texto a imagen

Genera imágenes de alta calidad a partir de prompts de texto usando el modelo multimodal unificado de 7B de OmniGen2 con arquitectura de doble ruta. ![Vista previa del flujo de trabajo de texto a imagen de OmniGen2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abre y ejecuta este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “OmniGen2” en la biblioteca de plantillas

**Salida de ejemplo** ![Ejemplo de salida de texto a imagen de OmniGen2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_omnigen2_t2i.png)

### 

​

1\. Descargar el archivo del flujo de trabajo

### 

​

2\. Completar el flujo de trabajo paso a paso

![Guía de pasos del flujo de trabajo](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_t2i_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=0811f0f5d6dbe974749752b85fa7e3b9) Sigue los pasos numerados en la imagen para confirmar paso a paso y garantizar el funcionamiento correcto del flujo de trabajo correspondiente:

  1. **Cargar el modelo principal** : Asegúrate de que el nodo `Load Diffusion Model` cargue `omnigen2_fp16.safetensors`
  2. **Cargar el codificador de texto** : Asegúrate de que el nodo `Load CLIP` cargue `qwen_2.5_vl_fp16.safetensors`
  3. **Cargar VAE** : Asegúrate de que el nodo `Load VAE` cargue `ae.safetensors`
  4. **Establecer las dimensiones de la imagen** : Configura las dimensiones de la imagen generada en el nodo `EmptySD3LatentImage` (se recomienda 1024x1024)
  5. **Introducir los prompts** : 
     * Introduce los prompts positivos en el primer nodo `CLipTextEncode` (contenido que quieres que aparezca en la imagen)
     * Introduce los prompts negativos en el segundo nodo `CLipTextEncode` (contenido que no quieres que aparezca en la imagen)
  6. **Iniciar la generación** : Haz clic en el botón `Queue Prompt` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de texto a imagen
  7. **Ver los resultados** : Cuando finalice la generación, las imágenes correspondientes se guardarán automáticamente en el directorio `ComfyUI/output/`, y también puedes previsualizarlas en el nodo `SaveImage`



## 

​

Flujo de trabajo de edición de imágenes con ComfyUI OmniGen2

OmniGen2 cuenta con amplias capacidades de edición de imágenes y permite agregar texto a las imágenes.

### 

​

Edición de imágenes con OmniGen2

Edita imágenes con instrucciones en lenguaje natural usando las capacidades avanzadas de edición de imágenes de OmniGen2 y su soporte para renderizar texto. ![Vista previa del flujo de trabajo de edición de imágenes con OmniGen2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abre y ejecuta este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “OmniGen2 Image Edit” en la biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## image_omnigen2_image_edit_input_image.png

Nodo `LoadImage` 16 · `image_omnigen2_image_edit_input_image.png`

![image_omnigen2_image_edit_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_omnigen2_image_edit_input_image.png)

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_omnigen2_image_edit_input_image.png)![Salida de ejemplo de edición de imágenes con OmniGen2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_omnigen2_image_edit.png)

### 

​

1\. Descargar el archivo del flujo de trabajo

### 

​

2\. Completar el flujo de trabajo paso a paso

![Guía de pasos del flujo de trabajo](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/image/omnigen/omnigen2_image_edit_step_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=09899794b2d041a8c0e0775da557684a)

  1. **Cargar el modelo principal** : Asegúrate de que el nodo `Load Diffusion Model` cargue `omnigen2_fp16.safetensors`
  2. **Cargar el codificador de texto** : Asegúrate de que el nodo `Load CLIP` cargue `qwen_2.5_vl_fp16.safetensors`
  3. **Cargar VAE** : Asegúrate de que el nodo `Load VAE` cargue `ae.safetensors`
  4. **Subir la imagen** : Sube la imagen proporcionada en el nodo `Load Image`
  5. **Introducir los prompts** : 
     * Ingresa los prompts positivos en el primer nodo `CLipTextEncode` (contenido que quieres que aparezca en la imagen)
     * Ingresa los prompts negativos en el segundo nodo `CLipTextEncode` (contenido que no quieres que aparezca en la imagen)
  6. **Iniciar la generación** : Haz clic en el botón `Queue Prompt`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de texto a imagen
  7. **Ver los resultados** : Cuando finalice la generación, las imágenes correspondientes se guardarán automáticamente en el directorio `ComfyUI/output/`, y también puedes obtener una vista previa de ellas en el nodo `SaveImage`



### 

​

3\. Instrucciones adicionales del flujo de trabajo

  * Si quieres habilitar la segunda entrada de imagen, puedes usar el atajo **Ctrl + B** para habilitar las entradas correspondientes de los nodos que están en estado rosa/morado en el flujo de trabajo
  * Si quieres personalizar las dimensiones, puedes eliminar el nodo `Get image size` conectado al nodo `EmptySD3LatentImage` e ingresar dimensiones personalizadas



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/omnigen/omnigen2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/omnigen/omnigen2)

[Cosmos-Predict2](https://docs.comfy.org/es/tutorials/image/cosmos/cosmos-predict2-t2i)[Pixal3D](https://docs.comfy.org/es/tutorials/3d/pixal3d)
