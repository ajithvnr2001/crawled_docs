---
url: https://docs.comfy.org/es/tutorials/basic/lora/
title: Modelos LoRA en ComfyUI: instalar, cargar y aplicar estilos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.560226+00:00
---

# Modelos LoRA en ComfyUI: instalar, cargar y aplicar estilos - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/basic/lora/

## En esta página

Volver arriba

  * Instalación de los modelos requeridos
  * Archivo de flujo de trabajo de LoRA
  * Completar el flujo de trabajo paso a paso
  * Introducción al nodo Load LoRA
    * Tipos de entrada
    * Tipos de salida
  * Probar por tu cuenta



Basic Examples

# Modelos LoRA en ComfyUI: instalar, cargar y aplicar estilos

Copiar páginaCopiar página

Instala un archivo LoRA, cárgalo con el nodo Load LoRA y ejecuta un flujo de trabajo que combina su estilo con un checkpoint base.

Copiar páginaCopiar página

**LoRA (Low-Rank Adaptation)** es una técnica eficiente para el ajuste fino de modelos generativos grandes como Stable Diffusion. Introduce matrices entrenables de bajo rango en el modelo preentrenado, ajustando solo una parte de los parámetros en lugar de reentrenar el modelo completo, logrando así la optimización para tareas específicas con un menor costo computacional. En comparación con los modelos base como SD1.5, los modelos LoRA son más pequeños y más fáciles de entrenar. ![Comparación entre un modelo LoRA y un modelo base](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=742213e2c13c5be487ea3e9827630e5a) La imagen anterior compara la generación con los mismos parámetros usando [dreamshaper_8](https://civitai.com/models/4384?modelVersionId=128713) directamente frente a usar el modelo LoRA [blindbox_V1Mix](https://civitai.com/models/25995/blindbox). Como puedes ver, al usar un modelo LoRA podemos generar imágenes en diferentes estilos sin ajustar el modelo base. Vamos a mostrar cómo usar un modelo LoRA. Todas las variantes de LoRA: Lycoris, loha, lokr, locon, etc… se usan de la misma manera. En este ejemplo, aprenderás a cargar y usar un modelo LoRA en [ComfyUI](https://github.com/Comfy-Org/ComfyUI), y cubriremos los siguientes temas:

  1. Instalar un modelo LoRA
  2. Generar imágenes usando un modelo LoRA
  3. Una introducción sencilla al nodo `Load LoRA`



## 

​

Instalación de los modelos requeridos

Descarga el archivo [dreamshaper_8.safetensors](https://civitai.com/api/download/models/128713?type=Model&format=SafeTensor&size=pruned&fp=fp16) y colócalo en tu carpeta `ComfyUI/models/checkpoints`. Descarga el archivo [blindbox_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model&format=SafeTensor&size=full&fp=fp16) y colócalo en tu carpeta `ComfyUI/models/loras`.

## 

​

Archivo de flujo de trabajo de LoRA

Descarga la imagen a continuación y **arrástrala a ComfyUI** para cargar el flujo de trabajo. ![ComfyUI Workflow - LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/lora.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=5f67dbeed58fd00da65100432c06edc7)

Las imágenes que contienen el JSON del flujo de trabajo en sus metadatos se pueden arrastrar directamente a ComfyUI o cargar con el menú `Workflows` -> `Open (ctrl+o)`.

## 

​

Completar el flujo de trabajo paso a paso

Sigue los pasos del diagrama siguiente para asegurarte de que el flujo de trabajo se ejecute correctamente. ![Diagrama del flujo de trabajo de ComfyUI - LoRA](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/lora.png)

  1. Asegúrate de que `Load Checkpoint` cargue `dreamshaper_8.safetensors`
  2. Asegúrate de que `Load LoRA` cargue `blindbox_V1Mix.safetensors`
  3. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen



## 

​

Introducción al nodo Load LoRA

![Nodo Load LoRA](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfy_core/loaders/load_lora.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=86dd2ba28327b5c6c182a9fb4f4404bb) ComfyUI detecta los modelos de la carpeta `ComfyUI\models\loras` y puedes cargarlos con este nodo.

### 

​

Tipos de entrada

Nombre del parámetro| Función  
---|---  
`model`| Conecta con el modelo base  
`clip`| Conecta con el modelo CLIP  
`lora_name`| Selecciona el modelo LoRA que se va a cargar y usar  
`strength_model`| Afecta la intensidad con la que el LoRA influye en los pesos del modelo; los valores más altos hacen que el estilo del LoRA sea más fuerte  
`strength_clip`| Afecta la intensidad con la que el LoRA influye en los embeddings de texto de CLIP  
  
### 

​

Tipos de salida

Nombre del parámetro| Función  
---|---  
`model`| Devuelve el modelo con los ajustes de LoRA aplicados  
`clip`| Devuelve el modelo CLIP con los ajustes de LoRA aplicados  
  
Este nodo admite conexiones en cadena, lo que permite conectar varios nodos `Load LoRA` en serie para aplicar varios modelos LoRA. Para más detalles, consulta [Ejemplo de múltiples LoRAs en ComfyUI](https://docs.comfy.org/es/tutorials/basic/multiple-loras) ![Conexión en cadena de nodos LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf)

## 

​

Probar por tu cuenta

  1. Intenta modificar el prompt o ajustar distintos parámetros del nodo `Load LoRA`, como `strength_model`, para observar los cambios en las imágenes generadas y familiarizarte con el nodo `Load LoRA`.
  2. Visita [CivitAI](https://civitai.com/models) para descargar otros tipos de modelos LoRA y probar a usarlos.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/basic/lora.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/basic/lora)

[Upscale](https://docs.comfy.org/es/tutorials/basic/upscale)[Varios LoRA](https://docs.comfy.org/es/tutorials/basic/multiple-loras)
