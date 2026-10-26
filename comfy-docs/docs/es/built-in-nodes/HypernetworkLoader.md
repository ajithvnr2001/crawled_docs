---
url: https://docs.comfy.org/es/built-in-nodes/HypernetworkLoader/
title: Cargar hypernetwork - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:54.568632+00:00
---

# Cargar hypernetwork - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HypernetworkLoader/

Cargadores

# Cargar hypernetwork - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta ComfyUI/models/hypernetworks

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/hypernetworks`, y también lee modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo de la carpeta correspondiente. El nodo HypernetworkLoader está diseñado para mejorar o modificar las capacidades de un modelo determinado mediante la aplicación de una hiperred. Carga una hiperred específica y la aplica al modelo, alterando potencialmente su comportamiento o rendimiento según el parámetro de intensidad. Este proceso permite realizar ajustes dinámicos en la arquitectura o los parámetros del modelo, posibilitando sistemas de IA más flexibles y adaptativos.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`modelo`| El modelo base al que se aplicará la hiperred, determinando la arquitectura que se mejorará o modificará.| `MODEL`  
`nombre_hypernetwork`| El nombre de la hiperred que se cargará y aplicará al modelo, afectando el comportamiento o rendimiento modificado del modelo.| `COMBO[STRING]`  
`fuerza`| Un escalar que ajusta la intensidad del efecto de la hiperred sobre el modelo, permitiendo un ajuste fino de las alteraciones.| `FLOAT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo modificado después de aplicar la hiperred, mostrando el impacto de la hiperred sobre el modelo original.| `MODEL`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HypernetworkLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HypernetworkLoader)

[Cargar GLIGEN](https://docs.comfy.org/es/built-in-nodes/GLIGENLoader)[Cargador de puntos de control solo de imagen (modelo img2vid)](https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointLoader)
