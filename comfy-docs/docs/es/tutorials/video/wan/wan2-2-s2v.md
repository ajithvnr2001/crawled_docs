---
url: https://docs.comfy.org/es/tutorials/video/wan/wan2-2-s2v/
title: Wan2.2-S2V en ComfyUI: generaci\u00f3n de video a partir de audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:02.231315+00:00
---

# Wan2.2-S2V en ComfyUI: generación de video a partir de audio - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan2-2-s2v/

## En esta página

Volver arriba

  * Flujo de trabajo nativo de Wan2.2 S2V en ComfyUI
    * Generación de video a partir de audio con Wan2.2-S2V
    * 2\. Enlaces de modelos
    * 3\. Instrucciones del flujo de trabajo
    * 3.1 Acerca de Lightning LoRA
    * 3.2 Acerca de los modelos fp8_scaled y bf16
    * 3.3 Instrucciones de operación paso a paso



Wan Video

# Wan2.2-S2V en ComfyUI: generación de video a partir de audio

Copiar páginaCopiar página

Anima un retrato con audio usando el flujo de trabajo Wan2.2-S2V en ComfyUI: modelos de difusión 14B fp8 o bf16 y extensión de video.

Copiar páginaCopiar página

¡Nos emociona anunciar que Wan2.2-S2V, el avanzado modelo de generación de video a partir de audio, ya es compatible de forma nativa con ComfyUI! Este potente modelo de IA puede transformar imágenes estáticas y entradas de audio en contenido de video dinámico, con soporte para diálogos, canto, actuaciones y diversas necesidades de contenido creativo. **Aspectos destacados del modelo**

  * **Generación de video a partir de audio** : transforma imágenes estáticas y audio en videos sincronizados
  * **Calidad cinematográfica** : genera videos con calidad de cine y expresiones y movimientos naturales
  * **Generación de varios minutos** : admite la creación de videos de larga duración
  * **Soporte multiformato** : funciona con personajes de cuerpo completo y de medio cuerpo
  * **Control de movimiento mejorado** : genera acciones y entornos a partir de instrucciones de texto

