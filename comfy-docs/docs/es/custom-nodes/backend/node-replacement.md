---
url: https://docs.comfy.org/es/custom-nodes/backend/node-replacement/
title: Reemplazo de nodos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-03T14:55:24.012826+00:00
---

# Reemplazo de nodos - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/backend/node-replacement/

## En esta página

Volver arriba

  * Cuándo usar
  * Dónde registrar los reemplazos
  * Ejemplo completo
  * Ejemplos principales
    * Fusión simple de nodos
    * Corrección de un error tipográfico
    * Renombrar entradas con valores predeterminados
    * Asignación de entradas con Autogrow
  * Parámetros de NodeReplace
  * Asignación de entradas
  * Asignación de salidas
  * Vinculación de ID de widget
  * REST API
  * Comportamiento del frontend



Migration Guides

# Reemplazo de nodos

Copiar páginaCopiar página

Registra reemplazos de nodos para que los usuarios migren de los nodos obsoletos

Copiar páginaCopiar página

La API de reemplazo de nodos permite a los desarrolladores de nodos personalizados definir rutas de migración desde nodos obsoletos hasta sus equivalentes más recientes. Cuando actualizas o renombras nodos, los usuarios pueden mejorar automáticamente sus flujos de trabajo.

## 

​

Cuándo usar

  * **Cambiar nombres de clase de nodo** : Cambiaste el nombre de clase de un nodo (en su lugar, usa `DISPLAY_NAME` para cambios de nombre para mostrar)
  * **Fusionar nodos** : Varios nodos consolidados en uno (p. ej., `Load3DAnimation` fusionado en `Load3D`)
  * **Refactorizar entradas** : Los nombres o tipos de las entradas cambiaron entre versiones
  * **Corregir errores tipográficos** : Corregir nombres de nodos sin romper los flujos de trabajo existentes



## 

​

Dónde registrar los reemplazos

Registra los reemplazos durante el hook del ciclo de vida `on_load` de tu extensión. Crea un archivo dedicado (por ejemplo, `node_replacements.py`) en tu paquete de nodos personalizados:
    
    
    my_custom_nodes/
    ├── __init__.py
    ├── nodes.py
    └── node_replacements.py   # Register replacements here
    

## 

​

Ejemplo completo

Aquí tienes un ejemplo completo que muestra cómo estructurar los reemplazos de nodos en un paquete de nodos personalizados:
    
    
    # node_replacements.py
    from comfy_api.latest import ComfyExtension, io, ComfyAPI
    
    api = ComfyAPI()
    
    
    async def register_my_replacements():
        """Register all node replacements for this package."""
        
        # Simple rename - no input changes needed
        await api.node_replacement.register(io.NodeReplace(
            new_node_id="MyNewNode",
            old_node_id="MyOldNode",
        ))
        
        # Complex replacement with input mapping
        await api.node_replacement.register(io.NodeReplace(
            new_node_id="MyImprovedSampler",
            old_node_id="MyOldSampler",
            old_widget_ids=["steps", "cfg"],
            input_mapping=[
                {"new_id": "model", "old_id": "model"},
                {"new_id": "num_steps", "old_id": "steps"},
                {"new_id": "guidance", "old_id": "cfg"},
                {"new_id": "scheduler", "set_value": "normal"},  # New input with default
            ],
            output_mapping=[
                {"new_idx": 0, "old_idx": 0},
            ],
        ))
    
    
    class MyExtension(ComfyExtension):
        async def on_load(self) -> None:
            await register_my_replacements()
    
        async def get_node_list(self) -> list[type[io.ComfyNode]]:
            return []  # No nodes defined here, just replacements
    
    
    async def comfy_entrypoint() -> MyExtension:
        return MyExtension()
    

## 

​

Ejemplos principales

El núcleo de ComfyUI usa reemplazos de nodos para las migraciones de nodos integrados. Aquí hay ejemplos reales de [`comfy_extras/nodes_replacements.py`](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_replacements.py):

### 

​

Fusión simple de nodos

Cuando `Load3DAnimation` se fusionó con `Load3D`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="Load3D",
        old_node_id="Load3DAnimation",
    ))
    

### 

​

Corrección de un error tipográfico

Cómo corregir un error tipográfico en `SDV_img2vid_Conditioning` → `SVD_img2vid_Conditioning`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="SVD_img2vid_Conditioning",
        old_node_id="SDV_img2vid_Conditioning",
    ))
    

