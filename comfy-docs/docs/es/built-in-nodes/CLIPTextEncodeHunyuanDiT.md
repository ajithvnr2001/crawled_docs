---
url: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeHunyuanDiT/
title: Codificar texto CLIP para Hunyuan Image - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.008038+00:00
---

# Codificar texto CLIP para Hunyuan Image - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeHunyuanDiT/

Hunyuan Image

# Codificar texto CLIP para Hunyuan Image - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIPTextEncodeHunyuanDiT convierte descripciones de texto en un formato que el modelo HunyuanDiT puede entender.

Copiar páginaCopiar página

El nodo `CLIPTextEncodeHunyuanDiT` convierte descripciones de texto en un formato que el modelo HunyuanDiT puede entender. Es un nodo de condicionamiento avanzado diseñado para la arquitectura de doble codificador de texto de HunyuanDiT, que procesa dos entradas de texto separadas mediante diferentes tokenizadores y combina sus resultados en una única salida de condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`clip`| Una instancia del modelo CLIP utilizada para la tokenización y codificación de texto, que es fundamental para generar condicionamientos.| CLIP| Sí| -  
`bert`| Entrada de texto para codificar mediante el tokenizador BERT. Prefiere frases y palabras clave. Admite múltiples líneas y prompts dinámicos.| STRING| Sí| -  
`mt5xl`| Entrada de texto para codificar mediante el tokenizador mT5-XL. Admite múltiples líneas y prompts dinámicos (multilingües). Puede usar oraciones completas y descripciones complejas.| STRING| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`CONDITIONING`| La salida de condicionamiento codificada, que combina el texto tokenizado tanto por BERT como por mT5-XL, y se utiliza para el procesamiento posterior en tareas de generación.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/es.md)

* * *

**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPTextEncodeHunyuanDiT.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPTextEncodeHunyuanDiT)

[Acondicionamiento Hunyuan 3D v2 (multi-vista)](https://docs.comfy.org/es/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)[Hunyuan imagen a video](https://docs.comfy.org/es/built-in-nodes/HunyuanImageToVideo)
