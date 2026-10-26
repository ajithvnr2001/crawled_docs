---
url: https://docs.comfy.org/es/interface/layer-editor/
title: Editor de capas (Compositor): combina im\u00e1genes como capas en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.558718+00:00
---

# Editor de capas (Compositor): combina imágenes como capas en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/interface/layer-editor/

Componentes de funciones

# Editor de capas (Compositor): combina imágenes como capas en ComfyUI

Copiar páginaCopiar página

El Editor de capas compone dos o más imágenes como capas con transformaciones, modos de fusión y opacidad, y luego exporta el resultado como archivo PSD.

Copiar páginaCopiar página

El Editor de capas es un editor integrado al estilo PSD para combinar imágenes en una composición por capas. Lo abres desde una salida de imagen en el lienzo, apilas dos o más imágenes como capas y ajustas la posición, el tamaño, la rotación, la opacidad y el modo de fusión de cada capa. Con él funcionan dos tipos de entradas:

  * **Salidas de imagen de cualquier nodo.** El editor carga las imágenes de salida del nodo como capas separadas y exportas la composición finalizada como un archivo PSD.
  * **Create Layered Image.** [Create Layered Image](https://docs.comfy.org/es/built-in-nodes/ImageCompositor) almacena una composición por capas en una entrada opcional `compositor` que es exclusiva de este nodo. El editor carga la composición almacenada y escribe tus ediciones de vuelta en ella, de modo que la siguiente ejecución del flujo de trabajo usa la composición que creaste. Construye la pila de capas con la que compone usando [Agregar capa](https://docs.comfy.org/es/built-in-nodes/AddLayer) y [Capas desde cajas delimitadoras](https://docs.comfy.org/es/built-in-nodes/LayersFromBoundingBoxes), que producen capas en lugar de almacenar una composición.



## 

​

Abrir el editor de capas

Hay dos formas de abrir el editor desde el lienzo:

  1. **Vista previa de salida de imagen** : pasa el cursor sobre la vista previa de salida de un nodo que produjo más de una imagen y luego haz clic en el botón de capas (**Abrir editor de capas**) en la esquina superior derecha de la vista previa.
  2. **Paleta de comandos** : selecciona un solo nodo y ejecuta **Abrir editor de capas para el nodo seleccionado**.

![El botón Abrir editor de capas en la vista previa de salida de un nodo que produjo dos imágenes](https://mintcdn.com/dripart/PMfXID7TToRohL16/images/interface/layer-editor/layer-editor-entrypoint.png?fit=max&auto=format&n=PMfXID7TToRohL16&q=85&s=581d97a055f752493a12803811358b13) El nodo debe tener al menos dos imágenes de salida. Si tiene menos de dos, ComfyUI informa que el editor de capas necesita al menos dos imágenes de salida. Crear imagen por capas también incluye un botón **Abrir Compositor** en el propio nodo. Esa ruta requiere que el flujo de trabajo se haya ejecutado al menos una vez para que las imágenes de entrada existan; de lo contrario, ComfyUI te pide que ejecutes el flujo de trabajo una vez para cargar las imágenes de entrada.

## 

​

Diseño del editor

El editor se abre como un diálogo de ventana completa con cuatro áreas: ![El diálogo del Editor de capas: panel de Capas a la izquierda, lienzo en el centro, Panel de Propiedades a la derecha](https://mintcdn.com/dripart/PMfXID7TToRohL16/images/interface/layer-editor/layer-editor-compositor.png?fit=max&auto=format&n=PMfXID7TToRohL16&q=85&s=bd7ba4ddcd236c46c09905e8c2030dce)

Área| Ubicación| Contenido  
---|---|---  
Encabezado| Arriba| Título del editor, **Restaurar** (solo en Crear imagen por capas) y cerrar  
Panel de Capas| Izquierda| Lista de capas, orden de las capas, visibilidad y la entrada de Fondo  
Lienzo| Centro| Vista previa en vivo del compuesto y la barra de herramientas flotante  
Panel de Propiedades| Derecha| Configuraciones de la capa seleccionada, o del fondo cuando no hay nada seleccionado  
  
## 

​

Herramientas y controles del lienzo

La barra de herramientas se ubica sobre el lienzo:

  * **Seleccionar** : elige y transforma capas en el lienzo.
  * **Mano** : desplaza el lienzo sin modificar las capas.
  * **Zoom** : preajustes de zoom de 25%, 50%, 100% y 200%, además de **Ajustar** para encajar toda la composición en la vista.
  * **Deshacer** y **Rehacer** : recorre tus ediciones paso a paso.
  * **Exportar PSD** : descarga la composición como un archivo PSD.



## 

​

Trabajar con capas

Selecciona una capa en el lienzo o en el panel Capas y, después, ajústala en el panel de propiedades:

Propiedad| Qué puedes cambiar  
---|---  
Posición| Ubicación X e Y de la capa en el lienzo  
Dimensiones| Ancho y alto de la capa  
Alineación| Alinear a la izquierda, centrar horizontalmente, a la derecha, arriba, centrar verticalmente o abajo  
Rotación| Rotar la capa  
Voltear| Voltear la capa horizontal o verticalmente  
Opacidad| Opacidad de la capa  
Modo de fusión| Cómo se fusiona la capa con las capas que están debajo  
  
Las capas se dibujan en el orden de la lista. Usa las acciones de subir y bajar en el panel Capas para cambiar qué capa queda encima, y el interruptor de visibilidad para ocultar una capa sin eliminarla. Los modos de fusión incluyen Normal, Multiplicar, Trama, Superponer, Oscurecer, Aclarar, Subexponer color, Sobreexponer color, Luz fuerte, Luz suave, Diferencia, Exclusión, Subexposición lineal, Sobreexposición lineal, Luz intensa, Luz focal, Luz lineal, Mezcla fuerte, Restar, Dividir, Extraer grano, Fusionar grano, Tono, Saturación, Color y Luminosidad. Selecciona la entrada **Fondo** en el panel Capas para editar la composición en sí en lugar de una capa: el ancho y el alto del lienzo (de 64 a 8192 píxeles) y el color de relleno del fondo (el control se llama **Relleno**).

## 

​

Guardar y exportar

Las ediciones que haces en Crear imagen por capas forman parte del flujo de trabajo: el estado de las capas se guarda automáticamente en el nodo, así que la composición se restaura cuando vuelves a abrir el flujo de trabajo. El nodo reproduce la composición almacenada cuando las entradas que registró siguen coincidiendo con la pila de capas actual; si ya no coinciden, vuelve a componer a partir de las propiedades de las capas y marca la composición almacenada como obsoleta. El botón **Restaurar** de la cabecera deshace todos los cambios realizados en la sesión y devuelve el lienzo al estado cargado desde el nodo. **Exportar PSD** descarga la composición como un archivo PSD con sus capas, que puedes abrir en un editor de imágenes como Photoshop. La exportación necesita WebGL en tu navegador; si WebGL no está disponible, el lienzo no puede renderizarse y la exportación falla.

## 

​

Páginas relacionadas

## Crear imagen por capas

Combina una pila de capas en una sola imagen.

## Agregar capa

Agrega una imagen a una pila de capas del compositor.

## Layers From Bounding Boxes

Crea capas del compositor a partir de cajas delimitadoras.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/layer-editor.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/layer-editor)

[Editor de máscara](https://docs.comfy.org/es/interface/maskeditor)[Descripción general](https://docs.comfy.org/es/interface/settings/overview)
