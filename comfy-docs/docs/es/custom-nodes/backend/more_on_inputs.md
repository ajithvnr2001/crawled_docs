---
url: https://docs.comfy.org/es/custom-nodes/backend/more_on_inputs/
title: Entradas ocultas y flexibles - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:50.438265+00:00
---

# Entradas ocultas y flexibles - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/backend/more_on_inputs/

## En esta página

Volver arriba

  * Entradas ocultas
    * UNIQUE_ID
    * PROMPT
    * EXTRA_PNGINFO
    * DYNPROMPT
  * Entradas flexibles
    * Tipos de datos personalizados
    * Entradas comodín
    * Entradas creadas dinámicamente



Python (backend)

# Entradas ocultas y flexibles

Copiar páginaCopiar página

Entradas ocultas de ComfyUI (UNIQUE_ID, PROMPT, EXTRA_PNGINFO, DYNPROMPT) y flexibles, con tipos de datos personalizados y comodines para nodos personalizados.

Copiar páginaCopiar página

## 

​

Entradas ocultas

Además de las entradas `required` y `optional`, que crean las entradas o widgets correspondientes en el lado del cliente, existen tres opciones de entrada `hidden` que permiten al nodo personalizado solicitar cierta información al servidor. Se accede a ellas devolviendo un valor para `hidden` en el `dict` de `INPUT_TYPES`, con la firma `dict[str,str]`, que contenga uno o más de `PROMPT`, `EXTRA_PNGINFO` o `UNIQUE_ID`.
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {...},
            "optional": {...},
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "prompt": "PROMPT", 
                "extra_pnginfo": "EXTRA_PNGINFO",
            }
        }
    

### 

​

UNIQUE_ID

`UNIQUE_ID` es el identificador único del nodo y coincide con la propiedad `id` del nodo en el lado del cliente. Se usa comúnmente en las comunicaciones cliente-servidor (consulta [mensajes](https://docs.comfy.org/es/development/comfyui-server/comms_messages#obtener-node-id)).

### 

​

PROMPT

`PROMPT` es el prompt completo enviado por el cliente al servidor. Consulta [el objeto prompt](https://docs.comfy.org/es/custom-nodes/js/javascript_objects_and_hijacking#prompt) para obtener una descripción completa.

### 

​

EXTRA_PNGINFO

`EXTRA_PNGINFO` es un diccionario que se copiará en los metadatos de los archivos `.png` que se guarden. Los nodos personalizados pueden almacenar información adicional en este diccionario para guardarla (o como una forma de comunicarse con un nodo posterior).

Ten en cuenta que si Comfy se inicia con la opción `disable_metadata`, estos datos no se guardarán.

### 

​

DYNPROMPT

`DYNPROMPT` es una instancia de `comfy_execution.graph.DynamicPrompt`. Se diferencia de `PROMPT` en que puede mutar durante el transcurso de la ejecución en respuesta a la [Node Expansion](https://docs.comfy.org/es/custom-nodes/backend/expansion). 

`DYNPROMPT` solo debe usarse para casos avanzados (como implementar bucles en nodos personalizados).

## 

​

Entradas flexibles

### 

​

Tipos de datos personalizados

Si quieres pasar datos entre tus propios Nodos personalizados, puede resultarte útil definir un tipo de datos personalizado. Esto es (casi) tan sencillo como elegir un nombre para el tipo de datos, que debe ser una cadena única en mayúsculas, como `CHEESE`. Después puedes usar `CHEESE` en los `INPUT_TYPES` y `RETURN_TYPES` de tu nodo, y el cliente de Comfy solo permitirá que las Salidas `CHEESE` se conecten a una Entrada `CHEESE`. `CHEESE` puede ser cualquier Objeto de python. El único punto a tener en cuenta es que, como el cliente de Comfy no conoce `CHEESE`, necesitas (a menos que definas un widget personalizado para `CHEESE`, que es un tema para otro día) forzarlo para que sea una Entrada en lugar de un widget. Esto se puede hacer con la opción `forceInput` en el diccionario de opciones de la Entrada:
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { "my_cheese": ("CHEESE", {"forceInput":True}) }
        }
    

### 

​

Entradas comodín
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { "anything": ("*",{})},
        }
    
    @classmethod
    def VALIDATE_INPUTS(s, input_types):
        return True
    

El frontend permite usar `*` para indicar que una Entrada se puede conectar a cualquier Fuente. Como el backend no lo admite oficialmente, puedes Saltar la Validación de tipos del backend si aceptas un parámetro llamado `input_types` en tu función `VALIDATE_INPUTS`. (Consulta [VALIDATE_INPUTS](https://docs.comfy.org/es/custom-nodes/backend/server_overview#validate_inputs) para obtener más información.) Depende del nodo dar sentido a los datos que recibe.

### 

​

Entradas creadas dinámicamente

Si las Entradas se crean dinámicamente en el lado del cliente, no se pueden definir en el código fuente de Python. Para acceder a estos datos necesitamos un DICCIONARIO `optional` que permita a Comfy pasar datos con nombres arbitrarios. Dado que el Servidor de Comfy
    
    
    class ContainsAnyDict(dict):
        def __contains__(self, key):
            return True
    ...
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": ContainsAnyDict()
        }
    ...
    
    def main_method(self, **kwargs):
        # los datos de Entrada creados dinámicamente estarán en el DICCIONARIO kwargs
    
    

¡Gracias a rgthree por este truco pitónico!

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/backend/more_on_inputs.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/backend/more_on_inputs)

[Imágenes, latentes y máscaras](https://docs.comfy.org/es/custom-nodes/backend/images_and_masks)[Evaluación diferida](https://docs.comfy.org/es/custom-nodes/backend/lazy_evaluation)
