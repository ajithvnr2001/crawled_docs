---
url: https://docs.comfy.org/es/built-in-nodes/LatentBlend/
title: Mezcla latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:02.874099+00:00
---

# Mezcla latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentBlend/

Experimental

# Mezcla latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentBlend combina dos muestras latentes mezclándolas mediante un factor de mezcla especificado.

Copiar páginaCopiar página

El nodo LatentBlend combina dos muestras latentes mezclándolas mediante un factor de mezcla especificado. Toma dos entradas latentes y crea una nueva salida donde la primera muestra se pondera por el factor de mezcla y la segunda muestra se pondera por el inverso. Si las muestras de entrada tienen formas diferentes, la segunda muestra se redimensiona automáticamente para coincidir con las dimensiones de la primera.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`muestras1`| La primera muestra latente a mezclar| LATENT| Sí| -  
`muestras2`| La segunda muestra latente a mezclar| LATENT| Sí| -  
`factor_de_mezcla`| Controla la proporción de mezcla entre las dos muestras (predeterminado: 0.5)| FLOAT| Sí| 0 a 1  
  
**Nota:** Si `samples1` y `samples2` tienen formas diferentes, `samples2` se redimensionará automáticamente para coincidir con las dimensiones de `samples1` mediante interpolación bicúbica con recorte centrado.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`latent`| La muestra latente mezclada que combina ambas muestras de entrada| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/es.md)

* * *

**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentBlend.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentBlend)

[FreSca](https://docs.comfy.org/es/built-in-nodes/FreSca)[Extraer y guardar LoRA](https://docs.comfy.org/es/built-in-nodes/LoraSave)
