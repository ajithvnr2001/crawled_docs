---
url: https://docs.comfy.org/es/interface/canvas-controls/
title: Controles del lienzo - Minimapa, zoom y modo de enfoque - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.609540+00:00
---

# Controles del lienzo - Minimapa, zoom y modo de enfoque - ComfyUI

> Source: https://docs.comfy.org/es/interface/canvas-controls/

## En esta página

Volver arriba

  * Barra de herramientas del lienzo
  * Menú Ver
  * Modo de enfoque
  * Opciones del minimapa
  * Enlaces y globales del lienzo
    * Seleccionar enlaces
  * Páginas relacionadas



Lienzo

# Controles del lienzo - Minimapa, zoom y modo de enfoque

Copiar páginaCopiar página

Usa los controles del lienzo y el menú Ver: minimapa, visibilidad de enlaces, información, zoom, ajustar vista, modos Seleccionar/Mano y Enfoque.

Copiar páginaCopiar página

La barra de herramientas del lienzo de la esquina inferior derecha y el menú **Ver** controlan cómo te mueves por el gráfico. Los comandos principales del menú Ver incluyen Alternar panel inferior, Explorar plantillas, **Modo de enfoque** , información de rendimiento del lienzo, minimapa, visibilidad de enlaces, acercar/alejar y ajustar vista. ![La barra de herramientas del lienzo de la esquina inferior derecha con el minimapa abierto](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_toolbar.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=cd8c2ef1bdec81bd8c730b3a3c0159a4) ![Modo de enfoque activado: el marco del espacio de trabajo está oculto y se muestra un control de menú hamburguesa](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_focus_mode.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=fe9f3b0f77c39731e2d77a5147c16b2d) ![Visibilidad de enlaces activada: los nodos conectados se unen mediante cables](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_links_visible.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=4e20906792a1924523e3da25bdd920ac) ![Visibilidad de enlaces desactivada: los nodos permanecen en el lienzo pero los cables de conexión están ocultos](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/canvas-controls/canvas_links_hidden.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=2fb86dd45ba7907910bfdc0cfcf4e3b9)

## 

​

Barra de herramientas del lienzo

Cuando **Mostrar menú del lienzo del gráfico** (`Comfy.Graph.CanvasMenu`) está activado (predeterminado), una barra de herramientas flotante se ubica en la esquina inferior derecha del lienzo:

Control| Qué hace  
---|---  
**Modo lienzo**|  Menú para cambiar entre **Seleccionar** (editar nodos) y **Mano** (solo desplazamiento / lienzo de solo lectura). Valores predeterminados: `v` desbloquea Seleccionar, `h` bloquea Mano.  
**Ajustar vista**|  Encuadra el gráfico en el área de visualización (`Comfy.Canvas.FitView`, predeterminado `.`).  
**Zoom**|  Abre un panel emergente con Acercar, Alejar, Ajustar zoom y un campo de porcentaje (1-1000%). Los atajos predeterminados incluyen `Alt` \+ `=` / `Alt` \+ `-` para acercar/alejar.  
**Minimapa**|  Activa o desactiva el mapa de vista general (`Comfy.Canvas.ToggleMinimap`, predeterminado `Alt` \+ `Shift` \+ `M`). Se conserva como `Comfy.Minimap.Visible`.  
**Visibilidad de enlaces**|  Oculta o muestra los cables de conexión al alternar el modo de renderizado de enlace oculto (`Comfy.Canvas.ToggleLinkVisibility`).  
  
Puedes ocultar toda la barra de herramientas con **Mostrar menú del lienzo del gráfico** en las configuraciones de Lite Graph / Lienzo.

## 

​

Menú Ver

El menú **Ver** registra los mismos comandos de navegación para que puedas ejecutarlos desde la barra de menú o la paleta de comandos:

  * Alternar panel inferior
  * Explorar plantillas
  * Modo de enfoque
  * Rendimiento del Lienzo (`Comfy.ToggleCanvasInfo`, alterna `Comfy.Graph.CanvasInfo`)
  * Alternar minimapa
  * Alternar visibilidad de enlace
  * Acercar / Alejar / Ajustar vista



## 

​

Modo de enfoque

El **Modo de enfoque** (`Workspace.ToggleFocusMode`) oculta los elementos del espacio de trabajo para que puedas concentrarte en el gráfico. Mientras está activado:

  * La sección del menú superior queda oculta (menú nuevo).
  * Los paneles de la barra lateral izquierda y derecha, y el panel inferior, no se renderizan en el diseño dividido.
  * Aparece un control de tipo hamburguesa para que puedas salir del modo de enfoque (**Mostrar menú**).

Alterna el modo de enfoque de nuevo, o usa el control de hamburguesa, para restaurar el espacio de trabajo completo.

## 

​

Opciones del minimapa

Además de mostrar u ocultar, las Configuraciones de Minimapa controlan lo que dibuja el minimapa (colores de nodos, conexiones, grupos, estado de omisión, estado de error). Consulta [Configuraciones de Lite Graph](https://docs.comfy.org/es/interface/settings/lite-graph) y las entradas relacionadas de Apariencia cuando estén presentes.

## 

​

Enlaces y globales del lienzo

La forma del enlace y si se muestran los enlaces conectados también están disponibles como alternancias rápidas en **Configuración global** del [Panel derecho](https://docs.comfy.org/es/interface/right-side-panel) cuando no hay nada seleccionado, y de forma completa en la configuración de Lite Graph (`Comfy.LinkRenderMode` y opciones relacionadas). El espaciado de la cuadrícula y el ajuste a la cuadrícula se encuentran en las mismas áreas de Configuración global / Lite Graph.

### 

​

Seleccionar enlaces

Requiere ComfyUI frontend 1.58.0 o posterior. Seleccionar enlaces con un marco es el comportamiento predeterminado del lienzo en el Modo de selección (no es una opción de configuración). Arrastra un marco sobre los cables de conexión en los que quieras actuar. Un marco que no capture nodos, grupos ni redireccionamientos selecciona todos los enlaces visibles que cruza, y la caja de herramientas de selección reemplaza sus botones de nodo por dos acciones de enlace: **Ocultar** , que mantiene la conexión y oculta el cable, y **Eliminar** , que quita el enlace del gráfico. Cada acción es un paso de deshacer, y `Delete` o `Backspace` también eliminan una selección de enlaces. Los marcos con `Shift` y `Alt` seleccionan solo nodos y grupos, y el Modo lienzo Mano nunca selecciona enlaces.

## 

​

Páginas relacionadas

  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview)
  * [Atajos](https://docs.comfy.org/es/interface/shortcuts)
  * [Configuraciones de Lite Graph](https://docs.comfy.org/es/interface/settings/lite-graph)
  * [Panel del lado derecho](https://docs.comfy.org/es/interface/right-side-panel) (alternadores rápidos de Configuración global)
  * [Panel inferior](https://docs.comfy.org/es/interface/bottom-panel)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/canvas-controls.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/canvas-controls)

[Panel derecho](https://docs.comfy.org/es/interface/right-side-panel)[Nodes 2.0](https://docs.comfy.org/es/interface/nodes-2)
