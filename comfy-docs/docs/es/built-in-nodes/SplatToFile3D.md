---
url: https://docs.comfy.org/es/built-in-nodes/SplatToFile3D/
title: Crear archivo 3D (desde Splat) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:32.115541+00:00
---

# Crear archivo 3D (desde Splat) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SplatToFile3D/

Splat

# Crear archivo 3D (desde Splat) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SplatToFile3D convierte un gaussian splat en un objeto File3D que puede utilizarse con los nodos Save o Preview 3D.

Copiar páginaCopiar página

El nodo SplatToFile3D convierte un gaussian splat en un objeto File3D que puede utilizarse con los nodos Save o Preview 3D. Solo admite un elemento por lote y permite elegir entre diferentes formatos de archivo de salida para los datos 3D exportados.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`splat`| Los datos del gaussian splat que se serializarán en un archivo| SPLAT| Sí| -  
`formato`| El formato de archivo de salida para el archivo 3D. ply: gaussian splat 3D estándar con armónicos esféricos completos. ksplat: SplatBuffer de mkkellogg (nivel 0, sin comprimir), solo color base. spz: comprimido con gzip de Niantic (~10 veces más pequeño), solo color base (predeterminado: “ply”)| COMBO| Sí| ”ply"  
"ksplat"  
"spz”  
  
Nota: Este nodo admite solo un elemento por lote. Si el splat de entrada contiene más de un elemento en el lote, el nodo registra una advertencia y utiliza el primer elemento. Si se proporciona un formato no compatible, el nodo genera un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`modelo_3d`| Un objeto File3D que contiene los datos del gaussian splat serializados en el formato seleccionado, listo para guardar o previsualizar| FILE3D  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/es.md)

* * *

**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SplatToFile3D.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SplatToFile3D)

[Render Splat](https://docs.comfy.org/es/built-in-nodes/RenderSplat)[Extraer malla de Splat](https://docs.comfy.org/es/built-in-nodes/SplatToMesh)
