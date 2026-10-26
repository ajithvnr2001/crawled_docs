---
url: https://docs.comfy.org/es/built-in-nodes/RecordAudio/
title: Grabar audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.951971+00:00
---

# Grabar audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecordAudio/

Audio

# Grabar audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RecordAudio carga archivos de audio que han sido grabados o seleccionados a través de la interfaz de grabación de audio.

Copiar páginaCopiar página

El nodo `RecordAudio` carga archivos de audio que han sido grabados o seleccionados a través de la interfaz de grabación de audio. Procesa el archivo de audio y lo convierte en un formato de forma de onda que puede ser utilizado por otros nodos de procesamiento de audio en el flujo de trabajo. El nodo detecta automáticamente la frecuencia de muestreo y prepara los datos de audio para su posterior manipulación.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`audio`| La entrada de grabación de audio proveniente de la interfaz de grabación de audio| AUDIO_RECORD| Sí| N/A  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`AUDIO`| Los datos de audio procesados que contienen información de forma de onda y frecuencia de muestreo| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `3648f3c71f60f69e9ca117e25e9706187470866a1869ba9b8e5feceb42a7493a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecordAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecordAudio)

[Vista previa de audio](https://docs.comfy.org/es/built-in-nodes/PreviewAudio)[Guardar audio](https://docs.comfy.org/es/built-in-nodes/SaveAudio)
