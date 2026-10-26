---
url: https://docs.comfy.org/es/built-in-nodes/HiggsfieldMotionTransferNode/
title: Transferencia de movimiento Higgsfield Genjutsu - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.316256+00:00
---

# Transferencia de movimiento Higgsfield Genjutsu - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HiggsfieldMotionTransferNode/

Higgsfield

# Transferencia de movimiento Higgsfield Genjutsu - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Higgsfield Genjutsu Motion Transfer recrea un video con nuevos personajes

Copiar páginaCopiar página

El nodo **Higgsfield Genjutsu Motion Transfer** recrea un video con nuevos personajes, ubicaciones o estilos tomados de imágenes de referencia mientras conserva el movimiento, el movimiento de cámara, la sincronización y el audio del clip de origen. Conecta el clip que se va a reestilizar y una o más imágenes de referencia que describan el nuevo aspecto; luego describe el resultado en el prompt. La solicitud se envía a la API de Higgsfield y se devuelve el video generado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo que se va a usar. Al seleccionar un modelo se revelan los parámetros específicos de este: `video`, `reference_images`, `prompt`, `resolution` y `seed`.| DYNAMIC_COMBO| Sí| `"genjutsu-v1.0"`  
`video`| Video de origen cuyo movimiento, movimiento de cámara, sincronización y audio se conservan. Al menos 4 segundos; solo se usan los primeros 30 segundos.| VIDEO| Sí| 4 a 30 segundos  
`reference_images`| Ranura ampliable: conecta de 1 a 8 imágenes (`image_1`, `image_2`, …) de los personajes, ubicaciones o estilos que se van a usar. Una entrada por lotes cuenta una vez por imagen.| IMAGE| Sí| 1 a 8 imágenes  
`prompt`| Opcional. Describe el resultado, por ejemplo, qué referencia reemplaza a qué persona, o un nuevo entorno. (predeterminado: vacío)| STRING| Sí| Cualquier texto  
`resolution`| Resolución del video de salida. (predeterminado: `"720p"`)| COMBO| Sí| `"480p"`  
`"720p"`  
`"1080p"`  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Este parámetro tiene funcionalidad de «control después de generar» (predeterminado: 42).| INT| Sí| 0 a 2147483647  
  
El video de origen se valida antes de enviar la solicitud: un clip de menos de 4 segundos se rechaza, y un clip de más de 30 segundos se recorta a sus primeros 30 segundos. Su audio se transfiere al resultado. Las imágenes de referencia se suben primero, y el número total de imágenes en todas las ranuras conectadas no puede superar las 8, aunque el nodo expone ocho ranuras. La moderación de contenido de Higgsfield puede rechazar la entrada o el resultado, lo que genera un error en lugar de devolver un video.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El archivo de video reestilizado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/es.md)

* * *

**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HiggsfieldMotionTransferNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HiggsfieldMotionTransferNode)

[HeyGen Video Translate](https://docs.comfy.org/es/built-in-nodes/HeyGenVideoTranslateNode)[HitPaw mejora de vídeo](https://docs.comfy.org/es/built-in-nodes/HitPawVideoEnhance)
