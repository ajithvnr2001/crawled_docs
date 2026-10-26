---
url: https://docs.comfy.org/es/built-in-nodes/HyperTile/
title: HyperTile - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:54.336238+00:00
---

# HyperTile - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HyperTile/

Unet

# HyperTile - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

HyperTile aplica una técnica de teselado al mecanismo de atención dentro de los modelos de difusión para reducir el uso de memoria durante la generación de

Copiar páginaCopiar página

HyperTile aplica una técnica de teselado al mecanismo de atención dentro de los modelos de difusión para reducir el uso de memoria durante la generación de imágenes. Divide el espacio latente en mosaicos más pequeños, procesa la atención de cada mosaico por separado y luego reensambla los resultados. Esto permite trabajar con tamaños de imagen más grandes sin quedarse sin memoria.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión al que se le aplicará la optimización HyperTile| MODEL| Sí| -  
`tamaño_de_mosaico`| El tamaño de mosaico objetivo para el procesamiento (predeterminado: 256). Internamente, el valor se limita a un mínimo de 32 y luego se divide por 8 para obtener el tamaño de mosaico efectivo.| INT| Sí| 1 - 2048  
`tamaño_de_intercambio`| Controla cómo se reorganizan los mosaicos durante el procesamiento para mejorar la eficiencia. Los valores más grandes permiten una mayor variación en los tamaños de los mosaicos (predeterminado: 2)| INT| Sí| 1 - 128  
`profundidad_máxima`| El nivel de profundidad máximo (escala de resolución) para aplicar el teselado. Un valor de 0 aplica el teselado solo en la resolución más alta (predeterminado: 0)| INT| Sí| 0 - 10  
`escala_de_profundidad`| Cuando está habilitado, el tamaño del mosaico se escala proporcionalmente en niveles de profundidad mayores. Esto puede ayudar a mantener la calidad en resoluciones más bajas (predeterminado: False)| BOOLEAN| Sí| True / False  
  
Nota: `tile_size`, `swap_size`, `max_depth` y `scale_depth` están marcados como entradas avanzadas, por lo que solo se muestran cuando las opciones avanzadas están habilitadas en la interfaz.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con la optimización HyperTile aplicada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/es.md)

* * *

**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HyperTile.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HyperTile)

[FreeU V2](https://docs.comfy.org/es/built-in-nodes/FreeU_V2)[Reducir modelo (Kohya Deep Shrink)](https://docs.comfy.org/es/built-in-nodes/PatchModelAddDownscale)
