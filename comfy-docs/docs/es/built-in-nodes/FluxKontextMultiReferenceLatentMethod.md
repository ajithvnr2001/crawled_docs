---
url: https://docs.comfy.org/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod/
title: M\u00e9todo de referencia del modelo de edici\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:48.820568+00:00
---

# Método de referencia del modelo de edición - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod/

FLUX

# Método de referencia del modelo de edición - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo FluxKontextMultiReferenceLatentMethod actualiza los datos de condicionamiento almacenando en ellos un método de latentes de referencia elegido.

Copiar páginaCopiar página

El nodo FluxKontextMultiReferenceLatentMethod actualiza los datos de condicionamiento almacenando en ellos un método de latentes de referencia elegido. El método almacenado se utiliza luego cuando se procesan los latentes de referencia en pasos de generación posteriores. Este nodo está marcado como experimental y pertenece al sistema de condicionamiento Flux.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`acondicionamiento`| Los datos de condicionamiento que se modificarán con el método de latentes de referencia| CONDITIONING| Sí| -  
`método_latentes_referencia`| El método utilizado para el procesamiento de latentes de referencia. Si se selecciona un valor que contiene “uxo” o “uso”, se convierte a “uxo” antes de almacenarse. Este parámetro está marcado como avanzado.| COMBO| Sí| `"offset"`  
`"index"`  
`"uxo/uno"`  
`"index_timestep_zero"`  
`"index_timestep_zero_isolated"`  
`"index_timestep_zero_text_start"`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`conditioning`| Los datos de condicionamiento modificados con el método de latentes de referencia aplicado| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/es.md)

* * *

**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod)

[Escalar imagen Flux Kontext](https://docs.comfy.org/es/built-in-nodes/FluxKontextImageScale)[Aplicar cuadro de texto GLIGEN](https://docs.comfy.org/es/built-in-nodes/GLIGENTextBoxApply)