Código de Wan2.2 S2V: [GitHub](https://github.com/aigc-apps/VideoX-Fun) Modelo Wan2.2 S2V: [Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-S2V-14B)

## 

​

Flujo de trabajo nativo de Wan2.2 S2V en ComfyUI

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

### 

​

Generación de video a partir de audio con Wan2.2-S2V

Transforma imágenes estáticas y audio en videos dinámicos con una sincronización perfecta y generación de varios minutos. ![Vista previa del flujo de trabajo de generación de video a partir de audio con Wan2.2-S2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_s2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.2 S2V” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos correspondientes:

## video_wan2_2_14B_s2v_reference_image.jpg

Nodo `LoadImage` 52 · `video_wan2_2_14B_s2v_reference_image.jpg`

## video_wan2_2_14B_s2v_input_audio.MP3

Nodo `LoadAudio` 58 · `video_wan2_2_14B_s2v_input_audio.MP3`

![video_wan2_2_14B_s2v_reference_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2_2_14B_s2v_reference_image.jpg)

### 

​

2\. Enlaces de modelos

Puedes encontrar los modelos en [nuestro repositorio](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged) **diffusion_models**

## wan2.2_s2v_14B_fp8_scaled.safetensors

Modelo de difusión FP8 scaled. Colócalo en `ComfyUI/models/diffusion_models/`

## wan2.2_s2v_14B_bf16.safetensors

Modelo de difusión BF16. Colócalo en `ComfyUI/models/diffusion_models/`

**audio_encoders**

## wav2vec2_large_english_fp16.safetensors

Modelo de codificador de audio. Colócalo en `ComfyUI/models/audio_encoders/`

**vae**

## wan_2.1_vae.safetensors

Modelo VAE de Wan2.1. Colócalo en `ComfyUI/models/vae/`

**text_encoders**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto FP8 scaled. Colócalo en `ComfyUI/models/text_encoders/`
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_s2v_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_s2v_14B_bf16.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   ├───📂 audio_encoders/ # Crea una si no encuentras esta carpeta
    │   │   └─── wav2vec2_large_english_fp16.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Instrucciones del flujo de trabajo

![Instrucciones del flujo de trabajo](https://mintcdn.com/dripart/ht3vzHrjy1qaRsl9/images/tutorial/video/wan/wan_2.2_14b_s2v.jpg?fit=max&auto=format&n=ht3vzHrjy1qaRsl9&q=85&s=295f87179e12d937cbfbcc3e21d474c0)

#### 

​

3.1 Acerca de Lightning LoRA

#### 

​

3.2 Acerca de los modelos fp8_scaled y bf16

Puedes encontrar ambos modelos [aquí](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models):

## wan2.2_s2v_14B_fp8_scaled.safetensors

Modelo de difusión FP8 scaled

## wan2.2_s2v_14B_bf16.safetensors

Modelo de difusión BF16

Esta plantilla usa `wan2.2_s2v_14B_fp8_scaled.safetensors`, que requiere menos VRAM. Pero puedes probar `wan2.2_s2v_14B_bf16.safetensors` para reducir la degradación de calidad.

#### 

​

3.3 Instrucciones de operación paso a paso

**Paso 1: Cargar modelos**

  1. **Cargar modelo de difusión** : carga `wan2.2_s2v_14B_fp8_scaled.safetensors` o `wan2.2_s2v_14B_bf16.safetensors`
     * El flujo de trabajo incluido usa `wan2.2_s2v_14B_fp8_scaled.safetensors`, que requiere menos VRAM
     * Pero puedes probar `wan2.2_s2v_14B_bf16.safetensors` para reducir la degradación de calidad
  2. **Cargar CLIP** : carga `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. **Cargar VAE** : carga `wan_2.1_vae.safetensors`
  4. **AudioEncoderLoader** : carga `wav2vec2_large_english_fp16.safetensors`
  5. **LoraLoaderModelOnly** : carga `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors` (Lightning LoRA)
     * Probamos todos los LoRA lightning de wan2.2. Como este no es un LoRA entrenado específicamente para Wan2.2 S2V, muchos valores clave no coinciden, pero lo añadimos porque reduce significativamente el tiempo de generación. Seguiremos optimizando esta plantilla
     * Usarlo provoca una pérdida notable de dinamismo y calidad
     * Si consideras que la calidad de salida es demasiado baja, puedes probar el flujo de trabajo original de 20 pasos
  6. **LoadAudio** : sube el archivo de audio que proporcionamos o tu propio audio
  7. **Cargar imagen** : sube la imagen de referencia
  8. **Tamaños de lote** : configúralos según la cantidad de nodos de subgrafo Video S2V Extend que añadas
     * Cada subgrafo Video S2V Extend añade 77 fotogramas a la salida final
     * Por ejemplo: si añadiste 2 subgrafos Video S2V Extend, el tamaño de lote debe ser 3, lo que representa el número total de iteraciones de muestreo
     * **Chunk Length** : mantén el valor predeterminado de 77
  9. **Configuraciones del sampler** : elige configuraciones distintas según si usas Lightning LoRA
     * Con Lightning LoRA de 4 pasos: steps: 4, cfg: 1.0
     * Sin Lightning LoRA de 4 pasos: steps: 20, cfg: 6.0
  10. **Configuraciones de tamaño** : define las dimensiones del video de salida
  11. **Video S2V Extend** : nodos de subgrafo de extensión de video. Como nuestro valor predeterminado de fotogramas por muestreo es 77 y este es un modelo de 16 fps, cada extensión generará 77 / 16 = 4.8125 segundos de video
     * Necesitas hacer algunos cálculos para que la cantidad de nodos de subgrafo de extensión de video coincida con la duración del audio de entrada. Por ejemplo: si el audio de entrada dura 14 s, el total de fotogramas necesarios es 14x16=224 y cada extensión de video son 77 fotogramas, así que necesitas 224/77 = 2.9, redondeado hacia arriba a 3 nodos de subgrafo de extensión de video
  12. Usa Ctrl-Enter o haz clic en el botón Run para ejecutar el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan2-2-s2v.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan2-2-s2v)

[Wan Dancer](https://docs.comfy.org/es/tutorials/video/wan/wan-dancer)[Wan2.2 Fun Inp](https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-inp)
