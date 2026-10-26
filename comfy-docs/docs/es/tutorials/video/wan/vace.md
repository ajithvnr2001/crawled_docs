---
url: https://docs.comfy.org/es/tutorials/video/wan/vace/
title: Ejemplos de video con Wan2.1 VACE en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:00.802270+00:00
---

# Ejemplos de video con Wan2.1 VACE en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/vace/

## En esta página

Volver arriba

  * Acerca de VACE
  * Descarga y carga de modelos en los flujos de trabajo
    * Descarga de modelos
    * Carga de modelos
    * Cómo cambiar el estado Omitir de un nodo
  * 1\. VACE texto a video
    * Wan2.1 VACE texto a video
    * Pasos para ejecutar
  * 2\. VACE imagen a video
    * Wan2.1 VACE referencia a video
    * Pasos para ejecutar
    * Notas adicionales
  * 3\. VACE de video a video
    * Video de control con Wan2.1 VACE
    * Pasos para ejecutar
  * 4\. Inpainting con VACE
    * Inpainting con Wan2.1 VACE
  * 5\. Outpainting de video con VACE
    * Wan2.1 VACE Outpainting
  * 6\. Generación de video con fotograma inicial y final de VACE
    * Wan2.1 VACE First-Last Frame



Wan2.1

# Ejemplos de video con Wan2.1 VACE en ComfyUI

Copiar páginaCopiar página

Cómo completar los ejemplos de generación de video con Wan VACE en ComfyUI

Copiar páginaCopiar página

Como hemos hecho ajustes a la plantilla y agregado el uso y las instrucciones correspondientes para CausVid LoRA, este documento necesita ser actualizado y requiere algo de tiempo de preparación. Mientras tanto, consulta las notas de la plantilla para saber cómo usarla.

## 

​

Acerca de VACE

