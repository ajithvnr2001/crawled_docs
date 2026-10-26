---
url: https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3DigitalIllustration/
title: Estilo Recraft - ilustraci\u00f3n digital - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:21.391768+00:00
---

# Estilo Recraft - ilustración digital - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3DigitalIllustration/

Recraft

# Estilo Recraft - ilustración digital - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo configura un estilo para usar con la API de Recraft, seleccionando específicamente el estilo “digitalillustration”.

Copiar páginaCopiar página

Este nodo configura un estilo para usar con la API de Recraft, seleccionando específicamente el estilo “digital_illustration”. Permite elegir un subestilo opcional para refinar aún más la dirección artística de la imagen generada.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`subestilo`| Un subestilo opcional para especificar un tipo particular de ilustración digital. Si no se selecciona, se utiliza el estilo base “digital_illustration”.| STRING| No| `"digital_illustration"`  
`"digital_illustration_anime"`  
`"digital_illustration_cartoon"`  
`"digital_illustration_comic"`  
`"digital_illustration_concept_art"`  
`"digital_illustration_fantasy"`  
`"digital_illustration_futuristic"`  
`"digital_illustration_graffiti"`  
`"digital_illustration_graphic_novel"`  
`"digital_illustration_hyperrealistic"`  
`"digital_illustration_ink"`  
`"digital_illustration_manga"`  
`"digital_illustration_minimalist"`  
`"digital_illustration_pixel_art"`  
`"digital_illustration_pop_art"`  
`"digital_illustration_retro"`  
`"digital_illustration_sci_fi"`  
`"digital_illustration_sticker"`  
`"digital_illustration_street_art"`  
`"digital_illustration_surreal"`  
`"digital_illustration_vector"`  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`estilo_recraft`| Un objeto de estilo configurado que contiene el estilo “digital_illustration” seleccionado y el subestilo opcional, listo para ser pasado a otros nodos de la API de Recraft.| STYLEV3  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/es.md)

* * *

**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecraftStyleV3DigitalIllustration.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecraftStyleV3DigitalIllustration)

[Recraft reemplazar fondo](https://docs.comfy.org/es/built-in-nodes/RecraftReplaceBackgroundNode)[Recraft style - biblioteca de estilos infinita](https://docs.comfy.org/es/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary)
