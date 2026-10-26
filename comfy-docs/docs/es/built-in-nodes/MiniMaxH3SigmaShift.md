---
url: https://docs.comfy.org/es/built-in-nodes/MiniMaxH3SigmaShift/
title: MiniMax H3 Sigma Shift - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:11.366258+00:00
---

# MiniMax H3 Sigma Shift - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MiniMaxH3SigmaShift/

Minimax

# MiniMax H3 Sigma Shift - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Establece los valores de desplazamiento de flujo de video y audio para un modelo MiniMax H3.

Copiar páginaCopiar página

Establece los valores de desplazamiento de flujo de video y audio para un modelo MiniMax H3. El desplazamiento de video controla el programa de sigma del muestreador, y ambos valores de desplazamiento se pasan al transformador interno del modelo, que los utiliza para derivar el programa de audio a partir de la cuadrícula base compartida.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se le aplica el parche de desplazamiento de sigma. El nodo clona el modelo, por lo que el original permanece sin cambios.| MODEL| Sí| -  
`desplazamiento de video`| El valor de desplazamiento de flujo de video. Controla el programa de sigma del muestreador. Valor por defecto: 12.0.| FLOAT| Sí| 0.01 a 100.0  
`desplazamiento de audio`| El valor de desplazamiento de flujo de audio. El modelo lo utiliza para derivar el programa de audio. Valor por defecto: 3.0.| FLOAT| Sí| 0.01 a 100.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`MODEL`| El modelo clonado con los ajustes de desplazamiento de sigma de video y audio aplicados.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/es.md)

* * *

**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MiniMaxH3SigmaShift.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MiniMaxH3SigmaShift)

[Aplicar MiniMax H3 Fun ControlNet](https://docs.comfy.org/es/built-in-nodes/MiniMaxH3FunControlNetApply)[Aplicar ControlNet DiffSynth para Qwen Image](https://docs.comfy.org/es/built-in-nodes/QwenImageDiffsynthControlnet)
