---
url: https://docs.comfy.org/es/tutorials/image/krea/krea-2/
title: Ejemplo de flujo de trabajo de Krea-2 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.177657+00:00
---

# Ejemplo de flujo de trabajo de Krea-2 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/krea/krea-2/

## En esta página

Volver arriba

  * Mira el evento de lanzamiento
  * Pesos de modelo disponibles
  * Flujo de trabajo de texto a imagen de Krea-2 Turbo
    * Krea-2: Texto a imagen
    * Generación con un solo clic
    * Controles del flujo de trabajo
    * LoRA de estilo
    * Descargas de modelos
    * Ubicación de almacenamiento de los modelos
  * Flujo de trabajo de referencia de estilo de Krea-2 Turbo
    * Krea-2 Int8: referencia de estilo de imagen
    * Usar la referencia de estilo



Krea 2

# Ejemplo de flujo de trabajo de Krea-2 en ComfyUI

Copiar páginaCopiar página

Krea 2 es un modelo de texto a imagen diseñado para lograr alta calidad estética y diversidad estilística. Viene en dos variantes: RAW (base) y Turbo (destilada).

Copiar páginaCopiar página

**Krea 2** es un modelo de generación de imágenes de [Krea AI](https://www.krea.ai), entrenado desde cero y enfocado en la exploración creativa y estilística. Krea 2 se distribuye como dos modelos diseñados para trabajar juntos: **entrena LoRAs en RAW y ejecuta la inferencia en Turbo** :

  * **Krea 2 RAW** : el modelo base con muestreo de pasos completos (52 pasos). Sin destilación, diverso y altamente moldeable, ideal para ajuste fino y entrenamiento de LoRA.
  * **Krea 2 Turbo** : un checkpoint destilado de 8 pasos para una generación rápida y de alta calidad. Los LoRA entrenados en RAW se aplican sin problemas a Turbo.

**Licencia** : [Krea AI Community License](https://www.krea.ai/krea-2-licensing)

## 

​

Mira el evento de lanzamiento

Para aprender más acerca de Krea 2, la historia detrás de su desarrollo, sus capacidades y lo que significa para el ecosistema de código abierto, mira la grabación del evento de lanzamiento que aparece arriba (con la participación de Victor Perez, Miguel Lara y ComfyAnonymous).

## 

​

Pesos de modelo disponibles

Krea 2 está disponible en dos variantes:

  * **Krea 2 RAW** : el modelo base con muestreo de pasos completos (52 pasos). Diseñado para ofrecer diversidad y flexibilidad; ideal para fine-tuning y entrenamiento de LoRA.
  * **Krea 2 Turbo** : un checkpoint destilado de 8 pasos creado para una generación rápida y de alta calidad. Los LoRA entrenados en RAW se aplican sin problemas en Turbo.

**Enlaces relacionados** :

  * [Krea 2 en Hugging Face (RAW)](https://huggingface.co/krea/Krea-2-Raw)
  * [Krea 2 en Hugging Face (Turbo)](https://huggingface.co/krea/Krea-2-Turbo)
  * [Comfy-Org/Krea-2 (modelos de ComfyUI)](https://huggingface.co/Comfy-Org/Krea-2)
  * [Repositorio oficial en GitHub](https://github.com/krea-ai/krea-2)
  * [Guías de prompting](https://github.com/krea-ai/krea-2/blob/main/docs/prompting.md)
  * [Informe técnico](https://www.krea.ai/blog/krea-2-technical-report)



## 

​

Flujo de trabajo de texto a imagen de Krea-2 Turbo

### 

​

Krea-2: Texto a imagen

Genera imágenes a partir de prompts de texto con Krea 2, un modelo fundacional pensado para la calidad estética y el control creativo. Se centra en generar imágenes expresivas y estilísticamente diversas. ![Vista previa del flujo de trabajo de texto a imagen de Krea-2 Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea-2” en la Biblioteca de plantillas

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

El flujo de trabajo se organiza en varias partes:

  1. **Text to Image (Krea-2 Turbo) subgrafo** : el pipeline de generación principal, que incluye la carga de modelos, el manejo del prompt, el muestreo y la decodificación del VAE
  2. **ResolutionSelector** : elige la resolución de salida que quieras. Krea 2 admite salidas de 1K a 2K. Establece el valor de megapíxeles en 2.0 para obtener resolución 2K.
  3. **CustomCombo (selector de LoRA)** : un selector de palabras de activación ya preparado para las LoRA de estilo disponibles. Si descargas LoRA adicionales, puedes personalizar este selector y emparejarlas con los archivos de LoRA correspondientes.
  4. **SaveImage** : guarda la imagen generada



## Aprende sobre Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y ampliar el flujo de trabajo.

### 

​

Generación con un solo clic

En el caso más simple, basta con introducir un prompt de texto en el subgrafo, elegir una resolución y hacer clic en **Queue Prompt**. Los valores predeterminados (8 pasos, mejora del prompt activada, sin LoRA) producen una imagen de alta calidad con una configuración mínima.

### 

​

Controles del flujo de trabajo

El subgrafo **Text to Image (Krea-2 Turbo)** expone los siguientes controles:

Control| Descripción  
---|---  
**Text String (User Prompt)**|  El prompt de texto que describe la imagen que quieres generar  
**prompt_enhance**|  Activa o desactiva la expansión del prompt con un LLM  
**LLM_max_token**|  Longitud máxima en tokens para la mejora del prompt  
**Width / Height**|  Resolución de salida (controlada por ResolutionSelector)  
**Seed**|  Semilla aleatoria para poder reproducir el resultado  
**enable_lora?**|  Activa o desactiva la LoRA de estilo  
**LoRA Strength**|  Fuerza de la LoRA de estilo aplicada  
**LoRA Trigger Word**|  Palabra de activación que se rellena automáticamente para la LoRA seleccionada  
  
### 

​

LoRA de estilo

Krea también publicó una colección de LoRA de estilo para Krea 2. Selecciona una en el nodo **CustomCombo** y activa `enable_lora?` en el subgrafo para aplicar el estilo:

LoRA| Palabra de activación| Fuerza recomendada| Descarga  
---|---|---|---  
krea2_darkbrush| estilo de aguada de tinta monocroma| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_darkbrush.safetensors)  
krea2_dotmatrix| estilo de punteado monocromo| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_dotmatrix.safetensors)  
krea2_kidsdrawing| estilo de boceto expresivo naíf| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_kidsdrawing.safetensors)  
krea2_neondrip| estilo abstracto texturizado| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_neondrip.safetensors)  
krea2_rainywindow| estilo de ventana lluviosa| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_rainywindow.safetensors)  
krea2_retroanime| estilo retro anime púrpura| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_retroanime.safetensors)  
krea2_softwatercolor| estilo de acuarela art déco| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_softwatercolor.safetensors)  
krea2_sunsetblur| estilo de desenfoque de movimiento etéreo| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_sunsetblur.safetensors)  
krea2_vintagetarot| estilo de tarot vintage| 1.0| [Descargar](https://huggingface.co/Comfy-Org/Krea-2/blob/main/loras/krea2_vintagetarot.safetensors)  
  
Guarda los archivos `.safetensors` en `ComfyUI/models/loras/`.

### 

​

Descargas de modelos

Para uso local, descarga los archivos de modelo optimizados para ComfyUI desde [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2).

## Modelo de difusión (FP8)

krea2_turbo_fp8_scaled.safetensors: Turbo FP8 (recomendado para la mayoría de los usuarios)

## Codificador de texto (FP8)

qwen3vl_4b_fp8_scaled.safetensors: codificador de texto Qwen3VL-4B

## VAE

qwen_image_vae.safetensors

## LoRA de estilo

Consulta todas las LoRA de estilo en Hugging Face

También hay otras variantes del modelo (BF16, NVFP4, MXFP8) para usuarios con hardware de gama alta.

#### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── krea2_turbo_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_4b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 loras/
    │       └── krea2_softwatercolor.safetensors (and other style LoRAs)
    

## 

​

Flujo de trabajo de referencia de estilo de Krea-2 Turbo

### 

​

Krea-2 Int8: referencia de estilo de imagen

Genera imágenes con el modelo Krea-2 Turbo tomando como referencia el estilo de 1–2 imágenes subidas, con el formato Int8 Convrot de alto rendimiento para una inferencia rápida. ![Vista previa del flujo de trabajo de referencia de estilo de Krea-2 Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_int8_image_style_reference-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea-2 Style Reference” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## krea2_reference_image.png

Nodo `LoadImage` 69 · `krea2_reference_image.png`

![krea2_reference_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/krea2_reference_image.png)

**Salida de ejemplo** ![Ejemplo de salida de la referencia de estilo de Krea-2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_krea2_turbo_int8_image_style_reference.png) El flujo de trabajo con referencia de estilo se basa en el pipeline de Krea-2 Turbo añadiendo el condicionamiento por imagen de referencia. Sube una o más imágenes de referencia para influir en el estilo estético, el ambiente y la dirección visual del resultado generado. El flujo de trabajo se organiza en varias partes:

  1. **Image Style Reference (Krea-2 Turbo) subgrafo** : el pipeline de generación principal con soporte para referencia de estilo, que incluye la carga de modelos, el condicionamiento por imagen de referencia, el manejo del prompt y el muestreo
  2. **LoadImage** : sube tus imágenes de referencia de estilo
  3. **ResolutionSelector** : elige la resolución de salida que quieras. Krea 2 admite salidas de 1K a 2K.
  4. **SaveImage** : guarda la imagen generada



### 

​

Usar la referencia de estilo

  1. **Sube las imágenes de referencia** : usa el nodo **LoadImage** para cargar una o más imágenes de referencia de estilo
  2. **Escribe tu prompt** : introduce una descripción de texto en la entrada de prompt del usuario del subgrafo
  3. **Selecciona una variante del modelo** : elige el checkpoint en el selector de modelo del subgrafo
  4. **Ajusta la configuración** : establece la resolución, la semilla y, si quieres, activa la mejora del prompt
  5. **Haz clic en Queue** : pulsa `Ctrl+Enter` para generar

Este flujo de trabajo de referencia de estilo usa un modelo de difusión y una LoRA dedicados. El codificador de texto y el VAE se comparten con el flujo de trabajo de texto a imagen.

## Modelo de difusión (INT8)

krea2_turbo_int8_convrot.safetensors

## Codificador de texto (FP8)

qwen3vl_4b_fp8_scaled.safetensors: codificador de texto Qwen3VL-4B

## VAE

qwen_image_vae.safetensors

## LoRA de referencia de estilo

krea2_style_reference.safetensors

Guarda los archivos en los siguientes directorios:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── krea2_turbo_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_4b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── qwen_image_vae.safetensors
    │   └── 📂 loras/
    │       └── krea2_style_reference.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/krea/krea-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/krea/krea-2)

[PiD Latent Upscale](https://docs.comfy.org/es/tutorials/image/nvidia/pid-latent-upscale)[Ideogram 4.0](https://docs.comfy.org/es/tutorials/image/ideogram/ideogram-v4)
