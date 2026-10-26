---
url: https://docs.comfy.org/es/built-in-nodes/WanAnimate2Cache/
title: WanAnimate2Cache - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:45.173967+00:00
---

# WanAnimate2Cache - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanAnimate2Cache/

Animar

# WanAnimate2Cache - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Cachea una sola vez las activaciones por bloque del video de pose para que no haya que recalcularlas en cada paso de muestreo, lo que reduce el tiempo de generación a la mitad aproximadamente.

Copiar páginaCopiar página

Caches the pose-video’s per-block activations once so they do not need to be recomputed on every sampling step, which roughly halves generation time. The tradeoff is extra memory usage: about 12.5 GB of system RAM at 480x832 resolution with 81 frames in bf16, scaling with resolution and video length.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo Wan Animate2 al que se le adjunta la caché.| MODEL| Sí|   
`dispositivo`| Dónde mantener la caché. cpu (RAM) es la opción segura; la caché no cabe en VRAM junto con el modelo en tamaños típicos. gpu (VRAM) puede ser más rápida si cabe. (predeterminado: “cpu”)| STRING| Sí| ”cpu"  
"gpu”  
`tipo de dato`| Precisión de almacenamiento. default almacena las activaciones en el dtype de cómputo del modelo. int8 reduce la caché a la mitad, int4 a la cuarta parte, convrot se usa para mantener la precisión. (predeterminado: “default”)| STRING| Sí| ”default"  
"int8"  
"int4”  
  
Nota: Cuando se usan ventanas de contexto, cada ventana se almacena en caché por separado, por lo que el uso de memoria escala con el número de ventanas. Se debe usar el programa static_standard, porque los programas uniformes desplazan las ventanas en cada paso y la caché nunca se reutiliza.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo clonado con la caché de activaciones del pose-video adjunta. La caché se libera automáticamente cuando la generación finaliza.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/es.md)

* * *

**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanAnimate2Cache.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanAnimate2Cache)

[VOIDInpaintConditioning](https://docs.comfy.org/es/built-in-nodes/VOIDInpaintConditioning)[WanAnimate2ToVideo](https://docs.comfy.org/es/built-in-nodes/WanAnimate2ToVideo)
