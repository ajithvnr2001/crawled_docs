---
url: https://docs.comfy.org/es/tutorials/flux/flux-3-klein/
title: FLUX 3 Image Klein en ComfyUI: texto a imagen y edici\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:30.508823+00:00
---

# FLUX 3 Image Klein en ComfyUI: texto a imagen y edición - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/flux/flux-3-klein/

## En esta página

Volver arriba

  * Acerca de FLUX.3 [klein]
  * Flujos de trabajo de FLUX 3 Image Klein
    * FLUX 3 Image Klein: Texto a imagen
    * FLUX 3 Image Klein Distilled: Texto a imagen
    * FLUX 3 Image Klein: edición de imágenes
    * FLUX 3 Image Klein Distilled: edición de imágenes
  * Descargas del modelo FLUX 3 Image Klein
  * Consejos para prompts y referencias



FLUX

# FLUX 3 Image Klein en ComfyUI: texto a imagen y edición

Copiar páginaCopiar página

Ejecuta FLUX.3 [klein] en local en ComfyUI: texto a imagen con pesos abiertos y edición por instrucciones, con un checkpoint destilado para 4–16 pasos.

Copiar páginaCopiar página

## 

​

Acerca de FLUX.3 [klein]

FLUX.3 [klein] es el modelo de imágenes FLUX.3 de pesos abiertos de Black Forest Labs para ComfyUI local: texto a imagen y edición de imágenes guiada por instrucciones en una misma familia, con un checkpoint completo y una variante destilada por pasos para ejecuciones más rápidas de 4–16 pasos. Los pesos se publican en Hugging Face bajo la Licencia FLUX Kommunity. Descárgalo una vez, ejecútalo en tu propia GPU, sin clave API ni créditos por imagen. ¿Prefieres la ruta alojada? FLUX.3 también se ejecuta como Partner Node mediante [FLUX 3 Image](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-image) (con cobro por imagen). Usa los pesos locales de klein en tu GPU; usa el Partner Node cuando quieras el modelo alojado sin descarga. **Aspectos destacados del modelo:**

  * Texto a imagen y edición de imágenes con los mismos pesos; las ediciones usan un prompt de instrucción e imágenes de referencia
  * Dos checkpoints: FLUX 3 Image Klein completo y Distilled para muestreo sin orientación en 4–16 pasos
  * Prompts con múltiples referencias mediante `<ref_image_0>`, `<ref_image_1>`, etc.
  * Upsampler de prompts Qwen3.5 9B opcional que expande solicitudes breves en descripciones completas antes de la generación
  * Checkpoints de archivo único en bf16, int8 (convrot) y nvfp4, con un codificador de texto Qwen3-VL-4B y el VAE de FLUX.2

