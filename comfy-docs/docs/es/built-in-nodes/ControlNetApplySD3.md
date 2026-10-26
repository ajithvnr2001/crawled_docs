---
url: https://docs.comfy.org/es/built-in-nodes/ControlNetApplySD3/
title: Aplicar controlnet con VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:41.503087+00:00
---

# Aplicar controlnet con VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ControlNetApplySD3/

Controlnet

# Aplicar controlnet con VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo aplica la guía de ControlNet al condicionamiento de Stable Diffusion 3.

Copiar páginaCopiar página

Este nodo aplica la guía de ControlNet al condicionamiento de Stable Diffusion 3. Toma entradas de condicionamiento positivo y negativo junto con un modelo ControlNet y una imagen, y luego aplica la guía de control con parámetros ajustables de fuerza y temporización para influir en el proceso de generación. **Nota:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`positivo`| El condicionamiento positivo al que se aplicará la guía de ControlNet| CONDITIONING| Sí| -  
`negativo`| El condicionamiento negativo al que se aplicará la guía de ControlNet| CONDITIONING| Sí| -  
`control_net`| El modelo ControlNet que se usará para la guía| CONTROL_NET| Sí| -  
`vae`| El modelo VAE utilizado en el proceso| VAE| Sí| -  
`imagen`| La imagen de entrada que ControlNet usará como guía| IMAGE| Sí| -  
`fuerza`| La fuerza del efecto de ControlNet (predeterminado: 1.0). Cuando se establece en 0.0, el nodo omite la aplicación de ControlNet y devuelve el condicionamiento sin cambios.| FLOAT| Sí| 0.0 - 10.0  
`porcentaje_inicio`| El punto de inicio en el proceso de generación donde ControlNet comienza a aplicarse (predeterminado: 0.0)| FLOAT| Sí| 0.0 - 1.0  
`porcentaje_final`| El punto final en el proceso de generación donde ControlNet deja de aplicarse (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 1.0  
  
**Nota:** Cuando `strength` se establece en 0.0, no se aplica la guía de ControlNet y el condicionamiento de entrada se transmite sin cambios a ambas salidas. **Nota:** Si el mismo condicionamiento se reutiliza en otro lugar y ya contiene información de control, el nuevo ControlNet se enlaza después del anterior, por lo que se pueden aplicar varios ControlNets en secuencia.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positivo`| El condicionamiento positivo modificado con la guía de ControlNet aplicada| CONDITIONING  
`negativo`| El condicionamiento negativo modificado con la guía de ControlNet aplicada| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/es.md)

* * *

**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ControlNetApplySD3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ControlNetApplySD3)

[Aplicar ControlNet](https://docs.comfy.org/es/built-in-nodes/ControlNetApplyAdvanced)[Aplicar ControlNet inpainting AliMama](https://docs.comfy.org/es/built-in-nodes/ControlNetInpaintingAliMamaApply)
