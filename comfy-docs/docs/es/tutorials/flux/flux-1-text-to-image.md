---
url: https://docs.comfy.org/es/tutorials/flux/flux-1-text-to-image/
title: Ejemplo de flujo de trabajo de texto a imagen con Flux.1 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:42.424254+00:00
---

# Ejemplo de flujo de trabajo de texto a imagen con Flux.1 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-1-text-to-image/

## En esta página

Volver arriba

  * Ejemplo de texto a imagen con Flux.1 versión completa
    * Flux.1 Dev
    * Flux.1 Dev fp8: texto a imagen
    * 1\. Archivo del flujo de trabajo
    * 2\. Instalación manual de modelos
    * 3\. Pasos para ejecutar el flujo de trabajo
    * Flux.1 Schnell
    * Flux.1 Schnell FP8
    * 1\. Archivo del flujo de trabajo
    * 2\. Instalación manual de modelos
    * 3\. Pasos para ejecutar el flujo de trabajo
  * Ejemplo de texto a imagen con la versión FP8 del checkpoint Flux.1
    * Flux.1 Dev
    * Flux.1 Dev: texto a imagen
    * Flux.1 Schnell
    * Flux.1 Schnell FP8



FLUX

# Ejemplo de flujo de trabajo de texto a imagen con Flux.1 en ComfyUI

Copiar páginaCopiar página

Genera imágenes a partir de texto con el modelo de código abierto Flux.1 en ComfyUI, con versiones de checkpoint full y FP8 y una configuración paso a paso.

Copiar páginaCopiar página

