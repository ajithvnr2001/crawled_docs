---
url: https://docs.comfy.org/es/built-in-nodes/RenderUVAtlas/
title: Renderizar atlas UV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.269524+00:00
---

# Renderizar atlas UV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RenderUVAtlas/

Texturing

# Renderizar atlas UV - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Renderiza el diseño UV de una malla como una imagen.

Copiar páginaCopiar página

Renderiza el diseño UV de una malla como una imagen. Cada región UV conectada (isla UV) se rellena con un color distinto, y los bordes del contorno de las islas se delinean en negro sobre un fondo gris oscuro.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`mesh`| La malla 3D cuyo diseño UV se renderizará. La malla debe tener coordenadas UV; de lo contrario, el nodo genera el error “mesh has no UVs to render. Run UnwrapMesh first.”| MESH| Sí| -  
`resolution`| El ancho y alto, en píxeles, de la imagen cuadrada renderizada (predeterminado: 1024).| INT| Sí| 64 a 4096 (paso 64)  
  
Nota: Si la malla contiene una dimensión de lote (arreglos UV o de caras en 3D), solo se renderiza el primer elemento del lote.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen del atlas UV renderizada, devuelta como un lote de una sola imagen. Cada isla UV está coloreada y los bordes del contorno de las islas se delinean en negro.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/es.md)

* * *

**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RenderUVAtlas.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RenderUVAtlas)

[Textura de malla a imagen](https://docs.comfy.org/es/built-in-nodes/MeshTextureToImage)[Desplegar las UV de la malla](https://docs.comfy.org/es/built-in-nodes/UnwrapMesh)
