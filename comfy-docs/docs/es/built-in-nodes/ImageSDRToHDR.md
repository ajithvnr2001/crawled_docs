---
url: https://docs.comfy.org/es/built-in-nodes/ImageSDRToHDR/
title: Convertir SDR a HDR - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.245641+00:00
---

# Convertir SDR a HDR - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageSDRToHDR/

Color

# Convertir SDR a HDR - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Convert SDR to HDR expande imágenes sRGB de rango dinámico estándar a HDR Rec.2020 HLG.

Copiar páginaCopiar página

El nodo **Convert SDR to HDR** expande imágenes sRGB de rango dinámico estándar a HDR Rec.2020 HLG. Conserva el aspecto existente de la imagen y mapea su brillo a un rango más amplio, por lo que el resultado debe guardarse con un espacio de color HDR seleccionado. El canal alfa se conserva sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| La(s) imagen(es) SDR en sRGB que se expandirán a HDR.| IMAGE| Sí| -  
`algorithm`| Algoritmo de expansión HDR. Al seleccionar un algoritmo, se muestran sus parámetros (`target_luminance`).| DYNAMIC_COMBO| Sí| `"lottes"`  
  
### 

​

Entradas de lottes

Estos parámetros aparecen cuando `algorithm` se establece en `"lottes"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`target_luminance`| Objetivo de blanco máximo en nits. 0 mantiene el renderizado calibrado. Las imágenes oscuras no se normalizan a este máximo. (predeterminado: 650.0)| FLOAT| Sí| 0.0 a 10000.0 (paso 1.0)  
  
Cada imagen del lote se convierte por separado: la codificación sRGB se invierte a luz lineal, el brillo se expande con una curva racional estilo Lottes combinada con una curva de ganancia logarítmica monótona calibrada, y el resultado se recodifica como Rec.2020 HLG. Como la salida es HDR, el nodo de guardado debe usar el espacio de color `HDR`; guardarla como sRGB renderiza el brillo incorrectamente. HLG asume una pantalla de referencia de 1000 nits, por lo que los valores de `target_luminance` inferiores a 1000 conservan esa referencia y un valor de `0` deja el renderizado calibrado intacto. Las imágenes de un solo canal se expanden a tres canales antes de la conversión, y el canal alfa se copia sin cambios.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La(s) imagen(es) HDR Rec.2020 HLG.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/es.md)

* * *

**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageSDRToHDR.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageSDRToHDR)

[Imagen RGB a YUV](https://docs.comfy.org/es/built-in-nodes/ImageRGBToYUV)[Imagen YUV a RGB](https://docs.comfy.org/es/built-in-nodes/ImageYUVToRGB)
