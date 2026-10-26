---
url: https://docs.comfy.org/es/tutorials/image/cosmos/cosmos-predict2-t2i/
title: Cosmos Predict2 en ComfyUI: generaci\u00f3n de texto a imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:43.425210+00:00
---

# Cosmos Predict2 en ComfyUI: generación de texto a imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/cosmos/cosmos-predict2-t2i/

Imagen

# Cosmos Predict2 en ComfyUI: generación de texto a imagen

Copiar páginaCopiar página

Genera imágenes con Cosmos-Predict2 de NVIDIA en ComfyUI: instala los modelos y completa el flujo de trabajo desde un prompt.

Copiar páginaCopiar página

Cosmos-Predict2 es el modelo fundacional del mundo físico de nueva generación de NVIDIA, diseñado específicamente para tareas de generación y predicción visual de alta calidad en escenarios de IA física. El modelo destaca por su precisión física, su interactividad con el entorno y su capacidad de reproducción de detalles, lo que permite simular de forma realista fenómenos físicos complejos y escenas dinámicas. Cosmos-Predict2 admite varios métodos de generación, como texto a imagen (Text2Image) y video a mundo (Video2World), y se usa ampliamente en simulación industrial, conducción autónoma, planificación urbana, investigación científica y otros campos. GitHub:[Cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2) huggingface: [Cosmos-Predict2](https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959) Esta guía te acompañará paso a paso para completar el flujo de trabajo de **texto a imagen** en ComfyUI. Para la sección de generación de video, consulta la siguiente página:

## Generación de video con Cosmos Predict2

Usa Cosmos-Predict2 para generar video

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

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/cosmos/cosmos-predict2-t2i.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/cosmos/cosmos-predict2-t2i)

[Ming Image 0.1](https://docs.comfy.org/es/tutorials/image/ming-image/ming-image-0-1-design)[OmniGen2](https://docs.comfy.org/es/tutorials/image/omnigen/omnigen2)