### 

​

Renombrar entradas con valores predeterminados

Cómo reemplazar `ImageScaleBy` por `ResizeImageMaskNode`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="ResizeImageMaskNode",
        old_node_id="ImageScaleBy",
        old_widget_ids=["upscale_method", "scale_by"],
        input_mapping=[
            {"new_id": "input", "old_id": "image"},
            {"new_id": "resize_type", "set_value": "scale by multiplier"},
            {"new_id": "resize_type.multiplier", "old_id": "scale_by"},
            {"new_id": "scale_method", "old_id": "upscale_method"},
        ],
    ))
    

### 

​

Asignación de entradas con Autogrow

Para los nodos que usan Autogrow (entradas dinámicas), usa la notación con punto:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="BatchImagesNode",
        old_node_id="ImageBatch",
        input_mapping=[
            {"new_id": "images.image0", "old_id": "image1"},
            {"new_id": "images.image1", "old_id": "image2"},
        ],
    ))
    

## 

​

Parámetros de NodeReplace

Parámetro| Tipo| Descripción  
---|---|---  
`new_node_id`| str| Nombre de clase del nodo de reemplazo  
`old_node_id`| str| Nombre de clase del nodo obsoleto  
`old_widget_ids`| list[str] | None| Lista ordenada que vincula los ID de widget con sus índices relativos  
`input_mapping`| list | None| Cómo asignar las entradas del nodo antiguo al nuevo  
`output_mapping`| list | None| Cómo asignar las salidas del nodo antiguo al nuevo  
  
## 

​

Asignación de entradas

Cada entrada de la asignación define cómo se transfiere una entrada del nodo anterior al nuevo. **Asignar desde la entrada anterior:**
    
    
    {"new_id": "model", "old_id": "model"}
    

**Establecer un valor fijo:**
    
    
    {"new_id": "scheduler", "set_value": "normal"}
    

**Asignar entradas dinámicas/autogrow (usa notación con punto):**
    
    
    {"new_id": "images.image0", "old_id": "image1"}
    

## 

​

Asignación de salidas

Las asignaciones de salidas usan referencias basadas en índices:
    
    
    {"new_idx": 0, "old_idx": 0}  # Map first output
    {"new_idx": 1, "old_idx": 0}  # Old output 0 -> new output 1
    

## 

​

Vinculación de ID de widget

El campo `old_widget_ids` asigna los ID de widget a sus índices posicionales. Esto es requerido porque el JSON del flujo de trabajo almacena los valores de los widgets por posición, no por ID.
    
    
    old_widget_ids=["steps", "cfg", "sampler"]
    # Widget at index 0 = "steps"
    # Widget at index 1 = "cfg"
    # Widget at index 2 = "sampler"
    

## 

​

REST API

Recupera todos los reemplazos registrados:
    
    
    GET /api/node_replacements
    

**Respuesta:**
    
    
    {
      "OldSamplerNode": [
        {
          "new_node_id": "NewSamplerNode",
          "old_node_id": "OldSamplerNode",
          "old_widget_ids": ["num_steps", "cfg_scale", "sampler_name"],
          "input_mapping": [
            {"new_id": "model", "old_id": "model"},
            {"new_id": "steps", "old_id": "num_steps"},
            {"new_id": "scheduler", "set_value": "normal"}
          ],
          "output_mapping": [
            {"new_idx": 0, "old_idx": 0}
          ]
        }
      ]
    }
    

## 

​

Comportamiento del frontend

Cuando un flujo de trabajo contiene un nodo obsoleto, el frontend:

  1. Obtiene los reemplazos desde `GET /api/node_replacements`
  2. Detecta los nodos que coinciden con `old_node_id`
  3. Pide al usuario que actualice
  4. Aplica las asignaciones de entrada y salida automáticamente
  5. Conserva las conexiones y los valores de los widgets

Consulta la implementación del frontend:

  * [PR de lógica de negocio #8364](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8364)
  * [PR de lógica adicional #8483](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8483)
  * [PR de vistas de UI #8604](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8604)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/backend/node-replacement.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/backend/node-replacement)

[Migración del menú contextual](https://docs.comfy.org/es/custom-nodes/js/context-menu-migration)[Documentación de nodos](https://docs.comfy.org/es/custom-nodes/help_page)
