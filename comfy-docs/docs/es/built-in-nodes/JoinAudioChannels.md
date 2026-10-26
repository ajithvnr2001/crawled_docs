---
url: https://docs.comfy.org/es/built-in-nodes/JoinAudioChannels/
title: Unir canales de audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.274960+00:00
---

# Unir canales de audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/JoinAudioChannels/

Audio

# Unir canales de audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Unir Canales de Audio combina dos entradas de audio mono separadas en una única salida de audio estéreo.

Copiar páginaCopiar página

El nodo **Unir Canales de Audio** combina dos entradas de audio mono separadas en una única salida de audio estéreo. Toma un canal izquierdo y un canal derecho, asegura que tengan frecuencias de muestreo y duraciones compatibles, y los fusiona en una forma de onda de audio de dos canales.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`audio_izquierdo`| Los datos de audio mono que se usarán como canal izquierdo en el audio estéreo resultante.| AUDIO| Sí|   
`audio_derecho`| Los datos de audio mono que se usarán como canal derecho en el audio estéreo resultante.| AUDIO| Sí|   
  
**Nota:** Ambas transmisiones de audio de entrada deben ser mono (un solo canal). Si tienen diferentes frecuencias de muestreo, el canal con la frecuencia más baja se remuestreará automáticamente para igualar la más alta. Si las transmisiones de audio tienen diferentes duraciones, se recortarán a la duración de la más corta.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`audio`| El audio estéreo resultante, que contiene los canales izquierdo y derecho unidos.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/es.md)

* * *

**Source fingerprint (SHA-256):** `6dced8c2288fb8f214e04b621ed3ab934231983d7987ff08aa43da6814331be0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/JoinAudioChannels.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/JoinAudioChannels)

[Audio vacío](https://docs.comfy.org/es/built-in-nodes/EmptyAudio)[Cargar audio](https://docs.comfy.org/es/built-in-nodes/LoadAudio)
