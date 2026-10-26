---
url: https://docs.comfy.org/es/interface/settings/lite-graph/
title: Configuraciones de ComfyUI LiteGraph (Lienzo) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:30.437566+00:00
---

# Configuraciones de ComfyUI LiteGraph (Lienzo) - ComfyUI

> Source: https://docs.comfy.org/es/interface/settings/lite-graph/

## En esta página

Volver arriba

  * Lienzo
    * Mostrar caja de herramientas de selección
    * Selección en vivo
    * Nivel de detalle de nodos al hacer zoom (umbral de tamaño de fuente)
    * FPS máximo
    * Siempre ajustar a la cuadrícula
    * Tamaño de la cuadrícula para ajustar
    * Habilitar el atajo de zoom rápido (Ctrl + Shift + Arrastrar)
    * Mostrar menú del lienzo del gráfico
    * Velocidad de zoom del lienzo
    * Mostrar información del lienzo en la esquina inferior izquierda (FPS, etc.)
    * Velocidad de auto-desplazamiento
  * Navegación del lienzo
    * Modo de navegación del lienzo
    * Comportamiento del clic izquierdo del ratón
    * Desplazamiento de la rueda del ratón
  * Menú contextual
    * Escalar los menús (listas) de los widgets combo de los nodos al hacer zoom
  * Gráfico
    * Modo de renderizado de enlace
  * Grupo
    * Haz doble clic en el título del grupo para editarlo
    * Relleno de nodos seleccionados en grupo
    * Seleccionar los elementos del grupo al hacer clic
  * Enlace
    * Marcadores de punto medio de enlace
  * Liberación de enlace
    * Acción al liberar enlace (Shift)
    * Acción al liberar enlace (Sin modificador)
  * Nodo
    * Reducir siempre los nuevos nodos
    * Habilitar el recorte de elementos DOM (habilitarlo puede reducir el rendimiento)
    * El clic central crea un nuevo nodo de reenrutamiento
    * Mantener todos los enlaces al eliminar nodos
    * Resaltar nodo al ajustar enlace
    * Ajustar automáticamente el enlace a la ranura del nodo
    * Habilitar tooltips
    * Retraso de la información sobre herramientas
    * Modo de insignia de ciclo de vida del nodo
    * Modo de insignia de ID de nodo
    * Modo de insignia de fuente de nodo
    * Haz doble clic en el título del nodo para editarlo
  * Widget de nodo
    * Decimales de redondeo del widget flotante [0 = automático]
    * Desactivar el redondeo predeterminado del widget flotante
    * Desactivar los deslizadores del widget del nodo
    * Mostrar siempre los widgets avanzados en todos los nodos
    * Formato de imagen de vista previa
    * Mostrar ancho × alto debajo de la vista previa de imagen
  * Puntero
    * Habilitar gestos del panel táctil
    * Intervalo de doble clic (máximo)
    * Deriva del clic del puntero (distancia máxima)
  * Reroute
    * Desplazamiento de spline de reenrutamiento



Configuraciones de ComfyUI

# Configuraciones de ComfyUI LiteGraph (Lienzo)

Copiar páginaCopiar página

Descripción detallada de las opciones de configuración de LiteGraph, el motor de renderizado gráfico de ComfyUI

Copiar páginaCopiar página

Las configuraciones descritas en esta página se encuentran en el **menú de configuraciones dentro de la aplicación de ComfyUI**. Puedes abrirlo navegando a **Configuraciones** (icono de engranaje) o usando el atajo de teclado `Ctrl + ,`, y luego seleccionar la categoría correspondiente para ver y configurar estas opciones.

LiteGraph es el motor de renderizado gráfico subyacente de ComfyUI. Las configuraciones de esta categoría controlan principalmente el comportamiento y la apariencia de las interfaces gráficas, como el lienzo, los nodos y las conexiones.

## 

​

Lienzo

### 

​

Mostrar caja de herramientas de selección

  * **Valor predeterminado** : Habilitado
  * **Función** : La caja de herramientas de selección es una barra de herramientas flotante de acciones rápidas que aparece sobre los nodos después de seleccionarlos, y ofrece operaciones rápidas comunes como ejecución parcial, fijar, eliminar, cambiar el color, etc.

![Mostrar caja de herramientas de selección](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/selection-toolbox.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=477b7ea42f5c0d270240538fad73c60f)

