---
url: https://docs.comfy.org/es/built-in-nodes/LatentCompositeMasked/
title: Componer latente con m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.011856+00:00
---

# Componer latente con máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentCompositeMasked/

Latente

# Componer latente con máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentCompositeMasked está diseñado para combinar dos representaciones latentes en coordenadas específicas

Copiar páginaCopiar página

El nodo LatentCompositeMasked está diseñado para combinar dos representaciones latentes en coordenadas específicas, utilizando opcionalmente una máscara para una composición más controlada. Este nodo permite crear imágenes latentes complejas superponiendo partes de una imagen sobre otra, con la capacidad de redimensionar la imagen de origen para un ajuste perfecto.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`destino`| La representación latente sobre la cual se compondrá otra representación latente. Actúa como la capa base para la operación de composición.| `LATENT`  
`fuente`| La representación latente que se va a componer sobre el destino. Esta capa de origen puede redimensionarse y posicionarse según los parámetros especificados.| `LATENT`  
`x`| La coordenada x en la representación latente de destino donde se colocará el origen. Permite un posicionamiento preciso de la capa de origen.| `INT`  
`y`| La coordenada y en la representación latente de destino donde se colocará el origen, lo que permite una superposición precisa.| `INT`  
`redimensionar_fuente`| Un indicador booleano que determina si la representación latente de origen debe redimensionarse para coincidir con las dimensiones del destino antes de la composición.| `BOOLEAN`  
`máscara`| Una máscara opcional que puede utilizarse para controlar la mezcla del origen sobre el destino. La máscara define qué partes del origen serán visibles en la composición final.| `MASK`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La representación latente resultante después de componer el origen sobre el destino, utilizando potencialmente una máscara para una mezcla selectiva.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentCompositeMasked.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentCompositeMasked)

[Compuesto latente](https://docs.comfy.org/es/built-in-nodes/LatentComposite)[Escalar latente](https://docs.comfy.org/es/built-in-nodes/LatentUpscale)