VACE 14B es un modelo unificado de edición de video de código abierto lanzado por el equipo Tongyi Wanxiang de Alibaba. Al integrar capacidades multitarea, admitir el procesamiento en alta resolución y ofrecer mecanismos flexibles de entrada multimodal, este modelo mejora notablemente la eficiencia y la calidad de la creación de video. El modelo es de código abierto bajo la licencia [Apache-2.0](https://github.com/ali-vilab/VACE?tab=Apache-2.0-1-ov-file) y puedes usarlo con fines personales o comerciales. A continuación, un análisis detallado de sus características principales y sus aspectos técnicos más destacados:

  * Entrada multimodal: admite varias formas de entrada, como texto, imágenes, video, máscaras y señales de control
  * Arquitectura unificada: un solo modelo admite múltiples tareas con funciones que puedes combinar libremente
  * Transferencia de movimiento: genera acciones coherentes a partir de videos de referencia
  * Reemplazo local: reemplaza áreas específicas del video mediante máscaras
  * Extensión de video: completa acciones o extiende fondos
  * Reemplazo de fondo: conserva al sujeto y cambia el fondo del entorno

Actualmente VACE tiene dos versiones publicadas: 1.3B y 14B. En comparación con la versión 1.3B, la versión 14B admite salida en resolución 720P, con mejores detalles de imagen y mayor estabilidad.

Modelo| 480P| 720P  
---|---|---  
[VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B)| ✅| ❌  
[VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)| ✅| ✅  
  
Pesos de modelo y repositorios de código relacionados:

## VACE-1.3B

Pesos del modelo 1.3B en Hugging Face

## VACE-14B

Pesos del modelo 14B en Hugging Face

## Repositorio de GitHub

Código fuente y documentación de VACE

## Página del proyecto VACE

Página oficial del proyecto con ejemplos

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

Descarga y carga de modelos en los flujos de trabajo

Dado que todos los flujos de trabajo que se tratan en este documento usan la misma plantilla, primero podemos completar la introducción de la información de descarga y carga de modelos y, después, habilitar o deshabilitar distintas entradas omitiendo diferentes nodos para lograr flujos de trabajo distintos. La información de descarga de los modelos ya está incorporada en la información del flujo de trabajo de cada ejemplo concreto, así que también puedes completar la descarga de los modelos al descargar los flujos de trabajo de ejemplo.

### 

​

Descarga de modelos

**Modelos de difusión**

## wan2.1_vace_14B_fp16.safetensors

Modelo de difusión VACE 14B (recomendado, ~32GB). Colócalo en `ComfyUI/models/diffusion_models/`

## wan2.1_vace_1.3B_fp16.safetensors

Modelo de difusión VACE 1.3B (más ligero, ~7GB). Colócalo en `ComfyUI/models/diffusion_models/`

Si ya has usado flujos de trabajo relacionados con Wan Video, ya tienes descargados los siguientes archivos de modelo.

**VAE**

## wan_2.1_vae.safetensors

Modelo VAE de Wan. Colócalo en `ComfyUI/models/vae/`

**Codificadores de texto** (elige una versión)

## umt5_xxl_fp16.safetensors

Codificador de texto de precisión completa (mayor calidad y mayor tamaño). Colócalo en `ComfyUI/models/text_encoders/`

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto FP8 (menor uso de VRAM). Colócalo en `ComfyUI/models/text_encoders/`

Ubicación para guardar los archivos:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └─── wan2.1_vace_14B_fp16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # o umt5_xxl_fp16.safetensors
    │   └── 📂 vae/
    │       └──  wan_2.1_vae.safetensors
    

### 

​

Carga de modelos

Como los modelos que se usan en los flujos de trabajo de este documento son los mismos, los flujos de trabajo también son iguales y solo se omiten distintos nodos para habilitar o deshabilitar las entradas. Consulta la siguiente imagen para asegurarte de que los modelos correspondientes estén cargados correctamente en los distintos flujos de trabajo. ![Carga de modelos de Wan2.1 VACE](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-model-loading.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=d46629d2ee7cfa1b942d4d92217992b1)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `wan2.1_vace_14B_fp16.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado `umt5_xxl_fp8_e4m3fn_scaled.safetensors` o `umt5_xxl_fp16.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `wan_2.1_vae.safetensors`



### 

​

Cómo cambiar el estado Omitir de un nodo

Cuando un nodo se establece en estado Omitir, los datos que pasan a través de él no se verán afectados por el nodo y se enviarán directamente a la salida. Solemos establecer nodos en estado Omitir cuando no los necesitamos. Aquí tienes tres formas de cambiar el estado Omitir de un nodo: ![Alternar Omitir](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/nodes/cancel-bypass.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=3a57352f6bc6f1c16ce0792d384d16fd)

  1. Después de seleccionar el nodo, haz clic en la flecha de la sección de indicadores del cuadro de herramientas de selección para cambiar rápidamente el estado Omitir del nodo
  2. Después de seleccionar el nodo, haz clic derecho en el nodo y selecciona `Mode` -> `Always` para cambiar al modo Always
  3. Después de seleccionar el nodo, haz clic derecho en el nodo y selecciona la opción `Bypass` para cambiar el estado Omitir



* * *

## 

​

1\. VACE texto a video

**Qué hace:** Transforma descripciones de texto en videos de alta calidad con el modelo Wan2.1 VACE 14B. Compatible con resolución 480p y 720p.

### 

​

Wan2.1 VACE texto a video

Transforma descripciones de texto en videos de alta calidad. Compatible con 480p y 720p con el modelo VACE-14B. ![Vista previa del flujo de trabajo Wan2.1 VACE texto a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_14B_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE Text to Video” en la Biblioteca de plantillas

Si no puedes cargar el flujo de trabajo desde el archivo mp4, asegúrate de que la versión del front-end de ComfyUI sea la más reciente indicada en [requirements.txt](https://github.com/Comfy-Org/ComfyUI/blob/master/requirements.txt) y comprueba que puedes cargar el flujo de trabajo desde el archivo mp4.Actualmente, 1.19.9 es la última versión del front-end de ComfyUI en el archivo requirements.txt.

### 

​

Pasos para ejecutar

![image](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-t2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=6f24e0be5f1ee91ea5becd79501053bd) Sigue los pasos numerados de la imagen para asegurar una ejecución fluida del flujo de trabajo:

  1. Ingresa los prompts positivos en el nodo `CLIP Text Encode (Positive Prompt)`
  2. Ingresa los prompts negativos en el nodo `CLIP Text Encode (Negative Prompt)`
  3. Define las dimensiones de la imagen (se recomienda una resolución de 640x640 para la primera ejecución) y la cantidad de fotogramas (duración del video) en `WanVaceToVideo`
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de video
  5. Una vez generado, el video se guardará automáticamente en el directorio `ComfyUI/output/video` (la ubicación de la subcarpeta depende de las configuraciones del nodo `save video`)



Durante las pruebas con una GPU 4090:

  * Resolución 720x1280, generar 81 fotogramas tarda unos 40 minutos
  * Resolución 640x640, generar 49 fotogramas tarda unos 7 minutos

Sin embargo, la calidad de video en 720P es mejor.

* * *

## 

​

2\. VACE imagen a video

**Qué hace:** Genera videos que coincidan con el estilo y el contenido de una imagen de referencia. Ideal para generar videos con un estilo consistente. Puedes seguir usando el flujo de trabajo anterior; solo tienes que quitar el bypass del nodo `Load image` en **Load reference image** e ingresar tu imagen. También puedes usar la imagen de abajo. En este archivo ya hemos configurado los parámetros correspondientes.

### 

​

Wan2.1 VACE referencia a video

Crea videos que coincidan con el estilo y el contenido de una imagen de referencia. Ideal para generar videos con un estilo consistente. ![Vista previa del flujo de trabajo Wan2.1 VACE referencia a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_14B_ref2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE Reference to Video” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## video_wan_vace_14B_ref2v_reference_image.jpg

nodo `LoadImage` 73 · `video_wan_vace_14B_ref2v_reference_image.jpg`

![video_wan_vace_14B_ref2v_reference_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan_vace_14B_ref2v_reference_image.jpg)

### 

​

Pasos para ejecutar

![Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-i2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=e22bf953a5900de76c55ed9af3881ea3) Sigue los pasos numerados de la imagen para que el flujo de trabajo se ejecute sin problemas:

  1. Ingresa la imagen correspondiente en el nodo `Load image`
  2. Puedes modificar y editar los prompts como en el flujo de trabajo de texto a video
  3. Configura las dimensiones de la imagen (se recomienda una resolución de 640x640 para la primera ejecución) y la cantidad de fotogramas (duración del video) en `WanVaceToVideo`
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del video
  5. Una vez generado, el video se guarda automáticamente en el directorio `ComfyUI/output/video` (la ubicación de la subcarpeta depende de la configuración del nodo `save video`)



Tal vez quieras usar nodos como los que obtienen las dimensiones de la imagen para establecer la resolución, pero debido a los requisitos de incremento de ancho y alto de los nodos correspondientes, es posible que recibas mensajes de error si las dimensiones de tu imagen no son divisibles entre 16.

### 

​

Notas adicionales

VACE también permite ingresar varias imágenes de referencia en una sola imagen para generar los videos correspondientes. Puedes ver ejemplos relacionados en la [página](https://ali-vilab.github.io/VACE-Page/) del proyecto VACE.

* * *

## 

​

3\. VACE de video a video

**Qué hace:** Genera videos controlando videos de entrada e imágenes de referencia con Wan VACE. Controla el estilo y el movimiento del video mediante materiales de referencia.

### 

​

Video de control con Wan2.1 VACE

Genera videos controlando videos de entrada e imágenes de referencia con Wan VACE. ![Vista previa del flujo de trabajo de video de control con Wan2.1 VACE](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_14B_v2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE Control Video” en la Biblioteca de plantillas

Usaremos los siguientes materiales como entrada:

## Imagen de referencia

Imagen de referencia de entrada para el estilo y el contenido.

## Video de control (preprocesado)

Video de control preprocesado (profundidad). Úsalo directamente en `Load Video`, dentro de **Cargar video de control**.

  1. Imagen de entrada como referencia:

![v2v-input](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/input.jpg)

  2. El siguiente video ya está preprocesado y se usará para controlar la generación del video:



  3. El siguiente video es el video original. Puedes descargar estos materiales y usar nodos de preprocesamiento como [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) para preprocesar las imágenes:



### 

​

Pasos para ejecutar

![Pasos del flujo de trabajo](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan-vace-v2v-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=a59e79204a1faf9b3f63c482b65df764) Sigue los pasos numerados en la imagen para asegurar una ejecución fluida del flujo de trabajo:

  1. Ingresa la imagen de referencia en el nodo `Load Image`, dentro de **Cargar imagen de referencia**
  2. Ingresa el video de control en el nodo `Load Video`, dentro de **Cargar video de control**. Como el video proporcionado ya está preprocesado, no necesitas procesamiento adicional
  3. Si necesitas preprocesar el video original por tu cuenta, puedes modificar el grupo **Preprocesamiento de imágenes** o usar los nodos de `comfyui_controlnet_aux` para completar el preprocesamiento
  4. Modifica los prompts
  5. Establece las dimensiones de la imagen (se recomienda una resolución de 640x640 para la primera ejecución) y la cantidad de fotogramas (duración del video) en `WanVaceToVideo`
  6. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de video
  7. Una vez generado, el video se guardará automáticamente en el directorio `ComfyUI/output/video` (la ubicación de la subcarpeta depende de las configuraciones del nodo `save video`)



* * *

## 

​

4\. Inpainting con VACE

**Qué hace:** Edita regiones específicas en videos y conserva el contenido que las rodea. Ideal para eliminar o reemplazar objetos.

### 

​

Inpainting con Wan2.1 VACE

Edita regiones específicas en videos y conserva el contenido que las rodea. Ideal para eliminar o reemplazar objetos. ![Wan2.1 VACE Inpainting workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_inpainting-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE Inpainting” en la Biblioteca de plantillas

**Materiales de entrada**

## Input Video

Video de entrada para el inpainting. Cárgalo en el nodo `Load Video`.

## First Frame & Mask

Primer fotograma con la máscara superpuesta para la región de inpainting.

## Reference Image

Imagen de referencia para el contenido del inpainting.

[Pendiente de actualización]

## 

​

5\. Outpainting de video con VACE

**Qué hace:** Genera videos extendidos ampliando el tamaño del video con el outpainting de Wan VACE.

### 

​

Wan2.1 VACE Outpainting

Genera videos extendidos ampliando el tamaño del video con el outpainting de Wan VACE. ![Vista previa del flujo de trabajo Wan2.1 VACE Outpainting](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_outpainting-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE Outpainting” en la Biblioteca de plantillas

**Materiales de entrada**

## Video de entrada

Video de entrada para el outpainting. Cárgalo en el nodo `Load Video`.

[Pendiente de actualización]

* * *

## 

​

6\. Generación de video con fotograma inicial y final de VACE

**Qué hace:** Genera transiciones de video suaves definiendo los fotogramas inicial y final. Admite secuencias personalizadas de fotogramas clave.

### 

​

Wan2.1 VACE First-Last Frame

Genera transiciones de video suaves definiendo los fotogramas inicial y final. Admite secuencias personalizadas de fotogramas clave. ![Vista previa del flujo de trabajo Wan2.1 VACE First-Last Frame](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_flf2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.1 VACE First-Last Frame” en la Biblioteca de plantillas

**Materiales de entrada**

## Fotograma inicial

Imagen del fotograma inicial. Cárgala en el nodo `Load Image`.

## Fotograma final

Imagen del fotograma final. Cárgala en el nodo `Load Image`.

Para que los fotogramas inicial y final sean efectivos, el ajuste `length` del video debe cumplir que `length-1` sea divisible entre 4. El ajuste `Batch_size` correspondiente debe cumplir `Batch_size = length - 2`. [Pendiente de actualización]

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/vace.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/vace)

[Causal Forcing I2V](https://docs.comfy.org/es/tutorials/video/wan/wan-causal-forcing)[Wan-Move](https://docs.comfy.org/es/tutorials/video/wan/wan-move)
