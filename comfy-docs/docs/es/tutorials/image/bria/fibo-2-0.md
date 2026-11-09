---
url: https://docs.comfy.org/es/tutorials/image/bria/fibo-2-0/
title: Bria FIBO 2.0 con pesos abiertos en ComfyUI: edici\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:31.396470+00:00
---

# Bria FIBO 2.0 con pesos abiertos en ComfyUI: edición de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/bria/fibo-2-0/

## En esta página

Volver arriba

  * Fibo 2.0 Turbo: Image Edit
  * Fibo 2.0 Dev: Image Edit
  * Descarga de modelos
  * Licencia



FIBO 2.0

# Bria FIBO 2.0 con pesos abiertos en ComfyUI: edición de imágenes

Copiar páginaCopiar página

Edita imágenes en local con Bria FIBO 2.0 en ComfyUI usando los flujos de pesos abiertos Turbo y Dev.

Copiar páginaCopiar página

FIBO 2.0 es el modelo de imágenes de 8B de Bria que genera y edita con un solo conjunto de pesos. La versión de pesos abiertos se ejecuta en local en ComfyUI sin créditos, trabaja en el espacio latente del VAE de FLUX.2 y codifica los prompts con Qwen3-VL-4B. Incluye dos plantillas. **Fibo 2.0 Turbo: Image Edit** es la versión destilada para probar direcciones rápido, y **Fibo 2.0 Dev: Image Edit** ejecuta la base sin destilar para la edición más limpia. Ambas reciben una imagen de referencia y una instrucción de una línea.

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

Fibo 2.0 Turbo: Image Edit

![Fibo 2.0 Turbo: Image Edit, imagen de referencia](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_turbo_pe-1.webp) ![Fibo 2.0 Turbo: Image Edit, resultado](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_turbo_pe-2.webp)

## Ejecutar en Comfy Cloud

Ejecuta el flujo de edición Turbo en Comfy Cloud

## Fibo 2.0 Turbo: Image Edit

Descarga el flujo de trabajo o busca “Fibo 2.0 Turbo: Image Edit” en la Biblioteca de plantillas

## auburn_afro_payphone_portrait.png

Imagen de referencia de ejemplo para el nodo LoadImage

Carga la imagen de referencia, describe en `prompt` cómo debe quedar la zona que quieres cambiar y ejecuta.

## 

​

Fibo 2.0 Dev: Image Edit

![Fibo 2.0 Dev: Image Edit, imagen de referencia](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-1.webp) ![Fibo 2.0 Dev: Image Edit, resultado](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-2.webp)

## Ejecutar en Comfy Cloud

Ejecuta el flujo de edición Dev en Comfy Cloud

## Fibo 2.0 Dev: Image Edit

Descarga el flujo de trabajo o busca “Fibo 2.0 Dev: Image Edit” en la Biblioteca de plantillas

## red_bowler_hat_portrait.png

Imagen de referencia de ejemplo para el nodo LoadImage

El mismo grafo con los pesos sin destilar. El muestreo tarda unas doce veces más y resuelve mejor la textura. Mantén el `negative_prompt` estructurado que incluye.

## 

​

Descarga de modelos

Ambas plantillas cargan los archivos int8_convrot, el codificador de texto 4B en bf16 y el codificador 8B con el que el potenciador de prompts lee la imagen de referencia. Los archivos bf16 de difusión son los mismos pesos en precisión completa, con el doble de tamaño.

## fibo2_edit_turbo_int8_convrot.safetensors

fibo2_edit_turbo_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## fibo2_dev_int8_convrot.safetensors

fibo2_dev_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## fibo2_edit_turbo_bf16.safetensors

fibo2_edit_turbo_bf16.safetensors → ComfyUI/models/diffusion_models/

## fibo2_dev_bf16.safetensors

fibo2_dev_bf16.safetensors → ComfyUI/models/diffusion_models/

## qwen3vl_4b_bf16.safetensors

qwen3vl_4b_bf16.safetensors → ComfyUI/models/text_encoders/

## qwen3vl_4b_int8_convrot.safetensors

qwen3vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## qwen3vl_8b_int8_convrot.safetensors

qwen3vl_8b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## flux2-vae.safetensors

flux2-vae.safetensors → ComfyUI/models/vae/

## fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors

LoRA Turbo opcional, hace que la base Dev vaya más rápido → ComfyUI/models/loras/

## 

​

Licencia

BRIA AI publica los pesos de FIBO 2.0 bajo [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), que cubre el uso no comercial. El uso comercial requiere un acuerdo aparte con Bria o los [nodos de partner de Bria FIBO 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bria/fibo).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/bria/fibo-2-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/bria/fibo-2-0)

[Combinar ControlNet](https://docs.comfy.org/es/tutorials/controlnet/mixing-controlnets)[P-H3-Image](https://docs.comfy.org/es/tutorials/image/pruna/p-h3-image)
