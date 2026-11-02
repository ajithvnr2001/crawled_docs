---
url: https://docs.comfy.org/es/custom-nodes/js/javascript_overview/
title: Extensiones de JavaScript - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.220463+00:00
---

# Extensiones de JavaScript - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/js/javascript_overview/

## En esta página

Volver arriba

  * Extender el cliente de Comfy
    * Exportar WEB_DIRECTORY
    * Incluir archivos .js
    * Registrar una extensión



JavaScript (UI)

# Extensiones de JavaScript

Copiar páginaCopiar página

Aprende a extender ComfyUI con extensiones de JavaScript exportando WEB_DIRECTORY, añadiendo archivos .js y registrando una extensión con app.registerExtension.

Copiar páginaCopiar página

## 

​

Extender el cliente de Comfy

Comfy se puede modificar mediante un mecanismo de extensiones. Para añadir una extensión necesitas:

  * Exportar `WEB_DIRECTORY` desde tu módulo de Python,
  * Colocar uno o más archivos `.js` en ese directorio,
  * Usar `app.registerExtension` para registrar tu extensión.

Estos tres pasos se describen a continuación. Cuando ya sepas cómo añadir una extensión, consulta los [hooks](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks) disponibles para que tu código se ejecute, la descripción de los distintos [objetos de Comfy](https://docs.comfy.org/es/custom-nodes/js/javascript_objects_and_hijacking) que puedas necesitar, o pasa directamente a algunos [fragmentos de código de ejemplo](https://docs.comfy.org/es/custom-nodes/js/javascript_examples).

### 

​

Exportar `WEB_DIRECTORY`

El cliente web de Comfy se puede extender creando un subdirectorio en el directorio de tu nodo personalizado, al que por convención se llama `js`, y exportando `WEB_DIRECTORY`, de modo que tu `__init_.py` incluirá algo como:
    
    
    WEB_DIRECTORY = "./js"
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
    

### 

​

Incluir archivos `.js`

Todos los archivos `.js` de JavaScript los cargará el navegador a medida que se carga la página web de Comfy. No necesitas especificar el archivo en el que está tu extensión.

_Solo_ se añadirán a la página web los archivos `.js`. Otros recursos (como los archivos `.css`) se pueden consultar en `extensions/custom_node_subfolder/the_file.css` y añadir mediante código.

Esa ruta _no_ incluye el nombre del subdirectorio. El valor de `WEB_DIRECTORY` lo inserta el servidor.

### 

​

Registrar una extensión

La estructura básica de una extensión consiste en importar el objeto principal `app` de Comfy y llamar a `app.registerExtension`, pasando un diccionario que contenga un `name` único, y una o más funciones que los hooks del código de Comfy llamarán. Una extensión completa, trivial y molesta podría tener este aspecto:
    
    
    import { app } from "../../scripts/app.js";
    app.registerExtension({ 
    	name: "a.unique.name.for.a.useless.extension",
    	async setup() { 
    		alert("Setup complete!")
    	},
    })
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/js/javascript_overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/js/javascript_overview)

[Inversión del modelo de ejecución](https://docs.comfy.org/es/development/comfyui-server/execution_model_inversion_guide)[Ganchos](https://docs.comfy.org/es/custom-nodes/js/javascript_hooks)
