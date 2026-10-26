---
url: https://docs.comfy.org/es/built-in-nodes/RandomNoise/
title: Ruido aleatorio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.286460+00:00
---

# Ruido aleatorio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RandomNoise/

Ruido

# Ruido aleatorio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RandomNoise crea un generador de ruido basado en un valor de semilla para su uso durante el proceso de muestreo.

Copiar páginaCopiar página

El nodo RandomNoise crea un generador de ruido basado en un valor de semilla para su uso durante el proceso de muestreo. La misma semilla siempre produce el mismo patrón de ruido, lo que permite obtener resultados consistentes y reproducibles en múltiples ejecuciones. Los muestreadores utilizan el ruido generado al procesar imágenes latentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`semilla_ruido`| El valor de semilla utilizado para generar el patrón de ruido aleatorio (predeterminado: 0). La misma semilla siempre produce la misma salida de ruido. Esta entrada incluye una opción de control posterior a la generación para actualizar automáticamente la semilla después de cada generación.| INT| Sí| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`noise`| Un objeto de ruido que genera ruido aleatorio para muestras latentes basado en el valor de semilla proporcionado. Utilizado por los muestreadores durante el proceso de muestreo.| NOISE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/es.md)

* * *

**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RandomNoise.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RandomNoise)

[Desactivar ruido](https://docs.comfy.org/es/built-in-nodes/DisableNoise)[Seleccionar KSampler](https://docs.comfy.org/es/built-in-nodes/KSamplerSelect)
