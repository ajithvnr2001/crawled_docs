---
url: https://docs.comfy.org/es/interface/model-library/
title: Biblioteca de modelos - Explora modelos locales - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.077795+00:00
---

# Biblioteca de modelos - Explora modelos locales - ComfyUI

> Source: https://docs.comfy.org/es/interface/model-library/

## En esta página

Volver arriba

  * Cómo abrir la Biblioteca de modelos
  * Explorar por carpeta
  * Búsqueda
  * Vista previa y actualización
  * Arrastra un modelo al lienzo
  * Configuraciones relacionadas
  * Páginas relacionadas



Barra lateral izquierda

# Biblioteca de modelos - Explora modelos locales

Copiar páginaCopiar página

Abre la barra lateral Biblioteca de modelos para encontrar checkpoints y otros modelos en tu carpeta de modelos de ComfyUI, y luego arrástralos al lienzo.

Copiar páginaCopiar página

La entrada **Modelos** de la barra lateral izquierda abre la Biblioteca de modelos. Después de que ComfyUI se inicie, enumera las carpetas y los archivos de modelos detectados dentro del árbol `ComfyUI/models` (y cualquier ruta de modelos adicional que hayas configurado). Úsala para buscar por nombre, explorar por tipo de carpeta, obtener una vista previa de los metadatos y arrastrar un modelo al lienzo para insertar el nodo cargador correspondiente. La disponibilidad varía según la versión:

  * **Autohospedado / Desktop** : la barra lateral muestra un árbol de carpetas con los archivos de modelos locales. En Desktop, las descargas en curso aparecen en la parte superior del panel y el icono de la barra lateral puede mostrar una insignia con el número de descargas.
  * **Comfy Cloud** : cuando el sistema de recursos esté disponible y la opción **Usar el navegador de recursos para la biblioteca de modelos** esté activada (valor predeterminado en Cloud), al hacer clic en **Modelos** se abre el navegador de recursos para modelos en lugar del árbol de la barra lateral. La carga o importación de tus propios pesos se explica en [Importar modelos](https://docs.comfy.org/es/cloud/import-models).

Los archivos multimedia (imágenes, video, audio, 3D) no se enumeran aquí. Se encuentran en [Recursos](https://docs.comfy.org/es/interface/assets). ![La barra lateral de la Biblioteca de modelos con la carpeta checkpoints expandida y la caja de búsqueda encima del árbol](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/model-library/model_library.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=45a85041be034c947ab6e8b6fe8092f9)

## 

​

Cómo abrir la Biblioteca de modelos

Haz clic en el icono **Modelos** de la barra lateral izquierda. El título del panel es **Biblioteca de modelos**.

## 

​

Explorar por carpeta

Sin una consulta de búsqueda, el panel muestra las carpetas raíz de modelos (por ejemplo `checkpoints`, `loras`, `vae`, `controlnet`, `diffusion_models`, `upscale_models`, `text_encoders`, y otras que devuelve el servidor). Expande una carpeta para cargar sus archivos. De forma predeterminada, las carpetas raíz cargan su contenido cuando las abres. Puedes cambiar eso en Configuraciones:

  * **Cargar automáticamente todas las carpetas de modelos** (`Comfy.ModelLibrary.AutoLoadAll`): cuando está activado, cada carpeta se carga en cuanto abres la biblioteca (puede ser lento en bibliotecas grandes). Cuando está desactivado (predeterminado en instalaciones propias), una carpeta se carga cuando la expandes. Esta configuración está oculta en Comfy Cloud.
  * **Qué nombre mostrar en la vista de árbol de la biblioteca de modelos** (`Comfy.ModelLibrary.NameFormat`): `title` (predeterminado) usa los títulos de los metadatos del modelo cuando están disponibles; `filename` muestra un nombre de archivo simplificado, sin el directorio ni la extensión `.safetensors`.

Cuando el flag de funciones de recursos está desactivado, aparece un botón **Cargar todas las carpetas** en el encabezado del panel, junto a Actualizar.

## 

​

Búsqueda

La caja de búsqueda en la parte superior filtra los modelos por nombre y campos relacionados que se pueden buscar mientras escribes. Al buscar, se cargan todas las carpetas para que los resultados estén completos. Los resultados se expanden automáticamente en el árbol. Si coinciden más de 500 modelos, el panel muestra una nota de resultados limitados; refina la consulta para llegar al resto.

## 

​

Vista previa y actualización

Pasa el cursor sobre una hoja de modelo para abrir una tarjeta de vista previa cuando haya metadatos disponibles. La tarjeta puede mostrar el título, el nombre del archivo, la arquitectura, el autor, la vista previa de imagen, la sugerencia de uso, la frase de activación y la descripción. Usa el botón de actualizar en el encabezado del panel, o presiona `r` (`Comfy.RefreshNodeDefinitions`), después de agregar o eliminar archivos de modelo mientras ComfyUI está en ejecución. Esa actualización también recarga las listas desplegables de nodos para que los widgets de carga detecten los archivos nuevos.

## 

​

Arrastra un modelo al lienzo

Las hojas de modelo se pueden arrastrar. Arrastra una al lienzo para crear el nodo cargador asignado a esa carpeta (por ejemplo, `CheckpointLoaderSimple` para `checkpoints`, `LoraLoader` para `loras`, `VAELoader` para `vae`, `UNETLoader` para `diffusion_models`, `CLIPLoader` para `text_encoders` y otras asignaciones registradas en el frontend). El widget correspondiente se rellena con el nombre del archivo del modelo. Si un tipo de carpeta no tiene una asignación de cargador registrada, es posible que al soltar el modelo no se cree un nodo. Los modelos faltantes que espera un flujo de trabajo siguen apareciendo en la pestaña **Errores** del [Panel lateral derecho](https://docs.comfy.org/es/interface/right-side-panel), con acciones para descargar o importar cuando estén disponibles.

## 

​

Configuraciones relacionadas

Configuración| Dónde| Qué hace  
---|---|---  
Cargar automáticamente todas las carpetas de modelos| `Comfy` → Biblioteca de modelos| Cargar todas las carpetas al abrir en lugar de al expandir  
Formato de nombre| `Comfy` → Biblioteca de modelos| Mostrar `title` o `filename` en el árbol  
Usar el navegador de recursos para la biblioteca de modelos| Experimental / Orientado a la nube| Abrir el navegador de recursos en lugar del árbol de la barra lateral cuando los recursos están habilitados  
  
## 

​

Páginas relacionadas

  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview)
  * [Recursos](https://docs.comfy.org/es/interface/assets) (archivos multimedia, no pesos de modelos)
  * [Importar modelos](https://docs.comfy.org/es/cloud/import-models) (Cloud)
  * [Panel lateral derecho](https://docs.comfy.org/es/interface/right-side-panel) (errores de modelo faltante)
  * [Configuraciones de Comfy](https://docs.comfy.org/es/interface/settings/comfy) (sección Biblioteca de modelos)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/model-library.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/model-library)

[Biblioteca de nodos](https://docs.comfy.org/es/interface/node-library)[Flujos de trabajo](https://docs.comfy.org/es/interface/workflows)
