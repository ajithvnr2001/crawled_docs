---
url: https://docs.comfy.org/es/built-in-nodes/DeprecatedCheckpointLoader/
title: DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.319773+00:00
---

# DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DeprecatedCheckpointLoader/

Cargadores

# DeprecatedCheckpointLoader - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CheckpointLoader está diseñado para operaciones de carga avanzadas

Copiar páginaCopiar página

El nodo CheckpointLoader está diseñado para operaciones de carga avanzadas, específicamente para cargar puntos de control de modelos junto con sus configuraciones. Facilita la recuperación de los componentes del modelo necesarios para inicializar y ejecutar modelos generativos, incluyendo configuraciones y puntos de control desde directorios especificados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`config_name`| Especifica el nombre del archivo de configuración a utilizar. Esto es crucial para determinar los parámetros y ajustes del modelo, afectando su comportamiento y rendimiento.| COMBO[STRING]  
`ckpt_name`| Indica el nombre del archivo de punto de control que se cargará. Esto influye directamente en el estado del modelo que se está inicializando, impactando sus pesos y sesgos iniciales.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model`| Representa el modelo principal cargado desde el punto de control, listo para operaciones posteriores o inferencia.| MODEL  
`clip`| Proporciona el componente del modelo CLIP, si está disponible y se solicita, cargado desde el punto de control.| CLIP  
`vae`| Entrega el componente del modelo VAE, si está disponible y se solicita, cargado desde el punto de control.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DeprecatedCheckpointLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DeprecatedCheckpointLoader)

[Combinar pares de acondicionamiento (Establecer por defecto)](https://docs.comfy.org/es/built-in-nodes/PairConditioningSetDefaultCombine)[DeprecatedDiffusersLoader](https://docs.comfy.org/es/built-in-nodes/DeprecatedDiffusersLoader)
