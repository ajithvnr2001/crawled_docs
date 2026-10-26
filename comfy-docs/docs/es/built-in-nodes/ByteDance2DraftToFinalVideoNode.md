---
url: https://docs.comfy.org/es/built-in-nodes/ByteDance2DraftToFinalVideoNode/
title: ByteDance Seedance 2.5 Borrador a v\u00eddeo final - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:34.264539+00:00
---

# ByteDance Seedance 2.5 Borrador a vídeo final - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ByteDance2DraftToFinalVideoNode/

Bytedance

# ByteDance Seedance 2.5 Borrador a vídeo final - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo renderiza el video final en 1080p de un borrador de Seedance 2.5.

Copiar páginaCopiar página

Este nodo renderiza el video final en 1080p de un borrador de Seedance 2.5. Un borrador es una vista previa rápida en 480p: en un nodo de video de Seedance 2.5 (texto a video, primer y último fotograma a video o referencia a video), establece `model` en `Seedance 2.5 Draft`, ejecútalo y conecta su salida `draft_task_id` aquí. El video final conserva la escena y el movimiento del borrador, y reutiliza el prompt, las referencias, la duración, la relación de aspecto y la configuración de audio que produjeron el borrador.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`draft_task_id`| La salida `draft_task_id` de un nodo Seedance 2.5 ejecutado con el modelo Seedance 2.5 Draft, o un ID de tarea de borrador pegado. Cuando vuelvas a ejecutar el nodo productor, establece su control de semilla en fijo; de lo contrario, la siguiente ejecución generará un nuevo borrador en lugar de reutilizar el que revisaste.| STRING| Sí| -  
`marca de agua`| Indica si se debe agregar una marca de agua al video. El valor predeterminado es False. Esta es una configuración avanzada.| BOOLEAN| No| True / False  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video final renderizado en 1080p, descargado del proveedor una vez que se completa la tarea de renderizado.| VIDEO  
  
**Nota:** Un borrador se puede renderizar durante 7 días después de su creación. El ID de tarea del borrador identifica al borrador por sí solo, por lo que el prompt, las referencias, la duración, la relación de aspecto y la configuración de audio no necesitan pasarse de nuevo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ByteDance2DraftToFinalVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ByteDance2DraftToFinalVideoNode)

[Bria Video Reemplazar Fondo](https://docs.comfy.org/es/built-in-nodes/BriaVideoReplaceBackground)[ByteDance Seedance 2.0 Primer-Último Fotograma a Video](https://docs.comfy.org/es/built-in-nodes/ByteDance2FirstLastFrameNode)
