---
url: https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1-5/
title: ACE-Step 1.5 en ComfyUI: generaci\u00f3n local de m\u00fasica con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:28.909194+00:00
---

# ACE-Step 1.5 en ComfyUI: generación local de música con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1-5/

## En esta página

Volver arriba

  * Opción 1: Checkpoint todo en uno (recomendado)
    * ACE-Step 1.5 Music Generation AIO
    * Descarga del modelo AIO
  * Opción 2: archivos de modelo separados
    * Flujo de trabajo de generación de música ACE-Step 1.5
    * Descargas de modelos separados
  * Características clave de ACE-Step 1.5 en ComfyUI
    * Planificación con Chain-of-Thought
    * Arquitectura híbrida LM + DiT
  * Próximamente en ComfyUI
  * Recursos relacionados de ACE-Step 1.5 en ComfyUI



ACE-Step

# ACE-Step 1.5 en ComfyUI: generación local de música con IA

Copiar páginaCopiar página

Genera canciones completas en local en ComfyUI con ACE-Step 1.5, un modelo de música de código abierto que convierte texto y letras opcionales en audio.

Copiar páginaCopiar página

ACE-Step 1.5 es un modelo de generación de música de código abierto de ACE Studio y StepFun que convierte una descripción de texto y letras opcionales en una canción completa. ComfyUI lo ejecuta de forma nativa, así que puedes generar pistas completas localmente, desde bucles de 10 segundos hasta composiciones de varios minutos. En el núcleo del modelo hay un planificador de modelo de lenguaje emparejado con un decodificador de audio Diffusion Transformer (DiT). El planificador expande una consulta simple en un plano de canción, sintetizando estructura, metadatos, letras y descripciones mediante razonamiento de cadena de pensamiento, y el DiT renderiza el audio. La alineación se apoya en los mecanismos internos del propio modelo en lugar de un modelo de recompensa externo o datos de preferencia humana. La generación es lo bastante rápida para sesiones interactivas: menos de 2 segundos para una canción completa en una A100 y menos de 10 segundos en una RTX 3090. La configuración de menos de 4 GB de VRAM ejecuta solo el DiT con el planificador LM desactivado. Entrenar un LoRA con unas pocas canciones es suficiente para capturar tu propio estilo.

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

**Puntos destacados del modelo** :

  * **Calidad de nivel comercial** : Calidad superior a la de la mayoría de los modelos de música comerciales, con una puntuación de coherencia musical de 4.72
  * **Generación rápida** : Una canción completa en menos de 2 segundos en una A100, o menos de 10 segundos en una RTX 3090
  * **Salida de larga duración** : Duraciones desde 10 segundos hasta 10 minutos
  * **Más de 50 idiomas** : Sólido soporte para inglés, chino, japonés, coreano, español, alemán, francés, portugués, italiano y ruso
  * **Ajuste fino con LoRA** : Personalización ligera mediante entrenamiento de LoRA en ComfyUI



## 

​

Opción 1: Checkpoint todo en uno (recomendado)

La versión AIO empaqueta todos los modelos en un solo archivo checkpoint, lo que facilita su descarga y administración.

### 

​

ACE-Step 1.5 Music Generation AIO

Ingresa etiquetas de estilo y letras para generar una canción completa. El flujo de trabajo usa el modelo ACE-Step 1.5 para producir música de calidad comercial en menos de 10 segundos en hardware de consumo.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “ACE-Step 1.5 Music Generation AIO” en la Biblioteca de plantillas

### 

​

Descarga del modelo AIO

## ace_step_1.5_turbo_aio.safetensors

Archivo checkpoint todo en uno (recomendado para la mayoría de los usuarios).

**Ubicación de almacenamiento del modelo AIO**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── ace_step_1.5_turbo_aio.safetensors
    

## 

​

Opción 2: archivos de modelo separados

La versión separada te permite descargar cada componente del modelo por individual.

### 

​

Flujo de trabajo de generación de música ACE-Step 1.5

Introduce un prompt de texto que describa el estilo musical y, opcionalmente, la letra. Genera una canción de audio completa y de alta calidad en menos de 10 segundos en hardware de consumo.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “ACE-Step 1.5 Music Generation Workflow” en la Biblioteca de plantillas

### 

​

Descargas de modelos separados

## acestep_v1.5_turbo.safetensors

Modelo de difusión.

## qwen_0.6b_ace15.safetensors

Codificador de texto (0.6B).

## qwen_1.7b_ace15.safetensors

Codificador de texto (1.7B).

## ace_1.5_vae.safetensors

Modelo VAE.

**Ubicación de almacenamiento de los modelos separados**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── acestep_v1.5_turbo.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_0.6b_ace15.safetensors
    │   │   └── qwen_1.7b_ace15.safetensors
    │   └── 📂 vae/
    │       └── ace_1.5_vae.safetensors
    

## 

​

Características clave de ACE-Step 1.5 en ComfyUI

### 

​

Planificación con Chain-of-Thought

El modelo ACE-Step 1.5 sintetiza metadatos, letras y descripciones mediante razonamiento Chain-of-Thought para guiar el proceso de diffusion, lo que da como resultado composiciones de larga duración más coherentes.

### 

​

Arquitectura híbrida LM + DiT

ACE-Step 1.5 combina un modelo de lenguaje que planifica la estructura de la canción con un Diffusion Transformer (DiT) que se encarga de la síntesis de audio, y todo se ejecuta de forma nativa en ComfyUI.

## 

​

Próximamente en ComfyUI

Estas funciones están disponibles en ACE-Step 1.5, pero aún no son compatibles con ComfyUI:

  * **Cover** : Dale al modelo cualquier canción como entrada junto con un nuevo prompt y una letra, y reimaginará la pista en un estilo completamente distinto.
  * **Repaint** : Selecciona un segmento, vuelve a generar solo esa parte y el modelo la integra de nuevo mientras mantiene todo lo demás intacto.



## 

​

Recursos relacionados de ACE-Step 1.5 en ComfyUI

  * [Página del proyecto](https://ace-step.github.io/)
  * [Hugging Face](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)
  * [GitHub](https://github.com/ace-step/ACE-Step)
  * [Entrada del blog](https://blog.comfy.org/p/ace-step-15-is-now-available-in-comfyui)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/audio/ace-step/ace-step-v1-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/audio/ace-step/ace-step-v1-5)

[ACE-Step 1.0](https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1)[Preprocesadores](https://docs.comfy.org/es/tutorials/utility/preprocessors)
