---
url: https://docs.comfy.org/es/tutorials/image/minimax/minimax-h3-image/
title: MiniMax-H3-Image: texto a imagen de 16 MP y edici\u00f3n de im\u00e1genes en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-25T17:52:25.504454+00:00
---

# MiniMax-H3-Image: texto a imagen de 16 MP y edición de imágenes en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/minimax/minimax-h3-image/

## En esta página

Volver arriba

  * Características principales
  * Plantillas
    * MiniMax-H3-Image Texto a imagen
    * MiniMax-H3-Image Edición de imagen
    * MiniMax-H3-Image Intercambio de personaje
  * Descarga de modelos
  * Muestreo y tamaño del lienzo
  * Imágenes de referencia en la edición de imágenes
  * Expansor de prompt



MiniMax

# MiniMax-H3-Image: texto a imagen de 16 MP y edición de imágenes en ComfyUI

Copiar páginaCopiar página

Ejecuta MiniMax-H3-Image en ComfyUI: un checkpoint de pesos abiertos para texto a imagen y edición de imágenes a unos 16 MP, destilado a 6 pasos del sampler.

Copiar páginaCopiar página

**MiniMax-H3-Image** es el modelo de imagen de pesos abiertos de MiniMax, y un solo checkpoint cubre tanto texto a imagen como la edición de imágenes. El transformer de difusión tiene 33.1B parámetros en BF16, destilado a un sampler de 6 pasos sin CFG. La salida es nativa a unos 16 MP, así que una imagen de 4096 x 4096 se genera en una sola pasada en lugar de una cadena de upscale. **Enlaces relacionados**

  * [MiniMaxAI/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image): model card y pesos oficiales
  * [MiniMax-H3-Image (ModelScope)](https://modelscope.cn/models/minimax/MiniMax-H3-Image): espejo oficial para China continental
  * [MiniMax-AI/MiniMax-H3-Image (GitHub)](https://github.com/MiniMax-AI/MiniMax-H3-Image): ejemplos y skill oficiales
  * [Comfy-Org/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3-Image): modelo de difusión y VAE de imagen
  * [Comfy-Org/MiniMax-H3 (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3): text encoder Qwen3-VL-32B que usa este modelo
  * [MiniMaxAI/MiniMax-H3-Image-PE (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE): expansor de prompts oficial



## Características principales

  * **Texto a imagen y edición en un mismo checkpoint** : sin necesidad de cargar un modelo de edición aparte
  * **Muestreo de 6 pasos** : la orientación está fijada en 1, así que no hay pase CFG ni prompt negativo
  * **Unos 16 MP de forma nativa** : 4096 x 4096 hasta 6272 x 2688 sin un pase de upscale
  * **Varias referencias** : hasta 16 imágenes de entrada, a las que te refieres como `<Picture 1>` en adelante en el prompt
  * **Expansor de prompt opcional** : convierte una petición breve en el caption detallado que el modelo interpreta mejor
  * **Pesos abiertos** : control local completo en ComfyUI



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

## Plantillas

El modelo incluye tres flujos de trabajo de plantilla. Todos requieren ComfyUI **0.45.0+**. Las plantillas de texto a imagen y edición de imágenes necesitan el paquete de plantillas **0.11.104+** ; el intercambio de personaje necesita **0.11.115+**.

### MiniMax-H3-Image Texto a imagen

Genera una imagen a partir de un prompt de texto. La plantilla se abre a 16 MP (4096 x 4096 en 1:1), la resolución nativa del modelo. Baja `megapixels` en el Selector de resolución a unos 4 MP si tienes poca VRAM o quieres ejecuciones más rápidas. ![Salida de ejemplo de texto a imagen de MiniMax-H3-Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax-H3-Image: Text to Image” en Template Library

### MiniMax-H3-Image Edición de imagen

Edita una imagen describiendo el cambio. La plantilla carga la fuente como `<Picture 1>`, construye un caption que tiene en cuenta la referencia a partir de tu instrucción y termina con un nodo de comparación antes/después. ![Salida de ejemplo de edición de imagen de MiniMax-H3-Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_edit-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax-H3-Image: Image Edit” en Template Library

**Materiales de entrada** La plantilla incluye una imagen de origen, cargada como `<Picture 1>` en su nodo `LoadImage`.

## vintage_yellow_taxi.png

Imagen de origen que edita la plantilla

### MiniMax-H3-Image Intercambio de personaje

Sustituye a la persona de una foto por un personaje de una imagen de referencia. La plantilla lee la foto como `<Picture 1>` y el personaje como `<Picture 2>`, mantiene la pose, el encuadre y la iluminación de la toma, y traslada la cara, el vestuario y los materiales del personaje de referencia. Se ejecuta sobre el mismo checkpoint con un adaptador de intercambio de personaje a fuerza 1.0. ![Intercambio de personaje de MiniMax-H3-Image: foto de origen y resultado](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_character_swap-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “MiniMax-H3-Image: Character Swap” en la Biblioteca de plantillas

Se diferencia de las otras dos plantillas en dos cosas. La foto de origen se escala a 1 MP, 864 x 1152 con las imágenes de ejemplo, y ese tamaño pasa a ser el de salida. Tampoco tiene expansor de prompt: el adaptador se entrenó con instrucciones de edición breves, así que escribe tú la instrucción y nombra las referencias, por ejemplo “Sustituye a la persona de `<Picture 1>` por el personaje de `<Picture 2>`, mantén la escena, el encuadre y la pose del objetivo”. **Materiales de entrada** La plantilla incluye una foto de origen y un personaje de referencia.

## h3_char_swap_source.png

Foto que se edita, se lee como la primera imagen

## h3_char_swap_reference.png

Personaje que se traslada, se lee como la segunda imagen

## Descarga de modelos

Las plantillas de texto a imagen y edición de imágenes usan estos cuatro archivos, todos de repositorios espejo de Comfy-Org. La plantilla de intercambio de personaje no usa el expansor de prompt y necesita un archivo más, un adaptador publicado por su autor.

## Modelo de difusión: minimax_h3_image_pruned_int8_convrot.safetensors

DiT podado INT8, 21 GB. Colócalo en `ComfyUI/models/diffusion_models/`

## Codificador de texto: qwen3vl_32b_minimax_h3_int8_convrot.safetensors

Qwen3-VL-32B, INT8, 25.28 GB. Colócalo en `ComfyUI/models/text_encoders/`

## Expansor de prompt: qwen3.5_9b_w4a8_gptq.safetensors

Qwen3.5 9B W4A8, 7.34 GB. Colócalo en `ComfyUI/models/text_encoders/`. Solo texto a imagen y edición de imágenes

## VAE: minimax_h3_image_vae_fp16.safetensors

VAE de imagen, FP16, 1.17 GB. Colócalo en `ComfyUI/models/vae/`

## Adaptador de intercambio de personaje: h3_image_character_swap_v1.safetensors

LoRA rank 16, 155 MB, del repositorio original del adaptador. Colócalo en `ComfyUI/models/loras/`

**Ubicación de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── h3_image_character_swap_v1.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
    │   │   └── qwen3.5_9b_w4a8_gptq.safetensors
    │   └── 📂 vae/
    │       └── minimax_h3_image_vae_fp16.safetensors
    

El adaptador es [akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA), entrenado con 140 ediciones emparejadas y evaluado sobre el checkpoint INT8 anterior. Su uso sigue el Acuerdo de Licencia Comunitaria de MiniMax H3 Image.

## Muestreo y tamaño del lienzo

Todas las plantillas incluyen la programación destilada:

Ajuste| Valor  
---|---  
Sampler| euler  
Scheduler| simple  
Pasos| 6  
Orientación (CFG)| 1  
Denoise| 1  
  
Con la orientación en 1, no hay una pasada de orientación libre de clasificador, por lo que las plantillas no incluyen un prompt negativo. Escribe todo lo que quieras, incluidas las cosas que quieres evitar, en el prompt positivo. La salida nativa es de unos 16 MP. Cada borde se genera en un múltiplo de 32 px, y puedes usar cualquier ancho y alto. Estos tamaños cubren las relaciones de aspecto comunes:

Relación de aspecto| Tamaño (ancho x alto)  
---|---  
1:1| 4096 x 4096  
4:3| 4736 x 3552  
3:4| 3552 x 4736  
3:2| 5024 x 3360  
2:3| 3360 x 5024  
16:9| 5472 x 3072  
9:16| 3072 x 5472  
21:9| 6272 x 2688  
  
Los lienzos más pequeños también funcionan y requieren menos tiempo. En la plantilla de texto a imagen, el Selector de resolución establece la relación de aspecto y los megapíxeles objetivo por separado, así que cualquier tamaño desde unos 4 MP hasta el límite de 16 MP del selector está a un solo ajuste de distancia.

## Imágenes de referencia en la edición de imágenes

La plantilla de edición de imágenes envía la imagen fuente al modelo como `<Picture 1>`. Las imágenes adicionales se etiquetan en orden, `<Picture 2>`, `<Picture 3>`, hasta 16 referencias, y el prompt se dirige a cada una por su etiqueta. La primera imagen es la que se edita; las demás aportan identidad, accesorios, materiales o composición. Basta con una instrucción breve, por ejemplo, reemplazar el vehículo de `<Picture 1>` por el de `<Picture 2>`. Para añadir una referencia, coloca otro nodo `Load Image` en el flujo de trabajo y conéctalo tanto al paso de generación del prompt como al nodo de acondicionamiento. Las imágenes de referencia no necesitan preparación: la plantilla redondea la fuente a un múltiplo de 32 px y ComfyUI escala las copias internas por sí mismo, con un lado corto de 1024 px para el lado de visión y un lado corto limitado entre 1024 y 2048 px para el lado del VAE, ambos en la cuadrícula de 32 px. Si una edición se queda sin memoria, habilita el nodo `Resize Image/Mask` de la plantilla y reduce sus megapíxeles antes del muestreo.

## Expansor de prompt

Las plantillas de texto a imagen y de edición de imágenes incluyen un paso de generación de texto delante del sampler. En la plantilla de texto a imagen, reescribe el prompt en una descripción detallada en inglés. En la plantilla de edición de imágenes, convierte una instrucción breve en una descripción de la imagen finalizada que tiene en cuenta la referencia. El expansor oficial para MiniMax-H3-Image es un modelo Qwen3.8-27B FP4, publicado como [MiniMaxAI/MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE). Las plantillas usan en su lugar una versión más ligera de Qwen3.5 9B W4A8, para que el expansor quepa junto al modelo de diffusion de 21 GB en una sola GPU. Las plantillas de texto a imagen y de edición de imágenes vienen con el expansor activado, así que tu prompt se reescribe antes del muestreo. Desactívalo para enviar tu prompt al modelo exactamente como lo escribiste.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/minimax/minimax-h3-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/minimax/minimax-h3-image)

[Combinar ControlNet](https://docs.comfy.org/es/tutorials/controlnet/mixing-controlnets)[FIBO 2.0](https://docs.comfy.org/es/tutorials/image/bria/fibo-2-0)
