---
url: https://docs.comfy.org/es/interface/right-side-panel/
title: Panel derecho: Propiedades y errores de los nodos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.831407+00:00
---

# Panel derecho: Propiedades y errores de los nodos - ComfyUI

> Source: https://docs.comfy.org/es/interface/right-side-panel/

## En esta página

Volver arriba

  * Abrir y cerrar el panel
  * El panel sigue tu selección
    * Parámetros
    * Nodos
    * Información
    * Configuraciones
    * Errores
  * Entradas favoritas
  * Relacionado



Panel derecho

# Panel derecho: Propiedades y errores de los nodos

Copiar páginaCopiar página

Usa el panel derecho de ComfyUI para editar parámetros y ajustes de nodos, favoritos, estado del nodo y corregir errores del flujo.

Copiar páginaCopiar página

El Panel de Propiedades es el panel situado en el Lado derecho del Espacio de trabajo de ComfyUI. Muestra los Parámetros, la Información y las Configuraciones de lo que tengas Seleccionado en el Lienzo, mantiene las Entradas que más usas a un clic de distancia y enumera los errores del Flujo de trabajo junto con sus soluciones.

## 

​

Abrir y cerrar el panel

Haz clic en el icono del panel en el área de controles superior derecha para abrirlo. La información emergente del botón dice **Mostrar/ocultar panel de propiedades** , y cuando el flujo de trabajo tiene errores mientras el panel está cerrado, el botón muestra un punto rojo para que puedas abrir el panel directamente en la lista de errores. Cierra el panel desde el icono en su propio encabezado. ![Área de controles superior derecha de ComfyUI con el botón del panel de propiedades resaltado](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_button.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=54658426a24489c6a3fd458dc065428b) ComfyUI recuerda el estado del panel entre sesiones.

## 

​

El panel sigue tu selección

El título y las pestañas disponibles cambian según lo que esté seleccionado en el lienzo:

Selección| Título del panel| Pestañas  
---|---|---  
Nada| Resumen del flujo de trabajo| Parámetros, Nodos, Configuraciones  
Un nodo| El nombre del nodo| Parámetros, Información, Configuraciones, más Errores cuando corresponda  
Un nodo de subgrafo| El nombre del nodo| Parámetros, Configuraciones, más Errores cuando corresponda y el botón Editar subgrafo  
Varios elementos| El número de elementos seleccionados| Nodos, Configuraciones, más Errores cuando corresponda  
  
Haz clic en el botón de lápiz junto al título para cambiar el nombre del nodo o grupo seleccionado. Para un nodo de subgrafo, el encabezado también muestra un botón **Editar subgrafo** que abre el editor de subgrafos dentro del panel. La pestaña Errores aparece solo cuando la selección tiene errores relevantes, o cuando no hay nada seleccionado y el flujo de trabajo contiene errores. Puedes ocultar la pestaña por completo con el ajuste **Mostrar la pestaña de errores en el panel lateral** en `Comfy` → `Sistema de errores`.

### 

​

Parámetros

Con un nodo seleccionado, la pestaña **Parámetros** muestra sus entradas en **ENTRADAS**. Con varios elementos seleccionados, la misma vista se denomina **Nodos** y muestra las entradas de cada elemento seleccionado. Ambas vistas tienen un campo de búsqueda en la parte superior y una sección que se puede contraer por nodo. Las entradas marcadas como avanzadas se agrupan en una sección separada de **ENTRADAS AVANZADAS**. Cada entrada tiene un menú de acciones con **Renombrar** , **Favorito** y **Restablecer a predeterminado** , además de **Ocultar entrada** para las entradas promovidas desde un subgrafo. Cuando hay varios nodos seleccionados, cada sección también tiene un botón para localizar sus nodos en el lienzo. ![Panel del lado derecho con un nodo seleccionado, mostrando la pestaña Parámetros y su lista de ENTRADAS](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_parameters.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=aeded554ee84c0b44d7e44cc7fdcd9a9) Cuando no hay nada seleccionado, la misma pestaña muestra tus entradas favoritas en su lugar, para que puedas ajustar los valores que cambias con más frecuencia sin seleccionar un nodo primero.

### 

​

Nodos

La pestaña Nodos se muestra cuando no hay nada seleccionado. Enumera cada nodo del flujo de trabajo con sus entradas, con búsqueda y secciones que se pueden contraer, para que puedas revisar o editar cualquier nodo desde un solo lugar. También es la etiqueta que usa la vista de parámetros cuando hay varios elementos seleccionados.