### 

​

Selección en vivo

  * **Valor predeterminado** : Habilitado
  * **Función** : Cuando está habilitada, los nodos se seleccionan y deseleccionan en tiempo real mientras arrastras un rectángulo de selección, de forma similar a otras herramientas de diseño



### 

​

Nivel de detalle de nodos al hacer zoom (umbral de tamaño de fuente)

  * **Valor predeterminado** : 8
  * **Rango** : 0 - 24
  * **Función** : Establece cuándo cambian los nodos a una representación simplificada del nivel de detalle mientras alejas la vista, medido como un tamaño de fuente mínimo en píxeles. Los valores más altos hacen que los nodos cambien antes a la representación simplificada, los valores más bajos mantienen la calidad completa de los nodos por más tiempo, y 0 desactiva por completo el cambio de nivel de detalle. Los diferentes modos de representación se muestran a continuación

![Representación de baja calidad](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/render-mode.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=cd5b2cb2c03dc6ef09eb42350358f5b9)

### 

​

FPS máximo

  * **Valor predeterminado** : 0 (usar la frecuencia de actualización de la pantalla)
  * **Rango** : 0 - 120
  * **Función** : Limita la frecuencia de cuadros de representación del lienzo. 0 significa usar la frecuencia de actualización de la pantalla. Un FPS más alto hará que la representación del lienzo sea más fluida, pero también consumirá más rendimiento. Los valores demasiado bajos provocarán un tartamudeo más evidente.



### 

​

Siempre ajustar a la cuadrícula

  * **Valor predeterminado** : Deshabilitado
  * **Función** : Cuando esta opción no está habilitada, puedes mantener presionada la tecla `Shift` para alinear los bordes de los nodos con la cuadrícula. Cuando está habilitada, los bordes de los nodos se alinearán automáticamente con la cuadrícula sin necesidad de mantener presionada la tecla `Shift`.



### 

​

Tamaño de la cuadrícula para ajustar

  * **Valor predeterminado** : 10
  * **Rango** : 1 - 500
  * **Función** : Cuando el ajuste automático está habilitado o cuando mueves nodos mientras mantienes presionada la tecla `Shift`, este parámetro determina el tamaño de la cuadrícula para el ajuste. El valor predeterminado es 10 y puedes ajustarlo según tus necesidades.



### 

​

Habilitar el atajo de zoom rápido (Ctrl + Shift + Arrastrar)

  * **Valor predeterminado** : Habilitado
  * **Función** : Habilita la función de zoom rápido con `Ctrl + Shift + Clic izquierdo y arrastrar`, lo que proporciona un método de zoom más rápido



### 

​

Mostrar menú del lienzo del gráfico

  * **Valor predeterminado** : Habilitado
  * **Función** : Controla si se muestra el menú del lienzo en la esquina inferior derecha

