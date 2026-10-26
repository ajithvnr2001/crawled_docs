---
url: https://docs.comfy.org/es/basic-concepts/nodes/
title: Nodos de ComfyUI: tipos, entradas y salidas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:29.690822+00:00
---

# Nodos de ComfyUI: tipos, entradas y salidas - ComfyUI

> Source: https://docs.comfy.org/es/basic-concepts/nodes/

## En esta página

Volver arriba

  * Los nodos realizan operaciones
  * Diferentes estados de los nodos
  * Conexiones entre nodos
    * Conectar y desconectar nodos
  * Apariencia del nodo
    * Insignias del nodo
  * Menús contextuales de nodos
    * Menú contextual del nodo
    * Modo
    * Menú contextual de entradas y salidas
  * Caja de herramientas de selección de nodos
  * Subgrafos
  * Nodos personalizados
    * ComfyUI Manager



Conceptos básicos

# Nodos de ComfyUI: tipos, entradas y salidas

Copiar páginaCopiar página

Los nodos son los bloques básicos de ComfyUI: módulos de Comfy Core o personalizados que conectas con enlaces para armar flujos de trabajo.

Copiar páginaCopiar página

En ComfyUI, los nodos son los bloques de construcción fundamentales para ejecutar tareas. Cada nodo es un módulo construido de forma independiente, ya sea un nodo **Comfy Core** o un **nodo personalizado** , con su propia funcionalidad única. Los nodos se enlazan entre sí mediante conexiones, lo que nos permite construir funcionalidades complejas como si ensamblaras bloques LEGO. Las combinaciones de diferentes nodos crean las posibilidades ilimitadas de ComfyUI. ![Nodo K-Sampler de Comfy Core](https://mintcdn.com/dripart/7m9lukFrTCZs7Mhj/images/comfy_core/sampling/k_sampler.png?fit=max&auto=format&n=7m9lukFrTCZs7Mhj&q=85&s=5bb2412a6e137d0a0b630b14845944e1) Por ejemplo, en el nodo K-Sampler, puedes ver que tiene múltiples entradas y salidas, y también incluye múltiples configuraciones de parámetros. Estos parámetros determinan la lógica de ejecución del nodo. Detrás de cada nodo hay una lógica de Python bien escrita, que te permite lograr la funcionalidad correspondiente sin tener que escribir código tú mismo.

ComfyUI está en desarrollo activo, por lo que algunos detalles aquí pueden estar desactualizados. Si detectas algo que ha cambiado, no dudes en [ayudarnos a actualizar la documentación](https://github.com/Comfy-Org/docs).

## 

​

Los nodos realizan operaciones

En ciencias de la computación, un _**nodo**_ es un contenedor de información, que normalmente incluye instrucciones programadas para realizar alguna tarea. Los nodos casi nunca existen de forma aislada, casi siempre están conectados a otros nodos en un gráfico de red. En ComfyUI, los nodos toman la forma visual de cajas que se conectan entre sí. Los nodos de ComfyUI suelen ser _**operadores de función**_. Esto significa que operan sobre ciertos datos para realizar una función. Una función es un proceso que acepta datos de entrada, realiza alguna operación sobre ellos y produce datos de salida. En otras palabras, los nodos hacen un trabajo y contribuyen a completar una tarea, como generar una imagen. Por eso los nodos de ComfyUI casi siempre tienen al menos una entrada o una salida, y normalmente tienen múltiples entradas y salidas.

## 

​

Diferentes estados de los nodos

![Estados de los nodos](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/status.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=150ab91575a7c9300b7ed20d8026e499) En ComfyUI, los nodos tienen múltiples estados. Estos son algunos de los estados más comunes:

  1. **Estado normal** : el estado predeterminado
  2. **Estado en ejecución** : el estado de ejecución, que normalmente se muestra cuando un nodo se está ejecutando después de que inicias la ejecución del flujo de trabajo
  3. **Estado de error** : error del nodo, que normalmente se muestra después de ejecutar el flujo de trabajo si hay un problema con la entrada del nodo, indicado por el marcado en rojo del nodo de entrada erróneo. Debes corregir la entrada problemática para asegurarte de que el flujo de trabajo se ejecute correctamente
  4. **Estado faltante** : este estado suele aparecer después de importar flujos de trabajo, con dos posibilidades: 
     * Falta un nodo nativo de Comfy Core: esto suele ocurrir porque ComfyUI se ha actualizado y estás usando una versión anterior de ComfyUI. Debes actualizar ComfyUI para resolver este problema
     * Falta un nodo personalizado: el flujo de trabajo usa nodos personalizados desarrollados por autores de terceros, pero tu versión local de ComfyUI no tiene estos nodos personalizados instalados. Puedes usar [ComfyUI Manager](https://docs.comfy.org/es/manager/overview) para encontrarlos e instalarlos, o seguir [Cómo instalar nodos personalizados](https://docs.comfy.org/es/installation/install_custom_node) para conocer otros métodos



## 

​

Conexiones entre nodos

En ComfyUI, los nodos se conectan mediante [enlaces](https://docs.comfy.org/es/basic-concepts/links), lo que permite que datos del mismo tipo fluyan entre distintas unidades de procesamiento para lograr el resultado final. ![Enlaces de nodos de ComfyUI](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/inpaint.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=40a62b27aa2f44cb97eae917c8c1f8da) Cada nodo recibe una entrada, la procesa a través de su módulo y la convierte en la salida correspondiente. Las conexiones entre distintos nodos deben cumplir con los requisitos del tipo de datos. En ComfyUI, usamos diferentes colores para distinguir los tipos de datos de los nodos. A continuación se muestran algunos tipos de datos básicos: ![Tipos de datos de nodos de ComfyUI](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

Tipo de datos| Color  
---|---  
modelo de difusión| lavanda  
modelo CLIP| amarillo  
modelo VAE| rosado  
acondicionamiento| naranja  
imagen latente| rosa  
imagen de píxeles| azul  
máscara| verde  
número (entero o flotante)| gris  
malla| verde brillante  
  
A medida que ComfyUI evoluciona, es posible que ampliemos a más tipos de datos para satisfacer las necesidades de más escenarios.

### 

​

Conectar y desconectar nodos

![Conexión de nodos de ComfyUI](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/link_nodes.gif?s=06359a20664f48e43763696313a063f9) **Conectar** : Arrastra desde el punto de salida de un nodo hasta la entrada del mismo color en otro nodo para conectarlos **Desconectar** : Haz clic en el punto de entrada y arrastra con el botón izquierdo del ratón para desconectar, o cancela la conexión mediante el menú del punto medio del enlace

## 

​

Apariencia del nodo

![Apariencia del nodo](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/index/node.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=e7ed881cf2c91cc9c48892dd491cae7b) Te ofrecemos varias configuraciones de estilo para que personalices la apariencia de los nodos:

  * Modificar estilos
  * Haz doble clic en el título del nodo para modificar el nombre del nodo
  * Redimensiona el nodo arrastrando cualquiera de sus esquinas



### 

​

Insignias del nodo

![Insignias del nodo](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=1e22b62c50745c547e2b99c5f13df990) Ofrecemos varias funciones de visualización de insignias en los nodos, como:

  * ID del nodo
  * Fuente del nodo

Actualmente, los **nodos de Comfy Core** se muestran con un icono de zorro, mientras que los nodos personalizados usan sus nombres. De esta forma puedes entender rápidamente de qué paquete de nodos proviene un nodo. Puedes configurar la visualización correspondiente en el menú: ![Configuración de insignias](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/badge_setting.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f63c9698836a1debc6a1bed84d77fdf2)

## 

​

Menús contextuales de nodos

Los menús contextuales de nodos se dividen principalmente en dos tipos:

  * El menú contextual del propio nodo
  * El menú contextual de las entradas y salidas



### 

​

Menú contextual del nodo

Al hacer clic derecho sobre un nodo, puedes expandir el menú contextual correspondiente: ![Menú contextual del nodo](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_1.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=d7d99664537a4f2b09aaf0acc228da4f) En el menú contextual del botón derecho del nodo, puedes:

  * Ajustar el estilo de color del nodo
  * Modificar el título
  * Clonar, copiar o eliminar el nodo
  * Establecer el modo del nodo

En este menú, además de la configuración relacionada con la apariencia, las siguientes operaciones del menú son importantes:

  * **Modo** : Establece el modo del nodo: Siempre, Nunca, Omitir



#### 

​

Modo

En cuanto a los modos, es posible que notes que actualmente ofrecemos cuatro: Siempre, Nunca, En evento y En disparador, pero en realidad solo **Siempre** y **Nunca** son efectivos. **En evento** y **En disparador** no son efectivos por ahora, ya que aún no hemos implementado esta función por completo. Además, puedes entender **Omitir** como un modo. A continuación se explica los modos disponibles:

  * **Siempre** : El modo predeterminado del nodo. El nodo se ejecutará cada vez que se ejecute por primera vez o cuando cualquiera de sus entradas cambie desde la última ejecución
  * **Nunca** : El nodo nunca se ejecutará bajo ninguna circunstancia, como si se hubiera eliminado. Los nodos posteriores no pueden leer ni recibir ningún dato de él
  * **Omitir** : El nodo nunca se ejecutará bajo ninguna circunstancia, pero los nodos posteriores aún pueden intentar obtener datos que no han sido procesados por este nodo

A continuación se muestra una comparación entre los modos Nunca y Omitir: ![Comparación entre los modos Nunca y Omitir](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/node/never_vs_bypass.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=9adb00fa408eb3f09805030cd7a731c2) En este ejemplo de comparación, puedes ver que ambos flujos de trabajo aplican dos modelos LoRA de forma simultánea, con la diferencia de que un nodo `Load LoRA` está configurado en modo `Never` mientras que el otro está configurado en modo `Bypass`.

  * El nodo configurado en modo `Never` hace que los nodos posteriores muestren errores, porque no reciben ningún dato de entrada
  * El nodo configurado en modo `Bypass` todavía permite que los nodos posteriores reciban datos sin procesar, por lo que cargan los datos de salida del primer nodo `Load LoRA`, lo que permite que el flujo de trabajo posterior continúe ejecutándose con normalidad



### 

​

Menú contextual de entradas y salidas

Este menú contextual está relacionado principalmente con el tipo de dato de la entrada o salida correspondiente: ![Menú contextual de entrada y salida del nodo](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/context_menus_2.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=2daf16654cdd151a6b9ace6ef9d9e530) Cuando arrastras la entrada o la salida de un nodo, si aparece una conexión pero no te has conectado a la entrada o salida de otro nodo, al soltar el mouse aparecerá un menú contextual para esa entrada o salida, que sirve para agregar rápidamente nodos del tipo relacionado. Puedes ajustar la cantidad de sugerencias de nodos en las configuraciones: ![Cantidad de sugerencias de nodos](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/node_suggestions.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=7a063583df5825a8cc24dc13a1723761)

## 

​

Caja de herramientas de selección de nodos

La **Caja de herramientas de selección de nodos** es una herramienta flotante que proporciona operaciones rápidas para los nodos. Cuando seleccionas un nodo, esta aparece flotando sobre el nodo seleccionado. A través de esta caja de herramientas, puedes:

  * Cambiar el color del nodo
  * Establecer rápidamente el nodo en modo Omitir (no se ejecuta durante el runtime)
  * Bloquear el nodo
  * Eliminar el nodo

Por supuesto, estas funciones también se encuentran en el menú de clic derecho del nodo correspondiente. La caja de herramientas de selección de nodos solo proporciona una operación rápida. Si quieres desactivar esta función, puedes hacerlo en las configuraciones. ![Desactivar la caja de herramientas de selección de nodos](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/setting_selection_toolbox.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=60747b0e83640a2f7a4f1bc66e63a89c)

## 

​

Subgrafos

Puedes contraer una selección de nodos en un único nodo de subgrafo reutilizable para ordenar gráficos complejos y reutilizar la misma estructura en distintos flujos de trabajo.

## Subgrafo

Aprende a crear, editar, anidar y publicar planos de subgrafos en la biblioteca de nodos.

## 

​

Nodos personalizados

ComfyUI incluye muchos nodos de **Comfy Core** en la instalación base. La comunidad también mantiene un amplio catálogo de [**nodos personalizados**](https://registry.comfy.org) para flujos de trabajo especializados. Para ver un resumen completo de cómo instalar nodos personalizados (ComfyUI Manager, clonación con Git, descarga de ZIP, dependencias y consejos de seguridad), consulta [Cómo instalar nodos personalizados](https://docs.comfy.org/es/installation/install_custom_node).

### 

​

ComfyUI Manager

Usa **ComfyUI Manager** para el trabajo diario con nodos personalizados: busca e instala desde el registro, actualiza o desactiva paquetes, detecta nodos faltantes en flujos de trabajo importados y administra modelos y snapshots junto con las extensiones. Las compilaciones de escritorio lo incluyen habilitado; las instalaciones portátiles y manuales pueden necesitar activarlo primero.

## ComfyUI Manager

Descripción general, cómo habilitar el Manager y flujos de trabajo de instalación de nodos

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/basic-concepts/nodes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/basic-concepts/nodes)

[Flujos de trabajo](https://docs.comfy.org/es/basic-concepts/workflow)[Nodos personalizados](https://docs.comfy.org/es/basic-concepts/custom-nodes)
