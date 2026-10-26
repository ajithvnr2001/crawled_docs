---
url: https://docs.comfy.org/es/built-in-nodes/AudioAdjustVolume/
title: Ajustar volumen de audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:30.862201+00:00
---

# Ajustar volumen de audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AudioAdjustVolume/

Audio

# Ajustar volumen de audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo AudioAdjustVolume modifica el volumen del audio aplicando ajustes de ganancia en decibelios (dB).

Copiar páginaCopiar página

El nodo AudioAdjustVolume modifica el volumen del audio aplicando ajustes de ganancia en decibelios (dB). Toma una entrada de audio y aplica un factor de ganancia basado en el nivel de volumen especificado, donde los valores positivos aumentan el volumen y los negativos lo disminuyen. El nodo devuelve el audio modificado con la misma frecuencia de muestreo que el original.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`audio`| La entrada de audio que se va a procesar| AUDIO| Sí| -  
`volumen`| Ajuste de volumen en decibelios (dB). 0 = sin cambios, +6 = duplicar, -6 = reducir a la mitad, etc. (valor predeterminado: 1)| INT| Sí| -100 a 100  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`audio`| El audio procesado con el nivel de volumen ajustado| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/es.md)

* * *

**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AudioAdjustVolume.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AudioAdjustVolume)

[Comfy Cloud MiniMax Music 3 Texto a audio [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudMiniMaxMusic3TextToAudioNode)[Concatenar audio](https://docs.comfy.org/es/built-in-nodes/AudioConcat)
