---
url: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeKandinsky5/
title: Codificar texto CLIP para Kandinsky 5 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.870643+00:00
---

# Codificar texto CLIP para Kandinsky 5 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeKandinsky5/

Kandinsky

# Codificar texto CLIP para Kandinsky 5 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIP Text Encode (Kandinsky 5) prepara prompts de texto para usarlos con el modelo Kandinsky 5.

Copiar páginaCopiar página

El nodo CLIP Text Encode (Kandinsky 5) prepara prompts de texto para usarlos con el modelo Kandinsky 5. Toma dos entradas de texto separadas, las tokeniza con un modelo CLIP proporcionado y las combina en una única salida de condicionamiento que guía el proceso de generación de imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para tokenizar y codificar los prompts de texto.| CLIP| Sí|   
`clip_l`| El prompt de texto principal. Esta entrada admite texto multilínea y prompts dinámicos.| STRING| Sí|   
`qwen25_7b`| El prompt de texto secundario. Esta entrada admite texto multilínea y prompts dinámicos.| STRING| Sí|   
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento combinados generados a partir de ambos prompts de texto, listos para alimentar un modelo Kandinsky 5 para la generación de imágenes.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/es.md)

* * *

**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPTextEncodeKandinsky5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPTextEncodeKandinsky5)

[TextEncodeJoyImageEdit](https://docs.comfy.org/es/built-in-nodes/TextEncodeJoyImageEdit)[Kandinsky 5 imagen a video](https://docs.comfy.org/es/built-in-nodes/Kandinsky5ImageToVideo)
