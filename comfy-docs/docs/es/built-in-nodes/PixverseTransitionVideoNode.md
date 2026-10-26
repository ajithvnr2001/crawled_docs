---
url: https://docs.comfy.org/es/built-in-nodes/PixverseTransitionVideoNode/
title: Video de transici\u00f3n PixVerse - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.102254+00:00
---

# Video de transición PixVerse - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PixverseTransitionVideoNode/

Pixverse

# Video de transición PixVerse - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video de transición entre dos imágenes de entrada mediante la API de PixVerse.

Copiar páginaCopiar página

Genera un video de transición entre dos imágenes de entrada mediante la API de PixVerse. Debe proporcionar una imagen inicial y una imagen final, y el nodo crea un video fluido que hace la transición de una a la otra, guiado por su prompt de texto y la configuración seleccionada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`primer fotograma`| La imagen inicial para la transición del video| IMAGE| Sí| -  
`último fotograma`| La imagen final para la transición del video| IMAGE| Sí| -  
`prompt`| Prompt para la generación del video (por defecto: cadena vacía)| STRING| Sí| -  
`calidad`| Configuración de calidad del video (por defecto: `"540p"`)| COMBO| Sí| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`duración en segundos`| Duración del video en segundos| COMBO| Sí| `5`  
`8`  
`modo de movimiento`| Estilo de movimiento para la transición (por defecto: `"normal"`)| COMBO| Sí| `"normal"`  
`"fast"`  
`semilla`| Semilla para la generación del video (por defecto: 0)| INT| Sí| 0 a 2147483647  
`prompt negativo`| Una descripción de texto opcional de elementos no deseados en una imagen (por defecto: cadena vacía)| STRING| No| -  
  
**Nota sobre las restricciones de los parámetros:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en `"normal"` y la duración se limita a 5 segundos. Para cualquier duración distinta de 5 segundos, el modo de movimiento también se establece automáticamente en `"normal"`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El video de transición generado| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `9774f15ae93377d4768cee9f51ce004a791ecaad3cadd0a2467d354c4dbc6f23`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PixverseTransitionVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PixverseTransitionVideoNode)

[PixVerse texto a video](https://docs.comfy.org/es/built-in-nodes/PixverseTextToVideoNode)[PixVerse V6 Extender vídeo](https://docs.comfy.org/es/built-in-nodes/PixverseV6ExtendVideoNode)
