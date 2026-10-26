---
url: https://docs.comfy.org/es/built-in-nodes/LoadVideo/
title: Cargar video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.868295+00:00
---

# Cargar video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadVideo/

Video

# Cargar video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Load Video carga archivos de video desde el directorio de entrada y los pone a disposición para su procesamiento en el flujo de trabajo.

Copiar páginaCopiar página

El nodo Load Video carga archivos de video desde el directorio de entrada y los pone a disposición para su procesamiento en el flujo de trabajo. Lee archivos de video desde la carpeta de entrada designada y los genera como datos de video que se pueden conectar a otros nodos de procesamiento de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`archivo`| El archivo de video que se cargará desde el directorio de entrada. La lista desplegable se completa dinámicamente con todos los archivos de video encontrados en la carpeta de entrada de ComfyUI, y se pueden subir nuevos archivos de video directamente mediante el selector de archivos.| COMBO| Sí| Múltiples opciones disponibles (todos los archivos de video en el directorio de entrada)  
  
**Nota:** Las opciones disponibles para el parámetro `file` se completan dinámicamente a partir de los archivos de video presentes en el directorio de entrada. Solo se muestran los archivos que coinciden con los tipos de contenido de video compatibles, y la lista se ordena alfabéticamente. También puede subir un nuevo archivo de video directamente a través de la interfaz del selector de archivos del nodo. Si un archivo de video seleccionado previamente ya no se encuentra, el nodo informa un error de archivo no válido.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| Los datos de video cargados que se pueden pasar a otros nodos de procesamiento de video para su posterior manipulación o análisis.| VIDEO  
  
**Nota:** El nodo también produce una vista previa del video cargado, que se muestra directamente en el nodo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadVideo)

[Obtener componentes de video](https://docs.comfy.org/es/built-in-nodes/GetVideoComponents)[Cargar Video (desde Carpeta)](https://docs.comfy.org/es/built-in-nodes/LoadVideoDataSetFromFolder)
