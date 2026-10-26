---
url: https://docs.comfy.org/es/tutorials/basic/multiple-loras/
title: ComfyUI con varios LoRA: encadena cargadores para combinar estilos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.623927+00:00
---

# ComfyUI con varios LoRA: encadena cargadores para combinar estilos - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/basic/multiple-loras/

## En esta página

Volver arriba

  * Instalar los modelos
  * Flujo de trabajo con varios LoRA
  * Completar el flujo de trabajo paso a paso
  * Pruébalo tú mismo



Basic Examples

# ComfyUI con varios LoRA: encadena cargadores para combinar estilos

Copiar páginaCopiar página

Aplica dos o más modelos LoRA a la vez en ComfyUI encadenando nodos Load LoRA y combina estilos y personajes en una sola generación.

Copiar páginaCopiar página

En nuestro [Ejemplo de LoRA en ComfyUI](https://docs.comfy.org/es/tutorials/basic/lora) presentamos cómo cargar y usar un solo modelo LoRA, y mencionamos la capacidad de conexión en cadena del nodo. ![Encadenamiento de nodos LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/lora/chain_link.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=905ee3b2883bf67bd986989f57f62caf) Este tutorial muestra cómo encadenar varios nodos `Load LoRA` para aplicar dos modelos LoRA al mismo tiempo: [blindbox_V1Mix](https://civitai.com/models/25995?modelVersionId=32988) y [MoXinV1](https://civitai.com/models/12597?modelVersionId=14856). La siguiente comparación muestra los efectos individuales de estos LoRA con parámetros idénticos: ![Comparación de los efectos de cada LoRA por separado](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/compare.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=3f26ac1b06c82aa86bf13062a1409131) Al encadenar varios modelos LoRA, logramos un estilo combinado en el resultado final: ![Resultado de aplicar varios LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/multiple_loras.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=f96d5ad3564a7ce69c8acc643eab0776)

## 

​

Instalar los modelos

Descarga el archivo [dreamshaper_8.safetensors](https://civitai.com/api/download/models/128713?type=Model&format=SafeTensor&size=pruned&fp=fp16) y colócalo en tu carpeta `ComfyUI/models/checkpoints`. Descarga el archivo [blindbox_V1Mix.safetensors](https://civitai.com/api/download/models/32988?type=Model&format=SafeTensor&size=full&fp=fp16) y colócalo en tu carpeta `ComfyUI/models/loras`. Descarga el archivo [MoXinV1.safetensors](https://civitai.com/api/download/models/14856?type=Model&format=SafeTensor&size=full&fp=fp16) y colócalo en tu carpeta `ComfyUI/models/loras`.

## 

​

Flujo de trabajo con varios LoRA

Descarga la imagen de abajo y **arrástrala a ComfyUI** para cargar el flujo de trabajo: ![Flujo de trabajo de ComfyUI con varios LoRA](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/multiple_loras.png)

Puedes arrastrar directamente a ComfyUI las imágenes que contienen el JSON del flujo de trabajo en sus metadatos, o cargarlas desde el menú `Workflows` -> `Open (ctrl+o)`.

## 

​

Completar el flujo de trabajo paso a paso

Sigue los pasos del diagrama de abajo para asegurarte de que el flujo de trabajo se ejecute correctamente. ![Diagrama del flujo de trabajo con varios LoRA](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/basic/multiple_loras/flow_diagram.png?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=daa5ef546221542dfe0b2ec8b408f689)

  1. Asegúrate de que `Load Checkpoint` cargue **dreamshaper_8.safetensors**
  2. Asegúrate de que el primer `Load LoRA` cargue **blindbox_V1Mix.safetensors**
  3. Asegúrate de que el segundo `Load LoRA` cargue **MoXinV1.safetensors**
  4. Haz clic en `Queue` o pulsa `Ctrl/Cmd + Enter` para generar



## 

​

Pruébalo tú mismo

  1. Ajusta los valores de `strength_model` en ambos nodos `Load LoRA` para controlar la influencia de cada LoRA
  2. Explora [CivitAI](https://civitai.com/models) para encontrar más LoRA y crear tus propias combinaciones



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/basic/multiple-loras.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/basic/multiple-loras)

[LoRA](https://docs.comfy.org/es/tutorials/basic/lora)[ControlNet](https://docs.comfy.org/es/tutorials/controlnet/controlnet)
