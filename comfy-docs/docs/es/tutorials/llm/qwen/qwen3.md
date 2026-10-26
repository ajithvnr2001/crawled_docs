---
url: https://docs.comfy.org/es/tutorials/llm/qwen/qwen3/
title: Ejemplo de flujo de trabajo de Qwen 3.0 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.780013+00:00
---

# Ejemplo de flujo de trabajo de Qwen 3.0 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/llm/qwen/qwen3/

## En esta página

Volver arriba

  * Casos de uso
  * Flujo de trabajo disponible
    * Qwen3.0: generación de texto
  * Descarga del modelo



LLM

# Ejemplo de flujo de trabajo de Qwen 3.0 en ComfyUI

Copiar páginaCopiar página

Qwen 3.0 es el LLM de código abierto de Alibaba Cloud, con gran capacidad de razonamiento; disponible en 4B para texto y razonamiento estructurado.

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

**Qwen 3.0** (también conocido como Qwen3) es un potente LLM de código abierto de Alibaba Cloud diseñado para la generación de texto, el razonamiento y el análisis estructurado. Es compatible de forma nativa con ComfyUI mediante el nodo integrado `TextGenerate`. **Aspectos destacados del modelo** :

  * **Razonamiento sólido** : Qwen3-4B-Thinking admite razonamiento paso a paso con cadena de pensamiento
  * **Enfocado en la generación de texto** : optimizado para la salida de texto estructurado, el análisis y las tareas de programación
  * **Nativo en ComfyUI** : funciona con el nodo integrado `TextGenerate`, sin necesidad de Nodos personalizados
  * **Ligero** : comparte el mismo formato de codificador de texto que Qwen3.5, disponible en variantes de 2B, 4B y 9B para ajustarse a diferentes configuraciones de hardware



## 

​

Casos de uso

Qwen 3.0 es adecuado para tareas que requieren generación de texto estructurado y razonamiento inteligente dentro de un flujo de trabajo de ComfyUI:

  * **Optimización de prompts** : pasa prompts existentes a Qwen 3.0 y pídele que los reescriba, los expanda o los refine para obtener mejores resultados de generación de imágenes. Por ejemplo, convierte un prompt corto de palabras clave en descripciones detalladas y estructuradas con detalles de estilo, iluminación y composición.
  * **Razonamiento sobre la lógica del flujo de trabajo** : usa el modelo para analizar los parámetros del flujo de trabajo, sugerir pasos de procesamiento o generar instrucciones estructuradas que alimenten otros nodos.
  * **Análisis basado en texto** : extrae información, clasifica contenido o genera informes estructurados a partir de entradas de texto.
  * **Razonamiento de cadena de pensamiento** : activa el modo de pensamiento para tareas complejas de varios pasos que se benefician de un razonamiento intermedio antes de producir la salida final.



## 

​

Flujo de trabajo disponible

### 

​

Qwen3.0: generación de texto

Introduce un prompt de texto para generar respuestas detalladas y razonadas con el modelo Qwen3-4B-Thinking. ![Vista previa del flujo de trabajo de generación de texto de Qwen 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_text_gen-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen3.0: Text Generation” en la Biblioteca de plantillas

Este flujo de trabajo demuestra las capacidades fundamentales de **generación de texto** de Qwen 3.0. Acepta un prompt de texto y genera respuestas detalladas y estructuradas usando las capacidades de razonamiento integradas del modelo. **Entradas** :

  * **Prompt de texto** : tu pregunta, instrucción o descripción de la tarea

**Controles principales** :

  * **Longitud máxima** : número máximo de tokens a generar (predeterminado 256)
  * **Modo de muestreo** : activa o desactiva el muestreo y ajusta la temperatura, top-k, top-p, la penalización por repetición y la semilla
  * **Modo de razonamiento** : habilita el razonamiento paso a paso antes de la respuesta final
  * **Usar plantilla predeterminada** : aplica el prompt de sistema integrado del modelo

**Salida** :

  * **Texto generado** : la respuesta del modelo como una cadena de texto simple



## Aprende sobre Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

## 

​

Descarga del modelo

Los modelos Qwen 3.0 se cargan como codificadores de texto en ComfyUI. Los archivos de modelo se comparten con Qwen3.5. Descarga la variante que mejor se adapte a tu hardware:

## Qwen3.5 2B (bf16)

Ligero, ~4.5 GB. Ideal para configuraciones con poca VRAM y descargas rápidas.

## Qwen3.5 4B (bf16)

Equilibrio entre tamaño y calidad. Recomendado para la mayoría de GPU de consumo.

## Qwen3.5 9B (bf16)

La variante más grande, ~19 GB. Salida de mayor calidad, requiere más VRAM.

Coloca el archivo `.safetensors` descargado en:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 text_encoders/
    │       └── qwen3.5_4b_bf16.safetensors   # or 2b / 9b variant
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/llm/qwen/qwen3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/llm/qwen/qwen3)

[Gemma 4](https://docs.comfy.org/es/tutorials/llm/gemma4/gemma4)[Qwen3.5](https://docs.comfy.org/es/tutorials/llm/qwen/qwen3_5)
