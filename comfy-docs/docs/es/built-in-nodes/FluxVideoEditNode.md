---
url: https://docs.comfy.org/es/built-in-nodes/FluxVideoEditNode/
title: Edici\u00f3n de v\u00eddeo Flux - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.191517+00:00
---

# Edición de vídeo Flux - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxVideoEditNode/

BFL

# Edición de vídeo Flux - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Edita un clip de video existente a partir de una instrucción escrita.

Copiar páginaCopiar página

Edita un clip de video existente a partir de una instrucción escrita. Puedes eliminar, agregar o reemplazar objetos, cambiar el escenario, cambiar el estilo del material, cambiar el texto en pantalla o reemplazar el diálogo hablado. La duración, el encuadre, el movimiento de cámara y el audio provienen del clip de origen, por lo que todo lo que no menciones en el prompt debe permanecer como estaba.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| Clip de origen de 0.7 a 15 segundos, de al menos 160x160 píxeles. La salida se renderiza a 24 fps y se limita a aproximadamente 0.9 megapíxeles por fotograma, por lo que una fuente más grande se devuelve más pequeña.| VIDEO| Sí| 0.7 a 15 segundos; mínimo 160x160 píxeles  
`prompt`| Qué cambiar, en lenguaje sencillo, hasta 4096 caracteres. Todo lo que no menciones debe permanecer como estaba. El diálogo de reemplazo debe ajustarse al tiempo que dura el habla original, y un clip silencioso permanece silencioso. Predeterminado: cadena vacía.| STRING| Sí| 1 a 4096 caracteres  
`auto_downscale`| Reduce automáticamente la escala de las fuentes con un área superior a 1280x704 píxeles antes de la carga. Se conserva la relación de aspecto; los videos más pequeños no se modifican. Predeterminado: true.| BOOLEAN| No| true  
false  
`safety_tolerance`| Tolerancia de moderación; 0 es la más estricta. Predeterminado: 4.| INT| No| 0 a 4  
`seed`| Semilla para determinar si el nodo debe volver a ejecutarse; FLUX elige su propia semilla, por lo que los resultados reales no son deterministas independientemente de este valor. Predeterminado: 42.| INT| No| 0 a 4294967295  
  
**Nota:** El `prompt` debe contener al menos 1 carácter y no más de 4096 caracteres. El `video` de origen debe durar entre 0.7 y 15 segundos y tener al menos 160x160 píxeles; las cargas que queden fuera de estos límites se rechazan antes de enviar la solicitud.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El clip de video editado devuelto por el servicio FLUX.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/es.md)

* * *

**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxVideoEditNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxVideoEditNode)

[Flux 3 Continuación de Video](https://docs.comfy.org/es/built-in-nodes/Flux3VideoContinuationNode)[Ampliación de vídeo Flux](https://docs.comfy.org/es/built-in-nodes/FluxVideoUpscaleNode)
