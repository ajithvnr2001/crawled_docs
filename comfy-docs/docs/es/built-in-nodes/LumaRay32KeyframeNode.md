---
url: https://docs.comfy.org/es/built-in-nodes/LumaRay32KeyframeNode/
title: Luma Ray 3.2 Fotograma Clave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:07.772520+00:00
---

# Luma Ray 3.2 Fotograma Clave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaRay32KeyframeNode/

Luma

# Luma Ray 3.2 Fotograma Clave - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo ancla una imagen guía a una posición específica en la línea de tiempo del video de salida de Luma Ray 3.2.

Copiar páginaCopiar página

Este nodo ancla una imagen guía a una posición específica en la línea de tiempo del video de salida de Luma Ray 3.2. Conecte este nodo a la entrada “keyframes” del nodo Luma Ray 3.2 Keyframes to Video, y encadene varios keyframes conectando la entrada opcional “keyframes”.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`image`| Imagen guía para colocar en el momento elegido del video de salida.| IMAGE| Sí| -  
`position`| Cómo colocar esta imagen en la línea de tiempo del video de salida.| DYNAMIC_COMBO| Sí| ”Fraction of duration (0.0-1.0)"  
"Absolute time (seconds)“  
`keyframes`| Keyframes anteriores opcionales para encadenar con este.| LUMA_RAY32_KEYFRAME| No| -  
  
### 

​

Entradas de Fraction of duration (0.0-1.0)

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`fraction`| Dónde se aplica esta imagen en el video de salida (0.0 = inicio, 1.0 = final). Predeterminado: 0.0.| FLOAT| Sí| 0.0 a 1.0 (paso: 0.01)  
  
### 

​

Entradas de Absolute time (seconds)

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`seconds`| Tiempo en segundos desde el inicio del video de salida donde se aplica esta imagen. Predeterminado: 0.0.| FLOAT| Sí| 0.0 a 10.0 (paso: 0.1)  
  
El parámetro `position` determina qué valor se usa para colocar la imagen en la línea de tiempo. Solo se muestra y se usa el subparámetro que pertenece a la opción seleccionada: `fraction` para “Fraction of duration (0.0-1.0)” y `seconds` para “Absolute time (seconds)”.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`keyframes`| Una cadena de keyframes que incluye el nuevo keyframe combinado con los keyframes anteriores opcionales.| LUMA_RAY32_KEYFRAME  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/es.md)

* * *

**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaRay32KeyframeNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaRay32KeyframeNode)

[Luma Ray 3.2 Imagen a Video](https://docs.comfy.org/es/built-in-nodes/LumaRay32ImageToVideoNode)[Luma Ray 3.2 Fotogramas clave a video](https://docs.comfy.org/es/built-in-nodes/LumaRay32KeyframesToVideoNode)
