---
url: https://docs.comfy.org/es/interface/app-mode/
title: Modo aplicaci\u00f3n de ComfyUI: crea y comparte flujos de trabajo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.353686+00:00
---

# Modo aplicación de ComfyUI: crea y comparte flujos de trabajo - ComfyUI

> Source: https://docs.comfy.org/es/interface/app-mode/

## En esta página

Volver arriba

  * Entrar en modo aplicación
  * Crear un flujo de trabajo en Modo App
    * Paso 1: Selecciona las entradas
    * Paso 2: Selecciona las salidas
    * Paso 3: Vista previa
    * Paso 4: Establece una vista predeterminada
  * Usa el modo App
  * Guarda y comparte el flujo de trabajo
    * Guardar flujo de trabajo
    * Compartir flujo de trabajo



Componentes de funciones

# Modo aplicación de ComfyUI: crea y comparte flujos de trabajo

Copiar páginaCopiar página

Aprende a crear y usar el modo aplicación de ComfyUI: define entradas y salidas personalizadas para simplificar el uso del flujo.

Copiar páginaCopiar página

El Modo App simplifica la interacción con los flujos de trabajo al permitirte definir interfaces de entrada y salida personalizadas, lo que facilita compartir y usar flujos de trabajo sin editar nodos.

El Modo App es compatible oficialmente desde la versión 1.41.13 del front-end de ComfyUI. Las versiones anteriores se encuentran en fase de pruebas inicial.

## 

​

Entrar en modo aplicación

Hay dos formas de entrar en el modo aplicación: haz clic en el icono de la esquina superior izquierda (**1**) y selecciona **Entrar en modo aplicación** en el menú desplegable, o usa el menú desplegable de la ruta de navegación (**2**) en la parte superior de la interfaz. ![Entrar en modo aplicación desde el menú superior izquierdo](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_1.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=3c8daee576fd15e1a53a8abd44af7283)

  1. Haz clic en el icono de la esquina superior izquierda (marcado con **1**) para abrir el menú desplegable y selecciona **Entrar en modo aplicación**.
  2. Como alternativa, usa el menú desplegable de la ruta de navegación (marcado con **2**) en la parte superior para entrar en el modo aplicación.



## 

​

Crear un flujo de trabajo en Modo App

Si el flujo de trabajo nunca se ha configurado para el Modo App, al entrar en Modo App se abrirá automáticamente el constructor de aplicaciones. ![Pantalla de entrada del constructor de aplicaciones](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_2.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=9a454584b80a132f6270bd80de067120)

  1. Si el flujo de trabajo no tiene ninguna configuración de Modo App, el constructor de aplicaciones se abre de forma predeterminada.
  2. Haz clic en **Entrar al constructor de aplicaciones** para abrir el constructor y empezar a configurar.



### 

​

Paso 1: Selecciona las entradas

La interfaz del constructor muestra cuatro pasos guiados (marcados como **1** , **2** , **3** , **4**) en la parte superior. La barra inferior te permite salir del constructor o navegar entre pasos. ![Vista general de la interfaz del constructor de aplicaciones](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_3.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=55d218dc7427a34d6e8fd29a24f75d88)

  1. Los números **1 2 3 4** de la parte superior corresponden a los cuatro pasos de creación: seleccionar entradas, seleccionar salidas, previsualizar y establecer la vista predeterminada.
  2. Los botones de la parte inferior te permiten salir del constructor o moverte entre pasos.
  3. Las áreas marcadas en el lienzo son parámetros de entrada/salida que se pueden seleccionar.
  4. El panel derecho muestra una vista previa en vivo de la configuración actual.

Haz clic en el paso **Entradas** de la parte superior. El lienzo resalta los nodos de entrada que se pueden seleccionar. Haz clic en un nodo para seleccionarlo como parámetro de entrada: las opciones incluyen carga de imágenes, entradas de prompt de texto y selección de modelo. Los parámetros seleccionados aparecen en la barra lateral derecha.

### 

​

Paso 2: Selecciona las salidas

Haz clic en el paso **Salidas**. Elige qué nodos de salida mostrar en la App, como un nodo Preview Image o un nodo Save Image. ![Selección de nodos de salida con vista previa en el panel derecho](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_4.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=3da63ddf5f39682e821b05b13e0b391d)

  1. Selecciona los nodos de salida que se mostrarán en la App.
  2. Al igual que con las entradas, la barra lateral derecha muestra una vista previa en vivo de los nodos de salida seleccionados.



### 

​

Paso 3: Vista previa

Haz clic en el paso **Vista previa** para revisar el diseño final de la App. Las entradas seleccionadas aparecen en el panel derecho y el área de salida se muestra en el lienzo. ![Modo de vista previa mostrando el diseño de entradas y salidas](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_5.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=457267923842de9c0896bb2293aa5e38)

  1. Este es el modo de vista previa: comprueba que todas las configuraciones de entrada y salida aparezcan como se espera.
  2. Si necesitas hacer ajustes, haz clic en **Anterior** para volver al paso previo.



