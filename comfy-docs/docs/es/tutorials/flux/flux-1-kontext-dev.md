---
url: https://docs.comfy.org/es/tutorials/flux/flux-1-kontext-dev/
title: Ejemplo de flujo de trabajo nativo de FLUX Kontext Dev para ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:42.629210+00:00
---

# Ejemplo de flujo de trabajo nativo de FLUX Kontext Dev para ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-1-kontext-dev/

## En esta página

Volver arriba

  * Acerca de FLUX.1 Kontext Dev
    * Información de las versiones
  * Descarga de modelos
  * Flujo de trabajo de FLUX.1 Kontext Dev
    * Edición de imágenes con FLUX Kontext Dev
    * 1\. Descargar el flujo de trabajo y la imagen de entrada
    * 2\. Completar el flujo de trabajo paso a paso
  * Técnicas de prompts para FLUX Kontext
    * 1\. Modificaciones básicas
    * 2\. Transferencia de estilo
    * 3\. Consistencia de personajes
    * 4\. Edición de texto
  * Soluciones a problemas comunes
    * El personaje cambia demasiado
    * Cambios en la posición de la composición
    * Aplicación imprecisa del estilo
  * Principios fundamentales
  * Plantillas de buenas prácticas



FLUX

# Ejemplo de flujo de trabajo nativo de FLUX Kontext Dev para ComfyUI

Copiar páginaCopiar página

Flujo de trabajo FLUX.1 Kontext Dev para ComfyUI: edita imágenes con entrada de texto e imagen usando el modelo de edición multimodal abierto de 12B de Black Forest Labs.

Copiar páginaCopiar página

## 

​

Acerca de FLUX.1 Kontext Dev

FLUX.1 Kontext es un modelo revolucionario de edición de imágenes multimodal de Black Forest Labs que admite entrada simultánea de texto e imagen, comprende de forma inteligente el contexto de la imagen y realiza ediciones precisas. Su versión de desarrollo es un modelo diffusion transformer de código abierto con 12 mil millones de parámetros, que ofrece una excelente comprensión del contexto y un gran mantenimiento de la consistencia de los personajes, lo que garantiza que elementos clave como los rasgos del personaje y la composición se mantengan estables incluso después de múltiples ediciones iterativas. Comparte las mismas capacidades principales que la suite FLUX.1 Kontext:

  * Consistencia de personajes: conserva los elementos únicos de las imágenes a través de múltiples escenas y entornos, como personajes u objetos de referencia en la imagen.
  * Edición: realiza modificaciones específicas en elementos concretos de la imagen sin afectar a las demás partes.
  * Referencia de estilo: genera escenas nuevas conservando el estilo único de la imagen de referencia según el prompt de texto.
  * Velocidad interactiva: latencia mínima en la generación y edición de imágenes.

Si bien la versión API publicada anteriormente ofrece la máxima fidelidad y velocidad, FLUX.1 Kontext [Dev] se ejecuta por completo en equipos locales, lo que brinda una flexibilidad inigualable a desarrolladores, investigadores y usuarios avanzados que desean experimentar.

### 

​

Información de las versiones

  * **[FLUX.1 Kontext [pro]** : versión comercial, centrada en la edición iterativa rápida
  * **FLUX.1 Kontext [max]** : versión experimental con mayor adherencia al prompt
  * **FLUX.1 Kontext [dev]** : versión de código abierto (la que se usa en este tutorial), 12B de parámetros, principalmente para investigación

Actualmente en ComfyUI puedes usar todas estas versiones: las [versiones Pro y Max](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext) están disponibles a través de los Nodos asociados, mientras que para la versión de código abierto Dev, consulta las instrucciones de esta guía.

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

Descarga de modelos

Para ejecutar correctamente los flujos de trabajo de esta guía, primero necesitas descargar los siguientes archivos de modelo. También puedes obtener directamente los enlaces de descarga de los modelos desde los flujos de trabajo correspondientes, que ya incluyen la información de descarga de los archivos de modelo. **Modelo de difusión**

  * [flux1-dev-kontext_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors)



Si quieres usar los pesos originales, puedes visitar el repositorio correspondiente de Black Forest Labs para obtener y usar los pesos originales del modelo.

**VAE**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**Codificador de texto**

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors) o [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn_scaled.safetensors)

Ubicación de guardado de los archivos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── flux1-dev-kontext_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── ae.safetensor
    │   └── 📂 text_encoders/
    │       ├── clip_l.safetensors
    │       └── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn_scaled.safetensors
    

## 

​

Flujo de trabajo de FLUX.1 Kontext Dev

