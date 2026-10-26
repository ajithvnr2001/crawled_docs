---
url: https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-native/
title: Flujos de trabajo de MiniMax H3 en ComfyUI: texto a video, imagen a video y referencia a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:00.402631+00:00
---

# Flujos de trabajo de MiniMax H3 en ComfyUI: texto a video, imagen a video y referencia a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-native/

## En esta página

Volver arriba

  * MiniMax H3 Texto a Video (T2V)
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para el prompt
  * MiniMax H3 Imagen a Video (I2V)
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para el prompt
  * MiniMax H3 Referencia a Video (R2V)
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para el prompt
  * Flujos de trabajo avanzados con los nodos nativos
    * Anclar guías en cualquier frame (#15439)
    * Relleno inteligente y extensión con máscaras de ruido latente (#15375)



MiniMax H3

# Flujos de trabajo de MiniMax H3 en ComfyUI: texto a video, imagen a video y referencia a video

Copiar páginaCopiar página

Ejemplos paso a paso de flujos nativos de MiniMax H3 en ComfyUI, con anclaje de guías y máscaras de ruido latente para un control más fino del video.

Copiar páginaCopiar página

Esta página cubre las tres plantillas base de MiniMax H3 y las técnicas avanzadas con nodos nativos. Para conocer las capacidades, el ajuste y las mejoras de velocidad, consulta la [descripción general de MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3).

## 

​

MiniMax H3 Texto a Video (T2V)

Genera videos a partir de prompts de texto con audio estéreo nativo.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax H3 T2V” en la Biblioteca de plantillas

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_fl2va_pruned_int8_convrot

Coloca en `ComfyUI/models/diffusion_models/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Coloca en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Coloca en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Coloca en `ComfyUI/models/vae/`

## LoRA: minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16

Requerido por el escaneo de modelos del flujo de trabajo; habilita el modo turbo opcional de Lightning LoRA. Coloca en `ComfyUI/models/loras/`

### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   ├── 📂 vae/
    │   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
    │   │   └── minimax_h3_audio_vae_fp32.safetensors
    │   ├── 📂 loras/
    │   │   └── minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors
    │   └── 📂 embeddings/
    │       └── minimaxh3_art_is_explosion.safetensors
    

### 

​

Consejos para el prompt

  1. **Primero la escena** : la escena general, y luego los planos con sus tiempos
  2. **Un solo bloque** : planos, cámara, diálogo, SFX y música juntos
  3. **Resolución** : el 16:9 nativo es **1344×768** (768 px en el lado corto); redondea a múltiplos de **32**
  4. **Duración** : se ajusta a **17k+5** fotogramas a 24 fps
  5. **Primer y último fotograma** : conecta las imágenes a `first_frame` / `last_frame` en `MiniMaxH3ImageToVideo` para FL2VA
  6. **Turbo** : **20** pasos por defecto; activa `turbo_mode` para el Lightning LoRA de **8** pasos (más rápido, con movimiento y audio algo más suaves). Sube los pasos (por ejemplo, **25**) para mejorar la calidad del movimiento

Guía base oficial: [guía de prompts](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide).

## 

​

MiniMax H3 Imagen a Video (I2V)

Genera videos a partir de una imagen de entrada, con fotogramas clave opcionales de inicio y fin.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax H3 I2V” en la Biblioteca de plantillas

## Imagen de entrada: transparent_rgb_gaming_mouse.png

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_fl2va_pruned_int8_convrot

Coloca en `ComfyUI/models/diffusion_models/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Coloca en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Coloca en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Coloca en `ComfyUI/models/vae/`

## Turbo LoRA: minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16

Coloca en `ComfyUI/models/loras/`. Se usa cuando `turbo_mode` está activado.

### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   ├── 📂 loras/
    │   │   └── minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors
    │   ├── 📂 vae/
    │   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
    │   │   └── minimax_h3_audio_vae_fp32.safetensors
    │   └── 📂 embeddings/
    │       └── minimaxh3_art_is_explosion.safetensors
    

### 

​

Consejos para el prompt

  1. **Fotogramas clave** : `first_frame` / `last_frame` opcionales; el movimiento se genera entre ellos
  2. **Prompt** : planos, movimiento y audio en un solo bloque
  3. **Resolución / duración** : las mismas reglas que en T2V (objetivo nativo **1344×768** , cuadrícula **17k+5**)
  4. **Turbo** : `turbo_mode` usa `turbo_steps` (valor predeterminado **8**) y `turbo_model_strength` (valor predeterminado **1.0**) en lugar de 20 pasos

`first_frame` se redimensiona al lienzo sin conservar su relación de aspecto, así que una imagen con otra relación de aspecto sale estirada. `last_frame`, en cambio, se recorta desde el centro. La plantilla de I2V se abre en **1:1** y **0.4** MP (**640×640**), así que ajusta la relación de aspecto a tu imagen y sube los megapíxeles para el render final. Guía base oficial: [guía de prompts](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide).

## 

​

MiniMax H3 Referencia a Video (R2V)

Fija el personaje, el estilo, el movimiento, la cámara o la voz a partir de imágenes, videos y audio de referencia.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax H3 R2V” en la Biblioteca de plantillas

## Imagen de referencia: red_superboy_on_city_roof.png

Referencia de personaje para el flujo de trabajo, o usa tus propias imágenes.

## Imagen de referencia: mecha_dragon_lightning.png

Referencia de estilo y de sujeto para el flujo de trabajo, o usa tus propias imágenes.

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_ref2va_pruned_int8_convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Colócalo en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Colócalo en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Colócalo en `ComfyUI/models/vae/`

## LoRA: minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16

Requerido por el escaneo de modelos del flujo de trabajo; habilita el modo turbo opcional con Lightning LoRA. Colócalo en `ComfyUI/models/loras/`

### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_ref2va_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   ├── 📂 vae/
    │   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
    │   │   └── minimax_h3_audio_vae_fp32.safetensors
    │   ├── 📂 loras/
    │   │   └── minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors
    │   └── 📂 embeddings/
    │       └── minimaxh3_art_is_explosion.safetensors
    

### 

​

Consejos para el prompt

  1. **Etiquetas** : Haz referencia a las entradas como `<Picture 1>`, `<Video 1>`, `<Audio 1>` (`ref_image_0` → `<Picture 1>`). Orden de los nodos: primero imágenes, luego videos y al final audio
  2. **Asigna roles** : Indica qué referencia controla la identidad, el estilo, el movimiento, la cámara o la voz
  3. **Límites** : Hasta **9** imágenes, **3** videos y **3** clips de audio independientes
  4. **FPS del video** : El video de referencia se lee a **24fps** sin metadatos. Convierte otras frecuencias de fotogramas a 24fps antes de cargarlo
  5. **Sonido del video** : La imagen y la pista de sonido son referencias separadas. Conecta `ref_video_audio_N` para que coincida con `ref_video_N`, o el audio del archivo no se usará como `<Audio N>`
  6. **Numeración del audio** : Las pistas de sonido del video reciben `<Audio N>` primero (según el orden de los videos) y luego los clips independientes. Los índices de video e imagen son independientes
  7. **Conexión del VAE** : La pista de sonido del video necesita `vae` \+ `audio_vae`; el audio independiente solo necesita `audio_vae`
  8. **Roles del audio** : por ejemplo, `use <Audio 1> exactly as it is` frente a `follow the timbre of <Audio 2>`
  9. **Voz** : El audio aporta timbre, no palabras. Especifica la interpretación; usa una referencia de audio por hablante cuando la asignación deba ser exacta
  10. **`ref_image_size`** : El valor predeterminado es **`match`** (ajustar al lienzo). **`max`** mantiene 2048px en el lado corto y es mucho más lento; no escala archivos pequeños (redondea los lados a 32). Escala previamente a 2048 en el lado corto cuando sea necesario
  11. **Pesos** : R2V usa el modelo **`ref2va`** , no el **`fl2va`** de T2V/I2V
  12. **Turbo** : LoRA Lightning opcional de **4** pasos (más rápido, con referencias y audio más débiles). Prefiere **20–25** pasos cuando las referencias deban mantenerse
  13. **LoRA de estilo** : Compiten con las referencias; usa una fuerza baja (~**0.5**) con el scheduler base cuando importe la fidelidad

Guía oficial de referencias: [guía de prompt](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide).

## 

​

Flujos de trabajo avanzados con los nodos nativos

Requiere una compilación reciente de ComfyUI para las funciones que se describen a continuación.

### 

​

Anclar guías en cualquier frame (#15439)

[`MiniMaxH3AddGuide`](https://github.com/Comfy-Org/ComfyUI/pull/15439) ancla una guía en cualquier `frame_idx` (negativo = desde el final), no solo en el primer o último frame. Conecta `positive` y el latente de un nodo H3 en `MiniMaxH3AddGuide`. Entradas:

  * **image** : Imagen fija o clip (los lotes de varios frames se recortan a longitudes válidas de **17k+5** ; con <5 frames se usa solo la primera imagen)
  * **audio** : Pista de audio en el mismo índice de frame, recortada a la duración restante
  * **frame_idx** : Posición de anclaje

Conecta `vae` para guías de imagen y `audio_vae` para audio. Encadena nodos para varios anclajes. Ejemplo: los primeros **22** frames de un clip en el frame **0** continúan ambos flujos; una imagen fija en el frame **60** fuerza la toma a pasar por esa pose. Esto es acondicionamiento, no video a video: el muestreo sigue partiendo del latente vacío del flujo de trabajo. `denoise` no escala la fuerza de la guía como en V2V. Para cambiar el estilo de un clip completo, usa R2V; para editar regiones, usa las máscaras de [Fun ControlNet Union](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-fun-controlnet). Consulta la plantilla [Multiframe Reference](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-multiframe).

### 

​

Relleno inteligente y extensión con máscaras de ruido latente (#15375)

Las [máscaras de ruido por token](https://github.com/Comfy-Org/ComfyUI/pull/15375) en los latentes de video y audio te permiten regenerar parte de un clip. Conecta una máscara a `denoise_mask` del sampler: **0** = mantener, **1** = regenerar. Las máscaras de video se ajustan a la cuadrícula de parches latentes de 2×2; las de audio, a frames latentes completos. Úsalas para relleno inteligente, eliminación o extensión mientras mantienes el resto estable.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/minimax/minimax-h3-native.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/minimax/minimax-h3-native)

[FastVideo FastH3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-fastvideo)[Referencia multifotograma](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-multiframe)
