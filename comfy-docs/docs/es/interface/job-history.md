---
url: https://docs.comfy.org/es/interface/job-history/
title: Historial de trabajos - Cola y ejecuciones anteriores - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:29.385566+00:00
---

# Historial de trabajos - Cola y ejecuciones anteriores - ComfyUI

> Source: https://docs.comfy.org/es/interface/job-history/

## En esta página

Volver arriba

  * Activar el Historial de trabajos
  * Abrir el panel
  * Pestañas: Todas, Completadas, Fallidas
  * Buscar, filtrar y ordenar
  * Lista de tareas y acciones
  * Cómo se relaciona con Recursos y Errores
  * Páginas relacionadas



Barra lateral izquierda

# Historial de trabajos - Cola y ejecuciones anteriores

Copiar páginaCopiar página

Con Comfy.Queue.QPOV2 activado, la barra lateral Historial de trabajos muestra tareas activas y pasadas con insignias, filtros y acciones.

Copiar páginaCopiar página

**Historial de trabajos** es una pestaña de la barra lateral izquierda que aparece cuando está activada la opción **Panel acoplado de historial/cola de trabajos** (`Comfy.Queue.QPOV2`). El frontend la registra en la parte **superior** de la barra lateral (`prepend`) para que puedas ver los trabajos activos y explorar ejecuciones anteriores sin usar la superposición flotante de la cola. Cuando la opción está desactivada, la pestaña se elimina y, en su lugar, queda disponible la superposición flotante del historial de trabajos (`Comfy.Queue.ToggleOverlay`). Los controles de ejecución y cola del encabezado superior siguen iniciando trabajos en ambos casos. Esta página trata sobre la superficie del Historial de trabajos en la **barra lateral**. ![El panel Historial de trabajos mientras una ejecución está activa: la línea de estado, el grupo Running, los trabajos completados y las pestañas Todas y Completadas](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/job-history/job_history_panel.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=12b96c86e3780d05edfc42ca322d6c2f) ![El icono de Historial de trabajos con la insignia del recuento de trabajos activos mientras la pestaña no está abierta](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/job-history/job_history_badge.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=ca7132f25c4737f70b064eb5b610c6c5)

## 

​

Activar el Historial de trabajos

  1. Abre **Configuraciones**.
  2. En `Comfy` → `Queue` → `Layout`, habilita **Panel acoplado de historial/cola de trabajos** (`Comfy.Queue.QPOV2`).
  3. El icono **Historial de trabajos** aparece en la parte superior de la barra lateral izquierda.

La configuración es experimental. En las compilaciones nocturnas está activada de forma predeterminada; en otras compilaciones, revisa la configuración si no ves la pestaña.

## 

​

Abrir el panel

Haz clic en el icono **Historial de trabajos**. Mientras hay tareas en ejecución o en cola y esta pestaña **no** está activa, el icono muestra una insignia numérica con la cantidad de tareas activas. Al abrir la pestaña, la insignia deja de mostrarse en esa vista.

## 

​

Pestañas: Todas, Completadas, Fallidas

El encabezado del panel tiene pestañas de estado:

  * **Todas** : todas las tareas del historial según los filtros actuales.
  * **Completadas** : ejecuciones finalizadas.
  * **Fallidas** : solo aparece cuando existe al menos una tarea fallida en la lista.

Debajo de las pestañas, una línea de resumen muestra cuántas tareas se están ejecutando y cuántas están en cola (o que no hay trabajos activos). El control **Limpiar cola** cancela todas las tareas pendientes (en cola, aún sin ejecutarse).

## 

​

Buscar, filtrar y ordenar

Usa las herramientas del encabezado para acotar la lista:

  * **Buscar** : filtra los trabajos por texto.
  * **Filtrar** : **Todos los flujos de trabajo** o **Flujo de trabajo actual**.
  * **Ordenar** : **Más reciente** o **Tiempo total de generación**.



## 

​

Lista de tareas y acciones

Las tareas se muestran con su estado, el progreso cuando están en ejecución y miniaturas de vista previa cuando existen salidas. Desde la fila de una tarea o su menú contextual puedes: **En ejecución o en cola**

  * Abrir como flujo de trabajo en una pestaña nueva
  * Copiar ID de trabajo
  * Cancelar trabajo

**Completadas**

  * Inspeccionar recurso (cuando existe una vista previa)
  * Agregar la salida al flujo de trabajo actual como nodo de carga
  * Descargar el recurso de vista previa
  * Abrir como flujo de trabajo en una pestaña nueva
  * Exportar flujo de trabajo
  * Copiar ID de trabajo

**Fallidas**

  * Abrir flujo de trabajo en una pestaña nueva
  * Copiar ID de trabajo
  * Copiar mensaje de error
  * Reportar error
  * Quitar trabajo de la lista del historial

El menú de acciones del encabezado incluye **Limpiar historial** , que abre un cuadro de diálogo de confirmación. Limpiar el historial elimina las entradas del historial de la cola; lee la nota del diálogo sobre cómo se relaciona eso con los recursos almacenados en tu instalación.

## 

​

Cómo se relaciona con Recursos y Errores

Las salidas de las ejecuciones completadas también aparecen en [Recursos](https://docs.comfy.org/es/interface/assets) cuando el sistema de recursos está habilitado. Los fallos del flujo de trabajo y los recursos faltantes se muestran en la pestaña **Errores** del [panel lateral derecho](https://docs.comfy.org/es/interface/right-side-panel) mientras corriges el gráfico.

## 

​

Páginas relacionadas

  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview)
  * [Recursos](https://docs.comfy.org/es/interface/assets)
  * [Panel lateral derecho](https://docs.comfy.org/es/interface/right-side-panel)
  * [Configuraciones de Comfy](https://docs.comfy.org/es/interface/settings/comfy)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/job-history.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/job-history)

[Aplicaciones](https://docs.comfy.org/es/interface/apps)[Panel derecho](https://docs.comfy.org/es/interface/right-side-panel)