### 

​

Edición de imágenes con FLUX Kontext Dev

Edición inteligente de imágenes que mantiene la consistencia de los personajes, edita partes específicas sin afectar a las demás y conserva los estilos originales. ![Vista previa del flujo de trabajo de FLUX Kontext Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_kontext_dev_basic-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX Kontext Dev” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## flux_kontext_dev_basic_input_image.jpg

Nodo `LoadImage` 190 · `flux_kontext_dev_basic_input_image.jpg`

![flux_kontext_dev_basic_input_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_kontext_dev_basic_input_image.jpg)

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/flux_kontext_dev_basic_input_image.jpg)![Salida de ejemplo de FLUX Kontext Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_kontext_dev_basic.png)

Este flujo de trabajo usa el nodo `Load Image(from output)` para cargar la imagen que se va a editar, lo que hace más cómodo acceder a la imagen editada para varias rondas de edición.

### 

​

1\. Descargar el flujo de trabajo y la imagen de entrada

### 

​

2\. Completar el flujo de trabajo paso a paso

![Guía paso a paso del flujo de trabajo](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_1_kontext_dev_basic_step_guide.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=90995e36fa39a53693aeff3b560c60ef) Puedes guiarte por los números de la imagen para completar la ejecución del flujo de trabajo:

  1. En el nodo `Load Diffusion Model`, carga el modelo `flux1-dev-kontext_fp8_scaled.safetensors`
  2. En el nodo `DualCLIP Load`, asegúrate de que estén cargados `clip_l.safetensors` y `t5xxl_fp16.safetensors` o `t5xxl_fp8_e4m3fn_scaled.safetensors`
  3. En el nodo `Load VAE`, asegúrate de que el modelo `ae.safetensors` esté cargado
  4. En el nodo `Load Image(from output)`, carga la imagen de entrada proporcionada
  5. En el nodo `CLIP Text Encode`, modifica los prompts; solo se admite inglés
  6. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Técnicas de prompts para FLUX Kontext

### 

​

1\. Modificaciones básicas

  * Simple y directo: `"Change the car color to red"`
  * Mantén el estilo: `"Change to daytime while maintaining the same style of the painting"`



### 

​

2\. Transferencia de estilo

**Principios:**

  * Nombra el estilo con claridad: `"Transform to Bauhaus art style"`
  * Describe las características: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
  * Conserva la composición: `"Change to Bauhaus style while maintaining the original composition"`



### 

​

3\. Consistencia de personajes

**Marco de trabajo:**

  * Descripción específica: `"The woman with short black hair"` en lugar de “ella”
  * Conserva las características: `"while maintaining the same facial features, hairstyle, and expression"`
  * Modificaciones paso a paso: cambia primero el fondo y luego las acciones



### 

​

4\. Edición de texto

  * Usa comillas: `"Replace 'joy' with 'BFL'"`
  * Mantén el formato: `"Replace text while maintaining the same font style"`



## 

​

Soluciones a problemas comunes

### 

​

El personaje cambia demasiado

❌ Incorrecto: `"Transform the person into a Viking"` ✅ Correcto: `"Change the clothes to be a viking warrior while preserving facial features"`

### 

​

Cambios en la posición de la composición

❌ Incorrecto: `"Put him on a beach"` ✅ Correcto: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### 

​

Aplicación imprecisa del estilo

❌ Incorrecto: `"Make it a sketch"` ✅ Correcto: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## 

​

Principios fundamentales

  1. **Sé específico y claro** : usa descripciones precisas y evita términos vagos
  2. **Edición paso a paso** : divide las modificaciones complejas en varios pasos simples
  3. **Preservación explícita** : indica qué debe permanecer sin cambios
  4. **Selección de verbos** : usa “cambiar” y “reemplazar” en lugar de “transformar”



## 

​

Plantillas de buenas prácticas

**Modificación de objeto:** `"Change [object] to [new state], keep [content to preserve] unchanged"` **Transferencia de estilo:** `"Transform to [specific style], while maintaining [composition/character/other] unchanged"` **Reemplazo de fondo:** `"Change the background to [new background], keep the subject in the exact same position and pose"` **Edición de texto:** `"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Recuerda:** Cuanto más específico, mejor. Kontext destaca por comprender instrucciones detalladas y mantener la consistencia.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-1-kontext-dev.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-1-kontext-dev)

[FLUX.1 Krea Dev](https://docs.comfy.org/es/tutorials/flux/flux1-krea-dev)[Flux.1 texto a imagen](https://docs.comfy.org/es/tutorials/flux/flux-1-text-to-image)
