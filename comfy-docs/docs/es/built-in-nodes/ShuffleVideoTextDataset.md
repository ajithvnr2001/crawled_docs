---
url: https://docs.comfy.org/es/built-in-nodes/ShuffleVideoTextDataset/
title: Mezclar Pares de Video-Texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.579798+00:00
---

# Mezclar Pares de Video-Texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ShuffleVideoTextDataset/

Lote

# Mezclar Pares de Video-Texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo baraja aleatoriamente el orden de pares de video-texto en una lista, manteniendo cada video emparejado con su texto correspondiente.

Copiar páginaCopiar página

Este nodo baraja aleatoriamente el orden de pares de video-texto en una lista, manteniendo cada video emparejado con su texto correspondiente. Toma dos listas de igual longitud y aplica la misma permutación aleatoria a ambas, garantizando que los emparejamientos originales se conserven después del barajado. Un valor de semilla controla el orden de barajado para que los resultados puedan reproducirse.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`videos`| Lista de videos para barajar.| VIDEO| Sí| Lista de elementos de video  
`texts`| Lista de textos para barajar (las descripciones emparejadas con los videos).| STRING| Sí| Lista de cadenas de texto  
`seed`| Semilla aleatoria que determina el orden de barajado (valor predeterminado: 0).| INT| Sí| 0 a 18446744073709551615  
  
Nota: `videos` y `texts` deben tener la misma longitud, ya que el nodo empareja cada video con el texto en la misma posición y conserva esos emparejamientos al barajar. Internamente, el valor de `seed` se reduce usando el módulo 4294967295 (2^32 - 1) antes de generar el orden aleatorio, por lo que los valores de semilla muy grandes pueden producir el mismo barajado que los más pequeños.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`videos`| Videos barajados en el nuevo orden aleatorio.| VIDEO  
`texts`| Textos barajados en el mismo nuevo orden que los videos.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/es.md)

* * *

**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ShuffleVideoTextDataset.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ShuffleVideoTextDataset)

[Mezclar Lista de Videos](https://docs.comfy.org/es/built-in-nodes/ShuffleVideoDataset)[Preprocesar LTXV](https://docs.comfy.org/es/built-in-nodes/LTXVPreprocess)
