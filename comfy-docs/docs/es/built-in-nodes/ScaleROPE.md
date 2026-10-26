---
url: https://docs.comfy.org/es/built-in-nodes/ScaleROPE/
title: Escalar ROPE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.079833+00:00
---

# Escalar ROPE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ScaleROPE/

Parches

# Escalar ROPE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ScaleROPE le permite modificar la codificación posicional rotatoria (ROPE) de un modelo aplicando factores de escala y desplazamiento separados a sus

Copiar páginaCopiar página

El nodo ScaleROPE le permite modificar la codificación posicional rotatoria (ROPE) de un modelo aplicando factores de escala y desplazamiento separados a sus componentes X, Y y T (tiempo). Es un nodo avanzado y experimental que se utiliza para ajustar el comportamiento de codificación posicional del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo cuyos parámetros ROPE serán modificados.| MODEL| Sí| -  
`escala_x`| El factor de escala que se aplicará al componente X del ROPE (por defecto: 1.0).| FLOAT| Sí| 0.0 - 100.0 (step 0.1)  
`desplazamiento_x`| El valor de desplazamiento que se aplicará al componente X del ROPE (por defecto: 0.0).| FLOAT| Sí| -256.0 - 256.0 (step 0.1)  
`escala_y`| El factor de escala que se aplicará al componente Y del ROPE (por defecto: 1.0).| FLOAT| Sí| 0.0 - 100.0 (step 0.1)  
`desplazamiento_y`| El valor de desplazamiento que se aplicará al componente Y del ROPE (por defecto: 0.0).| FLOAT| Sí| -256.0 - 256.0 (step 0.1)  
`escala_t`| El factor de escala que se aplicará al componente T (tiempo) del ROPE (por defecto: 1.0).| FLOAT| Sí| 0.0 - 100.0 (step 0.1)  
`desplazamiento_t`| El valor de desplazamiento que se aplicará al componente T (tiempo) del ROPE (por defecto: 0.0).| FLOAT| Sí| -256.0 - 256.0 (step 0.1)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo con los nuevos parámetros de escala y desplazamiento ROPE aplicados.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/es.md)

* * *

**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ScaleROPE.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ScaleROPE)

[Reescalar CFG](https://docs.comfy.org/es/built-in-nodes/RescaleCFG)[Aplicar Fun ControlNet](https://docs.comfy.org/es/built-in-nodes/ZImageFunControlnet)
