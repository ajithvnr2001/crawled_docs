---
url: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Sketch/
title: Rodin 3D generar - generar boceto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.920816+00:00
---

# Rodin 3D generar - generar boceto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Sketch/

Rodin

# Rodin 3D generar - generar boceto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera activos 3D utilizando la API de Rodin.

Copiar páginaCopiar página

Este nodo genera activos 3D utilizando la API de Rodin. Toma imágenes de entrada y las convierte en modelos 3D a través de un servicio externo. El nodo gestiona todo el proceso, desde la creación de la tarea hasta la descarga de los archivos finales del modelo 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`Imágenes`| Imágenes de entrada que se convertirán en modelos 3D. Se pueden proporcionar múltiples imágenes.| IMAGE| Sí| -  
`Semilla`| Valor de semilla aleatoria para la generación (predeterminado: 0). Establecer en 0 para semilla aleatoria.| INT| No| 0-65535  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`Ruta del modelo 3D`| Ruta del archivo al modelo 3D generado (solo para compatibilidad hacia atrás)| STRING  
`GLB`| El modelo 3D generado en formato GLB| FILE3DGLB  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/es.md)

* * *

**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Rodin3D_Sketch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Rodin3D_Sketch)

[Rodin 3D generar - generar regular](https://docs.comfy.org/es/built-in-nodes/Rodin3D_Regular)[Rodin 3D generar - generar suavizado](https://docs.comfy.org/es/built-in-nodes/Rodin3D_Smooth)
