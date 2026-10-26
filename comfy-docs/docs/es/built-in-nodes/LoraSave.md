---
url: https://docs.comfy.org/es/built-in-nodes/LoraSave/
title: Extraer y guardar LoRA - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.752368+00:00
---

# Extraer y guardar LoRA - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoraSave/

Experimental

# Extraer y guardar LoRA - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoraSave extrae y guarda archivos LoRA (Adaptación de Bajo Rango) a partir de diferencias de modelos.

Copiar páginaCopiar página

El nodo LoraSave extrae y guarda archivos LoRA (Adaptación de Bajo Rango) a partir de diferencias de modelos. Puede procesar diferencias de modelos de difusión, diferencias de codificadores de texto, o ambas, convirtiéndolas en formato LoRA con rango y tipo especificados. El archivo LoRA resultante se guarda en el directorio de salida para su uso posterior.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prefijo_nombre_archivo`| El prefijo para el nombre del archivo de salida (predeterminado: “loras/ComfyUI_extracted_lora”)| STRING| Sí| -  
`rango`| El valor de rango para el LoRA, que controla el tamaño y la complejidad (predeterminado: 8)| INT| Sí| 1-4096  
`tipo_lora`| El tipo de LoRA a crear (predeterminado: “standard”)| COMBO| Sí| `"standard"`  
`"locon"`  
`"loha"`  
`"lokr"`  
`"dylora"`  
`diferencia_sesgo`| Si se deben incluir las diferencias de sesgo en el cálculo del LoRA (predeterminado: True)| BOOLEAN| Sí| -  
`diferencia_modelo`| La salida de ModelSubtract que se convertirá en un lora| MODEL| No| -  
`diferencia_codificador_texto`| La salida de CLIPSubtract que se convertirá en un lora| CLIP| No| -  
  
**Nota:** Se debe proporcionar al menos uno de los parámetros `model_diff` o `text_encoder_diff` para que el nodo funcione. Si ambos se omiten, el nodo no generará ninguna salida.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
-| Este nodo guarda un archivo LoRA en el directorio de salida, pero no devuelve ningún dato a través del flujo de trabajo| -  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/es.md)

* * *

**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoraSave.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoraSave)

[Mezcla latente](https://docs.comfy.org/es/built-in-nodes/LatentBlend)[¡Mahiro es tan linda que merece una mejor función de guía!! (。・ω・。)](https://docs.comfy.org/es/built-in-nodes/Mahiro)
