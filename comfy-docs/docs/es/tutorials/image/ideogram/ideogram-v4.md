---
url: https://docs.comfy.org/es/tutorials/image/ideogram/ideogram-v4/
title: Tutorial de Ideogram 4.0 de c\u00f3digo abierto en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.018577+00:00
---

# Tutorial de Ideogram 4.0 de código abierto en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/ideogram/ideogram-v4/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen con Ideogram 4.0
    * Ideogram v4: texto a imagen
    * Formato del prompt
    * Descargas del modelo Ideogram 4.0
    * Pasos del flujo de trabajo
    * Nota sobre el filtro de seguridad
  * Conversación en vivo con Ideogram y ComfyOrg



Ideogram

# Tutorial de Ideogram 4.0 de código abierto en ComfyUI

Copiar páginaCopiar página

Ideogram 4.0 en ComfyUI: ejecuta en local su modelo de texto a imagen de código abierto, con texto preciso y prompts JSON o en lenguaje natural.

Copiar páginaCopiar página

Ideogram 4.0 es el modelo de texto a imagen más reciente de Ideogram, publicado como modelo de código abierto que se ejecuta íntegramente en tu propio hardware. Ofrece una calidad fotorrealista superior, un renderizado de texto preciso y un control de estilo exacto. Puedes usar lenguaje natural sin más o **prompts JSON estructurados** para controlar con precisión el diseño, los colores y el texto dentro de la imagen.

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

Flujo de trabajo de texto a imagen con Ideogram 4.0

### 

​

Ideogram v4: texto a imagen

Introduce un prompt de texto o una descripción JSON estructurada. Genera una imagen con control preciso de diseño, color y estilo usando Ideogram 4.0. ![Vista previa del flujo de trabajo de texto a imagen de Ideogram 4.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ideogram4_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram v4: Text to Image” en la Biblioteca de plantillas

**Ejemplo de salida** ![Ejemplo de salida de Ideogram 4.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_ideogram4_t2i.png)

### 

​

Formato del prompt

El flujo de trabajo de código abierto admite dos modos de prompt:

  1. **Lenguaje natural** : rápido y sencillo, ideal para ideas simples
  2. **JSON estructurado** : para un control preciso del diseño, los colores y el estilo

El flujo de trabajo incluye una plantilla de construcción de prompts que puedes usar con cualquier LLM para generar prompts JSON que coincidan con el formato. Una nota dentro del flujo de trabajo explica:

> El modelo se entrenó con subtítulos JSON estructurados (resumen de la escena, bloque de estilo, fondo y descripciones opcionales por objeto con cuadros delimitadores y paletas de colores hexadecimales). La inferencia oficial valida los prompts contra ese esquema.

### 

​

Descargas del modelo Ideogram 4.0

Puedes encontrar todos los archivos del modelo reempaquetados en [Comfy-Org/Ideogram-4](https://huggingface.co/Comfy-Org/Ideogram-4) en Hugging Face.

## ideogram4_fp8_scaled.safetensors

Modelo de difusión para Ideogram 4.0 (~13.8 GB). Colócalo en `models/diffusion_models/`

## ideogram4_unconditional_fp8_scaled.safetensors

Modelo de difusión incondicional para Ideogram 4.0 (~13.8 GB). Colócalo en `models/diffusion_models/`

## qwen3vl_8b_fp8_scaled.safetensors

Codificador de texto para Ideogram 4.0 (~8 GB). Colócalo en `models/text_encoders/`

## gemma4_e4b_it_fp8_scaled.safetensors

Codificador de texto para Ideogram 4.0 (~2 GB). Colócalo en `models/text_encoders/`

## flux2-vae.safetensors

VAE para Ideogram 4.0 (~335 MB). Colócalo en `models/vae/`

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── ideogram4_fp8_scaled.safetensors
    │   │   └── ideogram4_unconditional_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen3vl_8b_fp8_scaled.safetensors
    │   │   └── gemma4_e4b_it_fp8_scaled.safetensors
    │   └── 📂 vae/
    │       └── flux2-vae.safetensors
    

## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender.

### 

​

Pasos del flujo de trabajo

  1. Descarga los modelos y colócalos en los directorios correctos (consulta la tabla anterior)
  2. Descarga el archivo del flujo de trabajo y arrástralo a ComfyUI
  3. Introduce tu prompt (lenguaje natural o JSON estructurado) en el nodo del subgrafo Ideogram4
  4. (Opcional) Ajusta la resolución con el nodo `ResolutionSelector`
  5. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  6. Revisa el resultado en el nodo `Save Image`. Los archivos de salida se guardan en `ComfyUI/output/`



### 

​

Nota sobre el filtro de seguridad

Si ves “Image blocked by safety filter”, se trata del filtro de seguridad integrado de Ideogram 4.0. Los prompts que no son JSON (texto plano) tienen una tasa más alta de falsos positivos. Usar prompts JSON estructurados reduce la probabilidad de que tu prompt sea bloqueado. Para más detalles, consulta la [guía oficial de prompts de Ideogram 4](https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md#safety-filter).

## 

​

Conversación en vivo con Ideogram y ComfyOrg

Una conversación en vivo especial con Mohammad Norouzi (CEO de Ideogram) y Yoland Yan (CEO de ComfyOrg), presentada por Purz y Rob.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/ideogram/ideogram-v4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/ideogram/ideogram-v4)

[Krea 2](https://docs.comfy.org/es/tutorials/image/krea/krea-2)[Mage-Flow](https://docs.comfy.org/es/tutorials/image/mage-flow/mage-flow)
