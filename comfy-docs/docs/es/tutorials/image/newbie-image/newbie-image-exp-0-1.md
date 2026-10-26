---
url: https://docs.comfy.org/es/tutorials/image/newbie-image/newbie-image-exp-0-1/
title: Ejemplo de flujo de trabajo de ComfyUI NewBie-image-Exp0.1 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.461083+00:00
---

# Ejemplo de flujo de trabajo de ComfyUI NewBie-image-Exp0.1 - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/newbie-image/newbie-image-exp-0-1/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen con NewBie-image
    * NewBie Exp0.1: generación de anime
  * Enlaces de modelos
  * Formato del prompt
    * Prompt estructurado en XML
    * Referencia de etiquetas XML



NewBie-image

# Ejemplo de flujo de trabajo de ComfyUI NewBie-image-Exp0.1

Copiar páginaCopiar página

NewBie-image-Exp0.1 es un modelo texto a imagen de anime de 3.5B basado en Next-DiT para arte detallado con prompts XML estructurados en ComfyUI.

Copiar páginaCopiar página

**NewBie-image-Exp0.1** es un modelo DiT de 3.5B parámetros desarrollado por NewBieAI Lab para la generación de imágenes de estilo anime a partir de texto. Construido sobre la arquitectura Next-DiT, ofrece imágenes anime notablemente detalladas y visualmente impactantes. **Características principales** :

  * **Modelo de 3.5B parámetros** : un tamaño de modelo eficiente pero potente para generar anime de alta calidad
  * **Arquitectura Next-DiT** : basada en la investigación de la arquitectura Lumina, con una arquitectura NewBie de nuevo diseño
  * **Doble codificador de texto** : usa Gemma3-4B-it como codificador principal junto con Jina CLIP v2 para mejorar la comprensión del prompt
  * **VAE de FLUX** : utiliza el VAE de 16 canales de FLUX.1-dev para colores más ricos y texturas más finas
  * **Prompts estructurados en XML** : admite el formato XML para un mejor vínculo de atención y una mejor separación de atributos

