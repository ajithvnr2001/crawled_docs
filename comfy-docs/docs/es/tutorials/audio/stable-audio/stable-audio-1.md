---
url: https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-1/
title: Ejemplo de flujo de trabajo de Stable Audio 1.0 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.081941+00:00
---

# Ejemplo de flujo de trabajo de Stable Audio 1.0 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-1/

## En esta página

Volver arriba

  * Flujo de trabajo
    * Stable Audio 1.0: Text to Audio
  * Descargar el modelo
    * Checkpoint
    * Codificador de texto



Stable Audio

# Ejemplo de flujo de trabajo de Stable Audio 1.0 en ComfyUI

Copiar páginaCopiar página

Guía para generar audio a partir de texto con el modelo open source Stable Audio 1.0 de Stability AI en ComfyUI.

Copiar páginaCopiar página

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

**Stable Audio 1.0** es el primer modelo de generación de audio de código abierto de Stability AI. Recibe un prompt de texto y genera un clip de audio. En ComfyUI funciona como un pipeline estándar de texto a audio: CLIP codifica el prompt, un KSampler aplica denoise al latent y el VAE lo decodifica a audio. **Enlaces relacionados** :

  * [Hugging Face (stabilityai/stable-audio-open-1.0)](https://huggingface.co/stabilityai/stable-audio-open-1.0)



## 

​

Flujo de trabajo

### 

​

Stable Audio 1.0: Text to Audio

Genera audio a partir de prompts de texto con Stable Audio. ![Vista previa del flujo de trabajo de texto a audio con Stable Audio 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_example-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Stable Audio 1.0: Text to Audio” en la biblioteca de plantillas

El flujo de trabajo usa **nodos estándar de ComfyUI** : no necesitas nodos personalizados. Carga el checkpoint de Stable Audio 1.0, codifica tu prompt mediante un codificador de texto CLIP (t5-base), aplica denoising al audio latent con un KSampler y lo decodifica a audio mediante el VAE del modelo. **Cómo usarlo** :

  1. **Carga el checkpoint** : el nodo `CheckpointLoaderSimple` usa `stable-audio-open-1.0.safetensors`
  2. **Escribe un prompt** : introduce tu descripción en el nodo `CLIPTextEncode` (por ejemplo, “heaven church electronic dance music”)
  3. **Establece la duración** : ajusta el valor de longitud del nodo `EmptyLatentAudio` (47.6 segundos por defecto)
  4. Haz clic en **Run** (`Ctrl/Cmd + Enter`) para generar. El audio se guardará en `ComfyUI/output/audio/`



## 

​

Descargar el modelo

Al cargar el flujo de trabajo, ComfyUI te mostrará enlaces de descarga para los modelos faltantes. Para configurarlo manualmente, descarga los archivos a continuación y colócalos en las carpetas correctas.

### 

​

Checkpoint

## stable-audio-open-1.0.safetensors

2.3GB. Colócalo en models/checkpoints/

Coloca el checkpoint en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── stable-audio-open-1.0.safetensors
    

### 

​

Codificador de texto

## t5-base.safetensors

Codificador de texto para el conditioning del prompt. Colócalo en models/text_encoders/

Coloca el codificador de texto en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── t5-base.safetensors
    

Después de colocar los archivos, presiona **R** en ComfyUI para actualizar los nodos y cargar los últimos modelos.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/audio/stable-audio/stable-audio-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/audio/stable-audio/stable-audio-1)

[MiniMax Music 3](https://docs.comfy.org/es/tutorials/audio/minimax/minimax-music-3)[Stable Audio 3](https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-3)
