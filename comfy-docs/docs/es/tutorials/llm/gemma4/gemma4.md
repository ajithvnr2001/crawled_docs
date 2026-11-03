---
url: https://docs.comfy.org/es/tutorials/llm/gemma4/gemma4/
title: Gemma 4 en ComfyUI: LLM multimodal con TextGenerate - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:29.736858+00:00
---

# Gemma 4 en ComfyUI: LLM multimodal con TextGenerate - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/llm/gemma4/gemma4/

## En esta página

Volver arriba

  * Flujo de trabajo disponible
    * Gemma4: Text Generation
  * Descarga del modelo



LLM

# Gemma 4 en ComfyUI: LLM multimodal con TextGenerate

Copiar páginaCopiar página

Ejecuta Gemma 4 de Google en ComfyUI a través del nodo TextGenerate para generación de texto, comprensión de imágenes y transcripción de audio.

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

**Gemma 4** es la última generación de LLM abiertos y ligeros de Google DeepMind, creada para la generación de texto, la comprensión de imágenes, el análisis de video, la transcripción de audio y el uso estructurado de herramientas. ComfyUI lo admite de forma nativa como modelo **Text Generation** predeterminado. **Aspectos destacados del modelo** :

  * **Multimodal por diseño** : acepta entradas de texto, imagen, video y audio de forma simultánea
  * **Tres tamaños disponibles** : 
    * **E2B (2B)** : rápido y ligero, ideal para GPU de consumo
    * **E4B (4B)** : rendimiento equilibrado, opción predeterminada recomendada
    * **12B** : mejor calidad, requiere más VRAM
  * **Modo de pensamiento** : razonamiento paso a paso integrado antes de generar las respuestas
  * **Contexto largo** : hasta 128K tokens (E2B/E4B) y 256K tokens (12B)
  * **Multilingüe** : más de 35 idiomas listos para usar, con preentrenamiento en más de 140 idiomas
  * **Llamada a funciones** : soporte nativo para el uso estructurado de herramientas y flujos de trabajo agénticos
  * **Nativo en ComfyUI** : ComfyUI lo carga y lo ejecuta a través de los nodos integrados `TextGenerate` y `CLIPLoader`

**Enlaces relacionados** :

  * [Hugging Face (Comfy-Org/gemma-4)](https://huggingface.co/Comfy-Org/gemma-4)
  * [Google AI for Developers](https://ai.google.dev/gemma)
  * [Código fuente de ComfyUI (nodes_textgen.py)](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_textgen.py)



## 

​

Flujo de trabajo disponible

### 

​

Gemma4: Text Generation

Ingresa tu prompt de texto y, de forma opcional, una imagen, audio o video. Genera una salida de texto con soporte configurable para razonamiento, programación y varios idiomas. ![Vista previa del flujo de trabajo de generación de texto de Gemma 4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_gemma4_text_gen-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Gemma4: Text Generation” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos opcionales a los nodos correspondientes:

## the_lily_veil.png

Nodo `LoadImage` 2 · `the_lily_veil.png`

## long_demo.mp3

Nodo `LoadAudio` 5 · `long_demo.mp3`

## video_wan_vace_inpainting_input_video.mp4

Nodo `LoadVideo` 6 · no se usa en la generación de este flujo de trabajo · `video_wan_vace_inpainting_input_video.mp4`

Este flujo de trabajo demuestra las capacidades principales de **generación de texto** de Gemma 4. Acepta una imagen, un archivo de audio o un video opcional como contexto adicional junto a tu prompt de texto, y genera una salida en lenguaje natural, con soporte para razonamiento, programación y prompts multilingües. **Entradas** :

  * **Prompt de texto** : tu pregunta o instrucción
  * **Imagen** (opcional): para tareas de comprensión visual (OCR, detección de objetos, lectura de gráficos, etc.)
  * **Audio** (opcional): para reconocimiento de voz o transcripción
  * **Video** (opcional): la plantilla carga el video y lo divide con **Obtener componentes de video** , pero esos fotogramas no están conectados al generador de texto, así que el video no afecta la salida

**Controles principales** :

  * **Longitud máxima** : número máximo de tokens a generar (256 por defecto)
  * **Modo de muestreo** : activa o desactiva el muestreo y ajusta temperatura, top-k, top-p, penalización por repetición y semilla
  * **Modo de pensamiento** : activa el razonamiento paso a paso antes de la respuesta final
  * **Usar plantilla predeterminada** : aplica el prompt de sistema integrado del modelo

**Salida** :

  * **Texto generado** : la respuesta del modelo como una cadena de texto sin formato



## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para un procesamiento modular. Consulta la documentación de Subgraph para saber cómo personalizar y ampliar el flujo de trabajo.

## 

​

Descarga del modelo

Los modelos Gemma 4 se cargan como codificadores de texto en ComfyUI. Descarga el archivo del modelo correspondiente y colócalo en el directorio correcto:

## Gemma 4 2B (E2B IT FP8)

Rápido y ligero. Recomendado para GPUs de consumo.

## Gemma 4 4B (E4B IT FP8)

Rendimiento equilibrado. El modelo predeterminado en el flujo de trabajo.

## Ver todas las variantes

Explora todos los pesos del modelo Gemma 4.

Coloca el archivo `.safetensors` descargado en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── gemma4_e4b_it_fp8_scaled.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/llm/gemma4/gemma4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/llm/gemma4/gemma4)

[Hunyuan3D-2](https://docs.comfy.org/es/tutorials/3d/hunyuan3D-2)[Qwen 3.0](https://docs.comfy.org/es/tutorials/llm/qwen/qwen3)