El menú del lienzo se encuentra en la esquina inferior derecha de toda la interfaz de ComfyUI y contiene operaciones como el zoom del lienzo, ocultar temporalmente todas las conexiones, escalar rápidamente el flujo de trabajo para que se ajuste al lienzo, etc., como se muestra en la imagen a continuación ![Mostrar menú del lienzo del gráfico](https://mintcdn.com/dripart/A0ohfUGOp7aobXHn/images/interface/setting/lite-graph/canvas_menu.jpg?fit=max&auto=format&n=A0ohfUGOp7aobXHn&q=85&s=d4ae22081d9b4ecf741867f749360f6c)

### 

​

Velocidad de zoom del lienzo

  * **Valor predeterminado** : 1.1
  * **Rango** : 1.01 - 2.5
  * **Función** : Controla la velocidad del zoom del lienzo y ajusta la sensibilidad del zoom con la rueda del mouse



### 

​

Mostrar información del lienzo en la esquina inferior izquierda (FPS, etc.)

  * **Valor predeterminado** : Habilitado
  * **Función** : Controla si se muestra la información del lienzo en la esquina inferior izquierda, mostrando métricas de rendimiento como los FPS

![Información del lienzo](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/lite-graph/canvas-info.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=7ecbaf0b57b8ab66d8df31779e5f5926)

### 

​

Velocidad de auto-desplazamiento

  * **Valor predeterminado** : 15
  * **Rango** : 0 - 30
  * **Función** : Establece la velocidad máxima que se usa cuando el lienzo se desplaza automáticamente al arrastrar un nodo o un enlace contra el borde del lienzo. Establécelo en 0 para desactivar el auto-desplazamiento



## 

​

Navegación del lienzo

### 

​

Modo de navegación del lienzo

  * **Valor predeterminado** : Navegación por arrastre
  * **Opciones** : Estándar (Nuevo), Navegación por arrastre, Personalizado
  * **Función** : Selecciona un ajuste preestablecido para los dos comportamientos de navegación del lienzo que se describen a continuación. Estándar (Nuevo) selecciona con el botón izquierdo del ratón y desplaza con la rueda del ratón, Navegación por arrastre (el valor predeterminado) desplaza con el botón izquierdo del ratón y acerca/aleja con la rueda del ratón, y Personalizado mantiene lo que hayas configurado para cada comportamiento de forma individual. Si cambias cualquiera de los comportamientos respecto a su ajuste preestablecido, esta opción pasa a Personalizado.



### 

​

Comportamiento del clic izquierdo del ratón

  * **Valor predeterminado** : Desplazamiento
  * **Opciones** : Desplazamiento, Seleccionar
  * **Función** : Define qué hace arrastrar con el botón izquierdo del ratón sobre una parte vacía del lienzo: desplazar el lienzo o dibujar un rectángulo de selección.



### 

​

Desplazamiento de la rueda del ratón

  * **Valor predeterminado** : Acercar/alejar
  * **Opciones** : Desplazamiento, Acercar/alejar
  * **Función** : Define qué hace la rueda del ratón en el lienzo: acercar y alejar, o desplazar verticalmente.



## 

​

Menú contextual

### 

​

Escalar los menús (listas) de los widgets combo de los nodos al hacer zoom

  * **Valor predeterminado** : Desactivado
  * **Función** : Controla si se escalan los menús (listas) de los widgets combo de los nodos al hacer zoom, lo que permite a los usuarios seleccionar los widgets combo de los nodos



## 

​

Gráfico

### 

​

Modo de renderizado de enlace

  * **Valor predeterminado** : 2 (Spline)
  * **Opciones** : Recto, Lineal, Spline, Oculto
  * **Función** : Establece el estilo de renderizado de las conexiones, controlando el estilo visual de los enlaces entre nodos

![Modo de renderizado de enlace](https://mintcdn.com/dripart/EeFKEryMLH5667kk/images/interface/setting/lite-graph/link-render-mode.jpg?fit=max&auto=format&n=EeFKEryMLH5667kk&q=85&s=7e84452d1f5a5a71def87b3d27c95462)

## 

​

Grupo

Esta sección de configuraciones está relacionada principalmente con la funcionalidad de grupos de nodos. ![Grupo de nodos](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-group.png?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=02765d28e1720e5cc0bc2f6a1f70ab02)

### 

​

Haz doble clic en el título del grupo para editarlo

  * **Valor predeterminado** : Habilitado
  * **Función** : Controla si puedes hacer doble clic en el título del nodo para editarlo, lo que permite renombrar nodos; está marcado como la parte `1` en la imagen



### 

​

Relleno de nodos seleccionados en grupo

  * **Valor predeterminado** : 10
  * **Rango** : 0 - 100
  * **Función** : Establece el relleno interno al agrupar nodos seleccionados, controlando el espacio entre el marco del grupo y los nodos; está marcado como la parte `2` señalada por la flecha en la imagen



### 

​

Seleccionar los elementos del grupo al hacer clic

  * **Valor predeterminado** : Deshabilitado
  * **Función** : Cuando está habilitado, al hacer clic en un grupo se seleccionan todos los nodos y elementos que contiene



## 

​

Enlace

### 

​

Marcadores de punto medio de enlace

  * **Valor predeterminado** : Círculo
  * **Opciones** : Ninguno, Círculo, Flecha
  * **Función** : Establece el estilo del marcador en los puntos medios de los enlaces, mostrando indicadores de dirección en dichos puntos.

![Marcadores de punto medio de enlace](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/setting/lite-graph/link-midpoint.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=8657ef27abace2e70e48f25300bde988)

## 

​

Liberación de enlace

Esta sección del menú actualmente controla principalmente las operaciones relacionadas cuando se liberan las conexiones de enlace. Las dos operaciones relacionadas actuales son: **Aparecerá una lista de recomendación de nodos relacionada con la entrada/salida actual después de liberar** **Se abrirá una caja de búsqueda después de liberar**

### 

​

Acción al liberar enlace (Shift)

  * **Valor predeterminado** : caja de búsqueda
  * **Opciones** : menú contextual, caja de búsqueda, sin acción
  * **Función** : establece la acción al liberar enlaces mientras se mantiene presionada la tecla Shift, comportamiento especial al liberar enlaces mientras se mantiene Shift



### 

​

Acción al liberar enlace (Sin modificador)

  * **Valor predeterminado** : menú contextual
  * **Opciones** : menú contextual, caja de búsqueda, sin acción
  * **Función** : establece la acción predeterminada al liberar enlaces, controla el comportamiento después de arrastrar y liberar enlaces



## 

​

Nodo

### 

​

Reducir siempre los nuevos nodos

  * **Valor predeterminado** : Deshabilitado
  * **Función** : Controla si los nodos se reducen automáticamente al crearlos, de modo que siempre se muestren con el tamaño mínimo; sin embargo, puede provocar que parte del texto se trunque al agregarlo, por lo que tendrás que ajustar manualmente el tamaño del nodo



### 

​

Habilitar el recorte de elementos DOM (habilitarlo puede reducir el rendimiento)

  * **Valor predeterminado** : Habilitado
  * **Función** : Habilita el recorte de elementos DOM (puede afectar el rendimiento); optimiza el renderizado, pero puede reducir el rendimiento



### 

​

El clic central crea un nuevo nodo de reenrutamiento

  * **Valor predeterminado** : Habilitado
  * **Función** : Crea un nuevo nodo de reenrutamiento al hacer clic con el botón central, lo que permite crear rápidamente nodos de reenrutamiento para organizar las conexiones



### 

​

Mantener todos los enlaces al eliminar nodos

  * **Valor predeterminado** : Habilitado
  * **Función** : Omite automáticamente las conexiones al eliminar nodos intermedios; intenta reconectar los enlaces de entrada y salida al eliminar nodos



### 

​

Resaltar nodo al ajustar enlace

  * **Valor predeterminado** : Habilitado
  * **Función** : Resalta los nodos cuando arrastras enlaces hacia ellos, proporciona retroalimentación visual y muestra qué nodos se pueden conectar. Cuando está habilitado, el efecto es el que se muestra en la imagen a continuación: el lado correspondiente del enlace se mostrará con un estilo resaltado

![Resaltar nodo al ajustar enlace](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/highlights-node.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=242f3b88d95229d99744f720cf86c935)

### 

​

Ajustar automáticamente el enlace a la ranura del nodo

  * **Valor predeterminado** : Habilitado
  * **Función** : Se ajusta automáticamente a las ranuras disponibles cuando arrastras enlaces hacia los nodos, simplifica las operaciones de conexión y encuentra automáticamente las ranuras de entrada adecuadas



### 

​

Habilitar tooltips

  * **Valor predeterminado** : Habilitado
  * **Función** : Algunos datos de los nodos incluyen tooltips, como las descripciones de los parámetros, etc. Cuando está habilitado, estos tooltips se mostrarán al pasar el mouse por encima, como se muestra en la imagen a continuación

![Habilitar tooltips](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/lite-graph/tooltips.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=df329458465d6f20efea955e638c9656)

### 

​

Retraso de la información sobre herramientas

  * **Valor predeterminado** : 500
  * **Rango** : 100 - 3000
  * **Función** : Controla el retraso antes de que aparezca una información sobre herramientas, en milisegundos



### 

​

Modo de insignia de ciclo de vida del nodo

  * **Valor predeterminado** : Mostrar todo
  * **Función** : Controla la visualización de los marcadores de ciclo de vida del nodo, mostrando información del estado del nodo



### 

​

Modo de insignia de ID de nodo

  * **Valor predeterminado** : Ninguno
  * **Función** : Controla la visualización de los marcadores de ID de nodo, mostrando los identificadores únicos de los nodos

![Modo de insignia de ID de nodo](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-id-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=ca8e1edfff6c7673f1432ba0ac2edde5)

### 

​

Modo de insignia de fuente de nodo

  * **Valor predeterminado** : Ocultar incorporados
  * **Opciones** : 
    * Ninguno
    * Ocultar incorporados
    * Mostrar todo
  * **Función** : Controla el modo de visualización de los marcadores de fuente de nodo, mostrando información sobre la fuente de los nodos. El efecto correspondiente se muestra en la imagen a continuación. Si seleccionas Mostrar todo, se mostrarán etiquetas tanto para los nodos personalizados como para los nodos incorporados, lo que te facilitará determinar la fuente del nodo correspondiente. El logotipo del zorro representa los nodos incorporados de ComfyUI

![Modo de insignia de fuente de nodo](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/node-source-badge.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=383afc337b63f52be2f8d3cb9e7c4ed7)

### 

​

Haz doble clic en el título del nodo para editarlo

  * **Valor predeterminado** : Habilitado
  * **Función** : Controla si puedes hacer doble clic en el título del nodo para editarlo, lo que te permite renombrar los nodos



## 

​

Widget de nodo

### 

​

Decimales de redondeo del widget flotante [0 = automático]

  * **Valor predeterminado** : 0 (automático)
  * **Rango** : 0 - 6
  * **Función** : Establece los decimales para el redondeo del widget flotante; 0 significa automático; requiere recargar la página



### 

​

Desactivar el redondeo predeterminado del widget flotante

  * **Valor predeterminado** : Desactivado
  * **Función** : Controla si se desactiva el redondeo predeterminado del widget flotante; requiere recargar la página; no se puede desactivar cuando el backend del nodo ha establecido el redondeo



### 

​

Desactivar los deslizadores del widget del nodo

  * **Valor predeterminado** : Desactivado
  * **Función** : Controla si se desactivan los controles de deslizador en los widgets de los nodos, forzando la entrada de texto en lugar de deslizadores



### 

​

Mostrar siempre los widgets avanzados en todos los nodos

  * **Valor predeterminado** : Desactivado
  * **Función** : Cuando está habilitado, los widgets avanzados siempre están visibles en todos los nodos sin necesidad de expandir cada nodo individualmente



### 

​

Formato de imagen de vista previa

  * **Valor predeterminado** : Cadena vacía (usar el formato original)
  * **Función** : Establece el formato de las imágenes de vista previa en los widgets de imagen; convierte a formatos ligeros como webp, jpeg, etc.



### 

​

Mostrar ancho × alto debajo de la vista previa de imagen

  * **Valor predeterminado** : Habilitado
  * **Función** : Muestra la información de Ancho × Alto debajo de las vistas previas de imagen, mostrando la información de dimensiones de la imagen

![Mostrar Ancho × Alto debajo de la vista previa de imagen](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/show-size.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=e7fdfd5227158a413b5b0051a6e171bf)

## 

​

Puntero

### 

​

Habilitar gestos del panel táctil

  * **Valor predeterminado** : Activado
  * **Función** : Esta opción habilita el modo de panel táctil para el lienzo, permitiendo el zoom con pellizco de dos dedos y el arrastre.



### 

​

Intervalo de doble clic (máximo)

  * **Valor predeterminado** : 300
  * **Función** : Tiempo máximo (en milisegundos) entre dos clics de un doble clic. Aumentar este valor ayuda a resolver problemas en los que a veces no se reconoce el doble clic.



### 

​

Deriva del clic del puntero (distancia máxima)

  * **Valor predeterminado** : 6
  * **Función** : Si el puntero se desplaza más que esta distancia mientras mantienes pulsado el botón, se considera un arrastre (en lugar de un clic). Ayuda a evitar movimientos accidentales del ratón al hacer clic.



## 

​

Reroute

### 

​

Desplazamiento de spline de reenrutamiento

  * **Valor predeterminado** : 20
  * **Función** : Se utiliza para determinar la suavidad de las curvas a ambos lados de los nodos de reenrutamiento. Los valores más grandes hacen que las curvas sean más suaves; los valores más pequeños, más marcadas.

![Desplazamiento de spline de reenrutamiento](https://mintcdn.com/dripart/qYv6P0RgI3co7-eH/images/interface/setting/lite-graph/reroute-spline-offset.jpg?fit=max&auto=format&n=qYv6P0RgI3co7-eH&q=85&s=a76bc935bc5e37fe1b3c99129c7b5fe3)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/settings/lite-graph.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/settings/lite-graph)

[Comfy](https://docs.comfy.org/es/interface/settings/comfy)[Apariencia](https://docs.comfy.org/es/interface/appearance)