**Enlaces relacionados** :

  * [GitHub](https://github.com/NewBieAI-Lab/NewBie-image-Exp0.1)
  * [Hugging Face](https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1)
  * [Guía de primeros pasos](https://ai.feishu.cn/wiki/NZl9wm7V1iuNzmkRKCUcb1USnsh)



## 

​

Flujo de trabajo de texto a imagen con NewBie-image

### 

​

NewBie Exp0.1: generación de anime

Genera imágenes detalladas de estilo anime con la arquitectura Next-DiT de NewBie Exp0.1. Admite prompts estructurados en XML para mejorar las escenas con varios personajes y la vinculación de atributos. ![Vista previa del flujo de trabajo de texto a imagen con NewBie-image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_newbieimage_exp0_1-t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “NewBie-image” en la biblioteca de plantillas

**Ejemplo de salida** ![Ejemplo de salida de NewBie-image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_newbieimage_exp0_1-t2i.png)

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

Enlaces de modelos

**text_encoders**

  * [gemma_3_4b_it_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/text_encoders/gemma_3_4b_it_bf16.safetensors)
  * [jina_clip_v2_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/text_encoders/jina_clip_v2_bf16.safetensors)

**diffusion_models**

  * [NewBie-Image-Exp0.1-bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/blob/main/split_files/diffusion_models/NewBie-Image-Exp0.1-bf16.safetensors)

**vae**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/vae/ae.safetensors)

**Ubicación de almacenamiento de los modelos**
    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │      ├── gemma_3_4b_it_bf16.safetensors
    │   │      └── jina_clip_v2_bf16.safetensors
    │   ├── diffusion_models/
    │   │      └── NewBie-Image-Exp0.1-bf16.safetensors
    │   └── vae/
    │          └── ae.safetensors
    

## 

​

Formato del prompt

NewBie-image es un modelo de generación de imágenes de anime optimizado para generar personajes. Utiliza prompts estructurados en XML para el entrenamiento, donde cada etiqueta `<>` define una categoría (como `<appearance>`, `<clothing>`) y `</>` la cierra. Las etiquetas internas son etiquetas estándar de Danbooru. Esta estructura permite un control preciso de escenas con varios personajes, con una mejor vinculación de atributos. Para consultar la guía completa de escritura de prompts, ve a la [documentación oficial](https://ai.feishu.cn/wiki/NZl9wm7V1iuNzmkRKCUcb1USnsh). NewBie-image-Exp0.1 admite tres formatos de prompt:

  * **Lenguaje natural** : Descripciones de texto estándar
  * **Etiquetas** : Etiquetas al estilo Danbooru
  * **Formato estructurado XML** : Recomendado para escenas con varios personajes



### 

​

Prompt estructurado en XML

En escenas con varios personajes, usar prompts estructurados en XML suele producir resultados de generación de imágenes más precisos, con una mejor vinculación de la atención y separación de atributos.
    
    
    <character_1>
    <n>$character_1$</n>
    <gender>1girl</gender>
    <appearance>chibi, red_eyes, blue_hair, long_hair, hair_between_eyes, head_tilt, tareme, closed_mouth</appearance>
    <clothing>school_uniform, serafuku, white_sailor_collar, white_shirt, short_sleeves, red_neckerchief, bow, blue_skirt, miniskirt, pleated_skirt, blue_hat, mini_hat, thighhighs, grey_thighhighs, black_shoes, mary_janes</clothing>
    <expression>happy, smile</expression>
    <action>standing, holding, holding_briefcase</action>
    <position>center_left</position>
    </character_1>
    
    <character_2>
    <n>$character_2$</n>
    <gender>1girl</gender>
    <appearance>chibi, red_eyes, pink_hair, long_hair, very_long_hair, multi-tied_hair, open_mouth</appearance>
    <clothing>school_uniform, serafuku, white_sailor_collar, white_shirt, short_sleeves, red_neckerchief, bow, red_skirt, miniskirt, pleated_skirt, hair_bow, multiple_hair_bows, white_bow, ribbon_trim, ribbon-trimmed_bow, white_thighhighs, black_shoes, mary_janes, bow_legwear, bare_arms</clothing>
    <expression>happy, smile</expression>
    <action>standing, holding, holding_briefcase, waving</action>
    <position>center_right</position>
    </character_2>
    
    <general_tags>
    <count>2girls, multiple_girls</count>
    <style>anime_style, digital_art</style>
    <background>white_background, simple_background</background>
    <atmosphere>cheerful</atmosphere>
    <quality>high_resolution, detailed</quality>
    <objects>briefcase</objects>
    <other>alternate_costume</other>
    </general_tags>
    

### 

​

Referencia de etiquetas XML

Etiqueta| Descripción  
---|---  
`<n>`| Nombre/identificador del personaje  
`<gender>`| Género del personaje (1girl, 1boy, etc.)  
`<appearance>`| Rasgos físicos (cabello, ojos, tipo de cuerpo)  
`<clothing>`| Atuendo y accesorios  
`<expression>`| Expresión facial  
`<action>`| Pose y acciones  
`<position>`| Posición en la imagen  
`<count>`| Número de personajes  
`<style>`| Estilo artístico  
`<background>`| Descripción del fondo  
`<atmosphere>`| Ambiente general  
`<quality>`| Etiquetas de calidad  
`<objects>`| Objetos en la escena  
`<other>`| Etiquetas adicionales  
  
¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/newbie-image/newbie-image-exp-0-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/newbie-image/newbie-image-exp-0-1)

[HiDream-O1-Image](https://docs.comfy.org/es/tutorials/image/hidream/hidream-o1)[ERNIE-Image](https://docs.comfy.org/es/tutorials/image/ernie-image/ernie-image)
