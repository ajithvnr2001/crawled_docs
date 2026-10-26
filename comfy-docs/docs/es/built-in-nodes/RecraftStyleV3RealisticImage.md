---
url: https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3RealisticImage/
title: Recraft style - imagen realista - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:21.959776+00:00
---

# Recraft style - imagen realista - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3RealisticImage/

Recraft

# Recraft style - imagen realista - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea una configuración de estilo para generar imágenes realistas utilizando la API de Recraft.

Copiar páginaCopiar página

Este nodo crea una configuración de estilo para generar imágenes realistas utilizando la API de Recraft. Selecciona el estilo `realistic_image` y permite elegir un subestilo opcional para ajustar la apariencia del resultado.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`subestilo`| El subestilo específico a aplicar al estilo `realistic_image`. Si se establece en “None”, no se aplicará ningún subestilo.| STRING| Sí| Múltiples opciones disponibles (determinadas por la API de Recraft)  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`recraft_style`| Un objeto de configuración de estilo de Recraft que contiene el estilo `realistic_image` y la configuración del subestilo seleccionado. Esta salida se puede conectar a otros nodos de Recraft que acepten una entrada de estilo.| STYLEV3  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/es.md)

* * *

**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecraftStyleV3RealisticImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecraftStyleV3RealisticImage)

[Estilo Recraft - logo ráster](https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3LogoRaster)[Recraft Texto a Imagen](https://docs.comfy.org/es/built-in-nodes/RecraftTextToImageNode)