### 

​

Información

La pestaña Información aparece para un único nodo seleccionado que no sea un subgrafo. Muestra el mismo contenido de ayuda de [Documentación de nodos](https://docs.comfy.org/es/interface/features/node-docs) que obtienes del icono de documentación de la caja de herramientas de selección y del botón de ayuda en Nodes 2.0.

### 

​

Configuraciones

Con una selección, la pestaña Configuraciones abarca los nodos y grupos seleccionados:

  * **Estado del nodo** : **Normal** , **Bypass** o **Mute**.
  * **Color del nodo** : elige un color para el nodo.
  * **Fijado** : fija el nodo para que permanezca en su lugar en el lienzo.

![Pestaña Configuraciones del panel del lado derecho con los controles de estado del nodo, color del nodo y fijado](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_settings.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=dbaec8a4b6a018140394fddc4f40ab4d) Los cambios se aplican a cada elemento de la selección, así que puedes establecer el mismo estado o color para todo un grupo a la vez. Los grupos solo exponen los controles de color y de fijado. Cuando no hay nada seleccionado, la pestaña se denomina **Configuración global** y reúne alternadores rápidos que replican el diálogo de configuración completo:

  * **Nodos** : Mostrar parámetros avanzados, Mostrar caja de herramientas al seleccionar, Nodes 2.0.
  * **Lienzo** : Espaciado de la cuadrícula, Ajustar nodos a la cuadrícula.
  * **Enlaces de conexión** : Forma del enlace, Mostrar enlaces conectados.
  * **Ver toda la configuración** : abre el diálogo de configuración completo.



### 

​

Errores

La pestaña Errores agrupa los problemas que bloquean el flujo de trabajo, para que puedas resolverlos antes de ejecutarlo:

  * **Errores de nodo** : el nodo que falla, el mensaje de error, un control para **Expand** y **Collapse** , y **Locate node on canvas**.
  * **Paquetes de nodos faltantes** : **Install All** , **Apply Changes** y **View in Manager** cuando ComfyUI Manager esté disponible. En Comfy Cloud, el grupo se denomina **Unsupported Node Packs** , ya que no puedes instalar paquetes de nodos allí.
  * **Modelos faltantes** : **Download** para un solo archivo o **Download all** , **Import** en Comfy Cloud para los modelos que proporciones tú mismo, y una nota cuando un modelo está restringido en Hugging Face y requiere una cuenta con sesión iniciada y la licencia aceptada.
  * **Entradas faltantes** : medios de entrada que el flujo de trabajo espera pero no puede encontrar.
  * **Registro de errores** y enlaces para enviar un issue en GitHub o contactar soporte.



## 

​

Entradas favoritas

Las entradas favoritas son los accesos directos del panel. Abre la pestaña Parámetros, haz clic en el menú de acciones de cualquier entrada y elige **Favorito**. Las entradas favoritas aparecen entonces en el panel siempre que no haya nada seleccionado, donde puedes buscarlas y reordenarlas. Usa **Quitar de favoritos** en el mismo menú para eliminar una. ![El panel del lado derecho en la pestaña Errores, mostrando una entrada faltante para el nodo Load Image con el botón de localizar](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_errors.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=076927960b2cf80d531b6f0b008d72a9) ![La pestaña Información mostrando la documentación integrada del nodo KSampler seleccionado](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_info.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=61fab494dd86b58e5f22fe89371a24db) ![El botón de alternar el Panel de Propiedades con el indicador de error mientras el panel está cerrado](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/right-side-panel/right_side_panel_error_badge.png?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=e1b930304ab8bcb9b9f552e817897cd1)

## 

​

Relacionado

  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview) para conocer las áreas del espacio de trabajo.
  * [Configuraciones de ComfyUI](https://docs.comfy.org/es/interface/settings/overview) para ver el diálogo completo de configuraciones.
  * [Documentación de nodos](https://docs.comfy.org/es/interface/features/node-docs) (el mismo contenido de ayuda que la pestaña Información).
  * [Biblioteca de nodos](https://docs.comfy.org/es/interface/node-library).



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/right-side-panel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/right-side-panel)

[Historial de trabajos](https://docs.comfy.org/es/interface/job-history)[Controles del lienzo](https://docs.comfy.org/es/interface/canvas-controls)
