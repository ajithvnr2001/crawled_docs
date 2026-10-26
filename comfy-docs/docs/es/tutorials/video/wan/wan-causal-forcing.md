---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-causal-forcing/
title: Ejemplo de flujo de trabajo de Causal Forcing I2V en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.007795+00:00
---

# Ejemplo de flujo de trabajo de Causal Forcing I2V en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-causal-forcing/

## En esta página

Volver arriba

  * Cómo funciona
    * Causal Forcing vs Causal Forcing++
  * Usar el flujo de trabajo
    * Entradas
    * Parámetros del subgrafo WAN I2V
  * Pasos para ejecutar
  * Descarga de modelos
    * Wan2.1 I2V
    * CLIP y VAE
    * Ubicación de almacenamiento de modelos



Wan2.1

# Ejemplo de flujo de trabajo de Causal Forcing I2V en ComfyUI

Copiar páginaCopiar página

Genera video a partir de imágenes con Causal Forcing o Causal Forcing++ y Wan2.1. Logra un video suave y temporalmente coherente en tan solo 1 paso de inferencia.

Copiar páginaCopiar página

**Causal Forcing** es una técnica de generación de video que aplica **conditioning recurrente** durante la inferencia, en la que cada fotograma generado se devuelve al modelo para predecir el siguiente fotograma. Así se obtienen videos suaves y coherentes en el tiempo a partir de una sola imagen inicial en tan solo **1 a 4 pasos de inferencia**. Este flujo de trabajo usa **Wan2.1** y admite tanto el modo **Causal Forcing** (estándar) como **Causal Forcing++** (mejorado). ![Flujo de trabajo I2V de Causal Forcing](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_causal_forcing_i2v-1.webp)

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

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Causal Forcing” en la Biblioteca de plantillas

**Materiales de entrada**

## girl_riding_a_wolf.png

Imagen de entrada para el primer fotograma. Descárgala y úsala, o reemplázala por una tuya.

## 

​

Cómo funciona

A diferencia de la generación de video estándar, que procesa todos los fotogramas en paralelo, Causal Forcing trata la generación de video como un **proceso secuencial** :

  1. El modelo toma una imagen de entrada como **primer fotograma**
  2. Genera el siguiente fotograma condicionado por el anterior
  3. Cada nuevo fotograma se convierte en la entrada para la siguiente predicción
  4. Esto se repite durante el número de fotogramas deseado

Este enfoque recurrente crea una **fuerte consistencia temporal** : cada fotograma surge de forma natural del anterior. Esto puede producir resultados de alta calidad con muy pocos pasos de inferencia (de 1 a 4).

## Acerca de Subgraph

Este flujo de trabajo usa un nodo Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

### 

​

Causal Forcing vs Causal Forcing++

Modo| Descripción  
---|---  
**Causal Forcing**|  conditioning recurrente estándar. Buena calidad con 2–4 pasos.  
**Causal Forcing++**|  Modo mejorado que aplica conditioning adicional para una mejor coherencia temporal. Funciona bien con solo 1–2 pasos.  
  
## 

​

Usar el flujo de trabajo

### 

​

Entradas

El flujo de trabajo acepta una sola imagen de entrada (el primer fotograma) y un prompt de texto que describe el contenido de video deseado (opcional).

Ajuste| Descripción  
---|---  
**first_frame** (requerido)| La imagen inicial del video. Carga un PNG/JPG con el nodo **LoadImage**.  
**positive_prompt** (opcional)| Una descripción de texto del contenido de video deseado. Déjalo vacío para no aplicar conditioning.  
**duration** (opcional)| El número de fotogramas a generar. Predeterminado: el número de fotogramas de la salida esperada del modelo.  
  
### 

​

Parámetros del subgrafo WAN I2V

Se exponen como controles en el nodo del subgrafo del plano:

Parámetro| Predeterminado| Descripción  
---|---|---  
`unet_name`| -| El checkpoint del modelo Wan2.1 I2V que se va a usar  
`clip_name`| -| El modelo CLIP / codificador de texto para el prompt  
`vae_name`| -| El modelo VAE para codificar/decodificar  
`width`| -| Ancho del video de salida  
`height`| -| Alto del video de salida  
`noise_seed`| -| Semilla para la reproducibilidad  
  
## 

​

Pasos para ejecutar

  1. **Carga una imagen** : usa el nodo **LoadImage** para cargar tu fotograma inicial
  2. **Escribe un prompt** (opcional): describe el contenido de video que deseas
  3. **Establece la duración** : cuántos fotogramas generar
  4. **Selecciona los modelos** : elige el checkpoint, CLIP y VAE de Wan2.1 I2V
  5. **Elige el modo** : Causal Forcing o Causal Forcing++ (configúralo mediante la configuración interna del subgrafo o una entrada específica de Causal Forcing si está disponible)
  6. **Ejecuta** : los fotogramas se generarán de forma secuencial y se guardarán en `ComfyUI/output/`



## 

​

Descarga de modelos

Descarga el modelo Wan2.1 I2V y los archivos necesarios. Colócalos en los subdirectorios correspondientes de `models/`.

### 

​

Wan2.1 I2V

## Wan2.1 I2V 14B

wan2.1_i2v_480p_14B_fp16.safetensors - checkpoint Wan2.1 I2V 14B

## Wan2.1 I2V 1.3B

wan2.1_t2v_1.3B_fp16.safetensors - checkpoint Wan2.1 1.3B (8 GB de VRAM como mínimo)

### 

​

CLIP y VAE

## CLIP (google-bert)

google-bert/bert-base-uncased - codificador de texto CLIP

## VAE (Wan2.1)

Wan2.1_VAE_bf16.safetensors - VAE de Wan2.1

### 

​

Ubicación de almacenamiento de modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      └── wan2.1_i2v_480p_14B_fp16.safetensors (or 1.3B variant)
    │   ├── 📂 text_encoders/
    │   │      └── bert-base-uncased (folder with model.safetensors)
    │   └── 📂 vae/
    │          └── Wan2.1_VAE_bf16.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-causal-forcing.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-causal-forcing)

[InfiniteTalk](https://docs.comfy.org/es/tutorials/video/wan/wan-infinitetalk)[Wan2.1 VACE](https://docs.comfy.org/es/tutorials/video/wan/vace)
