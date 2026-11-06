---
url: https://docs.comfy.org/es/built-in-nodes/VSRDecode/
title: VSRDecode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:54.684372+00:00
---

# VSRDecode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VSRDecode/

Latente

# VSRDecode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

VSR Decode convierte los latentes de fotograma clave de RelayVSR Conditioning de nuevo en un vídeo completo con el decodificador RelayVSR Flash.

Copiar páginaCopiar página

VSR Decode convierte los latentes de fotograma clave de RelayVSR Conditioning de nuevo en un vídeo completo con el decodificador RelayVSR Flash. El decodificador añade su detalle sobre un escalado bicúbico de los fotogramas de baja calidad que se le pasan, con el factor x2 o x4 del decodificador. El número de fotogramas permanece igual.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`vae`| El decodificador RelayVSR Flash, cargado con Load VAE: `relayvsr_flash_vae_x2_fp32.safetensors` o `relayvsr_flash_vae_x4_fp32.safetensors`. Los metadatos del archivo establecen el factor de escalado, por lo que debe coincidir con el modelo.| VAE| Sí| N/A  
`samples`| El latente devuelto por el muestreador, que contiene un fotograma por cada fotograma clave.| LATENT| Sí| N/A  
`images`| El mismo vídeo de baja calidad que se proporcionó a RelayVSR Conditioning.| IMAGE| Sí| N/A  
`detail`| Cuánto detalle del decodificador se conserva sobre el escalado bicúbico: 1 es la salida completa del modelo, 0 es el escalado simple. (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 1.0 (paso 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`images`| El vídeo escalado con cada fotograma restaurado.| IMAGE  
  
## 

​

Notas

  * Pase el mismo vídeo de baja calidad a ambos nodos. El decodificador lo lee fotograma a fotograma, por lo que una discrepancia en la longitud o la resolución produce un resultado incorrecto o roto.
  * Reducir `detail` suaviza el detalle restaurado y mantiene la salida más cerca de un escalado bicúbico simple, lo que puede ayudar con fuentes muy ruidosas.



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/es.md)

* * *

**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VSRDecode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VSRDecode)

[Obtener tamaño del latent de imagen/vídeo](https://docs.comfy.org/es/built-in-nodes/GetLatentSize)[Cargar modelo ControlNet](https://docs.comfy.org/es/built-in-nodes/ControlNetLoader)
