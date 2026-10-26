---
url: https://docs.comfy.org/es/tutorials/basic/outpaint/
title: Outpainting en ComfyUI: extiende una imagen m\u00e1s all\u00e1 de sus bordes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.738682+00:00
---

# Outpainting en ComfyUI: extiende una imagen más allá de sus bordes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/basic/outpaint/

## En esta página

Volver arriba

  * Acerca del outpainting
  * Explicación del ejemplo de flujo de trabajo de outpainting en ComfyUI
    * Preparación
    * 1\. Instalación del modelo
    * 2\. Imagen de entrada
    * 3\. Flujo de trabajo de outpainting
    * Explicación del uso del flujo de trabajo de outpainting
    * Nodo Pad Image for outpainting
    * Parámetros de entrada
    * Parámetros de salida
    * Contenido de la salida del nodo



Basic Examples

# Outpainting en ComfyUI: extiende una imagen más allá de sus bordes

Copiar páginaCopiar página

Usa el nodo Pad Image for Outpainting con un modelo de inpainting para ampliar el lienzo y mantener los nuevos bordes coherentes con la imagen original.

Copiar páginaCopiar página

Esta guía te introduce en el concepto de outpainting en la generación de imágenes con IA y en cómo crear un flujo de trabajo de outpainting en ComfyUI. Cubriremos:

  * Usar un flujo de trabajo de outpainting para extender una imagen
  * Entender y usar los nodos relacionados con outpainting en ComfyUI
  * Dominar el proceso básico de outpainting



## 

​

Acerca del outpainting

En la generación de imágenes con IA, a menudo nos encontramos con situaciones en las que una imagen existente tiene una buena composición, pero el área del lienzo es demasiado pequeña, por lo que necesitamos extender el lienzo para obtener una escena más grande. Aquí es donde entra en juego el outpainting. Básicamente, requiere un contenido similar al de [Relleno inteligente](https://docs.comfy.org/es/tutorials/basic/inpaint), pero usamos nodos diferentes para **construir la máscara**. Las aplicaciones del outpainting incluyen:

  * **Extensión de escena:** Expande el alcance de la escena de la imagen original para mostrar un entorno más completo
  * **Ajuste de composición:** Optimiza la composición general extendiendo el lienzo
  * **Adición de contenido:** Agrega más elementos de escena relacionados a la imagen original



## 

​

Explicación del ejemplo de flujo de trabajo de outpainting en ComfyUI

### 

​

Preparación

#### 

​

1\. Instalación del modelo

Descarga el siguiente archivo de modelo y guárdalo en el directorio `ComfyUI/models/checkpoints`:

  * [512-inpainting-ema.safetensors](https://huggingface.co/Comfy-Org/stable_diffusion_2.1_repackaged/blob/main/512-inpainting-ema.safetensors)



#### 

​

2\. Imagen de entrada

Prepara una imagen que quieras extender. En este ejemplo, usaremos la siguiente imagen: ![Imagen de entrada para outpainting en ComfyUI](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/input.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=70f072d92be155e740f8763e0265240f)

#### 

​

3\. Flujo de trabajo de outpainting

Descarga la imagen de abajo y **arrástrala a ComfyUI** para cargar el flujo de trabajo: ![Flujo de trabajo de outpainting en ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/image/basic/outpaint.png)

Las imágenes que contienen el JSON del flujo de trabajo en sus metadatos se pueden arrastrar directamente a ComfyUI o cargar con el menú `Workflows` -> `Open (ctrl+o)`.

### 

​

Explicación del uso del flujo de trabajo de outpainting

![Diagrama del flujo de trabajo de outpainting en ComfyUI](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/outpainting_workflow.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=b56842f634fedc85c66bccd0ead52bb6) Los pasos clave del flujo de trabajo de outpainting son los siguientes:

  1. Carga el archivo de modelo instalado localmente en el nodo `Load Checkpoint`
  2. Haz clic en el botón `Upload` del nodo `Load Image` para subir tu imagen
  3. Haz clic en el botón `Queue` o usa el atajo `Ctrl + Enter` para ejecutar la generación de la imagen

En este flujo de trabajo usamos principalmente el nodo `Pad Image for outpainting` para controlar la dirección y el alcance de la extensión de la imagen. En realidad se trata de un flujo de trabajo de [Inpaint](https://docs.comfy.org/es/tutorials/basic/inpaint), pero usamos nodos distintos para construir la máscara.

### 

​

Nodo Pad Image for outpainting

![Nodo Pad Image for outpainting](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/image/pad_image_for_outpainting.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=9a9eaf8b01a18692b50a684cbff5d8e1) Este nodo recibe una imagen de entrada y devuelve una imagen extendida junto con su máscara correspondiente, donde la máscara se construye a partir de los parámetros del nodo.

#### 

​

Parámetros de entrada

Nombre del parámetro| Función  
---|---  
`image`| Imagen de entrada  
`left`| Cantidad de relleno a la izquierda  
`top`| Cantidad de relleno arriba  
`right`| Cantidad de relleno a la derecha  
`bottom`| Cantidad de relleno abajo  
`feathering`| Controla la suavidad de la transición entre la imagen original y el relleno añadido; valores más altos crean transiciones más suaves  
  
#### 

​

Parámetros de salida

Nombre del parámetro| Función  
---|---  
`image`| La salida `image` representa la imagen con relleno  
`mask`| La salida `mask` indica el área de la imagen original y el área del relleno añadido  
  
#### 

​

Contenido de la salida del nodo

Después del procesamiento por el nodo `Pad Image for outpainting`, la vista previa de la imagen y la máscara de salida es la siguiente: ![Resultados del nodo Pad Image for outpainting](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/outpaint/pad_Image_for_outpainting_result.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=cc8fd3e8159dca0e8abf9def1bfe6d39) Puedes ver los resultados de salida correspondientes:

  * La salida `Image` es la imagen extendida
  * La salida `Mask` es la máscara que marca las áreas extendidas



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/basic/outpaint.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/basic/outpaint)

[Relleno inteligente](https://docs.comfy.org/es/tutorials/basic/inpaint)[Upscale](https://docs.comfy.org/es/tutorials/basic/upscale)
