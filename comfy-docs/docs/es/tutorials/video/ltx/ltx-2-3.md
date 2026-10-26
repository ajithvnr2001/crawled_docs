---
url: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-3/
title: LTX-2.3: ejemplos de flujos de trabajo en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:59.379831+00:00
---

# LTX-2.3: ejemplos de flujos de trabajo en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-3/

## En esta página

Volver arriba

  * Características clave
  * Primeros pasos
  * Flujos de trabajo nativos de ComfyUI
    * LTX-2.3 Texto a video (T2V)
    * LTX-2.3 Texto a video
    * Descarga de modelos
    * Almacenamiento de modelos
    * Consejos para escribir prompts
    * LTX-2.3 Imagen a video (I2V)
    * LTX-2.3 Imagen a video
    * Descarga de modelos
    * Almacenamiento de modelos
    * LTX-2.3 FLF2V
    * LTX-2.3 Primer y último fotograma a video
    * Descarga de modelos
    * Almacenamiento de modelos
    * LTX-2.3 Imagen y audio a video (IA2V)
    * LTX-2.3 Imagen y audio a video
    * Descarga de modelos
    * Almacenamiento de modelos
    * LTX-2.3 IC-LoRA Union Control
    * Descarga de modelos
    * Almacenamiento de modelos
    * Edición de video con IC-LoRA
    * Eliminar subtítulos de un video
    * Eliminar un objeto de un video
    * Restaurar material de archivo
    * Outpainting de video
    * Googly Eyes
    * LTX-2.3 ID-LoRA
    * LTX-2.3 ID LoRA
    * Descarga de modelos
    * Almacenamiento de modelos
  * Consejos para escribir prompts
  * Recursos



LTX

# LTX-2.3: ejemplos de flujos de trabajo en ComfyUI

Copiar páginaCopiar página

Usa LTX-2.3 en ComfyUI con flujos de trabajo nativos para texto a video, imagen a video, FLF2V, video con audio, control IC-LoRA y personalización ID-LoRA.

Copiar páginaCopiar página

[LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) es la última evolución del modelo de generación de audio y video de código abierto de Lightricks, ahora compatible de forma nativa con ComfyUI. Sobre la base de LTX-2, esta versión ofrece mejoras importantes de calidad en detalles finos, video de retratos, calidad de audio, consistencia de imagen a video, comprensión de prompts y renderizado de texto. ComfyUI incluye seis flujos de trabajo nativos para LTX-2.3, cada uno diseñado para un modo de generación específico:

  * **Texto a video** (T2V): Genera videos a partir de prompts de texto
  * **Imagen a video** (I2V): Genera videos a partir de una imagen de entrada
  * **FLF2V** : Interpola entre una imagen inicial y una imagen final
  * **Imagen y audio a video** (IA2V): Genera videos con sincronización labial a partir de una imagen y audio
  * **IC-LoRA Union Control** : Controla la generación de video con orientación de profundidad, pose o bordes
  * **ID-LoRA** : Genera videos personalizados con audio sincronizado a partir de una imagen de referencia y un clip de audio



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

  * **Detalles más finos** : nuevo espacio latente y VAE actualizado para texturas más nítidas, bordes más limpios y visuales más precisos
  * **Soporte para formato vertical 9:16** : calidad muy mejorada en videos verticales
  * **Mejor audio** : sonido más limpio con menos ruido y diálogos mejorados
  * **Imagen a video mejorado** : movimiento más consistente y menos fallos
  * **Comprensión de prompts más inteligente** : codificador de texto mejorado para una interpretación más precisa
  * **Soporte nativo en ComfyUI** : todos los flujos de trabajo son integrados, no se requieren Nodos personalizados



## 

​

Primeros pasos

LTX-2.3 es compatible de forma nativa con ComfyUI. Para empezar:

  1. Actualiza ComfyUI a la última versión
  2. Ve a **Biblioteca de plantillas** > **Video** > elige cualquier flujo de trabajo de LTX-2.3
  3. Sigue la ventana emergente para descargar los modelos y ejecutar el flujo de trabajo



## 

​

Flujos de trabajo nativos de ComfyUI

### 

​

LTX-2.3 Texto a video (T2V)

Genera videos a partir de prompts de texto con mejor comprensión de prompts y mejor renderizado de texto.

### 

​

LTX-2.3 Texto a video

