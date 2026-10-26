---
url: https://docs.comfy.org/es/built-in-nodes/TripoSplatSamplingPreview/
title: Vista Previa de Muestreo TripoSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.309487+00:00
---

# Vista Previa de Muestreo TripoSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TripoSplatSamplingPreview/

Triposplat

# Vista Previa de Muestreo TripoSplat - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo modifica un modelo TripoSplat para que, al usarlo con el nodo KSampler estándar

Copiar páginaCopiar página

Este nodo modifica un modelo TripoSplat para que, al usarlo con el nodo KSampler estándar, se muestre una vista previa en vivo del splat gaussiano decodificado en cada paso de muestreo. Funciona envolviendo la devolución de llamada del muestreador para decodificar la salida del modelo en una imagen de vista previa después de cada paso.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo TripoSplat que se modificará para la vista previa en vivo| MODEL| Sí|   
`vae`| Decodificador VAE de TripoSplat| VAE| Sí|   
`nivel_octree`| Profundidad del octree para la decodificación de la vista previa (menor = más barato/más grueso). Predeterminado: 5| INT| No| 2 a 8  
`número_de_gaussianos`| Número de gaussianos a generar para la vista previa (redondeado a un múltiplo de 32). Predeterminado: 16384| INT| No| 1024 a 262144 (paso: 32)  
`yaw`| Yaw de la cámara de vista previa en grados. Predeterminado: 90.0| FLOAT| No| -360.0 a 360.0 (paso: 1.0)  
`pitch`| Pitch de la cámara de vista previa en grados. Predeterminado: 15.0| FLOAT| No| -89.0 a 89.0 (paso: 1.0)  
`tamaño_de_punto`| Radio máximo del splat en píxeles. Cada gaussiano se dimensiona según su escala y se limita aquí; menor = más fino/puntiagudo, mayor = más grueso. Predeterminado: 3| INT| No| 1 a 16  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El modelo TripoSplat modificado con funcionalidad de vista previa en vivo añadida| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/es.md)

* * *

**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TripoSplatSamplingPreview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TripoSplatSamplingPreview)

[Decodificación de textura VAE de Trellis2](https://docs.comfy.org/es/built-in-nodes/VaeDecodeTextureTrellis)[Decodificar TripoSplat](https://docs.comfy.org/es/built-in-nodes/VAEDecodeTripoSplat)
