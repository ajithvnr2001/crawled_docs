---
url: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5/
title: LTX-2.5 en ComfyUI: flujos de video, audio y multishot - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-27T13:04:12.163928+00:00
---

# LTX-2.5 en ComfyUI: flujos de video, audio y multishot - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5/

## En esta página

Volver arriba

  * Características clave
  * Primeros pasos
  * Flujos de trabajo nativos de ComfyUI
    * LTX-2.5 Texto a video (T2V)
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para el prompt
    * LTX-2.5 de imagen a video (I2V)
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para escribir prompts
    * LTX-2.5 FLF2V
    * Descargas de modelos
    * Almacenamiento de modelos
    * Consejos para el prompt
  * LTX-2.5 DFR: Imagen a video
  * Recursos



LTX

# LTX-2.5 en ComfyUI: flujos de video, audio y multishot

Copiar páginaCopiar página

El modelo de video open source de Lightricks en ComfyUI: texto a video, imagen a video, primer-último fotograma, DFR, multishot, audio sincronizado y 4K HDR.

Copiar páginaCopiar página

[LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) es el modelo abierto de video y de mundo de Lightricks, con soporte nativo en ComfyUI. Se basa en LTX-2.3 con un pipeline Diffusion Fidelity Rendering que asigna el cómputo de renderizado según la complejidad de la escena. El modelo conserva la generación sincronizada de audio y video de LTX-2.3 y añade multishot nativo: una sola generación produce varias tomas conectadas que mantienen el personaje, el entorno, la iluminación y la voz a través de los cortes. LTX-2.5 incluye un codificador de texto Gemma 4 12B personalizado que retiene múltiples sujetos, acciones, iluminación y dirección de cámara en prompts complejos, además de un mejorador de prompts opcional que expande prompts cortos en instrucciones detalladas. La duración automática predice la longitud del clip a partir de la acción descrita antes de que comience la difusión. El modelo destilado ofrece una generación más rápida, y la salida admite 4K HDR nativo a hasta 50 FPS con un flujo de trabajo RAW para pipelines de postproducción profesionales. ComfyUI incluye cuatro flujos de trabajo nativos para LTX-2.5:

  * **Text-to-Video** (T2V): Genera videos a partir de prompts de texto
  * **Image-to-Video** (I2V): Genera videos a partir de una imagen de entrada
  * **FLF2V** : Interpola entre una imagen de primer fotograma y otra de último fotograma
  * **DFR** : Genera un video con audio mediante el pipeline Diffusion Fidelity Rendering, a partir de una imagen o de texto



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

Características clave

  * **Diffusion Fidelity Rendering** : generación que prioriza los fotogramas clave y construye cada escena sobre una cuadrícula de fotogramas clave de alta fidelidad
  * **Diffusion Video Decoder** : rostros más nítidos, texto legible y menos arrastres en movimiento rápido
  * **Multishot nativo** : una sola generación produce varias tomas conectadas que mantienen el personaje, el entorno, la iluminación, la voz y el estilo entre cortes
  * **Codificador de texto Gemma 4 12B** : conserva varios sujetos, acciones, iluminación, detalle y dirección de cámara en prompts complejos
  * **Mejorador de prompt** _(opcional)_ : un modelo ligero que amplía prompts cortos y los convierte en instrucciones detalladas
  * **Duración automática** : predice la longitud correcta del clip a partir de la acción descrita antes de generar
  * **4K HDR nativo** : salida HDR de alta resolución pensada para el acabado profesional, con audio y video sincronizados a hasta 50 FPS



## 

​

Primeros pasos

LTX-2.5 es compatible de forma nativa con ComfyUI. Para empezar:

  1. Actualiza ComfyUI a la última versión
  2. Ve a **Biblioteca de plantillas** > **Video** > elige cualquier flujo de trabajo de LTX-2.5
  3. Solicita acceso al repositorio del modelo en Hugging Face (consulta abajo) y luego sigue la ventana emergente para descargar los modelos y ejecutar el flujo de trabajo



Los archivos del modelo LTX-2.5 están alojados en los repositorios restringidos [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) y [Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler) en Hugging Face. Abre las páginas de los repositorios, acepta la licencia del modelo y espera a que se apruebe tu solicitud de acceso antes de descargar los modelos. Las descargas de modelos fallarán si no tienes acceso.

## 

​

Flujos de trabajo nativos de ComfyUI

### 

​

LTX-2.5 Texto a video (T2V)

Genera videos a partir de prompts de texto con ampliación espacial opcional para mejorar la resolución.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 T2V” en la Biblioteca de plantillas

#### 

​

Descargas de modelos

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Coloca el archivo en `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Coloca el archivo en `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_int8_convrot

Opcional: solo se necesita cuando el mejorador de prompt está habilitado. Coloca el archivo en `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Coloca el archivo en `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Coloca el archivo en `ComfyUI/models/vae/`

## Upscaler: ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0