### 

​

Paso 4: Establece una vista predeterminada

Haz clic en el paso **Establecer una vista predeterminada**. Elige si el flujo de trabajo debe abrirse de forma predeterminada en modo **App** o en modo **Grafo de nodos**. Haz clic en **Aplicar** para confirmar. ![Paso de vista predeterminada con las opciones App y Grafo de nodos](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_6.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ec36d6fd020ad0615d793250f4223d5f)

  1. Elige si el flujo de trabajo se abre de forma predeterminada en modo **App** o en modo **Grafo de nodos**.
  2. Selecciona **App** y haz clic en **Aplicar** para confirmar. A partir de entonces, el flujo de trabajo se abrirá en Modo App de forma predeterminada.

Después de aplicar los cambios, aparecerá un mensaje de confirmación. ![Mensaje de confirmación con el botón Ver aplicación](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_7.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ac6ce14aa972d805f57d1c0cd37752f1) Haz clic en **Ver aplicación** para entrar en Modo App y empezar a usar el flujo de trabajo.

## 

​

Usa el modo App

En el modo App, el panel derecho muestra todas las opciones de entrada configuradas. Ajusta las entradas según sea necesario y luego haz clic en **Run** para ejecutar el flujo de trabajo. ![Interfaz del modo App con el panel de entradas y el botón Ejecutar](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_8.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=758765a3cfeaccdc8b2460332c15d318)

  1. El panel **Entrada** de la derecha te permite ajustar los parámetros de entrada antes de ejecutar.
  2. Haz clic en **Run** para ejecutar el flujo de trabajo.
  3. La barra lateral izquierda ofrece controles adicionales, como reconstruir la App, ver los recursos y abrir el panel del flujo de trabajo.

El modo App también está optimizado para diseños móviles y de pantalla estrecha. La interfaz se adapta a una vista basada en pestañas, lo que te permite cambiar entre el panel de entrada, la vista de salida y el panel de Recursos multimedia. ![Diseño móvil del modo App con las pestañas de entradas, salidas y recursos](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_15.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=6812f8d01533cbf935c7f66fe68e638e) Mientras se ejecuta, aparece un botón **Cancelar esta ejecución** en la parte superior para detener la ejecución actual. ![Estado de ejecución con la opción de cancelar y el panel de resultados](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_9.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ed115b64ed6c910f26ed801af6b37493)

  1. Haz clic en **Cancelar esta ejecución** en la parte superior para detener la ejecución actual.
  2. Cambia entre la vista de cola y la vista de resultados en el panel inferior.
  3. Haz clic en el área correspondiente para abrir el panel de recursos.



## 

​

Guarda y comparte el flujo de trabajo

### 

​

Guardar flujo de trabajo

Usa `Ctrl + S` (o `Cmd + S` en Mac) para guardar el flujo de trabajo y reutilizarlo más adelante. Haz clic en el botón de la barra lateral izquierda para abrir el panel de flujos de trabajo guardados. ![Barra lateral izquierda que muestra flujos de trabajo APP guardados](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_11.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=6433652fefd4a49791e6dc22985821d1)

  1. Haz clic en el botón de la barra lateral izquierda para abrir el panel, que muestra todos los flujos de trabajo APP guardados.
  2. Cambia entre los flujos de trabajo APP guardados desde este panel.



### 

​

Compartir flujo de trabajo

En el modo App, haz clic en el botón **Compartir** de la barra lateral izquierda. Si el flujo de trabajo aún no se ha guardado, un cuadro de diálogo te pedirá que lo guardes primero antes de poder crear un enlace. ![Cuadro de diálogo para compartir que solicita guardar el flujo de trabajo](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_12.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=c1181a5a379c95a1e7f7bfaeea838d07)

  1. Haz clic en el botón Compartir de la barra lateral izquierda para abrir el cuadro de diálogo Compartir.
  2. Si el flujo de trabajo no está guardado, introduce un nombre para el flujo de trabajo y haz clic en **Guardar flujo de trabajo** para continuar.

Una vez guardado, el cuadro de diálogo Compartir muestra la opción de generar un enlace. ![Cuadro de diálogo para compartir con el botón Crear un enlace](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_13.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=4bc962ef36b0edd6941468de3d8ffa9b) Haz clic en **Crear un enlace** para generar una URL compartible del flujo de trabajo. ![Cuadro de diálogo para compartir que muestra el enlace generado con el botón Copiar](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_14.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=32360bed156ac214b248a392e9630dfe) Haz clic en **Copiar** para copiar el enlace. Quienes lo reciban pueden abrirlo y ejecutar el flujo de trabajo directamente: la configuración completa del flujo de trabajo está incluida en el enlace.

Los enlaces para compartir solo son compatibles con Comfy Cloud.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/app-mode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/app-mode)

[Plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template)[Subgrafo](https://docs.comfy.org/es/interface/features/subgraph)
