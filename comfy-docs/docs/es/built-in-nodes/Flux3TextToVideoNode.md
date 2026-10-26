---
url: https://docs.comfy.org/es/built-in-nodes/Flux3TextToVideoNode/
title: Flux 3 Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:47.874289+00:00
---

# Flux 3 Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Flux3TextToVideoNode/

BFL

# Flux 3 Texto a Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video con audio sincronizado a partir de un prompt de texto usando FLUX 3.

Copiar páginaCopiar página

Genera un video con audio sincronizado a partir de un prompt de texto usando FLUX 3. El nodo envía tu prompt al servicio FLUX 3, espera a que finalice la generación y devuelve el clip de video completado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Lo que deseas, en lenguaje natural; el prompt se interpreta y se expande antes de la generación. Describe el sonido ambiental, la música y la voz por separado para obtener audio en capas. (predeterminado: "")| STRING| Sí| Texto multilínea  
`aspect_ratio`| Relación de aspecto de salida. ‘auto’ elige una a partir del prompt y las entradas. (predeterminado: “auto”)| COMBO| Sí| Múltiples opciones disponibles, incluida `"auto"`  
`duration`| Duración del clip en segundos. ‘auto’ ajusta la duración al contenido. (predeterminado: “auto”)| COMBO| Sí| Múltiples opciones disponibles, incluida `"auto"`  
`resolution`| Resolución de salida. (predeterminado: “720p”)| COMBO| Sí| `"720p"`  
`"1080p"`  
`"1440p"`  
`"2160p"`  
`generate_audio`| Genera audio sincronizado (ambiental, voz, efectos). Desactivado produce un video sin pista de audio. (predeterminado: True)| BOOLEAN| Sí| True  
False  
`safety_tolerance`| Tolerancia de moderación; 0 es la más estricta. Las solicitudes que envían imágenes o video están limitadas a 2, sin importar lo que configures aquí. (predeterminado: 2)| INT| Sí| 0 a 4  
`seed`| Semilla para determinar si el nodo debe volver a ejecutarse; FLUX 3 elige su propia semilla, por lo que los resultados reales no son deterministas independientemente de este valor. (predeterminado: 42)| INT| Sí| 0 a 4294967295  
  
Nota: `safety_tolerance` es una entrada avanzada. La entrada `seed` incluye controles Control After Generate en la interfaz. El precio mostrado se basa en `resolution` y `duration`: HD (720p) se cobra a $0.2431 por segundo y FHD (1080p) a $0.4147 por segundo. QHD (1440p) a $0.572 por segundo y UHD (2160p) a $1.144 por segundo. Cuando se elige una duración fija, se muestra el costo total estimado del clip; cuando `duration` es “auto”, se muestra la tarifa por segundo.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El clip de video generado, con audio sincronizado cuando `generate_audio` está habilitado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `2fa8c715c8467e2a2a3e131875d3b459a5599c2bab550656670aa1461e896aab`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Flux3TextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Flux3TextToVideoNode)

[Flux 3 Imagen a Video](https://docs.comfy.org/es/built-in-nodes/Flux3ImageToVideoNode)[Flux 3 Continuación de Video](https://docs.comfy.org/es/built-in-nodes/Flux3VideoContinuationNode)
