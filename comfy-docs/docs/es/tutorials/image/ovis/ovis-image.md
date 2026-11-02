---
url: https://docs.comfy.org/es/tutorials/image/ovis/ovis-image/
title: Ovis-Image en ComfyUI: modelo de renderizado de texto de 7B - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.622768+00:00
---

# Ovis-Image en ComfyUI: modelo de renderizado de texto de 7B - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/ovis/ovis-image/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen de Ovis-Image
    * Ovis-Image: texto a imagen
  * Enlaces del modelo



Ovis

# Ovis-Image en ComfyUI: modelo de renderizado de texto de 7B

Copiar páginaCopiar página

Ejecuta Ovis-Image en ComfyUI para renderizar texto nítido en chino e inglés en pósteres, banners, logos y maquetas de UI desde un prompt de texto.

Copiar páginaCopiar página

**Ovis-Image** es un modelo de texto a imagen de 7B construido sobre [Ovis-U1](https://github.com/AIDC-AI/Ovis-U1) y optimizado específicamente para el renderizado de texto de alta calidad. Ofrece una calidad de renderizado de texto comparable a la de sistemas mucho más grandes, de la clase de 20B, y sigue siendo lo bastante compacto para ejecutarse en hardware ampliamente accesible. **Aspectos destacados del modelo** :

  * **Renderizado de texto sólido a escala 7B** : ofrece una calidad de renderizado de texto comparable a la de sistemas mucho más grandes, de la clase de 20B, como Qwen-Image, y competitiva con modelos de código cerrado líderes como GPT4o en escenarios centrados en texto
  * **Alta fidelidad en prompts con mucho texto** : destaca en prompts que exigen una alineación estrecha entre el contenido lingüístico y la tipografía renderizada (por ejemplo, pósteres, banners, logotipos, maquetas de UI, infografías)
  * **Renderizado de texto bilingüe preciso** : produce texto legible, con la ortografía correcta y semánticamente coherente tanto en chino como en inglés, en fuentes, tamaños y relaciones de aspecto diversos
  * **Eficiencia y facilidad de despliegue** : cabe en una sola GPU de gama alta con memoria moderada y admite un uso interactivo de baja latencia

**Enlaces relacionados** :

  * [GitHub](https://github.com/AIDC-AI/Ovis-Image)
  * [Hugging Face](https://huggingface.co/AIDC-AI/Ovis-Image-7B)



## 

​

Flujo de trabajo de texto a imagen de Ovis-Image

### 

​

Ovis-Image: texto a imagen

Ovis-Image es un modelo de texto a imagen de 7B optimizado específicamente para el renderizado de texto de alta calidad en las imágenes generadas. Está diseñado para funcionar de forma eficiente bajo restricciones computacionales estrictas. ![Vista previa del flujo de trabajo de texto a imagen de Ovis-Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ovis_text_to_image-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ovis image” en la Biblioteca de plantillas

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

Enlaces del modelo

**text_encoders**

  * [ovis_2.5.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/blob/main/split_files/text_encoders/ovis_2.5.safetensors)

**diffusion_models**

  * [ovis_image_bf16.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/blob/main/split_files/diffusion_models/ovis_image_bf16.safetensors)

**vae**

  * [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/vae/ae.safetensors)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── ovis_2.5.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── ovis_image_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/ovis/ovis-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/ovis/ovis-image)

[HiDream-O1-Image](https://docs.comfy.org/es/tutorials/image/hidream/hidream-o1)[NewBie-image-Exp0.1](https://docs.comfy.org/es/tutorials/image/newbie-image/newbie-image-exp-0-1)
