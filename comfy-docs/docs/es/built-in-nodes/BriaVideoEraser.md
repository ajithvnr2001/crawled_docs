---
url: https://docs.comfy.org/es/built-in-nodes/BriaVideoEraser/
title: Borrador de v\u00eddeo Bria - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:33.889434+00:00
---

# Borrador de vídeo Bria - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaVideoEraser/

Bria

# Borrador de vídeo Bria - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Borra con Bria todo lo que cubra una máscara por fotograma de un video y rellena el hueco.

Copiar páginaCopiar página

Borra con Bria todo lo que cubra una máscara por fotograma de un video y rellena el hueco. La máscara debe ser blanca en aquello que debe desaparecer y negra en el resto. Bria acepta clips de como máximo 5,1 segundos a 20-30 fotogramas por segundo con dimensiones de píxeles pares; el audio se conserva de forma predeterminada. El clip devuelto puede ser unos fotogramas más corto que la entrada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| Clip del que se va a borrar.| VIDEO| Sí| -  
`mask`| Una máscara por fotograma del video, blanca donde está el objeto que se debe borrar. Proporcione una máscara o un video de máscara, pero no ambos.| MASK| No| -  
`mask_video`| Un video de máscara ya codificado con las mismas dimensiones y el mismo número de fotogramas que el video. Proporcione una máscara o un video de máscara, pero no ambos.| VIDEO| No| -  
`preserve_audio`| Conserva la pista de audio de la entrada. Predeterminado: true.| BOOLEAN| No| `true`  
`false`  
  
**Notas sobre las restricciones:**

  * Debe conectarse exactamente uno de `mask` o `mask_video`. Se genera un error si no se proporciona ninguno de los dos, o si se proporcionan ambos.
  * El video debe durar como máximo 5,1 segundos y reproducirse a 20-30 fotogramas por segundo. Ajuste la temporización del clip con Get Video Components y Create Video si es necesario.
  * El video debe tener dimensiones de píxeles pares (ancho y alto divisibles entre 2). De lo contrario, recórtelo o escálalo primero.
  * Cuando se usa `mask`, debe contener un fotograma de máscara por cada fotograma del video, y su relación de aspecto debe coincidir con la del video. Las máscaras se binarizan al 50 %: las áreas pintadas con menos de la mitad de opacidad se ignoran, y una máscara vacía genera un error. Si la resolución de la máscara difiere de la del video, se redimensiona a las dimensiones del video.
  * Cuando se usa `mask_video`, debe tener las mismas dimensiones y el mismo número de fotogramas que el video.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El clip editado con las áreas enmascaradas borradas y los huecos rellenados. La salida puede ser unos fotogramas más corta que el clip de entrada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/es.md)

* * *

**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaVideoEraser.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaVideoEraser)

[Bria Eliminar Fondo de Video (Transparente)](https://docs.comfy.org/es/built-in-nodes/BriaTransparentVideoBackground)[Bria Video Green Screen](https://docs.comfy.org/es/built-in-nodes/BriaVideoGreenScreen)
