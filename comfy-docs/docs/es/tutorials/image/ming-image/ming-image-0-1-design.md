---
url: https://docs.comfy.org/es/tutorials/image/ming-image/ming-image-0-1-design/
title: Ming Image 0.1 Design: texto a imagen RGBA en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.381180+00:00
---

# Ming Image 0.1 Design: texto a imagen RGBA en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/ming-image/ming-image-0-1-design/

## En esta página

Volver arriba

  * Para qué sirve Ming Image 0.1 Design
  * Salidas de ejemplo
  * Flujo de trabajo de texto a imagen de Ming Image 0.1 Design
    * Pasos para ejecutar el flujo de trabajo
    * Descargas de modelos
  * Guía de prompts
  * Empezar



Ming Image

# Ming Image 0.1 Design: texto a imagen RGBA en ComfyUI

Copiar páginaCopiar página

Genera diseños con texto legible y fondos transparentes con Ming Image 0.1 Design, un modelo de pesos abiertos de 6B de inclusionAI en ComfyUI

Copiar páginaCopiar página

**Ming Image 0.1 Design** es un modelo de texto a imagen de 6B con pesos abiertos de inclusionAI (Ant Group), publicado bajo la licencia MIT. Está orientado al trabajo de diseño más que al realismo fotográfico: pantallas de interfaz, infografías, pósteres y otras maquetas que contienen mucho texto. Las salidas son RGBA con un canal alfa real, así que un resultado transparente se puede colocar directamente en un archivo de diseño. El flujo de trabajo coloca una etapa de reescritura del prompt antes del sampler. Qwen3.8-27B expande una idea breve en una descripción estructurada de la maqueta antes del muestreo, y el potenciador se puede desactivar cuando quieres que tu texto se envíe exactamente como lo escribiste. **Enlaces relacionados**

  * [inclusionAI/Ming-Image (GitHub)](https://github.com/inclusionAI/Ming-Image)
  * [Comfy-Org/Ming-Image (Hugging Face)](https://huggingface.co/Comfy-Org/Ming-Image)
  * [inclusionAI/Ming-Image-0.1-Design (Hugging Face)](https://huggingface.co/inclusionAI/Ming-Image-0.1-Design)



## 

​

Para qué sirve Ming Image 0.1 Design

  * **Diseños largos y estructurados** : páginas, pósteres e infografías con muchas secciones, compuestos sección por sección
  * **Representación de texto** : las cadenas entrecomilladas en el prompt se respetan con precisión, por lo que las etiquetas, los precios y los títulos se mantienen legibles
  * **Salida transparente** : imágenes RGBA con un canal alfa real para la composición de elementos aislados
  * **Reescritura de prompts** : un modelo de visión-lenguaje que sigue instrucciones amplía una breve descripción en un caption detallado del diseño
  * **Pesos abiertos** : con licencia MIT, por lo que puedes usar y ajustar los checkpoints libremente



## 

​

Salidas de ejemplo

Generación de texto a imagen de un diseño con mucho texto, guardada como un solo PNG: ![Ejemplo de texto a imagen de Ming Image 0.1 Design](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_ming_image_01_design_t2i.png)

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

Flujo de trabajo de texto a imagen de Ming Image 0.1 Design

Genera una composición de diseño a partir de un prompt de texto, mientras el modelo se encarga de la disposición, la tipografía y la transparencia del fondo. ![Vista previa del flujo de trabajo de texto a imagen de Ming Image 0.1 Design](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Ming Image 0.1 Design” en la Biblioteca de plantillas

### 

​

Pasos para ejecutar el flujo de trabajo

  1. Entra en el subgrafo **Text to Image (Ming Image 0.1 Design)** con el botón **Entrar en subgrafo** en la parte inferior de ese nodo
  2. Escribe tu prompt en el campo `prompt`, describiendo la disposición sección por sección y colocando entre comillas cualquier texto que quieras que se renderice
  3. Elige el lienzo con el nodo `ResolutionSelector`: 2048 x 2048 ofrece la mejor calidad y 1024 x 1024 es más rápido
  4. Deja activado el mejorador de prompt para que Qwen3.8-27B expanda tu prompt, o desactiva `enable_PE` para enviar tu texto exactamente como lo escribiste
  5. Pon el prompt en cola. La imagen decodificada aparece en el nodo `PreviewImage`
  6. Para obtener un fondo transparente, antepón una frase RGBA a tu prompt, por ejemplo `RGBA, 4-channel, transparent background`



### 

​

Descargas de modelos

## ming_image_0.1_design_int8_convrot.safetensors

Modelo de difusión para Ming Image 0.1 Design (cargado por la plantilla).

## ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors

Codificador de texto para Ming Image 0.1 Design (cargado por la plantilla).

## qwen3.8_27b_w4a8.safetensors

Codificador de texto de reescritura de prompts que usa el mejorador de prompts.

## ming_image_vae_bf16.safetensors

VAE para Ming Image 0.1 Design.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── ming_image_0.1_design_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors
    │   │   └── qwen3.8_27b_w4a8.safetensors
    │   └── 📂 vae/
    │       └── ming_image_vae_bf16.safetensors
    

Ese repositorio también publica checkpoints de precisión completa, [ming_image_0.1_design_bf16.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_bf16.safetensors) y [ming_image_0.1_ling_mini_2.0_bf16.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_bf16.safetensors), además de variantes `_layer` tanto del modelo de difusión como del codificador de texto.

## 

​

Guía de prompts

  * [Reescritura de prompts de texto a imagen](https://github.com/inclusionAI/Ming-Image#text-to-image-prompt-rewriting): la estructura oficial del prompt y el system prompt del reescritor que ejecuta el enhancer de este flujo de trabajo
  * [Consejo para generar con fondo transparente](https://github.com/inclusionAI/Ming-Image#transparent-background-generation-tip): las frases RGBA fijas que debes anteponer a un prompt



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión. El soporte de Ming Image 0.1 está en las compilaciones más recientes de ComfyUI
  2. Ve a Biblioteca de plantillas y busca `Ming Image 0.1 Design`



Comfy Desktop y Comfy Cloud siguen las versiones estables, así que un modelo que solo tiene soporte en la compilación más reciente de ComfyUI puede que aún no esté disponible allí.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/ming-image/ming-image-0-1-design.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/ming-image/ming-image-0-1-design)

[Mage-Flow](https://docs.comfy.org/es/tutorials/image/mage-flow/mage-flow)[Cosmos-Predict2](https://docs.comfy.org/es/tutorials/image/cosmos/cosmos-predict2-t2i)