**Licencia** : [FLUX Kommunity License](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/blob/main/LICENSE.md) **Requisito de versión** : las plantillas de FLUX 3 Klein necesitan ComfyUI 0.41.0 o posterior (incluido en el backport 0.41.1, ComfyUI#17070).

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

Flujos de trabajo de FLUX 3 Image Klein

### 

​

FLUX 3 Image Klein: Texto a imagen

Genera una imagen a partir de un prompt, sin archivos de entrada. El flujo de trabajo es un subgrafo: ábrelo para acceder a los cargadores, al sampler y al tamaño del lienzo. ![Vista previa del flujo de trabajo de texto a imagen de FLUX 3 Image Klein](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image Klein: Text to Image” en la Biblioteca de plantillas

  1. Escribe tu prompt en el widget de prompt positivo del subgrafo
  2. Define `width` y `height`, o elige un formato en `ResolutionSelector` (1:1 cuadrado de forma predeterminada)
  3. Ajusta `steps` (50 de forma predeterminada) y `cfg` (3.5 de forma predeterminada)
  4. El ampliador de prompts está activado de forma predeterminada, así que un prompt corto se amplía con el ampliador Qwen3.5 9B antes del muestreo. Desactiva `enable_prompt_upsampler` para generar a partir de tus propias palabras
  5. Haz clic en **Queue**. El nodo `SaveImage` guarda la imagen en `ComfyUI/output/`



### 

​

FLUX 3 Image Klein Distilled: Texto a imagen

Genera una imagen a partir de un prompt con el checkpoint destilado por pasos, que se ejecuta en 16 pasos sin orientación. La ampliación del prompt está activada de forma predeterminada, por lo que un prompt corto se expande a una descripción completa antes del muestreo. ![Vista previa del flujo de trabajo de texto a imagen de FLUX 3 Image Klein Distilled](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image Klein Distilled: Text to Image” en la Biblioteca de plantillas

  1. Escribe tu prompt. La plantilla lo amplía primero, así que basta con una descripción corta
  2. Configura `steps` entre 4 y 16 (16 de forma predeterminada). El checkpoint destilado se ejecuta con `cfg` 1, así que aumentar `cfg` no ayuda
  3. Elige un tamaño de `ResolutionSelector`
  4. Haz clic en **Queue** para generar

**Ejemplo de salida** ![Ejemplo de texto a imagen de FLUX 3 Image Klein Distilled](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux3_klein_distilled_t2i.png)

### 

​

FLUX 3 Image Klein: edición de imágenes

Edita una foto a partir de un prompt de instrucción, con la imagen original conectada como referencia. La instrucción reemplaza el contenido de la referencia: aquí el prompt cambia el color del vestido a rojo mientras todo lo demás permanece igual. ![Vista previa del flujo de trabajo de edición de imágenes de FLUX 3 Image Klein](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image Klein: Image Edit” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## fashion_portrait_blue_silk_gown_vis.png

nodo `LoadImage` 54 · `fashion_portrait_blue_silk_gown_vis.png`

![fashion_portrait_blue_silk_gown_vis.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/fashion_portrait_blue_silk_gown_vis.png)

  1. Carga tu imagen fuente en el nodo `LoadImage`
  2. Conéctala a `Set Reference Multi Latent`. La primera referencia es `<ref_image_0>` en el prompt, la siguiente es `<ref_image_1>`, y así sucesivamente
  3. Escribe la edición como una descripción completa del resultado. En el ejemplo incluido, el prompt es `In <ref_image_0>, change the dress color <obj_1> to red`
  4. Ajusta el lienzo con `Empty Flux 2 Latent` (1024 x 1024 en la plantilla) si quieres un tamaño de salida diferente
  5. Haz clic en **Queue**. `ImageCompare` muestra la entrada y el resultado en paralelo

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/fashion_portrait_blue_silk_gown_vis.png)![Ejemplo de salida de la edición de imágenes de FLUX 3 Image Klein](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_flux3_klein_image_edit.png)

### 

​

FLUX 3 Image Klein Distilled: edición de imágenes

Edita una imagen con el checkpoint destilado en pasos: una imagen de referencia, un prompt de instrucción, 16 pasos y sin orientación. ![Vista previa del flujo de trabajo de edición de imágenes de FLUX 3 Image Klein Distilled](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image Klein Distilled: Image Edit” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## woman_gold_earring_teal_top_portrait.png

Nodo `LoadImage` 11 · `woman_gold_earring_teal_top_portrait.png`

![woman_gold_earring_teal_top_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/woman_gold_earring_teal_top_portrait.png)

  1. Carga la imagen que quieres editar y conéctala a `Set Reference Multi Latent`
  2. Escribe el prompt de edición. El ejemplo incluido reemplaza un arete y describe el nuevo con detalle, incluyendo lo que no debe aparecer
  3. Mantén `steps` en el rango de 4 a 16 y deja `cfg` en 1
  4. Haz clic en **Queue** y compara la entrada con el resultado en `ImageCompare`



## 

​

Descargas del modelo FLUX 3 Image Klein

Los pesos de FLUX 3 Klein están en el repositorio con acceso restringido [black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy). Ábrelo, acepta el acuerdo de licencia y luego descarga los archivos. Las plantillas usan los checkpoints de archivo único int8 (convrot); las versiones bf16 y nvfp4 de esos mismos checkpoints están en el mismo repositorio.Las plantillas cargan las compilaciones int8 para mantener pequeño el consumo de memoria. Si tienes más de 24 GB de VRAM, cambia a la compilación bf16 del mismo checkpoint (`flux3-image-klein-base-bf16.safetensors`, o `flux3-image-klein-bf16.safetensors` para el checkpoint destilado) y al upsampler de prompt bf16: siguen con más fidelidad los prompts largos.

## flux3-image-klein-base-int8-convrot.safetensors

Modelo de difusión, checkpoint completo de FLUX 3 Image Klein. Las plantillas de Texto a imagen y de edición de imagen cargan este archivo.

## flux3-image-klein-int8-convrot.safetensors

Modelo de difusión, checkpoint destilado por pasos para 4 a 16 pasos.

## qwen3vl_4b_int8_convrot.safetensors

Codificador de texto para ambos checkpoints. Cárgalo con `CLIPLoader` de tipo `flux3`.

## qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors

Upsampler de prompt que usan las plantillas de Texto a imagen.

## flux2-vae.safetensors

VAE para FLUX 3 Klein. El VAE de FLUX.2.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │      ├── flux3-image-klein-base-int8-convrot.safetensors
    │   │      └── flux3-image-klein-int8-convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │      ├── qwen3vl_4b_int8_convrot.safetensors
    │   │      └── qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
    │   └── 📂 vae/
    │          └── flux2-vae.safetensors
    

## 

​

Consejos para prompts y referencias

  * **Escribe el resultado, no el cambio.** Las plantillas de edición de imágenes esperan una descripción completa de la imagen final con la edición incorporada, y por eso los ejemplos describen el objeto nuevo en detalle en lugar de decir «cambia esto».
  * **Las referencias se añaden a los dos conditioning.** Conecta imágenes adicionales a `Set Reference Multi Latent` en orden, refiérete a ellas como `<ref_image_0>`, `<ref_image_1>` y así sucesivamente, y añade cada una tanto al prompt positivo como al negativo, tal como lo hace el pipeline de referencia.
  * **El tamaño de las referencias es un control de costo.** Las plantillas redimensionan cada referencia a aproximadamente 1 megapixel y el latente de salida toma ese tamaño. Mantener las referencias en su tamaño nativo, que es lo que hace el pipeline de Black Forest Labs hasta unos 16 megapíxeles, conserva más detalle en la edición a un costo mayor.
  * **El número de pasos depende del checkpoint.** El checkpoint completo se ejecuta con 50 pasos en las plantillas, con orientación 3.5 en texto a imagen y 1 en edición de imagen. El checkpoint destilado por pasos se ejecuta con 16 pasos y la orientación fija en 1, y es el que debes usar cuando quieras una pasada rápida.
  * **Las plantillas incluyen un nodo`Create Bounding Boxes`.** Dibuja cajas sobre la imagen fuente para planificar ediciones regionales, y su lista de cajas aparece en el nodo `Preview Any` para que puedas incorporar las regiones al prompt.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/flux/flux-3-klein.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/flux/flux-3-klein)

[MOSS-Image](https://docs.comfy.org/es/tutorials/image/moss-image/moss-image)[FLUX.2 Dev](https://docs.comfy.org/es/tutorials/flux/flux-2-dev)
