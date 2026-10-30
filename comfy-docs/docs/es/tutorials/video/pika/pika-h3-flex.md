---
url: https://docs.comfy.org/es/tutorials/video/pika/pika-h3-flex/
title: Flujos de trabajo de Pika H3 Flex en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-30T13:55:13.703296+00:00
---

# Flujos de trabajo de Pika H3 Flex en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/pika/pika-h3-flex/

## En esta página

Volver arriba

  * Características clave
  * Elegir un flujo de trabajo de plantilla
  * Texto a video (T2V)
    * Descargas de modelos
  * Referencia a video (Ref2VA)
    * Descargas de modelos
  * Primer y último fotograma (FL2VA)
    * Descargas de modelos
  * Dónde van los modelos
  * Cómo redactar prompts
  * Preguntas frecuentes



Pika

# Flujos de trabajo de Pika H3 Flex en ComfyUI

Copiar páginaCopiar página

Ejecuta Pika H3 Flex en ComfyUI: flujos de trabajo en seis pasos de texto a video, referencia a video y primer y último fotograma con audio estéreo.

Copiar páginaCopiar página

![Pika H3 Flex](https://mintcdn.com/dripart/icfaG51neLouz0RW/images/pika/pika-h3-flex-logo-black.png?fit=max&auto=format&n=icfaG51neLouz0RW&q=85&s=728a44c1e60884f629fd3785193d68b2) ![Pika H3 Flex](https://mintcdn.com/dripart/icfaG51neLouz0RW/images/pika/pika-h3-flex-logo-white.png?fit=max&auto=format&n=icfaG51neLouz0RW&q=85&s=3816cb5dde6a980b9edf9607ffc19d10) [Pika H3 Flex](https://github.com/Pika-Labs/Pika-H3-Flex) es una versión con entrenamiento posterior de [MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3). Pika realizó un ajuste fino de H3 sobre un corpus multitarea curado de video, audio y ejemplos de referencia, destiló el generador de 50 pasos hasta **seis pasos** y luego lo refinó con retroalimentación de recompensa y optimización de preferencias. Se distribuye como dos adaptadores LoRA que se ejecutan sobre la base MiniMax H3 que ya tienes en ComfyUI, así que no interviene ninguna arquitectura de modelo nueva.

Los adaptadores se distribuyen bajo el [MiniMax H3 Community License Agreement](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE). Revisa sus términos, incluidas las condiciones territoriales y de uso comercial, antes de usar las salidas con fines comerciales.

## 

​

Características clave

  * **Seis pasos, mismo territorio** : un clip de 5 segundos en 1344x768 se completa en aproximadamente un minuto en una sola tarjeta, en lugar de los 20 a 50 pasos que necesita una ejecución de H3 sin destilar
  * **Audio estéreo nativo** : el diálogo, los efectos de sonido y la música se generan en la misma pasada que la imagen
  * **Control basado en referencias** : hasta 12 referencias por generación (9 imágenes, 3 videos y 3 clips de audio), incluidos el video de referencia de movimiento y las muestras de voz
  * **Dirección de múltiples tomas** : describe cortes secos, coreografía de cámara y diálogo dentro de un solo prompt
  * **Pesos abiertos** : los dos adaptadores son públicos y se cargan mediante el nodo estándar `LoraLoaderModelOnly`



## 

​

Elegir un flujo de trabajo de plantilla

Tres flujos de trabajo de plantilla `video_pika_h3_flex_*` están disponibles en **Template Library** > **Video**. Los tres cargan la base H3 más un adaptador, y los tres ejecutan el programa de muestreo de seis pasos de Pika.

## Texto a video

Solo prompt, sin entrada de imagen. ComfyUI **0.43.2+**.

## Referencia a video

Dos o más referencias de imagen determinan la identidad, los accesorios y la escena. ComfyUI **0.30.0+**.

## Primer y último fotograma

Dos fotogramas anclan el inicio y el final de la toma. ComfyUI **0.30.0+**.

Las tres plantillas incluyen el programa de seis pasos publicado por Pika: `lcm` con `ManualSigmas` y CFG 1.0 mediante `BasicGuider`. Mantén la lista de sigmas y la fuerza del adaptador en 1.0, y no apiles un LoRA turbo o Lightning encima, porque el adaptador ya está destilado a seis pasos y un segundo LoRA de aceleración rompe la salida.

## 

​

Texto a video (T2V)

Genera un video con audio sincronizado a partir de un prompt.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pika H3 Flex: Text to Video” en la Biblioteca de plantillas

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_fl2va_pruned_int8_convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_fl2va_v1_bf16

Colócalo en `ComfyUI/models/loras/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Colócalo en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Colócalo en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Colócalo en `ComfyUI/models/vae/`

## 

​

Referencia a video (Ref2VA)

Genera un video con audio sincronizado a partir de imágenes de referencia. Las referencias aportan la identidad, el vestuario, la forma del objeto y el entorno, mientras que el prompt aporta la acción y el plano.

## Run on Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pika H3 Flex: Reference to Video” en la Biblioteca de plantillas

## Imagen de entrada: ref_pilot_profile.png

Referencia 1 en la plantilla. Reemplázala por tu propio sujeto.

## Imagen de entrada: ref_subject_station.png

Referencia 2 en la plantilla. Reemplázala por un segundo sujeto o una escena.

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_ref2va_pruned_int8_convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_ref2va_v1_bf16

Colócalo en `ComfyUI/models/loras/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Colócalo en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Colócalo en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Colócalo en `ComfyUI/models/vae/`

## 

​

Primer y último fotograma (FL2VA)

Anima entre dos fotogramas fijos. La primera imagen abre la toma, la segunda la cierra, y el prompt describe el recorrido entre ambas.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Pika H3 Flex: FL2VA” en la Biblioteca de plantillas

## Imagen de entrada: ref_popart_woman.png

Primer fotograma de la toma.

## Imagen de entrada: lastP_spin_jump_hole.png

Último fotograma de la toma.

### 

​

Descargas de modelos

## Modelo de difusión: minimax_h3_fl2va_pruned_int8_convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## LoRA: pika_h3_flex_fl2va_v1_bf16

Colócalo en `ComfyUI/models/loras/`

## Codificador de texto: qwen3vl_32b_minimax_h3_nvfp4_awq

Colócalo en `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_video_vae_int8_convrot

Colócalo en `ComfyUI/models/vae/`

## VAE: minimax_h3_audio_vae_fp32

Colócalo en `ComfyUI/models/vae/`

## 

​

Dónde van los modelos

Las tres plantillas esperan esta estructura. Los archivos base de H3 se comparten con las plantillas existentes de MiniMax H3; los únicos archivos nuevos son los dos adaptadores.
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   ├── minimax_h3_fl2va_pruned_int8_convrot.safetensors
    │   │   └── minimax_h3_ref2va_pruned_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   ├── pika_h3_flex_fl2va_v1_bf16.safetensors
    │   │   └── pika_h3_flex_ref2va_v1_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
    │   └── 📂 vae/
    │       ├── minimax_h3_video_vae_int8_convrot.safetensors
    │       └── minimax_h3_audio_vae_fp32.safetensors
    

## 

​

Cómo redactar prompts

Los prompts siguen la misma estructura que el resto de H3. Para T2V y FL2VA, describe el estilo, luego cada plano con su movimiento de cámara y, por último, los dos campos de sonido. Para Ref2VA, usa el formulario de referencia completa con `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape` y `non_diegetic_music`, y etiqueta cada referencia como `<Subject 1>`, `<Picture 1>`, `<Video 1>` o `<Audio 1>`. Consulta [Prompt guide](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide) para ver la sintaxis completa, incluidos el vocabulario de cámara y las etiquetas de diálogo. Notas prácticas de las pruebas con los adapters publicados:

  * **La amplitud de cámara es orientativa.** Describe el movimiento como parte de la frase del plano y dale siempre un punto de detención. Los grados explícitos y las marcas de tiempo de corte pueden desviarse entre 0.2 y 0.3 segundos, o ir en la dirección opuesta.
  * **Describe el encuadre como contenido.** Un “plano general” por sí solo tiende a renderizarse como un plano medio; decir que el sujeto es pequeño dentro de una habitación grande y vacía mantiene mejor el encuadre general.
  * **Las restricciones de contacto fino no son confiables.** Una mano que debería detenerse a unos centímetros de distancia suele hacer contacto, así que haz que el momento siga funcionando incluso si ocurre.
  * **El texto renderizado se mantiene.** Las etiquetas cortas en utilería y productos siguen siendo legibles a través de los movimientos de cámara.



## 

​

Preguntas frecuentes

¿Puedo usar estos adaptadores con las plantillas existentes de MiniMax H3?

Sí. Las [plantillas de MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3) usan `res_multistep` con `BasicScheduler`, que es la ruta de 20 pasos. Carga el adaptador de Pika en el nodo LoRA de la plantilla, cambia el sampler a `lcm` y reemplaza el programador por `ManualSigmas`.

¿Por qué seis pasos?

Pika destiló el generador H3 de 50 pasos con destilación por coincidencia de distribuciones y luego lo refinó con retroalimentación de recompensa. Seis pasos es la programación entrenada, así que aumentar el número de pasos no añade detalle, y reducir la lista de sigmas a menos de siete valores rompe la programación.

¿Cuántas referencias puedo conectar?

El adaptador Ref2VA acepta hasta 9 imágenes, 3 videos y 3 clips de audio independientes, 12 archivos en total. Las referencias de video y de audio deben durar de 2 a 15 segundos cada una, y la duración combinada de cada tipo se mantiene dentro de los 15 segundos.

¿De dónde vienen los adaptadores?

Pika los publica en [Pika-Labs/Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex), y Comfy republica los archivos listos para ComfyUI en [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3/tree/main/loras) con los mismos nombres de archivo. Los nodos de la plantilla apuntan al reempaquetado de Comfy.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/pika/pika-h3-flex.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/pika/pika-h3-flex)

[Guía de prompts](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide)[LTX-2.5 DFR](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5-dfr)
