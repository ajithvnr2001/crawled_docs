---
url: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Detail/
title: Rodin 3D generar - generar detalle - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.062674+00:00
---

# Rodin 3D generar - generar detalle - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Rodin3D_Detail/

Rodin

# Rodin 3D generar - generar detalle - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Rodin 3D Detail genera activos 3D detallados utilizando la API de Rodin.

Copiar páginaCopiar página

El nodo **Rodin 3D Detail** genera activos 3D detallados utilizando la API de Rodin. Toma imágenes de entrada y las procesa a través del servicio Rodin para crear modelos 3D de alta calidad con geometría y materiales detallados. El nodo gestiona todo el flujo de trabajo, desde la creación de la tarea hasta la descarga del archivo final del modelo 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`Imágenes`| Imágenes de entrada utilizadas para la generación del modelo 3D. Se pueden proporcionar múltiples imágenes.| IMAGE| Sí| -  
`Semilla`| Valor de semilla aleatoria para obtener resultados reproducibles| INT| No| -  
`Tipo_Material`| Tipo de material que se aplicará al modelo 3D| STRING| No| -  
`Recuento_Polígonos`| Cantidad objetivo de polígonos para el modelo 3D generado. Determina el nivel de calidad de la malla.| STRING| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`Ruta del modelo 3D`| Ruta del archivo al modelo 3D generado (solo para compatibilidad hacia atrás)| STRING  
`GLB`| El modelo 3D generado en formato GLB| FILE3DGLB  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/es.md)

* * *

**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Rodin3D_Detail.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Rodin3D_Detail)

[Meshy: Modelo de textura](https://docs.comfy.org/es/built-in-nodes/MeshyTextureNode)[Rodin 3D generar - generar Gen-2](https://docs.comfy.org/es/built-in-nodes/Rodin3D_Gen2)
