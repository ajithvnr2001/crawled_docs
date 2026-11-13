---
url: https://docs.comfy.org/es/tutorials/utility/relayvsr/
title: RelayVSR: ampliaci\u00f3n de video 2x y 4x en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:12.575110+00:00
---

# RelayVSR: ampliación de video 2x y 4x en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/relayvsr/

## En esta página

Volver arriba

  * Modelos
  * Upscale de video: RelayVSR 2x



Upscale & Restore

# RelayVSR: ampliación de video 2x y 4x en ComfyUI

Copiar páginaCopiar página

Amplía tu video 2x o 4x en ComfyUI con RelayVSR, un modelo Wan2.2 de un paso que restaura fotogramas clave y completa cada fotograma con un decodificador Flash.

Copiar páginaCopiar página

RelayVSR escala metraje real en una sola pasada. Un modelo Wan2.2 5B de un paso escribe latentes de referencia cada 15 cuadros, y un decodificador Flash pequeño rellena los cuadros intermedios a partir de esos latentes y del clip original de baja calidad. El soporte de ComfyUI llegó en [ComfyUI #17511](https://github.com/Comfy-Org/ComfyUI/pull/17511). La frecuencia de cuadros y el audio pasan sin modificaciones, así que solo se reescala la imagen. El factor de escala proviene del checkpoint, no de un widget: un modelo 2x solo funciona con el VAE 2x, y mezclar pares falla.

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

## Modelos

Descarga el par correspondiente a la escala que quieras y coloca cada archivo en la carpeta que se indica en su tarjeta.

## Modelo de difusión (2x)

relayvsr_x2_lightx2v_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## VAE (2x)

relayvsr_flash_vae_x2_fp32.safetensors → ComfyUI/models/vae/

## Modelo de difusión (4x)

relayvsr_x4_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## VAE (4x)

relayvsr_flash_vae_x4_fp32.safetensors → ComfyUI/models/vae/

[LightX2V](https://huggingface.co/lightx2v/RelayVSR_X2) reentrenó el par 2x para la etapa posterior a la generación de video, así que un clip de 768 x 1344 de MiniMax-H3 sale a 1536 x 2688. El par 4x es la escala original de RelayVSR.

## Upscale de video: RelayVSR 2x

Aplica upscale 2x a un clip con el flujo de trabajo de abajo. El upscaler se ejecuta dentro de un subgrafo, así que el lienzo solo muestra el video que entra y el que sale. ![Vista previa del flujo de trabajo de upscale de video RelayVSR 2x](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_relayvsr_video_x2_upscale-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “RelayVSR 2x” en la Biblioteca de plantillas

**Materiales de entrada**

## utility_relayvsr_video_x2_upscale_input.mp4

`LoadVideo` · `utility_relayvsr_video_x2_upscale_input.mp4`

  1. Carga tu clip en el nodo `Load Video`. La plantilla lo recorta a los primeros 5 segundos con un nodo `Trim Video`, así que aumenta esa duración para clips más largos o aplica upscale a material extenso en varias pasadas.
  2. Ejecuta el flujo de trabajo. `Save Video` guarda el resultado en `ComfyUI/output/video/`.

Para 4x, intercambia los dos valores de los cargadores en el subgrafo: `UNETLoader` por `relayvsr_x4_int8_convrot.safetensors` y `VAELoader` por `relayvsr_flash_vae_x4_fp32.safetensors`. No cambia nada más. Si una pasada se queda sin memoria, recorta el clip y aplícale upscale en varias pasadas.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/relayvsr.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/relayvsr)

[SeedVR2](https://docs.comfy.org/es/tutorials/utility/seedvr2)[Segmentación con SAM 3.1](https://docs.comfy.org/es/tutorials/utility/video-segment-sam3)