Coloca el archivo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   ├── 📂 vae/
    │   │   ├── ltx-2.5-video-vae-bf16.safetensors
    │   │   └── ltx-2.5-audio-vae-bf16.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
    

#### 

​

Consejos para el prompt

  1. **Describe toda la escena** : incluye el tipo de plano, la escena, la acción, los personajes y el movimiento de cámara en un solo párrafo fluido
  2. **Audio** : describe los sonidos y el diálogo que necesita la escena; el modelo genera audio sincronizado junto con el video
  3. **Usa el mejorador de prompt (opcional)** : el flujo de trabajo lo mantiene desactivado de forma predeterminada. Habilita `prompt_enhance` en el nodo LTX-2.5 para expandir prompts cortos en instrucciones cinematográficas detalladas. Requiere el modelo mejorador aparte (~5 GB) y añade entre 1 y 2 minutos al tiempo de generación



* * *

### 

​

LTX-2.5 de imagen a video (I2V)

Genera videos a partir de una imagen de entrada. El modelo anima la escena desde el primer fotograma proporcionado.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 I2V” en la Biblioteca de plantillas

## Imagen de entrada: neon_cyborg_portrait.png

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

#### 

​

Descargas de modelos

El flujo de trabajo I2V usa el mismo conjunto de modelos que texto a video.

## Modelo de difusión: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## Codificador de texto: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Colócalo en `ComfyUI/models/text_encoders/`

## Codificador de texto: gemma4_e2b_it_int8_convrot

Opcional: solo se necesita cuando el mejorador de prompt está habilitado. Colócalo en `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Colócalo en `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Colócalo en `ComfyUI/models/vae/`

## Upscaler: ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0

Colócalo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   ├── 📂 vae/
    │   │   ├── ltx-2.5-video-vae-bf16.safetensors
    │   │   └── ltx-2.5-audio-vae-bf16.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
    

#### 

​

Consejos para escribir prompts

  1. **Describe lo que ocurre a continuación** : escribe el movimiento, el movimiento de cámara y los sonidos que se derivan de la imagen de entrada; no vuelvas a describir lo que ya es visible
  2. **Ancla el primer fotograma** : usa expresiones como “Usa la imagen de inicio proporcionada como primer fotograma” cuando escribas una continuación
  3. **Audio** : describe el diálogo y los sonidos de la escena; el modelo genera audio sincronizado



* * *

### 

​

LTX-2.5 FLF2V

Genera un video entre una imagen de primer fotograma y una de último fotograma, combinando ambas en una sola secuencia animada.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.5 FLF2V” en la Biblioteca de plantillas

## First Frame: robot_hand_back.png

Primer fotograma del video.

## Last Frame: robot_hand_energy.png

Último fotograma del video.

#### 

​

Descargas de modelos

El flujo de trabajo FLF2V usa el mismo conjunto de modelos que texto a video, sin el upscaler espacial.

## Diffusion Model: ltx-2.5-22b-distilled-transformer-comfy-int8-convrot

Colócalo en `ComfyUI/models/diffusion_models/`

## Text Encoder: gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot

Colócalo en `ComfyUI/models/text_encoders/`

## Text Encoder: gemma4_e2b_it_int8_convrot

Opcional: solo se necesita cuando el mejorador de prompt está activado. Colócalo en `ComfyUI/models/text_encoders/`

## VAE: ltx-2.5-video-vae-bf16

Colócalo en `ComfyUI/models/vae/`

## VAE: ltx-2.5-audio-vae-bf16

Colócalo en `ComfyUI/models/vae/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
    │   │   └── gemma4_e2b_it_int8_convrot.safetensors (optional)
    │   └── 📂 vae/
    │       ├── ltx-2.5-video-vae-bf16.safetensors
    │       └── ltx-2.5-audio-vae-bf16.safetensors
    

#### 

​

Consejos para el prompt

  1. **Describe la transición** : escribe lo que ocurre entre los dos fotogramas, incluido el movimiento de cámara y el audio
  2. **Mantén los fotogramas alineados** : usa imágenes con la misma relación de aspecto para lograr una interpolación suave
  3. **Audio** : describe el diálogo y los sonidos de la escena; el modelo genera audio sincronizado



* * *

## 

​

LTX-2.5 DFR: Imagen a video

DFR es la receta de calidad de producción: un transformer destilado combinado con un IC-LoRA de detallado, con keyframes generados dentro del clip y reutilizados como guías por las pasadas posteriores. Se ejecuta a partir de una imagen, o desde texto con `Switch to T2V`. Tiene su propia página: [LTX-2.5 DFR: Imagen a video](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5-dfr).

## 

​

Recursos

  * [Modelo en Hugging Face](https://huggingface.co/Lightricks/LTX-2.5)
  * [Página del modelo LTX](https://ltx.io/model/ltx-2-5)
  * [Repositorio en GitHub](https://github.com/Lightricks/LTX-Video)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/ltx/ltx-2-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/ltx/ltx-2-5)

[LTX-2.5 DFR](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5-dfr)[LTX-2.3](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-3)
