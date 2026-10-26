---
url: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Smooth/
title: Rodin 3D generar - generar suavizado - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:25.042078+00:00
---

# Rodin 3D generar - generar suavizado - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Smooth/

Rodin

# Rodin 3D generar - generar suavizado - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Rodin 3D Smooth genera activos 3D utilizando la API de Rodin, procesando imágenes de entrada y convirtiéndolas en modelos 3D suaves.

Copiar páginaCopiar página

El nodo **Rodin 3D Smooth** genera activos 3D utilizando la API de Rodin, procesando imágenes de entrada y convirtiéndolas en modelos 3D suaves. Toma múltiples imágenes como entrada y produce un archivo de modelo 3D descargable. El nodo maneja todo el proceso de generación, incluyendo la creación de tareas, la verificación periódica del estado y la descarga automática de archivos.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`Imágenes`| Imágenes de entrada para usar en la generación del modelo 3D. Se pueden proporcionar múltiples imágenes.| IMAGE| Sí| -  
`Semilla`| Valor de semilla aleatoria para la consistencia de la generación.| INT| No| -  
`Tipo_de_Material`| Tipo de material que se aplicará al modelo 3D.| STRING| No| -  
`Recuento_de_Polígonos`| Número objetivo de polígonos para el modelo 3D generado. Determina la calidad de la malla y el nivel de detalle.| STRING| No| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`Ruta del modelo 3D`| Ruta del archivo al modelo 3D descargado (solo para compatibilidad con versiones anteriores).| STRING  
`GLB`| El modelo 3D generado en formato GLB.| FILE3DGLB  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/es.md)

* * *

**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Rodin3D_Smooth.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Rodin3D_Smooth)

[Rodin 3D generar - generar boceto](https://docs.comfy.org/es/built-in-nodes/Rodin3D_Sketch)[Hunyuan3D: Parte 3D](https://docs.comfy.org/es/built-in-nodes/Tencent3DPartNode)
