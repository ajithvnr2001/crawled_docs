---
url: https://docs.comfy.org/es/development/comfyui-server/comms_messages/
title: Mensajes del servidor de ComfyUI (API WebSocket) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.396711+00:00
---

# Mensajes del servidor de ComfyUI (API WebSocket) - ComfyUI

> Source: https://docs.comfy.org/es/development/comfyui-server/comms_messages/

## En esta página

Volver arriba

  * Mensajes
    * Tipos de mensaje integrados
    * Usar executed
    * Tipos de mensaje personalizados
    * Obtener node_id



Self-Hosted Server API

# Mensajes del servidor de ComfyUI (API WebSocket)

Copiar páginaCopiar página

Cómo el PromptExecutor de ComfyUI envía mensajes WebSocket al cliente, tipos integrados como execution_start y progress, y cómo registrar tipos de mensaje personalizados.

Copiar páginaCopiar página

## 

​

Mensajes

Durante la ejecución (o cuando cambia el estado de la cola), el `PromptExecutor` envía mensajes de vuelta al cliente mediante el método `send_sync` de `PromptServer`. Estos mensajes los recibe un listener de eventos de socket definido en `api.js` (al momento de escribir esto, alrededor de la línea 90, o busca `this.socket.addEventListener`), que crea un objeto `CustomEvent` para cada tipo de mensaje conocido y lo despacha a los listeners registrados. Una extensión puede registrarse para recibir eventos (normalmente en la función `setup()`) siguiendo el idioma estándar de JavaScript:
    
    
    api.addEventListener(message_type, messageHandler);
    

Si `message_type` no es uno de los integrados, se añadirá automáticamente a la lista de tipos de mensaje conocidos. Se llamará a `messageHandler` con un objeto `CustomEvent`, que extiende el evento emitido por el socket para añadir una propiedad `.detail`, un diccionario con los datos enviados por el servidor. Así que el uso general es algo como:
    
    
    function messageHandler(event) {
        if (event.detail.node == aNodeIdThatIsInteresting) {
            // haz algo con event.detail.other_things
        }
    }
    

### 

​

Tipos de mensaje integrados

Durante la ejecución (o cuando cambia el estado de la cola), el `PromptExecutor` envía los siguientes mensajes de vuelta al cliente mediante el método `send_sync` de `PromptServer`. Una extensión puede registrarse como listener de cualquiera de ellos.

evento| cuándo| datos  
---|---|---  
`execution_start`| Cuando un prompt está a punto de ejecutarse| `prompt_id`  
`execution_error`| Cuando ocurre un error durante la ejecución| `prompt_id`, más información adicional  
`execution_interrupted`| Cuando la ejecución se detiene porque un nodo lanza `InterruptProcessingException`| `prompt_id`, `node_id`, `node_type` y `executed` (una lista de los nodos ejecutados)  
`execution_cached`| Al inicio de la ejecución| `prompt_id`, `nodes` (una lista de los nodos que se omiten porque se pueden usar sus salidas en caché)  
`execution_success`| Cuando todos los nodos del prompt se han ejecutado correctamente| `prompt_id`, `timestamp`  
`executing`| Cuando un nodo nuevo está a punto de ejecutarse| `node` (ID del nodo o `None` para indicar que terminó), `prompt_id`  
`executed`| Cuando un nodo devuelve un elemento de UI| `node` (ID del nodo), `prompt_id`, `output`  
`progress`| Durante la ejecución de un nodo que implementa el hook necesario| `node` (ID del nodo), `prompt_id`, `value`, `max`  
`status`| Cuando cambia el estado de la cola| `exec_info`, un diccionario con `queue_remaining`, el número de elementos de la cola  
  
### 

​

Usar executed

A pesar del nombre, un mensaje `executed` no se envía cada vez que un nodo termina su ejecución (a diferencia de `executing`), sino solo cuando el nodo devuelve una actualización de UI. Para hacerlo, la función principal debe devolver un diccionario en lugar de una tupla:
    
    
    # al final de mi método principal
            return { "ui":a_new_dictionary, "result": the_tuple_of_output_values }
    

`a_new_dictionary` se enviará entonces como valor de `output` en un mensaje `executed`. La clave `result` se puede omitir si el nodo no tiene salidas (mira, por ejemplo, el código de `SaveImage` en `nodes.py`)

### 

​

Tipos de mensaje personalizados

Como se indicó antes, en el lado del cliente puedes añadir un tipo de mensaje personalizado simplemente registrándote como listener de un nombre de tipo de mensaje único.
    
    
    api.addEventListener("my.custom.message", messageHandler);
    

En el servidor, el código es igual de sencillo:
    
    
    from server import PromptServer
    # después, en tu función de ejecución principal (normalmente)
            PromptServer.instance.send_sync("my.custom.message", a_dictionary)
    

#### 

​

Obtener node_id

La mayoría de los mensajes integrados incluyen el ID del nodo actual en el valor de `node`. Es probable que quieras hacer lo mismo. El node_id está disponible en el servidor mediante una entrada oculta, que se obtiene con la clave `hidden` del diccionario `INPUT_TYPES`:
    
    
        @classmethod    
        def INPUT_TYPES(s):
            return {"required" : { }, # aquí van tus entradas requeridas 
                    "hidden": { "node_id": "UNIQUE_ID" } } # Añade la clave hidden
    
        def my_main_function(self, required_inputs, node_id):
            # haz algunas cosas
            PromptServer.instance.send_sync("my.custom.message", {"node": node_id, "other_things": etc})
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfyui-server/comms_messages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfyui-server/comms_messages)

[Rutas HTTP y WebSocket](https://docs.comfy.org/es/development/comfyui-server/comms_routes)[Flags de inicio](https://docs.comfy.org/es/development/comfyui-server/startup-flags)
