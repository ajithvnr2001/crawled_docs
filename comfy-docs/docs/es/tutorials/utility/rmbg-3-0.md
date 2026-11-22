---
url: https://docs.comfy.org/es/tutorials/utility/rmbg-3-0/
title: RMBG 3.0: mattes alfa suaves para eliminaci\u00f3n de fondo en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:52.201921+00:00
---

# RMBG 3.0: mattes alfa suaves para eliminación de fondo en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/rmbg-3-0/

## En esta página

Volver arriba

  * Eliminar fondo: RMBG 3.0
  * Controles del flujo de trabajo
  * Cuando el recorte no es correcto
  * Licencia



Segmentation & Background

# RMBG 3.0: mattes alfa suaves para eliminación de fondo en ComfyUI

Copiar páginaCopiar página

Elimina fondos con RMBG 3.0 en ComfyUI: modelo de matting de 4 pasos que devuelve un matte alfa suave de 8 bits, un recorte RGBA y una placa de fondo.

Copiar páginaCopiar página

RMBG 3.0 es el tercer modelo de eliminación de fondo de Bria y el primero construido sobre un modelo generativo en lugar de una red de segmentación. Genera una matte alfa en escala de grises suave en lugar de una máscara binaria dura, por lo que el cabello, el pelaje, la malla, los velos y el desenfoque de movimiento conservan transparencia parcial. La base es Fibo 2.0, con un transformer de difusión de 8B y un codificador de prompt e imagen Qwen3-VL-4B, destilado a 4 pasos de muestreo sin orientación libre de clasificador. El soporte de ComfyUI llegó en [ComfyUI #17240](https://github.com/Comfy-Org/ComfyUI/pull/17240), y la plantilla necesita ComfyUI 0.46.0 o posterior. El flujo de trabajo recibe una imagen y devuelve tres salidas: el recorte RGBA, la placa de fondo y la máscara procesada.

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

## Eliminar fondo: RMBG 3.0

![Flujo de trabajo para eliminar fondo con RMBG 3.0 y comparación de ANTES y DESPUÉS](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_rmbg3_remove_background-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Remove Background: RMBG 3.0” en la Biblioteca de plantillas

**Modelos**

## Modelo de difusión

rmbg3_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## Codificador de texto

qwen3vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## VAE

flux2-vae.safetensors → ComfyUI/models/vae/

Ese mismo repositorio también incluye versiones BF16 del modelo de difusión y del codificador de texto, si prefieres cambiar memoria por precisión. **Material de entrada**

## withered_hydrangeas_still_life_vintage_lit.png

Cárgala en el nodo `LoadImage`

  1. Arrastra tu foto al nodo `LoadImage`.
  2. Activa `auto_prompt`, que viene desactivado en la plantilla. Con él desactivado, el nodo envía la instrucción fija y `subject_note` no se usa.
  3. Opcional: escribe una frase corta sobre el material en `subject_note`, por ejemplo `Clear glass bottle, paper label, metal cap`.
  4. Ejecuta el flujo de trabajo. `SaveImage` escribe ambos resultados en `ComfyUI/output/rmbg3/`.



## Controles del flujo de trabajo

  * `auto_prompt`: cuando está activado, un modelo de visión escribe la instrucción de matting a partir de la imagen y tu `subject_note`. Cuando está desactivado, se envía tal cual la instrucción fija con la que se entrenó el modelo y `subject_note` se ignora.
  * `cfg`: mantenlo en 1.0. El modelo está destilado sin orientación, así que un valor más alto sacrifica fidelidad a la fuente a cambio de transparencia.
  * `alpha_brightness`, `alpha_contrast`, `mask_threshold`, `hard_mask`: posprocesamiento del matte. Deja `hard_mask` desactivado para conservar los bordes suaves.
  * `mask_expand`, `mask_tapered_corners`: amplían y redondean el matte antes de aplicarlo.



## Cuando el recorte no es correcto

Síntoma| Solución  
---|---  
El vidrio, el velo o el humo salen sólidos| Activa `auto_prompt`, describe el material en `subject_note` y luego aumenta `cfg` a 1.5 o 2.0  
Neblina gris sobre el fondo| Baja `alpha_brightness` o activa `hard_mask`  
El vidrio de color permanece opaco| Baja `alpha_brightness` o pinta esa área a mano  
  
Hay dos limitaciones que provienen del propio modelo: las escenas muy cargadas o de bajo contraste pueden incluir hierba, objetos o una marca de agua junto al sujeto, y las estructuras finas, como las alas de los insectos, pueden perder píxeles.

## Licencia

Los pesos se publican bajo [CC BY-NC 4.0](https://huggingface.co/briaai/RMBG-3.0-Comfy). El uso comercial requiere un acuerdo por separado con Bria: ya sea una licencia autoalojada o la [API de Bria](https://docs.bria.ai/whats-new/rmbg-3). El nodo socio de Bria ejecuta el mismo modelo a través de esa API.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/rmbg-3-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/rmbg-3-0)

[BiRefNet](https://docs.comfy.org/es/tutorials/utility/remove-background-birefnet)[SAM 3D Body](https://docs.comfy.org/es/tutorials/utility/sam3d-body)