![Flux](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_example.png?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=199a3f0f9e2381586b482029d246f4bb) Flux es uno de los modelos de generación de texto a imagen de código abierto más grandes, con 12B de parámetros y un tamaño de archivo original de aproximadamente 23GB. Fue desarrollado por [Black Forest Labs](https://blackforestlabs.ai/), un equipo fundado por antiguos miembros del equipo de Stable Diffusion. Flux es conocido por su excelente calidad de imagen y su flexibilidad, y es capaz de generar imágenes diversas y de alta calidad. Actualmente, el modelo Flux.1 tiene varias versiones principales:

  * **Flux.1 Pro:** El modelo con mejor rendimiento, de código cerrado, disponible únicamente mediante llamadas a la API.
  * **[Flux.1 [dev]:](https://huggingface.co/black-forest-labs/FLUX.1-dev)** De código abierto pero limitado a uso no comercial, destilado de la versión Pro, con un rendimiento cercano al de la versión Pro.
  * **[Flux.1 [schnell]:](https://huggingface.co/black-forest-labs/FLUX.1-schnell)** Usa la licencia Apache2.0, requiere solo 4 pasos para generar imágenes y es adecuado para hardware de bajas prestaciones.

**Características del modelo Flux.1**

  * **Arquitectura híbrida:** Combina las ventajas de las redes Transformer y de los modelos de difusión, integrando de forma eficaz la información de texto e imagen, mejorando la precisión de la alineación entre las imágenes generadas y los prompts, con una excelente fidelidad ante prompts complejos.
  * **Escala de parámetros:** Flux tiene 12B de parámetros, captura relaciones de patrones más complejas y genera imágenes más realistas y diversas.
  * **Compatible con múltiples estilos:** Admite estilos diversos, con un rendimiento excelente en distintos tipos de imágenes.

En este ejemplo, presentaremos ejemplos de texto a imagen usando tanto Flux.1 Dev como Flux.1 Schnell, incluyendo el modelo de versión completa y la versión simplificada FP8 Checkpoint.

  * **Flux versión completa:** El mejor rendimiento, pero requiere más recursos de VRAM y la instalación de varios archivos de modelo.
  * **Flux FP8 Checkpoint:** Requiere solo un modelo en versión fp8, pero la calidad se reduce ligeramente en comparación con la versión completa.



Los metadatos de todas las imágenes de los flujos de trabajo contienen la información de descarga del modelo correspondiente. Puedes cargar los flujos de trabajo de estas formas:

  * Arrastrándolos directamente a ComfyUI
  * O usando el menú `Workflows` -> `Open（ctrl+o）`

Si no usas la versión Desktop o algunos modelos no se pueden descargar automáticamente, consulta las secciones de instalación manual para guardar los archivos de modelo en la carpeta correspondiente. Asegúrate de que tu ComfyUI esté actualizado a la última versión antes de empezar.

## 

​

Ejemplo de texto a imagen con Flux.1 versión completa

Si no puedes descargar los modelos de [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev), asegúrate de haber iniciado sesión en Huggingface y aceptado el acuerdo de licencia del repositorio correspondiente.![Acuerdo de Flux](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flux_agreement.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=7171d72127bc5b3d6943996a9ef06970)

### 

​

Flux.1 Dev

### 

​

Flux.1 Dev fp8: texto a imagen

Genera imágenes con la versión cuantizada fp8 de Flux.1 Dev. Adecuada para dispositivos con VRAM limitada, solo requiere un archivo de modelo, pero la calidad de imagen es ligeramente inferior a la de la versión completa. ![Vista previa del flujo de trabajo Flux.1 Dev fp8](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_dev_checkpoint_example-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Dev fp8” en la biblioteca de plantillas

**Salida de ejemplo** ![Salida de ejemplo de Flux.1 Dev fp8](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_dev_checkpoint_example.png)

#### 

​

1\. Archivo del flujo de trabajo

#### 

​

2\. Instalación manual de modelos

  * El archivo `flux1-dev.safetensors` requiere aceptar el acuerdo de [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) antes de descargarlo desde el navegador.
  * Si tu VRAM es baja, puedes probar a usar [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors?download=true) en lugar del archivo `t5xxl_fp16.safetensors`.



Descarga los siguientes archivos de modelo:

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp16.safetensors?download=true) Recomendado cuando tu VRAM es superior a 32 GB.
  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)
  * [flux1-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/flux1-dev.safetensors)

Ubicación de almacenamiento:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp16.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    │   └── diffusion_models/
    │       └── flux1-dev.safetensors
    

#### 

​

3\. Pasos para ejecutar el flujo de trabajo

Consulta la imagen a continuación para asegurarte de que todos los archivos de modelo estén cargados correctamente. ![Flujo de trabajo de ComfyUI Flux Dev](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_dev_t5fp16.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=fbdc3a3b3b795328425b4ab854b77f13)

  1. Asegúrate de que el nodo `DualCLIPLoader` tenga cargados los siguientes modelos: 
     * clip_name1: t5xxl_fp16.safetensors
     * clip_name2: clip_l.safetensors
  2. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `flux1-dev.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `ae.safetensors`
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



Gracias a la excelente capacidad de Flux para seguir el prompt, no necesitamos ningún prompt negativo

### 

​

Flux.1 Schnell

### 

​

Flux.1 Schnell FP8

Genera imágenes rápidamente con la versión cuantizada fp8 de Flux.1 Schnell. Ideal para hardware de gama baja, solo requiere 4 pasos para generar imágenes. ![Vista previa del flujo de trabajo Flux.1 Schnell FP8](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Schnell” en la biblioteca de plantillas

#### 

​

1\. Archivo del flujo de trabajo

#### 

​

2\. Instalación manual de modelos

En este flujo de trabajo, solo dos archivos de modelo son diferentes respecto al flujo de trabajo de la versión Flux1 Dev. Para t5xxl, puedes seguir usando la versión fp16 para obtener mejores resultados.

  * **t5xxl_fp16.safetensors** -> **t5xxl_fp8.safetensors**
  * **flux1-dev.safetensors** -> **flux1-schnell.safetensors**



Lista completa de archivos de modelo:

  * [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors?download=true)
  * [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors?download=true)
  * [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/ae.safetensors?download=true)
  * [flux1-schnell.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/main/flux1-schnell.safetensors)

Ubicación de almacenamiento de los archivos:
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   ├── clip_l.safetensors
    │   │   └── t5xxl_fp8_e4m3fn.safetensors
    │   ├── vae/
    │   │   └── ae.safetensors
    │   └── diffusion_models/
    │       └── flux1-schnell.safetensors
    

#### 

​

3\. Pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de la versión Flux Schnell](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/flux/flow_diagram_flux_schnell_t5fp8.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=6ce852c65510f40dde8069dc6370869d)

  1. Asegúrate de que el nodo `DualCLIPLoader` tenga cargados los siguientes modelos: 
     * clip_name1: t5xxl_fp8_e4m3fn.safetensors
     * clip_name2: clip_l.safetensors
  2. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `flux1-schnell.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `ae.safetensors`
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Ejemplo de texto a imagen con la versión FP8 del checkpoint Flux.1

La versión fp8 es una versión cuantizada de la versión original Flux.1 fp16. Hasta cierto punto, la calidad de esta versión será inferior a la de la versión fp16, pero también requiere menos VRAM y solo necesitas instalar un archivo de modelo para probar a ejecutarla.

### 

​

Flux.1 Dev

### 

​

Flux.1 Dev: texto a imagen

Genera imágenes de alta calidad con la versión completa de Flux Dev. Requiere más VRAM y varios archivos de modelo, pero ofrece la mejor capacidad de seguimiento del prompt. ![Vista previa del flujo de trabajo de texto a imagen de Flux.1 Dev](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_dev_full_text_to_image-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Dev FP8” en la Biblioteca de plantillas

**Ejemplo de resultado** ![Ejemplo de resultado del checkpoint Flux.1 Dev FP8](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/flux_dev_full_text_to_image.png) Descarga la imagen a continuación y arrástrala a ComfyUI para cargar el flujo de trabajo. Descarga [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors?download=true) y guárdalo en el directorio `ComfyUI/models/checkpoints/`. Asegúrate de que el nodo `Load Checkpoint` correspondiente cargue `flux1-dev-fp8.safetensors` y ya puedes probar a ejecutar el flujo de trabajo.

### 

​

Flux.1 Schnell

### 

​

Flux.1 Schnell FP8

Genera imágenes rápidamente con la versión cuantizada FP8 de Flux.1 Schnell. Ideal para hardware de gama baja, solo requiere 4 pasos para generar imágenes. ![Vista previa del flujo de trabajo del checkpoint Flux.1 Schnell FP8](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Flux.1 Schnell FP8” en la Biblioteca de plantillas

Descarga la imagen a continuación y arrástrala a ComfyUI para cargar el flujo de trabajo. Descarga [flux1-schnell-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-schnell/blob/main/flux1-schnell-fp8.safetensors?download=true) y guárdalo en el directorio `ComfyUI/models/checkpoints/`. Asegúrate de que el nodo `Load Checkpoint` correspondiente cargue `flux1-schnell-fp8.safetensors` y ya puedes probar a ejecutar el flujo de trabajo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-1-text-to-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-1-text-to-image)

[FLUX.1 Kontext Dev](https://docs.comfy.org/es/tutorials/flux/flux-1-kontext-dev)[ByteDance USO](https://docs.comfy.org/es/tutorials/flux/flux-1-uso)
