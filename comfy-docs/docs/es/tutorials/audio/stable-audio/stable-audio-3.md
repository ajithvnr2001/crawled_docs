---
url: https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-3/
title: Ejemplo de flujo de trabajo de Stable Audio 3 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.187606+00:00
---

# Ejemplo de flujo de trabajo de Stable Audio 3 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-3/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Stable Audio 3.0 Medium
    * Stable Audio 3.0 Medium Base
  * Descarga de modelos
    * Checkpoints
    * Codificadores de texto



Stable Audio

# Ejemplo de flujo de trabajo de Stable Audio 3 en ComfyUI

Copiar páginaCopiar página

Ejecuta Stable Audio 3 de código abierto de Stability AI en ComfyUI para generar audio desde texto, con expansión de prompt con Qwen y reprompting por categoría.

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

**Stable Audio 3** ([GitHub](https://github.com/Stability-AI/stable-audio-3)) es el modelo de generación de audio de código abierto más reciente de Stability AI, entrenado con datos musicales totalmente licenciados y con licencia para uso comercial. Utiliza un nodo de subgrafo dedicado para producir audio estéreo de alta calidad (incluyendo música, efectos de sonido e instrumentos) a partir de descripciones de texto, con reprompting opcional por categoría impulsado por Qwen. Stable Audio 3 está disponible en tres variantes:

  * **Small-SFX** : Efectos de sonido y ambientes cortos, de hasta 2:00. Lo suficientemente pequeño para ejecutarse en CPU.
  * **Small-Music** : Bucles musicales cortos, aptos para ejecutarse en el dispositivo, de hasta 2:00.
  * **Medium** : Pistas más largas con mayor estructura y musicalidad, de hasta ~6:20. Requiere una GPU.

**Enlaces relacionados** :

  * [GitHub: Stability-AI/stable-audio-3](https://github.com/Stability-AI/stable-audio-3)
  * [Hugging Face (Comfy-Org/stable-audio-3)](https://huggingface.co/Comfy-Org/stable-audio-3)
  * [Blog: Anuncio](https://blog.comfy.org/p/stable-audio-3-day-0-support)



## 

​

Flujos de trabajo disponibles

### 

​

Stable Audio 3.0 Medium

Introduce una idea breve en texto, la duración opcional, la semilla y la categoría. Genera audio estéreo (música, SFX o instrumentos) con Stable Audio 3 y la expansión de texto opcional impulsada por IA. ![Stable Audio 3 Medium workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Stable Audio 3.0 Medium” en la biblioteca de plantillas

El flujo de trabajo **Stable Audio 3 Medium** es un pipeline completo de generación de texto a audio. Tú proporcionas una idea breve en texto, la duración opcional, la semilla y la categoría. El flujo de trabajo expande tu prompt con Qwen mediante una **plantilla de reprompt según la categoría** y después genera audio estéreo con el checkpoint de Stable Audio 3. **Cómo usarlo** :

  1. **Idea de texto** : introduce una descripción breve del sonido, la música o el efecto que quieres (por ejemplo, “upbeat electronic dance track with heavy bass”)
  2. **Duración** : define la longitud deseada del clip en segundos (el valor predeterminado varía)
  3. **Semilla** : controla la reproducibilidad ajustando el valor de la semilla
  4. **Categoría** : elige un preset de reprompt: **Music** , **Instrument** , **SFX** o **One-shot**
  5. **Activar reprompt** : activa `use_reprompt` para que Qwen expanda tu idea breve en un prompt detallado antes de la generación
  6. Haz clic en **Run** (`Ctrl/Cmd + Enter`) para generar. El audio se guarda en `ComfyUI/output/audio/`



### 

​

Stable Audio 3.0 Medium Base

Introduce una descripción breve en texto de un sonido, una música o un efecto. El flujo de trabajo expande tu prompt con Qwen y genera un clip de audio estéreo con Stable Audio 3. ![Stable Audio 3 Medium Base workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium_base-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Stable Audio 3.0 Medium Base” en la biblioteca de plantillas

Una versión simplificada de Stable Audio 3 sin la expansión de reprompt de Qwen. Espera un prompt de texto completo y lo pasa directamente al modelo. Úsala cuando ya tengas un prompt detallado y quieras una generación más rápida. **Cómo usarlo** :

  1. **Prompt de texto** : introduce una descripción detallada del audio que quieres
  2. **Duración** : define la longitud del clip en segundos
  3. **Semilla** : controla la reproducibilidad
  4. Haz clic en **Run** (`Ctrl/Cmd + Enter`) para generar



## 

​

Descarga de modelos

Al cargar el flujo de trabajo, ComfyUI te mostrará enlaces de descarga para los modelos faltantes. Para configurarlo manualmente, descarga los archivos a continuación y colócalos en las carpetas correctas.

### 

​

Checkpoints

## stable_audio_3_medium.safetensors

Para el flujo de trabajo Medium. Colócalo en models/checkpoints/

## stable_audio_3_medium_base.safetensors

Para el flujo de trabajo Medium Base. Colócalo en models/checkpoints/

Coloca los checkpoints en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       ├── stable_audio_3_medium.safetensors
    │       └── stable_audio_3_medium_base.safetensors
    

### 

​

Codificadores de texto

## t5gemma_b_b_ul2.safetensors

Requerido para todos los flujos de trabajo de Stable Audio 3. Colócalo en models/text_encoders/

## qwen3.5_2b_bf16.safetensors

Requerido para el flujo de trabajo Medium (reprompt de Qwen). Colócalo en models/text_encoders/

Coloca los codificadores de texto en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       ├── t5gemma_b_b_ul2.safetensors
    │       └── qwen3.5_2b_bf16.safetensors
    

Después de colocar los archivos, presiona **R** en ComfyUI para actualizar los nodos y cargar los modelos más recientes.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/audio/stable-audio/stable-audio-3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/audio/stable-audio/stable-audio-3)

[Stable Audio 1.0](https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-1)[ACE-Step 1.0](https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1)
