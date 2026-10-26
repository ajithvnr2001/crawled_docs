---
url: https://docs.comfy.org/es/interface/features/subgraph/
title: Subgrafo - Simplifica tu flujo de trabajo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.865372+00:00
---

# Subgrafo - Simplifica tu flujo de trabajo - ComfyUI

> Source: https://docs.comfy.org/es/interface/features/subgraph/

## En esta página

Volver arriba

  * Crear un subgrafo
  * Trabajar con subgrafos
    * Operaciones básicas
    * Editar subgrafos
    * Panel de parámetros
    * Subgrafos anidados
    * Salir del subgrafo
  * Desempaquetar subgrafos en nodos
  * Plano de subgrafo
    * Publicar subgrafo en la biblioteca de nodos
    * Editar plano de subgrafo



Componentes de funciones

# Subgrafo - Simplifica tu flujo de trabajo

Copiar páginaCopiar página

Una introducción a la función Subgrafo en ComfyUI, incluyendo cómo crear, navegar y administrar subgrafos.

Copiar páginaCopiar página

La función de subgrafo requiere la versión 1.24.3 o posterior del frontend de ComfyUI. Si no ves esta función, consulta: [Cómo actualizar ComfyUI](https://docs.comfy.org/es/installation/update_comfyui)

  * Las imágenes de este documento se crearon con la versión nocturna del frontend; consulta la interfaz real.



Para obtener documentación para desarrolladores sobre cómo trabajar con subgrafos mediante programación, consulta la [Guía para desarrolladores de subgrafos](https://docs.comfy.org/es/custom-nodes/js/subgraphs).

Un subgrafo es una potente función de ComfyUI que te permite empaquetar flujos de trabajo complejos en un único nodo de subgrafo reutilizable, lo que facilita su administración y uso compartido. ![Subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=83b3c5bf6e698d015bc63c608f88376e) Piensa en un subgrafo como una “carpeta” para tu flujo de trabajo: puedes agrupar nodos relacionados y usar toda la colección como un único nodo de subgrafo unificado. **Usa los subgrafos para:**

  * Simplificar flujos de trabajo complejos
  * Reutilizar combinaciones de nodos comunes
  * Crear flujos de trabajo más eficientes con componentes modulares



## 

​

Crear un subgrafo

1

Selecciona los nodos

Selecciona los nodos que quieres agrupar en ComfyUI

2

Haz clic en el icono de subgrafo

![Icono de subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_icon.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=3b0cf3b8160ef5408ef02a339685f460)Encuentra el icono de subgrafo en la barra de herramientas

3

Subgrafo creado

![Flujo de trabajo usando un subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/workflow_using_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=ceab1312d0e599aa036d91e9adbb7335)ComfyUI crea automáticamente un subgrafo a partir de las entradas y salidas de los nodos seleccionados

4

Personaliza tu subgrafo

Consulta Editar subgrafos; puedes editar y organizar el subgrafo para crear un nodo totalmente funcional![Flujo de trabajo usando un subgrafo](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=091d4223d6fb2cd2d44009cfee191bab)

## 

​

Trabajar con subgrafos

### 

​

Operaciones básicas

Los subgrafos funcionan igual que los nodos normales. Puedes:

  * Cambiar colores y nombres
  * Usar Omitir para deshabilitar
  * Aplicar todas las operaciones estándar de nodos



### 

​

Editar subgrafos

**Para entrar en modo de edición:**

  * Haz doble clic en el área vacía dentro del subgrafo (no sobre los widgets), o
  * Haz clic en el botón de edición del subgrafo

![Modo de edición de subgrafos](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=da969844db24259fc6af4e58abe047df) **En el modo de edición verás:**

  1. **Barra de navegación** : Sal del subgrafo actual y vuelve al nivel superior
  2. **Ranuras de entrada** : Entradas de nodos internos expuestas al exterior 
     * Conecta las salidas a las ranuras como lo harías con nodos normales
     * **Haz clic derecho** en los puntos de conexión para renombrar o eliminar las ranuras expuestas
  3. **Ranuras de salida** : Salidas expuestas al exterior (misma funcionalidad que las ranuras de entrada)

![Ranuras del subgrafo](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5f4cdd87ea46007d9bf35921576f12cb) **Trabajar con ranuras:**

  1. **Ranura predeterminada** (etiquetada como 1): Úsala para agregar nuevas conexiones de entrada/salida
  2. **Haz clic derecho** en las ranuras existentes para renombrar, eliminar o desconectar de los nodos originales



> Nota: Las conexiones de las ranuras siguen las reglas estándar de validación de tipos de datos

### 

​

Panel de parámetros

Con ComfyUI v0.3.66 o posterior, puedes editar los parámetros del subgrafo directamente desde el panel de parámetros sin entrar al subgrafo. Puedes seleccionar cualquier subgrafo y usar el botón “Editar Widgets de Subgrafo” para abrir el panel de parámetros. ![Abrir panel de parámetros](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/parameters_panel_open.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=30157b83417245ba715cb58e8b68717a) Después de abrirlo, puedes editar el orden y la visibilidad de los widgets del subgrafo directamente en el panel de parámetros. ![Abrir panel de parámetros](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/parameters_panel_edit.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=710bcf6bced65bab02112c3ac699c086)

  1. Reordenar: usa clic derecho y mantén presionado el widget para arrastrarlo a la posición deseada
  2. Visibilidad: puedes alternar la visibilidad del widget haciendo clic en el icono del ojo



### 

​

Subgrafos anidados

Crea flujos de trabajo aún más complejos anidando subgrafos dentro de subgrafos. ![Subgrafo anidado](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7e92ac585c91b067ab2527da1b5c521c) La barra de navegación muestra tu nivel actual y te permite moverte fácilmente entre subgrafos anidados. ![Navegación de subgrafos anidados](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_navigation.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=bad6ce874c9e68e4f537f657fd44d564)

### 

​

Salir del subgrafo

Para salir de un subgrafo y volver al nivel superior:

  * Usa la **Barra de navegación** (etiquetada como 1 en la imagen) en la parte superior del lienzo, o
  * Presiona la tecla **Esc**

![Modo de edición de subgrafos](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=da969844db24259fc6af4e58abe047df) Haz clic en la barra de navegación o presiona Esc para salir del subgrafo actual y volver al flujo de trabajo principal.

## 

​

Desempaquetar subgrafos en nodos

Cuando termines de crear un subgrafo, puedes volver a convertirlo en nodos si lo necesitas. ![De subgrafo a nodo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_to_nodes.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=fa9b87c2b097d3131d065829b0c09864)

  1. Puedes seleccionar el nodo de subgrafo y luego usar el menú de clic derecho «Desempaquetar subgrafo» para volver a convertirlo en nodos.
  2. Haz clic en el botón «Desempaquetar subgrafo» del cuadro de herramientas de selección para volver a convertirlo en nodos.



## 

​

Plano de subgrafo

Con la versión 1.27.7 o posterior del frontend de ComfyUI, puedes publicar tu subgrafo en la biblioteca de nodos. Esta función te permite convertir un subgrafo en un nodo `Subgraph Blueprints`, lo que significa que es un nodo de subgrafo reutilizable.

### 

​

Publicar subgrafo en la biblioteca de nodos

![Publicar subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_publishing.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=8a94ff214584859eb09e7149fa313f4a) Actualmente, tienes dos formas de publicar un subgrafo en la biblioteca de nodos, ambas en la caja de herramientas de selección:

  1. Haz clic en el icono `book(publish)` de la caja de herramientas de selección
  2. Abre el menú de la caja de herramientas de selección y usa el menú `Add Subgraph to Library` para publicar el subgrafo

Después de hacer clic en el icono `book(publish)` o en el menú `Add Subgraph to Library`, verás el siguiente diálogo: ![Nombrado del subgrafo](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/features/subgraph/subgraph_naming.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=0578432c55fd791c59c483e768fe02f3) De forma predeterminada, el subgrafo usará el nombre del nodo de subgrafo como nombre del plano de subgrafo. Después de publicarlo, verás el nodo de plano de subgrafo en la biblioteca de nodos. ![Nodo de plano de subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_blueprints.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=e5c08a91ace167af1d100833c04f5768) Ahora puedes arrastrar o buscar el subgrafo igual que un nodo normal. El nuevo nodo de subgrafo que se ha agregado desde Planos de subgrafos sigue siendo aislado, lo que significa que, después de agregarlo al flujo de trabajo, se puede editar de forma independiente, sin que se afecten entre sí.

### 

​

Editar plano de subgrafo

Si quieres editar el plano de subgrafo, puedes hacer clic en el botón de edición como en la imagen a continuación; también puedes eliminarlo. ![Editar plano de subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=e89a0e1bbf452688543d960bbef02288) Esto habilitará el modo de edición de subgrafo ![Modo de edición de subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_editing_mode.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=5d7ef14271c50660175ea05d33392458) Después de editar el plano de subgrafo, puedes ir al nivel principal para previsualizar el subgrafo. ![Actualizar plano de subgrafo](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/save_updated_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=5b7d2d527099a7b065acd7e16cde9a7f) Si quieres guardar el plano de subgrafo actualizado, puedes hacer clic en el botón de guardar o usar el atajo de teclado Ctrl + S.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/features/subgraph.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/features/subgraph)

[Modo aplicación](https://docs.comfy.org/es/interface/app-mode)[Ejecución parcial](https://docs.comfy.org/es/interface/features/partial-execution)
