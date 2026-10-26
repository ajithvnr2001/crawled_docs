---
url: https://docs.comfy.org/es/built-in-nodes/WavespeedFlashVSRNode/
title: FlashVSR escalado de video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:47.362269+00:00
---

# FlashVSR escalado de video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WavespeedFlashVSRNode/

Wavespeed

# FlashVSR escalado de video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WavespeedFlashVSRNode es un escalador de video rápido y de alta calidad que aumenta la resolución y restaura la claridad de material de video de baja

Copiar páginaCopiar página

El nodo WavespeedFlashVSRNode es un escalador de video rápido y de alta calidad que aumenta la resolución y restaura la claridad de material de video de baja resolución o borroso. Procesa una entrada de video y genera un nuevo video a una resolución superior seleccionada por el usuario.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`video`| El archivo de video de entrada que se va a escalar. Debe estar en formato contenedor MP4 con una duración entre 5 segundos y 10 minutos.| VIDEO| Sí| N/A  
`resolución_objetivo`| La resolución deseada para el video de salida escalado.| STRING| Sí| `"720p"`  
`"1080p"`  
`"2K"`  
`"4K"`  
  
**Restricciones de entrada:**

  * El archivo de `video` de entrada debe estar en formato contenedor MP4.
  * La duración del `video` de entrada debe estar entre 5 segundos y 10 minutos (600 segundos).



## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El archivo de video escalado a la resolución objetivo seleccionada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/es.md)

* * *

**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WavespeedFlashVSRNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WavespeedFlashVSRNode)

[Wan texto a vídeo](https://docs.comfy.org/es/built-in-nodes/WanTextToVideoApi)[Mejora de escala de vídeo Crystal de Clarity AI](https://docs.comfy.org/es/built-in-nodes/ClarityCrystalVideoUpscaleNode)
