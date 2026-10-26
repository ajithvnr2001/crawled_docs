---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-animate-2/
title: Wan Animate 2: transferencia de movimiento - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:00.873229+00:00
---

# Wan Animate 2: transferencia de movimiento - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-animate-2/

## En esta página

Volver arriba

  * Puntos destacados del modelo
  * Flujo de trabajo de Wan Animate 2
    * Descarga de modelos
    * Instrucciones del flujo de trabajo
    * Extender a videos más largos



Wan Video

# Wan Animate 2: transferencia de movimiento

Copiar páginaCopiar página

Anima un personaje estático con Wan Animate 2 en ComfyUI: transfiere el movimiento desde un video guía directamente, sin extracción de poses ni preprocesamiento de esqueleto.

Copiar páginaCopiar página

Wan Animate 2 es un framework de animación de personajes de extremo a extremo del equipo de Wan que consume directamente videos guía en un Diffusion Transformer rediseñado. Logra una generación de movimiento de alta fidelidad y una fuerte preservación de la identidad al eliminar los extractores de movimiento intermedios: no se necesita extracción de pose ni preprocesamiento de esqueletos. El modelo también añade control de perspectiva impulsado por texto, lo que desacopla la perspectiva de la cámara de salida del video de conducción. Esto te permite animar a un personaje estático usando un video de conducción mientras controlas la cámara de forma independiente, e incluso generar un fondo nuevo a partir de tu prompt de texto.

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

Puntos destacados del modelo

  * **Transferencia directa de movimiento** : Anima a un personaje estático a partir de un video guía sin extracción de pose ni preprocesamiento de esqueleto
  * **Preservación de la identidad** : Mantiene intactas la identidad, la apariencia y los detalles del personaje de referencia
  * **Control de cámara por texto** : Desacopla la perspectiva de la cámara de salida respecto del video guía
  * **Fondos nuevos** : Genera un fondo nuevo a partir de tu prompt de texto en lugar de copiar el fondo del video guía
  * **Movimiento de alta fidelidad** : Replica movimientos y expresiones complejas del video guía



## 

​

Flujo de trabajo de Wan Animate 2

Anima un personaje estático con un video guía, transfiriendo el movimiento directamente desde los fotogramas del video. La salida conserva la identidad del personaje de referencia y, al mismo tiempo, genera un fondo nuevo y un movimiento de cámara a partir de tu prompt de texto.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan Animate 2” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos correspondientes:

## Imagen de referencia

Nodo `LoadImage`: pink_hair_mech_arms_ref.png (el personaje que se va a animar)

## Video guía

Nodo `LoadVideo`: street_dance_drive.mp4 (la fuente del movimiento)

### 

​

Descarga de modelos

Este flujo de trabajo usa el modelo de difusión `wan_animate_2_int8_convrot.safetensors`. El repositorio también incluye variantes BF16 y destiladas; si prefieres usarlas, cambia la selección de modelo en el nodo `UNETLoader`. Todos los archivos están disponibles en el repositorio [Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2):

## Modelo de difusión (INT8, obligatorio)

wan_animate_2_int8_convrot.safetensors: Modelo de difusión cuantizado INT8 convrot que usa este flujo de trabajo

## Modelo de difusión (BF16, opcional)

wan_animate_2_bf16.safetensors: Modelo base de precisión completa. Requiere cambiar la selección de modelo en UNETLoader.

## Modelo de difusión (destilado INT8, opcional)

wan_animate_2_distill_int8_convrot.safetensors: Variante INT8 destilada. Requiere cambiar la selección de modelo en UNETLoader.

## Modelo de difusión (destilado BF16, opcional)

wan_animate_2_distill_bf16.safetensors: Variante BF16 destilada. Requiere cambiar la selección de modelo en UNETLoader.

## LoRA

lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors: LoRA de aceleración LightX2V

## Codificador de texto

umt5_xxl_fp8_e4m3fn_scaled.safetensors: Codificador de texto UMT5-XXL FP8

## CLIP Vision

clip_vision_h.safetensors: Codificador CLIP Vision

## VAE

Wan2_1_VAE_bf16.safetensors: VAE de Wan2.1 para codificar y decodificar

Coloca los archivos en los siguientes directorios:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── wan_animate_2_bf16.safetensors
    │   │   ├── wan_animate_2_distill_bf16.safetensors
    │   │   ├── wan_animate_2_distill_int8_convrot.safetensors
    │   │   └── wan_animate_2_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   └── 📂 vae/
    │       └── Wan2_1_VAE_bf16.safetensors
    

### 

​

Instrucciones del flujo de trabajo

  1. Asegúrate de que todos los modelos se cargan correctamente
  2. Sube la imagen de referencia: el personaje de esta imagen es el personaje objetivo que se va a animar
  3. Sube el video guía: su movimiento se transfiere al personaje de referencia
  4. Actualiza el prompt para describir la escena, el fondo y el movimiento de cámara que quieres
  5. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar el video



### 

​

Extender a videos más largos

Los videos más largos se gestionan dentro del flujo de trabajo: el Subgraph `Motion Transfer (Wan Animate 2)` itera (`StartLoop` / `EndLoop`) y sigue generando hasta cubrir todo el video guía, así que con un solo Subgraph es suficiente. No hay que duplicar ni recablear nada. Cada iteración del bucle genera 81 fotogramas, unos 3.4 segundos a 24 fps. Ese es el valor `Int (fragment_length)` dentro del Subgraph. Puedes aumentarlo, pero debe mantenerse en una longitud válida de Wan: 81, 85, 89, etcétera, es decir, `4n + 1`. El cálculo del bucle lee el número de fotogramas del video guía, determina cuántas continuaciones hacen falta y recorta el final para que la salida tenga exactamente los mismos fotogramas que el video guía. Cada continuación repite el último fotograma del segmento anterior y ese duplicado se elimina, así que cada segmento adicional añade `fragment_length - 1` fotogramas nuevos. El bucle usa los nodos de bucle del núcleo, así que el flujo de trabajo necesita ComfyUI 0.36.0 o superior. El Subgraph `Video Stitch` es la vista previa comparativa: coloca el video generado junto al video guía. No forma parte de la ruta de extensión.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-animate-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-animate-2)

[LTX-0.9.5](https://docs.comfy.org/es/tutorials/video/ltxv)[Wan2.2](https://docs.comfy.org/es/tutorials/video/wan/wan2_2)
