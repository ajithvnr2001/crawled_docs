---
url: https://docs.comfy.org/es/built-in-nodes/ViduStartEndToVideoNode/
title: Generaci\u00f3n de video Vidu de inicio a fin - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.672868+00:00
---

# Generación de video Vidu de inicio a fin - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ViduStartEndToVideoNode/

Vidu

# Generación de video Vidu de inicio a fin - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento: El nodo Vidu Start End To Video Generation crea un video generando fotogramas entre un fotograma inicial y un fotograma final. Utiliza un prompt de texto para guiar el proceso de generación del video y admite varios modelos de video con diferentes configuraciones de resolución y movimiento. El nodo valida que los fotogramas inicial y final tengan relaciones de aspecto compatibles antes de procesarlos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| Nombre del modelo| COMBO| Sí| `"viduq1"`  
`primer_cuadro`| Fotograma inicial| IMAGE| Sí| -  
`cuadro_final`| Fotograma final| IMAGE| Sí| -  
`prompt`| Una descripción textual para la generación del video| STRING| No| -  
`duración`| Duración del video de salida en segundos (predeterminado: 5, fijo en 5 segundos)| INT| No| 5-5  
`semilla`| Semilla para la generación del video (0 para aleatorio) (predeterminado: 0)| INT| No| 0-2147483647  
`resolución`| Los valores admitidos pueden variar según el modelo y la duración (predeterminado: “1080p”)| COMBO| No| `"1080p"`  
`amplitud_de_movimiento`| La amplitud de movimiento de los objetos en el fotograma (predeterminado: “auto”)| COMBO| No| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Nota:** Los fotogramas inicial y final deben tener relaciones de aspecto compatibles (validadas con una tolerancia de relación min_rel=0.8, max_rel=1.25).

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El archivo de video generado| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ViduStartEndToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ViduStartEndToVideoNode)

[Generación de video a partir de referencia Vidu](https://docs.comfy.org/es/built-in-nodes/ViduReferenceVideoNode)[Generación de video Vidu de texto a video](https://docs.comfy.org/es/built-in-nodes/ViduTextToVideoNode)
