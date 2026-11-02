---
url: https://docs.comfy.org/es/custom-nodes/help_page/
title: A\u00f1adir documentaci\u00f3n de nodos para tu nodo personalizado de ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.030779+00:00
---

# Añadir documentación de nodos para tu nodo personalizado de ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/help_page/

## En esta página

Volver arriba

  * Documentación de nodos con Markdown
  * Configuración
  * Funciones de Markdown compatibles
  * Estructura de ejemplo
  * Archivo Markdown de ejemplo



Package & Publish

# Añadir documentación de nodos para tu nodo personalizado de ComfyUI

Copiar páginaCopiar página

Cómo crear documentación completa para tus nodos personalizados

Copiar páginaCopiar página

## 

​

Documentación de nodos con Markdown

Los nodos personalizados pueden incluir documentación en Markdown completa que se mostrará en la interfaz en lugar de la descripción genérica del nodo. Esto ofrece a los usuarios información detallada sobre la funcionalidad, los parámetros y los ejemplos de uso de tu nodo. Si ya has añadido tooltips para cada parámetro en la definición del nodo, puedes acceder directamente a esta información básica desde el panel de documentación del nodo. No es necesario añadir más documentación del nodo, y puedes consultar la implementación relacionada de [ContextWindowsManualNode](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_context_windows.py#L7)

## 

​

Configuración

Para añadir documentación para tus nodos personalizados o documentación con soporte para varios idiomas:

  1. Crea una carpeta `docs` dentro de tu `WEB_DIRECTORY`
  2. Añade archivos Markdown con el nombre de tus nodos (los nombres de tus nodos son las claves del diccionario `NODE_CLASS_MAPPINGS` que se usa para registrarlos): 
     * `WEB_DIRECTORY/docs/NodeName.md`: documentación predeterminada
     * `WEB_DIRECTORY/docs/NodeName/en.md`: documentación en inglés
     * `WEB_DIRECTORY/docs/NodeName/zh.md`: documentación en chino
     * Añade otros idiomas según sea necesario (por ejemplo, `fr.md`, `de.md`, etc.)

El sistema cargará automáticamente la documentación adecuada según el idioma del usuario, y recurrirá a `NodeName.md` como respaldo si no hay una versión localizada disponible.

## 

​

Funciones de Markdown compatibles

  * Sintaxis Markdown estándar (encabezados, listas, bloques de código, etc.)
  * Imágenes con sintaxis Markdown: `![texto alternativo](image.png)`
  * Elementos multimedia HTML con atributos específicos: 
    * Etiquetas `<video>` y `<source>`
    * Atributos permitidos: `controls`, `autoplay`, `loop`, `muted`, `preload`, `poster`



## 

​

Estructura de ejemplo
    
    
    my-custom-node/
    ├── __init__.py
    ├── web/              # WEB_DIRECTORY
    │   ├── js/
    │   │   └── my-node.js
    │   └── docs/
    │       ├── MyNode.md           # Documentación de respaldo
    │       └── MyNode/
    │           ├── en.md           # Versión en inglés
    │           └── zh.md           # Versión en chino
    

## 

​

Archivo Markdown de ejemplo
    
    
    # Mi nodo personalizado
    
    Este nodo procesa imágenes con algoritmos avanzados.
    
    ## Parámetros
    
    - **image**: imagen de entrada que se va a procesar
    - **strength**: intensidad del procesamiento (0.0 - 1.0)
    
    ## Uso
    
    ![uso de ejemplo](https://docs.comfy.org/es/custom-nodes/help_page/example.png)
    
    <video controls loop muted>
      <source src="demo.mp4" type="video/mp4">
    </video>
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/help_page.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/help_page)

[Reemplazo de nodos](https://docs.comfy.org/es/custom-nodes/backend/node-replacement)[Plantillas de flujos de trabajo](https://docs.comfy.org/es/custom-nodes/workflow_templates)
