---
url: https://docs.comfy.org/es/built-in-nodes/AudioConcat/
title: Concatenar audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:30.921195+00:00
---

# Concatenar audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AudioConcat/

Audio

# Concatenar audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo AudioConcat combina dos entradas de audio uniéndolas.

Copiar páginaCopiar página

El nodo AudioConcat combina dos entradas de audio uniéndolas. Toma dos entradas de audio y las conecta en el orden que especifiques, ya sea colocando el segundo audio antes o después del primero. El nodo maneja automáticamente diferentes formatos de audio convirtiendo audio mono a estéreo y emparejando las frecuencias de muestreo entre las dos entradas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`audio1`| La primera entrada de audio que se concatenará| AUDIO| Sí| -  
`audio2`| La segunda entrada de audio que se concatenará| AUDIO| Sí| -  
`dirección`| Si se añade audio2 después o antes de audio1 (predeterminado: “after”)| COMBO| Sí| `"after"`  
`"before"`  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`AUDIO`| El audio combinado que contiene ambos archivos de audio de entrada unidos| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/es.md)

* * *

**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AudioConcat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AudioConcat)

[Ajustar volumen de audio](https://docs.comfy.org/es/built-in-nodes/AudioAdjustVolume)[Ecualizador de audio (3 bandas)](https://docs.comfy.org/es/built-in-nodes/AudioEqualizer3Band)