Genera videos a partir de prompts de texto con mejor comprensión de prompts y mejor renderizado de texto. ![Vista previa del flujo de trabajo LTX-2.3 Text to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 T2V” en la Biblioteca de plantillas

#### 

​

Descarga de modelos

## Checkpoint: ltx-2.3-22b-dev-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Colócalo en `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Colócalo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

#### 

​

Consejos para escribir prompts

  1. **Acciones principales** : Describe los eventos y las acciones tal como ocurren a lo largo del tiempo
  2. **Detalles visuales** : Describe todos los detalles visuales que quieres que aparezcan en el video
  3. **Audio** : Describe los sonidos y el diálogo que necesita la escena



* * *

### 

​

LTX-2.3 Imagen a video (I2V)

Genera videos a partir de una imagen de entrada con un movimiento más consistente y animaciones más fluidas.

### 

​

LTX-2.3 Imagen a video

Genera videos a partir de una imagen de entrada con una consistencia de movimiento mejorada. ![Vista previa del flujo de trabajo LTX-2.3 Image to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 I2V” en la Biblioteca de plantillas

## Imagen de entrada: egyptian_queen.png

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

#### 

​

Descarga de modelos

El flujo de trabajo I2V usa el mismo conjunto de modelos que el de texto a video.

## Checkpoint: ltx-2.3-22b-dev-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Colócalo en `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Colócalo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

* * *

### 

​

LTX-2.3 FLF2V

Interpola entre una imagen inicial y una imagen final para generar una transición de video fluida.

### 

​

LTX-2.3 Primer y último fotograma a video

Interpola entre una imagen inicial y una final. ![Vista previa del flujo de trabajo LTX-2.3 First-Last Frame to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_flf2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 FLF2V” en la Biblioteca de plantillas

## Imagen inicial: high_view_classic_car.png

Primer fotograma del video.

## Imagen final: low_view_classic_car.png

Último fotograma del video.

#### 

​

Descarga de modelos

El flujo de trabajo FLF2V usa el checkpoint distilled en lugar del checkpoint dev.

## Checkpoint: ltx-2.3-22b-distilled-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-distilled-fp8.safetensors
    │   └── 📂 text_encoders/
    │       └── gemma_3_12B_it_fp4_mixed.safetensors
    

* * *

### 

​

LTX-2.3 Imagen y audio a video (IA2V)

Sube una imagen y un archivo de audio para generar un video de alta calidad con movimientos labiales sincronizados.

### 

​

LTX-2.3 Imagen y audio a video

Genera videos con sincronización labial a partir de una imagen y audio. ![Vista previa del flujo de trabajo LTX-2.3 Image and Audio to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ia2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 IA2V” en la Biblioteca de plantillas

## Imagen de entrada: cactus_man.png

Imagen de referencia para el personaje que habla.

## Audio de referencia: ltx_23_audio.mp3

Pista de audio para la sincronización labial.

#### 

​

Descarga de modelos

El flujo de trabajo IA2V usa el mismo conjunto de modelos que el de texto a video.

## Checkpoint: ltx-2.3-22b-dev-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Colócalo en `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Colócalo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

* * *

### 

​

LTX-2.3 IC-LoRA Union Control

Genera videos con LTX-2.3 e IC-LoRA usando entradas de control alineadas como profundidad, pose o bordes. IC-LoRA es un LoRA in-context entrenado sobre LTX-2.3 que aplica la guía estructural de un video de referencia. Acepta señales de control de varios preprocesadores, incluidos mapas de profundidad, bordes de Canny y esqueletos de pose. Este flujo de trabajo usa un Subgraph para el procesamiento modular. ![Vista previa de LTX-2.3 IC-LoRA](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ic_lora-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 IC-LoRA” en la Biblioteca de plantillas

## Aprende sobre Subgraph

Este flujo de trabajo usa un nodo Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y ampliar el flujo de trabajo.

**Materiales de entrada**

## Video de control: stone_ruins.mp4

Video guía del que se extrae la señal de control.

## Imagen de referencia: the_forgotten_gate.png

Imagen de referencia para el estilo y el contenido.

#### 

​

Descarga de modelos

## Checkpoint: ltx-2.3-22b-distilled-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## LoRA: IC-LoRA Union Control

Colócalo en `ComfyUI/models/loras/`

## LoRA: gemma abliterated

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

## Geometry: MoGe Normal

Colócalo en `ComfyUI/models/geometry_estimation/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-distilled-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors
    │   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 geometry_estimation/
    │       └── moge_2_vitl_normal_fp16.safetensors
    

* * *

### 

​

Edición de video con IC-LoRA

Los pesos IC-LoRA no se limitan al control de la generación. La Biblioteca de plantillas incluye flujos de trabajo IC-LoRA de LTX-2.3 ya preparados para editar material existente, y cada uno se ejecuta en Comfy Cloud o de forma local en ComfyUI. Los checkpoints IC-LoRA de la comunidad entrenados sobre LTX-2.3 (por ejemplo, la familia [LTX2.3-ICEdit-Insight](https://huggingface.co/joyfox/LTX2.3-ICEdit-Insight)) también son compatibles con el modelo nativo LTX-2.3.

#### 

​

Eliminar subtítulos de un video

Elimina subtítulos, rótulos, marcas de agua u otras superposiciones de texto de un video: ![Vista previa del flujo de trabajo de eliminación de subtítulos de LTX-2.3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_remove_subtitles_from_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Remove Subtitles” en la Biblioteca de plantillas

#### 

​

Eliminar un objeto de un video

Elimina un objeto concreto del primer plano de un video describiéndolo en el prompt: ![Vista previa del flujo de trabajo de eliminación de objetos de LTX-2.3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_obscura_remova_lora_remove_object_from_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Remove Object” en la Biblioteca de plantillas

#### 

​

Restaurar material de archivo

Restaura material de archivo antiguo o degradado: ![Vista previa del flujo de trabajo de restauración de material de archivo de LTX-2.3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_restore_archival_footage-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Restore Archival” en la Biblioteca de plantillas

#### 

​

Outpainting de video

Amplía un video en cualquier dirección con el IC-LoRA Video Outpainting de LTX-2.3: ![Vista previa del flujo de trabajo de outpainting de video de LTX-2.3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_video_outpainting-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Video Outpainting” en la Biblioteca de plantillas

#### 

​

Googly Eyes

Aplica el LoRA Googlyeyes de LTX-2.3 a un video de entrada para poner ojos saltones a todas las personas del fotograma: ![Vista previa del flujo de trabajo Googly Eyes de LTX-2.3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_googly_eyes-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Googly Eyes” en la Biblioteca de plantillas

Para los IC-LoRA de la comunidad, coloca el LoRA de edición en `ComfyUI/models/loras/` y cárgalo con un cargador de LoRA junto al checkpoint de LTX-2.3; después ejecuta el flujo de trabajo con tu video como entrada y un prompt como:
    
    
    Remove subtitles, captions, and related text occlusions from the video, restoring a clean and natural underlying image.
    

* * *

### 

​

LTX-2.3 ID-LoRA

Genera videos personalizados con audio sincronizado a partir de un prompt de texto, una imagen de referencia y un clip de audio corto. Usa ID-LoRA para adaptar la apariencia y la voz de una persona en un solo modelo generativo.

### 

​

LTX-2.3 ID LoRA

Genera videos personalizados con audio sincronizado a partir de una imagen de referencia y un clip de audio. ![Vista previa del flujo de trabajo LTX-2.3 ID LoRA](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_id_lora-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTX-2.3 ID-LoRA” en la Biblioteca de plantillas

## Imagen de referencia: vintage_thinker.png

Imagen de referencia para la apariencia del personaje.

## Audio de referencia: ltx23_reference_audio.mp3

Clip de audio para la clonación de voz y la sincronización labial.

#### 

​

Descarga de modelos

## Checkpoint: ltx-2.3-22b-dev-fp8

Colócalo en `ComfyUI/models/checkpoints/`

## LoRA: distilled 1.1

Colócalo en `ComfyUI/models/loras/`

## LoRA: ID-LoRA TalkVid

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: gemma 12B

Colócalo en `ComfyUI/models/text_encoders/`

## Upscaler: spatial x2

Colócalo en `ComfyUI/models/latent_upscale_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── ltx-2.3-22b-dev-fp8.safetensors
    │   ├── 📂 loras/
    │   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
    │   │   └── ltx-2.3-id-lora-talkvid-3k.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── gemma_3_12B_it_fp4_mixed.safetensors
    │   └── 📂 latent_upscale_models/
    │       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
    

## 

​

Consejos para escribir prompts

Cuando escribas prompts para LTX-2.3, céntrate en descripciones detalladas y cronológicas de acciones y escenas:

  1. **Acciones principales** : Describe los eventos y las acciones tal como ocurren a lo largo del tiempo
  2. **Detalles visuales** : Describe todos los detalles visuales que quieres que aparezcan en el video
  3. **Audio** : Describe los sonidos y el diálogo que necesita la escena



## 

​

Recursos

  * [Modelo de Hugging Face](https://huggingface.co/Lightricks/LTX-2.3)
  * [Repositorio de GitHub](https://github.com/Lightricks/LTX-2)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)
  * [Modelo IC-LoRA](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/ltx/ltx-2-3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/ltx/ltx-2-3)

[LTX-2.5](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-5)[LTX-2.0](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2)
